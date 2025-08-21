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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3b42872-34d3-348f-bc64-c1941d848d3a | -13.1364 | -54.9376 | 2025-08-21 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| c68261a1-4f9c-343d-a107-4dc1b7de6c8b | -6.4529 | -53.3669 | 2025-08-21 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 76b2e0c7-1c34-3304-848c-4109c279d95d | -13.051 | -45.1693 | 2025-08-21 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 287.7 |
| 354e98d3-399b-3b90-8d8e-7d8a44f57dfc | -13.3349 | -54.4027 | 2025-08-21 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 130.2 |
| d33cb86c-4efe-38de-b58e-eb8f85e2e82d | -14.3127 | -52.0249 | 2025-08-21 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 5e354ff1-8404-3b31-88f7-51ee07c0dbcd | -7.6369 | -46.2599 | 2025-08-21 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| da6d230a-b2a8-3a3f-b637-0c57dbc25b3c | -12.9533 | -46.2419 | 2025-08-21 14:20:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 6e06f4fe-b38e-3510-9aa7-4a9c03875eca | -9.7052 | -47.9609 | 2025-08-21 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 0fb18d47-3e8c-38e7-a91f-450397206152 | -7.602 | -44.3801 | 2025-08-21 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 3cc08fc5-e0f2-3a06-8a9b-97329bef5684 | -7.5832 | -44.3819 | 2025-08-21 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 128142d7-d974-3f01-b52f-b71fb22eae56 | -8.4776 | -48.2578 | 2025-08-21 14:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 186.8 |
| 340e2cd5-ad77-3f76-a84e-ec14cb4b7c94 | -8.8736 | -62.4115 | 2025-08-21 14:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 190.8 |
| 07aebe07-f388-39a8-a283-182a4f0297a9 | -7.0166 | -44.6184 | 2025-08-21 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| e02abf2e-3a6b-36a5-8700-9bc35f12d366 | -14.3321 | -52.0224 | 2025-08-21 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 230.0 |
| 6bc77af6-ea2c-3e45-bea0-8c013de6c296 | -8.4964 | -48.256 | 2025-08-21 14:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 145.8 |
| eb5cb4ae-48ff-3b1c-b4ff-b25f4bfe2cc4 | -13.3346 | -54.4233 | 2025-08-21 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 09f06f44-dc8f-39fe-9f9c-69e0173eb523 | -14.8543 | -47.9279 | 2025-08-21 14:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 2c719306-0a97-31e6-ab0a-54cef56afdae | -5.2518 | -40.7296 | 2025-08-21 14:20:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 107.7 |
| 2750e36b-e761-3f37-a293-915c9781a9d8 | -6.5388 | -45.4998 | 2025-08-21 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 9644d86e-b02d-3385-a20a-e11a0a1aa685 | -5.2518 | -40.7296 | 2025-08-21 14:30:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 114.0 |
| 42c0a1bc-b323-30db-bb4a-cda9a8be2721 | -13.3349 | -54.4027 | 2025-08-21 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 114.8 |
| c72a201b-0c42-3a88-9859-9bd6fb403f5c | -9.5519 | -48.1306 | 2025-08-21 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 44964c4c-52c1-32ee-9658-df4932084863 | -12.4282 | -47.6707 | 2025-08-21 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| e78c7696-d36d-3fe6-b0ec-65f1041eb238 | -14.9999 | -54.8343 | 2025-08-21 14:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 4570336e-c6a5-36c5-9883-c9da6509b8f3 | -6.4158 | -44.6695 | 2025-08-21 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 04ec7887-8e10-35d1-8da5-ebcfb5292b76 | -13.3346 | -54.4233 | 2025-08-21 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 4d09acfb-3df4-3dd5-8604-915687bc7493 | -8.7756 | -45.4713 | 2025-08-21 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 2f476758-ca64-34c7-9877-2e7e85b89682 | -7.5832 | -44.3819 | 2025-08-21 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 727282a7-7203-330c-b7d4-3b47c766c0d2 | -13.3157 | -54.4047 | 2025-08-21 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| b437981e-d96f-3252-aa62-cb31a8735c9a | -7.6293 | -45.2691 | 2025-08-21 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 350bb19f-b928-3aba-8697-acf2dc4909aa | -6.5199 | -45.5238 | 2025-08-21 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| e6b80ab5-6b42-3ec1-9ec9-bb03c8c2e476 | -13.1367 | -54.9171 | 2025-08-21 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 272.1 |
| 438514e9-1ce8-3eb2-8074-4553d799bbaa | -8.8552 | -62.3933 | 2025-08-21 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 72e4682e-53f9-3b1d-8cb7-89cadd8700cb | -7.6296 | -45.2464 | 2025-08-21 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 1dfb43b8-789b-3571-84f4-279bacf43151 | -13.1555 | -54.9357 | 2025-08-21 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 7a673c38-77ea-302e-a48f-15e0aa719c3e | -8.69 | -62.1153 | 2025-08-21 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 4be9ded2-47ea-3b81-afb0-155edda2eeb5 | -6.1002 | -44.374 | 2025-08-21 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 6d173216-bbfc-3021-a659-a1acb8f7da60 | -15.0193 | -54.832 | 2025-08-21 14:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 97802652-eb18-348c-aed0-7089834a6dad | -7.1477 | -44.6524 | 2025-08-21 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 136.2 |
| cb8a5777-3e29-3dd9-b919-d302ce8918b5 | -8.7759 | -45.4486 | 2025-08-21 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 9ba3d231-5a17-3bf1-b3fe-975727dc7cd1 | -9.1895 | -59.6364 | 2025-08-21 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 39c412fd-f5d7-34e9-a52b-1a6eb5cba8e1 | -12.9353 | -46.1762 | 2025-08-21 14:30:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 7c8fc042-8174-305c-8cab-6e2adf89d960 | -13.3154 | -54.4254 | 2025-08-21 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 302a319b-7ef7-3b5a-9a3b-7cdd24210c11 | -4.7844 | -45.3057 | 2025-08-21 14:30:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 928f4bcd-5ae0-361c-8ee1-73ebbefe8b44 | -8.8735 | -62.4305 | 2025-08-21 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| c44fc2b6-7940-3faa-9beb-34464d7a7b98 | -6.5388 | -45.4998 | 2025-08-21 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 3b418daf-db99-3d5c-8103-65eaefa37ba2 | -8.6901 | -62.0963 | 2025-08-21 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 797b0156-a321-34af-abbc-e4333a6525e8 | -13.1364 | -54.9376 | 2025-08-21 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 97.9 |
| e9a47f2d-db5e-3c2d-a929-c30fcb9e41e5 | -6.4528 | -53.3872 | 2025-08-21 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 48908219-1a9e-3c16-ac45-fdf194b26bcc | -9.7241 | -47.9588 | 2025-08-21 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 404.0 |
| 1c1e9367-d974-3cf6-9d42-143043d63b51 | -9.1712 | -59.5987 | 2025-08-21 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 71b9e128-bd31-3f78-8340-1f57c63b20a4 | -6.4855 | -45.2101 | 2025-08-21 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 2ed591bc-20e3-317a-9001-014e62e4efc3 | -7.0354 | -44.6167 | 2025-08-21 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 14a61c02-ccbc-3077-9273-c20641c92989 | -8.4964 | -48.256 | 2025-08-21 14:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 13033448-d787-3270-821e-7d68a318e90a | -8.7948 | -45.4465 | 2025-08-21 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| ffd1b89e-f343-380a-b00a-a50cf26a73dc | -7.0166 | -44.6184 | 2025-08-21 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| a1395521-9a1f-370b-b3fa-7b997deae15b | -8.7951 | -45.4238 | 2025-08-21 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 9b81886c-915c-33ae-aa6a-1944618062c3 | -8.8551 | -62.4123 | 2025-08-21 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 6303f0fc-bfd2-301a-8c07-c8c9e52b223e | -7.602 | -44.3801 | 2025-08-21 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 9d787ef0-591e-30cb-be8f-357dc908f357 | -8.6343 | -62.1367 | 2025-08-21 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| e51b3ad6-eba6-3efa-a689-70cf9bb255f0 | -14.9805 | -54.8366 | 2025-08-21 14:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| acd8083a-7312-3a2f-8e36-299f9f09f3f4 | -6.4529 | -53.3669 | 2025-08-21 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 16841c50-a016-3ede-b7ea-13f1de817497 | -13.0505 | -45.1925 | 2025-08-21 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 672c486e-6db0-3938-96e7-1e7c8a52de0e | -8.8737 | -62.3925 | 2025-08-21 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 139.7 |
| d301fc18-6205-367e-99e1-2a538687cf1d | -8.5555 | -66.9574 | 2025-08-21 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 33300fdc-650c-37df-b012-fa4f05be5852 | -6.5386 | -45.5224 | 2025-08-21 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 169.8 |
| e6ccf0d3-0d2d-3404-b977-e82e47ca47e7 | -6.4857 | -45.1874 | 2025-08-21 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| c36ec715-0030-3b57-bccc-794e95fffd87 | -8.4967 | -48.2342 | 2025-08-21 14:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| b576cca5-6fed-34a5-9b48-fa6c0726be9c | -12.2191 | -45.4152 | 2025-08-21 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| c0596564-cf9d-3412-8d99-0f26c0d11fba | -12.9533 | -46.2419 | 2025-08-21 14:30:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 4d23a159-ab87-39ef-9393-b0b15f434628 | -13.051 | -45.1693 | 2025-08-21 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 209.6 |
| 59e751e3-17ba-3918-9d86-3987f539e5af | -15.0189 | -54.8528 | 2025-08-21 14:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 1559b3b6-c0fd-3cd2-9b96-a49cf7ca3a4b | -8.0152 | -47.6656 | 2025-08-21 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 7ff375e4-5962-3b30-b7bc-2953d735c581 | -12.9968 | -56.8597 | 2025-08-21 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 02921c3c-f5b0-3d99-84d3-46a7fec8a691 | -9.1711 | -59.618 | 2025-08-21 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 6c71e4b0-3a6b-3040-accd-b71a96ce97e5 | -4.7656 | -45.3293 | 2025-08-21 14:30:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| eb604c55-b10a-3b44-8e5b-36d12eeb29f8 | -14.9996 | -54.855 | 2025-08-21 14:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 42e7e737-3b46-353d-b4e1-a6f9f5313c41 | -4.7152 | -47.2216 | 2025-08-21 14:30:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 41a7d81a-7820-37cc-8193-395ee3283837 | -9.7052 | -47.9609 | 2025-08-21 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 480.6 |
| 492ee8c8-426a-33b8-b2ab-25fb8df3210e | -8.855 | -62.4313 | 2025-08-21 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 0411bd3c-fc6c-30ca-8b8d-34ef6916adbb | -15.9183 | -52.2303 | 2025-08-21 14:40:00 | GOES-19 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 215.5 |
| a2885237-f1f1-3ac5-8afa-73fb8696f7a8 | -13.3349 | -54.4027 | 2025-08-21 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 0058ff48-34a5-3f4f-8f4e-6842c41829c4 | -6.539 | -45.4772 | 2025-08-21 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 3e19a208-9f1e-3ed3-a5aa-77aa4d12aa8b | -9.053 | -67.4636 | 2025-08-21 14:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| af15d050-bed3-3289-b809-476facfe29f6 | -14.9999 | -54.8343 | 2025-08-21 14:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 163.7 |
| a1685135-0243-375c-926e-3735e8297a49 | -6.7994 | -43.8544 | 2025-08-21 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 0f3a083c-1f92-30d2-85a3-dfaf7f73ad4a | -9.1711 | -59.618 | 2025-08-21 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 81210e7a-4e34-3f5e-b336-c1483d82d9b6 | -14.9996 | -54.855 | 2025-08-21 14:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 92.1 |
| edf52193-5e2c-3e0a-b385-1c51450a8cd7 | -12.9533 | -46.2419 | 2025-08-21 14:40:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 730d762a-d3fc-3ed4-a60d-2c993afd7a6a | -13.0505 | -45.1925 | 2025-08-21 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 9ceea456-7137-3ab1-8179-02f14ea7fe45 | -14.3321 | -52.0224 | 2025-08-21 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 145.8 |
| b6a5f202-43f8-399c-80b3-f47c471ced51 | -6.5388 | -45.4998 | 2025-08-21 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| b2edbc67-82c4-37a4-8e84-f83f054bb493 | -13.1364 | -54.9376 | 2025-08-21 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 986af4ea-9784-3af6-b3d0-97972dbea395 | -4.7656 | -45.3293 | 2025-08-21 14:40:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| ea7bdc8c-94a3-371c-9117-722193416b89 | -13.1367 | -54.9171 | 2025-08-21 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 208.5 |
| 612c0343-49ed-31a6-a219-adac2a2ad9d9 | -8.8737 | -62.3925 | 2025-08-21 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 0904d5fc-a1f6-37bd-a581-0245f8a64f02 | -11.2892 | -44.9523 | 2025-08-21 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 2e8ff3f1-44fd-34d7-aa8b-1f172c0c0a59 | -14.527 | -51.9114 | 2025-08-21 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 1f7df798-b678-3be2-a4f9-7f6f426c789c | -13.1555 | -54.9357 | 2025-08-21 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 134.8 |
| e26e9b91-6243-30ea-a301-b93c2ebf8cc2 | -7.0354 | -44.6167 | 2025-08-21 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |


[Clique aqui para ver as próximas entradas](README66.md)
