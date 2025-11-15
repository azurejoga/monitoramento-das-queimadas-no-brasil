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
| 7d2c65df-dc13-378d-87af-f62b9df7f39a | -5.2397 | -44.3448 | 2025-11-15 02:20:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 204.1 |
| 5d2a2d7b-b0bb-3c6f-ac86-3eba7ce70a17 | -4.5381 | -43.2107 | 2025-11-15 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 9578b34c-46f4-39c1-9c65-b0b058ac096f | -5.2396 | -44.3677 | 2025-11-15 02:20:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| d5e5eedb-5b26-3776-b03d-0f57f8990527 | -4.5568 | -43.2096 | 2025-11-15 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 17275ef6-1101-3d14-885f-1bd3827936bf | -2.5053 | -47.812 | 2025-11-15 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 03ad022a-00fd-3859-9c46-3b2b3bac0985 | -2.5238 | -47.8115 | 2025-11-15 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| dc7afa01-dcdb-329d-9a80-d37be16863a5 | -11.849 | -49.2 | 2025-11-15 02:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 9a896ae3-b546-35d3-9a72-ec67b64d8ef9 | -4.5381 | -43.2107 | 2025-11-15 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 6efa5e84-06b8-3928-a4eb-1878c42adfef | -11.849 | -49.2 | 2025-11-15 02:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 0e52ca0c-1f9b-3fea-92b0-a0a9f992abc6 | -2.5053 | -47.812 | 2025-11-15 02:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 2e609129-3b74-3b47-8131-98e858c9ff33 | -11.8486 | -49.2218 | 2025-11-15 02:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 153.4 |
| c66cc9a5-057c-3669-8694-02d4fb9045f8 | -12.6745 | -46.7605 | 2025-11-15 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 993994ec-b604-3ff9-904e-890056ee0e41 | -4.538 | -43.2341 | 2025-11-15 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 134e74cd-ab89-379d-af73-fbf7f7282ae6 | -4.5568 | -43.2096 | 2025-11-15 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 0aaa443b-3ff4-3d00-aff4-0dda085c8f3e | -11.8295 | -49.2242 | 2025-11-15 02:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| d5985722-cf57-38a0-90d3-72df6278c0c0 | -5.221 | -44.346 | 2025-11-15 02:30:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 30c7efc0-62d0-39f4-ae87-2f84823d24eb | -5.2397 | -44.3448 | 2025-11-15 02:30:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 177.1 |
| b934e445-af5c-3025-92e8-04af165c8178 | -12.6741 | -46.7831 | 2025-11-15 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 97ca9c66-eeda-3989-9ffd-777d55191813 | -5.2396 | -44.3677 | 2025-11-15 02:30:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| aca6a3c1-2d63-3cc8-9c93-f0b35c91c24f | -2.5238 | -47.8115 | 2025-11-15 02:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 9649e3b2-21ad-3925-8db9-aefa0057b5d0 | -5.2397 | -44.3448 | 2025-11-15 02:40:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 8f95bf04-c631-30ff-be31-f5a385248792 | -4.5568 | -43.2096 | 2025-11-15 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 7a4e4169-9594-31a4-b8ca-ad3e8a24c824 | -11.8486 | -49.2218 | 2025-11-15 02:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 156.8 |
| e477bcc7-fa4f-3962-8d95-770520b6e0bc | -2.5238 | -47.8115 | 2025-11-15 02:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| eb50ad9c-1544-3299-b83a-d584993c11bf | -11.849 | -49.2 | 2025-11-15 02:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| d0553af5-9cc3-3930-9c85-a765d1fc3bed | -5.2396 | -44.3677 | 2025-11-15 02:40:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| ccaddad2-5f00-3ffa-a21c-c0be03eaae44 | -4.5567 | -43.2329 | 2025-11-15 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| eae22796-cd56-3d90-9137-30b47d5b0ea7 | -12.6745 | -46.7605 | 2025-11-15 02:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 254f6c5a-309f-3067-818c-f3394e65f166 | -2.5053 | -47.812 | 2025-11-15 02:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| dfe5feb2-706c-3b5e-9755-91ee42557dac | -4.5381 | -43.2107 | 2025-11-15 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 742c5bfd-6e24-3be5-9b11-17d7d51262d5 | -4.538 | -43.2341 | 2025-11-15 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 4062b7b8-4730-34c7-884e-3e59c0872b71 | -11.8295 | -49.2242 | 2025-11-15 02:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 3c101242-4b2d-3d76-9695-e5870ee1b27c | -4.5568 | -43.2096 | 2025-11-15 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 067c0574-c130-36ad-896d-cf4142ce9ab9 | -5.2396 | -44.3677 | 2025-11-15 02:50:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| d63046b1-0b57-3516-b181-eb19d7d15167 | -2.5053 | -47.812 | 2025-11-15 02:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| e126f80e-8ea6-3716-bfba-bc3c7b369c01 | -4.538 | -43.2341 | 2025-11-15 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 162631f3-6f0c-3003-840e-3f9e7728e0f7 | -11.8486 | -49.2218 | 2025-11-15 02:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 6bcf2c98-cd6f-3cbc-9676-da4b23c222a8 | -11.849 | -49.2 | 2025-11-15 02:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 4cad37e3-6e49-3276-9aa6-27e81c8363bf | -4.5381 | -43.2107 | 2025-11-15 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 55854306-5dfe-374d-bca3-ce4233208868 | -2.5238 | -47.8115 | 2025-11-15 02:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 70af0676-ca48-35e5-9311-51e8c797095e | -5.2397 | -44.3448 | 2025-11-15 02:50:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 72b5b9e3-9896-3d8f-ada3-b439d8676fea | -5.221 | -44.346 | 2025-11-15 02:50:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 7800dddf-3736-33c0-86bd-6f3ff92abbe4 | -11.8486 | -49.2218 | 2025-11-15 03:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 148.8 |
| af98f148-9424-39ec-899d-01f3fdc1396f | -11.849 | -49.2 | 2025-11-15 03:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 01d123ad-b239-37c2-9d29-624882a233a0 | -4.538 | -43.2341 | 2025-11-15 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 9ed75e3f-3a32-372d-a992-55c8a34cfbad | -4.5381 | -43.2107 | 2025-11-15 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 4a60eaf2-5dbe-3b9f-8e40-6b241ffd5ebd | -2.5238 | -47.8115 | 2025-11-15 03:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| cf75f17a-4372-3d6d-8a2b-a063ca5f9702 | -5.2397 | -44.3448 | 2025-11-15 03:00:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 966351a2-25e2-386c-8358-b77c06e83078 | -5.2396 | -44.3677 | 2025-11-15 03:00:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 3358b154-2f8c-3a44-8062-0cf619fe0dcd | -4.5568 | -43.2096 | 2025-11-15 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 51ab9e21-41fe-3435-ae9f-b0284f4dbb7c | -5.2397 | -44.3448 | 2025-11-15 03:10:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 69c5ccfc-8e86-3237-b173-496f48b109e3 | -4.538 | -43.2341 | 2025-11-15 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 60e6a1bf-e25b-315e-9f45-863929ffe58d | -11.849 | -49.2 | 2025-11-15 03:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| d965d123-ff93-39c3-ae8d-a2d453b1e773 | -5.2396 | -44.3677 | 2025-11-15 03:10:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 7f44f9dc-b8d3-30f3-ba28-5707d5a1623b | -2.5053 | -47.812 | 2025-11-15 03:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| d45a236a-04e2-3a85-8a4a-5b39c591becb | -4.5381 | -43.2107 | 2025-11-15 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 19f83aea-7b8f-3b03-8254-dc8719585efb | -11.8486 | -49.2218 | 2025-11-15 03:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 34fdf57f-0b75-30de-9366-3ec937cc3c4b | -2.5238 | -47.8115 | 2025-11-15 03:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 94cdae52-56cd-3daa-b596-e5a3b645884f | -11.849 | -49.2 | 2025-11-15 03:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 46cac48a-0cf5-3595-9092-a7d08ac56541 | -15.2329 | -49.4021 | 2025-11-15 03:20:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 5db771b6-1ac8-36ac-8816-e847c6350cfe | -5.2396 | -44.3677 | 2025-11-15 03:20:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| a6ea106f-0f78-33f1-baa2-6449c8222544 | -15.2524 | -49.399 | 2025-11-15 03:20:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 75330fac-2952-35ff-adcd-d8e5bc971864 | -2.5238 | -47.8115 | 2025-11-15 03:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 976ed29b-545f-3fc5-92bd-e84df899cd5b | -11.8486 | -49.2218 | 2025-11-15 03:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 58fe7cd5-f46c-38bf-ab72-7707ea5806b7 | -4.538 | -43.2341 | 2025-11-15 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 774c471a-cc3b-38d1-92a3-e18298874ca7 | -4.5381 | -43.2107 | 2025-11-15 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 5169c5e2-1ec8-3af4-b973-aaa766bc516d | -5.2397 | -44.3448 | 2025-11-15 03:20:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| dba7db35-0635-3b2c-9275-7e73232c4ae2 | -5.2397 | -44.3448 | 2025-11-15 03:30:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 01c6f59d-6976-3228-a4e8-602f481015ff | -4.538 | -43.2341 | 2025-11-15 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| fde5f825-0cb3-39ea-93ae-d94c3d3656c8 | -4.5381 | -43.2107 | 2025-11-15 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 47a807d5-ee90-3e54-b040-bdf526ca62d5 | -11.8486 | -49.2218 | 2025-11-15 03:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 86cc767f-d781-3222-a3bd-293a582df172 | -2.5238 | -47.8115 | 2025-11-15 03:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| cb9def13-0871-375c-8089-b441ea26cb5d | -11.849 | -49.2 | 2025-11-15 03:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 8d47053b-9f78-3733-ac0e-007bd8b740c4 | -4.98515 | -43.88912 | 2025-11-15 03:34:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cfe695fb-1e9e-33c8-a46d-50e438a70b29 | -5.51624 | -40.97916 | 2025-11-15 03:34:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| af2a345c-3458-37b2-9e1b-59b1cac9e173 | -4.8054 | -41.61304 | 2025-11-15 03:34:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b20209f3-80d3-3023-9720-75607113fc62 | -3.47861 | -45.65038 | 2025-11-15 03:34:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f5dd68d-baa6-3fc5-8af1-0e794955afcb | -4.3932 | -44.07899 | 2025-11-15 03:34:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b284d067-d998-3aa5-9020-4b8a097cbdba | -4.91408 | -38.68724 | 2025-11-15 03:34:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| eab606e1-665b-3a11-9672-5979fecca2a9 | -3.37903 | -41.16139 | 2025-11-15 03:34:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| efdf1a17-4459-3d60-aa70-5ea28aeb8012 | -4.46369 | -45.65047 | 2025-11-15 03:34:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06b08969-e2b4-3976-8975-0da50f7b05ba | -2.74158 | -45.29659 | 2025-11-15 03:34:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2f604b79-eb9f-35cf-8b95-25d0e51be25b | -5.48362 | -40.96725 | 2025-11-15 03:34:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d562e1e9-9ed0-3915-9952-dfb02d68c1eb | -4.85621 | -43.25497 | 2025-11-15 03:34:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d8ee3dfb-2430-3619-8da5-a1c0c7752410 | -3.65963 | -44.81464 | 2025-11-15 03:34:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 787fa2e3-9488-3767-845a-1cffe040e957 | -4.44101 | -43.65739 | 2025-11-15 03:34:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48c4efc8-05b9-326d-8e0a-f381d349109b | -3.98931 | -44.26369 | 2025-11-15 03:34:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12bfb166-aca5-33a2-926a-9878370f1e4e | -3.47621 | -45.64849 | 2025-11-15 03:34:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b352477-3615-333a-ad45-41d6fe9bc399 | -4.85816 | -43.2588 | 2025-11-15 03:34:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 174e3df3-e35e-3b14-89eb-bb3633a7c6c8 | -4.68061 | -45.85082 | 2025-11-15 03:34:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f3e1a0b7-c45d-33c2-b0ac-f97f13432b1f | -4.89736 | -44.05307 | 2025-11-15 03:34:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 216f1dd3-f840-3b20-8c99-a214386a3252 | -4.68602 | -45.85908 | 2025-11-15 03:34:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 116f8331-4a83-3bcd-a25b-af2921670342 | -3.37854 | -41.16437 | 2025-11-15 03:34:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6643cdfb-75f8-3579-bebc-a8297ea1b076 | -2.74057 | -45.30249 | 2025-11-15 03:34:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5a6e66af-a363-3933-8c9c-adb5fac3da55 | -5.9354 | -35.2914 | 2025-11-15 03:34:00 | NOAA-21 | PARNAMIRIM | RIO GRANDE DO NORTE | Brasil | 2403251 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9aa929ec-61b0-35a7-a992-09622ddbcc7d | -4.90333 | -44.05408 | 2025-11-15 03:34:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1bec4507-84c3-305c-9b6e-fa3630f87672 | -3.22208 | -45.48518 | 2025-11-15 03:34:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1a11edb5-6797-36c1-b4df-dd85e94774f9 | -3.90636 | -45.80407 | 2025-11-15 03:34:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ed78cfb-116d-3867-b6bc-b02dd0e6bb61 | -4.97927 | -43.88803 | 2025-11-15 03:34:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19a50258-e671-368e-88c4-ad6eb56e7de7 | -5.42803 | -40.66222 | 2025-11-15 03:34:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |


[Clique aqui para ver as próximas entradas](README12.md)
