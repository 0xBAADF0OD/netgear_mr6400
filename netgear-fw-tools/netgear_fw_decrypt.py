import sys
import re
import os
import argparse
import binascii

from termcolor import colored
from Crypto.Cipher import AES

DEBUG_ON = False

magic = b'\x80\x40\x4C\x21\x51\x9B\xFD\xC5\xCD\xFF\x2E\xD3\x66\x0B\x8F\x6E'
aes_key = b'\x67\x45\x8B\x6B\xC6\x23\x7B\x32\x69\x98\x3C\x64\x73\x48\x33\x66\x51\xDC\xB0\x74\xFF\x5C\x49\x19\x4A\x94\xE8\x2A\xEC\x58\x55\x62'
aes = AES.new(aes_key, AES.MODE_ECB)
xor_key = b'\x3D\x52\x1F\x34\x5F\x50\x28\x84\x55\x1E\x67\x0F\xB2\x57\x77\x31\x53\xBA\xAD\xB0\x44\x82\x40\xEC\xA2\x71\xA1\xB4\x57\xCC\x08\x34\xA9\xBE\x8B\xA0\xCB\xBC\x94\xF0\xC1\x8A\xD3\x7B\x1E\xC3\xE3\x9D\xBF\xB7\xAA\xAD\x41\x7F\x3D\xE9\x9F\x6E\x9E\xB1\x54\xC9\x05\x31\xA6\xBB\x88\x9D\xC8\xB9\x91\xED\xBE\x87\xD0\x78\x1B\xC0\xE0\x9A\xBC\xC4\xB7\xBA\x4E\x8C\x4A\xF6\xAC\x7B\xAB\xBE\x61\xD6\x12\x3E\xB3\xC8\x95\xAA\xD5\xC6\x9E\xFA\xCB\x94\xDD\x85\x28\xCD\xED\xA7\xC9\xC9\xBC\xBF\x53\x91\x4F\xFB\xB1\x80\xB0\xC3\x66\xDB\x17\x43\xB8\xCD\x9A\xAF\xDA\xCB\xA3\xFF\xD0\x99\xE2\x8A\x2D\xD2\xF2\xAC\xCE\xA7\x9A\x9D\x31\x6F\x2D\xD9\x8F\x5E\x8E\xA1\x44\xB9\xF5\x21\x96\xAB\x78\x8D\xB8\xA9\x81\xDD\xAE\x77\xC0\x68\x0B\xB0\xD0\x8A\xAC\xED\xE0\xE3\x77\xB5\x73\x1F\xD5\xA4\xD4\xE7\x8A\xFF\x3B\x67\xDC\xF1\xBE\xD3\xFE\xEF\xC7\x23\xF4\xBD\x06\xAE\x51\xF6\x16\xD0\xF2\xCD\xC0\xC3\x57\x95\x53\xFF\xB5\x84\xB4\xC7\x6A\xDF\x1B\x47\xBC\xD1\x9E\xB3\xDE\xCF\xA7\x03\xD4\x9D\xE6\x8E\x31\xD6\xF6\xB0\xD2\x28\x1B\x1E\xB2\xF0\xAE\x5A\x10\xDF\x0F\x22\xC5\x3A\x76\xA2\x17\x2C\xF9\x0E\x39\x2A\x02\x5E\x2F\xF8\x41\xE9\x8C\x31\x51\x0B\x2D\x85\x78\x7B\x0F\x4D\x0B\xB7\x6D\x3C\x6C\x7F\x22\x97\xD3\xFF\x74\x89\x56\x6B\x96\x87\x5F\xBB\x8C\x55\x9E\x46\xE9\x8E\xAE\x68\x8A\xDD\xD0\xD3\x67\xA5\x63\x0F\xC5\x94\xC4\xD7\x7A\xEF\x2B\x57\xCC\xE1\xAE\xC3\xEE\xDF\xB7\x13\xE4\xAD\xF6\x9E\x41\xE6\x06\xC0\xE2\x94\x87\x8A\x1E\x5C\x1A\xC6\x7C\x4B\x7B\x8E\x31\xA6\xE2\x0E\x83\x98\x65\x7A\xA5\x96\x6E\xCA\x9B\x64\xAD\x55\xF8\x9D\xBD\x77\x99\xCB\xBE\xC1\x55\x93\x51\xFD\xB3\x82\xB2\xC5\x68\xDD\x19\x45\xBA\xCF\x9C\xB1\xDC\xCD\xA5\x01\xD2\x9B\xE4\x8C\x2F\xD4\xF4\xAE\xD0\xFA\xED\xF0\x84\xC2\x80\x2C\xE2\xB1\xE1\xF4\x97\x0C\x48\x74\xE9\xFE\xCB\xE0\x0B\xFC\xD4\x30\x01\xCA\x13\xBB\x5E\x03\x23\xDD\xFF\x9E\x91\x94\x28\x66\x24\xD0\x86\x55\x85\x98\x3B\xB0\xEC\x18\x8D\xA2\x6F\x84\xAF\xA0\x78\xD4\xA5\x6E\xB7\x5F\x02\xA7\xC7\x81\xA3\xC6\xB9\xBC\x50\x8E\x4C\xF8\xAE\x7D\xAD\xC0\x63\xD8\x14\x40\xB5\xCA\x97\xAC\xD7\xC8\xA0\xFC\xCD\x96\xDF\x87\x2A\xCF\xEF\xA9\xCB\xD5\xC8\xCB\x5F\x9D\x5B\x07\xBD\x8C\xBC\xCF\x72\xE7\x23\x4F\xC4\xD9\xA6\xBB\xE6\xD7\xAF\x0B\xDC\xA5\xEE\x96\x39\xDE\xFE\xB8\xDA\xAA\x9D\xA0\x34\x72\x30\xDC\x92\x61\x91\xA4\x47\xBC\xF8\x24\x99\xAE\x7B\x90\xBB\xAC\x84\xE0\xB1\x7A\xC3\x6B\x0E\xB3\xD3\x8D\xAF\x95\x88\x8B\x1F\x5D\x1B\xC7\x7D\x4C\x7C\x8F\x32\xA7\xE3\x0F\x84\x99\x66\x7B\xA6\x97\x6F\xCB\x9C\x65\xAE\x56\xF9\x9E\xBE\x78\x9A\xC8\xBB\xBE\x52\x90\x4E\xFA\xB0\x7F\xAF\xC2\x65\xDA\x16\x42\xB7\xCC\x99\xAE\xD9\xCA\xA2\xFE\xCF\x98\xE1\x89\x2C\xD1\xF1\xAB\xCD\xB3\xA6\xA9\x3D\x7B\x39\xE5\x9B\x6A\x9A\xAD\x50\xC5\x01\x2D\xA2\xB7\x84\x99\xC4\xB5\x8D\xE9\xBA\x83\xCC\x74\x17\xBC\xDC\x96\xB8\x3E\x31\x34\xC8\x06\xC4\x70\x26\xF5\x25\x38\xDB\x50\x8C\xB8\x2D\x42\x0F\x24\x4F\x40\x18\x74\x45\x0E\x57\xFF\xA2\x47\x67\x21\x43\x12\x05\x08\x9C\xDA\x98\x44\xFA\xC9\xF9\x0C\xAF\x24\x60\x8C\x01\x16\xE3\xF8\x23\x14\xEC\x48\x19\xE2\x2B\xD3\x76\x1B\x3B\xF5\x17\xD6\xC9\xCC\x60\x9E\x5C\x08\xBE\x8D\xBD\xD0\x73\xE8\x24\x50\xC5\xDA\xA7\xBC\xE7\xD8\xB0\x0C\xDD\xA6\xEF\x97\x3A\xDF\xFF\xB9\xDB\x61\x54\x57\xEB\x29\xE7\x93\x49\x18\x48\x5B\xFE\x73\xAF\xDB\x50\x65\x32\x47\x72\x63\x3B\x97\x68\x31\x7A\x22\xC5\x6A\x8A\x44\x66\xBE\xB1\xB4\x48\x86\x44\xF0\xA6\x75\xA5\xB8\x5B\xD0\x0C\x38\xAD\xC2\x8F\xA4\xCF\xC0\x98\xF4\xC5\x8E\xD7\x7F\x22\xC7\xE7\xA1\xC3\xAB\x9E\xA1\x35\x73\x31\xDD\x93\x62\x92\xA5\x48\xBD\xF9\x25\x9A\xAF\x7C\x91\xBC\xAD\x85\xE1\xB2\x7B\xC4\x6C\x0F\xB4\xD4\x8E\xB0\x7B\x6E\x71\x05\x43\x01\xAD\x63\x32\x62\x75\x18\x8D\xC9\xF5\x6A\x7F\x4C\x61\x8C\x7D\x55\xB1\x82\x4B\x94\x3C\xDF\x84\xA4\x5E\x80\xAC\x9F\xA2\x36\x74\x32\xDE\x94\x63\x93\xA6\x49\xBE\xFA\x26\x9B\xB0\x7D\x92\xBD\xAE\x86\xE2\xB3\x7C\xC5\x6D\x10\xB5\xD5\x8F\xB1\xF6\xE9\xEC\x80\xBE\x7C\x28\xDE\xAD\xDD\xF0\x93\x08\x44\x70\xE5\xFA\xC7\xDC\x07\xF8\xD0\x2C\xFD\xC6\x0F\xB7\x5A\xFF\x1F\xD9\xFB\x4A\x3D\x40\xD4\x12\xD0\x7C\x32\x01\x31\x44\xE7\x5C\x98\xC4\x39\x4E\x1B\x30\x5B\x4C\x24\x80\x51\x1A\x63\x0B\xAE\x53\x73\x2D\x4F\x8C\x7F\x82\x16\x54\x12\xBE\x74\x43\x73\x86\x29\x9E\xDA\x06\x7B\x90\x5D\x72\x9D\x8E\x66\xC2\x93\x5C\xA5\x4D\xF0\x95\xB5\x6F\x91\x4E\x41\x44\xD8\x16\xD4\x80\x36\x05\x35\x48\xEB\x60\x9C\xC8'
fwhead_len = 0x190
sechead_len = 0x90
output_dir = ""
full_file = b''
file_count = 0

def log(string, debug=False):
    if debug:
        if DEBUG_ON:
            print("{}{}".format(colored("[DBG] ", "white", attrs=["bold"]), string))
    else:
        print("{}{}".format(colored("[LOG] ", "green", attrs=["bold"]), string))

def xor_shift_key(count):
    return xor_key[-count:]+xor_key[:-count]

def xor_decrypt_data(data, key):
    #byte-wise XOR, processing key-length bytes of data at a time.
    out = bytearray()
    section_count = 0
    key_length = len(key)
    while True:
        data_section = data[section_count*key_length:(section_count+1)*key_length]
        for i in range(len(data_section)):
            k=key[i % len(key)]
            d=data_section[i]
            out.append(k^d)
        if section_count % 1000 == 0:
            log("{} bytes processed".format(key_length*section_count), True)
        if len(data_section) < key_length:
            return out
        section_count+=1
            
def extract_chunks(chunks, prev_chunk_name = "", depth=0):
    global output_dir, file_count, full_file
    chunk_count = 0
    for chunk in chunks:
        #AES decrypt the chunk header
        if chunk_count > 0 or depth > 0:
            chunk_header = aes.decrypt(chunk[:sechead_len])
            chunk_body_enc = chunk[sechead_len:]
            chunk_name = chunk_header[0xc:0x10].decode()
        else:
            chunk_header = aes.decrypt(chunk[:fwhead_len])
            chunk_name = "BASE"
            chunk_body_enc = False
        with open(os.path.join(output_dir,"{:02d}_{}_{}_header.bin".format(file_count, prev_chunk_name, chunk_name)), "wb") as f:
            f.write(chunk_header)
        file_count += 1
        #XOR decrypt the chunk body
        if chunk_body_enc:
            if (depth == 0) or (magic in chunk_body_enc):
                #XOR Key is shifted by the chunk body length (chunk - header, without the magic)
                #But the XOR process is applied to the entire chunk. We'll discard the first secheader_len bytes
                xor_keyshift = (len(chunk_body_enc)) % 32
                xor_key_mod = xor_shift_key(xor_keyshift)
                log("{} body has length of {}, keyshift of {}".format(chunk_name, len(chunk_body_enc), xor_keyshift))
                chunk_body = xor_decrypt_data(chunk, xor_key_mod)
            else:
                log("{} body has length of {}, no need to XOR".format(chunk_name, len(chunk_body_enc)))
                chunk_body = chunk
            chunk_body = chunk_body[sechead_len:]
            with open(os.path.join(output_dir,"{:02d}_{}_{}_body.bin".format(file_count, prev_chunk_name, chunk_name)), "wb") as f:
                f.write(chunk_body)
            file_count += 1
            if (magic*16 in chunk_body):
                log("[!] entering a nest!, depth is {}".format(depth), True)
                nested_chunks = chunk_body.split(magic*16)[1:]
                extract_chunks(nested_chunks, chunk_name, depth+1)
                
        if depth == 0:
            if chunk_count > 0:
                full_file += b'\x00'*0x100
            full_file += chunk_header
            if chunk_body_enc:
                full_file += chunk_body
        chunk_count += 1

def main():
    global output_dir, full_file
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()

    firmware_file = args.filename
    with open(firmware_file, "rb") as fw:
        fwdata = fw.read()

    fpath = os.path.abspath(args.filename)
    dirname, fname = os.path.split(fpath)
    
    log("Using %s in %s"%(fname,dirname))
    output_dir = os.path.join(dirname,"%s-files"%(fname))
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    #BEGIN PROCESSING INPUT FILE
    chunks = fwdata.split(magic*16)
    extract_chunks(chunks)
    
    #Fix remaining issues with the full file
    full_file = full_file.replace(magic, b'\x00'*0x10)
    with open(os.path.join(output_dir,"_{}.dec".format(fname)), "wb") as f:
        f.write(full_file)    
        
main()