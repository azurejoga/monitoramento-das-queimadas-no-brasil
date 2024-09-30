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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5070b36-d439-3360-8ad3-3e907eb2dfdd | -18.52394 | -43.35835 | 2024-09-30 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| db7c6979-2b29-3aa0-b190-52d5243468b3 | -18.52335 | -43.36339 | 2024-09-30 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d83c2d40-f7f1-34a7-aaed-f876720d2c97 | -20.0794 | -44.6657 | 2024-09-30 04:34:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bf8e163-309c-33f9-9735-e7b36697246c | -20.07889 | -44.67002 | 2024-09-30 04:34:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 444d7b46-f6e7-3a8b-a64f-df942e8f45cb | -20.16323 | -44.02603 | 2024-09-30 04:34:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 406406a9-6a14-3680-98c2-f41e7ef7aab1 | -19.97153 | -43.95112 | 2024-09-30 04:34:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 93e4ada1-f847-3f81-aae5-2bc6ec0eda7b | -19.97102 | -43.95554 | 2024-09-30 04:34:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 25294977-4f8a-3628-9f41-883837b765fb | -19.97051 | -43.95988 | 2024-09-30 04:34:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| db873898-4fef-3c8c-9969-243f7535852c | -21.47121 | -44.67575 | 2024-09-30 04:34:00 | NOAA-20 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 71a05ca9-6abc-358b-b14a-533b95c30f6c | -21.46629 | -44.6799 | 2024-09-30 04:34:00 | NOAA-20 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6f08b760-305d-3aa9-aa53-6f8f7c1a629c | -23.08007 | -45.40815 | 2024-09-30 04:34:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3908682d-76e6-31e6-8827-c849c40159b9 | -23.07959 | -45.41217 | 2024-09-30 04:34:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 149ae329-24f9-3bdf-8724-b70c2eae841e | -23.07877 | -45.41097 | 2024-09-30 04:34:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| bd295f56-c5b6-3a49-ba72-ee302c884cb0 | -17.72109 | -53.1813 | 2024-09-30 04:34:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 399fe3a3-23e6-3078-8c3d-306679501dcc | -23.0753 | -45.41182 | 2024-09-30 04:34:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9156b689-6845-3201-a3e4-61eb118e0495 | -23.07448 | -45.41063 | 2024-09-30 04:34:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b0c76512-e1df-3c27-8099-9ac7572a5700 | -22.72556 | -44.8228 | 2024-09-30 04:34:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| b8640511-9aeb-300f-85c7-c2fef27caf64 | -22.72509 | -44.82539 | 2024-09-30 04:34:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| a2ee4389-241e-3731-a4f5-726ae0d90d5e | -22.72505 | -44.82712 | 2024-09-30 04:34:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7c6e43d0-f2db-3fe9-abd4-eb203548801f | -22.6764 | -45.51916 | 2024-09-30 04:34:00 | NOAA-20 | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 26bea38a-1975-39a5-8268-fc991ef1991c | -22.67593 | -45.52318 | 2024-09-30 04:34:00 | NOAA-20 | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3dbfeed9-5731-3ff3-9c69-de323c59cc8e | -22.67179 | -45.52205 | 2024-09-30 04:34:00 | NOAA-20 | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3123522b-677c-3d3d-a727-bf20f52ff4af | -15.88684 | -45.05738 | 2024-09-30 04:34:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e4e1342-5287-317b-aa45-e60606a0d68a | -15.88613 | -45.06263 | 2024-09-30 04:34:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c91400a-c783-3302-8858-13a392c8880b | -15.88359 | -45.05157 | 2024-09-30 04:34:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd6eb5a7-ed81-32a9-8960-f2833634bfd6 | -17.142 | -44.83939 | 2024-09-30 04:34:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36f7b203-57a3-3114-baba-87d805c7719f | -16.90433 | -45.32705 | 2024-09-30 04:34:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0ab21743-922d-3abf-b19c-f0e520c40355 | -16.90364 | -45.33225 | 2024-09-30 04:34:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9850910b-be67-309b-b79e-eb7a9c5fbe34 | -16.90107 | -45.32127 | 2024-09-30 04:34:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b8c255b-d423-3a8e-a3d0-ce4ab3e873ec | -16.89387 | -45.31488 | 2024-09-30 04:34:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 067ca057-8b98-36c7-af30-48fe775e84d9 | -19.44965 | -45.87421 | 2024-09-30 04:34:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 564cfe04-ca5f-3efe-9a96-ce0aa8227185 | -19.44173 | -45.87331 | 2024-09-30 04:34:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2915985f-b57a-3f4b-8b00-3d93aac7a2f3 | -19.44101 | -45.8788 | 2024-09-30 04:34:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| a9314cef-8aff-39f4-ba1c-955e06098be7 | -19.43776 | -45.8729 | 2024-09-30 04:34:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9c87972-139e-3ed6-a721-a7778521ee78 | -19.43638 | -45.88347 | 2024-09-30 04:34:00 | NOAA-20 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b35a91e7-d3af-3f7a-b294-612d6a3b7caf | -19.43571 | -45.88863 | 2024-09-30 04:34:00 | NOAA-20 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50b96ab4-eb6f-37b9-9e4f-0587d3d672ac | -19.4352 | -45.86171 | 2024-09-30 04:34:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2f4eb4c-e8d9-387a-aa32-377fdb21317e | -19.43312 | -45.8777 | 2024-09-30 04:34:00 | NOAA-20 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8316c7cc-b99d-3c78-9667-25f8d6c3a9df | -19.43124 | -45.86119 | 2024-09-30 04:34:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ab91b8bd-300f-339a-96a2-435fa7fef96e | -19.4285 | -45.88229 | 2024-09-30 04:34:00 | NOAA-20 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 837e9da0-c891-3d8e-be54-63f092a200a8 | -19.42389 | -45.88689 | 2024-09-30 04:34:00 | NOAA-20 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb682264-60c5-3853-ab8a-610a26b58656 | -18.97396 | -45.45668 | 2024-09-30 04:34:00 | NOAA-20 | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16b81c00-a9a2-3f97-9cbc-85cd6172c792 | -18.97349 | -45.46034 | 2024-09-30 04:34:00 | NOAA-20 | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 210d536c-2f6c-308e-afb4-2120cd92c3a3 | -18.96994 | -45.45615 | 2024-09-30 04:34:00 | NOAA-20 | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 40095183-7301-3eca-beb8-f8412daeee83 | -18.96946 | -45.45981 | 2024-09-30 04:34:00 | NOAA-20 | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d986ee80-bca3-3a14-86e2-239870dfe9b1 | -20.31862 | -46.63648 | 2024-09-30 04:34:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c058d29-567b-3f17-8760-1d01c501f6ce | -20.64869 | -46.28325 | 2024-09-30 04:34:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36fcbf1e-c469-31ae-83ea-27df9de19729 | -20.60266 | -46.23762 | 2024-09-30 04:34:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 654e20e4-fe1c-319b-bbf3-8463802d909a | -20.60185 | -46.2437 | 2024-09-30 04:34:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9276cb7d-8599-300a-9087-c5ee9faeb6cb | -20.59874 | -46.23707 | 2024-09-30 04:34:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| abb2abbd-2bb7-3c35-960d-e03090f079e5 | -20.59798 | -46.24283 | 2024-09-30 04:34:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3ffe5f7d-8944-3604-896b-6dfb0af7e847 | -20.5972 | -46.24873 | 2024-09-30 04:34:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55e63d48-d384-3e32-a26c-bea13267db5b | -20.59334 | -46.2478 | 2024-09-30 04:34:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a402b58-941a-35d5-83fb-a97cb92f61aa | -20.59254 | -46.25386 | 2024-09-30 04:34:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e06b2581-2eb5-3983-9ffd-4ed7904ff025 | -20.51045 | -46.30413 | 2024-09-30 04:34:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8952468c-b02b-37ab-8c0a-71e407a50eb3 | -20.28428 | -46.11074 | 2024-09-30 04:34:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37d876a9-7681-384c-a1dc-c9afb0b2c792 | -22.29376 | -46.82635 | 2024-09-30 04:34:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e96c1456-1089-311d-9183-590ae63a6e00 | -21.98364 | -46.81753 | 2024-09-30 04:34:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 10.5 |
| fda511cd-383d-35f3-ad3c-f58da9eceef1 | -21.97978 | -46.81695 | 2024-09-30 04:34:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 10.5 |
| aab33995-92e4-312a-97db-dd3fad213456 | -20.88477 | -46.69755 | 2024-09-30 04:34:00 | NOAA-20 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 74aeb577-781d-360c-a342-a83c1e8ae095 | -22.38378 | -45.80059 | 2024-09-30 04:34:00 | NOAA-20 | CONCEIÇÃO DOS OUROS | MINAS GERAIS | Brasil | 3117801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0d9c123e-9a27-339e-a898-09fa2fd86a58 | -22.20978 | -45.86742 | 2024-09-30 04:34:00 | NOAA-20 | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d555d4e7-bcf4-37b9-bba8-a089c6052d18 | -22.15581 | -46.00545 | 2024-09-30 04:34:00 | NOAA-20 | CONGONHAL | MINAS GERAIS | Brasil | 3117900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b29d417d-d312-31be-bf4d-969eb666792a | -21.92877 | -46.03923 | 2024-09-30 04:34:00 | NOAA-20 | ESPÍRITO SANTO DO DOURADO | MINAS GERAIS | Brasil | 3124401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 05506cc7-f858-3e1e-a141-a5a1eaaf9bac | -21.92832 | -46.04295 | 2024-09-30 04:34:00 | NOAA-20 | ESPÍRITO SANTO DO DOURADO | MINAS GERAIS | Brasil | 3124401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4b10e446-7566-3e81-ae01-0cb98eaa11c1 | -21.9278 | -46.04024 | 2024-09-30 04:34:00 | NOAA-20 | ESPÍRITO SANTO DO DOURADO | MINAS GERAIS | Brasil | 3124401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 763e570d-aec8-3593-83ca-15187059dfa8 | -21.92732 | -46.04397 | 2024-09-30 04:34:00 | NOAA-20 | ESPÍRITO SANTO DO DOURADO | MINAS GERAIS | Brasil | 3124401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 757fee40-6d03-3954-9f2a-3fb0a3076088 | -21.83933 | -45.485 | 2024-09-30 04:34:00 | NOAA-20 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f28f8a0a-daf0-35f5-a306-8c6345a37ba9 | -21.61652 | -45.58632 | 2024-09-30 04:34:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7c792b60-2559-3874-8dbf-e19e63da2e67 | -21.53094 | -45.87846 | 2024-09-30 04:34:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 10828205-273d-32b5-8b57-e4fb9f85c748 | -21.5269 | -45.87778 | 2024-09-30 04:34:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dd124a50-4fae-3eba-87a0-9ba1d1e5418c | -21.23052 | -45.93347 | 2024-09-30 04:34:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fc61b84f-0bc4-3648-a7e7-19243e6da5c0 | -21.09201 | -45.8532 | 2024-09-30 04:34:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 72b14afa-ce6d-32ea-aecc-d2862513d7c0 | -21.09124 | -45.85328 | 2024-09-30 04:34:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d1c3c91f-37e0-3dc9-b9cf-701ef8ef866a | -22.75154 | -47.074 | 2024-09-30 04:34:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41d7d475-56d0-35ac-977a-97f8620865a3 | -22.77002 | -46.80867 | 2024-09-30 04:34:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 800102f9-8a8a-35e5-93d6-2f13cf784de5 | -17.74251 | -47.22841 | 2024-09-30 04:34:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1764bd5-2b84-3aeb-9241-07af11b0d6d6 | -17.63536 | -46.66533 | 2024-09-30 04:34:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1bf4ec6d-f5e9-3597-9ef1-8c0b47fbb3c8 | -17.63473 | -46.66987 | 2024-09-30 04:34:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 38b8a6be-4172-315f-8f3a-5d54294e7856 | -17.59069 | -46.95545 | 2024-09-30 04:34:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c5b590b-115a-3356-86ac-3af1fb72cb71 | -16.91818 | -47.17091 | 2024-09-30 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78df3557-1cab-375b-bc67-368fc480d00e | -16.91757 | -47.17515 | 2024-09-30 04:34:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2118076d-31bc-3296-932c-0518dcefa718 | -19.00591 | -47.14843 | 2024-09-30 04:34:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90878ab7-a684-363b-ab85-d6590663f4c4 | -19.00225 | -47.1479 | 2024-09-30 04:34:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a461dfb3-ab6c-3c8f-aee2-570eee7dd543 | -19.74727 | -47.8899 | 2024-09-30 04:34:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6744809-eb39-34d0-92f7-5214b4c09f98 | -19.74669 | -47.88862 | 2024-09-30 04:34:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f847a22-9a5f-3bba-9dac-9816f58a55b6 | -19.74431 | -47.88514 | 2024-09-30 04:34:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd17b88d-210f-3b08-9b42-e60df5415fd0 | -19.74371 | -47.88937 | 2024-09-30 04:34:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcaf80e5-f561-3ab3-b5c7-d40af2f60884 | -19.74314 | -47.88809 | 2024-09-30 04:34:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd466c13-8e51-3fbb-9204-727b3aa7ac45 | -20.46981 | -47.00399 | 2024-09-30 04:34:00 | NOAA-20 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f775f3a-2285-3c5d-be94-070ca0d4a14a | -20.32502 | -46.64684 | 2024-09-30 04:34:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a25cd28c-7261-30cf-9372-716ccb9cb7dd | -20.3244 | -46.65149 | 2024-09-30 04:34:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b07c529b-c71a-34ce-89f6-ad7c72847cbf | -20.32379 | -46.65609 | 2024-09-30 04:34:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8953bcb0-18ef-37e7-8644-9dbfacefd468 | -20.31931 | -46.66052 | 2024-09-30 04:34:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 01b53bb9-879d-35ef-a81c-76f6a7a75efb | -20.31795 | -46.64149 | 2024-09-30 04:34:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b8f55746-c3e6-30c0-943a-9d130e0d7666 | -20.31729 | -46.64647 | 2024-09-30 04:34:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 45e64928-afb6-3ee2-9f2e-7743f0b60d07 | -20.31665 | -46.65131 | 2024-09-30 04:34:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 89faffe8-31e6-3584-9730-6b776f4615ea | -20.3154 | -46.66066 | 2024-09-30 04:34:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b158f907-8125-325a-8c53-dd210ac8a0d8 | -20.31479 | -46.66524 | 2024-09-30 04:34:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f40c00e4-d797-3536-a4e1-5d5fc0c3db47 | -20.31153 | -46.66059 | 2024-09-30 04:34:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README54.md)
