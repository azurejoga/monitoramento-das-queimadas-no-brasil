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
| ae96cc76-a11d-346f-9475-a98b4ef19af1 | -1.0919 | -53.4359 | 2024-12-03 04:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| faf7538c-5e13-3f60-a756-811d6d9cc7f8 | -3.347 | -46.0486 | 2024-12-03 04:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 4c8f703f-cb20-3137-84a3-885be591fb8e | -1.0735 | -53.4562 | 2024-12-03 04:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| a874d754-cf98-3d6d-abd6-b9d49a890796 | -5.1181 | -43.1964 | 2024-12-03 04:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| b485b321-d19c-3fb0-9cdf-488ffceaa46f | -5.8197 | -46.4706 | 2024-12-03 04:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 015801a1-005f-3702-8201-144079a07c41 | -1.0736 | -53.436 | 2024-12-03 04:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 5a26ce98-df35-3b46-8d07-9e34f4795288 | -3.259 | -53.659 | 2024-12-03 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| edcb3695-7443-37e9-8cbd-087a5cd585af | -3.076 | -53.3808 | 2024-12-03 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| a1d768c0-0cf6-33ae-a19d-76c44c395121 | -2.8196 | -53.0629 | 2024-12-03 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 57942328-a502-3c0e-8704-22d1ac05fa8b | -5.8009 | -46.4941 | 2024-12-03 04:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 01a4c200-033c-3f5e-ad2c-83be80cc073e | 2.7267 | -60.3916 | 2024-12-03 04:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.5 |
| f6ee55d4-86cc-3aa3-93a2-593b33824e2d | -3.2591 | -53.6186 | 2024-12-03 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 153d6181-5cbd-37e1-945b-927073964eba | -1.0919 | -53.4561 | 2024-12-03 04:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 533ef0d3-4774-31f7-8192-793f67c80ef0 | -3.0944 | -53.3804 | 2024-12-03 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 89b2ec70-7234-349e-a6e0-877978fd9116 | -5.801 | -46.4719 | 2024-12-03 04:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 184.9 |
| a82ba9f8-a2c8-3d49-80af-16cf7aa089cc | -3.259 | -53.6388 | 2024-12-03 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| f81fe960-aa8c-3099-8137-4e7559e310a0 | -3.2406 | -53.6595 | 2024-12-03 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| c5e23c0d-7afc-39da-8865-6a88434247ea | -5.81 | -46.48 | 2024-12-03 04:00:00 | MSG-03 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c2f25bed-9b05-35dd-ad73-0934dbcf9a48 | -1.7488 | -52.78387 | 2024-12-03 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 752d8e5d-7db1-33a0-bc17-12b8960cb3c8 | -2.23538 | -46.38596 | 2024-12-03 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea725316-6e10-3b09-a1e7-cba74a07cf5e | -3.11917 | -45.99228 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 24f206d2-701c-3887-b0d7-4d7e632d866b | -3.26735 | -53.34021 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 876c3945-7e4a-30b5-8814-94c8da1ffbec | -6.18507 | -43.41306 | 2024-12-03 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7a93074b-782e-3731-8341-f7fd939ae93c | -2.4286 | -46.48241 | 2024-12-03 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 690276f7-d681-388c-9927-d021fb1b8b34 | -3.55303 | -51.45647 | 2024-12-03 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dbb6367-52bd-3474-a7be-de9bf21de9e8 | -3.08543 | -53.37911 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| c3ce0155-1211-3ea6-85cf-e6692826dc89 | -2.67892 | -46.61051 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44f8a506-35e4-3fe5-b0be-15743fcc686d | -3.55194 | -50.18218 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 900365cd-da8f-3d6a-96cc-dcd6cac78802 | -3.27311 | -50.32825 | 2024-12-03 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2ab29d5b-9f78-3523-86c9-4d7787230f4a | -3.02746 | -53.86947 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1a55594b-7196-37a7-9293-1df6599af220 | -2.8575 | -45.83436 | 2024-12-03 04:06:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e220be3a-9a74-36c0-9711-466a34550d0b | -2.59321 | -46.01519 | 2024-12-03 04:06:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a321c42e-dbc1-333d-b62f-d4ac0d3fa299 | -4.16699 | -48.19665 | 2024-12-03 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| aba879be-80fb-3ae6-80b9-b06c3da20be4 | -3.85648 | -46.53149 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04d090a7-dfac-3d2b-a293-25527af06235 | -3.21153 | -53.12409 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 281315eb-4277-314d-b598-d848d6dd80b2 | -5.1181 | -43.20421 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| df485725-1eb4-32cd-931d-c5a0af3d39a0 | -4.04687 | -46.81885 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa5c3f11-0dd1-3144-8c9b-15188c4a373d | -6.00219 | -45.41594 | 2024-12-03 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a0cff45-b9ff-37b7-8cfa-3167a19689a5 | -4.1646 | -48.59145 | 2024-12-03 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 67bc87e5-5ae5-37f3-aabd-b28fa8a5af46 | -3.27803 | -50.33273 | 2024-12-03 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 230262e0-0339-374b-b465-d6cf9418f756 | -3.82859 | -46.5952 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db9f25b3-cf27-3acd-9f9b-9f6669b11b63 | -3.8861 | -50.07499 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 669b4827-6b53-3549-895b-c2a306e7fd7c | -2.88704 | -45.44727 | 2024-12-03 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8c3b7aae-8419-3dfb-b3de-58cebc4b6499 | -3.84995 | -46.51873 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71880f86-6347-3526-83be-393769fea93f | -3.54113 | -50.18008 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cab7379c-c975-38b8-825d-3829863bfe99 | -3.26155 | -53.6234 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8b91de4-e0a7-3aac-bc1a-5e9560b4bb6f | -4.16778 | -48.19182 | 2024-12-03 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 56a8811a-371a-32d3-a93f-a2ff4817ef6f | -3.90206 | -46.65122 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44deb816-86d5-3490-a16a-687f858e4fd0 | -3.33806 | -46.05253 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 92e7f1bf-8f0a-3452-9d8c-28a8ec9e37fd | -2.10031 | -46.57726 | 2024-12-03 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eedb9fcc-2d78-309e-bbcf-78ef38c7be91 | -3.93541 | -46.92299 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5845401-2e66-38ca-8561-dbaf18027ab7 | -3.92071 | -52.38758 | 2024-12-03 04:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11633a86-6b58-3e9d-aa78-95a54a19a88d | -5.13082 | -44.56118 | 2024-12-03 04:06:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d9455d1-11e5-3ea9-b0f4-0cfcf9e50094 | -4.18777 | -51.18409 | 2024-12-03 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20eec444-aeb7-362a-a6bc-fdb5df1fd3d8 | -2.81661 | -53.05696 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3363ec51-2de3-3cbc-aa16-358da2de835f | -3.55793 | -50.17977 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4c38f387-dd58-3543-8e81-49200cf06aeb | -4.09437 | -47.42336 | 2024-12-03 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71e7935f-d66d-31b9-9546-3924ec5d9258 | -2.46919 | -46.54592 | 2024-12-03 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e907b4c7-ac30-335d-ba9c-3511c7c9a5f5 | -5.79576 | -46.48654 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6c049ccc-25a5-31a9-8d9f-e59784eba3f5 | -3.92343 | -52.39428 | 2024-12-03 04:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d17b0db6-4790-34b4-9fa0-85b76960c7fd | -3.18773 | -51.164 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e9967a1a-e33c-3a0d-a40e-b2debbac3df8 | -4.20985 | -44.37367 | 2024-12-03 04:06:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8c8afbc5-445d-3f2b-8274-b063b70886db | -5.45364 | -44.82535 | 2024-12-03 04:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9a4d632c-70d6-337d-834e-e933232d9f48 | -6.12036 | -43.96494 | 2024-12-03 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 0d6b16ca-52d2-34ba-b5f8-7538cdd004b1 | -4.07383 | -46.68101 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5987cb1b-12d1-3b86-8372-b3144430a90d | -6.18851 | -43.41358 | 2024-12-03 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 437ddba7-6b10-3209-a340-7fd90900dba5 | -4.04751 | -46.86862 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3b7affb-959e-3833-a8ab-80487b72c928 | -5.80921 | -46.48116 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3457ca38-4f5a-37b3-a09e-7fa38a3af4ab | -5.80452 | -46.48417 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 65fcc52d-0ac0-3238-b6bd-9fe23784f67c | -2.57269 | -46.40905 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ca7bdc5-d442-3565-9816-92b46a1be4ea | -5.57086 | -44.88824 | 2024-12-03 04:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cc2addc8-620a-35ac-b7a3-b8bdec7d790f | -6.02651 | -46.24705 | 2024-12-03 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 597ee3f0-b126-3bc4-a33b-270ad174733b | -3.09016 | -53.37716 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 500ec783-5e7b-39f9-b4f5-0a2d39535b4f | -2.21008 | -45.73611 | 2024-12-03 04:06:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9dbaf9e1-25a3-3e13-96e1-6ebfac03151c | -3.02764 | -53.87347 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e77124d9-963e-3b4a-9270-09af10fe6f87 | -5.11749 | -43.20795 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 731710fa-4f7d-3316-b517-ca1084478105 | -3.48407 | -50.24599 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 259aa11d-0b81-38d7-b77a-8cf6f40e68bf | -1.67952 | -47.55465 | 2024-12-03 04:06:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d143f5ea-9505-39fc-82fb-5e8f720ffc2e | -3.37943 | -51.01193 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d3a1bc99-bd29-3d13-916b-f83ad32d54c0 | -1.51441 | -45.90996 | 2024-12-03 04:06:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34e35ff7-96e1-3124-836e-e35657cad1bf | -5.11329 | -43.21931 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 77998a54-11cb-34da-9abf-a4d930040929 | -5.14831 | -43.23605 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7e3697c2-5dad-38c9-aba6-0e38ab4f49d1 | -4.16856 | -48.59736 | 2024-12-03 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51fe8c43-24a4-39ce-a22e-3b8dd5bd20df | -3.26903 | -46.93295 | 2024-12-03 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1f2a723-5b80-37a5-869f-0aab1f98ac26 | -3.53974 | -50.18018 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b992c655-c480-3f6c-b23a-7195ebc906a7 | -3.81923 | -46.6777 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a18cdcc9-7485-3bc7-b9ec-8d35fa8d6b2f | -1.67484 | -47.55394 | 2024-12-03 04:06:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c62b3a7-b38a-33cb-bbe5-b96ed98e8160 | -5.81796 | -46.47888 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85860c14-ca44-3150-b23e-e51c3fc8266f | -3.99195 | -46.62943 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b0fdf560-5444-31e1-abe2-d7dbd33b028b | -3.90447 | -46.65865 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4986d39-b4e3-3e3f-881e-7deb6b89e8e2 | -3.34681 | -46.05061 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ec35c689-2ddd-3aa7-9eca-039536d35639 | -1.74115 | -52.62899 | 2024-12-03 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7119cb86-0c6e-36a4-914d-980b7fcdaeb1 | -5.10984 | -43.21876 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| da0c646a-164d-3709-88c3-7cacbc34a7f8 | -1.91 | -46.30075 | 2024-12-03 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aeab83e7-eb54-3c84-805d-bdafab04e06a | -1.07877 | -53.46158 | 2024-12-03 04:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 657f4188-a4e2-3b54-8d5a-641e3545f67b | -4.0462 | -46.82288 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da7e56da-ec5a-391b-beab-adf8b75c0859 | -5.411 | -42.92805 | 2024-12-03 04:06:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 44f526e8-bf1e-3c9a-bc1d-716e461a33f3 | -5.11566 | -43.2192 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 7a519f51-aa61-37ed-ae2f-0fd4a09fbd89 | -3.61377 | -42.74253 | 2024-12-03 04:06:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a39815fc-c88f-3735-8c91-97f9208518a4 | -4.19352 | -51.18498 | 2024-12-03 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README25.md)
