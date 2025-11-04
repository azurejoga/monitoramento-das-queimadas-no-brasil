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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d318651-99b7-39a0-875f-f2d331c37cc8 | -5.25773 | -44.81388 | 2025-11-04 04:31:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d68c4bee-35de-3ca6-96ca-2988b389f0ed | -3.49659 | -50.45839 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d0179bc-81a5-35f2-ac12-e51fb2e91c53 | -2.83902 | -49.40903 | 2025-11-04 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9cd16b4f-e758-3bad-a5ac-5501629f78f6 | -3.17416 | -46.58054 | 2025-11-04 04:31:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd4fed8c-a69b-34b1-9c11-658fad67bb60 | -5.83377 | -44.66573 | 2025-11-04 04:31:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8419cf8-e399-30a5-8172-7aa402fea15f | -4.47559 | -43.23163 | 2025-11-04 04:31:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 2d54d18b-7b8b-38c4-a957-352d2c410954 | -5.25978 | -48.47757 | 2025-11-04 04:31:00 | NOAA-20 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e011847a-3f86-373e-ad19-61108728c6ab | -3.92297 | -47.69228 | 2025-11-04 04:31:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fb76fb33-627a-35e1-b4f6-c578a44c3ce6 | -3.01718 | -51.09603 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11601d89-cac4-3012-9b09-85e833530fc6 | -5.3546 | -46.71524 | 2025-11-04 04:31:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f165639d-f38a-3e29-9d16-43941e2ff8ac | -2.83665 | -49.83447 | 2025-11-04 04:31:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70426506-a31e-37b8-ba44-376ffba1dcb8 | -4.61769 | -46.10297 | 2025-11-04 04:31:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6cf18ea-5bfb-3bef-ab7b-3acf6c027d72 | -2.65277 | -48.50426 | 2025-11-04 04:31:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9003d731-2c35-365b-8b33-1ebdb4f077f2 | -5.36865 | -45.07949 | 2025-11-04 04:31:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e30c8e8d-1f0a-35e6-8ac5-4696862dd83f | -3.44091 | -50.2454 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| a8e282b7-62d3-3cc6-b96d-7408f0c73c48 | -5.76391 | -43.92229 | 2025-11-04 04:31:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59d5c3de-9b3d-38f0-bfac-260d2f67e35c | -7.61477 | -46.4796 | 2025-11-04 04:31:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce265800-1e47-3a62-8e75-0a95d18a8efc | -5.83384 | -44.07436 | 2025-11-04 04:31:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d57ab7ca-ed8d-33aa-b206-ee4ef15ac51e | -3.89805 | -45.1163 | 2025-11-04 04:31:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5f5a591-53ba-30a0-9f4b-9af57bbe0135 | -4.38076 | -46.27259 | 2025-11-04 04:31:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81318450-e94f-3cdc-ad80-59c8080bdb68 | -2.98588 | -48.70785 | 2025-11-04 04:31:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81b5d4aa-6b35-3a35-bfcd-2c5d61a68ba9 | -1.76785 | -53.55648 | 2025-11-04 04:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed3ce278-bbe2-3b2e-ab3a-9f4387ee4828 | -9.23934 | -47.54377 | 2025-11-04 04:31:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7200b052-b416-33fb-85b9-915526d23adc | -2.31598 | -48.59314 | 2025-11-04 04:31:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e07306bc-ccc8-3ef5-900f-e1a171a96153 | -2.3753 | -47.72172 | 2025-11-04 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d6adddb0-5040-35a3-b6c8-e13c10acc5f1 | -5.92583 | -41.32795 | 2025-11-04 04:31:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7cd16a3d-9b65-3451-b638-d57a004c6f96 | -4.59051 | -44.61353 | 2025-11-04 04:31:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c042fa1-bb6d-3ae5-b037-1caf6afed576 | -4.52115 | -45.25467 | 2025-11-04 04:31:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76415e30-dac5-3bc9-92d8-18af91773d2b | -9.31956 | -43.1011 | 2025-11-04 04:31:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3f6fa26b-3a01-3368-90e7-511a1286ca81 | -4.91449 | -45.09242 | 2025-11-04 04:31:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40bfbe7b-2045-3b2d-8662-9c67e9bdabbe | -4.00977 | -45.30082 | 2025-11-04 04:31:00 | NOAA-20 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a44d9f3-c04c-31e1-8b99-2b21a09e83fc | -5.61472 | -45.97901 | 2025-11-04 04:31:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28ee9172-0023-3bd9-94da-13a4dac5bbf5 | -2.90257 | -51.46719 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c26ff697-f875-3bf9-9831-0cadd9d3c479 | -5.27587 | -48.50531 | 2025-11-04 04:31:00 | NOAA-20 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 71e63b8a-cd9b-3b9a-b9af-70dd33cc6c0f | -5.30134 | -44.81244 | 2025-11-04 04:31:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9bf38854-2069-3b48-b3a5-f5d8acfbba63 | -6.40651 | -43.07017 | 2025-11-04 04:31:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec086573-888f-3158-b394-3191707c6ca6 | -8.11062 | -43.82265 | 2025-11-04 04:31:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 15f8ba36-6925-39f3-813e-128d70806dc4 | -3.91912 | -47.69522 | 2025-11-04 04:31:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3c3a5065-a5cc-37b4-a119-d4b749c52912 | -3.86328 | -52.33107 | 2025-11-04 04:31:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f00ce7d9-b33f-36aa-abb9-0bc9b163a1f4 | -5.28118 | -44.61224 | 2025-11-04 04:31:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b3a168e-4534-3322-bce4-0a2974a4b77f | -3.92188 | -47.69919 | 2025-11-04 04:31:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c9dae4e5-45b1-3bfb-8015-ceb692a7e921 | -4.28279 | -47.17746 | 2025-11-04 04:31:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db739611-8547-3107-940c-eae2c33093ca | -6.12456 | -41.68148 | 2025-11-04 04:31:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dd3f3e56-bb07-3b97-b402-1515a65b621f | -2.66889 | -49.95979 | 2025-11-04 04:31:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1670fdf-052c-3c66-a5da-15c22f5a9864 | -5.25054 | -50.96483 | 2025-11-04 04:31:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa214433-1a0c-30e5-b340-57a965284ea5 | -4.57862 | -43.34459 | 2025-11-04 04:31:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ee1dc9f9-65b3-3230-a715-55326e0db9f7 | -3.4107 | -50.18145 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13e0b63c-6983-3770-b9ad-813c7ee104c8 | -5.77744 | -40.8097 | 2025-11-04 04:31:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6a0b5831-ee92-3c93-aa2b-b5a2eba5f76f | -5.23549 | -46.56376 | 2025-11-04 04:31:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7c0a6b14-32b7-3557-9544-07067705b019 | -4.02591 | -45.46569 | 2025-11-04 04:31:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e95c343e-3216-3cb6-8a88-dc777d9ac419 | -6.32224 | -46.00033 | 2025-11-04 04:31:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81b4f42d-1f04-329c-9be5-7506852a4427 | -3.01454 | -51.39768 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c99d8abc-ee0a-3c0c-890e-6d3b1aaa4b3e | -2.87885 | -45.29617 | 2025-11-04 04:31:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1c60784-42cc-3d47-845d-b41b897b2213 | -6.46777 | -43.22483 | 2025-11-04 04:31:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 87ab3cc3-bfaf-3df5-99b8-33514943b938 | -3.1703 | -46.58347 | 2025-11-04 04:31:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e15c50c1-5b6e-3672-8f88-5d795c7e181b | -3.3105 | -48.71765 | 2025-11-04 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cb6e3e29-113b-3f3c-a38e-202eb1f9b862 | -2.94839 | -51.58049 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46b6c9d7-b363-381e-8ca9-dc84f98e2ec5 | -3.23524 | -50.80106 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd867a3d-397e-307c-9139-efd69e2b0388 | -4.91161 | -45.08801 | 2025-11-04 04:31:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 100c18ec-6898-3c2a-9526-0156941d38c9 | -7.55401 | -45.85131 | 2025-11-04 04:31:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac670fa3-885c-37a5-ab63-5be0182be2c4 | -4.41389 | -49.77949 | 2025-11-04 04:31:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21f10379-167a-39df-a87f-7685caef80a7 | -4.47042 | -50.92029 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83b2fadd-dca8-305b-8878-28b5652095e4 | -4.02031 | -51.01252 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2259375e-ec1a-3713-b8fc-f1dedebf7850 | -2.60871 | -46.91463 | 2025-11-04 04:31:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d7b84dd-4da3-3fbe-9a8d-e86f0a8da832 | -3.48648 | -50.31502 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2fe4f60-ccef-349f-8cad-cd4039623e2d | -5.11992 | -43.37162 | 2025-11-04 04:31:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d22f9b1c-5f56-3c56-a804-dbf71f808501 | -2.4841 | -49.23284 | 2025-11-04 04:31:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f65fed7a-572c-38f4-9ad7-d89e88af0b14 | -5.98854 | -41.92266 | 2025-11-04 04:31:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 34a79d74-09bc-3ddd-b7b8-6d3c2bf2dc46 | -6.40726 | -43.06514 | 2025-11-04 04:31:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0889333-d3e3-3420-8791-41a4bede5514 | -4.9573 | -44.90834 | 2025-11-04 04:31:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5ebf8c5-e2c3-380d-8c37-4af4b74fdb74 | -3.3884 | -54.27607 | 2025-11-04 04:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d189cb5d-5547-360b-9ed5-225fa8f65a87 | -4.01823 | -46.78694 | 2025-11-04 04:31:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82c273d6-ffed-3f49-b5bd-de8e0ff84139 | -3.91471 | -47.7016 | 2025-11-04 04:31:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b94185b-9a6c-348f-b46b-2eb53ebfe7f9 | -6.70805 | -43.56883 | 2025-11-04 04:31:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a238f01-9b91-3878-ab83-a1bf14236597 | -3.53323 | -49.44773 | 2025-11-04 04:31:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d53f550-a9ce-3dc9-a144-da1e5442b99d | -5.8981 | -42.90726 | 2025-11-04 04:31:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d10b16cd-258d-3567-9faa-e98b0f6f1e22 | -3.74698 | -52.07835 | 2025-11-04 04:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f709c73f-2c57-340a-b23a-affe763c712b | -5.83184 | -44.08748 | 2025-11-04 04:31:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad43be1a-e426-39a1-9def-5ba018389f30 | -3.23896 | -50.80167 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50a8677b-3ecf-3398-9832-6caf3cdd54c4 | -3.23596 | -50.79663 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08390405-f5e0-3024-97dc-a0824e79755b | -7.07001 | -46.73524 | 2025-11-04 04:31:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8841cec6-6b94-3810-be9c-e405ffc51630 | -3.25277 | -52.91241 | 2025-11-04 04:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 434cb5af-16d4-3ad1-95e5-a4b57db60361 | -6.4112 | -43.06576 | 2025-11-04 04:31:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 16452cc5-c6a6-3c53-8587-25a9003fe331 | -5.31314 | -43.52856 | 2025-11-04 04:31:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22c94168-26d8-33d2-9ee0-4e0e0b3e7404 | -7.85303 | -44.20889 | 2025-11-04 04:31:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 876341e6-6b7e-32bb-9007-5f26a0dd2ac1 | -3.3521 | -50.23636 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 018dee37-a319-321c-bc7e-eea190ac26d8 | -2.66443 | -51.62239 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| fa14fc27-ff08-3606-88d9-a02bd69fca42 | -3.44157 | -50.24127 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 63ba1487-4759-3bdc-b041-21938d076567 | -5.03225 | -43.6191 | 2025-11-04 04:31:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 20a3a711-ea58-32f8-8e06-48fe0ae6dd92 | -3.91195 | -47.69763 | 2025-11-04 04:31:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| d9d07b02-c5ef-3129-9459-af0c018cbc11 | -3.43797 | -50.2407 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| b99e6426-a2c2-30ce-9acd-ecaf9fd49195 | -6.48517 | -39.41967 | 2025-11-04 04:31:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a39d2e71-db4e-3f48-94f9-05daf0ea717d | -3.44463 | -51.47172 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4935d35-2f5e-36ef-8ba1-6c12458c53b8 | -6.34632 | -45.84554 | 2025-11-04 04:31:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc6a47d9-d92d-30dd-92f8-64955e84d6fc | -4.64972 | -46.29275 | 2025-11-04 04:31:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff299ad1-2c57-3429-aab2-a25e0653b01c | -4.58858 | -40.97922 | 2025-11-04 04:31:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c09402fe-eb5b-33d4-ab1f-02feecbc8106 | -1.58864 | -53.2284 | 2025-11-04 04:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 673b7b47-8892-3097-af35-05efd5cbd594 | -3.24267 | -50.80228 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b73757fd-676d-34ac-ac28-1b4b88ec4919 | -4.91506 | -47.3267 | 2025-11-04 04:31:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec9433d9-20ff-3035-95e3-cc45c0d36d93 | -5.61585 | -45.97173 | 2025-11-04 04:31:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |


[Clique aqui para ver as próximas entradas](README19.md)
