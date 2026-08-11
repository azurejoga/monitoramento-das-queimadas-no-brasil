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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4971f7ea-bd28-376d-80d4-331cc5ac2cbe | -8.95787 | -60.56755 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bad8500f-1889-3bbd-8921-50ad11b8d841 | -8.9495 | -60.51217 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a4fa442-7d8e-3925-9199-32af47d6f536 | -8.94285 | -60.51112 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a323c6d8-a45c-31e4-a065-d3619d2a53b3 | -13.87178 | -53.78295 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d7b677ef-12b4-3d59-a462-1d3f77e2f8b3 | -11.22877 | -54.85363 | 2026-08-11 05:29:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 912fcc4a-9e8d-3dba-88b4-103edbfbbe94 | -9.47011 | -60.52507 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d17dbef0-b44a-345f-b0d2-829b2256f406 | -8.95285 | -60.53433 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bcc1295-ea95-33e1-8c7e-440a89a401e6 | -11.19149 | -54.85321 | 2026-08-11 05:29:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 626e5d34-6aa8-3812-bf4b-2a31dc408f8e | -8.95895 | -60.5389 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f26b0707-24d1-3ab4-a343-bd311895cc15 | -9.07071 | -65.45857 | 2026-08-11 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dce44369-c475-3ed4-90d7-4e781f4381fc | -10.15233 | -67.72726 | 2026-08-11 05:29:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18e0bc23-9c40-354c-9865-a22b050f8286 | -11.22925 | -54.85156 | 2026-08-11 05:29:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f323d87b-ce90-3d47-9261-581c576109cd | -9.71962 | -60.20559 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 848066f5-3c0d-3362-b9a2-aa881af22f67 | -8.95836 | -60.49913 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4613fcc5-de49-3673-a874-bc0d733349f0 | -13.43216 | -57.04776 | 2026-08-11 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4d162bb-3d82-3835-9dad-2fa9bbdbc21e | -8.8953 | -60.57564 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d00ed0ca-42d1-3468-bc21-c013171ddc74 | -8.9423 | -60.51464 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44305151-7887-34b0-8c37-f4d80135a249 | -8.954 | -60.57053 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f9bc8931-8602-39e3-a41d-33af6742ac1d | -8.8964 | -60.56861 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59abd5ff-2894-3bdf-b5f9-60cbcd61c53d | -11.23175 | -54.83249 | 2026-08-11 05:29:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97342d42-ca39-368a-a81a-941ab547263c | -8.94953 | -60.5338 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3528067c-d90d-39a2-9043-078185be4496 | -8.9523 | -60.53785 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 050c233a-7dd0-398a-bd06-593f826f63fd | -9.06707 | -60.41064 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c9331cc-4009-30b7-921c-9a1eb6196381 | -8.95677 | -60.57457 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47bd165f-0256-3a18-ac87-649ab7225d28 | -8.89198 | -60.57512 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee02a73b-154e-3567-8b3f-4e3c052252df | -8.94618 | -60.51164 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2930c9b-2dd5-3841-85c9-98657e0f875a | -9.47512 | -60.53673 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ebb7397-7428-3d35-8de7-6dfece7ff71c | -13.43725 | -57.04092 | 2026-08-11 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30a1ab4e-5285-34d5-a0c2-927bf354169d | -8.89698 | -60.58671 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bdebc839-2322-3cfd-8a89-07c1b27419d3 | -8.95398 | -60.54892 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb0db53b-f159-30c0-aa83-ba51cb1cb3b3 | -8.95005 | -60.50864 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54d52f42-50f4-323d-99df-b0b41a64b18d | -14.30964 | -54.91801 | 2026-08-11 05:29:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d7ac390c-ead0-384c-bf88-f29548ff7307 | -14.00478 | -53.97904 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ca4206c-1bc7-3fb6-808f-835362330463 | -9.90265 | -60.27102 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99163944-071c-3441-b4a0-f14b6b424292 | -11.22716 | -54.83185 | 2026-08-11 05:29:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 847787da-2568-31bf-8525-7d55919b5f1a | -10.73634 | -50.45441 | 2026-08-11 05:29:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b420ae8-10e6-3973-a141-e43afe252a7f | -10.88904 | -50.37487 | 2026-08-11 05:29:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 286fd26d-1a16-38f2-a25f-016b4f17650f | -13.86429 | -53.80164 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bbf02c1a-4eed-32f5-83e6-f487add74e93 | -13.42401 | -57.04652 | 2026-08-11 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1475474c-f07a-309f-bd40-8d31da3b5640 | -8.95618 | -60.53486 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35399d86-4cd8-347e-8378-74cee61e6bb1 | -10.27976 | -60.5389 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16bf57c0-d40f-3145-a8ca-5b1808c1a75d | -9.47344 | -60.5256 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21df86df-3475-37b8-948f-8da53d9e7a83 | -8.68288 | -62.86931 | 2026-08-11 05:29:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bb93860-107c-3b9f-b1b5-cbc238337840 | -11.2399 | -54.87685 | 2026-08-11 05:29:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d862bf5-8c51-32a5-84ba-4a84c6af153e | -13.59414 | -55.21567 | 2026-08-11 05:29:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7cf0701d-060c-367b-9914-edaa347034f9 | -8.9451 | -60.54032 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3b444a2-cfa2-345a-83ca-a98f6c020a51 | -11.4899 | -54.60841 | 2026-08-11 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85f63d2e-626e-3d02-81e2-da7d904a9fa6 | -8.90085 | -60.58372 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0cf586e-3d8c-3ca0-94cc-c53a7fa1c471 | -9.47567 | -60.53319 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2361a814-fa6c-316f-8306-88094fdf18d5 | -8.9601 | -60.5751 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d4fa4d9-682d-3179-82f4-12eb0f020bd1 | -8.94343 | -60.52924 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf9f13b9-ec26-3b93-8194-27d7e40e875f | -12.13322 | -57.99223 | 2026-08-11 05:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e5c73a3-0193-394d-a7f0-b6b83d40540d | -13.84136 | -53.68954 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad86b11c-7276-3eae-8443-3b80ef48055f | -8.89972 | -60.56914 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdc82d44-4527-3591-9192-1bd4cb2d4742 | -14.00442 | -53.98204 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df92565b-0100-39eb-8eb7-a0b4d3c0004b | -8.9551 | -60.56353 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f7402ad5-4a13-3db6-9346-e18f0e7d682e | -11.2305 | -54.84202 | 2026-08-11 05:29:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb7ef2cc-390e-3b8a-85fe-33fe37d66766 | -10.93828 | -57.11278 | 2026-08-11 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3613a576-a982-3e6d-a13a-f4a4fea95ebc | -10.72664 | -47.91779 | 2026-08-11 05:29:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2b4c8441-5b06-30c4-b945-e821a577f392 | -8.9562 | -60.5565 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 71fb18bf-3b3f-3bb1-b5df-3632bdf01466 | -13.43317 | -57.04033 | 2026-08-11 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62702572-be27-3748-b932-83faef8a06cc | -8.9512 | -60.54488 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28ecf015-520c-35bb-afa8-34aceb5b4418 | -8.89253 | -60.57161 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e5e6afe-f656-3479-b52a-c8ba00688e31 | -13.63916 | -57.92717 | 2026-08-11 05:29:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2035cbcf-8514-3b21-88ca-06805b47edad | -10.73164 | -50.43641 | 2026-08-11 05:29:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ece5e9ce-b45b-37bb-8db3-38a7800cfe90 | -8.98001 | -60.53502 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9dd80dd-b87d-3281-9606-3a6fe7e4421d | -10.89577 | -50.37088 | 2026-08-11 05:29:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47a9938e-8b83-339f-b75f-723d6a5c8be7 | -14.30955 | -54.91637 | 2026-08-11 05:29:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 060c79c4-1dc6-382f-826a-3a6ecd88a5a9 | -10.73368 | -47.91915 | 2026-08-11 05:29:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 743251d4-2962-3dfd-b9cd-16a0ddd45dde | -14.00069 | -53.98077 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5198367a-37f4-3f9e-ba26-ea5adf3098bb | -8.95343 | -60.55245 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eed13639-1692-39bc-a6aa-1efd31249a32 | -13.42758 | -57.05082 | 2026-08-11 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ad8d963-8f04-338e-8d1d-1271c167ddda | -8.95008 | -60.53029 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 298157b2-60da-36e5-b5da-92f02afeb702 | -14.00574 | -53.98148 | 2026-08-11 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 126fa339-5e85-3825-afa4-ce5c0348662e | -9.9032 | -60.26741 | 2026-08-11 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e17e443-517d-3ca8-b75c-71218fef68b6 | -8.95891 | -60.49561 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9677dfa9-14b7-39a7-939a-d6f3d87896ca | -8.95455 | -60.56703 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba20e2ee-bc11-347e-94f5-8f0db98c0568 | -11.22403 | -54.85576 | 2026-08-11 05:29:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb0f4c7d-4224-3fcf-a528-d60fdd456818 | -8.94398 | -60.52572 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 29905761-c52f-3fc9-b0df-4d6be9a7d241 | -9.23134 | -60.83673 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8050b916-aa21-365c-9987-3a0028b486c3 | -8.95287 | -60.55597 | 2026-08-11 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4e87b7b-2ce7-3ae3-817d-4ef44bf6eb18 | -9.06691 | -65.45792 | 2026-08-11 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 05546070-6ce3-3cab-a613-8f8b429ba857 | -4.2635 | -48.1799 | 2026-08-11 05:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 018b4973-a59c-3a5a-8b92-35c4bdf804b0 | -8.96 | -60.5358 | 2026-08-11 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.3 |
| aa3d4405-8ff1-3836-89a2-1bd99d1f5604 | -8.9601 | -60.5165 | 2026-08-11 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 01128301-6b7f-3c0b-861b-211c801450ad | -4.2634 | -48.2016 | 2026-08-11 05:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| a50f68da-a7c9-3737-aadd-3fe00c2e9d55 | -8.9415 | -60.5174 | 2026-08-11 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.8 |
| f6cf3478-7821-388d-8726-a4757e4b84bb | -8.9416 | -60.4982 | 2026-08-11 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| d686a81b-2ab2-3dd5-899a-fad16270ac99 | -8.9602 | -60.4973 | 2026-08-11 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 0a224021-4bab-3c63-ae0b-ba5dad4cc862 | -9.3714 | -47.5119 | 2026-08-11 05:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| dd2bae3f-a526-3ee7-b749-13cfa642e38b | -17.13176 | -51.66189 | 2026-08-11 05:31:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ab95455-e7b8-3a6e-ab17-e80ba72f659b | -17.13904 | -51.65643 | 2026-08-11 05:31:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcdba080-dbae-3987-bfe2-ea198e27a1af | -17.13302 | -51.65475 | 2026-08-11 05:31:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2db9e8dc-3794-3e32-b9a3-c1a1f7d1b970 | -17.1323 | -51.65668 | 2026-08-11 05:31:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad66890f-ba2c-3613-94bc-78821493ba09 | -15.87368 | -56.25721 | 2026-08-11 05:31:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c911083-9246-32c2-9060-679fa253c3f1 | -15.87543 | -56.25518 | 2026-08-11 05:31:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 367db7de-0dde-3186-98ad-ec5ae21c1719 | -16.28219 | -56.60254 | 2026-08-11 05:31:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ff563cb3-6a65-32cd-9cb0-1e3a749b689d | -17.13775 | -51.6637 | 2026-08-11 05:31:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e9a8e28-96a6-3494-9611-eb911cb60fea | -17.12981 | -51.68049 | 2026-08-11 05:31:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cea411e9-c1d8-3f57-9756-73a0736f27af | -17.1325 | -51.66006 | 2026-08-11 05:31:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README30.md)
