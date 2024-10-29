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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3a27b4d-5b01-3d8b-8873-2e9511659f37 | -1.4315 | -60.276402 | 2024-10-29 01:14:13 | METOP-B | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5d44eb2e-c763-3c6a-8d25-bfb6a9db1866 | -1.3144 | -60.214401 | 2024-10-29 01:14:15 | METOP-B | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e99188ca-8241-3b8b-b0f2-ddfd9e306287 | 3.4562 | -51.243 | 2024-10-29 01:15:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b3788701-3501-3035-ac92-b5466ad3f62d | -1.714 | -54.5335 | 2024-10-29 01:15:15 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| a5c2a7a2-449d-3f1c-af7a-1652fe04ee8e | 2.2133 | -61.657101 | 2024-10-29 01:15:17 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7cd72cfb-8102-308f-ba8f-b57f05bc98e3 | -2.3353 | -48.9137 | 2024-10-29 01:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 171.2 |
| 1e102524-c105-32c9-a9bc-bd55fa2f6dfa | -2.3353 | -48.8924 | 2024-10-29 01:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| dc05dc6d-a43b-34d7-a9c5-88b4bb325c61 | -2.3537 | -48.9346 | 2024-10-29 01:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 4d8c490a-e2e7-3f6f-9060-264ab5774e02 | -2.3537 | -48.9133 | 2024-10-29 01:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 261.5 |
| 1ed83681-452b-3d88-8051-54a5ef97d44a | -2.3538 | -48.8919 | 2024-10-29 01:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 35702637-6946-3b4a-9fce-cf91606dbd1d | -2.5066 | -47.4425 | 2024-10-29 01:15:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| d4b36864-afee-35fd-aa10-220ae952aa57 | -2.8555 | -53.3459 | 2024-10-29 01:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 2f969ed3-cd37-3052-bc3f-0e8e77beed83 | -2.8739 | -53.3454 | 2024-10-29 01:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 4450d1d8-77e4-3406-8917-fd20be63da40 | -2.9804 | -54.5099 | 2024-10-29 01:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 46a5bfb1-54f7-34b8-9a97-7665a48eab5a | -3.0913 | -54.287 | 2024-10-29 01:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 7ae6792c-d696-3e36-9052-4c4a4a003cbb | -3.1097 | -54.2865 | 2024-10-29 01:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| f08414ad-cc7d-3934-a4ac-6d534a65a977 | -3.1098 | -54.2665 | 2024-10-29 01:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| c3674d6a-8603-3fc6-9b6a-ad7b3efa8fd8 | -3.1281 | -54.286 | 2024-10-29 01:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| aa272a6a-568b-3622-90b8-bd214ee7c5d6 | -3.1281 | -54.266 | 2024-10-29 01:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| b5fddd87-bab2-3072-8a83-7dc26ca72c37 | -3.1794 | -50.3922 | 2024-10-29 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 68a9fc85-a605-3df2-bd79-6bfd6e194ef1 | -3.3044 | -47.198 | 2024-10-29 01:15:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 376763da-a58b-3478-9f23-1cf9ed49aed8 | -3.3573 | -44.0361 | 2024-10-29 01:15:25 | GOES-16 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| f6674d59-3fde-3490-b7ca-fe36ef9c581e | -4.2762 | -46.0956 | 2024-10-29 01:15:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 846a3070-33c2-32e8-9282-e6c3dd1895db | -4.6619 | -44.1751 | 2024-10-29 01:15:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| dc1418fb-42a8-3ea1-91d8-e4e3fa8bce7a | -6.0791 | -44.6276 | 2024-10-29 01:15:40 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| fc19151d-e6a1-37ea-9632-c2c040ff31e5 | -6.5956 | -47.3867 | 2024-10-29 01:15:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 9ec65425-c01f-3c41-b2cf-5cdf9173faa9 | -6.6141 | -47.4073 | 2024-10-29 01:15:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 4b4f89b1-6768-324a-973c-edd500e71e85 | -6.6143 | -47.3853 | 2024-10-29 01:15:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |
| d2839841-b3d6-3759-8653-c6198ff8f133 | 4.0492 | -61.244202 | 2024-10-29 01:15:45 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 320a980f-01c2-3c1d-a5bf-a92556d8b9e1 | 4.0523 | -61.2304 | 2024-10-29 01:15:45 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4688895d-a00e-38f2-a063-3a83859d75a1 | 4.0507 | -61.237301 | 2024-10-29 01:15:45 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8642b145-d32f-3c3e-bdad-0c2a482e1e4a | 4.0887 | -61.1152 | 2024-10-29 01:15:46 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4660af7c-bbec-37b5-b6f3-7a7c75cc4ad7 | 4.0871 | -61.122101 | 2024-10-29 01:15:46 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 67624c06-3f2e-3bdb-b130-84e840140577 | -11.138 | -55.5313 | 2024-10-29 01:16:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 942f891d-c696-35e6-829b-d6084678e6cb | -12.3526 | -49.9184 | 2024-10-29 01:16:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| dc17bf24-68a3-33e0-8981-6fdafbfab6c0 | -12.673 | -43.8042 | 2024-10-29 01:16:17 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 37.6 |
| d2e7a2ca-59fc-3155-94f4-52d0ad6d5576 | -13.6887 | -46.1247 | 2024-10-29 01:16:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| c92a510d-5389-37fb-92f4-4d0620360270 | -13.6891 | -46.1017 | 2024-10-29 01:16:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 65da6419-d20e-3534-ab17-c85b133d5fae | -13.7086 | -46.0985 | 2024-10-29 01:16:23 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| d8489664-9d3b-355a-bd58-67997a79c09e | -21.80441 | -53.49345 | 2024-10-29 01:24:00 | TERRA_M-M | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 14.5 |
| b2be5dad-2518-3f6a-ae4f-b32bfd1ea599 | -22.68999 | -54.66114 | 2024-10-29 01:24:00 | TERRA_M-M | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 5fba9c90-c5de-3edc-a451-634745f21b88 | -22.68868 | -54.65122 | 2024-10-29 01:24:00 | TERRA_M-M | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| ce7f4f68-671a-3412-aef5-3773fd2d814e | -24.0075 | -54.12854 | 2024-10-29 01:24:00 | TERRA_M-M | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 26.1 |
| 5614a10c-8243-3529-b682-4fc43c8c3ae2 | -24.00619 | -54.11864 | 2024-10-29 01:24:00 | TERRA_M-M | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| b6842ee6-c8a7-3b06-baf0-ad5ca93eed29 | -23.99852 | -54.12999 | 2024-10-29 01:24:00 | TERRA_M-M | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| b7b1a562-dcc5-318b-9b92-fc768b4a2933 | -23.99721 | -54.12008 | 2024-10-29 01:24:00 | TERRA_M-M | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 40.3 |
| 6ac0f011-7242-3a61-802b-b13cdf0c29ab | -1.714 | -54.5335 | 2024-10-29 01:25:15 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| d47f46fe-0e0c-3640-b89d-78a4739899ed | -2.3352 | -48.9351 | 2024-10-29 01:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| b40d22a8-bbeb-367b-87f9-b1308a661240 | -2.3353 | -48.9137 | 2024-10-29 01:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 206.0 |
| 34fccb4b-5fc7-3cd2-9784-7b1eb3a5e30e | -2.3353 | -48.8924 | 2024-10-29 01:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 6efae5ac-2f8d-3df6-a088-487c66cc99d9 | -2.3537 | -48.9133 | 2024-10-29 01:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 0bb460a2-3538-3ba9-aa52-defe79ceeb14 | -2.3538 | -48.8919 | 2024-10-29 01:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 4a6a971b-7c98-327e-8a9a-1083c1378653 | -2.5251 | -47.442 | 2024-10-29 01:25:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 409cd11e-5d34-3e80-86de-d6d31f7d5d0c | -2.8555 | -53.3459 | 2024-10-29 01:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 91461080-6c79-34bc-a191-da1cf17f55d5 | -3.0913 | -54.287 | 2024-10-29 01:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| b42bf1c9-ece1-33f0-a99c-c24eac9e0ea8 | -3.1097 | -54.2865 | 2024-10-29 01:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 177.7 |
| 1f2a8c9d-1477-3a3b-a08b-869b60020389 | -3.1098 | -54.2665 | 2024-10-29 01:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| e2534b83-e83c-3aa7-a6d9-51290a557985 | -3.1281 | -54.286 | 2024-10-29 01:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 4b98dfe1-d09f-3fd6-b4f6-bea72dca9688 | -3.1281 | -54.266 | 2024-10-29 01:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 670a0c5b-703e-3768-8b9f-a2b589bfb79e | -3.1794 | -50.3922 | 2024-10-29 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| a3f8bf96-43be-3341-a01e-64088e4b22ef | -3.3044 | -47.198 | 2024-10-29 01:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| eb65f7e3-75b9-30b5-a128-8929ada70b80 | -3.3229 | -47.1973 | 2024-10-29 01:25:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 0d3ecfab-3c0e-3e36-b9fb-17fbf4ff000d | -4.3473 | -43.779 | 2024-10-29 01:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 3c45f4b1-522e-3526-8044-b3f53330d646 | -4.3475 | -43.7559 | 2024-10-29 01:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 1d4e092e-db8b-398e-ab7d-8ccf0a0f0e64 | -4.366 | -43.778 | 2024-10-29 01:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 22ddc0c2-835d-3e0d-86f3-9cec66edd269 | -4.2761 | -46.1178 | 2024-10-29 01:25:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 1d2a7466-b4e2-3e68-acf5-d2bc4cf5c061 | -4.2762 | -46.0956 | 2024-10-29 01:25:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 1940854f-831a-32aa-a9a5-cedc6dc292de | -4.6619 | -44.1751 | 2024-10-29 01:25:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| f23893fc-b18e-38e0-99ef-bf2034842b9f | -4.6621 | -44.1521 | 2024-10-29 01:25:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 7bba7fee-dbd8-3bb2-b4c5-7e6b9dd9863b | -6.5054 | -47.0414 | 2024-10-29 01:25:43 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| b684c319-4994-383c-adb7-6c85bc94872b | -6.5956 | -47.3867 | 2024-10-29 01:25:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 50f31db9-8447-3b1e-8fb0-5829016a5941 | -6.6143 | -47.3853 | 2024-10-29 01:25:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| a5c52106-5dfa-303a-be2c-244445cbd283 | -13.69354 | -46.11671 | 2024-10-29 01:26:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 1a52cffe-3cf1-3d72-b121-09f0ea681685 | -13.60561 | -45.59402 | 2024-10-29 01:26:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| f16b7545-7f85-3748-8b33-900edcbc731f | -20.2637 | -55.42598 | 2024-10-29 01:26:00 | TERRA_M-M | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2dd93a6f-027e-355f-80d4-2ab60ec6fd4a | -20.26239 | -55.41609 | 2024-10-29 01:26:00 | TERRA_M-M | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5bede00e-484a-3437-9680-67add049ac57 | -19.47466 | -56.64385 | 2024-10-29 01:26:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 1bc8330a-19c0-341e-ae70-18316571ab02 | -19.58463 | -56.71062 | 2024-10-29 01:26:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| b2b669eb-044a-30f4-b9ab-ca487486f591 | -19.52592 | -56.70781 | 2024-10-29 01:26:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 52a37a79-6271-30fe-810a-72da66c89609 | -19.51246 | -56.59898 | 2024-10-29 01:26:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| dadf4fdc-84de-3d17-9bb2-bda2c27f612e | -19.51112 | -56.58817 | 2024-10-29 01:26:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| c46e524b-e055-3cbf-85bf-20f9b1b83d93 | -19.50715 | -56.59515 | 2024-10-29 01:26:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.3 |
| b1bec9a0-2b61-3fc1-96f2-02d7450172be | -19.50062 | -56.69556 | 2024-10-29 01:26:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 371583a8-369d-3b74-bd44-cb816f803488 | -19.49923 | -56.68465 | 2024-10-29 01:26:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 70d6065e-c564-3c6d-aa0b-68434fd8f89a | -19.48417 | -56.64249 | 2024-10-29 01:26:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| b945c776-28b9-3cf0-9cc7-66e91d7cce50 | -11.138 | -55.5313 | 2024-10-29 01:26:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 7d685c60-de74-3b38-bc6e-3c792229dc8e | -12.3331 | -49.9424 | 2024-10-29 01:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| a1c163d2-f524-349a-bf1b-60796b9ae46b | -12.3334 | -49.9208 | 2024-10-29 01:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 552bd250-0ce7-3063-bcd5-b20cf6a8d153 | -12.3522 | -49.94 | 2024-10-29 01:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 80a11cf7-ffd5-3bef-80cf-6424ef709d6b | -12.3526 | -49.9184 | 2024-10-29 01:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 64c15c45-b123-3b5f-92e1-0c27822cebb3 | -12.6725 | -43.8279 | 2024-10-29 01:26:17 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 421fa8b3-3f28-372d-b7ff-ad12e5511aaa | -12.673 | -43.8042 | 2024-10-29 01:26:17 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 25ad2a83-254e-3990-ac97-433dd2b51f6f | -9.70536 | -46.25245 | 2024-10-29 01:28:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 43609f7b-be12-392a-a61d-6c1260de8103 | -9.70144 | -46.25845 | 2024-10-29 01:28:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| a9d6e0a5-941c-3313-8ede-b5ce687b29a0 | -6.50659 | -47.03371 | 2024-10-29 01:28:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 40132407-d273-3f17-b9d8-6f4adbea35fc | -6.50261 | -47.04118 | 2024-10-29 01:28:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 951d66f4-3557-382f-bf72-90778b0699e5 | -6.61035 | -47.41781 | 2024-10-29 01:28:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| a5d33298-eede-3eba-b88f-973a24725e6d | -6.6046 | -47.38334 | 2024-10-29 01:28:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 816378e6-d9b4-39bb-81fd-e23ba5abc5ff | -6.60382 | -47.42426 | 2024-10-29 01:28:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| b2c40d0e-c86d-3d44-b5d9-dbc89c2319c5 | -6.59826 | -47.38956 | 2024-10-29 01:28:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 173.5 |


[Clique aqui para ver as próximas entradas](README17.md)
