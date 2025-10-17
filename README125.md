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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 871b599b-b522-3b6f-a3a3-d2f09ede7b71 | -12.699 | -48.6299 | 2025-10-17 14:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 76c32981-b470-317c-bb39-1e5ea5100f75 | -10.1063 | -47.6525 | 2025-10-17 14:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 3aaac329-ca52-305f-8742-a7668ba5a0fd | -10.9261 | -49.9349 | 2025-10-17 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 3e7651d8-af2c-30e3-95ce-d88500f03752 | -10.9189 | -45.4171 | 2025-10-17 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 0ee865ec-0fe5-3b04-868c-ec041991ce63 | -9.898 | -47.6758 | 2025-10-17 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| bf330e2b-8d59-3a8b-9484-74c0f25c08f9 | -10.5132 | -43.4289 | 2025-10-17 14:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 452.9 |
| d0ec8c82-59b2-3be8-be47-eaa5806ecc59 | -10.5136 | -43.4052 | 2025-10-17 14:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 0841d0a9-3e11-3878-b0de-fb549b69db9c | -4.0088 | -44.1887 | 2025-10-17 14:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 141.4 |
| a82a9a76-1ea1-3fe8-b9ca-43b04db191e0 | -11.9709 | -45.3603 | 2025-10-17 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 57098bec-26db-38cb-922c-47706393c29f | -14.1754 | -47.9252 | 2025-10-17 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| dad52273-12b6-302d-b6a4-2bc10bdc1c5a | -11.496 | -44.0617 | 2025-10-17 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 941dfd7a-43ea-3aac-9436-e921f5b81c2b | -9.9828 | -47.0234 | 2025-10-17 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 177.3 |
| f8083128-1d60-3f3d-b5e5-aa27025de570 | -15.9847 | -41.5179 | 2025-10-17 14:00:00 | GOES-19 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 135.9 |
| 5d984466-c092-3b12-ac47-c09893f56eed | -3.9822 | -42.4924 | 2025-10-17 14:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 139.4 |
| 6f2eef1d-6f8a-3727-a6d4-c349a66cbe06 | -4.4446 | -43.2164 | 2025-10-17 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 219.3 |
| a0bda4a8-acb2-339d-bfa1-e9751853d22b | -10.2554 | -44.0506 | 2025-10-17 14:00:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 394.8 |
| 3833eb7e-02c3-3bc1-bb1d-67cb9b3fe826 | -10.4945 | -43.4079 | 2025-10-17 14:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 02a4e5b0-0825-3c7a-a5ab-d5cf0ac285bb | -5.6095 | -42.715 | 2025-10-17 14:00:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| f768afd3-f240-338e-a1fc-38fab4e8fa85 | -12.4866 | -45.4895 | 2025-10-17 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 187fcb5b-484e-3b31-b86a-d93fbfdde082 | -4.4351 | -41.9441 | 2025-10-17 14:00:00 | GOES-19 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 110.8 |
| 062fc1a4-f0ed-3d0d-a81a-1dc215c95d00 | -12.4678 | -45.4694 | 2025-10-17 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| d13f118c-3b61-3168-be40-3d97b2a7ce22 | -12.1678 | -45.0771 | 2025-10-17 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| e587a3c7-0b08-3d35-8369-1196fe44645f | -12.9265 | -41.8118 | 2025-10-17 14:00:00 | GOES-19 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 147.2 |
| ea602616-34c5-34f1-90e5-40e3bfab1edb | -12.9459 | -41.8082 | 2025-10-17 14:00:00 | GOES-19 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 91.6 |
| 4ef65f6d-671e-32a8-b6c6-e88060288742 | -5.799 | -42.5112 | 2025-10-17 14:00:00 | GOES-19 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |
| 25d600bc-93b8-39cb-b603-d7f184d229ba | -12.9259 | -41.8363 | 2025-10-17 14:00:00 | GOES-19 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 116.2 |
| 1912684b-491c-304b-96e1-7ad95951a350 | -9.9831 | -47.0011 | 2025-10-17 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 89830ecb-6fe6-3466-9928-c37cb8c193f5 | -13.2451 | -47.1036 | 2025-10-17 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 4dab2132-72b1-3f43-8049-9212c4b09381 | -6.2012 | -41.7389 | 2025-10-17 14:00:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 110.2 |
| e40c92f2-3908-3cfc-8960-a64e82ea1324 | -11.7622 | -51.1663 | 2025-10-17 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 8ac326f4-964f-3865-8774-51f0fc33b7a1 | -11.2642 | -45.3011 | 2025-10-17 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 01f514ac-a214-346b-a4c8-60bbdcac3528 | -11.9521 | -45.3401 | 2025-10-17 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 99a9ddc2-ff0a-329a-a8a8-6864ce18dbeb | -4.4248 | -43.3805 | 2025-10-17 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 96da1b07-1e78-3c35-9185-ddc9ee692dbe | -14.8657 | -52.4405 | 2025-10-17 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| d4f35934-8c53-3b66-8c1f-483229874ebb | -11.4923 | -44.2727 | 2025-10-17 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 5a5db468-2b80-3fef-a885-3ffa5d38a3e8 | -14.8854 | -52.4167 | 2025-10-17 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 5b1c404e-9489-3f1a-90e0-4086da673cda | -11.0214 | -47.3443 | 2025-10-17 14:00:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 20321ac4-e98c-3761-b8e0-271268f42a7e | -11.9516 | -45.3632 | 2025-10-17 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| c776ed1a-9372-30f0-9a13-565f154e7014 | -18.3938 | -55.4559 | 2025-10-17 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.7 |
| e25f2106-ff28-3302-ba08-30402a971efa | -6.1532 | -40.9215 | 2025-10-17 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| 71f4a2a6-5a96-399f-972d-32c407591174 | -12.5059 | -45.4866 | 2025-10-17 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 6787cc03-695a-3d3f-b580-40f962bb9bf2 | -11.6274 | -47.5561 | 2025-10-17 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 1db02d6d-8951-3845-af58-5acabea3df2f | -10.9938 | -47.9019 | 2025-10-17 14:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 32eb898c-021a-3437-9138-79824988d26c | -10.6028 | -47.3955 | 2025-10-17 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| a53a6f7d-ea3e-3dd2-8dd1-ef5a637a7891 | -11.1208 | -45.8919 | 2025-10-17 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 403.2 |
| 8308a3e0-7150-3001-8759-0ab5c95ce906 | -10.8101 | -43.9275 | 2025-10-17 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| ba447e14-59ef-3413-98f9-dea0a36cbdc9 | -11.1013 | -45.9172 | 2025-10-17 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| a93c6b9f-ee26-3ccc-a6a0-2017eafe1987 | -3.9635 | -42.4934 | 2025-10-17 14:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 109.2 |
| e55d58df-1ca5-361c-adf0-749e46a84479 | -11.1419 | -55.1869 | 2025-10-17 14:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 7efee3fc-14b2-3abf-8690-7698d412c255 | -9.7158 | -44.538 | 2025-10-17 14:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 86316a38-1cc7-36af-8d1b-5b08c3ae3337 | -5.4561 | -41.0054 | 2025-10-17 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 154.5 |
| e2068755-b91c-3f1a-a870-57d785970505 | -12.4451 | -51.3217 | 2025-10-17 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 5f51c956-bbef-3254-bd02-be8d23f473bc | -10.534 | -49.5471 | 2025-10-17 14:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| e2dec8b7-1670-38d8-b3bf-3d5538c175c6 | -14.866 | -52.4193 | 2025-10-17 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 88033667-74a6-3795-9e04-ff34dde71fa6 | -4.6984 | -39.4641 | 2025-10-17 14:00:00 | GOES-19 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 127.1 |
| de8db29a-83eb-3725-ab84-ab4b72f1e0f6 | -12.9607 | -47.9294 | 2025-10-17 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 418d866f-5703-35bd-a63e-79a6afbbc83a | -11.5724 | -44.0736 | 2025-10-17 14:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| dffd7f4c-2f07-3ff1-94ac-5e8c3d33597b | -6.0279 | -38.493 | 2025-10-17 14:00:00 | GOES-19 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 89.6 |
| afae6828-4415-393c-9ee8-64ab0fb23f82 | -12.1682 | -45.0539 | 2025-10-17 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| e1b858db-ed28-3cb7-97d1-d81b81efc93c | -13.2644 | -47.1007 | 2025-10-17 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 09d9c78b-0cbd-3fbc-bc08-bca4d65c975f | -11.3603 | -45.2646 | 2025-10-17 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 2b8dc5f3-3c24-381d-b279-0a8df7ebf96e | -10.938 | -45.4146 | 2025-10-17 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 226a15af-cbb3-3d5e-b037-fb2f01faac6e | -5.2863 | -41.0673 | 2025-10-17 14:00:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 172.7 |
| 91ebca59-3c6b-32a6-ba22-d2eac5a4c3a2 | -10.4941 | -43.4315 | 2025-10-17 14:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 356.4 |
| 2a6b56d8-da68-3411-8968-3a6c5cac7d05 | -14.0905 | -43.6235 | 2025-10-17 14:00:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 32a96ade-e521-3f9c-9d0f-fe3a52f301ce | -11.4965 | -44.0382 | 2025-10-17 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| bc03418c-288d-35b9-8ad9-2b6e095cb2e4 | -11.5921 | -44.0472 | 2025-10-17 14:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 184.0 |
| 4c0a6feb-9fdd-376c-99d3-10c0b74fa423 | -18.3739 | -55.4587 | 2025-10-17 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.6 |
| 2b0b6b90-b3d5-3c13-bafc-afd0183bc616 | -11.1021 | -45.8717 | 2025-10-17 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 71c81029-d4f0-3ad6-a709-64edd36a6a15 | -9.7155 | -44.5612 | 2025-10-17 14:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 191.4 |
| 437639e5-1505-3cd6-87fb-9014b6fbdc86 | -10.9748 | -47.9042 | 2025-10-17 14:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 6b687e11-9e6b-39bc-99c2-dad36285d8aa | -11.3996 | -44.0995 | 2025-10-17 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 7429443f-3488-3128-b1f0-1f1a97cf7851 | -12.487 | -45.4664 | 2025-10-17 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 160.5 |
| bc2e5075-3446-3d2a-a14f-28f29d51b469 | -10.8797 | -47.9157 | 2025-10-17 14:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 236eca7b-78d9-3c6e-8669-96bd1491811d | -12.284 | -47.1544 | 2025-10-17 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 4e2a5df7-f2d3-31d5-9d34-77c076c857dc | -9.9828 | -47.0234 | 2025-10-17 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 247.1 |
| 9ef2618b-57e7-3bbf-b3ba-1333d296edd4 | -5.4558 | -41.0297 | 2025-10-17 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 153.6 |
| 6baedcae-01c6-3755-a1f8-92e5ae1879b0 | -13.2447 | -47.1262 | 2025-10-17 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| d3077a21-870e-3935-9f40-aa9dde26b2a0 | -14.866 | -52.4193 | 2025-10-17 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 5896e58d-6c5a-311d-aa0e-28641a15d42d | -10.2748 | -44.0247 | 2025-10-17 14:10:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 198.2 |
| 7c9d3911-2aa7-3808-ab8c-aacfb046b644 | -9.879 | -47.6779 | 2025-10-17 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| ebe8543d-7cae-31c7-afb8-4f2e1fcf3ea0 | -12.907 | -41.8154 | 2025-10-17 14:10:00 | GOES-19 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 117.3 |
| e2edbf23-8848-3509-9541-6266fcc8e6cf | -12.4866 | -45.4895 | 2025-10-17 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 168.0 |
| e796f944-f9c7-3116-a3cb-32217d8e2875 | -10.9376 | -45.4375 | 2025-10-17 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 53ee8a68-6f9b-375f-8f64-e1cf587f2943 | -11.3603 | -45.2646 | 2025-10-17 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| ca2f90da-f69c-30e6-aa15-82036c379baf | -4.4248 | -43.3805 | 2025-10-17 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 8fd0e2b8-ff29-3770-a78b-7c7848f881df | -11.1021 | -45.8717 | 2025-10-17 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 75f0a194-3e94-3ee5-8178-5eab5197ab85 | -13.0137 | -48.1884 | 2025-10-17 14:10:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| c220032c-5575-3630-a0f0-04035f262f18 | -6.0301 | -41.9214 | 2025-10-17 14:10:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| 31c86bc8-1db9-3179-ac86-04c6b9f80043 | -6.411 | -41.4793 | 2025-10-17 14:10:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| da2f1e40-4c46-3a95-b563-1b86a2ea75ee | -9.9831 | -47.0011 | 2025-10-17 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 89db201c-8c09-37b4-9d34-a519045841ce | -4.4351 | -41.9441 | 2025-10-17 14:10:00 | GOES-19 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 131.6 |
| 4d032528-a467-3d00-a957-d108a63a397d | -12.1547 | -50.3735 | 2025-10-17 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 071da976-abc7-33c2-992a-7b05e62254e6 | -18.3938 | -55.4559 | 2025-10-17 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.4 |
| 923ef42e-cd88-33c2-b44a-b0e6f81bfa53 | -10.5837 | -47.3978 | 2025-10-17 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| de89c894-c0e3-3751-b1d3-bd263ef3bc05 | -9.9638 | -47.0256 | 2025-10-17 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| bada9508-f6ef-31aa-aa73-b2d560ffe1af | -13.0299 | -47.2935 | 2025-10-17 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| e765faa4-768b-3dae-bc62-69239078d9f0 | -5.2863 | -41.0673 | 2025-10-17 14:10:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 132.6 |
| 46713790-e32c-33e7-a1c7-be014496d0c1 | -6.3544 | -41.4846 | 2025-10-17 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 70.3 |
| a4e6476d-543d-31b7-aad9-dd8441f8de50 | -10.5132 | -43.4289 | 2025-10-17 14:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 238.5 |


[Clique aqui para ver as próximas entradas](README126.md)
