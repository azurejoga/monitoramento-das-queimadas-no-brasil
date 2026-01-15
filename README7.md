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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1548ae1e-aedd-37f4-a2da-c20c3b497ce2 | 2.70153 | -60.0719 | 2026-01-15 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 688bdca2-e88a-3f02-b1d2-d6725930e278 | -2.93112 | -48.22762 | 2026-01-15 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 28677e68-25aa-346a-8b63-3d5feb851767 | 2.70343 | -60.07015 | 2026-01-15 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 838ff252-70ef-32f9-a825-2be98b876876 | -5.26281 | -44.7295 | 2026-01-15 05:01:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 411e6c45-8f2e-367e-96d0-226e56d4d63a | -5.2623 | -44.733 | 2026-01-15 05:01:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a8780fcc-939c-3017-8ebc-77610e09b0c8 | 3.70197 | -60.89953 | 2026-01-15 05:01:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9ad9ac1e-e467-39b1-aecd-1018ebda3394 | 0.05467 | -49.92638 | 2026-01-15 05:01:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7790eac6-da42-3c50-abce-3f7870c0c6b9 | -1.32489 | -47.80638 | 2026-01-15 05:01:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9dba08ba-c368-347c-8ebc-84dea2475585 | -2.92758 | -48.23379 | 2026-01-15 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65fb982c-a40a-3ee9-8f0d-d3fdb76b9e7a | -2.26346 | -47.86864 | 2026-01-15 05:01:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a39c09bf-d8ed-397a-a412-eac1299a01d4 | -5.89799 | -42.5489 | 2026-01-15 05:01:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 56cc20e9-e6f1-386f-a70a-880172fbe033 | -5.89588 | -42.55049 | 2026-01-15 05:01:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 73736238-82f6-32a2-a273-ba1d82e971e7 | -2.92997 | -48.23496 | 2026-01-15 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d94faee0-c21a-3413-b7a7-62478e80ecb4 | -0.90361 | -47.55133 | 2026-01-15 05:01:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b54f82ec-c154-3178-81ed-df5042be87d7 | -1.05188 | -47.2608 | 2026-01-15 05:01:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5c16e40-71c5-3f0c-86a7-e32c42f69b06 | 3.7015 | -60.89629 | 2026-01-15 05:01:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6b404503-a995-3d7b-ae0a-a6c6e17166f7 | -3.24008 | -41.80298 | 2026-01-15 05:01:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b98f6b3a-992e-367d-81df-cc17fe0314e7 | -2.92868 | -48.22642 | 2026-01-15 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42267e1c-4b41-3cc2-a324-2a95a126230d | -8.15325 | -43.18457 | 2026-01-15 05:03:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0704f8ed-8a56-3fd2-b487-f8969b2388cc | -12.08805 | -45.57591 | 2026-01-15 05:03:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e935502-23d2-3803-9be1-8c30f7d84dc5 | -7.61151 | -47.05867 | 2026-01-15 05:03:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c61c9966-c764-3db5-b015-b6f7075a736d | -12.12772 | -45.58099 | 2026-01-15 05:03:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec71d540-bb4a-37ea-9f9e-4f0e3272121a | -12.6549 | -46.7619 | 2026-01-15 05:03:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b98cc337-7208-3a2d-9026-6448bac65cb0 | -8.15951 | -43.18554 | 2026-01-15 05:03:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f5aeba71-d4d9-364e-b6ba-a0a221ba4124 | -12.08851 | -45.57204 | 2026-01-15 05:03:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5115c55e-ba5a-393d-af78-071208e076be | -12.66017 | -46.76263 | 2026-01-15 05:03:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92ccdb50-ec91-32c1-a502-d0343deac9fe | -12.08944 | -45.56429 | 2026-01-15 05:03:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84d92346-9c22-375d-a077-691372039cdc | -12.66057 | -46.75929 | 2026-01-15 05:03:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0edfc818-565c-3b34-911a-123b81114fb8 | -12.66127 | -46.75988 | 2026-01-15 05:03:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5d1b3859-f388-32ea-9c70-4cdfa1c87672 | -11.66485 | -43.7722 | 2026-01-15 05:03:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edad3583-a7e8-3058-91a4-93594a7facba | -8.42735 | -44.01729 | 2026-01-15 05:03:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0dd265ea-1073-33de-a2b2-90a28fa4695c | -10.59203 | -44.96935 | 2026-01-15 05:03:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e134d57c-2097-3be4-a50b-60c4534f73a4 | -8.42673 | -44.02193 | 2026-01-15 05:03:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fb5b86d-b3ec-3690-8176-05b00f0f77df | -9.37111 | -47.07938 | 2026-01-15 05:03:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 903dadc8-f8d5-3018-b777-a65771591dfe | -12.08694 | -43.76417 | 2026-01-15 05:03:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 386a4185-eae7-314b-b481-ad092f73c81d | -12.09147 | -45.3019 | 2026-01-15 05:03:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15f2c20f-5b4a-3daa-8328-2b5db5fdab3e | -12.1282 | -45.57709 | 2026-01-15 05:03:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b21a48c3-d6d7-3e7b-b108-20fcc6b73e5c | -10.59152 | -44.97342 | 2026-01-15 05:03:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fb088ee1-83a3-309d-8072-2511baccb267 | -10.31398 | -59.06054 | 2026-01-15 05:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2f20f36-745f-332e-bd23-40cea28858aa | -12.08719 | -45.28888 | 2026-01-15 05:03:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ce0dd19-9d3e-3d95-ab94-7f273c244455 | -10.31773 | -59.06116 | 2026-01-15 05:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33993417-3b78-33ad-a25a-6dbbfcb10452 | -6.887 | -42.83941 | 2026-01-15 05:03:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7b281b5c-e374-37b2-9a4c-0b8c79a3ae35 | -6.88633 | -42.84437 | 2026-01-15 05:03:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5f2537b5-cfd3-39f2-89d4-a81377b902a8 | -10.59729 | -44.97426 | 2026-01-15 05:03:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5b44c9df-cb97-3fdf-806e-d3de8289d802 | -12.65516 | -46.76572 | 2026-01-15 05:03:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fb8ffd36-5180-31aa-b155-48a93862d749 | -12.08898 | -45.56816 | 2026-01-15 05:03:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd113e25-1721-3466-839b-abce6ff9ecf0 | -12.66043 | -46.76647 | 2026-01-15 05:03:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d025dfcf-6db2-3439-8ba1-6f4e170faec4 | -12.65978 | -46.76591 | 2026-01-15 05:03:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 14d2ce7e-1177-3140-8560-ba84510b1d62 | -10.31319 | -59.06511 | 2026-01-15 05:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5d12b30-cf11-3d79-8d40-3a438963f715 | -12.09195 | -45.29774 | 2026-01-15 05:03:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c813e709-021b-3f0c-a443-812eb7484fc9 | -12.08713 | -45.28883 | 2026-01-15 05:03:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31d5a917-2ab3-3f8c-bde9-9238fa77f8e0 | -12.09144 | -45.30191 | 2026-01-15 05:03:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddae9c7e-a181-3410-b3df-bce1829618da | -12.09195 | -45.29776 | 2026-01-15 05:03:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8267964c-9f34-334f-b44c-0a68667cc5cd | -11.66545 | -43.76727 | 2026-01-15 05:03:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf5c054e-daca-3e71-8809-890dc73a83f3 | -12.66085 | -46.7632 | 2026-01-15 05:03:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c05e6f39-5af7-3f29-b410-0b25305c1575 | -11.97805 | -47.8389 | 2026-01-15 05:03:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a2633e1-7cc3-3f5d-afae-0b1a3531cf7c | -11.66747 | -43.76813 | 2026-01-15 05:03:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6a7d623-c953-31da-8464-fcea6a97c5df | -11.66113 | -43.76749 | 2026-01-15 05:03:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3a4033ac-88ea-3e32-8af2-76a44cd52861 | -12.6545 | -46.76516 | 2026-01-15 05:03:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f5864a1e-54d2-36c6-a858-95d18749ab1f | -8.15654 | -43.18338 | 2026-01-15 05:03:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7c8fe05b-670f-3f8b-838d-df4ecd3b33a6 | -8.15029 | -43.18241 | 2026-01-15 05:03:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 19b93d42-7792-3ad4-93e3-2615cca20c0b | -9.11449 | -61.48808 | 2026-01-15 05:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9efa6e51-9301-3560-96f2-970d408ea346 | -7.6106 | -47.05561 | 2026-01-15 05:03:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d448b9e1-7040-3166-ab75-ea33ecbd1090 | -12.12868 | -45.57314 | 2026-01-15 05:03:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66e7daab-912c-3975-85a1-ba4a92a97811 | -12.65557 | -46.76247 | 2026-01-15 05:03:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6856894c-2cce-3e95-ab5b-aa1c85f9d274 | -7.6099 | -47.06074 | 2026-01-15 05:03:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1b4808b-f12a-30da-8927-4eeca8f0d3d6 | -15.96507 | -58.23937 | 2026-01-15 05:05:00 | NPP-375D | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff909d4e-2506-3be5-ac98-d596f3832f1f | -14.40548 | -44.58262 | 2026-01-15 05:05:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf2f61d9-e3d5-36a3-9599-1e1f890d132d | -15.59146 | -57.34518 | 2026-01-15 05:05:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 036b6632-9fba-34be-9f10-b962013fd03d | -13.68994 | -55.67488 | 2026-01-15 05:05:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5c5450f-20c8-356d-9748-fc40532ef38c | -13.99936 | -56.07627 | 2026-01-15 05:05:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eef34275-e1ff-382d-836e-f7e83256a187 | -13.69271 | -55.67899 | 2026-01-15 05:05:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e1e8a70-9bb6-306e-b314-5f7559685964 | -14.00269 | -56.07683 | 2026-01-15 05:05:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 132cdc71-3ce9-3321-869b-3bc76f106177 | -16.59117 | -58.21585 | 2026-01-15 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9b3e9c67-deeb-340f-862c-ca16e8e0ef87 | -16.44629 | -58.16381 | 2026-01-15 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6595ba32-f1a3-3e3c-980e-4e418ca9e3cc | -15.96531 | -58.2393 | 2026-01-15 05:05:00 | NPP-375D | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38f184bd-30ca-3a1e-80da-db1842ee3d2c | -15.59205 | -57.34156 | 2026-01-15 05:05:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3032395-a323-3bdc-ba5c-257cb9978939 | -14.40492 | -44.58751 | 2026-01-15 05:05:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 742e2911-596b-37dc-949f-aa9f5fa84ebe | -14.00213 | -56.08039 | 2026-01-15 05:05:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 916dbda8-ce3e-309e-a7be-fba65d76ac47 | -13.69327 | -55.67543 | 2026-01-15 05:05:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23a02825-8eef-3b5b-b72d-84ccdf58dc41 | -17.01842 | -54.0748 | 2026-01-15 05:05:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b244dce6-ebff-3e48-a5bc-199378470d64 | -13.9988 | -56.07983 | 2026-01-15 05:05:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f614017d-aa92-302a-8fc2-3a0443f6668d | -12.83955 | -58.29885 | 2026-01-15 05:05:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 081844a8-acd4-3e3a-a34b-ee8fd0366929 | -16.32137 | -57.36108 | 2026-01-15 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| d9c37a60-5b2a-3fda-a858-5a397752e8c3 | -13.98166 | -60.3322 | 2026-01-15 05:05:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efcb3d43-f170-308b-8b46-9ef46f2b4092 | -13.68938 | -55.67844 | 2026-01-15 05:05:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b24bdb6-d6a4-35fa-b7d3-2cd15acc9c74 | -15.5954 | -57.34212 | 2026-01-15 05:05:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23b098bf-420e-3ad1-80cf-3d313733063d | -17.02197 | -54.07533 | 2026-01-15 05:05:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ef21e48-fdbb-39fe-857f-ff6232384503 | -19.34382 | -54.17973 | 2026-01-15 05:08:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4256e014-81e9-335c-b38c-bdc654f1d1bd | -21.358 | -56.86952 | 2026-01-15 05:08:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cd5feff8-b344-383a-ac2b-2d99e0f1ace0 | -20.42294 | -57.8367 | 2026-01-15 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8c756d83-7b5a-3eb4-8022-228d7c70761e | -20.40647 | -57.81095 | 2026-01-15 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| d453b192-0ac3-3c3f-8497-7d7e3bb24bff | -20.7111 | -56.45124 | 2026-01-15 05:08:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0be39616-7375-389b-aace-0e0f1906ff5f | -20.41627 | -57.8355 | 2026-01-15 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 9342b78f-6b33-3c2c-8b73-4bf572fef81f | -21.35521 | -56.86516 | 2026-01-15 05:08:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| a32f63f5-c1dd-30ba-976a-0e11ce006ac0 | -20.8449 | -51.73822 | 2026-01-15 05:08:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c4e24cd5-fcc0-3169-b0f3-b989e5376b32 | -20.27484 | -55.13172 | 2026-01-15 05:08:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef2af5e4-9d87-34d3-8dac-a23e5eda0135 | -20.71448 | -56.45182 | 2026-01-15 05:08:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16f4d06a-1d71-32a9-8e8f-41745ecca7e4 | -18.95227 | -52.37451 | 2026-01-15 05:08:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e79ab0d-612d-3b28-8b15-7dad34ca13fc | -20.41353 | -57.8312 | 2026-01-15 05:08:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |


[Clique aqui para ver as próximas entradas](README8.md)
