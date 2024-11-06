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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13ef3736-577e-315c-bbc6-970c1b4a2eca | -3.0207 | -53.443 | 2024-11-06 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 21ee7ef7-26ed-3bae-8de0-7b221a08a57f | -3.2164 | -50.3701 | 2024-11-06 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| e1df2db4-af59-3354-9412-87933c3cc4ed | -1.2922 | -54.5585 | 2024-11-06 03:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 1f8a485a-3737-38ff-aec2-5d7ea34a2b39 | -6.4906 | -44.6862 | 2024-11-06 03:30:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 94c63141-4543-3d8f-9c19-c428d6ebb6ec | -3.5446 | -47.3855 | 2024-11-06 03:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 187.0 |
| 5f3846f8-4226-32d5-aee3-8e11c8bb1dec | -6.5014 | -47.4813 | 2024-11-06 03:30:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 40e8f8a0-750f-3f80-a9a6-dab75892c962 | -6.4827 | -47.4827 | 2024-11-06 03:30:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| ab1b4706-27bc-3458-8def-bb89e725a8ac | -2.937 | -51.0673 | 2024-11-06 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 42360bb5-e730-3cfe-bf6d-435ea731042b | -4.1432 | -43.5822 | 2024-11-06 03:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 224.2 |
| c471c566-7d31-3be7-9b72-c8eb9eb5b4e3 | -6.1226 | -43.9809 | 2024-11-06 03:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| e912ebe5-c847-3531-bf2b-1cbe5f60944c | -2.4457 | -49.039 | 2024-11-06 03:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 05ea50ad-a698-39ca-ba7e-80cc3e09cea5 | -2.8423 | -51.7942 | 2024-11-06 03:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 820d1688-f014-3360-9f72-f6dc22f19f66 | -2.7243 | -54.1552 | 2024-11-06 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 032632b8-7b2f-3af7-b747-d10a06ba26fa | -4.1434 | -43.5591 | 2024-11-06 03:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 79a800c5-4927-3382-a4d7-3581222485ac | -4.5614 | -48.0141 | 2024-11-06 03:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 1be5617c-c4cf-3b21-b82f-11cf9a589a56 | -3.5444 | -47.4073 | 2024-11-06 03:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| a6c6e92f-0512-3b98-8f47-1e6a7a43bb0d | -3.0396 | -53.2805 | 2024-11-06 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| ce90718d-bddb-3623-b66c-7d0f19175944 | -6.5012 | -47.5033 | 2024-11-06 03:30:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| b7b171cd-dd60-3b42-a10f-8950a783de8f | -6.4825 | -47.5046 | 2024-11-06 03:30:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 2499b8ac-b6a9-3383-ae5c-ba47d886373e | -3.2349 | -50.3695 | 2024-11-06 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 01ad5f4c-6d54-3a94-91eb-d21c135f0d8b | -6.1041 | -43.9593 | 2024-11-06 03:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| e2162c3e-84b7-3b19-ac07-72e169034177 | -3.0397 | -53.2603 | 2024-11-06 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| a2661507-4b5d-3ec0-ba46-179cd51aa315 | -2.6764 | -51.8189 | 2024-11-06 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 57414d6e-2826-30ab-b5ec-f9186cc660e5 | -3.1213 | -51.1036 | 2024-11-06 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| ada37415-7e91-3fe2-9fe8-b09ce6455bd3 | -3.526 | -47.3862 | 2024-11-06 03:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 0832f3a0-ed60-39d4-a313-765d21c805f6 | -2.8424 | -51.7529 | 2024-11-06 03:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 2d1084f0-3da4-3043-9572-0b91d75aaf2b | -4.1244 | -43.6064 | 2024-11-06 03:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 94ad4e59-e601-3bf9-b9f7-33145ae1eccb | -2.7244 | -54.1351 | 2024-11-06 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 991a17d1-65ae-32a7-ae30-ac92f1664ec7 | -3.1616 | -50.2248 | 2024-11-06 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| cefac9a6-c7d2-3507-a6b3-02148ac83ecc | -4.1246 | -43.5833 | 2024-11-06 03:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 209.6 |
| 0a451821-0f77-3288-bfff-3caded23f7a7 | -2.8423 | -51.7735 | 2024-11-06 03:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 2babeb3f-870a-3931-a2a7-40bd3476861f | -3.2163 | -50.391 | 2024-11-06 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 15dd353f-23d0-34a2-a335-5af1b1471580 | -2.8608 | -51.7731 | 2024-11-06 03:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 55054038-29ad-3769-ad24-c65e3c950218 | -4.1247 | -43.5601 | 2024-11-06 03:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| e238d127-6db9-36cd-9ca1-5ead3c2cc341 | -3.0023 | -53.4232 | 2024-11-06 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| d2d13375-aa2d-3c09-9439-2f3c3ca9d6bf | -2.9371 | -51.0465 | 2024-11-06 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 906a2138-8ce9-32d3-a541-4ea6c72f6ddf | 3.6184 | -51.3162 | 2024-11-06 03:30:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 39.5 |
| b43ff057-6201-33a3-8aa6-634d64ba5845 | -3.0207 | -53.4227 | 2024-11-06 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 742be08e-62d1-35ba-b01b-8e811f06a6df | -3.1617 | -50.2038 | 2024-11-06 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 08346fdb-70c0-39e3-a0fd-733a2920fbad | -2.8065 | -51.4855 | 2024-11-06 03:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| cddb50a1-d346-3c41-a530-49369548946f | 3.6 | -51.3168 | 2024-11-06 03:30:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 31dff6c3-d41d-3517-bf7c-db3ffaa8b92d | -2.9185 | -51.0678 | 2024-11-06 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 0d244a90-541f-373f-83e7-476a6718e48f | -3.2348 | -50.3904 | 2024-11-06 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 68b60338-6e7b-35b0-8546-74d79b54f5b5 | -2.8608 | -51.7524 | 2024-11-06 03:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 735a55fb-e2d5-31f0-87cd-9a149d336cc2 | -3.967 | -48.15 | 2024-11-06 03:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| e1a57caf-acfb-3d84-8d83-3466918f43c8 | -2.9186 | -51.047 | 2024-11-06 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| dc5acf8d-823e-3dbb-a95d-2a8e3b1cdda5 | -6.5094 | -44.6847 | 2024-11-06 03:30:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 9d6c1488-2891-3d4e-bb38-66d6c6ab4721 | -6.1039 | -43.9824 | 2024-11-06 03:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 05bfdcae-5c99-3f22-9a34-b0c95c6a01ed | -1.2922 | -54.5585 | 2024-11-06 03:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 6e06aee2-48ff-32de-96d2-18d0cce46da0 | 3.6184 | -51.3162 | 2024-11-06 03:40:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 51.3 |
| d0631bc0-1791-3fc9-a1b6-9df17b7832e1 | -3.0207 | -53.4227 | 2024-11-06 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| fc5240f3-8c92-3dc6-bed3-5353f23e4d9c | -6.4825 | -47.5046 | 2024-11-06 03:40:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 41ec5505-dbff-3bbe-8508-6dc5e1d501fb | -2.8423 | -51.7735 | 2024-11-06 03:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| a2e9b947-7e70-32ef-ac21-a30d2c701378 | -3.0207 | -53.443 | 2024-11-06 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 39965279-3396-3bf7-a20f-06e8c38437f8 | -6.1226 | -43.9809 | 2024-11-06 03:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 8525b003-e74a-3848-96d0-0441a2399e50 | -2.8506 | -49.4744 | 2024-11-06 03:40:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 7feddaf0-db67-38ed-9f2b-2fa079a359fd | -3.0397 | -53.2603 | 2024-11-06 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 7cc335dc-c3ec-3b95-802e-1ec5fbc08579 | -6.5094 | -44.6847 | 2024-11-06 03:40:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 39e5cd99-4998-3aeb-a1e1-9140ff32895d | -2.9371 | -51.0465 | 2024-11-06 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 2da7feab-b993-3566-8a37-f6f4669c3001 | -6.5014 | -47.4813 | 2024-11-06 03:40:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 124.2 |
| ab19c377-1b69-36f2-b863-d137444e8e22 | -3.1617 | -50.2038 | 2024-11-06 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 1846e3e5-bd44-39fd-a81d-58904cfd277d | -3.526 | -47.3862 | 2024-11-06 03:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 5df1dd03-b211-3865-b314-c3ff16d1b043 | -2.7243 | -54.1552 | 2024-11-06 03:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 8c384486-3c32-3d3e-8a8b-8bd7b0cef40e | -3.2348 | -50.3904 | 2024-11-06 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| c61b2002-88c2-37bc-93de-070f9319f18e | -6.5096 | -44.6618 | 2024-11-06 03:40:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 4948644e-84b4-3fb4-8c56-d67dd9a6de38 | -3.0396 | -53.2805 | 2024-11-06 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 0aaccb7e-00bf-3c52-8b9d-fb5062e7a946 | -2.7244 | -54.1351 | 2024-11-06 03:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 5d14233c-2539-3d1f-a350-8458f806db31 | -2.8423 | -51.7942 | 2024-11-06 03:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| d2f0a7aa-a80d-3d25-8178-3e325ca6b6ae | -3.2349 | -50.3695 | 2024-11-06 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| ee5f5634-ec29-37ec-a23d-bde89e0e479a | -2.8607 | -51.7937 | 2024-11-06 03:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 2a6c7571-ea17-3f4d-88ff-637490bc90fb | -3.5631 | -47.3847 | 2024-11-06 03:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 60d4dbf3-6683-3d22-9e9a-440de58a6e31 | -4.5614 | -48.0141 | 2024-11-06 03:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 268d5945-dab1-39cf-a190-293cb487172a | -6.4827 | -47.4827 | 2024-11-06 03:40:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 260749e5-30b1-3520-8ced-4bbc161cd80e | -3.2164 | -50.3701 | 2024-11-06 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| fc0d428f-acfd-357b-8a14-052a4b85d91c | -4.1246 | -43.5833 | 2024-11-06 03:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 201.8 |
| 4c9b002e-690f-340a-8147-4901cc0da757 | -4.1247 | -43.5601 | 2024-11-06 03:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| c3170330-ba21-3a09-9391-e9195835d1ab | -2.6764 | -51.8189 | 2024-11-06 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| c86e02e7-bcda-37a8-9256-a1381dd5be2d | -3.0023 | -53.4434 | 2024-11-06 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| bc26f3cc-e08c-39df-814c-44ea169d3b8f | -2.9186 | -51.047 | 2024-11-06 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 4499d95d-78a5-3eed-9fed-9aa0f6939197 | -3.2163 | -50.391 | 2024-11-06 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 7f6f78da-d6a0-3a29-bd92-2f852d58e7e5 | -2.9187 | -51.0262 | 2024-11-06 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| afc5c21f-5d2a-3482-bdc7-2a97ec1d0032 | -4.1432 | -43.5822 | 2024-11-06 03:40:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 149.1 |
| c7ea733a-08f3-35ac-b790-1a4f55e53035 | -6.1041 | -43.9593 | 2024-11-06 03:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| e0235cf3-a832-3d44-9964-a346804e25e0 | -3.5446 | -47.3855 | 2024-11-06 03:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 204.3 |
| 1e037438-da0e-3476-b904-782e1a7a3dd1 | -6.4906 | -44.6862 | 2024-11-06 03:40:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| ff2061d7-f2c8-3831-a314-3beee0301338 | -0.3952 | -51.9947 | 2024-11-06 03:40:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 58.0 |
| dce9c250-a952-3e38-afe4-798386148ac1 | -6.5012 | -47.5033 | 2024-11-06 03:40:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 44e37735-6baf-3020-a3d3-14df572c5dbf | -2.937 | -51.0673 | 2024-11-06 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 9fe3ddf3-b75a-3773-a885-f092a59399da | -2.6764 | -51.8395 | 2024-11-06 03:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| ca7415da-277b-3255-99de-9fa972ecb02c | -3.967 | -48.15 | 2024-11-06 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 42a5e246-28ad-3166-a874-166d35f75284 | -3.5447 | -47.3636 | 2024-11-06 03:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 3df70e67-dad3-39a9-a3ca-1172423c1c29 | -2.8608 | -51.7731 | 2024-11-06 03:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 153.7 |
| f5c9b8c1-c3ca-3462-8f47-e276775482fa | -3.0023 | -53.4232 | 2024-11-06 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 21cddc3f-35e3-3500-9643-74b0ab3d0669 | -6.1229 | -43.9578 | 2024-11-06 03:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 959555b8-88cb-3523-a372-421eba60bfa7 | -3.1616 | -50.2248 | 2024-11-06 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 80b03dd9-0bc4-3e8f-a322-07829d28999e | -3.60679 | -42.86126 | 2024-11-06 03:46:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 889053e5-f7a5-32cf-abad-1769ec39f514 | -2.65587 | -48.56609 | 2024-11-06 03:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c53e2340-12d0-3ebf-8759-6f4013e056fa | -3.71629 | -41.68607 | 2024-11-06 03:46:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 87e0e671-71fe-33f6-bc5a-1751129a01ba | -3.60906 | -42.86219 | 2024-11-06 03:46:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99510af8-5f75-3a7c-8cdc-5621a7134f1d | -3.31857 | -40.0349 | 2024-11-06 03:46:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README23.md)
