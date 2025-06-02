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
| 36f823ce-168e-3da8-a05a-f467535e9937 | -17.3041 | -42.643 | 2025-06-02 02:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 366504b7-1ba5-37e9-adcb-7c8b1886a605 | -17.284 | -42.6479 | 2025-06-02 02:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 3ed52f3c-7199-3a0c-863b-69361ff2a1b5 | -17.3041 | -42.643 | 2025-06-02 02:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 64.8 |
| bda0b2e2-1694-3462-9a5d-026ab16978e3 | -17.284 | -42.6479 | 2025-06-02 03:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 64.8 |
| c943ee2e-aaba-3d11-b698-912ed8cd2bd1 | -17.3041 | -42.643 | 2025-06-02 03:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 63.8 |
| e8837f6f-f39e-324d-94b2-0a6517bf9ba5 | -9.4964 | -40.3088 | 2025-06-02 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 86.6 |
| f0273606-29bc-3254-86cf-b3c8aaf85d99 | -17.284 | -42.6479 | 2025-06-02 03:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 729dfe26-41bb-3001-8306-cf0c8e622ec4 | -17.3041 | -42.643 | 2025-06-02 03:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 2354c406-4277-358f-8729-c7886fb12f3e | -17.3041 | -42.643 | 2025-06-02 03:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 62.0 |
| df5a3933-f9b3-374c-9b24-f6f80700f2e6 | -8.77883 | -37.02426 | 2025-06-02 03:47:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 309cc7e8-cf01-363a-a023-e32548a03372 | -7.07318 | -44.92234 | 2025-06-02 03:47:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| fa9b7473-a2fa-382d-ac31-39891d7fc727 | -7.08292 | -46.55944 | 2025-06-02 03:47:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0482cc3a-b084-33df-adf7-3333ab4141fa | -6.73452 | -42.88451 | 2025-06-02 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 35a89082-d8d7-3612-b3d2-0f770c238438 | -5.62457 | -39.61145 | 2025-06-02 03:47:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3bfd6f3b-7275-3e83-bc61-9f3e4c96c22e | -7.05896 | -43.20786 | 2025-06-02 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 486296d4-b768-3472-89ee-483a8c84f2bc | -5.36859 | -37.32902 | 2025-06-02 03:47:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dc264a97-1be0-3744-b293-82b27cd42e7e | -7.07223 | -44.92786 | 2025-06-02 03:47:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7b6953fd-d088-3a79-9400-a4167051cdbf | -5.76341 | -37.56652 | 2025-06-02 03:47:00 | NOAA-21 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 8e8905d2-b880-3866-9a93-c1bf5cd3418e | -5.36804 | -37.3325 | 2025-06-02 03:47:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6ff270b5-9969-343f-bb9e-df203f62299e | -7.00968 | -44.60589 | 2025-06-02 03:47:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01811baf-057e-3bb1-ab6a-cf2ad838e4a9 | -5.06901 | -37.71593 | 2025-06-02 03:47:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 24ce3259-c7b7-35d3-a936-1d51197f3b36 | -5.92419 | -45.53462 | 2025-06-02 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 665132d0-eaba-3292-b4a1-824f8dbc9a33 | -4.82311 | -44.35573 | 2025-06-02 03:47:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6fdfc6c-07ed-3f4e-afcb-edf4b422ddf4 | -5.9201 | -45.52753 | 2025-06-02 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99ab9d0f-c4bd-350c-818f-76865d411382 | -6.63921 | -43.20548 | 2025-06-02 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e3dcb543-8a24-3504-98bb-0c17fb89a6b4 | -7.01234 | -44.59048 | 2025-06-02 03:47:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5e95b73-42f0-3245-96f3-8f739c33222d | -6.73314 | -42.89263 | 2025-06-02 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e0659465-be4a-36ed-ba76-9e97b2aeaa67 | -7.47623 | -37.40847 | 2025-06-02 03:47:00 | NOAA-21 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8f119005-0995-3d8c-8d8e-3715d40072fe | -6.74458 | -42.90298 | 2025-06-02 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 50a47543-6f49-32ee-8d57-989df5a7e419 | -6.63849 | -43.20656 | 2025-06-02 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 920047cc-1907-39d9-ae9f-0217084e60ef | -6.49358 | -42.85075 | 2025-06-02 03:47:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5d077d85-27a1-3004-bf15-28fcc4a24612 | -7.08357 | -46.55582 | 2025-06-02 03:47:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1afcd99f-690e-3ffd-828e-a36a9fa597b6 | -6.49227 | -42.84967 | 2025-06-02 03:47:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7b62c09a-cb53-3f82-94fa-ea421b37256e | -7.00875 | -44.61124 | 2025-06-02 03:47:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36cea1e3-f460-365c-b3d9-25bd2d800bc3 | -4.81822 | -44.35496 | 2025-06-02 03:47:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17682c2e-3342-3f0d-b0b3-82d2bd3c9157 | -6.63918 | -43.20236 | 2025-06-02 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 934690cf-2412-3ff4-bc7a-4540fc85dbb9 | -5.92474 | -45.53156 | 2025-06-02 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 248384ff-956c-3760-a2cc-af051acdb6b2 | -5.92365 | -45.5304 | 2025-06-02 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a4b0e02-1f89-3573-881a-9f662b38a962 | -6.73245 | -42.89667 | 2025-06-02 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f3a7accc-1644-3f85-a530-457f7741eac1 | -7.35553 | -43.14396 | 2025-06-02 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a40f131c-8a0e-3e03-a9f9-aec80a9673f4 | -5.92313 | -45.53347 | 2025-06-02 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 438a7eb9-96ca-3c61-9859-84839529878b | -5.91956 | -45.53062 | 2025-06-02 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04f92c2b-fb65-376d-a05b-adc6769c3e74 | -5.91847 | -45.52946 | 2025-06-02 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fee3731-f7aa-38b0-9bf8-5eb883b4ce56 | -6.73382 | -42.8886 | 2025-06-02 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bb416d44-c2ea-372d-b9e3-c905ebc66804 | -7.47689 | -34.84214 | 2025-06-02 03:47:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 783b3cc4-101f-3282-90bf-c21a95d9d3f0 | -5.92417 | -45.52731 | 2025-06-02 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dace6781-a199-3f30-b156-a76eef30f19c | -4.82077 | -44.35705 | 2025-06-02 03:47:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 651afd8e-8d89-3c11-b6d9-8c4c644983ab | -7.07422 | -44.94544 | 2025-06-02 03:47:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1c9429cd-d2f3-3073-8727-ec39994d2d37 | -8.07403 | -34.97718 | 2025-06-02 03:47:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 704e49bb-0736-3dea-bd48-4c106f4f46d2 | -7.01148 | -44.59547 | 2025-06-02 03:47:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 144a29dd-76c9-3dca-bb03-3d177ff85d3f | -5.83313 | -44.08996 | 2025-06-02 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1402df14-2d02-31f7-a148-c4f9de9e0957 | -9.5646 | -40.77839 | 2025-06-02 03:49:00 | NOAA-21 | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6848daa4-b342-36c7-9642-4c397999b8e1 | -8.32702 | -47.1009 | 2025-06-02 03:49:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dceecda6-2abb-39ed-90a5-c851e7da3467 | -7.8824 | -46.23101 | 2025-06-02 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 590f1585-2342-3088-b8ec-852b7e0fc532 | -9.40152 | -40.36425 | 2025-06-02 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 7aa6c747-a8ce-344b-9867-2944059c5a85 | -13.10705 | -45.26558 | 2025-06-02 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a382097-9872-3b73-a64f-73bc63bc2865 | -8.32778 | -47.09666 | 2025-06-02 03:49:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b219697-cf51-36cf-bfa8-c48a1c8bb61f | -13.08373 | -45.26591 | 2025-06-02 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7adc51af-019b-38ed-97d0-51c7cd0e58bd | -9.39798 | -40.36367 | 2025-06-02 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 4d23448c-4bed-3b21-b776-acff0fb3ce6f | -9.16883 | -45.33409 | 2025-06-02 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3b43b5a-e239-3426-af76-f1127a2b8789 | -9.33843 | -47.08156 | 2025-06-02 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 885fd3d7-f475-34a1-9c6e-5cf3e44cf770 | -9.11506 | -47.64637 | 2025-06-02 03:49:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4dd4672b-fac4-363a-9a63-1ee289f0e07f | -4.33209 | -40.18836 | 2025-06-02 03:49:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f523c8d6-04f1-3cb4-b426-35b669c7b1ef | -9.11575 | -47.64256 | 2025-06-02 03:49:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f16b983f-b557-3d42-b9aa-aeae48fb00fe | -10.98249 | -44.62325 | 2025-06-02 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2709b8d-45ef-3d8e-8dbd-01bd9892b5e4 | -13.08288 | -45.27055 | 2025-06-02 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 974cfd7b-85a4-3336-a014-ae6d34f5369a | -3.51596 | -40.35736 | 2025-06-02 03:49:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cd014177-cf26-349f-9a96-ca688c715594 | -7.95613 | -45.42029 | 2025-06-02 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03ada330-06ac-369d-8381-5421e48d3d7c | -9.39863 | -40.35961 | 2025-06-02 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| dfe01ebb-eed0-3859-add0-a4c6e44b73a8 | -13.09357 | -45.26297 | 2025-06-02 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d83abbb2-3ed2-3f5e-9d98-51397e3c8801 | -8.5926 | -39.53923 | 2025-06-02 03:49:00 | NOAA-21 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 97476d85-83ef-3b6b-9865-46243273dac2 | -10.46961 | -47.94571 | 2025-06-02 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ac36569-70ab-38ad-ab2d-d57356b4b6f3 | -9.39443 | -40.36309 | 2025-06-02 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 43b73241-51ff-3457-91c9-c05baa35c806 | -13.09273 | -45.2676 | 2025-06-02 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5023306b-de45-39f7-bf54-ebf522e35b1f | -10.46817 | -47.95344 | 2025-06-02 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e32ec306-3135-3552-b7e5-b5010e2a5a64 | -9.07318 | -47.15671 | 2025-06-02 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c02713e1-b4c7-3499-8c4f-685881193ca4 | -8.3339 | -47.09438 | 2025-06-02 03:49:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46d962df-d39f-300e-b8b5-f6dbadc3fb50 | -7.8836 | -46.22438 | 2025-06-02 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c25a19d-59d7-3c8d-9ff4-53fba3dd6634 | -9.39509 | -40.35903 | 2025-06-02 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 3c5fff9c-4bd4-37c4-9c0d-5443c3543f7d | -10.46663 | -47.94842 | 2025-06-02 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8a758312-59be-3cb9-b124-b6f0774eb702 | -9.56891 | -40.77479 | 2025-06-02 03:49:00 | NOAA-21 | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5fcc2c30-8b88-3785-a0d8-e4bed928c0f6 | -9.78347 | -36.99405 | 2025-06-02 03:49:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0dab6f15-5348-3037-89f8-c5e4aa618bae | -9.78293 | -36.99754 | 2025-06-02 03:49:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4e760e4b-ab8a-3890-80fc-02560f511948 | -13.08823 | -45.26675 | 2025-06-02 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 316bcde0-0959-3571-86f8-dd547f918a7a | -10.46589 | -47.95224 | 2025-06-02 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1f7d15c0-abef-3105-8438-4660c85e28eb | -13.10256 | -45.26468 | 2025-06-02 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3109a588-a4d5-305d-9243-8473f05a70fc | -9.33775 | -47.08516 | 2025-06-02 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62c40e28-0510-375f-a6bf-3635fcb85273 | -7.883 | -46.22769 | 2025-06-02 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8f2127a-0cf1-3bb4-b162-1bc13a202631 | -9.11816 | -47.64465 | 2025-06-02 03:49:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 73378076-3b86-3a56-bf63-97326d753af9 | -10.46889 | -47.94957 | 2025-06-02 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ff5e55e1-5a53-34f7-9d5e-c22b66220f67 | -9.40218 | -40.36019 | 2025-06-02 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 3bfd4b53-c69f-3759-8fbb-ca5c3d99d05b | -17.3041 | -42.643 | 2025-06-02 03:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 2db422a7-e759-3444-99c7-4fbb17a1fd64 | -18.68403 | -47.00052 | 2025-06-02 03:51:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ec37a44-4da4-32a2-954a-f9358bb7659b | -17.75159 | -42.89412 | 2025-06-02 03:51:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df6c3253-7772-3228-9bd2-3df1b395ebfe | -17.29144 | -42.65744 | 2025-06-02 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| c0da4081-6744-30e5-9342-8526e1210d3e | -17.74796 | -42.8935 | 2025-06-02 03:51:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a54b438b-b91c-34fa-b154-dfd27a742630 | -17.28859 | -42.65241 | 2025-06-02 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 598a71ef-66cb-3662-952d-a2d0f12197f8 | -20.0854 | -50.98137 | 2025-06-02 03:51:00 | NOAA-21 | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2da3056f-bcda-3303-ac66-e035c1f0841c | -17.62497 | -50.91475 | 2025-06-02 03:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35029e29-52ce-3773-a5dc-d53d87ddb60f | -17.25755 | -42.66021 | 2025-06-02 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README3.md)
