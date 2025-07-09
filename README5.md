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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84b4a480-db61-3ab9-937c-40b0a4662e18 | -8.5217 | -43.2593 | 2025-07-09 01:50:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| 8c4d1d06-5367-3835-b35e-0000d408af7f | -8.5025 | -43.285 | 2025-07-09 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 309.0 |
| c9d89e95-c870-3faf-9daa-7a533dfc305d | -11.4393 | -45.1154 | 2025-07-09 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 203.1 |
| 34e61c16-e819-33d1-89a2-194ad6eda4dc | -18.6467 | -55.7351 | 2025-07-09 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.6 |
| 8b5dfde6-3285-3bb6-b3d5-ef4f32d6c3c4 | -10.6296 | -49.472 | 2025-07-09 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 8a7f4a68-e88e-3e0e-afc1-6bfcfb05e6b9 | -11.4584 | -45.1126 | 2025-07-09 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| c000d6b1-fb1c-3422-8752-23801c03d448 | -7.2405 | -43.0899 | 2025-07-09 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.5 |
| ed21abaa-b4da-3807-93c4-fea4af3a4977 | -7.2408 | -43.0664 | 2025-07-09 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 126.3 |
| 04c76c0c-8dc2-318f-9723-07e019069672 | -11.6737 | -43.7762 | 2025-07-09 01:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| d88a8b02-b5ca-35cf-9e2f-6b5537d2dced | -11.4205 | -45.095 | 2025-07-09 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 270ed47e-2187-3222-94d4-7e18d7484e39 | -6.1792 | -48.0494 | 2025-07-09 01:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 4f0ff500-3adb-325a-a056-c2fc24552ba7 | -8.5214 | -43.2828 | 2025-07-09 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 336.3 |
| ebd9b092-e28c-3e4c-b469-3e5ca0019b26 | -8.5211 | -43.3063 | 2025-07-09 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 259.4 |
| bb551f69-63f1-3af9-aac7-9062120bfe09 | -11.4588 | -45.0895 | 2025-07-09 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 65938679-46e7-3225-bfa0-ec369998dbf9 | -8.5022 | -43.3085 | 2025-07-09 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 238.9 |
| 69daedc7-4a36-31da-88c4-57e565068557 | -6.1606 | -48.0507 | 2025-07-09 01:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 7d360dee-42e4-38d4-a6d8-6ae612d26788 | -10.5776 | -49.1316 | 2025-07-09 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| de6e5ed8-d695-3bc1-a30d-9d75b1a12a4e | -11.4397 | -45.0923 | 2025-07-09 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 70df50c9-2b72-3855-be89-da5da0453b9a | -11.4201 | -45.1181 | 2025-07-09 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| f4a2959f-d61d-322d-95ea-80756149875b | -11.4393 | -45.1154 | 2025-07-09 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 189.7 |
| 60ca0860-1d2f-3f08-9a14-bb632ac0f3c8 | -11.4588 | -45.0895 | 2025-07-09 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| ee878b0a-6520-3a31-8cbd-46a0a3671665 | -11.4397 | -45.0923 | 2025-07-09 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 991ea97a-dae8-3cf5-8a91-aec2e360d615 | -8.5214 | -43.2828 | 2025-07-09 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 343.3 |
| a2f32f73-d260-34da-b1f3-26828353c90d | -10.5779 | -49.1098 | 2025-07-09 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| b8cbd59a-d591-3ac3-99c6-82d0ec008be4 | -7.2408 | -43.0664 | 2025-07-09 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 133.6 |
| da45da1c-db4c-3caf-9b2e-cad52a15a3b6 | -6.1606 | -48.0507 | 2025-07-09 02:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 61320126-4fc7-3de7-9d14-50bf5248f2a2 | -8.5025 | -43.285 | 2025-07-09 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 251.9 |
| f29f4d40-0648-3c70-a0ec-2e2cb2ac2802 | -8.5211 | -43.3063 | 2025-07-09 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 190.4 |
| 0597d013-5ee9-353e-abe5-1632bccba2aa | -10.5776 | -49.1316 | 2025-07-09 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 4c24b46f-0200-3492-b841-12f189045103 | -11.4201 | -45.1181 | 2025-07-09 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 976371f1-0b92-3e3a-a38d-7cdc003348aa | -11.4205 | -45.095 | 2025-07-09 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 325faea1-0e60-3efb-84ba-16d80e5049be | -6.1792 | -48.0494 | 2025-07-09 02:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 144.1 |
| ad479eb7-949e-3c9f-afc6-1c991be28cb7 | -8.5217 | -43.2593 | 2025-07-09 02:00:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 61.9 |
| 3afe82f1-7961-366a-9b43-0135118bf9c3 | -8.5022 | -43.3085 | 2025-07-09 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 146.5 |
| b32ca2a8-127a-3869-8cfe-52ac349e6a45 | -11.4584 | -45.1126 | 2025-07-09 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| f7ce7a45-4be3-3a8f-88de-7f386fa070a2 | -11.4201 | -45.1181 | 2025-07-09 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 04e07c99-5933-37f7-9be2-4d77c03989a9 | -8.5022 | -43.3085 | 2025-07-09 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 148.8 |
| 7f94f39e-4101-3eff-8467-35a636ba231f | -6.1792 | -48.0494 | 2025-07-09 02:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 3140e0fe-a0f2-39d8-81fe-cde1fbc038bf | -11.4588 | -45.0895 | 2025-07-09 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| fdfe7084-66cb-34b1-92c3-686c0c5526d1 | -8.5025 | -43.285 | 2025-07-09 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 271.1 |
| b167f4d8-1eb0-3fe2-8072-216b435102ee | -11.4205 | -45.095 | 2025-07-09 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 423e413e-8ac0-3ea3-86d8-6b3fb474b47b | -8.5214 | -43.2828 | 2025-07-09 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 237.3 |
| fc3103d6-aa1b-38e7-ab05-0ed09d356283 | -10.5779 | -49.1098 | 2025-07-09 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 043a516b-2a2e-3778-bce0-641b1632136d | -11.4397 | -45.0923 | 2025-07-09 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| b2fdf211-1942-3e2f-8d1f-2b10c67e9548 | -11.4393 | -45.1154 | 2025-07-09 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 186.5 |
| ef5c11f6-e103-3db8-a1fb-28f5cc253f3d | -11.4584 | -45.1126 | 2025-07-09 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 8d0d30ca-84a9-3a2e-ac6a-8b7d9294b9bd | -10.5776 | -49.1316 | 2025-07-09 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 4a456c9f-f809-330c-afa3-dfce4172c521 | -7.2408 | -43.0664 | 2025-07-09 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 108.2 |
| 3479ea12-2812-3933-ac64-c645a3b430a4 | -6.1606 | -48.0507 | 2025-07-09 02:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 57da594a-53e0-3e4b-a27b-bd70029ad65a | -8.5211 | -43.3063 | 2025-07-09 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 82945739-9b40-3778-b382-b06d7ae08875 | -8.5022 | -43.3085 | 2025-07-09 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 222379f8-e43f-3c8c-99ca-d3fe8973da25 | -10.5776 | -49.1316 | 2025-07-09 02:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| df0fe212-8996-36bf-8bb7-341543907406 | -11.4205 | -45.095 | 2025-07-09 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| e246d22d-ee69-3318-8612-c1fefce1d4e0 | -8.5214 | -43.2828 | 2025-07-09 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 280.0 |
| 6bfe6687-012d-37eb-aefb-56f21963fb67 | -6.1606 | -48.0507 | 2025-07-09 02:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 7391ebb8-e92f-39df-a4f6-04c0420ff7c2 | -11.4584 | -45.1126 | 2025-07-09 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 6ed6b5e3-4bdb-32c4-8324-1034fb6f840d | -8.5025 | -43.285 | 2025-07-09 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 186.1 |
| ac7050f9-cd31-311a-bf02-645b99aae306 | -11.4588 | -45.0895 | 2025-07-09 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.7 |
| a25340a9-58ec-36c7-8417-cc861c4c9f50 | -6.1792 | -48.0494 | 2025-07-09 02:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 0a3f56b5-5ffb-354b-890b-3350728e4b5b | -7.2408 | -43.0664 | 2025-07-09 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| a8d9feeb-26c9-3399-8ebb-402b3122e28d | -11.4201 | -45.1181 | 2025-07-09 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 365c3a49-7798-30b5-9352-2393c4699022 | -8.5217 | -43.2593 | 2025-07-09 02:20:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 6e4cd360-e917-322c-87ce-1e68bc0c759b | -8.5211 | -43.3063 | 2025-07-09 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 605477fa-84c3-3932-9809-bcfb90dee142 | -11.4393 | -45.1154 | 2025-07-09 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 186.0 |
| a19088da-6769-3341-a431-fbdb776b9b73 | -11.6737 | -43.7762 | 2025-07-09 02:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 46.7 |
| f22ddb9b-de75-3cbc-90e2-505a1eecd37f | -11.4397 | -45.0923 | 2025-07-09 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 155.4 |
| c34d91c9-f5f7-36c0-8cd7-758059bcf56b | -8.5028 | -43.2614 | 2025-07-09 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.2 |
| ebdbb9ad-e0e8-3ebb-bc56-16c1999c7968 | -11.4393 | -45.1154 | 2025-07-09 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 10807942-d23b-3c8e-8c52-31a547d639eb | -7.2408 | -43.0664 | 2025-07-09 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| ccbf8111-f0be-3334-8f32-91cfd0a307c8 | -8.5028 | -43.2614 | 2025-07-09 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.6 |
| 96e41e5f-7dfa-35e7-9f83-8288f7d2535a | -11.4584 | -45.1126 | 2025-07-09 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 92520f3b-f379-3e82-aaf5-344e252e53b5 | -8.5022 | -43.3085 | 2025-07-09 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 843d2f34-590f-35c8-8b3f-df7d20e5215f | -10.5776 | -49.1316 | 2025-07-09 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| ab1de427-ddfa-38c3-b639-0b5e103d114b | -8.5025 | -43.285 | 2025-07-09 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 257.3 |
| f2371bc2-9058-34fa-b280-445a9b174109 | -11.6737 | -43.7762 | 2025-07-09 02:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| b44dddfd-8813-3915-8b61-b4d3e22b4c72 | -11.4397 | -45.0923 | 2025-07-09 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 147.2 |
| cd39385f-a83e-342d-8e82-1bc881ab133b | -6.1606 | -48.0507 | 2025-07-09 02:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 7dc51e6d-79fe-3225-8a84-54ae845f555f | -8.5217 | -43.2593 | 2025-07-09 02:30:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| c99c3e6b-c967-352d-951e-ac90d58161d4 | -6.1792 | -48.0494 | 2025-07-09 02:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 28fbbbf1-bd67-305f-beb1-27bd2f2ccb75 | -11.4205 | -45.095 | 2025-07-09 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| ef101428-0000-328b-b8ac-78ffe331604c | -8.5211 | -43.3063 | 2025-07-09 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 129.8 |
| af73c530-e41b-3575-84f1-51fbf99065ce | -8.5214 | -43.2828 | 2025-07-09 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 271.3 |
| d36c7658-8aeb-3565-b667-90298428be1b | -11.4201 | -45.1181 | 2025-07-09 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 4baa7710-f626-3914-b39c-fac00909135f | -10.5776 | -49.1316 | 2025-07-09 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| ded58f04-a8c7-3d1f-8277-d97679e9aef3 | -7.2408 | -43.0664 | 2025-07-09 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 8700f2bb-92b6-39de-af56-461f59fdfdce | -8.5211 | -43.3063 | 2025-07-09 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 717b5512-1e3b-37d3-b9ab-9045fdadfa6c | -11.4201 | -45.1181 | 2025-07-09 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 87518add-d013-3336-bf2b-afa70b28d5e7 | -11.4584 | -45.1126 | 2025-07-09 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 137b30b5-da8c-367e-9f60-169f90bf24b8 | -8.5217 | -43.2593 | 2025-07-09 02:40:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 100.3 |
| 9b896fc6-e489-3a65-bf06-7ec73a0d8d75 | -6.1792 | -48.0494 | 2025-07-09 02:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 2f7e93d5-07fb-30f4-8a98-ddc8bdfe9085 | -8.5022 | -43.3085 | 2025-07-09 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 9d495f11-e406-39bc-923b-bcacb07df935 | -11.4205 | -45.095 | 2025-07-09 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| e7191b57-3917-3942-b424-57c7328c0eb3 | -6.1606 | -48.0507 | 2025-07-09 02:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 091f4482-29ed-3609-8e2c-d1c181f69b6f | -8.5214 | -43.2828 | 2025-07-09 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 248.2 |
| afb2457b-2d22-3bd1-93fc-afadbcfb43e9 | -8.5025 | -43.285 | 2025-07-09 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 254.5 |
| 5db8927c-3109-33f5-9fe2-691525598a27 | -11.4393 | -45.1154 | 2025-07-09 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 180.6 |
| 77049dbe-186b-31f4-bf19-b90c48d25f88 | -11.4397 | -45.0923 | 2025-07-09 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 0e5a3ed6-5006-361c-a707-7f7f5ca8a4d7 | -8.5028 | -43.2614 | 2025-07-09 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 134.5 |
| 4bc2c720-8d56-37bd-8e73-a538fbaf6348 | -8.5214 | -43.2828 | 2025-07-09 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 173.9 |
| dbbd4ee0-e9b4-3063-b874-fba5c994be27 | -10.5776 | -49.1316 | 2025-07-09 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |


[Clique aqui para ver as próximas entradas](README6.md)
