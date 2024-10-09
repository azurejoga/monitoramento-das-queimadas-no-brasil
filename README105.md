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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b0a9a30-2b9f-3193-ba9b-f58310909be0 | -16.66228 | -57.45093 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2d1a969a-7b37-3fea-bb9c-6c152f838490 | -16.93555 | -57.45692 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 31.2 |
| 76c11110-50a0-39ff-a31e-77bd15610d3d | -16.65725 | -57.44458 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 85313ef7-72e4-38a8-be9a-9ee6cf1d2076 | -16.65617 | -57.4495 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c3c28f5e-eb6f-343c-8120-e626869f9965 | -16.95379 | -57.46118 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 15d95b77-0028-3d1b-b2f7-d3d76776b060 | -16.95272 | -57.46604 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 14d5d3f2-1623-35e6-b00b-444ecbe6e6db | -16.95093 | -57.44519 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 98170029-9e54-3238-9f3c-f23b842ce811 | -16.94986 | -57.45005 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| b5a87685-1805-31a6-887a-775d03780d50 | -16.94879 | -57.45489 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 485dd6f1-299b-33ca-8f0e-addea9fc5d25 | -16.94771 | -57.45976 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 32572da2-50e2-313b-a272-9ffba7244305 | -16.94271 | -57.45346 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| bbaa5fef-d429-3eee-8649-f16bb817ef59 | -16.94055 | -57.46322 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 34b60ec2-4d45-3b51-8a5b-f86832086774 | -16.93948 | -57.46809 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 9a3bac6f-8a5a-3746-a5c6-d6ad1b4e938f | -16.93447 | -57.46181 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 0ecbc33e-1aff-3459-b23a-fcd237a4ca66 | -16.93339 | -57.46667 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 354b19f4-e3f7-3f81-818d-06801e988828 | -16.92876 | -57.45851 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 0f49f080-904a-3655-acee-12f379039974 | -16.9284 | -57.46037 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| af981395-3419-3ddc-a9aa-ccc680102b14 | -16.92771 | -57.46341 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| d18d1048-46f0-37fb-91f3-fbd3b6c2a000 | -16.92732 | -57.46524 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| c6eeaca9-801a-3a90-a868-979d84b8e2cf | -16.92666 | -57.46828 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| d9443e67-67c8-38f3-a41c-1cb83c7b5177 | -16.92163 | -57.46193 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 61fe7184-18d9-3a7b-8bf8-bf9c00ed071b | -16.92124 | -57.46378 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| fdbe4606-2204-37ac-b775-6826e292ac90 | -16.92058 | -57.46682 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| f4f86b96-28cf-37da-a583-34c5465b783a | -16.95343 | -57.49189 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| 24b312c5-4b4d-3f3d-9ac5-06cf2d686214 | -16.95164 | -57.47092 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| edf092da-1dc2-303f-9dfd-c72df53da709 | -16.95057 | -57.47581 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| d6426cba-39a9-3104-bad8-1d334f66bbb6 | -16.94949 | -57.4807 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| a1b1ed3c-db9e-323e-a20e-bbd0fdc42f15 | -16.94733 | -57.49048 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| 1f649564-5029-3db8-9342-76d90bdb078b | -16.94556 | -57.46951 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 4a4e6a63-2f87-3b25-9a79-ae2a693aad80 | -16.94448 | -57.4744 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 4eaceba8-52c4-3aeb-8596-d1a253749fc5 | -16.94232 | -57.48416 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 7222949a-34b3-3d51-8c9c-70fd0674bb08 | -16.94124 | -57.48906 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| b6b9b443-3f8f-300a-a607-3cb3a663012c | -16.94016 | -57.49394 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 9eb49f0e-336c-3150-8c89-d9f8cd9b7b41 | -16.9384 | -57.47296 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 105e899e-fed9-3541-8889-265e9b05ad57 | -16.93732 | -57.47784 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 7e7d6ac1-c75b-32aa-9fc4-9cd0ef6ceff9 | -16.93624 | -57.48274 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 98505476-7c7f-36ad-b028-e61d8e645ea7 | -16.93515 | -57.48765 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 8e39683e-9e76-32a1-adec-dd413bd90588 | -16.93232 | -57.47153 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| dff8f6e0-51e7-36e0-9d3c-26bef35adff1 | -16.93124 | -57.47641 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| e8c926b5-0b0d-3968-abd7-63d1f286835f | -16.92798 | -57.49112 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| cb920da3-1a57-3d25-a9c2-56e58c3545ee | -16.92689 | -57.49601 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| c00dffe6-8205-33d5-87d3-7b2044b506eb | -16.92624 | -57.47011 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| c61cd8d9-f3e8-38a4-9f51-089c95f17539 | -16.92561 | -57.47319 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 34681c0e-07f4-3f37-ba60-49a0e9de42b5 | -16.92515 | -57.475 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 5af7e4ad-2418-3739-b644-cb02a3fa0f26 | -16.92189 | -57.48969 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 8ffbce2a-069d-3ce9-89c1-91912b6d015d | -16.92138 | -57.49284 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.2 |
| 9d3abaaa-0ce2-375e-aeb4-4a9bb4bb9cd9 | -16.9208 | -57.49459 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| c11c3065-0936-3b31-9d6d-8d964dab281f | -16.91953 | -57.47173 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 831e8449-b32c-3851-9ca5-132b1b9864a9 | -17.11217 | -57.43725 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| b1ca3fda-a2da-3905-b864-1b52d060c35e | -17.11112 | -57.44206 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| d3fee809-6a39-3412-81a7-3c371f64c02b | -17.11006 | -57.44691 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 14af7645-fb5b-3701-9081-4d52ed092827 | -17.10901 | -57.45174 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 60bf5941-a252-3ef1-8874-4e0597950b51 | -17.10611 | -57.43583 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 44a16ac5-c890-35d3-a51c-c5652cfdfa0f | -17.10506 | -57.44067 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 3bab6eb2-44cd-31c6-a97e-83809a6ce85d | -17.104 | -57.4455 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| ef878823-6d5e-3435-9241-39d1dab4c849 | -17.10296 | -57.45033 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 77e1e79f-00c1-30b5-907c-5ec2667d9655 | -17.1019 | -57.45515 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| c8ba5331-34e8-3138-ac01-79abd60a256a | -17.10007 | -57.43437 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 3ef731e6-ffa8-34e2-89fb-241ceae1a119 | -17.09901 | -57.43921 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| e9058973-fe3c-35f6-94d0-9a8d58d6ef2f | -17.09795 | -57.44406 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| b0ce93bf-c021-3420-825d-19803e386b5c | -17.0969 | -57.44891 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| d1c7ec8c-132b-3c9d-ae2a-106233d56003 | -17.09402 | -57.43293 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 100f0b25-1c9a-37a8-b2e9-61339abef1c0 | -17.09296 | -57.43777 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 3865de05-724a-328e-b2a2-5b438e9e5284 | -17.0919 | -57.44262 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 64958ed5-51d6-337d-872c-fef1a2cd0b4a | -17.09084 | -57.44747 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| cba1c0bc-6d86-3a2d-9ef9-1700655f3148 | -17.08691 | -57.43635 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e9d71f95-9c1f-31cf-9708-a6ba2f3802f0 | -17.13533 | -57.44777 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.6 |
| aa6cf1d4-b791-3ca1-b2d0-efdd380ea2ed | -17.13428 | -57.45261 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.6 |
| aa3aba6c-a6ed-3330-9290-cbfd7515fe0b | -17.13241 | -57.43183 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 54ce8cd9-1606-3f81-ade6-bfaa5311f4a4 | -17.13137 | -57.43666 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 9749dd89-6495-32b9-92fa-608ac3b57861 | -17.13032 | -57.44149 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| a2fafc5f-4b15-356d-ae33-24047f9d1d2b | -17.12928 | -57.44632 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.6 |
| 6fdebc00-bcd5-30bc-a6ff-f17ce1fb5909 | -17.12823 | -57.45118 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.6 |
| b1586284-c09e-3447-aafb-5e11a120b508 | -17.12718 | -57.45602 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.1 |
| 7a8ec9f9-3f0b-3a0e-88c0-e2c740424155 | -17.12637 | -57.4304 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 698bbeff-7b76-38e3-ac49-11dc91345eae | -17.12532 | -57.43524 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| d9a43965-c607-3d47-8a59-355c5954a913 | -17.12427 | -57.44008 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 2406afb7-59fd-3ba3-8053-ecb4e270c551 | -17.12323 | -57.44489 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| d031fc10-2c03-3b99-9961-b51a86a0bf89 | -17.12218 | -57.44975 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| a58638c5-920a-3379-9b34-b820c59be945 | -17.12113 | -57.45459 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.3 |
| c1be7eaf-d131-3b2f-b33c-9535f4154a7d | -17.11927 | -57.43382 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| c4c6520a-c738-369e-a225-38c594a3a00e | -17.11822 | -57.43866 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 1600b99e-ca1e-3994-b287-9d0a3b73be40 | -17.11717 | -57.44348 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| cdf8bfa3-d033-38ea-8c6c-0d7d84b19294 | -17.11612 | -57.44832 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 51ef8d6e-b3c8-3932-9b1f-aeac071e5b8f | -17.11507 | -57.45317 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.3 |
| da19dab2-1a22-38b5-8312-aca34d8222b8 | -16.85973 | -57.45259 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4399f6c9-a7ec-390b-bb46-332e9ba709ce | -16.85364 | -57.45118 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 4714f232-e912-3420-a9f9-35c89df48a42 | -16.82716 | -57.42727 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| fdea6eb5-ecad-3f3e-8f5b-2674ebebcd72 | -16.82643 | -57.42954 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 583555a3-f0b1-3407-827c-20bb5e500d5c | -16.82612 | -57.43214 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| e2365f83-9c0a-3499-9f32-69871e8d6790 | -16.82535 | -57.43441 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0c8ae046-0b7b-37ed-b4e9-18e23e716c34 | -16.82143 | -57.42326 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c75483ee-14e1-3bb2-ac33-d7f8903f47cf | -16.82108 | -57.42583 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 36c58a81-1d12-3056-817f-198942097268 | -16.82035 | -57.42813 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8d1ff3e2-6e62-3f22-b0bc-5f3e85326e9c | -16.81535 | -57.42185 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e0e50e81-5d6c-3f0d-81e3-d2f4d56c3fdf | -16.815 | -57.4244 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6ce56054-1597-3e0d-b492-80b640643c00 | -16.81426 | -57.42672 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| bac34762-8a4d-3737-9989-dd22e91ed763 | -16.80073 | -57.43131 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8fef951c-1f87-3903-a208-7274fe3dcdec | -16.79993 | -57.43364 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 2f5098d6-7d99-3db7-a575-7ad4b66d6c08 | -16.79968 | -57.43619 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |


[Clique aqui para ver as próximas entradas](README106.md)
