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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6f0ab50-b5e8-3866-82e9-95c26df8d97b | -15.94881 | -43.52575 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 71614189-f6e7-33f0-8d0d-72d2a14a2ef0 | -15.94791 | -43.5206 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 04ddf27c-e30b-3ff0-9031-709651532b49 | -15.94581 | -43.53164 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d11e748b-7309-3caa-8419-3926d581357b | -15.93919 | -43.51696 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 51a52d62-c920-35b6-8ac9-5e92a47713e2 | -15.9389 | -43.53822 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5ae44c6b-3453-3254-a3e1-9093ede0e9d3 | -15.938 | -43.53312 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 795ce4bf-7c6a-3dae-9c80-0f59a5fadd82 | -15.9371 | -43.528 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5aed6aad-0a7f-39bd-b851-760f7a70544f | -15.93588 | -43.47523 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6b4408e3-6bfe-36e5-a31d-bdb74a8e8f4f | -15.92719 | -43.54042 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7fc16d16-5608-3d84-932d-4eea5fedda17 | -15.92629 | -43.53531 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bc8533aa-9787-3c0b-af82-628d25fd2b76 | -15.92329 | -43.54117 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 444937a2-45b7-3d88-8062-962a8fb4be7d | -15.92238 | -43.53605 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 816507af-ebe1-35d0-b475-eb78aeecb919 | -15.92147 | -43.53093 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f446204a-254a-3c1b-84b9-5c48c7f96928 | -15.91848 | -43.5368 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fec99478-0510-3d7a-a3e1-ed8ff84be6e4 | -15.83802 | -43.46955 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 540967f1-b5c0-3c7d-b858-14da3d62f1fa | -15.83711 | -43.46437 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a89acab2-bf58-30ef-a007-4be00e30d7d6 | -15.83405 | -42.972 | 2024-10-25 16:50:00 | NOAA-21 | SERRANÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3166956 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 43220f2e-d591-3503-9f23-5bcdf21e8d8d | -15.83319 | -43.46513 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d7ec6fa5-3694-3bfe-b62d-04a7c735820e | -15.83257 | -43.43847 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 01717d96-2b4a-3788-9127-2bab84394b3f | -15.83166 | -43.43329 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 73d1ca6b-e735-3c28-a38e-4b51bc5311ec | -15.82955 | -43.4444 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b8153aac-e7ae-369c-9dc8-50e0a301a20c | -15.82864 | -43.43922 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 80d9b139-e76c-39be-a0a6-e1580fe5a7ce | -15.82681 | -43.42884 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0ae8a03d-5ecc-34bc-b55d-5f03ff551049 | -15.8247 | -43.43996 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e20050f1-9644-3f6c-9c7e-8bc40fb956a3 | -15.82077 | -43.44071 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| cb261459-f57e-3646-a31b-228d08ba3c86 | -15.81356 | -43.46891 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 140a9a8c-e22d-39c0-9a9d-07d5323d7bf4 | -15.79042 | -43.61128 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a74b79a0-a8c8-3a55-b8d7-cccbdc595f4a | -15.78955 | -43.6079 | 2024-10-25 16:50:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 43738ed2-ad65-37d9-8ea3-69d49447af9b | -15.77937 | -43.80307 | 2024-10-25 16:50:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1f572675-4917-3a50-99e3-9a9177a6c1b8 | -15.68012 | -43.02473 | 2024-10-25 16:50:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3c4c81f3-2927-35f6-917b-1dc4b830c643 | -15.67977 | -43.02404 | 2024-10-25 16:50:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 78bc0080-a2b0-3e48-ab1a-af8af9a9b6a4 | -9.3146 | -43.25735 | 2024-10-25 16:50:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 14d008ab-9af9-39f0-bb78-8956a1179575 | -9.28972 | -42.90522 | 2024-10-25 16:50:00 | NOAA-21 | VÁRZEA BRANCA | PIAUÍ | Brasil | 2211357 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| ac3266b3-fbde-3dd6-8b33-125e07c644a7 | -9.26856 | -43.32886 | 2024-10-25 16:50:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 21.9 |
| f60128b8-35c9-3b8f-bc8c-83f6b7925b33 | -9.26779 | -43.3244 | 2024-10-25 16:50:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 25.9 |
| cca7e1f0-dc24-3cba-b93d-6a664eedb939 | -9.20292 | -43.33974 | 2024-10-25 16:50:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 50215c0e-f60f-32b3-86c2-6a40c655a55e | -9.20237 | -43.34104 | 2024-10-25 16:50:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 331c59f9-61eb-385c-9df3-9856f7bfebb9 | -9.20158 | -43.33657 | 2024-10-25 16:50:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| cea6b9fe-1556-31d7-8922-78ab17611f45 | -9.19927 | -43.34507 | 2024-10-25 16:50:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 71c821a5-3c94-3c25-a59a-1d3c015664c9 | -9.19875 | -43.34631 | 2024-10-25 16:50:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 17b96db3-30ff-347a-8866-126c5de66aa0 | -9.19851 | -43.34061 | 2024-10-25 16:50:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 17ae1271-e489-306f-b122-b2ecf523cde7 | -9.19796 | -43.34188 | 2024-10-25 16:50:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 16dc254a-d9e8-3fb7-8ce4-0bf628c56d39 | -9.19486 | -43.34589 | 2024-10-25 16:50:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 47.7 |
| 370f913c-2e50-3f05-a431-0b33f41eb3c0 | -9.19013 | -43.26438 | 2024-10-25 16:50:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 5b9a7682-58bc-31fe-8af5-51f6a9a6e9aa | -9.14595 | -42.86603 | 2024-10-25 16:50:00 | NOAA-21 | BONFIM DO PIAUÍ | PIAUÍ | Brasil | 2201929 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 2082b0f9-a8d8-3a37-8def-fe859216dc7b | -9.06702 | -42.98056 | 2024-10-25 16:50:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 1fac9696-1afc-39cd-85da-3799b0441f98 | -9.0662 | -42.9759 | 2024-10-25 16:50:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| fea0b6c0-2a5f-347b-b8dc-a0ee2cc90efc | -9.75481 | -43.85718 | 2024-10-25 16:50:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 00f5877d-270f-301e-97ee-a7ed65257c9d | -9.63396 | -43.91219 | 2024-10-25 16:50:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 822fdaeb-a623-3ff1-a488-830df3c1617d | -9.63395 | -43.91231 | 2024-10-25 16:50:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 926f089a-f6f8-36d8-82a8-daf6fdef609e | -9.63331 | -43.90828 | 2024-10-25 16:50:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 67c9cb3c-ec04-3cc4-b8fd-a9e819ec9069 | -9.63327 | -43.90841 | 2024-10-25 16:50:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 1c4d7a7a-b824-333b-b475-3b190eab3bbf | -9.62909 | -43.90908 | 2024-10-25 16:50:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| ace70c53-e91b-3241-a951-0e1743dfe8b9 | -9.62905 | -43.90919 | 2024-10-25 16:50:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e28cc187-4e2e-3021-8cf8-966c4ffcb4c9 | -10.22971 | -43.93757 | 2024-10-25 16:50:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f1d26b21-4a28-3787-9276-29861a757c20 | -9.99442 | -44.14383 | 2024-10-25 16:50:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 92ce7299-17e1-3cd1-ae46-ec5e89b32610 | -9.9924 | -44.14414 | 2024-10-25 16:50:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c11f33ca-975e-365b-820c-b02a6b5e91b1 | -9.96626 | -43.95055 | 2024-10-25 16:50:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| db444d06-2b6b-3d6a-947d-f084daa4aee3 | -9.96282 | -43.95135 | 2024-10-25 16:50:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 73107243-fc46-3776-aa5f-1fd9c9efca2f | -9.96213 | -43.94743 | 2024-10-25 16:50:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 9caaf98f-b33b-3a09-80e0-64187f28c8fd | -9.96208 | -43.95131 | 2024-10-25 16:50:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| c027977c-8a5b-372f-bfab-3ef5b6443e9f | -9.83608 | -43.89991 | 2024-10-25 16:50:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d699c6c0-eba6-3723-915d-7861c2dfdb5b | -10.23039 | -43.9415 | 2024-10-25 16:50:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 308fef0d-a70a-32b4-a53e-eec7a691657c | -10.14503 | -44.0271 | 2024-10-25 16:50:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9642fb75-2b70-3040-b4ad-a829e0f923fc | -10.02412 | -44.13054 | 2024-10-25 16:50:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| efa17c5f-c72e-3488-9471-0f00de78cf66 | -9.9193 | -42.91224 | 2024-10-25 16:50:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 31.3 |
| 3611a2e8-d458-3032-9237-2564b1bb58f4 | -9.65077 | -42.8347 | 2024-10-25 16:50:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 88ab749d-dfee-3903-a854-20b99f72d8e9 | -9.65014 | -42.83668 | 2024-10-25 16:50:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 328ce852-ea0b-3433-a115-bf5bcd3f1fde | -10.28763 | -43.43923 | 2024-10-25 16:50:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| e0425d96-5323-347a-a2f1-110f12a10656 | -10.16269 | -43.6265 | 2024-10-25 16:50:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 360f559c-4cb8-31d6-9d2a-d1561db8bb78 | -10.74572 | -43.35743 | 2024-10-25 16:50:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 0fd06718-3005-3674-9aec-055cd808dbec | -10.62431 | -43.33599 | 2024-10-25 16:50:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b2531fd1-19a6-3bf7-b678-67e04ea69c56 | -10.76765 | -43.65315 | 2024-10-25 16:50:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f1996d0e-1ceb-324f-b14b-3869905bc7a8 | -10.47883 | -43.64356 | 2024-10-25 16:50:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 44dc8667-d684-3fb9-b171-a2bebff2ddd9 | -10.44512 | -43.47712 | 2024-10-25 16:50:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c57de1bf-502d-3db5-a410-c67046d1ef02 | -10.43231 | -43.49509 | 2024-10-25 16:50:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54f6f694-95d4-335e-bbbb-368d832a71fa | -10.35725 | -43.47021 | 2024-10-25 16:50:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 17c78ffd-0416-3e5a-9d39-f1e17897ea13 | -10.79321 | -44.02706 | 2024-10-25 16:50:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ca36aa5d-c58a-31b7-8519-4197ef58c483 | -10.76977 | -44.20736 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 99df4d79-51bc-3311-a141-9c933c84b515 | -10.76933 | -44.20423 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 4ecefa3c-6f64-30ef-a6a9-b333b872bf97 | -10.76912 | -44.20367 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 9a241f55-b2ff-31eb-b258-73081956a634 | -10.7687 | -44.20051 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| f17c19cd-6774-31f6-ab22-8208f26706e7 | -10.76526 | -44.20496 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 09b45907-8af7-38b6-bb4f-f2e43817f951 | -10.76505 | -44.20439 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| bde096ed-1e96-38c1-aba9-f98e35267c98 | -10.71441 | -44.10347 | 2024-10-25 16:50:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 69c57604-1f9a-3d27-8bfa-8972255a4d06 | -10.6775 | -44.25481 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 07ca3780-a066-3985-939a-72cc22cb34b6 | -10.54288 | -44.22477 | 2024-10-25 16:50:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0ca607fd-23a2-387e-93b1-7159c52dc215 | -10.54226 | -44.22104 | 2024-10-25 16:50:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3c9d456e-d62b-3b3c-9237-7aa2baf80c75 | -10.52251 | -44.1789 | 2024-10-25 16:50:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d367750e-e34f-35a7-b602-f9f3896b47a2 | -10.51018 | -44.03115 | 2024-10-25 16:50:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 882ed4a8-da38-3c5c-9ab4-1aa0b149d1b2 | -10.50927 | -44.0509 | 2024-10-25 16:50:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e0b0a16a-bd6b-311c-bf33-b71586dab554 | -10.50515 | -44.05164 | 2024-10-25 16:50:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0609c028-9363-3290-9b1f-7961ad9d44c3 | -10.48558 | -44.13567 | 2024-10-25 16:50:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 02b5d092-348b-3efb-8dee-6422a1d506b1 | -12.13752 | -44.36885 | 2024-10-25 16:50:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 572e5bc4-687b-3fa3-bbd7-a38d0845bc5e | -12.13662 | -44.3637 | 2024-10-25 16:50:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1bba2ae6-e6ec-33eb-b0fe-214bfc77a800 | -12.03625 | -44.24767 | 2024-10-25 16:50:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| addbc8f1-5058-3579-9829-3c52e914658c | -11.99439 | -43.90762 | 2024-10-25 16:50:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 05f6c333-9796-3780-b774-d89d44cf9f0b | -11.99033 | -43.90837 | 2024-10-25 16:50:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ca670df2-00a2-3029-8980-fbdf57e54b5d | -11.56036 | -44.08393 | 2024-10-25 16:50:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fa67b520-6e05-3dc9-8f59-b7de37a0fb22 | -11.53918 | -43.98587 | 2024-10-25 16:50:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |


[Clique aqui para ver as próximas entradas](README144.md)
