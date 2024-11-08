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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22d155e4-0c9a-3025-8c6e-0929566dc4e2 | -5.9903 | -45.3615 | 2024-11-08 00:10:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33ed7a72-7d4e-382c-af8d-9e8589af5f19 | -5.6372 | -44.240398 | 2024-11-08 00:10:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 908af90f-b859-35bf-a007-d80bac0d0f7b | -2.7023 | -45.6908 | 2024-11-08 00:10:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 26fef3f9-5971-3e71-ba7a-c179e9e141d5 | -6.2575 | -39.373699 | 2024-11-08 00:10:00 | METOP-C | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3cf7ff4c-1f53-3166-bb25-d2eb5d469171 | -2.8309 | -45.213902 | 2024-11-08 00:10:00 | METOP-C | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9bc2ea71-3dbe-374d-afa7-24519e7a6f29 | -7.176 | -37.9207 | 2024-11-08 00:10:00 | METOP-C | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 2cdb71e2-fd87-38b7-9ccb-c49003e166c0 | -7.0311 | -43.572399 | 2024-11-08 00:10:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1fb65027-d344-3056-be9e-7f8080219f6f | -3.0624 | -45.736301 | 2024-11-08 00:10:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f143656d-af59-31c5-bfbb-a32821a97f81 | -3.6876 | -43.724701 | 2024-11-08 00:10:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| edb672ff-f166-3bdd-a5cb-948f53536c9b | -2.8703 | -46.751598 | 2024-11-08 00:10:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92d3e85e-6b88-3c4f-a9c4-81ac6be9acf4 | -5.0795 | -47.920502 | 2024-11-08 00:10:00 | METOP-C | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 98be2b38-3a0a-3b44-b25c-c466e50ae740 | -3.7071 | -41.6889 | 2024-11-08 00:10:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a4423c0c-b6bb-3dfd-8740-6a3fae5d0260 | -2.4406 | -46.306301 | 2024-11-08 00:10:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f9becabc-6e99-3a0e-92e9-aec1dfced001 | -5.9203 | -44.862099 | 2024-11-08 00:10:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 516e6c97-4491-3504-8df4-82b198abee11 | -7.4795 | -43.5532 | 2024-11-08 00:10:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3a1fc686-6ae0-3ed0-a479-c000dd949185 | -3.2818 | -45.7966 | 2024-11-08 00:10:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7775aeee-bdb7-3857-b958-a78c78a68e3f | -2.9004 | -45.611801 | 2024-11-08 00:10:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a40d6c9f-e819-3c91-b111-5ee2c56ce20f | -3.8561 | -40.767601 | 2024-11-08 00:10:00 | METOP-C | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bbbab2f0-917f-3953-aaa5-8544f2db8334 | -3.15 | -45.305 | 2024-11-08 00:10:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 008a2081-a44a-33a1-8f6f-dab89716466e | -2.8649 | -46.773201 | 2024-11-08 00:10:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 446da7e7-8b53-3baf-a3eb-1087d6bb2191 | -9.7531 | -36.341499 | 2024-11-08 00:10:00 | METOP-C | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b4e6cb6e-8a74-3013-b7b6-7323cd5639de | -3.381 | -46.099899 | 2024-11-08 00:10:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e2dfb26c-0056-3ae5-8bc1-0f0c1fd16846 | -6.2663 | -39.544201 | 2024-11-08 00:10:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9c472002-e6da-3da6-ac28-02268f77eeac | -4.3049 | -45.6824 | 2024-11-08 00:10:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1c912552-d4a5-321f-be07-5d884bc1cb31 | -3.5475 | -47.388699 | 2024-11-08 00:10:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b709f261-6b6b-36b8-bfa8-4c2c94689d8c | -2.8627 | -46.7635 | 2024-11-08 00:10:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96304dbf-8933-39e6-89bc-44f259c87602 | -3.2369 | -45.688999 | 2024-11-08 00:10:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e6fd8fbe-71ab-317e-95a3-1d0e3de7bf64 | -5.9268 | -43.650902 | 2024-11-08 00:10:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30eabb89-6984-31b8-877c-d417e248ac28 | -3.0172 | -45.809299 | 2024-11-08 00:10:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 195a33f0-085e-3e01-a497-85e42b3e124b | -10.0162 | -36.318199 | 2024-11-08 00:10:00 | METOP-C | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 9b322f38-4059-3fd1-b0bd-724815046f68 | -3.2482 | -46.467999 | 2024-11-08 00:10:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 91332244-a7ad-3fe1-aa81-dc159be8b9ad | -3.1383 | -45.298901 | 2024-11-08 00:10:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ac003a79-217b-3fab-b3d2-3abd499f00c6 | -3.4456 | -46.066799 | 2024-11-08 00:10:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 57b83ea2-80e2-3a0a-87a1-55f266ff53ee | -8.8528 | -39.881001 | 2024-11-08 00:10:00 | METOP-C | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b5fdc0f5-0c2f-331a-9ba4-c442338a4b9f | -9.7555 | -36.3512 | 2024-11-08 00:10:00 | METOP-C | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4d2b4476-fbee-32cf-a2d6-5cdbba60d480 | -3.1603 | -45.805099 | 2024-11-08 00:10:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 508db31f-777e-3f25-9d1e-9c72ea3653e4 | -3.142 | -45.3153 | 2024-11-08 00:10:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c3ebcc00-1d7f-3869-90df-f126035e769b | -10.7088 | -44.898499 | 2024-11-08 00:10:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9d4f5531-7c46-3702-8571-8ec539fc3e6e | -5.0725 | -47.935101 | 2024-11-08 00:10:00 | METOP-C | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ae269ee6-d8a5-32b7-af92-01d846ecc1b3 | -3.4476 | -46.075802 | 2024-11-08 00:10:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cd01787e-0526-3589-9854-705950b3da0f | -9.0915 | -43.031399 | 2024-11-08 00:10:00 | METOP-C | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1baf8466-d7f7-3692-bbfe-33a66d02942f | -7.4778 | -43.545601 | 2024-11-08 00:10:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 164e1a95-0258-3b26-a110-0c4892233fe2 | -5.5765 | -43.148201 | 2024-11-08 00:10:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| fa6642d6-f4ef-3f5b-a45d-c9f71b2559a4 | -6.7456 | -39.253399 | 2024-11-08 00:10:00 | METOP-C | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 05939ef3-0ab8-348f-8abe-ef88eeb5fa45 | -5.9222 | -44.870499 | 2024-11-08 00:10:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7bab385a-6ddc-39c8-84aa-7fdb5e58e87f | -4.2004 | -44.259499 | 2024-11-08 00:10:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c56d16e2-c187-3cbf-84df-35cf542d685b | -4.5284 | -45.670601 | 2024-11-08 00:10:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 22f69cde-020f-3f8c-838d-32f6a84c9754 | -5.5847 | -43.138901 | 2024-11-08 00:10:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| ec035b31-9cce-3e7a-b849-5cd530586d72 | -4.5206 | -45.681599 | 2024-11-08 00:10:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 335a027f-e72c-3cf4-ad5b-49cab406f195 | -4.5587 | -45.851898 | 2024-11-08 00:10:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ceaada4b-34cf-3854-b1e8-422802b17cf3 | -7.0426 | -43.577801 | 2024-11-08 00:10:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| eaf89570-232b-3f32-b1b8-8c039315203d | -6.4956 | -39.553699 | 2024-11-08 00:10:00 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 551d8d7c-122f-358a-b770-4ea6532fa4c5 | -3.233 | -45.671902 | 2024-11-08 00:10:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 93f0f912-b77f-3b51-a1dc-0a7dfde438e1 | -2.0056 | -46.5648 | 2024-11-08 00:10:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b4a0529-7588-3917-a950-d823ce7461ae | -2.8725 | -46.761299 | 2024-11-08 00:10:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| baa564ba-1783-31aa-b74f-600897c90f87 | -4.6805 | -46.397499 | 2024-11-08 00:10:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4d724799-a155-3bc7-83ca-491e06f6e9f6 | -3.0259 | -45.120499 | 2024-11-08 00:10:00 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 896bded8-a322-3344-afff-fd2ffa07297e | -5.639 | -44.248199 | 2024-11-08 00:10:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ef1bbbc-0aac-33ff-858e-dad12986fedd | -4.5186 | -45.672798 | 2024-11-08 00:10:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e3c52a83-f6cc-345a-a6a8-e476c224a92e | -3.235 | -45.6805 | 2024-11-08 00:10:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5d180a17-e2f4-3125-9de6-52e77d5fa9e0 | -5.3936 | -45.1273 | 2024-11-08 00:10:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb8dede7-2df2-3ee8-b685-f4fef4286de1 | -8.1231 | -42.933201 | 2024-11-08 00:10:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a084215b-eaff-354e-b1d0-9e54b61da95b | -4.6936 | -46.363899 | 2024-11-08 00:10:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 21359251-3ccd-3aa1-ae81-731a8367746d | -4.2021 | -44.267101 | 2024-11-08 00:10:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 34d727a1-aa0d-304f-9f87-f07153c4033b | -3.1402 | -45.307098 | 2024-11-08 00:10:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c72009d8-aee9-3d91-b68c-ed180a74d146 | -2.8888 | -41.764702 | 2024-11-08 00:10:00 | METOP-C | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ddc6df5d-486a-3a1b-9363-768e41098462 | -3.7087 | -41.695801 | 2024-11-08 00:10:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 16d87714-b09f-396e-91de-321944917b66 | -4.5567 | -45.8428 | 2024-11-08 00:10:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eac33ee3-8215-3000-8a46-a36b8bf763f4 | -3.5346 | -44.366901 | 2024-11-08 00:10:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea82ec03-d5f3-39be-94c1-a646bd379d5b | -9.1495 | -43.153801 | 2024-11-08 00:10:00 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 60e5a9b4-2fb9-31b4-8a61-626dfdd67aa4 | -3.7056 | -41.682098 | 2024-11-08 00:10:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a4d058b7-6565-39ad-a30b-40fefb55d5e3 | -3.272 | -45.798801 | 2024-11-08 00:10:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9b2f8af3-d7d7-3fed-8a63-f9945849f426 | -3.15 | -44.3969 | 2024-11-08 00:10:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eeb3fc3a-f39d-3aec-8c12-386592973eac | -9.0932 | -43.038898 | 2024-11-08 00:10:00 | METOP-C | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4a424ec6-b293-304a-8baf-bb77a94f8d86 | -4.6827 | -46.407299 | 2024-11-08 00:10:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4e8d761d-794d-3744-b844-c1b143d2c23c | -7.5155 | -35.2076 | 2024-11-08 00:10:00 | METOP-C | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c18806e8-d99b-3e94-b3e2-74b07af8f175 | -7.5096 | -35.183201 | 2024-11-08 00:10:00 | METOP-C | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 79b7294b-3e2f-3c83-b9d2-655edc625fcf | -2.6821 | -45.964901 | 2024-11-08 00:10:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b3341059-5b8a-3662-a569-97e590dc6263 | -7.5057 | -35.209999 | 2024-11-08 00:10:00 | METOP-C | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9910a520-33f1-3571-bd3f-de128cb2e139 | -2.4426 | -46.315399 | 2024-11-08 00:10:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7708d292-5cc8-33c8-93ca-49e5355aedd4 | -2.7042 | -45.6992 | 2024-11-08 00:10:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a12a7a48-381a-3674-b6d4-6f020cc33eba | -7.0409 | -43.570202 | 2024-11-08 00:10:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5ffe7464-430c-3d15-8fa3-be3fca325c8e | -3.1517 | -44.4044 | 2024-11-08 00:10:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5698b5f1-7f54-3278-b524-286dd610e76a | -4.5226 | -45.690498 | 2024-11-08 00:10:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0894f09d-3e1a-3f85-9668-aa2b10653531 | -4.3029 | -45.673599 | 2024-11-08 00:10:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a6a8bed7-b83a-37f1-93d2-61581ddb7f89 | -7.5125 | -35.1954 | 2024-11-08 00:10:00 | METOP-C | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 11952b48-d5f6-30ad-9779-8fad872e18db | -8.5099 | -42.0867 | 2024-11-08 00:10:00 | METOP-C | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ecf4f585-6b51-370a-8c76-6cf2bdb7e166 | -7.5449 | -44.078701 | 2024-11-08 00:10:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 15c1ff4e-63d2-3101-beb6-fcdb833e1264 | -2.5894 | -47.009201 | 2024-11-08 00:10:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 109b3180-716c-31a3-ba42-5758cf27d100 | -3.0605 | -45.727798 | 2024-11-08 00:10:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| af133b0a-4776-37b2-b1cb-18e9cc6de120 | -9.7578 | -36.360802 | 2024-11-08 00:10:00 | METOP-C | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bf4567d2-ae62-3f4a-a0c7-ab6503a6c19f | -5.681 | -46.421001 | 2024-11-08 00:10:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d468632b-1272-3253-9404-88d6d6de3f63 | -4.1987 | -44.251999 | 2024-11-08 00:10:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b645fb42-ee28-313d-82a9-57428d1d5c79 | -4.5304 | -45.679501 | 2024-11-08 00:10:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fd71fea1-f7e9-3030-a7a2-53e76e0cc87d | -5.5863 | -43.146 | 2024-11-08 00:10:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 6109e976-504d-3325-94fb-3ffea129899e | -4.3167 | -45.689201 | 2024-11-08 00:10:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c92a5a46-a2e1-3d96-af31-9a6459bdff6e | -3.5427 | -47.367001 | 2024-11-08 00:10:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6f56b5e-3b78-3fda-93d2-602e005d5640 | -8.5115 | -42.0938 | 2024-11-08 00:10:00 | METOP-C | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8173684d-6526-3445-92d7-77d5ae09d2e0 | -5.6832 | -46.431099 | 2024-11-08 00:10:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 588f1e1b-238a-33a4-a26a-859b18bc7321 | -4.2755 | -45.688801 | 2024-11-08 00:10:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
