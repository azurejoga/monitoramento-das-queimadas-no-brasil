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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b038d80d-de20-303f-9e02-a8102192bdc9 | -5.80641 | -43.07825 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 46189c7e-87f1-3a0c-9289-66be516adc3e | -5.80548 | -43.94544 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d32809db-ba11-3034-97a7-5fae6329cdd5 | -10.79027 | -47.66994 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4fd1b22-b27b-3ae8-8b33-99a419a2add0 | -6.26054 | -43.90637 | 2025-10-17 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 81595788-37da-3b3d-951b-235aa18a37b4 | -6.39952 | -42.54556 | 2025-10-17 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 39541229-fcc9-358d-b10e-99368592d601 | -10.23435 | -49.86923 | 2025-10-17 04:19:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a244b5e-620d-3ff8-b1c7-c9da6bff4d01 | -5.40777 | -47.7873 | 2025-10-17 04:19:00 | NOAA-21 | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbdcc460-952e-3d17-864a-41c3c8cd81cb | -6.54013 | -41.4813 | 2025-10-17 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 40a8ee90-fd40-3b38-8892-6cb652a46491 | -9.08288 | -48.02809 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 518679aa-a609-37d4-b3bb-02ebf407c7cd | -10.13759 | -44.56716 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ba70777-799d-3724-9131-9a120b8f7102 | -6.92661 | -44.08546 | 2025-10-17 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed9c5dc4-4ecf-3448-a78b-be3d76781a10 | -5.59775 | -50.05715 | 2025-10-17 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0bd1fe62-8291-378b-8d50-7c2d7d7a9221 | -4.93393 | -41.54097 | 2025-10-17 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3fc41cdd-d7bf-359f-a8bd-838b097a35ac | -9.70237 | -44.56769 | 2025-10-17 04:19:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5f43e81c-a686-33da-831b-d9ca4bef19fb | -10.2774 | -44.03148 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1954f0b2-ac1f-3649-aeea-25ea674197bf | -6.70464 | -44.39873 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3dc5f173-943f-3ba6-8603-6ddb07902b8b | -6.35544 | -41.48516 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 68fe819b-58a3-3b48-93a2-49bbe87e5f74 | -5.25834 | -50.98278 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56fde324-ba88-3cd6-a001-20a4397d0a8a | -8.22583 | -43.31223 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cffbc924-c63a-3c6d-9f2d-f79c9802c953 | -3.51627 | -52.49211 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 73b800f5-f6eb-318b-80ae-1cdd0d5c69d5 | -4.04248 | -47.50182 | 2025-10-17 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b03f95d5-0209-348d-b91c-3a2fb909ee67 | -7.34969 | -43.85795 | 2025-10-17 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 2c085f60-8892-39c1-bd04-eac6a2ff86db | -10.10129 | -47.64727 | 2025-10-17 04:19:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 663958f3-3571-3724-a22f-c96a747adbf9 | -6.95812 | -47.72016 | 2025-10-17 04:19:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02fffdfd-1e95-3b93-88b8-59a92044e13b | -4.64286 | -42.51315 | 2025-10-17 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 947bbb33-c322-3fd3-a0d7-3c21af31b632 | -10.50559 | -43.42718 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| e63197fb-704e-32d3-a283-5e4548be10a4 | -4.50139 | -47.28844 | 2025-10-17 04:19:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d56b1501-0655-35ee-999c-6c13a892e4d3 | -7.66727 | -45.63598 | 2025-10-17 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94ef1aeb-ceb1-371e-9135-b13760f86751 | -5.3812 | -42.79949 | 2025-10-17 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 455ddd91-0f01-365b-b374-3bc9ffe3f397 | -4.95283 | -44.958 | 2025-10-17 04:19:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1bd16b65-c7ef-3745-9725-8c0f5bb085dc | -7.35551 | -41.90916 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2b201131-58d5-3c5c-9b1e-0c2132466622 | -5.8142 | -42.33435 | 2025-10-17 04:19:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7687b08d-2c9d-3616-95f2-4c0aded05c1e | -5.84709 | -43.87387 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6adfed91-0c59-35b8-aa0a-716a053c09fb | -4.25595 | -48.56434 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e397d75a-5cd6-3a8e-b2ec-282826147385 | -11.48589 | -44.20065 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ddf268a6-c0ad-36a6-9f73-15f050852732 | -6.58636 | -43.93267 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 73c118db-f397-3966-93bb-efd0d8a1de49 | -5.24492 | -50.95326 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f0da9ce-c6ba-39e9-a0c4-f23fe5a23b23 | -7.33071 | -44.15641 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4864d49e-ff70-327d-a58d-c0fa3ca80a7a | -10.53485 | -44.50547 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e9179f63-4d4f-3b7b-9cee-9a0233f13a8c | -5.16773 | -45.21282 | 2025-10-17 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe981f59-c584-3f92-96ac-d61a16bd0317 | -11.01435 | -47.35463 | 2025-10-17 04:19:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ad29f4f-10ea-3751-a38a-cda2298ed52f | -11.469 | -44.19801 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb149071-57a8-3d86-9039-a405f70c55d0 | -5.60901 | -42.68898 | 2025-10-17 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 07535573-e73c-3e69-bb16-00da6f081c66 | -10.2965 | -44.04181 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 2cd7a28c-35f8-3acc-888c-659da97fdde7 | -8.2533 | -44.01996 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aeacb3c3-4b6c-3709-b80a-82d31e429b47 | -9.88993 | -47.67148 | 2025-10-17 04:19:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7f438be-9bd5-39b6-8f95-5d3fc2e95a14 | -10.0583 | -43.83721 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b279a56d-777e-33a6-b82e-114b80ee971c | -5.58754 | -44.75108 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1454f2e4-343b-3fdd-81ee-d6b9f67c70ce | -8.56373 | -44.58549 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a6920cc-91ef-3473-8901-f20fba6e16be | -9.04001 | -40.57548 | 2025-10-17 04:19:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| daca39b1-0df9-3885-a1a2-70a671803881 | -7.48053 | -42.74697 | 2025-10-17 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 96ba73b0-d95e-3c9d-8cd2-9ffc6ae47292 | -5.60039 | -46.3808 | 2025-10-17 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d032cf93-84b0-3490-80d3-e6eee925d0bf | -7.28353 | -41.95251 | 2025-10-17 04:19:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d347ca2d-5a38-3804-be73-87be77396d20 | -7.09328 | -44.26138 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85350d75-9082-34f8-ba11-4c8c484d9827 | -9.139 | -46.63829 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| ac39e296-3505-36d3-8b8a-cca8e39c853e | -5.7257 | -43.82319 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54c8db9b-bdb8-3e71-b9db-9363b5699fd6 | -9.13507 | -46.64135 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc6273d1-5026-35df-b9ce-06743cd6a7e0 | -10.60485 | -47.40528 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 771e4cab-9868-3aa0-9d21-433775fbfc89 | -6.9707 | -45.30729 | 2025-10-17 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e348b711-d0b9-34ec-80c8-818508b71467 | -10.28918 | -44.02197 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0d879209-6e64-30ec-8e56-878cf29af2a9 | -4.14501 | -47.65754 | 2025-10-17 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9905bb61-004f-373b-a2fd-5f90cd8c388d | -5.17565 | -42.93438 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38b5c7fb-ce4d-32dd-aa50-e32b44907057 | -9.17641 | -46.74062 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acb969e0-3a51-3c56-9e2c-1fed47fab3ab | -5.88722 | -43.90152 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1081483b-9300-312b-b85d-f3faebb4683e | -5.78975 | -42.49601 | 2025-10-17 04:19:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 91e19e09-80b4-3579-a92b-60eddb568f5a | -9.1345 | -46.64497 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 88a95fc8-1b4b-3386-9800-44abbe497ac8 | -9.07761 | -45.91011 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7716a91-1e54-3afa-a8e6-840252416d8a | -8.27865 | -43.36116 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0ac265ca-7a0d-30aa-afd6-9a218eead4f9 | -10.58545 | -47.41735 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87681ffa-91fa-3bd8-be49-5331081604ea | -8.98434 | -45.35646 | 2025-10-17 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c01cc148-b5ac-3754-a52a-064b364539e0 | -6.16543 | -41.7084 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 952d6aa6-431a-308e-93ac-5ebe6445eb6e | -5.32797 | -42.92058 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9fa735c3-129d-3cde-af21-6e792098f913 | -6.47901 | -44.55713 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96ff0b0e-dd83-3b6f-9303-0029b27bd039 | -5.83497 | -40.81606 | 2025-10-17 04:19:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 69ad59a7-6627-345f-8341-65924f7996e7 | -6.97041 | -42.20498 | 2025-10-17 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ad755f00-427f-3b10-a620-6c8a0454b26f | -9.43414 | -47.90104 | 2025-10-17 04:19:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46ed9f7e-d152-30eb-ab67-ca6665da511b | -6.76522 | -42.38166 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9efdc81f-7833-334b-a11a-e4ff5b79e9db | -11.39531 | -44.20534 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0bb9fe52-bf32-317e-9604-f7cef17df17b | -10.26675 | -44.03355 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1dc00c26-60a1-3dba-956a-706321df5114 | -8.21545 | -43.97787 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a2e0679-c19e-34ce-8454-064d75a31970 | -6.22336 | -44.14565 | 2025-10-17 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6715565-5adb-348b-bc36-1b0f23b414f6 | -11.07397 | -45.85409 | 2025-10-17 04:19:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f3b13a96-6c9f-3ef2-9186-ea58aef55ba2 | -9.16068 | -41.05267 | 2025-10-17 04:19:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 1c0b7ee3-0578-30d9-99d9-48197bbac3d7 | -5.88064 | -44.83651 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 511fafc0-2ae0-3aaa-8915-10711878500f | -6.49313 | -46.59675 | 2025-10-17 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6b89699-6802-3e55-b410-1531c1fc65cf | -5.23325 | -42.00406 | 2025-10-17 04:19:00 | NOAA-21 | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1370c4e3-3f91-3a89-9126-71e98cab17d9 | -5.96616 | -43.17217 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c0633b85-182f-38c8-ae2e-7087b3e6d6ae | -8.33539 | -46.2338 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41e20455-1049-326f-815f-bb3467194611 | -6.77462 | -46.94449 | 2025-10-17 04:19:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7146745-7739-3d5d-b5b0-4cb3cfb9e42d | -10.27234 | -44.01939 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f61a50e3-6696-35e9-bedf-ba9947cb3bdc | -8.19045 | -42.35509 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dd6586bc-59fb-339d-8133-544677a70aa3 | -8.19397 | -42.35561 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0c4a4981-3e01-3547-977b-ac2f533a46b6 | -11.40341 | -44.1048 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b3755e68-22d0-3d76-beea-d6e872d3e688 | -8.26149 | -44.07528 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8b82a63f-4c77-358c-8970-630326a91c62 | -7.17032 | -42.50702 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cc1266de-bd35-3c19-97e0-03f520848a7d | -7.13698 | -43.78152 | 2025-10-17 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5da69000-7629-3350-8f1a-a61bd93e9335 | -7.11517 | -44.73211 | 2025-10-17 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cf8bfd5-f6cb-3432-8407-8b2a06595ed9 | -8.30475 | -43.44009 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fe85707d-83a9-3a9a-a058-42b4b4da5b0f | -8.39984 | -46.23341 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c5dabae-8bc7-3f8e-a6e9-10cff0898d23 | -10.43503 | -45.02121 | 2025-10-17 04:19:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |


[Clique aqui para ver as próximas entradas](README39.md)
