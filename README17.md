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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5fa5280f-efd8-3fdf-97bc-b01b680a6aa9 | -5.92 | -43.6032 | 2026-08-19 02:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 97f6947a-ffaa-33dd-87c7-3fd23ec4c283 | -6.0912 | -57.9187 | 2026-08-19 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 8aef8e02-5c03-3810-864e-078e4ada376d | -5.4319 | -48.3996 | 2026-08-19 02:30:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 602b4697-34f5-33cf-944c-5d210e5c798d | -5.9198 | -43.6264 | 2026-08-19 02:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 168.8 |
| daabd1ac-4ba0-3c5c-9536-37f70fd57eb5 | -5.9995 | -57.8444 | 2026-08-19 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 5bd0b15e-e4c9-3571-9dbe-3c69fa3dc9e7 | -6.8593 | -59.0318 | 2026-08-19 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 8d84f9d2-933f-3f1d-8bcc-726f9724e53c | -9.3875 | -60.5528 | 2026-08-19 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 37.0 |
| b0450701-1a76-382c-bcd8-190df36973f5 | -21.4442 | -48.5236 | 2026-08-19 02:40:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 09de1085-32b9-31fe-9b54-4259bf5884c8 | -19.7442 | -57.9425 | 2026-08-19 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.0 |
| d0397b4c-a845-3488-b2b6-4cba34fe9108 | -5.4319 | -48.3996 | 2026-08-19 02:40:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 816bab9b-200e-34e7-a30a-59940bb2879b | -6.0912 | -57.9187 | 2026-08-19 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 87baa216-9559-3ef1-821f-98ad272c157d | -9.406 | -60.5711 | 2026-08-19 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| f958677b-6df3-317c-bd14-6019fe23a8c8 | -5.92 | -43.6032 | 2026-08-19 02:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 524c2565-6ebd-3e28-9ae5-d540c30f9e06 | -9.4257 | -60.416 | 2026-08-19 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 4b361eaf-f522-366c-b232-cc49ddb472d3 | -10.4272 | -61.1905 | 2026-08-19 02:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 39.3 |
| ccaba5b1-1806-381c-9192-8ea95c89d1cd | -5.9994 | -57.8639 | 2026-08-19 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 3ed6a6af-ccb7-3b51-a547-e79b923e9b33 | -16.2552 | -57.6647 | 2026-08-19 02:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 45dff6a7-5f12-33d3-8c99-48d5a2d41c9f | -9.4256 | -60.4353 | 2026-08-19 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 7a4f1edd-7bd9-3f5c-ad2e-5e03544f1952 | -5.9011 | -43.6279 | 2026-08-19 02:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 273f8f4e-165e-3b7a-8524-23e3e2e0027c | -9.4061 | -60.5518 | 2026-08-19 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 47d7442f-b5c6-3408-914a-d8c57fb2088c | -9.3873 | -60.5721 | 2026-08-19 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 37.9 |
| e12bd32b-7df4-35e9-8778-9bbde5645a5b | -5.4317 | -48.4212 | 2026-08-19 02:40:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 168.8 |
| 87cef583-f4b8-3af8-9c4b-aec12e9ec73c | -6.6938 | -58.942 | 2026-08-19 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 525798fd-bb03-3320-ab80-8ce5f5eb82f9 | -5.9198 | -43.6264 | 2026-08-19 02:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 189.8 |
| 5d39fcbd-0d95-3132-880d-1a693fc1c3f3 | -6.0728 | -57.9194 | 2026-08-19 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| db3dcbe3-abd5-3ceb-acfb-4f50e786aaa9 | -6.0912 | -57.9187 | 2026-08-19 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 8375c317-72b3-3bce-8b0f-a940e3eb928d | -5.9011 | -43.6279 | 2026-08-19 02:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 0518441a-abc6-3727-bbdc-e0c658ea78c5 | -5.9994 | -57.8639 | 2026-08-19 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| a6aa225d-9b9e-3bdf-b330-ec64dfbef762 | -6.6938 | -58.942 | 2026-08-19 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 4a45442f-56c8-3c5b-b9fb-6dd05821072b | -6.0178 | -57.8631 | 2026-08-19 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 396ec3e9-d1af-30e9-b719-6ca78b76a494 | -5.4319 | -48.3996 | 2026-08-19 02:50:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 867aac43-6507-335c-82d0-53777ca6d8c5 | -5.4317 | -48.4212 | 2026-08-19 02:50:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 595fabf1-c8bb-32d4-ac9a-32b57accd1ac | -5.9995 | -57.8444 | 2026-08-19 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| b3e56f9c-418d-3b3c-980d-de0979eccb6c | -6.7123 | -58.9412 | 2026-08-19 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 80e9320f-5262-3bf9-b86d-ad403b268143 | -6.0913 | -57.8992 | 2026-08-19 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 783e346e-984f-3e1d-a58b-3b557e4af0d2 | -5.92 | -43.6032 | 2026-08-19 02:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 70c7ed25-440a-37a7-84ed-539387b35615 | -19.7442 | -57.9425 | 2026-08-19 02:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.9 |
| e53e2b5f-a8f0-3567-a604-aae2b1a5e685 | -5.9198 | -43.6264 | 2026-08-19 02:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 3c1b05bd-cf76-3a57-820b-985a62521f25 | -5.4503 | -48.4201 | 2026-08-19 02:50:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| c877b82e-9435-3cdb-9095-c5e49dfc2a43 | -5.4317 | -48.4212 | 2026-08-19 03:00:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 150.8 |
| e4e19a07-ccfb-31a1-8ffc-c11d8ebe1e65 | -19.7438 | -57.9633 | 2026-08-19 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.3 |
| f8cf63b2-b08e-39d5-ab77-d1cf6abcf078 | -9.3875 | -60.5528 | 2026-08-19 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 32706a1a-896d-3102-83c8-2f0f81ace262 | -19.7639 | -57.9607 | 2026-08-19 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.5 |
| 5320136f-0226-31ed-a2de-270425a8db90 | -5.4503 | -48.4201 | 2026-08-19 03:00:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 1ebbaedf-7305-3b0b-8763-03133238dd23 | -5.9995 | -57.8444 | 2026-08-19 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| c7127fb5-3680-31d0-b343-5b4b5a197cee | -5.92 | -43.6032 | 2026-08-19 03:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| f906d1fe-1700-3fc7-bb6c-1ffd102de73c | -19.7643 | -57.9399 | 2026-08-19 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.7 |
| 97f80045-30a1-303c-bfbb-58b8f45ef450 | -19.7442 | -57.9425 | 2026-08-19 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 217.3 |
| 58d2bb72-bd63-3dec-bb39-072837c4854a | -6.6938 | -58.942 | 2026-08-19 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 5f5dee34-09df-32a6-a86e-5f5a951f4dac | -5.9994 | -57.8639 | 2026-08-19 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 506cf45a-547e-3c5e-a0f7-3ffde253bea7 | -6.0178 | -57.8631 | 2026-08-19 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 68aac923-8d87-36d2-95b1-9b91a613fd00 | -9.4257 | -60.416 | 2026-08-19 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 6404a7fa-9ff8-31fa-9ee4-61e5e5f480d4 | -5.9198 | -43.6264 | 2026-08-19 03:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 63004fb4-4b95-3d76-9c30-f67fad93eeb8 | -5.9011 | -43.6279 | 2026-08-19 03:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 0f9f1249-84a9-3112-b5e9-439f007cca9f | -6.0912 | -57.9187 | 2026-08-19 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 26ecb8f5-09c5-3c96-bc63-0897c1156d00 | -19.7446 | -57.9217 | 2026-08-19 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.2 |
| 42719b37-cd48-3323-8acc-3158fff272c0 | -9.3873 | -60.5721 | 2026-08-19 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 9a618292-e2e5-3278-af84-7c8e6a4854cd | -19.7241 | -57.9452 | 2026-08-19 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.4 |
| e4407a42-0fe2-341d-9247-d724fdc2edb2 | -5.4319 | -48.3996 | 2026-08-19 03:00:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 983e7f91-06e9-3a0a-ae1f-b4e2ca8d29fb | -9.4256 | -60.4353 | 2026-08-19 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 72956b2f-1539-3b24-8444-f7b2fde7d70f | -5.9994 | -57.8639 | 2026-08-19 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 0dcb871d-8f35-38ee-b62d-905a0fc8e036 | -9.4256 | -60.4353 | 2026-08-19 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 3868ad3f-234d-3d00-9b21-4b842bcf969e | -5.4317 | -48.4212 | 2026-08-19 03:10:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 136.6 |
| cc504c7a-3f0b-3fe2-aae1-4f8cf846b4c7 | -5.4503 | -48.4201 | 2026-08-19 03:10:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| f54d7006-2bcc-3a6e-8f0e-ecb2b69ed7c7 | -9.4257 | -60.416 | 2026-08-19 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| b6da404a-e1a2-3037-853d-157ca83287dd | -19.7643 | -57.9399 | 2026-08-19 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.8 |
| a42fa79c-dd97-3eb3-bd76-37aade21961d | -6.0912 | -57.9187 | 2026-08-19 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 7c309bce-f6d1-3d49-9f76-9634de7835d1 | -5.92 | -43.6032 | 2026-08-19 03:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| d78b2928-bf2b-316a-9b7c-9b63d8a7f286 | -6.6938 | -58.942 | 2026-08-19 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| c63381d9-5fb0-3a60-8193-b6c7b2bc7582 | -5.9013 | -43.6047 | 2026-08-19 03:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| bff6d312-862c-3b64-a361-aa83f9e6d24f | -5.4319 | -48.3996 | 2026-08-19 03:10:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| d10bf36b-1818-3974-8ee1-e1db02c51482 | -19.7639 | -57.9607 | 2026-08-19 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.5 |
| d94f34a4-bb57-385b-8475-9f4a34d28dd3 | -19.7442 | -57.9425 | 2026-08-19 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.8 |
| 3dab7b12-6dbf-387a-a375-ba2378654a0b | -5.9011 | -43.6279 | 2026-08-19 03:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 12078f96-fbd2-351d-9f49-c038f0a9c4a7 | -6.0178 | -57.8631 | 2026-08-19 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| cc8d37ce-46f5-3c77-9636-de4c75aa351f | -5.9198 | -43.6264 | 2026-08-19 03:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 3538fa33-4175-34b2-88ee-8aaf5d7ced19 | -5.91 | -43.61 | 2026-08-19 03:15:00 | MSG-03 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e1a024c-83aa-31d8-ae2c-53b56cd93820 | -5.92 | -43.6032 | 2026-08-19 03:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 69fb72c8-dd28-3592-835c-9de93889be8d | -6.0913 | -57.8992 | 2026-08-19 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| acac5c64-e181-389c-b90d-c7ceef63a05c | -6.7123 | -58.9412 | 2026-08-19 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| db774187-1d11-3541-aa49-1a7645a44e78 | -5.4319 | -48.3996 | 2026-08-19 03:20:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 38047335-a4f3-3843-af5b-258e42e77303 | -5.9011 | -43.6279 | 2026-08-19 03:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 8bb3ac27-4279-39c3-b1cd-62f5ae676334 | -5.9198 | -43.6264 | 2026-08-19 03:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 179.5 |
| 0c59ca4b-49c0-386d-9266-70ae5900b135 | -5.9994 | -57.8639 | 2026-08-19 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| db58f759-e3e9-3601-95b3-11b8d3808f00 | -6.6938 | -58.942 | 2026-08-19 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| a54297a6-feec-3aa3-9b9e-047ed15912a0 | -5.4503 | -48.4201 | 2026-08-19 03:20:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 871022de-5d0d-3cab-a069-fe423842d365 | -19.7442 | -57.9425 | 2026-08-19 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.3 |
| e357eafe-2276-35fd-9f0e-4b7d7367259a | -5.4317 | -48.4212 | 2026-08-19 03:20:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 173.5 |
| 54895f09-a787-3446-9942-869e217f81ad | -6.0178 | -57.8631 | 2026-08-19 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 63c9c753-54a2-3993-bb7e-529ffa2363ea | -6.0912 | -57.9187 | 2026-08-19 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| aa4cf916-89d0-34bb-8207-c6dc4fbf21f0 | -19.7438 | -57.9633 | 2026-08-19 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.5 |
| 8f3aa610-6b84-31b0-9aaa-bf5e0b4ae7f5 | -5.9198 | -43.6264 | 2026-08-19 03:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 204.0 |
| 8f9de517-5557-3610-84eb-252b67179eb3 | -5.9995 | -57.8444 | 2026-08-19 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 50aa06d5-a476-37f1-8830-4fa0ddefe9bc | -5.9011 | -43.6279 | 2026-08-19 03:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 96917b84-7310-3f04-a89e-b7e998d88dc0 | -19.7639 | -57.9607 | 2026-08-19 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 142.8 |
| 8b2fcbd4-03a4-3e58-a7f9-7b6db5eeea88 | -5.92 | -43.6032 | 2026-08-19 03:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 0457be8f-59e5-370d-9478-eb029f59c702 | -19.7442 | -57.9425 | 2026-08-19 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.4 |
| 4fbc422c-2e76-341a-8a0d-07ac6eaf6271 | -5.4317 | -48.4212 | 2026-08-19 03:30:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 209.1 |
| 25dec7b4-2e2b-39d2-b636-b3d40a1eedea | -5.9994 | -57.8639 | 2026-08-19 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 4d654879-e79c-3191-b9d5-4e61137175c0 | -5.4319 | -48.3996 | 2026-08-19 03:30:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 127.4 |


[Clique aqui para ver as próximas entradas](README18.md)
