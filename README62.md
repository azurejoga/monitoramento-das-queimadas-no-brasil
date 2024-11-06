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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 180a2990-810e-3df2-807e-861e2d46138b | -2.84286 | -52.90152 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| e08580e5-1432-35f6-a9b9-54e09ea3211e | -3.15052 | -51.32449 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31d87d74-0e97-34e7-8475-da1bd3583718 | -3.24463 | -53.40478 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 568fb310-4290-340d-8958-43eacb8d09b5 | -3.65692 | -52.33863 | 2024-11-06 05:31:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec3cea55-1c6f-307d-adab-7a3242f414df | -2.95182 | -54.79722 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f6ca9ca4-b02e-3f85-8cb7-13a8707bc83d | -3.67231 | -50.23304 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2a14d5c8-8049-3a6b-8a7e-51e511fc0bbc | -4.19263 | -51.02123 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f1f83591-68de-3cc9-b3c4-b2c66ee764d6 | -1.57263 | -60.35821 | 2024-11-06 05:31:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 877079bf-c659-3729-b213-96f82953252f | -2.99838 | -53.8531 | 2024-11-06 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a6bbc50-4cb7-3a15-886f-cfbd6a5625a3 | -2.79975 | -51.48758 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 843be298-78ee-30fd-ae7c-abd9d67545a3 | -11.77094 | -64.98074 | 2024-11-06 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 517b11a9-8d13-3b7b-8132-2e59f7b8c2e7 | -9.60159 | -49.53864 | 2024-11-06 05:31:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b56c777e-2fc6-3def-9c1d-3eb61c722942 | -3.01068 | -51.39082 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b3c2a69-eb94-33b2-848e-b4f261affcc1 | -2.8715 | -51.39289 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ef2f3b5-4ad7-373f-b260-b937901e3382 | -2.81045 | -51.49294 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8eb82f80-87fa-38ee-b4f1-2137a8a7ee51 | -3.59761 | -51.57414 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e716823e-d567-382f-af05-734e15d47ac9 | -2.81613 | -52.94067 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e3e97461-90a9-3584-828a-8fa645da5ed9 | -3.21759 | -53.10012 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad0f3f0f-dd92-38a7-9b85-2c01c00f9b51 | -1.49246 | -60.3707 | 2024-11-06 05:31:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ef592f9-c33a-314f-bff4-5e5d05add696 | -3.2353 | -53.39904 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7b0319bf-ac9c-3de5-9947-d6b5a6175e4d | -2.83543 | -52.91623 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86366910-3db5-3d69-bbc3-0a18c0acd177 | -3.53828 | -50.29604 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c0e3b12-3a39-3848-af0c-6ce69599dac7 | -3.111 | -51.10602 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28f4afaa-19b2-3d0d-969b-dac76844a525 | -3.73966 | -50.06902 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0a03db3-11bf-3146-a7eb-66e41be4ffb6 | -4.36216 | -48.6516 | 2024-11-06 05:31:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d138e293-835b-3795-bc41-85e7c4c1a382 | -2.8467 | -51.78178 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c51ae7ae-3036-3729-819e-74e282eb0f30 | -3.76244 | -51.77067 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a85aee0-ad69-37e7-a810-5989d66c0aca | -3.80545 | -52.35769 | 2024-11-06 05:31:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f59bd4b-4e01-36b7-955d-8959d08bac4a | -3.17983 | -50.60001 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d74829b7-2fb1-36e0-97eb-a12bcd0176db | -9.45778 | -66.63905 | 2024-11-06 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cef05289-02a5-34b6-9402-84cf9a84c92f | -3.02813 | -54.0862 | 2024-11-06 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b04b0fc-5d2e-3d4b-9ed7-4b50702230ac | -3.21462 | -49.22792 | 2024-11-06 05:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38bf820c-7803-3164-952c-8dc5e7eefbb3 | -4.36211 | -48.64656 | 2024-11-06 05:31:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6bd37ba0-0e9b-3c79-ab8a-d348bb390e3c | -11.79319 | -64.84175 | 2024-11-06 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7af7f6d4-9ad9-36bd-a9d3-b893ee1c4438 | -3.72816 | -53.3901 | 2024-11-06 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 317ee6b3-f355-36b0-ae0f-e95d2786023d | -2.87472 | -51.30853 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42f75d66-6b9a-325d-82af-e364a400d4c6 | -3.0858 | -50.95363 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 41bbb8fe-204e-3b3e-ac19-42ced054670f | -2.9388 | -51.06353 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c39e57de-60e3-33c9-ace5-fdc3308eb6aa | -2.93363 | -51.05856 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a87464fa-1c25-3756-b9e3-f36525c3bff6 | -3.27591 | -51.27997 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bbb86e8-1db1-3e43-9e20-15f687c26b72 | -3.04284 | -53.27773 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f61cae6-4224-3a6f-99ed-7444f347a596 | -3.03911 | -53.26821 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fc6e9a15-dc4c-361f-8ad2-c1e7fccb5144 | -10.53226 | -67.78544 | 2024-11-06 05:31:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ffbc06a-bb5b-33e0-935b-9f4323c03907 | -2.84332 | -52.89847 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30e7699f-f584-34ed-8e66-325fb2a7fd46 | -3.12826 | -51.11195 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e6e549d7-4126-3ba4-b7d5-212549ed0d78 | -1.34 | -54.6147 | 2024-11-06 05:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ce9cc76-a85b-3718-97a5-2a676c0f5f78 | -2.85328 | -51.77531 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 52f6e95f-3eb9-3c41-8af0-f9852af0c5ec | -3.67913 | -50.22934 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 488fb848-d6b1-3384-9331-70ad6cf9985f | -2.82259 | -52.93233 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c75369e1-fb16-36dd-b1c0-a40b747b41e2 | -3.2197 | -50.37856 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 97f3c0a1-3944-38d3-b3b8-04658bd62298 | -2.99358 | -53.85242 | 2024-11-06 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5dfa346b-64ed-3e71-b62b-66cf50588c4f | -2.81509 | -52.91257 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ff109143-125a-3956-959a-72c393fbe3fd | -3.04242 | -53.28062 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 842ece50-330b-3c10-ab3e-a0d227100803 | -4.36126 | -48.65241 | 2024-11-06 05:31:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1aa76120-fc95-3238-b62e-df6efe86646a | -2.78158 | -51.61137 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf87ace3-ad90-3007-8076-d51f7e582d49 | -3.05885 | -52.49979 | 2024-11-06 05:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cf821026-da44-3c18-8294-ff33b18ce687 | -2.7992 | -51.49134 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5d2b7644-94a7-3656-934b-1b4eac43292e | -12.07264 | -63.15343 | 2024-11-06 05:31:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0213715-72f4-3025-b8ef-f04e550bf02c | -3.09697 | -53.71471 | 2024-11-06 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 531b6254-c537-3d3c-8576-f4395552fff7 | -3.2245 | -50.381 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| c1386996-739f-3d38-9073-fe9e073bca72 | -2.87289 | -51.30626 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c83b7d81-b349-3fea-bc0c-16d71d8d584d | -2.82453 | -52.95421 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 186c45bb-bcb3-3097-8bcb-bc73a9410e47 | -2.81664 | -51.48991 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84645c38-545e-37b9-85a6-98ff527af240 | -2.31769 | -48.86627 | 2024-11-06 05:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| fdefdb88-4f12-3ac1-9354-84f32663c7f3 | -1.33117 | -54.61306 | 2024-11-06 05:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b00c04e-949d-3a44-a700-db9ba9c0093b | -2.72675 | -51.71585 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b26525e5-1f40-3512-8306-f67da69e21b4 | -3.08758 | -54.51429 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 969d4d6e-5852-377f-8808-4ef6edabc158 | -2.67688 | -51.82242 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 1ef7652e-3c0b-34bc-bb72-513747cf85ef | -3.66076 | -50.23042 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b5dc42d6-9b94-3c86-8f25-f7683872f822 | -2.80596 | -51.48445 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b79cdbf-8e4e-3508-b5c3-fbcb9c7a1f23 | -3.22721 | -54.86153 | 2024-11-06 05:31:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f55119b8-6b28-3450-a9ec-289b53638d8b | -2.77368 | -54.72864 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 772c180c-d89d-3083-9fbe-b741cf49cd02 | -3.00236 | -54.09755 | 2024-11-06 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ced988f-beac-3fc4-93b6-33f058064096 | -3.05732 | -51.06821 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a1ea0a6a-9cb6-394e-a44f-3c13a83f15be | -2.91921 | -51.03711 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c693ee95-4c58-32b7-abd6-e7dd6382bee6 | -10.12701 | -65.0247 | 2024-11-06 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dcb669a-d36d-316b-939f-7c84d6a15eb4 | -2.44669 | -49.02941 | 2024-11-06 05:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a33421fc-105b-3c38-97c0-6e435f30d364 | -2.97121 | -53.87115 | 2024-11-06 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 70133902-6fa0-37bc-b66e-35f661940f00 | -3.47597 | -50.38179 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb238042-9429-33c9-a127-ff8f4f5e7546 | -3.01381 | -53.23133 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6a762f39-c553-340a-84cc-237e3d1c364f | -2.71913 | -54.15086 | 2024-11-06 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 9a4c6adb-868d-35fc-8c97-4d6b3dd05cbf | -2.91342 | -51.03621 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 73119063-84f0-397e-88a8-4d5811dd1ddb | -2.80032 | -51.48369 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b20ae58-082c-3bcd-9265-c6c49355d3c0 | -2.80538 | -51.48838 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 957c7dcf-e4ce-3590-9822-2ae595de3022 | -2.83805 | -51.80254 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 59051a89-428e-37d6-8707-8c6a487997c8 | -2.75969 | -53.21659 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3c78951e-c334-31b9-97c2-233dff273927 | -2.84173 | -49.46944 | 2024-11-06 05:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 773be38a-5286-34ff-9def-1d14807d8b52 | -3.58695 | -50.26253 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b27c8fd-b96e-3283-84b4-d2929b297cc8 | -2.94282 | -54.79601 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2889e945-0081-3241-b88f-e7414ab941e8 | -3.67304 | -50.23268 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e07da903-15a9-3861-9452-2515c1fc970e | -3.14834 | -54.26299 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7bc88af-f512-30e8-bd36-2521592818ea | -2.97435 | -51.02488 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0f657434-fc38-374e-931b-4b3f184a0e15 | -2.8254 | -52.94841 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 0a73442e-766c-306d-a323-452d756ff38a | -3.16829 | -50.2097 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 9c020d33-4b2f-3574-b131-f643dc9188d4 | -2.91811 | -51.04359 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c315b5ba-2c63-3abc-902c-ec37e7dc0aea | -2.80967 | -51.80296 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e30ea931-96ef-3a02-94e1-057ebded427f | -3.56344 | -51.50861 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 427c7f77-8a5f-356a-b308-cc50efe52f53 | -2.82706 | -52.90234 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 26413cb2-b307-3855-a837-56eef960f38a | -3.65658 | -50.25916 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c91c8350-2b53-33d1-9fbb-4b5a6320f310 | -3.01421 | -53.43013 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |


[Clique aqui para ver as próximas entradas](README63.md)
