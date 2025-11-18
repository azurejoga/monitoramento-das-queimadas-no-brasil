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
| a253aedd-9be7-3b1c-a62c-c8cabdc4055d | -4.1781 | -50.2091 | 2025-11-18 00:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 22fe7fde-075a-3329-a91a-78138883b73a | -3.4584 | -46.0664 | 2025-11-18 00:00:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 35908ed0-11b6-30b5-9618-2b2406014db8 | -4.1782 | -50.188 | 2025-11-18 00:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| b0c466a9-6a43-374f-a40c-59aed52d7d78 | -3.477 | -46.0656 | 2025-11-18 00:00:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 185.2 |
| 1af85a50-21fe-3088-9015-afa017151c4c | -11.51 | -48.9583 | 2025-11-18 00:00:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 00de64f7-8682-3073-af30-f4b41701c92c | -5.3382 | -43.7391 | 2025-11-18 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 55937563-135c-36cc-ae5a-50fe778cc269 | -4.1764 | -44.2257 | 2025-11-18 00:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 300.2 |
| eb412ead-c0b4-3fde-bbb5-1137f55b29b4 | -4.195 | -44.2247 | 2025-11-18 00:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 314.3 |
| ddc8e0e5-aea3-32bc-ba61-770d76b0bb77 | -12.7378 | -45.4274 | 2025-11-18 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| c1481918-b77b-3433-93fc-aa2026b5dc3f | -9.4158 | -48.4504 | 2025-11-18 00:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| c3999c91-9b89-396b-8cb6-5002d54daa24 | -2.8677 | -45.2382 | 2025-11-18 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 136.8 |
| d4abe1db-d0e5-3776-8319-d05e35b13d2e | -12.7193 | -45.3842 | 2025-11-18 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 6d986ffd-84e3-3a0c-8dd4-ccec184b3adc | -15.4693 | -43.1804 | 2025-11-18 00:00:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 88.2 |
| ece91f36-e7a2-34bc-aab7-c31ade27b2f5 | -3.3555 | -44.3798 | 2025-11-18 00:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| e4c2e4fb-f704-3eb6-a98b-ac9bdf0d1704 | -5.338 | -43.7623 | 2025-11-18 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 1886b640-74b5-3580-83d0-56691b38143b | -4.2137 | -44.2237 | 2025-11-18 00:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 804addaa-2235-36ee-80e5-38197de79756 | -12.7575 | -45.4013 | 2025-11-18 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| f82d393c-6ef0-3654-bfe9-979655d58ef3 | -11.5291 | -48.9559 | 2025-11-18 00:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 4f04908e-7ae5-3d9f-9ee1-67ef3a820c5a | -8.3223 | -44.0519 | 2025-11-18 00:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 1b514178-ccd9-32ac-b112-01f12259e139 | -2.2851 | -47.2302 | 2025-11-18 00:00:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 402683aa-6a56-3201-a251-21c1e603ee63 | -12.7386 | -45.3812 | 2025-11-18 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| d12e1122-9084-34dd-8a28-5cbd2f31bc15 | -3.4769 | -46.0879 | 2025-11-18 00:00:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 96.1 |
| b9f250ab-6d49-3a4b-9b1e-502c84db9df8 | -6.1138 | -42.9569 | 2025-11-18 00:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| 3d90c3b7-0240-3f50-bb66-8a7191fcc5e3 | -9.3972 | -48.4305 | 2025-11-18 00:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| c1b264d1-1c31-3527-b905-2e0ffd4f5d8a | -12.7382 | -45.4043 | 2025-11-18 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 65a36f77-703f-3a89-af5c-c8af0446cfd3 | -4.0931 | -45.6131 | 2025-11-18 00:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 84edee00-e047-3901-8556-3a2ed083362f | -4.2135 | -44.2466 | 2025-11-18 00:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 64887489-621e-30c9-b574-64129b265305 | -5.4192 | -43.0347 | 2025-11-18 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 408e2bb7-f139-3b37-bf82-d811be22f7cd | -3.0236 | -47.8396 | 2025-11-18 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 23d1345f-9f6a-30fe-8e14-a2e095f04b64 | -8.2851 | -44.0095 | 2025-11-18 00:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 37.4 |
| c587584d-af6c-3e89-88be-c4c3a5e5bc06 | -4.1949 | -44.2476 | 2025-11-18 00:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 362.7 |
| da58d20d-cdb2-36cf-b295-7efbda9253fd | -5.419 | -43.0582 | 2025-11-18 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 64a7543b-4fd1-3151-8f23-a3c5ca905f98 | -4.1762 | -44.2486 | 2025-11-18 00:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 344.3 |
| ddcdcecc-da92-3f80-8720-1ab8ae37b594 | -2.8298 | -45.4195 | 2025-11-18 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 3e418637-6056-3457-9121-61f723cca11c | -9.3969 | -48.4523 | 2025-11-18 00:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 137.2 |
| ec092fe8-d5c5-39a6-8040-1e1128aadcb0 | -3.1256 | -45.7449 | 2025-11-18 00:00:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 5e30721a-70ce-31ef-b195-2b7193eba5c3 | -10.3532 | -48.9392 | 2025-11-18 00:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 1222087e-0819-393e-9044-4d026a208109 | -8.3037 | -44.0307 | 2025-11-18 00:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 100.8 |
| e9ea09b6-0161-353b-b462-92e33d7fbac4 | -4.1117 | -45.6122 | 2025-11-18 00:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 81.0 |
| f98be263-47d8-3c5f-9981-548ead8d40be | -10.3535 | -48.9174 | 2025-11-18 00:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 4db3d4a2-c06a-348d-b73f-a59a2cfa1352 | -8.3226 | -44.0287 | 2025-11-18 00:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 58cb29fd-e722-3f0b-9460-081cd54352a4 | -12.7579 | -45.3781 | 2025-11-18 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 1307b47b-053e-34da-8e36-c98053524fe1 | -3.3554 | -44.4026 | 2025-11-18 00:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 145.0 |
| fab7fcb2-4021-321f-9e19-14dae54aa5da | -8.304 | -44.0075 | 2025-11-18 00:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 87040926-8595-3516-bd36-8721d72631c2 | -2.5238 | -47.8115 | 2025-11-18 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| d65745f6-0d7a-309a-a6bc-06a93747c57e | -8.3034 | -44.0539 | 2025-11-18 00:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 052fc001-dd98-3fb8-8d97-f5cc5b1d2454 | -3.4849 | -52.3511 | 2025-11-18 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| fcecde07-e2da-32c3-a6a7-18dba4a6e7ba | -6.1326 | -42.9554 | 2025-11-18 00:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| 9a4dedeb-1574-30ac-923f-5ec11455687c | -2.8678 | -45.2156 | 2025-11-18 00:00:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 9f97370f-92cd-38e1-adab-6f6e7aa13705 | -11.58 | -48.1381 | 2025-11-18 00:00:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 6bd5f79c-1ff4-393d-b9ec-03a9abe03209 | -2.8491 | -45.2388 | 2025-11-18 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 30e5e75b-02a5-350b-b7ff-1f539b269a8c | -5.4379 | -43.0333 | 2025-11-18 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 209f8224-f522-3fee-859b-5df6580b49c3 | -2.3347 | -55.7945 | 2025-11-18 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 0a796a65-484c-3079-acad-a7328938af48 | -5.4377 | -43.0568 | 2025-11-18 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 4f162079-bda7-3d72-9fd5-f878e2a0bfc7 | -9.3969 | -48.4523 | 2025-11-18 00:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 00cb1c32-2f4b-3305-b916-a8c4ef492def | -2.8491 | -45.2388 | 2025-11-18 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 122.3 |
| f0f1ced2-48c9-3a0c-a9a4-0e3292ff3340 | -3.4956 | -46.0649 | 2025-11-18 00:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 82d8acad-0754-3355-ad06-8fe93d0ce716 | -5.3382 | -43.7391 | 2025-11-18 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| cb32f5ec-3639-39bf-bdb2-474f72a73950 | -5.419 | -43.0582 | 2025-11-18 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 139.8 |
| fe0c21e0-2035-395c-9e2e-1e11cd8cb5d2 | -2.2851 | -47.2302 | 2025-11-18 00:10:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| a30be38b-0759-3b3b-a4f3-16b6e53c5548 | -4.0931 | -45.6131 | 2025-11-18 00:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 112a5b1b-be1c-3ee3-a529-b52ce16b2493 | -9.3972 | -48.4305 | 2025-11-18 00:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 89445ccb-0e81-3798-93dc-b96d5ac5f3b3 | -8.2851 | -44.0095 | 2025-11-18 00:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 53731874-723a-3485-8790-b9411afaf1ef | -9.1124 | -44.3334 | 2025-11-18 00:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 285.6 |
| 219363df-8de6-318b-8f31-81918dc2c4c2 | -10.3532 | -48.9392 | 2025-11-18 00:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 4eee27bf-287c-3502-a38b-5ce7574c1b2f | -3.4849 | -52.3511 | 2025-11-18 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| c5dab76e-c82f-3cf1-9532-383c1046ab7f | -8.3037 | -44.0307 | 2025-11-18 00:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 821f2cbf-f356-3916-a929-36b691e28e6c | -5.338 | -43.7623 | 2025-11-18 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 5ee058f3-db4a-38ae-82cf-00d99b049d0a | -5.4377 | -43.0568 | 2025-11-18 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| e0a6b27c-bf92-3771-a128-2502862b7587 | -2.8492 | -45.2163 | 2025-11-18 00:10:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 3d23b867-acf5-3af6-9c1d-25ea99982f74 | -2.5238 | -47.8115 | 2025-11-18 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| dbc8c6a9-6001-3525-b7de-063fcc94eb39 | -3.3554 | -44.4026 | 2025-11-18 00:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 59bc782d-5b7b-333a-a59c-5b5f98c0f887 | -9.0934 | -44.3356 | 2025-11-18 00:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 572.9 |
| 78e9b248-acf0-37cc-aa81-dfdf642ff993 | -9.0931 | -44.3588 | 2025-11-18 00:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| df55d461-9d5f-38c3-81b0-822da9e4bf25 | -4.1781 | -50.2091 | 2025-11-18 00:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 6d3ece8f-b1c5-357a-a623-c0cedbd1da26 | -12.856 | -41.4813 | 2025-11-18 00:10:00 | GOES-19 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 72.1 |
| f4738616-3e38-3460-a76d-8ca7818f8db9 | -2.8677 | -45.2382 | 2025-11-18 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 112.3 |
| e7084848-8409-3957-9a86-a9cc2b4a9f4b | -5.4379 | -43.0333 | 2025-11-18 00:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 399e5d20-b982-3999-927d-0246e7f4bfd6 | -3.477 | -46.0656 | 2025-11-18 00:10:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 189.7 |
| b6342bc0-d0f1-36e6-81f2-2fe3acb7c6d5 | -2.8298 | -45.4195 | 2025-11-18 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 0da357e7-5adc-348a-bf51-0965f7b21a90 | -8.79 | -44.3936 | 2025-11-18 00:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 1b44c49f-70cd-3aa0-9326-6c041f646082 | -11.5291 | -48.9559 | 2025-11-18 00:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| b4767ef4-19c4-321c-be3c-46dcddd5729c | -12.7382 | -45.4043 | 2025-11-18 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 72db1656-f179-3554-9f42-86c70895dfd3 | -3.3555 | -44.3798 | 2025-11-18 00:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 8ac3f60b-e8eb-3c17-af57-29a89a5338b9 | -12.7386 | -45.3812 | 2025-11-18 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 52e775d8-8df9-3ba6-afd8-1a42e48dcbb3 | -4.1764 | -44.2257 | 2025-11-18 00:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 280.7 |
| 137482d5-00a9-3e2b-b38a-ce05d3173cee | -2.3347 | -55.7945 | 2025-11-18 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 6afbd419-6ce2-3b21-9703-e8ed3ebfd4f9 | -4.5585 | -48.4895 | 2025-11-18 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| d1a79441-57ab-3419-8ee4-6225cd263823 | -10.3535 | -48.9174 | 2025-11-18 00:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 9a110437-57c0-399f-aab5-dd054b1a2b62 | -6.1326 | -42.9554 | 2025-11-18 00:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 59.1 |
| 6b5c9fab-9434-3ea4-8f81-0d002b70eb6f | -12.7378 | -45.4274 | 2025-11-18 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| d9dd109e-e339-3c96-8c85-3373be445c33 | -6.1138 | -42.9569 | 2025-11-18 00:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 66.3 |
| 402a05e7-0278-37e0-9c68-e4140305427f | -12.8566 | -41.4566 | 2025-11-18 00:10:00 | GOES-19 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 58.3 |
| 2216b7f8-2b7f-3460-9887-a3d46f65fb2b | -2.8678 | -45.2156 | 2025-11-18 00:10:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 74.4 |
| d01af9be-2964-3ccc-bb61-a14c6f44ac16 | -3.1256 | -45.7449 | 2025-11-18 00:10:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 91.6 |
| efe3d740-0c07-37ed-805f-27068d3d8529 | -3.4769 | -46.0879 | 2025-11-18 00:10:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 458c5e4b-5564-3c47-9005-87da39f0a68c | -11.6952 | -44.7081 | 2025-11-18 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| f52f4266-e660-38fb-afd0-4d7d3b72c86f | -9.0937 | -44.3124 | 2025-11-18 00:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 182.6 |
| 74e1f7c4-4771-37c3-abef-2545583fdefc | -4.1117 | -45.6122 | 2025-11-18 00:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 75.3 |
| c0bf3be8-0b33-3733-94c9-9a8b156d07ce | -4.1949 | -44.2476 | 2025-11-18 00:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 312.1 |


[Clique aqui para ver as próximas entradas](README2.md)
