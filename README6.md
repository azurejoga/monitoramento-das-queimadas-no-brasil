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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 409d8346-acf5-381e-85cf-0af78c22e1eb | -20.3085 | -57.32584 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 7862bff3-3e11-338f-b827-05a7517535fa | -19.43931 | -54.77555 | 2026-01-31 05:08:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64a27e70-52d8-392b-96b3-07934dcddac0 | -20.29414 | -57.30816 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fcc6266-3aec-357b-bfbe-98a59414a453 | -19.47119 | -55.46428 | 2026-01-31 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e5915a54-2100-3c36-8f2f-cf04a29d14ec | -20.30517 | -57.32525 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 489513c9-7b44-3d31-9e4f-bc38dc44a992 | -20.29271 | -57.36103 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3a58e0b2-75ce-37ac-9ce7-76f5a49cbbfe | -20.2972 | -57.35423 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72fabe6d-cf4a-3b84-b0ee-aebe185e2956 | -20.30054 | -57.35481 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86d3efb2-014c-375a-9a78-da319a3c9673 | -20.31548 | -57.36884 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 30dc32f2-8348-30e0-929e-01ba88a61de8 | -19.47463 | -55.46485 | 2026-01-31 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| c38c044b-da2b-3b82-a9b2-5da31b5dc333 | -20.31606 | -57.36514 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1bea0f54-8153-3953-b82f-6879e133af76 | -20.31098 | -57.37564 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| d71d075b-423e-3bbd-b997-3161669ecd4a | -20.32215 | -57.37001 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a136266c-4684-3ebe-a9ac-018599529444 | -20.31214 | -57.36825 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a6779c9a-58ff-3f85-a74d-d0e06d4238e9 | -20.26452 | -57.32945 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66f74a7e-631c-320a-8cd3-12b17f30a775 | -20.29134 | -57.31144 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 359d8804-bbba-343d-bb3d-9179339c18c9 | -23.27709 | -50.31287 | 2026-01-31 05:08:00 | NPP-375D | ABATIÁ | PARANÁ | Brasil | 4100103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c5cb4adb-a6fd-3cfc-9ed2-697958407658 | -19.86499 | -55.50837 | 2026-01-31 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 750750ff-5dfb-3e4b-bc89-1ef42c094214 | -20.30489 | -57.37077 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 33e3d28e-8036-3802-bb4f-7c6ce02e834c | -20.31939 | -57.36573 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b7b89e3e-ac5f-351d-86e2-734d4e34a93c | -20.28628 | -57.32189 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b7f3850-2a7c-3f14-96c6-08c25e8b7ea5 | -20.30459 | -57.32895 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 6555a969-b1b4-3523-8057-92b46ea41829 | -19.43578 | -54.775 | 2026-01-31 05:08:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25ced319-ec77-34b3-9615-1996e92c87bd | -20.26509 | -57.32578 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4b23af8-07bc-323d-9d49-9845d4b37f8e | -20.31881 | -57.36942 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f4c0c159-9fcc-3115-a207-ef6b98746b92 | -20.32273 | -57.36631 | 2026-01-31 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6ae36565-fa65-3d3e-8f5e-ba653549e4be | -1.8058 | -54.4923 | 2026-01-31 05:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 50a15200-2f23-3371-a649-a4f726f4f2fa | -26.26962 | -52.71424 | 2026-01-31 05:10:00 | NPP-375D | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 096d0a38-cdc7-3cb0-9c00-2537062e7e3b | -26.26535 | -52.71357 | 2026-01-31 05:10:00 | NPP-375D | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 5d6eff8f-31ab-321e-90f3-d75bed30543c | -1.8058 | -54.4923 | 2026-01-31 05:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 2e7c1418-5ef2-32db-a3d6-569476a227ec | -4.36783 | -55.76979 | 2026-01-31 05:22:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4570a6c3-de9f-35d6-8325-3a6e36b28b7b | 4.17071 | -61.05293 | 2026-01-31 05:22:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc32bf59-a95f-30f0-a928-bfb30adfed61 | 1.42382 | -60.79991 | 2026-01-31 05:22:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e1b8645-6a47-3486-8cc0-40b00f9ab552 | -10.71923 | -59.22741 | 2026-01-31 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 66249f08-4464-3a1f-a105-efe865373a0f | -11.00281 | -54.00152 | 2026-01-31 05:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c63a17e-8f41-37c8-ad96-9d74aa7d4e69 | -10.7233 | -59.22402 | 2026-01-31 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f13f40a-7d5a-3bb1-b97c-65f003517957 | -10.32225 | -59.05363 | 2026-01-31 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7681e4f6-0869-37ff-89f8-c08637371ce5 | -11.95037 | -58.74226 | 2026-01-31 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e32dce0-cf71-3cd2-b4ea-65d74695565f | -12.818 | -62.16223 | 2026-01-31 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 93550cc3-2514-3e66-b0ed-1e613319b94a | -11.951 | -58.738 | 2026-01-31 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6975f513-ac7b-31dd-a244-2b5461d1ce50 | -12.30211 | -57.36736 | 2026-01-31 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 261a1a78-c697-3bee-b6d0-8a02cb076215 | -11.95397 | -58.74283 | 2026-01-31 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc9acf52-3544-3b21-8e38-571f33795f78 | -12.29076 | -57.39159 | 2026-01-31 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdc89538-feff-3ff1-9314-ba52acb48457 | -12.29721 | -57.40276 | 2026-01-31 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00746aff-56a3-3817-b8eb-50992bb1ca45 | -12.80145 | -62.15952 | 2026-01-31 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 351edf59-28af-3fb7-998a-5f245462228f | -12.30674 | -57.36285 | 2026-01-31 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43722f1a-6276-3fe4-a971-b4422745148d | -12.43631 | -58.03567 | 2026-01-31 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ea48297d-cd9c-3002-8d98-12d0659d3910 | -12.29749 | -57.37186 | 2026-01-31 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35b53c6a-dafe-37e0-90e8-7a46a0928d10 | -10.71981 | -59.22346 | 2026-01-31 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96243f5b-95e2-3cdb-ad47-8bdadecfada4 | -11.17757 | -55.9176 | 2026-01-31 05:25:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d505ad8-6714-355b-9faf-9ea904e37dd1 | -12.30604 | -57.36794 | 2026-01-31 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e30d3a46-e03d-34f3-80dd-0741473d2382 | -12.29329 | -57.40219 | 2026-01-31 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 329cac1c-3bb7-315e-b8f6-41a90c129768 | -1.80876 | -54.48951 | 2026-01-31 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 17f0042d-be80-3bfc-a82f-82116600aa6e | -3.63162 | -51.94498 | 2026-01-31 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a20e7bd1-f62c-3978-8021-3378d187697a | -1.80524 | -54.4853 | 2026-01-31 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4d921e0c-67e4-3065-a3e7-ee3b23949288 | -1.81283 | -54.49015 | 2026-01-31 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27c1fff7-8c17-378f-939a-6da963b1f145 | -2.57997 | -54.72395 | 2026-01-31 05:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38909541-5e01-3f69-a3d8-383fc2f4f25f | -2.57942 | -54.7275 | 2026-01-31 05:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b37109c-f2bb-3b59-b0ce-74a974937d10 | -1.80416 | -54.49244 | 2026-01-31 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| ae747462-3064-3d34-a05d-5b1bf2adc936 | -1.80361 | -54.49599 | 2026-01-31 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b08d4f7d-b609-3c0c-9202-38138f013a6e | -1.80009 | -54.49182 | 2026-01-31 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 081905ee-e960-381b-b29d-5a4d3c2e62bb | -1.8047 | -54.48887 | 2026-01-31 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 4ad9878f-f7da-3725-9145-578550418f40 | -1.80931 | -54.48594 | 2026-01-31 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4bb7d00c-ef28-30fb-9010-25d56be0f4f5 | -1.8169 | -54.49075 | 2026-01-31 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19e8e95e-cd44-34ff-b98e-0bf2442877b2 | -1.80062 | -54.4883 | 2026-01-31 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 327ea7df-c246-31ab-b9cc-10c798c234c1 | -1.80117 | -54.48471 | 2026-01-31 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2b4462c-0f55-32cb-bae2-a44c817b697e | -19.47056 | -55.46289 | 2026-01-31 05:27:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 25e0616e-bdf2-3bf8-9bdf-29916fe01b02 | -15.26726 | -60.41302 | 2026-01-31 05:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 828c796b-50ca-32d4-a545-4b9cfe7841a7 | -16.58269 | -57.80463 | 2026-01-31 05:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| ed61a46f-51de-31f2-aa69-08f4c2659bbb | -19.47482 | -55.46925 | 2026-01-31 05:27:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1ce7f9a0-7710-3348-9f6b-997178492406 | -16.57865 | -57.80401 | 2026-01-31 05:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 8e4934cb-9bb4-3406-9feb-5475955103b6 | -16.25417 | -60.03004 | 2026-01-31 05:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59f33ad5-cd95-3775-b128-c569a55574b9 | -15.02854 | -59.6757 | 2026-01-31 05:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f2b439e-39ac-3c0e-9545-44c16d0f0d2f | -16.58625 | -57.80885 | 2026-01-31 05:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 78ca424a-551f-3221-b752-95498c452ac4 | -16.57816 | -57.80764 | 2026-01-31 05:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 79328ea6-e88a-304a-b5b9-368a8a030234 | -19.86197 | -55.50985 | 2026-01-31 05:27:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41236f3a-2bbc-30a3-ba9f-3160e3756e19 | -15.79538 | -59.687 | 2026-01-31 05:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ad483e9-22dc-3852-92c4-7cd324cfe66c | -16.58221 | -57.80825 | 2026-01-31 05:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 83bef34e-792b-379f-bc02-e5c288a7158a | -26.2683 | -52.7114 | 2026-01-31 05:29:00 | NOAA-20 | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 32b99167-2b88-3628-8ed8-d72efb1166e6 | -26.26794 | -52.71656 | 2026-01-31 05:29:00 | NOAA-20 | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 6098ebad-7b50-3769-beba-8599e50ed2eb | -1.8058 | -54.4923 | 2026-01-31 05:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 7ab559f3-2fa5-3595-8b49-f772db4307a2 | -1.8058 | -54.4923 | 2026-01-31 05:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 19cebfaa-69e8-3d06-9fb2-9552bc34c70d | -1.8058 | -54.4923 | 2026-01-31 05:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 096c12d8-59b5-3fa9-bb9b-f927ce125689 | -1.8058 | -54.4923 | 2026-01-31 06:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 0afbe72f-8237-3ca5-8519-874689c4daef | -1.8058 | -54.4923 | 2026-01-31 06:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| b11d1e47-f3a0-3b43-8918-5f4ae8782010 | -1.8058 | -54.4923 | 2026-01-31 06:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| f17605b2-1282-35a1-be50-4d243e84d05a | -1.8042 | -54.49315 | 2026-01-31 06:26:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 8a45c01c-c19d-36dd-b726-b4265c16568c | -1.80651 | -54.47824 | 2026-01-31 06:26:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| d09f081a-f34c-3999-a74a-15f67ce81a84 | -26.47069 | -49.02415 | 2026-01-31 06:33:00 | AQUA_M-M | GUARAMIRIM | SANTA CATARINA | Brasil | 4206504 | 42 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| de24f327-647b-3398-8ad6-54d5922e671f | -26.26328 | -52.70694 | 2026-01-31 06:33:00 | AQUA_M-M | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 87c811dd-50f9-3981-9982-589540ac7d76 | -26.47277 | -49.00479 | 2026-01-31 06:33:00 | AQUA_M-M | GUARAMIRIM | SANTA CATARINA | Brasil | 4206504 | 42 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 134645f8-9d7f-37eb-8d9a-d753486f37cd | -1.8058 | -54.4923 | 2026-01-31 07:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 66a53edd-c9e8-3e03-85f2-d38cea16f009 | -8.67852 | -39.39706 | 2026-01-31 11:34:00 | TERRA_M-M | ABARÉ | BAHIA | Brasil | 2900207 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 38a13801-612f-3b57-92ba-722bd393297b | -3.90811 | -38.83461 | 2026-01-31 11:34:00 | TERRA_M-M | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| a3617623-a342-39cf-8b2e-83b6013cc021 | -8.65352 | -39.25792 | 2026-01-31 11:34:00 | TERRA_M-M | ABARÉ | BAHIA | Brasil | 2900207 | 29 | 33 | nan | nan | nan | Caatinga | 14.7 |
| de1239a4-10af-355c-842f-ba3d33e29c87 | -8.65225 | -39.26678 | 2026-01-31 11:34:00 | TERRA_M-M | ABARÉ | BAHIA | Brasil | 2900207 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| bfd65bcf-9c9f-390a-9b94-d9dbb66fdfbc | -6.08967 | -38.79702 | 2026-01-31 11:34:00 | TERRA_M-M | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 59e6e40f-af40-3d9d-9d21-7c1c25685d31 | -5.3965 | -36.7965 | 2026-01-31 11:34:00 | TERRA_M-M | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 46.9 |
| c363d22a-9dba-38d2-b856-0b1a585e8eae | -8.6798 | -39.3882 | 2026-01-31 11:34:00 | TERRA_M-M | ABARÉ | BAHIA | Brasil | 2900207 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 955acda8-3655-3ebd-b713-fb4cc9188c25 | -10.56829 | -38.95238 | 2026-01-31 11:34:00 | TERRA_M-M | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |


[Clique aqui para ver as próximas entradas](README7.md)
