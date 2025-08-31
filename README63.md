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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48fb1628-c9d4-30fb-a0bc-2e169c7798fd | -12.52262 | -53.8152 | 2025-08-31 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54178e18-82c0-3f14-bc0a-c49b3448a68a | -14.40329 | -53.19667 | 2025-08-31 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25a56702-c354-3215-91ce-83ed8c247a8c | -11.31694 | -63.27271 | 2025-08-31 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1ca9df3a-4078-34d9-afc9-5bfbd77e899e | -12.93131 | -56.98217 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8116cb68-9864-3de7-8d27-79c0e379358c | -11.81518 | -46.42916 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 5adfaafe-0cb5-3847-82a9-0197685d7a13 | -8.46023 | -43.63 | 2025-08-31 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a809f09-7fbe-31fe-981a-14a738a9fdd9 | -9.45842 | -62.3429 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9f714037-76c2-301e-8e8e-6711b7b18440 | -11.8275 | -46.53064 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0219a61d-7547-375f-8c44-0bc771a73e31 | -13.40051 | -46.94958 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0afc4ca-ac79-3925-9b02-0e668b83aa35 | -13.48257 | -46.96104 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5ba3e14c-41f7-38f4-ac8e-69b4e031dc6c | -11.05121 | -52.04436 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66898ce3-20b6-3953-8706-ceee9c803f7f | -11.88606 | -46.73498 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b4422644-c3b1-389a-8e8b-18034e1b909b | -14.35544 | -51.90462 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3808cd7-6f39-3304-8188-199986c912b3 | -9.44217 | -62.34317 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1d944df-5116-38c4-803e-e5e403e2a559 | -8.74291 | -62.38091 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5588c86-d89a-3666-9d58-ae2841830ac4 | -10.31704 | -59.19668 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b3dbc47b-f87c-3de3-abbc-add679e350ea | -13.31774 | -46.94545 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80888fbd-2104-3d4f-9b4b-52860eac30cb | -11.81682 | -46.42649 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ae74f18e-8cfd-327f-a6a3-8304cf3ff287 | -12.63244 | -48.22276 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3ab75d5-ba6a-3714-b475-48317865f6a9 | -9.44338 | -62.3366 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e2c672c-57de-30aa-8629-cfe4d681068d | -10.6139 | -54.92036 | 2025-08-31 04:51:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d66c1f6-6d8f-3ef0-b76f-ea94d6e0741a | -10.61054 | -54.91982 | 2025-08-31 04:51:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05dece66-7a88-3972-adb6-673c47e02b70 | -13.36184 | -46.95464 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 87dd6378-61e8-3c1b-bebd-f1e580dfd826 | -13.47786 | -46.96067 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d2a473a-fc8f-323a-a9e0-7d544e72061b | -8.74637 | -62.39178 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bd50c5b-3a04-33a1-bc16-a8ca5cd5efbc | -7.72231 | -50.26563 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6fcba4ff-b7e4-38a2-b887-a53e7c66d550 | -12.80949 | -48.08693 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f36b84d5-cdee-3f62-9628-2298f4c60183 | -11.55882 | -47.61428 | 2025-08-31 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a9b1a76-aa86-3e4e-ad30-22983674b6dd | -13.34082 | -51.85924 | 2025-08-31 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7c326fc-dec5-3133-8cba-7217381cedeb | -9.43234 | -62.33791 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b042485-da0d-37da-ab5b-556cfd5c82f9 | -9.69609 | -47.04514 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6e9e3f4-573e-3c43-b892-8fc82e2ffc1d | -10.95441 | -50.85234 | 2025-08-31 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c14ecdcc-d897-33ab-811d-31fe32cb45a9 | -10.41582 | -50.85546 | 2025-08-31 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce1b1372-26f4-3371-bb75-82de667b16f5 | -9.43694 | -62.34224 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb9aca96-aabd-360c-a05a-59b033e24aff | -13.49552 | -46.97148 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| beccfbc3-804a-3daa-bb13-3d45d2a20f3c | -12.91646 | -56.98382 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 11f858c4-26fa-3886-937b-04c4520b14ee | -11.32562 | -63.25645 | 2025-08-31 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4e1af486-f61a-387a-a76f-8a919ac07a92 | -11.82467 | -46.43032 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cb5b92f0-4a64-3232-b6ae-522c11023082 | -11.28174 | -63.23955 | 2025-08-31 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef9a1b42-433f-3582-b028-6e0777020ec3 | -13.51305 | -46.98308 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91cfa7c5-fa34-3624-b56a-8ed86c664971 | -9.44396 | -62.33344 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed8e44c7-c6ad-3a8e-b020-b301945f47b0 | -11.31069 | -43.69432 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba1911f3-6f0d-3c81-a2db-7a2327259c38 | -11.29894 | -43.67177 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9de75ac7-264e-3b3b-a71e-b79263a22df9 | -7.71578 | -50.30942 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62be9e8a-23af-39b6-907b-1247629e9eed | -7.74952 | -47.44315 | 2025-08-31 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aec5e022-88f6-390a-aaaf-74414839d4bb | -9.47248 | -47.61192 | 2025-08-31 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d4c545e-41b7-3216-8988-29b574f903e4 | -11.32016 | -43.68594 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac9b869f-2ce6-3fb1-89ed-2b8c319080f4 | -8.91954 | -62.42574 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f5d745c-b14d-3f74-a7c1-bc5fccbbe79c | -11.9033 | -46.6992 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53042082-3289-3a78-b47f-a0b6f6b0335c | -11.82629 | -46.4278 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 899a0fd1-3382-35f2-b65c-835018397034 | -11.07214 | -52.04388 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44187b97-2dc4-324a-b33b-9a55edf65824 | -8.68774 | -62.4222 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 654fa970-14cf-3a6e-bb00-8eeaca2d3c14 | -12.65393 | -48.221 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b5bbfba7-b0b9-376f-8005-c90a1890e189 | -9.44278 | -62.33986 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ebfbadf-fa87-3ae9-a62c-0357c6e0ca4f | -10.40692 | -64.53226 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a834629-4673-39da-89c4-5df1043d5bd7 | -9.25357 | -47.06542 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e68f358e-8238-3365-b9c4-e9e413204ab5 | -9.68539 | -48.30053 | 2025-08-31 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 558572c7-b5db-399a-a7e5-f22eb1e7dbdd | -9.29987 | -59.22145 | 2025-08-31 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1797923-6934-3a32-9b01-245c8e4353d7 | -7.71282 | -50.30512 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0243d068-94b0-335f-aeff-3d05d6b06c29 | -11.60831 | -51.94505 | 2025-08-31 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d05357af-1c8f-368a-9a59-375984bbce60 | -9.6967 | -47.04263 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20d55a7c-7396-3015-94a4-bee5daf5a707 | -11.36186 | -43.55756 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98530767-0dfa-33f4-8a83-151e90e56401 | -10.02975 | -48.09519 | 2025-08-31 04:51:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4c2aa7c2-eb96-3277-aa07-5aaa49ea92e6 | -9.58441 | -54.4764 | 2025-08-31 04:51:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c25481a8-043c-3cba-9de9-8aa905750e18 | -13.01322 | -56.90344 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d2a0233-06e4-3367-9a36-09191d09c948 | -13.02094 | -56.90068 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85a0ed06-c0f6-37cc-8f1e-324d786e785a | -10.31497 | -59.20836 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d6185e1-ee80-3e41-a0c7-ff31b39bc11f | -9.30127 | -59.21878 | 2025-08-31 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5495c01-ab2f-36b6-a250-e220281c0cfd | -14.38037 | -53.39118 | 2025-08-31 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e9240eb-4f2b-3067-96e4-28d5940be9e1 | -12.09237 | -44.72382 | 2025-08-31 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 1a776f78-f001-3db5-aecc-1143e50908e7 | -8.54932 | -51.3041 | 2025-08-31 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c0616ac-8f82-3de5-a32b-4f95a4eb38ea | -11.3021 | -43.67006 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b646c19-8889-35bc-be93-aa2ce7cb9f2e | -13.48024 | -46.94173 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c3535a95-4279-3be8-96e3-3a12302fe5d1 | -11.81173 | -46.4548 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2dfbef7d-f2c9-345e-9653-c983fb387b32 | -8.73331 | -62.3826 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fec2983e-4552-397b-a70d-6a7149ede861 | -9.58918 | -46.0108 | 2025-08-31 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e825d9c6-9d19-3406-8a84-f2f516220a34 | -13.09536 | -57.12718 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecb192a9-4906-3e85-9b1b-801508b2e6ab | -11.36137 | -43.56158 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8051c6ef-0fec-3df6-9740-83e3130a922c | -8.73983 | -62.39745 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a0c0250-634f-3bd1-a7f6-459abd2dbcb5 | -12.60991 | -57.01816 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a781dece-8ac5-311a-8f65-e5d802e37961 | -13.30223 | -46.91809 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aeeee163-a0bd-3e75-9d91-dce40d27e821 | -10.31219 | -59.19982 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6fcab516-5997-38b9-bee0-9e54ab3a7a2d | -12.52042 | -53.8293 | 2025-08-31 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 495f419d-3b81-398a-b18b-b909c8d525cb | -8.28394 | -46.31767 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e3ac748-374f-3650-bcd1-72b878dc81af | -11.36313 | -43.5947 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebc9fc3b-12aa-3a7e-8c47-a0a76a828fcb | -11.88429 | -46.35318 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b8e45a64-5995-3e9d-82c4-7e3931eb0a08 | -13.02581 | -56.89328 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ae665e1-f786-3e14-8981-e4acef332458 | -9.24862 | -47.0689 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3cf29be3-d011-3dd1-964c-21c2c564d54f | -11.94718 | -46.68996 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| efb7928e-d1e8-3712-a2e9-440065bd79b7 | -12.93839 | -56.9834 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 937db4bc-3b74-3fe2-89a6-4f516ef350db | -10.94973 | -50.83496 | 2025-08-31 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7589074c-56ff-3b42-98a5-016c9b958ed5 | -12.87033 | -48.08978 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a8cb5a2-ef01-3125-84de-4cffd3c8164d | -10.33782 | -59.2007 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 045a6d01-fbe5-39f5-8550-acd95a59ac5d | -11.2391 | -44.67929 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9985f4b4-afa2-34be-a069-c4143289fa60 | -11.84164 | -51.48988 | 2025-08-31 04:51:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 264d60cf-2231-3f01-87ae-2c7f3c182391 | -9.65821 | -48.34665 | 2025-08-31 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a70784e-b8f0-3862-b75b-9daac151f1d9 | -8.97099 | -50.02885 | 2025-08-31 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b479312-3384-375a-b06c-26767257c1b3 | -13.35061 | -51.76774 | 2025-08-31 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 529cc078-b1fb-33ef-a755-207d2af21b0d | -9.44408 | -60.5718 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ee47c23a-fa9f-38ba-b77a-048f89803530 | -14.55356 | -51.98166 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README64.md)
