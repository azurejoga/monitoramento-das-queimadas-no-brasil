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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 122ea764-8b4d-361d-ae15-3cd99ce2d1cb | -2.64012 | -46.57178 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 286dbe09-a588-3efc-a08e-9a2a733ccf81 | -2.11444 | -50.12871 | 2024-11-21 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77f40004-98b4-34f7-b4c7-79c4156d4304 | -1.61328 | -55.40673 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cdf7e81-d4e5-3d45-aa2d-28635b637045 | -3.15615 | -46.62398 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c39fadd-93fa-31a3-a180-34f76e2852bb | -3.2784 | -48.8021 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 41db5451-0671-3008-8b37-025bd1f5dfd2 | -3.3043 | -50.36213 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b85e93a-658b-316b-9fcf-e6db2ae56e90 | -2.27068 | -48.98872 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8779f675-98b6-32f5-8756-12eb8f2a8bd1 | -1.20427 | -51.77602 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 402dafd6-7ce9-3e15-8a91-f7e83816ff0e | -1.61028 | -52.61189 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2584f0fe-feb5-3b73-85e3-b867b5c7e651 | -2.95677 | -49.21368 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af5a03a1-80d6-3193-a5f4-e233182e1125 | -4.2456 | -46.10648 | 2024-11-21 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 278fe1ec-f189-35d3-be6d-b4f9020bf2cc | -2.69221 | -46.23956 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ead61c1-e695-3c3d-8467-773c997d936a | -3.26316 | -50.62205 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 393b37cf-3754-3c89-9089-0405d341315b | -2.56486 | -49.2017 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fa51295-fcf9-33c0-87fe-cb20be32410c | -2.66952 | -46.23607 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 30e7e41b-2c73-3998-a735-b5be5cea0932 | -2.55683 | -46.54111 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 869fc5ca-11d7-3bc3-9d45-dd11e766afdb | -1.87167 | -45.32017 | 2024-11-21 04:29:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41566bb2-01a3-3ee5-b5bb-10e1706e837a | -1.62266 | -52.26359 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 887406b8-ac31-3d45-89d9-efa5367ea775 | -1.55823 | -51.22927 | 2024-11-21 04:29:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 30bc8233-b27c-35c9-8515-9e12038d56f2 | -3.23281 | -48.78419 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f496576c-bfe5-38e9-8cf3-a6262f4f5f0f | -3.67503 | -45.24043 | 2024-11-21 04:29:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e7a2533-84eb-3df6-ac4c-d55c889e103a | -3.57517 | -50.41769 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d1b22469-83dd-35d3-9f5e-3e61fa88f6a8 | -2.10387 | -50.36274 | 2024-11-21 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 947a79bc-5af8-398c-b45e-806368ddc5a9 | -2.42256 | -46.5133 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 719c47ad-8ede-3708-b938-4fbc22b2d2c9 | -2.17575 | -52.13132 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f21db357-6899-341c-960f-237252d78c83 | -3.40288 | -44.19028 | 2024-11-21 04:29:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e59aef7d-1a17-3c7f-aad9-742fa006d0db | -2.04065 | -48.96175 | 2024-11-21 04:29:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88272880-8476-33dc-b053-4f3d6b8f6afd | -1.26472 | -51.60482 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 779f4add-cbe9-323e-b1bf-8b708f7ef813 | -1.34573 | -51.4339 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2394268-7e45-34cc-8aa0-3f045ceca2fe | -2.79112 | -48.57316 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8479e480-a5b3-31e6-8272-bd0c336746a7 | -2.78501 | -52.55006 | 2024-11-21 04:29:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7779a823-2a77-31a4-9c9d-7ceea934d383 | -2.91667 | -53.06397 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8c6a8d59-8978-314e-90f3-6bbf81ad7963 | -1.96029 | -53.00566 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b01f608b-557c-3801-95df-d69c8ad65bb3 | -3.08331 | -45.96746 | 2024-11-21 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51ede12d-a3a2-38da-847a-f92848135c2e | -2.18402 | -52.13273 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c4e52982-093b-30a1-9263-cd1b1ee3b503 | -3.34809 | -51.6476 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef878ce0-20fd-3059-b4c3-6e2320bba1b8 | -1.05127 | -51.74094 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 50b09cd8-8ede-34fe-9f46-a02363d05823 | -2.61838 | -48.18781 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96443344-d6b4-3e63-adae-d634a4fd1d5d | -3.95845 | -46.9053 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40f4a29f-615e-3203-a737-3047287341f0 | -2.95489 | -48.33141 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 60f49398-edb5-3790-96e1-61cfcc501c1b | -2.72719 | -48.73244 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 290fcbd8-f598-3bf8-ba6d-5734e778ef8e | -1.54083 | -54.89806 | 2024-11-21 04:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45ab461b-49f1-3334-b0ab-5a399c3e315c | -3.05885 | -44.34001 | 2024-11-21 04:29:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25adfe8f-0d4f-3451-94b0-dfc669a46c9b | -2.69663 | -46.23314 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5eabc19-206f-3a61-90f1-0ee41d33a196 | -3.35549 | -50.18292 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 667f170a-3141-3e46-b6f3-55811a3ec042 | -2.9032 | -51.77379 | 2024-11-21 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 533c404d-f075-3d63-97d8-8f0078cdcc24 | -2.6204 | -54.26995 | 2024-11-21 04:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6166aebf-2c0f-38f4-9635-e3f7b92b841e | -2.21411 | -48.20216 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94585e43-7be5-37d4-b0ee-83ea17f8ee19 | -3.0071 | -51.01504 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 26b06527-cb5b-3373-924c-e906a31e8420 | -2.08249 | -48.94497 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 573dab79-5eeb-3525-8922-532f6acddcae | -3.46892 | -50.00629 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 53d4154c-3080-3c0d-bb89-db631b91a366 | -2.25432 | -48.69806 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ff57c47-5921-38f2-90fd-617dacf24e11 | -0.94821 | -51.63913 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5121d6fe-a0dc-37dc-8b7c-82e868830e10 | -3.18617 | -46.49752 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 901afd3a-eb8e-34be-8121-db7e77781cdc | -2.39343 | -53.71429 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc024927-3ec4-3d84-b094-f05abb775b79 | -2.69421 | -46.07944 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1cd15d9-5ddb-3d11-a78e-ebfc87dd961c | -2.57844 | -46.55508 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9a77646-305c-345f-b294-e384e6dc3a4d | -2.2601 | -46.55816 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 30f6a488-6af2-3fc6-a378-6040837f5815 | -2.60692 | -46.26548 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41411fa9-f84e-349c-8ea7-47f96f7d5ecd | 0.41514 | -50.81273 | 2024-11-21 04:29:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b9dd401-00f8-357c-b6d5-f8721d26174b | -3.33747 | -45.81452 | 2024-11-21 04:29:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2afbfba9-f615-3a57-96d7-88c2c377fe4d | -1.6185 | -52.58814 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6082e781-2ed1-3148-94a8-b5b8bf55ef13 | -1.10819 | -51.75374 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9480c78-a734-3254-a2ee-0a7b2be56cd2 | -2.24881 | -53.67865 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 211dcb25-d31d-33d4-8563-d064bdd41227 | -2.69476 | -46.07595 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52d7da3c-9259-3493-b791-ca64733ccf49 | -3.18916 | -48.57501 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9e6f1b7-16bb-32cc-acf9-c6781b0931ad | -2.09343 | -53.34219 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 806ecec5-dd77-3e04-9132-9631ab79c37e | -3.37189 | -50.72139 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51f14b27-2a8e-38e4-9e0b-64ce99dbca9f | -2.42758 | -46.52468 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28cbc7c2-d522-37a8-b5f2-b6ba91716571 | -1.70413 | -50.20314 | 2024-11-21 04:29:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6dfa102e-80de-3499-92c3-b4a7100cd501 | -3.3962 | -50.25367 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 90ab6900-cb0b-3fe6-bfd4-1fc14d090be8 | -1.46799 | -51.12052 | 2024-11-21 04:29:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ed6d258-9670-30b2-aa26-8329177081ad | -2.94418 | -48.33341 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7768614b-c9b6-3b3c-af3c-b7055827b98c | -2.61966 | -48.07118 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d46f8985-b50e-3226-a3a4-25ec3a3e43ed | -3.18855 | -46.54755 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1faaca05-a9df-3ff2-b7cb-b2833b6b4f22 | -2.82107 | -49.15416 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 485dbd51-c7f5-3777-ad05-1042dc129029 | -2.63895 | -46.21355 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a30ec95-fdf1-3d6d-a8e6-ea0be3055b8d | -1.62712 | -52.58953 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 469ca9e9-fe6f-32f7-a037-cef5eb1c25c2 | -1.3664 | -51.38154 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecb5327e-8d84-3bb5-ac84-d4924c018069 | -0.81272 | -52.4854 | 2024-11-21 04:29:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1fca5ab-d6f7-349b-b0b7-0bd0babf117d | -1.19392 | -51.97575 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 635c1730-9e9a-33af-a0e0-eaa2933ee09e | -2.71896 | -46.09041 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da13cef5-f7ee-3b6c-9aab-7736bc318e37 | -3.51218 | -50.22764 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e302f562-c05a-3b8d-bc47-447587b1c504 | -2.06417 | -53.43286 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f44605c-e4a1-3e02-b90a-29d1c4855987 | -2.80717 | -45.96434 | 2024-11-21 04:29:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f703d5ad-f5ca-37c1-a9c9-ead4cbd427d0 | -2.82214 | -54.01855 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 642d0952-e60d-3560-b27a-b34d5fe3ba5e | -3.00241 | -51.31139 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7670da0d-3d2a-380c-905c-c0335ef40da0 | -3.78497 | -48.95582 | 2024-11-21 04:29:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cca7374-4832-3ab0-96f3-7228fbf9f038 | -3.84854 | -46.63309 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9c9e18f-60b0-3b99-9afe-f08e504cb841 | -1.46032 | -52.68217 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48fea9a8-8858-3dd1-b18c-e738ec88897a | -0.77502 | -51.76213 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5be9b8c8-d92c-3001-8209-c073f6477373 | -2.4558 | -53.70144 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b6888ac-be63-3f42-be10-d69c0dd9c279 | -4.06936 | -46.84455 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a3e2778-309a-3112-bc1c-3c4493a42ab6 | -0.96329 | -51.72313 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95534db7-6534-3fe4-8af7-7ccf574b2bf0 | -2.2482 | -46.82804 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3712008a-5f22-3298-b59b-0df20a210ba7 | -2.40734 | -48.61183 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc7f42cb-4e15-3c71-885a-048413adf750 | -2.91851 | -46.8663 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1859a745-7bfc-371a-bf7f-4fdc99ef5eb5 | -2.4051 | -48.60767 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08b4ba6d-01d4-3a53-9655-f44cc4831e8a | -2.61326 | -48.22004 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ac7fa14-bb39-3a5f-b923-a651325d1e39 | -1.96475 | -48.49837 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README33.md)
