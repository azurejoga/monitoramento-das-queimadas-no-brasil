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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43e7f24e-5ba0-3d46-81f7-bb7236b865cd | -14.3865 | -52.51823 | 2026-09-01 07:29:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| f623455a-d8f7-3a2d-95e7-1074fcb453c6 | -7.5894 | -60.4827 | 2026-09-01 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 4ce9cfae-79b7-3d36-9dad-c4b04981252c | -14.4011 | -52.5014 | 2026-09-01 07:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| d877811b-3c24-33ea-ab57-a41347a6abca | -7.571 | -60.4643 | 2026-09-01 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 436cae8b-396c-3a43-bec8-20991e2abf54 | -7.5709 | -60.4835 | 2026-09-01 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 669a8ce4-c884-3f0f-8497-7b9b549154f5 | -8.2602 | -54.9388 | 2026-09-01 07:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| a63c95b9-82de-3b94-96e0-dd75da30c38b | -7.5895 | -60.4636 | 2026-09-01 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 13e1d082-7d4a-3141-8196-f30bc6f47de0 | -18.25491 | -52.73814 | 2026-09-01 07:31:00 | AQUA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 95134f17-4ab5-3191-b743-5902643a594f | -18.25373 | -52.73038 | 2026-09-01 07:31:00 | AQUA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 2e6d2dd3-0772-31a7-afce-1a416bc10e82 | -7.5895 | -60.4636 | 2026-09-01 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 91fff2de-0e80-31c2-890a-5d77fdea492f | -7.571 | -60.4643 | 2026-09-01 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 04df4bb5-27c5-36b0-b221-801a7d5316f0 | -7.5709 | -60.4835 | 2026-09-01 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 345dda5d-cb26-3ca4-87de-fc3da90c3359 | -7.5894 | -60.4827 | 2026-09-01 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 292b900f-d525-3c61-91ca-d0345a952b89 | -14.4011 | -52.5014 | 2026-09-01 07:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 1cce75e3-2514-3184-8816-5f368b16c6c1 | -10.8206 | -50.7159 | 2026-09-01 07:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| dbb6143e-9820-3a4a-8474-65deac159295 | -7.8996 | -51.5857 | 2026-09-01 07:50:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 8445c019-e610-3892-8192-38d2f63eccce | -10.8396 | -50.7139 | 2026-09-01 07:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 85591a1a-7fe6-339a-8554-f079c9d1e2b3 | -7.5894 | -60.4827 | 2026-09-01 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 5f396029-561c-3959-8586-af7abcec0be8 | -11.213 | -46.0839 | 2026-09-01 07:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 18ea133d-29fc-368e-a6b9-98d2d6c74873 | -7.571 | -60.4643 | 2026-09-01 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 7abf340f-8bb9-3029-99dc-eca5f5d80f5f | -7.8994 | -51.6066 | 2026-09-01 07:50:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 9f23d1a2-fe40-315d-be54-446c9b957412 | -7.5709 | -60.4835 | 2026-09-01 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 9bfa8b2b-c975-305a-8835-cd6c39220887 | -7.5894 | -60.4827 | 2026-09-01 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| de07126b-5f76-31f6-b4da-965bc36fbf51 | -10.8398 | -50.6926 | 2026-09-01 08:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| c044b45e-5dfb-3dee-8dfe-4f4ed447ddba | -14.4204 | -52.4989 | 2026-09-01 08:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 0bbb5641-e42c-3668-8a55-25df4161821e | -10.8396 | -50.7139 | 2026-09-01 08:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| d8d34294-0fea-3fce-9540-210cadb2f036 | -14.4011 | -52.5014 | 2026-09-01 08:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| ca7ad78d-723c-3c7a-8ecb-76d6b2d5d5dd | -10.8206 | -50.7159 | 2026-09-01 08:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 5f759c30-8bb0-3912-8fa1-d2e40ea22f3c | -8.2602 | -54.9388 | 2026-09-01 08:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| af376e29-8bfa-3e0e-bd88-80c172634ca6 | -7.571 | -60.4643 | 2026-09-01 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 86b6dff7-c4bd-340c-b7bc-7c2b17b71699 | -7.5709 | -60.4835 | 2026-09-01 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 529eb286-8921-3f45-855d-3680570dd7b2 | -14.4208 | -52.4777 | 2026-09-01 08:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| d246948d-e3a9-3afb-880b-d22a7073f3eb | -7.5895 | -60.4636 | 2026-09-01 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| fd513ee5-b236-3445-9de2-4bac2199178b | -10.8209 | -50.6945 | 2026-09-01 08:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| cc40a1f9-c826-3633-ad68-4de537f63456 | -10.8398 | -50.6926 | 2026-09-01 08:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.0 |
| cc28a0d0-1fcf-3890-8573-724d80d8da2b | -14.4204 | -52.4989 | 2026-09-01 08:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| f030d575-f4fa-3680-8e9d-66ed513c52c8 | -14.4011 | -52.5014 | 2026-09-01 08:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 109.5 |
| f5393967-252c-32f0-8981-631c478125ae | -10.8396 | -50.7139 | 2026-09-01 08:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 131.6 |
| bc7cdc26-ba7c-38fe-a114-f7d6b85c8d9d | -10.8206 | -50.7159 | 2026-09-01 08:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 6e2076e4-3b36-33df-82c2-8fa3b13e0877 | -7.5894 | -60.4827 | 2026-09-01 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 62be3832-2cdc-3c58-8852-403205148e6d | -10.8398 | -50.6926 | 2026-09-01 08:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 37162b48-182f-3471-b91a-c608d13213cf | -10.8209 | -50.6945 | 2026-09-01 08:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 057b23a8-921e-3944-9825-b46eb1130af7 | -7.5894 | -60.4827 | 2026-09-01 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| c5d63839-e942-3c02-ada0-56541e2dcf30 | -10.8206 | -50.7159 | 2026-09-01 08:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 5a99e304-ecf4-393b-a06a-57e5a41eade7 | -10.8396 | -50.7139 | 2026-09-01 08:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 135.6 |
| acaa06c4-7199-3bdc-952d-70f1a62ece52 | -14.4011 | -52.5014 | 2026-09-01 08:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 2f80cd36-aace-3c12-a163-ec1e5f7a0e13 | -10.8206 | -50.7159 | 2026-09-01 08:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 1bbd51b5-b253-3086-80e8-af5f9230534f | -10.8398 | -50.6926 | 2026-09-01 08:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| d815e144-ca85-3fec-8d3d-dee702179ce2 | -14.4011 | -52.5014 | 2026-09-01 08:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| f97e3ec6-8891-3fc5-b256-7c48c78966be | -10.8209 | -50.6945 | 2026-09-01 08:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| a109a5da-9b52-3300-9277-e02fe0254071 | -10.8396 | -50.7139 | 2026-09-01 08:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 7a417793-41af-35e1-872d-4b380711d28d | -14.4011 | -52.5014 | 2026-09-01 08:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| ab37f9fb-e485-3b8f-b0b4-fa8a08ff7a40 | -10.8396 | -50.7139 | 2026-09-01 08:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 04a121c7-f11c-370d-bdf3-c5f51c026ae7 | -10.8209 | -50.6945 | 2026-09-01 08:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| b92eb50c-188a-34dc-a0b1-7a5e5bc77bd9 | -10.8206 | -50.7159 | 2026-09-01 08:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 124.9 |
| a887e9d8-adcf-3605-bcbd-001048a9dec6 | -10.8398 | -50.6926 | 2026-09-01 08:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| f9662300-789d-393e-988a-8eb1b14d4601 | -14.4011 | -52.5014 | 2026-09-01 08:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| d9a1c0f5-6fd2-31e2-ba4e-5c59ac070ced | -10.8206 | -50.7159 | 2026-09-01 09:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 8223a18e-a4cd-3838-9640-fd834840a1d3 | -10.8206 | -50.7159 | 2026-09-01 09:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |
| bac88ede-2433-3b63-8685-dcc852acfe3b | -10.8206 | -50.7159 | 2026-09-01 10:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 0beb9eb7-1f80-3f4a-b0d8-12db6d65a83d | -10.8209 | -50.6945 | 2026-09-01 10:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 114.7 |
| e1937df0-d654-3dbb-8d5f-527c2b653f3b | -10.8209 | -50.6945 | 2026-09-01 10:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| b4e837c6-ba54-36f2-8e05-9950d7e70d0d | -10.8206 | -50.7159 | 2026-09-01 10:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 1cb3de40-41cb-359e-bb2b-baa069118411 | -10.8206 | -50.7159 | 2026-09-01 10:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.9 |
| f168189c-3a72-3420-ac5d-f7b5ddf99737 | -7.9048 | -44.2577 | 2026-09-01 10:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 9b0c8d73-63c6-35bf-810c-486680413227 | -10.8209 | -50.6945 | 2026-09-01 10:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.6 |
| c5b612c5-18fa-399c-b13b-ae2b898044c4 | -10.8206 | -50.7159 | 2026-09-01 10:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 9c0a0df2-6419-3e08-a21a-1940ae128372 | -10.8209 | -50.6945 | 2026-09-01 10:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 73fa0257-5951-3c4a-9009-6330e693b64a | -10.8206 | -50.7159 | 2026-09-01 10:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 15cf910d-65f4-32d9-9d30-0dcc86a86b82 | -10.8209 | -50.6945 | 2026-09-01 10:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 5feff8a8-bcb8-3b08-8143-7c321c5314e1 | -11.5092 | -45.496 | 2026-09-01 10:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 11f38001-b315-3aa6-b95d-aabc39d37e0a | -11.5283 | -45.4933 | 2026-09-01 10:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 270.4 |
| fb4629c6-30ac-33e6-8613-2101c0e32917 | -11.5287 | -45.4703 | 2026-09-01 10:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 249.4 |
| 65c3c9eb-87d0-34ff-a668-98a75148a4da | -15.4429 | -52.681 | 2026-09-01 10:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 0a54850b-b6c3-3df6-a9de-8a88e878b526 | -6.9552 | -55.635 | 2026-09-01 10:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 40ea3a1b-aa92-341f-9226-ace95b717320 | -11.5096 | -45.473 | 2026-09-01 10:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| ab2d1cfd-623a-38f7-86ff-ac4cec9cbf8e | -10.8209 | -50.6945 | 2026-09-01 10:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| bf45229b-e461-32db-8203-d951fdd7ffc3 | -6.9552 | -55.635 | 2026-09-01 11:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 138.9 |
| 74045d92-976a-38f0-b19f-0dabc245f5a6 | -10.8209 | -50.6945 | 2026-09-01 11:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 139.8 |
| bb307ace-12d6-308f-89d4-1fd8c1dafbc5 | -11.5283 | -45.4933 | 2026-09-01 11:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 280.9 |
| a9150246-2600-3683-aae4-8524012e3f70 | -6.9553 | -55.6151 | 2026-09-01 11:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 7eb80aff-a0e4-3029-9504-ae0913238691 | -6.9552 | -55.635 | 2026-09-01 11:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 181.9 |
| 21a73c31-08e9-348c-8540-592c841e7949 | -11.5283 | -45.4933 | 2026-09-01 11:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 676.3 |
| a2365b92-9a6b-3108-a165-8fa5f9ccfeaa | -6.9553 | -55.6151 | 2026-09-01 11:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 5a17a67d-8c95-33ed-b378-df8db98d1c99 | -3.87495 | -44.04661 | 2026-09-01 11:10:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 9242c917-2923-354c-aaa9-36dc7018176c | -3.06503 | -40.82973 | 2026-09-01 11:10:00 | TERRA_M-M | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 16.5 |
| a7ec0490-8d0f-3ec7-8cb8-53a51649eb9b | -7.88806 | -47.08894 | 2026-09-01 11:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 7a7bed2a-5440-3bba-ba4e-656f9ef94fec | -6.80316 | -40.90901 | 2026-09-01 11:13:00 | TERRA_M-M | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 35.0 |
| f276bd6c-a5e4-37bb-bba1-e1f210c2d189 | -7.88928 | -47.0819 | 2026-09-01 11:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 72ff20f9-94fc-3d37-88d9-1735b365b116 | -11.21333 | -46.08698 | 2026-09-01 11:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 9d7406b5-e33a-32b4-bf69-3376e2ad0747 | -8.49944 | -44.73863 | 2026-09-01 11:13:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 27458369-203b-3116-b698-8c3234ad2b93 | -6.80466 | -40.89887 | 2026-09-01 11:13:00 | TERRA_M-M | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 0f35af9c-ea38-3df4-bc7b-6a5981bf3c86 | -11.91687 | -45.06565 | 2026-09-01 11:13:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e059d8a1-c30c-357a-9570-63d030a680aa | -10.44591 | -46.73131 | 2026-09-01 11:13:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 76bf1a54-b6a5-3878-9c95-3ed7d6c5348e | -11.26314 | -45.12164 | 2026-09-01 11:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 9929933b-d3fa-3d52-b321-697bb0ec6efc | -11.67964 | -42.16333 | 2026-09-01 11:13:00 | TERRA_M-M | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 12cc5791-ee0d-3edb-886f-13300c8827f2 | -11.22629 | -46.08885 | 2026-09-01 11:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 4470b002-ce94-3a7f-8134-c60dab67dea0 | -10.45391 | -46.72661 | 2026-09-01 11:13:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 2d0e927a-527e-3160-a136-e136c43cb95c | -7.25332 | -39.21263 | 2026-09-01 11:13:00 | TERRA_M-M | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 0426a43a-298a-3cdd-a45c-bd156eb43733 | -7.24317 | -39.22031 | 2026-09-01 11:13:00 | TERRA_M-M | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |


[Clique aqui para ver as próximas entradas](README91.md)
