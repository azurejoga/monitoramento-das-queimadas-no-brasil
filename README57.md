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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1500bf6-96df-3640-ac47-acd4fa986d6d | -2.16756 | -48.54382 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a1c60f9-5aa5-37a1-a486-125b4a920527 | -2.53133 | -47.30964 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c05227f-b87e-36d7-9d48-239da7650e2e | -2.089 | -50.80714 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 08e188b0-36dc-350b-a52f-c6a7b905d476 | -2.19441 | -48.84854 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb6c4ce6-2c9e-33d3-b29c-00f0c681b30b | -2.33126 | -48.51643 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 347d88ad-ed86-3839-8b2c-086493ba0c85 | -1.17425 | -53.6944 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9eaa41d7-847e-35c5-89c3-1f99e6607d1d | -1.28293 | -53.71712 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2402cfc2-3df0-37f8-9980-47832dff1b5b | -2.22894 | -48.36991 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c60af7d1-639b-3480-a6cc-22283202ce78 | -2.18243 | -48.3415 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e86bc55-4f73-397d-b981-92098be6f255 | -2.20234 | -47.74323 | 2024-11-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f524907-a4e2-315a-877a-bf0b65dd1a59 | -2.38925 | -46.77047 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f8c78ef-a1a4-3419-abcf-8a500ed5cc6d | -2.56797 | -47.34819 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dc4342e-06d2-3e01-891e-e6f0478466d2 | -1.32421 | -52.23889 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2448cd2-c527-3e63-ad72-2212bfdf53fd | 1.11493 | -50.8864 | 2024-11-10 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3aaf641a-d23b-3aa4-9b85-88f1890716fe | -2.3792 | -47.93033 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de330589-e796-3a15-a49a-cae6eb0e1056 | -2.14145 | -50.14001 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9de1cd2-c66e-30f5-8aad-26b53198c00e | -1.24497 | -51.76218 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 081d12e1-e63e-3093-af3f-a10c6e40a1b2 | -2.68336 | -46.80752 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e130b821-dd89-3ee5-aab5-d10ea9ccdf19 | -1.23454 | -51.75604 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ac8edf17-7c06-358a-aec4-7d50cdee65d6 | -2.19522 | -48.36819 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e5c526c4-7e6d-332b-a716-5f75c7b7c7e7 | -2.21519 | -48.39247 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 249acfb2-f466-372d-bfbd-e42057739a5c | -2.30873 | -46.08647 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf5c4c5c-dad5-30de-b65e-622fe8375c57 | -1.37413 | -52.25922 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 564a5cb4-09f4-37af-a508-980a477ca46c | -2.24784 | -48.22818 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e02494d-2f5d-36ce-ab51-d1cf9bd8b39a | -1.59395 | -47.56705 | 2024-11-10 04:36:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f92e7689-8801-3928-9d3f-6c3a4770c761 | -2.78882 | -45.96679 | 2024-11-10 04:36:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7e5ead3-1da6-3454-8e5f-a33b2ed32a2e | -2.37622 | -46.74234 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7a5ae7e-01af-3ec5-93d9-d611f140bd53 | -1.24218 | -51.77971 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5357082-ebc9-3715-bdb9-72cb0b2fc75a | -1.34478 | -54.62886 | 2024-11-10 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cc07dc2c-43ab-3ccc-83a8-456c86772e97 | -1.14607 | -53.65593 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dca5e7af-ba1a-3ba2-b5fa-3e607ce0add7 | -0.11 | -51.76091 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a245c01-d8ba-3d75-b07a-1fa238f11da1 | -0.91131 | -51.65322 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 671e4051-a2fc-30d7-a0f5-34a8b5d191e6 | -2.2184 | -46.43555 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf9bfd48-65db-32f9-9e20-81d37edbb76b | -2.18751 | -48.37405 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71527fee-f0db-3075-bed9-5a9d640119bf | -2.13885 | -46.69836 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ecb14e0-7f9d-3e2b-8cfe-e4a3e48db1f9 | -0.95565 | -52.44572 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08d2d938-cda0-3649-8f8d-345254c33a34 | -2.35406 | -46.66031 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08df6710-d55b-3b77-a81f-4b30f8b3a57c | -2.30969 | -48.32962 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91cb371f-1a14-3dc2-bd14-521be6b8a87f | -2.19667 | -49.85824 | 2024-11-10 04:36:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28e11edb-8d35-3ab4-bc76-c51e0314cb35 | -1.15468 | -53.7907 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 37bdbdd0-aaaf-3077-a22c-b1ecb2e9f61f | -2.79295 | -45.96339 | 2024-11-10 04:36:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf644dfe-4ec5-36fb-89e1-07ec999bff60 | -2.47068 | -48.44683 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d32bdd4-6fd5-3b7c-9b97-6f9787675e77 | -2.30268 | -46.74253 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0c475c8-8f56-3978-a0ea-764185a9d7ff | -2.18859 | -48.36716 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa7be9bc-b43c-3ada-b2e1-b65d149709c7 | -1.17573 | -52.09972 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8d19b84c-bc10-3932-bfce-f883ce85be80 | -2.21961 | -46.40527 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89098485-acab-3268-b623-fced0944623f | -2.29853 | -49.10687 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6396a0c1-cad2-325e-a1fe-904c2730fc8a | -2.19372 | -49.12937 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20977608-040f-38f5-b497-76b114cbcad2 | -2.1825 | -48.36269 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d81084a5-3bd0-3551-9758-4c737a8cb3a3 | -1.19794 | -53.70761 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c365206-5742-343b-8c1c-0f10c8547b9c | -2.00192 | -46.81497 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8cc896a-158e-3a6a-9f2b-9df5792fb9cf | -2.12076 | -48.56488 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3840d1b5-2210-3738-a362-e54e93bcf355 | -1.15949 | -54.07938 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d6e8c98-ba88-32f3-ae02-ec5f78720a7f | -2.22898 | -46.5471 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73df5e92-0f2d-309d-9a4c-e723a673b5f3 | -2.30272 | -46.72013 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b462d64-3374-36af-9495-fbfa7fc13733 | -2.10102 | -48.96532 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa81da64-a3f7-35a2-a339-850f9bcc6320 | -1.28673 | -52.20451 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f78d923b-d299-3eb5-8477-9067a0e759aa | -2.34882 | -46.51648 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6514c5d2-b54d-3c85-b51f-da5c4b310ef9 | -2.51193 | -46.31468 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f393a0d-cca2-3c57-9d45-57ff8d67cc80 | -2.36425 | -46.86332 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c51643fd-a99f-3c47-944a-eb576de1d4ac | -2.15588 | -46.70097 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 617fd552-3ae3-356a-a840-8a2ebe058b1e | -2.24419 | -46.55711 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74bdb0b8-e194-3992-99ac-49a5ccaa7369 | -2.64532 | -46.80534 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20ef4e25-de50-33db-bad6-99dc0e317bba | -1.34019 | -51.42138 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5af07ed-eda9-3807-9476-2b57694f958b | -2.20271 | -48.85699 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e0f49d6-0431-392e-a59c-7026715a5933 | -1.72977 | -52.33223 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 140ae883-2bc9-35b9-aba2-1ee3a24bbd23 | 3.36954 | -51.26981 | 2024-11-10 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6eeca763-8ce8-3803-8b4f-4e009fa1e581 | -1.43438 | -54.54171 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54731f66-aee1-3cc9-8df8-25b105e2fbf8 | -1.34035 | -54.62804 | 2024-11-10 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a91b2d79-9de3-3d40-8937-0d38b0bc68b7 | -2.68053 | -46.78087 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c9f897a-52ab-3d34-bad4-0fe1c1488f9b | -1.17951 | -52.10032 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7198b7db-4e2b-3453-9294-0e6d428cd6a5 | -1.40624 | -48.13532 | 2024-11-10 04:36:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c52e743-d060-33c4-926f-d82afc37a6ae | -2.51539 | -46.31522 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdbdc4cc-bfdf-3be4-9413-64fd4baf9c9c | -2.09907 | -46.55019 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27c6430a-d177-301b-a9c5-fdc954eb0121 | -2.68279 | -46.81119 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90bdcbc8-5212-3ee7-89c7-58b18fa4e647 | -2.16751 | -48.31108 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8100cf12-dfe1-3860-978a-76ecb1ee33d1 | -2.29229 | -48.80718 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bdda3ef-fa03-35bd-967e-8afec8dae5f4 | -1.13225 | -54.19197 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fd062e16-a06e-35ae-8500-2c8b67126213 | -2.39897 | -48.49213 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e0f3930-177f-3327-9607-c1c6df612f65 | -2.57069 | -46.18779 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2aabd2aa-fdd0-3910-9b20-2da5edf9d7d5 | -2.18954 | -48.31792 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4f84a66-c05d-3150-b667-3c31afa9cf37 | -1.03679 | -47.79535 | 2024-11-10 04:36:00 | NPP-375D | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| da8efd92-813f-32c2-a087-7e48d1c93c63 | -2.09664 | -48.82636 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d8368e3f-d4e1-3b64-931b-359ba9da3ecf | -2.28785 | -47.93029 | 2024-11-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1babc57-3fec-3584-9bec-f17958811ecb | -2.15899 | -48.85719 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2365faf-04cb-3703-8fed-fc62393a0b6a | -1.8327 | -52.0711 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ee98f85-6d78-3e09-81a3-d1ed10d754d2 | -2.21458 | -48.74193 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a923a54-6a28-31a3-aeaf-6af9094461ca | -0.41005 | -51.47584 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49e793b0-bbb3-39af-9b04-cc4d407dad7f | -1.04868 | -47.89252 | 2024-11-10 04:36:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0871fd6c-f803-374f-98dc-905580444c2f | -2.14708 | -50.46046 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 186af2fd-853e-3a55-b183-3fa411452b3a | -2.12178 | -46.38308 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92c4f496-df03-31bd-b33f-8fdbbdcb9133 | -2.22826 | -48.33099 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 958e8a7a-1f73-35a1-8550-89c9bfce18e7 | 1.62029 | -56.04861 | 2024-11-10 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c75b1925-a6be-309e-a440-c3709df07ddd | -1.69993 | -48.16362 | 2024-11-10 04:36:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69fb43d5-0cc6-3d92-a51e-1921372169fd | -1.376 | -50.57316 | 2024-11-10 04:36:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20832063-4b82-3575-9882-c212cb242d8c | -2.29565 | -46.49692 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6208bc4c-0d87-3acd-8a30-0ccfaa9c5a26 | -2.36652 | -46.87104 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d31f87ff-6c70-3fed-8ea5-37992a374c26 | -2.02668 | -48.40893 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b6ca7d5-95a2-3784-a133-07c1f8122aaa | -2.1736 | -48.31555 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86e6c8c6-86ea-36e7-a628-2bc5b542ff29 | -2.20958 | -48.36337 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README58.md)
