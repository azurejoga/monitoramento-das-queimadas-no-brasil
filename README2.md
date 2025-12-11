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
| 6d48135c-fc06-3741-806c-25e9c47ad38d | -3.22533 | -47.47171 | 2025-12-11 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12f7b02e-cac5-36d8-9bee-af9b4d87cb9c | -2.26372 | -51.93866 | 2025-12-11 00:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0b5d3a47-6d38-343a-9c64-1630dbbb31df | -3.52047 | -47.20788 | 2025-12-11 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 48e94ef6-bcc7-383b-9896-d1f166ef3fc0 | -3.34478 | -46.86423 | 2025-12-11 00:13:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| daafcadf-f9c2-3f04-98ab-6d232b0f1e50 | -2.02641 | -45.86249 | 2025-12-11 00:13:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 18.1 |
| e4b21258-be69-3136-a5d1-14c3a77dd3d7 | -3.60236 | -47.53574 | 2025-12-11 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| c33d5ded-84be-3b81-b84d-c1c8bfdfbf7a | -2.22252 | -45.4156 | 2025-12-11 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7d7ce8b2-5b50-38d8-85e8-c806aa9f3caf | -3.95273 | -45.4719 | 2025-12-11 00:13:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f664610f-a955-3390-a843-653922affb43 | -2.21122 | -45.67019 | 2025-12-11 00:13:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ceda8b91-0cf9-3870-9857-1a37989f83cd | -4.07369 | -43.68611 | 2025-12-11 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 4ec1b577-c310-38f7-b702-d232d15c3493 | -2.34716 | -45.6479 | 2025-12-11 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 64db3395-bedb-3b86-bf79-46a8e447017f | -3.392 | -45.41529 | 2025-12-11 00:13:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e9b768c8-833b-30e6-b109-906e64b90d82 | -1.93992 | -45.43685 | 2025-12-11 00:13:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ac6d6c41-5aff-39c3-a4bd-aa9f407c2429 | -3.62575 | -44.64161 | 2025-12-11 00:13:00 | TERRA_M-M | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3dec9db4-9150-344e-8209-a3c30406b823 | -1.69656 | -46.54918 | 2025-12-11 00:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 7c4d43ee-4257-3b18-ab36-1c5428eb82de | -4.53708 | -44.04531 | 2025-12-11 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 42cd4e75-c409-3449-b4c6-219eb4664cca | -2.85608 | -45.79926 | 2025-12-11 00:13:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 00f2b493-3850-3699-8195-c0ed9e6d6ab8 | -3.95828 | -41.53052 | 2025-12-11 00:13:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 24.4 |
| b138886c-856a-3208-978d-1b2521d9ce6b | -2.59848 | -45.40254 | 2025-12-11 00:13:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e1a5752b-8d09-3b46-b9fd-290ae3b0fa5c | -3.69791 | -50.94355 | 2025-12-11 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| f933857f-ae74-34d4-a41f-d19850d1318d | -4.08092 | -43.69949 | 2025-12-11 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 39d542fb-8545-304f-803d-74af59ed34c2 | -2.75206 | -45.64816 | 2025-12-11 00:13:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 3e8af1f1-945b-3698-a050-bf76451ed407 | -2.32335 | -46.48099 | 2025-12-11 00:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 25ab4bc4-0fdc-31fb-aa31-89fbb0819143 | -3.34818 | -46.2195 | 2025-12-11 00:13:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f3bc07e2-4ff2-39fb-acb1-76f545654fb4 | -1.15885 | -47.52114 | 2025-12-11 00:13:00 | TERRA_M-M | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fcc8b548-47a3-3996-a06e-0a8fe322d7b2 | -4.3083 | -44.11674 | 2025-12-11 00:13:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 60d0a645-c9af-3bb2-95ea-3a538b748d19 | -3.23433 | -47.47047 | 2025-12-11 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| cfd73f5c-76cc-320c-95be-fbbe240e2996 | -4.8294 | -44.94269 | 2025-12-11 00:13:00 | TERRA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3d7c5af3-9c8b-3e39-9eee-71372ef94075 | -4.681 | -43.25191 | 2025-12-11 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 690ebd73-7cbf-3480-b989-3ef51b866f8f | -2.21887 | -45.66001 | 2025-12-11 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 90ff3cbe-65ce-36f5-a5d6-ae12f356d753 | -1.68515 | -45.799 | 2025-12-11 00:13:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 54760f99-146f-3180-b075-33e6a55eb0fd | -4.23528 | -42.50385 | 2025-12-11 00:13:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| e1a7c906-cc34-32e2-b884-7921df827206 | -2.90946 | -46.72073 | 2025-12-11 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| df5ab731-1dd2-3001-b7e0-1e1a736d2d59 | -1.45208 | -45.64323 | 2025-12-11 00:13:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0412868e-e2f3-31ca-a204-b8d57e6d7309 | -3.4051 | -44.17779 | 2025-12-11 00:13:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 41c83e78-6558-3740-972f-b1e1fc80acdb | -5.45911 | -47.77551 | 2025-12-11 00:13:00 | TERRA_M-M | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 186f4a20-3c97-384b-a9cd-8d7435c798f9 | -3.48773 | -51.52977 | 2025-12-11 00:13:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 37b99044-2e37-3618-b64b-027ebf4e1b9f | -4.68253 | -43.26251 | 2025-12-11 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1b33d11a-68f8-3192-b891-9e3527ae756d | -4.50945 | -44.63451 | 2025-12-11 00:13:00 | TERRA_M-M | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3772ff69-050e-316d-bd5f-0a75a53bcce3 | -2.89929 | -49.5358 | 2025-12-11 00:13:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 78a92698-7f9c-3499-aa09-f91f66ae555b | -3.68194 | -52.5283 | 2025-12-11 00:13:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| ead74515-1ac9-30ed-9234-6494e7cc841b | -1.31483 | -53.49538 | 2025-12-11 00:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 59a726b9-d912-31ba-a418-5a34a8f206a4 | -2.20917 | -51.89497 | 2025-12-11 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 809e3404-13bd-3102-8218-945cc7fff175 | -1.80467 | -54.05325 | 2025-12-11 00:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| bc95d683-6bed-38dd-bdc5-60462bce54c7 | -1.58292 | -53.75679 | 2025-12-11 00:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 958081c3-d6d5-383b-b1fe-e7e7d5ac1ffe | -5.1786 | -44.80383 | 2025-12-11 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e974d267-911e-361d-b39f-4f77969f53df | -4.16691 | -43.83134 | 2025-12-11 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a6c2368e-5f8f-37cf-937e-0fa6e9e39375 | -4.237 | -42.51581 | 2025-12-11 00:13:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 5778db14-d178-38dc-b209-8447fad5f6e6 | -1.8144 | -54.05839 | 2025-12-11 00:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 552bcedd-8a21-32a9-8b04-9d1be73d2386 | -3.95508 | -41.52302 | 2025-12-11 00:13:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 45.6 |
| 7938d64e-f296-30a4-a4e8-49cd48a63a33 | -1.10862 | -53.6932 | 2025-12-11 00:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 2c34e388-77a0-3f07-8b07-ab8182b048e1 | -4.2101 | -45.39889 | 2025-12-11 00:13:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 82f29846-445e-38e4-af22-78ca1c125eb8 | -5.28947 | -47.21099 | 2025-12-11 00:13:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b45a6b38-6880-3c9d-a4e3-18d65bc77d07 | -5.19042 | -43.08701 | 2025-12-11 00:13:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 64eb26e9-bad8-3cf7-bdf2-f44298024d92 | -1.69777 | -46.55795 | 2025-12-11 00:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 079bfd8b-402f-3399-911c-9cb640e79d4d | -4.05976 | -47.31016 | 2025-12-11 00:13:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 33a73c3e-b156-3c64-8f4d-7ab5d20a1f22 | -3.53784 | -45.46431 | 2025-12-11 00:13:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 58371dc5-24be-31d8-acf5-4cd4914bd56c | -4.83832 | -44.94139 | 2025-12-11 00:13:00 | TERRA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 318ed8ab-529a-334a-a5cb-c361c40cbbfa | -3.50725 | -45.9073 | 2025-12-11 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3e4769be-354a-39ae-862a-7a2e97c36ad2 | -3.56006 | -46.95824 | 2025-12-11 00:13:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 02f11767-2d4f-346c-b37c-daba6cd26885 | -4.01729 | -50.32872 | 2025-12-11 00:13:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b9827f2f-aa26-33a8-be86-639a7c2ba0b3 | -2.95816 | -49.14653 | 2025-12-11 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 51471777-918e-36e4-a523-cd2e2a8bdbd9 | -2.85096 | -46.83419 | 2025-12-11 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| b1a591a4-e417-37a1-a07d-ea50bb7ae98a | -2.65894 | -51.65252 | 2025-12-11 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b33b3fe1-2b4c-399d-9ee0-1f9bc2fb3832 | -4.11252 | -47.29339 | 2025-12-11 00:13:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 90e35931-18db-3c07-8f6b-71e0fed1cdac | -4.07511 | -43.69633 | 2025-12-11 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| fc67395b-9000-3271-9f4f-37a109e311f6 | -4.53845 | -44.05502 | 2025-12-11 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a00563e5-f077-3e8a-8e13-265d37169fbb | -1.86868 | -46.65584 | 2025-12-11 00:13:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 425bfcee-322f-374b-932e-98f5027f3e81 | -1.52962 | -47.1311 | 2025-12-11 00:13:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 53844429-1ac9-30af-95f9-8d8813187842 | -2.84974 | -46.82536 | 2025-12-11 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| e3596811-2c18-35ec-8240-2e950d5721c6 | -5.29075 | -47.22029 | 2025-12-11 00:13:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fbd6d817-893e-3dbc-8639-8ea93b327dca | -4.94118 | -43.96282 | 2025-12-11 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b57834d8-1ea6-3d43-a240-d01390d06d14 | -3.97067 | -44.47212 | 2025-12-11 00:13:00 | TERRA_M-M | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f6c6526d-9007-3f9c-8701-3fab42678eca | -3.26519 | -46.41645 | 2025-12-11 00:13:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 20a3db52-66bd-34ca-bdc4-d0dd67ee14c3 | -4.2287 | -45.3903 | 2025-12-11 00:13:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c628f05d-001b-3a2a-9edc-2cee544e18a2 | -2.21231 | -45.40783 | 2025-12-11 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 203.3 |
| bc7b2405-1eb0-3c7b-a9db-6279a641b566 | -2.02765 | -47.13915 | 2025-12-11 00:13:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cae30323-2f95-329f-997f-93811befa6e4 | -4.21075 | -44.47693 | 2025-12-11 00:13:00 | TERRA_M-M | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 339086d5-ec81-3fa0-af55-a8e3c0db822f | -2.68889 | -45.58444 | 2025-12-11 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 5d96d171-b860-3b06-a2e9-8caab3cecc87 | -1.19819 | -47.54303 | 2025-12-11 00:13:00 | TERRA_M-M | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5c98b78f-0e9f-3ec4-aad1-13469e060cc6 | -2.67543 | -49.17027 | 2025-12-11 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d07adae4-18e4-3896-bddb-1d793326406c | -3.2664 | -46.42523 | 2025-12-11 00:13:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| efc8ed55-d081-309c-ab80-1442e8ab97f3 | -2.02278 | -52.05249 | 2025-12-11 00:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 49c97dc4-9186-34f0-b1a5-683b6adcd2bc | -3.75 | -45.06786 | 2025-12-11 00:13:00 | TERRA_M-M | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8836af6e-cd5f-3324-9504-400fd1e65868 | -4.65461 | -44.48797 | 2025-12-11 00:13:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 76098f55-2d20-3a6f-b2cb-acc75963915b | -3.02267 | -45.4099 | 2025-12-11 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 25125f9f-9848-3844-b0f5-3735a001a7e5 | -3.01584 | -45.1561 | 2025-12-11 00:13:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 77892986-b612-3c6e-893f-45445b643f6c | -4.06876 | -47.30888 | 2025-12-11 00:13:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e10ce728-5522-3427-9f5a-f1c15728374f | -2.23617 | -46.51744 | 2025-12-11 00:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1812e51c-9b85-3bc9-9449-83d7e3714475 | -3.69888 | -50.9492 | 2025-12-11 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 6d524d8f-426f-34d6-b896-eab528c9733b | -2.02296 | -46.56845 | 2025-12-11 00:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 06fb4bd0-ac7c-3caf-9ec4-56b2381847bd | -2.25469 | -45.77603 | 2025-12-11 00:13:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 905f5d53-feaf-33b2-bd17-854ca0e906da | -4.31953 | -45.38026 | 2025-12-11 00:13:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 3373f5af-f4ce-32ff-a500-1cea9ceb2d6c | -2.94039 | -45.14527 | 2025-12-11 00:13:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9fc14b57-7531-32b5-b823-f0e32e2cc0a2 | -2.41244 | -48.26794 | 2025-12-11 00:13:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 182f6a78-e891-38b2-bef2-2dbdb01bffcc | -2.22125 | -45.40657 | 2025-12-11 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 609bd965-1250-382c-8c86-480a786b4497 | -3.54671 | -45.46305 | 2025-12-11 00:13:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 650d965f-5339-34e6-8340-8b0c27ef9936 | -3.39767 | -42.10032 | 2025-12-11 00:13:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 2f870c26-5e95-32c1-be06-3bbc0745d4ad | -3.85456 | -45.22187 | 2025-12-11 00:13:00 | TERRA_M-M | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 083d6d82-3c9c-3392-b3f0-e1cf9ce3ca12 | -1.16805 | -48.8519 | 2025-12-11 00:13:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |


[Clique aqui para ver as próximas entradas](README3.md)
