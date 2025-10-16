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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f6ab7c2-8f0b-3e0c-b3ba-94c3133467e3 | -12.2652 | -47.1346 | 2025-10-16 12:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| e702d3e1-14b7-30f3-bf7a-99fc955c5e10 | -13.0165 | -43.0547 | 2025-10-16 12:20:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 121.1 |
| ecd463bd-c346-329a-8efd-b89a9eb258a5 | 1.84 | -55.7824 | 2025-10-16 12:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| dfe05610-140d-3fc0-a69e-dd7a8df8c0fa | -13.9127 | -45.5808 | 2025-10-16 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 0fd1f0b2-275a-3811-9af3-dec770e09f5b | 1.8402 | -55.7034 | 2025-10-16 12:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 3be251ae-0ebb-3ea7-a8f6-ea9bb2e5df2e | -11.4376 | -44.1172 | 2025-10-16 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 2da9f725-4313-3662-8c73-f874d75c8b75 | -10.673 | -45.3125 | 2025-10-16 12:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 88e3cab6-b43a-351e-8a19-4262a8f04115 | -11.5724 | -44.0736 | 2025-10-16 12:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 5c71c084-8e91-3dda-851d-0ba53ae8bd89 | -12.9905 | -47.3442 | 2025-10-16 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 0ddd1a13-94bc-37f6-bf6f-e5a4fc9ba1fb | -13.0165 | -43.0547 | 2025-10-16 12:30:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 96.5 |
| 3c35b904-431f-38b2-b299-d4d5c8df9f2b | -11.5917 | -44.0707 | 2025-10-16 12:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 30c270e6-8bcb-337d-8e4f-163db6c8bda4 | -10.6172 | -45.2282 | 2025-10-16 12:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| ea0a2003-f4a5-3bec-9136-eb06b026ac4f | -11.4756 | -44.135 | 2025-10-16 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 1b76986c-c63d-3969-b4c7-605e649bbcf9 | -11.5917 | -44.0707 | 2025-10-16 12:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 70976620-629b-3ced-a542-2496087d8242 | 1.8402 | -55.7034 | 2025-10-16 12:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 7d281440-8a3a-3db0-9c96-47e64cbfe74b | -10.6211 | -47.4377 | 2025-10-16 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| b56e271a-ca0e-3d6e-8fdc-8e9c5efe9447 | 1.0765 | -51.1026 | 2025-10-16 12:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 68.8 |
| efcaae06-1ebc-3caf-a3db-87970b7ddf82 | -13.9127 | -45.5808 | 2025-10-16 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| e075299e-ba28-3906-8722-a590101d49fe | -10.133 | -44.5777 | 2025-10-16 12:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d7bbddd2-10d0-3ea4-9cfe-0252392ba7a7 | 1.0398 | -51.0407 | 2025-10-16 12:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 70.7 |
| cd9f50e9-0c9e-3753-88b2-c7beb91e4ea0 | 1.84 | -55.7824 | 2025-10-16 12:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| cf7acf2f-22a9-3554-9aab-aff459dfbe4f | -10.5144 | -43.3579 | 2025-10-16 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| e9458735-3295-36a1-bd7b-4a70f64d7ccf | -13.0743 | -46.9717 | 2025-10-16 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 951021d4-a917-34e9-8aa1-f6a02de08c0b | -11.3224 | -45.247 | 2025-10-16 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 33b8ebe1-c5f7-3aa5-acb0-8d69bdd8a616 | -10.514 | -43.3815 | 2025-10-16 12:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| f6f2aef6-4fd5-33db-a2ff-b44ad73f0354 | -10.673 | -45.3125 | 2025-10-16 12:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 2e354212-9e6b-324c-be55-0ca60f2ca1bb | -10.6726 | -45.3355 | 2025-10-16 12:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 54adbc4b-b1b7-34ce-8a64-eea168090336 | -11.496 | -44.0617 | 2025-10-16 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| ee5bcac0-0270-3f43-870d-a9e160977ee5 | 1.0582 | -51.0198 | 2025-10-16 12:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 69.7 |
| c0a6f212-3911-3450-a43f-eabc9507e400 | -11.5729 | -44.0501 | 2025-10-16 12:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 9b75fe6d-883b-3f48-ba18-fc614c8dabfa | -10.1333 | -44.5545 | 2025-10-16 12:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| c9cb9710-5de2-3406-9289-c4b81b811857 | -12.6475 | -41.2737 | 2025-10-16 12:40:00 | GOES-19 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 112.7 |
| dd4257a4-ba81-3153-a7aa-1f6d31397569 | -11.5724 | -44.0736 | 2025-10-16 12:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 4647d9c5-ebbc-3560-b5ee-707188665052 | -10.6024 | -47.4178 | 2025-10-16 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 81170a55-671e-3fca-95bd-33624b691c90 | -11.3032 | -45.2497 | 2025-10-16 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 5a192dcb-430e-396f-b3ed-b98a79e8eaaf | -10.6172 | -45.2282 | 2025-10-16 12:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 74b4534b-2a2b-3cad-a62e-04053767e6ed | -12.4866 | -45.4895 | 2025-10-16 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| eb770c32-9e6f-3649-b24f-fd7407b41ceb | -11.5729 | -44.0501 | 2025-10-16 12:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 3f360e0e-ef70-3159-a9f6-996e39e22d0c | -12.4866 | -45.4895 | 2025-10-16 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| bc8308f0-72dc-3f15-877a-09985e36e9bc | 1.8402 | -55.7034 | 2025-10-16 12:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| ee9d9412-e9af-3b3e-8d2b-24d55385fc33 | -13.9127 | -45.5808 | 2025-10-16 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 5d4af585-1d2a-3638-a43c-18512680be3c | -12.3116 | -45.6081 | 2025-10-16 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 496ee91d-1db1-318b-8b64-c542ed6cdb03 | -12.2652 | -47.1346 | 2025-10-16 12:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 22fc53b2-334e-3ed6-9d49-224aa01ab292 | -10.6172 | -45.2282 | 2025-10-16 12:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 61b49d11-9e48-305d-b0bb-353e6bf6c54c | -10.1333 | -44.5545 | 2025-10-16 12:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 4d2aff12-f529-3fd1-aafd-ec80d0e6516a | -10.5144 | -43.3579 | 2025-10-16 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| b5a62a00-b52b-3702-98a0-5f9bd86204d1 | -10.673 | -45.3125 | 2025-10-16 12:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| b4bf616a-5ff8-30fa-b4fc-989b08badf79 | -11.2862 | -44.0226 | 2025-10-16 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| cf931435-e875-3701-b18b-325f3280852a | -10.6539 | -45.3151 | 2025-10-16 12:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 7d260735-4e17-3063-b6d3-8957998ce3ba | -11.5917 | -44.0707 | 2025-10-16 12:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 177.8 |
| 1f4b140e-ca0e-34ef-9f08-1f2d82ded5fa | -10.6169 | -45.2512 | 2025-10-16 12:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| a5bd039f-fbc9-3f72-8d9c-477b253c1cc8 | -11.5912 | -44.0942 | 2025-10-16 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 3f277558-6dc8-3795-be38-6164407a9171 | 1.8401 | -55.7232 | 2025-10-16 12:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 41fba0b7-92cb-3937-bd84-dbe5ddbf449d | -10.514 | -43.3815 | 2025-10-16 12:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| a0b4be44-1488-32a8-bdb7-abc4c6191b31 | -10.6726 | -45.3355 | 2025-10-16 12:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| c1d6ac68-bdcd-35bc-bf7a-78b3fd89e58d | -13.0743 | -46.9717 | 2025-10-16 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 29c51cc3-9f61-3867-96e0-f3e45940dbff | -10.133 | -44.5777 | 2025-10-16 12:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| db9aee3b-0388-3e9a-b19e-84a21e4858cf | -11.5724 | -44.0736 | 2025-10-16 12:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 2b75a434-0251-3c1f-a5db-bee2aa1dca84 | -11.5729 | -44.0501 | 2025-10-16 13:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 371c3e81-0e18-3695-9d4a-58141aaa7434 | 1.8402 | -55.7034 | 2025-10-16 13:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 30644db4-b4e4-3463-be91-9baa03e0df07 | -10.6172 | -45.2282 | 2025-10-16 13:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 597112ed-978f-3d98-b363-da0227546596 | -13.9127 | -45.5808 | 2025-10-16 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 384.5 |
| a35e5610-3199-32d1-bf95-68437ccf6fe0 | -11.4768 | -44.0645 | 2025-10-16 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 3ff71fa4-1e3f-3dd8-a1d9-3589773c9ccd | -10.133 | -44.5777 | 2025-10-16 13:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 692b42da-b946-38be-83ea-8377f23a9c77 | -10.1333 | -44.5545 | 2025-10-16 13:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 33544f1b-bc75-3710-842f-ff2e7e769a57 | -11.5917 | -44.0707 | 2025-10-16 13:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 170.1 |
| a71d63c2-3283-3b5d-9887-66f74cc9be20 | -10.6169 | -45.2512 | 2025-10-16 13:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 33142100-19cb-3adc-877c-87cdba964208 | -10.514 | -43.3815 | 2025-10-16 13:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 9a5969f0-79ef-39b6-9d5f-2203a97acbaa | -11.5912 | -44.0942 | 2025-10-16 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 2aaa77ce-34a9-3de1-8ddf-294c57c05b64 | -10.673 | -45.3125 | 2025-10-16 13:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 9e6237bb-e7df-365c-951c-5b246697d90e | -12.3116 | -45.6081 | 2025-10-16 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| e2beb212-d642-3f0a-a4a6-18c70c098b57 | 1.8401 | -55.7232 | 2025-10-16 13:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| df2fb562-a4f7-3fb1-948b-c22ed9db0064 | 1.0765 | -51.1026 | 2025-10-16 13:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 08c8daa8-300f-314c-a03f-2e32c59c02d0 | 1.7479 | -56.0791 | 2025-10-16 13:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 8a662822-3c13-395f-8b62-6bc0e1573f9f | -10.6539 | -45.3151 | 2025-10-16 13:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| e5f6395f-f0c7-3e4e-8fd4-94c4cb0df619 | -11.2862 | -44.0226 | 2025-10-16 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| ef808201-7f7c-3fdc-bc8e-f7eb82bb315c | -10.6726 | -45.3355 | 2025-10-16 13:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| a0427a99-abc7-324b-816c-862b362808d2 | -11.572 | -44.0971 | 2025-10-16 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| cf6e4dde-9239-3021-ad28-57cfc017556a | -10.6024 | -47.4178 | 2025-10-16 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 7dbf9aab-4c71-3d13-8674-52389dfbaf47 | -11.4764 | -44.088 | 2025-10-16 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 9ababc72-c822-3604-b141-e7259ff690b9 | 1.8213 | -56.0191 | 2025-10-16 13:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 4ab43932-423f-3cac-8d61-731260f8dfd4 | -11.5724 | -44.0736 | 2025-10-16 13:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 173.4 |
| 535bb80a-2eb8-351f-85e3-a3336468d8d3 | -12.4866 | -45.4895 | 2025-10-16 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| a9ce4719-c739-3566-af66-35c0cc02e350 | 1.2239 | -51.018 | 2025-10-16 13:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 81.6 |
| a5d82f16-4021-3e7e-8f14-ee221fb239cb | -10.5144 | -43.3579 | 2025-10-16 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 988fbcc9-9a0d-3913-85a0-67876af816f0 | -10.673 | -45.3125 | 2025-10-16 13:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| dd2193d7-3897-368f-bccf-5ea7861399bf | -10.6169 | -45.2512 | 2025-10-16 13:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 9bfc5ec1-8ddf-300b-8ad0-7a743ffefcd5 | 1.7479 | -56.0791 | 2025-10-16 13:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 272c619d-97a0-379d-a9e0-ecce5a5aba74 | -11.5917 | -44.0707 | 2025-10-16 13:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 9e34adaf-8e02-32d3-bc3b-5051a00fb60b | -10.6539 | -45.3151 | 2025-10-16 13:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 111.6 |
| ecb60f4a-9af2-312f-8a2b-81fc0a094a71 | -11.572 | -44.0971 | 2025-10-16 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| afd6baff-e8e5-3247-8457-f592d0c0c2b7 | -11.5729 | -44.0501 | 2025-10-16 13:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 4a421327-0a5b-3687-ae5e-a5029e078f16 | -9.2255 | -48.6 | 2025-10-16 13:10:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 3b3eabab-79b9-3688-a10c-53fbb82620b8 | -11.5724 | -44.0736 | 2025-10-16 13:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 149.5 |
| c7fd7081-1445-394c-8843-8e07faa7828a | -10.6214 | -47.4155 | 2025-10-16 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| ce002497-cd66-34e9-9664-8f4ecbc0a23b | -10.514 | -43.3815 | 2025-10-16 13:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 50fa06a9-f6eb-38fe-aebb-ff46960294ff | -11.2862 | -44.0226 | 2025-10-16 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 390.2 |
| 4e423864-cd12-30ce-ac18-eb5d574ddde5 | -12.3116 | -45.6081 | 2025-10-16 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 75e61bc1-e6a3-3988-b3cc-8dc321fcc0bc | -12.9179 | -47.1078 | 2025-10-16 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 6e849e54-f8ca-3a99-ba2e-f174f12ef720 | -10.8289 | -43.9482 | 2025-10-16 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |


[Clique aqui para ver as próximas entradas](README90.md)
