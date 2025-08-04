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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9491f334-00f6-3647-b665-0f78a37ac141 | -6.656 | -59.0981 | 2025-08-04 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 99f2d21a-7d56-3d52-a5a5-ee4f68fd3e37 | -8.0132 | -43.1278 | 2025-08-04 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.1 |
| c2809001-434c-301d-b3a9-46824a71fbd3 | -7.9934 | -43.2005 | 2025-08-04 01:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 71.8 |
| e66fa75b-7383-3715-9611-22d291dcacd3 | -4.7346 | -44.4457 | 2025-08-04 01:40:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| edd3280c-2491-3ceb-a6c0-721c7f17268b | -8.0126 | -43.1749 | 2025-08-04 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.9 |
| a040ebad-3dee-3f0d-a639-0f708e46411e | -6.6144 | -59.9656 | 2025-08-04 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 92ebbeda-0a39-3061-876a-2467a198fd45 | -6.6329 | -59.9649 | 2025-08-04 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 5c30eee4-0f09-3235-8a73-c78812873cdd | -8.0123 | -43.1984 | 2025-08-04 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| 86f41bc4-c14a-3785-a728-66e7edc90460 | -6.656 | -59.0981 | 2025-08-04 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 5fdd8764-db6d-3a5b-8551-f39463742d84 | -7.9934 | -43.2005 | 2025-08-04 01:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |
| 96001054-012c-37f6-9333-1f2d313c8852 | -8.0129 | -43.1513 | 2025-08-04 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.9 |
| 4f662c6b-9313-36fc-a055-8b09e0db15e3 | -6.6144 | -59.9656 | 2025-08-04 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 23211a39-f1a2-33b4-b098-22bc8ecd92c6 | -6.6329 | -59.9649 | 2025-08-04 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| f553d62b-beb4-32b8-bba7-725ce5e3078e | -4.7346 | -44.4457 | 2025-08-04 01:50:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| ec92aad5-e8e8-3f2c-8f95-330c869c2384 | -8.0132 | -43.1278 | 2025-08-04 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| e0ae6216-e890-3cd2-bbcc-354cb55ceba2 | -21.1418 | -49.0559 | 2025-08-04 01:50:00 | GOES-19 | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.7 |
| a4425ee0-2567-3186-9ab2-20f19db96949 | -7.994 | -43.1534 | 2025-08-04 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| 567a8e98-b68a-35c5-bcc7-bc214c897239 | -21.1624 | -49.0512 | 2025-08-04 01:50:00 | GOES-19 | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.9 |
| c26a3bd0-fabb-3445-9c7b-bfc647aec255 | -8.0123 | -43.1984 | 2025-08-04 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |
| 3edf0419-b4f4-3250-adff-fa4da391da74 | -8.0126 | -43.1749 | 2025-08-04 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 642512c1-71fb-30a3-a533-64be6f25ef5e | -6.1465 | -57.9165 | 2025-08-04 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| eb2f1cae-1243-3141-b4b8-f30e7cb3e1f4 | -7.9934 | -43.2005 | 2025-08-04 02:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 66.3 |
| 872c4260-1465-343b-8664-3a8e17ce5c50 | -21.1418 | -49.0559 | 2025-08-04 02:00:00 | GOES-19 | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.9 |
| f7c3a197-ccb7-3a78-8ff6-7381f7cac752 | -7.994 | -43.1534 | 2025-08-04 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| b9282d90-6c80-3115-96ce-55735f943384 | -8.0123 | -43.1984 | 2025-08-04 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.1 |
| 9ea81ff5-c1aa-3ddf-b736-d716754285ab | -8.0129 | -43.1513 | 2025-08-04 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 8a153306-fa9b-39a2-912f-9d01bb3608b4 | -8.0126 | -43.1749 | 2025-08-04 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 8a170d80-b042-3e14-86ce-9a8cc8ef19c1 | -6.656 | -59.0981 | 2025-08-04 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 932d6521-74fe-3951-85bc-b4c059be45f8 | -6.6144 | -59.9656 | 2025-08-04 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 4444865b-49c1-310d-8a34-b973b3a6e88b | -6.1465 | -57.9165 | 2025-08-04 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 8d338290-2842-398e-9f64-f778154e4715 | -6.6329 | -59.9649 | 2025-08-04 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 9ca2f823-dfc7-3d0c-9280-60417eb9c4e1 | -21.1624 | -49.0512 | 2025-08-04 02:00:00 | GOES-19 | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.6 |
| 0a14a712-b491-339e-9739-f86ac39a6b33 | -8.0132 | -43.1278 | 2025-08-04 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.9 |
| bd54bb78-4bf2-36db-a00e-72efe649329e | -8.0129 | -43.1513 | 2025-08-04 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 125.4 |
| 1ace6b06-6a83-3cbd-88fe-1331fcb4403b | -8.0123 | -43.1984 | 2025-08-04 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.0 |
| 958e6caf-c0cf-3fcc-85da-7f7ffc7f60ba | -7.994 | -43.1534 | 2025-08-04 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.8 |
| 02904693-fbd6-3bc3-b646-06a8fffd9149 | -7.9934 | -43.2005 | 2025-08-04 02:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 67.6 |
| ca26c671-1a0a-36c4-ac2f-4cd353b43246 | -6.6329 | -59.9649 | 2025-08-04 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 3ec7cf9d-ea0c-37e1-a8d0-63e740c4fe9d | -6.656 | -59.0981 | 2025-08-04 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 7a0c9101-d49d-3665-8bc5-3f12b382bb79 | -7.0208 | -59.8346 | 2025-08-04 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 48a71330-29c8-3851-9126-3cb2d2c5fe57 | -6.6144 | -59.9656 | 2025-08-04 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 37b71580-7a34-30be-8f6e-1acffcd5de32 | -8.0126 | -43.1749 | 2025-08-04 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.2 |
| 839f433f-8a47-365a-a0bd-35d3e4f4c729 | -8.7259 | -46.4009 | 2025-08-04 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 47.3 |
| b93fe266-71cb-339c-873c-19c3cb6d1b95 | -6.1465 | -57.9165 | 2025-08-04 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 26adc205-c3d1-395a-b297-0a5d0173cbe4 | -8.0132 | -43.1278 | 2025-08-04 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 10b640ab-bce5-3f3f-84a6-6085153302fd | -6.656 | -59.0981 | 2025-08-04 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| ea3c92b4-8e72-3e08-a4e5-9eba63e83e5f | -8.7259 | -46.4009 | 2025-08-04 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 45218929-9541-37d0-8633-438d225b30b2 | -7.9943 | -43.1298 | 2025-08-04 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.2 |
| 64b009ca-6aea-342b-b6f4-c2aba54a1e54 | -7.994 | -43.1534 | 2025-08-04 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| 8b7a09a0-1b62-3a01-bb34-1614c6653c50 | -6.6329 | -59.9649 | 2025-08-04 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| f8036f6f-ebf1-348a-a5e8-a6de23133b88 | -8.7448 | -46.3989 | 2025-08-04 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| d8a04780-b00f-3caf-88c8-1bf52192b8b7 | -8.0132 | -43.1278 | 2025-08-04 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| a197f2ce-6a45-3c89-bc06-d05fb53a2439 | -8.0123 | -43.1984 | 2025-08-04 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.1 |
| df575537-e61d-36f4-b22b-3f8c7cc12c81 | -8.0126 | -43.1749 | 2025-08-04 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.3 |
| 69cf5513-f152-3a00-bf3a-a6ed554ebe11 | -8.0129 | -43.1513 | 2025-08-04 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| da86dd49-0c61-3643-b681-c3fa5cc269d6 | -7.9934 | -43.2005 | 2025-08-04 02:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 60.1 |
| 64ff420c-3648-38bd-a3ed-594850c9dd07 | -6.6144 | -59.9656 | 2025-08-04 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 9071d6cf-5fe3-3a4a-8cbe-5b0d02677047 | -6.1465 | -57.9165 | 2025-08-04 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 82813c21-7343-33dc-9b15-713f471a5331 | -9.98656 | -67.57198 | 2025-08-04 02:24:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 01691636-c5ec-389d-ad11-2b39e21323e0 | -9.9466 | -67.585701 | 2025-08-04 02:29:00 | METOP-C | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 28aca36a-0341-3b09-8078-c7ad72808249 | -8.012 | -43.2219 | 2025-08-04 02:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 44.7 |
| a7f1293d-74bc-321b-846f-60c0c65d6925 | -6.6329 | -59.9649 | 2025-08-04 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 2fb1a71a-f29b-32b0-9bf8-10e217751d93 | -6.1465 | -57.9165 | 2025-08-04 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 54135953-fb44-3215-a8ca-342b5989e710 | -7.9931 | -43.224 | 2025-08-04 02:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 47.4 |
| e1b082c5-ba69-367c-980f-8701d233ccbc | -7.994 | -43.1534 | 2025-08-04 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.0 |
| a9b614b5-1e9c-38f1-b0cf-429229804b35 | -6.656 | -59.0981 | 2025-08-04 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| c958b376-b1c9-3cd1-9ce3-9dd334189b34 | -8.0132 | -43.1278 | 2025-08-04 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.5 |
| d5bcb7fa-a499-352f-ae94-8c49656e1bc5 | -8.0123 | -43.1984 | 2025-08-04 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.1 |
| 6436c41a-cef9-31b9-8dca-c7c53ebc8d2c | -8.0126 | -43.1749 | 2025-08-04 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.2 |
| c157cc90-ce7d-33ca-8a8b-c9ca1f2b141d | -8.0129 | -43.1513 | 2025-08-04 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 127.7 |
| d999e9ae-b71f-3ba2-a5bd-b2b68baa4679 | -6.6329 | -59.9649 | 2025-08-04 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| d455486d-0180-36b3-a5cb-baee681911d6 | -8.0129 | -43.1513 | 2025-08-04 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| f2d7d742-f0d7-3646-b719-d4801c758d63 | -6.656 | -59.0981 | 2025-08-04 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 7a1368a4-2b6c-36b5-8cd8-f19345b4c124 | -7.994 | -43.1534 | 2025-08-04 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| 115d55a2-fd4b-3ef6-964a-2c0dcf15ac2c | -7.9931 | -43.224 | 2025-08-04 02:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| a7a070fe-6d99-35b7-a1b1-f9bd81983e16 | -8.0132 | -43.1278 | 2025-08-04 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.9 |
| 3652a0c8-d5aa-3bfd-9e08-c1a932ffedbc | -7.9934 | -43.2005 | 2025-08-04 02:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| be1d40e8-74f5-3cf3-b0e6-3a336bfd85c0 | -6.1465 | -57.9165 | 2025-08-04 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| c6c09087-5579-390f-af50-205b076cf618 | -6.6329 | -59.9649 | 2025-08-04 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 4d7ab815-ae80-39dd-8ac9-b41219ad60cb | -7.994 | -43.1534 | 2025-08-04 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 0d9b61e9-9df3-3fa3-a644-726726faf6e4 | -8.0129 | -43.1513 | 2025-08-04 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.6 |
| 1d644618-9a14-3921-badb-e38fc9c657b6 | -8.0132 | -43.1278 | 2025-08-04 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.5 |
| 8d9b1ad7-d188-3b76-91c2-a6aaf34f1e14 | -6.6329 | -59.9649 | 2025-08-04 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 67ba84ca-9be9-3b04-b69f-cdf6d5bdd960 | -7.994 | -43.1534 | 2025-08-04 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| 2c072245-9ad0-3bdb-b918-02aa2787d322 | -8.0132 | -43.1278 | 2025-08-04 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 6c8b1af4-5b8c-3ab5-b9e9-e797ceb3b925 | -8.0129 | -43.1513 | 2025-08-04 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| 0962f96a-1103-38d5-9c3f-1b5f98ed11b0 | -6.656 | -59.0981 | 2025-08-04 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 2edca567-e90f-38ed-9558-c9285ec4ea23 | -21.1405 | -49.1022 | 2025-08-04 03:10:00 | GOES-19 | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.6 |
| 77f35243-afdf-33bf-8c5b-7ee59b05920a | -8.0132 | -43.1278 | 2025-08-04 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| 860694fe-abdd-3d42-8b86-24cd2d7d4159 | -6.6329 | -59.9649 | 2025-08-04 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 553535fb-2501-34a6-a8ad-f5c895edcacc | -21.1611 | -49.0976 | 2025-08-04 03:10:00 | GOES-19 | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.2 |
| bf9be1e6-713e-3a8b-a675-b3f20139c522 | -7.994 | -43.1534 | 2025-08-04 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.9 |
| e1f9bd17-c783-3180-9978-fb11276e4caf | -8.0129 | -43.1513 | 2025-08-04 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 123.4 |
| 85afe1f4-1eec-3a71-aa77-149dda30147a | -4.7346 | -44.4457 | 2025-08-04 03:10:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 20bcbcd3-31a6-37e1-a943-c6ffa59487a3 | -8.04423 | -43.10606 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 7b38c28e-29ca-37fd-8774-501201839983 | -8.0359 | -43.11145 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| bb854581-f65d-3dfb-8fe2-c1cb742500e1 | -8.04852 | -43.1087 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 69bec4e9-bca9-3ecb-83b3-9818bdd637c4 | -7.98982 | -43.1605 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 689b8d94-c190-3673-8bae-841f89ea4b3b | -8.00945 | -43.13485 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| c60a1dfd-6e8b-3d23-84e4-4c9e95e3d94e | -8.014 | -43.18675 | 2025-08-04 03:15:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |


[Clique aqui para ver as próximas entradas](README6.md)
