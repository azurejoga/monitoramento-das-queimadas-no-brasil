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
| 579e07f1-6afe-3e71-abbe-5905951418fe | -3.42831 | -42.09551 | 2025-11-28 12:16:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 94e8fbc8-5d4b-3928-832e-805133389be4 | -4.41926 | -47.83742 | 2025-11-28 12:16:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f86e958f-667a-3d74-8c20-4252f65d98fc | -3.38666 | -42.39954 | 2025-11-28 12:16:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 13.6 |
| b7b4c0c8-295b-303f-99b8-beaf47096f5a | -3.60117 | -44.83563 | 2025-11-28 12:16:00 | TERRA_M-T | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 14b3d133-8cd0-3c67-8a22-d41e496dd703 | -6.4676 | -38.86877 | 2025-11-28 12:16:00 | TERRA_M-T | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 99.4 |
| fe4a1f02-9055-3a0e-b3cf-9eb78a4e3ce9 | -4.17171 | -43.76293 | 2025-11-28 12:16:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 954cdb23-f2e9-376e-a41b-492d84a77366 | -3.19045 | -44.40658 | 2025-11-28 12:16:00 | TERRA_M-T | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 3055fd91-d027-3f4b-82b6-d438dd37674b | -3.52946 | -43.6719 | 2025-11-28 12:16:00 | TERRA_M-T | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 291.0 |
| a4a2cb91-42e9-327e-b066-c91121761a34 | -8.16551 | -43.20786 | 2025-11-28 12:16:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 79459194-d188-3c0c-9c27-69a4d31c8718 | -3.39576 | -44.18122 | 2025-11-28 12:16:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| a07ef8da-e188-30d0-9bb3-c1c92fec9e88 | -3.69863 | -43.47209 | 2025-11-28 12:16:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7b33a7a3-e7e0-3e56-9c3e-727d0d29cdc9 | -3.70663 | -41.85211 | 2025-11-28 12:16:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 84267561-7116-304e-a50d-e3d5484cb405 | -4.17351 | -43.75027 | 2025-11-28 12:16:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| f6cf131b-bc6f-3d23-9327-7cbf557b3004 | -3.50861 | -43.66909 | 2025-11-28 12:16:00 | TERRA_M-T | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 05c0aa2b-40e9-327b-9eb1-ef2f0613e782 | -2.69606 | -49.5559 | 2025-11-28 12:16:00 | TERRA_M-T | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| c5bb49d6-9d57-3413-8724-ea0754e5f615 | -6.72412 | -40.82014 | 2025-11-28 12:16:00 | TERRA_M-T | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 40.7 |
| 0d7b7671-6c3e-30bf-8cdc-18268db1a175 | -16.64816 | -49.93751 | 2025-11-28 12:18:00 | TERRA_M-T | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 41fcd4d8-d316-3935-9390-bd8c4b9159a1 | -3.1878 | -44.4096 | 2025-11-28 12:20:00 | GOES-19 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 3d1f0cbe-f674-34f2-a94e-9478a73bf4bc | -17.90316 | -48.79054 | 2025-11-28 12:21:00 | TERRA_M-T | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1de15f6d-94b2-34c1-8938-e678edc50dcd | -18.85507 | -53.57672 | 2025-11-28 12:21:00 | TERRA_M-T | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8a3c8577-94ec-3cd2-88a1-ff18133fbaed | -18.26727 | -50.74229 | 2025-11-28 12:21:00 | TERRA_M-T | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5b8213e1-e6c5-3127-b47d-90321088be16 | -20.57642 | -49.50556 | 2025-11-28 12:21:00 | TERRA_M-T | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f4c66556-ba11-322a-b9f4-9dc23a342d1a | -18.31563 | -51.73465 | 2025-11-28 12:21:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| e54e1499-e4e4-3b6f-ada2-95a2578a6d67 | -17.41118 | -49.22619 | 2025-11-28 12:21:00 | TERRA_M-T | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 18d4d6ac-684c-3379-8540-39b1cd44c187 | -17.40983 | -49.23587 | 2025-11-28 12:21:00 | TERRA_M-T | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d72641eb-c7d0-3710-9952-9441894ce40c | -19.98668 | -49.98737 | 2025-11-28 12:21:00 | TERRA_M-T | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| d0fc2769-3a63-3a88-abf9-b61e1b5912d8 | -25.12061 | -52.27032 | 2025-11-28 12:23:00 | TERRA_M-T | MARQUINHO | PARANÁ | Brasil | 4115457 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| fb516908-9a1b-3abb-8115-d4bf9a0cd385 | -23.11897 | -52.08271 | 2025-11-28 12:23:00 | TERRA_M-T | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 27243dd9-68f7-3ebb-931e-b20b0840c4a7 | -25.29112 | -51.51073 | 2025-11-28 12:23:00 | TERRA_M-T | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| f12871ba-d353-37f5-bbf8-78291b595230 | -23.46155 | -47.04655 | 2025-11-28 12:23:00 | TERRA_M-T | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 5ac0f074-6ee0-3283-ab91-1559eb179c02 | -25.49806 | -49.08022 | 2025-11-28 12:23:00 | TERRA_M-T | PIRAQUARA | PARANÁ | Brasil | 4119509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| a713170b-b358-35b5-8b31-4ecc09be2394 | -23.42946 | -47.13315 | 2025-11-28 12:23:00 | TERRA_M-T | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| 4d9888d8-c1ec-3890-8df0-07db55ce8e8c | -25.49955 | -49.06802 | 2025-11-28 12:23:00 | TERRA_M-T | PIRAQUARA | PARANÁ | Brasil | 4119509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 86c7c969-51e8-344f-9e63-e7e8451467bb | -26.64125 | -52.32906 | 2025-11-28 12:23:00 | TERRA_M-T | ABELARDO LUZ | SANTA CATARINA | Brasil | 4200101 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| eb30249e-1d2f-3e89-beab-914f5b5fbda0 | -25.61038 | -49.17051 | 2025-11-28 12:23:00 | TERRA_M-T | SÃO JOSÉ DOS PINHAIS | PARANÁ | Brasil | 4125506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| f2507aab-3465-3bcd-88c2-220528a1dd9b | -27.11497 | -50.73651 | 2025-11-28 12:23:00 | TERRA_M-T | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 834d4b36-d724-3e71-93a5-ea71885b858c | -29.03137 | -51.17708 | 2025-11-28 12:25:00 | TERRA_M-T | FLORES DA CUNHA | RIO GRANDE DO SUL | Brasil | 4308201 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| abbc0712-4dbd-36e7-9ed8-d2ea8d8a3203 | -30.28797 | -51.98006 | 2025-11-28 12:25:00 | TERRA_M-T | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 6.4 |
| 5f0bf398-fd5b-3d01-b37a-3ad6c0ae56fe | -28.93402 | -51.09277 | 2025-11-28 12:25:00 | TERRA_M-T | SÃO MARCOS | RIO GRANDE DO SUL | Brasil | 4319000 | 43 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| e6a19d5b-6b89-356f-9626-12ac32255ec2 | -30.28656 | -51.99073 | 2025-11-28 12:25:00 | TERRA_M-T | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 12.7 |
| 40dfa63e-79a3-3eca-b294-c0d34cf80d53 | -29.7501 | -51.52074 | 2025-11-28 12:25:00 | TERRA_M-T | MONTENEGRO | RIO GRANDE DO SUL | Brasil | 4312401 | 43 | 33 | nan | nan | nan | Pampa | 13.3 |
| ebba0f48-d576-3399-94c8-b0b7ff454a21 | -29.61317 | -51.7244 | 2025-11-28 12:25:00 | TERRA_M-T | PAVERAMA | RIO GRANDE DO SUL | Brasil | 4314159 | 43 | 33 | nan | nan | nan | Pampa | 5.9 |
| 02269d40-60c2-36d3-a368-35eeb7853cdb | -3.1878 | -44.4096 | 2025-11-28 12:30:00 | GOES-19 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 105.5 |
| f1b85cf0-dfd9-3093-8b2b-e3c6b57f66a1 | -3.2064 | -44.4089 | 2025-11-28 12:30:00 | GOES-19 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 523d50f7-3374-38ad-bb4a-53f2181c1653 | -6.7199 | -40.8188 | 2025-11-28 12:30:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| dbe68569-9549-3630-aa68-324bc723b577 | -6.7199 | -40.8188 | 2025-11-28 12:40:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 101.5 |
| 349474b5-0c04-3715-97b6-6eb32e932695 | -3.1878 | -44.4096 | 2025-11-28 12:40:00 | GOES-19 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 471498bd-c092-3930-b052-1906fa34f031 | -6.7199 | -40.8188 | 2025-11-28 12:50:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 123.1 |
| 053ef257-b19c-39cc-949a-5c4b3f20350f | -3.3285 | -42.4311 | 2025-11-28 12:50:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| b80aab5c-4256-38e0-b947-a7b3dafd4821 | -3.5083 | -43.6837 | 2025-11-28 12:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 569c9559-74d3-3237-a05e-39aa24df4614 | -6.4775 | -38.8795 | 2025-11-28 12:50:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 132.1 |
| 10103608-7c69-3c01-84dc-160a86da660b | -6.4586 | -38.8815 | 2025-11-28 12:50:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 113.5 |
| 8154d539-409a-3d42-b365-b44ed23ceac6 | -6.7199 | -40.8188 | 2025-11-28 13:00:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |
| be388e43-1bab-38f2-a4f7-b10db8dddc1f | -6.7199 | -40.8188 | 2025-11-28 13:10:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 138.1 |
| 70dd471b-f7f7-3afe-97ff-d1c5c13f658c | -3.5023 | -41.4467 | 2025-11-28 13:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 86.4 |
| 60041ba3-badb-3a37-b446-714631eddb9a | -2.6919 | -47.4153 | 2025-11-28 13:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| eefc5eda-4c50-3c72-9504-992a87c71059 | -2.7104 | -47.4147 | 2025-11-28 13:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 47c73887-ec23-3c59-98cf-daeff7506b21 | -6.8847 | -38.0949 | 2025-11-28 13:10:00 | GOES-19 | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 93.1 |
| 023d74dc-03c3-3a72-b214-9744df90f141 | -6.7199 | -40.8188 | 2025-11-28 13:20:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 124.2 |
| 662913b5-f86c-3d06-aab4-0fa5421655a1 | -2.6919 | -47.4153 | 2025-11-28 13:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 137.8 |
| c6291912-5948-3b21-b4dc-f1ee4ebaaaf9 | -2.7104 | -47.4147 | 2025-11-28 13:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| aa09e0c6-6836-33d3-b8c6-2e09684942d7 | -3.5083 | -43.6837 | 2025-11-28 13:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 117.8 |
| f09fddfb-fbf7-3bf5-9d1d-46723daf9338 | -6.6711 | -40.1357 | 2025-11-28 13:20:00 | GOES-19 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 92.2 |
| ba212564-bdcc-3895-aebe-e7cd59d84dc0 | -3.0695 | -41.9451 | 2025-11-28 13:30:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 1a283412-c0c2-32dc-8392-b0cb482c4079 | -6.0906 | -37.9484 | 2025-11-28 13:30:00 | GOES-19 | MARTINS | RIO GRANDE DO NORTE | Brasil | 2407401 | 24 | 33 | nan | nan | nan | Caatinga | 92.2 |
| 91ea8954-6e3a-3801-9114-7a949a0e6811 | -2.9937 | -42.162 | 2025-11-28 13:30:00 | GOES-19 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 95da0508-db37-32fe-a9bd-f5be5e07039e | -19.0522 | -57.5148 | 2025-11-28 13:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 80.3 |
| 8d2626eb-798f-3be5-8c8e-731fb3567384 | -19.2147 | -57.3483 | 2025-11-28 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.6 |
| 7ae20833-3c23-359e-9923-e96ece9dcb6b | -6.5154 | -38.8756 | 2025-11-28 13:30:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 144.6 |
| fbad0815-fc6c-379c-99c4-1e891075c9b5 | -4.9472 | -41.1895 | 2025-11-28 13:30:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| bd202afe-334f-3677-8f6c-f4e8bec15c52 | -3.5956 | -41.4899 | 2025-11-28 13:30:00 | GOES-19 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 124.3 |
| a8b925fb-a604-3638-8742-69283e9ff76d | -3.0508 | -41.9459 | 2025-11-28 13:30:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 65495ab2-f82c-30b5-b676-0c10b2b6379b | -6.7199 | -40.8188 | 2025-11-28 13:30:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 115.2 |
| 08aa7668-d770-39fb-b2b6-8fd327a962a2 | -19.2347 | -57.3456 | 2025-11-28 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.1 |
| e9a8231b-f5a6-39ea-ab39-5b7cb0f82738 | -3.5269 | -43.6828 | 2025-11-28 13:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 259.8 |
| e4699752-a3b7-391e-9892-39a3a534b8bd | -3.0695 | -41.9451 | 2025-11-28 13:40:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| bf559ee2-2b06-3ab3-b1bd-3f92a7e7c1f4 | -6.7199 | -40.8188 | 2025-11-28 13:40:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 129.7 |
| 8115e28a-80b6-3f09-ade8-1b313f47ff5e | -3.5271 | -43.6597 | 2025-11-28 13:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 342e60b2-2975-32ed-842a-ef085abc49fb | -2.9937 | -42.162 | 2025-11-28 13:40:00 | GOES-19 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| b699bdda-be1c-3b25-95e3-5a1f89968154 | -6.4778 | -38.8542 | 2025-11-28 13:40:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 143.4 |
| 6a1a60ec-9ed3-3c87-b823-9fec81465ad8 | -19.0522 | -57.5148 | 2025-11-28 13:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 79.4 |
| 9e8c5e76-c88a-3e35-9999-b1ebdd95c110 | -3.5083 | -43.6837 | 2025-11-28 13:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| d97ff6a5-e8e8-389f-b865-89863cbc8955 | -4.9472 | -41.1895 | 2025-11-28 13:40:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 107.8 |
| d2d48d9b-f20a-3e89-bcf2-3b0be7d2250f | -4.9472 | -41.1895 | 2025-11-28 13:50:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 112.7 |
| 9d84d08b-f275-3bc5-a1a9-460eb8d8f6e0 | -19.0522 | -57.5148 | 2025-11-28 13:50:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 79.0 |
| adc227d3-ecd8-3425-af8f-f67d279b125e | -20.4076 | -57.9577 | 2025-11-28 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 13489dda-ac5c-36b9-9f88-4553cf0ba327 | -3.5271 | -43.6597 | 2025-11-28 13:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 38e5bde2-f444-3544-8a44-3eb546cd4f24 | -3.5083 | -43.6837 | 2025-11-28 13:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 3be103d4-54a6-3bd0-a369-4a2a30611ca1 | -20.408 | -57.9368 | 2025-11-28 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.1 |
| bc9a735f-db84-3052-8885-f99fd034d608 | -5.3041 | -41.187 | 2025-11-28 13:50:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 152.7 |
| ccd02ab7-05b0-375e-80f7-d09924410e7b | -3.5269 | -43.6828 | 2025-11-28 13:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 226.6 |
| e2e6b158-bbf1-3d9e-a2b7-e269eb838589 | -4.966 | -41.1881 | 2025-11-28 13:50:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 106.9 |
| 3413da7d-bbde-3c58-9729-42a25a02cccb | -19.2347 | -57.3456 | 2025-11-28 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.0 |
| db1d0d4c-ead4-3e75-bf13-94bb63f68e93 | -19.2151 | -57.3275 | 2025-11-28 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.2 |
| f2ce678d-0b61-3075-9213-b0e9c6c6cff3 | -2.9563 | -42.1636 | 2025-11-28 14:00:00 | GOES-19 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| a274f738-9cea-3bb1-b115-1de46d35f6bf | -3.8709 | -42.3567 | 2025-11-28 14:00:00 | GOES-19 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| 696f03fa-c6d5-32ce-a9f6-cddd7bb7de2a | -19.2343 | -57.3665 | 2025-11-28 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.4 |
| c66877b0-68b0-3aeb-a95d-eb3f84dfd24f | -19.2147 | -57.3483 | 2025-11-28 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.4 |
| c52e9e4e-7e1b-3fc1-9b25-4c816e76918a | -4.9474 | -41.1653 | 2025-11-28 14:00:00 | GOES-19 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 118.5 |
| 226d8170-56fe-3df0-ae03-0bac8b265bba | -4.3872 | -43.406 | 2025-11-28 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |


[Clique aqui para ver as próximas entradas](README25.md)
