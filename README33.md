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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a30167ee-6bf3-392e-88a2-f290c158d494 | -6.32623 | -51.12364 | 2026-10-01 04:14:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71396737-29e8-3ec7-baca-0f732eaa84db | -8.33346 | -44.16077 | 2026-10-01 04:14:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bc8d1425-13ab-30d7-a292-5b4dd992e29a | -9.21685 | -50.68194 | 2026-10-01 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8d0da00-76e5-3992-8be4-3719150d350c | -7.12473 | -43.16103 | 2026-10-01 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 4ce726e6-a709-3d8c-bad3-6a1118ba81e7 | -7.11818 | -43.15569 | 2026-10-01 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| fa7220f8-6776-38bc-8eef-160dc4cc9e6a | -11.38306 | -43.36986 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d9ca6eb-83db-3d8c-b35d-5e23b92657e4 | -10.54715 | -50.011 | 2026-10-01 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e039d388-5b01-3be7-903f-17fb8e6d44a8 | -11.46784 | -43.46505 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a643e207-c153-382f-9118-36ea5d56fc02 | -12.51355 | -43.10024 | 2026-10-01 04:14:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f86ecc25-926c-3c89-bd61-6be0b274da09 | -4.28955 | -50.77699 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1462.4 |
| d5c83fe0-ce36-3bfa-875a-ca78de9cc64c | -4.2665 | -50.81144 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8e3fc3ae-c046-377d-9abf-dc21c63b4d07 | -4.28584 | -50.73589 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dab0f677-a44f-3dc7-be61-46a1bb176b90 | -7.50044 | -45.7974 | 2026-10-01 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3cbca34-6bf2-3d8f-b7c0-20e555244e18 | -4.28272 | -50.81535 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| fafb2afc-b7d2-3b66-baa2-ce3843d9afc9 | -9.2127 | -45.81963 | 2026-10-01 04:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98dec2e9-6c45-3c1d-93df-22a7410e6a0e | -4.29119 | -50.74173 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66f137e3-c6b9-33fb-a40f-c590cb83b213 | -10.71975 | -45.32352 | 2026-10-01 04:14:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84a0a662-0a7d-3787-adf2-27ea6156f17d | -10.75735 | -50.50965 | 2026-10-01 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6156739-0c8e-3e97-9e12-e3956532eebb | -4.86282 | -45.84325 | 2026-10-01 04:14:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a771170c-6b17-3c3b-9ffc-166147aa76ca | -4.27738 | -50.80949 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c65e9633-4e34-37f7-899a-fe63f17ec88c | -4.3047 | -50.79947 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ee5c4938-474e-3a6a-80a8-51d334875695 | -4.30386 | -50.80423 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 69813cbb-b52e-3218-ba41-754706a812bd | -9.20026 | -45.81822 | 2026-10-01 04:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afab4989-837d-37a0-9a8d-b311dd4816a1 | -4.25709 | -50.81567 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b11856fd-4bf1-3262-ae40-e612364a0a2a | -11.61841 | -43.5376 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc06aba0-7e8a-3e34-bb04-ab619d822650 | -8.84294 | -50.51156 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52692ab6-925e-3152-a818-de64aaa23550 | -11.44156 | -43.42818 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 05fa5621-cda2-3e08-beb2-06ec97400f12 | -4.29404 | -50.76227 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 749d5ca9-0d43-36c2-ad23-a1a5afdae3cd | -11.40101 | -51.02459 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 35b6d7f6-c8c7-3c8d-9352-d8526523694a | -11.4184 | -43.41615 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8586db92-743f-3d88-beed-7db73934d91d | -4.28383 | -50.78476 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 8bf9b918-9a7f-32cd-8e0a-ab5f55c493e3 | -8.38837 | -46.2921 | 2026-10-01 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 434e79ef-3780-36f3-bf42-9430952e0146 | -5.76538 | -45.1693 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d7b15f1-ff44-312d-8fa8-4acd828a1e8d | -4.28804 | -50.82141 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ffe47c4e-af11-38ff-862c-28ce1a3eccab | -9.80074 | -44.8148 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0704ba51-6bbf-3ebb-adb9-49c24bd4ec01 | -4.29655 | -50.74757 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f1847ab7-9cdc-3556-a3ee-9ec3c52f4542 | -11.21652 | -45.14546 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 95c06763-68ff-3d0c-b37c-27a1ac8b0611 | -4.66489 | -49.23096 | 2026-10-01 04:14:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 857c1fb7-9255-3969-8768-8185d629b4f5 | -6.76634 | -48.67859 | 2026-10-01 04:14:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e11f5b3c-d966-3231-90e7-ed9a24eb643d | -10.55606 | -50.05075 | 2026-10-01 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ea78870-707f-3279-b1a8-c11df320278f | -4.26207 | -50.75255 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 7dfe9f35-535a-3bcf-840a-4aa4ba56ab25 | -4.29464 | -50.74841 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1825736c-b618-3b77-bd6a-b635553df859 | -4.28758 | -50.7523 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ca525d63-c96a-3da2-a701-fa75eb1c6402 | -7.5011 | -45.79347 | 2026-10-01 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90354615-2d00-3ab3-adba-436997853418 | -12.35216 | -46.38208 | 2026-10-01 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1077db74-e8cb-3d81-b6dd-fa2b63674dc3 | -8.62241 | -45.37926 | 2026-10-01 04:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ee45684-b9e9-3e82-a49d-6038fb6ba144 | -4.2962 | -50.78696 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| b2799d87-de06-3f8d-aacc-3e00219d52ad | -8.20376 | -45.4946 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88392fef-6661-3d37-be13-82b3b7df17b6 | -7.49202 | -45.7959 | 2026-10-01 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4ca9ced-099f-314d-935d-4f6aaf281d5f | -11.40387 | -51.02877 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 286691f0-96bd-36e0-a3a0-1bda89cc4629 | -4.28586 | -50.76194 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| d1251b38-e3aa-3b1b-86ee-687eefa82f22 | -12.32856 | -46.39746 | 2026-10-01 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3dc3ba51-5fcb-346f-addb-6a9269a821f8 | -4.28399 | -50.73677 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6c7c505-e5a2-33f9-a5e5-4697a113c7ae | -11.4466 | -43.44116 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1dafc49c-7279-3e0c-8f29-28e3275025e8 | -11.18434 | -45.11289 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cf31caec-81c7-3040-aa37-0948bbc9a692 | -11.42386 | -43.40501 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cb26e96-8f94-3c99-8e7d-884800f8563e | -9.21474 | -50.68526 | 2026-10-01 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| caa4708c-1adc-3900-8715-f110035a439d | -5.17944 | -46.19628 | 2026-10-01 04:14:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 98452e0f-8ff3-3f1d-855e-25db8ba2eddd | -6.14231 | -53.25864 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4a49b5d3-2b43-38dc-90d2-c37477442dfb | -10.29775 | -44.64258 | 2026-10-01 04:14:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d282c9c0-7e96-36bf-a802-8bb9d0863c21 | -8.36881 | -45.37831 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d03a8949-e0d4-3c3a-b39c-be44bd9c7fba | -11.41774 | -43.48469 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2fe1324f-460e-3d2c-8052-6fb382b2ccab | -4.2525 | -50.74482 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 76f964d4-6456-3951-8a6a-7903b2965876 | -11.26754 | -43.52045 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3609468d-990a-3c17-b781-88d724d707fc | -4.2533 | -50.74023 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2f4f3700-b6ab-3648-9f3c-1e62d8f2928f | -10.5567 | -50.0474 | 2026-10-01 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d35f959b-f52f-3f5a-aee1-ea26620f9800 | -8.85473 | -44.39308 | 2026-10-01 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c1dc8d1-3c2a-3702-9faf-77da7c02dd6a | -4.29373 | -50.80149 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5e2ef8c9-959d-3a35-a4aa-e66df180b6d2 | -11.16666 | -45.12442 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 87c31d36-87d3-34c7-b162-e9ecc86207b2 | -11.40508 | -43.40982 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdca86b2-b269-3888-9ca6-322f54d39c2b | -11.2253 | -45.18551 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96d05fbc-8a53-3249-a08a-937b0bb0618e | -11.22449 | -45.19021 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ead73aa6-35c2-37c9-8042-3fb59a7467ef | -6.47186 | -46.56054 | 2026-10-01 04:14:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e578aeef-b031-3248-a499-7bb1f4aac1af | -8.20441 | -45.49073 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ec6c34cc-7826-332d-87f8-b7f527a5b0ea | -9.06514 | -49.87479 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4613f15-bc62-39ea-931e-7cbb192e57e0 | -5.75131 | -45.15116 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 32d76d73-e127-3d88-82e0-027ad6ddaac3 | -4.26946 | -50.83142 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3ca9077f-88fc-37fa-90ad-57e213212f26 | -4.8577 | -45.84675 | 2026-10-01 04:14:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3745bb86-990b-3ef4-a3b1-5ce45897b2a7 | -4.25905 | -50.78061 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 49aae145-54c6-3969-b8e6-f6d88b025931 | -11.36016 | -43.35429 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11936437-7ff0-3895-9042-9fb9fcc24f71 | -9.81061 | -44.82626 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44c83282-12aa-384a-ab4a-e4a845a30732 | -4.26821 | -50.75383 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| d3b648db-2f9b-3ce3-8029-cb3b04c700d8 | -11.45644 | -43.44691 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 880415f1-c8d2-320b-95fd-3bcedbd92c3b | -10.29776 | -44.64089 | 2026-10-01 04:14:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f08a8c9e-5534-3e21-bb09-d191cbf11607 | -10.32967 | -47.78844 | 2026-10-01 04:14:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d747945-67d6-3f59-8786-fcd2e0cab4ec | -7.38481 | -46.42835 | 2026-10-01 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26c6c966-685b-3973-8da4-9974b23cc674 | -10.91309 | -43.84477 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4baa943-edf7-3406-bb65-211de0dbb1c2 | -9.90479 | -50.16697 | 2026-10-01 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cac5ba6-2580-35ce-b668-2c6a1195a82b | -7.5101 | -44.5425 | 2026-10-01 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb81c184-3818-3594-b0d0-3570faafae52 | -7.78552 | -49.87628 | 2026-10-01 04:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 614a72bc-642c-3b8f-87be-46c5852a4071 | -4.29864 | -50.77263 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| fa59646e-9525-39ff-a8d9-dd404a6c019d | -4.63753 | -50.6225 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d22a7aa2-5f5c-32be-8c2d-c1c292494adf | -8.58994 | -49.83716 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad426870-c724-39d1-9813-9361da4938d1 | -12.50951 | -43.1034 | 2026-10-01 04:14:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 87e03970-6e41-37cd-8a74-78343ac6ec5b | -4.28265 | -50.82907 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aa12ca77-d8c9-3eb3-870f-c1b324a2fb9c | -4.28669 | -50.8054 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 519f6d46-56f6-3b9f-8e52-3d831a8cabee | -4.26121 | -50.80506 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 182d4c9d-b6c7-3f7f-8c80-a5fc898a2529 | -11.17126 | -45.12049 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 78ffb26d-8e4c-31a0-b4e2-cd9a368e926e | -11.4562 | -43.42669 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 64e4c798-708c-3506-a939-eb56a48ad2b1 | -4.27973 | -50.7606 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |


[Clique aqui para ver as próximas entradas](README34.md)
