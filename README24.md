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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fff83bb5-8a14-3cf2-8a32-c65858096bd3 | -3.1786 | -50.6016 | 2024-10-30 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 00e2996c-fcdd-3dc1-b245-70b3e88e8133 | -3.1787 | -50.5807 | 2024-10-30 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| e6b53fa0-499c-3cbc-a12b-04c19e33347b | -3.234 | -50.5789 | 2024-10-30 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 96020706-7754-3ae9-b731-d8c5b4e755ca | -3.2564 | -45.5831 | 2024-10-30 02:35:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 47.7 |
| e7b5b7fb-d8cd-3602-821f-9786e692c1af | -3.2534 | -50.3689 | 2024-10-30 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 5035f18a-95ce-346d-8564-eeb12c1214ee | -3.2718 | -50.3683 | 2024-10-30 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| ed1ded75-0f98-3b86-b3d1-1a2d32716ed2 | -3.2535 | -50.3479 | 2024-10-30 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 180.0 |
| 2a9fa54a-f0cd-37fc-a6b7-1c067e177698 | -3.5818 | -47.3621 | 2024-10-30 02:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 4dbe17fc-db5c-3865-9272-cf126684f8c0 | -3.5817 | -47.384 | 2024-10-30 02:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 173.1 |
| 30398c29-e0a6-3b97-9d7f-a9706f42e6bc | -3.5632 | -47.3629 | 2024-10-30 02:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 7ffb7c52-0f7e-38f6-b9e7-e90e99023ba3 | -3.5631 | -47.3847 | 2024-10-30 02:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 194.0 |
| f3ff5331-dfad-3a13-8377-0b85ad60345c | -3.4597 | -54.0765 | 2024-10-30 02:35:26 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| b727ad3f-6abf-3c07-b063-c121adf0b3bd | -3.8037 | -51.1644 | 2024-10-30 02:35:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 1f4e208a-ba85-30ce-9c89-5e14bdbf94fb | -4.0867 | -50.0021 | 2024-10-30 02:35:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 1140c891-5fe0-3717-8dad-1401eff018dd | -4.0866 | -50.0232 | 2024-10-30 02:35:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 05da2feb-4589-3b54-a38a-4fe66d51e4ff | -4.0682 | -50.0029 | 2024-10-30 02:35:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| db0569a2-2f99-3521-96f9-a0540f00114c | -4.0681 | -50.024 | 2024-10-30 02:35:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 68df9804-8d7f-3e4f-bfde-5e18c92aa9cf | -4.2679 | -50.6879 | 2024-10-30 02:35:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| fad5967d-e4a6-3d3f-9d9c-8780f3418493 | -4.2496 | -50.6677 | 2024-10-30 02:35:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 7921fa4d-0428-3c39-90d1-bfacc51aacbe | -4.2563 | -43.4368 | 2024-10-30 02:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 3d526fd7-a682-319c-a0a2-9b3002c17455 | -4.2748 | -43.4589 | 2024-10-30 02:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 5de80af8-61a8-3873-b1d5-ec0411c3efe7 | -4.2749 | -43.4357 | 2024-10-30 02:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 9625291d-d0f1-3a06-9de0-a535a027052e | -4.2681 | -50.6669 | 2024-10-30 02:35:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 4a556690-3915-34a9-9d04-fcb0887a3585 | -4.5864 | -44.2943 | 2024-10-30 02:35:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 8cbcb53b-9929-3810-92bd-1bfe05ee9809 | -4.6051 | -44.2932 | 2024-10-30 02:35:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 202.5 |
| 5bef971e-ad89-31d1-a946-1527f2c004c2 | -4.6049 | -44.3161 | 2024-10-30 02:35:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 138ae2e0-dd53-3b6f-8cb9-3b9f62003fd4 | -4.5862 | -44.3172 | 2024-10-30 02:35:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 75c7623d-a49c-3bae-9b74-4069b4be7961 | -5.2306 | -47.9566 | 2024-10-30 02:35:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| d5110834-2525-3a6e-8fc6-cf5f7d48a410 | -5.2308 | -47.9349 | 2024-10-30 02:35:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 51e714a1-ed25-3c1c-886b-853b11f435d7 | -6.8408 | -59.0519 | 2024-10-30 02:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| a9eaf75b-24be-389f-bde7-79bd68d7e3dc | -6.8592 | -59.0511 | 2024-10-30 02:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 0908b7ad-8a58-3904-80a2-2fc4d59b5d9d | -10.3434 | -49.6536 | 2024-10-30 02:36:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 132.9 |
| a908cbb2-cf0b-3897-9f26-fcf841ed771d | -10.3437 | -49.6321 | 2024-10-30 02:36:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 96c708ca-054e-387a-bbf8-c0fc2090af26 | -10.3624 | -49.6516 | 2024-10-30 02:36:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| fb2208b4-54bf-33cc-9d10-846ebb8da3ef | -10.7175 | -44.916 | 2024-10-30 02:36:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 37c5e502-d36f-33d4-a225-100419b52ff1 | -11.9187 | -53.5588 | 2024-10-30 02:36:13 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| a70f28a6-5ddf-38b6-b0b2-7a05d8181c29 | -11.9377 | -53.5569 | 2024-10-30 02:36:14 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 74250526-92c6-3b70-bad8-8c795bae1103 | -13.6887 | -46.1247 | 2024-10-30 02:36:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 9a505d81-800d-3b0d-889c-fd046ba6d7c8 | -13.6891 | -46.1017 | 2024-10-30 02:36:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 205.0 |
| 7b3fc639-4952-3bb2-bc5c-e1330e82891f | -13.7081 | -46.1215 | 2024-10-30 02:36:23 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 4d530583-64c2-3c3f-961a-d1e4cf17fb21 | -13.7086 | -46.0985 | 2024-10-30 02:36:23 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 178.8 |
| b55e5b64-bf2a-3ccf-8d46-ea24bb45c532 | -19.5662 | -56.7164 | 2024-10-30 02:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 74.3 |
| e17b9fd5-4f6e-33e2-babb-4224a67c113b | -19.5859 | -56.7346 | 2024-10-30 02:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 46.5 |
| 9b00cc33-bbfc-3cca-b0eb-b142fd898ce0 | -19.5862 | -56.7136 | 2024-10-30 02:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 98.9 |
| fc63ee84-9a70-38c2-9c29-865b7761adfa | -19.6063 | -56.7108 | 2024-10-30 02:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 135.1 |
| fd5c2a49-6217-3567-ab18-b7b91876c069 | -19.6067 | -56.6898 | 2024-10-30 02:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 1c79c85f-d4d9-3c02-8bf4-4ef66477fbf6 | -19.6264 | -56.7079 | 2024-10-30 02:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 65.9 |
| 91778c96-691f-3a62-afae-5f1774e7c7fc | -1.458 | -54.0763 | 2024-10-30 02:45:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 026d8f40-da0f-31e8-bf79-c023ec18903b | -1.458 | -54.0562 | 2024-10-30 02:45:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 1bcdaf53-e564-3816-9639-5e8b3af215a4 | -2.7335 | -57.4911 | 2024-10-30 02:45:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 8f0de89e-a05d-30b4-8808-238fd4f55673 | -2.833 | -49.2413 | 2024-10-30 02:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 0819719a-29ad-3e57-920b-75b2a74a8cca | -2.8331 | -49.22 | 2024-10-30 02:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 8b231e12-ef66-38e1-9c49-457a10d123d6 | -2.8515 | -49.2408 | 2024-10-30 02:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| bd3d946a-674e-3fb1-aad7-7d44cd9a0275 | -3.2719 | -50.3473 | 2024-10-30 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| b632642d-05a3-35ee-9db5-a8599207ef5f | -3.2718 | -50.3683 | 2024-10-30 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| e2a1a5b8-422e-31e4-ac9e-2dfdc5c4cbd8 | -3.2535 | -50.3479 | 2024-10-30 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| b75b77d0-3ffd-3b8b-9f6c-b0ed027cc758 | -3.2534 | -50.3689 | 2024-10-30 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| fe1c9344-7daf-3b42-bf30-306d63a75746 | -3.234 | -50.5789 | 2024-10-30 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| f3cc12d3-1c29-393e-b517-2000929be745 | -3.2378 | -45.5839 | 2024-10-30 02:45:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 85.3 |
| e30b86cf-2aec-3c23-bd54-d1d9d86c8ff2 | -3.1787 | -50.5807 | 2024-10-30 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 9b78781f-f6a4-3efa-b756-47f8ad79a53a | -3.1786 | -50.6016 | 2024-10-30 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 172b52ce-7a68-34e9-9d3c-2a946ff0a8bd | -3.1602 | -50.5812 | 2024-10-30 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 776c977d-3253-3865-a979-bb382bff8ecd | -3.1601 | -50.6021 | 2024-10-30 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 72a7421a-0d0f-32bd-8fcb-7944a8ad52ea | -3.5818 | -47.3621 | 2024-10-30 02:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 27ed6844-b359-3aac-93de-819a72846452 | -3.5817 | -47.384 | 2024-10-30 02:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 157.9 |
| 84c3f4f6-84ed-3dd7-a3c0-c0b4448a582a | -3.5632 | -47.3629 | 2024-10-30 02:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 3524ceeb-3959-3e84-bccb-5171f9f81332 | -3.5631 | -47.3847 | 2024-10-30 02:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 216.4 |
| 54abf8fb-3f6f-3856-946c-236a3c614a89 | -3.8037 | -51.1644 | 2024-10-30 02:45:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 7e18aaca-25b0-3b7d-a90b-d8b674d594bc | -3.9486 | -48.1291 | 2024-10-30 02:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 9c622e96-f6d0-398a-849d-f1f96643022e | -4.0682 | -50.0029 | 2024-10-30 02:45:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 75714278-62ca-3fd1-8af7-c8d9e410958c | -4.0681 | -50.024 | 2024-10-30 02:45:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 578e89be-ebbc-3e8d-bc5a-744f5a68509c | -4.2679 | -50.6879 | 2024-10-30 02:45:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| abee6381-cecc-33f5-a4e2-43a762a6ee79 | -4.2681 | -50.6669 | 2024-10-30 02:45:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 6219e5b0-e490-378b-a1d2-7128686337b0 | -4.2496 | -50.6677 | 2024-10-30 02:45:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| c6f346bd-3bd6-35da-8539-ea3233360dcb | -4.6049 | -44.3161 | 2024-10-30 02:45:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 4c294a9b-eddb-3e12-8f84-4ec9a04b868c | -4.6051 | -44.2932 | 2024-10-30 02:45:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 32a187b6-ed49-3c21-b6a9-ca6431ddafa0 | -5.2306 | -47.9566 | 2024-10-30 02:45:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 49.4 |
| bf4ee09f-7c59-33e1-a67e-fc20bd895de5 | -5.9788 | -45.3621 | 2024-10-30 02:45:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 56991796-f398-3d4f-b5de-4f66f9bdbc9e | -6.8408 | -59.0519 | 2024-10-30 02:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| fa457a8c-b6cb-3d25-92d8-444a78241f72 | -6.8592 | -59.0511 | 2024-10-30 02:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 879f752e-1c98-3da3-a22a-a71d4ec58bd9 | -10.3434 | -49.6536 | 2024-10-30 02:46:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 3f047603-40df-34bc-a7ad-09941dbb6ec9 | -10.7175 | -44.916 | 2024-10-30 02:46:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 3b8456b4-6da4-3432-8144-452051da7af7 | -19.5662 | -56.7164 | 2024-10-30 02:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 78.6 |
| 38897b73-7cb6-3334-9e6d-22420dc75aa2 | -19.5859 | -56.7346 | 2024-10-30 02:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 67.0 |
| 953c4238-1a36-39c2-9c5a-b25941fab546 | -19.5862 | -56.7136 | 2024-10-30 02:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 135.8 |
| 006360c4-8291-36e6-893e-3907ed3bf124 | -19.6063 | -56.7108 | 2024-10-30 02:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 141.9 |
| 365cb35c-6cf2-3a12-a394-5672f9f66227 | -19.6067 | -56.6898 | 2024-10-30 02:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 66.0 |
| a24f4800-1e04-39ec-920d-334d600be1c4 | -19.6264 | -56.7079 | 2024-10-30 02:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.6 |
| 334eb214-4d83-34c6-bbe2-4cd4e893359d | -1.458 | -54.0763 | 2024-10-30 02:55:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 40640b25-7078-3876-b913-61fd9524a18d | -2.8329 | -49.2626 | 2024-10-30 02:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 9f02bb89-b15a-379e-a48d-ef6c1fef8380 | -2.833 | -49.2413 | 2024-10-30 02:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 6d7be965-d1fc-3a29-b26a-04cec294dbcc | -2.8331 | -49.22 | 2024-10-30 02:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 712278ea-beda-3769-9e63-c60fe8e4839f | -2.8515 | -49.2408 | 2024-10-30 02:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 1ce2f5d4-0a9f-302d-beef-6603b44325a6 | -3.1601 | -50.6021 | 2024-10-30 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 501655a8-3264-3c65-bbe1-5638142ad97d | -3.1602 | -50.5812 | 2024-10-30 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 533173bc-63ff-3728-bf0c-ad65d54ada30 | -3.1786 | -50.6016 | 2024-10-30 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 7fafae90-eeea-398f-95f8-5df3e7fe6ed8 | -3.1787 | -50.5807 | 2024-10-30 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| b3905b92-c3ca-3699-a764-07f2bd64a71d | -3.2378 | -45.5839 | 2024-10-30 02:55:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 16720d52-a0ab-366d-8e33-1599a1c1453c | -3.2564 | -45.5831 | 2024-10-30 02:55:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 97e2058f-ba90-34ca-817b-940299dd269d | -3.2565 | -45.5607 | 2024-10-30 02:55:24 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 49.2 |


[Clique aqui para ver as próximas entradas](README25.md)
