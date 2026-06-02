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
| 2ad1616c-5aeb-3bec-9be1-a9d0d0caf0bf | -14.19025 | -52.87515 | 2026-06-02 05:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| abb524bb-94cb-31af-bde4-17a93fe56e01 | -12.29939 | -57.40145 | 2026-06-02 05:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17f16a03-9f56-3799-935c-c9736d6814e6 | -14.18964 | -52.88067 | 2026-06-02 05:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4f533f70-e633-3919-a12b-5031056793e1 | -10.56952 | -57.326 | 2026-06-02 05:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fd247dfb-4643-30fe-b3c5-2d2b72ff7152 | -12.54709 | -57.18046 | 2026-06-02 05:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc33687e-02e6-3cd7-be5f-dde29593de26 | -9.23051 | -63.62166 | 2026-06-02 05:40:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5508729-e9f9-3a97-b9cd-38948f6e6293 | -10.03649 | -59.34729 | 2026-06-02 05:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f1d7b90-37a7-3109-89e8-368eb2bb7914 | -12.55127 | -57.18656 | 2026-06-02 05:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc938e17-001c-355e-80d8-fe0a3d6e763d | -13.98329 | -53.87186 | 2026-06-02 05:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2deb2ba-35b4-353b-8b2d-63854c59aa0d | -13.97821 | -53.861 | 2026-06-02 05:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0b0017a-0103-33c8-ba7e-73979f46b1b4 | -11.57106 | -54.57524 | 2026-06-02 05:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7abb4c95-e944-3cb4-bd84-71f3a6fa8a80 | -9.19418 | -58.05441 | 2026-06-02 05:40:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8adf2e48-62bf-3bd6-b9be-899a2eb3b7dd | -10.54203 | -58.92615 | 2026-06-02 05:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e03990af-93c0-370b-a3df-d3fa63892d47 | -12.73195 | -54.19316 | 2026-06-02 05:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4464577-1b71-3ffc-b6ff-faea5a3f7778 | -11.74613 | -54.78907 | 2026-06-02 05:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 220b02fc-1320-39c5-8aa7-f488679f48cf | -16.15642 | -58.46754 | 2026-06-02 05:42:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f4a8b845-1e6b-35b4-8bb2-c2385232ac29 | -16.15578 | -58.47266 | 2026-06-02 05:42:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a8bd93e9-e105-31f7-b5d3-3ef43ac42e91 | -16.16048 | -58.47334 | 2026-06-02 05:42:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ea367958-7046-3d49-8f43-e6380b9ebd24 | -11.6184 | -55.18725 | 2026-06-02 07:07:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 17ccdf8c-da9f-35ea-87f6-558a7235ae2f | -10.57115 | -57.32106 | 2026-06-02 07:07:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 1e5fc3f5-41c4-3649-8126-79104788299e | -11.61985 | -55.17723 | 2026-06-02 07:07:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| e21e0649-9542-3228-96ff-357a9aaac24c | -11.62131 | -55.16718 | 2026-06-02 07:07:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f88198a6-5ab7-3fc0-a3d4-9d78c3bb3edd | -10.56981 | -57.32993 | 2026-06-02 07:07:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d5178d10-059e-3851-82ee-f886e97a8c84 | -7.01383 | -50.54704 | 2026-06-02 12:32:00 | TERRA_M-T | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 28eea295-2670-3fd1-9d74-78adf49a4ad3 | -11.74568 | -54.78911 | 2026-06-02 12:34:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f7170f76-f102-37a1-be8d-a8b4a3967114 | -11.32218 | -51.39365 | 2026-06-02 12:34:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 24.0 |
| f570c454-bc99-306b-b7b7-111544dab759 | -14.10853 | -58.93488 | 2026-06-02 12:34:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2360ffa8-5655-3d0f-b371-0bf735685a6b | -11.03824 | -56.92503 | 2026-06-02 12:34:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d42e1a9a-677a-3225-a247-298aacf78ae6 | -8.51721 | -51.56271 | 2026-06-02 12:34:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 8513c2db-50be-30f4-8ba2-81bddc1e5a50 | -12.30016 | -57.39923 | 2026-06-02 12:34:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c46c3ceb-db6e-3693-853d-bc8357025215 | -11.32604 | -51.38142 | 2026-06-02 12:34:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f8b27584-3f35-32ca-aea9-3c5caf910fb8 | -11.80818 | -52.51581 | 2026-06-02 12:34:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| ce5cdaf7-50b4-30fd-ae7f-a723b432438b | -8.98807 | -51.27105 | 2026-06-02 12:34:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 93f38cf5-5342-3f1b-9338-d39083ed44e6 | -11.32378 | -51.40045 | 2026-06-02 12:34:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 27.6 |
| e65d89c9-599b-3ec8-a3fa-86ea596ed7a5 | -14.03421 | -56.7915 | 2026-06-02 12:34:00 | TERRA_M-T | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1c2de58a-04c6-303d-a4b7-824a05c01598 | -11.7345 | -54.79885 | 2026-06-02 12:34:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| ea21186c-0fe3-33d4-b5b6-88381b7ace7f | -11.43787 | -55.10126 | 2026-06-02 12:34:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7a34a4f8-d3cf-3414-9f2d-7a1cd2c70de6 | -11.8811 | -61.04039 | 2026-06-02 12:34:00 | TERRA_M-T | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5afead4a-5155-3631-8105-b038e0c26618 | -11.62082 | -55.18094 | 2026-06-02 12:34:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| ef0bc356-df5e-31c2-8456-5e6b3c73d34f | -11.81708 | -52.5229 | 2026-06-02 12:34:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| e128b372-0cd6-3e0b-b572-f9eec6feab7f | -10.57616 | -57.32691 | 2026-06-02 12:34:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7546351c-7883-3a46-8d80-d50033c45bbc | -11.57045 | -54.57213 | 2026-06-02 12:34:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 9a78724e-cf1b-3912-acdf-fb19fc2614a0 | -11.8793 | -61.05214 | 2026-06-02 12:34:00 | TERRA_M-T | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1ebcac78-25f6-3456-a667-2b788b102bbf | -12.17662 | -54.53832 | 2026-06-02 12:34:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5be7a85e-774e-3183-9007-3262b6ab227d | -11.62223 | -55.17047 | 2026-06-02 12:34:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 38e88b76-42ee-3e20-a2ea-bba326c9c060 | -7.51039 | -55.00601 | 2026-06-02 12:34:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9cc5bf03-4ad8-353b-88e6-7a63285d0a69 | -10.86076 | -53.74993 | 2026-06-02 12:34:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| d03aebef-fda0-3f65-b458-48f6e29e376b | -7.50123 | -55.00471 | 2026-06-02 12:34:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2bb2b1c0-0242-3b91-a43a-fe8447773a0f | -11.43859 | -54.09213 | 2026-06-02 12:34:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 280c7aca-99ac-3f89-8ee5-64c3789bbdaa | -23.06166 | -52.24831 | 2026-06-02 12:36:00 | TERRA_M-T | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 39.3 |
| eb942a9f-4eba-3e39-b56d-e85e63f82daa | -23.05322 | -52.25458 | 2026-06-02 12:36:00 | TERRA_M-T | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 56.2 |
| 2d67dd63-2730-3819-818e-e01eacdcf07f | -19.1708 | -55.18135 | 2026-06-02 12:36:00 | TERRA_M-T | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 18.5 |
| 2598b07e-bcdb-32ef-9ed7-8d284fd511aa | -22.15651 | -56.06581 | 2026-06-02 12:36:00 | TERRA_M-T | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cbd1ff6a-2dc0-3fbe-8ccf-c9e7a0a1a64b | -23.05912 | -52.27442 | 2026-06-02 12:36:00 | TERRA_M-T | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| 0cafdff7-33fd-3374-b4db-4ebb29041652 | -30.51203 | -52.61023 | 2026-06-02 12:38:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 32.3 |
| 26b02d0d-3289-367b-b46e-073d57b5e3b4 | -10.6991 | -49.9167 | 2026-06-02 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| b012b849-7f96-3fdf-82d5-967920c0e7a9 | -10.6991 | -49.9167 | 2026-06-02 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| d5b422bc-cedb-31c4-badf-fb052068b9d5 | -11.886 | -57.8329 | 2026-06-02 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 6bd77185-e4ea-3fba-a3a0-38a64e1dc411 | -11.6329 | -55.1844 | 2026-06-02 14:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 15554d93-11fd-352e-8a5f-dfd33419a44f | -11.6332 | -55.1641 | 2026-06-02 14:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 5a8d23ef-76cd-3343-bfee-1e303534d772 | -14.0522 | -46.3391 | 2026-06-02 14:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 84.0 |
| c8460ece-4a47-3a39-9f18-e962634969a8 | -11.6329 | -55.1844 | 2026-06-02 14:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 287318ab-bec1-31f3-97c3-05233abcea8c | -11.6332 | -55.1641 | 2026-06-02 14:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 0c375497-e5b2-3b05-bc95-c0f4f307de9e | -11.886 | -57.8329 | 2026-06-02 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| af10c846-c0b4-3c00-a091-c753bae80a39 | -14.0522 | -46.3391 | 2026-06-02 14:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 98.5 |
| e24f854a-3f71-31fc-9edf-ad3d42a6d630 | -11.886 | -57.8329 | 2026-06-02 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| b7de4dda-516f-392d-8f81-e60e6c5ef70a | -11.886 | -57.8329 | 2026-06-02 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 20069d52-a490-3a1b-9205-158b5f72265b | -11.886 | -57.8329 | 2026-06-02 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 126.4 |
| ac11f5e0-bfb7-372e-9eeb-b8f18d557e4e | -11.6329 | -55.1844 | 2026-06-02 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| d85bd9d0-6a09-3592-9389-0869faa65995 | -11.8858 | -57.8528 | 2026-06-02 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| cd18714b-5cd2-3e31-a2b5-2ddbed4ea9d7 | -11.8671 | -57.8344 | 2026-06-02 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| dc306a6d-f536-33ba-a2d0-147446147e6f | -11.6332 | -55.1641 | 2026-06-02 14:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 2907b302-d87c-31fc-a31c-ec30151d5293 | -11.6329 | -55.1844 | 2026-06-02 14:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 01426f92-c393-398f-a353-25cba7e9fa6d | -11.8858 | -57.8528 | 2026-06-02 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| eabd66ba-df37-3a1b-88b5-de403b379301 | -11.886 | -57.8329 | 2026-06-02 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 98.6 |
| b1784020-d39c-32a3-b91d-7338269b456a | -11.6329 | -55.1844 | 2026-06-02 15:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| e76e1041-871d-32e4-923e-43e3e2523597 | -11.6332 | -55.1641 | 2026-06-02 15:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| d75a6a2e-80ee-3287-8c60-da19e7f16421 | -11.8858 | -57.8528 | 2026-06-02 15:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 621d6e12-20f0-3dd1-98b8-a5bfb56f0f21 | -11.886 | -57.8329 | 2026-06-02 15:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 46f27d18-b750-3f63-b9c6-216afe37803c | -11.8858 | -57.8528 | 2026-06-02 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 62e465ad-f264-326d-ac58-3cb35219eeca | -11.8671 | -57.8344 | 2026-06-02 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| d380eaf2-85a6-3c8c-ac7b-7d44b45424ab | -11.886 | -57.8329 | 2026-06-02 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 137.5 |
| c5e38e6b-1c66-3bd3-a043-3551eb2c6829 | -11.886 | -57.8329 | 2026-06-02 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 96145713-7b59-3847-9942-28c868be98a1 | -11.6332 | -55.1641 | 2026-06-02 15:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 0bc4684a-5a3a-3cdf-8ade-2c81a8c95a0a | -10.8573 | -53.7425 | 2026-06-02 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 4607ddc6-3ca7-35ef-940b-22a8f23159c6 | -16.1655 | -58.4842 | 2026-06-02 16:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.6 |
| c19068b1-4e4c-390f-8996-976938fdf0b8 | -10.8573 | -53.7425 | 2026-06-02 16:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 3d654d72-3105-3621-8196-5a4022afecba | -16.1655 | -58.4842 | 2026-06-02 16:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 389ab893-1d7a-383c-894f-2ce3f2be112e | -10.5736 | -57.3165 | 2026-06-02 16:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| c7ebbeb1-6f30-3788-84f6-35af830b8198 | -10.8573 | -53.7425 | 2026-06-02 17:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 02d592f8-1465-3cba-ba5e-e33c60dcc293 | -10.5736 | -57.3165 | 2026-06-02 17:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 94fc2e9d-013a-3ccb-8c36-14d62b7b8d16 | -11.886 | -57.8329 | 2026-06-02 17:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 65d01a23-59ed-3cbe-853d-bb42dd0fe321 | -10.8573 | -53.7425 | 2026-06-02 17:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| c73b5e17-e44f-3c97-ab4d-69b5a7b19293 | -10.5736 | -57.3165 | 2026-06-02 17:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 3ece18cc-30ec-396e-8d61-ad455c2e7a67 | -11.8858 | -57.8528 | 2026-06-02 17:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 765547de-3c68-350c-afc2-328e45a9cd0b | -11.5647 | -54.5794 | 2026-06-02 17:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| da78dab0-1564-3957-8fa1-aa293d18826c | -11.886 | -57.8329 | 2026-06-02 17:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 8b728c3c-8c58-3327-817b-922c80abd369 | -11.8029 | -47.3323 | 2026-06-02 17:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 6c74e52b-2c9a-3576-8c9d-aa4b0ef25cfe | -10.5736 | -57.3165 | 2026-06-02 17:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 9f713792-ff10-39c7-a808-ac98e8327747 | -13.981 | -46.0301 | 2026-06-02 17:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |


[Clique aqui para ver as próximas entradas](README8.md)
