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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| beaf2804-e443-3c37-9f2e-9c2b4fb609b4 | -4.05496 | -48.24815 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23f52ac0-b353-3bee-8bdb-6a2c04ddcfed | -4.56612 | -45.41037 | 2024-11-10 04:38:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66cd8b35-7de1-3d38-8e83-fc01ab3408c4 | -8.39772 | -44.13587 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07c3ee69-90ec-33a0-afd4-e749399ed0a5 | -6.32686 | -46.71712 | 2024-11-10 04:38:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 405b25fb-0ef4-3900-a368-8a53df2f703a | -1.86177 | -53.73441 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7dafe848-1bca-39d8-a5aa-7c69d4c7cf06 | -4.10673 | -48.97489 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e44cf0bc-4465-3fed-b266-51db97773caf | -4.12187 | -46.11069 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcc5defa-5d41-325f-ad55-590d37870aff | -3.02291 | -48.07697 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8a49303-ea78-3028-8c9d-24f22f48ad06 | -4.90701 | -48.55533 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 196dca2d-5082-33c0-a37f-6ba0a9047c00 | -2.98047 | -53.73972 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| adb1570b-e148-3fdb-be0b-21d2e8d997df | -3.45615 | -47.66847 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7a15673b-53b3-3cf1-beec-c14077c7b067 | -2.36275 | -50.61219 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d34ed70-5f64-3873-b781-a1ace27185a8 | -3.08334 | -50.56866 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8b0f5ad-5a0a-334d-8b57-136eda7e990c | -4.45837 | -45.9155 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d071ee60-ab2e-322f-b26f-f48c659e147b | -2.56667 | -54.73445 | 2024-11-10 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 631affed-b8ba-3e8d-816c-61140fc9c1d0 | -3.53003 | -50.32789 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01aaf610-6f21-3b20-9ec3-06b055e1f973 | -2.56742 | -54.73206 | 2024-11-10 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31fba287-4a83-382c-93b6-6d31045d5274 | -2.93033 | -49.83966 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ee4adcf-a055-3a8e-b8cb-9e18864c5af4 | -4.27475 | -48.18261 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f5ab436b-e59c-345c-ae66-d3d79bd5f54a | -2.24882 | -50.08151 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee51462b-d99b-3d61-a0fa-5a500af3f429 | -5.11827 | -49.91833 | 2024-11-10 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 507df39c-4033-3fa1-80cd-bfb15821c014 | -3.23284 | -50.26306 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ff95600-b4d1-3e4f-a558-472a75a3cd9c | -4.28475 | -48.18416 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b513c6f3-c2a2-3bc6-b30c-8e4410ab5546 | -3.21814 | -53.06291 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b1eb3d00-4102-35d9-8a62-5e0806b1d928 | -3.03511 | -49.52621 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c054db79-37a4-334f-a6f5-ea30fbd8c861 | -2.67127 | -48.65451 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e745003-86d8-3bca-8696-975822e2ae59 | -5.1368 | -48.25187 | 2024-11-10 04:38:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 501695ff-9c3e-312a-9ab3-70036ac3bbdb | -2.62622 | -49.45862 | 2024-11-10 04:38:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b8c4b467-6822-3241-91ca-667d2266029b | -3.34137 | -50.13119 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21363a17-5d48-35e1-ab85-0864ae8d438e | -2.62942 | -48.57714 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a33782fc-d541-3112-9d5a-f73e053304cc | -2.81421 | -51.35046 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8e737272-8513-381d-a0c8-2ebaa59ba6fa | -3.1918 | -48.66188 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f789441c-d1a7-33af-ae9f-316491339127 | -2.94027 | -51.06166 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48a6dcf1-ad38-38a1-8c67-d2e68314dcea | -3.61603 | -48.9296 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 676841ab-3940-3d4f-b165-5b19b418fffa | -2.83423 | -49.46986 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e29d4428-6390-323f-a4e7-347b8b6b8333 | -3.03716 | -50.32996 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7b78c36d-24e9-35bd-9134-5193986aae32 | -2.87343 | -49.45062 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b861911a-e343-3267-a955-1689ae38447a | -3.36063 | -51.22928 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| de9ddcdf-0251-375c-b6b6-726afee6089c | -7.47337 | -43.59431 | 2024-11-10 04:38:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 988db747-2121-3d92-8639-4c54c38bb746 | -3.10129 | -45.95108 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75f947b2-f09e-3b5e-8e43-4135202f3284 | -2.15942 | -50.50808 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06cfd8bf-4a2e-3973-a672-0b664ec99468 | -8.40166 | -44.10857 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d87c47c-ce9b-39d6-a94f-0291016fca1c | -2.91805 | -49.49356 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d6fc2a9-caab-3df7-8cb7-ae396f8ffa9c | -4.60707 | -49.57601 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05867445-a04e-3818-81f8-d13252e341a3 | -3.47691 | -50.37543 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c94da407-2fe8-362e-85fd-0f2be7cf6d8e | -2.7221 | -49.29752 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a6331bb-50e9-311a-af03-9a17b4ea8a01 | -2.77399 | -49.35275 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62ba1b4f-9331-3731-8bad-929c3b2dc597 | -3.65545 | -43.86942 | 2024-11-10 04:38:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca5105d6-6289-39c7-ade6-fcb27d650858 | -4.71052 | -46.38172 | 2024-11-10 04:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88594974-784f-3d15-a2ce-d1cb3022ed83 | -4.35055 | -48.62803 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fac6941f-9623-360e-a318-87da7cf624dd | -3.04328 | -48.03399 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32a6ab40-04e8-37fc-851c-2a260194f855 | -3.28954 | -49.62357 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92643679-362c-3ff3-a68d-0d8ac05af035 | -3.36994 | -49.92986 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38c3a39e-116a-3f34-81c1-fa6946eb3d89 | -4.51626 | -56.07763 | 2024-11-10 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9702e3b9-4d88-332d-91c5-3a60c44ad4e5 | -3.53738 | -49.26135 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd9c599c-8815-3dd8-b81e-459203447384 | -3.34201 | -44.97517 | 2024-11-10 04:38:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| feab7591-a005-397a-ba67-30e52c8b97ee | -3.2353 | -46.53402 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ee6b763-f1d6-37b8-89e3-d9b52db4f2ce | -3.51114 | -53.79489 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34d9621b-868e-3b3d-8758-8c1492084618 | -3.54125 | -49.2584 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 481017f3-2a80-35e3-b9f3-3ed539da266b | -4.9505 | -48.45184 | 2024-11-10 04:38:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8747245f-4047-31ae-903e-0ee9788548ee | -3.9743 | -48.17867 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13c9d0cf-e931-355c-9be9-5a10c0770691 | -3.9582 | -48.17258 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| d952c652-bbba-31ea-ad58-af60b4bd4884 | -8.39632 | -44.11575 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6292a2b-5b62-38f4-9027-bb8c23342b80 | -4.04306 | -51.07087 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad628b73-5525-3cbe-9aaa-97ba80440dfb | -2.88006 | -51.6617 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b83ab11-771a-3975-95a7-38075092906e | -7.46529 | -43.58918 | 2024-11-10 04:38:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c44cda84-adda-3373-9f18-bc25b314aaf1 | -2.7049 | -49.34137 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8816ea36-aa12-343d-9f27-d9280d8d1c57 | -4.61707 | -49.57757 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ce864a9-727b-3b0c-9e0b-56a92cf61edb | -3.18313 | -52.34681 | 2024-11-10 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bc22198e-30b4-30e4-8d81-42b030fc4cb7 | -2.1162 | -50.74806 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 260306e6-ddcb-3bc6-947b-7c4a82c0e9a2 | -1.48491 | -55.43912 | 2024-11-10 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 00ede064-6ab4-347b-adbe-d5c9308b6681 | -2.41948 | -53.66117 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb1113e9-6441-3ff8-a5ab-c6aa47d43e86 | -3.29993 | -50.08067 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8343ce05-2496-3e8f-b413-20f92aca3060 | -3.72954 | -54.73887 | 2024-11-10 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7aa0cc26-084c-36fe-8fe7-417b419e04c0 | -2.65624 | -49.39859 | 2024-11-10 04:38:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3b1a0fae-095b-3714-bd93-740a1e342b6a | -3.92435 | -48.32368 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae18cb89-e9c4-30a0-8449-46f4d5f3f598 | -4.13149 | -53.50567 | 2024-11-10 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6f11846-3bc7-33c9-a82a-916d655d3afc | -2.70725 | -49.49985 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9539090-b832-3dc0-b341-76e330202f82 | -2.34375 | -49.9661 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c0596e2-35a1-32b3-8cb8-fec79ab06539 | -2.50777 | -49.90238 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a212a79c-0ae8-3370-b595-2d06b7ccca63 | -2.67904 | -51.82191 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c309e7ee-e9cc-3aeb-bb44-5894d7d40419 | -2.65289 | -49.39807 | 2024-11-10 04:38:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f0803714-3209-3ca9-878c-39109e96d9d4 | -2.22049 | -50.88945 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 892e02be-9575-35b7-bead-bdd82c0b36a5 | -2.63765 | -49.87447 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ac36e6cf-adad-3244-8590-c114f1a8f037 | -3.22462 | -50.68556 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 9f113b25-28ae-389f-ac95-6f4143ff8b84 | -3.46144 | -50.18667 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49abe6d7-4082-3a57-aefc-418eccb1b6ee | -3.51937 | -44.0289 | 2024-11-10 04:38:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 51385f91-19f2-3f63-9632-d6a50bf2dbab | -3.57891 | -50.28349 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea38d086-df8d-3a46-a4cc-2bb1c9d55749 | -3.08722 | -51.22456 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c5968e4-8a6c-35b9-9762-c7923f8ee349 | -4.30847 | -48.61439 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0e171f57-d27b-34be-aa5d-67e572373372 | -4.16792 | -46.6027 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9836eb5a-1c69-3fc3-85a4-cc3d594e4f00 | -2.03358 | -52.04814 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 75f244b2-e2c9-3574-a23a-a633169bd783 | -2.86241 | -48.4511 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c26df926-48a1-36aa-93ee-843e59270fb7 | -2.79541 | -51.76908 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88d67ecf-4ad2-3635-9182-2850f85baa94 | -3.97539 | -48.17171 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eaf6792c-68a7-395d-bdba-cd741279bb15 | -3.76636 | -50.37938 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e90a5d55-2b02-3e2f-b04d-6936b5288647 | -2.86834 | -51.47107 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c44cba5-a6e2-3489-9d16-c3679091710c | -2.86673 | -49.51432 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9cc9d2d-e223-30d4-b948-992e6e2d73f1 | -4.22034 | -45.69592 | 2024-11-10 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85c8d655-419d-37c3-9f08-23f2d6c0c613 | -3.09646 | -54.27297 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README101.md)
