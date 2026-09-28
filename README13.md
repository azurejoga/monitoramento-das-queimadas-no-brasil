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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1760ef1-197e-3943-b174-64cec29e4e94 | -11.4425 | -44.9303 | 2026-09-28 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 7df537f7-19aa-3c78-8870-3e04cc3032d6 | -10.8907 | -43.6813 | 2026-09-28 01:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 282.6 |
| fc34e9ec-8eaf-3a39-a6ed-d48eafcd4ba0 | -3.1471 | -54.0849 | 2026-09-28 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 0074c1e2-d53c-3a89-9e6c-5f5f6314dde4 | -9.1584 | -61.4082 | 2026-09-28 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| cf485156-57fc-3e19-a1ab-acaeb5a3e1b0 | -6.7064 | -45.599 | 2026-09-28 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 186e8b12-c0aa-38e2-9ad0-26f04983294d | -2.7767 | -49.4765 | 2026-09-28 01:30:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 18702343-4042-3ef1-9acc-e82d0eed6b94 | -2.9081 | -54.1309 | 2026-09-28 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 1b86da76-a1b8-3d8b-9774-e8bed29518dd | -6.6627 | -55.1112 | 2026-09-28 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| cf811c89-86a9-38e3-b7ac-9e6974971b02 | -6.7251 | -45.5975 | 2026-09-28 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 7ace9f28-be23-3318-94ab-bf3ad9f6199d | -3.1471 | -54.1049 | 2026-09-28 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 066d7b89-daca-3e5f-80db-19c893bd5ccd | -3.1655 | -54.0844 | 2026-09-28 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| fbdd0c23-f90c-30b2-aebf-a286e559006d | -9.22898 | -67.60535 | 2026-09-28 01:37:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 77c4fbd3-e897-33e7-bd17-e3f6821f48c6 | -6.98102 | -71.6841 | 2026-09-28 01:37:00 | TERRA_M-M | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| cbafa91d-653e-3c8b-8e13-cd752b3d1218 | -11.2353 | -44.7519 | 2026-09-28 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| c5ff6318-062a-332b-840b-9f9bd1e97bd9 | -6.7251 | -45.5975 | 2026-09-28 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 136.5 |
| c3afb356-70ae-38a4-a9ff-3861eeab37f7 | -10.8907 | -43.6813 | 2026-09-28 01:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 351.7 |
| 9dff138c-63f6-3931-9407-0fa397b9b459 | -11.4425 | -44.9303 | 2026-09-28 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| f84dc743-c0f6-3e90-899e-89d18a3cafae | -15.112 | -53.8838 | 2026-09-28 01:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 1eb76032-6f46-377b-94f0-10913bab38b8 | -9.9973 | -50.1393 | 2026-09-28 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 5a9055fd-05f9-3e6e-924a-a037bf77f929 | -6.7064 | -45.599 | 2026-09-28 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 330bbbf4-22f0-3ffd-9ddc-64896293db09 | -10.8715 | -43.684 | 2026-09-28 01:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 597a4a96-9a19-3a7c-aaea-9e39abd95ec1 | -15.1842 | -46.1642 | 2026-09-28 01:40:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 73.5 |
| c68e84ba-6894-3bb5-82ec-4de976c9f7c4 | -2.9081 | -54.1309 | 2026-09-28 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| fe998b3d-54a3-3703-956c-f894801974c3 | -15.1847 | -46.141 | 2026-09-28 01:40:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 4e7d0e9e-b838-359f-8fa5-d159e4b84ce7 | -3.1655 | -54.0844 | 2026-09-28 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 3485e389-1421-3331-9bc9-70aed108b5ce | -11.2162 | -44.7546 | 2026-09-28 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| dfa75c57-c865-322f-8243-cc2758cf665e | -3.2137 | -51.0384 | 2026-09-28 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| f949c5f5-5c60-3cdc-825d-29999eedc117 | -9.177 | -61.4073 | 2026-09-28 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| eb6a1966-747e-3263-90bb-58d2e0877ffe | -3.1471 | -54.0849 | 2026-09-28 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 7daf82c7-22a0-3fdb-8ffa-f642f358c87f | -10.8903 | -43.7048 | 2026-09-28 01:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| c20818cd-0bd9-328c-8c8b-aa2e50860093 | -14.9201 | -49.4951 | 2026-09-28 01:50:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 2b90040f-c506-387d-96b5-99a121dabfef | -6.7064 | -45.599 | 2026-09-28 01:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| fc13efc3-0b43-3874-a308-a9501ace2972 | -6.7066 | -45.5765 | 2026-09-28 01:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 9a70024d-98e9-3d7e-97f4-886d77999e64 | -12.7417 | -47.2909 | 2026-09-28 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 1f7b666a-d664-36a6-940b-c4df12bca769 | -11.7828 | -51.0578 | 2026-09-28 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| e34455af-2762-3514-8e13-4df8f5e6948a | -6.7251 | -45.5975 | 2026-09-28 01:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 166.9 |
| b8fafa4b-ab48-3280-9a5f-e89240fa3762 | -10.8907 | -43.6813 | 2026-09-28 01:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 192.8 |
| 00c5eb45-037a-3309-a749-37c0c74d3205 | -3.1471 | -54.0849 | 2026-09-28 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| ea01e70b-b119-392f-b090-205e7d66a29d | -6.7254 | -45.5749 | 2026-09-28 01:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 652786ca-4e84-3bd8-b806-1bab146a7d34 | -9.177 | -61.4073 | 2026-09-28 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 068139e3-ceda-3863-a6b3-d4c3a013ed10 | -14.9006 | -49.4981 | 2026-09-28 01:50:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 121.7 |
| dddcab60-9be6-3e3d-b53f-0b8c69e2e019 | -15.1842 | -46.1642 | 2026-09-28 01:50:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 87.7 |
| b3db475f-5464-32eb-92b8-751f94d39c08 | -11.4425 | -44.9303 | 2026-09-28 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| d1878ec8-e4e2-3bb9-9630-02979fe812d0 | -11.7828 | -51.0578 | 2026-09-28 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 8418c66b-27a4-3114-ae9d-5134e85d9bc9 | -10.8907 | -43.6813 | 2026-09-28 02:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| a2cb2a9e-5757-38f5-a672-6ecaf29205e0 | -6.7066 | -45.5765 | 2026-09-28 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 953507f4-4491-34e7-8291-9cde161f7faf | -6.7835 | -59.3823 | 2026-09-28 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| b63f8e39-88aa-3b19-9bfe-9b20f28341ba | -11.8018 | -51.0556 | 2026-09-28 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| a2416372-bf97-391c-95b0-5b3a81fc1ee3 | -6.6627 | -55.1112 | 2026-09-28 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 5799ae88-6f0f-37c1-97bd-b17607847692 | -11.7831 | -51.0365 | 2026-09-28 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 1c042b38-d37f-32dc-b9e1-d3c463f11e46 | -6.7254 | -45.5749 | 2026-09-28 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| e00a56de-d339-3a8f-af3a-924ce4fb1620 | -3.1471 | -54.0849 | 2026-09-28 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 23e0f4f1-5cbb-30a1-803a-e2200df3571c | -6.7064 | -45.599 | 2026-09-28 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 7524fabe-39f1-31e1-afb7-f2266d6badfa | -6.7251 | -45.5975 | 2026-09-28 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 7f034d41-9e92-37f3-9e56-ebd7b6fee035 | -10.1245 | -45.1313 | 2026-09-28 02:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| a29ce40d-6c46-3c3b-a10d-c615c0bc01ce | -2.9081 | -54.1309 | 2026-09-28 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| aacd2ef5-f84f-38b6-9d70-692b505e6b95 | -9.177 | -61.4073 | 2026-09-28 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 4c8a218b-60d2-3fec-b816-4d3869e409c1 | -6.7254 | -45.5749 | 2026-09-28 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| fca9eb77-c7bc-382a-8899-886a16294849 | -6.7251 | -45.5975 | 2026-09-28 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 74e5799c-57ed-39ea-a90e-3da3a391ccf9 | -11.7831 | -51.0365 | 2026-09-28 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 743f13f9-328d-3f7a-b3e2-1dbd6dc4f130 | -6.6627 | -55.1112 | 2026-09-28 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 0dea0860-ba22-3658-86c4-f7aff34f7882 | -11.7828 | -51.0578 | 2026-09-28 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 88014c14-82ef-3e6d-9f56-89a421bd0504 | -3.1471 | -54.0849 | 2026-09-28 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 079a7771-24fc-3afc-835d-3d00cd5c85d5 | -10.8907 | -43.6813 | 2026-09-28 02:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| efa47831-a8f4-3ed4-9a48-b1d4cba0b42f | -6.7064 | -45.599 | 2026-09-28 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 61f1bb31-11d3-3558-95d7-102e2748763f | -11.2162 | -44.7546 | 2026-09-28 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 62b1ce76-2af9-34b2-98c6-6b35bc2ce3f4 | -6.7066 | -45.5765 | 2026-09-28 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 3845a6d7-f5a0-37ac-8515-48f8d0628136 | -2.9081 | -54.1309 | 2026-09-28 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 394b60fc-db31-3302-ae80-2e01c8a4abbf | -9.177 | -61.4073 | 2026-09-28 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 5d954919-19b8-3846-ab96-c3e211c0f8d9 | -11.22 | -44.81 | 2026-09-28 02:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 18d34aae-8874-345b-9f64-eed60e7592d3 | -11.18 | -44.76 | 2026-09-28 02:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 81c543ab-9763-3139-a9b7-1df802bf6cd3 | -11.22 | -44.86 | 2026-09-28 02:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 302ef854-3478-3abf-940e-19033af68a8c | -11.19 | -44.85 | 2026-09-28 02:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 50fe04ac-3041-3dd4-a60d-bad69b191062 | -11.19 | -44.8 | 2026-09-28 02:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 96fffd96-c3b3-3482-ae66-bc1113bf5da1 | -11.25 | -44.82 | 2026-09-28 02:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 572c8785-c0cc-39c3-be3e-3c319e992b68 | -11.21 | -44.76 | 2026-09-28 02:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 931ba6bd-c769-3236-bca2-3ccc3584bb3b | -11.16 | -44.84 | 2026-09-28 02:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| af451527-dc3a-3861-9db3-20ecdecbc164 | -11.16 | -44.8 | 2026-09-28 02:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 98ddf313-8d74-3578-abe5-272f3c5a333f | -10.8051 | -60.745 | 2026-09-28 02:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| fa5b612e-054e-3ab6-908e-5c23b81e5f28 | -6.7251 | -45.5975 | 2026-09-28 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 197.2 |
| 7c950028-04bb-3741-b696-b46ef7c89e37 | -3.1471 | -54.0849 | 2026-09-28 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| a143c4b1-7e7e-36f0-b7a8-bfdaabf58b92 | -14.901 | -49.4761 | 2026-09-28 02:20:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 4ef9de02-9213-3e19-b6cc-00957ed9c62e | -2.998 | -54.7492 | 2026-09-28 02:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| ff4112ea-be6b-3b4c-9286-939e3d783aa3 | -11.8018 | -51.0556 | 2026-09-28 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 7ae629cb-d6bb-3976-92af-26b364efa78e | -9.177 | -61.4073 | 2026-09-28 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| b5b32e60-4c17-34aa-a2e0-f7896aab39bc | -11.7831 | -51.0365 | 2026-09-28 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 218.1 |
| 7f539b1c-45c1-382c-904f-3e805a08b7f9 | -6.7254 | -45.5749 | 2026-09-28 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| d98c4b98-f1a3-310e-b4b3-90838a3c4e23 | -11.8021 | -51.0343 | 2026-09-28 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 824054b0-b1ea-352f-959f-830fc19eeba1 | -14.9201 | -49.4951 | 2026-09-28 02:20:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| a46507f1-debb-3ae4-8e77-0da81f2171b3 | -14.9006 | -49.4981 | 2026-09-28 02:20:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 8dd1e81b-00c5-3e67-8023-286b25c23862 | -10.8238 | -60.744 | 2026-09-28 02:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 8ce6aa28-9082-3bcc-9708-989d8c28cb05 | -6.6627 | -55.1112 | 2026-09-28 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 88927120-a2ef-372a-a072-35fd5d91e3f5 | -6.7064 | -45.599 | 2026-09-28 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 3f02ae28-a1b8-304c-9398-9def7a835d71 | -6.7066 | -45.5765 | 2026-09-28 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 6ea93d7a-1c3a-3631-80e0-f2903b1f6dd2 | -11.7828 | -51.0578 | 2026-09-28 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 9628c3b7-ffe0-30d0-9c57-f451cb878ab7 | -3.1471 | -54.0849 | 2026-09-28 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 1edccaca-3f78-3346-b9fd-0280c70e9d31 | -14.9006 | -49.4981 | 2026-09-28 02:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 358.5 |
| 9ff9d949-7197-325d-a6c8-6ee8c950279c | -10.8238 | -60.744 | 2026-09-28 02:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 89a7fb4f-97ac-3f94-91de-cdc4ed8c1b96 | -2.7767 | -49.4765 | 2026-09-28 02:30:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 667afebb-ac0c-3f4b-afc4-d416f7db6496 | -14.9205 | -49.473 | 2026-09-28 02:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 129.9 |


[Clique aqui para ver as próximas entradas](README14.md)
