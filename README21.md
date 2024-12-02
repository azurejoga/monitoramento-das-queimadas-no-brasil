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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b010cd35-38a6-36a1-a6fb-d404a8a7a290 | -11.27574 | -41.73482 | 2024-12-02 03:10:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 6520a429-3e91-36ee-9a46-0520cf502cb4 | -9.78118 | -36.14751 | 2024-12-02 03:10:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| fd3e4023-c671-3930-8e70-65b31d8d8986 | -11.13347 | -37.22152 | 2024-12-02 03:10:00 | NOAA-20 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3481c89a-1737-3bcc-8848-d9e116a9d146 | -9.84466 | -36.16522 | 2024-12-02 03:10:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 1c13ed63-83a8-3381-9802-91f00964b2b3 | -10.05642 | -36.55654 | 2024-12-02 03:10:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2bc35462-9900-3b6f-93b5-3f29dc62f3d6 | -11.13408 | -37.21833 | 2024-12-02 03:10:00 | NOAA-20 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 20be1b62-86f9-312e-bc15-e453314a2c1f | -22.54828 | -43.56359 | 2024-12-02 03:14:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7fa07e0a-fa9c-3b3b-9d4f-764f070d2104 | -5.5882 | -45.1412 | 2024-12-02 03:20:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 7259b9c7-12ce-328a-af7d-1b92202d4d05 | -12.4358 | -63.7455 | 2024-12-02 03:20:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 7e6052d0-227a-3bdf-a47d-af4b9beca481 | -2.6348 | -53.3712 | 2024-12-02 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 1a8dd8f8-8679-382b-873b-11b896659968 | -12.4359 | -63.7264 | 2024-12-02 03:20:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 90291d22-7fce-3359-9426-e48d9b00213b | -2.8013 | -53.043 | 2024-12-02 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 1d9da91d-a181-3ab6-8a22-2371f60c87a7 | -3.259 | -53.6388 | 2024-12-02 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| e2a27fae-6637-3f6b-84d7-9d4c4def279e | -5.118 | -43.2198 | 2024-12-02 03:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 348ed036-0492-3a82-9f95-8f7bbe355932 | -2.6349 | -53.351 | 2024-12-02 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 8594b696-ee40-360e-8177-f91d999e175f | -2.5612 | -53.3931 | 2024-12-02 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 1408edfa-ecac-30c1-962a-63f0b8b0f76e | 1.1072 | -56.007 | 2024-12-02 03:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 7fbb317a-1e71-3e72-a427-29577846d4c1 | -2.5428 | -53.4137 | 2024-12-02 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 31dc22c4-b401-3e8b-abb5-1c4bdba395b3 | -12.4169 | -63.7465 | 2024-12-02 03:20:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| ae3c2421-96f2-37c1-82f6-15d75c4978f3 | -3.2591 | -53.6186 | 2024-12-02 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 82afe8b8-51dd-359d-96f5-2bf318d0b3aa | -2.8012 | -53.0633 | 2024-12-02 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| b48dd0ac-9e97-37d8-9f1a-eae696e02c6e | -3.4017 | -50.2381 | 2024-12-02 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 88fce452-bec7-3e57-affd-00572a0a4055 | -6.086 | -48.0557 | 2024-12-02 03:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 98f6b3e4-1151-34f4-93b2-e7eb97e7bc07 | -5.1181 | -43.1964 | 2024-12-02 03:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| ddd0b5fb-8a48-3eb1-899e-71a2d9580635 | -5.1369 | -43.1951 | 2024-12-02 03:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 6c521f28-20d5-3ace-8aa7-b264f0e430a5 | -2.8196 | -53.0629 | 2024-12-02 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| c9c6d29d-0707-302d-bcd9-a2970238d738 | -2.5612 | -53.4133 | 2024-12-02 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| b6c0072e-13fe-3771-95f0-860629d5b30e | -5.1367 | -43.2185 | 2024-12-02 03:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 3ecdda23-9899-3aae-986b-8a70ef1f1f1e | -2.8197 | -53.0425 | 2024-12-02 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 6a392ab3-e3df-33da-9acc-cc9374f36fd9 | -4.5745 | -43.3483 | 2024-12-02 03:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| a8b31f6f-39dc-3619-a5de-50ea83ed2ea0 | -12.4358 | -63.7455 | 2024-12-02 03:30:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 1e1b9d2e-268f-33d7-830f-38e9cba165d9 | -12.4169 | -63.7465 | 2024-12-02 03:30:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 0503f7ce-9014-3034-bed8-87917fff07ec | 1.1256 | -55.9872 | 2024-12-02 03:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 8afcacf8-5476-349e-9270-dd1448dee5fe | 3.3658 | -60.5139 | 2024-12-02 03:30:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 54a36aa4-71af-353d-9269-c9b16ce6a817 | -2.8013 | -53.043 | 2024-12-02 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| dcd92ae3-43b0-3ba0-928f-917c977c599d | -2.8012 | -53.0633 | 2024-12-02 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 2096eb73-d408-3f27-aa08-45d3c6ed993b | -2.5612 | -53.4133 | 2024-12-02 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 9e182fbf-912a-3f9c-9ee6-3d98efd1f73c | -2.5428 | -53.4137 | 2024-12-02 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 50414689-2cf5-3d3a-9b0b-0db8e1ae270e | -5.1369 | -43.1951 | 2024-12-02 03:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| fbca36c2-9d1b-3743-a2cb-ad7870215b50 | -2.6349 | -53.351 | 2024-12-02 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| bbafe56a-2bb2-3686-a105-dcc3e4faad97 | -5.118 | -43.2198 | 2024-12-02 03:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| ecc21124-d2b8-35ba-a820-76969b023e0c | -2.6348 | -53.3712 | 2024-12-02 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 0fe18327-53e0-31ad-95ac-e7e840a6d3ae | -2.8196 | -53.0629 | 2024-12-02 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 494d2943-f196-30ee-8d6f-56c91f266206 | -3.259 | -53.6388 | 2024-12-02 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 384c2634-3cc3-3bde-a85b-1db168eb9aa5 | -2.5612 | -53.3931 | 2024-12-02 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| de001ce6-a3e5-3bd0-afe6-ba74d2eff1f9 | -5.1181 | -43.1964 | 2024-12-02 03:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| e29fb2b9-c2d7-3218-a149-2d2b8b5ffb58 | -2.8197 | -53.0425 | 2024-12-02 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| a1a65409-9cf4-32c2-a2b6-07bbea482428 | -6.086 | -48.0557 | 2024-12-02 03:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 1001adf5-14db-378b-b5a7-f73d1d70e956 | -5.5882 | -45.1412 | 2024-12-02 03:30:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 5e1e012b-84e1-374c-8a92-9e3e64d3b11b | -12.4359 | -63.7264 | 2024-12-02 03:30:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 81934510-325d-3000-b15f-85f4a9c942f0 | -3.2591 | -53.6186 | 2024-12-02 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 9709d8cd-22ce-3959-8a90-5b7011e56cd5 | -12.4359 | -63.7264 | 2024-12-02 03:40:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 46.2 |
| d61ff339-693f-3dba-93ec-0134c75c6b00 | -2.5612 | -53.4133 | 2024-12-02 03:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 0e8c3f9f-c5b9-3e7b-8120-fd50bdb59d07 | -2.6349 | -53.351 | 2024-12-02 03:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 214dc932-9d2d-3062-b8ef-465623070bd8 | -2.6348 | -53.3712 | 2024-12-02 03:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 451d1596-6457-3d0f-8f86-688b27ca99f4 | -3.2591 | -53.6186 | 2024-12-02 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 102c9d4c-aa08-3c42-93e8-0158bac28e51 | -4.5745 | -43.3483 | 2024-12-02 03:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 2870863a-2839-3453-90b9-0d3f587db74f | -3.259 | -53.6388 | 2024-12-02 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 46710910-08f7-3877-a221-e568f8b97054 | -6.086 | -48.0557 | 2024-12-02 03:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| bf9c9893-0d05-3a21-be98-27405014bbf8 | -5.1181 | -43.1964 | 2024-12-02 03:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 7d3cdedd-844a-3ded-b9d8-7f6587661b3f | -12.4169 | -63.7465 | 2024-12-02 03:40:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 91f45dac-9956-3f48-a4bd-6d1b898029a8 | -1.4379 | -55.2136 | 2024-12-02 03:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| d459140d-b50e-39f7-8e44-0ede84eff786 | -2.5612 | -53.3931 | 2024-12-02 03:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| e85ace60-33ab-305f-9543-b004433d40bd | -1.4562 | -55.2134 | 2024-12-02 03:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 2f77bd1b-dbbe-3a5b-a69b-72a269c1df0c | -5.1367 | -43.2185 | 2024-12-02 03:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| ffbf10df-fc4f-3c9a-a4cf-1f207c32d9ef | -12.4358 | -63.7455 | 2024-12-02 03:40:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 72.2 |
| f32b91c7-af6d-337e-a0bb-19f4513a8c75 | -5.1369 | -43.1951 | 2024-12-02 03:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| b1b8d048-7854-34d7-8f7f-6896d9660a62 | -5.118 | -43.2198 | 2024-12-02 03:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| d5ce06f8-68d5-32f0-bd65-fd0dd86dd53f | -5.1369 | -43.1951 | 2024-12-02 03:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 3e24e0db-70f5-3994-bba2-61fdbc86708e | 1.1072 | -56.007 | 2024-12-02 03:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 722d6d56-7d5d-34b2-bf97-997b198cea0b | 1.0889 | -56.0072 | 2024-12-02 03:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| e4d5aec1-5476-3255-be63-7fdfa46f861d | 1.1072 | -55.9874 | 2024-12-02 03:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 43991408-9958-332f-beb1-f4571797991d | -2.6349 | -53.351 | 2024-12-02 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 390d0c30-b621-3369-9099-782a9831503d | -5.1367 | -43.2185 | 2024-12-02 03:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 11364b16-edb4-38e0-bc9d-2a720f361a96 | -2.6348 | -53.3712 | 2024-12-02 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| b102e108-d027-3c29-abb6-807c7c8a83e3 | -6.086 | -48.0557 | 2024-12-02 03:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 8cae9ca6-d823-3331-9a2a-5004094f8bd5 | -5.5882 | -45.1412 | 2024-12-02 03:50:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 9ee948ea-6260-3f9d-9135-8aae119cc899 | -12.4358 | -63.7455 | 2024-12-02 03:50:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 84763921-2b45-3411-b1a0-8204fbd188a5 | -3.2591 | -53.6186 | 2024-12-02 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 4badf668-0a45-3ae6-abf2-6213b5f498ac | -12.4169 | -63.7465 | 2024-12-02 03:50:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 45.8 |
| fd273574-1bd3-3852-941e-b98fa0d80c0f | 1.1256 | -55.9872 | 2024-12-02 03:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 29a1cd2f-138b-34de-8eea-048adba2ec21 | 1.6119 | -50.94141 | 2024-12-02 03:59:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 09bacc5b-2841-34a8-a0f9-d6aa14810ece | 1.60911 | -50.9402 | 2024-12-02 03:59:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f7203af6-2846-3c9b-99dd-9e57b03266f3 | -2.6349 | -53.351 | 2024-12-02 04:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 03835452-494c-3631-9000-bf1b75a29a95 | -2.5612 | -53.3931 | 2024-12-02 04:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 25565912-5325-33ef-9532-f5a34a580668 | -3.2591 | -53.6186 | 2024-12-02 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 5dc21d9a-1f2e-36b5-8647-966de8e7fd04 | -2.5428 | -53.4137 | 2024-12-02 04:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 1dd0f006-8e41-3efb-9e37-721cc7dc3369 | -12.4358 | -63.7455 | 2024-12-02 04:00:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 02b93b24-2f73-366b-901a-10adb3a8c660 | 1.1072 | -56.007 | 2024-12-02 04:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 0fadc753-d718-3751-b187-e3f4a31ce984 | -3.259 | -53.6388 | 2024-12-02 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| bb947b9d-885a-3283-8534-21d83e82f551 | -2.5612 | -53.4133 | 2024-12-02 04:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| c43e4c5e-4a44-3504-9fe5-a8d90d99cf00 | 1.0889 | -56.0072 | 2024-12-02 04:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 202ad88e-fe6d-3b7c-b3d9-3d7782636f37 | -5.1369 | -43.1951 | 2024-12-02 04:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| fb27199d-4692-379e-a52c-cebd6490af2a | -2.6348 | -53.3712 | 2024-12-02 04:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 0b45d97d-010f-303b-b0b5-203925c39b87 | -3.2708 | -46.4511 | 2024-12-02 04:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 57.8 |
| e8201ab7-e427-31a1-88ff-11f8e8c0f76b | -5.1181 | -43.1964 | 2024-12-02 04:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 2b35c7b7-f45d-3949-8a1b-b2407f9c8243 | -5.5882 | -45.1412 | 2024-12-02 04:00:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| fb7fc55c-3255-3a39-af03-26e71df32483 | -3.36555 | -53.20778 | 2024-12-02 04:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59b66327-f7a3-35cb-892e-bb81b75e4131 | -3.7261 | -51.08133 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 47a57c9c-2bec-36d8-853a-900b39aa35d5 | -1.82858 | -46.22906 | 2024-12-02 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README22.md)
