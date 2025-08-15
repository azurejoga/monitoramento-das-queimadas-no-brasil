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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c1ffb45-de5b-3c94-bb7e-072e17e696b2 | -7.43251 | -60.03063 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| b9da2c0f-74fa-33e8-b728-2256b7db219e | -9.17047 | -59.6898 | 2025-08-15 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 41cbce2e-5a6d-3683-9d52-bd3bed3c4c37 | -6.9353 | -59.53711 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 1ff783be-94d3-365a-abc3-ae81d2fdec32 | -6.6719 | -59.08263 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8b67b260-4a25-3a19-b8ae-3b2353dd1d17 | -6.0706 | -59.96988 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 4a4e4292-88ff-35bd-b8a5-9aa7ae010b20 | -7.08666 | -59.24543 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 40a764e8-464e-30bf-b045-2c7beb015d3f | -7.29522 | -60.62222 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.3 |
| c97e42e8-3ca4-35f6-ba78-b5957c0f23e6 | -7.81738 | -61.32591 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c4e760c4-fd77-39f2-a01a-2509cfba50b9 | -7.52999 | -61.37628 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 1663eee4-fe9c-34e6-9b4e-3b614d034490 | -7.24402 | -60.00098 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0cc97666-3181-3949-b3e6-d985f71ec3be | -6.06638 | -59.93987 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 70267704-cd79-39bd-82ab-ec75fc26f5a5 | -8.55681 | -63.92164 | 2025-08-15 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9178f315-cbc1-361a-9c74-aa2376a356b2 | -6.64499 | -58.82328 | 2025-08-15 01:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5a7dfde4-0495-3d7f-8c65-2af6649552e3 | -9.16764 | -59.6704 | 2025-08-15 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 98b75166-1b82-37cf-a599-54bf2522ae53 | -7.06023 | -59.22247 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 4a2242d5-1be8-3b9a-bbd5-f6bb1cc206c0 | -6.87141 | -59.8387 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 4da26f31-0c16-35e3-8e39-555cf1541758 | -6.67348 | -59.09374 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 88f78dfb-cce8-3548-8a4a-018398136c9a | -7.58612 | -63.46279 | 2025-08-15 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7a289cd3-d1b9-3d37-a98e-e3d269367172 | -7.28862 | -64.68999 | 2025-08-15 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6bafb082-1386-3238-a64f-fd4c6f8b40f9 | -6.65231 | -59.08551 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 249786b9-e645-3e40-aa47-dfbe13638931 | -6.68607 | -58.82296 | 2025-08-15 01:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ab4aeab5-fa60-365d-b869-43b0b117c003 | -6.08208 | -59.94188 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 4b019206-efd5-3982-841c-8aca3f9d412e | -8.10578 | -61.20527 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 17e51aa1-3be3-3cb3-8978-f647b1631640 | -6.07271 | -59.94333 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| e538ef1b-f5c2-3b6d-bf5f-c3cb14202c46 | -7.2803 | -64.70217 | 2025-08-15 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.0 |
| ab9cc4b6-c974-35bc-9c19-b520b8aa6f9e | -5.92422 | -59.92591 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c1cb7e2c-2daf-39db-8aa7-c11c277a9e45 | -6.95038 | -60.0124 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| fd924910-d44f-3bcd-8491-fc3a4b324e3c | -7.87639 | -61.81566 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 42d15a66-7d66-34d1-9d15-e51e87450a5c | -8.1159 | -61.21293 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b1a0c9cc-fd2d-3a42-9abf-bf2e407c606d | -7.1553 | -59.6487 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 4767b60b-cd45-3971-a83e-2561080e3214 | -8.67286 | -62.44709 | 2025-08-15 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a7b4f4a2-8993-3b8f-bd0c-f114da7c7c03 | -8.11339 | -61.19505 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 64360df2-43ce-3baf-adfb-66e347d6e820 | -7.32358 | -60.62751 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| acf98271-eba6-3047-b965-ac1a425796f5 | -7.45894 | -59.90082 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4193467d-97d7-3292-ab5e-de7c39cbafb4 | -8.60046 | -62.65832 | 2025-08-15 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 84f3a225-ae8d-39f6-869d-6c2b7d85d4b7 | -7.27888 | -64.69129 | 2025-08-15 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 117e3cdf-62dc-3a5d-9bab-d0bb9b9cd9f1 | -6.10735 | -59.91771 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 59d82210-a653-33ec-99f1-abd07dc622d0 | -9.07608 | -60.76802 | 2025-08-15 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8653dcbe-8dac-373d-9ee0-f15bf6822192 | -6.05841 | -59.95128 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1573e40d-1d5f-3825-9543-672991c3dfd7 | -7.27704 | -64.69732 | 2025-08-15 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.7 |
| fdff471e-1f02-3841-a875-460f6cf2b45e | -7.9497 | -61.74457 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 014bb4fb-ed02-339a-9044-7dab71541501 | -7.1514 | -60.12933 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 64e4b1ef-12e4-320e-a727-33884ca10fbd | -9.15062 | -59.66886 | 2025-08-15 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 5bb6cb37-6b07-3fd3-87fa-d57d693e66d2 | -7.11668 | -59.61893 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e3eb1654-a8cc-3eae-851a-d835e926b2d2 | -6.65621 | -58.82744 | 2025-08-15 01:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 718ed863-5271-39fe-90d1-467384b2bb48 | -7.08353 | -59.22412 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 7b49a0c5-256f-3ed9-b7be-9f1df02df22c | -8.94711 | -62.23315 | 2025-08-15 01:28:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 26582ab7-32b8-37ed-969f-61328f57e70a | -6.95001 | -60.14134 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 141707b8-3a2a-3685-af6b-23f783a6152a | -9.152 | -59.67857 | 2025-08-15 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.9 |
| e842dd5c-6869-3a67-ba5c-7a163aad535e | -7.31326 | -60.61959 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 8bfdff82-5ba4-3908-b1b1-f789da8457e9 | -6.0994 | -59.9291 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6b146708-a684-34b0-a37f-8d36d12102b7 | -6.06779 | -59.94991 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| c7bc8521-d2e3-35ea-892e-6297776e8f18 | -7.60041 | -63.49979 | 2025-08-15 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 42671150-9c2b-379d-9501-26723c9d395a | -7.45797 | -60.40585 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 04912d25-e1aa-3e18-b0ff-54673a1eca65 | -9.17189 | -59.69954 | 2025-08-15 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| d247ee2c-1563-3026-9a7d-94f43a78f342 | -6.93507 | -59.63714 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7aa68afb-d391-3d4b-acb7-c7a9255e4fb8 | -7.00122 | -59.98896 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 24570617-3042-32a8-a550-8df3ec51534d | -7.92319 | -61.74836 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 413d3e24-2f1d-3f32-9346-f73a480419d2 | -8.28802 | -64.01395 | 2025-08-15 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1d0122fe-d23a-3f7a-8b23-17d6e61a1eb7 | -7.60426 | -63.52857 | 2025-08-15 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 05fb4af6-b258-3178-8302-ac330fdce9ae | -6.07416 | -59.95332 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 141.0 |
| 756562f1-465f-32d8-aafe-5d7425776c83 | -7.53513 | -61.34828 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 57d285ad-a64c-3ddb-8961-c6fea9ccbd3c | -7.07229 | -59.21481 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 83828162-cb20-3756-8fa7-e9173af68499 | -6.1023 | -59.94925 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 3fc318ab-cdac-33ae-8109-750917f57506 | -6.69935 | -58.84428 | 2025-08-15 01:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 879dd750-becf-3fdc-9131-ca8b9c097968 | -7.03857 | -59.85261 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 890e7146-4f24-3434-840f-cec0effb25ed | -5.44095 | -60.14561 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 26fc3f9b-1969-3fd9-a998-4cbe76ab2c61 | -8.90347 | -60.59237 | 2025-08-15 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1c8ca575-b70d-30e6-9a86-71cfa0f5d386 | -7.2862 | -60.62352 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 02caf70f-d87f-350a-919b-f8842db17ebb | -6.65451 | -58.81599 | 2025-08-15 01:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 99224c39-33ff-3a6d-9f42-6b3a3059be2e | -6.6977 | -58.83293 | 2025-08-15 01:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 929127dd-67ad-392a-99c2-36f7d597a144 | -7.62263 | -63.52603 | 2025-08-15 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 05e5e30f-1166-3447-b712-5b92bf038d9a | -7.44036 | -60.01963 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e161ad70-9f8d-3d37-be28-f3cf0e29b755 | -7.13162 | -60.12243 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ad3a4c78-9374-328b-aa34-b06e692c48ef | -7.95093 | -61.75344 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 37.7 |
| e471addb-e24c-35c0-8a51-d0c8465f64dd | -8.29362 | -64.01787 | 2025-08-15 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 5e2cf118-2b51-3467-a68b-bd51a209be44 | -7.09317 | -59.22266 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 7a93f7e5-fb4a-31e3-ad23-833196682425 | -6.70099 | -58.85561 | 2025-08-15 01:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.7 |
| d1393fa8-9a45-3dca-b208-7fe98acf8213 | -5.43955 | -60.13564 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2b662dab-29e3-3dd2-82c4-ab4ff0b3f5c4 | -6.94216 | -59.82187 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.9 |
| ada21780-7d4f-31ad-9c5d-836bc33c93ee | -7.03433 | -59.82285 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 21516b2b-89f3-3ddb-803f-79ddf676d981 | -7.6104 | -63.4972 | 2025-08-15 01:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 2647b392-8857-346a-8428-47e923de0ebc | -9.518 | -60.5268 | 2025-08-15 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 6dff2169-bada-31d1-9346-baec6278d013 | -6.0623 | -59.9472 | 2025-08-15 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 103.7 |
| ed0e9c6f-c0ca-39c0-99a1-bd9a12681298 | -7.5292 | -61.3254 | 2025-08-15 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| a93b291d-f7bb-37dd-a682-da5356091997 | -7.5291 | -61.3444 | 2025-08-15 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| d54aa307-e206-361a-a9c2-28f9205cbc25 | -11.3468 | -55.4124 | 2025-08-15 01:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 190.1 |
| 0718f0ca-b7d9-36fd-8cc0-0d6d1fd8065c | -9.4995 | -60.5085 | 2025-08-15 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| e7a99b0a-876c-3467-985e-b074f12bb7bd | -11.3655 | -55.431 | 2025-08-15 01:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 149.2 |
| 8bc903ba-9d05-3812-882c-3a1b2764a8cc | -6.0807 | -59.9465 | 2025-08-15 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 251.6 |
| 93c9b5d5-540c-32fc-8f8b-34dfdeba32d1 | -6.0622 | -59.9663 | 2025-08-15 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 081dce01-4d18-3309-bbec-1a1bf26fa051 | -6.0991 | -59.9459 | 2025-08-15 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 9160c9af-8b25-3959-82e1-85953b28b9d9 | -7.6103 | -63.516 | 2025-08-15 01:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 09da515d-a5ac-3f59-a5b3-ffc4de6ac39b | -9.3875 | -60.5528 | 2025-08-15 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| fa6c4060-d243-3e92-91b9-d7169059c2c7 | -14.2444 | -44.5897 | 2025-08-15 01:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 48ca5f10-bd4d-3d82-bef0-cc0373b8cd99 | -2.4876 | -47.5737 | 2025-08-15 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 3f24c6ef-94a8-363e-923d-43b33f6b46e9 | -11.3466 | -55.4326 | 2025-08-15 01:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 3214c0ab-e6f5-303e-b4d4-005c84da5aab | -9.4992 | -60.547 | 2025-08-15 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| a8f4696d-be21-33f8-b80d-c96f236c30f7 | -6.0806 | -59.9657 | 2025-08-15 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 153.9 |
| 7889d949-acf6-3374-958f-b702e949bf03 | -6.9303 | -59.5305 | 2025-08-15 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |


[Clique aqui para ver as próximas entradas](README13.md)
