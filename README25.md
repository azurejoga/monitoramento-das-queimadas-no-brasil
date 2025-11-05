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
| a3b4d3b5-7856-381e-9104-166b2fb9bf86 | -5.45844 | -47.41188 | 2025-11-05 04:14:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5a1082fc-2999-3544-a60c-5b83b5705db3 | -7.07304 | -41.58058 | 2025-11-05 04:14:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 31995208-bc39-3ac8-9901-67c15d75fff1 | -8.59461 | -44.15603 | 2025-11-05 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f28eef51-ca5e-3e0d-92f7-6e89de21b865 | -7.96887 | -43.23664 | 2025-11-05 04:14:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e9488b51-a4ee-3d3b-bfdc-3751c1d9f7d3 | -5.89203 | -49.14932 | 2025-11-05 04:14:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af56a68e-531e-3bff-9220-41ad36f45f4f | -6.21877 | -46.13537 | 2025-11-05 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 24966b95-4374-3f8e-b0fd-34279100b9b8 | -6.07062 | -43.2501 | 2025-11-05 04:14:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 85ee4cbf-a191-3c9e-bf72-77578b8de407 | -7.9421 | -49.73547 | 2025-11-05 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39cc7702-b314-35a3-8a75-d5a9614be7a5 | -9.87193 | -47.46191 | 2025-11-05 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f275cc3f-5aec-38f2-bbe8-78e46b18494e | -7.942 | -49.73692 | 2025-11-05 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91c1146f-f76b-3975-ab32-24ebf3b11781 | -8.05697 | -49.64356 | 2025-11-05 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b3e52cd8-cb1c-3893-bcc7-529d6d609065 | -8.05336 | -49.63847 | 2025-11-05 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7cb832a7-42a0-3fcd-b77f-ce644d95c711 | -8.75181 | -44.23564 | 2025-11-05 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 613b68c2-cdfb-3c7a-9f7b-f543d3c3510a | -6.0591 | -44.69312 | 2025-11-05 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c891ba4d-a195-31e6-a7b3-b735f33a4ef3 | -9.06266 | -48.83028 | 2025-11-05 04:14:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18796755-81a4-31fa-9769-382e3c094967 | -7.07248 | -41.58418 | 2025-11-05 04:14:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| feb417fa-b395-36e4-9d06-721e5b6efe17 | -9.05367 | -46.99927 | 2025-11-05 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e88f36dc-aeee-36de-847f-5f2b2b6711aa | -6.70427 | -40.83585 | 2025-11-05 04:14:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 15be02c2-ed0a-3906-b5c6-91aee539a676 | -6.31645 | -47.38147 | 2025-11-05 04:14:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c3b3fad-a846-3a62-a0c0-c3e1beb9bf3a | -6.71415 | -47.79462 | 2025-11-05 04:14:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 31c98b34-589b-3e8a-a987-b0d2056201f4 | -8.31764 | -40.44785 | 2025-11-05 04:14:00 | NOAA-20 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 62a7ad07-6338-388f-b853-f42f984aec7c | -5.51583 | -46.24041 | 2025-11-05 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3f05f2c-b371-3fa0-80f1-b4e1098e9fd3 | -11.79433 | -43.35819 | 2025-11-05 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e4f786a-eebf-3f17-932d-035f18937f36 | -7.12017 | -45.05676 | 2025-11-05 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d21c7d0-d4f5-3656-b07f-cd1787852445 | -6.06209 | -47.30754 | 2025-11-05 04:14:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6d2b5e9-6fe9-3d62-bf03-afe4ed352ba5 | -6.84872 | -46.29446 | 2025-11-05 04:14:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 48e04f72-8b4c-30ac-8d9d-9063fdd048cf | -9.04729 | -47.0131 | 2025-11-05 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c48d7928-bdd5-3666-b3d7-52f9ea81f840 | -8.30406 | -49.65849 | 2025-11-05 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d01d5aa2-0821-36f5-936a-d09666581093 | -7.33373 | -38.85011 | 2025-11-05 04:14:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b7870c30-3722-32bf-ba73-cf399c4dca8c | -7.30939 | -46.29405 | 2025-11-05 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e28bdc9-d09c-3271-af6e-997dfa7533ba | -5.23365 | -48.506 | 2025-11-05 04:14:00 | NOAA-20 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 15.9 |
| f86f87cb-a58f-340e-9ad8-0e884393619b | -7.44191 | -46.60916 | 2025-11-05 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a621e2ab-de34-3f1c-8e2c-29f726c9778a | -11.73204 | -43.84502 | 2025-11-05 04:14:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b2b899e-b193-38fc-85d7-b62100e3b6cc | -11.29725 | -44.61983 | 2025-11-05 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 425bf5f5-e74e-3650-b504-e54927fb9478 | -8.69325 | -40.54138 | 2025-11-05 04:14:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3fcf54b3-bae0-386c-9416-dfd20f4fd02f | -10.40627 | -44.38826 | 2025-11-05 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| adb20bd5-45bf-3a7b-b38a-5152d88570f9 | -6.19674 | -42.51675 | 2025-11-05 04:14:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 48fd4348-86ca-393e-b8a6-36e9ffec43f5 | -7.87252 | -46.79408 | 2025-11-05 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 394541ef-0eb5-33fc-99c2-cb375cb1e7e1 | -12.33581 | -43.65189 | 2025-11-05 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c013701-5732-35eb-9ee5-191db8df1278 | -8.22851 | -49.9901 | 2025-11-05 04:14:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd694df7-54c1-38af-87cc-922580901db9 | -6.94156 | -42.66177 | 2025-11-05 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d12903a2-a738-3cbe-8baa-a3e964622d9f | -7.9677 | -50.00678 | 2025-11-05 04:14:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b390ab70-8961-3b5b-8b6d-e9aa53aaa4d7 | -8.9652 | -44.11171 | 2025-11-05 04:14:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 540f324c-d56e-31d9-9872-616e4a61bedc | -12.25874 | -43.07457 | 2025-11-05 04:14:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 151c4415-7f9a-3c96-9de2-02effc6271e0 | -7.36366 | -49.87115 | 2025-11-05 04:14:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6efc79e2-5f11-31c5-96d4-78c79ebb722d | -6.43234 | -43.07057 | 2025-11-05 04:14:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d506ecb9-78ac-374a-8a47-24bc08b971e7 | -5.93066 | -43.68286 | 2025-11-05 04:14:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c09faec8-540a-3e79-aacd-5c84ed44e657 | -6.21809 | -46.13951 | 2025-11-05 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e1df61c2-7ef1-3f07-86bd-8a5731e310ce | -9.56001 | -47.80952 | 2025-11-05 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e79ec49b-8b36-39c4-98db-4892edfb40c8 | -7.95027 | -40.18039 | 2025-11-05 04:14:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b19ac9fc-1210-3e3e-94ff-867181be24c2 | -6.98934 | -45.45258 | 2025-11-05 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e94e867-736f-3d88-9d99-0bda59c13c60 | -7.52522 | -45.92609 | 2025-11-05 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4919ad64-1ed8-309d-8e1f-47e20c8e34ed | -10.41675 | -44.38639 | 2025-11-05 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2062ba5-c27a-392c-b8d6-99952fca042a | -8.85226 | -49.88285 | 2025-11-05 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60446a52-3058-33f1-9847-4f174c5849db | -9.88004 | -47.45882 | 2025-11-05 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe372af9-9839-3a2a-bddc-3104d24fb20a | -10.38043 | -47.76057 | 2025-11-05 04:14:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41c18935-60bd-3957-992d-e7f719e0ddaf | -8.93634 | -40.87461 | 2025-11-05 04:14:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 49f57810-6821-3295-8bd6-f40269413b32 | -8.22851 | -49.98426 | 2025-11-05 04:14:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3eb30d9b-5065-3e91-bac9-4750519dcfaa | -8.05769 | -49.63927 | 2025-11-05 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bc20ce68-7362-37e7-b70f-ee46a80caca9 | -7.72368 | -45.81712 | 2025-11-05 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b4eae76-a837-353e-b73c-896bde932b7c | -7.33302 | -38.85496 | 2025-11-05 04:14:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 102ab03d-811c-33f7-bd12-461560f6d87b | -12.65664 | -43.92508 | 2025-11-05 04:14:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0bb8ecc-2571-33ce-ab80-cc8b11459f02 | -6.70687 | -43.56834 | 2025-11-05 04:14:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e8070af-42a7-3107-bf84-e6f62a1c28d9 | -6.52237 | -39.68731 | 2025-11-05 04:14:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 52884faf-818b-3a9c-b0d2-43badecd64c0 | -12.81585 | -43.77566 | 2025-11-05 04:14:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1b765f9d-0328-3312-a56b-8bf4bc7169d4 | -6.27296 | -42.57126 | 2025-11-05 04:14:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5b3b4e28-538c-32fb-87a4-0c989197c3ce | -8.68906 | -40.54495 | 2025-11-05 04:14:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 415bea02-3c3d-3c79-8936-69893d80060e | -6.52202 | -39.68997 | 2025-11-05 04:14:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c9f4cccb-1166-38d2-8105-6e862f14dc5d | -6.74089 | -44.16427 | 2025-11-05 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63a57374-27cf-3c82-b4b8-cde60e4c59e8 | -5.47096 | -46.55853 | 2025-11-05 04:14:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cdbf9d1-19bf-3121-b1c0-bd751111fb51 | -6.46835 | -43.22834 | 2025-11-05 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a2de4a1-9dea-3389-a3d4-432a0f7459a6 | -8.59124 | -43.74836 | 2025-11-05 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef9d2cb5-8edf-391a-912f-fd2fd666c2ba | -9.77456 | -43.61408 | 2025-11-05 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0a8eefd3-3722-3fcd-a01a-35d7671b8ec1 | -6.94849 | -41.13846 | 2025-11-05 04:14:00 | NOAA-20 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b9307722-799a-3a6c-a6fb-56c8a8a5c6e1 | -6.73592 | -44.1526 | 2025-11-05 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| d6d1c4d3-f764-3289-a9a0-2660117552e2 | -10.38196 | -47.75158 | 2025-11-05 04:14:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 59690b1a-d870-3bcd-9023-6f771b671283 | -5.8563 | -43.99813 | 2025-11-05 04:14:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14eb131e-a899-30c7-9798-ec53b2c427ef | -6.37252 | -42.41272 | 2025-11-05 04:14:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| e5cda0f6-ed9d-3bdd-8aa1-25e6fc3afee3 | -6.73258 | -44.15206 | 2025-11-05 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7c834f4f-e4b9-3611-8f9f-ce245e7cb304 | -6.26965 | -42.57075 | 2025-11-05 04:14:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 12842ba8-ab71-36ca-8fd5-3d194dff63b8 | -8.9488 | -40.83841 | 2025-11-05 04:14:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1f3385c9-9ea6-39dc-b0bf-71ead683dbc4 | -11.29781 | -44.61631 | 2025-11-05 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b08001d-c4c2-3bcd-a5b7-c712e05d3d42 | -7.33312 | -46.29727 | 2025-11-05 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0383f20e-f641-39c1-81a5-cf8310567ddd | -7.0391 | -41.46304 | 2025-11-05 04:14:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4e0cc56c-f2f0-3d5b-9d7f-336d5cf8fc6c | -10.37376 | -47.75477 | 2025-11-05 04:14:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3e55d27a-e372-35f2-a38f-2bbefa52067a | -6.58899 | -44.62756 | 2025-11-05 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f59b4858-4325-3bff-bef9-d707957cf7c6 | -9.06205 | -48.83388 | 2025-11-05 04:14:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 722e3d05-1ba8-3f9d-a61e-84e596cd99fc | -11.84178 | -43.72902 | 2025-11-05 04:14:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 653f31e9-85e0-38b5-82e8-1ff8f1b282ae | -12.23444 | -50.28823 | 2025-11-05 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3515567-68f6-3833-97a0-ee94db0f1c42 | -5.65381 | -46.43011 | 2025-11-05 04:14:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27158fa5-2656-33c0-9575-4f4e3fb406cb | -7.06909 | -41.58369 | 2025-11-05 04:14:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 43602e45-2566-308a-902d-fc11f0bd5ef5 | -13.01221 | -43.64612 | 2025-11-05 04:14:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5e81455-5908-393c-b9ea-580f16a95088 | -9.78062 | -43.61862 | 2025-11-05 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bb36c685-481f-34aa-98f8-48f671f19184 | -6.37139 | -42.39825 | 2025-11-05 04:14:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f3c706ad-6d94-3756-a3c7-6fa81e355183 | -7.54515 | -45.84869 | 2025-11-05 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b09cf75f-1825-3113-9f42-e5c6f0be6021 | -9.37809 | -47.07806 | 2025-11-05 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c7f15c2-8ec7-3798-8518-c0a03a481da3 | -6.14552 | -42.38745 | 2025-11-05 04:14:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a23dc7af-5990-3f3b-8c44-62cc133c9ae2 | -7.32954 | -46.29665 | 2025-11-05 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e20a0053-0b27-3c3f-b331-767b14c72672 | -10.39359 | -44.38264 | 2025-11-05 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 836c173a-d8dc-3873-885a-a88ce53080ca | -7.0345 | -46.98603 | 2025-11-05 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README26.md)
