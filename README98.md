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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75c4e2b4-db89-32f6-be2f-ad39e4b735d5 | -14.67108 | -48.14407 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 462665fa-5b16-361d-8eec-e9b984af0ac0 | -17.3907 | -47.15034 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f189752-f719-3f13-8d4e-6d5374eae580 | -14.59829 | -48.29199 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b9ecccf-d158-3164-a5f9-c8d9ec958c57 | -15.12879 | -48.38286 | 2025-09-30 05:10:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 359e1e9e-f71b-35e4-9c73-cfe49c448380 | -13.80907 | -47.89186 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d5cfc35-8354-3c5a-975a-af908b941ed5 | -16.20535 | -52.82423 | 2025-09-30 05:10:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18d52a63-8faf-3255-8d61-d79933a3138e | -13.7809 | -47.94148 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d0955b2a-34ce-337f-b55d-9408af2fdc6f | -17.40849 | -47.15512 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06985b64-9b9a-3b59-b9aa-4d634c36f8b8 | -15.71619 | -59.51097 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30abd208-321f-367f-93ba-283be331ae3d | -14.64526 | -46.97032 | 2025-09-30 05:10:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b376f4b-7a6b-3d32-8090-e3bc3da9118b | -14.67197 | -48.14516 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aea58d03-df2f-3eff-8487-ed03c04205f4 | -20.61386 | -46.07303 | 2025-09-30 05:10:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd798630-f51c-3a56-a7dc-64b6d4870ce9 | -15.07521 | -45.05607 | 2025-09-30 05:10:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 835e7f73-a7ae-3699-9ca9-e58ec684e6c3 | -16.00558 | -59.51421 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6324ff53-e739-375a-8c8e-138a09c0704b | -15.93033 | -59.50501 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a354acca-d465-3f1b-bf63-966b193ccfb4 | -14.54805 | -48.2523 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98601656-98df-3921-bf55-9ae8fd8de93e | -14.74327 | -45.66283 | 2025-09-30 05:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 421f262e-12f5-3f9c-918a-bca4de0bf370 | -14.53629 | -48.24771 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db347b25-f19a-3916-abad-16e8a91e6f69 | -15.33602 | -47.83113 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03ec7510-0f18-3b7c-9dfd-6d2062f7e315 | -15.92706 | -48.13002 | 2025-09-30 05:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75a46f87-cfd5-3708-b9ea-bc5261bfab87 | -14.56086 | -48.47085 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b4dfc35-5edd-3073-aa35-f36ecf6b1091 | -17.9193 | -57.60631 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 309a767b-efdd-360b-90e2-f3f4efe89554 | -15.32886 | -46.2688 | 2025-09-30 05:10:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcb5da59-13e5-3a7d-9167-ead49dc91240 | -15.1639 | -46.42722 | 2025-09-30 05:10:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9577a435-b215-3408-8742-6b8ce6f48210 | -16.06546 | -51.02963 | 2025-09-30 05:10:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a791b75c-09f8-386e-aea0-41f0a80ee0fb | -14.51634 | -48.43425 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45d6452e-7345-3545-b1c5-6d549000bba0 | -14.7087 | -48.16281 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 145b99f1-526c-3322-b3dd-091d4e17b2ea | -14.68275 | -59.83997 | 2025-09-30 05:10:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c710e20-d450-36c5-8fd5-47964f35a21c | -16.06027 | -51.03389 | 2025-09-30 05:10:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4f3edd6-942e-34ab-9168-030369bb8a9f | -14.54189 | -48.25815 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2f3d3fbf-0563-38ca-8bcf-4a0c5932a02e | -14.53671 | -48.24426 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f494a257-aa9f-3ac9-8dbd-bebfc2bbdb47 | -15.72509 | -47.59021 | 2025-09-30 05:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6bcc17d7-2bf1-318f-8597-c34e92aae2ed | -15.29594 | -46.4053 | 2025-09-30 05:10:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b212415e-eca2-3572-80db-39e75243fa40 | -14.72871 | -45.23415 | 2025-09-30 05:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ea0af16-f86e-38be-8f9c-8d2739aae68e | -16.27979 | -52.53547 | 2025-09-30 05:10:00 | NPP-375D | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 943bccdb-b08f-39cf-bf58-1af5d3897c25 | -13.74149 | -47.89986 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c9231a1-7cba-326e-ae3a-655da217638e | -16.38487 | -47.03837 | 2025-09-30 05:10:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b97b0cf-2ed1-3ed7-a47a-64f129513178 | -14.54239 | -48.48997 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4e55ed5b-e65e-352e-9ced-1399ed17de2b | -13.83263 | -47.50244 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64935982-b1f0-3ad5-8f50-a41462d6b3d4 | -18.534 | -46.05064 | 2025-09-30 05:10:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 96b2efff-f1f8-37ff-b5d6-003eaa606a8d | -14.53801 | -48.23348 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fcae110b-fdae-3fda-8939-75ebd0db93cf | -16.06428 | -51.03913 | 2025-09-30 05:10:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51feff36-0291-3eb1-a6d9-86d82f9cd500 | -14.52433 | -48.43583 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e77831d7-5ef3-35d5-8652-d8e1433799dc | -13.7555 | -47.92136 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9188d0a9-33fd-3c03-8b9b-20d599d47fd4 | -14.57746 | -48.28263 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d377889-bab8-3147-ba50-d3830fd55225 | -19.71725 | -45.88503 | 2025-09-30 05:10:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cc32afab-3ab4-3aed-a202-69af50c00a65 | -13.65635 | -48.05453 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d3c91f20-8dd2-33c0-9e9c-529482d3763e | -14.51705 | -48.40654 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c4e7f00-f0d4-31c2-8e53-515bd0adbed8 | -19.76889 | -48.96667 | 2025-09-30 05:10:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9dc41bb-8cd2-3ed5-b463-f9162428f3e9 | -15.26915 | -49.26796 | 2025-09-30 05:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 38e4831d-e9d8-318f-bd9b-bef63fc8c587 | -18.32918 | -57.10511 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 35be0ace-4243-3e92-9866-0bf0b967f394 | -15.97372 | -57.23893 | 2025-09-30 05:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9c81821-ab1e-38f3-afce-6ef543383778 | -16.53285 | -49.43311 | 2025-09-30 05:10:00 | NPP-375D | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 050af1f6-d033-396b-92a6-fd8b51e7234c | -14.51522 | -48.44406 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ab5effb1-1440-3996-98ea-5330ad35c135 | -14.56167 | -48.46395 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c51bfd85-79a8-38e4-afec-2ddefec3b6d0 | -15.52181 | -50.04971 | 2025-09-30 05:10:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c8ba4fa-6391-39a0-9652-c6c87563482d | -18.33258 | -57.10567 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7754c80b-a947-38ef-b3aa-77bd705d88f2 | -15.85123 | -56.39707 | 2025-09-30 05:10:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf30a4e1-eff5-3b2b-9467-8256e5f33fd6 | -14.70835 | -48.16584 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 281a46d6-8566-3ed5-bea7-3047005c7e29 | -15.17039 | -52.2966 | 2025-09-30 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f61c74a-fa49-3575-9508-59cdfe43379b | -14.56127 | -48.46739 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cdc5461-f1a0-33a2-9b9c-90e5eef62e83 | -14.68596 | -48.16807 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 477d3c6c-31ce-36d6-8f3d-2580183da1bc | -13.64657 | -48.04432 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3ab46be-4baf-31ce-805c-73bf744bc4bb | -14.53272 | -48.2422 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e91b45ff-9b6b-3d29-81ac-39f580fda670 | -15.32271 | -43.80426 | 2025-09-30 05:10:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa62455c-6c11-31dd-b6be-1c40c51f3978 | -14.51164 | -48.451 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4717ea23-c198-36a9-bd4e-6b71cf06572b | -17.39111 | -47.14611 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d2205d8-7787-3b4f-a2af-e14bf32e2bb3 | -13.81671 | -47.49199 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6fe7490-bf93-3e1a-9bce-8b9ef0b004cb | -15.17135 | -46.40704 | 2025-09-30 05:10:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 87880e8e-f64c-364d-916c-6724de53f9ff | -15.71341 | -59.50667 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5945163c-c5b4-3420-aea6-0d338ad8fc62 | -14.53886 | -48.2264 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4f5a511-7e46-314e-8186-a76fb07f3602 | -15.25756 | -49.71286 | 2025-09-30 05:10:00 | NPP-375D | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 016f3183-e6f2-3152-b46b-8ef30ed587ec | -14.79266 | -48.30111 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| df3013e0-a073-3761-afd7-af1fa8e0ec75 | -13.7603 | -54.72846 | 2025-09-30 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85bda005-add6-300e-97b0-fbb2150eb46e | -15.2688 | -49.2523 | 2025-09-30 05:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e7529e6c-b53e-3dbc-989e-445a16f0a513 | -15.4885 | -48.56068 | 2025-09-30 05:10:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82730858-8173-3d4d-b887-68ff1505346c | -13.79457 | -47.87326 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ff87af6-53bf-3cb5-923a-642e37976b9c | -17.38962 | -47.14859 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44ea473e-3da1-35be-86dd-abca098bd76f | -17.75741 | -51.34081 | 2025-09-30 05:10:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c254637-21c9-3e35-a486-b124113a2efd | -14.69438 | -48.23847 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dbcf1d6c-3c52-30cc-b2b0-18eaa1b527e5 | -14.53616 | -48.26031 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 20a17247-c208-3cd3-b291-3c7230bf75f8 | -15.71743 | -59.50346 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6db996f3-f3f3-360c-8ce4-c1ce233e85ee | -15.25189 | -49.71818 | 2025-09-30 05:10:00 | NPP-375D | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 71321831-25d7-3d15-b0bc-39e86d3b4ef3 | -14.70551 | -48.14264 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c96d59a4-0674-3890-93a7-8f38fd426206 | -14.56744 | -48.46098 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 014f2477-11a2-3dba-9362-b483e95ec74f | -13.80417 | -47.97864 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfae656f-d9a7-3394-8631-e96516356ba9 | -14.57442 | -48.21416 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e71e24f5-43fc-3124-9c59-5e7264aee188 | -15.8273 | -48.16807 | 2025-09-30 05:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4eee7c03-0bf2-3258-9636-a76c99cc2c48 | -15.71155 | -59.51798 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a95c25fe-27d3-3b07-8d91-cb389ac1bb1c | -14.71656 | -45.67099 | 2025-09-30 05:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1764efe8-f083-3cf8-a9e3-70685deef7eb | -15.20837 | -50.11824 | 2025-09-30 05:10:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 60b4759e-17b0-3541-ad72-d015ff8dcab0 | -14.3856 | -47.13942 | 2025-09-30 05:10:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 310d43f0-47f0-3c36-b526-8b76596fb0c7 | -14.54889 | -48.48062 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| baf19855-68ab-33c5-9d55-959b16c7b065 | -13.83785 | -47.50668 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a25bd89-23bb-30a4-8bed-c000532d74b1 | -14.53432 | -48.22801 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e7056a9-b814-320d-825c-65be703dd471 | -13.7354 | -54.72457 | 2025-09-30 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 52c4ae83-3e0e-3f5b-85da-02ba62858317 | -13.65594 | -48.05798 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7d458a0d-402f-39ea-abdf-b7e5d1c6bd4d | -17.10219 | -48.57438 | 2025-09-30 05:10:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34521acd-b2fe-398e-8b27-441fe52cdb4d | -14.52314 | -48.44561 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1f1534ea-c883-31b8-a29b-b633918bc0ff | -15.35314 | -56.96718 | 2025-09-30 05:10:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README99.md)
