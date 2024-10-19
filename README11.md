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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a53676de-f154-34fd-80c4-f10310fb1113 | -3.4388 | -50.1948 | 2024-10-19 02:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 92f1c480-7338-3fda-803e-d899c72d7335 | -3.4387 | -50.2158 | 2024-10-19 02:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 3ce43727-ab19-32a9-b0e0-0963327247eb | -3.4203 | -50.1954 | 2024-10-19 02:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| f1c7f078-c9ee-3497-a590-de6179373ac7 | -3.4202 | -50.2164 | 2024-10-19 02:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 142.5 |
| 84e4b73b-cacb-306d-ab5d-8d1ac0ceac22 | -3.5737 | -42.0403 | 2024-10-19 02:15:26 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 55.4 |
| 3c98cf07-b785-3100-9a9b-3c96c060c493 | -3.702 | -45.6988 | 2024-10-19 02:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| ef4af043-fa85-3eee-8bd6-b6e3b2ec4aeb | -3.7019 | -45.7212 | 2024-10-19 02:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 61acc6cd-40b9-3f88-b9a1-a1ad0374012c | -3.6834 | -45.6996 | 2024-10-19 02:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 1059c7b9-532b-38a0-a665-f1027f01e397 | -3.6833 | -45.722 | 2024-10-19 02:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 63ca8ce9-f317-39ab-8e59-110572c8688a | -8.0152 | -70.948502 | 2024-10-19 02:15:34 | METOP-C | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 079efe99-bcde-391a-b1b1-57061cbf4885 | -7.7621 | -70.060303 | 2024-10-19 02:15:35 | METOP-C | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b4f697e6-0947-3d91-aaac-1e07d097dba9 | -7.7636 | -70.067101 | 2024-10-19 02:15:35 | METOP-C | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1baf21e1-5c43-3c42-8f84-1522518e6227 | -7.8043 | -70.608299 | 2024-10-19 02:15:36 | METOP-C | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 90a9e3e9-23a4-346d-825a-4571e79e0d18 | -7.7811 | -70.642601 | 2024-10-19 02:15:36 | METOP-C | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| f6e18541-aa18-3e51-9e24-a42097362abf | -7.7797 | -72.885696 | 2024-10-19 02:15:45 | METOP-C | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c56e8c36-06b7-3c9a-85a9-9769d735026a | -7.6355 | -73.069901 | 2024-10-19 02:15:48 | METOP-C | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 83c7c561-3757-363f-9a38-832bf6f2740f | -7.5956 | -73.121399 | 2024-10-19 02:15:48 | METOP-C | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 42ee0c5d-4fa3-3058-86fd-e5e2e9160c2f | -7.5938 | -73.113297 | 2024-10-19 02:15:48 | METOP-C | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 3aa425b9-8bf4-30b3-9730-50e7db77b893 | -7.6054 | -73.119301 | 2024-10-19 02:15:48 | METOP-C | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c69c2969-2f75-304a-a514-367d2a051246 | -7.6036 | -73.111198 | 2024-10-19 02:15:48 | METOP-C | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 497b81a2-feda-3811-a22c-545cd1a44112 | -7.6337 | -73.061699 | 2024-10-19 02:15:48 | METOP-C | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e28cb70c-326c-31d9-ac81-ef9566d92b64 | -7.2812 | -72.770103 | 2024-10-19 02:15:52 | METOP-C | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b228925f-8f06-3fcc-ab77-a76b43863995 | -7.2794 | -72.762299 | 2024-10-19 02:15:52 | METOP-C | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8354d8d9-7807-3ee5-8b7a-71b886d378bd | -7.3173 | -72.886398 | 2024-10-19 02:15:52 | METOP-C | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dbde8611-9cc1-302e-8b4c-29992210ec25 | -7.3156 | -72.878403 | 2024-10-19 02:15:52 | METOP-C | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6ebaa2ce-44c3-30f5-a3b8-ad569d28ce3d | -7.2892 | -72.760101 | 2024-10-19 02:15:52 | METOP-C | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d223809c-a7e7-3a41-8156-49dd8d521139 | -7.3271 | -72.884201 | 2024-10-19 02:15:52 | METOP-C | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5f1e906c-b284-3eb7-a6ca-93436805cafa | -7.3254 | -72.876198 | 2024-10-19 02:15:52 | METOP-C | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee07e14d-2c8b-3e8c-8c5c-ceb36772c68f | -7.3316 | -72.858299 | 2024-10-19 02:15:52 | METOP-C | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cf0dba8d-4de5-319b-867d-c492227d3ffe | -6.8955 | -71.509003 | 2024-10-19 02:15:54 | METOP-C | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b76ed99b-a031-3ae8-b0bb-0e2ec4bb4bbe | -9.053 | -67.4451 | 2024-10-19 02:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 8d07ea54-6025-3398-a757-fce14a68c0f1 | -9.053 | -67.4636 | 2024-10-19 02:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 3395cd54-df07-3b9a-9af3-6595fd5a174a | -9.0345 | -67.4455 | 2024-10-19 02:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 113.5 |
| ee0c4127-e205-3978-b149-440cddff3d1e | -9.0344 | -67.4641 | 2024-10-19 02:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 121.9 |
| b5549ca8-2ceb-33cd-b6ae-722a2ceb167c | -5.6728 | -68.693199 | 2024-10-19 02:16:03 | METOP-C | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9737f756-dfe6-3187-95b6-085e46baf24c | -5.6843 | -68.698303 | 2024-10-19 02:16:03 | METOP-C | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c7eaf86d-2598-346c-8f55-144a3add72bb | -5.6826 | -68.691002 | 2024-10-19 02:16:03 | METOP-C | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ce50150-663f-3d7c-8958-9c69345e5e91 | -5.6809 | -68.683701 | 2024-10-19 02:16:03 | METOP-C | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 02725974-f54a-3f9a-b116-fd4e959ea964 | -12.0041 | -63.5008 | 2024-10-19 02:16:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 06bad33b-82c4-3b2f-9670-4cd85669fbb1 | -12.004 | -63.5199 | 2024-10-19 02:16:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 6835c8f5-2ed3-34e4-bb77-8889bcf0995b | -12.5147 | -63.3014 | 2024-10-19 02:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 0fb05fca-66ba-325f-b751-be9c42cf029a | -2.5635 | -47.0694 | 2024-10-19 02:25:20 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| fc627889-c778-3d9f-b9bc-c44bf2f00c64 | -2.9489 | -52.9174 | 2024-10-19 02:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| b97d7c84-21e4-372a-8120-e93e5c7c5c81 | -2.9489 | -52.897 | 2024-10-19 02:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 5086a096-01b7-3ae2-9908-efab659ccb3b | -2.9673 | -52.9169 | 2024-10-19 02:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| d890dd59-0217-3d01-8034-8524636ee69f | -2.9673 | -52.8966 | 2024-10-19 02:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 3e75f179-883d-3ead-a388-a8945d23752c | -3.4202 | -50.2164 | 2024-10-19 02:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| db9364ce-edcd-342f-a087-c0ed1a04485e | -3.4387 | -50.2158 | 2024-10-19 02:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 37addad1-e37e-3ab0-b919-4c42d76d8d7f | -3.4388 | -50.1948 | 2024-10-19 02:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 0545353d-aa7a-3618-8c3c-4a9046132c91 | -3.6833 | -45.722 | 2024-10-19 02:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 191.3 |
| 24ff46ba-acd5-37d0-a6e9-53555d585a24 | -3.6834 | -45.6996 | 2024-10-19 02:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 144.6 |
| d283f9ef-ba9e-3d36-93bb-a5a8655095cb | -3.7019 | -45.7212 | 2024-10-19 02:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 279.5 |
| 6cd9b8e7-f011-35ba-a4bc-aebd8641cf4e | -3.702 | -45.6988 | 2024-10-19 02:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 205.7 |
| e04187be-0320-3ac6-a902-e92b099a81ad | -9.0344 | -67.4641 | 2024-10-19 02:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 3b308cfd-fe30-3f7e-a086-329307e0d1e7 | -9.0345 | -67.4455 | 2024-10-19 02:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 68d76652-68af-353e-b5cf-09ca70b39794 | -9.053 | -67.4636 | 2024-10-19 02:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 062d5d77-3299-31cc-aa4c-0fe133960b2e | -9.053 | -67.4451 | 2024-10-19 02:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 2d67ab5f-2915-3fd5-99c5-d2d927b053bc | -12.004 | -63.5199 | 2024-10-19 02:26:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 730be342-23c5-38bc-bf79-e0c74d1a77a1 | -12.0228 | -63.5189 | 2024-10-19 02:26:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 0973ae76-012d-340a-93c4-28361acf00bd | -12.023 | -63.4998 | 2024-10-19 02:26:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| e668a552-a02b-36e5-b113-acc67ec6c2d0 | -12.5147 | -63.3014 | 2024-10-19 02:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.3 |
| ed0c0133-a464-393d-83b5-c0d0f24c18e0 | -12.5149 | -63.2822 | 2024-10-19 02:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 157c5da3-3c09-3f11-9fc0-7a9d2a3f4d68 | -18.9959 | -43.1304 | 2024-10-19 02:26:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.8 |
| 3dc8c464-2de0-3f4a-abf1-9aad99eaff7b | -21.9662 | -49.7186 | 2024-10-19 02:27:07 | GOES-16 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.3 |
| 52cccc16-0a27-324d-8fc5-b36a4a674d38 | -2.9673 | -52.9169 | 2024-10-19 02:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| ff99dfdd-1c1e-3a1b-b8c6-537a2f1f9d35 | -2.9489 | -52.897 | 2024-10-19 02:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 42d5e0cd-1b76-32fe-ab49-b2687332a1fb | -2.9489 | -52.9174 | 2024-10-19 02:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 6b0c52f7-27f8-3924-90c3-566f2ddcad8d | -3.4387 | -50.2158 | 2024-10-19 02:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 69d4bf4d-44c6-3b6b-ac80-6659b8572962 | -3.4202 | -50.2164 | 2024-10-19 02:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| c436a8bc-a477-3674-93c5-b0f9f8495b08 | -3.6833 | -45.722 | 2024-10-19 02:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 79860a85-66ca-3e75-8d82-14ed0f4e5bd7 | -3.7019 | -45.7212 | 2024-10-19 02:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 9df07710-d1b4-328f-8bed-3bc68f5844ca | -3.702 | -45.6988 | 2024-10-19 02:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 81.2 |
| bfe1f8e6-7060-3c99-9f06-b81d174813d9 | -5.5716 | -44.8927 | 2024-10-19 02:35:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| cc39efbb-bb04-3a70-8599-cc3c78f87c58 | -9.0344 | -67.4826 | 2024-10-19 02:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 4546e5a8-1385-3275-8746-337689b3edd4 | -9.0344 | -67.4641 | 2024-10-19 02:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 233.0 |
| ae207ff1-7ea4-3103-80fe-bd93f4e098ec | -9.0345 | -67.4455 | 2024-10-19 02:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 169.0 |
| e54295ef-a4f1-3fe3-a4b1-6b07a4efd9ae | -9.053 | -67.4636 | 2024-10-19 02:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 106.4 |
| d80a3f85-091e-3487-9d42-f9cd18052fe6 | -9.053 | -67.4451 | 2024-10-19 02:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 08007e3e-78e8-38fc-afdd-b7e009535fc4 | -12.5147 | -63.3014 | 2024-10-19 02:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 82.8 |
| f0d26cee-1644-377e-b816-bbdbfd1834cd | -12.5149 | -63.2822 | 2024-10-19 02:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 542c0134-febf-352a-a041-661c31fb0258 | -12.5338 | -63.2812 | 2024-10-19 02:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 0ec2a49f-bdcd-3ce8-b0e0-ffbbc1f924ed | -12.5336 | -63.3003 | 2024-10-19 02:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| fcfef5e6-601e-327c-9421-7072e93c7b94 | 5.0513 | -60.1319 | 2024-10-19 02:44:37 | GOES-16 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 30.2 |
| f432254e-f3c6-31d2-9f1c-4e692d14898e | -2.7007 | -45.1763 | 2024-10-19 02:45:21 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 8143716e-b5ad-3745-a148-1ef541de1637 | -2.9489 | -52.9174 | 2024-10-19 02:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 5da623a5-5319-351f-afa1-76b9af997f4f | -2.9489 | -52.897 | 2024-10-19 02:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| b917219e-1f5e-334f-980d-03cbb71cf0ab | -2.9673 | -52.9169 | 2024-10-19 02:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 71bd6144-c352-3b26-975d-10d6664dc1ef | -3.4202 | -50.2164 | 2024-10-19 02:45:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 87bebc1d-91b7-3837-adf9-7fb65a4067d3 | -3.4387 | -50.2158 | 2024-10-19 02:45:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| b45ce9a9-ffcd-344f-b546-0add480fa203 | -4.6873 | -45.8504 | 2024-10-19 02:45:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 52.8 |
| e051dae1-061f-31b7-9511-9d8b4454b8dd | -4.6875 | -45.828 | 2024-10-19 02:45:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 48.7 |
| c695e739-8264-3c7c-bcbd-0ad336bea1c9 | -4.706 | -45.8493 | 2024-10-19 02:45:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 1088bdaf-1d3a-379a-a887-0bee171bb6d6 | -4.7061 | -45.8269 | 2024-10-19 02:45:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 80.0 |
| ceb9df01-502f-32db-bd1b-dde82041165a | -9.0344 | -67.4641 | 2024-10-19 02:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 208.1 |
| 44f7789c-f275-3e41-ac9c-7dcd14494588 | -9.0345 | -67.4455 | 2024-10-19 02:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 123.6 |
| d9ff77f1-3c15-3ac0-87e5-b0fa63c70e81 | -9.053 | -67.4636 | 2024-10-19 02:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 951ec833-eb7d-3843-a7cd-bb97be5c7b6f | -9.053 | -67.4451 | 2024-10-19 02:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 71208dc3-21c2-3aa4-8bd7-8041b43447b4 | -1.1348 | -49.0421 | 2024-10-19 02:55:12 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 50812f44-2ae3-3b0d-8c8d-b432c078480a | -2.7007 | -45.1763 | 2024-10-19 02:55:21 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 7549482c-5192-3ab9-86ed-8fabe3f14e92 | -2.9489 | -52.9174 | 2024-10-19 02:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |


[Clique aqui para ver as próximas entradas](README12.md)
