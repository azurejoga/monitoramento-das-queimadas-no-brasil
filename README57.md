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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46f1bebb-e70a-3adc-a186-dc2d3ae7ebaf | -21.2854 | -47.6277 | 2024-10-03 02:57:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 9729113f-07ee-3d24-b4e7-c798ac6fb7d6 | -22.184 | -48.6256 | 2024-10-03 02:57:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.1 |
| 0ac2fcc8-4c51-39f7-9c21-da15b83b40f2 | -22.1833 | -48.6491 | 2024-10-03 02:57:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.4 |
| 09bd2389-be44-3495-a9fb-959404977dc9 | -4.1134 | -48.4886 | 2024-10-03 03:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| d6442be0-3391-3c66-8668-903d0d0000b3 | -4.095 | -48.4679 | 2024-10-03 03:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| c662fd67-33bf-3cb9-bcc2-d5adefd04c8e | -4.0949 | -48.4894 | 2024-10-03 03:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 3213b21b-3802-31a2-999e-84cb2c224ef4 | -4.5375 | -43.304 | 2024-10-03 03:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| ba52fd5a-48cf-3d59-b195-d480beb9fdea | -4.5373 | -43.3273 | 2024-10-03 03:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| ff07c6d5-5699-3b6d-8240-211be37bcf2c | -4.9264 | -43.79 | 2024-10-03 03:05:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| ef140d6a-fc62-378f-a3de-79a7ecab3abe | -4.9265 | -43.7669 | 2024-10-03 03:05:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 92837d85-e4c0-36a0-9d17-cf9456f6801b | -7.0752 | -48.028 | 2024-10-03 03:05:46 | GOES-16 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 23c235fe-7ef7-3ce3-8738-324d8a099fbc | -7.075 | -48.0498 | 2024-10-03 03:05:46 | GOES-16 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| a2d6af8a-d68c-3279-938e-2e27b31eca09 | -8.4259 | -46.2968 | 2024-10-03 03:05:53 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 6088806c-c964-3e67-905e-b9e28e724c42 | -8.8695 | -45.5066 | 2024-10-03 03:05:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 45.7 |
| d9fcf99e-c6d6-3c2c-b44f-b6d7607e0763 | -8.8506 | -45.5086 | 2024-10-03 03:05:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 6b79bc6c-3a87-35a4-9c99-47b0b65a9eb0 | -9.0515 | -67.871 | 2024-10-03 03:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 5fd7034e-de08-37be-aed9-e4903244260d | -9.0149 | -67.7423 | 2024-10-03 03:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| dac51fc8-bd2e-3e29-89f1-99a4bbd54a88 | -8.9976 | -67.4094 | 2024-10-03 03:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 0f9cc6b9-ad27-3e50-b5d8-005e6e774042 | -8.9791 | -67.4099 | 2024-10-03 03:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 100ecbb6-a570-37ef-bd14-c4e5fd651cac | -9.4866 | -62.3849 | 2024-10-03 03:06:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 55c125c6-5ea9-3fa2-aab3-922a5686a9d7 | -10.9384 | -46.5717 | 2024-10-03 03:06:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 2373991b-4584-34ef-9dc5-180622da10a6 | -10.8942 | -63.8971 | 2024-10-03 03:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 77bb368d-cc66-3d5f-8ef0-72d87ccab82f | -11.6932 | -64.9785 | 2024-10-03 03:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 70ff5ff6-05f2-397a-b40c-9857b72dc0f3 | -11.6931 | -64.9974 | 2024-10-03 03:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 7cb56a48-72b4-3bb4-8e1f-a069bb853ff3 | -11.6744 | -64.9793 | 2024-10-03 03:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 76.8 |
| e5970606-5a3b-3dcd-a971-617262d69b21 | -11.6743 | -64.9983 | 2024-10-03 03:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 58918ca0-1e85-340c-9d42-a55bd6f4ec22 | -11.6742 | -65.0172 | 2024-10-03 03:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 8b665f41-ef42-3540-a10d-1798b68d744f | -12.404 | -62.9817 | 2024-10-03 03:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 820232cf-c798-356a-8fe2-150069a3d2c1 | -12.4038 | -63.0009 | 2024-10-03 03:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 149.4 |
| c64105c8-d7e5-3183-8edd-10b87fd4a029 | -12.6484 | -63.1214 | 2024-10-03 03:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 73d239ef-bd63-38a3-a9a2-b3fcaba7fadf | -12.8991 | -62.5491 | 2024-10-03 03:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 466a4d79-103a-3b81-bdfd-6958df4084af | -12.8802 | -62.5503 | 2024-10-03 03:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 74.6 |
| e48090e9-87d8-3c18-b51d-adb625b91c68 | -13.0402 | -51.1432 | 2024-10-03 03:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 70355b96-1666-3222-b454-66b6bb89e733 | -13.0975 | -51.1575 | 2024-10-03 03:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 8fdb212e-7b36-3ead-8c1b-3ea733e16cfb | -13.0971 | -51.1789 | 2024-10-03 03:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 66268915-7e41-3655-ad5b-012fba8ba2fa | -13.0783 | -51.1599 | 2024-10-03 03:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 147.2 |
| e40bf251-d3da-3fda-8b47-35691250c910 | -13.0779 | -51.1813 | 2024-10-03 03:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| c7773438-4539-3a12-9116-82da05fbde71 | -16.779 | -57.8306 | 2024-10-03 03:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 668059c7-b8a1-3bd4-8bf5-a7840910ddeb | -16.761 | -57.7308 | 2024-10-03 03:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.3 |
| 582b69b1-34d1-3d5f-8cab-00cd1c6c543c | -16.7606 | -57.7512 | 2024-10-03 03:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.6 |
| e0bab0e7-c2e4-3245-888d-42abd9b88d45 | -16.7597 | -57.8124 | 2024-10-03 03:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.4 |
| ca59d1ae-5db9-3081-8ca4-04b61bc0fd81 | -16.7594 | -57.8328 | 2024-10-03 03:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.1 |
| 0eebdcac-e7f6-3cb3-9292-d6f64559a712 | -16.9179 | -57.6926 | 2024-10-03 03:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.0 |
| 19e2a936-8030-3919-9a3f-5cf08e9ba147 | -16.9176 | -57.7131 | 2024-10-03 03:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 532b8b3c-c2ed-3021-9470-0a7bc55c4871 | -16.8983 | -57.6949 | 2024-10-03 03:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.5 |
| 5e91b81e-c65a-3484-9cfc-7bedf771d382 | -19.0344 | -43.1944 | 2024-10-03 03:06:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.6 |
| 2c050ce5-caf8-39bf-ba28-5d2987318083 | -9.6295 | -40.61628 | 2024-10-03 03:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 8671d522-f428-39d8-9856-599adff31962 | -9.6229 | -40.61489 | 2024-10-03 03:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a4ef3ac1-9234-3388-9ac2-0eacefd0edb5 | -9.45776 | -40.36746 | 2024-10-03 03:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3ce67e06-32f0-3879-a5cb-cb30ff00c8d6 | -9.45667 | -40.37307 | 2024-10-03 03:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 43d94321-f6f0-3f9b-ad4a-049bde265f13 | -15.23221 | -43.33692 | 2024-10-03 03:13:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 62f6fd4c-66c6-3cad-aec3-7d5a2cf77c76 | -12.38842 | -38.00183 | 2024-10-03 03:13:00 | NPP-375D | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a60d6511-191b-3e11-9703-d3e363b08179 | -12.38774 | -38.00531 | 2024-10-03 03:13:00 | NPP-375D | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 66904b8e-1f12-31dd-9996-97faacdc06f2 | -12.34808 | -38.06544 | 2024-10-03 03:13:00 | NPP-375D | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5fc8f2cc-2419-33f2-a975-257df0a98e1c | -12.34201 | -38.06783 | 2024-10-03 03:13:00 | NPP-375D | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 14405c79-947c-3680-a74b-8f9fa52289f0 | -15.67944 | -39.21927 | 2024-10-03 03:13:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 82fe68ac-538f-30c8-9522-743c821ebed8 | -11.21486 | -41.06648 | 2024-10-03 03:13:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 00c39b2f-abd1-349e-9fa4-f0f84e2d29c4 | -11.21221 | -41.0633 | 2024-10-03 03:13:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6529cc1e-0fd3-3c18-9873-e8ef0458a5f6 | -11.21105 | -41.06918 | 2024-10-03 03:13:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d9d8c127-453e-3de4-a582-ed72725fb87a | -11.20821 | -41.06535 | 2024-10-03 03:13:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cbf0175b-89bf-32eb-bbee-a26a061809a8 | -15.08144 | -41.93834 | 2024-10-03 03:13:00 | NPP-375D | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 79d97f2f-244f-3aeb-896f-fb6eba1d115d | -15.81131 | -42.48802 | 2024-10-03 03:13:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0d646f05-228a-3a22-9ab4-8cced38b831a | -15.81002 | -42.49371 | 2024-10-03 03:13:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1c936d8d-e3ea-348e-9f3f-85f640009a85 | -15.80818 | -42.48801 | 2024-10-03 03:13:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c621eac3-0741-389f-bafa-1cf44e32f4c0 | -15.80691 | -42.49381 | 2024-10-03 03:13:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eeb6da12-828f-3602-b43f-0d689f177ce7 | -16.33927 | -42.30014 | 2024-10-03 03:13:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d5ebeb92-a81f-3be7-b37f-8c4118413609 | -16.3327 | -42.29911 | 2024-10-03 03:13:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6860789e-a90d-33de-87f6-5b0dcfa77925 | -15.23919 | -43.3386 | 2024-10-03 03:13:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8dfbe281-c56c-3f57-a037-ee5a80f86358 | -17.25413 | -43.18306 | 2024-10-03 03:15:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 942d0a96-e806-37b4-84db-68f3a3f7117c | -17.25261 | -43.18954 | 2024-10-03 03:15:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b35e0f6a-4604-3b09-8ff0-7e321e37b94b | -18.39569 | -44.01332 | 2024-10-03 03:15:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 81c7287c-5c64-37c0-80df-217eacc16126 | -18.86816 | -43.63263 | 2024-10-03 03:15:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1125227a-223b-3d07-9396-91bc612ac7b3 | -18.76714 | -43.38451 | 2024-10-03 03:15:00 | NPP-375D | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c7a4a477-a665-31d9-81fe-ffa5f3d68ee4 | -18.76579 | -43.39023 | 2024-10-03 03:15:00 | NPP-375D | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4b1468d9-a1da-3284-b812-171e7fcd4737 | -18.76292 | -43.38594 | 2024-10-03 03:15:00 | NPP-375D | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4f9a9f5a-c76c-3645-a8a3-8d21264f6e92 | -18.59805 | -43.39285 | 2024-10-03 03:15:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a09a4f87-9d71-390b-a2c6-118a4b14ce3c | -18.59666 | -43.39886 | 2024-10-03 03:15:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 62264268-39ff-3c17-aba7-209f79f9d5e1 | -18.59149 | -43.39109 | 2024-10-03 03:15:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 84d17c8e-dc91-338e-aa73-d87580f3ddc3 | -18.59011 | -43.39706 | 2024-10-03 03:15:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1c69c8c2-e013-3331-a5e3-57a3b66877e1 | -18.32172 | -43.23434 | 2024-10-03 03:15:00 | NPP-375D | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| b5b01cb2-090f-33fd-a7c8-43d5e94e5850 | -18.31747 | -43.23465 | 2024-10-03 03:15:00 | NPP-375D | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c0b9b35f-1602-3188-8028-4aa84728019e | -18.31518 | -43.23261 | 2024-10-03 03:15:00 | NPP-375D | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| c89ad805-975a-32d0-9d6a-eb98de483b82 | -18.31406 | -43.23734 | 2024-10-03 03:15:00 | NPP-375D | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 79a0d383-2293-37d2-9800-2136c343f4b3 | -18.31084 | -43.23329 | 2024-10-03 03:15:00 | NPP-375D | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| ad70968f-d9bc-3aa7-98a6-d283d93236a4 | -18.30958 | -43.23875 | 2024-10-03 03:15:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 960b2015-17eb-3b71-940e-5dfdc4cd05e1 | -19.27769 | -43.77554 | 2024-10-03 03:15:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e5f3ff01-93b9-3feb-a5ee-7f8116c8f804 | -19.27501 | -43.76878 | 2024-10-03 03:15:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8cc0e59c-e48f-308d-8e74-dd7de6dd9387 | -19.27351 | -43.77501 | 2024-10-03 03:15:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ec9d99c-edbb-3b7b-8623-15d3acb8df53 | -19.2726 | -43.76723 | 2024-10-03 03:15:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a5d2ba8c-7030-36be-90c0-fad2e4e839dd | -19.2711 | -43.77362 | 2024-10-03 03:15:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d04d4bd7-3f45-39c2-af5c-fd0fd89f03e4 | -19.26843 | -43.76688 | 2024-10-03 03:15:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b95f9004-b208-3f7e-ba40-0ff60e1d87c1 | -19.26689 | -43.77323 | 2024-10-03 03:15:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b54de8ac-aa5a-38c8-a8c6-708f6aaa047c | -19.26447 | -43.77187 | 2024-10-03 03:15:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb42b30a-9b88-3806-8e09-605ffd857f85 | -19.26311 | -43.77764 | 2024-10-03 03:15:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cab1832b-5f50-35d2-955a-7b3dec78d3ef | -19.24216 | -43.37775 | 2024-10-03 03:15:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 86d05c3f-4132-38b1-97cd-da89075ebb8d | -19.24059 | -43.38447 | 2024-10-03 03:15:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a92689ca-a140-3f43-ba78-22bf2c7b0cf2 | -20.148 | -43.8551 | 2024-10-03 03:15:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 92cf9db9-a633-3754-8d2b-f3968766e96c | -20.14477 | -43.82243 | 2024-10-03 03:15:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 541d32ed-1055-3b0b-9737-de092ecea845 | -20.14447 | -43.8532 | 2024-10-03 03:15:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 7f925104-e710-3d7e-9356-e134592353e9 | -20.14349 | -43.82787 | 2024-10-03 03:15:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |


[Clique aqui para ver as próximas entradas](README58.md)
