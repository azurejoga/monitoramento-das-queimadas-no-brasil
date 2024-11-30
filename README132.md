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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65ad67ad-3614-30d0-9a0f-4afc5f6ab5d9 | -7.91653 | -61.54858 | 2024-11-30 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4ef0c5e-ca5c-3ff4-ab73-aad64cd43d58 | -9.74131 | -63.03871 | 2024-11-30 05:29:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de7349d7-4b3c-39fa-b62c-3cdd586924f0 | -8.42089 | -64.03185 | 2024-11-30 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0030aee3-9c32-30e3-a5d1-5711c864ccd6 | -9.85849 | -63.9898 | 2024-11-30 05:29:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40f21f39-f6b3-38a6-badf-238840f07915 | -9.37738 | -63.57621 | 2024-11-30 05:29:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47d6a1bd-5fc2-3f01-9138-2e2ff4f37d09 | -9.80571 | -63.31771 | 2024-11-30 05:29:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31e69cd4-d9dc-3feb-9624-f679c6dfcdec | -8.14028 | -54.85701 | 2024-11-30 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 231ac76d-3dbd-3c0c-8933-b1b0465a9f21 | -10.0731 | -63.75086 | 2024-11-30 05:29:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 774f1f14-6edf-3c2e-ba8f-3e9fc146a861 | -9.47127 | -63.24204 | 2024-11-30 05:29:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f3d86c0-9132-37cf-9638-fa8ec9b82215 | -9.38015 | -63.58029 | 2024-11-30 05:29:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52df2978-f2b1-3a0b-a819-ec4e21b1444d | -11.85781 | -63.20753 | 2024-11-30 05:29:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e915412-7d22-36bc-950e-b62989a43618 | -9.40999 | -63.22113 | 2024-11-30 05:29:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62c23c32-1e91-362a-9c84-98d5c1e80f5f | -9.41108 | -63.23565 | 2024-11-30 05:29:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d0cd87fd-f2cc-37b7-bf62-7944be51a00b | -9.15143 | -63.24445 | 2024-11-30 05:29:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c8bcbc2-aff3-3e75-ba5e-b49789e85424 | -6.00734 | -57.83836 | 2024-11-30 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab5b9082-08fe-372b-b354-5201b534b962 | -9.74331 | -64.64072 | 2024-11-30 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b5b993b-5c46-32c0-9339-aff9c77a1327 | -9.66108 | -65.74193 | 2024-11-30 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 50cfce5a-9f55-32bf-8621-69545ecf8721 | -7.55214 | -63.43245 | 2024-11-30 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6f7658a-39b5-39e1-bf4f-79a152b67c84 | -10.22213 | -59.08438 | 2024-11-30 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88ea3b86-c6e0-3ee4-82dc-759de8cf651a | -9.81979 | -64.23123 | 2024-11-30 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbf5fa89-e9e9-342a-b5e0-a4f97a8c2b52 | -9.18621 | -62.37856 | 2024-11-30 05:29:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7f88bfd-0bce-38b4-b8a9-eb5be74fe4b0 | -10.26033 | -62.21788 | 2024-11-30 05:29:00 | NOAA-20 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9cad104a-d316-3f60-ad47-83905bba0f02 | -7.89786 | -63.26608 | 2024-11-30 05:29:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5111d7b5-43c7-3c6a-ac8d-41d89726aa50 | -9.27788 | -62.11747 | 2024-11-30 05:29:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9a963c0-38a0-3416-848c-f6864c6f1318 | -8.33372 | -64.09281 | 2024-11-30 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7da43bf7-32cc-3411-b6d4-9e47145233a8 | -9.20065 | -63.61724 | 2024-11-30 05:29:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80936ef7-b94b-3b1a-a520-97d1160daf85 | -11.80712 | -59.0714 | 2024-11-30 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dbf3d78-ac1b-3f23-aa5a-41ccba376f0c | -9.28758 | -64.24577 | 2024-11-30 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0a2f317-f74c-3edf-90ac-e471d9f7fdca | -3.606 | -49.9995 | 2024-11-30 05:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e4265709-fa7c-37aa-8b55-d6e10be76136 | -3.2591 | -53.6186 | 2024-11-30 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| cbc26edb-43f1-336c-ae4f-be5bbdbfe833 | -1.6419 | -53.8731 | 2024-11-30 05:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 06f56226-12fb-35b4-b257-e45f1a62d936 | -3.2406 | -53.6393 | 2024-11-30 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 9f17ebb1-c3b4-355d-8317-5405c7ed9318 | -3.259 | -53.6388 | 2024-11-30 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 927a484a-abb3-3dd1-a56f-339105ef8960 | -3.6061 | -49.9784 | 2024-11-30 05:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 129.7 |
| ec0d257b-7c34-3781-9339-1949fae7c6d3 | -1.6938 | -46.7833 | 2024-11-30 05:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 55b90900-b05b-3a00-8443-c59153e81313 | -3.5876 | -49.9791 | 2024-11-30 05:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 550fd24c-2ce4-3d79-b585-d83da43590a9 | -12.42212 | -63.65594 | 2024-11-30 05:31:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78512a5d-8acc-31cb-bcee-fd940dd232ba | -12.30557 | -64.45298 | 2024-11-30 05:31:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22c1069e-9759-33bb-a6d8-c62c8711f282 | -12.34753 | -64.12608 | 2024-11-30 05:31:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9cef762b-6f67-3b85-8921-b3c02ca0ac21 | -12.22477 | -64.35841 | 2024-11-30 05:31:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbd6040c-d110-3bea-8d92-76ce0497fd27 | -12.21089 | -63.53109 | 2024-11-30 05:31:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 230cc2c5-7441-339f-a5bb-3ae22b3200ae | -12.28333 | -64.4419 | 2024-11-30 05:31:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 79e521d8-17b9-3ccd-811a-a07f2cbc0ff6 | -12.2142 | -63.53163 | 2024-11-30 05:31:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 531ca469-c140-38ef-84c2-bbe1d402622a | -12.17375 | -64.1705 | 2024-11-30 05:31:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 812df508-f356-3d81-b00b-452b04b419a9 | -12.28391 | -64.43829 | 2024-11-30 05:31:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 88dedea6-5bf2-386b-8b08-aa7d4eac75b9 | -12.37797 | -63.65595 | 2024-11-30 05:31:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a28340a-4194-302a-a3e8-bc3135e07961 | -13.96556 | -60.34148 | 2024-11-30 05:31:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ada55ee-1a74-3781-90a8-1f6854141e8e | -3.6061 | -49.9784 | 2024-11-30 05:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 06188d35-1d6b-325f-9425-7654e2ac9da3 | -1.6938 | -46.7833 | 2024-11-30 05:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| a728da7d-ead3-3bb3-a1bb-7df66b622dc7 | -3.2591 | -53.6186 | 2024-11-30 05:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| cf33df35-556c-3073-bbbb-af68b1a918ae | -1.6602 | -53.8728 | 2024-11-30 05:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 324dacbc-5224-3efd-8161-14b34b24131b | -3.259 | -53.6388 | 2024-11-30 05:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| fa5fbe53-6eb6-3f9b-ac11-9753674b626a | -3.2406 | -53.6393 | 2024-11-30 05:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| bdbd6695-576a-3a7f-bdc8-80477dbce093 | -1.6419 | -53.8731 | 2024-11-30 05:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 9ad8c89b-1a1e-3102-a30e-8be7a8f38262 | -3.606 | -49.9995 | 2024-11-30 05:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 06978ec1-5f39-3f0f-ab31-bf460a0f1602 | -3.606 | -49.9995 | 2024-11-30 05:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 22703be6-c0c8-34d4-9da4-27c6a6dd9b5c | -1.6938 | -46.7833 | 2024-11-30 05:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| bb72e447-a271-3187-b063-db70c5ef3467 | -3.2591 | -53.6186 | 2024-11-30 05:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| f18d825e-007f-3e01-9ccb-763329d22206 | -3.259 | -53.6388 | 2024-11-30 05:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| d588aea4-7495-31cf-bbc9-14e921d448fe | -1.6419 | -53.8731 | 2024-11-30 05:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 9e7e8cdc-d7a4-3a58-815f-753b54a2300a | -3.6061 | -49.9784 | 2024-11-30 05:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| ffbebb23-e053-3e9a-a013-54da0ac3936d | -3.2406 | -53.6393 | 2024-11-30 05:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 1329d180-7462-32e9-9777-a6a8f335fb59 | -3.6061 | -49.9784 | 2024-11-30 06:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 61450667-4517-366f-9dff-ff7fec251dc7 | -1.6938 | -46.7833 | 2024-11-30 06:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| b387964b-f2ef-35eb-a1c2-0f2211c94a0a | -1.6602 | -53.8728 | 2024-11-30 06:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| a5acb339-7366-3432-9e86-8e07b9367a85 | -1.6419 | -53.8731 | 2024-11-30 06:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| c895feb9-f89b-325d-b02a-6c94560effd5 | -3.606 | -49.9995 | 2024-11-30 06:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| c2a2f507-b057-307f-85ad-de46b9eaf17d | -6.9 | -43.56 | 2024-11-30 06:00:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1a19511b-a4ff-31a1-b179-2059575c7c22 | -6.92 | -43.52 | 2024-11-30 06:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 54a5071d-b31b-3bcb-b6dd-7e622f7e0c68 | -6.93 | -43.56 | 2024-11-30 06:00:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 974ec9b8-aeea-305e-8c68-740d1bbb2d0b | -3.6061 | -49.9784 | 2024-11-30 06:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 2a960691-a676-32b7-b12a-59f563e993f6 | -6.9156 | -43.5418 | 2024-11-30 06:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| f531f03c-e552-3a01-bb8d-062b7bd140bf | -1.6419 | -53.8731 | 2024-11-30 06:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| f2e8ce36-bd74-32ff-9bd8-c4ea69f0c57c | -6.9344 | -43.5401 | 2024-11-30 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 35.9 |
| cdeb7860-1cee-3adb-9006-20202f79ee70 | -6.9153 | -43.5652 | 2024-11-30 06:20:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 37.8 |
| fe7bb3ae-3be8-3883-8564-c7ee7ba78e90 | -3.2591 | -53.6186 | 2024-11-30 06:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 7f0acf48-267a-3549-b757-ec440b121646 | -3.259 | -53.6388 | 2024-11-30 06:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| d4fb47b0-a01f-3360-b161-d4f9e6c760ba | -6.9156 | -43.5418 | 2024-11-30 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| dc004977-0ff8-3d9a-b585-38e93fea9021 | -1.6419 | -53.8731 | 2024-11-30 06:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 0a97e920-5e4d-383b-92d1-b142a71fcde1 | -3.2406 | -53.6393 | 2024-11-30 06:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| cf705128-f29d-3f5d-a841-b9368e1bb5af | 1.09973 | -59.58653 | 2024-11-30 06:20:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dd8eb647-b9df-35e1-979c-a1e54f441755 | -2.89968 | -54.77052 | 2024-11-30 06:22:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8e013544-3370-309a-8bb7-56c91300fe67 | -1.43715 | -55.24606 | 2024-11-30 06:22:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| ecbba044-ca47-3abb-962b-6fcdb895587b | -0.58207 | -51.68856 | 2024-11-30 06:22:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 54.5 |
| d9dd9cbd-d8d1-3dc5-8908-16a32ab8c7ea | -3.2621 | -53.63265 | 2024-11-30 06:22:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 9bababf6-bf96-33e9-b2c9-ad0e302e4a0f | -3.25189 | -53.60918 | 2024-11-30 06:22:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 44c0a01f-b866-3caf-bb89-c5aff606a6f4 | -1.64349 | -53.86437 | 2024-11-30 06:22:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |
| c20f704c-7783-366f-92e4-73ce0e4cd244 | -3.60501 | -49.96219 | 2024-11-30 06:22:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 2938f690-1405-3d3e-a6b6-9ec53dcbe0af | 1.19263 | -55.966 | 2024-11-30 06:22:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 0938329f-087b-38eb-b4e6-a1c264d1080d | -1.43703 | -55.24076 | 2024-11-30 06:22:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 5665fd19-4467-3b32-990f-68d95dc6741b | 1.09981 | -59.58455 | 2024-11-30 06:22:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3db14c3e-0e52-353f-be8e-3f53ea6dc4e9 | -0.58261 | -51.68172 | 2024-11-30 06:22:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 45.4 |
| ed58a333-09ef-3f40-b8df-d4ef33f49b87 | -1.26556 | -54.54858 | 2024-11-30 06:22:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 683f1112-36dc-3774-b524-b7aaf4803eff | -1.82536 | -54.53403 | 2024-11-30 06:22:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 4d8d2bf6-f514-30b0-94cb-2a421412e7f8 | -3.24891 | -53.63058 | 2024-11-30 06:22:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 4bfa73e9-012a-314a-b234-3d08a34db161 | -1.83519 | -54.51118 | 2024-11-30 06:22:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| b9a01364-420a-39e9-9f12-b115a7aa2bc6 | -3.14483 | -53.81918 | 2024-11-30 06:22:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 10cb08ef-ddb0-3eb9-9c87-482343dc0298 | -3.48876 | -53.78851 | 2024-11-30 06:22:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| c020e0d5-b12d-37f7-ab22-cd7c0bc6512b | -3.48788 | -53.8042 | 2024-11-30 06:22:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 116f6678-7bac-318a-a9f8-c0400457faca | -1.70835 | -52.63023 | 2024-11-30 06:22:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |


[Clique aqui para ver as próximas entradas](README133.md)
