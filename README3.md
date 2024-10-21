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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ea4a1cf-ab6b-328b-8500-1cec91ccc019 | -2.8097 | -45.7786 | 2024-10-21 00:35:22 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 023e948a-fc31-3a5e-bd18-d7905f4634dd | -2.8069 | -51.3613 | 2024-10-21 00:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 2b8b3239-738f-39d6-a9dd-de5d2d435f98 | -2.8481 | -45.4862 | 2024-10-21 00:35:22 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 7cffde31-dab0-3061-bccc-e033ce8a5567 | -2.8482 | -45.4637 | 2024-10-21 00:35:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 158d61a7-8a30-3345-b98d-20f63e494de1 | -2.8372 | -53.3261 | 2024-10-21 00:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 4c7d185d-c42b-3194-bfa6-0d1de3700c6e | -2.8667 | -45.4855 | 2024-10-21 00:35:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 43456d6f-0e93-3574-bbd0-c16ec72041b4 | -2.8668 | -45.4631 | 2024-10-21 00:35:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 6640201b-11a0-323a-9f19-96f6f5e195ac | -2.8865 | -45.1924 | 2024-10-21 00:35:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| f6134397-f8b5-3ad6-87e5-ac64e502c55b | -2.905 | -45.2143 | 2024-10-21 00:35:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 123.3 |
| b84202f9-99cd-347e-b8e3-ba056add0f2b | -2.9051 | -45.1918 | 2024-10-21 00:35:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 2d0bfa25-6f0f-32ec-b199-2c35cfccc09c | -2.9674 | -47.9931 | 2024-10-21 00:35:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 4311569a-87ce-318f-a84c-e15a4cdfe2c3 | -2.9852 | -53.0587 | 2024-10-21 00:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 4cda5de6-eefb-3bf2-b486-82b9b83344a4 | -3.0036 | -53.0583 | 2024-10-21 00:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 10804f59-1566-3608-aceb-e90994f7131e | -3.0037 | -53.038 | 2024-10-21 00:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 3c548845-50a8-3e33-950b-e4d6e6cbd3e2 | -3.0176 | -54.3489 | 2024-10-21 00:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 93079ac5-208d-3ca5-ba4a-e84d122c834f | -3.0581 | -53.2395 | 2024-10-21 00:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 60bd4873-5e2e-34aa-8898-50a917323f51 | -3.1138 | -53.1163 | 2024-10-21 00:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 737af2a5-97b5-3476-8aa4-e1b9cef84531 | -3.1962 | -50.8099 | 2024-10-21 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 504ea2ae-0749-3d77-9dda-13de268b0865 | -3.1963 | -50.789 | 2024-10-21 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 75a9510c-59c4-3fd5-bc81-b9d9a86cf86c | -3.2146 | -50.8093 | 2024-10-21 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |
| ae0ad7b8-8b39-36e8-bdb0-c6c1bc2fba9f | -3.2147 | -50.7884 | 2024-10-21 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 121.8 |
| c1e04326-28b2-34c5-bc48-f8f8a5d0443f | -3.2585 | -53.78 | 2024-10-21 00:35:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 901759b6-c119-37f2-a657-35c267873b16 | -17.7616 | -57.4272 | 2024-10-21 00:35:26 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 12ecf3f5-07eb-3e57-b662-26898f1ad7cc | -17.7658 | -57.452599 | 2024-10-21 00:35:26 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a545fa22-30fe-358a-876d-89ff845ba40b | -17.7477 | -57.403702 | 2024-10-21 00:35:26 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1db5ea3a-c0e3-3271-aaf6-a6196a945629 | -17.7519 | -57.429001 | 2024-10-21 00:35:26 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c349ebfc-ae61-316c-b60f-890e975552ad | -17.756201 | -57.454399 | 2024-10-21 00:35:26 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 71936999-f578-3003-b8bf-e4a13ffe5d4e | -17.742201 | -57.430698 | 2024-10-21 00:35:26 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5597cb28-18ba-3762-aa46-a1519ca9a96f | -17.7465 | -57.4561 | 2024-10-21 00:35:26 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c5dcc519-fdc8-3df3-b1e6-677316603a49 | -17.732599 | -57.4324 | 2024-10-21 00:35:26 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f11264cb-7e52-308c-a491-6bc68030ec20 | -17.7187 | -57.408798 | 2024-10-21 00:35:26 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 96bd0bd7-3457-342e-a31e-32c741cf786f | -17.7229 | -57.434101 | 2024-10-21 00:35:26 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7ebbda7e-798d-36a4-b1ad-6c589d08a9d2 | -17.7272 | -57.4594 | 2024-10-21 00:35:26 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 758e1327-55ff-34f5-9210-1c6937f76bef | -17.7132 | -57.435799 | 2024-10-21 00:35:27 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 973fa21b-5838-376a-9d33-efec4814f2e6 | -17.6896 | -57.413898 | 2024-10-21 00:35:27 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6e7a8110-ed08-3c64-890d-c11528abdf3c | -17.693899 | -57.439201 | 2024-10-21 00:35:27 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2e418f0a-422f-379a-89d1-df76e96779ed | -17.675699 | -57.3904 | 2024-10-21 00:35:27 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2bca9357-a99e-373c-9c7e-6dc62e2bf985 | -17.679899 | -57.4156 | 2024-10-21 00:35:27 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e2cb9182-1e96-34ba-acea-a8df08087525 | -17.6842 | -57.440899 | 2024-10-21 00:35:27 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d24e5f33-1647-3b1d-9100-87d611cd75d3 | -17.6661 | -57.392101 | 2024-10-21 00:35:27 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 90f9f442-183b-3333-b2b0-f3a346e96afe | -17.6703 | -57.417301 | 2024-10-21 00:35:27 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 988a81fc-a0d5-334b-bb89-2a858f78e04e | -4.0899 | -46.1493 | 2024-10-21 00:35:29 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 85b3fd34-b4da-322b-92f1-b0f1aa878ac0 | -19.508101 | -56.592499 | 2024-10-21 00:35:30 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f73c74fe-ca1b-39fa-993c-1a62028f8c13 | -4.4414 | -46.4425 | 2024-10-21 00:35:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| e12330f0-c3a7-3268-a9f9-43e051fa801d | -4.8291 | -46.8857 | 2024-10-21 00:35:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| fe2878ac-3405-3cb2-8ae1-82c2ac2f5f3d | -4.8477 | -46.8847 | 2024-10-21 00:35:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 54.5 |
| c5495a57-bae9-355b-9857-d45918c3e0a9 | -4.8924 | -45.8386 | 2024-10-21 00:35:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| f0a61051-fc7e-3f2a-b915-826a0b14fe52 | -4.911 | -45.8374 | 2024-10-21 00:35:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 899dbb56-3f0e-32af-98f9-34a8a1aab5ef | -5.6707 | -46.4363 | 2024-10-21 00:35:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 063d27bf-dc3a-3bc8-8012-a78b06bd72e5 | -5.6709 | -46.414 | 2024-10-21 00:35:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 5b6d731d-57e0-3b06-83e4-167d3e1b3379 | -5.6894 | -46.435 | 2024-10-21 00:35:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 18c17f50-8029-323d-91c6-a5208afdb136 | -5.6896 | -46.4128 | 2024-10-21 00:35:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| d3b8dbe1-1452-3ea1-aad4-979ad1496c6d | -5.7081 | -46.4338 | 2024-10-21 00:35:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| b113db9e-b963-3bfe-a70a-bb950349cf53 | -5.7083 | -46.4115 | 2024-10-21 00:35:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 2642e690-9c25-31e9-b757-ba4184642631 | -9.3718 | -66.4891 | 2024-10-21 00:36:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 06129e47-e0f0-34b0-b3ce-0bff6c807c87 | -9.934 | -36.0974 | 2024-10-21 00:36:01 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 105.7 |
| 33360c7a-d3ad-34e1-a124-607f51c16f20 | -9.9533 | -36.094 | 2024-10-21 00:36:01 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 72.0 |
| 2049db68-c143-3f44-a6d6-a68e101fa8fe | -12.4778 | -63.1885 | 2024-10-21 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| a0023a22-b6d2-3ea6-bf52-35a2ea3b4011 | -12.5147 | -63.3014 | 2024-10-21 00:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 706c1923-b480-3489-939a-99bbe567ba06 | -12.5357 | -63.0319 | 2024-10-21 00:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.4 |
| cb64f282-ac7d-32ff-a8c9-b864e8dd4450 | -11.9244 | -48.060398 | 2024-10-21 00:36:31 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0534ee0f-6eec-3989-ae1a-2a1e042e2dfe | -11.926 | -48.067402 | 2024-10-21 00:36:31 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f63e483-2188-369f-8882-a5d7a32f5f44 | -18.263 | -56.1021 | 2024-10-21 00:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.6 |
| 5f4322a7-0368-39d8-a32c-12772f27f372 | -18.2633 | -56.0812 | 2024-10-21 00:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.1 |
| 9a393f66-3dcc-33ea-84a7-d6edda11ba2a | -18.2828 | -56.0994 | 2024-10-21 00:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 175.0 |
| 4a34cdd8-cfd8-3b8d-b816-e6d73e7c11e7 | -18.2832 | -56.0785 | 2024-10-21 00:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.6 |
| 2bd54a67-9f85-3410-a9f8-8c0eceb33d5f | -7.1394 | -44.9641 | 2024-10-21 00:37:37 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7ffbf5d-0cd4-36d0-a88a-2b319840674f | -7.1417 | -44.973499 | 2024-10-21 00:37:37 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f863b20-78e9-3e9c-b108-7d590e466450 | -6.9925 | -50.233601 | 2024-10-21 00:37:59 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f757ec0-1643-3d45-bcc7-844915a214fa | -6.9941 | -50.240601 | 2024-10-21 00:37:59 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3402749e-34fc-3b56-b426-8e63060cb79b | -5.6542 | -46.424 | 2024-10-21 00:38:07 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ae65c2c-334c-3f72-ba83-b8e17b4b129c | -5.6561 | -46.432201 | 2024-10-21 00:38:07 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e78fb009-8105-3067-a83b-c494ce41e906 | -5.6579 | -46.4403 | 2024-10-21 00:38:07 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5bcec597-4a64-3f2b-80fd-af56336f1bba | -5.6425 | -46.417999 | 2024-10-21 00:38:07 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d7d91496-60c8-392e-9979-350f7e5dbf88 | -5.6444 | -46.426201 | 2024-10-21 00:38:07 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03b571b3-e700-3ca9-abdf-78a35fad6af0 | -5.6463 | -46.434399 | 2024-10-21 00:38:07 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f290904-7d0f-3a30-b049-0705e106ad1a | -5.6481 | -46.442501 | 2024-10-21 00:38:07 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4b7dfc02-4786-339e-81c5-53bd3fda820f | -5.3063 | -45.634201 | 2024-10-21 00:38:09 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 103e339a-7dc9-3d25-ad4c-8b3746d885ad | -5.4004 | -46.351898 | 2024-10-21 00:38:10 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 44cd85a8-7efa-3180-a41a-64a06a83617d | -5.4024 | -46.360199 | 2024-10-21 00:38:10 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c9fe6f14-983d-3d94-bf07-d768a4a7bb0f | -5.3906 | -46.354198 | 2024-10-21 00:38:11 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e523418d-e99e-34ca-9b84-c54a9a24c11f | -5.3926 | -46.362499 | 2024-10-21 00:38:11 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f1b408bf-0e73-32bd-9230-7a06a6cd574a | -4.8094 | -44.343601 | 2024-10-21 00:38:12 | METOP-B | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f6b97c0-b00d-3e1e-bc3f-fb1cfece0c36 | -4.8119 | -44.354599 | 2024-10-21 00:38:12 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26b9bf3c-cc4b-35d0-b7c1-804f4f09fbf6 | -4.8068 | -44.3326 | 2024-10-21 00:38:12 | METOP-B | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f6d2a2ad-1232-3033-a4ee-b67065e83a42 | -4.899 | -44.858398 | 2024-10-21 00:38:13 | METOP-B | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18c9b1fb-a124-32dc-87d3-6f1544248427 | -4.9014 | -44.868599 | 2024-10-21 00:38:13 | METOP-B | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6e83bb6-7179-3ffd-ba0f-ddb801e6d3be | -6.1794 | -50.881199 | 2024-10-21 00:38:14 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12c4bc5f-d395-359c-8c62-709dd83cea58 | -6.1565 | -50.871201 | 2024-10-21 00:38:15 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f76c221-ac58-39ec-9451-071b2030cc15 | -4.6403 | -44.588699 | 2024-10-21 00:38:16 | METOP-B | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4b76242d-6552-3438-a9cc-05b82cd92650 | -4.8675 | -45.8302 | 2024-10-21 00:38:17 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3fa0a73f-d755-3f04-bd55-db262e2f324a | -4.8696 | -45.839199 | 2024-10-21 00:38:17 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5f5d217b-2707-369e-a9c0-0e119b923b3a | -4.8716 | -45.848099 | 2024-10-21 00:38:17 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 080003b6-4899-3c80-9926-90d9ab2eaf71 | -4.8556 | -45.823502 | 2024-10-21 00:38:17 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c30ec0a8-5dea-39cf-a927-d779d7bffb79 | -4.8577 | -45.832401 | 2024-10-21 00:38:17 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 011b7396-023e-3532-a697-5419fcc15f3c | -4.8598 | -45.8414 | 2024-10-21 00:38:17 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ba6363e2-b066-3201-a3d7-2c17b4286e70 | -4.8479 | -45.834702 | 2024-10-21 00:38:17 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 99b18ebd-3b28-3ce2-bc27-7c8a7ee7826e | -4.7138 | -45.7897 | 2024-10-21 00:38:19 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9de6d61f-4465-355c-8cdd-79d31a74f748 | -4.704 | -45.792 | 2024-10-21 00:38:20 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4f5da72e-d5b2-3fb3-9423-5b2389563de7 | -4.632 | -45.703098 | 2024-10-21 00:38:20 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
