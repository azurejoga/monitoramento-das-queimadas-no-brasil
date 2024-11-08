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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96bea43c-5c8f-3fcc-be45-5769d39ba175 | -5.39839 | -45.13229 | 2024-11-08 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b34bb49-5892-3324-8883-2936f1fdf94f | -4.24583 | -48.53996 | 2024-11-08 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2102610e-1797-3f80-9bb3-a27582c6161c | -3.96689 | -48.17484 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6266180c-d5d8-3513-9015-ceb0508527f5 | -3.97209 | -48.1757 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8c11140d-0d7e-32ca-b325-df50b1440522 | -3.58693 | -50.27459 | 2024-11-08 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1d47da93-1cbe-33eb-952e-f0c5c66fe064 | -3.55423 | -47.37583 | 2024-11-08 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 68d6701f-e446-341d-a12c-5afb53ebfd36 | -5.58459 | -41.68258 | 2024-11-08 03:57:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f3014cde-9ec5-3aee-8dd1-61e1f88f6522 | -4.60738 | -49.57914 | 2024-11-08 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9aca1ec3-1bbd-3206-a8f5-5dccd5e7529e | -4.60671 | -49.583 | 2024-11-08 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36ade0aa-5eb8-3ac7-a856-56e82e2ddb51 | -1.61786 | -47.35624 | 2024-11-08 03:57:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40673ae7-166c-3dc9-b2ba-bbb91ef28b94 | -1.65707 | -47.9141 | 2024-11-08 03:57:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a3a3432f-90ad-3e14-9ce1-759a48d8754a | -2.63666 | -46.77197 | 2024-11-08 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b43fee7b-1d1d-31c1-9d0e-417f649554b4 | -4.87323 | -45.73368 | 2024-11-08 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9932013b-9969-37a8-93b2-d020e59db842 | -4.24526 | -48.54344 | 2024-11-08 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cb04ac9-82b0-3b4f-a305-29fd01c70ed0 | -5.4788 | -42.0797 | 2024-11-08 03:57:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b25f29a6-aeba-3bcb-8b40-2cd547f4088c | -3.9492 | -48.15267 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55987055-d979-37be-9554-59d324f43862 | -3.78949 | -44.02009 | 2024-11-08 03:57:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7fe1b1a7-ad96-3a68-b7f1-017454397fc7 | -5.58117 | -41.68203 | 2024-11-08 03:57:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5077a304-2b62-3fac-8508-c5f7b51b4fb3 | -0.64222 | -52.39698 | 2024-11-08 03:57:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6112e86-e714-3309-a4cf-46e989a2dab9 | -4.21962 | -47.38881 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce95f1e6-f8b4-37fd-80b9-bbf4657d8c67 | -4.13202 | -43.59481 | 2024-11-08 03:57:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e69db15-8e5b-3e2d-ab45-6d1e3c83295a | -3.96638 | -48.17791 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bb24b54c-cc5d-3a78-bcdc-b4cdf80ce754 | -3.9503 | -48.14606 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36c3a57c-367f-3679-a24c-974e45c8628d | -3.22569 | -46.01731 | 2024-11-08 03:57:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2d0a286-fa16-3a45-a048-b09801941693 | -4.10584 | -48.5043 | 2024-11-08 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38720894-97a1-3cd9-8b53-a61d38d26b6f | -6.26505 | -39.37185 | 2024-11-08 03:57:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5b7d0a60-bff8-3345-bb29-2e693a2b8ece | -4.24492 | -48.53638 | 2024-11-08 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40a1d7b2-730d-3237-9f86-7de25d313e6f | -3.55831 | -47.38205 | 2024-11-08 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| c60e81ee-9911-38a6-abe9-58ef389e9ac0 | -4.51601 | -45.68528 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 99410844-d4d1-39e6-a7f5-4bf313aa86b2 | -4.77026 | -48.67951 | 2024-11-08 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c53973b8-c720-33b2-bbe9-9ed650fbe714 | -0.64341 | -52.38968 | 2024-11-08 03:57:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3896d48-76c3-34ae-bbca-d8d97513b2c5 | -4.13419 | -38.70533 | 2024-11-08 03:57:00 | NOAA-20 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cf591c0c-482d-394b-b1a5-a6a5141121df | -4.11111 | -48.50537 | 2024-11-08 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd4219f4-b299-3cf4-90e4-b0c1eeaa2c40 | -3.54255 | -44.97195 | 2024-11-08 03:57:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52c4091a-e575-3f9f-a4c0-e43ed4510898 | -0.92577 | -47.1326 | 2024-11-08 03:57:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36067eb0-2456-36da-a992-012f894e9f76 | -4.60863 | -40.56924 | 2024-11-08 03:57:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 5b8a52c3-eb4b-3759-9610-d10550f25664 | -5.65155 | -37.45481 | 2024-11-08 03:57:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0b0dce8d-4d9a-3f77-9172-9984f11c18f4 | -3.79654 | -44.02373 | 2024-11-08 03:57:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 50c49726-596f-3ee2-890f-a2a2bb098325 | -5.74459 | -35.55931 | 2024-11-08 03:57:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1bdb98f2-b803-3ebe-b1e0-79b618b62074 | -4.21685 | -45.06284 | 2024-11-08 03:57:00 | NOAA-20 | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3679a79-6918-3ee7-a309-0e544e366ec3 | -4.47295 | -48.11756 | 2024-11-08 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e3375a1-85cf-328d-a09b-e446d8cc4088 | -3.80864 | -47.79583 | 2024-11-08 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9710b714-1614-3c28-be88-c78a702ab112 | -3.53957 | -43.62103 | 2024-11-08 03:57:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74c63c48-fa4b-3ab7-b850-0aae607ff164 | -3.68503 | -39.42631 | 2024-11-08 03:57:00 | NOAA-20 | UMIRIM | CEARÁ | Brasil | 2313757 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8841fd87-ee7d-38f2-a8db-ad2dfcea5b74 | -3.71052 | -49.00594 | 2024-11-08 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4b09ca7-6715-374f-94ca-088187edcae3 | -4.77466 | -45.89119 | 2024-11-08 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 851bd6c0-b9cd-3966-acc1-ecbc298bdd41 | -4.324 | -44.84058 | 2024-11-08 03:57:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a15d2347-0756-34b0-b0d4-0f922c50d2e5 | -3.79262 | -44.02304 | 2024-11-08 03:57:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a4e7dcca-4495-37b8-bed1-ce8528ed9c3b | -3.93703 | -47.1863 | 2024-11-08 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fbbc63e-20c8-3bda-a5ed-b722eba4ac4d | -5.50762 | -43.79264 | 2024-11-08 03:57:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8854611f-7cb5-3d2e-ab49-119fe685c4e5 | -2.71307 | -45.70233 | 2024-11-08 03:57:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30d22812-4eeb-322c-b564-3596af7f9718 | -3.9674 | -48.17175 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6255ffd1-7f6f-36b3-9512-653535115203 | -3.86391 | -40.76792 | 2024-11-08 03:57:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4e87668f-33eb-319e-a7bc-93beb0bd8b91 | -3.74928 | -52.10737 | 2024-11-08 03:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 696d2904-e938-389d-b4ba-11481b399b0c | -4.15558 | -45.92254 | 2024-11-08 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 973a3f19-ba50-34b8-85a9-b582c5abfe4c | -2.89099 | -41.76881 | 2024-11-08 03:57:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0cc0de7-f5b6-308a-98a9-2971328a6d83 | -4.93722 | -43.62778 | 2024-11-08 03:57:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eca5b9f2-35a1-3236-895f-ea818046e380 | -4.6993 | -38.4562 | 2024-11-08 03:57:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c49d92e6-68f3-3bba-934b-888ffc2d3d06 | -4.51391 | -45.69769 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 201027d8-5139-32cf-aa43-d7a851d543f3 | -2.7086 | -45.70156 | 2024-11-08 03:57:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f68e74c2-5b9f-3a28-b2d6-a0fa5573cd18 | -4.22961 | -46.90984 | 2024-11-08 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4325ecb1-b19c-34f1-aab2-2cab1639a907 | -3.96792 | -48.16858 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce906faa-95d2-39c5-aa09-20a604e9356a | -3.79571 | -44.02874 | 2024-11-08 03:57:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af5ec119-3293-3181-9814-764b74a3187b | -4.21671 | -45.74635 | 2024-11-08 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce8fe063-0dda-338e-b10f-b82cb87822db | -4.16651 | -47.46534 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e98a198-daa4-3014-b0ad-ec2c458e0cf5 | -4.5115 | -45.6786 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 15fe3ca9-8a65-3260-9dac-4eab4c28d794 | -3.79734 | -44.02147 | 2024-11-08 03:57:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a18c24f8-70f3-39c9-ae8c-143c04eb1dd3 | -1.61274 | -47.35545 | 2024-11-08 03:57:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 327e1941-7bf6-3614-b21b-e35c26bd8b1b | -2.20711 | -46.36433 | 2024-11-08 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a9e7bfed-8bc6-3fd7-90da-e2bf5dc4b402 | -4.51309 | -45.6761 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 7b378933-9b0b-3d3a-81de-f1129afffd68 | -3.96845 | -48.16537 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cbb329cb-52ef-3e4d-a5b9-9b1635375e3c | -1.14417 | -52.00935 | 2024-11-08 03:57:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 821470ab-4c81-30c3-8ebd-779c2953310e | -4.21484 | -48.56214 | 2024-11-08 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79fb7b8e-3cf9-31a4-8865-b8849ffbb517 | -4.13266 | -46.90101 | 2024-11-08 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c8240cd-515e-3af2-b801-c8ccfdae2df2 | -4.31926 | -44.84361 | 2024-11-08 03:57:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af9ae1b5-9e07-3cc1-80ff-e7e3172b209e | -5.57615 | -43.70502 | 2024-11-08 03:57:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b304be89-b7e6-3be8-911a-85036ac42db5 | -5.39901 | -45.12859 | 2024-11-08 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdde3a47-3832-360c-8210-1e9adf392797 | -4.78404 | -45.40752 | 2024-11-08 03:57:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45354cac-67c8-3285-b2e3-cc96692939ae | -5.33106 | -44.03738 | 2024-11-08 03:57:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ef5a50bb-5eb2-3a3f-9bf1-a0c9555057a2 | -1.15215 | -52.00398 | 2024-11-08 03:57:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3b521891-872e-36ca-8456-b65fd533962c | -3.71437 | -41.69056 | 2024-11-08 03:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 2fb5f4fc-6b55-345e-8033-347f5bcb8d47 | -4.18743 | -40.67656 | 2024-11-08 03:57:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 118e20ba-251b-33ef-846d-1894e1d59013 | -3.71784 | -41.69112 | 2024-11-08 03:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| b95f8c0a-af94-387e-b63d-5395713e3729 | -4.14631 | -44.42355 | 2024-11-08 03:57:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a96a6baa-dff6-3f52-be5f-03b43610dc0a | -3.25091 | -46.46878 | 2024-11-08 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06bbad5c-385a-3105-ba3a-6c7048ec110d | -5.5424 | -41.68339 | 2024-11-08 03:57:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| d316614a-e1b4-3b24-88a9-3cb4872c5eaa | -6.26559 | -39.36838 | 2024-11-08 03:57:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5e857208-e58a-306a-b26f-e036e7e4ecd7 | -4.56025 | -46.34055 | 2024-11-08 03:57:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa7ead7b-f913-3bbc-8f01-f906f5aa2e91 | -2.92853 | -45.15066 | 2024-11-08 03:57:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50139583-0af0-3571-9ecd-a4de7cf93183 | -4.61936 | -46.52119 | 2024-11-08 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26a54143-9ff5-36d2-a78b-9c7e1fd667c1 | -3.81197 | -40.96481 | 2024-11-08 03:57:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b7061f34-af88-3e8e-b3e4-c4bd607dd993 | -3.79654 | -44.02648 | 2024-11-08 03:57:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c53d91b1-12c3-3302-82ed-de2279d7fdb3 | -4.61253 | -40.56625 | 2024-11-08 03:57:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 6d68c175-df92-34c3-a925-e4952621d6a9 | -4.14286 | -44.41939 | 2024-11-08 03:57:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47626db6-56cd-343a-a36f-a6565a1f3349 | -0.92933 | -47.13176 | 2024-11-08 03:57:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e256b1e4-9a83-3407-b28a-616ef121701a | -4.48939 | -48.11401 | 2024-11-08 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7ab94b26-07dc-321a-a249-809df3c789d5 | -4.67762 | -46.45397 | 2024-11-08 03:57:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 276a7db0-6064-3415-bf53-062049322c19 | -5.17021 | -44.22946 | 2024-11-08 03:57:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 890f9e94-4d6b-3ce8-8207-29ccdb2f9bc0 | -2.1696 | -46.44642 | 2024-11-08 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 458b88b2-3b91-3f10-be80-83d86714ed85 | -4.23846 | -46.52349 | 2024-11-08 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README16.md)
