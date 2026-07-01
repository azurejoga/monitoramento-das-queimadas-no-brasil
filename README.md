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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74acd331-e951-30bf-8654-17a928c63e4a | -8.5933 | -48.0069 | 2026-07-01 00:00:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 0a49bb04-cf96-3a2c-89c9-f99e45bf4891 | -12.7746 | -44.5162 | 2026-07-01 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.7 |
| e49fae1e-c661-3678-b6c7-9f247fab8a7d | -16.3677 | -56.672 | 2026-07-01 00:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.8 |
| f4474d6e-4bbe-376e-b265-54a02d7e6255 | -11.8392 | -56.9401 | 2026-07-01 00:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| f4bfe20b-640c-34eb-a679-9c4d402e0328 | -9.6037 | -56.9276 | 2026-07-01 00:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 70b1188a-6e4e-3aa0-be83-12d435fd4793 | -10.4387 | -49.6005 | 2026-07-01 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 0d183215-0b96-3703-b51c-18ed30582f7f | -12.7557 | -44.4959 | 2026-07-01 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 321.5 |
| c5ad9513-9867-3521-8fa8-b42124d57b18 | -5.8058 | -43.7975 | 2026-07-01 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 76bd9131-1816-373d-982f-3a1f451ad4ad | -10.439 | -49.5789 | 2026-07-01 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 128.6 |
| e702700f-935c-3de2-923c-186e32c13f3b | -12.4285 | -58.385 | 2026-07-01 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 47e8796c-19b9-33d9-bab8-8e64960c4b43 | -16.3482 | -56.6743 | 2026-07-01 00:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.2 |
| af659f86-c0de-3e93-bd97-a2e1cffcec3d | -10.7654 | -53.5451 | 2026-07-01 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 9c519016-5a10-3b10-a062-2b888e555460 | -17.7114 | -46.8031 | 2026-07-01 00:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 56.5 |
| d0539b4c-ecc6-3c5e-93c4-07e6ad5c4a9a | -10.7843 | -53.5434 | 2026-07-01 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| b60470f0-e8b8-3515-8f50-5a88e6a4bfe8 | -8.1254 | -47.8749 | 2026-07-01 00:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 5358a997-35ff-3078-86d3-d54baed4d212 | -10.1237 | -52.0905 | 2026-07-01 00:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| c23770ae-3ecb-307c-a606-6f6d6d1568a4 | -17.712 | -46.7798 | 2026-07-01 00:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 7225a54c-2660-3a3e-9e62-e6004c53c84d | -16.368 | -56.6514 | 2026-07-01 00:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.8 |
| c5709346-e3ef-3f94-a3ff-8c3db2df7628 | -12.7751 | -44.4927 | 2026-07-01 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 429.3 |
| e7afbcb7-c7d3-3bf4-8eb5-1b47196298a6 | -12.7755 | -44.4693 | 2026-07-01 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 183.1 |
| f286250c-f339-35e6-9b22-d9922372913f | -12.4094 | -58.4063 | 2026-07-01 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 3df42b62-bc91-3285-99b8-414dc1d7bb61 | -12.7562 | -44.4724 | 2026-07-01 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 155.5 |
| ac1a4163-14ab-3f70-9a2d-a3d6de4847d9 | -10.7657 | -53.5245 | 2026-07-01 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| bdcdeb4e-f25f-3d0e-8f09-53c871b2f2da | -11.5337 | -47.4571 | 2026-07-01 00:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 37422572-900d-3705-b276-b7a79dca73f0 | -16.3485 | -56.6537 | 2026-07-01 00:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 80f86a25-f858-306c-88ef-61d22dfa8fbb | -11.5528 | -47.4546 | 2026-07-01 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| c7b10b0b-3147-3393-90f1-9668c40811b5 | -10.6784 | -54.5356 | 2026-07-01 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| e9fafb3c-7f7b-344c-8d3c-0daae8118da5 | -5.8245 | -43.7961 | 2026-07-01 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 546a539b-7409-31bb-8cdf-e9903dd8a766 | -12.4283 | -58.4048 | 2026-07-01 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 906429e7-d395-38ea-ac33-4f6c5656ac6b | -10.6596 | -54.5372 | 2026-07-01 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| ab645747-3988-3b4a-8f2f-480b5203cf35 | -11.6286 | -59.0169 | 2026-07-01 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 20e5a6f6-91dd-38e4-ba48-984fa242708e | -10.3822 | -49.5849 | 2026-07-01 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| f8b652ba-c7ed-39e5-be9c-3e783d454185 | -3.5043 | -48.039 | 2026-07-01 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 45fd799d-db2e-3169-a8df-d0a9fc62d661 | -12.4096 | -58.3865 | 2026-07-01 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 76c3d4e5-ece2-3fa2-93d9-2d804b82af39 | -9.6037 | -56.9276 | 2026-07-01 00:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 5f111c0c-c3e9-3c06-8c82-87c7b758ae46 | -10.6784 | -54.5356 | 2026-07-01 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 11f7d892-07cb-39d5-b713-e1282654998a | -11.5528 | -47.4546 | 2026-07-01 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 6b959c5b-6e8e-3db1-9076-458b9da87753 | -10.1237 | -52.0905 | 2026-07-01 00:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 8304c49a-c491-3cd1-8c9b-a5645b77f052 | -10.6596 | -54.5372 | 2026-07-01 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 3d4e18b6-a516-368d-b70e-f37d567fb37e | -16.3485 | -56.6537 | 2026-07-01 00:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| 1f2b3133-8602-3bb8-b2a6-e57a816b4e4f | -16.3677 | -56.672 | 2026-07-01 00:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.9 |
| 3c7488a6-91e6-3c76-8218-a479f7aba282 | -10.7657 | -53.5245 | 2026-07-01 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 8448a1f3-d140-38f9-a696-6200bd6eb461 | -12.7562 | -44.4724 | 2026-07-01 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 2fac83bf-f679-3258-8914-cb32f6d6dfa4 | -17.7114 | -46.8031 | 2026-07-01 00:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 125dfb9f-11fd-397d-9243-a861d3d8ae93 | -12.4096 | -58.3865 | 2026-07-01 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 6974f3ee-fb3d-39ae-ad47-b9ff9339f0c7 | -11.5337 | -47.4571 | 2026-07-01 00:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 62bd2356-2d40-3511-b4be-9288dc387511 | -12.7557 | -44.4959 | 2026-07-01 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 291.0 |
| 4363e78d-2da0-3b4d-a231-35063986e57a | -12.4094 | -58.4063 | 2026-07-01 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| f733a396-0fe4-326d-b9f7-66c78878d58c | -10.7843 | -53.5434 | 2026-07-01 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 6988c7c6-ab51-33e4-a445-bf3859981bde | -17.712 | -46.7798 | 2026-07-01 00:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 59.6 |
| b2b09139-7e6e-3bb3-b0f9-c6d21370a414 | -11.5532 | -47.4323 | 2026-07-01 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 8ebedcfe-4202-3e21-8a50-e8c450b73496 | -12.7751 | -44.4927 | 2026-07-01 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 538.1 |
| 15a48744-12cb-3713-8505-3dfb93963caa | -10.3822 | -49.5849 | 2026-07-01 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 3c083786-0905-3c9f-9095-8cfbe2824ebc | -10.4387 | -49.6005 | 2026-07-01 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 96ba47dc-b05a-3c9c-9384-d883b0a0c238 | -8.5933 | -48.0069 | 2026-07-01 00:10:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 158a4eee-b3ef-327f-b6b4-d51c4409166f | -16.368 | -56.6514 | 2026-07-01 00:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.4 |
| 43df5787-d824-3392-b392-0de2e2a59f67 | -5.8245 | -43.7961 | 2026-07-01 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 5d9f3d37-3f74-3689-a959-34f4543d1164 | -10.7654 | -53.5451 | 2026-07-01 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 147.3 |
| bd4f04f9-bda4-3465-a6e4-8c8fd8a4b2d0 | -3.5043 | -48.039 | 2026-07-01 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 0e40474b-0a47-3cb5-9f56-47514bd2d99f | -11.6286 | -59.0169 | 2026-07-01 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| e1473d41-a894-3c3a-91f9-cf6afe1dafc7 | -12.7755 | -44.4693 | 2026-07-01 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 1c960d00-0593-3f3b-811d-6341a198c0e1 | -12.4285 | -58.385 | 2026-07-01 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 996f7195-ec20-39fc-89de-b7c1f25825f9 | -10.439 | -49.5789 | 2026-07-01 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 9cafb00d-5278-39f9-ad07-d40332069c42 | -8.6121 | -48.0051 | 2026-07-01 00:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 6d24a023-380e-3f06-a879-ee3b54e3ec53 | -5.8058 | -43.7975 | 2026-07-01 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| d60b3022-9d59-39c7-9c20-eed06d644282 | -12.4283 | -58.4048 | 2026-07-01 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 1c1df087-b72f-389b-849e-0530ced10b6e | -11.8392 | -56.9401 | 2026-07-01 00:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 332a9473-8273-34bb-a16c-73362bf5b91f | -8.1254 | -47.8749 | 2026-07-01 00:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 2f9628bd-0d4c-3249-9b5b-901c2ac65325 | -10.6596 | -54.5372 | 2026-07-01 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 1688abcc-8166-3977-acd9-eb9a768ee2fa | -16.3485 | -56.6537 | 2026-07-01 00:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 3def62b8-0ae8-3353-b474-b3590d460fcc | -11.4149 | -56.0525 | 2026-07-01 00:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 230.6 |
| f1af2238-b2ca-3845-8212-ed9b72d1a267 | -11.4525 | -56.0695 | 2026-07-01 00:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 15b519af-2e1e-3023-b824-98b97fb21524 | -11.6286 | -59.0169 | 2026-07-01 00:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 945e06f9-6c60-3465-9b66-0f82efb39a24 | -8.5933 | -48.0069 | 2026-07-01 00:20:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 8c5867b8-c6dd-30a2-b97f-e028f752de76 | -5.8058 | -43.7975 | 2026-07-01 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| ee963a44-6780-3645-95b6-2b7bd976eb86 | -10.7843 | -53.5434 | 2026-07-01 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| a81457b8-4dca-3100-9e3e-5ad5a46bc829 | -10.3822 | -49.5849 | 2026-07-01 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 37d0a60f-0e2e-3be3-9935-f3eeb61df4ca | -9.6037 | -56.9276 | 2026-07-01 00:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 558c64ce-468a-3d8e-bc09-00ed687208bf | -11.4338 | -56.0509 | 2026-07-01 00:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 633.8 |
| 1a875082-9637-38e6-84f9-04dd055a88eb | -12.4096 | -58.3865 | 2026-07-01 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 133.5 |
| dcca397b-3862-3b9c-9098-ad5fcebe2520 | -12.4285 | -58.385 | 2026-07-01 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| d0a63ea4-9f52-3077-b6ba-c1c75eac7a0c | -10.7654 | -53.5451 | 2026-07-01 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 133.0 |
| 40c48075-aa14-3ad0-b863-f1ecfd759faf | -8.6121 | -48.0051 | 2026-07-01 00:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 02703619-e0e6-32a0-8804-95a0d9ac73d1 | -11.4336 | -56.0711 | 2026-07-01 00:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 943.3 |
| 5de4dc8e-757b-38ab-8914-49dec5aae09a | -11.4147 | -56.0726 | 2026-07-01 00:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 334.1 |
| 00b92a81-c002-30c7-9c60-232c849c0d72 | -10.439 | -49.5789 | 2026-07-01 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| e17b03da-0fcb-32fc-8265-9eadabdd359a | -11.5528 | -47.4546 | 2026-07-01 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 172.9 |
| dbe458b9-f929-3f79-b9cd-3545b0d77ec0 | -16.368 | -56.6514 | 2026-07-01 00:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| e212ee5f-e2bd-3efc-b8a2-f036b79caa8b | -11.8392 | -56.9401 | 2026-07-01 00:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 67f9e216-24c8-369a-acdd-384948c0c277 | -12.4094 | -58.4063 | 2026-07-01 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 00a792a2-48e6-3523-a1f1-17fbc2f3538b | -10.7657 | -53.5245 | 2026-07-01 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 6c3acd62-61f0-3222-b437-ac141462ba31 | -11.5532 | -47.4323 | 2026-07-01 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 7b0f814b-3227-3fb9-8dd7-fe636a2a6194 | -3.5043 | -48.039 | 2026-07-01 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 797a27aa-f218-3715-a550-95ff6cbdb0d8 | -10.6784 | -54.5356 | 2026-07-01 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 9ed0133a-22a5-3adf-b283-3b78cde769a9 | -11.4334 | -56.0912 | 2026-07-01 00:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| cc669b25-bb7d-3b01-9bae-e241cccdb9a0 | -10.1237 | -52.0905 | 2026-07-01 00:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 4ba1c3ec-0ecb-3525-9a76-ad22dc8db0d9 | -11.5337 | -47.4571 | 2026-07-01 00:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 123.4 |
| d636d79c-8274-3559-8457-33278b1bf674 | -12.222 | -56.5668 | 2026-07-01 00:30:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| ce4bf19e-0352-3c08-9ba7-9e395bb26648 | -12.4094 | -58.4063 | 2026-07-01 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| b9432164-7737-3baf-887d-e6530b339fa0 | -12.7751 | -44.4927 | 2026-07-01 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1113.4 |


[Clique aqui para ver as próximas entradas](README2.md)
