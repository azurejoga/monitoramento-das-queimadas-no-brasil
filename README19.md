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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68e7321e-b0bd-330e-8bb6-c77234394512 | -14.3268 | -58.9405 | 2026-07-29 12:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| b56b2217-67f7-3b22-a2be-3069e7bd39a6 | -13.3097 | -45.7505 | 2026-07-29 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 1b655df4-556e-3977-8145-d669bbe3c6f7 | -6.8708 | -46.0126 | 2026-07-29 12:50:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| f30f3bea-d6fb-3bfb-8a0d-284ca5f231c5 | -14.3268 | -58.9405 | 2026-07-29 13:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 253ffef9-41d0-3146-ad59-e25f57a24da5 | -13.7373 | -51.9077 | 2026-07-29 13:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 10194f55-7382-3512-a468-6d339712863f | -13.3097 | -45.7505 | 2026-07-29 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 0a439262-d409-3120-ab3f-bb6ba85403eb | -6.8708 | -46.0126 | 2026-07-29 13:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 2a54cfde-fa29-3935-849f-128c228880f7 | -14.0695 | -53.9683 | 2026-07-29 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 335e1000-f00f-3326-8979-242ed6844be9 | -10.3239 | -49.6987 | 2026-07-29 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 3dd894c5-6f8d-3071-bc27-4cf1c0c58f07 | -14.3268 | -58.9405 | 2026-07-29 13:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| b867c7a5-43b5-3647-b492-1e54a16108e7 | -13.7373 | -51.9077 | 2026-07-29 13:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| a166db74-72cd-39e5-af85-4cc854230fd3 | -4.0333 | -43.263 | 2026-07-29 13:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 8bec4436-fb66-309a-a5ff-3cb4f2822b22 | -11.4105 | -46.8248 | 2026-07-29 13:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 83c3b54d-3357-35ee-a08d-3aaf4b8d83fe | -13.3097 | -45.7505 | 2026-07-29 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 415e27f7-d412-3546-ae6c-203511c09a81 | -6.8708 | -46.0126 | 2026-07-29 13:10:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| be513531-9c64-3147-aeba-2d1e0fa8fa69 | -10.3236 | -49.7202 | 2026-07-29 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 02e18465-0fbf-3bd1-bf8f-05a5bc6f7704 | -10.3236 | -49.7202 | 2026-07-29 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 2a90d4a4-8eb4-3b25-b34a-ac901d951fd0 | -10.3239 | -49.6987 | 2026-07-29 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 52c04646-feef-3a99-8212-72f2c9b12559 | -6.8708 | -46.0126 | 2026-07-29 13:20:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 1b836693-4427-3c73-a172-39ed1c06407a | -10.3426 | -49.7183 | 2026-07-29 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 17c4c14e-7dfc-3183-89c2-227a0d99ef55 | -13.7373 | -51.9077 | 2026-07-29 13:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 9aaec6ce-4aec-3081-bcd1-e3703e026821 | -14.0698 | -53.9475 | 2026-07-29 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 22b0f4ac-9f44-3967-b18f-ce3961251244 | -13.3097 | -45.7505 | 2026-07-29 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 9fa11e59-8b8c-3c5b-9af6-e1248564a5ee | -14.3268 | -58.9405 | 2026-07-29 13:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 91fb2cc7-e092-3374-93c2-3e94a0dbb2d7 | -10.3236 | -49.7202 | 2026-07-29 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 3d062c6a-8a9b-3184-88c6-ea547ff9c1ca | -13.3097 | -45.7505 | 2026-07-29 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 298.3 |
| 1218e244-348b-3a9a-b8f3-80562dbc428b | -11.4102 | -46.8473 | 2026-07-29 13:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 73aa68a9-8b4f-31ee-beda-969635c77fa9 | -11.4105 | -46.8248 | 2026-07-29 13:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| c0a979fe-da96-319c-bbd6-bed816684998 | -13.7373 | -51.9077 | 2026-07-29 13:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 61b2015e-465f-34bb-92c8-aa7dd35bd42c | -6.8708 | -46.0126 | 2026-07-29 13:30:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| fe846f26-a61b-338a-81f2-0cf87681ddea | -14.0117 | -53.975 | 2026-07-29 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 111.8 |
| deac8b0e-a55a-3dca-8237-9114dd2fcea8 | -14.346 | -58.9388 | 2026-07-29 13:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| e663ee62-b355-365a-a0a2-cf0fe23e1e6c | -10.3239 | -49.6987 | 2026-07-29 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| f018dc1f-3bb0-3cfb-a1b5-30496e69604d | -0.79388 | -66.12312 | 2026-07-29 13:38:00 | TERRA_M-T | SANTA ISABEL DO RIO NEGRO | AMAZONAS | Brasil | 1303601 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 768c663d-7e6e-3ad0-89e0-a680dd361d1b | -14.0695 | -53.9683 | 2026-07-29 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 1d9fef9c-51d0-33ac-ae7d-d81807d5b3fd | -11.4105 | -46.8248 | 2026-07-29 13:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| b9d04562-dbdb-3c09-9bc5-984a7a32d5dd | -13.3097 | -45.7505 | 2026-07-29 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 553b7367-d17b-36ac-8102-d226c56936f3 | -6.8708 | -46.0126 | 2026-07-29 13:40:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| a4f8b8a8-411f-3e9a-b807-6611a8767b0c | -13.7373 | -51.9077 | 2026-07-29 13:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 27cc45ac-4345-343a-b2d9-c59b3dbf66f1 | -14.346 | -58.9388 | 2026-07-29 13:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 6703a3ba-2c5c-3cde-abab-f4e496267b00 | -11.4102 | -46.8473 | 2026-07-29 13:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 08ae551d-1a2f-3d85-85ca-99a5b63aa561 | -14.0117 | -53.975 | 2026-07-29 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| c96cd59f-080a-3f21-9ead-993fd2757a06 | -10.3426 | -49.7183 | 2026-07-29 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 4578b2fb-666c-377e-954d-24bb7e748bd0 | -14.3268 | -58.9405 | 2026-07-29 13:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| af8967b6-0e1c-3b6a-a24e-92e5827b3f70 | -14.0691 | -53.9892 | 2026-07-29 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| b6f0c8d8-d93f-3bb7-ab99-6eb0b8411e3f | -9.8362 | -37.2367 | 2026-07-29 13:40:00 | GOES-19 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 38f0b3f5-f9d0-3f94-a214-1adddd76ac26 | -10.3236 | -49.7202 | 2026-07-29 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| e4b81300-b308-3194-81f8-e92a7c7d98b3 | -14.0698 | -53.9475 | 2026-07-29 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 59451585-8e3c-35ca-91bf-2c4ffa179c5e | -13.7373 | -51.9077 | 2026-07-29 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 188.4 |
| 41ab44f7-9a8e-3576-978c-adaa12b91f1f | -11.4102 | -46.8473 | 2026-07-29 13:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 146.2 |
| ac136e7d-dfcc-307e-ab44-2d06a918e531 | -14.0117 | -53.975 | 2026-07-29 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 3ba98df5-1f22-3c5d-9dd4-e83565285118 | -11.4105 | -46.8248 | 2026-07-29 13:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 7c0415f7-94ad-3610-95a6-745a5041bcae | -11.6224 | -50.3288 | 2026-07-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| f64d96a0-d82e-3820-a0fa-26e64afb9a7b | -14.346 | -58.9388 | 2026-07-29 13:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 8dcc9621-6ef8-31fe-b1e2-5c145c13cec3 | -14.3266 | -58.9604 | 2026-07-29 13:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 3f5c9ee0-04bd-3e2d-9f9c-2db30a2cc5e1 | -14.3268 | -58.9405 | 2026-07-29 13:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 390.1 |
| 7715854f-4e5f-31ed-b88d-5709f9b6ff18 | -20.6025 | -57.2611 | 2026-07-29 13:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 3f904e8d-7784-34e3-8209-d36a9df91492 | -13.3097 | -45.7505 | 2026-07-29 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 365.1 |
| 8f1c9be9-c1fa-3862-a7be-47caf35b6c86 | -6.8708 | -46.0126 | 2026-07-29 13:50:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 9f80895b-7cc0-3023-85cf-317b81cd0395 | -9.8362 | -37.2367 | 2026-07-29 14:00:00 | GOES-19 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 106.9 |
| 3856cafb-fcb5-3779-a2b0-e491614d0de6 | -14.3268 | -58.9405 | 2026-07-29 14:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 112.6 |
| c0452b24-358b-3bec-91a9-e4af74fe5349 | -13.7373 | -51.9077 | 2026-07-29 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 59102406-589b-327d-83cc-9a98d4f89cc7 | -14.199 | -51.9122 | 2026-07-29 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 4dbf79fe-49b8-3a3e-8a9b-d8ba677641cd | -11.4105 | -46.8248 | 2026-07-29 14:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 6ef618e1-4d78-3a72-a83a-e8ed9989e3c9 | -6.8708 | -46.0126 | 2026-07-29 14:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 0f551cc5-1899-3e63-b3f8-7a813e0abdd6 | -11.4102 | -46.8473 | 2026-07-29 14:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| f835917b-a11e-3160-b406-f375ae819fb7 | -14.346 | -58.9388 | 2026-07-29 14:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| e8d5f352-1648-36b5-b654-50eb3a2982af | -20.6025 | -57.2611 | 2026-07-29 14:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 78.7 |
| e3bf9dd5-6ce3-341f-9e84-28021f5f23a6 | -14.0698 | -53.9475 | 2026-07-29 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 1edf8ac3-c114-367a-932b-3154b8359977 | -14.3268 | -58.9405 | 2026-07-29 14:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 303.7 |
| 730d7060-ae18-3816-8c4f-a82d954abb35 | -14.0698 | -53.9475 | 2026-07-29 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| a80b297e-5c33-3a24-9044-cbe10b0af3db | -12.3224 | -47.149 | 2026-07-29 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| befe5135-8228-3496-9423-4dc63141cfd8 | -20.6025 | -57.2611 | 2026-07-29 14:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 5229981f-2677-3c37-a46b-f0f9506c40bf | -6.8708 | -46.0126 | 2026-07-29 14:10:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| f06a142c-147f-32fb-9109-0c9ff09b186a | -13.7373 | -51.9077 | 2026-07-29 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 116.8 |
| abe7b195-a1ea-3749-acd0-4274395107c7 | -14.346 | -58.9388 | 2026-07-29 14:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 231.7 |
| a0c2f377-bf0a-346b-8a27-ed7ea59e8855 | -9.8362 | -37.2367 | 2026-07-29 14:10:00 | GOES-19 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 122.4 |
| a7a06a45-4631-356c-8338-e21e0c831d5d | -11.4102 | -46.8473 | 2026-07-29 14:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 139805ac-9055-32bd-be9a-0ac1e8759c3a | -14.199 | -51.9122 | 2026-07-29 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 40b26e93-1a79-3cdd-a648-57c02e45688b | -14.0695 | -53.9683 | 2026-07-29 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 6317c678-5070-3cd6-afa0-71b28fd7b3df | -14.3266 | -58.9604 | 2026-07-29 14:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| df115e9d-da92-3a50-94c4-9e0643d53d0e | -14.0505 | -53.9497 | 2026-07-29 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 4b0f89e7-d4e8-3ad5-8107-4e258b10c356 | -20.6025 | -57.2611 | 2026-07-29 14:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 79.3 |
| cb200eba-6c04-3a72-9cd2-11752e771525 | -9.8362 | -37.2367 | 2026-07-29 14:20:00 | GOES-19 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 99.7 |
| bc6477a3-a6c4-3027-9514-d5c1e455489d | -11.4102 | -46.8473 | 2026-07-29 14:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 47fbb402-3c52-3c96-b5c4-8a4acc3ecead | -11.6224 | -50.3288 | 2026-07-29 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 5ccefa32-339b-38e9-ae5f-deba150e2e18 | -13.3097 | -45.7505 | 2026-07-29 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 45680e85-4c46-335d-ad6e-852c11113d6c | -14.346 | -58.9388 | 2026-07-29 14:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 124.5 |
| d9cbdd8d-cf16-37bc-85a7-b74b7d20e63b | -6.8708 | -46.0126 | 2026-07-29 14:20:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| be806e31-dc0e-3e60-845a-6be9c6fb5c86 | -14.3268 | -58.9405 | 2026-07-29 14:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 109.1 |
| c39e7d5d-5d0b-3c00-984b-bff4b635410d | -13.7373 | -51.9077 | 2026-07-29 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 213.8 |
| 8e86f4c4-44ad-3335-b1bf-665c984faf03 | -14.0698 | -53.9475 | 2026-07-29 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 58227f2a-e32c-3626-86f2-9ca5a136544e | -20.5822 | -57.264 | 2026-07-29 14:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 61.9 |
| a4c25e9f-c04e-3e3f-b01f-5abd6421e5e4 | -11.6224 | -50.3288 | 2026-07-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 5c5376b8-374d-35e6-a2d3-d33e8d97c060 | -12.3292 | -54.0954 | 2026-07-29 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| ba611e7f-dceb-301d-8493-9276e180666c | -21.3518 | -44.8075 | 2026-07-29 14:30:00 | GOES-19 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 120.4 |
| c826783a-c1e6-3ed0-98d9-e0475cd4e9c3 | -20.6025 | -57.2611 | 2026-07-29 14:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 5b6263e5-d855-3687-b41e-6764cd544255 | -13.3097 | -45.7505 | 2026-07-29 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 04b21809-e20e-35f0-8325-72128414fc0a | -11.4102 | -46.8473 | 2026-07-29 14:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 63d3abad-2b88-3bc6-8a41-6f7351ec61e0 | -11.6221 | -50.3502 | 2026-07-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |


[Clique aqui para ver as próximas entradas](README20.md)
