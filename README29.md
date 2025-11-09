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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f14b908-dbe9-3a2b-a300-6a9f77717cb3 | -4.97261 | -47.81338 | 2025-11-09 04:38:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f780849-2186-3cd1-9977-66e21d8a83c9 | -2.6023 | -49.22707 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 674b7c00-0f34-3f1c-b57f-a40a49aa9c7d | -5.40253 | -47.2619 | 2025-11-09 04:38:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c38dd9d-078d-3623-9613-abd2988b30cb | -2.98381 | -48.70459 | 2025-11-09 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e2fa68b-4209-39be-8d69-f5d40020e16d | -4.17953 | -46.70087 | 2025-11-09 04:38:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c38974b5-0705-3ad3-8c14-0780ef1671f0 | -4.37462 | -49.73072 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0834353-9425-3749-afa3-16998ea3a47b | -3.3076 | -50.1627 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 114b8507-f597-30b8-bff7-fc0d23934f59 | -3.76508 | -44.2934 | 2025-11-09 04:38:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11235314-fd8c-3cb2-9f27-8bdead8f6aa8 | -3.30276 | -49.9974 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c1e4f49-7506-3261-add0-fbf1c35370cd | -5.94732 | -46.64991 | 2025-11-09 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c78a9be2-9f0f-3466-914c-9552d5377d9a | -4.22482 | -50.64295 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e080e1d0-869d-3a9f-af75-c33f8249a323 | -3.08363 | -52.92221 | 2025-11-09 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 308d2dd5-1862-3239-a21a-73d2a2727eea | -5.28075 | -44.95486 | 2025-11-09 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 38c28cab-8863-3644-a328-b721ca59b58a | -4.41442 | -49.02882 | 2025-11-09 04:38:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a267f15-4ff2-3255-9127-61b879279474 | -2.96464 | -41.58009 | 2025-11-09 04:38:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6741fc47-e699-3fe2-abd4-d0f132c08a0d | -3.8863 | -47.18343 | 2025-11-09 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c165d7cf-d4d7-3a94-8233-b4f35e4d90b6 | -2.28106 | -49.0661 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 384414b2-2474-3d00-9839-a3f50a6e1071 | -3.10076 | -50.32205 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e68780d0-7f8a-35ce-8966-6be6551b56e6 | -3.33039 | -44.3782 | 2025-11-09 04:38:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 35bd82de-4889-30c1-95ab-9b13e98f4964 | -5.48191 | -46.09181 | 2025-11-09 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1358dd2-0d05-3c6a-8a21-3f18dfd4e98e | -3.42554 | -52.89705 | 2025-11-09 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e552269d-9293-3c31-996a-8527893084b6 | -3.09737 | -49.25531 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3be10eea-15b4-317d-9118-f5f0c86248b3 | -6.32952 | -44.26601 | 2025-11-09 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57be6e1e-634e-3580-ba1f-ea356e7d81d0 | -2.65851 | -54.59987 | 2025-11-09 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09b31bb7-c16a-3ebc-ba86-836362e7ab2e | -3.65902 | -50.23215 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7351e372-fae5-3603-9711-510e6f3cec5d | -4.21 | -49.7622 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 547a2166-1bab-3450-a4a1-ae116168ffe1 | -3.15043 | -50.60381 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c55a25d1-f183-308c-ac20-9824a8864b7c | -4.48784 | -45.71594 | 2025-11-09 04:38:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2693a4c-386d-3858-8a3a-fc7fabaf4d7e | -3.45265 | -45.65629 | 2025-11-09 04:38:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e4399620-27b0-3065-ab50-2d28b4d1e9da | -2.60008 | -49.21963 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62e19126-ffcc-3971-b93f-c58c150ad75f | -3.335 | -44.37397 | 2025-11-09 04:38:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e5dba39a-dce0-3c63-8a2c-62ebb5c36ed7 | -3.57173 | -50.27032 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df4c35dd-ebcc-3ff9-b776-74b26b6b2bda | -3.0941 | -49.68302 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7f092d5-e6ef-3056-8a86-e392e582fd66 | -3.3473 | -50.20547 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09e7ddad-723f-3b97-b52f-624060eb8c14 | -3.33188 | -44.36861 | 2025-11-09 04:38:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0c549d14-d44d-37a1-bf7c-12e35c68c874 | -2.60616 | -49.22413 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3e4872da-937d-3316-9b6c-5026498cf5ec | -4.12237 | -47.29341 | 2025-11-09 04:38:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e1256394-63a7-38e8-be06-98d34ad1bb86 | -4.40457 | -45.95883 | 2025-11-09 04:38:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fff2a0a8-1853-3674-a7b6-c9ced78c51cf | -2.7438 | -45.16334 | 2025-11-09 04:38:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ef7e5a5-abd8-3525-bc31-7f5312360633 | -2.5169 | -49.44514 | 2025-11-09 04:38:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 949acc8a-72ca-307a-bb74-d7044a8de304 | -4.12662 | -49.79523 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70d2021a-e6f5-3b0f-a9c0-4278db87356a | -3.30665 | -50.01622 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7ad032e-1990-30e3-8db0-d759c5a3e711 | -3.25953 | -50.07449 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c2b08de-c53a-3629-b986-ceba2d385cc6 | -3.91036 | -50.0421 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 464f3df3-5d29-3bfc-a6ae-bafb27d52684 | -3.32709 | -53.24751 | 2025-11-09 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb2bca8c-e50e-3eb3-9f5f-63e777f306c5 | -4.45719 | -44.64676 | 2025-11-09 04:38:00 | NOAA-20 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 6712aacf-6820-3a37-99c2-45aad45c03f5 | -3.45177 | -48.82081 | 2025-11-09 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a00c94d-9d85-3eee-b01b-d6f5a9d86dda | -0.8128 | -47.15191 | 2025-11-09 04:38:00 | NOAA-20 | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 336b112e-36b5-34a7-b118-0cdb771f2301 | -4.85395 | -45.78993 | 2025-11-09 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0b5913e-d36c-3c8c-a669-cc742d7bd2f3 | -4.86526 | -45.98902 | 2025-11-09 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 894221db-156d-3a8a-bbae-ae017b333eba | -7.49699 | -46.60938 | 2025-11-09 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4449b0b6-434b-3b76-a43b-4c458f1805a2 | -2.10761 | -47.64626 | 2025-11-09 04:38:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cab2bf14-2f35-3acd-a6c1-668b866dce7e | -2.63351 | -49.5243 | 2025-11-09 04:38:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33105c85-8c77-3e0f-a29c-725abfb9befa | -5.22798 | -49.57819 | 2025-11-09 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a5e98ae8-3d43-3c47-b4a5-bfccd90902a5 | -2.97277 | -49.82595 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68b243a6-b00e-3fef-8ae1-d7fa400b0fee | -2.95083 | -53.28848 | 2025-11-09 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79e0bdbf-d024-3d78-89bc-1b2967df8496 | -2.6034 | -49.22015 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b04f5424-8a70-3746-944a-f6d808e96a94 | -3.48627 | -50.36428 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c28724b3-f69b-30f9-af74-65f1ea61a5f9 | -8.48874 | -40.52806 | 2025-11-09 04:38:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f95c279b-014b-3257-ab5c-515eab21fc50 | -3.32056 | -50.10242 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9824063a-699b-3685-974d-4dd7431fc80c | -3.80086 | -48.91124 | 2025-11-09 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae231278-2227-3bc6-8c54-f290b63812c9 | -5.39968 | -47.25759 | 2025-11-09 04:38:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab55fd9d-781e-3e1d-9fb4-96d1f9599fa9 | -3.35051 | -53.22601 | 2025-11-09 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2a5f04f7-6f7a-380c-8999-713efa2e4092 | -2.89148 | -53.13346 | 2025-11-09 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8bfd4fc0-3cf7-310d-ad15-20375b617247 | -3.87222 | -52.1399 | 2025-11-09 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb72804c-185b-3e21-8dea-9dd089744ac3 | -2.48042 | -48.23507 | 2025-11-09 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cdb0a28-46a9-365a-9f66-42a597300409 | -3.03642 | -50.3054 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c26dd65-ddd5-3731-a4e1-57c5e13cd36a | -3.94064 | -46.383 | 2025-11-09 04:38:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c82cebbc-1d25-3fa3-a29f-c3d65c17bc4a | -3.09512 | -49.22661 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d418fd8-55ac-393b-9dd9-92d4222a84c0 | -3.34457 | -50.17936 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40309af6-0ba3-3b59-9551-9c1d47427e1f | -3.0583 | -49.37336 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8efb3f22-7498-3ee6-bb56-25e1d915963a | -3.42632 | -52.89237 | 2025-11-09 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3790d513-4be7-309b-b3a2-776770051573 | -3.58932 | -41.66333 | 2025-11-09 04:38:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e192de07-442b-3d44-8707-93ef00063bcd | -3.84459 | -49.81498 | 2025-11-09 04:38:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0460effe-3b4f-338d-9a8b-ada4543a255a | -3.4057 | -50.45573 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9ac126be-8458-35f5-8ad9-b24d011a3b4b | -6.55034 | -43.21058 | 2025-11-09 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ff09e215-8fe4-3235-b7f8-d72ca043a6a4 | -5.20151 | -47.84054 | 2025-11-09 04:38:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91250e7f-c50b-3e36-b093-10ed91f7363e | -3.32811 | -49.12868 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a23e0fe-67f0-3367-aaf1-17d992d720a7 | -1.18142 | -47.61513 | 2025-11-09 04:38:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e677ecf7-1252-3ea0-9eec-595a341158e4 | -3.65945 | -50.27266 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31d006ea-3065-3a4e-bda9-0371674119ce | -3.09958 | -50.19967 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 9a76a57c-9f4e-3a04-9c43-2317f83db081 | -3.14582 | -50.61068 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60bf14cc-8720-3744-8405-c002fdc2d177 | -3.43355 | -50.28191 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21dbedc3-0ae4-3cd7-8d12-0de30a92936c | -4.18719 | -48.59504 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b5ddd78-84cb-3135-a9d5-510e1697153e | -3.42941 | -50.10109 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b33732fb-ab2f-3c63-9ccf-e2d3e5836559 | -5.37195 | -44.61971 | 2025-11-09 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd906945-7f54-36f2-a7af-37c350378bf5 | -6.26493 | -44.3612 | 2025-11-09 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4305167c-aa28-3110-898b-32490a5c7908 | -3.09406 | -49.25479 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83ce762e-ef3b-35a4-a368-70f611246395 | -3.25292 | -50.02959 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e4f399a8-c73a-389e-85e5-9a5947964abb | -3.46552 | -48.81944 | 2025-11-09 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cdb91a9b-df80-351d-9f48-bc5c6534e841 | -5.28147 | -44.95018 | 2025-11-09 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 787a2829-7cb9-398c-90ba-b3327bcafb37 | -3.83408 | -51.12816 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 807c788a-d352-31ac-a36e-93187863648b | -3.268 | -50.04295 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 91e14d4c-f875-34f4-9e3a-4e81dfdfc2d8 | -4.46105 | -44.64733 | 2025-11-09 04:38:00 | NOAA-20 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 2169d337-2d30-3bf2-981f-79a08806468d | -3.63742 | -51.94408 | 2025-11-09 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96cdf918-50b2-33e4-b33e-3dfbc0f6c48c | -3.1393 | -50.2762 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a4c4f786-d144-32b3-9168-d96e06d53691 | -7.09459 | -49.16253 | 2025-11-09 04:38:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d543db0-6d1f-34e7-90a7-ddb9ad3c0541 | -4.32884 | -49.76245 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 63ad012f-1030-393e-8866-0149f9a209c9 | -3.32757 | -49.13213 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eddb0ee1-2402-3b41-818e-a747c4680044 | -7.92011 | -43.30753 | 2025-11-09 04:38:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |


[Clique aqui para ver as próximas entradas](README30.md)
