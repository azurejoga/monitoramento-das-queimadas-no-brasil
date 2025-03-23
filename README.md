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
| d9626145-4d78-30ec-b8d7-7955eb092074 | 2.745 | -60.3913 | 2025-03-23 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 77d1a1e5-2591-3d4d-9700-0d9fddcb8040 | -8.1075 | -43.1411 | 2025-03-23 00:00:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 83e1ac76-a9a0-33a8-a0fd-7e7a124b0f0b | 2.7267 | -60.4106 | 2025-03-23 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 95.1 |
| c7726f6b-37b0-322a-aa7c-1903ec9df1ec | 2.7449 | -60.4103 | 2025-03-23 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 845f1e04-5dbb-3286-bc4a-e523fda0c3e4 | 2.7267 | -60.3916 | 2025-03-23 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 1b90f635-5d2b-322d-b4f5-efb4665b936b | 2.7449 | -60.4103 | 2025-03-23 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.3 |
| c8b64a21-c5d5-35c6-94d2-d7e46e4eb13c | 2.7267 | -60.4106 | 2025-03-23 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 92f8cf9e-f8ec-34f2-b170-655a970f1905 | 2.7267 | -60.3916 | 2025-03-23 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 8136f6fe-2aef-3795-8df2-10532f83428f | 2.745 | -60.3913 | 2025-03-23 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 18560e1d-8b20-33d8-9559-9110d5615c3a | -8.1148 | -43.138199 | 2025-03-23 00:17:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c9fcc32f-f248-3bf7-8434-17cf30428496 | -8.0699 | -41.278801 | 2025-03-23 00:17:00 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| acb26248-423a-315e-a64f-721fa6d0266a | -12.3802 | -41.443802 | 2025-03-23 00:17:00 | METOP-C | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c591314f-aa55-3924-9536-611ae27746b6 | -11.7421 | -37.632099 | 2025-03-23 00:17:00 | METOP-C | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c99e95db-8c57-35b4-9cfe-911b2f0e5a4e | -8.1116 | -43.124401 | 2025-03-23 00:17:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d4e5590d-ca90-30f0-b83b-833dad1885bd | -11.7374 | -37.612701 | 2025-03-23 00:17:00 | METOP-C | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4d3e8e53-e958-3d65-b5db-e0fafb9791d4 | -11.0632 | -41.594299 | 2025-03-23 00:17:00 | METOP-C | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d0778df6-34d6-351c-8209-c0535d5963d1 | -11.7398 | -37.622398 | 2025-03-23 00:17:00 | METOP-C | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 89643e23-3dff-3286-924d-f1b14b4a0527 | -8.0666 | -41.264301 | 2025-03-23 00:17:00 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9b5ee81f-5d3d-3c80-8428-33aa67de5e8d | -8.1163 | -43.145 | 2025-03-23 00:17:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8f4f5466-e43f-3335-a266-0f4fd1ce2304 | -8.0683 | -41.2715 | 2025-03-23 00:17:00 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f5033e69-4ccf-30b3-a848-c4fe026f34bf | -8.1132 | -43.131302 | 2025-03-23 00:17:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ca062343-e49e-3361-8c08-ed40cfe74226 | 2.7449 | -60.4103 | 2025-03-23 00:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 3ddfb4f0-7b46-3957-a2bd-e1582f8a952e | 2.7267 | -60.4106 | 2025-03-23 00:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 100.8 |
| d14e3093-1e1d-39c2-b006-d0d1d3035e55 | 2.745 | -60.3913 | 2025-03-23 00:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.0 |
| a22e0724-c6d3-3a26-a355-2863d3d9437e | 2.7267 | -60.3916 | 2025-03-23 00:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 09ab25c3-e2ed-327d-8752-48b0d890da6e | 2.7267 | -60.3916 | 2025-03-23 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 52043f13-bb5b-373d-bee2-c472001b54dc | 2.7449 | -60.4103 | 2025-03-23 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 6692b48c-9ce4-37dc-ae87-6807117970cd | 2.745 | -60.3913 | 2025-03-23 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 3207b721-340b-316a-8ed2-005b207e6fb6 | 2.7267 | -60.4106 | 2025-03-23 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 743e3e68-23cf-3bf4-b16e-42e0fedc060d | 2.7449 | -60.4103 | 2025-03-23 00:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 4c77ea55-669b-3bb6-927a-06f541a92f49 | 2.7267 | -60.3916 | 2025-03-23 00:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 42117680-2522-3d2a-834a-2d988f94b6b7 | 2.7267 | -60.4106 | 2025-03-23 00:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 2f29449b-39de-34e9-ab29-d5137300ec03 | 2.745 | -60.3913 | 2025-03-23 00:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 02ea9da0-2a6d-3bb9-8b17-7f848eaa5b21 | 2.745 | -60.3913 | 2025-03-23 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 71.4 |
| e0c6ddad-38fd-3520-9272-d61efab0c7b8 | 2.7267 | -60.4106 | 2025-03-23 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 80.1 |
| e6a92d87-a903-3e64-a95f-d4e3a874ae4f | 2.7449 | -60.4103 | 2025-03-23 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 48e5b203-ddf4-3903-b4b0-f3832b6f1759 | 2.7267 | -60.4106 | 2025-03-23 01:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 74.0 |
| f3ee0e6a-5d62-3d6b-9428-cc6d57fe02e6 | 2.7449 | -60.4103 | 2025-03-23 01:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 86.6 |
| fcc813ab-08ad-3e34-ad27-c326305cc146 | 2.745 | -60.3913 | 2025-03-23 01:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 29ad3d05-9bf3-3981-8ef5-9a15a7c68f0a | -11.50425 | -51.95433 | 2025-03-23 01:02:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f806bed8-012d-38cd-91f9-e2f58221de24 | -11.50549 | -51.96334 | 2025-03-23 01:02:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 66f67516-b04c-3a32-8f8e-258c12326fb3 | -8.1146 | -43.14518 | 2025-03-23 01:02:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.7 |
| 555e995c-b7e5-340a-8869-0330776d4068 | -8.09881 | -43.14783 | 2025-03-23 01:02:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.4 |
| 3f2aec62-6d2d-3a31-ba2a-9e85a5cfd895 | 1.30068 | -59.99854 | 2025-03-23 01:05:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 15.5 |
| ec7e2ff8-94ee-3753-a299-fdafcc102a11 | 1.2982 | -60.01581 | 2025-03-23 01:05:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 09e30aa2-a770-3af9-a123-c8992f8bc0b6 | 2.16349 | -61.26227 | 2025-03-23 01:05:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 8bb5ad73-e310-3c91-bd9e-811f1de81840 | 2.73988 | -60.37587 | 2025-03-23 01:05:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 4461f1c6-2c8a-310d-9563-9e41dc6ca6d3 | 2.20404 | -61.35614 | 2025-03-23 01:05:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 2e7da20b-81aa-30cb-b656-de444edf47b5 | 2.16781 | -61.25724 | 2025-03-23 01:05:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 26.2 |
| db402e5e-6800-39b7-b94f-e14108855846 | 2.73472 | -60.41163 | 2025-03-23 01:05:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 148.9 |
| 777b584b-fb2e-34f2-9019-b3f834aea93c | 2.7373 | -60.39372 | 2025-03-23 01:05:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 1648f142-ec70-35e6-8ba1-d81702fd2951 | 2.7449 | -60.4103 | 2025-03-23 01:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 66.7 |
| cfb383fc-4e48-3c56-aaae-f182e9965cd6 | 2.745 | -60.3913 | 2025-03-23 01:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 1cf571dd-e353-360a-96e5-c052478d1c27 | 2.7267 | -60.3916 | 2025-03-23 01:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 061aeece-a81f-35d5-87a7-8b13890fdebe | 2.7267 | -60.4106 | 2025-03-23 01:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 0c96343f-4208-3b28-84a0-d65641beb22d | 2.745 | -60.3913 | 2025-03-23 01:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| b9ca1199-39c4-31f1-b86c-1ef293bcf1ce | 2.7449 | -60.4103 | 2025-03-23 01:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 48d9c8c0-3fb6-32e3-8ca6-06973675010d | 2.7267 | -60.4106 | 2025-03-23 01:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 63df224f-12bc-3ba6-b026-4669abcc1a05 | 2.7267 | -60.3916 | 2025-03-23 01:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 0e943278-ab74-3e63-8e0e-093bffe5094d | 2.7267 | -60.4106 | 2025-03-23 01:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 1a8a8e09-8316-3862-8134-b5a65e2146b9 | 2.745 | -60.3913 | 2025-03-23 01:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 785e1b0b-888c-3be8-9bc2-1bfc0ccb60cb | 2.7267 | -60.3916 | 2025-03-23 01:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 319dbbeb-5f30-3127-b496-d80f5d44c94c | 2.7449 | -60.4103 | 2025-03-23 01:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 2f2342a7-f457-3352-9819-496a360a5fb9 | 2.7267 | -60.3916 | 2025-03-23 01:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 8ef252c9-df8c-33e8-ab60-53d0d42f817a | 2.7449 | -60.4103 | 2025-03-23 01:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 256355aa-97a0-303f-b947-439914e8b843 | 2.745 | -60.3913 | 2025-03-23 01:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 34ecbd91-0021-306e-9fef-219f2ee2530f | 2.7267 | -60.4106 | 2025-03-23 01:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 108.7 |
| c2499688-7f46-3c84-afa0-ac6d82c70c57 | 2.7449 | -60.4103 | 2025-03-23 01:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 41ae177d-b07b-38cd-b642-8ac783a93cb7 | 2.7267 | -60.4106 | 2025-03-23 01:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 9cb7f657-9c85-3798-95b5-6f1fa16c181d | 2.745 | -60.3913 | 2025-03-23 01:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.2 |
| c2156a7f-fdfd-3707-bf36-984682ce887a | 2.7449 | -60.4103 | 2025-03-23 02:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 12ac22f2-a615-3690-9979-a3393b5591cd | 2.745 | -60.3913 | 2025-03-23 02:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 8122b4de-3634-3745-a0e6-fee913822b96 | 2.7267 | -60.4106 | 2025-03-23 02:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 72.9 |
| d8f120dd-edb7-3657-97f3-ffacfbc065f6 | 2.7267 | -60.4106 | 2025-03-23 02:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 71.6 |
| fdc05d5e-5f62-36b5-96aa-45e2a5925cbd | 2.7449 | -60.4103 | 2025-03-23 02:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 08c42979-0bf4-3ac3-b091-7e5ad45a7bc8 | 2.745 | -60.3913 | 2025-03-23 02:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 2bd57ee8-2e35-316d-bfc6-2c9ceee0e05c | 2.745 | -60.3913 | 2025-03-23 02:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 79bc0a37-be40-3343-bdd1-84f69e4fe327 | 2.7267 | -60.4106 | 2025-03-23 02:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 75.4 |
| a3eb9910-f965-335f-8c4d-b69cece75b3e | 2.7449 | -60.4103 | 2025-03-23 02:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 9893f049-0632-3c7f-90e3-63c9351b943a | 2.7267 | -60.4106 | 2025-03-23 02:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 90.2 |
| d5881afc-770f-364e-bb65-799abde7c35b | 2.7449 | -60.4103 | 2025-03-23 02:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.2 |
| fe2dac68-346c-3cba-851c-d304f52ce734 | 2.7267 | -60.3916 | 2025-03-23 02:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.8 |
| a3ecefd4-4077-388c-bc20-8e8df3506bb7 | 2.7267 | -60.4106 | 2025-03-23 02:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 801814ba-d364-3994-a6fb-2d2efe84bc13 | 2.7449 | -60.4103 | 2025-03-23 02:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 74.8 |
| feb48a54-bb87-3d59-80ff-47d7cd92e61d | 2.7267 | -60.4106 | 2025-03-23 02:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 85.9 |
| c17d122d-4321-3650-9bb4-21983565e504 | -6.5631 | -51.1126 | 2025-03-23 02:50:00 | GOES-16 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| ad64f825-ff46-318a-85b3-13f6d45cd16b | 2.7449 | -60.4103 | 2025-03-23 02:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 17f6793f-d187-3caa-ab72-c5b7fcc25b6e | 2.7267 | -60.3916 | 2025-03-23 03:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 531df6aa-c8b5-3a7f-b491-a3f84db6c9bd | 2.7267 | -60.4106 | 2025-03-23 03:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 94.0 |
| eceb8f75-d802-3d87-bd39-be563519d637 | -11.7304 | -37.62541 | 2025-03-23 03:06:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 5b9a246e-6232-3ecf-a64d-423d32638ce3 | -11.72545 | -37.61956 | 2025-03-23 03:06:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ead9218e-2d4c-38e3-8eba-dd185a664ec2 | -11.73126 | -37.62107 | 2025-03-23 03:06:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4f13d9ad-97d0-3e7e-8ecf-0fe5803421fc | 2.7267 | -60.4106 | 2025-03-23 03:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 5446aa53-beaa-3d09-aad5-80dfe81962a1 | 2.7449 | -60.4103 | 2025-03-23 03:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.7 |
| e92a97ad-03e4-3e4e-b550-5ca50d398ced | 2.7267 | -60.4106 | 2025-03-23 03:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 29916471-553b-3b35-945c-470dc7dd372c | -5.51298 | -35.60148 | 2025-03-23 03:25:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cfb71891-c97d-3a5b-a39c-236e06c33dcb | -5.18884 | -35.75844 | 2025-03-23 03:25:00 | NOAA-20 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 8307db64-f966-3397-8243-9ce651ede7a2 | -8.10603 | -43.13749 | 2025-03-23 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| fa52fabf-2852-3831-b06a-18901fd30dc2 | -8.10523 | -43.14184 | 2025-03-23 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| dfb3900d-8411-3df9-ad67-b7a21f00f4cb | -11.05987 | -41.59394 | 2025-03-23 03:28:00 | NOAA-20 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README2.md)
