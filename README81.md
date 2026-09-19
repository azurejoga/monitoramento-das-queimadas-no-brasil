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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc2fb8cf-2346-322d-a827-d58723565f5d | -7.21649 | -49.63401 | 2026-09-19 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 589057ae-4637-3ecb-9805-e904baf2941b | -7.81382 | -44.95573 | 2026-09-19 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 922d8d78-aa4f-334d-b1bc-dcc73fafb25c | -9.2402 | -46.18727 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89b9bc92-8981-343f-a39e-2195097de57c | -10.52742 | -46.71862 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f175e501-d6fd-3ea8-a229-809d7d404877 | -6.6535 | -50.9148 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 817b57ef-fd72-32ac-abc5-a262df6b5a38 | -3.19051 | -57.87477 | 2026-09-19 04:57:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 154e46e9-fbac-3547-a075-2c9549493a07 | -7.95327 | -54.88818 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c78d246-f480-3c81-a8e2-d795d4d3f259 | -2.90091 | -54.18623 | 2026-09-19 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 072ba7e2-fe65-30db-b5fc-09f777b94c54 | -9.80969 | -46.40275 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bb230eb5-18b6-39b8-b0ea-7a5ceb771b63 | -4.44316 | -55.00947 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 404a6bf8-d478-3be9-b634-5af1cea17c15 | -7.59606 | -55.69671 | 2026-09-19 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e014aa19-cc9e-39bc-91dd-8118cdb0d53f | -8.88315 | -50.78447 | 2026-09-19 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae766402-9ed2-3d6b-b7a2-2eda009162b8 | -7.60672 | -45.4349 | 2026-09-19 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| da8fd75a-3fa9-3796-aa2c-b165a84b9391 | -7.01992 | -47.44059 | 2026-09-19 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9fe87e13-f41a-3d14-b3ae-e4ff56296d4d | -3.35402 | -50.46207 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d88e587-5a2c-331e-b7f7-a2a165c5e2a9 | -8.76596 | -48.7565 | 2026-09-19 04:57:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| db4f17d3-be6f-31b2-b5bd-fdcc5922cd2e | -8.60619 | -54.59874 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27c6d50a-84ed-343c-a052-7e7d4e66b75e | -7.64912 | -46.10777 | 2026-09-19 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 21e1f5df-8edf-37be-817a-9af8c651bbfc | -11.37705 | -47.03288 | 2026-09-19 04:57:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5418afcc-27d3-3050-9d53-e08bbaf8589a | -9.8879 | -46.54462 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac34f547-6b1b-319a-860f-d4005db3a63c | -6.01343 | -51.79541 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ae9d727-635a-3459-8ea1-b962823742f0 | -9.94031 | -53.98821 | 2026-09-19 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a29bdaa7-1b1b-3551-9c03-5e94f2ddff81 | -9.56786 | -46.56193 | 2026-09-19 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 63375874-7cfc-3ce1-82fc-b9be7369a8e8 | -7.05436 | -47.49565 | 2026-09-19 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5dc766b4-ed4f-3c31-8581-f66aa4b0c8fd | -3.36252 | -50.45221 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b690d0d0-f471-3381-a5aa-a631affdd3d6 | -11.30033 | -46.77407 | 2026-09-19 04:57:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e070604b-f594-38c1-bd34-49ac272e9af8 | -6.987 | -42.18724 | 2026-09-19 04:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ab5acd09-2f30-38ac-a10f-5525df04d5b8 | -11.12466 | -45.28314 | 2026-09-19 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a13be48-7899-34c7-8964-c04412facda4 | -7.63862 | -46.11574 | 2026-09-19 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2f518e7-5fae-3b8b-a34b-964f69724b1b | -3.76051 | -55.95609 | 2026-09-19 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 591cc8d7-c386-3246-89a4-7ea12a04c12b | -9.92349 | -46.59272 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4dd780e4-1ff9-344c-afaa-46c8b6273442 | -7.86091 | -44.87404 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45fb7e99-ee85-3d4a-a55f-2d5c8a934ded | -3.36592 | -50.45274 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 324b367c-6f2c-3503-911e-a48ea66dee29 | -8.45022 | -45.71702 | 2026-09-19 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f8bd804-184d-3237-95d4-0318803c0cce | -10.79744 | -50.88695 | 2026-09-19 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 00d3354e-8a31-3a9b-94cd-79391f2a5c71 | -7.75461 | -54.75079 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a143ba2-48be-386c-899c-13c7afc407d8 | -5.64801 | -51.7026 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67b91216-85ec-3b17-b236-e545956e13ff | -7.66879 | -46.13475 | 2026-09-19 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fea23ac-d3a0-34ad-9bac-d15ff5a9ac75 | -8.12684 | -44.8274 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9628ba4c-0947-3f29-ac7f-e4d68d3ccc59 | -11.22795 | -48.36425 | 2026-09-19 04:57:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8871429e-4d70-37a5-8c4e-37d0e45985d1 | -4.48789 | -55.49229 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e82c923-5ab9-3698-81d7-439ab0ceb958 | -10.81929 | -50.16814 | 2026-09-19 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 47a457cf-7ec9-367b-9570-08f47a527336 | -4.71689 | -55.69477 | 2026-09-19 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ef057df-a532-3df5-94c3-2563fa6ede12 | -11.08037 | -48.30354 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c6bf7a2b-2726-356e-80d7-709985040f2c | -8.89126 | -62.44444 | 2026-09-19 04:57:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d02ce00d-c9ca-3e98-b571-8a2c65dbcc4f | -8.46874 | -47.00911 | 2026-09-19 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c6c48be1-5256-3396-af7c-ae31d589b86a | -4.53593 | -54.9312 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff3ee0d4-573f-3040-8755-4bd7610ed220 | -4.48823 | -54.97623 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4424ed9-3212-3833-b260-ec6ecaf99f06 | -11.22848 | -48.36045 | 2026-09-19 04:57:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64aaca87-5da9-3b92-91f0-b9512fb2e09d | -5.86479 | -52.05236 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fdf865e-c84c-350a-a2aa-bb3b11d45e90 | -5.47177 | -48.99592 | 2026-09-19 04:57:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7882edc6-743e-3ee8-b630-ff832aaf0395 | -8.00795 | -54.85194 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4930be88-f8fb-3fff-9e7d-d13a7a8226c3 | -3.36764 | -50.73708 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f7f9caf-9ff8-3689-b0b5-a0f4927b8779 | -6.36514 | -58.29313 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed3e2973-20d9-322d-a325-215c2fb91aa4 | -4.40784 | -55.49789 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab74378b-d1dd-30ae-928a-f2b8c019c09a | -5.47072 | -48.99433 | 2026-09-19 04:57:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fffc094-6b99-3fb5-b5b6-7d1b51906a55 | -7.15545 | -47.51279 | 2026-09-19 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3541273-d56a-3d26-a835-33a422f44589 | -6.32713 | -55.28107 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ebf9e82-a6b7-3f2b-92d3-5b0c7ea0ce19 | -10.51142 | -51.32109 | 2026-09-19 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1695a69d-51c7-341f-b530-6d3ce2475506 | -4.56875 | -42.97601 | 2026-09-19 04:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8efa7b32-d17a-3318-aaf3-d801de4f1916 | -7.86515 | -45.13165 | 2026-09-19 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee03d0ef-4549-35b0-8dd3-d1a0a072687e | -4.5541 | -54.9301 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 949bab70-08ed-331c-bc7f-28d0e8c13c75 | -6.10091 | -57.68619 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39d3cf47-e8f3-371c-bb83-7ff05712df43 | -9.03362 | -48.73293 | 2026-09-19 04:57:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 15fce2dd-dac4-3fa4-a7b3-8ffe46a5e2bd | -6.99052 | -42.18587 | 2026-09-19 04:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 66361638-47fa-3583-810b-033532fda140 | -6.70378 | -59.46178 | 2026-09-19 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 19167147-435f-3aa8-a81a-eb6256eb9a88 | -11.05344 | -48.31358 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 018dfde1-48b7-3ef9-82e8-9074632eef7d | -9.9432 | -45.27916 | 2026-09-19 04:57:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8f3bfc6f-6b86-3e33-ac20-7288c5040972 | -5.97322 | -55.35868 | 2026-09-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 267f1330-2de4-3f82-b7bd-50696a81d68a | -9.7981 | -48.32646 | 2026-09-19 04:57:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54a2f017-54ba-3dcc-85b7-21603a431828 | -8.23154 | -45.60324 | 2026-09-19 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8e1a5706-a62b-3066-bbec-13dc65b6dbd5 | -5.86533 | -52.04888 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79852648-5215-3945-9b7b-ed6246a2a588 | -3.04042 | -51.37416 | 2026-09-19 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 685ed532-6074-382d-9bcc-9a8fd9537801 | -10.12456 | -45.56186 | 2026-09-19 04:57:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eb731af1-313d-3652-a515-6851e6d3c223 | -3.14714 | -53.93768 | 2026-09-19 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e75ccf6c-03a1-3252-bb70-25c64a7d9ff8 | -5.88193 | -52.05149 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71e84dee-6e49-3860-80cd-7609b108d407 | -9.15798 | -59.464 | 2026-09-19 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 800cd51d-25d4-3001-94ed-cdb10d728516 | -3.45593 | -50.61469 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 573daafc-5512-3b33-993a-c1f04146a09f | -3.81499 | -50.74316 | 2026-09-19 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0c91256-554a-3486-a664-121e8d9709fb | -4.59861 | -42.96221 | 2026-09-19 04:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecbdecaa-769c-332f-9c1e-ad940f4a3697 | -4.31992 | -60.88703 | 2026-09-19 04:57:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 70580287-f140-3e97-bb9b-b625e04bd024 | -9.58584 | -54.1859 | 2026-09-19 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 526f3fd0-ace9-3720-8768-84cde97e9562 | -5.88643 | -52.08784 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1926816e-991e-36de-877e-acade21dc976 | -5.75228 | -57.57758 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85886d2b-0511-38ae-8d13-280742c47317 | -4.82406 | -42.88424 | 2026-09-19 04:57:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f973cd73-8c08-302c-945e-1bbf7a79cfa3 | -6.703 | -59.46622 | 2026-09-19 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20752e09-4370-3004-9a80-307e87f9860a | -6.33412 | -55.28222 | 2026-09-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 98191e1a-7320-3e3c-afda-8e6f91644949 | -11.12229 | -45.30123 | 2026-09-19 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c41d007-ab7f-3938-85c3-48c14281ee02 | -5.87869 | -53.61441 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6809c67f-ef20-3fcd-b4cf-a0b3308e2d34 | -6.66145 | -50.93137 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65b5f37c-c466-3841-ae7f-188a7f548756 | -4.42187 | -55.52574 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57a9c3bb-49f4-3c44-9208-913f783f8dd8 | -8.77328 | -46.91808 | 2026-09-19 04:57:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b46c786b-2319-3917-8a39-7a2bdb2c2247 | -10.53277 | -46.74627 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 62097bf2-ca43-3657-92fa-2205b8d83870 | -10.91815 | -48.41729 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebf4f7a1-93fe-39bb-bf33-bfa1864f5ccc | -10.52947 | -44.849 | 2026-09-19 04:57:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efb864df-b9bd-3059-9a23-066c8b175fc1 | -7.77584 | -44.89743 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1270ac9-e54e-35cf-a3c5-24103ef08259 | -11.08095 | -48.29954 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 66adfdae-c28d-30fe-95e0-6ffe738f3f44 | -9.76191 | -46.07635 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c3e6321-0d02-3316-aec2-c607b3c9dc18 | -8.76643 | -48.67218 | 2026-09-19 04:57:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b3daeb19-05c3-3fd8-a37b-f2db3d20bf6a | -9.94881 | -46.54149 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README82.md)
