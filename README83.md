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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3499674-f768-3c8e-be3e-6fb7b28e452b | -8.4926 | -55.18863 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a76fe9f-b135-3508-946f-2a20c5be55d5 | -8.48946 | -55.03539 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 792ad759-f43e-30a3-b822-4b186dce603c | -8.41062 | -55.0545 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 77938651-47e8-32fe-80f7-e05e6b04957f | -8.40963 | -55.03568 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f5ae4e71-e520-3451-9341-cbd1496aa935 | -8.40743 | -55.02412 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 984495e9-97ce-32af-a106-317e043af3f7 | -8.40621 | -55.03131 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 76c2fb37-f811-3928-8857-98950ce85409 | -8.3564 | -55.07885 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dbae2b75-642a-34a1-a8c9-abd3b9df9290 | -8.32477 | -55.01767 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89aea302-921e-3cc5-baac-b4245a97b322 | -8.32416 | -55.02127 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65ee817e-7794-39cf-bb92-fdc988e64d0a | -8.31851 | -55.00539 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c502b300-9e7d-34d2-8736-c7019e3a2651 | -8.3179 | -55.00902 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ebfd0339-a159-310e-b668-8c8a2986a1c3 | -8.31506 | -55.00115 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c12f87b-06fd-3c5a-8312-340b205cfd9c | -8.31446 | -55.00474 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ad1a553-44a9-3722-8f55-957829f171d0 | -8.31385 | -55.00835 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4bb57e88-e589-387a-a80a-0354ca47e1bd | -8.31324 | -55.01196 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5da08901-6975-3b94-8680-924f2932534e | -8.31102 | -55.00047 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0a41084a-5475-3c5c-91eb-d576431f16a6 | -8.31042 | -55.00406 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| de998ec6-34b0-3f55-b712-911ca7a63e58 | -8.3098 | -55.00768 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 56e4dd01-d813-3cd8-b515-d275fa0813f6 | -8.2985 | -55.38936 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2271e612-fb4d-318f-8612-3f6354509a5a | -8.29783 | -55.3932 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f6b0f46-51e3-3ccf-8943-f639e87cab27 | -8.29435 | -55.38868 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bb36b30e-607f-314d-9b60-0dc05aa270b1 | -8.29368 | -55.39251 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3efa257-964c-31b9-84b0-0a3fa2e1f65c | -8.28953 | -55.39181 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f4292e5-e5b8-3e4f-81fb-adb1ede5604d | -10.75693 | -56.363 | 2024-09-27 04:40:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90014f43-01ed-3cf7-9aca-fca6b9285fd2 | -10.75621 | -56.36708 | 2024-09-27 04:40:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7670c1f-e1f1-3ac3-9e6f-dcc254b2a5c3 | -10.75549 | -56.37114 | 2024-09-27 04:40:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2d255841-e520-3be8-ba61-078cc4cd53ed | -11.88863 | -57.03155 | 2024-09-27 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86ae3e18-0dae-397d-b17b-d66fbb983893 | -11.84882 | -56.87944 | 2024-09-27 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cb038dd-3a77-32d2-be52-6ecea59835e3 | -7.68701 | -56.96185 | 2024-09-27 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac78fa4a-2740-3617-b573-05cb3b484fa5 | -7.68364 | -56.964 | 2024-09-27 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 16509523-9572-3f61-ae8b-fdc6b71524bf | -7.68236 | -56.96104 | 2024-09-27 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 704deb7a-ec67-3e92-a8f1-85d97d2845a1 | -7.68147 | -56.96603 | 2024-09-27 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 807f498b-cfa9-3d91-b835-86093e247e0d | -7.67982 | -56.95827 | 2024-09-27 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d903458-e030-363b-bde0-0111d19f4009 | -7.67898 | -56.96316 | 2024-09-27 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ba7d3fc-2d31-37ac-8eaf-0edeaa70492f | -7.96661 | -56.6904 | 2024-09-27 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f4adf81-8af5-32f9-9695-fb92929c1b8a | -7.8902 | -57.23155 | 2024-09-27 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d8fb8415-0195-336e-bb61-fe9fa537001f | -8.33195 | -56.49332 | 2024-09-27 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd3abdfd-96e8-3442-bac7-f184fdcfb1d5 | -8.32749 | -56.49251 | 2024-09-27 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 46ee63cd-34a2-32ba-8867-2a0995117cec | -8.3267 | -56.49702 | 2024-09-27 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b74ab95d-6a69-31c3-9c00-cf66466297f8 | -8.32144 | -56.50076 | 2024-09-27 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a53e990f-1e5f-3b80-8f68-cc726e97c0ef | -8.31698 | -56.49997 | 2024-09-27 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 577c484d-bbd3-32c0-873a-27e8e75ffa4d | -8.31252 | -56.49916 | 2024-09-27 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a5ed9b9b-ce03-3a7d-b719-7ea76ed9153b | -10.86251 | -57.43169 | 2024-09-27 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f40c8d23-cb40-3d9f-89a5-a8fc6ab4d36e | -10.8617 | -57.43628 | 2024-09-27 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5de9db71-f989-31d4-ba54-c445b35e562f | -10.63538 | -57.43566 | 2024-09-27 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cfa7e59-d939-38ce-a48f-e1eb5e3d76f5 | -10.63475 | -57.43794 | 2024-09-27 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 77273381-9a22-33c4-8cdf-f536014df823 | -10.6317 | -57.43005 | 2024-09-27 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb62cd86-f50d-30fb-9abe-e04f76be2736 | -6.82638 | -59.04395 | 2024-09-27 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39ab11f2-068e-3fa1-be45-e481a72b3e5a | -6.76 | -58.90356 | 2024-09-27 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 979c4d07-0220-337d-94ed-0ad0ce719050 | -6.7594 | -58.907 | 2024-09-27 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86fe9299-dfba-34b9-9e11-f75461593042 | -9.91004 | -59.45576 | 2024-09-27 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f1e2509-89ea-3589-9264-6531ee181183 | -9.9094 | -59.45926 | 2024-09-27 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d33e976b-130d-33d2-b222-8152717f254c | -9.67077 | -59.07653 | 2024-09-27 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b0b0d120-9b70-396c-bc12-741eafa9bfbc | -9.6656 | -59.07549 | 2024-09-27 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8dbc07f3-44a3-3210-9b4d-1e3ef5f7600a | -6.8986 | -59.65073 | 2024-09-27 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ed8fb9f-ab15-39a2-ab67-0e5df8b5c1e7 | -6.89792 | -59.65445 | 2024-09-27 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14fec1e8-6a21-3081-81f7-1f55568887e3 | -6.89363 | -59.64598 | 2024-09-27 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2dd35912-1f64-35c6-bfb2-987071eb66af | -6.89295 | -59.6497 | 2024-09-27 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6e8b997-d116-3746-be9b-f32b5757f8b5 | -6.89227 | -59.65343 | 2024-09-27 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cff43661-47f9-3f27-883d-36e979d4d30d | -6.8115 | -59.45016 | 2024-09-27 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 350bc673-3f28-3732-9cc7-e1ff306d92f7 | -6.79689 | -59.30532 | 2024-09-27 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d9476a3-b203-3ee0-9e30-996b4c51f342 | -6.79623 | -59.30902 | 2024-09-27 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61411f75-f2bd-3276-9bec-d433685210da | -6.79557 | -59.31274 | 2024-09-27 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c281fa1f-7a5f-3d88-a663-db04ebecf240 | -6.79068 | -59.30811 | 2024-09-27 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d162236-0baa-3b8c-b2ee-91bbfac2906b | -6.79002 | -59.31182 | 2024-09-27 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14bd09ef-59ee-3bca-9829-4dc881e71eca | -6.78936 | -59.31552 | 2024-09-27 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20d15bb4-3856-3e11-8929-774bee098c04 | -6.7877 | -59.35709 | 2024-09-27 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 841bf917-cdfb-3272-9f91-0569ba5b960d | -6.78704 | -59.3608 | 2024-09-27 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ba96522-2b46-38fa-a7a8-cab98b4bd6a0 | -6.78637 | -59.36457 | 2024-09-27 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56f4ea8c-7250-3d70-94bf-0883f779e382 | -7.09406 | -59.76269 | 2024-09-27 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c68013a-88ae-3bae-a9c8-45817a869eca | -6.98934 | -59.59887 | 2024-09-27 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fb260b2-ca53-3237-a065-4e4985a939a3 | -10.68736 | -60.73545 | 2024-09-27 04:40:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc3b3891-a1ca-3a03-aa81-449ad490c144 | -10.68658 | -60.73943 | 2024-09-27 04:40:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e1a0296-31fb-3acb-b057-46dc8413b79b | -8.00247 | -61.21915 | 2024-09-27 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5932105c-73c7-33ed-af93-dca087c9d07c | -8.00234 | -61.21944 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 35e4848d-876c-34e9-8092-4f549af21edd | -7.99637 | -61.2179 | 2024-09-27 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 773e6590-aa4d-38c5-8e32-559239cdd79c | -7.99624 | -61.21817 | 2024-09-27 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8688c0ee-50d8-3b89-931a-29dca16b95b3 | -7.99545 | -61.2227 | 2024-09-27 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94001874-728a-332f-8da5-878e7fe67ea5 | -7.99535 | -61.22299 | 2024-09-27 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ab990d3-c599-335a-a784-e3a97858f983 | -7.92246 | -61.27365 | 2024-09-27 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a7c2e97a-2ddf-3e40-a386-3cb7e1b7ece5 | -7.92156 | -61.27848 | 2024-09-27 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7eab25c4-00e9-3c75-b762-39a5ea7b0e72 | -7.82257 | -61.66585 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dfeee81f-18ab-3b5c-b14a-5425d81df7f0 | -7.8216 | -61.67094 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a92a80d-f7ce-3c2f-afec-8ae4f92880d8 | -7.81926 | -61.66791 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4b0e1f6a-aa25-3d88-a81b-53a56eb4ddde | -7.81832 | -61.67303 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 56931fd2-0b5c-34ce-a068-c1554ede2402 | -7.81625 | -61.66476 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cec0c5a2-fdf7-37bd-afb1-4176c2ba94ae | -7.81529 | -61.6698 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 406b00ee-20f4-3391-bdbd-0612c38bd639 | -7.55831 | -61.35801 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f581872f-4169-30d9-b0f6-da833c9caa47 | -7.5542 | -61.35524 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eed826b9-b08c-35b0-b2fe-34f7defa8ddb | -7.53634 | -61.38264 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 623e1d37-c3e4-3ba2-9f2b-900565d7aa5a | -7.53545 | -61.38752 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d88efd37-8334-3863-acb1-55cd9f1f6f8a | -7.53497 | -61.37927 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 76192ede-9e76-3336-b94d-85d95f1c6215 | -7.53405 | -61.38413 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 34774ec1-274d-30a8-adeb-9e93c52e4a65 | -7.53312 | -61.38902 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83699c5d-9b7c-3f7d-85fe-f3668384cf79 | -7.531 | -61.3766 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 13b9dd75-501f-3b97-b5ee-04f63d09679c | -7.53011 | -61.38148 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0ca80c67-672b-3b9c-807b-1a6c1ca00c40 | -7.52966 | -61.37326 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ee669824-877a-3a60-bad2-f2431cfd650f | -7.52923 | -61.38633 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6dce614c-fdee-33e7-9d52-8a007d0dc561 | -7.52873 | -61.37815 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f089ee1c-a6c0-3072-8d94-4d85cd17264f | -7.52781 | -61.38301 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README84.md)
