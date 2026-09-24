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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b559c94f-6ecb-3f65-bca1-6da68248c8d7 | -6.61752 | -59.91386 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ec43cad-eaf2-3ad0-b586-a6f9cf7e4f08 | -6.46306 | -55.0006 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4661a515-cf08-3908-a7de-fba21ec76480 | -1.27517 | -57.03582 | 2026-09-24 05:04:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a90f1729-5bce-3df4-98da-892c3f76bf32 | -1.63061 | -54.91865 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 545c861c-3227-389b-9118-6323b59a00b1 | -8.59462 | -54.62637 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dba2d997-26d4-359c-a3c9-888fc5633518 | -5.8407 | -53.84809 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68b069e9-de52-33d5-b1e1-b783695f4c2c | -4.45038 | -55.02814 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bc8ad8d-3310-321c-937d-240f4a0bf895 | -6.51449 | -55.36071 | 2026-09-24 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1863cd13-2b41-3364-9d2b-4c707426253a | -6.71411 | -58.99995 | 2026-09-24 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 238146f3-ae2d-37fc-b34c-3be0f562ce0e | -5.59444 | -60.19663 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 435549c2-4f41-3e97-901b-1053ed520135 | -7.42747 | -49.86615 | 2026-09-24 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7e966433-71ed-3c3a-89f4-577ded25617c | -6.46143 | -59.99264 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7845ef5c-3786-3971-813b-1395731286d4 | -3.07367 | -54.394 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10f78165-5def-3ddd-9d6e-318a958dccb9 | -10.07378 | -46.01405 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5d277b2-e425-3b54-b377-43bdef10ae11 | -5.3732 | -56.05052 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d0d765f-2063-3e9e-8dfe-840912beb7fb | -2.71354 | -57.51463 | 2026-09-24 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1181d0e1-b06f-3f69-ad28-0b35c1737553 | -5.59377 | -60.20065 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 646f2cf6-fc74-393c-84a8-19c821cf1255 | -8.38952 | -46.29856 | 2026-09-24 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9dd9ae91-b740-3fc8-a9ba-9d25d7a9fc36 | -4.373 | -55.27428 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a06b90dc-3b20-37ad-92c5-a78bf184ecb2 | -3.44838 | -50.06974 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c82d23bf-82b5-3676-b34a-e0375878e1dc | -3.68125 | -60.58128 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e62eb80a-1355-3238-bcf1-49277e72e7e5 | -1.25573 | -54.2257 | 2026-09-24 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ac5e0bb-c147-3a3f-bc30-65bf5c6c4172 | -4.47388 | -54.96688 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 378dcd1f-b13b-33b7-be1a-9965628f3432 | -4.87298 | -55.84707 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8b31f3f-cdd0-30e9-bf8e-f2e5a9a668d7 | -6.66988 | -58.55415 | 2026-09-24 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29d809f7-994f-3261-bd69-45fd68bda7f0 | -2.97524 | -50.39297 | 2026-09-24 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15999f22-9f3f-3adf-a180-c6c364370bfa | -7.43985 | -49.83706 | 2026-09-24 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e964a332-f488-3094-b3f5-96af5147ddda | -5.58812 | -51.82065 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ca29965-7851-3486-a464-66c87668e113 | -7.30995 | -50.0663 | 2026-09-24 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a70dd31c-5861-3a71-b159-28ec3e343231 | -4.02353 | -52.06806 | 2026-09-24 05:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 15bc61ee-04d1-3c7e-9c4c-cba296e53dfc | -6.67033 | -58.57015 | 2026-09-24 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7bf87f3-a3bc-3664-afb5-b6e240dd561e | -8.25968 | -54.76918 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83a8a2cf-63be-303b-a120-981fac93e852 | -9.25318 | -46.24501 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1892c464-0a6d-39df-b867-25957907be7b | -9.53893 | -45.36678 | 2026-09-24 05:04:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9477c5d-1d4c-34d2-bcbb-830f87b4c37a | -8.30182 | -50.85264 | 2026-09-24 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14cbe471-b2a1-34c0-8e44-f4796b86aa2a | -6.0108 | -59.93876 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 81dfb314-f1fd-3020-87db-0ab3365df572 | -5.9992 | -44.10993 | 2026-09-24 05:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 389f8551-a844-3beb-b598-f531ac62b6ac | -6.9009 | -55.57822 | 2026-09-24 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d194168-c5e8-385b-bb28-a21f4da14684 | -8.26906 | -54.77423 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 872875a8-a368-34dc-8fa5-6b7d2081cd5c | -6.68556 | -55.05422 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77a1be73-9ee6-34be-810c-d58482380ae9 | -3.15814 | -50.82911 | 2026-09-24 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 809bc529-3041-3e90-bc87-70f991b43a23 | -6.46722 | -59.95864 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bfce0de-dee2-3ac9-b145-c2303c8f1778 | -5.47861 | -51.00895 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2af3a73e-b1f5-3323-9f5a-deaa3efcf079 | -3.64562 | -54.74935 | 2026-09-24 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 971a15e7-1f8b-3c57-b115-4281c0daacfd | -5.77083 | -56.52124 | 2026-09-24 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df6a1356-bc89-3cc6-aca7-cd7007b12e74 | -3.06537 | -54.40339 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5449b35c-827c-316c-b49c-ade1766e0192 | -1.62384 | -54.91759 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dca505e5-f436-36e9-bc70-43da552167dd | -6.2661 | -43.13436 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 29415386-0fd4-30a8-bc94-be7de5b95788 | -4.10931 | -54.48299 | 2026-09-24 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a23a3cab-448a-3ae0-be75-77c058498240 | -5.82636 | -52.0294 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e46df11-d1d9-37a1-8f5d-503e60b03148 | -2.89386 | -54.09236 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33cae323-4ea3-32e5-aa17-8336bad12703 | -6.12694 | -44.59979 | 2026-09-24 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 101cf9b3-81a4-380e-983e-8e91f7224d62 | -2.94424 | -49.19625 | 2026-09-24 05:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a11f5f3e-4e84-3793-83af-54f39971c520 | -3.45803 | -50.06924 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5c5cbeb-bee5-373e-9a2f-082d8acf41ac | -3.18117 | -48.01987 | 2026-09-24 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 865543fa-0644-3120-a817-354e9d4a5714 | -6.30964 | -57.75065 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ade386a-9e14-3a63-a690-fe0cf3fccf0c | -3.3708 | -50.03088 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b80f9a0c-85fa-3da1-8106-73e2e972eb3f | -5.78624 | -49.18613 | 2026-09-24 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c3a69ff5-62b5-3254-8de8-d13871e11395 | -2.64531 | -54.69298 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 0f20e47d-81c4-3895-959a-3d654ccffdcb | -4.02694 | -52.06857 | 2026-09-24 05:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 67b5cbb8-30fb-3154-bb56-6c84c6dd0d8a | -3.90396 | -55.83151 | 2026-09-24 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 829af75b-c528-3d73-8183-14cca29c72c0 | -8.28614 | -54.75204 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69b2679f-0e5d-34ff-b3fb-0285cf62d4c5 | -9.58228 | -46.51226 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b042eb7-ac6f-36f1-9f95-9679fea03023 | -2.94148 | -51.29707 | 2026-09-24 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74240729-89f1-3dac-b82c-5f96476c725c | -3.10526 | -60.70932 | 2026-09-24 05:04:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06e663e2-d105-3ecb-b767-66798b416ae8 | -2.65657 | -54.62248 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bea33f70-85c5-330b-ad9d-87ff4d23e436 | -3.5464 | -59.94966 | 2026-09-24 05:04:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c5722bdd-92ac-3fc8-8ed1-5e6ba8ac81a9 | -10.07939 | -46.05519 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5a27def3-9ed7-344f-b258-414482e83549 | -3.17579 | -48.02692 | 2026-09-24 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1a1d375b-96a6-33c1-8199-d2c9c87ca8e6 | -8.27401 | -54.76434 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09c13a4e-518b-3da4-b052-7f5a76cc949f | -7.42824 | -49.86091 | 2026-09-24 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 917b1c8c-c71d-3989-bdf0-da16ce5682a1 | -9.74806 | -48.34741 | 2026-09-24 05:04:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9886bba-11f1-32ae-9075-68f0d88a43b8 | -8.25803 | -54.77959 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee2a45ac-d6a5-31ba-bc2f-64274b196b32 | -6.1285 | -57.75909 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d310e373-52fc-3a91-a60c-3e71739011b7 | -4.6853 | -55.92369 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d1192e4-8ac7-3afd-b7e4-40a43d16c809 | -4.2885 | -48.61241 | 2026-09-24 05:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e25e533-7e28-350c-9621-5e4733eeaac7 | -3.8348 | -59.38694 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63760b9e-04c8-3322-a388-0865399f45a4 | -8.15126 | -49.54787 | 2026-09-24 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 801aa7aa-b3b2-3517-b9ac-adf4758f6273 | -10.0949 | -46.06124 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 219a904a-f34d-3e96-842e-1d039805fd71 | -3.00281 | -54.17719 | 2026-09-24 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 583b9c25-edf5-3ce9-b708-ce4ed9f9bec6 | -2.94045 | -50.49103 | 2026-09-24 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb27653b-2e89-32bc-b0c9-b772304e0489 | -1.62326 | -54.92122 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 307ffb2a-5b69-3e7d-ad5c-ca42aaa85334 | -3.60576 | -60.58106 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32216881-d6d9-35cd-b17a-f4a927d44399 | -3.96169 | -59.35261 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 65f8f6dd-817c-3bf9-9e79-0cfb87721b48 | -9.24314 | -47.34721 | 2026-09-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d8ad144-5e86-36f6-9650-907b4280751e | -6.63633 | -59.92876 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08795a6f-4358-3569-bb9b-94499099011c | -6.6803 | -58.55736 | 2026-09-24 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0b150296-93eb-37db-9eff-49b3df7cf3b8 | -1.84016 | -54.71993 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| bb37f97b-f9ce-39f6-b56f-fc70a7f2999f | -4.98954 | -45.55126 | 2026-09-24 05:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ba9ac385-3770-37d1-bf7d-8803814b4d75 | -3.68504 | -60.55831 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8ee3be56-1309-355b-8f24-c910b8869625 | -3.76725 | -54.81921 | 2026-09-24 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96140e1c-f2f2-3f34-9239-b96454721a93 | -5.77378 | -45.10194 | 2026-09-24 05:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 54cea9ea-4b51-3d94-a7f6-50bcb980ca75 | -3.00558 | -54.18116 | 2026-09-24 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8ee5904-9794-3f20-9911-6c9898b53f23 | -6.52002 | -52.82048 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0770f809-195f-3d18-813c-7daa30198cd5 | -3.70703 | -54.1925 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38f94c19-a0c3-3854-96c1-f4e58f4058ea | -3.26763 | -49.15004 | 2026-09-24 05:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0914fd85-ef5b-3a4a-96b1-8f72c77e8f93 | -8.72013 | -47.60704 | 2026-09-24 05:04:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe12210a-67c0-3144-a060-2015882021b4 | -3.41794 | -54.00232 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c840256d-1f31-3061-887e-d2145bb54419 | -5.41039 | -60.21342 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a52fedbe-ace7-30da-aa68-4426ab6c916a | -7.41955 | -49.86492 | 2026-09-24 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README63.md)
