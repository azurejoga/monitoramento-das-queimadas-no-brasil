# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c93353e1-4028-3574-8c5f-2a4c048a1331 | -4.58494 | -46.62576 | 2024-11-14 00:41:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 02a7a779-7342-3753-b849-eb3c2ffc862d | -2.66436 | -46.99196 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 163.2 |
| de3c9cd7-47f1-3e7a-8f3d-dc3aaeef116d | -4.85347 | -46.9722 | 2024-11-14 00:41:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| db3ca4b7-391b-3efe-8bf3-ec761243d810 | -2.90386 | -45.59805 | 2024-11-14 00:41:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a888fe9a-c9c1-33ff-97d2-71e79e3ed96d | -4.04354 | -45.71377 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3362de04-5772-3b45-b69d-f9c2b0ad41eb | -3.13537 | -45.27616 | 2024-11-14 00:41:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 825a6362-83c1-3f59-9c51-4ebb30864476 | -1.85987 | -47.82938 | 2024-11-14 00:41:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 410b2335-3863-3ec9-84c4-9e87342fe45c | -2.19912 | -46.36251 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| d986cccf-edc0-304d-973e-0fa40501f4f2 | -3.15436 | -45.28251 | 2024-11-14 00:41:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4179e516-c6c8-3fdb-bdb8-187273ed36f2 | -6.04701 | -44.03305 | 2024-11-14 00:41:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 1775ea3b-667a-3516-ae17-3bf6de74f6db | -2.89475 | -46.8586 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f37af546-338a-3557-8bce-3c3ddad4f299 | -4.15602 | -46.25111 | 2024-11-14 00:41:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 0c4ac086-1f07-36cb-87aa-7a96bbafbd75 | -4.27389 | -46.90925 | 2024-11-14 00:41:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5aeb5878-4142-3d4a-a0c2-05efb4cfb9ef | -3.95199 | -46.7108 | 2024-11-14 00:41:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0fc4eaa9-ba2d-307e-a52f-324f33d53f02 | -3.16822 | -50.45211 | 2024-11-14 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 490fa08d-9d4d-31e1-8100-e425b233a166 | -3.14424 | -45.2749 | 2024-11-14 00:41:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 4c7e0b4c-17ed-3f20-b03e-e5c07ff9e07e | -2.66086 | -46.83582 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| db0ef4bc-1528-3b55-9d34-b9d5d01c7ad7 | -4.5317 | -45.91119 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 74c79ab4-56ef-3404-b6b1-546b13ac3522 | -4.2322 | -46.87418 | 2024-11-14 00:41:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e311cf23-7fde-3366-b805-b05fbcb49577 | -4.00622 | -45.57529 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 54ae2e7f-084f-3cf7-b0b7-3b3e11d01d34 | -1.34375 | -46.56491 | 2024-11-14 00:41:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 8b506f51-747e-3bcf-9db2-6e7331b9465a | -2.89601 | -46.86766 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| baa2fd63-aa15-33a4-8c7f-74f94f24fafb | -2.17801 | -48.54867 | 2024-11-14 00:41:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 73aed1f9-40eb-3395-99ef-5cd22d55cfda | -5.33185 | -45.10619 | 2024-11-14 00:41:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fac9840a-3a5c-3b48-8324-2154a359f6b5 | -3.28526 | -45.36653 | 2024-11-14 00:41:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 6bffb34c-70a5-3347-b210-fedb3b2ebf27 | -2.44815 | -47.02525 | 2024-11-14 00:41:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 56ee00a5-0246-32c4-8122-1a3af2c842dc | -3.37912 | -43.93641 | 2024-11-14 00:41:00 | TERRA_M-M | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 5f28fdfb-da6c-3928-9d92-37f52f6ffeca | -1.68558 | -45.45221 | 2024-11-14 00:41:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 61d246c1-d1d4-3b55-aca1-88ddb7b7d2a5 | -6.05811 | -44.04391 | 2024-11-14 00:41:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 61598e30-f955-36aa-b05a-745dabfb9400 | -2.66563 | -47.00104 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c1eb4c92-7634-3bc8-8b8c-d04904db3106 | -4.02995 | -44.68929 | 2024-11-14 00:41:00 | TERRA_M-M | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 8b32e70b-6a7e-3035-815f-e0a69e63baff | -4.79726 | -43.65967 | 2024-11-14 00:41:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a3f0c3a3-ca82-3ffa-87df-06051a5e5979 | -2.67334 | -46.99068 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 193.6 |
| 464a27ff-3242-39d8-b33f-078468abbc72 | -2.9806 | -51.24851 | 2024-11-14 00:41:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 4e2779f1-6251-37a5-9770-079aef5c4ed4 | -2.65066 | -46.82807 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 932efd03-7327-3caf-81f8-9f6aa3b793d2 | -5.36001 | -43.54552 | 2024-11-14 00:41:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 22ec9e72-92ea-38d9-a6b8-538ec97b0f95 | -4.59393 | -46.62455 | 2024-11-14 00:41:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c6fe3d09-0b15-3121-a32a-7416c78851ee | -3.16413 | -50.58617 | 2024-11-14 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 1c2993f1-99a7-30a7-959f-256575f7da0f | -1.6281 | -46.10273 | 2024-11-14 00:41:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 42384a53-7cb4-3921-ade7-046d28d8e8c5 | -5.0287 | -46.84027 | 2024-11-14 00:41:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 87659a79-0eb7-3dd9-b614-0fbecba70314 | -3.74223 | -50.45027 | 2024-11-14 00:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 8a01bcd1-e07d-30ed-a46d-77235a432a20 | -2.06756 | -46.54635 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3e210814-0589-38f2-b90d-0f743b764ece | -3.07497 | -44.2574 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c1642ce3-1034-3511-97fd-99200bb64fbd | -1.88175 | -47.05826 | 2024-11-14 00:41:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ef5dbdac-6241-36bf-aae0-42e5a094302a | -2.88704 | -46.86891 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5b2ad1a2-aad2-3597-bd08-092e959f0e3b | -6.26643 | -44.54312 | 2024-11-14 00:41:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c7b43cdd-322b-3fd9-a8e0-04ff4df8519b | -3.0234 | -45.66473 | 2024-11-14 00:41:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 304434cc-7786-3fde-bc96-1c5cc6e36189 | -5.20088 | -44.36806 | 2024-11-14 00:41:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 18a42901-6155-39cf-be1c-42db1fde9353 | -4.9184 | -44.52547 | 2024-11-14 00:41:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b62f5b10-663c-311f-8740-75fa4f81c694 | -4.79464 | -45.28251 | 2024-11-14 00:41:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 91ff093f-1aeb-3ddf-9a92-98cf68d93d2a | -3.04794 | -50.3302 | 2024-11-14 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| fa713e30-3bfd-39bf-a676-bf9fac68476d | -2.40677 | -45.33765 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c81ce0e4-da1d-322f-9623-81a103dc153e | -5.506 | -47.16976 | 2024-11-14 00:41:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2113494a-bf59-3957-a94f-dafa0207efda | -2.20991 | -53.70834 | 2024-11-14 00:41:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 086bb5af-9e85-36ce-ae27-fe8d82d535ea | -2.60677 | -46.176 | 2024-11-14 00:41:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6d6d2a22-a40b-37a9-bcfb-8551bbfe2f41 | -2.98613 | -45.86477 | 2024-11-14 00:41:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 20.5 |
| a6ae67e7-52fa-36d5-bc7a-05ad5cddc983 | -1.3703 | -47.09298 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dbd49a3d-10b0-3dcd-8592-177a1113d1ec | -2.02781 | -46.92169 | 2024-11-14 00:41:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| e53c8dc2-5650-3819-bef1-dcba018b7246 | -3.41114 | -50.29926 | 2024-11-14 00:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f2fb7b52-f4a0-36b1-819d-92249dd1f9f6 | -3.82223 | -51.9312 | 2024-11-14 00:41:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| fe5bacad-5f60-3958-8297-4accb6b4ed7b | -6.04831 | -44.0423 | 2024-11-14 00:41:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 90866c1d-cbc3-31e6-8266-a0f6552bfbe5 | -4.39649 | -47.26943 | 2024-11-14 00:41:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c402e0c2-973e-3047-a853-9abe8227b6d1 | -4.51897 | -46.48404 | 2024-11-14 00:41:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 19.2 |
| efcea21d-6aca-384c-abff-9cda539dce11 | -2.369 | -46.98718 | 2024-11-14 00:41:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5874d937-7aec-3885-a534-a2e75966f204 | -1.84611 | -46.07183 | 2024-11-14 00:41:00 | TERRA_M-M | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a36756f6-aaca-3301-a286-f4f0cdaf4336 | -2.88187 | -45.37586 | 2024-11-14 00:41:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d663b1a9-a88a-385e-8500-1503125bd45a | -3.48559 | -50.25389 | 2024-11-14 00:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 33e407cb-aec9-3edc-a920-66bc2bffa4ad | -2.37205 | -45.61983 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 58fbff48-bb69-34d5-b015-b0e414f6ebcb | -4.92764 | -45.44664 | 2024-11-14 00:41:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 19bbbf5b-5cbf-3bad-b16f-14536fca7655 | -6.96234 | -39.8311 | 2024-11-14 00:41:00 | TERRA_M-M | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 57.0 |
| 114130c8-e8e5-3e3c-aa5f-ea988f8c31af | -3.64584 | -52.27658 | 2024-11-14 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 01b95200-d86a-3cea-bf17-a4c0869094f2 | -4.78015 | -46.10247 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 1235f81a-9be8-3859-afe5-6e96f2277eea | -3.31399 | -44.05941 | 2024-11-14 00:41:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 85b36756-76be-3988-a587-566f5aafa9c8 | -5.93784 | -43.78366 | 2024-11-14 00:41:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| ccd48d97-b6b0-328c-917b-994c561e07fe | -5.12164 | -44.45972 | 2024-11-14 00:41:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bababe63-2eff-308f-850c-6a5041f0c32d | -3.24475 | -46.52851 | 2024-11-14 00:41:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6f04dc2d-0544-3f39-8a4a-aefe8b6d2051 | -3.82194 | -51.93773 | 2024-11-14 00:41:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| a5a4c8be-49e6-37b4-8e24-d823f3c2e190 | -3.33655 | -52.7971 | 2024-11-14 00:41:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 314cf6c5-ee18-3801-b8e5-350a8b302b3d | -2.64339 | -46.17983 | 2024-11-14 00:41:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 64.5 |
| c183c96c-f92c-3874-94aa-ca83d9ce5826 | -4.03061 | -46.54585 | 2024-11-14 00:41:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f9ca1bd7-9ac0-342f-9962-50df798254a8 | -4.92785 | -45.7076 | 2024-11-14 00:41:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 029a1f7d-f9fe-3d94-b022-6f2814c8751d | -3.95686 | -46.41591 | 2024-11-14 00:41:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ec3733e5-e31e-382e-8095-ad0391e26563 | -3.25151 | -50.39118 | 2024-11-14 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| bdc20d9c-29fd-37be-9760-8e7f2d487918 | -5.18935 | -44.3512 | 2024-11-14 00:41:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2d1ce9dc-8fef-375c-8db0-2476d557f365 | -2.65224 | -46.17859 | 2024-11-14 00:41:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 2354978c-e6e3-3113-b94c-f1767ef4f293 | -3.7713 | -41.60029 | 2024-11-14 00:41:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 09da1710-e8fe-3662-9fcc-e9bb27b26136 | -2.65101 | -46.16977 | 2024-11-14 00:41:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1a991419-6d57-3c0a-8e6d-43053ec1f395 | -2.52915 | -45.35976 | 2024-11-14 00:41:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7af44d5d-bfec-3dbc-8664-3775d7bdc7e7 | -3.96869 | -46.69924 | 2024-11-14 00:41:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5363babf-99ae-309e-a243-aa6309bb113e | -1.84733 | -46.08062 | 2024-11-14 00:41:00 | TERRA_M-M | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| cf3d4ea0-c3c8-3e1a-b8bf-9618631bc393 | -2.89074 | -45.3746 | 2024-11-14 00:41:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 79b25f0c-fe84-38a1-a4ec-6102aad5fea5 | -3.89467 | -46.09817 | 2024-11-14 00:41:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2270f502-7db0-39b3-b692-d309caa3a470 | -4.94414 | -44.96911 | 2024-11-14 00:41:00 | TERRA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cc345aec-3cb9-360d-9276-61549a8edcc5 | -3.16524 | -46.61862 | 2024-11-14 00:41:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4b842a6b-16d8-3b3c-b3e5-f26b08d5e0b4 | -2.93811 | -44.98855 | 2024-11-14 00:41:00 | TERRA_M-M | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| af9c7eee-480d-3677-b039-ae7bc9777f06 | -2.38384 | -46.49559 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4dd5a041-3370-389b-aacf-52be70c049c4 | -4.75377 | -49.09224 | 2024-11-14 00:41:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 864f0e02-3be7-3640-b3c3-09e19cd6004b | -3.28526 | -50.05461 | 2024-11-14 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 987e2dba-fa8b-3b2b-88be-996d31441ad0 | -4.47146 | -46.53681 | 2024-11-14 00:41:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 453e0511-2d94-3aa2-a139-bcb58d8cadfa | -3.89344 | -46.08931 | 2024-11-14 00:41:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 27.6 |


[Clique aqui para ver as próximas entradas](README11.md)
