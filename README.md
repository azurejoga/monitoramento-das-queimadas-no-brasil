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
| 9300d4d8-1df9-36d4-a3bf-c22f8238a363 | -6.1361 | -42.6017 | 2025-07-26 00:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 68.6 |
| f1d78730-2acc-390c-8b7a-a4df65503863 | -6.1551 | -42.5764 | 2025-07-26 00:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 114.4 |
| 96ab396d-bb60-3ec2-89bd-5445a9ae975c | -6.1737 | -42.5985 | 2025-07-26 00:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| 3a5df382-6e6e-30b1-9066-82e9deb3a54e | -13.698 | -45.6634 | 2025-07-26 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 45.7 |
| e13e5ed4-36e6-3843-a420-5d9a9117764c | -6.1549 | -42.6001 | 2025-07-26 00:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 219.7 |
| 521fa33c-b679-3cd9-82a8-9f9c9ac89db4 | -13.6975 | -45.6865 | 2025-07-26 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| df800a2c-f248-3ef8-b98d-14b5e0d5ec11 | -6.5626 | -56.25 | 2025-07-26 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| a013b4a0-2167-35a1-a7b3-75d396e83e97 | -11.9279 | -44.5569 | 2025-07-26 00:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 9789ea90-b548-33ac-88c0-86661141e6ed | -11.7317 | -48.1849 | 2025-07-26 00:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 2576dc3f-54d6-3737-a692-29685e6314b7 | -7.2405 | -43.0899 | 2025-07-26 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 125.1 |
| 41a87f65-389d-3cef-869b-13f54d8bf69f | -7.2408 | -43.0664 | 2025-07-26 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 293.3 |
| 513b507f-3706-3c24-9884-b43a8b93ceba | -15.011 | -49.8105 | 2025-07-26 00:00:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 40.5 |
| d19a2f0b-1f42-3cac-b24a-7c6b83e0205b | -11.7508 | -48.1825 | 2025-07-26 00:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| b20828f2-d825-3166-8fe3-ea8b22a9451e | -6.5441 | -56.2508 | 2025-07-26 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 005f1e75-b264-310a-afbe-078a53ccf61c | -7.5657 | -61.4001 | 2025-07-26 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 1c77e551-8607-3dcb-800b-5f9b25ce4fe8 | -4.0567 | -42.5354 | 2025-07-26 00:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 56.9 |
| 64a5d2fb-948c-319a-a6e5-29edb15edbad | -6.8764 | -43.685 | 2025-07-26 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| d188c250-6cc8-3d36-9a4f-2790c6487021 | -7.2597 | -43.0645 | 2025-07-26 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.9 |
| a9d53598-6992-3a17-98bd-e2d7169d7ec8 | -7.2405 | -43.0899 | 2025-07-26 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.0 |
| c96d5d97-8d53-39e3-8d22-1f0a449ccec5 | -11.7317 | -48.1849 | 2025-07-26 00:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| de4ef54c-cc42-3874-a232-614175d21ae2 | -6.5439 | -56.2706 | 2025-07-26 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 13b164c0-b90b-3abf-b140-1ebb9c94bcd3 | -8.163 | -43.229 | 2025-07-26 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.0 |
| 1f63bc2b-785f-30d5-a863-f3e50c373680 | -13.6975 | -45.6865 | 2025-07-26 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| de422449-0eb7-3030-884c-0535ddf175db | -6.8764 | -43.685 | 2025-07-26 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| a3173fb5-fe23-3871-afc2-5e45a22c79e4 | -6.1551 | -42.5764 | 2025-07-26 00:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| 05dbfc19-b1ef-3383-84bb-a8ebb6ff2ddd | -6.1549 | -42.6001 | 2025-07-26 00:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 239.9 |
| e22cf71d-9366-3c2c-9547-25d3e499f877 | -4.0754 | -42.5344 | 2025-07-26 00:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 53.7 |
| dab49394-9216-3820-ad8d-be5dfd9a3bd7 | -6.5441 | -56.2508 | 2025-07-26 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 2e95c2bb-043d-3d90-852a-4b38ef346ffd | -6.1737 | -42.5985 | 2025-07-26 00:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 90.8 |
| 2937b6e8-d6c8-363c-a58b-f08322f72ea6 | -7.2597 | -43.0645 | 2025-07-26 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 7548ff04-63cd-33fa-a27c-c6ca3387ba9e | -7.2408 | -43.0664 | 2025-07-26 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 236.9 |
| e68e28c3-5f8c-3ede-a843-e17779fbe17a | -11.7508 | -48.1825 | 2025-07-26 00:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 735bc8e9-f168-35e2-887b-fb82afc9a1e5 | -6.5626 | -56.25 | 2025-07-26 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 254a8768-d7c1-37eb-a95e-c7a8f30bd214 | -4.0567 | -42.5354 | 2025-07-26 00:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 55.6 |
| b8186fc4-6236-3610-b154-44f38cf8aec7 | -6.1361 | -42.6017 | 2025-07-26 00:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 85.1 |
| 423db1b0-52b6-3da6-8b8f-1ee0f5e5097e | -11.7317 | -48.1849 | 2025-07-26 00:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| b20cb5c4-d353-348b-8f62-8c017354e4eb | -11.7508 | -48.1825 | 2025-07-26 00:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| d73322bf-4453-34e7-986b-c01d4508c6ac | -6.5441 | -56.2508 | 2025-07-26 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 9bf5cd4b-08c6-35b1-9b55-646fd5f62a12 | -4.0567 | -42.5354 | 2025-07-26 00:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 49.5 |
| af84b8ce-93f1-394f-b0f1-e511127af6d7 | -7.2405 | -43.0899 | 2025-07-26 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.2 |
| ded47a86-4ac6-37a2-b2ac-76ec1a83a684 | -13.6975 | -45.6865 | 2025-07-26 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 57debb69-435e-3c6a-8236-cbd5222c7f72 | -6.1737 | -42.5985 | 2025-07-26 00:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 78a410d7-25ab-3aa4-a836-24e1fb31d4ad | -13.698 | -45.6634 | 2025-07-26 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 536a3118-6227-3dec-8a60-b015b28108ff | -4.0754 | -42.5344 | 2025-07-26 00:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| 4fd86432-1525-3d18-8550-650126c62e82 | -6.1551 | -42.5764 | 2025-07-26 00:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 122.5 |
| 2c2fdc6e-f2d4-3652-b1a4-3b4993facbc5 | -6.1361 | -42.6017 | 2025-07-26 00:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 60.9 |
| 729d58fe-dca8-356c-828c-7cd3f28a6ef1 | -6.8764 | -43.685 | 2025-07-26 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 57b7eea7-c652-3a02-ab47-345e5f89bf9e | -6.1549 | -42.6001 | 2025-07-26 00:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 228.8 |
| fa04e2e9-72d8-374d-9089-f32447528f5a | -7.2597 | -43.0645 | 2025-07-26 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| b2eb3172-d74a-34ae-aa7a-be5c7db5defa | -7.2408 | -43.0664 | 2025-07-26 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 221.8 |
| d772f846-753a-3d76-9b3c-8a3f54518f67 | -11.7317 | -48.1849 | 2025-07-26 00:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 5a9e3614-fb59-3b29-a6bc-54834860f0c5 | -11.7508 | -48.1825 | 2025-07-26 00:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 635bcaa7-146f-3cac-85e8-46f9dc2d5195 | -6.8764 | -43.685 | 2025-07-26 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 74c5eb05-76a7-3cc7-9d4b-c0b28f067b2b | -6.1551 | -42.5764 | 2025-07-26 00:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 110.7 |
| e1998970-49e9-3746-ba93-b624c17c9d7b | -7.2405 | -43.0899 | 2025-07-26 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| 93fd8765-d148-3665-8c3d-418aedfaaade | -6.1361 | -42.6017 | 2025-07-26 00:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 59.5 |
| 2c8a088d-39dc-3d00-8586-d1335d13f2bb | -6.1549 | -42.6001 | 2025-07-26 00:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 207.3 |
| 75fe5612-e2ba-366d-953f-ef016198199e | -3.3957 | -47.5003 | 2025-07-26 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 96d01e91-411a-390f-b888-e819a81a6c3a | -6.1737 | -42.5985 | 2025-07-26 00:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| b536beab-cdea-30e5-b42d-25e747faf3e0 | -6.5441 | -56.2508 | 2025-07-26 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 89220fa2-91f9-3419-b3cb-121ae10cbe54 | -8.1822 | -43.2034 | 2025-07-26 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.7 |
| 45fa50cd-5e39-3378-87da-6421099b0cea | -7.2597 | -43.0645 | 2025-07-26 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| f9b015a3-807f-3c73-85bc-d411d092a7b7 | -7.2408 | -43.0664 | 2025-07-26 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 188.9 |
| bc703d30-7092-3d1b-8076-4a040c6ef82b | -11.7317 | -48.1849 | 2025-07-26 00:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 038dca7e-0465-3551-aad9-f39a6d52cfc3 | -7.2408 | -43.0664 | 2025-07-26 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 183.3 |
| 274fa7be-ae27-3616-98c7-bf619a129eb9 | -6.8764 | -43.685 | 2025-07-26 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 1fe80a9e-05a1-33b9-8af6-57096f30bfb9 | -3.3957 | -47.5003 | 2025-07-26 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 878f5eaf-3d72-3dd0-9668-190bdfeaf509 | -3.3958 | -47.4785 | 2025-07-26 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| e45f9c04-bd48-3244-94e0-c401f86f4e01 | -6.1737 | -42.5985 | 2025-07-26 00:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| af1e3256-a5b1-36fa-bc5f-c45bf9c6d77e | -7.2597 | -43.0645 | 2025-07-26 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 60.0 |
| bde52376-854f-35bf-bc0c-a15f4b571c3b | -6.1549 | -42.6001 | 2025-07-26 00:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 209.7 |
| f70711dc-e3e9-3a5b-9628-6a4d2e25eb92 | -6.5441 | -56.2508 | 2025-07-26 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| e2580e2b-5ec6-39a8-968a-45765a354749 | -6.1551 | -42.5764 | 2025-07-26 00:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 118.8 |
| d41cfede-bedd-3662-8a64-80b6243fe905 | -7.2405 | -43.0899 | 2025-07-26 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.4 |
| 99cb641a-6293-3cab-a03a-edad8e57c8ba | -11.7508 | -48.1825 | 2025-07-26 00:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 6aced8f8-5779-343b-8884-ac2e81357164 | -6.5616 | -41.4894 | 2025-07-26 00:40:00 | GOES-19 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 54.3 |
| d13bbca8-965f-3142-9be5-798c8bda5920 | -6.1361 | -42.6017 | 2025-07-26 00:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| a51a37ba-7457-3cf8-a04b-d456b1a6b7b0 | -7.2405 | -43.0899 | 2025-07-26 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.2 |
| e638b615-51b9-3302-8d46-8b335c15cf76 | -7.2597 | -43.0645 | 2025-07-26 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.5 |
| f8d83e6c-5d33-34a2-a997-7ed1c64ce601 | -7.2408 | -43.0664 | 2025-07-26 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 161.5 |
| 3743433d-a6f0-3385-9957-fec7e570ff9a | -3.3958 | -47.4785 | 2025-07-26 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| f5cf2aa2-9548-371a-befe-dc1454a15301 | -8.1819 | -43.2269 | 2025-07-26 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.8 |
| 5abaf772-91bb-33d4-b79a-15048f020973 | -6.1551 | -42.5764 | 2025-07-26 00:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| 3b6f3857-bec9-32bc-bfcd-e5afe7bed1d8 | -6.1549 | -42.6001 | 2025-07-26 00:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 291.9 |
| 16a18da1-2340-3eaa-ad05-341edd552362 | -3.3957 | -47.5003 | 2025-07-26 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 0957e9bf-c709-3960-a97c-52df501d6aa6 | -11.7508 | -48.1825 | 2025-07-26 00:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 2dc95b8c-48c5-35d8-8779-a3f0f84c4f11 | -6.5441 | -56.2508 | 2025-07-26 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 467427e8-4922-3507-9bb4-2aad239b93c1 | -3.3957 | -47.5003 | 2025-07-26 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 7e531e5f-8250-3241-949b-3f32062afc41 | -7.2408 | -43.0664 | 2025-07-26 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 165.7 |
| d4f348f2-8a65-3798-b631-1ea4849aae98 | -11.7317 | -48.1849 | 2025-07-26 01:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| ecf24632-481f-3a53-9b6f-fd4267934bab | -6.1549 | -42.6001 | 2025-07-26 01:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 178.0 |
| 714682ee-cf39-3261-a8b0-634f47bbeafe | -6.1737 | -42.5985 | 2025-07-26 01:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| 4f668df2-a382-34c6-af0b-6885b107892e | -6.5441 | -56.2508 | 2025-07-26 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 5ab3f1bc-b3a5-3dca-aa3d-047fc61632c8 | -7.2405 | -43.0899 | 2025-07-26 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| 39193931-7247-3be0-8c69-3dd2552b6cea | -6.1551 | -42.5764 | 2025-07-26 01:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 104.6 |
| 5e1c6686-463e-3599-9b0c-5f18d778a24d | -3.3958 | -47.4785 | 2025-07-26 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 53e3869b-d9cd-3541-8701-51c49d825723 | -6.1737 | -42.5985 | 2025-07-26 01:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| ca75d1e8-2eb1-317a-be91-91e215b00fa1 | -6.1551 | -42.5764 | 2025-07-26 01:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| 4de02d8d-087e-32e2-af89-2b5119010664 | -7.2408 | -43.0664 | 2025-07-26 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 134.5 |
| e2c5e783-edb9-3913-9aea-82c60f968dec | -11.7317 | -48.1849 | 2025-07-26 01:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |


[Clique aqui para ver as próximas entradas](README2.md)
