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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b24a729a-b146-3201-9edd-0cbd8fb301e1 | -3.03163 | -53.86829 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aae21b26-6b22-319b-bab8-cb746da999c6 | -2.97355 | -51.02433 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d2b8337-9460-3779-a6cd-fa19d6044ae6 | -3.18159 | -54.10559 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 255b2a93-161d-3ba6-b140-89e9c04ea6be | -3.17045 | -54.08673 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49ea10f8-81d9-36a7-8c26-66536e8ea9e7 | -4.25874 | -50.74932 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 6efeba67-9115-3140-89bc-ec6356a6bb3f | -4.26013 | -50.7653 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 220b89ea-e393-3b66-876d-3a16d276ed23 | -3.11924 | -50.27633 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| af4c1d0d-7b14-337e-a1e8-b5e69836a040 | -4.26686 | -48.56202 | 2026-10-01 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2dc45d8e-ba2c-35a1-a875-3280cfe91fe9 | -4.04482 | -54.22775 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 536332c3-c2d0-3fac-9f67-2ce325c71359 | -6.2384 | -47.44896 | 2026-10-01 04:32:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 97e3625c-39ee-34b1-a9c9-a11d2741b6e3 | -3.43034 | -50.44058 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0452631f-9d54-37f2-888d-0206b57408da | -4.66568 | -49.23017 | 2026-10-01 04:32:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c97c5d27-35e3-304e-9f1a-c25cab56fd6d | -4.45671 | -47.92429 | 2026-10-01 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 609721f2-7212-3b7f-8af6-8307cea2bf4b | -3.02664 | -53.86744 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e4f62f0-ae16-35ac-8e34-2326e5afd486 | -5.74942 | -45.15232 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 68b9d5d0-a40d-3b4d-bb74-3872805a2db0 | -1.28624 | -46.6087 | 2026-10-01 04:32:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af163192-ea8e-360a-99d5-2556e5d475f7 | -3.28961 | -53.86026 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 6dcc839f-0953-3add-af71-e45ea6af622d | -3.18671 | -48.02042 | 2026-10-01 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dbc539a6-91e8-3b4f-91dc-98574ce35e60 | -2.41559 | -49.29766 | 2026-10-01 04:32:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fb55b2a1-01ea-3bee-8f40-647c77e89804 | -4.26993 | -50.76501 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 38dbee28-982d-3260-880b-e64aba48514e | -2.84274 | -45.12838 | 2026-10-01 04:32:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ebad53b-67c0-37d8-b458-f9862f4e9b8c | -5.45194 | -45.87929 | 2026-10-01 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7f0080b-cbee-3975-9f87-3f1801c0c0f7 | -7.31967 | -42.08143 | 2026-10-01 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 849c35dd-39b3-3efe-bba2-3986c8cb2e45 | -3.82671 | -50.62215 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b65db37b-f91b-3bc4-a23d-f1e72985afe2 | -4.2627 | -50.74998 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2e99854c-3ace-351a-a57f-ed75cd8a6da6 | -0.43978 | -52.00611 | 2026-10-01 04:32:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72884a8f-f294-3d09-bb77-caa96735b30c | -3.93523 | -45.41724 | 2026-10-01 04:32:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b99fcbd-7a52-37af-a5bb-a0f12eb9d512 | -2.90151 | -54.09497 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9a15742-b203-33ab-bbd8-04743e3a5a75 | -5.42572 | -43.4518 | 2026-10-01 04:32:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e92b353c-7576-3f3b-ae11-84433080c23c | -3.18457 | -48.02324 | 2026-10-01 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 906d8bc5-02e7-3db9-b623-9efc60262e00 | -3.11381 | -50.26021 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f02674c-615a-3d6e-bbaa-12741beb9e3e | -1.66501 | -50.48143 | 2026-10-01 04:32:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21da1e33-e52d-3e9e-b4ff-77f4f4e1d8bb | -3.17706 | -54.10164 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| c96ce63f-263d-3aa5-9001-592cbaafaa62 | -4.85994 | -45.84235 | 2026-10-01 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a956705-80c7-32fe-9ba4-eefeebc1876e | -1.44756 | -54.46085 | 2026-10-01 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf9efe21-d9f3-36eb-9544-0d9af973e3bf | -6.70542 | -45.66226 | 2026-10-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| efac4ad7-2f3c-3c04-bc31-44ef9d34584b | -6.47195 | -46.56104 | 2026-10-01 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37742c69-f9bf-3d4e-af7e-b0a7b280dbaa | -5.75332 | -45.14928 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f20aa1fb-1c31-342a-8e05-213c678a1093 | -3.16139 | -54.10194 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dea353fa-e2cc-3688-9326-b0b93a44a112 | -3.69038 | -47.12829 | 2026-10-01 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8e678d1f-3fe3-3db7-b1d8-31c0cd3964b5 | -4.26044 | -50.73922 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 089ed849-3526-3821-ab6a-ccb929b2f19e | -5.18071 | -48.2631 | 2026-10-01 04:32:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ff6a11b-9dbc-326f-b424-bbbdee4e01e8 | -3.16438 | -54.08447 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 184be024-afa6-3679-8a48-591a37e6923f | -2.24702 | -50.54567 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddc69aa9-8a69-3bbf-a3d3-3580cfee2356 | -3.6668 | -45.869 | 2026-10-01 04:32:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9580b85-7664-3935-bb54-b763211d4d0f | -2.72436 | -49.78865 | 2026-10-01 04:32:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c0440a7-77ee-3489-83a8-717a846623bf | -6.20423 | -41.60999 | 2026-10-01 04:32:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 20309ed0-50cc-35d7-8e3f-67bd22296fc2 | -3.24572 | -50.81179 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0817c126-2f8e-33e0-be37-44b463b62079 | -3.16174 | -54.0764 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5d888a3b-5508-3add-8d58-fd681c2443da | -5.18092 | -46.19689 | 2026-10-01 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| ad36a1f5-79a1-39ba-b9b3-ee4affa82af6 | -3.11452 | -50.28068 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e1bb5368-7ecb-3636-b643-5a18ff9374b6 | -3.03948 | -53.88279 | 2026-10-01 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9bc2db1-29c0-398f-b0ce-21e03877240e | -0.39391 | -51.84935 | 2026-10-01 04:32:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 00761277-fada-351b-b305-a4d458e003f9 | -4.04923 | -54.23226 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30d0fe8e-77aa-3e79-8d85-4924c7057d62 | -4.29556 | -50.79742 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 677d16a4-1c31-3a10-b790-fbd761b3cbf9 | -4.26829 | -50.77529 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 882eb72d-857b-306c-86db-4424039434a9 | -4.30941 | -50.76294 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f601c3fa-3f43-3cd1-82f6-afbe5175ed84 | -4.28794 | -48.56536 | 2026-10-01 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc009d8a-e97a-3ceb-8740-74a466b653e6 | -4.29611 | -50.7449 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a55ae6d-5759-3824-b81f-84ff9c26e1e2 | -3.576 | -54.3237 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a49c94b-e572-34b6-8072-7560560eea3a | -6.71922 | -45.5745 | 2026-10-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 33e5c098-bc35-350d-bae5-098885b9da1c | -4.86379 | -45.83942 | 2026-10-01 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f4e8f4c-649a-3f27-b0a0-4a40bd20bfb6 | -3.10005 | -48.6753 | 2026-10-01 04:32:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22b4d1c8-ea95-34b8-9225-f955a7377a4c | -5.42632 | -43.44782 | 2026-10-01 04:32:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b0ba9e26-f0ce-37f9-a016-5ef203b1827a | -3.27193 | -50.7005 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 873cb4f4-d718-365d-a004-05df92632bef | -3.09346 | -50.26198 | 2026-10-01 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec385fa7-ee9b-3df4-911f-f42231bc2d10 | -3.6303 | -54.50351 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a5eec54-7c1c-3017-ac26-3d909969a2e6 | -4.89182 | -48.37634 | 2026-10-01 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| b0ad0fcc-5b10-3c18-8369-137a8d287db8 | -2.49511 | -56.9099 | 2026-10-01 04:32:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d04643c0-8436-3ede-a2e4-ab8e6b500f6c | -5.29128 | -49.48293 | 2026-10-01 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e1e8ee5-c92a-34f9-a57c-5160cd1ad3d6 | -3.63164 | -54.50422 | 2026-10-01 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 465221fb-e7d6-336c-b833-a62f4a7fb78e | -3.51117 | -50.31286 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe6d2870-387c-3911-be0a-c48834bdf356 | -2.90277 | -54.15055 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c432eba4-11ca-38bf-882b-8d0f67598abe | -7.02657 | -45.27682 | 2026-10-01 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 50287caf-38cd-39e1-8e49-e2687739b3fd | -3.80228 | -51.03003 | 2026-10-01 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ecce7ee2-7d74-3502-8c24-532247c2ef70 | -4.27373 | -50.75706 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 3290ad7b-5b14-3d2b-90a5-8817727bbce2 | -4.26837 | -50.74044 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c42ad993-ac51-3cc7-a1e7-b29f53edba75 | -0.9365 | -47.55263 | 2026-10-01 04:32:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfc14b54-474d-32a1-a6d1-5b9e78142343 | -5.75556 | -45.15689 | 2026-10-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 80bea8cc-e2b5-3a72-b0fb-8c78c78f591a | -4.25701 | -50.75956 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| d5f5f202-c097-39b1-93f8-8cc35c57004c | -2.85888 | -54.13085 | 2026-10-01 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb4ca681-e5c6-39ec-b9d4-a1a892692078 | -2.84551 | -45.13236 | 2026-10-01 04:32:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 282225fe-2e66-35e2-9c7f-d91ff0ac8aa9 | -4.2879 | -50.7698 | 2026-10-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 909.5 |
| 7794414f-9353-377b-823f-c9870353a6e5 | -5.81319 | -46.216 | 2026-10-01 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec164769-257e-3a7d-b944-8f7674e53efa | -12.78205 | -47.29176 | 2026-10-01 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 310e44e3-010f-345e-be90-03f7d0424ec6 | -10.40834 | -53.78118 | 2026-10-01 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f87515c5-5cb3-3330-8e4a-3a78243526d1 | -11.45818 | -43.43539 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5cfc7be9-2212-310f-be9f-d7eae23c3f25 | -10.75941 | -49.10018 | 2026-10-01 04:34:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07e25a5c-1ac8-3e1b-8c7b-a362092463f6 | -13.35032 | -46.82391 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4cb57331-5f83-390c-b62e-2ed13c6bd9e3 | -13.36933 | -46.8344 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f25e3cc9-e87e-3466-b0fe-0b45c8c0e316 | -11.387 | -43.36865 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c9b72b35-412b-3182-b87e-f03431dbc173 | -8.12677 | -43.52412 | 2026-10-01 04:34:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52cd89e0-5c37-32fa-9a4e-36daf6d0a72e | -8.63046 | -47.21579 | 2026-10-01 04:34:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8be7cd3-68ae-3fb8-823f-f13ab28ca0b8 | -7.54504 | -55.04259 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dc2fc37-ffcb-3008-b989-3a04790aa733 | -6.31533 | -52.94315 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7c9a087-e736-34d3-b1b1-76a81de5b477 | -13.87034 | -44.43834 | 2026-10-01 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3eea532e-aba1-3988-82ef-71cf2ebc66e0 | -9.77796 | -53.84342 | 2026-10-01 04:34:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a7bd645-8975-383b-9613-ba3239e7059b | -11.45749 | -43.44015 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1bfe3244-a779-3f6e-9938-99b03c0811f5 | -8.02515 | -49.38324 | 2026-10-01 04:34:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa5bd96c-f3a6-3e84-9db5-4f7a0dbdedb6 | -10.52375 | -57.78013 | 2026-10-01 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README55.md)
