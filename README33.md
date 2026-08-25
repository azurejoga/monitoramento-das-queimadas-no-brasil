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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d3e442e-ac1a-3e0e-bb0f-1855ee82cd9f | -9.5306 | -49.27249 | 2026-08-25 04:25:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85a6c84d-d55c-3762-be59-47225f7e1e57 | -8.92228 | -45.72564 | 2026-08-25 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b48598d9-074f-30dd-b6e8-c00bff273f38 | -6.17156 | -53.47743 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c510f6e-eb2a-3ef0-a5f2-c9e8c54784a0 | -6.10167 | -53.41119 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f0362bd8-6bf8-3804-abf9-0a7e7ed29969 | -7.26169 | -45.84824 | 2026-08-25 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| af3f869a-8e40-3fda-868b-b57c36dabacb | -3.01264 | -51.05555 | 2026-08-25 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebea6ad1-f537-3d1d-8644-8161019d0d7a | -7.273 | -44.07679 | 2026-08-25 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e741d5fb-f0f0-309a-b8b4-a5f40d2a15f9 | -7.14737 | -42.75354 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6b28468e-8c29-3a4d-ba72-4e5d5f82e906 | -6.46745 | -43.10202 | 2026-08-25 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5326aa98-1fc7-3850-b4ae-5cd1644cf43e | -6.65103 | -43.90733 | 2026-08-25 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 39d219af-40f8-32e7-aeae-7bdb3fc58955 | -10.02965 | -46.42877 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb8b395d-b7d7-3aa3-9412-8b5bd16c4c9d | -6.21754 | -55.9293 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a207ea30-0347-3b66-b844-0be9cfd1d659 | -11.13054 | -44.47546 | 2026-08-25 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ace62091-dbf7-3a93-81b8-8d746ca01f71 | -6.64083 | -45.1603 | 2026-08-25 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ca87da9-6fcd-3474-98ca-a71e8b0cb5f8 | -7.26502 | -45.84877 | 2026-08-25 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a261d1c-bc17-3ae9-b774-6029be4db9fe | -6.1721 | -53.47434 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21918061-0aa5-3647-8ad2-13f71ba6969f | -6.13603 | -57.84801 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1b5a1d1-b73d-37cd-a508-efeb70e68f5b | -6.53834 | -55.08898 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f677bcfd-56bf-36a6-bf4d-87b1bb9cedb2 | -6.62087 | -58.49302 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c56cfc1-8b30-3009-9a40-ed8dde552096 | -7.25929 | -45.373 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9cfa45c8-278f-35b6-adde-60095e0126e7 | -7.1849 | -42.78683 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 40b000b4-475f-3845-9304-427bfdfab6ce | -7.27355 | -44.07326 | 2026-08-25 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 38401982-5ccd-32d4-8070-a22609a6f11b | -8.17081 | -46.7012 | 2026-08-25 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e61beb08-b201-3c15-9696-51d0694f3e5c | -7.90323 | -46.36013 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8da3033-33a0-3945-bc80-39343530eb0e | -7.74305 | -46.15294 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b54b6a7-b00e-30b3-9a20-4387f3be33e0 | -7.42515 | -43.08928 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 73d679c6-c6ba-3ecf-a9a4-8b5e9b9ca58b | -6.02084 | -44.84893 | 2026-08-25 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b5230ed-dace-34dc-ae58-74f92304b916 | -6.25748 | -55.42184 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3aa2231-2918-3aa9-bf90-de28271d2f15 | -6.97936 | -41.31416 | 2026-08-25 04:25:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f2ae3b95-d19a-3340-965c-a7f4864cc072 | -6.22866 | -55.48132 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c497c484-d129-3e78-8f12-5d11a1fce386 | -8.16466 | -46.6965 | 2026-08-25 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b74dd0ff-e2e7-3af5-a186-b7705e83d263 | -7.28522 | -45.35936 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 20295fa4-f1d5-389f-8fa7-8c3300d68e25 | -7.48645 | -55.36703 | 2026-08-25 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b30077bf-73c7-3d07-b460-a29142bf5ce2 | -7.06134 | -44.99323 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b777388-a74a-3d6c-bf68-fb188bd6ab35 | -7.2506 | -45.85363 | 2026-08-25 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 230ff998-c057-398f-999e-4bd3d5699acc | -8.11373 | -47.47868 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 573f0eba-522d-3d02-afa5-04cd3f6e8bad | -8.38718 | -44.7697 | 2026-08-25 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48a86a00-3a29-3d5f-b8e6-ca2e012483c1 | -6.35697 | -54.77037 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2999b2c8-8308-3160-9dae-a5ac3c9940a5 | -4.15214 | -44.27039 | 2026-08-25 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c195f80-cdd2-358e-a970-a383be169339 | -8.0635 | -46.88553 | 2026-08-25 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb800313-bf2e-36fe-8532-838a7a783357 | -6.95087 | -42.68916 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 729b4e61-ccf1-3604-a925-b036d67d3dad | -8.9289 | -45.72669 | 2026-08-25 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e8b5bfd-b793-33d1-8998-6f0831aa5cdb | -8.59811 | -54.7366 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60c852f7-0cdf-3fb1-8685-3ba1b4193cd8 | -5.95373 | -53.58033 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6870e759-ce94-3fa7-9d48-19ca57f0d1d2 | -7.26558 | -45.84527 | 2026-08-25 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1daaf3e-9f8d-381c-8463-8344c7f3df1a | -5.78274 | -57.56033 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 159fa2bc-2bc9-33fc-8440-4ed5582f0cee | -7.29459 | -45.36441 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 430cb142-1a6c-310a-b49e-fbb02d335d85 | -11.13336 | -44.47964 | 2026-08-25 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 0357a67d-7dff-3740-8e58-1d69dab08718 | -9.65516 | -48.32517 | 2026-08-25 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ed77643e-d1c5-34ff-87bf-3d22a0acd998 | -7.25449 | -45.85067 | 2026-08-25 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2f319c8a-339d-372a-ac3f-c8d33f6c9d5a | -7.97802 | -45.2535 | 2026-08-25 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd731172-cf62-3f9f-afe4-5c8659b948a1 | -7.49419 | -55.35665 | 2026-08-25 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d39000dc-db6a-38da-8810-20ff88e652e7 | -6.9418 | -52.78204 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0aff242-6884-382d-81d4-811fd43c6fdd | -7.64923 | -42.72883 | 2026-08-25 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c5c32c43-adac-3b8e-85ce-b05810a905bb | -6.64303 | -45.16774 | 2026-08-25 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c9749ff-2487-381b-a9f5-d8d221e9b43f | -8.61819 | -47.14421 | 2026-08-25 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33be0e98-1d0d-33c5-b5b4-401a706b328d | -10.71109 | -47.75515 | 2026-08-25 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c75da37f-91cf-30d7-a1d9-a0e6563a3715 | -7.08945 | -44.98704 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec45679e-528a-35ba-8f37-4a7309f0a65d | -6.22204 | -55.9288 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efb602ab-d76b-31f3-af82-19ef982b9f38 | -7.97471 | -45.25298 | 2026-08-25 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1d1aa1d-1d82-3a06-9ddf-0fcf572a39f4 | -6.83327 | -52.50099 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 978d893c-75eb-3a35-b995-3acaee63eca8 | -7.13634 | -42.77943 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5035d9f0-4ddd-39d9-a601-fd36809f4bdc | -8.09231 | -51.67381 | 2026-08-25 04:25:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| be471db5-7a56-399e-b6f4-6ea962b69907 | -8.10506 | -47.47365 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1757adf-e007-3b1d-b687-d7b140615926 | -10.36491 | -45.06083 | 2026-08-25 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c599b3b5-a8f6-3616-a0cc-72f01aadf77d | -7.41174 | -44.9676 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf924d19-4c56-3ec8-bd51-734daca7be23 | -7.35481 | -55.66363 | 2026-08-25 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a017a5e5-87e3-3619-9e44-f026db9b1a81 | -7.43945 | -43.1107 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dcc9af7a-b6f9-337a-b5cf-75eabaed9cf7 | -6.35008 | -54.77663 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dfa8f00-cf4a-3515-9eb1-ad05c8f07bd4 | -8.21481 | -54.97612 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b02989bc-8daa-37e2-a899-ddb8bc6a91b8 | -7.2449 | -43.12407 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8b25094e-c2e3-3d6c-8b07-367e2aabf810 | -3.69892 | -51.1124 | 2026-08-25 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fea53cb6-5501-3364-a6af-19d9c8fdd8c1 | -6.34877 | -54.78389 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60c475f9-b1c4-3026-86ea-befc5a633a76 | -3.53869 | -48.17701 | 2026-08-25 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 7d707356-02be-3579-86af-6573d306fb8c | -4.21152 | -54.56758 | 2026-08-25 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e0a1a3e-0bd1-3884-91c6-6c991adf5b93 | -8.57263 | -54.8786 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85008a30-8606-363e-99bf-aee251820688 | -5.91781 | -49.67936 | 2026-08-25 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4d8b8f0-caac-3f5c-a1f2-9befd5f2b092 | -6.54405 | -55.08981 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 002b7e1a-a060-3809-a23b-36563ebd2bb2 | -4.71762 | -42.77314 | 2026-08-25 04:25:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 87ce2424-dcbc-3795-87eb-c10208cce650 | -7.44461 | -43.09997 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1e06a24d-0d9f-3f14-b5f0-8a5f63177a26 | -10.0341 | -46.42228 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 735954df-1db0-324c-8775-5fefa23edcf4 | -3.54246 | -48.17758 | 2026-08-25 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 427359b0-8ffd-3d3a-be3d-861b25e52b2f | -6.20023 | -53.4953 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 381d4830-4321-37fe-bea6-e5cb5e94c62a | -7.63526 | -42.72671 | 2026-08-25 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f7878a81-9525-3162-934a-79583debcb18 | -7.28969 | -44.07942 | 2026-08-25 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5b7e9556-59dc-322e-aa2c-6ab8e2442860 | -8.91897 | -45.72511 | 2026-08-25 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14ddec0c-90d2-351d-8281-ee44d612c935 | -10.03022 | -46.42525 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6829498-728a-3793-ab51-003b137b4457 | -6.13489 | -57.85415 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14ec98c1-bc31-37c0-be12-6226c91b10a6 | -8.06886 | -44.65519 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c874f379-a24f-3b84-a539-276fca23d3b5 | -3.43498 | -45.19256 | 2026-08-25 04:25:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b79cffc1-0fb7-3c59-a360-e66d683f7c63 | -10.04024 | -46.40529 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5bed833-7f55-35d3-8e3a-f9a4a7526026 | -6.18212 | -55.4451 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bdf03558-9171-346e-804f-b5fd5c522a60 | -6.01063 | -57.67149 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f43a3fb8-5d11-3db0-b1e1-c1dd05c73826 | -7.16116 | -42.80278 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 17036624-67c1-3b2e-ba8c-e2d63d7a9f99 | -6.45243 | -41.5617 | 2026-08-25 04:25:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ba41cd8c-0e3b-3dc9-b673-3926819179e1 | -8.51397 | -55.3541 | 2026-08-25 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8900c91-1426-39e7-9176-1cac1bfadf83 | -6.33336 | -54.77349 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0513a7fb-fc54-391d-8749-befc2a928fd7 | -7.43487 | -43.11765 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d13201b4-ee71-36a0-8f4e-ecb5da4de3cd | -7.4326 | -43.08656 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 988e3eab-17ce-3e2b-817b-6f706592d732 | -7.19596 | -42.7611 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README34.md)
