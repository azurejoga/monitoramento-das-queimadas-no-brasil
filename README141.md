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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a0b0304-7655-3378-b3b7-03661c4502a1 | 1.1507 | -50.7483 | 2026-10-07 15:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 95f89ef5-fea5-3a28-8b39-c9fdddb728e9 | -3.8384 | -55.9577 | 2026-10-07 15:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 939de203-2274-3148-bb30-e80d93a5187c | -9.0988 | -65.3596 | 2026-10-07 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| f831b12d-6db8-3714-9686-1717c2c1bb65 | -9.432 | -45.8293 | 2026-10-07 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| f0a226f2-1e81-353f-9d1a-9e8af37a6b7b | -3.1117 | -53.7032 | 2026-10-07 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| da84f10e-49b4-3e5d-b6e8-046947bf8013 | -3.5495 | -54.6352 | 2026-10-07 15:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 864dff82-2917-3644-8a08-e4de98a7347a | -3.4971 | -59.3286 | 2026-10-07 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 994f408e-8edc-3aa8-a9cb-35741e8686ef | -10.9949 | -45.4298 | 2026-10-07 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 9fa9eb3b-9ace-3f93-934c-bebcf4b54f68 | -3.5171 | -58.752 | 2026-10-07 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| fbf322a4-d550-3142-a0fd-a5da2c22056b | -9.0797 | -65.491 | 2026-10-07 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 6fc15872-931d-3dbb-bc14-96af48a7409d | -3.8382 | -55.9972 | 2026-10-07 15:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 167.5 |
| 97191dd8-6ba5-3061-a416-39b3e0fb51bd | -3.5312 | -54.6157 | 2026-10-07 15:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| c20ce358-2b9c-34de-92fd-ed4d1b988ab1 | -9.9175 | -65.0313 | 2026-10-07 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 436e375c-e177-3dc5-9fba-6fd35f4322db | -3.9843 | -56.2099 | 2026-10-07 15:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 626ca078-8166-3670-a1ca-d677a7f0bf46 | -9.1057 | -60.9511 | 2026-10-07 15:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| c9d27f59-9210-34fa-8241-9427caf75b1c | -3.2576 | -54.0418 | 2026-10-07 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 192.7 |
| 9983fb92-6d90-3115-9db1-c470283d4d72 | -4.1194 | -50.8192 | 2026-10-07 15:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 00cacffb-fc0f-3f06-94f5-6af40dce4b73 | -2.0447 | -54.3085 | 2026-10-07 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 156d5856-1b57-3511-afb1-fa1efd3c7551 | -9.1356 | -65.4145 | 2026-10-07 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| bfb05929-67fd-302e-a7a7-2d1d21f1351d | -2.1361 | -54.4671 | 2026-10-07 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 63b7404d-16ba-34e9-b177-eaf79d93a626 | -6.6879 | -45.578 | 2026-10-07 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.5 |
| fc7bcb46-3344-390d-83c1-caaf0fbbe754 | -9.1174 | -65.359 | 2026-10-07 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| c0acc937-5b23-3d2f-b0d2-8a718496a51e | -3.1098 | -54.2665 | 2026-10-07 15:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 925a2c8a-4864-3f60-9e7a-b2d438738708 | -1.5118 | -54.8352 | 2026-10-07 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| f5c03c1c-74b2-3868-a3a8-f51951ac1519 | -3.9675 | -55.8157 | 2026-10-07 15:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 484108ad-346b-3e16-b05b-2796c180f256 | -3.295 | -53.8597 | 2026-10-07 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 216.6 |
| 158e0471-144e-379f-b24d-a0bf53e9ff31 | -2.9451 | -54.0497 | 2026-10-07 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 0f7465d5-43a1-3352-9900-cdd35d62dfd4 | -8.5912 | -67.3084 | 2026-10-07 15:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| d939cd03-ced3-3e23-8ab9-212ca9781ce6 | -4.0025 | -56.2487 | 2026-10-07 15:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| ee622922-5dfa-3020-bdca-01fb4107e142 | -1.5118 | -54.8153 | 2026-10-07 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 8a5838c9-66e2-3362-88f4-2e8061c630da | -3.8383 | -55.9774 | 2026-10-07 15:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 298.5 |
| bee8a915-d270-36a7-a3b4-58aa95864e9d | -3.3135 | -53.839 | 2026-10-07 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 9b6b1096-c03c-387a-939f-c6238948a974 | -3.0375 | -53.8865 | 2026-10-07 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 55cb2307-f37d-3d01-99b7-ba38fcb02d5f | -2.4988 | -56.1266 | 2026-10-07 15:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| dc8e503a-d785-3ed5-a5bc-b8f0ca9433a6 | -11.2337 | -44.8446 | 2026-10-07 15:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 7f52db22-c762-317d-bd7a-9bcf9849c7cb | -3.0932 | -53.7441 | 2026-10-07 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 7c5bac5e-4f0e-315a-a38a-7747f99e2c47 | -2.1361 | -54.4471 | 2026-10-07 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 15e29649-b4f3-3262-80f3-27f61f5d7a47 | -2.9327 | -58.3204 | 2026-10-07 15:30:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 78610416-f5a3-3d8e-a397-7654105aac57 | -3.476 | -54.6172 | 2026-10-07 15:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 7b2f65a8-7692-3891-bc04-8def6e838eb9 | -4.4277 | -55.6431 | 2026-10-07 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 02a7696f-ae96-32c4-851d-34a8e27ab430 | -3.0191 | -53.9071 | 2026-10-07 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 55a2d170-21e5-3edc-97b5-49f341601ca3 | -3.5862 | -54.6541 | 2026-10-07 15:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 298b6e21-f744-3428-9c65-35de64c6063f | -1.4752 | -54.7759 | 2026-10-07 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 224.7 |
| f7e1dd06-590b-3e5b-b07c-74532580c3be | -3.3134 | -53.8592 | 2026-10-07 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 204.6 |
| ef4bb763-dd6e-3854-9235-d5e26255a42b | -3.6381 | -55.5084 | 2026-10-07 15:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| aee39830-8753-3d54-989c-ef15de478302 | -3.4496 | -56.9303 | 2026-10-07 15:30:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 159.0 |
| 22e9eeeb-5371-37e7-b844-d75f8ba139c5 | 1.8038 | -55.5261 | 2026-10-07 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| ccbd491a-1f4e-39eb-8a59-b3916bac31cb | -9.1363 | -65.2835 | 2026-10-07 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| cbf92dd3-ed33-358d-ac9e-d5d84253e249 | -2.4245 | -56.5402 | 2026-10-07 15:30:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| ed0db1a1-4074-3f4b-b38d-397858971783 | -3.4312 | -56.9502 | 2026-10-07 15:30:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 9ae49403-4df1-39d8-80cb-6be693f64f4c | -2.9271 | -53.9295 | 2026-10-07 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 65ee6323-67c6-318d-b462-3a2ede354ea3 | -10.6199 | -60.4852 | 2026-10-07 15:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 185.2 |
| daeeaaf7-6ef3-3a35-bd07-88399129cd56 | -8.5367 | -67.032 | 2026-10-07 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| ed242144-be11-38f8-a7e4-a11607778a5d | -1.2455 | -49.062 | 2026-10-07 15:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 0270f615-7519-3846-ac32-83891e0b2cd0 | -3.6197 | -55.5089 | 2026-10-07 15:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 175.2 |
| 743339cf-a873-3e25-af5a-2c0fc3567c7e | -3.1299 | -53.7633 | 2026-10-07 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 92147c20-bd09-3838-998d-7ef735a5cb4b | -9.0612 | -65.4729 | 2026-10-07 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 79cf9ca4-78d2-3a2d-a169-9669e4fb3469 | -8.6291 | -67.0482 | 2026-10-07 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| d05350f7-4196-3260-972a-ac64f4c69c5d | -9.0046 | -65.6988 | 2026-10-07 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| e008d439-b67f-31ac-9130-62535b2dbfd4 | -0.4136 | -52.0151 | 2026-10-07 15:30:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 8931bbde-ca02-3018-b44f-4746e477d79a | -0.3952 | -52.0152 | 2026-10-07 15:30:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 19d1a9f5-6c1e-3c7e-8749-90d77154ac6d | -9.3394 | -65.4638 | 2026-10-07 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 221a81b6-eeea-319a-88a4-78fe7d5a7d57 | -1.2922 | -54.5585 | 2026-10-07 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| de262909-137d-3492-95b9-99ef4c859806 | -3.4495 | -56.9498 | 2026-10-07 15:30:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 124.4 |
| d8132d3d-ae38-3727-a369-e3c508b82cc7 | -3.2945 | -54.0006 | 2026-10-07 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 9e072d6d-e200-3d9c-b914-05c49175071e | -3.5875 | -54.3138 | 2026-10-07 15:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 398965dd-d8e1-3618-97b0-e5bc8dbfad64 | -3.2215 | -53.8616 | 2026-10-07 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 0a56e065-0cd2-3bf7-8b84-3e75a37305a3 | -9.1408 | -64.3836 | 2026-10-07 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 922b2f38-f0c9-3776-979c-670278e61a80 | -3.0074 | -57.7384 | 2026-10-07 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 27eb5321-ca7e-3e31-823f-424fdf8da596 | -3.0074 | -57.7578 | 2026-10-07 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| c1350536-7d5a-3168-8fb9-b44341119383 | -3.0559 | -53.9062 | 2026-10-07 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 154.3 |
| 8409c933-bdaa-3728-b36a-28d77697a26d | -2.3889 | -56.1285 | 2026-10-07 15:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| fefcd498-2fe4-3361-bc19-430dc275f530 | -9.0987 | -65.3783 | 2026-10-07 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| efb9050d-b914-3a51-8a48-7fa832ce5090 | -3.1301 | -53.7028 | 2026-10-07 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 1e6b9efa-6c92-3bbb-aff7-efd4742de065 | -1.8803 | -53.9701 | 2026-10-07 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 5a25786e-aaaf-306f-95a3-a04fe74cbac6 | -12.1746 | -44.7051 | 2026-10-07 15:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 124.6 |
| adf1e883-28ec-30f3-ba9b-0c5f98bfab9b | -8.629 | -67.0667 | 2026-10-07 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 31bf1811-a83a-3ca3-9cff-efdda835348f | -9.6757 | -65.0401 | 2026-10-07 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| f59126a4-0c58-3b74-a8fd-049d060917c2 | -3.5678 | -54.6547 | 2026-10-07 15:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 9624aa54-43a7-37cf-a5a5-1835397b12d2 | -9.0612 | -65.4916 | 2026-10-07 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 7c9095b7-5078-3546-a566-9e8084031b93 | -1.4569 | -54.7761 | 2026-10-07 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 215.7 |
| d83df70c-8712-3e47-8582-6a2307c8afc9 | -3.6021 | -55.311 | 2026-10-07 15:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| f1ceca94-de06-3c63-b602-300a59082e2e | -3.8567 | -55.9769 | 2026-10-07 15:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 178.2 |
| 23285e21-ede3-3875-b2cb-3be0336a81d2 | -11.3745 | -46.6948 | 2026-10-07 15:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 46d49401-5c0a-3a9a-bff4-16cc61c33d1e | -3.4312 | -56.9307 | 2026-10-07 15:30:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 48d7e6b4-1cbf-3515-9fef-cd5aca63abca | -9.5176 | -67.1173 | 2026-10-07 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 2163227e-0adc-3f80-ae01-f7ba3cc29dd6 | -2.4989 | -56.1069 | 2026-10-07 15:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 10b50735-ce04-33ee-9ade-3ca9cfe2d8d4 | 1.5283 | -56.0227 | 2026-10-07 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 5ea422ce-038a-3f80-9539-ca20fbcd85e2 | -1.0244 | -48.8087 | 2026-10-07 15:40:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 8af2a9d4-81b4-3905-8698-22c10e0f4ebc | -9.6757 | -65.0401 | 2026-10-07 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.8 |
| ba579eac-81f6-3b9b-912b-2e7bd26533d0 | -2.7696 | -57.6653 | 2026-10-07 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 9499715c-8981-3004-9e82-ca5b88adf6b9 | 0.7266 | -51.3955 | 2026-10-07 15:40:00 | GOES-19 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 8fce0ae7-0911-38be-94ff-9ceec4e5e14b | -3.4496 | -56.9303 | 2026-10-07 15:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 217.9 |
| d1e65d96-d56b-3c98-88da-235a3541c627 | -2.3889 | -56.1285 | 2026-10-07 15:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| ff8f426c-de16-3471-9663-8db816b4b82d | -2.9819 | -54.0287 | 2026-10-07 15:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 846f4e01-86e4-3da6-9340-86eabccfd332 | -12.1746 | -44.7051 | 2026-10-07 15:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| c1030d99-6d46-3b11-b549-31c4a28c890c | -9.0046 | -65.6988 | 2026-10-07 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 86aef1d6-d392-36a1-8e20-1d08bbced74a | -3.4312 | -56.9307 | 2026-10-07 15:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 118.3 |
| a1c0bed1-7617-3e9d-a48b-00d5c077e422 | -3.6197 | -55.5089 | 2026-10-07 15:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 288.2 |
| afed17dd-c29a-3ede-9564-20028aff794d | -3.4068 | -58.9083 | 2026-10-07 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |


[Clique aqui para ver as próximas entradas](README142.md)
