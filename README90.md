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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 002516d6-8882-352f-9b95-9a258ed76add | -11.5279 | -45.5162 | 2026-08-31 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 02544f57-a72b-3605-a4b7-d1fb074a68ab | -5.2362 | -55.9112 | 2026-08-31 14:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| e61a3e27-6df9-36ed-8584-a7e13668f17d | -11.2294 | -45.099 | 2026-08-31 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.1 |
| e5ac9200-d510-3fcf-849f-c0f6e9d184ce | -8.7628 | -46.4642 | 2026-08-31 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 153.0 |
| a909e3ff-76ce-3ec4-8b80-632a0a7db86a | -8.7631 | -46.4418 | 2026-08-31 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 202.2 |
| b86a80b1-7091-3844-8e1e-9c6241a8c5bc | -11.5283 | -45.4933 | 2026-08-31 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 308.7 |
| 42ad6ca7-079c-33cd-9af5-8baa1dce81d4 | -7.5843 | -61.3803 | 2026-08-31 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 5e09b8dc-8d2f-3432-8422-1907f08c5415 | -5.2548 | -55.8907 | 2026-08-31 14:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| ce1b4db3-f278-3f1a-afa4-f8bf22c18b98 | -18.2899 | -52.7035 | 2026-08-31 14:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 837174d5-7a97-3f7b-ba66-da2934e09538 | -9.7873 | -59.4479 | 2026-08-31 14:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| a33906bb-ef8b-36d5-acd8-8cea0e10a467 | -7.2933 | -60.5905 | 2026-08-31 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 1ef95b2e-ac75-3ef1-b907-17e637a71bf7 | -7.5659 | -61.362 | 2026-08-31 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 4f971689-6308-30cc-a176-49c30ed273e8 | -7.9236 | -44.2558 | 2026-08-31 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 5fd452c3-19a0-38db-97cf-7849077f7864 | -5.5831 | -60.2307 | 2026-08-31 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 151.1 |
| 75ef3d47-e45b-3bcf-80ba-d9e9bc364495 | -7.0222 | -45.8653 | 2026-08-31 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 40362317-cb73-339b-9414-e0d12be81481 | -6.6036 | -58.5972 | 2026-08-31 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 797.7 |
| 3486c726-2ea5-39bc-8851-04e4dfcf803d | -14.6899 | -54.912 | 2026-08-31 14:00:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 65f2660e-21f1-3721-9abb-817d7e48cbff | -13.9474 | -54.4179 | 2026-08-31 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 5a4efc88-c802-382c-aa2d-71ee4fd94a2f | -9.4342 | -45.6704 | 2026-08-31 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 140.4 |
| e2267fb5-3ff1-3213-bf98-3d14c7a6bf51 | -7.3119 | -60.5706 | 2026-08-31 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 137.9 |
| 3239e490-c565-3cf7-ad2c-9a24e48d9901 | -11.4828 | -58.5159 | 2026-08-31 14:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 316.8 |
| 4a3d8641-7d9a-3d25-9a54-f7c3bc5370ca | -3.6215 | -60.566 | 2026-08-31 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 5f1b1529-f411-37a2-9b17-8bb214e42c70 | -8.799 | -62.4905 | 2026-08-31 14:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 135.5 |
| d69fe9bd-f9ef-3300-a3b9-4abbc67a4c91 | -10.7409 | -54.0196 | 2026-08-31 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| d1255309-c884-3f78-b6e8-215da83e0b02 | -8.8174 | -62.5087 | 2026-08-31 14:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 0d215fae-8fdc-387a-988f-f127d97bf387 | -10.7598 | -54.0179 | 2026-08-31 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 3f697feb-e371-36ad-b0b9-42c6a35d6ef9 | -7.1126 | -42.749 | 2026-08-31 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 101.4 |
| 7ba2edc3-10cc-3471-b1f0-1430384abcc4 | -14.1459 | -52.7871 | 2026-08-31 14:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 581ea566-e1e9-32f2-9630-c7bdbb8eeacc | -8.8175 | -62.4898 | 2026-08-31 14:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 84202d3d-1efc-3df1-9f51-a1ad68b47847 | -18.2704 | -52.6851 | 2026-08-31 14:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 216.3 |
| 8e440f7f-d072-3457-ac23-64e0243cc3d1 | -13.967 | -54.395 | 2026-08-31 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 215e942c-b2e1-369e-b2ca-778b35dc6a58 | -8.7439 | -46.4661 | 2026-08-31 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 4ac5cdfd-ecf1-3355-86f8-f8ea0e8fe73c | -10.8209 | -50.6945 | 2026-08-31 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| fefe0bb7-a27b-3245-b8da-d5ae94a61a11 | -5.5943 | -42.3142 | 2026-08-31 14:00:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 69.9 |
| 06fa9dd6-e22e-34fd-933c-578f7904f258 | -8.7579 | -45.3823 | 2026-08-31 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 8a982f8b-bee2-30e4-bfea-474c330f4d60 | -7.9425 | -44.2538 | 2026-08-31 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 102.5 |
| bdc9a4e2-d2d6-312d-9300-eebfd84ceeb3 | -14.4394 | -52.5176 | 2026-08-31 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 96eda9ed-ad00-39d1-8d97-a8ddd93107df | -14.5868 | -54.1153 | 2026-08-31 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| a47591bf-d422-3cc0-9aee-400d099dac9f | -15.8844 | -56.4819 | 2026-08-31 14:00:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 78760659-0df3-308e-bc21-c4ed2cfcc0b3 | -9.5778 | -47.6003 | 2026-08-31 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 7cfac246-d0d1-39d1-9dd8-cc8e72814c73 | -10.9483 | -51.0634 | 2026-08-31 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 45b54e68-2e12-3083-8a76-9d6f41db7e68 | -13.4379 | -51.4348 | 2026-08-31 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 1da08c15-bf92-3e13-88d4-13fd32aa0d21 | -11.2482 | -45.1194 | 2026-08-31 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 191.9 |
| c983919c-d5ea-3c89-b3d2-02c7c3e5f73b | -15.346 | -53.7912 | 2026-08-31 14:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 9c52ad33-e13e-3b3a-ac16-8fd64fdf33a1 | -7.6149 | -44.8833 | 2026-08-31 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| ab2073de-41b1-3f7d-9dce-1111780c86f3 | -6.2471 | -53.6623 | 2026-08-31 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 35768cf9-d25b-31d4-8c86-312a102f7be4 | -5.8688 | -52.1487 | 2026-08-31 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 8da4f597-0bc0-310b-be01-01ba4ac96bb9 | -7.9794 | -44.3193 | 2026-08-31 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 409.7 |
| 4f1e5513-9ea9-3d43-bffc-0beac4ad482f | -13.9667 | -54.4157 | 2026-08-31 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 98a64df3-6a4f-3c4a-9229-3d5376eafdb0 | -11.5475 | -45.4906 | 2026-08-31 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 82a460b6-a487-3cd3-8b0e-048beabbc765 | -11.9378 | -45.0656 | 2026-08-31 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 318.2 |
| 74c11a8d-c9a8-33f6-a545-a0b39f7c1874 | -7.6253 | -55.2787 | 2026-08-31 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 74625f92-3db5-38e4-9591-2be909741a5c | -10.7596 | -54.0384 | 2026-08-31 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 143.5 |
| 50961dff-b770-30bd-9692-b3abf15373a1 | -10.8212 | -50.6732 | 2026-08-31 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| bfd0ab83-b7c4-3b0e-a3f9-5eb22e68d0cb | -11.229 | -45.1221 | 2026-08-31 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 45f8d6b7-7007-363f-b9d8-fe21351f7e68 | -11.0747 | -51.5153 | 2026-08-31 14:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 1102c2b1-c7ef-3d18-b810-e07d91b3ab6a | -10.1538 | -45.6982 | 2026-08-31 14:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 168.4 |
| 463e6677-6684-39bf-a87b-83081553ce3d | -10.7407 | -54.0401 | 2026-08-31 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 178.4 |
| 0c7a6483-6272-3f8b-8eb2-a433faa04d0c | -15.8041 | -51.0627 | 2026-08-31 14:00:00 | GOES-19 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 12cc85e5-6ca7-3548-83de-65c3a1808e79 | -9.5964 | -47.6204 | 2026-08-31 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 239.3 |
| 854c8ba1-4679-3619-be76-5e861efdabf8 | -7.3118 | -60.5897 | 2026-08-31 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 5b97becf-1936-376a-b0f0-7581aef54d4e | -7.2934 | -60.5713 | 2026-08-31 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 0f684ff7-c86c-336e-b318-195e4afabfeb | -10.8046 | -50.5046 | 2026-08-31 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 0341ec91-d752-34c9-bcfa-4ae0a30ed1a5 | -7.9907 | -46.5177 | 2026-08-31 14:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 30fb9710-8cda-35ec-962f-a0d53e685e69 | -8.7989 | -62.5095 | 2026-08-31 14:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 119.5 |
| a93d4252-7fd9-3eae-a951-f9581e945087 | -11.7973 | -47.6672 | 2026-08-31 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 13f0d8af-e16f-3a37-93c0-1888de4cc141 | -7.9605 | -44.3212 | 2026-08-31 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 151.6 |
| d5e37ec9-6d3d-3737-8469-9f72220ca374 | -5.3014 | -43.6722 | 2026-08-31 14:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 09b3cacb-e7fc-3cd5-a308-a4e7cd173097 | -8.1672 | -54.9246 | 2026-08-31 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| d90faebf-416f-35e7-84d1-dad951d45d55 | -5.9635 | -57.6899 | 2026-08-31 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 5f4ce2a7-90b3-3f8a-8b6a-d4098fd8e390 | -14.4201 | -52.5201 | 2026-08-31 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 251.9 |
| 73aecd57-9b8b-31fe-8a76-ebaabfd23d24 | -15.6786 | -45.9332 | 2026-08-31 14:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 13452e75-d968-3f0d-9e91-b34d4f955101 | -6.4083 | -45.4424 | 2026-08-31 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| f7b649cd-29ff-322b-8d24-c13c0b2009a1 | -7.5658 | -61.3811 | 2026-08-31 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 5c435130-2e19-32ab-b92d-17311973655a | -12.9032 | -45.8382 | 2026-08-31 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| a9f7587c-a30a-3ad8-a529-d4fa94046ab5 | -7.5845 | -61.3423 | 2026-08-31 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 823fb185-8418-3471-818e-b09e14567d1a | -9.7875 | -59.4285 | 2026-08-31 14:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| fc63abe4-be36-30a6-be46-a9a42771c952 | -8.7442 | -46.4437 | 2026-08-31 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 571a28a9-4a81-31d0-a684-1ae948b5513d | -6.9176 | -55.7166 | 2026-08-31 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 53a4630d-2d46-37ed-a7c4-c5f3158aafb3 | -8.1671 | -54.9447 | 2026-08-31 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 7e14610e-599d-39d7-a0ac-f3685772cbe8 | -11.5479 | -45.4676 | 2026-08-31 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 551c1455-38d9-320a-ae95-34da139c1ad6 | -12.9056 | -59.8661 | 2026-08-31 14:10:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| da8ed919-9c3d-3f86-a607-410b706b476b | -18.27 | -52.7068 | 2026-08-31 14:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 82aa8b7d-fd01-321b-bba5-6fdc59d3bc71 | -14.2792 | -52.8758 | 2026-08-31 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 88ecd700-4b6b-3974-a4a4-33de6d242a15 | -9.5964 | -47.6204 | 2026-08-31 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 226.0 |
| 6597938d-2e1a-3e34-9c2e-f9a3bf0cae5a | -10.3394 | -49.9547 | 2026-08-31 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 486e40fd-4baf-3d08-9fc8-34da53b33e85 | -5.2548 | -55.8907 | 2026-08-31 14:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 92e1ef4b-53d5-39b2-86b3-82d9e033e477 | -6.1109 | -57.684 | 2026-08-31 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 0083c678-4b6e-38e6-b4b0-c0b2c774cf62 | -11.5283 | -45.4933 | 2026-08-31 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 0cb57116-3d8e-3428-b19b-235fee5af55a | -8.87 | -66.8935 | 2026-08-31 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 03823054-e0f3-3d25-a42b-b5227c378b97 | -13.9474 | -54.4179 | 2026-08-31 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 93de9313-37a9-3d58-b7ca-631e4129a812 | -8.799 | -62.4905 | 2026-08-31 14:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 891be23a-178c-399e-8a41-3458da1ae3f5 | -7.2934 | -60.5713 | 2026-08-31 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| e90036d5-b52a-3d9a-b53c-24cea5cce822 | -8.7989 | -62.5095 | 2026-08-31 14:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 90dd709d-88fe-3516-8e84-d7eb68de9c6f | -9.1906 | -51.546 | 2026-08-31 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 7f3311b9-248e-3c45-baf5-ee083836610a | -7.5844 | -61.3613 | 2026-08-31 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 7f5dbc63-e166-321f-ad4e-1d82d70df395 | -5.2362 | -55.9112 | 2026-08-31 14:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| e32dcfa4-bc81-3cea-8822-4506c8f82075 | -14.1459 | -52.7871 | 2026-08-31 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 5fadbbfd-f846-3707-b87b-b48a7365081e | -12.9032 | -45.8382 | 2026-08-31 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| f9318290-ea91-344f-ac9f-e3df9eec70be | -8.7579 | -45.3823 | 2026-08-31 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 122.6 |


[Clique aqui para ver as próximas entradas](README91.md)
