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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28519320-3990-3179-b5c9-c1356178e181 | -7.40997 | -44.25484 | 2026-08-30 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0af7ea7b-23c6-3dc5-9108-54b8b5a5687a | -6.76389 | -55.65933 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e3350f0-1766-3a4a-a3a6-1ef2e3e5b087 | -7.1285 | -44.31654 | 2026-08-30 04:32:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e09a4d51-ab5a-37b4-a4c0-e10473b55a51 | -6.86946 | -41.66595 | 2026-08-30 04:32:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a0b75006-2894-3bdd-9f4b-c59b835d2be1 | -6.93243 | -55.71009 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b14d1231-a205-343c-9c1d-0bd4c2f66f84 | -8.76013 | -50.46795 | 2026-08-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8660ed9c-e386-3265-b1a7-c280759a10a2 | -3.48591 | -54.66182 | 2026-08-30 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ecc46cb7-76f3-370f-ade7-2ad300285187 | -4.9252 | -55.77156 | 2026-08-30 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1b2dee9-d566-3368-9266-5f4c5554dc97 | -2.9534 | -43.25014 | 2026-08-30 04:32:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2878b407-a208-3681-a355-4438af4c9c43 | -5.45553 | -48.93836 | 2026-08-30 04:32:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acf0dc32-7287-3354-9166-c899504f68f8 | -5.48217 | -57.14135 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 09bd8a1c-0be7-3ce0-86a2-73f21998a0dc | -7.09944 | -42.21244 | 2026-08-30 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 52c61f6c-137f-3512-8d77-f40cb6502510 | -7.52601 | -55.31816 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3004f23-d180-356c-a564-25be522e4fb9 | -6.90066 | -41.63166 | 2026-08-30 04:32:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 40854ba4-37f6-3519-b8a8-a7e03d570066 | -5.96498 | -57.68798 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f098152-5b0d-399f-b6a8-3561f4b3a2bf | -6.86598 | -41.66192 | 2026-08-30 04:32:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3c97fa35-be95-3841-93f1-1905c4b72d98 | -3.59503 | -55.30259 | 2026-08-30 04:32:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07d1f705-71c5-3e71-a47e-625b872d6997 | -6.94415 | -55.70559 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9152c761-6bfd-30c7-94e7-79a9109e61e1 | -6.92774 | -55.70572 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fe942a0-bad9-3c8b-8b6f-69a8e6dc8e4a | -5.50374 | -44.01848 | 2026-08-30 04:32:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05d77892-e7ee-380e-9b51-0ae5312585d2 | -8.66541 | -49.54206 | 2026-08-30 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ca07322-6834-3727-8a97-0f0b490b1b70 | -7.40358 | -44.2499 | 2026-08-30 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 219c27af-df34-39a5-90ac-eae383f39bab | -3.59605 | -55.3025 | 2026-08-30 04:32:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0a1f990-09fb-34cd-bec5-a527de438513 | -4.08097 | -45.94706 | 2026-08-30 04:32:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb22abc1-c01d-3b92-b74a-0356692d8daa | -3.26813 | -49.52582 | 2026-08-30 04:32:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d8e39af-0dc6-3962-ba2d-67c0f4b0d806 | -6.49461 | -53.25901 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bec80e80-2430-333f-848c-43f207f43628 | -6.78788 | -55.66992 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cd9e729-eaa5-3b6b-8c3d-a13216ceec86 | -5.48138 | -57.14579 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a4a8241d-69b9-3812-aacc-284e7bd4f769 | -7.49492 | -55.31517 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0622d2b3-9fb2-3beb-ae8e-e189c239922f | -2.5079 | -48.34854 | 2026-08-30 04:32:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f20e8867-5bcd-37f9-80d9-0fa093addc48 | -5.76439 | -51.6824 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| edeb221e-eed9-3d3c-ae24-5ec37826462c | -5.6033 | -44.12282 | 2026-08-30 04:32:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8dbaef2e-1172-3524-9721-2e8a0bcf1d1d | -6.8146 | -51.15401 | 2026-08-30 04:32:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e3603e15-60f5-3d06-9281-9a2860c46572 | -7.61168 | -45.8485 | 2026-08-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99109f85-9945-3754-b843-392b34fd9898 | -6.25996 | -55.42482 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36d01a97-48d7-3244-aaf8-3c7c272931c6 | -7.16242 | -48.21062 | 2026-08-30 04:32:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 73ab0b69-08e3-36e7-bd6b-03114ded20c5 | -5.96497 | -57.68839 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdd565ce-c8ef-319f-b39f-939dbcc95e7b | -6.86332 | -59.47229 | 2026-08-30 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0d7bebe8-2936-3406-b028-72fbdaff6a97 | -5.88868 | -46.11633 | 2026-08-30 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fbd134e-2e69-38f1-acbd-0cc7195995b5 | -7.94671 | -52.45268 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1bb9d9e2-5fa2-390e-87ad-8d2acb5c1186 | -6.76722 | -55.66336 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 69b442c5-5393-3dd6-9319-2b3572314690 | -7.18522 | -43.71499 | 2026-08-30 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c8469b5-3933-3eee-adc8-a7d3a2693910 | -5.88962 | -57.7557 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 912b8e25-f383-34ff-8143-c5d3cbd7c6c0 | -8.50317 | -49.55984 | 2026-08-30 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 436b20bc-c694-3485-af3b-3412844f4757 | -2.77093 | -48.02043 | 2026-08-30 04:32:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e2ea0c2-0595-37e3-a93b-474ce21eb6c2 | -7.09147 | -42.83001 | 2026-08-30 04:32:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b202d77d-0251-35dd-a3e4-38c6a1e4944f | -5.87907 | -57.77878 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 568e3e7d-20f6-3514-b3f4-2c76c46422ed | -5.50839 | -44.6208 | 2026-08-30 04:32:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae676fdf-7c81-3036-9554-0cc17fde4506 | -8.21894 | -40.7717 | 2026-08-30 04:32:00 | NOAA-20 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ee89cafd-bb05-3ad5-94eb-75d8508c5852 | -9.21463 | -46.06292 | 2026-08-30 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2596b272-c88a-374c-ae88-991a3c5feaa7 | -6.40941 | -51.6694 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2767ef38-f113-38d9-9f18-6618cc1f56f0 | -5.75492 | -51.68841 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c52cf1d0-1017-3e16-ae10-8064897fb616 | -6.17202 | -45.91294 | 2026-08-30 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f512c921-c57e-3bfe-bb93-28f0521bebcf | -4.07766 | -45.94654 | 2026-08-30 04:32:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aabaaf75-0151-31b1-94c7-ff6596033a4c | -7.94666 | -44.26882 | 2026-08-30 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a8d91f0-aaec-34e1-9190-15729a2f33de | -7.53334 | -44.34464 | 2026-08-30 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a629eaf8-c53c-399e-b8ba-a98396ff9c5e | -6.91745 | -44.95043 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df2d72d7-05a9-3cb6-9965-58b935c12b45 | -2.0185 | -52.11364 | 2026-08-30 04:32:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8ff42dc-70d5-34ad-8d5a-4c742d295971 | -2.48286 | -46.85641 | 2026-08-30 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37926a38-6e81-3ef9-a9be-eccf5e41c54a | -7.11015 | -42.19406 | 2026-08-30 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7fe4f514-630d-326a-847b-53b4cb443c7a | -6.15255 | -57.80062 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eef2b598-24cc-3cff-86cf-adc9eda25b97 | -6.89017 | -41.75963 | 2026-08-30 04:32:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ff831474-e250-3cbb-ae40-2c9603435533 | -5.80791 | -43.64167 | 2026-08-30 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 04cd22bb-7c29-37b0-a6d7-4c3e54b7782c | -5.97275 | -57.68007 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cb35338-28b9-3de2-a445-1d0a2be209c0 | -6.91156 | -59.48832 | 2026-08-30 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 228c9787-089e-3ede-95cb-698c88e51fc6 | -6.0629 | -44.88001 | 2026-08-30 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0705a4a4-4565-31cf-b892-9303c5bb4cbd | -6.87048 | -41.6592 | 2026-08-30 04:32:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 880283b8-e087-3d2c-9d1f-3debda03944a | -1.58687 | -47.73845 | 2026-08-30 04:32:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8609e883-f4df-3452-a7c9-982b8b06ae84 | -7.61202 | -44.85537 | 2026-08-30 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 2b8062b6-11b1-3935-9712-52826d625031 | -6.67536 | -52.86114 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0bd46ce-495d-3d67-93bb-8aa5586ef82c | -6.86199 | -41.66129 | 2026-08-30 04:32:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| eeb39496-fe40-3149-8d19-d071f7679e56 | -3.49165 | -54.65971 | 2026-08-30 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac27aecd-289e-357c-b6c0-96ee694ca73c | -7.09814 | -45.76842 | 2026-08-30 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4063827b-187e-35a7-8919-571d3b0ed53f | -5.47985 | -57.15437 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 503cd336-10f5-3d46-8b94-36fb57107263 | -4.26897 | -48.6592 | 2026-08-30 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c17a1a9-bdd2-3f08-b9c1-c95aa5b979cb | -5.95885 | -57.68733 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b5c2969-1f6b-36dc-8447-10dfb95e28e2 | -7.04905 | -42.20482 | 2026-08-30 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4760078e-5ebd-3431-9e50-6afa5948a631 | -6.92136 | -42.6746 | 2026-08-30 04:32:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a97a2251-31dd-3b8f-b98f-8a39d2e20b97 | -7.60834 | -45.84797 | 2026-08-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e065e66-8c03-389b-a31c-706c464ba79d | -3.75936 | -59.33813 | 2026-08-30 04:32:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 14f669b8-d98f-3940-adc7-d15132e7cc8a | -7.49548 | -55.31208 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d8fcc632-db2a-3059-921e-a53c73cc5b91 | -6.61691 | -55.44986 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0004293e-fb91-3a1f-942b-67723879dae3 | -4.9519 | -55.84653 | 2026-08-30 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 16eaa698-087f-324d-99b4-7e3eb3b5ceb2 | -6.34178 | -44.09893 | 2026-08-30 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 265e627a-d64d-3c06-b43d-09ff6cc0e82a | -5.99267 | -45.08602 | 2026-08-30 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9b3fff8-9e75-3eca-94e2-fde771a6924b | -8.34464 | -45.65004 | 2026-08-30 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fa08c91-29cd-30a0-b472-3ddf2b4439b2 | -4.96285 | -55.84896 | 2026-08-30 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7ce4096b-31b8-35a1-a983-3fa259ce82f7 | -6.52273 | -51.43788 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce87b727-8e60-3870-ba27-835da915c4fd | -6.87935 | -42.87578 | 2026-08-30 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4edba567-937d-3d96-a3e8-f3e346d58c95 | -6.87736 | -42.88897 | 2026-08-30 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ee2b0192-c5e3-3fa7-8497-967464d68a63 | -5.50027 | -44.01794 | 2026-08-30 04:32:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08761774-04f5-3e48-a045-37c57fa78d87 | -5.96672 | -57.67855 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 479ef66d-9efc-38aa-98af-f2a61595f72a | -5.57536 | -47.42092 | 2026-08-30 04:32:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3bbe9af7-8a2e-3c7e-80b1-b67b3644f2eb | -6.9377 | -55.71116 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 59d213df-05a9-31be-949c-f5c173ebf452 | -6.91219 | -41.63689 | 2026-08-30 04:32:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6fb0be7b-3f81-3bce-a6ef-6de10037c53b | -5.48061 | -57.15011 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 38c9eed9-e8a2-346c-a6bf-54f7442e2dc6 | -6.76446 | -55.65603 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56658016-62db-322c-986b-52c3693deedb | -2.79653 | -49.58513 | 2026-08-30 04:32:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88e39e21-4b3e-340d-bcaa-35795a3e2445 | -7.21186 | -42.7488 | 2026-08-30 04:32:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cc60b527-a970-3647-8b59-07a0953753b1 | -4.08463 | -54.11081 | 2026-08-30 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README38.md)
