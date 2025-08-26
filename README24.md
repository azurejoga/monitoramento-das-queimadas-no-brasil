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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e86034f4-f659-312c-bba0-253ddc30f775 | -11.2937 | -55.1129 | 2025-08-26 03:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 63fbddf1-0455-3301-b8e9-5054c090bf01 | -9.1724 | -59.4436 | 2025-08-26 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| ebdf2f30-faca-3084-a50b-12ef3831e29e | -8.8363 | -62.451 | 2025-08-26 03:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 162.3 |
| 40c87e87-4513-3a9a-a2e3-bf4b20cfb4c4 | -6.7819 | -59.6711 | 2025-08-26 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 6e32c6b3-f437-390f-8eba-a31f9c94ead0 | -6.8413 | -58.9552 | 2025-08-26 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 3e906d29-b163-3d9a-b810-c5b825f50235 | -8.8548 | -62.4503 | 2025-08-26 03:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 224.5 |
| 8c9d1e1e-a158-3d20-a721-1d7277d6e0f2 | -4.9606 | -55.8028 | 2025-08-26 03:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 5a71c7e6-6301-302a-b3fc-c7c8c3b2a2de | -11.5207 | -52.142 | 2025-08-26 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 3fdd9119-ab8e-3d14-bbda-4619c5ad62dc | -7.3854 | -64.3475 | 2025-08-26 03:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 336a80a3-e660-3f97-ba1e-4a6aa412139c | -5.5281 | -60.2133 | 2025-08-26 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 87b44c7e-ba78-3e6a-bdeb-47d2625ef202 | -7.3854 | -64.3662 | 2025-08-26 03:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 322d9e0f-ab8e-3150-8ba8-aee5c3db113d | -8.9873 | -65.4379 | 2025-08-26 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 37e20885-95c8-3eb9-92e9-f6a5b9b405cc | -11.521 | -52.1209 | 2025-08-26 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 1b753d53-9b57-3ae4-86e3-fb47f0ad1e85 | -11.54 | -52.119 | 2025-08-26 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 02664f4b-4418-3605-9240-488ec617fc6c | -8.855 | -62.4313 | 2025-08-26 03:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 74ead119-6893-39c4-bff4-09f5a18d7721 | -8.8364 | -62.4321 | 2025-08-26 03:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 1fdb109b-6809-32fe-a8cb-cacc3f9e963e | -6.8044 | -58.9568 | 2025-08-26 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 4fae255b-71b4-399a-8114-eb779ffd842c | -6.2459 | -60.0174 | 2025-08-26 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 3c4b394f-3bf0-3f8c-bae9-fb25573c8e73 | -9.1722 | -59.4629 | 2025-08-26 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 6fe43bac-de58-30e9-bc22-f6f3dd27ca66 | -8.9874 | -65.4192 | 2025-08-26 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| a03ab2d6-c367-352e-a5cd-7955317f06e7 | -11.5397 | -52.14 | 2025-08-26 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 6c164ef3-997c-31db-965f-b32e0d823312 | -6.246 | -59.9982 | 2025-08-26 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 07f16c6b-0a6c-337f-beba-2dd38cd12dde | -8.8734 | -62.4495 | 2025-08-26 03:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 73.3 |
| d21665cb-8514-35ca-84d6-73f8559058b3 | -8.8734 | -62.4495 | 2025-08-26 03:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 5f3afc7c-0966-3f26-ab4a-c54055cc6e7b | -4.9606 | -55.8028 | 2025-08-26 03:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 6e54bfcc-ed5e-3d90-a9eb-85fb6f1e53e7 | -6.246 | -59.9982 | 2025-08-26 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 6b830e87-754c-3b7a-8bcc-900e34114f0a | -4.9605 | -55.8226 | 2025-08-26 03:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| c3bcf817-43f9-322d-ba33-83a2b89c06c9 | -8.8364 | -62.4321 | 2025-08-26 03:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 82.4 |
| db0e4ff5-449c-3d95-959f-eeae05d5f3c0 | -6.8044 | -58.9568 | 2025-08-26 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.0 |
| e8a51c9d-efa8-3875-ba52-8e34213ab920 | -9.1724 | -59.4436 | 2025-08-26 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 70bd1215-128f-3a54-9080-e3d3689b07b1 | -6.2276 | -59.9989 | 2025-08-26 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 39e8ce78-e395-3bed-9260-58c230321c51 | -9.1722 | -59.4629 | 2025-08-26 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| fddadeac-fab0-3b05-bcc2-dc690519ed0c | -8.8363 | -62.451 | 2025-08-26 03:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 150.2 |
| 0d91034f-f856-3955-9221-a6691ca71355 | -8.8548 | -62.4503 | 2025-08-26 03:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 232.9 |
| 43dc1dab-2bde-3792-8a78-800b8ab03e9b | -8.9874 | -65.4192 | 2025-08-26 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 88884502-f4f9-395f-b116-264a2b400593 | -6.8043 | -58.9761 | 2025-08-26 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 1b374745-efb2-32b0-90bc-ff52584315a2 | -6.7819 | -59.6711 | 2025-08-26 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| f705446f-019f-3a45-9990-8ec3e3eeaa65 | -11.2937 | -55.1129 | 2025-08-26 03:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 9763433f-b59e-30f8-a7b0-f1fda176d63b | -6.2459 | -60.0174 | 2025-08-26 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| e1dd6da7-d7ee-3700-b32d-3f05f4222b9a | -8.855 | -62.4313 | 2025-08-26 03:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 4a596751-bb12-3a0d-a214-c18c7b63a37b | -6.8413 | -58.9552 | 2025-08-26 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 9599ea97-26bb-38d1-82ed-d6e3bbb52989 | -9.006 | -65.4 | 2025-08-26 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 17416ec1-bfbb-3ad8-b939-0a52984c08b7 | -8.9873 | -65.4379 | 2025-08-26 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| ce75189e-f758-36fc-938e-62b6563e882a | -7.3854 | -64.3475 | 2025-08-26 03:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 2be5dfb7-217c-360c-9b94-92f6d71d6d3e | -5.5281 | -60.2133 | 2025-08-26 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 7cba44e2-cc22-31b7-8cad-66479adde4f1 | -6.7635 | -59.6718 | 2025-08-26 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 37e8e50f-270c-3d5f-8f20-ccb8ce87d96e | -6.8229 | -58.956 | 2025-08-26 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 8db8eaef-7deb-33ee-b928-0a2eaa5cfc4e | -10.4241 | -64.3903 | 2025-08-26 03:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 25.9 |
| fe1b27f6-cfe1-371d-b980-4ca06636238d | -6.2275 | -60.018 | 2025-08-26 03:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 876adac7-2f45-3e61-9680-c9fa2563187d | -6.8228 | -58.9753 | 2025-08-26 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 155.2 |
| f0a47620-7579-32c2-a9f1-351dd5932a57 | -7.3854 | -64.3475 | 2025-08-26 03:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 82daafaa-8ea8-3d7b-9bb7-ef059bd47956 | -9.1724 | -59.4436 | 2025-08-26 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| e63d3a4f-dee0-3f6b-ad4d-6d1c7fd62fd7 | -7.3854 | -64.3662 | 2025-08-26 03:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| b5ed4639-e701-38d9-8621-8aefc41eea65 | -8.8548 | -62.4503 | 2025-08-26 03:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 205.9 |
| c6dcf125-f7a8-3dfc-8208-fb7cf652b6b6 | -6.8229 | -58.956 | 2025-08-26 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 8df45b2b-2023-3dfb-8afa-d78c807a15dc | -6.8228 | -58.9753 | 2025-08-26 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 139.6 |
| 413adf78-b25f-37ab-a0e5-b3f8bc1029d2 | -8.8364 | -62.4321 | 2025-08-26 03:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 8f10e8b0-ae7a-3018-ae44-43e3053c569a | -9.1722 | -59.4629 | 2025-08-26 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| a5b2378f-9eb6-37fa-8557-9148a11e1db1 | -8.8734 | -62.4495 | 2025-08-26 03:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| bcb6ce8c-26b7-31e1-ae5f-48c719a38b1f | -8.9873 | -65.4379 | 2025-08-26 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 2dc361cf-3c49-3f99-ab1a-0ffac236b731 | -8.8363 | -62.451 | 2025-08-26 03:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 22a3d42d-b42d-3223-bc5f-915ce50eaa31 | -6.7819 | -59.6711 | 2025-08-26 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 4792907c-db03-3392-8b48-e03e51794ec9 | -6.8412 | -58.9746 | 2025-08-26 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| afa7bfd0-e8bc-37eb-95e3-43a97a25ba97 | -8.855 | -62.4313 | 2025-08-26 03:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 42ccd9eb-0dc8-30f8-8c60-6303ed1d5c72 | -9.023 | -65.7355 | 2025-08-26 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| a9a28c80-1460-3644-ab4a-f5f1d9a2d1be | -9.006 | -65.4 | 2025-08-26 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 850f88df-09aa-3a2b-95d9-fa11d3188a22 | -6.7635 | -59.6718 | 2025-08-26 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| c28bef6a-9a3a-3db9-9a43-819df974c8e5 | -8.9874 | -65.4192 | 2025-08-26 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.5 |
| a5dcbcaf-1b6a-3d44-ad6e-bf8cb47f6f60 | -6.2459 | -60.0174 | 2025-08-26 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 5cd79430-1c34-3597-962d-1f781c8e3f58 | -6.8043 | -58.9761 | 2025-08-26 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| d11b133a-e9a7-3dac-91db-90c471a78b5e | -4.9605 | -55.8226 | 2025-08-26 03:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 97f3aaaf-6898-3a2d-bbce-decb265d39b9 | -6.8044 | -58.9568 | 2025-08-26 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 14043b46-a957-3967-88e9-a8c6c186e51a | -6.2275 | -60.018 | 2025-08-26 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| d773fe0d-a722-3e07-9971-da74053579e9 | -3.98258 | -47.8861 | 2025-08-26 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 33a1030d-d8f4-34d0-948b-55b827f5456f | -5.88206 | -36.80149 | 2025-08-26 03:53:00 | NOAA-21 | SÃO RAFAEL | RIO GRANDE DO NORTE | Brasil | 2412807 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b0f95244-54b5-391d-9244-3c2f87f32a61 | -3.98445 | -47.88677 | 2025-08-26 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c994cf11-14d4-3227-82fc-d326d22588cf | -5.15318 | -38.05492 | 2025-08-26 03:53:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 504cc358-107e-306b-9ed6-c75437d1178c | -5.47122 | -42.60742 | 2025-08-26 03:53:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| dbfbbd28-358e-3e9c-b63c-679a63cc7d10 | -5.46738 | -42.60677 | 2025-08-26 03:53:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 0a784db2-8ed6-3e3a-a6ff-cfabc109a5b8 | -4.62791 | -41.40175 | 2025-08-26 03:53:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ee117a00-7c8e-31d2-bbfa-e3cf028a77cb | -3.25633 | -46.91301 | 2025-08-26 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 38c98af9-1112-3f96-bde2-c3edad5a1d88 | -3.98375 | -51.06181 | 2025-08-26 03:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f676053-0aa7-320c-94eb-1934b3cc3b9b | -3.16768 | -49.48008 | 2025-08-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 542b28d1-68ea-3172-96eb-d73cceb27ec1 | -4.84947 | -42.8881 | 2025-08-26 03:53:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| e4d00483-f228-3c2d-b894-64704c134f99 | -5.46665 | -42.58715 | 2025-08-26 03:53:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 1ad8db03-aac3-3d33-8d2f-ad6478c4546c | -3.17023 | -49.48094 | 2025-08-26 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 83ec77f4-7e3e-3b8d-8c1e-3c141ee8f2fb | -3.97844 | -51.06099 | 2025-08-26 03:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 100a353f-f8fa-3c8c-b5de-f070f886635d | -3.25579 | -46.91633 | 2025-08-26 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c9b65356-a100-367a-b958-461cbec079f8 | -4.48545 | -47.66905 | 2025-08-26 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 331a9e03-56b4-3503-b761-4ee4bb1f1e16 | -3.06429 | -40.04768 | 2025-08-26 03:53:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 22.3 |
| e5a6975a-2dc3-345a-9462-8ef455288890 | -3.25158 | -46.90874 | 2025-08-26 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ec01d31-3625-326c-9cb1-dfb0dd6f1364 | -4.66206 | -41.42064 | 2025-08-26 03:53:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3cadac00-499c-3a8b-88ab-09393b05d4af | -5.50061 | -41.41376 | 2025-08-26 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 49dedb98-4276-34ec-b701-529e43cd2ef0 | -1.83328 | -44.88953 | 2025-08-26 03:53:00 | NOAA-21 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cd60911-a949-3c64-96bb-36a1f1bb1469 | -3.25688 | -46.90968 | 2025-08-26 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3eb72e6f-ab2d-3c8e-8fc5-649f91b1307c | -4.07447 | -48.04433 | 2025-08-26 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45fe0bb6-0d2c-3527-b100-9ad1e821829b | -4.84864 | -42.89318 | 2025-08-26 03:53:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6598d10b-6585-39c6-bb5d-98901fc80663 | -3.9851 | -47.88286 | 2025-08-26 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c38054b2-221b-35e2-9cc3-5775c723be8c | -2.48644 | -47.75446 | 2025-08-26 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b2dd487-19c3-3a11-9940-7ef5ef2b3bf3 | -3.24628 | -46.90778 | 2025-08-26 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README25.md)
