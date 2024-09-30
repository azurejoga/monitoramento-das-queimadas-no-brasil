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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2a619e5-52ae-3a89-b3b5-a02fb57b2a22 | -11.04253 | -52.4729 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc5d2141-8a33-3a1f-86f0-17ce4d42c381 | -12.78792 | -53.99233 | 2024-09-30 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 60d5c00f-fcff-30b6-b3e8-7f601584306d | -12.78764 | -53.98877 | 2024-09-30 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b096dda-9090-3d9e-a93e-c653c34229fc | -12.78399 | -53.9916 | 2024-09-30 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a7098e95-4253-3185-8ef1-8a15c206ba17 | -12.78371 | -53.98804 | 2024-09-30 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e2ef7834-b04d-3ed8-8726-33cfced33868 | -12.78006 | -53.99086 | 2024-09-30 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c2119e3c-7124-3ec0-8846-fccd504e9aec | -12.77612 | -53.99014 | 2024-09-30 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 633dedaa-3326-3de2-910c-51618a2348bd | -12.76825 | -53.9887 | 2024-09-30 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 81759863-daaa-3fa2-8e09-bfb06dd134af | -12.76737 | -53.9938 | 2024-09-30 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d8c330db-f051-31d5-a291-cee37aaadc37 | -12.76648 | -53.9989 | 2024-09-30 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a3c0afd1-983f-30d2-9db2-d74b52299611 | -12.76431 | -53.988 | 2024-09-30 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 39ce2aeb-5a67-3b3e-89ea-46110d9b8924 | -12.76343 | -53.9931 | 2024-09-30 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7369973d-bff3-35ef-a482-2498507a69ab | -12.76077 | -54.00842 | 2024-09-30 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 15ccb2e0-eef8-3ba8-bd96-09835ff5b43b | -12.70885 | -54.09539 | 2024-09-30 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 20c2eb36-b74c-37c5-bd7d-157d2b092e84 | -12.70489 | -54.09466 | 2024-09-30 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 33d27f5b-0a53-3609-85ce-bf98202a1808 | -12.66525 | -53.2095 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ddbdcd79-6c98-356c-b614-0b6cca6da63c | -12.66229 | -53.2041 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82047039-2ece-30d3-b687-83fdc6b4b515 | -12.57401 | -53.15177 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 64fefa4b-49ce-3687-9db3-b808a821d372 | -12.5198 | -53.1516 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d88a83e0-dd23-3f32-8769-ec5e008fea57 | -12.51685 | -53.1463 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a234820-9f95-3ee8-82a2-b19842211555 | -12.51604 | -53.15093 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2f60b32-0923-39a4-bc54-8612f9da17df | -12.51523 | -53.15558 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e0a09e5-3541-3a9f-b098-d24627f4e11e | -12.51442 | -53.16023 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d068d056-11f6-335b-bfb9-722cd770eaa9 | -12.51309 | -53.14564 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c150376c-d004-3050-9776-d1446019148a | -12.51228 | -53.15027 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56108b1f-4033-3c34-8fd5-9bd3c2e2c84e | -12.51147 | -53.15491 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3fc4f3e-da0d-3397-ad8b-c8e8a1983627 | -12.51066 | -53.15956 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f87922e8-5d23-3189-a1e3-fcd421d1f565 | -12.50984 | -53.16422 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 558297f3-ba17-3b96-86c3-26903cd1c35b | -12.50903 | -53.1689 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5797d848-c672-3c43-9837-ae52fd1d5e9d | -12.50821 | -53.17356 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8575f7e-d2a7-39ed-9015-2484065bfc22 | -12.50712 | -53.15668 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b93786d-55d5-3466-ba5c-990db4f6f1dd | -12.50689 | -53.15889 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5f74e5d-a5f4-35b8-bf5d-de6c232e4224 | -12.50634 | -53.16133 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf6e36f1-f67f-3db2-8df8-6cac77670d05 | -12.50608 | -53.16354 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f118538-fc9d-3c96-9c78-be11fec81373 | -12.50555 | -53.16601 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d4bdde3-1628-3e64-87b9-2a71a0b454ab | -12.50526 | -53.16822 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ceb3db3-e5cf-3c80-9526-0f83751e3b4c | -12.50476 | -53.17069 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88a8ebe7-4dcf-3f6a-9399-cc3993247f29 | -12.50445 | -53.17289 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b032ad0d-1227-36ea-978c-3bc419f24e74 | -12.50398 | -53.17537 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abd0fb4e-3f3b-3ade-b74b-e009ce5c1200 | -12.49986 | -53.17689 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c750c2c6-71cc-3f49-ab63-2a1a4fc8258d | -12.49942 | -53.17937 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fbf476d-a448-3f33-bf2f-45c79a04c008 | -12.49904 | -53.18156 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b6a70a1-d87e-3144-a0cc-c36d359a5db1 | -12.49863 | -53.18405 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 933e48d6-9aae-30a9-ab22-6f13a37322d2 | -12.49823 | -53.18622 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47525b75-4f6f-3588-9cb5-8fff9d30f6c6 | -12.4961 | -53.17622 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42465a71-a79b-3366-bb16-173db86f3bdc | -12.49565 | -53.1787 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06a2eb2f-79b3-33d3-9dfd-59fc240062e8 | -12.49528 | -53.18089 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a3f32d3-cfa9-362a-b298-99346f4b21f6 | -12.49486 | -53.18338 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5949a70e-4f60-3aba-ac08-6129d41ddc40 | -12.49446 | -53.18556 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8729b2e4-5460-364c-8818-8580e7ee35c6 | -12.49407 | -53.18806 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14534e43-c94b-3937-afa8-71a4661b29fe | -12.49233 | -53.17554 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7811c19d-6693-3c96-8c09-49c2a7721e1a | -12.49189 | -53.17802 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9cc71c34-bc95-3f3b-9db1-b51a5d506d81 | -12.49151 | -53.18022 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90ca0e26-ced3-3823-9e91-8ffe2b9a5603 | -12.49109 | -53.1827 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d162ca0d-2e6e-3799-bf2f-51125175b883 | -12.49069 | -53.1849 | 2024-09-30 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bf8f6d8-1454-3010-9c52-f10f8ac94557 | -11.78095 | -55.13127 | 2024-09-30 04:32:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b2d614a6-d3a1-3098-8c67-010840792ac1 | -11.21773 | -54.75503 | 2024-09-30 04:32:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6b014637-4bcd-3d08-ad1f-c3b563c9e70d | -11.21704 | -54.75902 | 2024-09-30 04:32:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 37be1b85-f6da-37e2-9b70-75b4476250b3 | -11.21634 | -54.76302 | 2024-09-30 04:32:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a6842a16-d806-370e-a2c9-79da91e02861 | -11.2121 | -54.76221 | 2024-09-30 04:32:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1b4508a9-d79b-33a2-afcd-71567b5d6f3f | -12.68927 | -54.67471 | 2024-09-30 04:32:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a40148a-29d0-370d-a182-6d190bf06350 | -12.68584 | -54.6702 | 2024-09-30 04:32:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cea61ec6-0058-3744-9928-cbc13267b222 | -12.6534 | -54.69582 | 2024-09-30 04:32:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 895cbb98-99e2-344a-8425-d13e54bbe0ae | -12.65274 | -54.69957 | 2024-09-30 04:32:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15a1cb0f-ae1b-362a-a884-4945540a5c34 | -12.64927 | -54.69509 | 2024-09-30 04:32:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d194293-815b-3e39-814b-5167ab483b84 | -12.64862 | -54.69883 | 2024-09-30 04:32:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d3abf93-1c3c-3466-9951-a6ca48782c54 | -17.12251 | -56.21498 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e896b120-a84d-36d8-a8dd-3cfae5f14a93 | -17.12211 | -56.19385 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 39120349-36b1-38d3-8262-52aa35601091 | -17.12175 | -56.21906 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 93551019-86f9-3f85-bbc3-97699b27b779 | -17.12135 | -56.19791 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 01f3ff51-ab83-3dc4-9f15-8271a9bf78b6 | -17.12099 | -56.22311 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 64ca5cdf-3ebe-306c-9e6a-ba16f173f33b | -17.12059 | -56.20197 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5c974e7e-b80f-3c19-a9ff-869452276111 | -17.11983 | -56.20602 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 59054a27-1af5-3b92-b3e1-6029c3491a32 | -17.11907 | -56.21006 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fb35ea18-c256-321f-b525-1ebfded89d29 | -17.11831 | -56.21411 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ef378742-9fc1-3d87-93d7-7286b1511729 | -17.11791 | -56.19299 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 40bb3a32-1cdd-3f5e-921b-bc09fcfc4814 | -17.11755 | -56.21819 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 47eb51b2-ced4-3c0b-9f40-4cd61e6496ce | -17.11715 | -56.19705 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 334e9643-6867-3d32-9c6e-a3f10819eab2 | -17.11411 | -56.21325 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9fbd9dc9-b069-385d-a11a-25d8828a1825 | -17.11371 | -56.19213 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7f564f7b-6f32-3268-a823-803fb5f07967 | -17.11334 | -56.21731 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| dda3449e-95aa-3a24-b6ea-22e12697f744 | -17.08391 | -56.21125 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e0954d8e-8677-3be2-9cf5-ca65afda7599 | -16.97626 | -56.20355 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c36796e3-d79b-3994-bc06-dfe098bb96f2 | -16.97359 | -56.19458 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0d9d0dfe-0200-3ee5-b750-5465914c2200 | -16.97282 | -56.19864 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ebab48d8-04f9-3dc2-96bb-20e8f12c4aa2 | -16.97205 | -56.2027 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| bd7730b8-c46c-358e-8439-8bac319ea1e3 | -16.97127 | -56.20678 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c15b6887-03a1-3de7-9511-2081714ba4f2 | -16.96957 | -56.1951 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b1bab7a7-1de8-3ab2-927e-a6779faa09a6 | -16.96882 | -56.19916 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ca3e42d1-b01c-35bd-b48b-29cef80a4ef4 | -16.96861 | -56.19778 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f5e2c309-cdac-3f91-9b11-b3808ca3a4d6 | -16.96784 | -56.20185 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 39dbaa0b-5e52-39fd-bacb-d5797f1fb6ef | -16.96536 | -56.19424 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d5978ecd-69c5-39d1-8722-dcba9c931e8c | -17.13202 | -56.18745 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| b7eb173f-7991-3c47-992b-2d1ee2bc893f | -17.12858 | -56.18255 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 6472fba3-9048-38b4-aac2-90505c93fb1c | -17.12783 | -56.18658 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 78e05752-5308-3a96-ba34-801026b26b54 | -17.12707 | -56.19064 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 923c3d6a-e651-3b26-861f-3eeffdede76d | -17.12514 | -56.17766 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 32da80b0-1cb5-3632-94dd-2fcdf5152791 | -17.12439 | -56.18169 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 82dd563c-c482-3ee9-90ff-a4eb7903f584 | -17.12363 | -56.18573 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 14cb0c14-40e7-32ad-8631-aece3e482cd9 | -17.12287 | -56.18978 | 2024-09-30 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |


[Clique aqui para ver as próximas entradas](README48.md)
