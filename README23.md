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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee820a8a-8a1e-3066-a211-73d94f13f0d4 | -8.91055 | -60.58012 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ffcd2d9-8138-30e5-89e7-8b5e3b3129c5 | -14.53397 | -52.78978 | 2025-08-07 05:21:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2fb8fd9a-eeb0-307f-9c50-457d2d12f6da | -9.93564 | -60.47195 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f8787c8-0f6e-39b2-9843-64feda5db5e2 | -8.91727 | -60.58122 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 092c265c-f575-343d-a329-7714a63c94ec | -8.90883 | -60.59085 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfe30de0-f94d-3c7a-9082-f254d6b46067 | -8.90622 | -60.54271 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7095e960-09c7-363a-a75a-6d5212822a4e | -9.93677 | -60.46486 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0495d343-3be7-3699-9360-6ee3a996a8da | -9.71038 | -61.29846 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 078e8531-09fb-330e-9240-a55342a3497c | -8.92752 | -60.74128 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| cd662e23-065b-349a-995c-0862d5a19153 | -8.91741 | -60.73962 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 068f0c01-ec4b-31ae-8d53-6b99c21e598d | -11.9064 | -54.78158 | 2025-08-07 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b93b6fbe-112f-3f7a-b1d6-427b981de510 | -9.94386 | -60.50603 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1fb40758-e83b-3090-935b-392761038646 | -11.33085 | -58.58204 | 2025-08-07 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c00fbfaa-309d-3dd9-b2fe-48331f1a6822 | -8.90449 | -60.55344 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cae51a2f-f863-3721-a778-7469190d7cb4 | -9.70977 | -61.30216 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eee04b66-f554-3c08-9164-d38ab98f1941 | -10.35108 | -57.50464 | 2025-08-07 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01422185-f6a7-32a8-863f-d026d8660e0f | -9.93612 | -60.49021 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62259965-cfa9-3c21-b1b7-db199f226c90 | -8.91735 | -60.5592 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d65f7fd2-6a9d-34d7-ac78-01458f1747e6 | -12.33623 | -46.0634 | 2025-08-07 05:21:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46f874a3-739f-3584-8cf6-f76f4f90d8bb | -8.92078 | -60.74018 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8c6d073c-ffa9-3508-971d-00b67df59b1d | -9.94109 | -60.50193 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f6a9233-40e5-31d9-9e8d-7ee34bb36a9e | -8.91449 | -60.5771 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b27146e-46be-304b-838c-15e477d264df | -9.46867 | -57.85176 | 2025-08-07 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 062e0fa2-f2be-34cc-9d61-642a11e42c1d | -8.91498 | -60.59552 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a85311bc-1235-3ed7-af57-c0c5a07ab857 | -8.92006 | -60.58534 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2cde082-24de-328f-89e7-d844aa995377 | -9.94231 | -60.47304 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5d201d6-4f36-3f41-9b3a-d64719439a72 | -8.91493 | -60.74683 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94c8b41c-a8ff-36f1-820c-9fd7273b84f1 | -8.90375 | -60.60104 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cc3f3b4-c874-3372-b644-4785cd1b51ae | -8.90383 | -60.57903 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5feaccd-dae1-3860-a110-0cb6c2696790 | -10.70716 | -48.86432 | 2025-08-07 05:21:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 779561f2-ade2-3835-bb54-413c609d3908 | -8.92186 | -60.5526 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84d4af2f-b2d3-3a07-800a-fd00cf2d9513 | -8.9185 | -60.55205 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3cca56c-e58e-38a5-8d1a-700ee722e8f3 | -8.92239 | -60.75156 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 27bfd8c4-decb-30ff-9295-410faf98d86a | -8.92506 | -60.59716 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8569fef1-2971-3a59-a5b3-b71d48dfa3bb | -12.37677 | -47.04411 | 2025-08-07 05:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c07da394-742c-344e-8642-710b8dfd0473 | -8.91834 | -60.59607 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4fc005f-e9c9-3ea1-9ec1-ea0fd8b660b0 | -8.914 | -60.55865 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce01adf1-5ce9-38fd-b124-2331ed65ba9e | -9.93031 | -60.49316 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2772490-3f68-36ab-9f62-d1d8ace586c1 | -12.52589 | -47.15093 | 2025-08-07 05:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 88fc464c-20be-3cee-8b71-7edbe6d52337 | -8.90785 | -60.55399 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ca9fd5b0-a58c-3d12-801c-8bd38e6bfed8 | -10.64218 | -55.31273 | 2025-08-07 05:21:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d4ae44c-0f53-325c-b39b-b82259fbb7e6 | -8.90277 | -60.56417 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ba2c214-cd54-3743-8850-f33b10a711ab | -8.92063 | -60.58177 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65940a94-7192-3b67-b316-3ad6863b4aae | -12.5462 | -47.15512 | 2025-08-07 05:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4993530a-f5af-3674-bf32-33f9ffd0222c | -8.92228 | -60.59304 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91f3a92f-f186-3d76-b8f7-c79ce86881ef | -8.91064 | -60.55811 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab6d0f72-4d2d-31cd-8af1-6d3fbcae72bc | -7.39802 | -60.00867 | 2025-08-07 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d835b925-3076-365e-a4b6-01a5cca8e4d6 | -11.18302 | -51.44443 | 2025-08-07 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2e273d2-db68-322d-bef6-94bf46ebde63 | -8.91678 | -60.56277 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de975ce9-9d6d-3ca6-a299-78d5431e8430 | -8.91843 | -60.75461 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5c7b0d9f-2e12-3c02-8aad-38fe3b6c1ea7 | -7.40528 | -60.0062 | 2025-08-07 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b6f63303-6de3-35e7-95d5-45744ed3fbbb | -14.53885 | -52.79052 | 2025-08-07 05:21:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93ecb69f-5b1b-315e-a448-bb08bec32307 | -8.9235 | -60.56387 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35b64f28-ed3c-3f84-96e9-87011f817aa1 | -7.40471 | -60.00974 | 2025-08-07 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8bd847d7-4b23-3cd7-be36-2f9ad91c203e | -7.40081 | -60.01274 | 2025-08-07 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2a2923ba-7fc5-383f-9557-9ebf0c98abd3 | -8.91609 | -60.7396 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 403fe111-1bd2-3b88-b58d-291404c080cb | -8.91726 | -60.76182 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| baf5ebe8-99b4-38bb-8ec8-366adea850be | -7.43266 | -60.01752 | 2025-08-07 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fcb34f98-ec41-39a0-81a1-5ccc50e44b05 | -8.91719 | -60.60323 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59c0639a-af62-37c9-a318-1c89299ae327 | -10.70658 | -48.86893 | 2025-08-07 05:21:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6d1275f-3ef2-3840-acd8-fad9ee979133 | -8.90555 | -60.56831 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3563a298-3705-3744-9926-3bc41627a920 | -8.90768 | -60.598 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f824178-0da0-3344-950e-2e5286e43158 | -8.90613 | -60.56472 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bf4eeaa-59da-37dc-b0c4-241c2fda4f14 | -8.91629 | -60.54434 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9504cb7f-d40e-32e8-9222-d45c792e0ce4 | -9.70879 | -61.28683 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7613540b-e501-3fb2-9b69-8974fbbdde0a | -8.91391 | -60.58068 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3df481a-3ec1-3833-91f7-c5b69b01f00f | -7.39858 | -60.00515 | 2025-08-07 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 1036ba4a-d466-389e-8d90-02df35b45411 | -9.26386 | -60.77705 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a4cab23-86d0-3aa0-af6f-13a2b7161779 | -8.91777 | -60.59964 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 668e17ff-f144-36dc-b62b-47ac3482326b | -8.92063 | -60.76237 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2e342a76-58ec-3962-ac85-eab44155f542 | -11.76081 | -48.19045 | 2025-08-07 05:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 96221c32-7efe-314d-bfff-c2e073d8e1c9 | -8.92243 | -60.54901 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b125f3be-0c09-3688-ab75-17e917afee9f | -12.51844 | -47.14427 | 2025-08-07 05:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 136cd3ca-cf77-30f4-89f8-975eab400750 | -12.33685 | -46.05069 | 2025-08-07 05:21:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6889da5-865d-3b55-8943-952acf40195f | -8.90728 | -60.55756 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 571ffd1b-d500-307a-97ea-4133db748093 | -12.51974 | -47.14373 | 2025-08-07 05:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 373d7cb8-6e3a-3ca4-bd1f-3b7719cbc3b8 | -8.91624 | -60.74683 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d75ebb71-ac2f-37b6-86bd-78fd5eb4d174 | -9.01794 | -51.11664 | 2025-08-07 05:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05c94bb6-8cf6-3286-b507-d69b10dabcd4 | -8.91793 | -60.55562 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b95580cd-9dbb-3db1-bb4b-4cf859d09a76 | -10.05965 | -64.99738 | 2025-08-07 05:21:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7051f56b-da7d-3d82-8ac7-2adbc355f9c4 | -13.71705 | -53.85656 | 2025-08-07 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 040c4839-aa86-3e67-83d6-20baec7e2240 | -9.93661 | -60.50847 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 934ca607-cd0f-3a1c-8445-64b51601c624 | -9.9337 | -60.47189 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e11dcbd9-7ae1-336b-8b7b-f9874cebbdeb | -8.92356 | -60.74434 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 6300a621-5686-364f-9115-413d61d14990 | -12.51291 | -47.14286 | 2025-08-07 05:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d1555db-0071-3125-bfcc-dfd3a2483a50 | -9.70417 | -61.29363 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ba4a9bd0-305d-37b6-bbbc-954e5f59311a | -8.91613 | -60.58838 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f37e3af-5ea3-36d1-97f3-272603a68e18 | -8.91351 | -60.54022 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d841fa06-d525-374b-b32c-1d67595883db | -7.40137 | -60.00921 | 2025-08-07 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0b46451b-ff28-31de-a51a-7c4cf6f43081 | -8.90335 | -60.5606 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c96ef4e5-2c70-38de-8912-0a703929de54 | -8.909 | -60.54683 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1c57abc7-db58-3804-9d52-c6468643592c | -12.5395 | -47.15306 | 2025-08-07 05:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d6b8b2e8-2f0e-3dd7-8cf0-6bea525c0aab | -8.91667 | -60.76543 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efb31b74-065f-32c9-b5dc-5dd4282a2c32 | -9.93897 | -60.47249 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3982774-3433-3bf1-b5b8-deae56170893 | -12.51905 | -47.15009 | 2025-08-07 05:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 127193fb-d485-3748-8c1c-a7ebe5864845 | -9.70357 | -61.29733 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3773a59b-1b9a-3c17-9f28-c2bd644b0419 | -9.93734 | -60.46133 | 2025-08-07 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0e4966e-fd9a-334c-8b63-617ab816bab7 | -13.05549 | -56.85623 | 2025-08-07 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 025ba9a6-7b3e-34ba-8387-b19be907862e | -11.18773 | -51.44817 | 2025-08-07 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29cba95b-8a47-37b2-bd3b-73a046791e91 | -8.91902 | -60.751 | 2025-08-07 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README24.md)
