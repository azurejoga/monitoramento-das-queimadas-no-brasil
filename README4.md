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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ea3f30b-a137-31c0-9cb7-2fbb46fa27d6 | -18.64076 | -54.59873 | 2025-03-23 05:12:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9608a8df-9e04-3637-98af-003d2ad65272 | -18.64027 | -54.60257 | 2025-03-23 05:12:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 414039be-9869-326d-8003-24c739a33bd1 | -18.63667 | -54.59807 | 2025-03-23 05:12:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa714a73-eeb8-3bd4-9744-2c26fd655458 | -18.49773 | -55.12904 | 2025-03-23 05:12:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 846ffec4-7fa3-3962-8d05-caf4a26ea447 | -8.10491 | -43.1269 | 2025-03-23 05:21:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| d8f111b0-e32a-340a-8ccd-4e456096ebb7 | -8.0961 | -43.12559 | 2025-03-23 05:21:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 168c8c96-8316-3955-b61c-e12dd2d8fa5c | -8.09477 | -43.13441 | 2025-03-23 05:21:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| f2020186-942f-316d-bfd0-27c0ffc39316 | -8.10358 | -43.13573 | 2025-03-23 05:21:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 6dd78493-09ad-34db-9f66-89e98b208703 | 2.3942 | -60.40882 | 2025-03-23 05:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b7e3d32-83d1-3fa1-9d6c-f0523a581fba | 0.82392 | -59.94666 | 2025-03-23 05:57:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95660dc0-16f2-3fec-816c-8208fc237be1 | 2.73389 | -60.41246 | 2025-03-23 05:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 0583a2f2-ee4e-35c8-b7db-f9630b8a0f59 | 1.29481 | -60.00012 | 2025-03-23 05:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7058a366-617a-302d-8cd0-192ec8c91b73 | 2.24876 | -60.30315 | 2025-03-23 05:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d790ca99-c307-3d75-9ae3-6067e51751f7 | 2.7384 | -60.37945 | 2025-03-23 05:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c35bb740-7b23-345e-a944-b4e7958dee40 | 0.82069 | -59.8597 | 2025-03-23 05:57:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5267cdd0-43e7-3de1-96f7-51358fb009d1 | 3.892 | -59.65754 | 2025-03-23 05:57:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 873b50c1-00c6-3749-a4a2-039173cdbcd4 | 0.82021 | -59.85662 | 2025-03-23 05:57:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 998b1902-6fa7-3c59-ae3c-8bb216c02a73 | 2.73219 | -60.402 | 2025-03-23 05:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 1a6c5630-89ce-3cbb-9894-855a5b284350 | 2.73304 | -60.40724 | 2025-03-23 05:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 441f3b60-b030-3664-bdda-a26350d03cec | 2.583 | -60.27144 | 2025-03-23 05:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 533d4df3-5b25-3d9f-83e6-07771dbf1416 | 1.29575 | -60.0061 | 2025-03-23 05:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36e0bdbe-b512-3903-a814-3dd99ed309a5 | 3.89247 | -59.66036 | 2025-03-23 05:57:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| dc00dbc7-9309-3e5c-bd44-a1879e8cd596 | 0.82903 | -59.94582 | 2025-03-23 05:57:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6eaff7c-794b-31b7-abab-369d4688b3f4 | 4.21289 | -60.13636 | 2025-03-23 05:57:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cc4d6d53-23b9-3d63-9a63-f2c68842f59c | 1.29527 | -60.00306 | 2025-03-23 05:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4544b4b-27a3-3c93-a3db-be916c3c409f | 2.72909 | -60.41325 | 2025-03-23 05:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 14.4 |
| fb73e333-dac9-37fd-a59b-36990a1f85f7 | 2.37795 | -59.93204 | 2025-03-23 05:57:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f8159e9-07ff-3be5-8a8a-e6bb2e96ac4a | 1.29624 | -60.00921 | 2025-03-23 05:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 92a9b18b-d19d-33a2-9379-179f1410751d | 2.73784 | -60.40644 | 2025-03-23 05:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 13.7 |
| e55c9083-1637-3e9c-936b-3e44229e19e7 | 1.30032 | -60.00218 | 2025-03-23 05:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50e9a676-6edd-381e-b951-85ae01674f76 | 4.21205 | -60.13125 | 2025-03-23 05:57:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ead0e3c-0b98-351b-a93b-ec9e20d4f48f | 0.82438 | -59.9496 | 2025-03-23 05:57:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61547b93-d0ba-3b41-95eb-d5030626cf56 | 2.16895 | -61.25441 | 2025-03-23 05:57:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d7a5095-d4fe-3c7d-be7c-86b55fd83914 | 1.29986 | -59.99926 | 2025-03-23 05:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4db02441-340e-3836-a865-66a46f8222d5 | 2.72824 | -60.40803 | 2025-03-23 05:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 17.5 |
| ae85405c-5aab-3ac6-8230-83cbaceb7b1a | 2.73614 | -60.39598 | 2025-03-23 05:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4dd6cbd3-3629-31c7-a255-ea6c780c706a | 1.9049 | -61.10028 | 2025-03-23 05:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c83a5ac2-12f4-339e-be26-7919c60f30ec | 2.73699 | -60.40121 | 2025-03-23 05:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 13.7 |
| d164d796-b56e-3bec-96ee-67417012f5d2 | -12.56154 | -57.75664 | 2025-03-23 06:01:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0c210ae1-0deb-312a-a5a4-651dcc9402e2 | -9.86063 | -65.26274 | 2025-03-23 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8df76cb7-817d-305b-bc66-e94f77730661 | -9.66655 | -65.75234 | 2025-03-23 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0844ce60-b617-3353-832c-1c41eaf6fc92 | 2.74096 | -60.39658 | 2025-03-23 06:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 13ed5cd4-be2c-3af6-87c4-53b791054d31 | 2.74073 | -60.38355 | 2025-03-23 06:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3b4c098d-8f86-3a21-8af0-73114d572a3e | 2.73501 | -60.40482 | 2025-03-23 06:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.3 |
| db6fb184-69ba-3ba5-9fde-84e04dcce27d | 2.74216 | -60.40358 | 2025-03-23 06:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1574f3b7-939c-3305-ba0e-ce4496ecf887 | 2.73855 | -60.38248 | 2025-03-23 06:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98ccfbf4-6b29-33a4-985c-bb40dfe0f330 | 2.7338 | -60.39779 | 2025-03-23 06:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 858566e2-370b-3dce-b3dc-3b83d94daa6e | 2.73622 | -60.41187 | 2025-03-23 06:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 0abd4cd0-c86f-370d-b442-98e1c5b1ba6a | 2.72907 | -60.41306 | 2025-03-23 06:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a16579be-d88e-34ed-ab09-177f0ccabfd9 | 2.73948 | -60.3765 | 2025-03-23 06:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eef3d997-567a-307e-a3ee-4352579d179e | 2.73733 | -60.3754 | 2025-03-23 06:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f3174b5e-a1d8-3498-a3eb-2d8e508f20a2 | 3.89263 | -59.65776 | 2025-03-23 06:57:00 | AQUA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 91190b94-ecde-3b71-a2b8-e117d4e38fff | 2.74776 | -60.37019 | 2025-03-23 06:57:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c735fb71-af44-3b42-a12e-4e50576aa43f | 2.74099 | -60.40209 | 2025-03-23 06:57:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 9ce949f8-ee72-3a88-ba15-ac94f1b37ead | 2.73869 | -60.38701 | 2025-03-23 06:57:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| d362645a-0e70-3b56-bef8-7d4971647c3d | 2.74327 | -60.41713 | 2025-03-23 06:57:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 62dc401b-4335-316c-94cc-01662b921657 | 1.29931 | -60.00313 | 2025-03-23 06:57:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 63671634-949c-3893-aeb1-a4790b3a54f0 | -9.02303 | -37.63885 | 2025-03-23 11:47:00 | TERRA_M-M | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 5.9 |
| b53d0e2f-8807-3de1-b8ac-f02ff0273c9d | -5.78193 | -36.63739 | 2025-03-23 11:47:00 | TERRA_M-M | SANTANA DO MATOS | RIO GRANDE DO NORTE | Brasil | 2411403 | 24 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 057fb546-e51c-34b4-9aa4-d0a5cb4dbd1e | -5.7909 | -36.63866 | 2025-03-23 11:47:00 | TERRA_M-M | SANTANA DO MATOS | RIO GRANDE DO NORTE | Brasil | 2411403 | 24 | 33 | nan | nan | nan | Caatinga | 6.6 |
| eeaffb2b-b9a5-3a03-9332-a66993e0f3f1 | -12.41571 | -39.15545 | 2025-03-23 11:49:00 | TERRA_M-M | ANTÔNIO CARDOSO | BAHIA | Brasil | 2901700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 042b2d35-d430-3f9f-9d73-8c31b96eccc3 | -11.91992 | -38.89582 | 2025-03-23 11:49:00 | TERRA_M-M | SANTANÓPOLIS | BAHIA | Brasil | 2928307 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 34713d5f-be1b-3c43-ab79-688ca386f382 | -15.36879 | -43.78809 | 2025-03-23 11:49:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| a3395976-8b52-31cc-b131-1339ce746602 | -9.85967 | -37.29052 | 2025-03-23 11:49:00 | TERRA_M-M | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 4737553e-de50-372f-ab5a-abdf1ab6804f | -15.39562 | -43.79893 | 2025-03-23 11:49:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 4eddec48-b6b9-3558-b359-808a9a416b8e | -12.42508 | -39.15697 | 2025-03-23 11:49:00 | TERRA_M-M | ANTÔNIO CARDOSO | BAHIA | Brasil | 2901700 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 6e87efd6-f0a2-3e5d-b5d2-a96e4c8f3eb2 | -12.32208 | -42.61878 | 2025-03-23 11:49:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 16.4 |


