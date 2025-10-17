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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2f95393-1636-38c1-9c52-5b5b23345a1c | -8.06337 | -45.41556 | 2025-10-17 03:28:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db7241da-e89e-36c1-944a-b0c9125e3971 | -7.3582 | -41.90946 | 2025-10-17 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2ad480e2-9b58-3ebd-9412-97c12b8ccd76 | -6.20023 | -41.75948 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6ffa0ced-c1c5-3262-a4c4-6a0ec9a8c8fe | -6.02104 | -41.93163 | 2025-10-17 03:28:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5c800dd5-72c6-3c5a-8857-8cb0b61c4016 | -6.1475 | -41.79447 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 68e9c599-537d-39d1-8f70-ec3f72723c8e | -7.98232 | -44.16261 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 254bd00e-4b19-3ac0-ae24-1079e0248f55 | -6.81577 | -41.70658 | 2025-10-17 03:28:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 284c8822-49cf-3d4b-8d68-f6d49d6cdfdc | -7.94564 | -44.11288 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e8e1e108-ebee-3bd2-b73a-c4f7b90237c4 | -6.13331 | -41.77652 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6e092b5a-861e-34d0-8fa1-dea79abe8cc7 | -4.94816 | -44.9687 | 2025-10-17 03:28:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f0afd96-5e74-39c4-bc03-5a4965fde5c1 | -6.37552 | -41.4748 | 2025-10-17 03:28:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 139c2a42-d211-31d4-a09f-1f698f17f872 | -8.25698 | -44.06533 | 2025-10-17 03:28:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f84ae990-ff70-3176-87fa-4b1ad59fca73 | -8.38026 | -46.26144 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 299a4312-b2fe-3bcc-a566-019b5cd634d8 | -8.35545 | -40.33216 | 2025-10-17 03:28:00 | NOAA-20 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0917a469-1804-3522-90a1-7d916915ce0e | -7.94697 | -44.15335 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4186a81-630c-3dfd-a25c-452eceb5fbfc | -5.99079 | -44.15434 | 2025-10-17 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c645b11f-7525-3484-a1c1-837b51a8fb18 | -4.94781 | -44.96158 | 2025-10-17 03:28:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 536319ef-8b48-3a3e-9ee1-32a8a15d4523 | -6.08794 | -42.39049 | 2025-10-17 03:28:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c7c25880-4ddf-3ff4-9d41-7ef4affd3a69 | -6.83513 | -42.42132 | 2025-10-17 03:28:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 40e7416e-48a6-3225-abad-0ef56a19e454 | -6.39634 | -41.48437 | 2025-10-17 03:28:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 79d864f8-70b7-3830-b814-321b23f497b4 | -6.83586 | -42.41727 | 2025-10-17 03:28:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 00eb5cdc-c4e2-3dbb-b8e0-5338943992d6 | -3.55858 | -40.52155 | 2025-10-17 03:28:00 | NOAA-20 | ALCÂNTARAS | CEARÁ | Brasil | 2300507 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3bb8163b-6696-364f-a8bd-207f12da3fb3 | -7.32604 | -44.16541 | 2025-10-17 03:28:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9466869c-8a17-3182-a4a4-88f6db1a1e12 | -5.90199 | -44.75605 | 2025-10-17 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9d883a96-4591-3c5b-b5e4-24ced5143bfc | -7.17329 | -42.36826 | 2025-10-17 03:28:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c1673a0c-a18d-3ccf-ba39-e7abc9e53739 | -9.15893 | -41.05586 | 2025-10-17 03:28:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 14fe8054-aa16-3a28-be7c-e9aed84b2eb3 | -6.69047 | -40.87815 | 2025-10-17 03:28:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0cd2d69d-9448-31a1-8a27-a302a601c6de | -7.47895 | -42.76309 | 2025-10-17 03:28:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5edbef94-4830-360e-b15b-6841e9b61a2c | -6.99664 | -39.23026 | 2025-10-17 03:28:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bf70f2c9-98c2-3344-8545-539db84e57e7 | -4.40645 | -43.4115 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| dad58e51-78f0-30c8-8338-18a5f75a8321 | -5.35696 | -44.82336 | 2025-10-17 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 125ae80a-f28a-30c3-8921-959440e11cad | -7.95331 | -44.15457 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efa20f19-3e9f-3055-8ec3-cb2e0b691238 | -3.97545 | -42.4902 | 2025-10-17 03:28:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| ec143217-da61-3be4-89e3-de49ee3c713f | -7.94661 | -44.12132 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f12b5a49-ee3d-33e3-98e2-c8f459b32fe7 | -7.20235 | -45.49424 | 2025-10-17 03:28:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 896debeb-b7cf-33b4-8550-0b1467db4cf8 | -5.88929 | -43.90461 | 2025-10-17 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 354d842f-5dd7-38d8-9584-038fab6012b0 | -6.41485 | -42.56993 | 2025-10-17 03:28:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f3ce9f2b-6167-32f4-9210-c15fbf9a7560 | -7.56319 | -41.00842 | 2025-10-17 03:28:00 | NOAA-20 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 402d09f0-3148-3fb7-8a84-36dabf4f8d96 | -7.45785 | -42.1623 | 2025-10-17 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 205798d4-f06c-3a35-9f28-72043585730c | -8.45751 | -44.17467 | 2025-10-17 03:28:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a6e888a5-09ec-38d0-9cb1-769209492edc | -8.06359 | -45.41844 | 2025-10-17 03:28:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 882a8bf3-223c-3350-9f00-7bf0465e6579 | -7.89602 | -44.98416 | 2025-10-17 03:28:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5ea7947d-8f31-300a-ae5f-ec7c9c9cead9 | -5.85451 | -43.87634 | 2025-10-17 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 321746e3-a7a1-3b86-9e22-dbb71ca39cd2 | -6.12842 | -41.75438 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f7ee0d45-37d9-3e64-9502-33cda040154b | -6.75391 | -42.37406 | 2025-10-17 03:28:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 764fbf11-68ff-3609-8dfe-3c61c12427b7 | -7.1816 | -42.19238 | 2025-10-17 03:28:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b02f8d77-86ec-3817-9637-14502918d254 | -6.31589 | -40.94939 | 2025-10-17 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 40689d1f-600d-365a-9916-b33d30437b00 | -6.09302 | -42.39591 | 2025-10-17 03:28:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 24152033-2007-311e-a6f2-1d97f61a43c2 | -8.30273 | -43.41525 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9a3f9cf9-3985-3f56-a7d8-2dab928b7069 | -4.40462 | -43.42194 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1a93190c-be8e-30ac-a158-e5e0f3a86d22 | -6.20298 | -41.74402 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| c8d96715-b5e3-3867-909c-40e21d3f5b54 | -5.87915 | -43.92207 | 2025-10-17 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 699e9f5c-a5e2-3d03-905c-6dfd41e3a7e8 | -7.45928 | -42.67089 | 2025-10-17 03:28:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 04e02de6-681e-3e64-8a44-018f06373d87 | -8.19367 | -42.35801 | 2025-10-17 03:28:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3f0bc8bd-7ebe-351c-b42d-539c1563659e | -8.44933 | -44.18338 | 2025-10-17 03:28:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3c4dac75-b285-3c82-8c1d-0a0dfbebad04 | -7.4664 | -42.14776 | 2025-10-17 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 57ffe8c8-8093-34af-98cc-823f3573f9e1 | -6.32265 | -44.31726 | 2025-10-17 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8ef2079f-0c2e-38bd-a17d-829551803d52 | -8.32165 | -40.38464 | 2025-10-17 03:28:00 | NOAA-20 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| df9f552f-ef5d-320c-8f91-f224208fbc4b | -6.07294 | -41.90413 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d4cfc8a5-b101-31ab-be0b-ae297a4067c3 | -6.55941 | -42.96399 | 2025-10-17 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20fa0ff1-15f5-3a4a-b8e9-e2caaf5e2d87 | -8.36885 | -46.31785 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b4509da7-a4e7-3536-b598-00008b3f9dd3 | -5.25719 | -44.21095 | 2025-10-17 03:28:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 89b6c6ce-08e6-3c26-ba32-5a34eccc7a09 | -5.84702 | -43.87789 | 2025-10-17 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9ba7d8b2-0f3e-3f36-a508-9c3f26aec303 | -6.09383 | -40.89204 | 2025-10-17 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| efdd8cfc-ef07-315f-beba-6d67c17ae00b | -5.29105 | -43.55447 | 2025-10-17 03:28:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 2032ccdd-387f-3ed6-b94b-8dd53e1adf86 | -5.25254 | -44.2155 | 2025-10-17 03:28:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02245087-078a-3365-9bd8-5426fcbc7bbe | -7.47972 | -42.75879 | 2025-10-17 03:28:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fdffd5f1-f3d4-3ac1-a63e-7bf603de7a8b | -7.18318 | -41.68453 | 2025-10-17 03:28:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 103bb460-c23f-3c08-89ca-956d141a3b40 | -4.8127 | -43.2025 | 2025-10-17 03:28:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7be74ac9-5ce6-3d1c-8e4c-f0e5a53d1a6a | -6.13254 | -41.74883 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 95723a2d-b681-3a41-a76b-a480362ca4ed | -6.15583 | -40.9136 | 2025-10-17 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 624b45aa-044f-365c-94e8-e2b15adb8cb7 | -5.2495 | -44.21541 | 2025-10-17 03:28:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7da3d816-29f1-3974-9011-1392c8d4c96e | -5.50662 | -43.87621 | 2025-10-17 03:28:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7b11101c-268b-3180-9bf7-752cf4392efb | -7.03951 | -42.73625 | 2025-10-17 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4267f21f-207b-3d6d-aadc-33dc99c90f34 | -3.97991 | -42.50063 | 2025-10-17 03:28:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7d70f6d5-2737-335c-b0db-0af782ed07bd | -4.38915 | -43.39708 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff371a9e-e8d8-3443-b233-632a5e6b7452 | -6.34512 | -41.51812 | 2025-10-17 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 06fc2b9b-f420-368e-99ef-48012f2bf4be | -5.29903 | -41.08531 | 2025-10-17 03:28:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fa9ee770-345d-31d5-a51c-26e77ee3d223 | -5.84604 | -43.886 | 2025-10-17 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3d9117e9-f5fb-3cef-962f-c0d8ef972e2f | -6.3614 | -41.49047 | 2025-10-17 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 62a34fa2-3d84-3f71-b9c3-c43ad5be6cfd | -9.15217 | -41.06405 | 2025-10-17 03:28:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a3fb4626-2277-3cd7-aa39-920995e4e3a7 | -8.37403 | -46.31309 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b435e91f-f67d-30ba-906c-3154d7cf6f52 | -6.22442 | -42.50093 | 2025-10-17 03:28:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 70480264-c3c9-3981-8577-a3fd91468845 | -5.85192 | -42.33915 | 2025-10-17 03:28:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 13a1212a-d8cb-3105-914b-213f98cf113e | -8.72947 | -43.87267 | 2025-10-17 03:28:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6473ff93-a705-3b27-9098-de0914468ad4 | -8.56015 | -44.58783 | 2025-10-17 03:28:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55bd7a5a-50da-303d-954a-c58e7a87842f | -4.39276 | -43.41412 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5b98a86a-44ee-33b9-bed3-4be3252ed279 | -7.66421 | -42.59533 | 2025-10-17 03:28:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 06b80f17-157c-3012-9fcf-0a9fa975e13f | -8.21006 | -43.31231 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 452823f3-5a92-3e13-8a69-8dbbb79527d8 | -3.58546 | -42.84275 | 2025-10-17 03:28:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a72805a1-df9a-3a46-ae9e-36e92109c5ad | -8.45118 | -46.23887 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 5618ee86-c684-3bdc-8ef0-318c7d55f0f7 | -7.94908 | -44.12954 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b2d22308-7e98-373a-9687-6ec007d6ee59 | -7.84005 | -45.46766 | 2025-10-17 03:28:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 218c065f-b070-30aa-8e40-bd7ac1f11984 | -6.48957 | -39.60719 | 2025-10-17 03:28:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3be6dd65-b091-3731-a371-12f14ed6217f | -5.25357 | -44.20974 | 2025-10-17 03:28:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2fd77e45-0765-3b4e-aa2d-6b49036de6db | -6.0938 | -42.39156 | 2025-10-17 03:28:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 41257341-7979-3b40-b27e-f27cdd598583 | -5.88391 | -43.89758 | 2025-10-17 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e008292d-4ed4-3d8d-9f01-52116f5c9707 | -8.45561 | -44.18472 | 2025-10-17 03:28:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c91a4ce8-5c75-3068-9ece-2b0173219353 | -5.98975 | -44.16008 | 2025-10-17 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7c78970-b480-3664-ba44-e0e43f44fba8 | -6.13122 | -41.75605 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README24.md)
