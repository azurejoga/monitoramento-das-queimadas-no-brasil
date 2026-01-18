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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2755203e-702f-3261-85ee-65f342ec32e8 | 1.1393 | -60.5222 | 2026-01-18 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.6 |
| d8ef026b-b619-38f0-8950-d8a81976160c | -18.8139 | -51.60553 | 2026-01-18 00:26:00 | TERRA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f54fe091-e6cd-3bd4-ad76-74a4a50ddb48 | -21.43241 | -48.63758 | 2026-01-18 00:26:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 31a1310f-cc1b-3676-b347-1b1b95e89cd4 | -18.65016 | -49.09362 | 2026-01-18 00:26:00 | TERRA_M-M | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 8d141d5f-bafc-3dd2-9676-08065980c9d4 | -18.65905 | -49.09224 | 2026-01-18 00:26:00 | TERRA_M-M | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2f0270f3-e18c-3cfe-a035-8d1e887be342 | -21.43369 | -48.64729 | 2026-01-18 00:26:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0d4392ac-5589-33a9-bd2b-d028b11ec3fe | -12.65948 | -46.762 | 2026-01-18 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6b5c8fb6-8e6c-31ab-bdd8-25f1b760b244 | -12.3527 | -51.21658 | 2026-01-18 00:28:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 01903fdd-bbfb-3abe-81a0-d62919390ddd | -12.70868 | -46.80326 | 2026-01-18 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f765cf39-44a5-38b8-8589-ff27111936a0 | -12.09709 | -51.2312 | 2026-01-18 00:28:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0c1d9113-799d-3959-9c96-f83c14df940f | -13.74079 | -43.66174 | 2026-01-18 00:28:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 753dbe18-ab26-370a-ace8-7646dfbd9a8d | -12.27253 | -49.34262 | 2026-01-18 00:28:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 607e4af2-14c6-33a6-b718-a5c30166b425 | -13.99148 | -45.7961 | 2026-01-18 00:28:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 202da526-e1d0-3ee3-b2f9-167747ad74eb | -12.66108 | -46.77288 | 2026-01-18 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a6f27d4d-2e9b-30c1-890d-e062c9387816 | -14.78405 | -45.94613 | 2026-01-18 00:28:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5c4e2120-f11c-3e49-be6d-1b958eece7b7 | -12.50233 | -48.73921 | 2026-01-18 00:28:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f875b6c1-983d-386b-ad01-6ac968fa151e | -13.68678 | -52.58954 | 2026-01-18 00:28:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 92b06cdd-6c99-3772-9a20-932436dcf2b7 | -13.42483 | -47.339 | 2026-01-18 00:28:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1b040c06-6a98-39bf-8114-518e7cf93cc8 | -12.70706 | -46.79247 | 2026-01-18 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 41eca88d-d87e-3576-a20a-40dc165ab37e | -13.91138 | -50.34713 | 2026-01-18 00:28:00 | TERRA_M-M | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5be65118-d5c7-35af-8350-29e8e9879b32 | -14.74687 | -45.91141 | 2026-01-18 00:28:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 1a76e309-f27c-3988-9ce9-77ad6dc93072 | -13.74666 | -43.65501 | 2026-01-18 00:28:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 525a690a-c75f-3c2a-af5a-1f8c66be466d | -13.74952 | -43.67208 | 2026-01-18 00:28:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 14fa6019-a3ce-354f-a184-803b245c84ee | -13.90243 | -50.34842 | 2026-01-18 00:28:00 | TERRA_M-M | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7088fd9d-cca6-3701-8bb5-443720b83794 | -14.74513 | -45.89986 | 2026-01-18 00:28:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f732d4b3-1eb2-3ae4-958a-78c5298b5c52 | 1.121 | -60.5224 | 2026-01-18 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.8 |
| fc2d2bff-f0eb-3e8d-8bcb-c7cedf43dd4e | 1.1393 | -60.5033 | 2026-01-18 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.7 |
| cd06efdc-e6dd-36c8-a5a9-df334b48b248 | 1.1393 | -60.5222 | 2026-01-18 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 3613b7fc-b846-3ca2-a8c0-7b6bc45ce6d9 | -4.6967 | -46.40922 | 2026-01-18 00:30:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0eed3521-673d-3a94-9ced-1b3baa3e58f1 | -4.69726 | -46.41579 | 2026-01-18 00:30:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| cf038fb0-0ff3-3ea8-ae56-c8763d4987ef | -2.45794 | -48.23861 | 2026-01-18 00:32:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 09211645-e9c5-3f94-9055-8d78152cfc9c | 1.121 | -60.5224 | 2026-01-18 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 56e47094-9871-36ff-af17-674b46e10620 | 1.1393 | -60.5222 | 2026-01-18 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 8bf02989-5454-35c8-b2f2-1a5c1505d480 | 1.1335 | -60.517502 | 2026-01-18 00:54:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5e4a6e32-ba61-35af-9f58-417bfed85ad4 | 1.1303 | -60.531399 | 2026-01-18 00:54:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| be7cf319-5efa-3753-bd37-2e28073e2c69 | -19.478701 | -55.465099 | 2026-01-18 00:54:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 06f06030-d932-3a3d-8f7b-04ab801f56a0 | 1.135 | -60.510601 | 2026-01-18 00:54:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 56991bf0-6e54-3c67-9622-1a3512d8074a | 1.1319 | -60.524399 | 2026-01-18 00:54:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 056aaf0a-c4d6-3da6-9bd2-6bc4ab15f190 | -19.476999 | -55.4576 | 2026-01-18 00:54:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1098d404-a750-3daf-ad0f-17d7f1409764 | -19.6716 | -56.936901 | 2026-01-18 00:54:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 98ba5f80-9734-3e82-9132-75f72d5cbb83 | 1.1393 | -60.5222 | 2026-01-18 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.1 |
| f998618b-7585-3977-a070-5e0a54c88820 | 1.121 | -60.5224 | 2026-01-18 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.5 |
| baf8089f-9e22-3884-a5f5-b41f6f28f11a | 1.1393 | -60.5222 | 2026-01-18 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.5 |
| f527abde-9e30-37cd-93dd-9e6003d9bc0b | -10.2579 | -36.2821 | 2026-01-18 01:20:00 | GOES-19 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 97.3 |
| 83b87a48-67a0-36ed-bb0b-2fa94106c515 | 1.1393 | -60.5222 | 2026-01-18 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 2acab9c5-7e1a-31a1-b639-9b6459d3a452 | -10.2579 | -36.2821 | 2026-01-18 01:30:00 | GOES-19 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 115.5 |
| 5f6aca3a-5761-3c50-9a65-234f5711ae38 | 1.121 | -60.5224 | 2026-01-18 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.7 |
| dc599348-877f-3ffb-8bc8-aabf10dbe5b8 | -19.6689 | -56.929001 | 2026-01-18 01:32:00 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ad8b93fb-b548-3276-96e2-676d67b1ee27 | 1.1304 | -60.514999 | 2026-01-18 01:32:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 44b49ea9-1409-384f-948a-dff9931dd5e8 | 1.1322 | -60.507099 | 2026-01-18 01:32:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f4e2ac2a-dea9-3911-8e17-54d5ec20d59d | 1.1286 | -60.5229 | 2026-01-18 01:32:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8c508d5c-bb0b-3ccd-8b6a-beddf72a72b5 | 1.1402 | -60.517101 | 2026-01-18 01:32:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 057378dc-5e9c-3cae-80e9-d690aadf081d | 1.1393 | -60.5222 | 2026-01-18 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.0 |
| e196788d-9c48-388d-9eae-e303bac96c59 | 1.121 | -60.5224 | 2026-01-18 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 6358a398-f07f-3b4c-baf0-533d60614248 | 1.1393 | -60.5222 | 2026-01-18 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.4 |
| e4b24056-e5d0-3be1-99aa-22852db46ab6 | 1.1393 | -60.5222 | 2026-01-18 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 795cde23-4c7a-36f9-93ed-c384090d961b | 1.121 | -60.5224 | 2026-01-18 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 8514c61f-e43a-31ef-99bb-2338111ccd19 | 1.121 | -60.5224 | 2026-01-18 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.1 |
| ef0f87c6-e382-3ba9-b4bc-d4f848f52068 | 1.1393 | -60.5222 | 2026-01-18 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.1 |
| b0c263d7-b517-3f11-a344-a90f5ec7a504 | 1.1393 | -60.5222 | 2026-01-18 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 7e0034b4-eab8-37f5-bb6b-f1f4d15cc0b6 | 1.1393 | -60.5222 | 2026-01-18 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 09b1949e-a979-3bf7-a4a8-5358c5d65f9b | 1.121 | -60.5224 | 2026-01-18 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.4 |
| f684ba04-6e67-39f2-ab30-b19918d17bfa | 1.1393 | -60.5222 | 2026-01-18 02:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 6628b1a2-5fcf-3107-be8a-a83595ae4bba | 1.1393 | -60.5222 | 2026-01-18 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 5c70efc2-9cf7-3135-a359-a9696af48581 | 1.121 | -60.5224 | 2026-01-18 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 4ac9d835-fd0f-3357-a27f-d042b1697898 | 1.1393 | -60.5222 | 2026-01-18 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 585184e3-a435-31a0-ab82-6a7042208dec | 1.1393 | -60.5222 | 2026-01-18 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 9ff39850-9f62-366e-b809-8a400863c0b6 | -5.88739 | -35.61337 | 2026-01-18 03:36:00 | NOAA-21 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 7d8c0ba2-26a2-357b-828c-bb934cee4523 | -7.14543 | -34.90637 | 2026-01-18 03:36:00 | NOAA-21 | JOÃO PESSOA | PARAÍBA | Brasil | 2507507 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 35ce8dae-5aa5-3ba6-a480-b1dcd8bc3749 | -5.89081 | -35.6139 | 2026-01-18 03:36:00 | NOAA-21 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 515d2f97-01b6-3a76-a2bc-a5764cb722cc | -5.88051 | -35.34782 | 2026-01-18 03:36:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 320ac6a5-c496-34a2-af35-66567b27f377 | -5.83673 | -35.64393 | 2026-01-18 03:36:00 | NOAA-21 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 6db84034-d348-38eb-a57b-3d38206f7e23 | -5.87992 | -35.35149 | 2026-01-18 03:36:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fe439765-910c-36be-8e1a-a5f873ddec3f | -5.84016 | -35.64448 | 2026-01-18 03:36:00 | NOAA-21 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b7da1ea1-e9df-3370-ab5f-a0f696b95434 | -6.49108 | -35.04161 | 2026-01-18 03:36:00 | NOAA-21 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7b049e59-b165-3400-a5c9-b1e2c91db295 | -6.28362 | -35.06328 | 2026-01-18 03:36:00 | NOAA-21 | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 1f99144f-7edb-3555-bf00-b20d1bd4c06f | -6.48154 | -35.05837 | 2026-01-18 03:36:00 | NOAA-21 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 11317968-4aa7-394f-a9d9-418571898bf5 | -9.4439 | -35.85502 | 2026-01-18 03:38:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e084b67a-50d9-361b-907c-8385eec0c511 | -9.57688 | -36.15689 | 2026-01-18 03:38:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 90ccda09-a980-3c4e-a385-60c91d73ad92 | -11.79207 | -45.35219 | 2026-01-18 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d22db76c-4b92-321e-b04f-695568abfa87 | -8.07825 | -35.41952 | 2026-01-18 03:38:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 85a2f8b8-3be6-3bcd-86e8-139d5240d270 | -12.48741 | -43.78408 | 2026-01-18 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f622a4e-a9a2-3612-838d-4d1f907fcf5c | -12.48684 | -43.78711 | 2026-01-18 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a5ad7fe-8870-36c0-8275-df49466a40f7 | -8.40318 | -35.17304 | 2026-01-18 03:38:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f1f8383c-fc6e-3d30-b6b0-335dbad8bd51 | -7.72409 | -36.39856 | 2026-01-18 03:38:00 | NOAA-21 | BARRA DE SÃO MIGUEL | PARAÍBA | Brasil | 2501708 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c6e1c4e9-799a-3000-a8c4-13c518c12579 | -11.8049 | -45.34682 | 2026-01-18 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a657c5b2-e5bf-35f9-883b-5e0abd4d968a | -8.07882 | -35.41593 | 2026-01-18 03:38:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 67aee1aa-5603-39ba-92ce-e46c00be8892 | -11.7985 | -45.34944 | 2026-01-18 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6625ca5e-4285-3597-a110-9f7e6e52d842 | -11.79777 | -45.35315 | 2026-01-18 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e750e039-c2d7-3d42-b707-82f4a29992e9 | -11.79701 | -45.35699 | 2026-01-18 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 66231c60-6c90-378e-91b5-42b9649ba8d9 | -11.7913 | -45.35606 | 2026-01-18 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c6cda88f-d122-38ce-a88d-398c4c3c405f | -12.66362 | -46.77144 | 2026-01-18 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d5947b4e-99dd-32d0-8985-5ff3188e3b9a | -10.2396 | -36.64381 | 2026-01-18 03:38:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9ae240c1-72a3-385f-89ed-f3c3c558d0a6 | -12.7085 | -46.80099 | 2026-01-18 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 62befc04-c147-3344-b735-1b81aea19e03 | -11.80418 | -45.3505 | 2026-01-18 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f0381d8a-37d8-3f4f-8505-efd6a1b760ea | -12.66459 | -46.76666 | 2026-01-18 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d5a909bd-2d32-394c-bad6-eabcba9d7817 | -7.32973 | -35.49546 | 2026-01-18 03:38:00 | NOAA-21 | MOGEIRO | PARAÍBA | Brasil | 2509404 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 07eda5c7-4a54-3623-b5ea-3078d001b778 | -9.57349 | -36.15633 | 2026-01-18 03:38:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8f9fa42d-5f01-3462-89af-83ea4e45f32b | -12.7095 | -46.79614 | 2026-01-18 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a0c2c86-e007-384c-896b-b21faf55c729 | -11.7984 | -45.3627 | 2026-01-18 03:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |


[Clique aqui para ver as próximas entradas](README2.md)
