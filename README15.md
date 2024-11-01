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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2ecc315-cbbc-3a07-8f7f-407392efbf32 | -6.52057 | -35.24884 | 2024-11-01 04:06:00 | NPP-375D | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d0fb920c-6141-3f72-89d3-5e9b67869ced | -8.4043 | -35.30015 | 2024-11-01 04:06:00 | NPP-375D | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 93cb4527-4a2a-3984-9aa0-2be26a50ab42 | -5.78106 | -35.38463 | 2024-11-01 04:06:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6b9689c5-8072-3528-8fab-0c9960dcf453 | -5.7706 | -35.51764 | 2024-11-01 04:06:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 34468447-4052-3bd8-97e8-8c86db352ad6 | -5.64376 | -35.36292 | 2024-11-01 04:06:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bc59649d-30c5-3770-970d-362788d8ff95 | -6.52494 | -35.24955 | 2024-11-01 04:06:00 | NPP-375D | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cb8b31ef-5d2d-3d6d-bf68-2ac13b319163 | -8.9059 | -37.23437 | 2024-11-01 04:06:00 | NPP-375D | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4fea5745-bcfe-3ab2-9f2d-107266e2f962 | -7.00025 | -45.20872 | 2024-11-01 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 657d2be2-f921-3dfb-b661-52c8ee0aa220 | -6.1188 | -43.95611 | 2024-11-01 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8867fb63-0128-3686-9af1-744e5d04738d | -6.10407 | -43.95769 | 2024-11-01 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 295002df-9946-3417-97a5-5ee4d4429604 | -6.12169 | -43.96062 | 2024-11-01 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d388007-9a6f-3afa-a61b-2246f5851149 | -6.12105 | -43.96454 | 2024-11-01 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8349f1ff-42c0-3775-a769-b83dfa8e3cb7 | -6.11816 | -43.96002 | 2024-11-01 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 652fbe38-5490-3290-9e32-37470b6110e6 | -6.10983 | -43.96673 | 2024-11-01 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1fa03fa6-da4d-35f8-bf1e-7ad43cae2274 | -6.1063 | -43.96617 | 2024-11-01 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f0448d8-7723-3e16-a030-5cf8b65719f5 | -6.63328 | -43.78469 | 2024-11-01 04:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb48fd01-4c70-3547-bd0f-b89d668d2632 | -6.62979 | -43.78413 | 2024-11-01 04:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b19ba058-f7eb-346f-9f5e-e6bfb0c420dc | -4.9976 | -38.19686 | 2024-11-01 04:06:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ea8909a6-1bf5-3472-9663-f3f9175506ec | -4.18876 | -38.15604 | 2024-11-01 04:06:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4a66be7d-c6c3-3af4-9b2c-d565824e071e | -5.13779 | -38.08249 | 2024-11-01 04:06:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 10dcfc6d-d0e4-3c80-aa51-a9a14c145bbf | -7.00463 | -38.77334 | 2024-11-01 04:06:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c8cac3ba-ca65-39ed-94b2-c151d9cd9947 | -6.9981 | -38.76835 | 2024-11-01 04:06:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9fd504f8-909b-3d50-a36a-70b01122634c | -6.90868 | -38.46413 | 2024-11-01 04:06:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 373caecc-e26f-3bd9-a068-70ae7d9b4700 | -6.90805 | -38.46829 | 2024-11-01 04:06:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 237d1cec-00af-3507-862e-255c96c0261d | -6.90444 | -38.46772 | 2024-11-01 04:06:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9bd75acc-4c71-37fb-a85d-9e0d02eca9b3 | -6.77442 | -37.54419 | 2024-11-01 04:06:00 | NPP-375D | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 52b76532-6cf8-3828-a93b-5c1cfcf7c397 | -4.98057 | -39.81143 | 2024-11-01 04:06:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1fb52c5f-88f2-3cdf-96e5-a9be946bd780 | -4.9772 | -39.8109 | 2024-11-01 04:06:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5d4d96e3-1849-3a0c-a6ef-157e19ba2c75 | -4.10654 | -38.74067 | 2024-11-01 04:06:00 | NPP-375D | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6dff8acc-b76a-31e1-a8fa-1604d1fe98e1 | -4.10596 | -38.74446 | 2024-11-01 04:06:00 | NPP-375D | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b9121080-108d-3cd5-9954-bacc1d6000ac | -3.79357 | -39.09787 | 2024-11-01 04:06:00 | NPP-375D | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3e037784-b501-3331-9e3f-c31c0e8f1b22 | -3.79016 | -39.09734 | 2024-11-01 04:06:00 | NPP-375D | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 7d39c003-80ee-3d7d-8cb3-de8501f22c6e | -6.38779 | -39.6722 | 2024-11-01 04:06:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5f80eeed-2f48-3dfa-be1e-19bcd0f60b4d | -5.04495 | -40.09026 | 2024-11-01 04:06:00 | NPP-375D | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6d0d7284-78a0-30f0-9667-88f4f252a7ad | -5.67402 | -39.86549 | 2024-11-01 04:06:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5485ddd0-6a77-3afe-bc9f-e6c89221febd | -5.6701 | -39.86847 | 2024-11-01 04:06:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d54bb3b5-eae7-3af6-80c0-4fd1bbf6f7b8 | -6.78997 | -40.23452 | 2024-11-01 04:06:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b8f6ac04-8c27-3fac-a79e-4135e4f1655a | -6.47511 | -39.96516 | 2024-11-01 04:06:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 80a59449-7ee1-332f-9c17-25832d9a2ebf | -6.54631 | -39.66113 | 2024-11-01 04:06:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fed29878-c979-3ac5-bbae-bd4a3d6a5fd3 | -6.54518 | -39.66852 | 2024-11-01 04:06:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2c4cfdc7-5620-3a69-86a5-46fe4cc5022e | -6.62836 | -39.71885 | 2024-11-01 04:06:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 874d25ca-5e12-3a9a-8adb-e0592736aa67 | -6.54575 | -39.66483 | 2024-11-01 04:06:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 91b121b8-345a-399b-bb2c-e347c8693c67 | -6.54233 | -39.66429 | 2024-11-01 04:06:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3b4e5371-fd4b-32af-b13e-90b4294b2797 | -3.51417 | -40.35653 | 2024-11-01 04:06:00 | NPP-375D | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6d1f39f0-eada-3479-bd25-9919a41bfe61 | -3.50546 | -40.75839 | 2024-11-01 04:06:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 83c603bb-76b6-3f93-9a56-1a77a9b0e3e4 | -3.50323 | -40.75098 | 2024-11-01 04:06:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 72c18d48-8e42-36d1-a9e9-0ad22e2da33a | -3.50269 | -40.75443 | 2024-11-01 04:06:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6ce7fe67-3c5f-376a-9a61-484e2b8596ce | -3.50214 | -40.75787 | 2024-11-01 04:06:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1fe5a9b1-48ea-37b4-b929-82e0886c42c9 | -3.49991 | -40.75046 | 2024-11-01 04:06:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f21e61ad-45cb-3cac-a7f4-8f39c0c9d9f1 | -3.03802 | -40.06943 | 2024-11-01 04:06:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 27bb2cea-c723-30a7-a1f2-755cfea9e952 | -2.96077 | -40.24208 | 2024-11-01 04:06:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| efe58684-8dd7-348c-b44e-6cd67365ebb9 | -2.88801 | -39.90676 | 2024-11-01 04:06:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 66111076-e3d6-3f0e-81a1-e2d4f41a9c7c | -4.54267 | -40.46702 | 2024-11-01 04:06:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 966776d3-3eae-3abe-9d79-873259d91d02 | -4.53934 | -40.4665 | 2024-11-01 04:06:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b6c60bac-29ec-3601-8741-30a94b2bb57f | -4.08611 | -40.87386 | 2024-11-01 04:06:00 | NPP-375D | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bead4f8e-c820-360b-8f87-8e0a29ccb695 | -3.85191 | -40.70673 | 2024-11-01 04:06:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ef197318-9f98-3374-9502-92bf5be2302a | -3.85137 | -40.71018 | 2024-11-01 04:06:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 34227b05-cbe4-3524-8164-898f650bcb71 | -3.94292 | -41.48243 | 2024-11-01 04:06:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 81ddc861-963c-3093-b905-d0859172d252 | -6.12015 | -41.81542 | 2024-11-01 04:06:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6b1567a7-5cf2-364d-ba97-8831360f0012 | -6.11683 | -41.81489 | 2024-11-01 04:06:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 03078d54-74b9-344c-95c0-bdce8d6ea9c6 | -6.04367 | -41.80685 | 2024-11-01 04:06:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 980f378d-b80c-3342-a2d7-e3d6eafeeb79 | -6.0409 | -41.80282 | 2024-11-01 04:06:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f11a8b4d-bd9b-35c7-a20f-d53381358ae7 | -6.04034 | -41.80632 | 2024-11-01 04:06:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f874ad78-76d2-36d7-97ad-97265c273bcd | -6.03979 | -41.80982 | 2024-11-01 04:06:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d2222255-7f96-3d44-b7eb-ac6d65bf4537 | -5.58884 | -41.77055 | 2024-11-01 04:06:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 85286551-8bd9-34eb-9899-bc742fde6fca | -5.5055 | -41.65731 | 2024-11-01 04:06:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9a99f8cc-c61d-33a8-b8e5-b81eef5db840 | -5.50218 | -41.65679 | 2024-11-01 04:06:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f164a692-8fbd-300f-bbd8-6047cc61f9e4 | -5.27337 | -41.2412 | 2024-11-01 04:06:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a1f0f34b-fa8b-3357-86d8-e9ae8b0bc71e | -5.27005 | -41.24068 | 2024-11-01 04:06:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 90d3bcbd-5b3b-37fa-a0a0-b385c9dc6ca6 | -5.7557 | -41.76833 | 2024-11-01 04:06:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7dd8d7b8-3df8-3a59-ab59-bde2ca6e57de | -5.75515 | -41.77181 | 2024-11-01 04:06:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| afe293cd-5828-3584-bd76-15ba2c490ce8 | -5.75237 | -41.7678 | 2024-11-01 04:06:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0f69ddb8-6b03-3e8e-a6ef-e195e323255d | -5.71273 | -41.54453 | 2024-11-01 04:06:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0f83782f-b187-3cad-b17a-32185cd30ad5 | -5.61761 | -41.71805 | 2024-11-01 04:06:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2093e777-b515-35da-9ecf-0bd8f991011c | -6.15398 | -41.83858 | 2024-11-01 04:06:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 818bafa0-4399-3bea-8e55-6c753d83436d | -6.1207 | -41.81194 | 2024-11-01 04:06:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1961c824-be82-3035-9072-367143f48a13 | -5.7546 | -41.77528 | 2024-11-01 04:06:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 097ddabb-2e0b-3d3b-bb73-fb51fca9e7f5 | -7.32436 | -41.85993 | 2024-11-01 04:06:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 10c6affd-38a6-3903-a226-dbf0531bff8c | -7.20982 | -42.18116 | 2024-11-01 04:06:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 53b87588-1608-35d5-8680-ea3326014b2d | -7.20649 | -42.18062 | 2024-11-01 04:06:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 10b4dc86-ef52-3541-a80a-5ad60486da60 | -8.39488 | -41.44449 | 2024-11-01 04:06:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 0544e86b-764f-3903-8617-1a1d61ecb648 | -8.39433 | -41.44799 | 2024-11-01 04:06:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 86f7d4e4-b103-3725-884c-ddd84fe2c47b | -8.39101 | -41.44747 | 2024-11-01 04:06:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2fc3c9a4-3e23-3b08-846c-02944462bcd5 | -8.26634 | -41.44215 | 2024-11-01 04:06:00 | NPP-375D | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| afe998ce-72c4-3a8e-8415-a0ef7c2167b9 | -3.39721 | -41.64027 | 2024-11-01 04:06:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a42db770-76bf-31a7-9d63-dd4f44a519f6 | -3.39666 | -41.64378 | 2024-11-01 04:06:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 30164cfd-d106-3f49-b024-c7cde2715e01 | -3.39497 | -41.63274 | 2024-11-01 04:06:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7fc67204-46b5-3f4a-bc9d-d1be3382a239 | -3.39442 | -41.63624 | 2024-11-01 04:06:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 87c89f15-7975-3e84-a1c2-db437fac8739 | -3.39387 | -41.63975 | 2024-11-01 04:06:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 220cb60b-d0b0-3e73-b7dc-bb3283b7d97a | -3.39331 | -41.64325 | 2024-11-01 04:06:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6d0d5c18-05a9-3d53-bb17-f91029f9e7e1 | -3.39276 | -41.64676 | 2024-11-01 04:06:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 170aa6b6-5354-323f-8e67-a79c8cf30cc0 | -3.39107 | -41.63572 | 2024-11-01 04:06:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 72efac8c-816c-3934-8361-cea121c0be4d | -3.36658 | -41.66065 | 2024-11-01 04:06:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d82b3789-a10d-340d-8f6e-702bd2a8b371 | -4.84109 | -42.47335 | 2024-11-01 04:06:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a06d8a9f-2919-316f-ab4d-9d6097ca115e | -4.71804 | -42.65467 | 2024-11-01 04:06:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d7c92321-265a-31d8-8c46-8927a6fc2671 | -5.46577 | -43.17538 | 2024-11-01 04:06:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5b2dfd1-9f7f-3a43-94c5-e202f4ec0ee8 | -3.94612 | -42.63169 | 2024-11-01 04:06:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e0449228-a05a-3378-a54f-4eb1c71de691 | -3.94554 | -42.63534 | 2024-11-01 04:06:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1bd7b467-5396-3e19-a155-0c7a0f0790cc | -3.94519 | -41.51131 | 2024-11-01 04:06:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 25690b9a-2f86-3abc-bc95-384a1ae3877e | -3.94464 | -41.51479 | 2024-11-01 04:06:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |


[Clique aqui para ver as próximas entradas](README16.md)
