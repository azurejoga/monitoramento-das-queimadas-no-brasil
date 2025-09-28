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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d567bbdc-da23-3425-822f-a8f7bc40bd4e | -4.48519 | -43.61283 | 2025-09-28 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 192a1812-82da-345b-9387-3466ff7f1619 | -5.80584 | -42.84042 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 27c0d17e-0f40-3f9b-a287-9f1988a96671 | -5.80328 | -42.85705 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ca8589a8-57ef-33a5-9ad3-1bbdb63e94bd | -4.95823 | -46.80504 | 2025-09-28 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b15e3f4-5a50-3f60-aeea-f144c4e5e1ea | -5.81942 | -42.63011 | 2025-09-28 04:23:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2bb62c40-eb63-3e11-8770-c1a6f7f2d6fa | -1.62605 | -55.17295 | 2025-09-28 04:23:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01bbbfaf-5089-354c-8f33-0886f0e34d56 | -5.71458 | -42.65504 | 2025-09-28 04:23:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 69ee48be-d91b-357e-9891-6dd7e4ac030c | -5.51507 | -42.73558 | 2025-09-28 04:23:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7a5a9318-60b9-37a7-91c1-1521b0fe8956 | -5.93917 | -40.25019 | 2025-09-28 04:23:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d48717dc-5dc5-3e6d-959f-86644a123a02 | -5.4586 | -41.08591 | 2025-09-28 04:23:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 460ca68a-89bf-31ab-b5ce-ac469c108583 | -2.65146 | -48.79918 | 2025-09-28 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe50016f-b7a4-38d9-8074-2c5c96e220dc | -3.08336 | -47.84897 | 2025-09-28 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83fea5ad-3269-347b-a357-b82946fde8e0 | -3.20865 | -51.27302 | 2025-09-28 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9e53665c-7156-388d-9040-ded81c23f1bf | -2.9689 | -49.23136 | 2025-09-28 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ad8164c-b152-399c-8848-3fde734fe3d0 | -5.74277 | -42.89033 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b6032a63-ebc5-3b4a-95f2-56039097cb9f | -5.33595 | -45.64058 | 2025-09-28 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b289c89-6967-30fe-8f71-9bb2a0e8180c | -3.7345 | -49.44024 | 2025-09-28 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff0da555-8343-3a49-9a55-a24dd129ee03 | -5.29532 | -43.14862 | 2025-09-28 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 65815cd7-cbce-310e-b7ea-27f546c0299b | -5.4631 | -41.0831 | 2025-09-28 04:23:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1201f05b-518b-332c-bb47-f7975f3f069b | -3.80589 | -41.57347 | 2025-09-28 04:23:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a108f646-575c-311d-8cab-18fc5eb21884 | -3.80281 | -41.56828 | 2025-09-28 04:23:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| c4cd303d-35b4-3ca3-91bc-6f9a26d8a8d6 | -5.18514 | -45.38972 | 2025-09-28 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 084ae52e-7977-3600-b3b3-283f646d61c3 | -2.93225 | -48.01837 | 2025-09-28 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc3834de-b57e-31d4-96ce-9cf0c840c7c2 | -4.87376 | -45.85756 | 2025-09-28 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f401877e-58e3-307b-9eec-dfde22d5b2c8 | -4.80965 | -42.80238 | 2025-09-28 04:23:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d65d196e-a9b4-3e15-a3ae-fd131dcdb100 | -5.61224 | -43.36826 | 2025-09-28 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cfb41e34-0f3b-3b60-8df7-cb14fe5bd96b | -5.28762 | -43.15152 | 2025-09-28 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 84c689ec-1b2a-30d2-98ef-57ae505e85d4 | -4.8592 | -45.75642 | 2025-09-28 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a69fbb3d-085c-3b95-b308-9495e39aeeea | -4.44431 | -43.98671 | 2025-09-28 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55109a35-e44d-3ea2-bc31-f3a7e157b5b1 | -5.29471 | -43.15261 | 2025-09-28 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7931ad38-504a-3b70-bb02-f2393b800d99 | -2.85249 | -40.46341 | 2025-09-28 04:23:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7b6f5e91-8445-3551-9a04-60dc5268cbdd | -3.78945 | -48.87016 | 2025-09-28 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81fe03a5-8917-3d34-8b0a-38f9c4ffcf8a | -5.69958 | -42.63084 | 2025-09-28 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2bcc8d51-a5f0-3248-b4ca-def10b4c354e | -5.73215 | -42.66226 | 2025-09-28 04:23:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a9133d52-27cd-38aa-b94d-91856751a60d | -5.70155 | -42.61787 | 2025-09-28 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 086a4f76-4ffa-312f-bd8b-38a0abd4b45f | -4.15351 | -40.00071 | 2025-09-28 04:23:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4634fcfd-5e1e-3077-ac84-2d504053e2a4 | -3.80339 | -47.58358 | 2025-09-28 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 726bc52c-cce0-367a-843b-debeed162ff8 | -4.26311 | -48.5526 | 2025-09-28 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6e3f21a-c9cc-3b4a-9930-59cc20b2b5e0 | -2.58382 | -48.40582 | 2025-09-28 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 2a15187c-7c75-3440-bcf0-ec44cde07c85 | -5.10396 | -46.07719 | 2025-09-28 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc0ab72b-ac91-3189-978c-083237ccd373 | -2.98159 | -49.54166 | 2025-09-28 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d1a9059-b4d7-3d80-a0a3-c8fc37345151 | -5.53213 | -44.27109 | 2025-09-28 04:23:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cdddfd55-8d89-358d-8432-e70e90b2d443 | -3.17419 | -48.59533 | 2025-09-28 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 153809fc-3da2-3b3b-b271-f4370838c968 | -5.37504 | -42.30297 | 2025-09-28 04:23:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4f8be061-3522-3a4d-851d-6832b1098739 | -3.59721 | -48.8794 | 2025-09-28 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4cd1d8ce-f4fc-321f-b6a6-4c26b8c2dd31 | -5.2306 | -35.60314 | 2025-09-28 04:23:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 563a019e-334c-37de-a731-3266c41b3f58 | -5.08685 | -42.97429 | 2025-09-28 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af9d6464-9927-3959-8a8c-7c60ad7b40f1 | -5.76991 | -42.88179 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e073085a-bf18-317e-9bf1-7c0c4101aabf | -5.62341 | -43.36596 | 2025-09-28 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 00c552a7-50f7-39d1-a150-ad8318e18263 | -4.18095 | -38.1183 | 2025-09-28 04:23:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 53ad7e70-a05a-3e0a-869a-dae5d65c17d7 | -5.75845 | -42.8843 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 306cb72c-bf3d-3d96-832e-8f2aa09882fc | -5.18609 | -43.72061 | 2025-09-28 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2181ce8d-d04d-3ddb-910a-3bc16e4e0595 | -5.07569 | -44.85455 | 2025-09-28 04:23:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0eaecc03-c625-3e3c-9a28-7c16d61432b7 | -5.18736 | -39.30711 | 2025-09-28 04:23:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 98bdff32-5f8a-3c20-a5d5-bd500373f4c3 | -3.8066 | -41.56886 | 2025-09-28 04:23:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aed3381b-7334-345f-882a-256f7dc8aaee | -5.38902 | -37.29361 | 2025-09-28 04:23:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 91d2b370-3bd3-38a4-841e-adad83dd98db | -3.8021 | -41.5729 | 2025-09-28 04:23:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| ce0dae8a-60e6-3381-9eaa-57cb6bd3d9c2 | -5.19358 | -43.7179 | 2025-09-28 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7dac61b7-213a-3e55-89ca-72c6197992fe | -5.85367 | -42.57795 | 2025-09-28 04:23:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5adb630a-0b5d-3d83-9bdd-3681b1499a61 | -2.70073 | -49.11948 | 2025-09-28 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc049f0c-e799-3736-a99b-043c71b46840 | -5.70662 | -42.65823 | 2025-09-28 04:23:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 500453b6-15b1-361d-8520-e8dd04ff737f | -5.69227 | -42.62972 | 2025-09-28 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4ec9a9d8-576b-3291-85f6-eef4db35d90e | -3.32262 | -52.54245 | 2025-09-28 04:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 78141bb7-abf0-38fb-8643-a019d4c4c649 | -5.32093 | -42.76369 | 2025-09-28 04:23:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 1517d986-7366-3061-b36b-fedfb86dd61b | -5.28933 | -43.16405 | 2025-09-28 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| be93105d-b65b-30c4-83e8-9e245a15aecf | -5.72851 | -42.66159 | 2025-09-28 04:23:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5bdd995c-b1ad-32d3-94c7-82ba55cd2db4 | -5.62693 | -43.36648 | 2025-09-28 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9c7a6493-8b67-3bce-a6cf-3b92d2378821 | -4.26183 | -44.95348 | 2025-09-28 04:23:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6389081-711e-334d-876e-337eaeda24e5 | -4.77622 | -41.04986 | 2025-09-28 04:23:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cd72d79f-0305-3e99-bbe3-e5e97cca50c8 | -5.08949 | -37.60586 | 2025-09-28 04:23:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c4bbd621-ece2-36c2-8607-f1543599c7e8 | -5.05071 | -45.31513 | 2025-09-28 04:23:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6d3ba15-4547-30de-9d6e-34bae2544b27 | -5.19704 | -43.71844 | 2025-09-28 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fcc5216b-f12c-3bce-8a23-49949d7400ae | -5.31794 | -42.75894 | 2025-09-28 04:23:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 5b33c002-6a45-3fd6-9c2b-3d5224da28c7 | -4.19204 | -46.259 | 2025-09-28 04:23:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ba81310-49fa-35ca-b2e7-aa37ae258cd7 | -5.7009 | -42.62217 | 2025-09-28 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9c8e3556-ac79-3956-bc80-d7021f0a441d | -3.86402 | -40.45663 | 2025-09-28 04:23:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e04b542f-299e-322b-89f3-c868b3a02ba1 | -4.87272 | -42.95619 | 2025-09-28 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 1f858640-ba71-3069-9a4a-c116c30386c7 | -5.76566 | -42.88547 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 79c9b87a-0d19-341d-b02d-5d96df4a8843 | -3.02893 | -50.43951 | 2025-09-28 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8c70b08-e7de-3475-b96a-481593ffe7bc | -4.5338 | -48.64614 | 2025-09-28 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2f92b69-b27a-3c5f-971d-16739071e099 | -4.62226 | -43.10454 | 2025-09-28 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df54148e-b6a5-34f5-9640-5ffa6ef21292 | -5.2941 | -43.15661 | 2025-09-28 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e1b46719-2113-3362-9786-7da97411bb8e | -3.64421 | -48.32373 | 2025-09-28 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c243748a-c6ea-3bec-9f8c-fb72ba71188a | -5.22243 | -44.63343 | 2025-09-28 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40323528-e59b-3bd2-bcf3-3b3d37b92e6d | -5.36567 | -42.31498 | 2025-09-28 04:23:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e48fd514-f5fd-3dda-86d1-3c4d9be5d42a | -5.76631 | -42.88122 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ca2cc5ca-d801-384a-9308-fcce8545e2a4 | -4.92017 | -48.16208 | 2025-09-28 04:23:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57b1828b-0062-3302-8661-351fefb4a3d7 | -4.12817 | -44.22037 | 2025-09-28 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae43ac0a-888f-3612-bfe7-9fcdb728b1c2 | -5.37438 | -42.30735 | 2025-09-28 04:23:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 999ad591-f053-3230-849f-b5156b55e70f | -4.25048 | -47.5731 | 2025-09-28 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af9248dd-d81a-3ba9-8ac4-ffc478b6b524 | -5.19416 | -43.71415 | 2025-09-28 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 46b800bd-5712-3c21-a663-0b6acb3af332 | -4.44585 | -40.97997 | 2025-09-28 04:23:00 | NOAA-20 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 021f4a4d-b3b7-353a-aeca-308d6f6c53d8 | -5.41241 | -42.2815 | 2025-09-28 04:23:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c63ef4f5-d0bd-3574-9a67-0c1eab0aaa87 | -8.04966 | -47.95752 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 702c7ab1-7c54-334d-8344-caa314b1aeb1 | -11.98557 | -47.04162 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a3000938-2720-3296-8624-76b3ed5a90bc | -12.95638 | -46.38205 | 2025-09-28 04:25:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cc2ce42-2452-3c31-bad7-6db679d73ed6 | -8.7208 | -47.98028 | 2025-09-28 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2675bf21-e0ec-3576-9440-8910778b4082 | -11.62385 | -52.85977 | 2025-09-28 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 730783ca-7b5b-30a8-9ee4-003e031d7c2e | -11.62518 | -52.85228 | 2025-09-28 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7addbf6d-e798-3a86-81c0-09d737113734 | -5.77481 | -43.83506 | 2025-09-28 04:25:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README55.md)
