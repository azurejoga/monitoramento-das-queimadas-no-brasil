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
| a1ca4f12-4c8c-3c78-9f7b-730064fb9ac5 | -21.66899 | -43.53612 | 2025-08-27 03:40:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6920ff80-904e-35ef-abd4-dec31c068326 | -19.64579 | -43.98385 | 2025-08-27 03:40:00 | NOAA-21 | CONFINS | MINAS GERAIS | Brasil | 3117876 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21207b85-f616-37f4-b44c-d6a122b79e42 | -15.08713 | -48.63193 | 2025-08-27 03:40:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e16bb057-f11b-3369-95c7-ab06d90327a2 | -20.1142 | -44.32541 | 2025-08-27 03:40:00 | NOAA-21 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6f17e572-5f4a-3d8b-83bc-bc27ed362301 | -16.70661 | -50.41669 | 2025-08-27 03:40:00 | NOAA-21 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b7b3b3a0-f018-378f-a5dd-9ee93c243111 | -16.91912 | -49.44793 | 2025-08-27 03:40:00 | NOAA-21 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2165d68f-68a3-3c30-8554-e87409a51d4a | -20.53319 | -43.96736 | 2025-08-27 03:40:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6f105a0b-e172-3599-b383-45956141b9e4 | -21.35245 | -46.89998 | 2025-08-27 03:40:00 | NOAA-21 | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 1348a202-3a5a-313f-b0c5-446085d1f5c2 | -20.05939 | -42.60444 | 2025-08-27 03:40:00 | NOAA-21 | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9d04a418-ca36-3259-a8d2-2faa11558f6d | -23.04154 | -50.32028 | 2025-08-27 03:42:00 | NOAA-21 | ANDIRÁ | PARANÁ | Brasil | 4101101 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 29899e7d-a8c8-3c9e-a61d-0b7a118a0b72 | -23.04731 | -50.31839 | 2025-08-27 03:42:00 | NOAA-21 | ANDIRÁ | PARANÁ | Brasil | 4101101 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 41626489-109d-3379-95d6-13dc11b38f82 | -23.04602 | -50.32364 | 2025-08-27 03:42:00 | NOAA-21 | ANDIRÁ | PARANÁ | Brasil | 4101101 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 08a9346f-f15e-3c8d-99bf-5deafd47d017 | -22.55045 | -49.76554 | 2025-08-27 03:42:00 | NOAA-21 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0042a713-ce62-3ba7-b848-e0b834f06a15 | -23.04756 | -50.32232 | 2025-08-27 03:42:00 | NOAA-21 | ANDIRÁ | PARANÁ | Brasil | 4101101 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a5500fe3-3d3e-3780-a587-fb69dd2b0edf | -10.2743 | -64.4907 | 2025-08-27 03:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 28.3 |
| ee531ff1-04e6-3f36-a11d-0bc31c64cf32 | -6.8228 | -58.9753 | 2025-08-27 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 2c0dff8f-a937-30a0-8d85-776fa4840615 | -6.8412 | -58.9746 | 2025-08-27 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 482639d9-252a-374f-bddb-4d821262a8ee | -9.1715 | -59.5599 | 2025-08-27 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 3dd1f430-a8b4-32d4-a858-71ea24012a92 | -9.4065 | -60.4941 | 2025-08-27 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 5147208b-b194-3ebb-9198-cac6234332c8 | -9.4062 | -60.5326 | 2025-08-27 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| b81a59bd-b86f-372a-a29b-b354456614f7 | -9.4064 | -60.5133 | 2025-08-27 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 0883c50d-ee47-3cd4-aa28-e0367b409a31 | -10.2743 | -64.4907 | 2025-08-27 04:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 28.4 |
| b6c8820c-8d25-34cb-9bec-284c2e9f7768 | -10.0977 | -62.9085 | 2025-08-27 04:00:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 7837a054-baf4-304d-a81f-751cc0af27db | -9.1715 | -59.5599 | 2025-08-27 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| e670efc8-e587-30c0-a79f-ffcd32371d7b | -9.4064 | -60.5133 | 2025-08-27 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 115.1 |
| a82f9421-bb0c-3dc4-a22d-ea39152c15ac | -6.8412 | -58.9746 | 2025-08-27 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 1ce217e7-5da9-364e-a65e-53b8cc86d669 | -10.079 | -62.9094 | 2025-08-27 04:00:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| de2725fb-9b4c-3a40-825c-058314c41990 | -9.4065 | -60.4941 | 2025-08-27 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| c8225a60-51d9-384c-a231-7ce0f81a5f5e | -6.8228 | -58.9753 | 2025-08-27 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 1ec606d7-791a-3e8f-af2e-105c0ee37726 | -9.4062 | -60.5326 | 2025-08-27 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| fa485fcf-2b7e-3d74-9373-23d06bc2727c | -3.74153 | -49.05004 | 2025-08-27 04:02:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a4b54e7c-c934-3cc0-9154-c99f3b019626 | -5.62361 | -45.72404 | 2025-08-27 04:02:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a14e5dc-e691-3ff4-b87f-641c9d240561 | -4.49748 | -46.37688 | 2025-08-27 04:02:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 313a4032-de22-381a-a5f2-726b5585bdf9 | -5.78253 | -46.14264 | 2025-08-27 04:02:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50ce7317-ec21-3b46-830a-4732c2dfdcee | -3.42179 | -49.04296 | 2025-08-27 04:02:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0c8aca02-c18f-3b33-bb79-b6a43a7a1847 | -5.10954 | -43.20999 | 2025-08-27 04:02:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3ce09acf-fcaa-3c55-8bff-baa286aeb637 | -5.49116 | -42.15778 | 2025-08-27 04:02:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| cebd480d-8859-3da9-843c-60f3307e632e | -5.10368 | -43.79306 | 2025-08-27 04:02:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57e6aac8-9433-31be-983c-45c790defb39 | -6.45645 | -35.02528 | 2025-08-27 04:02:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4f9e87b2-f16c-3c9a-9d83-6cb2de791a97 | -5.62291 | -45.72823 | 2025-08-27 04:02:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19da9487-18a0-3cf6-b8a1-0dfed0751158 | -3.98366 | -47.88342 | 2025-08-27 04:02:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 044b74e8-678e-305f-99f4-f6f0f9cecca7 | -6.30087 | -43.77031 | 2025-08-27 04:02:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7921450f-8474-3e82-80e7-922436270d57 | -3.48629 | -40.67284 | 2025-08-27 04:02:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 21542491-4bcb-32cb-9075-d68e20f9dba1 | -4.84765 | -42.88979 | 2025-08-27 04:02:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9e73b728-3656-300f-a566-31229b43d6c6 | -6.1638 | -42.61642 | 2025-08-27 04:02:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f19ec656-089e-38d3-a633-1ca3cf7e84e2 | -4.47938 | -47.66681 | 2025-08-27 04:02:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2434f25-9b8b-3f6b-b8b8-68a94d607938 | -4.67948 | -41.02889 | 2025-08-27 04:02:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2f44186b-f576-3c90-b2e8-e04c0b7810b7 | -6.12779 | -42.95391 | 2025-08-27 04:02:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| ea2f24bf-ca60-3584-b20e-91e82fae4fab | -4.67666 | -41.02466 | 2025-08-27 04:02:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2b59780a-3232-3d99-b3f5-e0a31fd2f3ae | -4.85058 | -42.88857 | 2025-08-27 04:02:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4691bb08-afd7-3bb9-a879-864bb029340e | -5.6619 | -47.49374 | 2025-08-27 04:02:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ebfad727-d165-3a99-a20c-71ecde37dfe7 | -6.19145 | -44.17019 | 2025-08-27 04:02:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 366bc8d9-08ab-3f1c-8d0e-ca2160249a6a | -6.18907 | -43.01373 | 2025-08-27 04:02:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ad3427d-95fe-37a9-bf2b-b65ce64c4fde | -3.97854 | -51.06331 | 2025-08-27 04:02:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8668cd34-b570-323e-b48a-913dda6c6637 | -5.13458 | -43.22543 | 2025-08-27 04:02:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7f360c7e-f701-3185-8d8d-16e03d24cb84 | -5.11398 | -43.20618 | 2025-08-27 04:02:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 22676c0f-d789-34ef-9279-9695a6b8b8b9 | -6.12846 | -42.9497 | 2025-08-27 04:02:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 7d891b33-6c43-369d-84b6-2bbfd1d37483 | -5.09981 | -43.79245 | 2025-08-27 04:02:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a03ffa38-9465-31ee-a716-fe1e5259b52e | -6.13209 | -42.95034 | 2025-08-27 04:02:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 3bf9c1d5-0989-3eee-9cf4-122f06db6536 | -5.62793 | -45.72485 | 2025-08-27 04:02:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9d4465b-1bb2-363b-ba63-6dea96b1b0e3 | -5.47312 | -42.59848 | 2025-08-27 04:02:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| f4d71f54-767d-3195-b394-23fbd2a013fb | -5.62723 | -45.72903 | 2025-08-27 04:02:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66d71089-b9fb-38f1-8083-1093e2eb15a7 | -3.7371 | -48.94236 | 2025-08-27 04:02:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 491a6434-2821-3cda-ab96-b416a02ef0c8 | -5.11701 | -43.21118 | 2025-08-27 04:02:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a0052b57-a81e-378f-81e6-d11435564b22 | -6.29253 | -43.77369 | 2025-08-27 04:02:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7141f672-67eb-3072-a4bd-4f54cba068a2 | -6.16737 | -42.61698 | 2025-08-27 04:02:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 877a6e82-cef7-346d-abc6-0cac933ff9bb | -5.25345 | -43.34854 | 2025-08-27 04:02:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f980fbcc-27a5-3101-89a3-c8ba3febfcb1 | -3.35994 | -43.36866 | 2025-08-27 04:02:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1aa597e6-f299-3514-90c6-533584e6cee2 | -5.11026 | -43.20556 | 2025-08-27 04:02:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 93a3486c-c4cf-3cca-a4eb-2d450b365394 | -6.29104 | -43.78276 | 2025-08-27 04:02:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09d87fcf-5de2-3002-8a84-5c4e92a427ad | -3.97942 | -51.05822 | 2025-08-27 04:02:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcb0c6c5-5aeb-3688-a0b6-05f1737c8512 | -5.94848 | -42.49632 | 2025-08-27 04:02:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 22580512-d0e2-36ec-9fc2-20dc1716a724 | -5.50591 | -36.67317 | 2025-08-27 04:02:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e144047b-4916-37a5-b9df-43e7b69e9b53 | -5.79871 | -42.28578 | 2025-08-27 04:02:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 32380b0a-c165-36ca-8ab2-a89921e5010b | -3.91924 | -47.69057 | 2025-08-27 04:02:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 052b7a4f-6ace-3681-9caf-8e772fc525bb | -5.8635 | -42.90405 | 2025-08-27 04:02:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3a43d1d6-7e44-3c10-921d-cc3c6f800fbd | -5.16798 | -37.63995 | 2025-08-27 04:02:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cbb50986-a74a-329b-9489-7a39fc787181 | -6.29179 | -43.77821 | 2025-08-27 04:02:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70a1ce26-b141-3b5a-8854-5d3f83a5b28e | -5.9527 | -42.49285 | 2025-08-27 04:02:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 05af3cab-33b2-32f2-a26e-6b49f0049247 | -7.55494 | -35.19112 | 2025-08-27 04:02:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 15d5a4df-ab2c-307a-baaa-26e5ff36196f | -4.48548 | -47.66945 | 2025-08-27 04:02:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 283c76e8-743f-3619-b5dd-6095f0a1d5d7 | -5.11815 | -43.20908 | 2025-08-27 04:02:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| cf546601-8126-3c18-ac95-39547d77522c | -5.74776 | -40.4416 | 2025-08-27 04:02:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e07e95ac-5b6b-3dd5-ab8c-2df6768fff56 | -3.98312 | -47.88661 | 2025-08-27 04:02:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bee7cada-54d1-3f5d-9a62-7094a7d9c5ac | -4.31248 | -48.0987 | 2025-08-27 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 49f1e3a2-21ec-3a11-bf80-64eab2588943 | -4.31714 | -48.10276 | 2025-08-27 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a6ae829-7ec4-31d3-add4-d3445c95b35b | -6.20554 | -44.15748 | 2025-08-27 04:02:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b81f5b6-74a0-3d71-8493-8976daf83c1f | -6.19222 | -44.16555 | 2025-08-27 04:02:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33ec9dc4-5ff7-3a10-9d35-b667d2b6aab8 | -3.73154 | -48.94137 | 2025-08-27 04:02:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7da4b9e0-d15f-3097-afaa-ea8d90f013eb | -4.49646 | -46.3754 | 2025-08-27 04:02:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fc351e87-8849-3dcb-a90f-64dafcad3c6f | -6.18975 | -43.00957 | 2025-08-27 04:02:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0ad6adc2-201f-31cf-8f69-b67af29ee8df | -6.13187 | -42.9531 | 2025-08-27 04:02:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a9769652-dff7-30ac-a84c-6b6742e59afc | -5.59562 | -46.33741 | 2025-08-27 04:02:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae12f0ff-64a4-3117-9b44-18ca34fe191f | -4.3166 | -48.10591 | 2025-08-27 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a90e8987-fb70-31f8-a2c9-ac179a645677 | -6.28723 | -43.78223 | 2025-08-27 04:02:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 366cc5d8-6107-3f3d-8719-bd88dd770353 | -6.14358 | -42.97243 | 2025-08-27 04:02:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 66b749f4-cac4-3a96-8557-b7df416ed139 | -3.97621 | -43.24518 | 2025-08-27 04:02:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6e430c0e-0e44-3662-aafd-da6e46d9257c | -5.50746 | -36.67837 | 2025-08-27 04:02:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b683d093-e3c6-357e-8820-b5e9ee28dfa7 | -5.11772 | -43.20675 | 2025-08-27 04:02:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3be811aa-7a46-3698-bf79-fdf858b297f9 | -5.87535 | -42.41585 | 2025-08-27 04:02:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README24.md)
