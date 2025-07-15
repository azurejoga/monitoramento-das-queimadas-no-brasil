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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3d44c99-f34b-3caa-b58d-eece0895b47c | -6.6493 | -45.6937 | 2025-07-15 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| ff45cf8d-66ec-39bf-a577-8ab078a74a97 | -6.668 | -45.6922 | 2025-07-15 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 0c881fa6-b542-3b09-9886-441b4e3ddbac | -12.4797 | -46.9243 | 2025-07-15 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 3bd2e5aa-b769-3531-944f-db93e77e1340 | -6.649 | -45.7163 | 2025-07-15 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 4e72f6e7-a4f0-3a93-b933-33c4b819dff3 | -6.4839 | -45.3686 | 2025-07-15 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| c7c3847a-1cf6-3c55-988a-cfdc7f14514c | -11.4598 | -47.3107 | 2025-07-15 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| e5c8a6c4-58dc-3781-83bb-eceed1894aa1 | -11.4588 | -45.0895 | 2025-07-15 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 0f2858ab-283e-32d4-9db2-95c68db89252 | -11.4789 | -47.3082 | 2025-07-15 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 03b56894-cc3c-3e81-875d-5544b9a54eb5 | -6.4848 | -45.2781 | 2025-07-15 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| cd451f24-f874-35b3-a5b7-b050225fc23d | -4.0417 | -48.0602 | 2025-07-15 13:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 4b5d6e4e-1124-3fba-b519-f02991254468 | -6.4839 | -45.3686 | 2025-07-15 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 2263289e-14a7-394d-bf08-f78e49e92bbf | -11.4789 | -47.3082 | 2025-07-15 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| c7ea08d8-5990-3008-a8a2-d77421f1c5ec | -7.658 | -44.4207 | 2025-07-15 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 150.7 |
| a68812cb-4070-30d6-b60f-217f8e543339 | -12.4797 | -46.9243 | 2025-07-15 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 80b99a64-9d87-3c22-a088-b95657ad90a6 | -11.4588 | -45.0895 | 2025-07-15 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 8b170e40-ba6a-36ef-9dbb-f24d23e7a338 | -12.4797 | -46.9243 | 2025-07-15 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 82e400e5-cb29-3763-aafb-3f4afa520d23 | -11.4588 | -45.0895 | 2025-07-15 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| b9a957ae-5bc0-3f08-970f-464824a1229a | -6.6493 | -45.6937 | 2025-07-15 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 34298aeb-b60c-3bcf-9e56-c536f7d4876e | -4.0417 | -48.0602 | 2025-07-15 13:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 13d95660-a390-3233-9183-6317c5eb1094 | -6.668 | -45.6922 | 2025-07-15 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 550a4e5f-4cf1-3755-a0af-35cebc2cf2af | -11.4598 | -47.3107 | 2025-07-15 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 77a53c62-c33f-36a9-ae3b-693b256fbe0f | -7.658 | -44.4207 | 2025-07-15 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 07e2afe0-f4f1-3861-8a10-768cdb926592 | -10.3775 | -49.9293 | 2025-07-15 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 26ccf0b1-2b99-3dfc-a8ee-fc1abdb2757e | -6.6678 | -45.7147 | 2025-07-15 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 244.3 |
| 3f5857c8-d86e-300e-a3b5-d24c530522d4 | -6.649 | -45.7163 | 2025-07-15 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 272.6 |
| 70d924f7-af0b-3223-8bab-2966fce2bc0f | -11.4789 | -47.3082 | 2025-07-15 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| dd385932-14b5-3aa8-a142-95a3cfb2b43a | -6.6493 | -45.6937 | 2025-07-15 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| fc0e7fda-5706-3f99-9cdb-d44e2a743e35 | -7.658 | -44.4207 | 2025-07-15 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| e00a5b56-fef3-32db-89a8-9d2e664b9a5f | -12.4797 | -46.9243 | 2025-07-15 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| f42ce348-bc9b-36f8-bc56-8370f8e3ba8b | -6.649 | -45.7163 | 2025-07-15 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 249.6 |
| 54ef86ce-9121-3d41-835e-ac11b55659e4 | -6.4846 | -45.3007 | 2025-07-15 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 0f065bb5-2002-3e0f-8f9c-7076f067d294 | -6.4848 | -45.2781 | 2025-07-15 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| b951fd19-f609-3992-bc7c-e1f467d9faa8 | -6.6678 | -45.7147 | 2025-07-15 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 176.4 |
| c0bd9cc2-ab4f-316f-8b9d-f6d71a3a74a8 | -11.4789 | -47.3082 | 2025-07-15 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| e5d621bb-97d2-340c-9f7c-1ed0aff964f0 | -10.3775 | -49.9293 | 2025-07-15 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 9b02875c-bd20-378a-8e2b-898ee045fdb7 | -6.668 | -45.6922 | 2025-07-15 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 5a8483d4-57c2-34e8-9eea-2d60900f6751 | -6.6678 | -45.7147 | 2025-07-15 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 52dfc650-a622-3065-b71f-f324cbca5c19 | -7.185 | -43.0013 | 2025-07-15 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.4 |
| e390d012-2dd5-361d-8348-f736c53b04ca | -7.2039 | -42.9994 | 2025-07-15 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 157.3 |
| fc6009c9-7e98-3cfc-b2a2-f39093589253 | -4.0417 | -48.0602 | 2025-07-15 14:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| ee9de9e0-1519-336b-a394-0ed22060c89f | -12.4797 | -46.9243 | 2025-07-15 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 2aada166-b92d-3838-8dfa-62d741051d85 | -4.0231 | -48.061 | 2025-07-15 14:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| eb798369-8c9c-3192-baab-360d53af7893 | -7.658 | -44.4207 | 2025-07-15 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 1179cc1e-f996-336e-a75a-5b198a72f133 | -6.649 | -45.7163 | 2025-07-15 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 17e34d5f-3a36-36dc-8f81-ec02367dff32 | -12.0825 | -43.4753 | 2025-07-15 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| dd7b4762-8ce3-3a39-8e11-d9048a9fcc9c | -12.0628 | -43.5022 | 2025-07-15 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 77a7281c-97f1-31c4-88ee-debd03bceef9 | -7.1848 | -43.0248 | 2025-07-15 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| de3830e2-4e83-3c08-8225-19f12f5d2e6a | -7.2039 | -42.9994 | 2025-07-15 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |
| 0396174d-2c7f-35e4-af05-fea1638cabc0 | -6.8676 | -42.7725 | 2025-07-15 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| b429d2e5-ed31-38b3-961c-643c8c887afe | -4.0417 | -48.0602 | 2025-07-15 14:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 840ea3a9-3bea-3abb-82a2-f5fcd40b759c | -7.658 | -44.4207 | 2025-07-15 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 2aa4c76c-5589-3873-9310-07890903cf8d | -6.4846 | -45.3007 | 2025-07-15 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 421c701c-b435-3200-b2d3-fd7d251d8fb0 | -6.4839 | -45.3686 | 2025-07-15 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 135.0 |
| f3199a4d-ac78-3567-83c1-23659ce044d8 | -10.34 | -49.9118 | 2025-07-15 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| a6c54e16-e9d8-3399-a70d-984212f5b255 | -7.185 | -43.0013 | 2025-07-15 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 137.5 |
| 8aaab127-50a9-340d-bad1-94b623620e93 | -12.0825 | -43.4753 | 2025-07-15 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 61ab7874-6dbd-3687-b14e-98a7767c75a8 | -6.465 | -45.3927 | 2025-07-15 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 8f32b978-1f96-38f0-bca5-2906728978f2 | -11.4588 | -45.0895 | 2025-07-15 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 22fd78df-0fa7-3b41-8711-ce3497de6239 | -6.649 | -45.7163 | 2025-07-15 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| c1cd4ca1-5b39-3e20-9460-4ad541ede988 | -4.0417 | -48.0602 | 2025-07-15 14:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 5988f5d6-f516-3934-9fbf-c0f08cc405ec | -7.185 | -43.0013 | 2025-07-15 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 149.8 |
| 83407aa8-4e81-3478-971e-467106a082de | -6.4846 | -45.3007 | 2025-07-15 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| b0d58c63-6f88-36e3-ab9e-23cf8a26936e | -10.34 | -49.9118 | 2025-07-15 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 201aca67-58f1-3aa5-93cb-0a81c371c019 | -6.161 | -45.8887 | 2025-07-15 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 7f20e143-4ba5-321e-98d6-450f1f27300b | -6.4848 | -45.2781 | 2025-07-15 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 66132150-be2a-38a1-8823-29697e329d8a | -7.2039 | -42.9994 | 2025-07-15 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.9 |
| 37fd4667-f98a-3751-ad01-b616871dd766 | -6.6678 | -45.7147 | 2025-07-15 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| b750cb55-753a-33cd-ab66-63195766d28d | -11.4588 | -45.0895 | 2025-07-15 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 86dbe659-fb02-375e-aeaf-5ee14b40a5e0 | -7.658 | -44.4207 | 2025-07-15 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.6 |
| edf191e9-3dda-3249-8584-89908715447c | -6.649 | -45.7163 | 2025-07-15 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 169.7 |
| f572b81d-b705-32b4-90c2-eb1878131084 | -7.1848 | -43.0248 | 2025-07-15 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| b0dc566f-f61e-39eb-a8c9-2c8777a75b80 | -7.6394 | -44.3995 | 2025-07-15 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| ca5477cf-fdb3-3348-9fe4-cde6a5194bd1 | -6.668 | -45.6922 | 2025-07-15 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| ed0b1584-3975-3bb1-a655-e9ceade704ac | -4.0417 | -48.0602 | 2025-07-15 14:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 0d84e641-88a1-376c-9925-d57a6c1cfd83 | -4.0231 | -48.061 | 2025-07-15 14:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 33991554-e2f4-308b-8142-6de33b236bed | -7.658 | -44.4207 | 2025-07-15 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 6b5c550c-4f1f-3c01-8d6a-2d0d732c5420 | -5.3741 | -43.9216 | 2025-07-15 14:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 14618328-7f71-3443-b74d-67c6753610f2 | -6.1612 | -45.8662 | 2025-07-15 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 3d6cb7a7-6262-3925-aa1f-b324eceb1843 | -6.6678 | -45.7147 | 2025-07-15 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 428e6ed5-df6c-3771-9697-0698445ba695 | -6.6493 | -45.6937 | 2025-07-15 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 6949f4b8-921f-3f01-8cfe-89aed687017f | -6.649 | -45.7163 | 2025-07-15 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 0b6d9052-cb9a-3bec-a77b-5bc1d9a40c00 | -11.4789 | -47.3082 | 2025-07-15 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| f2037639-f9f8-3a6e-bc6f-1fbeff4b1ec5 | -11.4588 | -45.0895 | 2025-07-15 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| d8f7da04-60aa-3ef4-a55e-24dfebee20a3 | -6.649 | -45.7163 | 2025-07-15 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 158.4 |
| 8f73c45d-a69e-39cb-99bd-819792618ea4 | -12.0825 | -43.4753 | 2025-07-15 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 7d789e48-80d3-3b06-b926-42de5ab2b1c0 | -6.4846 | -45.3007 | 2025-07-15 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 2f901393-11e7-379c-af1e-9070231cb003 | -11.4598 | -47.3107 | 2025-07-15 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 75df1bc1-7d66-3bfe-b757-4a7fbcced96b | -4.0417 | -48.0602 | 2025-07-15 14:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| ac135b60-6543-3174-af0a-6cf504cbf31f | -11.4789 | -47.3082 | 2025-07-15 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 2cb6528a-8f66-3229-ae4c-e712ce13cf67 | -7.658 | -44.4207 | 2025-07-15 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 1c02747e-27c2-3476-9a3f-b19f77f45f4a | -4.0231 | -48.061 | 2025-07-15 14:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 45719c31-6fb1-3c4b-b608-dfef5620328c | -11.4588 | -45.0895 | 2025-07-15 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 2978e0fe-5fb2-33a6-afb7-b577671c4612 | -6.4848 | -45.2781 | 2025-07-15 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |


