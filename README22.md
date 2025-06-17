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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b30ed831-0c2d-3875-9d08-d02983b0a6b4 | -10.29517 | -60.53165 | 2025-06-17 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 686cd15a-fe48-3cb4-bf0a-800f0b5a3234 | -10.29453 | -60.53669 | 2025-06-17 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4f9b25fb-bdce-3915-bb76-d0a789395d86 | -12.51186 | -58.35145 | 2025-06-17 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e52d469b-0805-3b0a-a2d3-b163c8e16c8b | -14.03048 | -55.12069 | 2025-06-17 05:50:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4dad8e2-6e7c-3cdc-9f9d-23c5c6a0c636 | -14.03047 | -55.12987 | 2025-06-17 05:50:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a0c4c778-fbc9-3cea-aa73-f6d184318611 | -10.29323 | -60.5468 | 2025-06-17 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ba06918-6ca7-300d-8df3-6b3b0d875658 | -10.92882 | -56.8412 | 2025-06-17 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6b7d6df3-63c4-3f4b-8983-cc4f04a59af3 | -10.29922 | -60.53732 | 2025-06-17 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8d10fe55-2c91-3ae2-84b3-9d0427efba47 | -9.46557 | -57.84986 | 2025-06-17 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 385d46a9-37af-3341-ac94-c063e2491b78 | -11.08769 | -55.05909 | 2025-06-17 05:50:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa753d3f-ebd7-3e6b-8532-709cfe9da7ea | -10.93656 | -56.82786 | 2025-06-17 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 309b3ad3-c681-386c-ac80-a0f729f7ef8e | -10.29105 | -60.54444 | 2025-06-17 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 513af5fd-5742-3ec2-a0a3-5b66a87f6bc5 | -12.02769 | -57.09505 | 2025-06-17 05:50:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2da4c9a9-80ec-31d1-9cf3-4c9dea7f1e95 | -10.28567 | -60.54892 | 2025-06-17 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4cc8700f-ed19-3b82-9001-5be271cd83b5 | -12.51143 | -58.35521 | 2025-06-17 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6505315e-361d-3098-aa2f-d551d9c624c4 | -13.29095 | -57.07207 | 2025-06-17 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2816bff7-7dc3-3345-b57e-413fc5fd7838 | -10.88151 | -54.32386 | 2025-06-17 05:50:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12cca956-144b-3e1f-94f1-728358be7894 | -10.92936 | -56.83664 | 2025-06-17 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2744760b-2e4f-329f-99e3-9aba47b14c34 | -14.02425 | -55.12196 | 2025-06-17 05:50:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37a0a1ae-e231-30d9-8062-f5c4540799f1 | -9.46 | -57.8491 | 2025-06-17 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1ce3568e-6316-31c0-b5bf-482d563a3fa3 | -13.29084 | -57.07217 | 2025-06-17 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2cd7ef45-2c76-391b-ac91-19a2deb79e40 | -10.29174 | -60.5394 | 2025-06-17 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 464ef702-e174-32f8-a3c6-96b3b687c9c7 | -14.17398 | -60.06083 | 2025-06-17 05:50:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1195231d-fe28-397b-9e82-bf1d05ba9a99 | -11.80663 | -57.34773 | 2025-06-17 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 340c4673-f3aa-34d6-b40b-0802a2ff67ae | -14.02354 | -55.11967 | 2025-06-17 05:50:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b218b26d-dce5-3151-9490-9302afc77dc3 | -11.8061 | -57.35232 | 2025-06-17 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9d90bb5-6742-308e-b4d8-1b78cd78db79 | -10.28303 | -60.5331 | 2025-06-17 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 89d38b67-76f6-36d6-8bbb-6cc7d32624fc | -10.28772 | -60.53377 | 2025-06-17 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1967ba86-bf07-3f18-9c28-569173be3eda | -10.93047 | -56.82731 | 2025-06-17 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8ecb129-6e23-3fcf-8816-7246fa596264 | -10.93543 | -56.83736 | 2025-06-17 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 606f4fd1-1d40-3e51-9717-2fe7c53a54e6 | -10.92828 | -56.84572 | 2025-06-17 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 937e1fb9-0ac4-307a-9f90-11cc6668ed27 | -10.36216 | -57.23251 | 2025-06-17 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b487afd4-7c5e-3cb1-8366-6c1907897f9e | -12.50754 | -58.35335 | 2025-06-17 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fada729-a319-38a0-a617-be67e0fe08f2 | -12.02823 | -57.09053 | 2025-06-17 05:50:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fed5dec-ffae-3ed6-83d6-83a09f034c1e | -10.29037 | -60.54952 | 2025-06-17 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9253e30c-fa2b-3e6a-92d7-d91718afa555 | -14.20668 | -57.40767 | 2025-06-17 05:50:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4954cb0-56da-3477-9fd2-9b73ddebf925 | -14.03119 | -55.12291 | 2025-06-17 05:50:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 24a092b0-24bc-3690-833d-ad84058f0fe8 | -12.17223 | -56.5392 | 2025-06-17 05:50:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 899f1cfb-fa4d-3ae0-a222-908ccf73cd28 | -10.29242 | -60.53438 | 2025-06-17 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f1de99d1-a974-376e-9395-94dc9476f5c4 | -10.29712 | -60.535 | 2025-06-17 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f410b8f9-e7b0-31f4-9800-3b0c81e3b7ba | -13.2914 | -57.06728 | 2025-06-17 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ac28157-c112-3101-b99f-f224aa55d706 | -9.46509 | -57.85351 | 2025-06-17 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e295929b-7da5-3e83-82b7-a971502c3283 | -10.29543 | -57.1419 | 2025-06-17 05:50:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a58fc138-5e97-3784-bfe0-8dd494a24255 | -14.0298 | -55.12767 | 2025-06-17 05:50:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b521c04f-879b-30ab-8eec-08139f961b36 | -11.07925 | -55.05293 | 2025-06-17 05:50:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 90730444-52c3-30ac-9e8b-2efff5ff8a1a | -14.17435 | -60.05773 | 2025-06-17 05:50:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1131844e-0caa-3d29-98cf-4f3622978ea5 | -9.46482 | -57.8478 | 2025-06-17 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6fb89089-b74f-3cb9-a217-e2c4dc97d10c | -10.36268 | -57.22828 | 2025-06-17 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a29730bf-f9a3-38a5-a781-aefacdb16fc2 | -11.08093 | -55.05814 | 2025-06-17 05:50:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 17b3c701-5b28-3042-8361-88e64011a613 | -10.93599 | -56.83264 | 2025-06-17 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 54473831-62fa-32a1-8081-066d1052d748 | -10.29781 | -60.52997 | 2025-06-17 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6081902b-2800-371c-811b-3d9e03701106 | -9.46048 | -57.84545 | 2025-06-17 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9c335e5e-c5f3-3d1e-9c09-26ca545ffb87 | -11.5679 | -54.57453 | 2025-06-17 05:50:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b6ccb85-2c11-3db6-a839-b4ae1cf888c4 | -10.52154 | -59.39325 | 2025-06-17 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3d21cc6-3c17-3cd5-afa1-bb09c348bbfc | -10.29643 | -60.54004 | 2025-06-17 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c83e867-a0a1-3cf2-a30b-22cbf5726547 | -10.28705 | -60.53876 | 2025-06-17 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06a61f7f-de30-3bee-be08-0637f52e9dd8 | -10.28636 | -60.54381 | 2025-06-17 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1b06bc3-c1a0-3ac8-b261-c3f7a320cb6c | -13.44507 | -56.85471 | 2025-06-17 05:50:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b85cdb5f-8dc3-3f97-961a-f6e08f10d442 | -9.5111 | -55.96478 | 2025-06-17 05:50:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d2c679c-bdab-34bd-9994-7993306e9b5c | -11.0853 | -55.05994 | 2025-06-17 05:50:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| aeb9d0a6-a1cd-3feb-be5a-71cfe091050b | -10.92991 | -56.83202 | 2025-06-17 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e78ce88-3a8c-3a74-a3eb-fcbfd0b92816 | -9.51378 | -55.96471 | 2025-06-17 05:50:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9536da00-5ffe-37ff-ad48-49b48ab6a6bb | -10.87446 | -54.32309 | 2025-06-17 05:50:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44e0c37d-c38e-3be5-baec-cd1aedb3d405 | -13.29147 | -57.06717 | 2025-06-17 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25acc240-9f15-3124-8f2f-3211c2e22ca9 | -15.62344 | -57.30828 | 2025-06-17 05:53:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55e26dcc-96f2-3e9c-8e2b-694b91ee14b1 | -15.62964 | -57.30928 | 2025-06-17 05:53:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7121ebf-66ff-390d-9510-720dc10cb331 | -7.2605 | -44.6421 | 2025-06-17 06:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 905f7657-de7e-3324-b790-dfaa0bb7d9b4 | -7.2605 | -44.6421 | 2025-06-17 06:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 1d727e9f-c213-3d30-a4f6-6577145c2a18 | -8.0703 | -43.0981 | 2025-06-17 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.4 |
| e26ffe16-9b1c-3611-92b1-62d9367b10f3 | -7.2605 | -44.6421 | 2025-06-17 06:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| baa5537c-a33e-3dac-8764-5387ce7c29b5 | -8.0703 | -43.0981 | 2025-06-17 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 9dd2b06b-f808-325a-9043-47b166c3f679 | -7.2605 | -44.6421 | 2025-06-17 06:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| cab7956d-28e8-3bf0-9a3a-7cb3fd3728c1 | -8.07 | -43.1216 | 2025-06-17 07:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 04923819-704a-3403-bc67-e5e6fb376673 | -8.0703 | -43.0981 | 2025-06-17 07:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.3 |
| 22dd4184-c528-30f3-a653-ed0bf9e6c61f | -12.2417 | -44.2042 | 2025-06-17 11:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 7e74490c-469b-33bc-9414-e495d8a055f2 | -12.2417 | -44.2042 | 2025-06-17 12:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 080db313-70e5-3e4a-942f-7d5998c4c7a7 | -19.0716 | -53.4382 | 2025-06-17 12:20:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 79d1acb7-c6c5-3c2f-a4a4-969bc1ece53c | -19.0716 | -53.4382 | 2025-06-17 12:30:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 0ca0ebb3-b2bc-35cf-9494-801c775cf85f | -12.2417 | -44.2042 | 2025-06-17 12:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 4555d12e-828f-395d-b14b-4daf1dcd214d | -4.5429 | -48.0151 | 2025-06-17 13:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| e06208d0-0cbb-3c46-b9ac-034b9df3f911 | -4.5614 | -48.0141 | 2025-06-17 13:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| ac3dcd86-c18b-3ab6-9ed6-32c7ef39bf37 | -12.2417 | -44.2042 | 2025-06-17 13:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| b9eb9960-fe82-3938-9e0a-b279c6fd4791 | -4.5429 | -48.0151 | 2025-06-17 13:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| c2ac9b71-4a72-3ad4-af34-40f4df04a90a | -10.9353 | -56.8522 | 2025-06-17 13:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 5e8f1737-dd89-3e79-a71b-e35b7485808d | -19.0716 | -53.4382 | 2025-06-17 13:20:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 927fc5b4-0fb6-3e28-bb91-1d6e1f148ba7 | -4.5429 | -48.0151 | 2025-06-17 13:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 3929e3e9-dbdd-3880-b849-ebbcf97f176b | -10.9355 | -56.8322 | 2025-06-17 13:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 305a79a3-65f8-3195-9b8d-93b2ebfe8b44 | -19.0716 | -53.4382 | 2025-06-17 13:30:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 74.6 |
| a5da9fbb-3b2d-398c-8925-b9cd287fff34 | -10.9355 | -56.8322 | 2025-06-17 13:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 151.5 |
| 4fca6a23-ee49-3922-9a90-003012922b9c | -4.5429 | -48.0151 | 2025-06-17 13:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 2d77e6bc-5004-3678-a8e5-20a8cfa3cb3a | -10.9353 | -56.8522 | 2025-06-17 13:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 152.5 |
| 40daeffd-f572-3b2a-aa2d-6156c5144d0c | -4.5614 | -48.0141 | 2025-06-17 13:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 02c04789-7f6e-3f72-9b97-5e1842b39e6d | -10.9164 | -56.8536 | 2025-06-17 13:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 0e9f707e-fc52-3ca7-8843-29ca92c7050d | -10.9353 | -56.8522 | 2025-06-17 13:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 3b5dde5d-8121-3299-b695-d07a1f0c39a7 | -4.5429 | -48.0151 | 2025-06-17 13:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| f428a80f-da89-323b-a1cb-7b2b7201446c | -10.8694 | -54.3151 | 2025-06-17 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 76aba77d-d541-390d-9d0a-b4df0008206c | -10.9167 | -56.8336 | 2025-06-17 13:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 122.0 |
| fd2e9a63-8a93-3c6d-ad64-48f83b304dbc | -10.9355 | -56.8322 | 2025-06-17 13:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 187.7 |
| 3a8eb02d-04da-30c8-9a21-c46ebdcb9d3f | -10.9164 | -56.8536 | 2025-06-17 13:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 138.9 |
| 1c93474f-508e-3232-a3ca-c8722b9e3557 | -10.9353 | -56.8522 | 2025-06-17 13:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 222.7 |


[Clique aqui para ver as próximas entradas](README23.md)
