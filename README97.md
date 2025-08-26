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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2d6fd6f-7f15-3ecd-9f0f-343f71441ce4 | -11.1779 | -44.76 | 2025-08-26 06:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 2cb358d5-2491-3ccb-853d-36693cb23797 | -9.1718 | -59.5211 | 2025-08-26 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 874c0d76-c2f1-3b48-9d0e-fca3472ad83c | -6.2275 | -60.018 | 2025-08-26 06:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 69b04ad4-a031-3a35-a98a-6ef48c822457 | -11.1587 | -44.7627 | 2025-08-26 06:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 537.6 |
| 95c33c3a-b174-388f-b9bf-df249a51f929 | -13.423 | -46.873 | 2025-08-26 06:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 55c3b1d8-9f1a-37f5-acc7-b36fe5ced19e | -6.7635 | -59.6718 | 2025-08-26 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| e11ef534-8f46-3b96-93cc-1a5a0da8f9a9 | -6.7819 | -59.6711 | 2025-08-26 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 0f6d2dd5-7338-31dc-a59b-aad28c0f32b0 | -9.1722 | -59.4629 | 2025-08-26 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 44d2572b-9e44-34c1-83df-1cce02ac56d7 | -8.8364 | -62.4321 | 2025-08-26 06:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 1ae600b8-9bab-34bf-a9f9-a843069211d6 | -7.3854 | -64.3475 | 2025-08-26 06:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| c2704622-5e90-39ff-a528-3f1f64afa9ca | -11.54 | -52.119 | 2025-08-26 06:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| de69481b-6788-3532-8e03-a34dc7e84fc2 | -11.5207 | -52.142 | 2025-08-26 06:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 9345d1a1-183c-3a08-8e21-b3cab759ac18 | -11.521 | -52.1209 | 2025-08-26 06:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 427f4235-83de-3be6-a94f-7451170e4d80 | -11.559 | -52.117 | 2025-08-26 06:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 84ba286c-a075-3848-8134-88cdecbc901e | -11.6273 | -46.4126 | 2025-08-26 06:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| cf5a81e9-22c3-3411-b0b7-fd9aa2aa0dae | -8.8548 | -62.4503 | 2025-08-26 06:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 156.7 |
| d9b9a3a9-dfb7-3d32-80be-e8a43a15c0d9 | -11.1396 | -44.7654 | 2025-08-26 06:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 216.2 |
| d56f54b8-f4f5-3b19-968c-9c9cf81aa042 | -4.9605 | -55.8226 | 2025-08-26 06:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 9b95eaf6-375c-36cd-9817-a2f29c1c403c | -9.1903 | -59.5395 | 2025-08-26 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| bf6e7d43-fe45-3141-8595-3453171f5928 | -9.1715 | -59.5599 | 2025-08-26 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 2b721de9-dedf-3a9a-8ea9-f25fa763a7b0 | -11.1583 | -44.7859 | 2025-08-26 06:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 152.5 |
| fa3f2a90-3f5f-3ab0-bba7-0a991a00d939 | -9.153 | -59.5415 | 2025-08-26 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 5bd22ff3-7301-34ed-951d-76050d8fca17 | -11.1591 | -44.7395 | 2025-08-26 06:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| ca1c8a02-4913-3ee3-b7ab-87e6a010f4f1 | -11.6273 | -46.4126 | 2025-08-26 06:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 1d0672cf-f8a1-3b99-a6fa-5766030f8a8d | -11.521 | -52.1209 | 2025-08-26 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 04bf648d-1271-33f2-bc0f-d8b9639204a5 | -11.1583 | -44.7859 | 2025-08-26 06:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 6b23e31b-53cd-3889-afa1-d10a72147c52 | -11.6465 | -46.41 | 2025-08-26 06:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| ee50e28c-cad6-300e-86b0-4ca5ca8e11a8 | -11.54 | -52.119 | 2025-08-26 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| a91385b0-e2b4-3b40-9de3-ab19b1b5323c | -8.855 | -62.4313 | 2025-08-26 06:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| e35f4451-6507-372f-b0ca-8ef215ee4133 | -9.1903 | -59.5395 | 2025-08-26 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| a83214e7-c101-3460-afbd-6b18fad2680e | -6.2459 | -60.0174 | 2025-08-26 06:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 6eb0c52f-c30b-3f90-8b22-7f8280e09abb | -8.8548 | -62.4503 | 2025-08-26 06:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 114.6 |
| efd3321f-3646-3897-9d52-f217779c778f | -11.5017 | -52.1439 | 2025-08-26 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 179ae3f8-4c3e-3cfb-921d-125c08515319 | -9.1722 | -59.4629 | 2025-08-26 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 992eb1e1-f0b8-38c3-b93e-bcfff43b7cda | -9.1904 | -59.5201 | 2025-08-26 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 6d7c793d-6614-3c33-82eb-f28436454172 | -8.8363 | -62.451 | 2025-08-26 06:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 9d29343b-0a99-3355-8e4f-8b2cfed98d80 | -11.559 | -52.117 | 2025-08-26 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| d1d985a4-c971-3ff4-b6f2-dda17e8aefc8 | -8.8364 | -62.4321 | 2025-08-26 06:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 91287623-19bf-3127-8f78-786aa2773d39 | -9.1717 | -59.5405 | 2025-08-26 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 0a01313e-5750-3eb5-8718-97650485f85e | -11.1396 | -44.7654 | 2025-08-26 06:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 202.4 |
| af2f1a59-b003-31ff-8b85-6a65addb68df | -11.5207 | -52.142 | 2025-08-26 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 9e347680-9f54-3ed5-b9bb-b41ea195ab96 | -8.8734 | -62.4495 | 2025-08-26 06:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 98bb9485-20ef-393b-8347-e0c28bd4dffe | -11.1392 | -44.7886 | 2025-08-26 06:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 62d0711b-5e12-3171-aea7-5fd727a44b44 | -11.5397 | -52.14 | 2025-08-26 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 2498e64d-f39d-3f63-ace8-d05bc45e9ba7 | -9.1718 | -59.5211 | 2025-08-26 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 1e92d0d7-4b36-3fd4-9318-f7ecabfd1bac | -11.1587 | -44.7627 | 2025-08-26 06:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 452.6 |
| b97d5bd9-bc1f-30a8-8e2b-7c5cfca2d0c8 | -6.7635 | -59.6718 | 2025-08-26 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 2cfe05a9-326c-3ae9-ae68-16085a8a55cc | -9.0172 | -65.7049 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 687ea8b2-1f1a-3c05-8787-756be6c8e5a8 | -8.98556 | -65.41332 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed8641c5-b9bd-36f1-8960-b2ee3febcf8e | -7.38897 | -64.35439 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ea4ab13-27cf-33e3-a8fd-2a780c97b58d | -9.01167 | -65.69933 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 499207d2-77a8-3dce-a27e-88db5cf48d8c | -7.38235 | -64.3595 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b12827fd-ac5d-376f-98fe-01f1e7814a8b | -8.99937 | -65.40504 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4d29c0dd-47d8-3560-8704-0e46806d4504 | -9.0841 | -66.06245 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fcff384c-fe09-302f-87e7-c44697ce87e8 | -10.6503 | -65.31924 | 2025-08-26 06:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 358c197f-7d19-3bf6-81b7-586a5c90223c | -8.81247 | -69.29188 | 2025-08-26 06:25:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90b2b529-9307-3f5f-acd6-ef0a51dc1aee | -7.37504 | -64.36424 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 29fc8627-4fb9-3627-9d11-5968063453ae | -9.8035 | -64.26314 | 2025-08-26 06:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dbba0ca-01e7-3c13-9352-d62bf414fc2c | -9.0953 | -65.72609 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 343395a6-e5a9-3eb2-9d26-58aed1ccd728 | -8.97741 | -65.42737 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 548c0329-e066-3c88-9971-fcb33f48acc1 | -7.37514 | -64.35821 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6bddae88-965d-3f9e-a11e-18e78b0d7542 | -9.08918 | -65.72348 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97c630b5-83a0-3efd-87dc-126ad09cf36f | -10.6487 | -65.3219 | 2025-08-26 06:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee4f11ca-2c84-39ce-a1b2-8d67ef1fef87 | -10.41545 | -64.38453 | 2025-08-26 06:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 810f1a1e-08f0-3720-8c19-d0bdaca39596 | -7.87764 | -63.01947 | 2025-08-26 06:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 613e47ae-abf6-3f14-b8c3-0e26a3d05fa0 | -9.31393 | -63.44266 | 2025-08-26 06:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1a783ee3-acad-3791-bb44-0823c45f6ba1 | -10.41947 | -64.39387 | 2025-08-26 06:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14b4edbe-bc7e-32b4-92a7-e709898631d5 | -8.99246 | -65.4092 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7f1f5ada-9c57-30b6-9ad4-5faefc6c6b78 | -9.80726 | -64.28835 | 2025-08-26 06:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b251dcd7-547a-3309-b782-986764eaf29d | -8.97678 | -65.43233 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ede50df-1b72-36cc-bb50-349959d5b0d9 | -9.05095 | -65.73047 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 025c34ce-8646-31c7-afa0-4821eac49078 | -9.02757 | -65.71754 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dd38b21-64fc-3330-b45d-80d7330ee439 | -9.07514 | -66.06715 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ea71619d-561a-30a2-a997-1db6064e0747 | -10.42222 | -64.38556 | 2025-08-26 06:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48e8919d-828d-31ba-aae4-992930fbbe68 | -9.07573 | -66.06274 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| af2f889f-2809-37a3-8c14-90d637ba6385 | -9.00063 | -65.39516 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 361a6a54-0a39-34d4-b8ac-73f934bcce1f | -7.38969 | -64.34879 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eb36169d-f4be-3ed9-9fdc-4f3ab53d5fb8 | -8.99873 | -65.41003 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 39e69d39-e4ed-33c6-8c7b-3f74424161b9 | -9.07061 | -65.72347 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d2bb3f5-d3a9-3aab-9a7c-b2705fc8c34b | -9.08296 | -65.72476 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 042c8f04-5f58-3974-b032-e0898938ad5f | -7.38098 | -64.36465 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 141b0640-bff8-38af-bdae-a62715aa0ffe | -8.10877 | -71.24814 | 2025-08-26 06:25:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb077966-b0c3-37d7-98fa-8ee77b3b383c | -7.88478 | -63.02032 | 2025-08-26 06:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 721069f1-b6b9-3358-9eaf-ce754b5a5e19 | -7.37579 | -64.35866 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 27f511b7-f8d1-38ec-842e-3122ce4f9890 | -7.8882 | -63.02039 | 2025-08-26 06:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7a6a7750-d80f-3f9d-8130-764d6293ad84 | -8.98367 | -65.42821 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6df2705e-9151-3a28-9c9d-36824b49e970 | -9.09477 | -65.72892 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ed8ab6c-abc9-32b9-a58f-5e9d1692be35 | -9.7923 | -64.25579 | 2025-08-26 06:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aea381bb-5128-371d-9012-4e661a3b690f | -9.79671 | -64.26231 | 2025-08-26 06:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c690ede-71e6-3033-860b-f956290ac8e8 | -9.05155 | -65.72571 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71ae152a-2912-3cb2-9129-1cefb5dc298f | -9.07807 | -66.06174 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff67be9b-5a3f-3d88-9790-b77b57b3cb35 | -9.017 | -65.70205 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f75a8b5-d6fe-3b31-acde-87ca01a46395 | -7.38386 | -64.34834 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e9c92bf4-268a-3cc3-aa8a-f0390d7d34be | -9.81403 | -64.28926 | 2025-08-26 06:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cea5dc88-3160-35e1-9a62-c6989d1aa31d | -9.08862 | -65.72807 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 611d74de-00e4-3d7c-8d1c-5d6e637c3085 | -7.37443 | -64.36379 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bfcd8211-0ac8-331f-b7e8-22440579fac2 | -9.07751 | -66.06617 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 66c1bca8-1166-3e47-9dca-9df4eef71336 | -8.97867 | -65.41743 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 840bc16f-2033-325e-9753-2bc52ffa5c3d | -9.79747 | -64.25616 | 2025-08-26 06:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24ab1afd-6d41-3cf9-8925-99e9178cec8a | -8.97053 | -65.43148 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README98.md)
