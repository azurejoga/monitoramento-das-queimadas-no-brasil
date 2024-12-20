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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40eea435-0a2b-31b6-8d58-e35a97a14349 | -3.23558 | -45.49968 | 2024-12-20 04:10:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3c007e0-d94f-3550-92ec-1156540a135d | -5.11711 | -43.19936 | 2024-12-20 04:10:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 37eaa2e0-2cf6-380e-982e-e0f33c3be829 | -4.86052 | -41.35022 | 2024-12-20 04:10:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f5be82ac-f413-3b63-b7be-c6dedf0a7f6f | -3.23463 | -46.79903 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 6dcb7d89-a31e-308c-94b7-037b414abc41 | -2.64796 | -47.18348 | 2024-12-20 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5897ef34-2abf-36de-9595-e29d2533a775 | -3.23073 | -46.79839 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 74f72895-829c-32d0-bcff-b0a393dc6abb | -2.70436 | -46.13918 | 2024-12-20 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 778c16e1-9c8b-3f44-90aa-10576b9c5135 | -4.67303 | -44.41097 | 2024-12-20 04:10:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d8d3ebb9-b53d-35a4-9674-ab9c9da1689c | -4.1141 | -46.70052 | 2024-12-20 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f39a0aff-3701-367b-9a0a-61d43c17bf3f | -3.67061 | -39.57792 | 2024-12-20 04:10:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5d899591-2008-304d-a8d2-0c0ae79cf7ce | -3.71274 | -41.69788 | 2024-12-20 04:10:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| be29cf4b-de2f-371b-8a3b-75458b28e2a9 | -2.38926 | -47.08396 | 2024-12-20 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b595ac3-6bbe-3ced-aaf6-642d893faf9f | -3.69969 | -42.12827 | 2024-12-20 04:10:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d6af5eb7-efd0-371b-8280-117858e57e6b | -4.4071 | -43.86042 | 2024-12-20 04:10:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79928989-797b-3e17-ad25-11ed849d2942 | -3.96511 | -44.05689 | 2024-12-20 04:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f88a4174-0c76-3569-8ba1-95270aa2773a | -2.58517 | -51.9241 | 2024-12-20 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ded49a7-a0f9-3a82-aa60-ab73499af4c2 | -2.55938 | -46.92966 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50f76033-c237-396c-8e19-df8d4274f565 | -1.61694 | -45.83846 | 2024-12-20 04:10:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ad13922-a55b-3d03-afd4-6dd722f262d8 | -2.50905 | -48.06327 | 2024-12-20 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a68c330c-3a2f-3939-ad45-be9228f7e3a8 | -3.30767 | -39.28218 | 2024-12-20 04:10:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2fc8df8b-151f-3870-9177-d25f55abb7da | -2.3259 | -46.27674 | 2024-12-20 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b96a8ca-c41f-3d91-a2e5-0f5bf9ef9ba4 | -3.67416 | -39.57846 | 2024-12-20 04:10:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 082f1d1b-97d7-3b70-bfe8-212281ae7a04 | -3.00375 | -46.71165 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c464c025-0703-3e16-8dc7-f89d3f1efd07 | -4.67645 | -44.4115 | 2024-12-20 04:10:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94945d66-766d-3b9f-88dd-9b7838216f2d | -5.22702 | -36.81459 | 2024-12-20 04:10:00 | NOAA-20 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9e258b8f-f3ca-3149-99ca-2075201a178e | -2.70218 | -46.15297 | 2024-12-20 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 847cce8a-5cc2-3b02-8a69-b5a2c6b2f15a | -2.46217 | -45.3263 | 2024-12-20 04:10:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75cd99a2-4957-310f-aee2-22923275f6e3 | -2.75827 | -45.55931 | 2024-12-20 04:10:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9a464ab-c6b9-36d5-9933-d18ab9d8cc64 | -2.9025 | -54.50111 | 2024-12-20 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 73089937-b6de-3836-9da0-54938bed3853 | -1.01279 | -48.0703 | 2024-12-20 04:10:00 | NOAA-20 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ca442c4-8367-304c-bd11-1c01a9894802 | -3.20822 | -45.50813 | 2024-12-20 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c20f0f59-4860-3f2d-8628-3aae8609e8ac | -2.76863 | -47.3931 | 2024-12-20 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 923f7b74-1263-3216-a884-f8da32604f12 | -4.92917 | -41.34232 | 2024-12-20 04:10:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3b68fc8c-149a-3f3c-a4de-86e73eb4db39 | -4.01545 | -42.88382 | 2024-12-20 04:10:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b060ce47-745d-306f-b673-da72dc4556d3 | -3.22917 | -46.80817 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b6e44ebd-00e5-3339-8ed2-1977b4f5e0af | -3.71606 | -41.69839 | 2024-12-20 04:10:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| eea385e8-e708-3100-857d-df035f5aa43d | -3.2323 | -46.78859 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 770807dc-5085-35e6-b034-e3ad00693ce3 | -4.11333 | -46.7053 | 2024-12-20 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2c7e499-742a-3b32-a168-9ed72e949193 | -3.00064 | -46.70612 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd6b7888-4a63-39a3-a3a4-33bc7d7e8164 | -2.70669 | -46.14899 | 2024-12-20 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5ed60a7-9b90-3c25-aedd-24fe7c3cff59 | -2.45683 | -51.843 | 2024-12-20 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fae26844-11af-3f32-9f3f-eacae3448fb1 | -2.62648 | -48.05075 | 2024-12-20 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c71452c3-f4bf-3b63-b419-92f77535c0cf | -5.11379 | -43.19884 | 2024-12-20 04:10:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 592db56f-cead-3394-9005-af3c39ed2867 | -3.23541 | -46.79414 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2442985e-07fa-3471-8477-4ddea725e76c | -1.33216 | -46.64838 | 2024-12-20 04:10:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2ce745c0-0f1a-30db-b1e8-736f4ff45074 | -3.20755 | -45.51233 | 2024-12-20 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 299dc74e-838e-3414-aa56-1761c933bcb8 | -1.78149 | -45.67802 | 2024-12-20 04:10:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70117481-b5aa-34f0-aede-17b78e0856c7 | -2.76454 | -47.39243 | 2024-12-20 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a185042-9432-3258-91c8-86b2ec8ce642 | -5.98403 | -41.60988 | 2024-12-20 04:10:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 942c7d98-554d-3631-8e3c-51caf80b093f | -4.33987 | -39.23493 | 2024-12-20 04:10:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b0752de1-913d-39d3-93cb-4953bdd46299 | -2.37417 | -45.01412 | 2024-12-20 04:10:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e034705a-7eb9-3c07-a7ee-6f17624a4b06 | -4.15125 | -43.72219 | 2024-12-20 04:10:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8b19946-80c3-3eb9-bf22-88074a05e7e9 | -4.01214 | -42.88329 | 2024-12-20 04:10:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 176b0405-c4a9-3473-a832-aba2c736030a | -1.3303 | -46.64903 | 2024-12-20 04:10:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67e844b5-7236-339d-acf3-d0f03cfbdef1 | -2.46797 | -47.08959 | 2024-12-20 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f68cd187-cc19-3b42-accb-d60191c301b1 | -2.46299 | -51.84029 | 2024-12-20 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9850a33d-cd33-36d9-9014-c47ebb2ca666 | -4.09646 | -46.63966 | 2024-12-20 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11230dee-a78b-324d-9751-b56bf09cafed | -3.23262 | -45.49492 | 2024-12-20 04:10:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ffa3c49b-947d-38f6-8621-c21898d2bbf6 | -3.95593 | -41.48929 | 2024-12-20 04:10:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f41505a6-c281-30c0-8d04-4b12160a2715 | -4.26189 | -43.45021 | 2024-12-20 04:10:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 491f9b7b-f536-3a04-bf0f-b8a95d863bb3 | -4.38935 | -42.14796 | 2024-12-20 04:10:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 24a48618-eb83-3beb-b43a-d57b0a73ab8c | -4.9258 | -41.34185 | 2024-12-20 04:10:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6f58a2b8-4d25-3f81-9c0c-f860a718768c | -2.79141 | -43.3423 | 2024-12-20 04:10:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2008ebe4-3822-3fa7-92c6-a54d337c16cc | -2.76395 | -47.39606 | 2024-12-20 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80b8c01e-f4da-3d34-88f3-63be3b3449c9 | -4.05174 | -44.26143 | 2024-12-20 04:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83cb65fe-6f78-3ac5-a829-ee6cb606fecf | -2.87619 | -45.24656 | 2024-12-20 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc3b80a8-adb0-3612-8893-c173abff3d3a | -3.18272 | -50.57011 | 2024-12-20 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28716760-a8b9-353a-962f-7aa10774ad11 | -2.50969 | -48.05922 | 2024-12-20 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c64c0316-deb4-36b7-8ffa-69e96a287550 | -3.23932 | -46.79477 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 899c0c30-40cf-3f9a-9acb-20a2b8720417 | -5.24755 | -41.25551 | 2024-12-20 04:10:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bbb5ff77-a21a-3e1b-8453-5d81b724795d | -3.99559 | -46.5438 | 2024-12-20 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f947268c-f294-3c9c-9e28-d7f7e0443a36 | -2.65256 | -47.18059 | 2024-12-20 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb77c902-520e-3e70-b866-f833c3b779e5 | -2.8726 | -45.246 | 2024-12-20 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1cbb3731-e218-38f1-876f-d0bbae91bddf | -5.25508 | -41.38537 | 2024-12-20 04:10:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2530e332-4ec8-3ac3-ae2d-a931a7b0d8a0 | -4.38064 | -46.27359 | 2024-12-20 04:10:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fff015c-6259-3e2a-ba85-5bed9911edb2 | -2.67438 | -46.91302 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c608e656-5a09-3d53-865d-e1ce782bd1de | -2.63077 | -48.05141 | 2024-12-20 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed32574a-a1c9-396c-8faa-269c4388d9d7 | -3.99865 | -46.54895 | 2024-12-20 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d10ab7a-4687-3ffd-9c47-b6afb80fc57d | -4.37691 | -46.27298 | 2024-12-20 04:10:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c28520d-e95b-38a9-a3d4-a8584583cea0 | -3.23776 | -46.80454 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54c77321-e257-3bdd-bf94-df0d5250ce95 | -4.42504 | -42.8918 | 2024-12-20 04:10:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d5a6698-42c0-30df-855b-2bcd343b0de1 | -2.50752 | -48.06233 | 2024-12-20 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff25884d-f7fc-3659-a635-3d346217cd10 | -6.00205 | -41.67099 | 2024-12-20 04:10:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0bf0c869-7645-30b3-b10b-1281c878bb26 | -5.25453 | -41.38894 | 2024-12-20 04:10:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6a148160-b5ca-307d-91b9-d884a347fd59 | -5.32398 | -43.73656 | 2024-12-20 04:10:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| de60c7f5-da66-3403-8ee8-9aa5d7f2a850 | -2.76804 | -47.39672 | 2024-12-20 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6e81821-f74e-3dbb-8857-b3fde796ee28 | -5.32844 | -43.73005 | 2024-12-20 04:10:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddb41860-0083-31fc-b29c-8b9b9732c297 | -2.69229 | -46.14197 | 2024-12-20 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d4026a9-acbe-3f2f-9f4e-e03b47783e32 | -4.67658 | -43.30071 | 2024-12-20 04:10:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97fddbb3-2653-3c6c-9b8a-4c140b44507a | -2.70363 | -46.14378 | 2024-12-20 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8996106f-eaf5-3561-995a-947202f7bbfd | -3.23307 | -46.8088 | 2024-12-20 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 37cb2e29-8335-310c-8f08-a2879750c09b | -4.9881 | -41.98922 | 2024-12-20 04:10:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 56f58698-9d68-3b78-b6e9-a41007f8d76a | -2.42841 | -45.67995 | 2024-12-20 04:10:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a87e6604-d72d-3dc0-97d5-939e5c55974a | -4.12296 | -43.55453 | 2024-12-20 04:10:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e854b13b-f2a6-3610-8376-864f8556d870 | -1.52892 | -46.05365 | 2024-12-20 04:10:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 147648db-0627-30d2-a670-c2a39870774b | -4.06775 | -46.40931 | 2024-12-20 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4347e917-6cdb-361a-904d-e3a33a209c09 | -5.09074 | -44.71543 | 2024-12-20 04:10:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59134b13-21ef-310b-92eb-47fe0ff64307 | -3.16438 | -45.97369 | 2024-12-20 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b65abfc5-bd21-3039-ad50-a3d7a3f49260 | -2.57958 | -51.92325 | 2024-12-20 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3dd8dfe8-90b5-3e1a-93f7-5cf5f2b985d9 | -4.92521 | -41.32344 | 2024-12-20 04:10:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README8.md)
