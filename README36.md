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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50c11966-e1e6-38ab-913a-bb8891cba7c9 | -9.21129 | -46.06239 | 2026-08-30 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7aec639c-5f18-361e-9afb-b89eac218706 | -6.78546 | -55.68333 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a4a2a6a-d806-3d8d-a16a-0e2f3f1aeb3c | -7.00605 | -59.65197 | 2026-08-30 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| de020ace-1748-3eeb-8a77-f3a3768610d6 | -3.48536 | -54.66499 | 2026-08-30 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57669bc0-9815-3cf1-b1c5-2bbc8fbea5e8 | -3.27307 | -50.02219 | 2026-08-30 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2640449c-a629-3e66-82fd-658f6f4dcd16 | -5.95975 | -57.68216 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3307555-1b0c-3034-8978-5f053efcc40d | -3.76087 | -59.33876 | 2026-08-30 04:32:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 61a56268-3ce9-3f8d-a039-a9ad62e485b2 | -6.9127 | -41.63337 | 2026-08-30 04:32:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3b91b1ba-0d69-394b-9a15-6f0ba4d8be20 | -5.87286 | -57.77804 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 35b4eee5-c640-3386-a349-bc9a8fd85bb1 | -7.52776 | -44.44996 | 2026-08-30 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 923abfd6-cdf9-3349-ab0c-3b6e5473428c | -5.9597 | -57.68254 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea54a5e8-2cae-3601-8b61-9054d83c9135 | -6.16826 | -57.78426 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb6736bf-14d5-3ca0-a2fd-0ff2470660eb | -8.01304 | -48.00803 | 2026-08-30 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 815be7fa-391e-33cc-b7db-47d7eb391a82 | -4.95674 | -55.85143 | 2026-08-30 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 351f27f8-e605-3777-9b76-160ea2099734 | -5.87405 | -57.77493 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b5e06e3-a7e1-31f6-9e82-53afd23da83b | -6.43815 | -41.54889 | 2026-08-30 04:32:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 92411d02-c2ac-30b4-81a2-d429be86ded2 | -7.04589 | -42.19934 | 2026-08-30 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 91137baf-af90-3ed6-838f-abcf45f2c779 | -8.38505 | -45.76619 | 2026-08-30 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4321084-46c0-3b62-837a-80faa86b630d | -9.21742 | -46.06702 | 2026-08-30 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ee93ec4-cf3d-3b62-81a9-67bf5fdfc6f9 | -3.3632 | -39.81992 | 2026-08-30 04:32:00 | NOAA-20 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0785bf60-40c9-3c40-ad0c-eaf222f33303 | -7.29289 | -49.95844 | 2026-08-30 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 75ea6f1d-7cba-32f4-b171-f2f977dcf986 | -6.93829 | -55.70783 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 85bf99f3-5836-373f-9410-d8831320392d | -6.67729 | -58.75225 | 2026-08-30 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 782286f3-22cc-3644-9094-631ec61cf82b | -7.10202 | -45.76541 | 2026-08-30 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b7742f2-8c40-3e53-9342-c48198df9ef0 | -8.20253 | -44.81691 | 2026-08-30 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b852cb1-aabd-3f25-a4cd-99c1b23c26e9 | -6.49218 | -53.27322 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d09b79f-c3d6-34ae-9ee1-914a428fc9f1 | -6.11357 | -53.55928 | 2026-08-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f4f402c-dd8a-32ef-bca4-c4f7b9c9517f | -3.49105 | -54.66248 | 2026-08-30 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d6af61a-f7a7-34ae-8146-175238ee3c04 | -6.95815 | -44.23197 | 2026-08-30 04:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4240b2f8-7d78-3646-852d-e728c5658b7f | -4.47961 | -55.76271 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e382bfb4-7eb8-30da-86dc-36424c37f1ea | -7.52836 | -44.44608 | 2026-08-30 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1700ee08-c517-3241-b797-61927a1b8568 | -7.10312 | -42.18802 | 2026-08-30 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 31239a6d-4703-39d7-8946-44a361ee3f2d | -8.79454 | -50.48707 | 2026-08-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6fdfeb7-443a-37d1-9cea-c78900cdfa9e | -6.92715 | -55.70904 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 410bedbc-9ce1-31a7-8677-4a0755a5b599 | -7.51164 | -55.28095 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3883cdb-036f-3e2e-993e-4bf8dd45cff8 | -6.87397 | -41.66321 | 2026-08-30 04:32:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c971e15e-c044-37e0-82a5-8a16b484c269 | -5.57479 | -47.42447 | 2026-08-30 04:32:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b29a064d-de81-339d-b366-b37b5139950c | -5.8904 | -47.72652 | 2026-08-30 04:32:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e28e7c9-e84e-3eee-9817-723ed8a7470d | -7.29924 | -49.53975 | 2026-08-30 04:32:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 645c5726-7011-33b8-953c-09907f101754 | -5.61848 | -49.36092 | 2026-08-30 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3124dba7-67de-3d53-8c7f-4ebffd76ba0b | -5.88782 | -57.76559 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0d62367-31c1-3bcb-b370-5807be63ca94 | -7.09267 | -42.23107 | 2026-08-30 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7f682c7e-2633-39c5-844e-1af4f95bc719 | -6.87869 | -42.8802 | 2026-08-30 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 76c57fa6-79b8-3bd6-b9a1-12195f7db821 | -2.79561 | -45.58871 | 2026-08-30 04:32:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4fd7a164-af7e-3494-8eaf-31bc9671c9b6 | -7.27835 | -49.84349 | 2026-08-30 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3b86121-7ddf-384f-aacf-c21305ce3515 | -2.93499 | -51.48349 | 2026-08-30 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 592b6ee4-9122-30b9-a205-3f07e6112c4f | -6.86342 | -41.67892 | 2026-08-30 04:32:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6f144586-dcd9-3cb0-a67c-092bc8596167 | -4.95252 | -55.84294 | 2026-08-30 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 08e62d05-f190-3ce8-8b13-d58d32137ae2 | -6.94126 | -55.72195 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d690e6ea-ed1c-365b-918b-cbcae1be541a | -5.49405 | -57.14356 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 64b87188-9453-3174-a867-d0ca8c2ca439 | -6.8743 | -42.88406 | 2026-08-30 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 914823cb-e009-3f2a-a052-6ebc89f84ab6 | -7.04129 | -42.20369 | 2026-08-30 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9d79d749-0b5d-38bd-97c7-e155b697e4d0 | -2.09786 | -48.21806 | 2026-08-30 04:32:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81beed5d-cdbf-3acf-be83-1d9221b6241f | -4.10586 | -47.22019 | 2026-08-30 04:32:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b23fb257-035a-329f-98e0-e5c6c3f138ca | -7.32022 | -45.34149 | 2026-08-30 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a58bd34e-bb47-3635-be26-9cc078f02c9f | -7.1269 | -44.31488 | 2026-08-30 04:32:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d6172ea-1aea-3ca2-bc22-e66450a8bcb1 | -8.14971 | -45.50571 | 2026-08-30 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 674c138c-96d3-3259-9168-7cf479a676fb | -6.82664 | -42.87244 | 2026-08-30 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fa3932c3-5fd3-3f1e-8a57-95642d0d3820 | -5.29027 | -50.94032 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fae7cdb9-0ef8-3c7b-8f73-86d62957d1f8 | -6.85027 | -42.86692 | 2026-08-30 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 77d77deb-8696-38cc-96a6-ec4c9a76dc5f | -3.69166 | -51.9999 | 2026-08-30 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 754a501d-9a15-37d1-b781-1b22494ebbb5 | -7.98075 | -45.50587 | 2026-08-30 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41f43c70-ae0c-32c0-a557-94e1c37c7fde | -2.80029 | -49.58575 | 2026-08-30 04:32:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b08fae82-3273-3ba4-8665-9103c63b6d7b | -6.86913 | -56.57037 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03970175-429a-302c-b193-88b7b43a8f6c | -6.78665 | -55.64649 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59ee7f85-aa9a-3137-bf0b-718571bfdca1 | -7.08637 | -42.22031 | 2026-08-30 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ca576aa5-ba4c-3535-a84f-636b06fcf5f4 | -6.96979 | -45.41146 | 2026-08-30 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4dfec38-dc60-3691-9984-02aa79a8c95f | -8.79381 | -50.49141 | 2026-08-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00c9c706-3ec4-30bd-9ecb-7e4836022b56 | -5.60792 | -44.11579 | 2026-08-30 04:32:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a85a1f3-1e8f-3ef6-b6b5-a407b570ef7d | -6.07913 | -57.89315 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 52792313-dc45-3496-9401-684cec6155a8 | -7.12714 | -42.82177 | 2026-08-30 04:32:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6f617259-dd49-31fe-ae23-c6403333abbe | -6.71192 | -58.56623 | 2026-08-30 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 11f8224d-a858-3a53-8f67-3be0d9423e5e | -3.21981 | -49.2278 | 2026-08-30 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ee31d39a-4e4c-3e8e-af38-6a378f2eebd4 | -3.32793 | -42.86496 | 2026-08-30 04:32:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b003aee-27f5-3235-88f2-7cf50c024e1d | -7.12485 | -42.76123 | 2026-08-30 04:32:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 442124c5-3c94-3f2d-8df2-53a3a15cce0e | -5.04581 | -44.69044 | 2026-08-30 04:32:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 64e2a117-b48a-359c-8ba4-a472174f739e | -6.88241 | -42.88073 | 2026-08-30 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6996fa76-613a-3e95-8ad1-2b3fc3b91852 | -6.85891 | -41.68174 | 2026-08-30 04:32:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 91ba26c1-bb90-365b-9cfc-6fe110e16206 | -2.25158 | -49.52719 | 2026-08-30 04:32:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9236546f-c5fb-3c1e-bf11-d67a216ca7aa | -4.35564 | -55.02808 | 2026-08-30 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 079bf77a-bdb3-3625-bb78-f25400593366 | -5.96586 | -57.6832 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0563deea-29b7-3ce8-bfbd-7348c5fe767d | -7.5627 | -48.36118 | 2026-08-30 04:32:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1023374f-5562-3ecc-b0ee-175063804b5a | -7.09727 | -42.22686 | 2026-08-30 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2b0ce3bd-d5de-383f-bb8d-54dc76e90a21 | -6.78847 | -55.66667 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 461ce108-b0c7-34ee-b4eb-6a0823f5c6b4 | -4.0782 | -45.9431 | 2026-08-30 04:32:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 245cd147-f0f0-369a-9f82-c7e696c6cfa5 | -3.22348 | -49.22839 | 2026-08-30 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1fc71dd3-a010-340b-9eda-72a0746111b3 | -6.31529 | -54.74461 | 2026-08-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc75f548-025a-3715-8e12-cc6103154dcf | -7.61259 | -44.85163 | 2026-08-30 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 2dd772cc-83b0-3896-aa97-473ec0327411 | -5.87487 | -57.77027 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c0749156-8311-33fc-81a3-33335936580c | -6.63867 | -53.18457 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f1c870f-1f6a-34c0-8f0c-b3ab2afe9ec8 | -7.21066 | -44.02139 | 2026-08-30 04:32:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ead4a66-c291-3bc1-b754-86f866f83799 | -7.32362 | -45.36406 | 2026-08-30 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d79cf9c3-a7b2-37a5-9f7e-94dc6fd1991b | -6.53649 | -55.10401 | 2026-08-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbbaeec8-7a47-3011-8de0-ab9aff68ec32 | -6.86445 | -41.67206 | 2026-08-30 04:32:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c795136c-65bc-3935-84f0-c54b015a4263 | -5.97024 | -57.69369 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7895b701-493b-3cd6-97e9-b6edcdf6de9e | -5.89571 | -57.75708 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 042da0b1-49b3-3b0b-b671-05aa479e55a8 | -6.77147 | -55.6471 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ef6118fe-0690-3044-9b7b-50421c24629f | -2.79725 | -49.58057 | 2026-08-30 04:32:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ffd4886c-3c1e-35fd-b887-688f8cdc7a07 | -6.60262 | -56.38416 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84a0ab21-ffd3-3a60-8f1f-257db32a06ea | -7.11984 | -48.06619 | 2026-08-30 04:32:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README37.md)
