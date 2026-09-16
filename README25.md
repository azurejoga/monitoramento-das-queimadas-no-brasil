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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76d1ceae-dac2-3031-a440-666456ceb9a6 | -5.17421 | -39.74396 | 2026-09-16 04:14:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5e357e82-6792-32d1-9e67-2e39c92ca88f | -9.76409 | -46.57685 | 2026-09-16 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6dd94cc6-49ac-3275-b17c-e51552fb58c1 | -3.3832 | -50.45415 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22225394-807c-338a-a420-bda9e14b0097 | -7.85382 | -55.46093 | 2026-09-16 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10ea0eab-6191-3aec-a035-feb13d03a72b | -7.45057 | -46.97514 | 2026-09-16 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17072de3-28eb-353f-8f32-67e336a06405 | -7.50768 | -50.15515 | 2026-09-16 04:14:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4946c91f-85dd-39e3-b154-c7a91f3f3cb2 | -10.80917 | -46.18083 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e50411f8-6dd1-3df2-b30f-88fe63542614 | -9.78466 | -46.54713 | 2026-09-16 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d711300-207c-39bb-b935-83521d54f009 | -10.58071 | -47.74864 | 2026-09-16 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1751f18f-f494-392e-88eb-ff4d398f4e55 | -2.89486 | -50.42643 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75ab2ded-3a31-3881-aa1c-c80b4d8b76f0 | -7.35093 | -44.49915 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5d44744-e4f8-3025-a7b0-f0cd3485ccf0 | -7.17006 | -42.10793 | 2026-09-16 04:14:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 40860058-e810-33c7-b0c9-239a3b8bf6f1 | -5.99262 | -46.63269 | 2026-09-16 04:14:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7122261a-ca59-3e4b-834a-e17483ea4d5f | -8.64587 | -44.45283 | 2026-09-16 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b738d0fb-5abe-3124-b080-4c9059d962e1 | -10.41218 | -48.64288 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0bed7b4-4824-39d5-ae79-c9c5d4856703 | -2.95414 | -50.40744 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86c6b5c9-0533-3654-8229-31f8e65d1e4a | -10.90275 | -46.2929 | 2026-09-16 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb907acb-771f-3be5-8794-e73be6efe7a4 | -10.85164 | -46.19427 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99417dcc-a5e3-360c-a244-a081fdb9828a | -9.11363 | -45.73774 | 2026-09-16 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2ace1078-79c3-33eb-adc9-b090c5de240c | -7.14612 | -39.53283 | 2026-09-16 04:14:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ad48d4a6-2036-331a-b645-d0bd8ecfb87c | -2.91052 | -50.40004 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 478127a5-b9dd-3f30-a2b0-f1ccb8a04bf7 | -9.80077 | -46.49722 | 2026-09-16 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c7659ee-eb2a-342e-85a0-9beb95fafaba | -7.17568 | -43.51057 | 2026-09-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8d39015b-b17a-37b1-bcce-1884e83db808 | -7.25469 | -46.16996 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 530356cd-3601-3be7-8222-09276a86fc81 | -11.20313 | -42.82877 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4be81608-1e16-353c-b8c8-cb0567370222 | -5.58475 | -40.89854 | 2026-09-16 04:14:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4cdedd4f-bd4b-324a-abba-9a564bddf55c | -8.84965 | -44.906 | 2026-09-16 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d46f8ed7-739c-320e-989a-bc6c29ace90d | -2.8888 | -50.42902 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18a21be4-c203-3e20-836e-63b8f3194f06 | -5.13902 | -44.40038 | 2026-09-16 04:14:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3e7c08a-ac78-389c-894f-03e2e025048e | -6.33263 | -44.09962 | 2026-09-16 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 982c23f6-9fb1-3f51-8c9f-580aef88545c | -5.65591 | -43.2318 | 2026-09-16 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1a09213-7db9-39ad-b7ec-1af18b5ce52a | -10.59886 | -47.76321 | 2026-09-16 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99cdda2a-9d20-31df-883b-25db154d31fc | -2.8688 | -49.14204 | 2026-09-16 04:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53ae39da-0e05-385a-ba05-6f9b35fa517c | -9.09682 | -45.7262 | 2026-09-16 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 45fc60e1-f8a9-377c-b18f-30ddf73a3553 | -3.31239 | -47.14075 | 2026-09-16 04:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 122dab9a-298d-386d-9975-fd1afca6afe5 | -6.95235 | -42.57927 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fe091b0a-9d28-3a0a-bb10-38452600d55d | -8.97925 | -42.69427 | 2026-09-16 04:14:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cc068090-918a-3bc8-9022-029acc30188a | -6.65883 | -43.64717 | 2026-09-16 04:14:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27d258aa-01fc-38a7-9c2d-2e6fd0bea9dc | -3.37354 | -50.84162 | 2026-09-16 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b85f3a07-8063-35d0-af83-9231aafb2951 | -5.9662 | -46.66185 | 2026-09-16 04:14:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd2f8f33-8e58-3200-b257-490b9d15ce97 | -2.91729 | -50.42665 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdd997c8-43c9-3077-a253-5f2449160f4b | -7.18027 | -41.80779 | 2026-09-16 04:14:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ccc471d9-ff6c-3f53-ab8e-0931381a8bc0 | -10.11419 | -46.32109 | 2026-09-16 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc65460c-d636-30b9-bdc9-670c12ae4b91 | -5.48791 | -43.40483 | 2026-09-16 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5b309bb-47f3-3012-86c3-aea199d34017 | -10.394 | -46.63974 | 2026-09-16 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fde9fd5-70fc-39b8-9c68-a56d4e0b0be8 | -6.01502 | -51.79642 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c0a853d-3dae-3eee-a491-55549f3e895b | -5.63478 | -40.85996 | 2026-09-16 04:14:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6be88f47-8a22-3067-a4f9-3013164de33f | -9.87177 | -49.83137 | 2026-09-16 04:14:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90096d25-a55d-3258-b9e8-f2732d07be1e | -11.1932 | -42.82716 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| caa46da4-9e9a-3f1b-84a4-b53f06d6050e | -6.19074 | -44.03038 | 2026-09-16 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e1896fc-14c2-3bbc-84c2-509dd253cfe7 | -2.91656 | -50.39741 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 666d1d09-8ff3-338b-abbd-e383b52e809f | -11.18505 | -43.4531 | 2026-09-16 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 33dde69e-d0f9-392e-a717-adb9adbe4350 | -2.91125 | -50.42923 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65c1012f-aada-384e-8e71-1a392cb44568 | -9.81016 | -48.91773 | 2026-09-16 04:14:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cd97272d-355e-3ecf-8904-04337c199123 | -6.00046 | -44.31319 | 2026-09-16 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6bd02396-6fae-358b-8d52-29581dd6a49b | -8.04893 | -43.74776 | 2026-09-16 04:14:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a0435d05-b8f4-331e-89ef-372032ac5a2b | -7.18743 | -41.80538 | 2026-09-16 04:14:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e5598360-3946-315d-b86e-8c9e79280927 | -9.80994 | -48.92006 | 2026-09-16 04:14:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3713634-66f3-30fa-9c8c-8214e9cd7022 | -3.22973 | -50.58757 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| edd9bcd5-d22a-37c9-876e-560fa1218051 | -5.62923 | -40.85189 | 2026-09-16 04:14:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 38fa9d64-9cb7-37e7-92f7-1b274d2cc023 | -4.67888 | -42.09134 | 2026-09-16 04:14:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9b3dbf81-5365-3508-9023-7efd081adac2 | -7.44025 | -49.47142 | 2026-09-16 04:14:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15f0a891-c877-3d4a-9247-be3919cefcce | -10.84807 | -46.17125 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab6730c5-ba61-35b7-8044-fe4e7ef8eb6f | -7.13582 | -42.08821 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fee3430a-9e78-3f03-84b0-a9b61c308055 | -2.63766 | -54.69618 | 2026-09-16 04:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bc183193-9216-3a43-829c-04728c9210de | -8.40299 | -42.21618 | 2026-09-16 04:14:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 63003993-f5de-390a-8894-bef6eec62a34 | -5.77621 | -45.09404 | 2026-09-16 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 883d442e-28db-3dc2-92b7-dab3e4017002 | -5.99555 | -52.10824 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54e15ea0-9579-3007-85d1-a85b7b2dcfc4 | -7.26763 | -46.6807 | 2026-09-16 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64989b97-847c-3da0-b716-1d5105c1e9b4 | -11.24823 | -43.44175 | 2026-09-16 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a58007cf-e7fa-32b6-a992-73c62df5da2a | -6.18825 | -44.03307 | 2026-09-16 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 948fee1b-e0ab-3449-9671-90398c87c532 | -7.45731 | -46.14857 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88742630-5cf7-3305-a668-11f9ec46a086 | -11.25098 | -43.44583 | 2026-09-16 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32eb150c-384f-39b8-be8f-0fa7e5943dae | -7.44499 | -49.47232 | 2026-09-16 04:14:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca470ff3-fe5d-3f70-93d4-47da12511a3e | -5.49246 | -43.678 | 2026-09-16 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85c13c58-410d-3e7d-85d2-ebe367bd72d7 | -10.83189 | -46.20239 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae748925-cc7f-350e-989b-a786d85a33f2 | -7.43446 | -44.56403 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6696e67-0367-3e77-ba71-bb4bd9e1328b | -11.23981 | -43.47298 | 2026-09-16 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7019d65c-43c8-398f-b3a1-646d5d022c55 | -2.90519 | -50.43185 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 237dfdd0-6844-3e68-987b-bf2ebf435ed3 | -9.22967 | -46.69931 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4dcce413-db23-3b5f-ad27-386df475a1e0 | -6.95291 | -42.57576 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7c1a9955-71fe-36d5-bcfb-1acabd8bbfbf | -9.23215 | -46.69763 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 396be7f2-4a49-3b0f-bd20-c7311188c34b | -6.36998 | -55.8328 | 2026-09-16 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 787a8a02-dad4-3a4e-8fca-c5cea82f98eb | -9.57115 | -46.59003 | 2026-09-16 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4a7bc2ca-1026-311e-8a5b-eef8c6690921 | -5.63381 | -51.69762 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0625d26f-01d4-3313-9d15-6a2c9a45cda7 | -10.40044 | -48.64389 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e2683ad-c703-3979-bc42-eda3f543c775 | -5.40561 | -41.108 | 2026-09-16 04:14:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cff88abe-c6f3-30ce-9bac-85d26d629458 | -9.48793 | -45.45012 | 2026-09-16 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89dced02-0940-3ef0-bcad-d3f486f7a314 | -2.91243 | -50.42215 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 873cdb6b-2fe8-380f-802f-c23445925421 | -5.63201 | -51.69522 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 06daf479-731f-34fc-9a01-b1db832b0142 | -7.572 | -44.93559 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c81dff5c-8672-370b-a72f-423f23934268 | -9.794 | -46.49128 | 2026-09-16 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3eaf2669-893c-3e18-b54f-6978f636d246 | -10.46366 | -44.94435 | 2026-09-16 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f82f0ae2-817e-3bda-910c-ab775adc3795 | -7.33753 | -44.493 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bb46da5-bfcd-32e9-914e-3532546c834f | -7.33402 | -44.49243 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 308542ef-4fbe-3857-b10b-1cbf964d7177 | -6.17172 | -44.01554 | 2026-09-16 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c5386d8-639a-3368-8a36-faf5c2c37e6e | -10.31203 | -45.27007 | 2026-09-16 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44fcb60e-a717-3246-b8fd-5d10638e3d5f | -6.33217 | -41.75754 | 2026-09-16 04:14:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f8a577d7-810c-3841-a951-96030a0d7943 | -8.69089 | -47.55936 | 2026-09-16 04:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db1c85fb-ddf8-3f21-9098-81d41022f4c3 | -8.85096 | -44.89799 | 2026-09-16 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README26.md)
