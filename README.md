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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 210b2a75-e5ed-34e2-96c0-724770d066e4 | -13.2252 | -42.3414 | 2025-10-11 00:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 295.5 |
| 8e81ce61-c160-3c05-895a-3035c2dab62f | -13.2052 | -42.3693 | 2025-10-11 00:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 113.5 |
| c5c487ab-3d71-314d-bec7-5f4acba255ae | -7.4613 | -46.8764 | 2025-10-11 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 2a0b91b3-a7e5-3957-a9f3-ef986febf271 | -17.4781 | -40.0753 | 2025-10-11 00:00:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 72.4 |
| ac4a656b-af2f-3cb9-be44-90c5fea037ce | -17.4579 | -40.0808 | 2025-10-11 00:00:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 90.8 |
| 02edd6b4-df1d-3a0f-a631-0de98aee3606 | -13.2057 | -42.345 | 2025-10-11 00:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 538.9 |
| 06548a87-fb08-3733-b87a-5a4e7e8f2254 | -13.2257 | -42.317 | 2025-10-11 00:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 57ad99cf-dc50-3c35-a6e3-7f534b5a521a | -8.1993 | -43.3424 | 2025-10-11 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 24f684db-0d9c-3f64-880d-f9c30b548e7f | -12.1544 | -48.019 | 2025-10-11 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 63d67f77-002a-30cd-8d4f-4eaa79ce9eba | -9.1616 | -68.1643 | 2025-10-11 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| a8726e3a-b690-36d3-8cda-b94dde2140fc | -5.8672 | -45.3024 | 2025-10-11 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 031012c0-ac38-3e26-94b9-f14a864f196c | -13.2246 | -42.3657 | 2025-10-11 00:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 91.9 |
| 5a964036-16fe-3eb4-89d9-1519d880ecc1 | -7.8645 | -44.4692 | 2025-10-11 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| eabf50c6-d214-3b9b-9045-3901f38fd151 | -7.9708 | -72.4761 | 2025-10-11 00:00:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 43.9 |
| b57970eb-db78-3c65-a0e8-a4a7aa67ae9f | -4.4054 | -43.4746 | 2025-10-11 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 94265b24-7d62-375c-b15d-551ed0472a08 | -5.8674 | -45.2798 | 2025-10-11 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 63ab36ee-5833-384c-9f8f-945987cbcf47 | -5.8859 | -45.3011 | 2025-10-11 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| a58c9629-9f90-3ce7-9f03-72cec18d67fc | -9.1615 | -68.1828 | 2025-10-11 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| a48a58e0-f3c9-3d4c-b790-6b3e6f123aea | -13.2062 | -42.3206 | 2025-10-11 00:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 121.6 |
| 24e6b374-10f6-3fbb-97a7-3f4712b745b7 | -8.1996 | -43.3189 | 2025-10-11 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 108.6 |
| e9b1e7ff-616e-3a3f-b600-e3309081e784 | -4.4241 | -43.4735 | 2025-10-11 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 7f3f2e35-2253-3d0e-9320-26a875ff826a | -17.4843 | -43.3358 | 2025-10-11 00:00:00 | GOES-19 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 2858f3bc-0ad2-30bf-8f07-2c7d886154c1 | -9.18 | -68.1824 | 2025-10-11 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| ef541fdf-7ff0-32bc-86b3-d7987c574af3 | -9.1801 | -68.1639 | 2025-10-11 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| ac9a7207-3fc6-36ff-867c-f1879f7a6914 | -7.4616 | -46.8542 | 2025-10-11 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 3e5937fd-af71-34bc-80f7-e90b906a2eda | -17.4789 | -40.0493 | 2025-10-11 00:00:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 215.6 |
| 0b67150d-d388-3c13-989d-e1c4c34f73b1 | -15.1141 | -42.4528 | 2025-10-11 00:00:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.6 |
| 0f2c6261-bfaf-3e68-989b-9791c6ebacb0 | -11.7589 | -43.3136 | 2025-10-11 00:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 5a5e8ea9-15d7-3115-ad41-9c9dd86ab3f2 | -17.4587 | -40.0547 | 2025-10-11 00:00:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 284.2 |
| 08bc5f59-cac2-3866-b9d9-e0aa45f1d05d | -15.1135 | -42.4774 | 2025-10-11 00:00:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.3 |
| c2d96b40-fc89-30a2-801b-d26228f03f44 | -17.4594 | -40.0287 | 2025-10-11 00:00:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 77.4 |
| 4fe85065-112b-35ad-aa98-908f7c7ff8ae | -12.6954 | -51.1855 | 2025-10-11 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 55dc942a-a368-3f19-8390-183056aaf336 | -12.6957 | -51.1641 | 2025-10-11 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 54707dd7-9d1d-38ed-ad21-03bdcdc2ee83 | -12.7148 | -51.1618 | 2025-10-11 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| b7cb57a3-4d2d-363d-ab85-f1f7b8e3ad96 | -12.7145 | -51.1832 | 2025-10-11 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| e0308c43-3a3e-3098-b25d-867c2920068f | -7.8642 | -44.4922 | 2025-10-11 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 5ca95300-fe94-37df-aec8-1f9618410b84 | -13.2257 | -42.317 | 2025-10-11 00:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 107.1 |
| 6ff85cff-3758-3e1c-9804-a418aa883001 | -7.8457 | -44.4711 | 2025-10-11 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 1f4792e3-85f9-3dc7-966f-53ca4255b7aa | -7.8645 | -44.4692 | 2025-10-11 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 98c7f2ae-c799-3753-a520-48c07371dc7d | -4.4054 | -43.4746 | 2025-10-11 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| dbe1c153-71b1-31d7-a1bc-780a40080f5b | -8.1996 | -43.3189 | 2025-10-11 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.4 |
| 7a1dfea0-bb71-392a-a567-83d753358d77 | -13.2052 | -42.3693 | 2025-10-11 00:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 109.5 |
| 8db84557-e6d6-3c14-83e8-beb904f632cc | -7.3447 | -43.8503 | 2025-10-11 00:10:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| b26c2707-26a9-349b-a03f-7de710edde02 | -13.8501 | -45.7992 | 2025-10-11 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 5b2613d4-5766-3f09-a3ee-8c367c941cb6 | -7.4616 | -46.8542 | 2025-10-11 00:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 33f8ff7d-64b7-3baa-b1fe-bf2c3f22ae29 | -12.6762 | -51.1878 | 2025-10-11 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 141.9 |
| a4f3d773-040b-370d-823d-70a987808a49 | -11.7589 | -43.3136 | 2025-10-11 00:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| e342ada4-397f-34bc-aeca-27065aef04db | -9.18 | -68.1824 | 2025-10-11 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 246d9cf2-83b9-3e49-bbe5-c87cab1d5bd8 | -12.6766 | -51.1665 | 2025-10-11 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 916dd6f4-387e-31c6-8f9a-68c098ceb141 | -13.2252 | -42.3414 | 2025-10-11 00:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 616.8 |
| 9fd56bb7-a48e-369e-8466-06f2b7e6d939 | -7.4613 | -46.8764 | 2025-10-11 00:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 2e894e4f-2c7b-3797-b673-53ff4ca37ad7 | -12.6954 | -51.1855 | 2025-10-11 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 289.4 |
| 6a521cde-8085-3188-8c00-cd8b31cd8c0e | -5.8672 | -45.3024 | 2025-10-11 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 9c7ef5e8-de63-30e9-9471-7b6c19476ba5 | -13.2246 | -42.3657 | 2025-10-11 00:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 110.5 |
| 1c2737cd-7665-390c-9856-c024c0ab8a49 | -4.4241 | -43.4735 | 2025-10-11 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| cd1facd7-4d67-33e8-a7f9-a7de1a78d9e7 | -13.2057 | -42.345 | 2025-10-11 00:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 437.9 |
| 9148ee70-d4e1-3cdf-a24a-20c07195d32e | -13.0228 | -61.4387 | 2025-10-11 00:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 86f4ab0b-ed6b-388e-9675-61078b4e9255 | -8.1993 | -43.3424 | 2025-10-11 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| 3dbc782f-461c-3329-9062-437d76459d3b | -9.1615 | -68.1828 | 2025-10-11 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 777d12b9-b333-3d3d-b673-e750a17de034 | -13.2062 | -42.3206 | 2025-10-11 00:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 14234b2e-1a0a-3317-a953-bc6cf3de21a6 | -12.6957 | -51.1641 | 2025-10-11 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 460.2 |
| 3c4bde57-90e2-332d-a04d-8c9750528847 | -13.8496 | -45.8223 | 2025-10-11 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| c27f3897-1a6c-3dc5-8def-b9d96d1f8d9c | -18.0777 | -45.0066 | 2025-10-11 00:10:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 633126f7-83d9-3fe4-a867-774d000ce5a5 | -13.8307 | -45.8024 | 2025-10-11 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| e49c001e-9d7b-3fef-b7c6-bf6e5bff7cc2 | -17.5044 | -43.331 | 2025-10-11 00:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 78.2 |
| cf771348-e9a0-345c-9705-4a5e964bac28 | -9.1615 | -68.1828 | 2025-10-11 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| cd9ac169-5817-3c25-a066-843c1e663ee3 | -12.7563 | -48.6441 | 2025-10-11 00:20:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 7b817c9e-5967-3eb4-afc5-e50aae733b17 | -13.2052 | -42.3693 | 2025-10-11 00:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 90.5 |
| 89088495-d55c-33dc-939a-52937eaa33a9 | -9.18 | -68.1824 | 2025-10-11 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d0a99bd9-658b-3582-ac16-6d547b0a719b | -8.1993 | -43.3424 | 2025-10-11 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| 3e086be1-398c-33f4-a931-8b5c56aa6fce | -7.8454 | -44.4941 | 2025-10-11 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 9e2f1217-26bc-303c-9994-c8edfbcf10f1 | -7.8457 | -44.4711 | 2025-10-11 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 5009b511-1a64-32d9-99df-e894d4ac2421 | -4.434 | -47.6076 | 2025-10-11 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 32381cff-6116-3629-b4ca-c913b9c99d0d | -13.2057 | -42.345 | 2025-10-11 00:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 334.4 |
| 3fa27a15-5695-3c21-85d0-42887e32ce0e | -7.8645 | -44.4692 | 2025-10-11 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 157.3 |
| fe243e6c-8678-3991-94e8-e42943b9d49b | -7.8642 | -44.4922 | 2025-10-11 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 4c37748b-5fa6-3956-9e7a-f7f08e37c84c | -11.7589 | -43.3136 | 2025-10-11 00:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| c055fb7d-63c7-3959-8ebc-b7b315e200b9 | -8.1996 | -43.3189 | 2025-10-11 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.7 |
| 46d646a3-b6fe-3942-bab1-d0786cc17fb2 | -4.4342 | -47.5857 | 2025-10-11 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 36ce8441-b181-37cf-95bb-ef31b5be2a8b | -13.2062 | -42.3206 | 2025-10-11 00:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 108.8 |
| 8f229938-88b0-3f64-aa88-0ea2212322a0 | -17.2504 | -52.2658 | 2025-10-11 00:20:00 | GOES-19 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 56.6 |
| c2e059c2-dfe3-3072-8a1d-5978b5d23ab1 | -13.2246 | -42.3657 | 2025-10-11 00:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 107.0 |
| 2133d3d3-0345-3c42-8e1b-8d09df032662 | -4.4241 | -43.4735 | 2025-10-11 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| a2e0e2d6-1ab9-3d0b-9144-940bf3c87f3a | -4.4054 | -43.4746 | 2025-10-11 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| a3b1088f-88c2-3e01-8596-acdf116b7ecc | -13.2252 | -42.3414 | 2025-10-11 00:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 412.6 |
| 2b733332-2056-37ed-b898-7e58395accc1 | -13.2257 | -42.317 | 2025-10-11 00:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 124.4 |
| a32483cd-b642-3421-bfb1-f1a572f621b2 | -7.4616 | -46.8542 | 2025-10-11 00:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 9eff1aef-d729-3615-8fbe-0d9ec3515741 | -9.18 | -68.1824 | 2025-10-11 00:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| c4829c44-29db-3f6a-a0dc-079d6b34409d | -12.6954 | -51.1855 | 2025-10-11 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 4b01c1a0-871b-3e66-ba01-efdded83e97c | -7.8457 | -44.4711 | 2025-10-11 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 34f29219-121e-3881-ac71-98de3867f10d | -13.2057 | -42.345 | 2025-10-11 00:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 498.3 |
| 0e492f00-0190-347e-829b-463192b478cc | -13.2052 | -42.3693 | 2025-10-11 00:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 125.1 |
| 3857330c-8965-3817-9ed3-aeb0b10aae95 | -13.2257 | -42.317 | 2025-10-11 00:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 126.4 |
| 7571ec91-fa0d-3d26-af23-b06b98963cc7 | -4.434 | -47.6076 | 2025-10-11 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 0f77e03c-8b18-3868-b13e-2fd1ac05922c | -13.2474 | -48.0214 | 2025-10-11 00:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| c41acfa0-bc1a-3eb4-95db-d3413b699881 | -8.1996 | -43.3189 | 2025-10-11 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.0 |
| 17629f21-ff48-3e34-b419-f5999ba81174 | -4.4054 | -43.4746 | 2025-10-11 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 42431bd2-f81a-3cae-a81e-64d9c7aeedda | -7.4613 | -46.8764 | 2025-10-11 00:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 4102f8c2-bf58-3469-972d-4e2f304eefd9 | -12.6957 | -51.1641 | 2025-10-11 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 149.7 |
| ead51b1b-6d30-3813-b388-a5a6eab3b0e3 | -4.4342 | -47.5857 | 2025-10-11 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |


[Clique aqui para ver as próximas entradas](README2.md)
