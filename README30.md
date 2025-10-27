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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 604c5485-4169-39df-9d16-be347134e277 | -7.05722 | -47.38368 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e5db1f7-aa12-3e45-aa3b-f4e622457fa3 | -3.11411 | -51.21301 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a940b1be-78d3-3651-aa59-cf4e4cf1bc99 | -5.65462 | -41.1001 | 2025-10-27 04:32:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 49326fbe-968b-336f-9b5d-0713b60dc018 | -5.61901 | -51.78995 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 424800c1-7a9a-35bf-b93e-963427c6c999 | -2.87859 | -44.37962 | 2025-10-27 04:32:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b5ca6e83-696e-36c4-a020-532428aaa73b | -6.99828 | -46.99582 | 2025-10-27 04:32:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 154fa2f4-0da2-3de3-bd0e-2eb84bb5e028 | -7.25633 | -44.9646 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc3b2463-a2ad-3400-86df-dd7a3a4bf2cb | -7.62401 | -42.20584 | 2025-10-27 04:32:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5a297e6a-dbc6-3cc0-8dbd-5acb80f1f688 | -3.70462 | -44.33793 | 2025-10-27 04:32:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6de531f-25d7-38e1-a330-3d4b363bd846 | -7.79509 | -45.38264 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3518d99d-0057-34a4-ada1-c7e8bdd5f97f | -4.51777 | -44.0424 | 2025-10-27 04:32:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49f47b0e-10a4-32b3-bf4c-b73ac34ae368 | -6.45627 | -42.33536 | 2025-10-27 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 304e98fc-437c-337b-9644-cc42e1627387 | -2.86632 | -46.76667 | 2025-10-27 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c98bb8d4-6a92-321b-8515-f30237eb81b7 | -7.85664 | -46.47891 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99629e5c-ebed-3c37-b4a6-6d0f20efe275 | -7.13337 | -47.02444 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f2bd268-6d6b-3b00-a57c-f4253287969d | -7.97372 | -45.47229 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e35d1ba2-4241-30f7-aa46-15b5badc8b78 | -4.88792 | -48.4546 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37ba6ce8-ea52-36d8-8c50-41ac1e5010d6 | -4.14577 | -50.68513 | 2025-10-27 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de518291-4132-3b53-b6c2-779c1fa6dada | -6.88677 | -43.57093 | 2025-10-27 04:32:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b519b35b-9bc8-3adc-a673-646fe7cf1f22 | -10.02183 | -47.14262 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f0c2aed-fe5e-39eb-b4d8-f37cb177ab84 | -6.89209 | -45.14906 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f7ef3f59-6131-3968-9edf-aff763fcd337 | -4.73574 | -41.48664 | 2025-10-27 04:32:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e9a6e693-12f4-3a06-bc8d-25b9ce8d571f | -4.22181 | -48.36342 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 932b2264-065f-3b83-8586-ac72c58a56a0 | -9.23316 | -45.83822 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2dddae96-94b6-30f4-a0da-c3aed4a58afc | -4.47235 | -43.42258 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f7812627-016d-3f46-a122-2a8c2645a7c1 | -6.46037 | -42.33618 | 2025-10-27 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1eb1a3c6-1ea5-3ce5-bc5d-59fc1f285657 | -6.17385 | -44.20922 | 2025-10-27 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31a3a5a9-5425-378d-bcf9-c6d89bce09d7 | -8.53082 | -47.20207 | 2025-10-27 04:32:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3c98876-79f8-3644-bb75-53fdae41bce3 | -7.82671 | -46.44847 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c10335fa-a17b-3ff9-9b17-97af3e8821cc | -5.71813 | -49.30824 | 2025-10-27 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e12ecac1-dc3c-3fcb-a63b-67c67b89cb65 | -3.12249 | -51.20947 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 702428fc-e69a-34aa-bb2b-98e52efea833 | -2.63878 | -47.30302 | 2025-10-27 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9c406a39-2f75-3a73-8193-57f50b07ef62 | -9.49322 | -45.81522 | 2025-10-27 04:32:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15e4aa94-7487-3ccd-94c4-e399308f885a | -9.26857 | -45.59979 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 90d4f391-3133-3ac9-b0b0-33ec1d6b96ed | -7.23971 | -44.98399 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52581e1d-4ab2-3b70-b0f9-1dfeab9e7134 | -7.13718 | -46.99989 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7792cf89-1caa-3d71-a442-06640de56ab8 | -6.67546 | -41.51006 | 2025-10-27 04:32:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ddf9f9da-087d-30b5-a635-f2848e414dbd | -4.29517 | -48.07083 | 2025-10-27 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90269f26-b423-3f04-a7b5-a5070457b319 | -5.59233 | -41.31434 | 2025-10-27 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 46107d46-6ac2-3f7e-a505-a0ecd2f54b1b | -3.18569 | -43.34275 | 2025-10-27 04:32:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 955806ca-04c8-331e-a70d-01e408ebfb11 | -7.44284 | -41.87117 | 2025-10-27 04:32:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 773d71ae-f0fd-3834-93f7-74f055050e1f | -6.90175 | -46.14084 | 2025-10-27 04:32:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 56be9791-8e86-3e74-b09c-6196fea25717 | -10.01126 | -47.16687 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7308f5fa-51cb-3bf3-ad36-96d7b01b08be | -9.25972 | -45.61069 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a421c70d-a273-3c00-aa5d-a30a41aa30de | -5.76706 | -45.55365 | 2025-10-27 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 142cb560-8a4d-3353-aa28-4e302c5b8451 | -7.53852 | -46.2663 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0501cb64-b646-36a8-9a02-acbb978d5e7b | -4.48052 | -43.41925 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| cdae687d-10c2-3ae3-b8f1-b446b3da70a9 | -5.53971 | -41.40078 | 2025-10-27 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8a39d060-59b2-3d4d-9b1e-cf895d37530a | -7.84146 | -46.48773 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0b0f6b26-30ab-30b4-bcc0-18667785403a | -6.68047 | -41.50647 | 2025-10-27 04:32:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0d87f077-3d22-3a4c-8d14-c1487fa6f956 | -3.09987 | -51.27854 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b06a31d-80df-3e70-a344-ceab55229f3e | -7.96725 | -45.46756 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 73be9c25-8777-34a5-8634-0c7718865142 | -4.20125 | -48.36383 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4e5a611-cad0-3a11-b00c-47958b8ff1cb | -9.5888 | -44.94785 | 2025-10-27 04:32:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fc84443-c1b9-3524-b033-aca7548a5bd1 | -7.84428 | -46.49186 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c61287b6-7b5f-30a1-b3b2-5c807faf0dc0 | -4.47609 | -43.42318 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| afbfb84f-4c3f-3315-b729-471bda673b73 | -7.44556 | -44.74218 | 2025-10-27 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fae785b-bd95-361a-8d5a-c4b9acca5f45 | -3.47184 | -49.97371 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3582f399-a19a-344e-9215-7c6164560e7f | -7.76344 | -45.40188 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ef7e678-75ce-3a4a-a9a3-54ecf78fd243 | -2.47953 | -49.25762 | 2025-10-27 04:32:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57ef4fe2-36d5-303a-8f54-5271f113b1b1 | -4.31134 | -48.2269 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22ff77b8-8b9f-3da1-a56b-73e31c63bd52 | -4.83515 | -45.33876 | 2025-10-27 04:32:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e8b7d4a-db83-3b66-bccd-1ab0fe1d6911 | -8.56618 | -47.39146 | 2025-10-27 04:32:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfafecb0-25f0-37e0-9442-d8a4c5c05153 | -4.44325 | -43.42982 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5ac722b-f4b1-30dc-b145-aa604bace35c | -4.45864 | -45.45719 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 47.2 |
| a649c64c-225b-3559-9aec-42cb840c7815 | -5.51158 | -41.71484 | 2025-10-27 04:32:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 934f8f4c-119f-36b8-a311-3f048323e828 | -7.80212 | -45.38377 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a2728c7-03d5-3676-b79d-8d25a401c116 | -7.22191 | -46.86884 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3244519a-c5b2-36ac-b8df-b6dd4c1bd6f6 | -8.04339 | -45.15078 | 2025-10-27 04:32:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9008dbca-58e6-3500-a012-22f326d0006a | -3.46894 | -49.96912 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a111e416-18df-3800-8783-06266e92e43c | -3.99753 | -48.31779 | 2025-10-27 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b104483-2801-382f-a570-6fb2608c80ed | -7.80504 | -45.38826 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56e0c102-8b8c-359f-bf05-5a45e699fcee | -7.13168 | -47.01345 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f16c704-b8fa-3279-b5ed-0a8e0b22ad8d | -4.16108 | -51.07743 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e6499b9-55a0-3e43-ab8b-18b343aa7ac3 | -4.32668 | -48.08644 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 691da9b9-8fdb-395d-a0c6-3bed9281b2d9 | -7.02377 | -44.68365 | 2025-10-27 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 07c7584e-73b9-3eeb-9214-44d4213d24ed | -3.09921 | -49.44623 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9758f068-7fb5-3855-8721-eec2eca6c61c | -7.38413 | -46.54332 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af681a1c-84fe-30ab-95a9-7e7670d9b2a2 | -4.447 | -43.4304 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a55617c-91cc-34c1-9542-8977d04d32a4 | -9.86647 | -44.88523 | 2025-10-27 04:32:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 861c1be5-5b8e-3e94-8f3a-877780bb23df | -7.06139 | -44.48144 | 2025-10-27 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c52e0bed-c356-3e9b-b2b0-347f0a9a7404 | -5.53282 | -41.7179 | 2025-10-27 04:32:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 516b5907-edde-3be4-b05c-94386218e3f7 | -4.46044 | -43.42534 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aee313d5-8f51-39cb-ac0d-25bf28609c31 | -7.96671 | -38.28019 | 2025-10-27 04:32:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 823ef971-2e0b-3e67-8bb0-e0c02d67229d | -6.44129 | -42.35184 | 2025-10-27 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1422d1d6-7d4f-35b0-8133-848d5043fcac | -5.60728 | -47.10217 | 2025-10-27 04:32:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 895d55f0-06bc-3248-b557-74317d53c2dd | -8.03768 | -46.73919 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3638953-b5bb-3c6d-9b5c-6ac74a8056b0 | -4.44544 | -43.42309 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54e740dc-c2af-3d4b-be32-2735a6e34cbd | -4.26238 | -40.68423 | 2025-10-27 04:32:00 | NOAA-21 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| eb645983-a8ee-3ac0-b08c-1e1d4da91a65 | -6.14533 | -43.13301 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b2730508-fbf6-37d9-8b22-a99e3e7c5148 | -7.76334 | -46.5127 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 759f1c84-5369-3825-971a-eb9d3c588dfb | -3.9121 | -54.68825 | 2025-10-27 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a172e4f1-7594-367b-a9e0-93e7859022d2 | -7.85608 | -46.48254 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8daf72e5-afd2-3020-89c5-eace7a17ff92 | -4.45954 | -45.45678 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9faf7e04-1988-376c-9e65-3c77c2ac2576 | -2.90281 | -48.98235 | 2025-10-27 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20e2e7e2-bbdc-3eb0-b0b6-f132e03480fa | -3.57101 | -44.52445 | 2025-10-27 04:32:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ed644f27-ff13-315c-85fa-7a9d6bbddf8a | -6.1507 | -42.68964 | 2025-10-27 04:32:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 59ace365-de89-3f02-aa94-ad3c9a60bae5 | -8.74119 | -49.60905 | 2025-10-27 04:32:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92211db8-65e2-319f-bfc3-333c9ceb5afe | -6.13327 | -41.71917 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e70edfac-1282-3074-82f7-94f50c156448 | -7.84484 | -46.48824 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README31.md)
