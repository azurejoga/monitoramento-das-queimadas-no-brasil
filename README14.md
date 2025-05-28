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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdbc9930-3e44-3277-b8a6-a9b041fe9ca1 | -14.6863 | -45.09505 | 2025-05-28 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 607fee15-40c9-3544-8973-69e6f50d646f | -19.70718 | -47.5669 | 2025-05-28 04:34:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c70606f3-cafe-37c0-9fcd-d35f66d940e5 | -15.69389 | -43.4217 | 2025-05-28 04:34:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 886a4877-9a28-3eab-9f1d-9077e6968745 | -14.61825 | -47.94603 | 2025-05-28 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61dab49c-3406-3332-a57e-bb11c8efe97d | -14.69022 | -45.09559 | 2025-05-28 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fe56e6f-9666-386a-9cf5-e89b05298c55 | -16.68167 | -43.88582 | 2025-05-28 04:34:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c16cc7b2-2972-37ab-90a9-b810f05cddca | -17.28411 | -42.65408 | 2025-05-28 04:34:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6f7ee6e8-6b13-3810-8c02-92ac4ee9278e | -16.03986 | -43.79785 | 2025-05-28 04:34:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ca01558-c9d1-323f-be6d-222343fe72f2 | -18.7947 | -54.37928 | 2025-05-28 04:34:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fe8e684-fa59-381b-92fa-a1594e11f5f0 | -16.61 | -43.32631 | 2025-05-28 04:34:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b93fc745-5bd6-3ead-b3f0-34ff78da1a28 | -20.99562 | -51.79289 | 2025-05-28 04:34:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a4fc041b-559e-3b54-be54-f1157a2a6b7d | -17.28004 | -42.64769 | 2025-05-28 04:34:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a089927b-524b-3fae-b3cb-a97edec993a8 | -14.69092 | -45.0904 | 2025-05-28 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48a6ab67-3108-3f15-93e2-af0f2ad8abbc | -17.27462 | -42.65258 | 2025-05-28 04:34:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 225c933b-316d-3f9c-af68-a26fcbe979fa | -17.95464 | -44.42287 | 2025-05-28 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ca25999-1ae8-3012-9368-58eb3c81950a | -15.98853 | -51.2135 | 2025-05-28 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8fa4d76-e294-37f3-803a-837d7b908632 | -15.17216 | -52.29286 | 2025-05-28 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e16b7e24-94c4-3881-99e1-4f61cbc67fe0 | -15.51418 | -41.97302 | 2025-05-28 04:34:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 34c32e7f-e774-322e-8d05-b49c34d64902 | -17.7028 | -48.29068 | 2025-05-28 04:34:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 892e22b0-1594-3fc9-9798-e76c4e6b5864 | -15.1715 | -52.29681 | 2025-05-28 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ded9a99a-e17c-3460-a76f-5d7f0ef23089 | -15.69831 | -43.4223 | 2025-05-28 04:34:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6223e0c0-84ae-35fc-ac85-55b545625fd9 | -16.71532 | -50.68785 | 2025-05-28 04:34:00 | NOAA-20 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ceb0e92-14dc-3094-a6c8-142b42ac5c62 | -19.70761 | -47.56908 | 2025-05-28 04:34:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5177a678-0528-302e-a62f-49cf34681b70 | -13.48879 | -52.95681 | 2025-05-28 04:34:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fe3b42cf-8a32-3723-9068-669d7eb181f0 | -15.17498 | -52.29742 | 2025-05-28 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d64ee19a-a43d-3d93-b9f8-f05643156ac0 | -15.99307 | -51.20675 | 2025-05-28 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d6f65003-4feb-300d-ab5d-7a8cdbd2bc17 | -15.80472 | -43.56953 | 2025-05-28 04:34:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 110de326-6e0f-32dc-8900-4b89f2a69fe2 | -16.71474 | -50.69146 | 2025-05-28 04:34:00 | NOAA-20 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96e6e97c-226f-3041-89e6-93ccd0ad7401 | -17.02531 | -50.29731 | 2025-05-28 04:34:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8474f96-2aa5-32cf-ad29-6e5671ed33f4 | -14.61881 | -47.94226 | 2025-05-28 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38af18ae-53e3-3676-ba02-1e64be5ca5c9 | -17.27936 | -42.65337 | 2025-05-28 04:34:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 795e4c14-d947-3c47-835b-a8ed82a9593b | -19.34342 | -54.16875 | 2025-05-28 04:34:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12f48954-f436-3502-bdfa-f6798e70d409 | -16.75166 | -42.47492 | 2025-05-28 04:34:00 | NOAA-20 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf3a12da-3e61-3f4f-9531-491e6eecd3c6 | -17.64978 | -47.45814 | 2025-05-28 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2ea89cc-5649-3600-ac1d-227a040be697 | -14.68075 | -45.39384 | 2025-05-28 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ced8312a-ff36-3810-95b6-d387c903c29e | -16.04419 | -43.79843 | 2025-05-28 04:34:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5de07070-cc88-3d56-bb0a-f9089353702d | -23.01327 | -50.03672 | 2025-05-28 04:36:00 | NOAA-20 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 11e7dc2b-e649-342c-b18c-317c4288450d | -22.16467 | -49.0979 | 2025-05-28 04:36:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6ac4636-9d9e-369d-8cd9-9bdd427c796c | -25.1252 | -49.55059 | 2025-05-28 04:36:00 | NOAA-20 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 162a2eee-26e4-331b-8412-32a92f930de7 | -21.51844 | -49.86215 | 2025-05-28 04:36:00 | NOAA-20 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 62103546-fce6-362e-a955-25a862c1e4f2 | -23.59767 | -49.00718 | 2025-05-28 04:36:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60c96beb-cacd-3b20-89f5-d9f9d947c9e8 | -24.08074 | -48.89392 | 2025-05-28 04:36:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49c5d65b-6f5f-3d24-9584-aceffe554937 | -24.08431 | -48.89454 | 2025-05-28 04:36:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09043f4f-ac9d-340d-ace8-7fefe4b9d559 | -23.6012 | -49.00777 | 2025-05-28 04:36:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b0573b1-7524-3837-a318-e0429fba4445 | -23.19085 | -49.77549 | 2025-05-28 04:36:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 664a93ff-05d3-3c38-8d95-4067ff4b0941 | -24.39783 | -49.90599 | 2025-05-28 04:36:00 | NOAA-20 | PIRAÍ DO SUL | PARANÁ | Brasil | 4119400 | 41 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a10b9ae7-08aa-3558-9ca7-307f6fd3d6ea | -22.9013 | -43.75208 | 2025-05-28 04:36:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0eeb5a5c-e5e2-39c6-851f-8fc4fce8a295 | -25.19178 | -49.3252 | 2025-05-28 04:36:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 88def75e-2033-3767-a414-be8c706d8d95 | -23.59413 | -49.00658 | 2025-05-28 04:36:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b64b001-2afe-303c-9266-49e8d13b0a1e | -23.25879 | -49.49634 | 2025-05-28 04:36:00 | NOAA-20 | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 64da4bad-a51c-3859-9fa8-1ff9d0040418 | -22.67479 | -42.85394 | 2025-05-28 04:36:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 84ce9383-581b-3660-bcee-89ef531c08a8 | -25.1924 | -49.32731 | 2025-05-28 04:36:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ade7c232-9529-3d83-b310-f174641f8c61 | -7.6762 | -46.0995 | 2025-05-28 04:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 32fe35c7-040f-3d89-92a0-183118cc3677 | -11.818 | -44.2703 | 2025-05-28 04:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 4895b1bb-9ea7-3c2f-aaf7-8bbe1307553e | -11.818 | -44.2703 | 2025-05-28 04:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 4d74ec6d-a85c-3bb9-94d8-183abb037a40 | -7.6762 | -46.0995 | 2025-05-28 04:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| cdd1f1ca-44bb-3361-97c2-d2bb2bec5f23 | -11.818 | -44.2703 | 2025-05-28 05:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| e31a526b-ca54-3d1f-bc65-9492e4ce462b | -7.6762 | -46.0995 | 2025-05-28 05:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 3db61545-3542-3b06-974e-49fd09d1027a | -7.6762 | -46.0995 | 2025-05-28 05:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| e3766e90-63f3-3555-81df-65ddd5f2734e | -11.818 | -44.2703 | 2025-05-28 05:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| a7a44450-52b6-3d55-8f69-d208ce9eea00 | -11.818 | -44.2703 | 2025-05-28 05:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| cfcfe75f-7559-3285-9ae0-d4a733b55380 | -7.6762 | -46.0995 | 2025-05-28 05:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| b0e9a718-ccf1-3281-9141-304c7b96374d | -11.29359 | -54.01199 | 2025-05-28 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 41512646-56aa-3dd9-94ad-fbfe3466cdf6 | -10.67129 | -49.44652 | 2025-05-28 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25ebab5d-4c6a-3996-8fa9-ec633635587d | -10.73729 | -49.28696 | 2025-05-28 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea6a8ffc-71e9-336e-94fc-bfafa7e7368a | -10.24396 | -52.22856 | 2025-05-28 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 89367cdb-2589-3406-be74-673a31950987 | -11.40039 | -52.94955 | 2025-05-28 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd9b6212-71e8-3ad0-9444-91840de5966f | -11.14471 | -53.9196 | 2025-05-28 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b3ea6a9-648d-3ecb-8505-79cf4d520587 | -11.75313 | -54.23148 | 2025-05-28 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f3bdeb5-5ae5-3639-bdec-038863dfa8b8 | -11.04355 | -55.07836 | 2025-05-28 05:23:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c254cbf0-406d-3d21-b4d4-1aa681d1c878 | -11.29767 | -53.97989 | 2025-05-28 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 893cf744-4540-361a-9bb6-87ced2e47cd4 | -6.63431 | -55.01121 | 2025-05-28 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e4e3c71-f81c-31e1-ac3e-81ca81c696bc | -10.66622 | -49.44826 | 2025-05-28 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8a4f2ec4-73b3-3a72-a956-3a357f1811ae | -11.97791 | -52.47038 | 2025-05-28 05:23:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84fa8e5f-11a4-31e3-9897-d9174671cbf9 | -10.24353 | -52.232 | 2025-05-28 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cac8f650-6ee2-3d2c-8da1-3dc60e4f5cdd | -12.11617 | -54.66919 | 2025-05-28 05:23:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d25eb8f8-13a5-32ce-8870-a424c21e300f | -11.1385 | -53.92955 | 2025-05-28 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa044ad7-3023-3283-87c2-794cbea43bd4 | -12.41443 | -49.99894 | 2025-05-28 05:23:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9d23523-6a26-3985-8d05-e5ce15fdfb2f | -11.28812 | -54.01661 | 2025-05-28 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3ec86b5-b046-37bd-9398-e6cc780794c3 | -10.75501 | -54.78128 | 2025-05-28 05:23:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 606862bd-6462-3d7f-84a7-584f7f9763e3 | -11.8107 | -55.07654 | 2025-05-28 05:23:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2fc64310-c7d9-33d5-8265-942cac758d7c | -11.39857 | -52.94998 | 2025-05-28 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d69a946-12a1-3336-aa79-8bdcc783b7b7 | -11.40077 | -52.9464 | 2025-05-28 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6480e29-4685-3bfa-83a2-e980a398b371 | -11.97878 | -52.46344 | 2025-05-28 05:23:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af2d059a-a86b-3c73-a704-b30e780d7ee7 | -10.23776 | -52.23472 | 2025-05-28 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6b0091b7-a91b-3abe-b363-2aa0cdcf9e26 | -11.29292 | -54.01728 | 2025-05-28 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 523352c7-3db9-3c40-bc40-d5afb7140a58 | -12.11217 | -54.6636 | 2025-05-28 05:23:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ac1283a-5a9f-3ad1-b4aa-244a6ac20c79 | -10.45632 | -47.94664 | 2025-05-28 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3b21d5a4-87ef-3861-89ae-ea13ab1d3183 | -10.47027 | -47.94882 | 2025-05-28 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 27a7cc76-7638-3ec4-9c0c-4bc20c646036 | -10.23201 | -52.23723 | 2025-05-28 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24ad87db-c721-3b0d-b1d1-fb1b48f25118 | -12.04007 | -54.96692 | 2025-05-28 05:23:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 927d6a3b-2f38-3cf5-8f47-5ce663f2716e | -11.14061 | -53.91345 | 2025-05-28 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cd9b537-3527-3400-a6ac-f608333911dd | -12.11152 | -54.66855 | 2025-05-28 05:23:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b4f5bf8-8428-3980-a34f-84247ff0edb0 | -11.14331 | -53.93026 | 2025-05-28 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67cc29f6-82dc-374a-a9c6-18f79752d4a0 | -11.29701 | -53.98512 | 2025-05-28 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a328b512-3d87-3411-ae8c-d1a0660f6de8 | -11.1392 | -53.92422 | 2025-05-28 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 75725616-83cc-3266-9027-672f91804283 | -10.65844 | -49.44499 | 2025-05-28 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c8e664e-0110-3f48-be36-f87b6e88d9c0 | -12.41165 | -49.99888 | 2025-05-28 05:23:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9f74ad2f-effa-36c5-bfb6-0cfbdc2c8432 | -10.23286 | -52.23043 | 2025-05-28 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 987de1d2-fc64-3a5b-8966-fe59d48c4864 | -10.53566 | -59.22416 | 2025-05-28 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README15.md)
