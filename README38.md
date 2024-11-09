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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ba23fc1-f173-310b-89c1-54163993ab08 | -1.14812 | -53.65039 | 2024-11-09 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 906cb7c3-b90d-3630-af88-9fca222a0313 | -1.48061 | -52.0867 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1413072-62b3-32c0-bd4a-a554cb34bb55 | -2.22616 | -46.54581 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d40e937d-698d-397e-87e0-cf0b74d19b21 | -3.11612 | -45.95818 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd9f823e-3e38-3387-a58a-d775bba6b80b | 2.10264 | -50.85886 | 2024-11-09 04:31:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 351e7381-f26f-355d-b2dd-8683e9b0220e | 0.84826 | -50.17783 | 2024-11-09 04:31:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd86cf71-a64b-3a5f-8ded-bf0b3ae88a7d | -2.85346 | -48.45053 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df109964-d5e0-37a9-846c-21839f08fb93 | -2.04901 | -52.08408 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5c6a64a8-ce4b-32ac-bfec-f736153890e9 | -2.15185 | -46.67529 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40aaed32-6964-3f58-a948-9915715c5df2 | -2.39871 | -46.77033 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| add9a2d4-a936-3737-80a1-e2acda48bcbc | -2.1998 | -46.69323 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ae19993-e407-38bb-9a7e-c06b7f7a7412 | -3.54133 | -43.5651 | 2024-11-09 04:31:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3a97cc0a-6b6d-31b4-a33c-22676ca27309 | -2.37549 | -46.74566 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3a7da22-5197-3975-83bc-eb8b57a70c81 | -2.4081 | -48.49078 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d89ab9cd-e5e7-39fa-961f-b92db92828ac | -2.81967 | -46.64552 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4674f9a1-a481-340f-897d-d9369b27197a | -2.46683 | -46.8793 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40558bd2-6dc2-3e4a-8d44-1f1e38458c02 | 3.74377 | -51.60527 | 2024-11-09 04:31:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2e96b9ad-f691-3207-a19d-7602db11146c | -2.84284 | -46.64908 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfc76d0d-dc86-3b7b-816a-0f776e257db4 | -2.27787 | -46.71656 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0ccb153-80e7-354d-8cf4-fc8303b4a0cd | -2.26884 | -46.46764 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa68290c-fe69-35fc-b1f2-6a9d4de9bd1a | -2.13092 | -46.78812 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8289f49b-89f3-34a5-9298-a5fc0923e7df | -3.12954 | -45.96025 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b30a7ba2-7488-3661-9754-a2eec7eae3bb | -1.51736 | -52.22281 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c13565f-eede-38fd-a3a0-a1021bcdb521 | -2.8339 | -48.46565 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95e4164d-db72-3df5-abed-43605e6bf74f | -2.53867 | -46.30757 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdede1ef-6dc8-387a-be05-25308200b929 | -1.34035 | -51.41476 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60091071-3239-3f0c-8d4d-dfd19fbf3c94 | -2.51743 | -46.37893 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1193110-5bca-3ced-8376-e3f5c0bc2d74 | -2.4486 | -46.31869 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 49c3ea6f-249a-3b59-906b-ee6cc3df8271 | -2.06603 | -53.28198 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f99a255c-46ad-3ae9-8ece-17d08701a1b6 | -2.151 | -49.13879 | 2024-11-09 04:31:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 470563ec-edc2-3c6a-b09e-e7011da52240 | -2.62729 | -46.15342 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86919ec7-d650-3231-abb0-92f37a664b37 | 1.32288 | -50.72539 | 2024-11-09 04:31:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 130cdbab-9f76-39eb-a75e-f1d9778b74ec | -2.22348 | -46.43237 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 566526e1-c9c7-3c00-a78c-8760c245c1f2 | -2.86758 | -47.90756 | 2024-11-09 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e6f07fa-05cc-3e4c-930f-5468c3ad3445 | -2.9489 | -46.75371 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a05dbb5f-a376-37fd-bc18-33cbbdda73c1 | -2.20404 | -48.38216 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7d89240b-3bdc-3d58-b11b-c539a81b149b | -2.62937 | -46.77421 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a92a2b8b-3f20-3e2d-a8d4-ec6af0bcb1b1 | -3.2974 | -43.54097 | 2024-11-09 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 044affac-80c7-345d-a448-82d5ccb27b46 | -1.05863 | -51.74691 | 2024-11-09 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92bcb6dc-7978-3745-8597-de50cb6236ea | -2.399 | -50.30878 | 2024-11-09 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b6ed0b6-decf-37a6-91c1-ba9c0e9747d3 | -2.0928 | -46.5288 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a639b68-4ebd-3f47-8231-e93c7c734ced | -2.62341 | -46.1564 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e814a703-9427-37a3-9011-63fb5e69ae9f | -1.56221 | -51.66177 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37ce51cc-4e88-33a7-89ec-49061b6581c0 | -2.57198 | -48.18624 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9482553b-f4f6-3733-bf39-2887e7423be2 | -2.13693 | -46.66244 | 2024-11-09 04:31:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6265baf2-39da-3ae7-a1fc-7795198c4411 | -2.21516 | -46.68151 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4795ab48-afbe-3dbc-b7c7-fba8cbc30c9b | -2.65652 | -46.07538 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61004d98-2c50-367a-b710-7c7bfa30ecfc | -2.45192 | -46.3192 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d676287-5e3e-3ab1-a0bf-940bc55fb1ac | -2.03406 | -48.56147 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 163297ea-81c3-38d7-a225-cc7445e09744 | -2.2929 | -48.55301 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a9295e3e-d6c9-3211-b527-07b17f23a22f | -2.21576 | -50.45013 | 2024-11-09 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfd96d60-f2ac-33a2-902a-f3d45aab58bc | -2.26367 | -48.98062 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 373909dd-786f-3ede-86f4-cafe751ac42f | -2.39572 | -46.59373 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7c730d9-ad78-340c-80ce-41477cf0c4c3 | -1.39 | -54.64793 | 2024-11-09 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57a01f80-528f-396c-87e0-daabfb12195a | 1.32362 | -50.73028 | 2024-11-09 04:31:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f4be611-e125-3b3d-907f-61c6203a229b | -3.14959 | -45.94152 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5947bca9-801d-358e-96bf-a6e342a72f36 | -2.31706 | -46.48638 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db30cdd0-e137-3dbf-931e-e43fcc52b796 | -2.02376 | -48.01786 | 2024-11-09 04:31:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91df2252-0b24-38e5-95d9-a6445ae21bb7 | -2.18114 | -48.33868 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41388bdb-34f2-391f-a28a-91b31851d852 | -2.45216 | -47.16849 | 2024-11-09 04:31:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b112a58e-37db-353f-a350-9136b9bf2f51 | -1.88001 | -50.96792 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 964635a6-417a-31af-84d6-67f3e55f025f | -2.51767 | -46.31145 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0aa3f9c5-0151-375b-a4be-1c9b4840d1cc | -2.26923 | -50.68399 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce673291-df81-3361-bf1b-465b3e5b733d | -2.67841 | -48.50669 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c717d49-63f0-3cec-bd86-d80ebd340517 | -2.83333 | -48.4692 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ddb4c676-805a-31fe-8335-a4e7d728798a | -2.04606 | -46.54631 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 772d2d68-bb8e-3ca1-aed9-3cecbd2e5d06 | -2.19927 | -46.69666 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c880c830-e5e9-3347-9478-97d0fd904e45 | -2.33561 | -48.86047 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 328e51d8-fc8d-3778-bc94-418ad05d1e9f | -1.62999 | -55.11187 | 2024-11-09 04:31:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a491512-d092-3cee-9909-b8bf4a844180 | -1.41426 | -54.76394 | 2024-11-09 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 00b08196-da40-3c52-916b-510c127afa5a | -1.14277 | -53.65455 | 2024-11-09 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 26018741-4285-32bb-8dfd-d531332c496f | -2.80463 | -46.61137 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e58d5fbf-368e-37a8-9606-c2567545ecfb | -3.13063 | -45.95315 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49a15224-243c-39d9-9615-d183d13c5ec1 | -2.29672 | -46.7476 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23c15493-b015-34ab-bcde-3a989c8ac385 | -2.51369 | -48.32159 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b593f12-2d3a-316e-b8b2-ccaa6aefc7d1 | -2.70158 | -48.65722 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1f3def6-c225-3fdf-ba54-5c438e3e5f05 | -2.20613 | -50.3417 | 2024-11-09 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6ffb110-bb79-35fa-aa05-b2b6e08ee61b | -1.15304 | -51.99447 | 2024-11-09 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 691e0fff-5c8d-34f4-95a9-86bd29c21647 | -0.38953 | -51.94183 | 2024-11-09 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 34e362f6-b4d6-35b8-9b06-b69a5baf06e2 | -2.13489 | -46.69732 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1439ece2-ac86-3a04-a4d6-edd2a942db26 | -0.30304 | -51.72217 | 2024-11-09 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5131a784-0b0b-3038-8258-2d5a229f4ab6 | -2.37604 | -48.57318 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe563be3-30ed-33c6-b3a1-838003c8e862 | -2.82769 | -48.46833 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17d478a6-5364-3c91-8738-0ae6640be0e2 | -2.67547 | -46.78556 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a80bdcc-2e96-3483-8e9e-c645d28a0973 | -2.57253 | -48.18274 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6b35298-dd58-3ac6-9979-4bda7fe8414e | -2.40275 | -48.42365 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5da539d-02ca-3179-8ee0-6e389091353d | -2.3043 | -46.72063 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1aaf3cec-dd32-3177-b4a4-0a07bdfadca3 | -1.51803 | -51.31243 | 2024-11-09 04:31:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18ab7091-cd86-3f9d-81f2-7e4c811cca32 | -1.19443 | -52.15377 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc8dc8bf-b8c8-39c5-8a00-1bc280e91ffa | 0.79151 | -52.00864 | 2024-11-09 04:31:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 63feacaa-7de8-340d-b711-843f5bb98417 | -1.3427 | -51.42524 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5cd2793f-1350-3f27-a40d-ade4456a68de | -2.79183 | -45.96662 | 2024-11-09 04:31:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8055cc7-6844-3edf-bd3f-debada0c2677 | 2.10523 | -50.85638 | 2024-11-09 04:31:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 648522eb-3419-3054-9e8a-77c801def077 | -2.22437 | -50.63231 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4317d82f-fc85-3157-a30b-e2bfd69a337a | -2.08409 | -52.04612 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f687aad8-a737-3470-b8bf-8a95d6adeb76 | -2.1622 | -48.39401 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcbe07a7-8ee6-3268-bf99-a1b3b2ee6c88 | -2.24982 | -48.22242 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3d24724-772f-3990-b6db-a08f953b91ee | -2.81708 | -48.47033 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 651c8af0-ca43-35c8-92f6-39a240cd5d66 | -2.27367 | -51.12984 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cb26478-7338-3867-980c-3f9396a0e504 | -1.38772 | -51.57256 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README39.md)
