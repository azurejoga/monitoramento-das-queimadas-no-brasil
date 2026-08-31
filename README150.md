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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82661731-9900-326f-b194-5725e6e63dad | -8.1715 | -54.9281 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 97d009b0-929f-36cc-af24-a2ab196e63d9 | -10.68983 | -48.42033 | 2026-08-31 16:50:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 98e3f59f-227b-3faa-938f-fb35417a3141 | -10.75572 | -44.86028 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6fd83762-46fd-378f-bd00-c4547c29fb1f | -11.91716 | -45.07804 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| f6db48af-b4bf-333f-bb44-b40e33dae360 | -11.49228 | -60.58152 | 2026-08-31 16:50:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7cd90c52-6920-3fa6-96bc-6ffe328e5dd9 | -10.3998 | -45.08619 | 2026-08-31 16:50:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9350cfb1-b320-3db1-a89c-912d2d040655 | -11.5259 | -46.94873 | 2026-08-31 16:50:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0bd87d4b-5b7b-30c0-bd11-766492ebaf82 | -12.17241 | -50.53328 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4fbd6806-e7c2-3eb2-9325-6e11e9d5ab74 | -10.22957 | -46.67831 | 2026-08-31 16:50:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b83ceca4-5b2d-33e4-87c3-eb2a90dc5b37 | -7.04043 | -45.41668 | 2026-08-31 16:50:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e712fc5a-4e32-3a57-989b-4c10eeac1d66 | -12.08235 | -47.14515 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 45308f0b-c092-38b5-a01a-64bff178aaf0 | -7.55726 | -60.47654 | 2026-08-31 16:50:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 170.2 |
| de3037ef-5101-34e6-9c25-386ada9f0153 | -11.17452 | -45.59201 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4054489e-c7d4-3b16-8642-0d2bd8c7c9ee | -8.44479 | -46.89704 | 2026-08-31 16:50:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0662921b-7ed2-33e5-92ee-1c2ce94d46cc | -5.65649 | -43.55617 | 2026-08-31 16:50:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 538c7cd8-3605-31d5-94ed-85015648e0f9 | -7.99386 | -44.34288 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 99012e98-22a9-33b2-b44e-4be67b6c5fc0 | -6.34367 | -44.09104 | 2026-08-31 16:50:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cd54b6e0-ac41-3303-ae5d-71758285acfc | -9.65509 | -48.2655 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34485bb1-8c12-31e8-bb95-8be3be62be1d | -9.65425 | -46.05445 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 7a7a031c-7e9b-3ce8-8687-a82c31dc5f59 | -8.362 | -47.64772 | 2026-08-31 16:50:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ac205a8-3b3d-3447-b0fb-3c8af148bf3e | -11.19111 | -46.11058 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 8dc0d5c4-3ce8-3823-985c-b6bec6e75c88 | -11.25312 | -45.36055 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 2cfaeb24-3b7e-34d6-b802-49561d310b87 | -9.67566 | -46.5455 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1081ffa0-4dc3-30e9-8ebb-6b7f1fdb7036 | -7.92792 | -44.23916 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 5d13dd6d-bba0-32fa-82d3-3e27c4e7b8b6 | -7.79557 | -44.0681 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| c4d0a5bc-3c5e-3b47-a719-97139a9bd0ae | -14.12691 | -52.80989 | 2026-08-31 16:50:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1be6021a-9d01-306d-9072-6e8ac9f172dd | -12.92224 | -45.84229 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e6663d51-9098-3e05-9b22-0aff9f92f962 | -11.25435 | -45.09747 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 453bdb5c-caf7-3213-91de-d78bd558b91c | -6.3898 | -44.93682 | 2026-08-31 16:50:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2e01e0f5-276e-340c-a986-f546850dc335 | -12.96956 | -45.94184 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| bade2a8b-4a0b-34bc-aced-7fdc55eec0a8 | -7.06044 | -42.21854 | 2026-08-31 16:50:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| ec92d286-e3cc-3d7f-bf90-39aa1da03267 | -8.23691 | -54.94385 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7d05a479-56f8-3cb6-a35f-3ccab33e4789 | -10.15725 | -45.70588 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| fff29b52-5cbc-3644-b08a-e1097a54b001 | -9.18706 | -51.54764 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 78e57e39-b5e1-3cf4-95cb-4f30739d805b | -7.05501 | -52.71977 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| af4a046d-2c22-3e50-8fbd-101cd8bec9f4 | -10.66188 | -46.26656 | 2026-08-31 16:50:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 86b83ac4-e293-3491-81a8-5eb1c51b12ed | -11.37632 | -45.20393 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 02b09719-7cf2-3602-90c8-26e6c66a0974 | -12.95301 | -45.92543 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 17ab650c-2b30-3b6b-b3f1-452b09f657ce | -4.14761 | -38.57912 | 2026-08-31 16:50:00 | NOAA-20 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 8aac8f8e-1002-35f1-b991-8aeccdead557 | -8.12626 | -45.57928 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 62a115c0-d916-37f0-9179-12410e8242d1 | -11.54463 | -45.48001 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5e6cecc0-9dfc-390a-b836-13c8160008c5 | -8.16393 | -54.93004 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d809d53c-1ecd-3168-b4ab-2627fbc03bec | -8.12794 | -45.4975 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 552915ba-78f0-38e4-9bbc-a8b16dfa5344 | -11.18444 | -55.0952 | 2026-08-31 16:50:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| bf3d046a-45bc-3b4b-bfd4-5d1c51426623 | -5.80155 | -43.6449 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 3177f6aa-1c73-34dc-85b7-ab1ed474fd3a | -11.25027 | -45.14024 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 75cc295e-b066-3487-8a60-23045b71a5c8 | -6.9405 | -55.64644 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1df73ecd-54df-3424-8c77-1245978cca8a | -8.81605 | -62.49857 | 2026-08-31 16:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 132542cd-808b-357c-9ce6-b20ee549c0f8 | -11.91477 | -44.84168 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 32bea7f3-4cd8-33fe-8c2e-3488e32a5399 | -11.68657 | -54.53936 | 2026-08-31 16:50:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 1a248542-36dc-3b6f-b830-c50b38778590 | -10.15568 | -45.70154 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 16fd99cd-a36c-3fd6-b9ec-3a1c23107405 | -10.0025 | -46.3969 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6c6eff2d-91ff-36b3-9fba-173c15594968 | -9.65775 | -48.28294 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a98fd3b8-a06e-3170-8a39-4b4a8dc94d23 | -11.71304 | -47.63309 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b72e11dc-169e-3904-b480-a95dc2484496 | -6.38518 | -45.51081 | 2026-08-31 16:50:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1a41b13e-a99a-3f4d-9ce3-1bd951455db7 | -11.2214 | -45.36543 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1c321584-af66-3b95-acd0-ba2c874ee43c | -13.83452 | -54.01501 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 06ded231-2e3f-3cfd-ad26-c9c3f01d2376 | -7.16798 | -44.68647 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ce4a85b4-f72e-3336-94a7-10bf498ca237 | -8.00339 | -44.28057 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 35.9 |
| f5642a00-43ae-3f59-a076-de8586c8c163 | -10.02194 | -45.56651 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 73e5812d-6266-390a-84dc-49f196e2fc36 | -7.90728 | -44.28399 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 5e712158-ae40-37af-bde4-52018fdc94ff | -6.85774 | -41.65569 | 2026-08-31 16:50:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| db280cd9-0aed-3a45-9d97-7337593d6c13 | -12.97295 | -45.94129 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b5c14053-6ed8-38a8-a59f-cc132ca464da | -7.63844 | -46.71854 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e9d830b8-b5f1-3d0f-be4b-5764fdb9cd59 | -10.82794 | -50.69319 | 2026-08-31 16:50:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 134c3d25-8e3e-3be9-99a7-970dabadcb59 | -12.27848 | -41.58632 | 2026-08-31 16:50:00 | NOAA-20 | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 5173ae6b-362e-3fbd-8c7b-200c8288bea6 | -7.69013 | -55.33687 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 079574a5-d057-39ae-9022-27857a71a46d | -9.60162 | -47.60992 | 2026-08-31 16:50:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a5219eec-ef2c-3334-a390-a07e321c6ccf | -10.92217 | -50.61942 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| ac5e3fae-a361-3303-a078-5b8429cb9866 | -6.62306 | -53.17402 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d55c7057-e969-315c-8b07-eb0bb5a339d4 | -10.15442 | -45.76147 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 1d3cdf21-f0d1-3b16-a13a-f6a6e7449380 | -7.06418 | -42.21313 | 2026-08-31 16:50:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 7c5949fe-1ec4-35f1-b654-e7ca77728ba8 | -9.16904 | -40.27713 | 2026-08-31 16:50:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 09cc9202-2967-3afe-832d-3ec3437f0859 | -9.16581 | -59.37208 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 0c4d0cef-0c32-3b5e-a612-d2cb816fd195 | -8.4129 | -44.98412 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 0d81d6a5-a428-3aee-9b36-7d4a53f850cc | -7.22507 | -42.77142 | 2026-08-31 16:50:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 2e986486-0feb-35f3-a1d6-580663986336 | -9.66658 | -47.94156 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bea5e711-10ff-3db5-ab85-f1eb26ebf1d7 | -10.99149 | -49.69636 | 2026-08-31 16:50:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44a51ac3-2e75-3020-9b77-ea3c73e28735 | -9.15787 | -59.38037 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5f73f021-0b85-3ba3-a1cc-c9184dbe7bbf | -8.82983 | -47.9519 | 2026-08-31 16:50:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b3d4e886-29b5-329b-a12e-2f7145bb24d1 | -6.80251 | -43.5619 | 2026-08-31 16:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d87865ed-2fc4-34f1-baef-528bc0f11c3a | -10.47162 | -46.54883 | 2026-08-31 16:50:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| ccb152bf-7208-3f7c-895b-c415cefa3715 | -13.96785 | -54.39715 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 17b368b8-090a-37dc-bea5-b33da57caa10 | -11.23893 | -45.13784 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b63f204e-d1a0-3cc8-919a-5fa37b56c66b | -10.84838 | -45.34381 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 4e5f199c-44e0-329e-b8ac-5c97c3450c39 | -9.47454 | -57.01597 | 2026-08-31 16:50:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b478937f-ba3b-3740-b34b-8ad1fa6da1ee | -13.46409 | -57.03661 | 2026-08-31 16:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 0871dc73-0b1f-3d3c-a320-ebe1c252a482 | -10.84579 | -45.32764 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0e1f561b-4280-3d9d-9cb0-8575c9e4eabc | -7.63836 | -44.84145 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1e2c82e5-2c6b-3f13-bc14-6fc7cc64b7bd | -6.9527 | -55.70008 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c8d8e88e-33c4-3593-95b6-7bc64557f58e | -10.83661 | -45.99723 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| d285f752-38c4-3279-aeb4-4c165472d15d | -7.04942 | -45.40184 | 2026-08-31 16:50:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| ef710fd6-254f-300d-8264-ab5fe1ed7da1 | -11.91996 | -50.81437 | 2026-08-31 16:50:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cdfe82e8-f013-3085-b75b-287966fc74f8 | -13.44318 | -51.75933 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9e31b80a-6a42-3cc4-a9b9-9a29469d1393 | -8.08858 | -45.46106 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3a8ccd76-5254-300a-b96f-4036179c829e | -11.62099 | -50.18288 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e18e1a2f-277b-322c-910e-3d1fc13ed054 | -11.15707 | -54.00192 | 2026-08-31 16:50:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 96505dbb-d59c-3526-9947-b1b886f1f8e2 | -7.54973 | -60.46755 | 2026-08-31 16:50:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 57d18f62-d856-3b96-a478-1f7b47152742 | -6.85854 | -41.66045 | 2026-08-31 16:50:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 63a8c7b8-5195-3785-988f-1415fb1c84ed | -11.64777 | -46.75544 | 2026-08-31 16:50:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |


[Clique aqui para ver as próximas entradas](README151.md)
