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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ba47d01-231b-3187-b825-510595b87c3a | -6.3679 | -45.7609 | 2025-10-18 02:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| bff1ff7e-88a9-3f01-8cda-01042cd43f62 | -11.6104 | -44.0913 | 2025-10-18 02:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 91089822-0a3b-3188-82a0-e42e7babf9b5 | -11.6297 | -44.0884 | 2025-10-18 02:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 0b483610-ee39-38ec-8c4d-8ee7934cd255 | -18.3891 | -41.8441 | 2025-10-18 02:40:00 | GOES-19 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 101.0 |
| 38a53b8c-7b73-3bbf-bf37-a26b89f5a5bd | -18.4094 | -41.8387 | 2025-10-18 02:40:00 | GOES-19 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 135.1 |
| b9e55c86-a677-3b5b-ad9d-12fb1729ac92 | -6.5261 | -44.8887 | 2025-10-18 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 4434c6c3-402c-3307-b4ac-2f115399391f | -18.3899 | -41.8187 | 2025-10-18 02:40:00 | GOES-19 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.5 |
| fceaba5b-d115-3738-8ab8-e695d8ceeb6c | -12.6135 | -52.8202 | 2025-10-18 02:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 103.5 |
| dc6ca1e0-6cb7-3799-b5d5-7982386a728c | -10.5128 | -43.4525 | 2025-10-18 02:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| cf58f374-3997-3236-b1d1-071c9bf2544f | -10.4937 | -43.4552 | 2025-10-18 02:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| cf959dcd-a6fc-3547-b85d-ed3e2641ea2a | -8.6032 | -40.1834 | 2025-10-18 02:40:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 121.1 |
| d3e5c981-8a5e-3a24-9503-dd71a8c406dd | -5.0215 | -46.0097 | 2025-10-18 02:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 151.5 |
| 7d9f076f-097f-3dc7-8427-9918d6cd3983 | -8.389 | -46.2333 | 2025-10-18 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 01989822-16b5-31f1-94fd-0cc5a81fb7e3 | -3.1431 | -50.2464 | 2025-10-18 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| d38fe4ec-8842-33c8-b900-b431d517d297 | -11.6109 | -44.0678 | 2025-10-18 02:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 12449146-c856-34e7-b51b-25dabb9245f5 | -12.5944 | -52.8223 | 2025-10-18 02:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| c1851784-e416-3c6c-a265-531151e7f8c3 | -6.5259 | -44.9114 | 2025-10-18 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| f6e24dd8-51d6-35c8-959f-ba7ba8dea294 | -18.4102 | -41.8133 | 2025-10-18 02:40:00 | GOES-19 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 119.2 |
| 4acd3b5e-1669-372c-9306-d60d8f58652b | -10.1528 | -44.5289 | 2025-10-18 02:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 7b9ed5e2-0add-3b63-85ff-0e5a7308bb2d | -11.6109 | -44.0678 | 2025-10-18 02:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 8617aa77-8d17-3f8a-a1c7-5e7e6ebf7a47 | -4.4446 | -43.2164 | 2025-10-18 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 66740d6b-92d3-3b27-a577-da7eb850f449 | -4.4632 | -43.2386 | 2025-10-18 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| d7efc5f0-2dfd-3d28-ba30-ae9006c69723 | -8.6029 | -40.2083 | 2025-10-18 02:50:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 83eae451-6878-30f4-89b5-55442d182848 | -5.0215 | -46.0097 | 2025-10-18 02:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 107.9 |
| a200d843-9f8f-3ea1-9fca-b61a3ef27676 | -4.4445 | -43.2397 | 2025-10-18 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| fe1b0b9c-9dc2-3725-b253-686fc87fbe4f | -12.6135 | -52.8202 | 2025-10-18 02:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 0714eaf3-5143-39a8-b661-effe90805770 | -11.204 | -47.8318 | 2025-10-18 02:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 8f6e50d2-e667-3adb-8ee7-931fca19bddb | -10.4941 | -43.4315 | 2025-10-18 02:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 0be0e863-62bd-3b39-b830-80fc1af3e3da | -18.4094 | -41.8387 | 2025-10-18 02:50:00 | GOES-19 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 114.1 |
| fe9d5447-07fe-3121-bb73-e3da45575137 | -5.0214 | -46.032 | 2025-10-18 02:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 80.7 |
| bb053c5e-fc86-377f-b7a2-88cf21f358be | -10.1528 | -44.5289 | 2025-10-18 02:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| e6a473b5-2697-3170-815c-58d9f6f756e4 | -11.6104 | -44.0913 | 2025-10-18 02:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 6d7c6339-3112-3c0b-bfe3-6c3841c735e6 | -3.1431 | -50.2464 | 2025-10-18 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 49a90edc-85ef-3cda-b517-55af356001ca | -18.4102 | -41.8133 | 2025-10-18 02:50:00 | GOES-19 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.0 |
| 66220766-cadd-31c7-8335-4ad6972b54fd | -8.6032 | -40.1834 | 2025-10-18 02:50:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 95.3 |
| 86aff390-e4c7-3674-bd82-3b13b5f324c8 | -12.6138 | -52.7993 | 2025-10-18 02:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 6852965b-7d50-3aa5-9f87-8101e7d76fb2 | -18.3899 | -41.8187 | 2025-10-18 02:50:00 | GOES-19 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.4 |
| 12485e9c-5cf5-304c-9fdc-6c932942153a | -4.4633 | -43.2152 | 2025-10-18 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| bec350fc-43fd-3b36-ace2-8675a37aedd8 | -10.4937 | -43.4552 | 2025-10-18 02:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 7b6f240d-f738-33d0-858d-d76cce4fd8ae | -18.3891 | -41.8441 | 2025-10-18 02:50:00 | GOES-19 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.4 |
| 0a370baa-b68f-3998-8e5a-086c16ec33b3 | -12.5944 | -52.8223 | 2025-10-18 02:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| cfc3dd27-7010-39cc-bee1-22e86f49cf85 | -10.1718 | -44.5264 | 2025-10-18 02:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 35605e3d-e977-3d58-add4-ad58a0af4cff | -5.0027 | -46.0331 | 2025-10-18 02:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 61.2 |
| de893648-663e-33d4-9d21-b3675cda901a | -5.0029 | -46.0108 | 2025-10-18 02:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 81.5 |
| f16b1180-972f-38f2-ac25-228783a7aa10 | -11.6104 | -44.0913 | 2025-10-18 03:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| d742bab5-b163-3ab6-ac5b-24602a53210b | -5.0215 | -46.0097 | 2025-10-18 03:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 95.2 |
| fcd19ab6-c1af-30da-a308-c673450a6fa9 | -10.4941 | -43.4315 | 2025-10-18 03:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 152.8 |
| a43bee2e-f0ab-3610-9a62-96bdd5429303 | -12.6135 | -52.8202 | 2025-10-18 03:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 1a385a02-5ee0-32a1-8a18-7cbf2ce1c979 | -3.1431 | -50.2464 | 2025-10-18 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| a2c5a822-2de1-3fb0-b9a0-b1cecc13bb7b | -18.4094 | -41.8387 | 2025-10-18 03:00:00 | GOES-19 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.8 |
| acd90ea7-bf23-3d34-8c4b-342cb439b356 | -5.0214 | -46.032 | 2025-10-18 03:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 360f7db0-59f6-3796-8e97-2697f188fab6 | -12.6138 | -52.7993 | 2025-10-18 03:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 2e219691-ac15-3830-84f8-33aefe6f056c | -10.1528 | -44.5289 | 2025-10-18 03:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 63.1 |
| c45be65f-b208-3d7e-90f1-f2195184d0f6 | -4.4445 | -43.2397 | 2025-10-18 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 70d6b0c2-ced2-3371-9e26-a2625f90ea12 | -11.204 | -47.8318 | 2025-10-18 03:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 7c33bae4-39ae-3d18-bdad-f1abb3dfd68a | -11.6109 | -44.0678 | 2025-10-18 03:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| ddce5f3d-f61d-3478-a2e5-e61e9bb6da9a | -10.4937 | -43.4552 | 2025-10-18 03:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| ef89fe40-3e68-35da-8b8b-1c8ee5eb9183 | -4.4632 | -43.2386 | 2025-10-18 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| c9a3c4a6-5fcf-31e4-9d7a-06e188ab4214 | -4.4446 | -43.2164 | 2025-10-18 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| fed56b73-279f-371f-8efc-bf94ba1ba622 | -8.6029 | -40.2083 | 2025-10-18 03:00:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 73.8 |
| 3095cd94-cc13-302d-85e6-fa5a7a4ba9c9 | -8.6032 | -40.1834 | 2025-10-18 03:00:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 78.8 |
| b540cdc7-6fd6-35f6-a9f4-12d0f04a32fb | -19.1114 | -57.5486 | 2025-10-18 03:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 57.3 |
| d3e64eea-6238-327f-b2a9-4653dad96250 | -18.4102 | -41.8133 | 2025-10-18 03:00:00 | GOES-19 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.3 |
| 8ba35258-f62b-3b89-8404-71427d569d79 | -10.4941 | -43.4315 | 2025-10-18 03:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 629f22dd-fe8c-3848-a6f5-822f51d41109 | -5.0215 | -46.0097 | 2025-10-18 03:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 9f7cb3a4-ecd9-3ecc-bb25-29587cb9c562 | -3.1431 | -50.2464 | 2025-10-18 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 80e103b7-788d-36d1-975b-db55692e0bf5 | -11.6104 | -44.0913 | 2025-10-18 03:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 9a30fc96-5fb0-3c91-ac51-147226cf5cf4 | -11.6109 | -44.0678 | 2025-10-18 03:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| f6a58953-4dcb-3cee-b896-86e30b4470d9 | -18.4094 | -41.8387 | 2025-10-18 03:10:00 | GOES-19 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.4 |
| e1fa9e7a-3e20-31fd-96b8-dcbfe15d62c2 | -19.1114 | -57.5486 | 2025-10-18 03:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 56.6 |
| 22cda649-7d70-3a24-a323-49a1aea65f51 | -12.6135 | -52.8202 | 2025-10-18 03:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 65d4a3ab-7582-3ae2-9850-b3801395ebe8 | -11.204 | -47.8318 | 2025-10-18 03:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| f80048f8-a846-3376-aea1-bb7f7f4a5036 | -8.4079 | -46.2314 | 2025-10-18 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| d549f6ea-83ca-3b58-8c6f-d7987d6da6ec | 1.7664 | -55.9608 | 2025-10-18 03:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 2abd3975-c2ec-34cb-a310-8278764bb335 | -10.4937 | -43.4552 | 2025-10-18 03:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 29683a68-72a8-3b0a-9998-eb91f191912a | -8.389 | -46.2333 | 2025-10-18 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 6572a0ea-b6c7-357d-8f04-3232c05b03d5 | -10.475 | -43.4342 | 2025-10-18 03:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| ec0ed4ab-40b1-3500-b002-4c1ddff5fd8e | 1.7664 | -55.9805 | 2025-10-18 03:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 1952b8e0-deb4-3586-bae9-aaad05e1ce08 | -12.6138 | -52.7993 | 2025-10-18 03:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 4688b36f-97bb-3fb0-be50-4dc7fc3c9840 | -5.0214 | -46.032 | 2025-10-18 03:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 312df3ec-03bc-3817-87a7-884ee8e639bf | -10.62006 | -42.30592 | 2025-10-18 03:10:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 674869fc-8229-3840-9eeb-145d6f674bde | -10.63204 | -42.30942 | 2025-10-18 03:10:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 61933cbc-7438-3529-8db1-ba700a35a4aa | -8.60895 | -40.19315 | 2025-10-18 03:10:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 5a4b054c-d8ec-3fa5-b212-19d02b6ece09 | -10.6249 | -42.30782 | 2025-10-18 03:10:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 64d9d22d-1261-3d45-a650-e6e2c8afdc20 | -7.81886 | -40.21131 | 2025-10-18 03:10:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 07d6944b-f126-36ac-a33c-22b8b38515e0 | -8.6056 | -40.201 | 2025-10-18 03:10:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 25.8 |
| c5516870-c5e1-3910-8bd0-ee5b0ad5818b | -8.61215 | -40.20238 | 2025-10-18 03:10:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 7f3b4f87-e2e0-3ccd-8e01-811b6cfde6cb | -11.84565 | -38.20347 | 2025-10-18 03:10:00 | NOAA-20 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 48449440-8f73-3208-b642-375fda0fcf10 | -7.02084 | -38.5129 | 2025-10-18 03:10:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aca972e3-df75-35d3-94a2-59544901535e | -8.60673 | -40.19522 | 2025-10-18 03:10:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 40.5 |
| e0523bb4-6d58-375b-9903-3de17761178b | -11.84013 | -38.20244 | 2025-10-18 03:10:00 | NOAA-20 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f3cbc91e-d35f-3ec1-af5d-cd2a6b24d98c | -8.60785 | -40.19896 | 2025-10-18 03:10:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 05f702ca-fb43-3be1-bd8b-3a3d9185eb95 | -6.9759 | -39.6971 | 2025-10-18 03:10:00 | NOAA-20 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| cd2bc259-24c2-3728-b033-09c9f1f30f91 | -6.98238 | -39.69152 | 2025-10-18 03:10:00 | NOAA-20 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 79fa1ef1-21fb-3786-865e-f481d3992a2a | -6.97676 | -39.6924 | 2025-10-18 03:10:00 | NOAA-20 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 85000e8f-a1b4-3eea-98bb-ad06b3522d54 | -10.62721 | -42.30747 | 2025-10-18 03:10:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8e2eef76-7391-3ef1-be25-da7cf832e34a | -7.54789 | -37.7914 | 2025-10-18 03:10:00 | NOAA-20 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 75ef7f08-c820-3699-86f1-523f23c1974d | -8.23081 | -39.039 | 2025-10-18 03:10:00 | NOAA-20 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 915d070f-551b-35d8-998f-37d0786ceca7 | -8.60242 | -40.19167 | 2025-10-18 03:10:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 9.6 |
| ac2f4e88-1a2e-3ef2-85b1-592051ae7c3d | -8.60022 | -40.2033 | 2025-10-18 03:10:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |


[Clique aqui para ver as próximas entradas](README11.md)
