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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c00a3ac-d6d3-33b3-91fe-6aa461b5e08e | -22.95297 | -46.12781 | 2025-10-06 04:29:00 | NOAA-21 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 0a059c5b-9acf-3341-a50e-0031545a7ddb | -17.8621 | -57.5818 | 2025-10-06 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.1 |
| 1979b111-c282-3032-8394-85aab88fc043 | -18.1362 | -53.4161 | 2025-10-06 04:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 816c5e0a-ef45-3e44-b789-ae592b19bc4b | -17.9813 | -57.5262 | 2025-10-06 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.3 |
| 01be7240-9ae2-3414-b402-888d57dc8d22 | -17.8818 | -57.5794 | 2025-10-06 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.7 |
| 602a2877-aec4-3592-9c1c-1a5784941f69 | -18.1167 | -53.3977 | 2025-10-06 04:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 610f3256-7c0b-33c6-a784-6a522109b1f6 | -17.8617 | -57.6024 | 2025-10-06 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.0 |
| bc6f7226-27f2-3cde-b3bc-025ee7f0c276 | -18.1366 | -53.3946 | 2025-10-06 04:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 72bf752f-e322-3bd1-9a4d-a631c1adcdde | -17.981 | -57.5468 | 2025-10-06 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.4 |
| 1ea613ab-900a-3cb0-b62e-f2c90a20091d | -23.19134 | -48.97232 | 2025-10-06 04:32:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e230f44b-07ed-3224-af5f-c6384c51d82d | -26.06466 | -48.95573 | 2025-10-06 04:32:00 | NOAA-21 | GARUVA | SANTA CATARINA | Brasil | 4205803 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| be22216a-f914-3d7d-a99d-a41903effb16 | -22.74322 | -50.9645 | 2025-10-06 04:32:00 | NOAA-21 | IEPÊ | SÃO PAULO | Brasil | 3519907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ee9bd2a0-ca73-39d5-a321-8a6fd6d60a8d | -24.09433 | -48.34632 | 2025-10-06 04:32:00 | NOAA-21 | RIBEIRÃO GRANDE | SÃO PAULO | Brasil | 3543253 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 755ffe67-8629-345e-bf42-efd08fcf58fd | -23.23958 | -50.75839 | 2025-10-06 04:32:00 | NOAA-21 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b618e804-0d3b-3be2-bc65-a2dd28399950 | -23.40755 | -46.99093 | 2025-10-06 04:32:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| bebe59be-92f9-3b12-8ba0-220895300766 | -23.53405 | -47.08567 | 2025-10-06 04:32:00 | NOAA-21 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6f3ff990-c24e-349a-aec4-1829d3864698 | -23.77415 | -52.86124 | 2025-10-06 04:32:00 | NOAA-21 | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 41a69b78-b39e-3b43-8e85-db8ff4672c51 | -23.23636 | -51.28497 | 2025-10-06 04:32:00 | NOAA-21 | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3ea6f6cd-0600-3818-8471-dd1b9b4680ad | -23.52932 | -48.28685 | 2025-10-06 04:32:00 | NOAA-21 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e087f564-be76-3a54-87f2-77bd98b3397d | -23.14085 | -49.95674 | 2025-10-06 04:32:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 22bbd658-1f7b-3ed4-b92b-7d1823f6518e | -22.95174 | -49.904 | 2025-10-06 04:32:00 | NOAA-21 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 16a05c98-77a8-3139-a154-25fe6eda4529 | -23.59271 | -50.26773 | 2025-10-06 04:32:00 | NOAA-21 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| db14f91a-bfc5-3e58-9ef3-d8818e83299f | -23.83788 | -48.52487 | 2025-10-06 04:32:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 2bf9d851-6e53-31d8-88b5-993d06ac9dc1 | -23.18798 | -48.97177 | 2025-10-06 04:32:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5dfde4ef-7db2-312c-8a5d-9969bcd5687a | -23.40248 | -47.57554 | 2025-10-06 04:32:00 | NOAA-21 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9b594803-0828-3131-af84-90a73f86860b | -23.70198 | -47.41843 | 2025-10-06 04:32:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 752077f5-b37f-37a9-b2ab-a827fbf92517 | -23.29372 | -47.73101 | 2025-10-06 04:32:00 | NOAA-21 | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 09cdd5be-23eb-3499-a9b9-233453055ab4 | -23.19295 | -50.94303 | 2025-10-06 04:32:00 | NOAA-21 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 471b4a77-6bb3-39aa-8115-6fab5460d566 | -23.58727 | -50.25903 | 2025-10-06 04:32:00 | NOAA-21 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 17dcc9f2-8b7c-300d-8871-2700ce6f5a00 | -23.5259 | -48.28629 | 2025-10-06 04:32:00 | NOAA-21 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 27437702-2693-32bf-85a6-138bd2008044 | -23.64021 | -47.47557 | 2025-10-06 04:32:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 468a294a-00e4-3efe-911b-7bede5af3791 | -23.58999 | -50.26338 | 2025-10-06 04:32:00 | NOAA-21 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 175472bd-4d4d-351c-b86e-e8f0b8a57fad | -23.73798 | -47.39341 | 2025-10-06 04:32:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 46a9636d-2b0c-300e-b881-0144e0d817c1 | -22.74593 | -50.96889 | 2025-10-06 04:32:00 | NOAA-21 | IEPÊ | SÃO PAULO | Brasil | 3519907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7280c6e9-a22d-39a2-a787-74072e80eb7e | -23.19356 | -50.93926 | 2025-10-06 04:32:00 | NOAA-21 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 117b60d7-ad13-399e-8919-f467293fb19c | -23.58552 | -50.27027 | 2025-10-06 04:32:00 | NOAA-21 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 42a5101b-438d-3bbb-a850-61d1cbf2df30 | -23.33481 | -46.79025 | 2025-10-06 04:32:00 | NOAA-21 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 754c94ec-7e5d-33af-9f52-09f7c5d81b5d | -23.14143 | -49.953 | 2025-10-06 04:32:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3964a5b6-b5c3-3420-8e74-2397087c8e98 | -23.40519 | -46.99334 | 2025-10-06 04:32:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 805b974d-7047-358f-8e58-74b3e4e2630f | -23.64572 | -46.20027 | 2025-10-06 04:32:00 | NOAA-21 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 021ed001-02d6-3686-b1ef-a6cbc2a2834e | -23.58668 | -50.26278 | 2025-10-06 04:32:00 | NOAA-21 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 92739ff1-c6fc-3e81-96bc-710540aabac3 | -23.23567 | -50.76154 | 2025-10-06 04:32:00 | NOAA-21 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0588d179-e90d-3692-9b24-c0c20882c05e | -23.28406 | -52.16306 | 2025-10-06 04:32:00 | NOAA-21 | PRESIDENTE CASTELO BRANCO | PARANÁ | Brasil | 4120408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 00f6568d-fd4e-3cfd-a662-8e0d56da02b8 | -23.24289 | -50.759 | 2025-10-06 04:32:00 | NOAA-21 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0c743bce-85d1-385a-89f8-20a3329cffe0 | -23.40599 | -47.57613 | 2025-10-06 04:32:00 | NOAA-21 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5edbe0fb-4f79-3935-a473-9d3943693e81 | -23.23697 | -51.28118 | 2025-10-06 04:32:00 | NOAA-21 | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9f432b01-4e3c-35fb-9478-0f4421d1bbba | -7.01936 | -42.78748 | 2025-10-06 05:12:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 38.1 |
| 04dc9ed1-bbc3-346c-964b-ab10e3a83461 | -4.65353 | -43.18023 | 2025-10-06 05:12:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| de7a1f68-4da0-30ad-8707-efcb71b63138 | -6.64467 | -41.97101 | 2025-10-06 05:12:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 40e47667-d52f-31fb-8782-db0c0bd0f194 | -7.01289 | -42.78137 | 2025-10-06 05:12:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 46.2 |
| f53a01cd-264d-34ad-992b-99858a675a47 | -7.04983 | -41.43517 | 2025-10-06 05:12:00 | AQUA_M-M | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| ce664402-376b-3c9c-8c77-908dc038db22 | -4.67878 | -43.21366 | 2025-10-06 05:12:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| f7ad19a7-3b88-3061-aa5f-de2eda1f38e0 | -4.65637 | -43.17298 | 2025-10-06 05:12:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 37.9 |
| dcab6cf7-0727-38af-8d0f-ada3ed98f91f | -5.67348 | -42.74963 | 2025-10-06 05:12:00 | AQUA_M-M | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 26.2 |
| e1b32e7f-222c-3904-942a-fd388851291c | -7.05944 | -41.43153 | 2025-10-06 05:12:00 | AQUA_M-M | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| db3dc630-07c4-3d86-acd6-e4bd4d87cdf5 | -5.65934 | -42.74695 | 2025-10-06 05:12:00 | AQUA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 33.5 |
| a4e58e28-70a8-390f-a93b-626ae906beb7 | -4.65182 | -43.20163 | 2025-10-06 05:12:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 833f1608-94f9-3323-a6a7-be591f049dc3 | -6.72221 | -42.81991 | 2025-10-06 05:12:00 | AQUA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 4eb99488-709d-363e-a56d-50b789a87561 | -6.71509 | -42.83586 | 2025-10-06 05:12:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| e948723c-10c0-3eb8-8a14-cb856aab9761 | -15.33748 | -47.30993 | 2025-10-06 05:14:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 3bb4774b-b87e-3d6d-83f0-965ec2050377 | -12.4846 | -45.54779 | 2025-10-06 05:14:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 8b4345af-8b42-33ce-9ebf-0c92401f29d6 | -12.47832 | -45.55431 | 2025-10-06 05:14:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.3 |
| b0228e6b-b93b-317a-9776-0aa507f6e538 | -2.24603 | -47.86731 | 2025-10-06 05:14:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 15aaf00d-c5ea-36d8-97f4-50cad21d9a6d | -4.32051 | -46.8107 | 2025-10-06 05:14:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd22dd36-01a2-3915-8842-d63c41b77dd3 | -4.31074 | -48.24368 | 2025-10-06 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 89d74111-0775-3434-b214-2a80e26cb8d4 | -4.30929 | -48.24077 | 2025-10-06 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d183fdc9-0f94-3a14-b729-ffe0ffbfc298 | -2.59216 | -48.12231 | 2025-10-06 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 52e3f61b-469a-33c7-bf2e-926226af9966 | -3.99718 | -55.65035 | 2025-10-06 05:14:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1d81f17-ba10-3cfc-aa54-931d109a5101 | -2.29584 | -47.99605 | 2025-10-06 05:14:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74022b98-45c4-3e30-8234-bff6af5e70d9 | -2.11606 | -56.81604 | 2025-10-06 05:14:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| daa154bc-2c30-36d3-9b87-df8c21097bad | -4.25413 | -48.57306 | 2025-10-06 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b3195cc-2bc6-37f1-be24-084bb3ca82a2 | -3.77858 | -51.87266 | 2025-10-06 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| feddbc2c-6a78-3555-8ced-1543ad9e3a10 | -4.24906 | -48.56884 | 2025-10-06 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ff37168-ebbc-35e6-a0ac-cde315b22538 | -3.904 | -54.6935 | 2025-10-06 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f807ba0-c84e-34b2-b20b-1abdbd089440 | -3.73772 | -52.67212 | 2025-10-06 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1e69183-9b34-3966-86f9-4e9ee66e8c32 | -2.11327 | -56.812 | 2025-10-06 05:14:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 98d1fdd3-6f69-34e2-9dfe-e9c94c92709a | -3.53747 | -54.07374 | 2025-10-06 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8abb5aca-5b51-3943-873b-866ab754d64e | 0.56809 | -50.8492 | 2025-10-06 05:14:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fda20c68-ea0d-30cd-8b40-b14fc654d3ad | -2.58656 | -48.12142 | 2025-10-06 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2e76661-f0e0-37c3-8d3e-157fe7f10edf | -3.93828 | -52.15454 | 2025-10-06 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5955739b-8205-31f3-8042-e94d993adaed | -3.94263 | -52.15511 | 2025-10-06 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d20fecc9-6b5d-3cf1-a86e-5f8b89ba66c2 | -2.11661 | -56.81252 | 2025-10-06 05:14:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b19c477d-a9fb-3409-9f25-e8a809360f82 | -2.85267 | -54.09554 | 2025-10-06 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03c753e3-1631-3e26-b14b-7bee4fb99a6c | -4.24853 | -48.57244 | 2025-10-06 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7e4be4f-d147-36f7-8811-9dbacf7c0b2a | -2.81219 | -54.38141 | 2025-10-06 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 609a35cb-964b-3a16-8e19-ef9437768a42 | 0.57183 | -50.84417 | 2025-10-06 05:14:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de8b2fa8-efdb-3605-b0f8-d369fa37dc4d | -4.22807 | -46.75851 | 2025-10-06 05:14:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06cd8a3e-3cd1-3f25-b2c1-2d56e1842988 | -3.65084 | -52.68274 | 2025-10-06 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95b24bb9-ae80-393d-af93-ae71e574739c | 0.56366 | -50.84988 | 2025-10-06 05:14:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df97928b-a675-31a4-b8ad-a58e898fc9b9 | -4.25466 | -48.56947 | 2025-10-06 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a656631-ddb9-3d79-9a63-387d7f522a0d | -3.29037 | -52.5457 | 2025-10-06 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12de9704-cf2c-3011-912f-74fb9a5b9c53 | -5.08859 | -47.51603 | 2025-10-06 05:14:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eea3e2bc-6a56-356c-b547-ad6211327895 | -4.25338 | -48.56861 | 2025-10-06 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2e178712-583f-3718-b225-d7124a51099f | -3.77878 | -51.8744 | 2025-10-06 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8552920c-13f8-32b4-bf25-48065421fc26 | -4.31498 | -48.2417 | 2025-10-06 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f233740d-dc29-36a6-844c-e1ecdb841210 | -3.59699 | -51.06742 | 2025-10-06 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0c1649a-1473-3df4-906b-fce270f2d943 | -3.65999 | -52.12736 | 2025-10-06 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0257a394-8c4b-3dc8-bca3-0b0090f3b63f | -2.29644 | -47.99219 | 2025-10-06 05:14:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2272a287-283b-309c-85f7-8eac3e5fc38c | -3.8377 | -52.23575 | 2025-10-06 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 216ad37d-439d-3cd1-8c0a-9106444690d4 | -3.54129 | -54.07425 | 2025-10-06 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README62.md)
