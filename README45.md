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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b60e0dfc-c81a-3f71-a8b8-835787128216 | 0.97556 | -59.39709 | 2026-09-02 05:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 171f8c19-b916-34d4-ab8e-1fc32e7cd386 | 0.97716 | -59.3836 | 2026-09-02 05:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3408e06-2075-3ed1-97b4-4788a6520408 | 2.51907 | -50.85201 | 2026-09-02 05:14:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dddcab6a-0d8f-39c9-86d3-ec291dde4a98 | 1.91139 | -60.58158 | 2026-09-02 05:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 346471d2-a952-3843-960d-e500f7c132ba | 0.97785 | -59.38791 | 2026-09-02 05:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 147ed790-70bd-335a-b1f0-ca98c8190814 | 4.33839 | -60.78596 | 2026-09-02 05:14:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0089cce7-27be-3f84-8300-163901689f6c | 4.33284 | -60.80676 | 2026-09-02 05:14:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bff55784-ca24-38f7-94f4-28a10cf31e4e | -1.39467 | -48.15443 | 2026-09-02 05:14:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c837668-188b-34e9-8513-b04a81a3403d | -1.01623 | -53.7247 | 2026-09-02 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d1e62aa-b69a-3048-90ac-8389962a3fd2 | 0.65184 | -59.57579 | 2026-09-02 05:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1fbe1858-3814-31ca-a0fa-8a6a1f289879 | 4.68034 | -60.47704 | 2026-09-02 05:14:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23bac071-9862-3d49-ad3e-0abfebb0d15a | -1.01685 | -53.72076 | 2026-09-02 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 618a77de-89eb-3663-b00a-73bd999696d3 | 3.28901 | -60.62839 | 2026-09-02 05:14:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f66cf85e-2034-36ad-bc9c-ed5a7a7890e8 | 4.33212 | -60.80639 | 2026-09-02 05:14:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50aa8b70-d434-38c2-bea7-ed2f1623e4d3 | 1.67005 | -60.14181 | 2026-09-02 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af3f4eda-bb6c-3d05-8115-0a68fd5b5148 | 0.97613 | -59.38111 | 2026-09-02 05:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8d1a6d6-902e-3106-b6a8-391c44e9761f | 4.33636 | -60.806 | 2026-09-02 05:14:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd26db06-0489-34d1-baea-bca7114b5b42 | 2.46521 | -51.11703 | 2026-09-02 05:14:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3bb94872-b10d-3d35-a471-de1550ba4627 | 4.33343 | -60.81077 | 2026-09-02 05:14:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4ec91ccb-e18d-3655-9872-2858ce417816 | -1.01913 | -53.72924 | 2026-09-02 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d73a0631-5020-30c2-b832-637cc8753417 | 0.97511 | -59.39893 | 2026-09-02 05:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ccf931c-bbbe-3cc0-b9d9-a6dab3fc1106 | 0.65115 | -59.57141 | 2026-09-02 05:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ca3cd57-bf2c-30df-99b0-6b73347a9aa9 | -1.01975 | -53.72529 | 2026-09-02 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2bb7485-4dfb-3203-b898-b91f76c0535d | 4.33591 | -60.79832 | 2026-09-02 05:14:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32167210-1162-33b4-9209-25c777a584ae | 0.9768 | -59.38542 | 2026-09-02 05:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55a0ebac-a9ac-3785-9b1a-19cf16ca58d4 | 4.33274 | -60.81041 | 2026-09-02 05:14:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ce8503f-8284-3aa5-989e-769b05d76479 | -8.44574 | -54.72652 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eeaf5954-aefe-3ce0-b89f-8da6c80f1613 | -4.23754 | -62.23712 | 2026-09-02 05:16:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| eaa6439d-146e-3ba6-be4c-f8bf92f3c411 | -3.85009 | -44.05718 | 2026-09-02 05:16:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 75ef84a1-09eb-3617-a08e-b619e80c1f09 | -3.63517 | -60.55263 | 2026-09-02 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c15eaa13-2ec7-3fca-8391-0c10f2a50982 | -6.93345 | -62.8857 | 2026-09-02 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66f0ff6a-a90b-3c9d-a892-eb371192cf89 | -7.18392 | -55.48323 | 2026-09-02 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67b1802a-ffbb-38a0-ac7a-8ebce49692cb | -8.4434 | -54.71746 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06ddec6b-df47-36ba-9765-a4bb6f44f69e | -4.35444 | -55.033 | 2026-09-02 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b1bb7f5-e755-3513-a3f8-f4d2675e0a3b | -7.45717 | -61.37366 | 2026-09-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fb1b1a5-19f1-3ee1-9018-c18538404891 | -5.12345 | -57.03182 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73ed9bc5-c5b0-38b2-915b-c3f909868edb | -6.43278 | -53.5668 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fda2251f-3549-39e8-9fac-50b5f0f96ce5 | -8.45012 | -54.69881 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 034e86fb-e260-3322-bc2e-443c924c1298 | -6.80779 | -59.10207 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 432f1036-4352-3e6f-b9ce-51392bf46b8a | -8.45252 | -54.70784 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3161b08-bf3e-3440-9f24-f660003b4bae | -6.57195 | -55.61696 | 2026-09-02 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2d8234c-1505-34ad-9ddb-2a7d49e59fec | -8.28322 | -54.93525 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1ef4483-ea4e-33b6-a92b-87d1c8ccc2f9 | -7.06354 | -52.72854 | 2026-09-02 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6900a980-e0ad-33ee-a21a-ffc8b3b6b431 | -7.53959 | -60.71821 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac73ca41-6d07-34f8-85d2-12ee4fd34b6c | -8.28745 | -54.93158 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86c3d2f5-7b4c-3601-9705-fa364f84df66 | -7.65024 | -45.8847 | 2026-09-02 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4dc6aad1-1e5b-3c6d-a2ef-5ab7ff74cec3 | -8.4922 | -54.59069 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0b2c42b-c8ac-3a17-a05d-5852ada64307 | -6.88529 | -59.40137 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b9be7c3-fd9f-3a2e-b2de-eca34b938084 | -8.47563 | -54.70271 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| fb580e65-d5f6-393f-82fe-b454c42bfd7f | -6.94452 | -56.4642 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8ab6430c-1cc1-3b9b-878b-cad470457f1d | -6.12765 | -59.89399 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6ad6b9a-7b2c-3bdd-b05a-6e5c56eca50f | -6.25856 | -55.42421 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 63874e98-58ff-3de5-aa90-6acf880fbd59 | -6.08817 | -57.71909 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 495eb99e-f45b-3117-ae89-9c34f6ef3115 | -4.96637 | -55.84902 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c4fba2a-dd17-370d-9858-670f3d3ee7a8 | -6.25679 | -55.43554 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5fc6033a-6f99-3897-948f-8bacc903b82f | -6.05178 | -57.73458 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28686a06-69cb-37e4-8381-c0db70c4d42d | -3.82856 | -59.00073 | 2026-09-02 05:16:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7f65bd56-74b1-35a4-bd00-b2c99f0984fc | -7.29841 | -60.62381 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45711362-9fe0-3132-83ef-b9000c26a127 | -6.96919 | -59.75002 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f5fd09e-cc1c-33c6-a882-3e04e0483889 | -4.12433 | -51.03145 | 2026-09-02 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17be1c31-2edd-35be-8327-42f142d3d459 | -6.14233 | -62.52788 | 2026-09-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 496436d5-ff7f-3b1b-867d-cfe84aa26bf6 | -6.14964 | -55.67456 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db77fa24-a481-3779-9287-e962843e7c95 | -4.36622 | -47.78047 | 2026-09-02 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| b0cd4358-4a54-355b-9f2d-9ce32b37fca3 | -3.74384 | -55.97923 | 2026-09-02 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb1fe9e8-b8ce-3de1-8c3a-4fe8c7c67dfb | -6.07453 | -57.95458 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f47e44d-dd78-3965-9a21-6afd8646e6ff | -6.14634 | -57.90952 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20e5e418-4839-3eb6-bcbf-ff080c363b6e | -6.83882 | -59.08129 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 598cfdae-76d7-3922-97ed-4b7bd0b7a993 | -5.99997 | -57.82556 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1a304fe-559a-3931-badd-76e61e3ccb9b | -8.44234 | -54.69997 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0f1b550-9b21-30b3-b2ba-c21920fa71c1 | -6.19262 | -55.27798 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5b8ecdb-2e56-3140-87c4-81ca7cbf56f6 | -6.12795 | -56.38504 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19908ab2-5196-3916-80a4-3939f730e3fe | -3.61741 | -60.54526 | 2026-09-02 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 48bf908e-0589-3047-bb40-0353c674efca | -3.14652 | -60.64222 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e6b1c99-ac7e-3d66-8254-69c8d1688003 | -6.12453 | -57.68232 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3ef10e37-a904-3813-916a-6876bb725984 | -8.44159 | -54.70616 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cee8b728-edf6-312e-9e48-19b4ce524046 | -6.9501 | -56.45049 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdc0b3bb-9c71-3eb3-ae5a-eeb7063f5cf3 | -6.12398 | -57.68578 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 756fff9a-e36f-3d91-b181-28065eccddab | -8.46521 | -54.72277 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 8754f336-29f1-3b2a-a2c4-35b234654491 | -8.4598 | -54.70895 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 27c5029b-3de2-3c9d-8f43-72615e275a6a | -5.94254 | -57.73844 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae7b3a0d-bc25-35e7-a682-3d8f60b1eb12 | -5.86849 | -57.77598 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7a2a6af-aac0-3b56-a7e8-e74fa8520f8a | -5.95904 | -57.69859 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98cb812e-a4ce-37bc-ab4e-b453c4f424e3 | -5.94636 | -57.69304 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6853bb43-d48c-3361-8c43-6a9c48e94433 | -3.57808 | -58.74575 | 2026-09-02 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53b2056c-8b39-396b-b653-c983b1002037 | -3.48918 | -59.26228 | 2026-09-02 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68ad8cb2-736d-3ed4-ae41-792d97d56442 | -7.64452 | -45.87875 | 2026-09-02 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 69eb462f-b954-3cb6-85db-82ce37b5c55a | -5.97502 | -57.68341 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c8832a3-862a-389e-9a1a-cae2f73b45f0 | -7.57797 | -60.48579 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4597bd76-a14b-3e65-be16-f23f35b747a4 | -7.35483 | -60.58628 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d50aad8d-a2d9-3688-8982-de6cb99e2496 | -5.50605 | -60.14851 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88c8da34-2675-30a0-a634-8b0b7a49c0a8 | -5.86203 | -51.70879 | 2026-09-02 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f4388d5-312a-3e68-a3fd-86dba763e5d3 | -5.96288 | -57.6744 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0662fb6a-274c-300d-909e-2507bc363106 | -7.19617 | -60.68989 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3df7fa58-0bc2-3049-b974-04f1df266b98 | -3.61669 | -60.54963 | 2026-09-02 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e8b0c86-35a2-38f7-9e29-587df4ae4f61 | -6.8841 | -59.40873 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b385d02a-db65-3a51-9e51-7e78caf39015 | -4.14762 | -60.69438 | 2026-09-02 05:16:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c261f9f-dfd7-3592-8d78-12f10f6c816d | -4.16581 | -47.835 | 2026-09-02 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11f34773-034b-3cfa-9880-e3f72ec18c1c | -6.08893 | -53.80126 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 209e491d-6611-3a4d-a799-d79fb715f4d2 | -7.28851 | -49.81353 | 2026-09-02 05:16:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b47f7ec-f245-3d7c-8631-60cd51e7bb08 | -7.35194 | -60.58174 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README46.md)
