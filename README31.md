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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22489ff0-c259-3134-92ca-901e75a70071 | -23.13736 | -49.64657 | 2025-09-19 04:51:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8e5a37ff-169b-370e-b051-34bc3b7b86cf | -23.60405 | -51.04698 | 2025-09-19 04:51:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| f2ea6a21-ff90-3398-af24-cb644efb5f27 | -20.15479 | -41.47797 | 2025-09-19 04:51:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 110b571b-ae0e-3490-bad8-dfd70fd8a1e6 | -19.96704 | -42.11206 | 2025-09-19 04:51:00 | NOAA-21 | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 880b20f7-44d8-357e-90ee-57546bebe16d | -19.58063 | -57.8247 | 2025-09-19 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 321efb95-ad3a-3153-a0e7-f16b30faaa55 | -21.28902 | -54.81406 | 2025-09-19 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 161b918d-d11d-3a09-9674-3a5266b8eff7 | -22.35247 | -46.74525 | 2025-09-19 04:51:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 36035db3-4396-3f74-8264-679ce4b9482d | -21.28197 | -48.79551 | 2025-09-19 04:51:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 640406f1-d135-3129-abf4-1552bdc35564 | -20.54546 | -44.02691 | 2025-09-19 04:51:00 | NOAA-21 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c3651a54-69cd-3123-a24a-3396a9d8b73c | -22.33559 | -46.76622 | 2025-09-19 04:51:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7ae3038-dd00-3e40-aa2a-4ef9d58be2d9 | -19.96473 | -42.11239 | 2025-09-19 04:51:00 | NOAA-21 | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 7c20a44c-41e4-3307-98c2-bbdcc12e541f | -21.11901 | -45.72171 | 2025-09-19 04:51:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| d018c48a-189d-383e-9893-c90f8a765645 | -21.28572 | -54.81347 | 2025-09-19 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8f4c648-e58c-318a-bc8c-67f39df5f0af | -24.15371 | -53.05526 | 2025-09-19 04:51:00 | NOAA-21 | GOIOERÊ | PARANÁ | Brasil | 4108601 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| bba26c19-2267-3d47-8444-142ab3f7bd8b | -22.93628 | -46.96062 | 2025-09-19 04:51:00 | NOAA-21 | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9bb90087-b444-30c2-9e71-4944e03b42b3 | -19.96507 | -42.10841 | 2025-09-19 04:51:00 | NOAA-21 | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| b389452e-5bc4-335b-87f8-472d40de0e93 | -22.93955 | -47.29039 | 2025-09-19 04:51:00 | NOAA-21 | MONTE MOR | SÃO PAULO | Brasil | 3531803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2e9b476d-89f8-36a7-bb16-f12886a93ccc | -21.28244 | -48.79144 | 2025-09-19 04:51:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 02eb88d6-379e-3123-95c0-7cfe86c87003 | -22.98977 | -49.07089 | 2025-09-19 04:51:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76918aec-0a6a-363f-828b-d29259f98ae7 | -20.34487 | -48.78668 | 2025-09-19 04:51:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| adcebe5d-7aca-3271-a3ec-64c9d43ac0de | -25.68648 | -49.90268 | 2025-09-19 04:51:00 | NOAA-21 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a2b18f8f-fd89-3ee0-91c0-b0b92d90ac1b | -22.70172 | -46.2751 | 2025-09-19 04:51:00 | NOAA-21 | ITAPEVA | MINAS GERAIS | Brasil | 3133600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 4e712557-d1d1-303d-95b2-66525db410d1 | -23.65488 | -50.82764 | 2025-09-19 04:51:00 | NOAA-21 | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| faafad4c-3650-39b3-8506-9cb78d20e912 | -21.28423 | -48.79762 | 2025-09-19 04:51:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| bfeee3df-c488-3a1f-8731-3cc385d428b7 | -21.28473 | -48.79353 | 2025-09-19 04:51:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c560a6cc-932a-3df4-8f22-7532882cc3bf | -23.38798 | -47.14678 | 2025-09-19 04:51:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 034b0ba3-4e76-3593-84c5-d28eaaa8c2d5 | -20.20953 | -44.60977 | 2025-09-19 04:51:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1d3ad72a-21ec-3eef-aab7-ebe86de03b54 | -23.08038 | -55.14839 | 2025-09-19 04:51:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 22e7a90e-7b65-3031-9b9b-0c87332f4a85 | -20.50236 | -56.87103 | 2025-09-19 04:51:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c8a4dce3-6edc-388c-ab1f-38afb3650bd5 | -21.29291 | -54.81097 | 2025-09-19 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7e50eea-97f1-3ea5-9ca0-34ba3daca158 | -20.74568 | -56.94512 | 2025-09-19 04:51:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78f7a672-07bf-3e29-bbc3-374046547bf0 | -20.2099 | -44.60619 | 2025-09-19 04:51:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 30d9f8bf-2018-3201-8587-e5e3f6dcf540 | -20.34439 | -48.79058 | 2025-09-19 04:51:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c51a8a1d-ef46-3e3a-83e3-12b066188167 | -20.79087 | -47.23632 | 2025-09-19 04:51:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b65f3b27-c353-311b-8c84-c8a1da3d4b02 | -19.07453 | -48.35701 | 2025-09-19 04:51:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58f32272-719b-31f5-b8e4-8117a6affe81 | -20.54581 | -44.0232 | 2025-09-19 04:51:00 | NOAA-21 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0b2c69e5-e2e8-3adc-9a49-fb88bd7c3342 | -20.16087 | -41.48408 | 2025-09-19 04:51:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 59e35339-99fc-3a85-9feb-1f1fac5f914e | -22.34579 | -46.76206 | 2025-09-19 04:51:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d3011983-a488-3323-8f56-1dedae40ee58 | -23.14138 | -49.6474 | 2025-09-19 04:51:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8080feb6-26f6-3bce-9ccc-c30d82e00c45 | -23.59634 | -49.78396 | 2025-09-19 04:51:00 | NOAA-21 | SIQUEIRA CAMPOS | PARANÁ | Brasil | 4126603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 31243d86-686f-3a5c-bd4e-72eac7bd5358 | -20.54022 | -44.02225 | 2025-09-19 04:51:00 | NOAA-21 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e2bf5fe5-c610-317c-8961-99c24adf1c81 | -22.23977 | -55.97429 | 2025-09-19 04:51:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e78a88d-6de2-3d1e-8947-32ae39a1c007 | -20.74914 | -56.9458 | 2025-09-19 04:51:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a89b7b3c-c607-32e1-92e5-7f3d764cc581 | -19.58871 | -57.82162 | 2025-09-19 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c008bdef-52e3-3459-9e68-7a3754b4ba69 | -22.75072 | -51.39938 | 2025-09-19 04:51:00 | NOAA-21 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 789bc9af-327c-3207-8da4-95c1f8bde010 | -22.33106 | -54.4111 | 2025-09-19 04:51:00 | NOAA-21 | FÁTIMA DO SUL | MATO GROSSO DO SUL | Brasil | 5003801 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5f579fc6-c799-3447-9648-c4e20658f51e | -25.69103 | -49.89941 | 2025-09-19 04:51:00 | NOAA-21 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| a5dea4d3-fd6e-3554-be8d-e1142a523950 | -20.51719 | -42.39563 | 2025-09-19 04:51:00 | NOAA-21 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 4110a1e1-9ada-3bd2-bbd2-cd605616ccc2 | -22.14595 | -51.1836 | 2025-09-19 04:51:00 | NOAA-21 | MARTINÓPOLIS | SÃO PAULO | Brasil | 3529203 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1ab2bc5-f4b4-3759-82de-4810316d29ba | -25.68693 | -49.8987 | 2025-09-19 04:51:00 | NOAA-21 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 84d8cb4d-b426-36fa-ae9d-54949bd4ce65 | -21.28839 | -48.79811 | 2025-09-19 04:51:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4d47ed2d-d74b-3070-a737-989028f75d9b | -22.34098 | -46.76141 | 2025-09-19 04:51:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 401a0a44-4ddc-3845-ab11-3e2bbce44a25 | -23.2379 | -47.62371 | 2025-09-19 04:51:00 | NOAA-21 | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 260e6052-552e-319d-94e5-64e0bb79c39e | -28.68552 | -50.62868 | 2025-09-19 04:53:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 95eb3643-859c-3fd0-b5f1-b9ee66822ef3 | 1.95239 | -50.96603 | 2025-09-19 05:10:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17fa3c58-445b-37e1-8b3c-3509b713eb44 | 1.95294 | -50.96792 | 2025-09-19 05:10:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0eda342a-31e7-3667-b9ab-cbc59f97ebd0 | 2.41239 | -60.69926 | 2025-09-19 05:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da92c755-6bff-302c-9555-c64a3f8f298d | -2.73612 | -49.40511 | 2025-09-19 05:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 829a7064-6dcb-3e33-9d86-271452c153ab | -3.28204 | -49.1507 | 2025-09-19 05:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37577d58-a436-31b3-9789-b38117b75fa5 | -4.66649 | -49.3312 | 2025-09-19 05:12:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0a7b022-b6e0-323f-8d65-a12dd9ca866b | -3.32028 | -54.92192 | 2025-09-19 05:12:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c3204b7-ddcb-39a3-8b71-5444a77da139 | -6.2595 | -43.90935 | 2025-09-19 05:12:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 44e27e74-13bc-386f-9f0e-93089bfbd3ff | -5.70873 | -49.09677 | 2025-09-19 05:12:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b92afd69-6deb-36cc-95b5-a468d00bde2b | -6.26472 | -43.92342 | 2025-09-19 05:12:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| fcea8979-a613-388e-b085-2699aa70da60 | -3.59405 | -53.47437 | 2025-09-19 05:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 23eb9dee-d99e-3e23-b759-7b6b243ef82d | -5.044 | -47.90386 | 2025-09-19 05:12:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6d961d96-e2bd-32f5-afb7-f2395007e329 | -2.26771 | -47.8882 | 2025-09-19 05:12:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e4b2ee0-96e0-3b3f-b4f1-3dfe3ffef57f | -5.7287 | -43.63746 | 2025-09-19 05:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d43091f-f17b-346e-8e6c-5f2c538b32a7 | -3.32371 | -54.92244 | 2025-09-19 05:12:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 007a08b5-fb2c-30fb-85bd-9bc610a78d57 | -1.77721 | -55.50487 | 2025-09-19 05:12:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 029760a5-7fb5-3643-929c-5dd65d3a2e8a | -2.42619 | -49.32786 | 2025-09-19 05:12:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e9ea99f-029e-37b6-90dc-540bf1a70904 | -3.7008 | -49.57372 | 2025-09-19 05:12:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e1c354f-798d-382a-aa50-4fc3896b3eba | -6.2604 | -43.90284 | 2025-09-19 05:12:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0c6d2d84-cfb8-364c-858e-892998ab869b | -6.25861 | -43.91582 | 2025-09-19 05:12:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 0f638980-a59a-3807-8c5e-025f3bdada1b | -5.46745 | -46.68477 | 2025-09-19 05:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e266b43b-8a7f-3c8a-b0c5-d7b15212bd56 | -3.92693 | -56.03603 | 2025-09-19 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 416c7443-9c1d-354e-b54e-86035325dbdb | -3.56242 | -55.53549 | 2025-09-19 05:12:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06bbd8d5-32a2-36b4-a9a3-1b9b5cb9079c | -2.9385 | -49.45545 | 2025-09-19 05:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fb3d8f6-b21b-39c1-9435-2019fbb51134 | -5.46912 | -46.68757 | 2025-09-19 05:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56d15fe1-13aa-36f8-b5aa-18ad82fb41d3 | -2.26352 | -47.84671 | 2025-09-19 05:12:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e89649c-21a3-39e9-9949-c24140d5fb96 | -2.94602 | -49.34058 | 2025-09-19 05:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0ef7fdd9-4b31-3fee-a9a7-2cb47e13a59e | -2.264 | -47.84358 | 2025-09-19 05:12:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7347cb53-f9b6-3528-8e52-b96ca3d94f7a | -5.77707 | -45.97253 | 2025-09-19 05:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45a03dc9-aeec-326d-a977-884cdacc3d40 | -3.28283 | -49.14556 | 2025-09-19 05:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2853a744-fc58-3db2-8f6b-4fc8f6f6f685 | -4.25562 | -49.3123 | 2025-09-19 05:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f6d1885-4298-3cce-a792-99d47cf1b888 | -5.08335 | -47.51857 | 2025-09-19 05:12:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7bd2c60-b2e0-36c2-b668-a0641a5fe94c | -5.63794 | -45.9488 | 2025-09-19 05:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2a1953f-72e9-3902-80ba-90178f61e98d | -6.26206 | -43.92187 | 2025-09-19 05:12:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 81c368e6-9bad-395c-97ab-45517b68b43a | -4.2593 | -54.84595 | 2025-09-19 05:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d09a2fb2-2eda-3e87-9754-eeac59bec72a | -4.93996 | -49.92732 | 2025-09-19 05:12:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7be4b6f-d4d9-3d90-b8f1-4522d79ee9b3 | -4.47747 | -54.85563 | 2025-09-19 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51d468bc-9ccb-343c-8537-baf19a0871af | -2.89453 | -52.87031 | 2025-09-19 05:12:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be1301ef-4d09-3d61-8cb9-100bd29f6f97 | -5.63244 | -45.94321 | 2025-09-19 05:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b90796ae-a4ea-3e6f-999d-97a980db0e41 | -2.94526 | -49.34565 | 2025-09-19 05:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| be9e7ba6-07f3-32c6-9898-97f1bda130f6 | -5.04347 | -47.90746 | 2025-09-19 05:12:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 771aef90-9b4f-3da1-917d-00c183be559f | -6.26649 | -43.91063 | 2025-09-19 05:12:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| c78b9330-7ca2-3b41-b716-617b7078a6c4 | -6.26991 | -43.91659 | 2025-09-19 05:12:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a32e1e91-5815-34fd-bddb-5b35569434da | -5.12836 | -47.82682 | 2025-09-19 05:12:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a2e6636c-29f5-356b-8130-934ef247d9c3 | -5.12788 | -47.83014 | 2025-09-19 05:12:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 439e0180-8fac-31b0-b254-36309dd61567 | -5.13328 | -47.83106 | 2025-09-19 05:12:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README32.md)
