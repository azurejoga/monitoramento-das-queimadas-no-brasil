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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eaf5e805-3684-358d-978e-6ec4ae7c26ff | -14.55291 | -49.30234 | 2024-10-05 04:40:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e45b9e95-0041-301f-b7e9-9d887c1e1aba | -14.52499 | -49.27833 | 2024-10-05 04:40:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e82cbc61-9b0c-32ad-a4a7-fb48b5ded8a5 | -14.47368 | -49.29401 | 2024-10-05 04:40:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82c04d16-07c6-3b8c-a0e6-b10849e189ee | -14.47027 | -49.29343 | 2024-10-05 04:40:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbc54db8-e52f-3caa-a91e-16ae3dc45335 | -14.46686 | -49.29285 | 2024-10-05 04:40:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2dc9c562-1204-35c9-843b-a5a8db31e844 | -14.46403 | -49.28912 | 2024-10-05 04:40:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48823309-9efb-327b-81f6-1ae99896743c | -14.46401 | -49.28843 | 2024-10-05 04:40:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90981286-d081-38c5-9512-aa5f65c2adcf | -14.46344 | -49.29227 | 2024-10-05 04:40:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9039a4fe-003f-379a-b6d6-7426c183f6e0 | -15.07726 | -48.94334 | 2024-10-05 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b2b85354-3c53-36d7-b11f-ddc337da10e1 | -16.10445 | -50.24951 | 2024-10-05 04:40:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 548e6635-8122-3ac4-a494-b2db390edddf | -16.10389 | -50.25324 | 2024-10-05 04:40:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0322d1c5-86a7-303d-aa2b-362858317362 | -16.10333 | -50.25698 | 2024-10-05 04:40:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ba86367c-0579-3dfe-a82c-67d6fd9efbd5 | -16.10107 | -50.24906 | 2024-10-05 04:40:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23bbb9f0-f288-3b01-8d9e-0563fbd028d2 | -16.10051 | -50.25281 | 2024-10-05 04:40:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e595223-943b-36e9-b9db-29fa4b1607d5 | -16.09939 | -50.23738 | 2024-10-05 04:40:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6ab1723a-4a56-3274-ae3f-7be071a5fb9e | -16.09882 | -50.24112 | 2024-10-05 04:40:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f8f4780-0e79-349c-a1d3-4b4589b9af1c | -16.09826 | -50.24486 | 2024-10-05 04:40:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8401cb7-a476-3925-a1f0-cbdb99687145 | -16.0977 | -50.24862 | 2024-10-05 04:40:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee055326-cd3b-3619-b88f-ba2dededf79f | -16.09602 | -50.23687 | 2024-10-05 04:40:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69664be0-3842-31a8-b0bf-d35d3d4ee53a | -16.09265 | -50.23637 | 2024-10-05 04:40:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7b2090a-0aac-32e0-9c34-1ae88efa13c1 | -16.09209 | -50.24011 | 2024-10-05 04:40:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09454a20-62a4-3af6-a6b2-9638422c2761 | -16.08872 | -50.23959 | 2024-10-05 04:40:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f2dab59c-df24-36f0-b866-7bbde4a5bafc | -16.08816 | -50.24333 | 2024-10-05 04:40:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e07ea109-f7f4-3dec-ab7a-fb95802b2952 | -16.08761 | -50.24702 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b0a3720-3e99-390e-81d7-50598f37ce63 | -16.08481 | -50.24273 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c541ab16-c7e8-3511-9da6-5d813dcfcf8a | -16.08426 | -50.2464 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 850fd39b-39f7-30d8-a413-5fae925164c1 | -16.08316 | -50.25366 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 029a5de8-b49a-37d8-bab0-df940fdec1dc | -16.08261 | -50.25734 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0cfaa1a-6f2c-3f33-a0dc-b9c1ff90b649 | -16.08206 | -50.26103 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd693dd1-3592-3bcb-a2a7-b5c5f073ab84 | -16.08095 | -50.26842 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd641764-0cdf-3f2a-9650-97e8863b8315 | -16.08091 | -50.24575 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5346e8c7-a2e2-3085-b49e-a1f8f51ad539 | -16.0804 | -50.27209 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53217b4d-2ebe-3ea7-a77a-066336f95ff0 | -16.08036 | -50.24939 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ba6f2dc3-ce1b-3045-a238-c27d5f26da95 | -16.07985 | -50.27577 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 749a310d-de7b-3782-999d-83cd6f6f635e | -16.07929 | -50.27946 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4085661-0925-3af0-943c-7c012b6513ff | -16.07921 | -49.71616 | 2024-10-05 04:40:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee83e9d0-70d7-3ba5-891f-2875bce6bd98 | -16.07873 | -50.28319 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c6e7618-1f1f-31f4-ad15-ff3f73e6d8b5 | -16.0737 | -50.29378 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0407b17-0095-3efd-ad5b-1ec88e31ec80 | -16.07194 | -50.23663 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4387d5d5-b929-38eb-96f1-1c96dd252438 | -16.07139 | -50.24027 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0815341c-7829-3190-a65d-f98bfdc8048c | -15.89018 | -50.1631 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1da6236-6873-31ce-8444-e96282d84d1d | -16.17422 | -49.2627 | 2024-10-05 04:40:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 0b0130d5-6da0-3e6a-82a2-20952d7fa0ab | -16.17077 | -49.26208 | 2024-10-05 04:40:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 81231ee6-8c04-3199-ab6d-8b1d15f36b16 | -16.17019 | -49.26603 | 2024-10-05 04:40:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a6bbb48f-cba8-301f-83e6-978b6bafbf2f | -16.16961 | -49.26997 | 2024-10-05 04:40:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d05a309f-f741-3ef5-857d-27ee7c29865e | -16.16673 | -49.26538 | 2024-10-05 04:40:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1cd1a62f-91b4-32b6-a4d6-eeaede62f5df | -16.15982 | -49.26413 | 2024-10-05 04:40:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c73e38c-e728-345f-80ef-7255d6bc70ee | -16.15924 | -49.26813 | 2024-10-05 04:40:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8942e62a-49b2-34d1-a517-c704d99cb690 | -16.15636 | -49.26354 | 2024-10-05 04:40:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d5df3d7-7960-32f4-bce5-0cf5b2045226 | -16.15578 | -49.26755 | 2024-10-05 04:40:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b66efc5-c2c2-3887-8655-4fa18b41f19c | -16.15519 | -49.27154 | 2024-10-05 04:40:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53cba555-3c50-3e8b-81cb-f5d351ff2af6 | -16.15116 | -49.27488 | 2024-10-05 04:40:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d92ffd2a-1d6f-3798-b533-75b8f947bd11 | -17.53957 | -49.23247 | 2024-10-05 04:40:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de3d3b47-8e9a-3caf-95f3-dee4f0c78686 | -16.74567 | -49.31238 | 2024-10-05 04:40:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc7c3601-bbc7-36a3-b159-db131a041a40 | -17.79546 | -50.63783 | 2024-10-05 04:40:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f1d07faa-ba38-33d5-8a25-0ed202988b58 | -18.42379 | -49.76245 | 2024-10-05 04:40:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 25.4 |
| dfccac19-d139-3b02-8ec3-977fbd26ec61 | -18.42321 | -49.76649 | 2024-10-05 04:40:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 01173acc-6f0d-346d-9f06-56bc6eba82d4 | -18.42031 | -49.76193 | 2024-10-05 04:40:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 56e4de01-ac37-3e69-a7ca-208851933a65 | -18.41973 | -49.76597 | 2024-10-05 04:40:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 31.0 |
| fe2cc5b1-62d4-3ab1-8f98-5f6e66b27428 | -20.09132 | -50.16206 | 2024-10-05 04:40:00 | NOAA-20 | MACEDÔNIA | SÃO PAULO | Brasil | 3528205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 6c6bde05-4159-3f3c-b579-e304bb855aa3 | -16.09567 | -50.46655 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 999ba2e0-c3de-3b0e-af89-87ef51f15306 | -13.19749 | -51.18456 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21160e84-737e-30be-8735-58c73d402921 | -16.10012 | -50.45988 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bba37e39-0deb-3115-885f-87cc14a92079 | -13.63508 | -51.20973 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f51d05e3-46d4-38f8-a542-c724c9620c2c | -13.63452 | -51.21327 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1b4fb2a-421d-321a-a1c9-7a9b3fde4634 | -13.63175 | -51.20924 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 818e7c73-c35e-35fb-b472-d01b28446b54 | -13.63119 | -51.21278 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2e2a911-2c16-3d5c-ac19-022fac8c8ba1 | -13.63066 | -51.21626 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25d8fc1b-f472-317f-994a-1c4b71a8a1e5 | -13.62844 | -51.2087 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1017c9f1-c00b-39c5-ae55-35ab16918b1a | -13.62788 | -51.21223 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59d5782b-00c0-3737-a445-2d17d23c9d8a | -13.62735 | -51.21571 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f37714e6-4cf5-301c-84f5-095591d0c6b3 | -13.62679 | -51.21925 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c584d948-bca2-33b3-8973-7d63f0aa6f41 | -13.62669 | -51.26278 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5257e29c-4911-3973-b375-da3ed2a04cf5 | -13.62623 | -51.22278 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70b8583f-d14f-3c15-83f3-067469f18d9e | -13.62613 | -51.26632 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 31ab0a8f-8153-35ee-a889-e4f68ea2de9e | -13.62567 | -51.22632 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03e2cbb1-aad3-35a9-9892-443c12df2eaf | -13.62557 | -51.26987 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1bcacbbb-b2f4-3da3-a4a9-bd1e1e857b42 | -13.62501 | -51.2734 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3f8ccf0-2b83-3f6e-94e0-f6ce37238d4b | -13.62338 | -51.26224 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ff9f893-e769-3a6f-b576-084675576576 | -13.62282 | -51.26578 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4f50b753-0bd0-392a-b38e-58fb3997321c | -13.62231 | -51.20379 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e48f8b52-75a2-3055-9116-ab3a89262483 | -13.62226 | -51.26932 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 641527c2-c9eb-3d6b-8503-50cc36ddbbf7 | -13.6217 | -51.27286 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2aed56c0-d40a-3fe7-a2e4-71657295cd67 | -13.62063 | -51.25815 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b406807-72af-3a41-b574-ba1796059d53 | -13.62012 | -51.19623 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9bb26106-93b2-3e70-8c34-45b0896e3ddc | -13.62007 | -51.26169 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54e3cd17-6a56-3695-bfd1-b6f986686b63 | -13.61956 | -51.19977 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a76df351-f464-38cf-aad0-ad0a801d99cd | -13.61951 | -51.26523 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9fbf04a9-4fdc-35cd-8eb3-535e05c13308 | -13.61895 | -51.26877 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a21cc05e-2c5f-3203-a10b-bc2dd81d7cc4 | -13.61669 | -51.26093 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c268b651-e9d0-30f2-919c-3b9718163313 | -13.61645 | -51.06863 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9cae409e-72ae-34b7-94f6-dc7e0e7d4ab4 | -13.61613 | -51.26447 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12ed3934-85bf-3288-b55d-9eda0a902c4f | -13.60945 | -50.87526 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b2fe0ac8-23d5-3d2a-80fe-fcd263b0e75d | -13.52374 | -51.11876 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa1efa89-40f6-38c0-abca-54c01d107f8a | -13.92026 | -50.84229 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2339b4c-18ad-3a18-99e4-f050992aa333 | -13.7154 | -50.95813 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46e4b3a9-84a0-3608-9a7c-f54a50b0d991 | -13.63783 | -51.21382 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5fd9420-145a-34b7-acbd-ff4ccac36bde | -13.63 | -51.26333 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 861e170a-5006-3d70-8cd3-cb55986053c7 | -13.62944 | -51.26687 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1ba67606-9e71-3a93-8414-e73fcabc1b65 | -16.13306 | -50.44636 | 2024-10-05 04:40:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README118.md)
