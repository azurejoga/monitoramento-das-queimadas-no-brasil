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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e010141-c3e5-3bed-9798-4f874fa2b630 | -6.18278 | -41.20447 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 20b18438-3fd3-341b-85cc-76e241bedf1b | -3.71373 | -43.53515 | 2025-09-16 04:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61b4c5b3-3f15-3dd8-b8e1-228792f44fb4 | -5.92166 | -45.72618 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67b23ef5-8c1c-3bf2-82c3-7987121e071a | -6.44541 | -44.09016 | 2025-09-16 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9038e36b-46b7-3bfb-a245-0d34de0dbf66 | -7.03487 | -44.14838 | 2025-09-16 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c339cf11-99e9-3587-826f-1f76b1f82cdd | -5.91778 | -45.72914 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8abb074d-6c03-38e3-a8c3-83e69f9997fa | -5.7754 | -45.53193 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6acc0ded-d3dc-39b0-a30a-8bdecf4ebe4f | -7.08296 | -44.55033 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac4f67c4-6a5e-3437-aa56-c8fd083ef629 | -7.27607 | -46.59511 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 399e780b-8e6e-3a53-a3ff-4428c3a0083c | -6.63527 | -44.73891 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7cda14c-1b80-370a-8086-0ebd9294b34a | -6.38978 | -43.46167 | 2025-09-16 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83fd672e-e542-3d0a-a71d-1062f7777bf8 | -5.75716 | -43.69422 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 305cb850-29b7-35dd-b930-d921f736d684 | -3.81715 | -41.55559 | 2025-09-16 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9ab6ce6b-e206-3e20-8614-c1d4efd07bbd | -7.0824 | -44.54957 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a93415e4-e237-3799-a048-00ed94b49c94 | -7.25367 | -44.48017 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 577a49fd-ebd4-391c-bae0-d75e9eedfab7 | -5.9593 | -42.72993 | 2025-09-16 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 572338b4-61e9-312a-8244-f7399e9cc618 | -5.78064 | -45.88921 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c510e5b-d8ab-3810-bea7-46c85004d887 | -6.18579 | -45.11662 | 2025-09-16 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 677e6975-7d12-38cb-ac67-1775d132c50c | -5.64796 | -45.80809 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 342eb4aa-b4d3-3a13-95dc-b182922359b8 | -2.67127 | -54.79192 | 2025-09-16 04:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3179e60b-154a-3b34-bda7-e99f67d56c52 | -5.79066 | -43.94627 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f1a0acca-d6c8-3baf-85ac-6a0cd2791090 | -7.43883 | -45.8345 | 2025-09-16 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b09b483-d5b8-3928-92f3-f69ae3529e8e | -6.90715 | -44.55823 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62d4eb17-72d5-3952-9b95-ccc7ba5667be | -2.64246 | -48.05301 | 2025-09-16 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d45c80df-dac8-3098-8985-b6023d0b6ba9 | -6.24335 | -44.38641 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7c1591af-4a01-3cf6-a232-29d42609d320 | -5.53637 | -42.65681 | 2025-09-16 04:27:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 1ac5935a-75ee-3091-8d54-1636d2ca8952 | -7.13379 | -47.96943 | 2025-09-16 04:27:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3545a769-ed4e-3019-82ee-822088186337 | -6.71769 | -46.3357 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9895308b-c80d-3803-9253-5c4bb42a1aeb | -6.43078 | -43.31054 | 2025-09-16 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60795e70-8515-33da-880e-7081458e7ad7 | -5.53204 | -42.66053 | 2025-09-16 04:27:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a6436f93-28bf-3bc2-94c3-b807ecfc39aa | -6.19007 | -43.47468 | 2025-09-16 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 212d4b77-2e3b-308e-8d38-68647cde0897 | -6.17776 | -41.21137 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1192a6fd-e97e-3913-803b-80f772536f4d | -4.15858 | -46.79352 | 2025-09-16 04:27:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f742ce2b-0b3d-33f2-9fb2-8c8769fbc3af | -6.18687 | -41.17612 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 96ae7e9a-15db-3c95-8ba5-59b7dbb7294d | -6.99833 | -44.57515 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fc4ee43-2ba2-33ff-9029-30b954f5f9eb | -5.05686 | -45.19767 | 2025-09-16 04:27:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1452a669-0854-383a-9cb7-6b14c5848b3d | -6.97635 | -44.54226 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ff513c1-4aca-370f-b2f2-10e868ec8706 | -7.05111 | -44.11169 | 2025-09-16 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7553e2a5-31d1-3000-9144-c57f4b85be07 | -5.89621 | -49.1045 | 2025-09-16 04:27:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4557b365-9b7f-3de0-a6a5-7db5d25d347b | -5.99778 | -43.69801 | 2025-09-16 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2626b52f-b754-3c07-a527-2b1f677489a2 | -6.45232 | -43.31392 | 2025-09-16 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 657a500f-8120-3592-b285-a32b8674fa60 | -6.54853 | -44.0073 | 2025-09-16 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9696d4a2-2b43-32b7-a682-385a9dc910af | -7.30168 | -43.92973 | 2025-09-16 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddf4aba4-efa3-3d9a-86f6-57ac7ec1b334 | -7.41479 | -45.58196 | 2025-09-16 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a13a9cba-0ad6-35d7-a5f4-64708dc4c66c | -5.06037 | -44.32188 | 2025-09-16 04:27:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd4221c5-8df9-38dd-89e6-c67bcb27f820 | -5.77261 | -45.52792 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbcc3c88-fd8c-3e46-8ec8-2c33320255b3 | -5.7843 | -43.89458 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad21d38a-c5eb-32e8-88a2-fe458a481583 | -6.17617 | -41.22187 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f4853317-cede-38cf-860b-ac5e21bb4cab | -6.97859 | -44.7721 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97e5c75f-9729-3f92-a5b3-72963d5cf660 | -5.93416 | -45.83474 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95f2c39c-8d46-3fba-b2ca-862081004bcf | -7.42492 | -40.07962 | 2025-09-16 04:27:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1c4e0665-674a-3e19-9f11-6c2eb9c83407 | -5.00311 | -47.64458 | 2025-09-16 04:27:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 954a17e7-5452-3eae-a869-4dffc9f11b25 | -5.97136 | -45.85839 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86d0ef28-eab1-3613-bb1a-103137b8ae6c | -6.46214 | -46.00689 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b36c4b0-9d23-3979-937c-fcc727aa4b49 | -5.90724 | -45.73105 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c3159dd-3cd5-3f87-9ddb-15614b673f09 | -3.21436 | -47.12677 | 2025-09-16 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 00c606c3-91ae-3992-87c7-618e5bf72a67 | -5.78962 | -45.93676 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58ea3892-89ff-3758-b69b-38bfa8b97241 | -3.65146 | -54.05573 | 2025-09-16 04:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2468c403-9552-3d5f-8fd8-4bd0973a8f5f | -5.79791 | -45.92744 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc3d38b8-a78d-3c01-9526-fb791803438d | -6.18329 | -41.20094 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 96e94316-d99c-3129-a285-57cc93599f39 | -6.28952 | -44.09048 | 2025-09-16 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62976404-5656-34bd-8b70-dc23f90bfada | -6.8266 | -47.86112 | 2025-09-16 04:27:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 457131cd-3f9f-3ecb-af80-a0e757b0850b | -3.38923 | -50.14772 | 2025-09-16 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c23f670a-8c9b-3510-8660-dfed0c6ce43b | -6.42971 | -52.0108 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff56477b-2e23-33ee-b96e-ac6d8a0034b7 | -5.07443 | -41.16724 | 2025-09-16 04:27:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aaaabe73-ceed-3ec8-9785-a187b9838d99 | -6.18431 | -41.19388 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 15cf60ba-eaf7-3e99-ae26-de5757de6ed1 | -6.65339 | -44.71174 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da7b6702-516c-3ea9-a04f-85c4b5709b59 | -6.01298 | -46.85571 | 2025-09-16 04:27:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f1d50b7-ef3a-3abf-a0cf-d5c5cfe0e0d1 | -3.1796 | -52.44879 | 2025-09-16 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcc265e6-283f-351c-81a0-6b6268986c7d | -3.80735 | -41.56847 | 2025-09-16 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cb64388f-6e71-3e1a-b9d4-b26f61677f87 | -5.22641 | -43.69984 | 2025-09-16 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c0e14c93-d080-315a-97ed-6618a3858266 | -4.40825 | -42.14907 | 2025-09-16 04:27:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c56bb430-4b48-36de-ae2b-efcdeb443b9c | -6.44573 | -46.11108 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e36da3a-f73d-3164-a959-9bf900099cd1 | -6.44812 | -43.31745 | 2025-09-16 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c13024e2-60f1-31d1-9a00-63c4c73b664d | -3.21416 | -47.1301 | 2025-09-16 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 0ab93c5d-e851-3fd4-85a9-9968b3fee57e | -5.56091 | -44.96151 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 582cc172-b212-3db9-902b-232578d25406 | -5.98121 | -45.79581 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8d0b57f-384b-349e-87d0-f524913226c8 | -3.42083 | -43.14741 | 2025-09-16 04:27:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e69af120-255c-3c8c-ad54-992f50249b4a | -4.4871 | -48.11359 | 2025-09-16 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 757a4750-4725-3b10-97f2-8eaefc402d3e | -3.23943 | -43.22404 | 2025-09-16 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d0af350b-4a19-3c16-968c-6be8f6433b30 | -7.03393 | -44.14919 | 2025-09-16 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c8f57bb7-b5c1-3215-8c11-b7c2bf4f10c6 | -3.5181 | -44.03207 | 2025-09-16 04:27:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2e302d64-098d-3341-bc08-387968619c93 | -5.93908 | -44.88119 | 2025-09-16 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d30ea93e-a33f-3b8a-93bd-1bff8aa9a96d | -6.04785 | -43.56121 | 2025-09-16 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d29531a-cdd6-32b1-bc63-8757c88fb6e3 | -6.15651 | -43.67261 | 2025-09-16 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13f0385a-8fc5-36a5-804c-49efdd15d184 | -6.92308 | -44.7719 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a844aba0-ba42-3305-aa33-3a33eee359cb | -6.50366 | -43.19465 | 2025-09-16 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6016f974-6254-385b-a570-36ff38037cf6 | -7.67236 | -44.49947 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b126a1ff-58ac-3a0b-9ec7-ca4f317c1c57 | -6.97231 | -44.56815 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6494cc37-7bd9-3d2d-b61a-4967bef6bab3 | -6.34053 | -43.16636 | 2025-09-16 04:27:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9a34d4d5-e2db-377f-a197-45b11ea49791 | -6.18234 | -41.20843 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0536fb80-8d76-31e6-8aee-7802b345bfbb | -6.83177 | -47.85066 | 2025-09-16 04:27:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 024b47a0-c6e9-3460-9509-591bf48a2b03 | -5.76497 | -43.96649 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a9cc189-b10d-3dd5-9678-30ba1919b41f | -5.98353 | -45.84605 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cea3996c-a4ec-30b4-8862-ddf7ec52a85c | -6.34934 | -44.31165 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f5e13cd-da87-3562-839e-69dec018a612 | -5.5892 | -43.80371 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbed85db-f141-346e-b0b9-7e68b67ddd3d | -5.79072 | -45.92987 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5468838-6c36-3c9c-8a61-c5a854bca8d5 | -7.1332 | -47.97307 | 2025-09-16 04:27:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ca890a8-8267-3f0a-83ca-79dde6d6fd37 | -5.77561 | -43.9284 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 659ae6db-7f38-31eb-acf3-bab85fdd1ec6 | -5.93471 | -45.83126 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README33.md)
