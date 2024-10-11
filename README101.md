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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69121b5e-40d7-33e8-8313-6d029b958b1f | -18.09453 | -56.40576 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5c71c44d-add4-3222-893a-b2b4f29f43b4 | -18.09144 | -56.39775 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 69fcc2fb-72c6-3629-a1f5-192ce4a2018b | -18.09097 | -56.40147 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 534c50dd-fe11-35ff-a502-ff9b805a58dd | -18.0874 | -56.39716 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f59fcddc-e7cb-3c74-908f-1226daa56a83 | -11.92562 | -56.9206 | 2024-10-11 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1b64459-1252-31d9-9398-bf0a4b18f804 | -11.92483 | -56.91808 | 2024-10-11 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ab793044-50e7-3716-8587-d42a274a4577 | -11.92419 | -56.92238 | 2024-10-11 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19f2e798-7e31-36a1-8b7d-027ab0349a86 | -11.91396 | -56.91644 | 2024-10-11 05:21:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3193e97-efca-3df8-abed-04257ff3984a | -12.61919 | -56.51488 | 2024-10-11 05:21:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bf9b2b43-3997-3828-87c0-a5d17d0a38ed | -15.86998 | -57.47079 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6feab409-9020-38d3-a019-44004f3f028f | -15.8694 | -57.47504 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ba72f6a-94e6-36b3-b1e8-e17edc2ec795 | -15.86881 | -57.47932 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 786f615f-b9a5-3845-ac04-d43d622410b1 | -15.86632 | -57.47004 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 215ebb86-320a-39fd-ad12-c74662914844 | -15.86513 | -57.47873 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 554ef473-6cbd-3772-8e40-9d45a037adac | -17.17494 | -57.44448 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b587f374-2253-307b-a457-0503553bf7e8 | -17.16366 | -57.47157 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5d0d6121-6707-3cb2-971e-e1bbb58db5b0 | -17.16303 | -57.47626 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 703d9f41-f7ee-3fe7-8a38-6a005191df67 | -17.00031 | -57.44796 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5673f144-beea-304a-bc48-b4ab73d9e60c | -16.99838 | -57.46199 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b7fd68be-fa5b-352e-88f7-cd9380b0885c | -16.99656 | -57.4474 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| af73587c-cc9a-3bfd-959b-39d23164bb0a | -16.99464 | -57.46143 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0fe230d0-e6d5-3a02-9594-fabac57cd758 | -16.994 | -57.4661 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8496e541-e51e-3605-94ec-50ece32a4cb1 | -16.99336 | -57.47076 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 89f4f04a-c97b-30e2-8669-6dd713c17fcd | -16.97785 | -57.44458 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 0b7ff359-2fcd-3470-8dde-8857fe5c8786 | -16.97722 | -57.44926 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 49e0378f-67ee-3e85-b738-0aeff556d7a6 | -16.97475 | -57.43933 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 349de9a2-26f9-33b1-9c2d-ebbfb8d46712 | -16.97412 | -57.44401 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4bbcce75-834b-35f7-9ca1-e6edc9a9477b | -16.97037 | -57.44344 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 10b32ec7-7cb7-36a2-bf65-55e537a8115b | -16.96789 | -57.43353 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8e5e6ab4-0fce-37f3-b069-0153bcf084e7 | -16.96663 | -57.44288 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 095f7a0e-0779-3f59-ae10-69be4cfae0cf | -16.96415 | -57.43296 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c42f977c-f073-3b72-a999-4f98360d01f5 | -16.95978 | -57.43708 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f1ecc83c-9ef9-38b8-87e8-8b58e3bdec22 | -16.95915 | -57.44175 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 19624114-09d5-3f43-b612-5ce28ab686bf | -16.95603 | -57.43651 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1f9b6184-e8b9-3116-a7ff-85b82a40a9d3 | -16.9554 | -57.44119 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3e8329eb-a88b-3d19-90b6-2dd6907ec6f9 | -16.95103 | -57.4453 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| cc7e5ef5-41dd-3a54-9844-fa176cd784de | -16.94729 | -57.44474 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 60c6eb45-2ea4-35f9-b47e-76a9a300ffbd | -16.94584 | -57.44651 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3b7bb3e8-2da6-3b68-8500-d3abbb00c124 | -16.86976 | -57.66533 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e6ed5b7f-f19c-3c2b-9c79-25d2398631d7 | -16.6452 | -57.44963 | 2024-10-11 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c955ea61-42e1-31b4-beef-119ecd38c0ad | -15.96771 | -59.10387 | 2024-10-11 05:21:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91e895b6-50ff-3c95-9668-75c0cafcee5d | -15.96428 | -59.10333 | 2024-10-11 05:21:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27eba28a-1632-3828-8f2d-9cbf4ce37ca3 | -15.71378 | -59.35493 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64001a04-e551-387d-be80-db140e6da945 | -15.71095 | -59.35061 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69dc18d5-67bc-31bb-9e7a-4256be16eabf | -15.70755 | -59.35009 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3aced496-3f8c-3510-b704-8928d4079fcb | -15.70528 | -59.34186 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c75d9f4-4a2a-301f-a1b5-c43cec7d2cda | -15.70472 | -59.34567 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99da7c6b-81ce-3f04-aca1-deaebeaebc02 | -15.70189 | -59.3413 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ebf956a-c300-3852-bf38-48eac3b5699c | -15.69737 | -59.34849 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57b1b7a2-43c8-34fd-9b63-c62f3b80ce36 | -15.69454 | -59.34408 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| afbf55f8-f13e-31e6-b205-9158af540dd5 | -15.69397 | -59.34797 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 313a14cd-60ac-3ca9-b32e-75f7c7c35a68 | -15.69358 | -59.34409 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6bc17348-3af5-3e21-824e-914f96b1a9ce | -15.6934 | -59.35184 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| faa21de3-167d-3a0a-846f-c7b403f130d2 | -15.693 | -59.34797 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 41641842-01b6-3d0e-b9b6-9b2493c5d601 | -15.68054 | -59.36153 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 410f4a73-fa93-3f7c-b44c-264ddd529f39 | -15.67715 | -59.33781 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f093894d-bb97-3c1a-b5f3-949189042c33 | -15.67659 | -59.36473 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95aaae57-ddaa-30e0-9950-1bbaf7d4427e | -15.67318 | -59.34109 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8aa272cf-56d8-36ca-85b6-6fcdb44a09ce | -15.67264 | -59.39107 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1adf6469-f606-3c92-9ec8-5b02aaba94a3 | -15.67211 | -59.32502 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f5724684-f8e7-39de-b99a-55b34e987d50 | -15.67206 | -59.39487 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 586c573e-5d3a-31c8-a25a-fe79049a6b8b | -15.66923 | -59.34432 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 625f1544-8317-3749-a2e5-56ef5cbcc7c2 | -15.66866 | -59.3481 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9296315a-ce74-3327-b198-3f3f32dea231 | -15.66815 | -59.32829 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51eb46be-ab38-3b95-a4df-55a9e30144f0 | -15.66757 | -59.33214 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ec2eacf-bc96-336a-be8c-9d702c807c88 | -15.66642 | -59.36307 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f1db5d0c-8273-3fa0-aec6-297ca152d5f4 | -15.66471 | -59.35127 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c784423a-d0a9-3a70-b9eb-408b894027a3 | -15.66414 | -59.35508 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40c0c42e-2bc2-3ab9-9661-887f7eaafa0c | -15.66359 | -59.3588 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54a76510-671a-3d03-8e0e-3fdda6327133 | -15.66303 | -59.36253 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 123ade2e-d782-33a1-b9cc-fafd9a5983cf | -15.66134 | -59.37378 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b87251f-dc2e-3d35-934a-bd53d3e6ef88 | -15.66022 | -59.38129 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6c34184-c483-3284-87fc-b6d731382c49 | -15.65683 | -59.38076 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9672ed31-f40e-3e62-8a81-41fdcb9c3162 | -15.65627 | -59.38455 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a931779c-777a-364c-af2d-180a1169f35c | -15.65344 | -59.38022 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b43ea6fc-1e6c-368b-85a3-0759afcc3dfe | -15.64608 | -59.40625 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ea8ec6a9-2493-3be4-9a99-8f32b4bb5508 | -15.64327 | -59.4019 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9cd3139f-afeb-3601-aa16-1dc417a8de2d | -15.64271 | -59.40565 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7ca6b898-6881-3af0-83d8-ced7e4d72abe | -15.64044 | -59.39761 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7eb8f4b6-dae1-3448-a9e9-5ea9a3673501 | -15.63992 | -59.44746 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 070409cf-c8a7-3afa-8265-d75c831b21fe | -15.63989 | -59.40131 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cbb1dfb1-1dd8-3b97-aa5a-9c1b3409741d | -15.63933 | -59.40505 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cf9e86c7-e397-3bcd-89be-78b27b0d22d4 | -15.63932 | -59.38186 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e822932f-a0b9-3f01-9f9d-0081e49e5a9d | -15.63874 | -59.38575 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 654f18ed-40dd-34d6-9d7b-90d286d8e00f | -15.63817 | -59.38955 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b6ea788-3422-33fd-9230-75db7d56c9e1 | -15.63762 | -59.3933 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d64d9e8-2509-36f8-ad68-6d52cf9fae9c | -15.63654 | -59.44691 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 65e40a3a-bd60-3996-b9de-a8c6899f036d | -15.63538 | -59.4083 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 366fcadb-8140-3f08-9092-1ccf83a4c191 | -15.63425 | -59.43906 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e89e1c69-843b-3788-a871-56f7960e6b7a | -15.63425 | -59.41584 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54d12a87-f13b-343c-a1bd-3d2b7c662a2f | -15.63371 | -59.44269 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7aa8624b-98fe-30fb-a9f4-26b16d90af58 | -15.6337 | -59.41957 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6f05651-2f98-3db3-85d5-a2f4e61f7f9d | -15.63313 | -59.42336 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2afc1d76-be22-333a-a348-2a0329e437c7 | -15.63256 | -59.42717 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 516054ec-47b0-3494-a463-6cd28e12b444 | -15.63144 | -59.41148 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d93681d-bd52-3290-a1ba-f7f411192cbe | -15.63143 | -59.43477 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e1eaffa-3616-332f-a0b0-09e0e6a5aadc | -15.63088 | -59.41523 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31407996-c4d0-3417-9307-231bcd0abf24 | -15.63087 | -59.4385 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20321f5a-ae28-3b68-b843-f0f69839312e | -15.62975 | -59.42278 | 2024-10-11 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 307405de-b3ed-30fd-9d27-9f4c460368a3 | -11.72313 | -59.28511 | 2024-10-11 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README102.md)
