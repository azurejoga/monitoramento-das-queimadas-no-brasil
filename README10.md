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
| 809b036a-0b00-312e-92d5-3383e8f8e5fc | -2.79724 | -52.97852 | 2025-11-15 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 29bc99d3-1d93-3fd1-83d1-e4e5c4641073 | -3.52707 | -56.32454 | 2025-11-15 01:13:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 59fbb96b-cba1-32b6-aee8-f808fa046c67 | -3.52912 | -56.3183 | 2025-11-15 01:13:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d71b849c-94ee-3afd-8154-e33e9c0c6fe9 | 2.75419 | -60.37021 | 2025-11-15 01:15:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 20836131-4557-312c-bd80-21f2229d3453 | -5.2209 | -44.369 | 2025-11-15 01:20:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 16a3df43-2b7c-350e-b834-f4453943c8e3 | -2.5053 | -47.812 | 2025-11-15 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| de605111-63e2-334f-9be1-b72873c0f19f | -10.3037 | -44.6017 | 2025-11-15 01:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 0377258a-594c-312b-8453-6b8046139a60 | -11.8486 | -49.2218 | 2025-11-15 01:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 218.1 |
| 6a944213-956c-30bc-8f30-2d49212d2838 | -17.2439 | -42.6575 | 2025-11-15 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 75.3 |
| c1a49df5-b4bb-3e56-b92a-d2da78f04d66 | -4.538 | -43.2341 | 2025-11-15 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 192.4 |
| 58d18056-3e75-3d8c-a994-b185333e0dbb | -3.51 | -43.3824 | 2025-11-15 01:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| f74d2816-8da3-3564-b186-020b033404b7 | -5.2397 | -44.3448 | 2025-11-15 01:20:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 66caa014-c3b5-3ec7-8c6b-5da5f3dc5965 | -4.5568 | -43.2096 | 2025-11-15 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 884fdb04-5c20-35e2-89fa-c404bb1265d3 | -5.2396 | -44.3677 | 2025-11-15 01:20:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 9c287043-644a-36ad-925d-2ef0b9e638d3 | -5.221 | -44.346 | 2025-11-15 01:20:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 37378ac9-7cde-3524-b6a1-194a290a512b | -2.5238 | -47.8115 | 2025-11-15 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 133.4 |
| a02594d6-4b33-3155-a2dd-4d014c65eed8 | -11.849 | -49.2 | 2025-11-15 01:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 198.2 |
| 4ea0af72-9778-3ab7-8fd0-cbdd3343873f | -4.5381 | -43.2107 | 2025-11-15 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 396.5 |
| 6ac5d97f-861a-3a2d-8544-e57187dc5d4c | -4.5567 | -43.2329 | 2025-11-15 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 230ead8b-564e-354e-bf12-749d33105770 | -7.3453 | -39.1631 | 2025-11-15 01:30:00 | GOES-19 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 38.7 |
| 93ef79b3-7329-3e05-bcb3-a2cbdf42500f | -12.6745 | -46.7605 | 2025-11-15 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 04676417-5a54-342e-8c9a-f3068ad49187 | -17.8173 | -40.1375 | 2025-11-15 01:30:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 241.2 |
| 91e86202-5bbc-34a8-b6bf-c52b5001aa53 | -4.538 | -43.2341 | 2025-11-15 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 126.2 |
| d52babf5-04a2-3af0-be2e-64c9c209fc10 | -11.8486 | -49.2218 | 2025-11-15 01:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 164.6 |
| dd19f1b1-20d7-3cea-a790-f3ffebc92182 | -11.849 | -49.2 | 2025-11-15 01:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 04b38bae-4c65-3a43-9c74-31dcab1b3a5e | -11.8295 | -49.2242 | 2025-11-15 01:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| a15c0d9f-b381-375b-83c9-7445dcc7ad25 | -4.5567 | -43.2329 | 2025-11-15 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 1c5352d3-c056-3ee7-950f-6bd47e15549d | -6.1606 | -48.0507 | 2025-11-15 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 700b148f-d221-3d80-9a4f-ac76a2ecbd9e | -5.221 | -44.346 | 2025-11-15 01:30:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 5c5d8d23-f3f0-3f37-9eb6-edfe2e7d831e | -11.8677 | -49.2195 | 2025-11-15 01:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| ad87fd7b-d82a-3141-9dd5-2b486fbd06b9 | -2.5238 | -47.8115 | 2025-11-15 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| e68aae4c-22c7-325b-be97-a47fc2c8a145 | -7.8947 | -48.3963 | 2025-11-15 01:30:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 48df9c83-fa0b-30f2-addf-1e50ec16414d | -5.2397 | -44.3448 | 2025-11-15 01:30:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 197.9 |
| 9a1a5be6-2cf1-3cfd-8180-d4af9725dd68 | -17.8165 | -40.1636 | 2025-11-15 01:30:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 217.6 |
| 456acd7e-6491-3abe-9b10-3c3ddb053352 | -5.2396 | -44.3677 | 2025-11-15 01:30:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| dc1e827e-7ec0-30df-86be-35f78acd3dae | -4.5381 | -43.2107 | 2025-11-15 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 299.3 |
| edc169dc-a17b-30e6-8a56-2d00d2353147 | -2.5053 | -47.812 | 2025-11-15 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| b82c2112-3cac-34f4-b961-0246886e5238 | -4.5568 | -43.2096 | 2025-11-15 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 6fddb7a1-9af6-322b-a87c-e934558a519a | -2.5238 | -47.8115 | 2025-11-15 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 3f07d81e-7a74-3293-9374-8a9371e29bbb | -11.8486 | -49.2218 | 2025-11-15 01:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 182.1 |
| 83fc9a59-5a16-3914-af26-7cada6278f5e | -17.7152 | -40.1914 | 2025-11-15 01:40:00 | GOES-19 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 78.6 |
| 3a7ff78f-f561-38cc-bc46-210c92781d43 | -4.538 | -43.2341 | 2025-11-15 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 7e17e349-42b2-3979-84ca-60c94d4d6e3d | -11.8677 | -49.2195 | 2025-11-15 01:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 4d1c03b5-a79f-32b0-9ad8-77360fd500c0 | -12.6745 | -46.7605 | 2025-11-15 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 4c308d01-fb93-3d28-988b-5005763acb4f | -5.2396 | -44.3677 | 2025-11-15 01:40:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| e0b70461-3da2-373f-b68a-71d28fefc948 | -17.6958 | -40.1709 | 2025-11-15 01:40:00 | GOES-19 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 287.9 |
| abdfeebc-1946-3dad-88ee-cdf6ad1580f1 | -2.5053 | -47.812 | 2025-11-15 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |
| e258614f-5281-3d0e-a7df-232bccdac149 | -11.849 | -49.2 | 2025-11-15 01:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 65fc59f2-09b8-369e-95d4-a453cd0d8f93 | -11.8295 | -49.2242 | 2025-11-15 01:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 2056dbd3-8f9b-332b-85b8-8efe5d04943f | -4.5568 | -43.2096 | 2025-11-15 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 9b099e7e-cf67-35ec-be66-4843a433113b | -17.695 | -40.197 | 2025-11-15 01:40:00 | GOES-19 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 423.7 |
| 31022f43-70c2-387d-9b96-876cd1032ca5 | -5.2397 | -44.3448 | 2025-11-15 01:40:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 290.2 |
| e58a4c90-74e6-35be-a1a5-809deceb9b49 | -4.5381 | -43.2107 | 2025-11-15 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 195.3 |
| 2d6d7b38-8125-3cc4-9654-b6ac06e6644c | -5.221 | -44.346 | 2025-11-15 01:40:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 3e769fed-cae4-3a0a-9883-868d9ee406b1 | -4.5567 | -43.2329 | 2025-11-15 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| abce1d35-8901-3021-ac58-44d0cdb31fcc | -5.2209 | -44.369 | 2025-11-15 01:40:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 19d4bd1c-581b-3f7d-985c-e350791e0259 | -4.5568 | -43.2096 | 2025-11-15 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 9334251a-6c95-3b90-8520-ae72a7109c14 | -2.5053 | -47.812 | 2025-11-15 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| c2dca847-9043-3b11-96d0-288a69b06091 | -4.5381 | -43.2107 | 2025-11-15 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 181.7 |
| 61fd16a6-7f6b-3c6c-bb36-43f5c6b70ede | -5.2396 | -44.3677 | 2025-11-15 01:50:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 142.9 |
| a8df106a-51c6-3621-806c-478903de32d7 | -11.8486 | -49.2218 | 2025-11-15 01:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 1b4eaea5-3438-3a42-996a-cdf0220c0bfb | -5.221 | -44.346 | 2025-11-15 01:50:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 649f8d77-eeec-3f83-9aa1-1e12abaad5b6 | -5.2397 | -44.3448 | 2025-11-15 01:50:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 259.8 |
| 1660609b-6727-3a62-936d-6ebfe2fe399e | -11.849 | -49.2 | 2025-11-15 01:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 5391b2c6-d21b-3867-b364-24bdb7520ce3 | -5.2209 | -44.369 | 2025-11-15 01:50:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 5d84664f-31d1-3b0d-9a70-09471c00d385 | -2.5238 | -47.8115 | 2025-11-15 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| b04af2d5-b1b9-345a-bb2a-1dd65dbc26be | -4.538 | -43.2341 | 2025-11-15 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 9fea20e5-6264-393a-9385-9c2b87e599a0 | -11.8295 | -49.2242 | 2025-11-15 01:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| e3a88042-d2fc-3404-9076-061d4f979490 | -4.5567 | -43.2329 | 2025-11-15 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| bbb92ac7-cab8-3412-be4b-72ec40b0368e | -11.8299 | -49.2024 | 2025-11-15 01:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 5f0f70e8-6114-39f7-936f-036cedf1f18c | -4.5568 | -43.2096 | 2025-11-15 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 164.4 |
| e6477e39-80cb-312a-97dc-e13e6a667b14 | -11.8486 | -49.2218 | 2025-11-15 02:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 9ce63297-065b-3f50-8f00-24edfd1e9db2 | -5.2396 | -44.3677 | 2025-11-15 02:00:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 99921cdb-d3c8-3430-a43c-51635286cf6a | -5.221 | -44.346 | 2025-11-15 02:00:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 07c96a5d-2859-3523-902c-a007fc84d770 | -11.8299 | -49.2024 | 2025-11-15 02:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 3660ddea-9ed7-323b-b0ff-35278ba54ac3 | -11.849 | -49.2 | 2025-11-15 02:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 124.3 |
| defeb112-34bd-3347-befb-2c6a6e5ddb7a | -5.2397 | -44.3448 | 2025-11-15 02:00:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 302.6 |
| b92eb1bc-1364-3c6a-9458-cea290ff40a0 | -4.538 | -43.2341 | 2025-11-15 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 2f4e37e7-a1f8-353c-8284-ba77b9d9152c | -12.6745 | -46.7605 | 2025-11-15 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 46.9 |
| dc96942e-5abd-3291-90a5-5a965e330316 | -11.8295 | -49.2242 | 2025-11-15 02:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 1a48ec59-ef45-3e99-806a-c2fd90819fa2 | -4.5381 | -43.2107 | 2025-11-15 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 229.6 |
| 79265255-5ab8-33e5-bfbf-d19ceca1f0b4 | -4.5567 | -43.2329 | 2025-11-15 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| d02fb2e8-9f6e-35f7-9a28-038a93cd039a | -2.5053 | -47.812 | 2025-11-15 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| a8706f83-9b41-39af-9066-f537f22f9f3f | -2.5238 | -47.8115 | 2025-11-15 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| bbeb87a9-b33f-397e-85a5-666c37641987 | -5.2397 | -44.3448 | 2025-11-15 02:10:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 229.6 |
| a7e8a8bb-3f3a-334c-8eba-a7dc78a4d7fe | -5.221 | -44.346 | 2025-11-15 02:10:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 4c07d51f-5ce7-304f-b088-e01211d023ed | -11.849 | -49.2 | 2025-11-15 02:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 0e69c086-4b38-3ac9-8063-f3f9edb3ffe9 | -4.5568 | -43.2096 | 2025-11-15 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 43bf272a-2cd8-33cd-9fe0-27c95f468aa1 | -4.5567 | -43.2329 | 2025-11-15 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 2806f2ea-d11f-3aa2-9ebe-dae3353229d7 | -11.8486 | -49.2218 | 2025-11-15 02:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 7b8e026c-a71e-3c46-9410-181b75f14f10 | -11.8295 | -49.2242 | 2025-11-15 02:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| e30a0769-3a9d-378a-8e60-ae6916843652 | -4.5381 | -43.2107 | 2025-11-15 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 212.5 |
| 776df550-4130-3277-8ba8-8ed02e6ea9dd | -5.2396 | -44.3677 | 2025-11-15 02:10:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| f5b73fae-1f0a-391b-94dc-79bb4562393c | -2.5053 | -47.812 | 2025-11-15 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 0e745ab3-03b9-339f-9511-143e45bd3273 | -4.538 | -43.2341 | 2025-11-15 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 128.1 |
| e7a1042d-5dd7-343f-90fe-f38243a115b8 | -2.5238 | -47.8115 | 2025-11-15 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| d927f455-38ef-3018-a4d9-70e389c49bd3 | -11.8486 | -49.2218 | 2025-11-15 02:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 456c85fb-f461-3ae4-8083-84836b5a6eaa | -4.538 | -43.2341 | 2025-11-15 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 0d439793-41f6-359c-9825-4ab5795d74f9 | -5.221 | -44.346 | 2025-11-15 02:20:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| c88d0250-3bf6-3a39-b802-8162400bbcb0 | -4.5567 | -43.2329 | 2025-11-15 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |


[Clique aqui para ver as próximas entradas](README11.md)
