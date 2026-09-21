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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f8e0f60-b94d-3459-baa5-e0b6e43422a7 | -10.09 | -46.10608 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3060a032-c1ab-33f2-a2cb-d0a32102fc56 | -10.67238 | -50.72905 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0adec5f5-7775-30f0-a4f2-af8df199667a | -7.57676 | -57.6967 | 2026-09-21 04:21:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9bd8db2a-1107-36fb-91c8-98389dcb2fc7 | -10.4685 | -50.28022 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 49531243-4f7d-3eea-b963-5935d307b87f | -16.03822 | -52.50719 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 3fac1f1b-a4d3-3c29-a3b0-32e9ef03c1a6 | -11.12334 | -54.01459 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f7c4e46-ced0-3e1f-9386-c762fdd89698 | -10.46153 | -50.27971 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f0ecab00-6e5b-34bd-b4d1-a492c0f05ab1 | -7.5653 | -57.67941 | 2026-09-21 04:21:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eb58eb7b-18e3-32dc-949e-01edacd64629 | -11.87603 | -49.01334 | 2026-09-21 04:21:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f31fd1f-ba68-3563-9cea-c18a2d3a399b | -9.77018 | -46.06572 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d4ba954-6099-399b-845c-a260b62af75b | -10.85553 | -50.16011 | 2026-09-21 04:21:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f0f919e-894b-3a18-b659-7d55d64444cd | -11.45343 | -50.24485 | 2026-09-21 04:21:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7cdac8b6-8707-3309-8467-bab4d132afce | -9.82636 | -48.31379 | 2026-09-21 04:21:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4c72a61a-b992-34c4-9276-6671c7c807c9 | -11.04968 | -54.92062 | 2026-09-21 04:21:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d975976-2177-39e0-8830-78c19717e7cf | -14.18464 | -47.8786 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d21c293-e6b7-3696-b51d-a1e19813d1f7 | -11.32187 | -47.30109 | 2026-09-21 04:21:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fbb2beb5-6d8e-3b5d-b1b9-022bf385f70b | -11.40648 | -47.33659 | 2026-09-21 04:21:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b0f7cb5-9a6d-38ba-9dc1-9d6cd96806b1 | -12.79779 | -54.0588 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce4e0b77-eb41-3959-a319-d06be7b3f0a1 | -13.89963 | -48.57602 | 2026-09-21 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd3f715a-2dc2-3b7a-a715-1fb4adc29778 | -15.6768 | -48.13054 | 2026-09-21 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ebd2a54-7e05-3a0d-9ee1-e2f34a381468 | -14.74204 | -50.27904 | 2026-09-21 04:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7890e5e2-f167-3a8b-a8e4-718d64ccc525 | -13.87451 | -48.59036 | 2026-09-21 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 014c3302-850d-3782-9781-613a61619116 | -11.13486 | -54.01315 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4b9446c-8910-3857-b401-9131674b358f | -11.09532 | -51.06333 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1bfb915b-31a5-389f-8856-76ba85f0e61f | -9.94917 | -45.68388 | 2026-09-21 04:21:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b54c53a8-f1a6-3cfb-a3fc-10225dfbad62 | -10.3137 | -50.55808 | 2026-09-21 04:21:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd67d6ea-f113-37ee-8ae0-e93eee08bb8d | -10.4117 | -50.23677 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| b1fba443-372e-3739-92e4-e084ae1fd626 | -13.26834 | -51.75393 | 2026-09-21 04:21:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5f029923-1750-3678-ac5c-c15770cb21b0 | -9.8254 | -48.31924 | 2026-09-21 04:21:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fb4ef918-0366-380e-bf1d-5c360263b6e8 | -10.74573 | -50.79826 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8c9f9abc-d4ad-3969-91bc-38e3b77e4f5b | -9.73069 | -48.15114 | 2026-09-21 04:21:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9682541c-bc0d-377a-954f-5fe57bb9f010 | -11.13014 | -54.00846 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3f07a9d-1c28-398f-9676-1e3309542c3c | -10.34823 | -50.2064 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ca89831-6195-3006-825c-c3063c757af0 | -10.42307 | -50.24728 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4b10cc6c-1be5-3f37-a7cc-06f73f43c12c | -16.04135 | -52.98064 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5ff1770-3c1d-3b27-9373-7926a79b61fc | -16.0284 | -52.51687 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| a817badb-314e-36c9-838f-71c6fd46e5af | -12.28932 | -50.1647 | 2026-09-21 04:21:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ece89ac-ef41-317f-8d32-ab6f933392d3 | -10.12129 | -45.5504 | 2026-09-21 04:21:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 00801b0f-7f1b-3fbf-bbfe-709f9f4f4834 | -11.08871 | -54.01903 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 653d7301-7ad6-34fe-b82f-82a4aa7db4a3 | -16.04898 | -52.53121 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df72b3c2-7159-31e2-ab50-3b5949395210 | -10.34751 | -50.21049 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bddcf4de-5690-3163-839a-e9d8c775e030 | -8.17262 | -54.78196 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2bd37bf-4d92-3cf7-bc89-e503144ad8c3 | -10.78151 | -50.82763 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7100f0c-3efd-3dec-99ca-0cc93a63be61 | -11.82077 | -46.84053 | 2026-09-21 04:21:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b64629e5-daac-3c84-93f0-55826d7e0eea | -10.47632 | -50.28588 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 2b6eb403-04d7-3b41-8271-75d171972f28 | -16.03647 | -52.51652 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 93a629a2-748d-34e4-a9f9-945ebd8e3000 | -14.67322 | -54.47605 | 2026-09-21 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2012941-272a-3870-8c88-c1774f136250 | -11.05209 | -54.90833 | 2026-09-21 04:21:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f39f6fd6-a75f-3bf2-a1cb-b7e352ce790a | -15.6541 | -52.71401 | 2026-09-21 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1915109-e014-3360-bfc2-d176c4c72715 | -12.41152 | -47.03136 | 2026-09-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16e85356-26c3-3108-a51c-c6e8cba512d8 | -13.03601 | -46.96665 | 2026-09-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e3d242fd-fb64-3d9e-a1cd-4631ea95d7d8 | -10.67574 | -48.73042 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77603c8d-fd4a-307a-ac18-4699afae6c5b | -15.51783 | -42.65435 | 2026-09-21 04:21:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 28dc5005-c741-3bc3-ac41-c14ffff18a1d | -11.8932 | -48.99928 | 2026-09-21 04:21:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b9da557-90f7-3147-99f2-4247491b207b | -10.55766 | -46.73421 | 2026-09-21 04:21:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29c0c010-823a-3300-9f2e-f570278ce397 | -10.34396 | -50.20561 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d9cf5a0-ee7d-3092-a068-ad004f727ff1 | -10.5397 | -54.49604 | 2026-09-21 04:21:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19c2b633-c29f-370f-87aa-14ce22b4404b | -10.91583 | -53.96872 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1453b25b-0f17-3288-b23e-5ea98d524c5a | -10.826 | -50.15465 | 2026-09-21 04:21:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0af55300-0b0e-3392-9d9c-7af0f2376bfa | -10.4544 | -50.26994 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 1bc228af-d953-3bef-8f5c-addd026624f0 | -11.99378 | -58.07691 | 2026-09-21 04:21:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34fd2499-78b4-35a1-8f41-04e693c57b6a | -10.46225 | -50.27561 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| cd0411ef-f43d-37f8-bf19-11be0c706485 | -10.88433 | -54.07385 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6b10c93-ecc8-3dc4-a50b-019a696042bf | -10.79598 | -50.77157 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 484f2140-b81f-380b-85d4-c8a501288b46 | -13.39101 | -49.44721 | 2026-09-21 04:21:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5b23d9f0-722f-326d-a34a-c534a064933c | -17.01687 | -47.13802 | 2026-09-21 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 599cf548-ae6e-3be4-b996-d69fc62f693b | -13.88572 | -48.56904 | 2026-09-21 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06572ef8-02c3-38ee-b08f-5e06e7619b49 | -10.20731 | -53.92427 | 2026-09-21 04:21:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba0b29fc-0a60-340c-8609-6857c9d48922 | -11.03397 | -54.15292 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e709e20-a456-301d-826a-e8888fbf784f | -12.57098 | -47.08022 | 2026-09-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| adf62853-5181-312a-b21b-56e84c01d64b | -9.73388 | -54.81795 | 2026-09-21 04:21:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93cba1d0-780a-347e-8ac6-c1bbf859fa16 | -9.82187 | -48.40748 | 2026-09-21 04:21:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8131cf02-1bbb-3ddc-acb0-66ee3d88fa81 | -10.81264 | -50.77792 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3e6e4dad-0614-3ead-a4ab-ee893097911d | -10.13818 | -45.55282 | 2026-09-21 04:21:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7aba946a-21a8-34a5-bea7-8c2804cdd828 | -9.82535 | -48.43304 | 2026-09-21 04:21:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 94b462ce-8104-37a8-81c8-a959189ff0d3 | -16.68041 | -47.88689 | 2026-09-21 04:21:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e69fd0a-aaca-366e-ba0c-2050b5e66002 | -16.02483 | -52.51124 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 399e8b98-ac08-3b7f-8021-ebf0ac8320ae | -9.76494 | -46.05769 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 032969df-fcdb-3959-8928-5da86e844432 | -11.79877 | -51.13253 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc50b1e4-4eb7-3ccd-9a04-29829aec53a0 | -10.86022 | -54.11042 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 195999a4-c9c8-30f0-825a-baaa49314da6 | -9.74799 | -46.24156 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 948061f5-acd1-3f9d-8e4f-a06a8cc79484 | -11.04229 | -54.89742 | 2026-09-21 04:21:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb28e177-6a33-3047-a1cc-75b1a2cd6e0d | -16.02839 | -52.50984 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 212.1 |
| 81019ede-f02e-32c0-985f-0c91fc159abd | -10.67885 | -50.74374 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e643eb94-27eb-35cc-a316-ed7b7a113ce2 | -11.02634 | -48.32043 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 33f4c0c8-0b11-305e-b253-edeb9f70d3bc | -16.02927 | -52.50517 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 212.1 |
| f8177acb-281f-3cdf-86d3-0afa1767bf73 | -15.63759 | -52.70062 | 2026-09-21 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7b08819-b633-30bb-ba5d-483ade0b895a | -10.66773 | -50.6789 | 2026-09-21 04:21:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a429187c-2e92-3ef9-95b3-df6da2c01924 | -10.74211 | -50.79305 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8eee86d5-e06f-3e12-a094-f0eed4885524 | -10.39462 | -50.23363 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| bb29ba92-7916-32e2-818d-7b4b702ea41f | -11.04069 | -54.90557 | 2026-09-21 04:21:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a9addae-3721-3a73-adba-772ddc1c2b56 | -16.18824 | -51.12449 | 2026-09-21 04:21:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5e68038-a693-3738-9223-f4fa7c006f5f | -11.93011 | -46.48198 | 2026-09-21 04:21:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de895d4b-dac6-3c47-8807-b2ce76fd1191 | -10.12467 | -45.55087 | 2026-09-21 04:21:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e0ecc3de-a2ba-337e-86cf-6ff3caad950d | -10.75817 | -50.80511 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8a88a7c3-2764-3b64-8acd-d5af26b37143 | -10.804 | -50.77758 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 544f5736-0609-36fb-9226-89705d252268 | -11.86655 | -48.96919 | 2026-09-21 04:21:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58177131-3b2d-380d-8cee-2233cb7ceef8 | -11.7965 | -49.8063 | 2026-09-21 04:21:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8874779-2828-395e-88a1-302a144f7521 | -15.86232 | -49.89962 | 2026-09-21 04:21:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3f14a94-5be8-36da-a9e0-9c0608c904b6 | -9.85499 | -46.42403 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README46.md)
