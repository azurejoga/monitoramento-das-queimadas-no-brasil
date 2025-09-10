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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00798a82-7741-3e8c-8cd2-8f9d9c0b6e94 | -15.08362 | -50.08038 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7aa6c77a-a427-3b2e-b64d-76ae02491a5b | -14.38429 | -47.33379 | 2025-09-10 05:06:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e010427e-ec06-33c3-9f76-106b1df379cd | -19.64355 | -45.04862 | 2025-09-10 05:06:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aa4617a7-e01e-3d9c-b895-96ad90fad6b1 | -18.02442 | -47.14146 | 2025-09-10 05:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| a0da835e-f466-316e-8101-7ab3b8b627c4 | -18.45284 | -49.56822 | 2025-09-10 05:06:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8bb882ab-518f-396a-ac9e-2d14f5a1f382 | -12.62199 | -56.96635 | 2025-09-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 21954962-8bbf-3c93-92b1-2e4fccc4db32 | -14.86062 | -49.53484 | 2025-09-10 05:06:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10fefe5a-9edc-3973-8f0b-c1ee7a7b3a88 | -15.16494 | -47.95071 | 2025-09-10 05:06:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28f52e12-5cb6-3760-9bf8-7463d09e2b97 | -15.13158 | -52.39437 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c7bc89b-1b5e-3094-9093-9f0b35175014 | -14.85495 | -49.53994 | 2025-09-10 05:06:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c346e298-0d59-301f-b8a1-8a1341a23e41 | -13.93495 | -48.25954 | 2025-09-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f52f5eb2-e307-3930-9fa1-1ec68f63f25d | -15.28146 | -53.78574 | 2025-09-10 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df816ff2-b0fe-3c9c-97d7-4ae51a2fe8f6 | -15.16125 | -52.31773 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eab62df7-f905-35e4-86bf-61697efafa9b | -15.22756 | -48.24229 | 2025-09-10 05:06:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95f3a2f6-9d90-3f8b-a88e-cce4d4804bb8 | -18.00824 | -47.11974 | 2025-09-10 05:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cbfc2fae-167a-322d-81cd-2d39d0472166 | -15.195 | -53.82594 | 2025-09-10 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8dea2796-cf64-316b-94e0-a195f2933649 | -15.05203 | -50.13946 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 27308ae9-e8ab-3c7a-a64e-3df91dcf935a | -16.12652 | -55.86519 | 2025-09-10 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 38f69a51-ada5-3199-82c1-5bf812904286 | -15.47666 | -49.36417 | 2025-09-10 05:06:00 | NOAA-20 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 715b73c8-9887-3cdf-8348-fd21760c4627 | -18.0069 | -47.1125 | 2025-09-10 05:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9af2b65d-8171-31e2-a062-06577cf593be | -15.85917 | -51.83154 | 2025-09-10 05:06:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f70ae1e-f5a7-3d95-917f-ce9fbdd774ae | -14.89182 | -55.86865 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d12c613-aa41-3057-985d-fcbded35352c | -15.05266 | -50.13438 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e422571c-64f1-3685-81af-4f4e2535834e | -18.05813 | -50.72901 | 2025-09-10 05:06:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22825bdd-1b56-368b-9ca3-6746a976aca6 | -14.39001 | -47.33421 | 2025-09-10 05:06:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e39ff96-6ed8-3098-acad-8b717f571333 | -16.12364 | -55.86076 | 2025-09-10 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 27a68d12-c51d-3255-8a26-31d6d56342b3 | -18.34016 | -49.33455 | 2025-09-10 05:06:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0333b77-1bb4-326e-9ea5-fea03cad2da6 | -14.90418 | -50.11349 | 2025-09-10 05:06:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0c79a80c-1941-3039-b9a2-c4147014e960 | -17.30585 | -46.74784 | 2025-09-10 05:06:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 366593fb-2651-389f-833d-8974ffc051a2 | -18.34501 | -49.33895 | 2025-09-10 05:06:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24b08421-9af9-36bb-a248-c90fd43be6dc | -14.92261 | -55.92017 | 2025-09-10 05:06:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 454a8ca9-8480-33d2-a0eb-be983f8779fa | -14.613 | -46.36097 | 2025-09-10 05:06:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 598bdbb4-6ede-3418-8188-cb16f4eeaa7f | -15.47953 | -49.38302 | 2025-09-10 05:06:00 | NOAA-20 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| facd9703-471a-3544-b308-14c478c2b1d0 | -15.69293 | -49.90042 | 2025-09-10 05:06:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 07e0c123-1c00-3f76-9510-e7def8dfb30c | -13.9346 | -48.26244 | 2025-09-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a22f4d2b-b783-30a3-b6d4-971979e8bbf2 | -13.92927 | -48.26174 | 2025-09-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 911d926b-025f-3a7a-9fd5-ba320343b774 | -15.48387 | -49.38956 | 2025-09-10 05:06:00 | NOAA-20 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a1c6471-f136-3756-b589-c2aef6f72ebb | -16.62247 | -49.77198 | 2025-09-10 05:06:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 045a2a49-bc70-38cd-8dce-048ac6e995f7 | -12.60156 | -56.96665 | 2025-09-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47fc0a49-2acc-3bf1-b95e-ac72edeab575 | -16.45189 | -51.97903 | 2025-09-10 05:06:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f45cd22-c096-3a91-b67b-7c5982a84ab3 | -15.95573 | -50.22487 | 2025-09-10 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c6bb05e-567f-3721-892b-52cf35b7f7f5 | -15.28079 | -53.79044 | 2025-09-10 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f900c00-9bc5-3333-b2fc-0e90692a0d63 | -18.34054 | -49.33105 | 2025-09-10 05:06:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c466a8a0-46d8-326d-b8a0-f5821dc5f9f9 | -15.99692 | -55.96064 | 2025-09-10 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3d85128f-67c1-30f3-9ef3-56a42ebdc2e3 | -13.96983 | -48.22307 | 2025-09-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4713d9fc-fb19-3ba1-bbb1-4af73136b996 | -13.13068 | -54.9246 | 2025-09-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 570e7cf9-ccb9-339c-baff-fee01e62d289 | -17.71204 | -44.42286 | 2025-09-10 05:06:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5bb8d45-442f-3dde-9d69-ea343d04de95 | -15.81752 | -52.23058 | 2025-09-10 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e9cfb27-b5ee-3f9c-a6b9-6e13d82d811c | -16.62888 | -51.82523 | 2025-09-10 05:06:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc434ad7-4dbd-3f73-9210-81bb657f7900 | -20.06526 | -47.53781 | 2025-09-10 05:08:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b359a04a-a89f-362a-bfed-73e04dd48a33 | -23.03382 | -50.10341 | 2025-09-10 05:08:00 | NOAA-20 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| ed8a7a8b-9b55-31d0-9cc5-252d115d6b40 | -20.00504 | -47.63763 | 2025-09-10 05:08:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1cc4427-da9e-35f0-8828-d71ad018b6dd | -20.93978 | -45.79974 | 2025-09-10 05:08:00 | NOAA-20 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b09ce8a-e182-3bfc-85b1-ccb98cdea211 | -22.56934 | -48.56289 | 2025-09-10 05:08:00 | NOAA-20 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2d5dbc6f-f118-35e6-b475-63ba343b10da | -20.06836 | -47.54418 | 2025-09-10 05:08:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aece44e4-b079-39e5-96ad-d601356343b2 | -21.11961 | -47.73132 | 2025-09-10 05:08:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cdde1cec-c661-393f-8ca1-0aef8b223b63 | -23.36098 | -47.20287 | 2025-09-10 05:08:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8d179fbd-9eb6-325d-becb-5f9f565e0a42 | -20.44245 | -53.77487 | 2025-09-10 05:08:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee6a27d4-7a3a-397f-bfd7-fa4885bf4cd8 | -20.05725 | -47.53348 | 2025-09-10 05:08:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bdf6dea-1c1b-3faf-b6c6-8db42c7de2f8 | -23.03415 | -50.09991 | 2025-09-10 05:08:00 | NOAA-20 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 6a5aa4a6-5ff1-3abc-8ab7-53e1681e6f67 | -19.35053 | -56.70398 | 2025-09-10 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c32669a7-c2d3-3161-aaff-ea5998abbd25 | -20.9835 | -48.0104 | 2025-09-10 05:08:00 | NOAA-20 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 97a4b675-181d-3632-aba9-b3fbe945f84e | -19.99541 | -47.61132 | 2025-09-10 05:08:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fd94ade-c93f-37c8-9b20-8e1b1d14bb9e | -20.0111 | -47.63729 | 2025-09-10 05:08:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bfd80895-7858-357a-946a-b5c0f2f4ecfc | -21.11919 | -47.73606 | 2025-09-10 05:08:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b5b6bf2-f71f-33ab-b88c-83b8c4778f78 | -21.02208 | -48.42067 | 2025-09-10 05:08:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39f61527-e22b-3b21-b02c-411afc711e2c | -22.87431 | -48.13591 | 2025-09-10 05:08:00 | NOAA-20 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab5f6b6d-0cf4-3c7b-9423-6d90ab3cb7bf | -22.88031 | -48.13625 | 2025-09-10 05:08:00 | NOAA-20 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66a21d65-9d9b-3c16-aa49-90d87be111db | -22.21549 | -56.19535 | 2025-09-10 05:08:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6378560a-0ff8-3988-88e7-09e9ae5a46fa | -23.35463 | -47.20231 | 2025-09-10 05:08:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 158aec67-1bd4-3e46-9a8a-b42ecb6d6efc | -20.55152 | -47.62668 | 2025-09-10 05:08:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae1df49a-0c8b-30df-816f-3814cc7a5aa2 | -20.10521 | -47.82359 | 2025-09-10 05:08:00 | NOAA-20 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8705c8b8-d499-3ea8-8e0b-de2ce343a419 | -23.35919 | -47.19579 | 2025-09-10 05:08:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1cacfddc-26eb-3d85-81b4-9f4e741d7b07 | -21.78028 | -45.56722 | 2025-09-10 05:08:00 | NOAA-20 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a9b29bed-4c7a-3970-b7e7-023533bad4bb | -21.6718 | -51.95847 | 2025-09-10 05:08:00 | NOAA-20 | CAIUÁ | SÃO PAULO | Brasil | 3509106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 98a36a4d-4458-3b9c-807c-79669752abcb | -20.0628 | -47.53894 | 2025-09-10 05:08:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de0ebede-2179-3e5f-9436-60cad7b4efa5 | -20.8121 | -55.34298 | 2025-09-10 05:08:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 247a5750-09af-3a4d-a6a7-dda9e8ea9939 | -20.00632 | -47.62387 | 2025-09-10 05:08:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c830078e-9db7-36f7-9bbf-0fa569fc4258 | -23.50506 | -51.72809 | 2025-09-10 05:08:00 | NOAA-20 | MARIALVA | PARANÁ | Brasil | 4114807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7fb707de-6196-3560-8dad-743dbefb6536 | -20.00082 | -47.61818 | 2025-09-10 05:08:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6722dd79-e3d8-3f28-913e-154739b32a97 | -22.87742 | -48.13901 | 2025-09-10 05:08:00 | NOAA-20 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80cee8ab-893b-3b86-8866-e4477ed29ba4 | -20.07126 | -47.53864 | 2025-09-10 05:08:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c10964d-8bf6-3688-9aa0-f30b77e11335 | -20.01158 | -47.63225 | 2025-09-10 05:08:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c1632f57-74cc-3608-b96f-2c9e92aa2ba6 | -21.92066 | -45.64412 | 2025-09-10 05:08:00 | NOAA-20 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c7c81af2-379a-30aa-9e3c-63e97cf63417 | -20.37621 | -46.63765 | 2025-09-10 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0407a479-0f1d-35c4-b6d9-f703bd8ea800 | -20.10478 | -47.82811 | 2025-09-10 05:08:00 | NOAA-20 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4440e32d-752f-384a-8072-237d5a619384 | -21.12558 | -47.73241 | 2025-09-10 05:08:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad2f398a-92b8-3605-819a-f98d06a90ef2 | -20.98539 | -48.01073 | 2025-09-10 05:08:00 | NOAA-20 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 744e0181-a5bb-3862-b7ea-1211d1f55346 | -20.98583 | -48.00622 | 2025-09-10 05:08:00 | NOAA-20 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| de2b92ea-2693-3e4e-ab13-eb4c43711d78 | -20.85117 | -54.98885 | 2025-09-10 05:08:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cce1f94-2683-3a88-be8b-238aa7cfde6c | -23.35873 | -47.20156 | 2025-09-10 05:08:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3c834fa3-dda2-341f-bd23-06b44ab79981 | -20.9839 | -48.00591 | 2025-09-10 05:08:00 | NOAA-20 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bdafd0d1-3132-3a88-9e6e-7d7e68cbf927 | -23.02788 | -50.1096 | 2025-09-10 05:08:00 | NOAA-20 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e5d385e2-d054-31f3-b90c-e3ebd46f13f5 | -24.18503 | -50.96264 | 2025-09-10 05:08:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4f96adea-2637-39d2-9533-4670e01e5116 | -20.07484 | -47.53999 | 2025-09-10 05:08:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19c1b447-0261-3ff3-ae29-d18777bc1149 | -20.00681 | -47.61866 | 2025-09-10 05:08:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 003c3dbf-c224-36c9-b39e-b463192f76ff | -23.3614 | -47.19711 | 2025-09-10 05:08:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0e1ae468-41ec-3ae2-b060-6fa24f193416 | -20.00546 | -47.63311 | 2025-09-10 05:08:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 634e3f2e-7083-36b6-b1fd-2cd102f6e38e | -23.40715 | -47.26712 | 2025-09-10 05:08:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| cc58c134-ed6a-32d2-9d4e-c0a653b99ebf | -20.05969 | -47.53223 | 2025-09-10 05:08:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README102.md)
