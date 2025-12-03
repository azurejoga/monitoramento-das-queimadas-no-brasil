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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 323fe4fa-473a-37d9-81e1-fa5d9a49c893 | -3.23925 | -45.56792 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 0a8a45f5-e656-34cc-9eac-986fd6a20d0c | -2.57231 | -47.16201 | 2025-12-03 04:38:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b45ce2d4-6f3d-335d-996c-16a579911e06 | -2.74331 | -49.33419 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0e5e701-cb1f-3d56-8b80-b76e6dc186ad | 1.37154 | -50.69831 | 2025-12-03 04:38:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 87c602f3-40aa-326c-9eb9-11c428f8f5aa | -2.59539 | -49.258 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f16cc551-af4e-3128-9f69-66a46ae9b419 | -3.76047 | -50.15256 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcb18027-f1df-3773-8d95-8bebd9966ff7 | -5.68947 | -47.51003 | 2025-12-03 04:38:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d21660e8-8d8c-3f6d-811a-915d9552bc49 | -3.63223 | -48.89526 | 2025-12-03 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e1baab8-b624-3b05-a66c-0621ee6f7e87 | -3.03691 | -50.23752 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f767818-8b5c-39df-9d1a-0fd2c8b5e551 | 1.99558 | -55.70966 | 2025-12-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98db6ced-0bc9-3576-af48-b021aceed8d7 | -2.99536 | -47.89847 | 2025-12-03 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f44e972-2c2a-3572-8cfb-9a74002c83d6 | -2.60148 | -49.26249 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a418241-30d2-3f57-b122-c57a881981de | -1.91832 | -52.17439 | 2025-12-03 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4167d735-c637-3ce5-95bc-19a6e2bd5a8a | -2.99815 | -47.90245 | 2025-12-03 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f48f79ee-2b3e-3cf8-9767-b4002d314879 | -3.24172 | -45.56585 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 00c4a460-b55f-38b7-a667-cb9179466d28 | -3.5937 | -47.26689 | 2025-12-03 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1abb2e43-89d7-3d98-b664-3ba04c3a278c | -3.2296 | -45.57248 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cc792ba7-03e8-30bf-b9ef-f9af20dacb46 | -3.53764 | -49.94675 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d31c978-c47a-3bad-b6ed-ec89be2b53a6 | -3.19303 | -41.85158 | 2025-12-03 04:38:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 2b09bf55-652b-394f-a438-337acf1f72c2 | -3.25981 | -45.55409 | 2025-12-03 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04537995-45c9-3a72-918b-edf63df14d61 | -3.63083 | -53.65887 | 2025-12-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0431b272-10e7-32e0-9abb-475c5bb1c724 | 2.87176 | -60.26258 | 2025-12-03 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7dc21ca1-4122-3576-abce-1d0f509742f3 | -5.38724 | -46.75641 | 2025-12-03 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29efbb2a-e247-32b6-93a9-0396217292fb | 0.21113 | -50.99574 | 2025-12-03 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38159d09-2b94-3f92-9520-308e4098c4cb | -3.84971 | -47.06394 | 2025-12-03 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf4ee90a-8706-3c92-87bc-fec257033d49 | -3.28653 | -50.07788 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6beb4d68-6243-3a7c-8f6a-6351ed55ae7b | -3.476 | -51.3672 | 2025-12-03 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bc4894a-ff3b-3f15-b528-e2bb571f9ffa | -2.89006 | -50.47906 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2962ff13-357f-359c-b767-c0e1064477cf | -4.12175 | -50.08573 | 2025-12-03 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07d2103d-f818-3dde-bce7-9cf54b7ac0a7 | -3.22367 | -45.5631 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eaf4fb52-1c8c-3a8b-ab49-fc52ec8d49dd | 1.37043 | -50.69944 | 2025-12-03 04:38:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c5cad62b-7c53-3cbf-a636-2f321938ff10 | -2.57606 | -46.88241 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acdf0d5b-938e-3121-b738-d0285fb1919c | -2.5987 | -49.25851 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0fda3f0-9def-3cd6-a58c-4c60e288a503 | -3.53088 | -49.98914 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c91274a2-4efc-3d4a-904a-ae7e1821e23b | -3.24459 | -45.5815 | 2025-12-03 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72248f58-132d-31fa-aec9-928e5f430fe8 | -2.98355 | -49.51471 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 211b13fe-b27e-3dd0-b765-3f8abf969a1d | -2.84011 | -50.46372 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| eea3b67d-4568-3106-b451-598cc141e52d | -3.23977 | -45.57829 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1a96d14e-99ef-3129-96c7-4d844a890c21 | -2.9264 | -48.23083 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7989a2c0-6737-3589-810c-a30c4a2c5c4b | -2.43946 | -47.19269 | 2025-12-03 04:38:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2eed37f4-9361-3cb3-9cb7-a36c3a0f8b81 | -1.05911 | -53.10091 | 2025-12-03 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4809d94b-5873-3ea2-a037-1c80c8c18bce | -2.78812 | -47.41753 | 2025-12-03 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f604b3cc-1894-3429-ba96-87bb26b03591 | -3.23321 | -45.57303 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 032d81ca-444a-3dba-8696-3a23dc846dfe | -2.27048 | -46.95783 | 2025-12-03 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea619822-c257-3de4-b1d8-d4967a856616 | -2.24175 | -48.52175 | 2025-12-03 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef7c5d84-16d4-38d4-822b-c45b413d52e7 | -2.1899 | -51.9767 | 2025-12-03 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 89768560-df16-3f72-a835-0fda7b5bb097 | -3.0496 | -48.42334 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ae3d0baf-27bf-3451-859e-e9e4ca29d294 | -2.03865 | -46.59471 | 2025-12-03 04:38:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7b2043b-82a0-3e1b-8386-e710dcc8376c | -3.24646 | -45.56907 | 2025-12-03 04:38:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ce846ad0-3437-367a-a225-044d4c3df87e | -3.22535 | -45.57608 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14be66a7-9109-3a80-965f-87dc23850feb | -4.278 | -48.09106 | 2025-12-03 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80e6d9f9-a657-3d0e-ab68-d2d1fa26c4c1 | -2.5755 | -46.88601 | 2025-12-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7fc4f58-b225-39a1-9572-9aace3fed9e6 | -3.27837 | -50.75526 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efbbbf28-fa35-39bd-9a82-be00ed2a3324 | -3.24536 | -45.55182 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfd759d7-d8b9-3039-a748-eab508f349cc | -3.63607 | -48.89233 | 2025-12-03 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9eba7b3-5e35-3aee-bcba-67e007f252a4 | 0.49275 | -51.15884 | 2025-12-03 04:38:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f2ad20f-a0e1-3022-ac9c-0eebaf173667 | -2.38421 | -48.95554 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8dd8c3f7-8220-33a7-89d7-66cf72bcd9f1 | -2.5722 | -49.10197 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f2086e5-48d9-3bd2-ab88-204f6f00e9e8 | -3.90869 | -43.96348 | 2025-12-03 04:38:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4c9c0a4-f854-37d0-9b43-f4484f8ca3bb | -3.23644 | -45.55228 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c9ff0639-de2c-3aa4-b2b8-13b274f9751f | -2.90095 | -45.35094 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74afad9c-bcd2-33cf-b28d-96cbded9b841 | -1.19614 | -53.09137 | 2025-12-03 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8f9426e7-e8bc-3d1f-8ae7-065b0de723be | -3.22581 | -45.7303 | 2025-12-03 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f88f106-3717-3171-a923-9e4c0dfdba2e | -3.22793 | -45.55949 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbe3192d-57bf-3687-a3b6-292852eacd19 | -2.95624 | -49.14828 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f7a5fef-2441-3a13-9ad5-e43c01851ee0 | -2.31126 | -45.67479 | 2025-12-03 04:38:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58eba7e6-a1f2-3678-b6fb-a77c4bf095ba | -6.28469 | -39.68885 | 2025-12-03 04:38:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 01501a97-7535-394c-ba86-c76a2c41fbda | -3.67651 | -50.44092 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e1ab66d-40b4-3d28-adcd-e42241162ae0 | -2.8367 | -50.46319 | 2025-12-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3ba8b17c-338c-36b7-aaed-6f38360bce23 | -2.19058 | -51.9724 | 2025-12-03 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6bc04ff3-9786-383a-becf-d561fcb73a1c | -3.22728 | -45.56364 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91fe039b-e07e-30cc-8ee8-f1caaa5478eb | -2.84505 | -52.61728 | 2025-12-03 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79bd6c51-d228-3bc1-93ca-7b26907cf176 | -3.22831 | -45.58078 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b2841b7-c535-3066-a82a-0e8b53eabcc6 | -5.39073 | -46.75695 | 2025-12-03 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d060f65-6456-3206-888b-3a09009b2060 | -3.98638 | -47.99896 | 2025-12-03 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9860167-f830-37b0-837e-3a7252d6a25f | -3.22174 | -45.57553 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7559953b-9049-33ef-b0df-6f6d2f537eec | -3.52849 | -49.98874 | 2025-12-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c67ede65-3995-3869-8faa-ec0ea6e9ed9d | -3.56137 | -42.70905 | 2025-12-03 04:38:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79698baa-7b4f-3c9c-8b5b-e91d271c59d0 | -6.26002 | -37.23764 | 2025-12-03 04:38:00 | NOAA-21 | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ef4a3fe3-5c7e-360b-b83f-93416282e24a | -2.94343 | -49.10038 | 2025-12-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 447ea920-31d9-3b79-8953-74049ffd76e3 | -3.23912 | -45.58244 | 2025-12-03 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 743e37ca-7e79-3417-a582-b505f84a04bf | -2.92586 | -48.23427 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b338f549-3801-3b99-8085-92238ffe4f9e | -3.23626 | -45.56319 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 5e0c0ec3-40c1-32d3-b840-613f385e6bd5 | -3.22922 | -45.5512 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2aa1001-4f19-3ed7-814d-9851d3d6db59 | -3.98693 | -47.99547 | 2025-12-03 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b711fc1-f802-3508-b9f5-4dd59d1f28e7 | -2.21072 | -48.00242 | 2025-12-03 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| de57303e-a905-3e79-a27c-52aa3b17236c | -2.09056 | -53.41541 | 2025-12-03 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06c45a2a-7d81-37d4-9a22-b9ffed4442fe | -1.91826 | -47.91426 | 2025-12-03 04:38:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 205135d9-2672-3e01-b375-c57144fab80d | -3.24175 | -45.55127 | 2025-12-03 04:38:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c677120-a0ef-3a35-a783-a9ea1deeb5cd | -1.94086 | -50.33247 | 2025-12-03 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c7cc8dd-3a9b-3609-b682-1953040f845f | -2.62562 | -45.1438 | 2025-12-03 04:38:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 201af297-31bb-30b1-b726-3f7f68451256 | -5.38664 | -46.76032 | 2025-12-03 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 886641c8-dc2a-3c20-bc5d-4306977b3989 | -3.21942 | -45.5667 | 2025-12-03 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a807428e-57d8-3772-ab8b-6e66b110b518 | -2.48537 | -47.83284 | 2025-12-03 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52f16782-d12d-3006-a54b-835d4808317f | -2.53805 | -47.31716 | 2025-12-03 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13ac3737-3842-3cbd-a255-1b8f6e447451 | -3.92034 | -47.70045 | 2025-12-03 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 539c0547-ecca-3516-9fe9-2d727a9d2ac5 | -4.39359 | -43.13961 | 2025-12-03 04:38:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 23dc4bcf-5e57-37b3-8c16-1a6f9ba2ce67 | -2.93652 | -53.27713 | 2025-12-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abd140bf-7e0a-358b-9d10-899209c2e405 | -1.51428 | -45.60414 | 2025-12-03 04:38:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bedfe4f-a5c0-366f-8af3-ca9b7d9d2c8d | -3.19234 | -41.85622 | 2025-12-03 04:38:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |


[Clique aqui para ver as próximas entradas](README14.md)
