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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e21e1fb2-dd92-3532-9316-f7f33c2cbca7 | -13.40994 | -41.32835 | 2024-12-29 03:57:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a7890402-283e-3b60-af18-007929f7db9a | -11.88753 | -40.95485 | 2024-12-29 03:57:00 | NOAA-21 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 553719e9-b030-3592-9942-eb0862cbb796 | -16.8905 | -40.55064 | 2024-12-29 03:57:00 | NOAA-21 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ad904841-2343-3add-8380-195d51c8e44d | -16.89712 | -40.55176 | 2024-12-29 03:57:00 | NOAA-21 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a003b9e6-ea34-34f9-8b6b-9dabbf159d42 | -15.52353 | -39.17528 | 2024-12-29 03:57:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d4b4fb83-f483-3205-a0c0-f3751c475e9d | -12.64383 | -38.56311 | 2024-12-29 03:57:00 | NOAA-21 | SÃO FRANCISCO DO CONDE | BAHIA | Brasil | 2929206 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 5ed926ee-094c-3568-9eb6-5615a0816072 | -11.96118 | -44.21619 | 2024-12-29 03:57:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c237195b-f432-3c48-8867-6ca70dc9a461 | -13.11609 | -43.37134 | 2024-12-29 03:57:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1999af1-c092-362f-ae5c-76c91a338580 | -11.88695 | -40.95847 | 2024-12-29 03:57:00 | NOAA-21 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e03dd68f-890d-3fe6-ae8f-cb3e7654d0c6 | -16.89381 | -40.5512 | 2024-12-29 03:57:00 | NOAA-21 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ac1eb0b0-d998-3e22-b2f5-058c33235920 | -12.64047 | -38.56258 | 2024-12-29 03:57:00 | NOAA-21 | SÃO FRANCISCO DO CONDE | BAHIA | Brasil | 2929206 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6a40ffe9-17d1-35e8-afb6-df0ebbffe528 | -12.76106 | -38.48347 | 2024-12-29 03:57:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d9284027-352e-3a24-825a-2f61eedf1aa4 | -15.09983 | -40.03986 | 2024-12-29 03:57:00 | NOAA-21 | ITORORÓ | BAHIA | Brasil | 2917102 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 91275302-4fce-3aa9-9abc-38601e7f0cbc | -12.41272 | -38.83457 | 2024-12-29 03:57:00 | NOAA-21 | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a5799b61-fba5-32bd-b5ae-aab8eae44de3 | -18.03908 | -39.92547 | 2024-12-29 03:57:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1ab38531-fae3-34b3-ba6c-4152fe859d07 | -15.59531 | -40.6369 | 2024-12-29 03:57:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3480280c-14c6-30cf-9674-6dc756ce61d6 | -12.64328 | -38.56676 | 2024-12-29 03:57:00 | NOAA-21 | SÃO FRANCISCO DO CONDE | BAHIA | Brasil | 2929206 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 20c4548b-8a36-37b2-baea-657c3a4a7425 | -13.11537 | -43.37564 | 2024-12-29 03:57:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2969c93-d7b8-3aae-8216-7f01187926af | -12.86272 | -38.36751 | 2024-12-29 03:57:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0f5a710c-82fd-3459-a787-759cec6b82cf | -12.93347 | -41.11705 | 2024-12-29 03:57:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fcf86023-3d83-3664-8c7b-a48d1ec807ae | -23.4066 | -46.55771 | 2024-12-29 03:59:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ebc0b895-b9c9-32c1-933a-0702ffb5bc23 | -20.99402 | -51.79344 | 2024-12-29 03:59:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 28d79e1b-ba7a-320a-9bc9-03ee4bc4ac7a | -22.53934 | -48.8119 | 2024-12-29 03:59:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fcb89c5-45a5-358a-af12-66c18980e2af | -23.70474 | -46.47892 | 2024-12-29 03:59:00 | NOAA-21 | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4514e788-1dd5-35dc-a91e-514bfdc1f112 | -23.33915 | -46.77497 | 2024-12-29 03:59:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7a5b2e14-7046-3ca3-8676-af8abdf399a3 | -23.33902 | -46.77276 | 2024-12-29 03:59:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 47468606-6794-3da4-8afd-2ef43430893e | -20.59673 | -51.60953 | 2024-12-29 03:59:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| db78bc41-be8d-31fe-9ab6-36eb5ffb7d67 | -24.24299 | -50.74043 | 2024-12-29 04:01:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c8fc78fc-b67d-38e8-b588-3d0b6da8e78b | -28.24438 | -54.00609 | 2024-12-29 04:01:00 | NOAA-21 | CATUÍPE | RIO GRANDE DO SUL | Brasil | 4305009 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3fadec5f-51ec-340a-9682-813ea15beff2 | 1.57945 | -55.84536 | 2024-12-29 04:18:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 10c58c9f-3147-36d0-aef1-5035b6aaab09 | -1.55705 | -45.67846 | 2024-12-29 04:18:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0fe35c0b-cf6b-3395-9277-c1b6cb12a5ec | 1.58071 | -55.84395 | 2024-12-29 04:18:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 72e4146e-f08b-3359-8f7b-edd3fc07d0c4 | -1.55764 | -45.67472 | 2024-12-29 04:18:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f20f9e9f-989d-3f97-a844-7339c2ef1eca | -3.2872 | -42.54137 | 2024-12-29 04:21:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a32268d4-22c0-3944-b33e-3ca6a8bc602f | -6.97595 | -43.00426 | 2024-12-29 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8eae61d7-2855-3f49-905c-109c7fad22c8 | -3.28689 | -42.54155 | 2024-12-29 04:21:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bc74f3c-80c6-300d-986b-c1370126c447 | -4.71046 | -44.62298 | 2024-12-29 04:21:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ae72b605-f877-3af0-850f-563930d2be40 | -4.78698 | -46.39578 | 2024-12-29 04:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c90a549c-6f5f-387a-a453-010df049641a | -2.25608 | -53.5566 | 2024-12-29 04:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d252be3-c89b-3858-b210-a3a4fc8104b4 | -5.42463 | -37.73922 | 2024-12-29 04:21:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ba2b91f9-8269-3b28-a16f-9a7057645616 | -9.65535 | -42.78476 | 2024-12-29 04:21:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 62c85cf0-2819-330b-83f8-2dc8fc6804ff | -7.3808 | -45.83591 | 2024-12-29 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6827238b-9005-3d9b-84c5-16c8d2afa113 | -6.99534 | -45.6232 | 2024-12-29 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 494beb6e-312f-3fb7-9762-014c7e587fb8 | -6.71002 | -44.31817 | 2024-12-29 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9929fbd0-f3e6-3a3e-88d9-844bee7c2162 | -2.07124 | -54.70298 | 2024-12-29 04:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4cdab814-6ace-3b8b-8b25-dfafefc01762 | -3.95642 | -43.24008 | 2024-12-29 04:21:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fe48285-6e2a-3b50-b083-79094750355d | -2.09268 | -45.40315 | 2024-12-29 04:21:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 677aef60-6117-3db0-a8ae-901ac64ee78b | -7.14759 | -46.55084 | 2024-12-29 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad8f64f7-7125-3cfd-837f-49d3cf3cc442 | -4.54882 | -50.18857 | 2024-12-29 04:21:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8d828de-674c-343d-bb90-7893b982d88c | -7.37746 | -45.83538 | 2024-12-29 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d2b16641-d4a2-30c3-95a4-0ba32a47a32f | -3.56682 | -40.85434 | 2024-12-29 04:21:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1bf55b4b-c043-3b4b-b086-4f30d241a1e5 | -4.79101 | -46.39265 | 2024-12-29 04:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8e7de72-bf62-336c-9ffd-17e765a72c20 | -5.20914 | -41.24121 | 2024-12-29 04:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1d90abd3-427c-3939-8b70-0547fdb23c97 | -7.58817 | -46.46102 | 2024-12-29 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8e62291-f4e6-383e-81d5-05173ef9e150 | -8.62936 | -46.02461 | 2024-12-29 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2369f6fa-92de-3f3d-8b0b-2f4ddbd70fa6 | -9.65595 | -42.78072 | 2024-12-29 04:21:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| da4bc2e0-7f27-357d-a74d-d78e97170221 | -5.49861 | -43.97926 | 2024-12-29 04:21:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| def233e8-5535-3f2b-861a-853a77cde030 | -5.49528 | -43.97874 | 2024-12-29 04:21:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1f1e7e5a-ae65-392f-a3c2-f494d6a74573 | -3.53021 | -40.92399 | 2024-12-29 04:21:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c33a1122-e5c4-38b7-ac56-52a40b5c7c76 | -4.51896 | -42.06879 | 2024-12-29 04:21:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f603b33b-e578-3dcc-86c1-f607961d3627 | -3.48371 | -43.58298 | 2024-12-29 04:21:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a22b04b-8560-30ed-83b4-7bc523c7e50e | -7.26564 | -45.36912 | 2024-12-29 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74d245f2-c447-3fb1-b179-abb2ce3ef798 | -8.95717 | -47.30543 | 2024-12-29 04:21:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4bee223d-08a1-3417-bf0e-682d8a36b097 | -4.79041 | -46.39637 | 2024-12-29 04:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20ec2e2d-37d7-3b9b-a7cc-e1244b3e712c | -6.97537 | -43.00799 | 2024-12-29 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b900ea71-d6fc-3acf-92f1-3a5fb9cca637 | -3.94299 | -43.23801 | 2024-12-29 04:21:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c019c868-30e1-3ea1-8d8c-81309f42ab80 | -5.4257 | -37.73782 | 2024-12-29 04:21:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 41e75fea-fe30-3330-a6bc-4390f649e0da | -4.71378 | -44.6235 | 2024-12-29 04:21:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cba86e46-1cdb-3ae3-9b47-b51c8a2abc23 | -8.62992 | -46.02108 | 2024-12-29 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6aece8ba-c3b9-3865-b2e5-463c7392b5d5 | -4.82498 | -45.37342 | 2024-12-29 04:21:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 836c3c84-b0a0-3a61-b7b2-731738e70a78 | -7.37411 | -45.83485 | 2024-12-29 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 069228ee-fb45-3bd6-be24-854a3024e1a1 | -5.42529 | -37.73454 | 2024-12-29 04:21:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ef92cb8e-ad22-3c8a-bb22-40560af5d426 | -3.97058 | -38.35941 | 2024-12-29 04:21:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cd6475f1-b8bb-301e-a42c-2982bb23fea7 | -4.79444 | -46.39324 | 2024-12-29 04:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c995fde7-e395-3465-971a-0cea2f265a73 | -5.49807 | -43.98275 | 2024-12-29 04:21:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f95be7ac-1fa9-3cb5-aef9-d527e1665f63 | -2.06974 | -54.71181 | 2024-12-29 04:21:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4aa801da-1d48-31db-a09f-c73664e14fc7 | -1.15285 | -53.59496 | 2024-12-29 04:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb21b076-f386-3917-bc69-c055af4b82a7 | -3.28664 | -42.54501 | 2024-12-29 04:21:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae8e5943-ad22-34f6-a345-72c68aa32391 | -9.65239 | -42.78018 | 2024-12-29 04:21:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9c635c0a-9947-328b-a8a0-4219bb512129 | -5.42988 | -37.73525 | 2024-12-29 04:21:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bd97594b-ca34-33e0-abbc-bc07c08f2ffb | -1.77938 | -45.91925 | 2024-12-29 04:21:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce8c6d4d-66c9-39fb-9266-b13b852e3a2b | -4.19769 | -42.89822 | 2024-12-29 04:21:00 | NPP-375D | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f38e412e-3a27-348f-bb69-07180a62b03d | -4.82163 | -45.37289 | 2024-12-29 04:21:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f84d51ca-ef6e-3d81-b96a-6a168bbdb4fb | -3.56444 | -40.84529 | 2024-12-29 04:21:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 572c4312-50d9-3631-bab0-fdc3e263f5a4 | -6.96562 | -43.00265 | 2024-12-29 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 601ae747-780c-3ae8-a4a8-bb4eeb873ad0 | -9.65179 | -42.78422 | 2024-12-29 04:21:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 699c3dd4-d739-3c75-9dae-e81dbe50c094 | -2.25668 | -53.55291 | 2024-12-29 04:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d9a494f-5e60-3bac-9246-5bd51bea4aea | -7.3769 | -45.83891 | 2024-12-29 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3586443f-4e3b-3b69-8a63-7319bbb63103 | -6.1627 | -44.42162 | 2024-12-29 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a00a77c-b983-3005-bb7b-28f0ff2598b5 | -5.42921 | -37.73994 | 2024-12-29 04:21:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5a99cb89-aae9-3eb3-91ac-4495f1453e3c | -5.76203 | -37.56083 | 2024-12-29 04:21:00 | NPP-375D | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 96a0f610-29b6-3d65-ad8e-738cf079d307 | -5.17529 | -37.6627 | 2024-12-29 04:21:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 63c6754e-72f8-3fa4-a7c7-8934905ad25e | -6.99868 | -45.62372 | 2024-12-29 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b820d0cc-f502-3428-aa52-89d6091ef0bd | -6.98214 | -47.08239 | 2024-12-29 04:21:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 082bc671-0d2b-3bb8-8419-5e73634bc7f5 | -9.37781 | -43.64166 | 2024-12-29 04:21:00 | NPP-375D | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0bb55509-4e71-3dcc-964d-d05ec450308b | -4.52245 | -42.06933 | 2024-12-29 04:21:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 3b5c839c-6881-3280-84e8-0faa1f92e7cc | -5.48951 | -45.47448 | 2024-12-29 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f0a0aaf-40cd-33a2-8ea0-825330477b93 | -5.49473 | -43.98223 | 2024-12-29 04:21:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 08773d2a-3d99-3b17-8c9c-16e896df0791 | -5.76378 | -37.56423 | 2024-12-29 04:21:00 | NPP-375D | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 1ef09323-ab41-3837-98fa-53a557249037 | -3.28632 | -42.54517 | 2024-12-29 04:21:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README3.md)
