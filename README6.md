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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1610832-81b7-35d3-b311-52c644a2c2b0 | -8.83274 | -48.33661 | 2026-07-14 04:57:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d158c05-4433-3b48-9562-b84ac4c21605 | -5.83311 | -43.4756 | 2026-07-14 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94a81f84-b6d1-3e03-ab13-dbb15c3896d2 | -5.52159 | -45.97002 | 2026-07-14 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6741505-fe64-3863-bf7d-a0c636e3d8ca | -7.01087 | -45.41899 | 2026-07-14 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff85e536-2a0c-35de-8181-c3e6af324b4b | -7.6801 | -47.32979 | 2026-07-14 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d62517ab-ece3-38eb-86e2-70419a0cbfe9 | -9.70119 | -47.70319 | 2026-07-14 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02dad1ee-f0bd-3601-82ea-09cbcbaf9dc8 | -6.54446 | -55.15243 | 2026-07-14 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1b1b142-fa5f-34e0-8604-e03122dddeb6 | -3.15667 | -48.57954 | 2026-07-14 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da4ae2e6-10ca-35e8-9ec1-cc4c4ed2263b | -5.31091 | -47.24265 | 2026-07-14 04:57:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9ae07768-4189-3b0d-bb46-a3ca980d01bb | -9.70286 | -47.70214 | 2026-07-14 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a2c515e-d57a-325c-ae67-bc6dd3d6533d | -3.41645 | -49.11885 | 2026-07-14 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf308fac-b008-3186-905f-4356b0e981f6 | -6.5532 | -55.16088 | 2026-07-14 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12b711c7-83da-3b83-a26e-de6711f6dd62 | -5.51962 | -45.96956 | 2026-07-14 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f364399c-d85f-3afd-8856-c59e770d4ab0 | -6.48845 | -42.22695 | 2026-07-14 04:57:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 111a47a0-2f64-3a9e-8416-5485efecb54b | -6.48626 | -42.22752 | 2026-07-14 04:57:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| cc633c36-9505-3763-aeb4-c5e36950efbd | -7.7007 | -49.34382 | 2026-07-14 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f04269f-11d1-3d49-86e1-2be625ca9ecc | -2.79322 | -49.52011 | 2026-07-14 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55b3b95b-ad04-3a3d-872f-006d455ab1b0 | -8.88578 | -48.50727 | 2026-07-14 04:57:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3045f923-4bd3-3987-abe6-a78602d79a94 | -7.01182 | -45.41504 | 2026-07-14 04:57:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3fd613ae-205d-317d-8efd-bbdac24817fa | -4.49541 | -48.29142 | 2026-07-14 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af1a1f76-bede-37b3-b4d1-e06279c6438b | -3.50149 | -48.03719 | 2026-07-14 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 444b3844-3aed-3e9c-963e-772d71192889 | -3.85723 | -54.08227 | 2026-07-14 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bebf75da-f256-3ae2-898c-d4b95d254bd1 | -7.76484 | -45.03368 | 2026-07-14 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 54b1f0d2-8103-312a-8600-d28f5a1db744 | -2.96617 | -48.99202 | 2026-07-14 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1a20167-6232-333d-a3e9-0b12fca4ad2b | -8.73446 | -48.3327 | 2026-07-14 04:57:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a7f2442-5a7b-3cf3-a13e-e356b351519e | -7.77127 | -45.50408 | 2026-07-14 04:57:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c749f94-ff5a-3394-a888-0aa713dc5368 | -9.18062 | -50.8834 | 2026-07-14 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c757c31-68b1-394d-b99d-c84e7edaf326 | -4.94733 | -48.24863 | 2026-07-14 04:57:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b80d1e7d-96dd-3533-91a3-063b359dc688 | -5.30643 | -47.24189 | 2026-07-14 04:57:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1cf2945-a06b-388e-ac68-868629e9dc6f | -5.91313 | -43.62819 | 2026-07-14 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 66b3aa68-d76c-358a-b37d-960543fc3ef5 | -6.4933 | -42.22361 | 2026-07-14 04:57:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 8e3f7244-d397-3f1b-8a66-e3887c821f86 | -6.48908 | -42.22215 | 2026-07-14 04:57:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| ef3dc78b-f3d5-3cf0-be6a-e8c2715f986e | -7.74904 | -45.02776 | 2026-07-14 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ce815162-facb-3ebc-9a5b-0b8e3773dc41 | -12.87506 | -58.28571 | 2026-07-14 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c7a42bd-cbd3-3ca3-b458-bd0488711a63 | -9.55159 | -65.68178 | 2026-07-14 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5a8328e-3099-3565-9f58-462b2007ba6b | -10.08246 | -50.11647 | 2026-07-14 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e6c1e445-5d7d-30b2-b0ac-8d6a9212830e | -12.92495 | -54.22216 | 2026-07-14 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad825278-e599-351e-9ff7-2f3fe7f0fd1e | -9.86715 | -57.80688 | 2026-07-14 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de3e3a8f-ba43-3ac1-9dc2-7c7031149e0d | -10.06438 | -50.12971 | 2026-07-14 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 553128d2-505e-3f93-a86d-eb5ba02826b8 | -11.57786 | -48.40544 | 2026-07-14 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c372a6cd-0456-39fa-a49f-f339df76489f | -10.07451 | -50.1153 | 2026-07-14 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 368c115d-05f7-3181-aeb1-f6964e47468e | -12.88908 | -58.28812 | 2026-07-14 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9841cd0-7489-39d8-88bc-6d9519ac066e | -12.4541 | -49.45123 | 2026-07-14 04:59:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15fbe909-54a5-30d3-9b84-8e125c6bb656 | -15.35264 | -49.61657 | 2026-07-14 04:59:00 | NOAA-21 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4f336f25-8213-3796-b9b1-bd543e9d454a | -9.64834 | -63.54576 | 2026-07-14 04:59:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8ac818b-6f00-3abc-a19a-13c761fdb522 | -10.62665 | -53.90125 | 2026-07-14 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9821e9bd-5459-3a20-b0cd-5a7072f1e6dc | -10.08717 | -50.11185 | 2026-07-14 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f49baabb-d3e8-3fc4-a05d-623cbf681d55 | -10.08319 | -50.11127 | 2026-07-14 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ef92e5ea-fe8e-3a76-8165-8c48cd5745c1 | -12.8834 | -58.27888 | 2026-07-14 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03858f91-9c35-38a0-85d0-6c0f9c7dc7ac | -12.45521 | -46.52631 | 2026-07-14 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5a2adbd-2acd-3f1e-856b-ac0954f24881 | -10.0604 | -50.12912 | 2026-07-14 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| deaef0dd-0962-36df-a6ab-7cca6cbc1fba | -11.57846 | -48.40075 | 2026-07-14 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 233e5198-4933-33d8-bfc2-83e7b0da68ce | -10.18382 | -50.16518 | 2026-07-14 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e226015-759d-3187-9ef5-1780ba721f28 | -12.87857 | -58.2863 | 2026-07-14 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a3876a7-4e72-3843-860b-f2a584a9aecb | -13.76093 | -46.26089 | 2026-07-14 04:59:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 219491cd-60b1-3774-8423-edab95e13f19 | -9.8636 | -57.80629 | 2026-07-14 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec878c27-53d9-3c3f-95c0-0b35184a5888 | -12.88974 | -58.28413 | 2026-07-14 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c63bf05-9958-3543-9653-03f8056326a5 | -11.64967 | -50.14806 | 2026-07-14 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d74186ac-064a-35ef-b0d7-98fc63d16a3d | -12.17847 | -52.90011 | 2026-07-14 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46dc8f68-8ffe-357e-a60b-1a65a1445d36 | -10.07053 | -50.11471 | 2026-07-14 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 0b1cdd50-db2d-3b05-a120-4b9579c7fbb2 | -10.90917 | -56.36496 | 2026-07-14 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c21e9646-0fa4-3cbe-b385-d202f7b1454f | -10.18979 | -50.12276 | 2026-07-14 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4acf0cd-ad7c-32ce-85d8-ecf87561171d | -12.88055 | -58.27427 | 2026-07-14 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 038e382b-2bca-320c-bb38-08057f09a82d | -12.45036 | -49.44647 | 2026-07-14 04:59:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d652283b-4b57-306e-8692-0afd8a0550db | -12.87222 | -58.2811 | 2026-07-14 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31d66a32-e3b1-3768-a8a3-800e972c5530 | -15.35322 | -49.61208 | 2026-07-14 04:59:00 | NOAA-21 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d5028af4-a0db-36c0-8eaf-0526c35e33cc | -10.18532 | -50.12566 | 2026-07-14 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48002b0a-9b10-3040-acce-7baaf954ce22 | -10.09721 | -50.09826 | 2026-07-14 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3aee5e32-c74f-33cc-bf26-bd20845bf26e | -11.95825 | -51.68666 | 2026-07-14 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5cbe80e3-4796-3c66-83f0-f9822c0f6a75 | -12.16003 | -56.54457 | 2026-07-14 04:59:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d9d2cfe6-f65d-3bd1-98fd-b0449cb4f69a | -10.10119 | -50.09884 | 2026-07-14 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 471487ee-94c8-3523-b1d8-5ebcf71801af | -10.07848 | -50.11588 | 2026-07-14 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3ed43629-eab1-3dee-9c24-c2a80a88cc5f | -10.06113 | -50.12393 | 2026-07-14 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| e961a15b-4b3d-3cfe-8adb-0253402cbf41 | -12.87355 | -58.27307 | 2026-07-14 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c26339d-ea7a-3a0a-b7ab-905750daa765 | -12.45559 | -46.52317 | 2026-07-14 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2225fc23-e563-365e-a640-5e11a1b90639 | -10.18484 | -50.12913 | 2026-07-14 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba765f94-d2bd-3540-b0c0-7143155165e0 | -12.87573 | -58.28168 | 2026-07-14 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27aef289-5f4c-3e94-945b-07a4d2d219a9 | -12.44925 | -49.58421 | 2026-07-14 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 037c1eef-99e4-33cf-a948-0cd6afd79fb4 | -10.18025 | -50.13287 | 2026-07-14 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f72da477-3636-34c3-8626-863f8d72804b | -12.43759 | -49.57415 | 2026-07-14 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 26bc232f-c98f-30fb-a065-878da7ec4358 | -12.45466 | -49.44706 | 2026-07-14 04:59:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8897a032-f84d-3e58-a358-a48ce37dae75 | -12.45675 | -46.51351 | 2026-07-14 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eddc6232-21ad-3201-98f2-173c119cb582 | -15.19317 | -55.35431 | 2026-07-14 04:59:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ad54c08-8110-3db2-8815-47da052d4f4b | -13.76054 | -46.26433 | 2026-07-14 04:59:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a8672a15-a114-3112-b170-6d8c21653909 | -11.58302 | -48.40139 | 2026-07-14 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 384cdde2-752d-3c87-b55a-29d51e9a2598 | -12.37155 | -47.88599 | 2026-07-14 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68b27539-bc83-3223-9370-06cb2b5fef3c | -10.82855 | -49.38118 | 2026-07-14 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78f2a101-4e8f-3196-aa7f-d8fa73cbca50 | -13.75538 | -46.26126 | 2026-07-14 04:59:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56add06a-2c78-3611-9f4c-fe9fde19d5d3 | -12.87705 | -58.27367 | 2026-07-14 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34dd443e-8125-38e0-a5e6-eb455796a975 | -11.95454 | -51.68614 | 2026-07-14 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2e05ae16-14b8-3db8-a9b5-886ff372a7ed | -12.88842 | -58.29213 | 2026-07-14 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cf6b215-53d2-3551-947e-5db50f1cd13d | -12.32697 | -50.01791 | 2026-07-14 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 344b7240-4054-3a31-804c-78364315d79e | -10.83331 | -49.37783 | 2026-07-14 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96f71902-af68-3b9f-9ff1-56ea3c5b5d06 | -10.0651 | -50.12452 | 2026-07-14 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| dac67539-b3e5-3dab-a56c-313d7ea971e4 | -12.87288 | -58.27708 | 2026-07-14 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd2f7bb7-30a3-3340-b760-20ed767bd50b | -12.45636 | -46.51675 | 2026-07-14 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3f7be616-2ce1-38d9-990a-2f41af8612d3 | -12.45597 | -46.51999 | 2026-07-14 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 04a17736-0ecf-3493-ad58-ed1324e3c119 | -12.4535 | -49.58485 | 2026-07-14 04:59:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5709136-aa73-39fe-9dd5-fe61b9bfb840 | -18.78574 | -52.40566 | 2026-07-14 05:01:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 408701b1-4e48-32e3-8570-75b35a195c35 | -18.778 | -52.4044 | 2026-07-14 05:01:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README7.md)
