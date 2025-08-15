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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be41fd59-e0d8-3a21-a6ce-6f81dc699582 | -9.5152 | -40.331 | 2025-08-15 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 110.6 |
| 2e73e72b-f0cb-30de-934c-5de4aa437c35 | -7.5291 | -61.3444 | 2025-08-15 03:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 6f1c3245-03f6-3c38-8349-7f1f52d1c6ea | -9.518 | -60.5268 | 2025-08-15 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 12a915ea-dfee-3767-b2d1-e0586405c774 | -11.3657 | -55.4107 | 2025-08-15 03:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 78212f22-8de5-36e9-ae2c-d2b1e6590fff | -9.5343 | -40.3282 | 2025-08-15 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 65.8 |
| 21f62ae0-b002-310a-980d-1f72b50522b1 | -7.0797 | -59.2157 | 2025-08-15 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 07d1f18a-a57a-396f-baba-afff8bb2913e | -7.5292 | -61.3254 | 2025-08-15 03:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 26ef5189-b6ff-31b5-ba30-a3d9abce3e10 | -9.5339 | -40.3531 | 2025-08-15 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 69.3 |
| 1d336021-d3ab-3567-bab6-a99455aab0fc | -9.1894 | -59.6558 | 2025-08-15 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| c09918e1-ea14-39ae-acba-e0a67c1731c7 | -6.7129 | -58.8251 | 2025-08-15 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| f4124d25-e859-3c35-bf5d-632c598b84e5 | -5.455 | -60.1391 | 2025-08-15 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| f4ec30b6-45ac-3c98-987c-0bd622917e62 | -6.6576 | -58.8274 | 2025-08-15 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| c974cbe6-5ddb-33c1-b068-5ef055747719 | -6.946 | -60.0104 | 2025-08-15 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 55011a65-5af3-33f7-ba55-de9a2563971c | -7.3116 | -60.628 | 2025-08-15 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| dd18becb-ffa6-3f8f-bbdd-4780567a1268 | -9.1706 | -59.6762 | 2025-08-15 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| cdecac88-8471-3b0a-be61-d525127d8d4f | -6.6577 | -58.8081 | 2025-08-15 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| bb6aa8ef-f67e-36bb-a1a6-e29a8f7fabb8 | -11.3655 | -55.431 | 2025-08-15 03:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| ca099bd1-0e3e-376c-8e3f-285a0fea9779 | -9.4992 | -60.547 | 2025-08-15 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| bb3c2cb2-6368-33f8-966a-1cf071a1d120 | -9.1706 | -59.6762 | 2025-08-15 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 34aee174-3849-3038-b731-dc29e472938a | -9.1708 | -59.6568 | 2025-08-15 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| c5978220-89e2-31fe-ac28-f1c9c4241eaa | -7.0797 | -59.2157 | 2025-08-15 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 3f381456-5558-37a6-a3a1-28017ce98d0a | -6.9461 | -59.9912 | 2025-08-15 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 99a43ce3-15a3-354b-9089-6eb4f81bcfa0 | -6.0623 | -59.9472 | 2025-08-15 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 22db4c35-0ff0-3ecc-aef9-7281a31ab89e | -6.6945 | -58.8259 | 2025-08-15 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 7c725c85-3f07-3663-9ae5-08e28e92adb2 | -6.946 | -60.0104 | 2025-08-15 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 2d399486-4b73-36af-bf1c-01e47a3e5f3d | -11.3466 | -55.4326 | 2025-08-15 03:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| ddbb4d8c-c554-33bc-a384-f16ac7001bcc | -7.5292 | -61.3254 | 2025-08-15 03:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 4fde0645-c783-30af-929f-96aa7b1dc0b6 | -5.455 | -60.1391 | 2025-08-15 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 11f82c3a-974d-3bee-b05d-d464b37ba0fe | -6.0807 | -59.9465 | 2025-08-15 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 56a04bc8-1707-3da8-9c36-1c87d16ac214 | -6.9302 | -59.5497 | 2025-08-15 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 8b270403-a24d-3015-8591-f83789d868d5 | -6.7129 | -58.8251 | 2025-08-15 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 9507a01a-0af8-3612-b09c-97f2150b42a0 | -9.1894 | -59.6558 | 2025-08-15 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 6532c14a-2e73-3410-99c7-67ad96940c4d | -6.6576 | -58.8274 | 2025-08-15 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 5bf3fc26-e256-3cde-be5f-70e9045db4f9 | -6.9303 | -59.5305 | 2025-08-15 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 553450f9-2301-3b71-bd1f-21fc104e66f9 | -9.4994 | -60.5278 | 2025-08-15 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| f616784d-afd1-38d1-a205-a41612f42f90 | -11.3468 | -55.4124 | 2025-08-15 03:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 2da68d6c-e332-350d-b748-166ebf8c45ab | -6.6945 | -58.8259 | 2025-08-15 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 488d448b-2e40-3f9a-ae6f-b2b4d8884b2a | -6.9303 | -59.5305 | 2025-08-15 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| efb9aa6f-8b89-3763-b032-0f30b20b0559 | -9.1706 | -59.6762 | 2025-08-15 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 5d54de08-a966-31fe-b5d1-5f3e4c5eaa06 | -6.6576 | -58.8274 | 2025-08-15 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| c38dc2e7-5259-3edc-9c09-fca4d54d508a | -6.7129 | -58.8251 | 2025-08-15 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| c1916aa8-67b7-31cc-a57a-7ad6109f99af | -5.455 | -60.1391 | 2025-08-15 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 6fec2579-7597-33e8-b188-edc284129e98 | -9.4994 | -60.5278 | 2025-08-15 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| d2db7afa-729a-33fb-8c0a-f6b1d682f2c5 | -9.1708 | -59.6568 | 2025-08-15 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 2650ed9e-f9fd-3e55-8471-37797f488b22 | -7.5291 | -61.3444 | 2025-08-15 03:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| cb665c2f-adbd-3169-ad1a-8eb7edff29e7 | -9.4992 | -60.547 | 2025-08-15 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 38ce37bb-573c-3157-9c2a-781b0129f6ee | -6.9461 | -59.9912 | 2025-08-15 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 508586e7-7f4c-307a-959a-352a2b0c84e9 | -6.9302 | -59.5497 | 2025-08-15 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 35d976eb-5d9d-3e6a-97c3-e19afb2404c5 | -6.6577 | -58.8081 | 2025-08-15 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| f40a66fd-3928-344f-9353-07315f0ae9ea | -11.3468 | -55.4124 | 2025-08-15 03:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 039aae4b-0b79-3412-8928-f2df5d3d08b6 | -7.5292 | -61.3254 | 2025-08-15 03:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 1ad959ef-ce3c-371a-ad27-8b7eb3fe48ac | -6.946 | -60.0104 | 2025-08-15 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| f7fbe7b3-8943-3f1d-b6af-87f1ecb9b2c5 | -9.1894 | -59.6558 | 2025-08-15 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 4865ff1f-8408-3705-b743-5ce6ae53e7b3 | -9.518 | -60.5268 | 2025-08-15 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 0783bd62-c646-3db0-9d12-927cf86895f5 | -11.3466 | -55.4326 | 2025-08-15 03:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 6019632a-ab82-3857-9b79-e25432b38bfb | -9.4994 | -60.5278 | 2025-08-15 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 823abe91-18af-3beb-aba9-452158da9dae | -9.1706 | -59.6762 | 2025-08-15 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 4cd4ac6b-2927-350e-9016-5033409c31d7 | -6.9302 | -59.5497 | 2025-08-15 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 54403c77-92a0-3c24-a714-e796c20b8c5c | -11.3468 | -55.4124 | 2025-08-15 03:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 2e5374c9-a5cb-3cbe-b9e3-fd61b0f6108d | -9.4992 | -60.547 | 2025-08-15 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| e3ffaf19-25aa-3b38-b371-d582d5367f93 | -5.455 | -60.1391 | 2025-08-15 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 1fa857f5-a9a9-3718-913a-a4f9226135d1 | -6.9303 | -59.5305 | 2025-08-15 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| fe9eae91-6f15-3c7e-9558-b307738b916b | -6.946 | -60.0104 | 2025-08-15 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| ed78fd33-87b9-3471-bd45-27f0eeb23fac | -6.7129 | -58.8251 | 2025-08-15 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| c9607bfe-2972-3c93-a0bb-5e09616f0317 | -7.0797 | -59.2157 | 2025-08-15 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| eec1039d-ac8b-3a74-819a-d79c58329119 | -9.1708 | -59.6568 | 2025-08-15 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 7310b2ee-5630-3edb-8751-71c84ae19ec8 | -9.518 | -60.5268 | 2025-08-15 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 285bf1a1-836a-3442-8f7b-a155b399c232 | -7.5292 | -61.3254 | 2025-08-15 03:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| b8747736-2785-3c0a-9257-dfc239cbb7a9 | -6.6945 | -58.8259 | 2025-08-15 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| dffba898-df5a-30b6-b284-7eb49d817cf7 | -6.6576 | -58.8274 | 2025-08-15 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 2d4e249e-0d1b-34ed-9888-5a14f5ba6f81 | -9.1894 | -59.6558 | 2025-08-15 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 37facdd7-420b-3a05-b082-59db4599a3ca | -11.3468 | -55.4124 | 2025-08-15 04:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 1a9e400b-0a3e-387c-a9d3-1840490277f4 | -9.4994 | -60.5278 | 2025-08-15 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 53cdce68-e23a-3d98-8b0d-5942d5a94f98 | -9.1708 | -59.6568 | 2025-08-15 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 6c4b7a88-52ac-31b6-aa6f-b5462c079fa5 | -6.9302 | -59.5497 | 2025-08-15 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| e58f3a75-12d8-32f6-998e-c45c76b4c311 | -5.455 | -60.1391 | 2025-08-15 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 136be363-32ce-3338-b1c8-8ba1e4fef25a | -9.4992 | -60.547 | 2025-08-15 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 9ffa03b0-6d20-3d18-9377-02cd0cdb0265 | -9.518 | -60.5268 | 2025-08-15 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 50f507b7-89ea-362b-b90f-4ad8d9e669c4 | -7.5292 | -61.3254 | 2025-08-15 04:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 59f60f10-ba73-3ea6-a4cd-371f6013d5f3 | -6.6945 | -58.8259 | 2025-08-15 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| a59625d0-b890-3d96-8d8d-bc52446a383f | -9.1894 | -59.6558 | 2025-08-15 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 1980567a-9edc-34d3-b581-b764f9a9e7df | -9.1706 | -59.6762 | 2025-08-15 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 3e422069-f850-3f75-90c3-6c89d5129d00 | -6.7129 | -58.8251 | 2025-08-15 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 270aa2a7-7197-302d-9c1e-847850e59248 | -6.9303 | -59.5305 | 2025-08-15 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 301fc6d6-e1c7-3fc1-82f1-3ad6503da9c3 | -7.3116 | -60.628 | 2025-08-15 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 837a1d6d-195c-38be-ab26-891fa1d6564a | -2.49142 | -47.57024 | 2025-08-15 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b92ad6e7-b626-30ef-a78d-60c154fa6f1b | -2.909 | -48.30065 | 2025-08-15 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 574c93e3-e1ef-3064-abe7-f02565b8d3e7 | -3.54558 | -44.8377 | 2025-08-15 04:00:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93f08993-f21d-35aa-a964-f1e2c73bad6d | -3.11501 | -47.4989 | 2025-08-15 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87c16197-4d7c-30a1-b02c-b433955e960e | -4.1837 | -42.43209 | 2025-08-15 04:00:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 98a6b266-94c7-3144-8f34-46420cab1eda | -4.18855 | -42.42464 | 2025-08-15 04:00:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| de52e2e2-9ce5-39f6-97fb-6cec38f66eb6 | -3.3109 | -39.28172 | 2025-08-15 04:00:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6d640cb0-b001-3889-8afb-72b46c7904a9 | -4.39042 | -41.91595 | 2025-08-15 04:00:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 891b9fa2-02ac-3e0a-945c-e2054d06782f | -2.48649 | -47.57446 | 2025-08-15 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8531dfbf-2fe4-36e3-9199-c46a2dd87c28 | -3.32388 | -48.72095 | 2025-08-15 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3696170c-9ccb-35d0-9382-3ac39455f423 | -3.31849 | -48.72009 | 2025-08-15 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a9da3b5-8478-3475-82a1-296e3ae9854e | -4.59489 | -37.74286 | 2025-08-15 04:00:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f43ca239-d2f4-3df2-8653-8ddfafd9ce52 | -2.90577 | -48.25366 | 2025-08-15 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e135dab2-0a18-3893-b4dc-8bdc85bd451e | -2.91305 | -48.30527 | 2025-08-15 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f757f711-442f-3e64-a9ee-07d529180cc1 | -2.91156 | -48.25121 | 2025-08-15 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README19.md)
