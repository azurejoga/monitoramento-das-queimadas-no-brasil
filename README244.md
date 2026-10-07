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

## Dados Diários - Página 244

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51c28aa6-94a6-32d7-8702-7e22d163a18c | -13.3676 | -43.8504 | 2026-10-07 17:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 6768cbb5-2c8d-3772-81fd-e95a8b26d56d | -11.7362 | -43.5068 | 2026-10-07 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 15878f04-0a39-333f-85ac-4016dffdd0e4 | -9.432 | -45.8293 | 2026-10-07 17:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 439dfc48-dc12-3a9c-be8b-5df895827256 | -2.8713 | -54.1518 | 2026-10-07 17:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 1a9d5e4a-6098-3847-b90b-db4863728ec9 | -9.8061 | -64.9979 | 2026-10-07 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 51dadb93-75d8-344a-bd8c-e547e7e22eee | -9.9596 | -43.5045 | 2026-10-07 17:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 157.7 |
| f419e42a-6e27-3ea4-b803-1e6b1706122a | -9.0399 | -46.9039 | 2026-10-07 17:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| f7dbbf50-a9e5-3c3e-a246-ed0bab4eea44 | -7.9178 | -70.9245 | 2026-10-07 17:50:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 036797b2-abd2-3bcd-87d0-72ead31b4d70 | -6.8292 | -39.5472 | 2026-10-07 17:50:00 | GOES-19 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 1860114a-bc58-324b-9f97-1155cdcfe4ef | -7.3085 | -73.0269 | 2026-10-07 17:50:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 7bc6b7c6-e470-3dde-b5e4-75ae07317aac | -9.4513 | -45.8044 | 2026-10-07 17:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| e4813ac7-0d34-3795-bb8d-8e8b5df83600 | -11.6186 | -43.6433 | 2026-10-07 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 31853d83-3cce-3efc-8230-acaebe3a5e77 | -11.6374 | -43.664 | 2026-10-07 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 2b2454f7-7ce9-3739-b160-53f3b913f7e0 | -11.6951 | -43.655 | 2026-10-07 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| e3ccd388-2a5a-308a-82ca-857745e46472 | -5.9649 | -40.914 | 2026-10-07 17:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 173.3 |
| ed3e5ff7-8402-3eb4-bfaa-f87d03080e6e | -7.8428 | -71.8203 | 2026-10-07 17:50:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 117.8 |
| bf795ea7-f85f-3d6f-86ec-1593c362005e | 1.8951 | -55.7224 | 2026-10-07 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| a7484927-1573-386b-b65f-647b081533da | -2.9449 | -54.1099 | 2026-10-07 17:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 154.6 |
| 2fa6b3d3-f27d-31e0-b78c-6f807c6712ce | -2.8714 | -54.1318 | 2026-10-07 17:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 08e3304a-329f-3cd7-9cc1-adcd2559ed92 | -7.8789 | -72.3492 | 2026-10-07 17:50:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 119.5 |
| c7271be3-4634-3b73-b353-43c48719c13d | -3.6419 | -54.5126 | 2026-10-07 17:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| f436fd3e-1d13-3bf6-a343-950bebc6a4c5 | -2.9634 | -54.0894 | 2026-10-07 17:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| c342db3a-867e-3c15-a774-c844693c20e4 | -3.1299 | -53.7431 | 2026-10-07 18:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 5568dbfe-a102-3149-9d52-5ea379bf9e52 | -5.9644 | -40.9627 | 2026-10-07 18:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 148.5 |
| 7ab841e8-95cd-35ff-9e46-bf953bb7d1b6 | -3.3134 | -53.8592 | 2026-10-07 18:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 168.5 |
| 2ba83cef-58aa-3121-b3f3-2156818a269d | -9.8246 | -65.016 | 2026-10-07 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.6 |
| bb81d64c-0512-3b45-a09f-f31c527bddd2 | -9.5425 | -65.6815 | 2026-10-07 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 104.9 |
| f99310dd-6131-3d6e-94b7-5af6f9d284e3 | -3.8786 | -44.1265 | 2026-10-07 18:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 084f68c3-6db0-3983-9d91-234973034ee1 | -7.7174 | -69.8841 | 2026-10-07 18:00:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 3c568610-4a95-3297-ab19-6de6904a61fd | -2.9634 | -54.0894 | 2026-10-07 18:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 71c6d703-6c73-3a6a-9059-63aa6b97d692 | 1.8951 | -55.7027 | 2026-10-07 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| e8c4a972-e8d3-332b-ba9f-702a6f9a6382 | -9.1363 | -65.2835 | 2026-10-07 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 150b103d-513d-39e3-a56c-f54e20e95795 | 1.8951 | -55.7224 | 2026-10-07 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 55f4bc3c-b5cd-3f9a-93ec-2d52ee12caec | -9.6757 | -65.0401 | 2026-10-07 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 2c2288ee-1ce9-35bf-bb5f-a6e46de4e460 | 1.7121 | -55.6261 | 2026-10-07 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 6df8403c-98d2-39ff-b3ca-65b82a9cfbc8 | -3.1299 | -53.7633 | 2026-10-07 18:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 336689a5-f391-3066-aa9c-babd0746a097 | 1.8584 | -55.7426 | 2026-10-07 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 7b66d2a2-e5a5-3f84-a140-c55a9c1bea8d | -7.3635 | -73.245 | 2026-10-07 18:00:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 90.8 |
| d94d57d0-9ce2-3215-821c-ddac4ebaa6a4 | 1.8768 | -55.7227 | 2026-10-07 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| fc56dfb3-9712-3566-85b2-62387968af64 | -2.945 | -54.0899 | 2026-10-07 18:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 3f9ceb37-b9a9-381f-bbb4-f9ee1cf61d6f | 1.6385 | -55.785 | 2026-10-07 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 8932dec9-7b8c-3cc1-999c-e7e5bdd595f3 | -3.13 | -53.7229 | 2026-10-07 18:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 641afd58-29d1-3f2f-87b8-6cd8a71d6a51 | -8.6201 | -70.0354 | 2026-10-07 18:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 82.2 |
| e8d6b327-4a16-3847-8120-a6ba8c792a8f | -9.5468 | -64.8196 | 2026-10-07 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 02fd778d-ca11-3cce-8c31-c9bbc78f66fb | -11.7362 | -43.5068 | 2026-10-07 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 622d5bec-4794-3990-970c-a768fcc3d0c1 | -9.806 | -65.0167 | 2026-10-07 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.2 |
| f8e19a7f-4ea5-3798-a862-32dd569e9ca9 | -3.2717 | -50.4102 | 2026-10-07 18:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 042fc856-1045-3102-a044-9faaa28d0f39 | -9.8431 | -65.0341 | 2026-10-07 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| b48df16c-f822-3daa-b157-fd760e38ddfd | -9.9596 | -43.5045 | 2026-10-07 18:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 208.8 |
| 400e58d1-0928-3d42-82b9-8c6ed262b817 | -7.3747 | -46.2161 | 2026-10-07 18:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 7d50e2b3-599e-3007-9196-2617eb56e17f | 1.7671 | -55.5859 | 2026-10-07 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| aafea554-efdd-307d-b27c-9191bf4884dd | -5.7312 | -41.7309 | 2026-10-07 18:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 148.2 |
| 528bd7a8-6e1f-3796-984d-1f4c3a1807d8 | -9.4621 | -67.0817 | 2026-10-07 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 46369a47-1d8c-359e-ab33-e1219f63e73e | -2.8713 | -54.1518 | 2026-10-07 18:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 5c92a7bb-761d-319a-b27b-aac837df78f6 | 1.8767 | -55.7424 | 2026-10-07 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 6e7d668a-cbd5-347c-b20d-f5ac5fcf3d07 | 2.4585 | -50.8299 | 2026-10-07 18:00:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 275f5604-62ef-32e2-a0db-cb83dda10de4 | -5.9835 | -40.9367 | 2026-10-07 18:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 182.9 |
| 49ec56f2-6220-3c89-975b-0fd066e109a4 | -6.1431 | -52.6481 | 2026-10-07 18:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| c83eff36-17fe-3289-8883-d9d67bcfa19a | -2.8899 | -54.0912 | 2026-10-07 18:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 3d5ad32f-e610-32f6-8075-b6d57f109a32 | -9.96 | -43.481 | 2026-10-07 18:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 172.3 |
| eab93153-5cb1-3010-af14-970665c903a0 | -4.1407 | -54.0152 | 2026-10-07 18:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 9b1eaa56-6bca-328d-ae0d-cf0e6611d628 | -5.496 | -42.8178 | 2026-10-07 18:00:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 108.0 |
| a256e0d4-b698-30d5-8bc7-1dfa00f6466d | -9.1829 | -67.3861 | 2026-10-07 18:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 2ffd0c9c-bdbf-3633-a8fc-90ad9085caed | -12.0457 | -43.3864 | 2026-10-07 18:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 152.1 |
| eee1b591-44f0-37dd-bad6-e893b08305d2 | -10.4594 | -46.8333 | 2026-10-07 18:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 185.6 |
| 637e3be0-d1eb-378b-a770-d098f9120d79 | -2.9449 | -54.1099 | 2026-10-07 18:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 155.1 |
| fd3004e9-ac25-3378-99bd-8daa1a736292 | -11.2333 | -44.8678 | 2026-10-07 18:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| c60b22da-8e92-34f6-b7f6-570ff76044c9 | 1.6937 | -55.6461 | 2026-10-07 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| f9d60883-818c-35b7-85e8-190bcf633a9a | -11.619 | -43.6196 | 2026-10-07 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.0 |
| c868ed17-2c41-300c-860b-752606546645 | -6.1781 | -52.9328 | 2026-10-07 18:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 2f379468-316b-369c-93bf-9bc2a685b140 | -4.2657 | -54.8729 | 2026-10-07 18:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 6ff4ed31-250c-3f3c-9025-5ae246681091 | -3.8788 | -44.1035 | 2026-10-07 18:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 56ea0888-4219-34a5-9798-a734fdd5ec4e | -2.9082 | -54.1108 | 2026-10-07 18:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 731a7bcd-6ef9-3aff-91db-ece437582cbe | -9.1711 | -65.7682 | 2026-10-07 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 66eddb77-3cc8-3f32-b44e-83f36bd53f7d | -6.8292 | -39.5472 | 2026-10-07 18:00:00 | GOES-19 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 100.9 |
| a0d4b538-fc1d-30dd-b473-f18d4a3941c1 | -2.7981 | -54.0732 | 2026-10-07 18:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 512.0 |
| 21ff4af4-aab9-3141-a2de-cc2702492f4d | -10.9953 | -45.4068 | 2026-10-07 18:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| da30b122-76db-36a4-a81a-511e0a2d111e | -2.0447 | -54.3085 | 2026-10-07 18:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 287.3 |
| 157860e2-70bf-381a-85f9-e9c59fd54120 | -9.7126 | -65.0951 | 2026-10-07 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 20d994dc-718b-363e-b3c3-0e7ee2b111b2 | -1.2922 | -54.5585 | 2026-10-07 18:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| f321fa24-1e0b-3328-8375-d777d788ecf1 | -9.4805 | -67.1183 | 2026-10-07 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 6f9e0de7-4738-39e8-b10d-299a3788cc69 | -5.4958 | -42.8413 | 2026-10-07 18:00:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 218.2 |
| db9b990a-ecf9-35b6-a7e2-2a8ea1a74a31 | -3.6566 | -55.4683 | 2026-10-07 18:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 9e96cefe-a671-352b-916b-00732452c865 | -6.1502 | -39.4158 | 2026-10-07 18:00:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 251.1 |
| efc5eca8-7679-3697-9c6b-b6b61389c81a | -7.2721 | -72.7177 | 2026-10-07 18:00:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| d67f0045-70e9-365a-8ab4-90bb084abfee | -2.9082 | -54.0907 | 2026-10-07 18:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| d2611b60-211b-3ca9-8c60-510620b051e8 | -3.55 | -54.4952 | 2026-10-07 18:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 537973d9-dab1-3c82-bbb4-bc866b29e70b | -2.8898 | -54.1112 | 2026-10-07 18:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| f9f40540-bd81-35bc-b801-44d3a5794258 | 1.712 | -55.6459 | 2026-10-07 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| dca10798-4720-3df0-b14f-33dee1ab3dec | -3.5875 | -54.3138 | 2026-10-07 18:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 47293360-873b-3b4b-8935-9c98cf84d7b0 | -4.3471 | -43.8021 | 2026-10-07 18:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 72512691-588b-373b-b1e2-8240cc0a09cd | -3.8081 | -40.4608 | 2026-10-07 18:00:00 | GOES-19 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 138.9 |
| 3fbeda4b-2119-3112-9101-55362f838e3c | -5.6829 | -40.8895 | 2026-10-07 18:00:00 | GOES-19 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 103.4 |
| 2530ce63-15b6-34ed-97b5-72d202d0d243 | -3.0932 | -53.7239 | 2026-10-07 18:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 9ff64ba6-8ffe-3329-a910-d2536d0e13d7 | -6.5794 | -41.5841 | 2026-10-07 18:00:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 92.9 |
| 198f3ddf-ffb9-3674-a405-c2c82e3be618 | -11.3749 | -46.6722 | 2026-10-07 18:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| a036a589-e244-3a8f-afdc-ab2c163f8db2 | -2.9819 | -54.0287 | 2026-10-07 18:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| ddf1ec79-2f57-3eab-997d-7ce056f667af | -2.7613 | -54.0941 | 2026-10-07 18:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 486.2 |
| d7ed52f8-2ffe-3197-9392-cc25aa5ad7b8 | 1.7121 | -55.6063 | 2026-10-07 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| db6708e7-2334-3ffd-a0c3-d8c46e31e2a2 | -9.462 | -67.1002 | 2026-10-07 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |


[Clique aqui para ver as próximas entradas](README245.md)
