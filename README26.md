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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb234473-e19f-39ea-8e6f-355013d893d0 | -5.73144 | -43.27873 | 2026-09-28 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| e70b4ccc-7453-37e3-8a97-2c069cf0edab | -3.19885 | -51.03524 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 77e55eba-dc7a-3b98-b2a0-3a81c9e6116d | -5.13018 | -50.71595 | 2026-09-28 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9866f700-867b-3346-9dd9-2c53702dc3fb | 0.2851 | -50.91125 | 2026-09-28 04:32:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4706b04d-fe5f-3901-a61f-6f306bf42f95 | -5.89416 | -42.44074 | 2026-09-28 04:32:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c316db9f-47eb-3c68-a94b-f09afda02e7d | -5.89885 | -42.43764 | 2026-09-28 04:32:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8d913f3e-ff08-39aa-a09d-fb7d1e9ad113 | -5.67665 | -41.35675 | 2026-09-28 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 65a38952-6d15-3d6c-ad56-e1f3ab7f0537 | 1.65176 | -55.90546 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe0c84e6-12f4-3636-b910-ddaa3fa12dc7 | 1.6451 | -55.89899 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49ed9133-3803-3007-a53b-245d971abddd | -3.19815 | -51.03968 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bc71f66d-bdde-37c1-9186-c22d474c81e5 | -2.65928 | -51.73373 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0b104f03-51f2-36dc-823c-922cf5e23902 | -5.64087 | -43.71846 | 2026-09-28 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4189bca1-300e-356b-8277-d2176b28823d | -4.41603 | -46.29852 | 2026-09-28 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 695604b6-f425-3e60-bfb4-d256225e9a2a | -5.79417 | -46.09342 | 2026-09-28 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fb9373c-92cf-3816-b684-6f46f3ef79e1 | -3.15029 | -54.09249 | 2026-09-28 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 577d831d-94af-3936-a14e-db9e455a24ff | -3.29121 | -50.30869 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38944dc1-1de3-3016-be0f-3df724cb4197 | -3.4251 | -50.41999 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0844e826-1b89-3d07-9b2d-ee9bd912c792 | -4.37779 | -46.24149 | 2026-09-28 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e4f3fa1-2b34-3246-aaeb-ed40e9ff0118 | -2.91295 | -54.12598 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 534c9fdf-af2a-3d84-8e12-d1d6ba92ff9c | -3.2081 | -51.03949 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 244e8cdb-8bfb-3010-ae60-d9ea4d5af6c8 | 1.67464 | -55.94316 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10df6a00-d80c-39c8-9719-b5682fdcff77 | -5.72751 | -43.27815 | 2026-09-28 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 32194f85-7c96-3c4b-9827-572ffd4f9b7b | -3.80491 | -44.09742 | 2026-09-28 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b949587f-0af0-36cb-89b2-d6d8ea0a0328 | -1.93064 | -52.14458 | 2026-09-28 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 232360e3-eb72-321d-9ebb-5c60febda821 | 1.6512 | -55.90183 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 452d598e-f1e9-3a86-b655-e3dccfcbfd9a | -5.19138 | -45.81428 | 2026-09-28 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4f30fef-78ab-3775-9c55-fac1ff16a264 | -5.67918 | -44.77622 | 2026-09-28 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35b05b88-1b12-3a75-9694-b8da87e6dba7 | -5.72746 | -43.27673 | 2026-09-28 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9e9c7b2e-b64c-30d0-ba99-a0968d81d0a2 | -2.56041 | -54.73259 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2f243ad0-9d69-30de-8134-da3e8c5ccece | -3.41802 | -48.33867 | 2026-09-28 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 9d7fabf0-15dd-331d-a81b-116c4683c15d | 1.66497 | -55.91867 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5e78ac0-3f9e-3217-9cb8-0e978ad4bbc4 | -3.19514 | -51.03465 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44d3120a-c5bd-3c8a-8d20-29acc39ac70f | -3.14805 | -54.07813 | 2026-09-28 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 48860c3e-9c49-32d2-bd71-80aa8d6d15c7 | 1.65954 | -55.9191 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed6d721b-7cd4-3238-9f07-8c5f2c3d1bea | -5.89525 | -42.43322 | 2026-09-28 04:32:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a9655802-1a16-3c46-bfc3-7f460a3b2213 | -3.20929 | -51.04144 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a18252cc-f7c6-3eee-bd87-2dce2268228b | -2.65799 | -51.73629 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 398ece7e-1373-3033-8029-20ef323cdf37 | -2.20334 | -48.85783 | 2026-09-28 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08c495e8-640c-35a7-a080-7361ce3e8a38 | 1.66852 | -55.9403 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46036fe0-2fd7-3135-94fd-235f12219cb5 | -1.77096 | -53.76345 | 2026-09-28 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 75f860f7-f88b-3c82-959d-fb503a4f20c3 | -5.85078 | -45.17271 | 2026-09-28 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d327ec06-4d1f-3c1d-b9be-c86ed009c5cc | -5.63567 | -43.72715 | 2026-09-28 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 910f7e51-6686-34b9-94f0-77de3ff3b0de | -3.80855 | -44.09798 | 2026-09-28 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 955afd1f-eba8-3419-b8eb-b0bbf0a1abb7 | -3.37653 | -44.36965 | 2026-09-28 04:32:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 46aed25e-7012-3976-a382-c829716ccc4f | -1.91009 | -52.06524 | 2026-09-28 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3211094-b808-3365-bb0c-86dd275e6bc5 | -4.00021 | -50.63994 | 2026-09-28 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8859b752-8a7c-3081-bf26-352d857e313e | -3.15255 | -54.07896 | 2026-09-28 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 89f0db2a-f37a-3853-8010-9934f13a2790 | 1.65401 | -55.91992 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd0b1cc4-d1f4-3611-bdf1-64cc37c676ca | -2.99922 | -50.47516 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60ee35d9-cae6-3f92-9c1b-70c11dafc22c | -3.79998 | -44.10535 | 2026-09-28 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 595b7a29-2ea2-3107-bfa7-64de74b0939b | 1.67214 | -55.92883 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef617c82-564c-326b-b3e5-b9b3d39b1903 | -3.42344 | -50.41593 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2319aedb-0553-319e-af89-57e4123ed3ba | -3.36938 | -44.36856 | 2026-09-28 04:32:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ca0389a-7b0e-3c94-82e4-a17d98f0d897 | -3.37295 | -44.3691 | 2026-09-28 04:32:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d23a5f98-f9e0-38a6-89d2-9a4669b03bba | -3.0182 | -54.20542 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce1a155c-5a1a-3f47-bee7-a24fdc0eae7b | -3.18825 | -49.24987 | 2026-09-28 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c274771f-6e0d-33f3-acbd-256915e9d4a1 | -5.84725 | -45.1722 | 2026-09-28 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6b67c27-4794-3c7b-b125-e75e74c01c04 | -3.82142 | -44.08694 | 2026-09-28 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c30d448c-472a-3732-b16b-3519513c22bc | -5.3297 | -46.19489 | 2026-09-28 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89a91051-e1cd-3c72-bc06-908b784bd374 | -2.66112 | -51.74184 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc4844a9-b044-393c-b0bb-83edbc148d7c | -3.963 | -48.11811 | 2026-09-28 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc83b343-c138-3b83-9720-7519e8bdf078 | -3.27065 | -50.14071 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc2437c0-276a-3eb8-a41b-2542073c8fa2 | -3.27001 | -50.14471 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 067e8cc8-aa31-3986-b17b-d5c06f6c5aad | -3.20627 | -51.03642 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c17a6b36-af3b-35a7-b3e0-e10550a6fd8b | -3.07127 | -51.20471 | 2026-09-28 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e45228ff-8118-3a36-a7a6-56dba4fb3712 | -3.0176 | -54.20734 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6151cd2f-e063-3185-aeb1-7aba2b68a0de | 1.66605 | -55.92598 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9f065c6-d7c5-3bcf-8f49-e41c6f00d121 | -3.43395 | -50.66342 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88e97dcc-3209-3593-9566-8a03dcd4c86c | -3.14861 | -54.09319 | 2026-09-28 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b75dc9d-da1b-3a45-be13-e24148e057ec | -1.99395 | -47.63195 | 2026-09-28 04:32:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ed2f9ff-6aad-3837-bcb8-d06a6843dcf7 | -1.55853 | -47.04699 | 2026-09-28 04:32:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0bd3f43-4900-3879-bc6a-527464369b4f | -2.08035 | -49.54874 | 2026-09-28 04:32:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9aa455be-22d6-336e-859c-f993a1250c66 | -3.1008 | -50.32219 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c14f7579-90f0-3b2c-8791-dfc94968c2c2 | -3.42019 | -50.42762 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1d5a1004-6cbf-31a0-98e8-eafc6513ad80 | -3.15457 | -54.08495 | 2026-09-28 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f6014cf1-bdb0-3513-89e4-16dc7599a91d | 1.76475 | -50.8367 | 2026-09-28 04:32:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41448251-04eb-33d2-8b1c-b5dcd26b3925 | -2.32949 | -49.08411 | 2026-09-28 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2eff7667-3436-31af-8fce-dc7a3294fd2d | -1.9266 | -52.14393 | 2026-09-28 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 085310fd-ba4a-3f0f-aa67-649edeba99b0 | -5.01665 | -49.94588 | 2026-09-28 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f4d995b-5a8a-3d09-a0e3-be3cdbb7633d | -1.86227 | -47.97386 | 2026-09-28 04:32:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46afc509-c5c1-338d-9945-d73f48b598d9 | -5.64017 | -43.72312 | 2026-09-28 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 691cd347-a06e-39ce-818f-d2663093ba49 | 2.38703 | -51.01711 | 2026-09-28 04:32:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 355d3ccf-bea7-3e8b-86f1-962a6fdc4cdf | -3.82013 | -44.09543 | 2026-09-28 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 509e9749-bc6d-384f-bd0e-17a063e3f468 | -1.90674 | -52.08633 | 2026-09-28 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a72840b2-69da-3a62-b23c-4a77045b761b | -5.12973 | -45.75912 | 2026-09-28 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0008a44-e59e-30e7-baf8-3f0f638aef9d | -2.92449 | -54.20237 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 720f90ac-5beb-3ff1-83d7-0a4d15edd18e | -1.76063 | -55.12637 | 2026-09-28 04:32:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0e606db-5d63-39a1-8f34-59b5c34c6363 | -3.68348 | -47.49258 | 2026-09-28 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ba1b9c7c-fb71-3a83-a521-a44a2f474b05 | 1.65175 | -55.90581 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18e2789c-76f6-34e2-b982-bb011931642a | -3.15078 | -54.07961 | 2026-09-28 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c854cea0-c5b5-370b-aeab-479a3f0e36b7 | 1.67579 | -55.9505 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 138289a0-4083-3fa9-b048-afbb2cd4e5aa | -3.92546 | -48.37916 | 2026-09-28 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 531fa926-92cc-3c20-b72f-e385d222d521 | -3.0326 | -51.47055 | 2026-09-28 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58d020dc-1c55-3dfc-b645-5c7ff88bbbbf | -3.01741 | -54.21013 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9de6822a-60f9-32cc-9747-68e8f51e1f09 | 1.67522 | -55.94684 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a136000b-feb9-3ccc-8999-8b911965c723 | -1.04902 | -53.56747 | 2026-09-28 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6fc0f392-65c5-3cbf-98d7-7acde42a7043 | -5.73536 | -43.27933 | 2026-09-28 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e50a83d-44c1-36b1-a50b-f70b4c3c05e3 | -2.4484 | -49.22003 | 2026-09-28 04:32:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| da86b0ca-323b-3e80-9c41-33876dbf834e | -3.28992 | -50.3168 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bad3c457-ec9b-3276-88f0-b5054f0311af | -2.11768 | -56.88756 | 2026-09-28 04:32:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README27.md)
