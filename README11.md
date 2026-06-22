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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2d90a40-3956-3d45-b0a0-787a7c2865ad | -10.7145 | -50.1723 | 2026-06-22 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 1d823247-d529-3988-9c6b-5a9484728927 | -12.8736 | -44.3828 | 2026-06-22 16:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 416.8 |
| a4e251bd-5d51-3f61-8a13-0b887184afc5 | -12.8736 | -44.3828 | 2026-06-22 16:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 285.2 |
| 8eee1b35-ab45-3f16-ba9c-cf4837c0247a | -11.0432 | -52.4622 | 2026-06-22 16:20:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 184.7 |
| 1983147e-7c9e-3e1e-8194-e00d57928796 | -12.8354 | -44.3657 | 2026-06-22 16:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 2b523a7b-b929-36db-92dd-497ec91986f5 | -12.8741 | -44.3593 | 2026-06-22 16:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1320.6 |
| 777b0570-ecdf-3c65-af40-c457cc0957e1 | -10.7145 | -50.1723 | 2026-06-22 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 215b267d-49af-3422-b828-6f58331eed98 | -12.8543 | -44.386 | 2026-06-22 16:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 228.1 |
| eae830cd-1281-300b-bacd-b22362d1feee | -11.043 | -52.4831 | 2026-06-22 16:20:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| d932e316-2205-328a-9204-0cc2c2fc6b74 | -18.5134 | -51.5783 | 2026-06-22 16:20:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 106.1 |
| d5afa004-826d-32a6-b665-a20f28895e0a | -18.4934 | -51.5818 | 2026-06-22 16:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 90.8 |
| add89cba-04b7-3de4-9283-398be2b62212 | -10.8454 | -50.2867 | 2026-06-22 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 57d7849c-aa1a-335c-a44a-c77990b5e832 | -12.8736 | -44.3828 | 2026-06-22 16:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 292.7 |
| 5df9d190-0a89-3e6a-9cd0-c77c921a6fd4 | -12.8741 | -44.3593 | 2026-06-22 16:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1453.3 |
| 754eb3ff-05e9-37c4-9b28-2a66ee733cd0 | -11.043 | -52.4831 | 2026-06-22 16:30:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 1b4ddae8-42af-3702-8281-c57d325a6128 | -12.8354 | -44.3657 | 2026-06-22 16:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 52276c6e-2510-319d-9fcc-b7a135b4ac5a | -12.8543 | -44.386 | 2026-06-22 16:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 232.5 |
| 474aebd3-e94c-3bc9-8150-7a0bbf95ed00 | -11.0432 | -52.4622 | 2026-06-22 16:30:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 160.2 |
| 1d8b79c1-e24a-3fd7-a01a-6c45c4806aee | -10.7145 | -50.1723 | 2026-06-22 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 0209a164-6d2a-3cc8-9137-11d0245b01e8 | -14.0907 | -59.4768 | 2026-06-22 16:30:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| ba26244e-10e7-365d-ba06-35dfe86aab36 | -10.7145 | -50.1723 | 2026-06-22 16:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 5b226496-0b38-3afb-9045-d0495740f8c8 | -12.8736 | -44.3828 | 2026-06-22 16:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 277.4 |
| 31543c73-7337-36b4-8a15-bf31136a7b15 | -12.8543 | -44.386 | 2026-06-22 16:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 227.3 |
| 93b4963a-da27-32cc-a4a7-b36baeffe096 | -12.8354 | -44.3657 | 2026-06-22 16:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 5ed98630-1b45-3af6-b867-02d3418f39a5 | -12.8741 | -44.3593 | 2026-06-22 16:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1375.8 |
| 5ea995ab-4fe8-38cf-a2ab-09fc5fbbb008 | -8.8697 | -46.9437 | 2026-06-22 16:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| c690bbb0-a037-3186-a0ef-c6b96545eace | -8.3168 | -47.5503 | 2026-06-22 16:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| a9a07f3b-e91e-33c5-907b-f13718300329 | -18.5134 | -51.5783 | 2026-06-22 16:50:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 230c0365-56c3-3a3c-ac56-8aa32c6b3c33 | -12.8736 | -44.3828 | 2026-06-22 17:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 447.5 |
| be83bef4-66c0-3220-a055-b436e760a549 | -11.9108 | -43.4081 | 2026-06-22 17:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 3f012e1a-24a2-3320-9f77-d104370d6d2d | -18.5134 | -51.5783 | 2026-06-22 17:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 0f6d48b9-da82-3716-8bd2-558339626b45 | -18.4934 | -51.5818 | 2026-06-22 17:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 60c9e762-ac53-3355-b0c7-efc4a8be02f5 | -12.8543 | -44.386 | 2026-06-22 17:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 388.7 |
| a788638a-2293-375c-8a19-a59cfd275bab | -12.8354 | -44.3657 | 2026-06-22 17:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 206.1 |
| 69e2fe50-dd38-3914-a512-091bdf264ea9 | -12.8741 | -44.3593 | 2026-06-22 17:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1310.5 |
| 18cab2cd-9676-3651-8ad5-504ae9b0af74 | -18.4934 | -51.5818 | 2026-06-22 17:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 857edae8-9c3f-34dc-9a09-04d1c38d2334 | -12.8543 | -44.386 | 2026-06-22 17:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 196.7 |
| 7cf6b587-9ba6-3436-9cca-1cd2b84d8f1d | -12.8354 | -44.3657 | 2026-06-22 17:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 4bb8deff-cdb5-3521-ab45-ac76f68be02b | -12.8741 | -44.3593 | 2026-06-22 17:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1288.2 |
| ab533f38-dacf-3f4b-acdc-e5ee938fa672 | -11.822 | -47.3298 | 2026-06-22 17:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| e4715c8a-94b9-3f62-8873-d1d59aa82a89 | -12.8736 | -44.3828 | 2026-06-22 17:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 232.4 |
| 5eac7f84-e276-388f-8139-419848445b8d | -18.5134 | -51.5783 | 2026-06-22 17:10:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 6a1ce051-33a0-33ef-a740-e11f95f15f26 | -11.9108 | -43.4081 | 2026-06-22 17:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 9d15c992-c517-3e8f-b186-c80dab692eb4 | -12.8741 | -44.3593 | 2026-06-22 17:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1174.5 |
| ba837077-9c76-3749-aa8b-725f30fbe8d6 | -12.8543 | -44.386 | 2026-06-22 17:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 284.7 |
| ccdbb804-7d3b-305c-a209-5c6d308eaa27 | -3.8671 | -42.9685 | 2026-06-22 17:20:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| b4493fbb-d214-3e9e-8e61-fff316e48a5f | -18.5134 | -51.5783 | 2026-06-22 17:20:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 243d3a4a-be66-3ed8-acd2-fa3f9a781cab | -18.4934 | -51.5818 | 2026-06-22 17:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 158.5 |
| fb3e7bd9-a94f-3b20-b4ef-48e3ddf951a1 | -12.8736 | -44.3828 | 2026-06-22 17:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 335.9 |
| 7dc0748f-1aa3-3b62-b28a-cf4664025571 | -11.8216 | -47.3521 | 2026-06-22 17:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| ef511c60-2a12-358b-9673-871c06604865 | -12.8354 | -44.3657 | 2026-06-22 17:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 189.6 |
| f3c97c1b-1832-303a-b28d-5714a2fa59c3 | -11.3226 | -51.3838 | 2026-06-22 17:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 3e8df252-3ed1-307f-8bb2-03de9efcb1fb | -11.3224 | -51.4049 | 2026-06-22 17:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 345adaa1-2252-33b0-b2ec-20f19ba00d02 | -12.8741 | -44.3593 | 2026-06-22 17:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1248.2 |
| fa2cd2db-cb77-35cf-a526-2ca72be94c6b | -12.8543 | -44.386 | 2026-06-22 17:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 03f384cd-025d-352a-af7d-4521b7c6b940 | -12.8736 | -44.3828 | 2026-06-22 17:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 222.1 |
| 52831639-1c74-31ae-9e9c-7790b8ed4fe2 | -8.6147 | -47.7858 | 2026-06-22 17:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 7b004d80-6db0-375f-8458-6a781059e74f | -11.822 | -47.3298 | 2026-06-22 17:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| c198ce7b-a078-38fd-8729-91c3ec1758a9 | -11.9108 | -43.4081 | 2026-06-22 17:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 8c7fc23c-bbe4-3da2-aebf-52213e3bec87 | -12.8354 | -44.3657 | 2026-06-22 17:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 0f802151-4df3-3489-b05c-58c0ac563588 | -11.8216 | -47.3521 | 2026-06-22 17:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 85eb73bf-d01e-32dc-ba3b-37d7ce61b982 | -12.8741 | -44.3593 | 2026-06-22 17:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1186.5 |
| dcc84f8b-ff0b-3380-9f88-950f8feebbf8 | -12.8736 | -44.3828 | 2026-06-22 17:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 206.3 |
| d2e58cf3-fc4f-33c8-8e63-35c7da3d71d3 | -12.8354 | -44.3657 | 2026-06-22 17:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 4b1f0f80-cce1-3ceb-82e5-03cf0cfb7f58 | -11.8216 | -47.3521 | 2026-06-22 17:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| f773a6f5-39ce-3f20-beae-59f0ce61c5fb | -11.822 | -47.3298 | 2026-06-22 17:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 7765fe78-815f-31c2-80b3-64bf0f5411b0 | -12.8543 | -44.386 | 2026-06-22 17:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 170.8 |
| b6c92fef-388b-3d5c-9a99-dcb14652b960 | -18.4934 | -51.5818 | 2026-06-22 17:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 201.9 |


