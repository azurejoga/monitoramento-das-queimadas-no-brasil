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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b774b211-7b4c-3772-a0f4-e36d963dfccb | -19.9181 | -44.497398 | 2024-10-07 00:25:09 | METOP-B | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 540d9e79-c7ff-3d62-86c4-ba2286cc66a6 | -19.9196 | -44.5047 | 2024-10-07 00:25:09 | METOP-B | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3a61c8ae-cfeb-3b32-85c2-6fec61a9d04d | -18.4604 | -46.6535 | 2024-10-07 00:25:09 | METOP-B | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d52565aa-7008-308a-8f13-e6437a26c870 | -18.5888 | -47.287498 | 2024-10-07 00:25:09 | METOP-B | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 03cad65e-0b21-3995-b60d-6b13df58e155 | -18.5905 | -47.296299 | 2024-10-07 00:25:09 | METOP-B | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8b9c53c2-e193-34ea-a8f3-aa0934fa6f0c | -18.5923 | -47.305099 | 2024-10-07 00:25:09 | METOP-B | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 83fb14b1-6258-333d-aca5-4f4b093406b9 | -19.1635 | -50.613602 | 2024-10-07 00:25:10 | METOP-B | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1cfa7918-986a-3739-9632-7151bb117fb2 | -20.476601 | -47.654999 | 2024-10-07 00:25:11 | METOP-B | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b5b8f38a-2a0e-318e-bf06-9a7e85003af3 | -19.492599 | -42.8736 | 2024-10-07 00:25:11 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 925966bb-3584-3b8f-844f-e181597faff7 | -19.4942 | -42.880901 | 2024-10-07 00:25:11 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 26e08c61-37f4-33d6-9b3f-7e2dd7b04fe5 | -20.4729 | -47.6357 | 2024-10-07 00:25:11 | METOP-B | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b5203a64-d937-3e22-b210-aa3f30257650 | -20.4748 | -47.645401 | 2024-10-07 00:25:11 | METOP-B | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 02c43e79-be78-3409-8d0c-7be713ef1504 | -20.465 | -47.647499 | 2024-10-07 00:25:11 | METOP-B | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0597fd6c-7f75-36b9-aca1-29be57c9b2cf | -20.4669 | -47.657101 | 2024-10-07 00:25:11 | METOP-B | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c9d9e37a-1137-3330-848d-6489746ce850 | -17.607599 | -43.25 | 2024-10-07 00:25:11 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d45693e6-ff3f-359d-8cd3-e18b53d7fa75 | -17.6092 | -43.257301 | 2024-10-07 00:25:11 | METOP-B | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 469ed6fd-8744-3036-a7b5-a79cb4b325c7 | -1.0182 | -53.739 | 2024-10-07 00:25:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| fae9a62e-974b-30cd-b513-ff310c9e9e82 | -1.0182 | -53.7189 | 2024-10-07 00:25:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 8d973e8e-6392-361e-8a42-7441d11d3413 | -1.0365 | -53.7389 | 2024-10-07 00:25:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| db275f3e-a0cf-36cd-9b9c-bd568ee0a68f | -1.0365 | -53.7187 | 2024-10-07 00:25:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 4f3f8282-aed5-3707-b289-573fc62c5935 | -18.242399 | -46.389801 | 2024-10-07 00:25:12 | METOP-B | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 04cc7343-cd89-350d-963d-dc964ee3c0d4 | -19.278099 | -42.560501 | 2024-10-07 00:25:13 | METOP-B | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 08bba94e-2961-3fda-88ab-6975300eaf29 | -19.2798 | -42.567902 | 2024-10-07 00:25:13 | METOP-B | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 85ae56c1-e7ee-3e97-9c4f-11d46832907e | -19.194599 | -42.510601 | 2024-10-07 00:25:14 | METOP-B | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dffeb3d7-755b-351c-a887-de780dacfaea | -19.196301 | -42.518002 | 2024-10-07 00:25:14 | METOP-B | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b3613f2c-d1ee-3b33-bdfa-a7b35c5004ec | -20.457199 | -48.620899 | 2024-10-07 00:25:14 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7a774d74-cbaa-36d0-b642-5bea6aeedf9f | -18.298901 | -47.1166 | 2024-10-07 00:25:14 | METOP-B | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e6861786-6b63-30da-856b-902c7905eaa5 | -18.3006 | -47.125198 | 2024-10-07 00:25:14 | METOP-B | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1db584ea-d194-383f-963b-d8befe0ea814 | -17.564199 | -43.7024 | 2024-10-07 00:25:14 | METOP-B | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a92b7dd1-acd6-3ec4-85f0-66f4fd34e44d | -17.5658 | -43.709499 | 2024-10-07 00:25:14 | METOP-B | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3b318efe-099b-3a6e-af9d-5ad6000b5e9f | -17.5396 | -43.730999 | 2024-10-07 00:25:14 | METOP-B | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e7a9c194-5b0f-3fa4-abe5-65a1cb5dcc3f | -17.541201 | -43.738201 | 2024-10-07 00:25:14 | METOP-B | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2fcdf70d-bb8f-3711-bea8-ba0707e2f244 | -17.542801 | -43.745399 | 2024-10-07 00:25:14 | METOP-B | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| aad28731-5bb2-3d22-9641-58ab11accb22 | -17.544399 | -43.752499 | 2024-10-07 00:25:14 | METOP-B | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1b5c0030-4b02-3b06-84f2-b85b0a33e8f8 | -17.546 | -43.759701 | 2024-10-07 00:25:14 | METOP-B | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a1a243f4-eb54-3ced-b774-783f48de0a68 | -17.5476 | -43.766899 | 2024-10-07 00:25:14 | METOP-B | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 97b9fef5-e984-3baf-ae6a-d3f6c3ad7dff | -17.549101 | -43.774101 | 2024-10-07 00:25:14 | METOP-B | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 51bb4b64-764e-3c04-9d19-781bb0067773 | -19.759399 | -45.3041 | 2024-10-07 00:25:15 | METOP-B | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7e88647c-7e40-3b71-b570-bda3fcc22b76 | -19.761 | -45.311699 | 2024-10-07 00:25:15 | METOP-B | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| af3572a3-a3f7-3791-b473-27ac6a6974cc | -19.7626 | -45.319401 | 2024-10-07 00:25:15 | METOP-B | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 053d304a-264b-34f8-a25b-4c70228f7283 | -18.322599 | -47.539001 | 2024-10-07 00:25:15 | METOP-B | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1d2730c0-1c2b-362c-8b5d-1e9f681112c7 | -18.3244 | -47.547901 | 2024-10-07 00:25:15 | METOP-B | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e995f9cc-92a1-3f6f-8aef-254fdfb789d3 | -18.312799 | -47.5411 | 2024-10-07 00:25:15 | METOP-B | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a9c9186f-bcba-3d4a-947f-ec10dc564577 | -18.3146 | -47.549999 | 2024-10-07 00:25:15 | METOP-B | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7f8e439d-528c-3fb2-be15-796cfdf13e17 | -19.064301 | -42.527199 | 2024-10-07 00:25:16 | METOP-B | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 76be1bdb-726a-3bc4-bb88-7666cbfe5587 | -19.066 | -42.534698 | 2024-10-07 00:25:16 | METOP-B | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8bfc4908-84ec-3e96-b13e-ac9420c75ba7 | -19.127199 | -42.715199 | 2024-10-07 00:25:16 | METOP-B | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 430f5ffc-fcce-3dfa-8ee0-394c8c4e6502 | -19.128901 | -42.722599 | 2024-10-07 00:25:16 | METOP-B | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c09d188a-914b-35d8-9292-13429209dc33 | -19.1306 | -42.73 | 2024-10-07 00:25:16 | METOP-B | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 34386826-40d8-3fc9-8e23-61fb0073fc12 | -19.119101 | -42.724998 | 2024-10-07 00:25:16 | METOP-B | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1beab6b9-a0e3-3f33-ab8a-3f29a5d90dc6 | -19.974501 | -46.811001 | 2024-10-07 00:25:16 | METOP-B | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6f0a8948-1a74-3f56-97c9-bec25d2c250a | -19.968201 | -46.830502 | 2024-10-07 00:25:16 | METOP-B | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f09cc626-303e-3830-a757-67617a0a92f2 | -19.229601 | -43.360901 | 2024-10-07 00:25:17 | METOP-B | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e05a8383-72cf-3fc8-b0ed-a14a9b7e4330 | -19.871799 | -46.451698 | 2024-10-07 00:25:17 | METOP-B | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 900f4ea8-66dd-3a43-9a9b-6384d5096e9f | -19.873501 | -46.460098 | 2024-10-07 00:25:17 | METOP-B | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 867e2e64-7be8-392c-b4aa-239dc483b97d | -20.0366 | -47.749401 | 2024-10-07 00:25:18 | METOP-B | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| efce515b-f7b2-3232-8de4-1164cfcd587f | -20.0385 | -47.758999 | 2024-10-07 00:25:18 | METOP-B | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1230ed5c-05a5-3356-9fa5-5bcd901414f2 | -20.0403 | -47.7687 | 2024-10-07 00:25:18 | METOP-B | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4a33d01a-2776-3f3e-95c3-28e34cb042e7 | -2.2113 | -53.7029 | 2024-10-07 00:25:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 7578407b-b43e-311f-9a65-f2a0c56e5a34 | -2.2114 | -53.6828 | 2024-10-07 00:25:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 724ab5d2-338f-365b-aa65-ac210e232300 | -2.2297 | -53.7026 | 2024-10-07 00:25:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 26679cf6-9d47-30d8-b6a5-c5182905d57e | -2.2297 | -53.6824 | 2024-10-07 00:25:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 4d433129-e5a0-3a58-b39a-f0bd4068fc1b | -19.820801 | -46.8088 | 2024-10-07 00:25:19 | METOP-B | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5391837e-7d65-38fd-9309-b270620a8062 | -19.1019 | -43.5294 | 2024-10-07 00:25:19 | METOP-B | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a3ae3b77-b54c-3fdc-91e4-47b5e2f2ad4a | -19.0921 | -43.5317 | 2024-10-07 00:25:19 | METOP-B | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4c43e75b-cc8a-3d2a-be07-0ca252b63209 | -19.0937 | -43.539001 | 2024-10-07 00:25:19 | METOP-B | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 17b3fa51-4682-3e01-8233-02550248e762 | -18.6227 | -41.500198 | 2024-10-07 00:25:20 | METOP-B | SÃO FÉLIX DE MINAS | MINAS GERAIS | Brasil | 3161056 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7e6a9973-cfc8-3b73-8cee-75dfc9cbebe7 | -18.6129 | -41.502701 | 2024-10-07 00:25:20 | METOP-B | SÃO FÉLIX DE MINAS | MINAS GERAIS | Brasil | 3161056 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5e13cedc-f616-32f5-8c8a-e6dadad9bc09 | -18.620899 | -41.492199 | 2024-10-07 00:25:20 | METOP-B | SÃO FÉLIX DE MINAS | MINAS GERAIS | Brasil | 3161056 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6b5101be-ba3f-3031-9712-1057a884a16b | -18.599501 | -41.489201 | 2024-10-07 00:25:20 | METOP-B | SÃO FÉLIX DE MINAS | MINAS GERAIS | Brasil | 3161056 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c7eb3d8d-93c8-3dea-a62d-8036c1e2edbb | -18.6014 | -41.4972 | 2024-10-07 00:25:20 | METOP-B | SÃO FÉLIX DE MINAS | MINAS GERAIS | Brasil | 3161056 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 90cfd713-0e12-30e6-87c0-a0c5ffed93ae | -18.954599 | -43.3284 | 2024-10-07 00:25:21 | METOP-B | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3d110cf0-0846-3fb2-95b6-3f2a97c93962 | -18.9562 | -43.335701 | 2024-10-07 00:25:21 | METOP-B | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e8d29533-0ed9-3f85-962a-a90be9e64f91 | -20.1269 | -49.026001 | 2024-10-07 00:25:21 | METOP-B | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 52bde14c-002f-35c7-949a-e0b46b30ea20 | -18.855499 | -42.883301 | 2024-10-07 00:25:21 | METOP-B | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f0ece814-cf0e-351c-b987-1126aa0a9296 | -18.857201 | -42.890598 | 2024-10-07 00:25:21 | METOP-B | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8d9187ff-eb54-3000-8ac3-89385d7d2739 | -20.115101 | -49.016602 | 2024-10-07 00:25:21 | METOP-B | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 22a3079a-e858-3307-bd25-defa58ba4b3b | -20.117201 | -49.028 | 2024-10-07 00:25:21 | METOP-B | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 734c1541-b679-39ea-a2eb-d42d1a6f9b4e | -20.119301 | -49.039398 | 2024-10-07 00:25:21 | METOP-B | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| da6ac5a8-efd2-345b-910b-b3b0931e15fd | -20.1215 | -49.0509 | 2024-10-07 00:25:21 | METOP-B | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2df8d167-10cf-30b6-8d90-e8848fcc4f43 | -20.107401 | -49.029999 | 2024-10-07 00:25:21 | METOP-B | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 00800ee3-3f06-31d7-8da6-0c9b6ae73ce7 | -20.1096 | -49.041401 | 2024-10-07 00:25:21 | METOP-B | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0eff6a6c-0fcd-39b7-be7e-7c6a83b86905 | -2.8569 | -52.9197 | 2024-10-07 00:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 170.9 |
| 283a60d0-6e38-336c-80fb-d9d616fb0511 | -2.857 | -52.8993 | 2024-10-07 00:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 195.5 |
| d760403a-8de3-33c8-b063-02a616b48c9d | -2.8753 | -52.9192 | 2024-10-07 00:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 257.7 |
| 5880a022-2f29-330c-812a-5f265192148f | -2.8754 | -52.8989 | 2024-10-07 00:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 352.7 |
| ca519814-2357-3aef-a694-e5c8fcf858f7 | -2.8937 | -52.9188 | 2024-10-07 00:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 5cd39a5f-b4f2-33ec-932a-00bf0ebe4e0a | -2.8937 | -52.8984 | 2024-10-07 00:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 532fa3db-1745-37f9-89b6-28426df7d852 | -18.842899 | -43.569099 | 2024-10-07 00:25:24 | METOP-B | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 04fb541a-7e2c-3e3e-b855-f7f51917feb0 | -18.3197 | -41.441399 | 2024-10-07 00:25:24 | METOP-B | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e26f5c67-6092-3837-9221-7b774f91fc03 | -17.619101 | -46.942699 | 2024-10-07 00:25:24 | METOP-B | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6124139a-8409-3b3e-83d0-0205bf3d8fa3 | -3.2956 | -49.1415 | 2024-10-07 00:25:25 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| e9af4b6e-4989-3e02-a28a-89ad6b805c68 | -18.6649 | -43.276501 | 2024-10-07 00:25:25 | METOP-B | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e79dbce5-bba1-3475-86b6-b27297a57f9e | -18.6665 | -43.283798 | 2024-10-07 00:25:25 | METOP-B | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 83e19940-cef9-33e7-8e31-5c6929bd21ed | -17.889099 | -48.593899 | 2024-10-07 00:25:25 | METOP-B | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 72e06f22-71b9-3d0e-9bdb-b72f3668be4b | -17.8911 | -48.603901 | 2024-10-07 00:25:25 | METOP-B | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5f87b09a-f3ac-35ae-b4c9-30af83908ec7 | -17.8794 | -48.596001 | 2024-10-07 00:25:25 | METOP-B | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9d933531-fa41-3879-a141-0701e72945e8 | -18.4596 | -42.408901 | 2024-10-07 00:25:26 | METOP-B | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bcf9711e-cc44-3524-919e-8b0a336bfbc5 | -18.4613 | -42.416401 | 2024-10-07 00:25:26 | METOP-B | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f8725afc-0a59-37e1-9c7f-24ceeb9a2a03 | -18.462999 | -42.423901 | 2024-10-07 00:25:26 | METOP-B | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README6.md)
