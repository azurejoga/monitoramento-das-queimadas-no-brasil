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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b2eb9fa-eb88-3dc5-b718-fc60645f43fd | -10.4937 | -43.4552 | 2025-10-18 13:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 71c8b60b-3981-3ab2-a680-fabe2eb88c47 | -14.09 | -43.6475 | 2025-10-18 13:50:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| c44cd65c-bb0b-39f9-a95f-04a3d93e4b63 | -16.3544 | -41.7551 | 2025-10-18 13:50:00 | GOES-19 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.4 |
| b4e384b3-f9cd-37bd-ae45-edd6dbae81c7 | -11.3767 | -44.3131 | 2025-10-18 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 196.8 |
| 1c5dac72-9920-387a-921f-fe27489ee817 | -13.7108 | -41.464 | 2025-10-18 13:50:00 | GOES-19 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 149.5 |
| 545171ce-04fd-3c16-9f4f-164e75228d23 | -10.2554 | -44.0506 | 2025-10-18 13:50:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| f9f22a90-c1de-370f-948a-77159968d2d0 | -11.3584 | -44.2692 | 2025-10-18 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 1eb36e71-b0ef-3f82-afa4-4cf8ac2cc4c1 | -4.3872 | -43.406 | 2025-10-18 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 9f70a033-64ec-3cdf-9261-b17af0c7ead3 | -11.3776 | -44.2663 | 2025-10-18 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 624.7 |
| 95ddd3b5-c320-3b49-9492-737beffc444c | -10.4945 | -43.4079 | 2025-10-18 13:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| f3ba73f2-8ef7-377e-a661-530bb9c45f7e | -12.1673 | -45.1003 | 2025-10-18 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 188.4 |
| 675e7236-c261-37f6-82de-481c657fee2b | -10.9189 | -45.4171 | 2025-10-18 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 381d41dc-ada9-358f-a1c7-0679b58d011e | -11.3794 | -45.2619 | 2025-10-18 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 463.5 |
| 53d3f5c2-afcc-3689-bf0d-557837f1fe5b | -13.2001 | -46.4312 | 2025-10-18 13:50:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 419f073b-afa5-37fe-b9e6-c805e842300b | -13.2005 | -46.4084 | 2025-10-18 13:50:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 598edb50-9874-3948-beb4-1998d58aa6d4 | -3.7626 | -41.7207 | 2025-10-18 13:50:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| c34f9d4c-db20-3768-a5aa-94bab86e690b | -3.7438 | -41.7456 | 2025-10-18 13:50:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 95.6 |
| 6145654e-d261-3b69-8ad5-7f8ea31ef2f5 | -14.0477 | -44.6957 | 2025-10-18 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 1a8a6ec1-734a-3c3b-b020-72aa3d7931a2 | -4.171 | -42.2215 | 2025-10-18 13:50:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 99.2 |
| 81d1fce2-b933-3072-b291-d28756c3ee34 | -10.8101 | -43.9275 | 2025-10-18 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 60f46bbc-b4db-3198-b7db-a8a101f7fcb2 | -11.3588 | -44.2458 | 2025-10-18 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| c17c1a32-9e03-37ef-9dd9-cbc56c380ec7 | -10.2367 | -44.0298 | 2025-10-18 13:50:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 5f513cd4-d4d4-3b1a-8f11-a23388cdde3b | -3.0632 | -43.2161 | 2025-10-18 13:50:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 202af889-365a-33db-b3b8-7a484818dd53 | -10.2363 | -44.0532 | 2025-10-18 13:50:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 69118d9d-0387-3745-a9d8-8efdc8e6164d | -13.2644 | -47.1007 | 2025-10-18 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 196.2 |
| f63bbe98-e29e-390e-8917-0f91c0016ca1 | -11.5724 | -44.0736 | 2025-10-18 13:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 0d483704-5695-3167-abd4-89f16e5252e0 | -10.5132 | -43.4289 | 2025-10-18 13:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 1648ff97-863a-3974-b9e2-c1fb7de5d04c | -4.4059 | -43.4049 | 2025-10-18 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| e00a93fa-ad26-3c94-9e98-47a82037a919 | -10.8293 | -43.9248 | 2025-10-18 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| e03d209e-5c23-3e32-9112-cb0cc3a00c09 | -4.1712 | -42.1978 | 2025-10-18 13:50:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| 63b8def3-ee11-34f3-b3b0-d1170472f430 | -12.7196 | -50.8622 | 2025-10-18 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 34bf03ed-cde7-3003-b759-dbfe2c92b3e5 | -12.1682 | -45.0539 | 2025-10-18 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| c4b90bdf-d76d-3a0d-affb-40657c06fc81 | -13.2451 | -47.1036 | 2025-10-18 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 100.0 |
| d819d678-ffdc-355d-8308-fddab81aa85e | -11.3603 | -45.2646 | 2025-10-18 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 434e6143-013d-35a3-bbec-36fc11373618 | -10.6853 | -44.5506 | 2025-10-18 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 9332e918-1d32-3eb5-9f4f-3a70c66c2a9d | -10.7044 | -44.548 | 2025-10-18 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 350117fa-3298-3dd5-a38d-c69f81f59859 | -13.6368 | -43.9446 | 2025-10-18 13:50:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 18dfcb83-b812-37cf-9e5b-af5e31e5425b | -11.245 | -45.3037 | 2025-10-18 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 033ef847-64c2-3e6f-a684-7a010605b08a | -16.4584 | -43.0615 | 2025-10-18 13:50:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 391cdd1a-34ac-3bbd-acaa-546a30a0bd1e | -10.2558 | -44.0273 | 2025-10-18 13:50:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| c18bc252-1368-323b-a5f7-d7482bd6237d | -11.5912 | -44.0942 | 2025-10-18 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| b5765a25-82cd-3144-bf93-0af854b074a7 | -13.6373 | -43.9208 | 2025-10-18 13:50:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 9dee4fb5-e5b9-3b4e-91c1-65fd3a0f5c83 | -11.378 | -44.2429 | 2025-10-18 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 225.2 |
| 83cd0b37-8636-316d-97be-520305ecc7ba | -11.3968 | -44.2635 | 2025-10-18 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 387.7 |
| 223481b7-4fea-3ec4-b3af-3b66f0351486 | -11.358 | -44.2926 | 2025-10-18 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 189.0 |
| 67016243-4980-3417-a6ab-6910dcb0c75a | -14.0282 | -44.6992 | 2025-10-18 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 68693c6f-89ec-368c-aae3-5d4f1b876124 | -4.6509 | -43.1337 | 2025-10-18 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 7ad8af0f-22f5-36a4-87bc-2b4fad1281d1 | -5.7976 | -42.6531 | 2025-10-18 14:00:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 66.1 |
| 54a7d4be-96fc-3e50-87db-ece99fb0e280 | -12.1485 | -45.08 | 2025-10-18 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 0c0f515e-4984-35cc-9bea-ec4d6abccf79 | -13.0488 | -47.3131 | 2025-10-18 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 82bf5b37-7220-3cba-a2c3-3c59eec69d40 | -13.2001 | -46.4312 | 2025-10-18 14:00:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 7e0471a6-b015-3e03-88eb-9e0b9fcff5d2 | -10.475 | -43.4342 | 2025-10-18 14:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 205.5 |
| 77296e31-91c3-3e7b-8e81-4b63a24689cf | -6.0301 | -41.9214 | 2025-10-18 14:00:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| a50348f4-ba42-3bc0-874f-8659329621b8 | -12.9716 | -47.3245 | 2025-10-18 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 7c52ac9d-27ac-3414-af03-dc8463ada114 | -10.1333 | -44.5545 | 2025-10-18 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| bd77553b-eec1-3bf4-bd57-c872467765f5 | -14.0092 | -44.6792 | 2025-10-18 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| cb4fa09c-e0f9-3ce1-a2b8-1ed88a19a98e | -12.1682 | -45.0539 | 2025-10-18 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 4386afc9-286f-3f38-b68b-63f26bec2283 | -10.685 | -44.5738 | 2025-10-18 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| d843bece-6a70-3910-99de-4f5b44273c32 | -10.8101 | -43.9275 | 2025-10-18 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 4e643bcc-02f5-36b9-82fe-f742a3599638 | -14.0477 | -44.6957 | 2025-10-18 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 254.6 |
| 3d11a384-a94d-3bf3-ae5b-bf939cdcc123 | -10.5136 | -43.4052 | 2025-10-18 14:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 44fff774-71e3-3e4a-bf58-b95f50021ff3 | -12.9712 | -47.347 | 2025-10-18 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 9b3aeb97-5c4b-303a-b26f-0c4709a8abd3 | -11.3794 | -45.2619 | 2025-10-18 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 399.4 |
| d76570a9-23cb-3a62-9d0e-7684813446b8 | -4.1712 | -42.1978 | 2025-10-18 14:00:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 88371a91-b404-3f2c-bcad-2f8ba17bf9d3 | -11.3772 | -44.2897 | 2025-10-18 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 948.5 |
| 5079661c-c788-3b98-9922-bcc4e0d68547 | -13.2644 | -47.1007 | 2025-10-18 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 188.6 |
| ae0616fc-fce5-361a-9341-7d3bff4b0bf8 | -6.0644 | -42.2522 | 2025-10-18 14:00:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 0768388b-61b9-3e4b-b8a9-4b4b1fe63a33 | -13.0106 | -47.2963 | 2025-10-18 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 7e21aa42-45f4-3734-95a8-9ae2ddbc6f29 | -13.0295 | -47.316 | 2025-10-18 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 05437dee-8dd8-32b3-a1c4-c28d667c68fa | -4.171 | -42.2215 | 2025-10-18 14:00:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| ce1dbd25-6a61-36a3-a47e-bf99d8a0a372 | -10.1143 | -44.557 | 2025-10-18 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 99ee3daf-a647-338b-aac7-6de71b02e148 | -12.9519 | -47.3499 | 2025-10-18 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| ace7013e-7a24-3985-a72e-fe04b4df67f7 | -11.3603 | -45.2646 | 2025-10-18 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 1dce860a-c5b1-3a92-b974-cb13d62af9f1 | -4.856 | -43.214 | 2025-10-18 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 5e27fab9-47be-3148-90e9-8baa857a1d60 | -13.2451 | -47.1036 | 2025-10-18 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 92.1 |
| d4344fab-fd40-3287-b659-95ca860fc782 | -6.3919 | -41.5052 | 2025-10-18 14:00:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| f6b3d610-2ba4-37fc-8a1e-54177edb9701 | -3.7439 | -41.7217 | 2025-10-18 14:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 6b86cf77-ffae-3b79-b286-e71cd6142b9c | -12.1673 | -45.1003 | 2025-10-18 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 224.6 |
| c87af087-f245-328d-9205-0b21a015922a | -14.0292 | -44.6521 | 2025-10-18 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 178.6 |
| e8833d89-917b-3eda-8061-e110ccfa5877 | -13.0299 | -47.2935 | 2025-10-18 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 30329bdf-0c26-3903-bb57-a827ccafe149 | -10.8289 | -43.9482 | 2025-10-18 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 171ea771-b47f-3d4d-9daa-bd654007b0dd | -11.5724 | -44.0736 | 2025-10-18 14:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 0070e641-272a-39e7-b8f7-9be572c39bdc | -11.6104 | -44.0913 | 2025-10-18 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 401.0 |
| 682374d3-adf6-36bd-adc3-037d54bbc99b | -10.7044 | -44.548 | 2025-10-18 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 06355b2e-a585-3b10-b705-be795caca411 | -11.358 | -44.2926 | 2025-10-18 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 662.0 |
| d6482a21-3f12-3750-b33e-72d00e2905a0 | -12.1678 | -45.0771 | 2025-10-18 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 2f6e0ac7-a10c-3fe1-b694-40cf29f99343 | -11.245 | -45.3037 | 2025-10-18 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 3696a0bb-6e2b-3b28-9ec5-72083b7059cc | -11.3415 | -45.2443 | 2025-10-18 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 0f262474-2756-3e73-b538-80debcc2d0fa | -10.133 | -44.5777 | 2025-10-18 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 60.0 |
| a5d78fb9-5140-3934-9260-de465c6cf3d8 | -12.1481 | -45.1032 | 2025-10-18 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 90866699-4a7a-3b08-ad4a-ffcc822107ff | -5.854 | -42.6486 | 2025-10-18 14:00:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 71.1 |
| cacae888-bbce-329b-87f3-eb740be0ccc4 | -3.7625 | -41.7446 | 2025-10-18 14:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| ae02076a-81a0-31e8-ac36-75125a1a9c54 | -10.1337 | -44.5313 | 2025-10-18 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 300.7 |
| 837dc975-03e4-32a4-ad0c-d125600f76f5 | -13.6174 | -43.9481 | 2025-10-18 14:00:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 0ed54494-8c23-34e1-b9d1-bb72e3f9ee02 | -14.0287 | -44.6757 | 2025-10-18 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 350.9 |
| ed813131-9125-3e11-81e5-53c9d6be0678 | -13.0303 | -47.2709 | 2025-10-18 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| f0509ebd-c186-3e06-bfb3-75e29758ca9a | -13.6373 | -43.9208 | 2025-10-18 14:00:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 99707e94-2149-3a7c-a6f3-592f87646e8c | -4.0963 | -42.2021 | 2025-10-18 14:00:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 106.8 |
| 78a010a3-9d72-3abb-bc81-5501a363dfc3 | -10.4945 | -43.4079 | 2025-10-18 14:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 171.7 |
| a56d4ba6-2a56-38ed-b9c2-e5c05a912388 | -13.6368 | -43.9446 | 2025-10-18 14:00:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |


[Clique aqui para ver as próximas entradas](README94.md)
