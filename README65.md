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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f935daff-9a7d-3cb6-82de-6f14942eabad | -6.88765 | -43.74299 | 2026-09-17 05:16:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 449dfb87-5976-36f0-a685-314400cdc005 | -8.1442 | -44.85931 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6851a04b-9c0a-35d0-b058-a0ce0041a8b6 | -9.46654 | -45.4444 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 148edfc4-c8e4-315e-8fc7-cdde49a41b4a | -9.86703 | -48.35445 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b23e3f1c-ff19-3ac5-b7d3-a381aed2b06e | -4.55535 | -42.93871 | 2026-09-17 05:16:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7aed0293-07e3-3192-988e-a7dec3d7dc81 | -9.1059 | -45.72964 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| bc809292-2a0b-3459-90ce-a541ef095361 | -7.64623 | -44.33883 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c7b9330e-f91f-37f0-b0db-8b68fb2b38c9 | -9.0095 | -57.12888 | 2026-09-17 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64437e89-f735-331d-8326-c435df9e5a17 | -8.8506 | -46.92266 | 2026-09-17 05:16:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e60cf8b6-2106-3585-997f-79738f0e0af0 | -7.27588 | -46.80343 | 2026-09-17 05:16:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4547b2bf-52cd-34f1-9ada-1f7709886f38 | -7.02513 | -42.07133 | 2026-09-17 05:16:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 952ecc3e-e01b-37c4-8977-80b4101c158e | -6.02724 | -59.93176 | 2026-09-17 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d184c1a-18ef-3dab-9544-aeae8554fc5e | -5.75153 | -57.59788 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 184d0aca-eb8f-392f-8488-59fec9ee7463 | -5.22232 | -49.33091 | 2026-09-17 05:16:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6633dcc2-ef89-36eb-8451-2f08fa37c026 | -4.48926 | -55.49428 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f77e9014-7797-3d4b-84ad-e926e26e07bc | -4.53197 | -54.97271 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2e44631-6cd3-30f9-bcd4-c3402f2b6c7d | -5.76216 | -45.10536 | 2026-09-17 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 991318b7-8409-3dfe-a450-e43d99deb74b | -9.62052 | -45.36047 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dc082afb-6b1b-3b4e-a7bf-01d1f80b4140 | -7.46227 | -46.83681 | 2026-09-17 05:16:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25733ac0-8a19-33ac-a886-dfe3aa8b1962 | -2.64165 | -54.68944 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4fe4d275-3cf6-3fa2-9bdd-72e0929ce7f1 | -9.61443 | -45.36245 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e8019dff-a303-35b2-a5c2-e97c9eda8a86 | -8.42865 | -47.75208 | 2026-09-17 05:16:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce93a412-d920-3370-8704-8f0734e32c41 | -5.46406 | -44.95831 | 2026-09-17 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d708014-b110-38d1-96ed-8d49ce06e3c4 | -6.80155 | -59.18165 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 787e5d8c-9dd1-3603-a94d-bcc967ac1af3 | -9.61892 | -45.37328 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 875a687c-139e-3767-a727-57bd8014970f | -3.13643 | -59.02055 | 2026-09-17 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38e6dc66-1526-3593-89ba-8c4f83978222 | -9.61671 | -45.34117 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 831fcc76-da7b-348b-a1a8-1370e6846c72 | -6.80289 | -58.78947 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50e3c9d4-870f-3099-aad7-ea07b298b75f | -5.86192 | -51.94896 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d534b66-24e4-34d1-b8e0-612d67a7d3b6 | -7.96733 | -44.83649 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73b9202b-f111-3bf5-8c70-7c01f57129a4 | -3.81701 | -58.89177 | 2026-09-17 05:16:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0be9e42f-cfb4-37ce-9bf2-03dccb0caacf | -3.78473 | -54.35184 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be19fd46-440c-3051-9480-4df6bf79489e | -5.86261 | -51.94445 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d0ceed4-a8a6-3a1d-b04e-50547e1e7dad | -2.95931 | -50.32343 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b85d0055-35b2-3d0b-8162-01befeb8a221 | -5.9064 | -59.93871 | 2026-09-17 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dda90c97-253a-34a6-9bc6-199344486e1b | -5.15204 | -55.9477 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd77edcc-1098-3b72-a43a-5e268b45d13a | -10.51062 | -46.28178 | 2026-09-17 05:16:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a12fb634-293d-38ce-a6f2-9b26e40eab0f | -5.61777 | -45.2467 | 2026-09-17 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acee015a-da95-32f1-abe3-975f4ee514b7 | -6.36984 | -58.28539 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| debaad7a-773a-35ab-be92-4ee81425dcec | -6.8053 | -59.18303 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8fdbb65-685c-3e2e-ba8c-f6ed8534b432 | -9.87211 | -48.35483 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ce9b377c-d9a0-38b1-b727-e4cbcba3d32f | -3.28352 | -57.91516 | 2026-09-17 05:16:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fe06459-8ebd-3fc5-8a44-04404e65d9f0 | -9.96133 | -45.31986 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84bbd816-8182-380a-ac21-dc7a539a832d | -5.54232 | -56.17406 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8efdae43-820a-3f05-99f2-98a7ce83010b | -6.90207 | -59.02575 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d07de6a-d2ca-3c84-af1a-e6298f8d8aea | -8.48032 | -46.89201 | 2026-09-17 05:16:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f777f6bf-1d37-3a9d-8c9d-70df20d8317e | -9.83461 | -48.36738 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f490dea2-ba54-3324-94f4-74ec9982ba1f | -2.90476 | -54.17945 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ede5e1f0-a29d-3d06-8e7d-d5011463b771 | -2.95853 | -50.32852 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 57468d1a-bb7a-3ba1-95dc-6bc6b1ab7097 | -4.8582 | -56.02563 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ab1b346-a85d-3967-9646-9981ca56ee2f | -4.10432 | -56.34534 | 2026-09-17 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3c0219b-f1fb-31f6-95c7-9591c063d761 | -6.03712 | -44.02824 | 2026-09-17 05:16:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e60b62f-cac0-38b5-a4b0-75d26dd59ecc | -7.96801 | -44.83145 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04fad1f6-ecd2-3715-be20-511dfac030c8 | -5.76917 | -45.09829 | 2026-09-17 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9e556a2c-3758-3c4b-b752-4f69a4c904d2 | -3.44241 | -58.41149 | 2026-09-17 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27cab9a1-4cdf-3070-a57f-d068ecfeeb6a | -3.33192 | -59.82591 | 2026-09-17 05:16:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2df4fc21-4a62-34fe-88d2-ac2456582b72 | -4.56628 | -54.90689 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3999b17a-e002-3ada-bebf-d8d5b1089e8a | -5.13705 | -55.93466 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6efd716e-420a-3b23-a420-45b07627d174 | -4.37361 | -55.02956 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b317e18-0b08-35e0-b157-c8d963f4cce3 | -3.28446 | -58.81983 | 2026-09-17 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 702bac68-1539-327a-9a0d-e3f702ba1bb7 | -8.47488 | -46.89121 | 2026-09-17 05:16:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d40383b-9f2a-3adc-84ba-1805a8531157 | -5.76745 | -45.11048 | 2026-09-17 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 5f1dd336-7fdb-3853-8dcc-4ca4e4ef5d25 | -4.43868 | -55.51828 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f6b4eb1-cc77-3fd6-a81f-d3cdf9f83454 | -2.97281 | -54.15034 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1178773f-5a8a-393d-bf18-e154d5fb1c30 | -5.77563 | -45.09519 | 2026-09-17 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 92cb2572-00a5-386c-8add-413d1571cd44 | -5.61831 | -45.24282 | 2026-09-17 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58378e67-c76c-3212-a747-ecd6f027c3b9 | -3.45839 | -59.2442 | 2026-09-17 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee540e4b-a08c-376c-a851-acf80326bf50 | -3.73886 | -55.94166 | 2026-09-17 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d796859-8a27-3dc5-98ee-3843bcb1a885 | -9.84035 | -48.3717 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5211c396-0461-3036-9921-b607afd0c52d | -9.60451 | -45.34328 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 37ae415b-ed28-3da3-8831-37668d2c1a6b | -4.39594 | -55.44418 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fdf2e8c-b762-382b-a49e-e7700382ffaf | -5.86356 | -52.06238 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 97d383af-e733-3a76-8d72-8c9c9d2ac4b3 | -8.85589 | -46.97558 | 2026-09-17 05:16:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 41cca50e-0faf-3231-8bf4-442c6ef6c003 | -2.9601 | -50.31835 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f925382-169c-31df-9c74-141595367518 | -9.83962 | -48.36821 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 424d1f13-b3f5-3564-839d-70806817ca8c | -7.27801 | -46.80124 | 2026-09-17 05:16:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 954ab07c-24e8-36f5-b563-f67250244a0a | -4.87541 | -56.06776 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08c2ebd8-b738-326c-b58c-11a0ec55c112 | -4.28547 | -54.77406 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 071fc109-b96a-3988-99d0-cd351e368b9f | -8.94966 | -44.39594 | 2026-09-17 05:16:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8cc0c59-4e08-3b19-9359-40ef5f0a7828 | -8.42906 | -47.74898 | 2026-09-17 05:16:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eac5fa11-7756-3157-b1a6-2562b581b852 | -6.31118 | -62.67309 | 2026-09-17 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 252c1846-b8e0-3284-b999-b163a97347b2 | -3.26669 | -54.26111 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ae537b3-ae78-36d4-b60e-529ca4d9338d | -2.9131 | -54.17001 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62190ea4-df30-376a-a5c8-3285bbbf80f4 | -6.10335 | -55.57983 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f3e2487-d8f4-330b-8619-3ea6c9b7b918 | -5.0604 | -56.20119 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c83a81d6-24d3-3ff9-aa0b-b5a82aa5746c | -3.58601 | -58.53658 | 2026-09-17 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2684922-3f00-397f-aa1d-674b42676743 | -3.70932 | -51.10694 | 2026-09-17 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a7b7a31-fc70-365a-bc93-18e66e86547f | -4.40693 | -55.0774 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77acaa37-8125-3b29-bd33-3aabea9ffee1 | -6.31658 | -62.6692 | 2026-09-17 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31132864-c124-3bff-9296-99f19070940f | -8.41373 | -54.72916 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0032cc8b-a3d1-3b07-b621-f0ed6b6fb2db | -5.77505 | -45.09931 | 2026-09-17 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f43cd48a-096f-3280-b53e-f6eeb5bb102e | -6.8125 | -59.18343 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da69090f-a157-3fbf-988a-75ab03596460 | -3.4821 | -54.70126 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ac67778-4eb9-3e3b-8aac-b0d3af9ce7bd | -9.12039 | -45.73313 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 355fc1a1-c86b-3b24-bd56-6951a855dda3 | -8.47441 | -44.55933 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 96bef1c9-c00d-3a27-86d6-da8064fb1d9c | -4.42039 | -55.50476 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4c01a00a-3a85-30c3-be3e-be610436f1de | -3.48045 | -54.71166 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b0f97709-a732-3e71-9d27-0deb41d59fae | -4.50426 | -54.97544 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ca7aacfa-5f95-3b53-b7b7-1270fb6bda16 | -7.37452 | -44.48489 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| a40c9b57-6911-3d5d-a2f4-abc1c70f2ce2 | -6.83516 | -55.76285 | 2026-09-17 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README66.md)
