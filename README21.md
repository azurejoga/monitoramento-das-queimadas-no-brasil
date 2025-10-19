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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12105f41-8d2d-37f5-8be7-af8062a00172 | -4.59236 | -46.51929 | 2025-10-19 04:10:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f0e3a24-6e41-3c15-98a5-aaa7397153c7 | -6.22893 | -44.13774 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b9513e15-598b-37ff-b749-5447c41641ab | -5.7128 | -46.45344 | 2025-10-19 04:10:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2f0c5230-6021-3212-8331-d18e9840de7e | -4.25163 | -40.35047 | 2025-10-19 04:10:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3faabe6d-d801-3445-8538-6d04c9b1a508 | -6.23483 | -44.14145 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e10c442f-582a-3355-8fc8-36e42ddaabb0 | -6.01621 | -42.76062 | 2025-10-19 04:10:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 23086080-a614-3c1c-890f-fb4387d5ca96 | -5.3005 | -45.08245 | 2025-10-19 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9b3562b5-909c-32d4-9827-e365b5def540 | -7.48154 | -42.18058 | 2025-10-19 04:10:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 634e8540-db1f-3174-b815-058532755eb0 | -3.64701 | -49.9709 | 2025-10-19 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93a94af0-f998-338a-be18-34b1565fce15 | -5.32757 | -47.47586 | 2025-10-19 04:10:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55b9679a-7142-307b-ab18-8da5ba700857 | -5.08745 | -47.18561 | 2025-10-19 04:10:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db3ed8c6-9326-3d0a-813e-c77d8247befa | -4.23837 | -44.6781 | 2025-10-19 04:10:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e2e2f91-afd3-311d-87ae-1698e8289341 | -4.5851 | -45.6439 | 2025-10-19 04:10:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c23106d-7a20-32c0-bd9d-0393697e0672 | -1.66657 | -46.76756 | 2025-10-19 04:10:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 393cd7f0-6019-37cc-9802-4162c73aaa46 | -4.76301 | -50.69588 | 2025-10-19 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b10c3b47-0087-33b9-a164-81edcc5616af | -5.49853 | -45.9281 | 2025-10-19 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b12e7424-82f2-35de-9cab-fa8eed303a4f | -6.37949 | -45.76041 | 2025-10-19 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 1eeded26-6979-3fa0-9764-b1f0d8743915 | -7.8406 | -41.74922 | 2025-10-19 04:10:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1a507eed-f163-3222-a189-4071be25be79 | -4.29125 | -45.47994 | 2025-10-19 04:10:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68fb260d-b590-3755-97f8-69d069a727b9 | -2.69437 | -49.5495 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ee181130-5940-3031-a662-b6a26c4a0003 | -5.37127 | -42.79932 | 2025-10-19 04:10:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b1f72764-4313-3b11-9537-3618a56b4c1d | -2.78935 | -49.65419 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0c0438aa-6201-3f56-8b9c-ff274bb547a8 | -5.10321 | -39.40508 | 2025-10-19 04:10:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4d5d816f-7ac7-37c9-b45e-8a57785894d1 | -3.59008 | -43.04364 | 2025-10-19 04:10:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 868ac350-ad7f-364c-9e0c-744858ae73a4 | -4.85361 | -44.5962 | 2025-10-19 04:10:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 68233f06-1db7-3485-83b7-9ed1a95b6977 | -5.99082 | -42.7896 | 2025-10-19 04:10:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 65ad8eb0-39cb-3898-be83-76f2119befcb | -4.41628 | -43.96851 | 2025-10-19 04:10:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0559979c-4814-3c6a-93e5-414c400d1d36 | -4.19279 | -45.79038 | 2025-10-19 04:10:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f973d524-132d-358d-af00-36ee0047ccc4 | -4.91489 | -45.41381 | 2025-10-19 04:10:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d28e7d9-811e-32ff-ac7c-bc410e4bafb5 | -5.49531 | -41.22213 | 2025-10-19 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0ef3c8d0-43c0-33a4-86ab-751c231ae4e0 | -6.02025 | -41.92338 | 2025-10-19 04:10:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fe081e6d-13f2-3559-ba7e-a5e33c159f03 | -5.27106 | -44.8195 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34047302-6c95-30a3-b5c0-935705f95b29 | -7.15715 | -42.37246 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cedf4de5-0499-313b-bb3f-f5f3702c5cb3 | -6.23994 | -44.15442 | 2025-10-19 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 94479bea-8824-3fe2-b6b7-2c22ef2d844b | -6.36877 | -45.75365 | 2025-10-19 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 714eebf8-17af-3049-a647-db58a7e40bde | -3.60886 | -42.85836 | 2025-10-19 04:10:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd99e9c6-d81d-3ea3-b870-e03468ab2000 | -4.26271 | -48.55019 | 2025-10-19 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c90bcea0-9e14-3ec7-bc5e-54ca843aec90 | -8.60461 | -38.84951 | 2025-10-19 04:10:00 | NPP-375D | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4a2d607c-c52a-3ede-bb11-e2c8a0f9d400 | -5.46483 | -44.88774 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 246fc073-43ed-3d65-9345-c975cea824ce | -7.4141 | -40.07124 | 2025-10-19 04:10:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ab3bf4b3-b6f1-3ecc-a815-2039393e058b | -6.37556 | -38.4076 | 2025-10-19 04:10:00 | NPP-375D | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7557b4e2-f433-31af-a448-f567501da50f | -4.41307 | -49.76085 | 2025-10-19 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae396aa9-7999-3dc3-b52f-4ccff4c98129 | -5.23706 | -50.95597 | 2025-10-19 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9eedc67f-1985-3048-9898-306f0652d379 | -2.65038 | -49.52256 | 2025-10-19 04:10:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0404aece-7d3c-3623-bad5-fb5692b3ee40 | -5.36313 | -44.94075 | 2025-10-19 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46fe1df4-ca3c-3d89-8d76-10285adcb633 | -4.77202 | -45.89181 | 2025-10-19 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7f88a905-76a2-3d81-b601-d6e858aa953d | -7.31377 | -42.46965 | 2025-10-19 04:10:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1d7340c3-0c68-3248-a471-b8f396f7e347 | -5.4641 | -44.89212 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48a11fb9-3fe6-382d-b935-c1919e4cc1e8 | -2.97981 | -50.30744 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2dab86b3-c388-31e9-92f0-3e4eab936686 | -4.56522 | -46.50371 | 2025-10-19 04:10:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8acccca-29a0-355b-8dc5-c0ddfa445f7f | -7.2448 | -44.21445 | 2025-10-19 04:10:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc9719ca-e68a-358c-ad8a-081aef18291a | -7.18281 | -39.66655 | 2025-10-19 04:10:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5c1344f4-fc0e-345a-880a-841b595d12fe | -5.8573 | -43.1859 | 2025-10-19 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 96cdb014-7bd2-39f4-9187-214f58b9d2ee | -6.35801 | -45.74722 | 2025-10-19 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 384da787-ec79-3491-a985-8f2c7ffdd89b | -5.76998 | -42.72944 | 2025-10-19 04:10:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 31379387-e8c7-393d-946f-bffb16d2d59f | -5.85854 | -42.76506 | 2025-10-19 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a6e19ffc-593f-381b-96e4-6ae7ac41c061 | -3.32748 | -45.62378 | 2025-10-19 04:10:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ce4a174-8d8e-3d02-9ec4-7ffc03853704 | -5.46714 | -42.87736 | 2025-10-19 04:10:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9a7946c1-e240-3bb8-8b99-b83a360fad3c | -4.41255 | -49.76392 | 2025-10-19 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 847d9c47-f5c5-3bec-904c-cccd5086f48e | -6.08632 | -46.4574 | 2025-10-19 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 61dff451-eec2-37e2-86b2-b5dfe5b8cb2e | -5.59815 | -50.05582 | 2025-10-19 04:10:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7383cb4d-8ba3-3588-894f-ab9dc83e4415 | -5.12299 | -43.12438 | 2025-10-19 04:10:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7aeb3f1-dadf-3302-9ecf-639a8b49ffb3 | -5.93633 | -42.25747 | 2025-10-19 04:10:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 36f1ac9b-5ff8-3d24-bc1a-2bc74a053a44 | -6.79085 | -46.46931 | 2025-10-19 04:10:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4bdbd6c4-ca89-3c22-97ce-bff444c75642 | -2.99101 | -39.9645 | 2025-10-19 04:10:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bf6f3c43-e5be-3867-9ad1-812370062a91 | -6.18883 | -41.56555 | 2025-10-19 04:10:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d5bbd1b5-8c6f-313e-bbf8-84caa59b6777 | -5.59937 | -46.36178 | 2025-10-19 04:10:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6d87936-3b8e-3d52-a6da-f68530a37f5b | -5.70817 | -46.45624 | 2025-10-19 04:10:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd2e76f2-cd3a-33b3-b84b-5d896f575c1f | -4.23785 | -43.09785 | 2025-10-19 04:10:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11f87e82-2583-3418-b66a-efad75577b9f | -3.97508 | -47.57975 | 2025-10-19 04:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 79798bb6-c133-3c13-bbd0-7078517633ae | -2.43889 | -49.37449 | 2025-10-19 04:10:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 698d5669-99a0-3dfa-9872-b70691586a1b | -4.52951 | -48.41671 | 2025-10-19 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2dcbd70-d9fd-34b6-a35a-76390bc0185f | -3.80093 | -51.94003 | 2025-10-19 04:10:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09314d3a-4d0c-3a5e-8447-13954e29c74b | -5.70863 | -46.50396 | 2025-10-19 04:10:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 855f7846-53aa-37aa-a1bf-66c42f7ba4f4 | -7.31099 | -42.4656 | 2025-10-19 04:10:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3cf7998e-ea0a-3320-a6c1-2ed6b05859bb | -6.55727 | -45.94672 | 2025-10-19 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8dab6c63-9458-3b45-8042-32b985793aa3 | -1.04385 | -47.79208 | 2025-10-19 04:10:00 | NPP-375D | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60292c04-912f-3248-98f2-2aef041a7663 | -4.76273 | -45.41593 | 2025-10-19 04:10:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1b91681-da84-372a-877c-13faf76b4eb7 | -5.49777 | -45.86497 | 2025-10-19 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08c8aef6-24d0-3110-9a2a-efda4a4d3a2b | -4.28595 | -42.9864 | 2025-10-19 04:10:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8747d623-1ba2-3db7-8c0b-b7acc60ef5b8 | -5.87538 | -48.17977 | 2025-10-19 04:10:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8200b827-d384-32af-8ce0-ce2dddbb89ca | -4.0618 | -43.23245 | 2025-10-19 04:10:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c767e45f-aede-3dd4-8a60-31b7b2d0b548 | -6.26 | -44.34293 | 2025-10-19 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a079d238-3a15-351a-af88-e3d544ffdea4 | -3.54782 | -46.43689 | 2025-10-19 04:10:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43c910f2-f8ec-314e-9a8c-b36942f8c15b | -6.26423 | -44.33946 | 2025-10-19 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ea9fe960-7007-3816-a7c6-08cec1403ecb | -2.68806 | -49.55502 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 228df400-6f52-3f40-b93a-efc731f3127c | -4.85728 | -44.59673 | 2025-10-19 04:10:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ca48ee41-986b-3a5d-92bd-3c677fa164a9 | -6.37488 | -38.40838 | 2025-10-19 04:10:00 | NPP-375D | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6c2b4c06-644b-31a9-8552-247e2519af8e | -7.1849 | -42.17617 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e3b5642b-2712-3ad8-97c5-861b811f7629 | -2.65042 | -49.52382 | 2025-10-19 04:10:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15435c67-47da-362a-ac35-b7b28695caf6 | -5.4309 | -42.73104 | 2025-10-19 04:10:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8619cd73-0485-36e2-acc2-1feac60047af | -5.7132 | -43.82177 | 2025-10-19 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 17afcb2b-877b-304d-bbc4-aed029e7f7ec | -5.46278 | -44.88964 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d49e9d3-f2ff-3c08-9106-361f78024441 | -7.4074 | -44.81254 | 2025-10-19 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28c75fdd-acdc-3027-a6ec-1926a538e7e6 | -4.75752 | -50.69501 | 2025-10-19 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2b4b6db-0252-3e23-a151-a511a898f6c5 | -4.26868 | -44.46932 | 2025-10-19 04:10:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a0b25d4d-a323-3369-90bb-71fa758d880e | -7.46537 | -42.74656 | 2025-10-19 04:10:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 30e03590-adfd-3a22-b253-a1a1b00845ff | -4.63253 | -46.53344 | 2025-10-19 04:10:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76fa7985-2779-341e-bbd3-f7bc02057016 | -5.6076 | -42.67747 | 2025-10-19 04:10:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 58dae763-a02b-3e1f-8645-77b1e11effe8 | -7.93909 | -39.8544 | 2025-10-19 04:10:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README22.md)
