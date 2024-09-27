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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7f5de9a-265c-3e0e-8c1c-071a735139a1 | -14.86617 | -48.91113 | 2024-09-27 03:49:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ecf0e960-cb58-3066-957e-5df242843d07 | -14.86294 | -48.89845 | 2024-09-27 03:49:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92b1a2f3-a3a9-3e1d-9858-3b26ed0fb051 | -14.85806 | -48.89376 | 2024-09-27 03:49:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e55dce6-c9f1-3d6a-a640-045dfdd2103e | -14.83456 | -48.86631 | 2024-09-27 03:49:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 489c01f5-f91b-3e5b-adbd-f7deefd9ef9e | -14.82235 | -48.85267 | 2024-09-27 03:49:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d48fffb0-d189-387b-863c-c20f103537cb | -14.81688 | -48.85088 | 2024-09-27 03:49:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38fbfe75-3623-3911-a339-30c9499ea049 | -14.7742 | -48.8886 | 2024-09-27 03:49:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d5e7d23-d229-3c00-9f5d-311220dfafe1 | -14.77336 | -48.89271 | 2024-09-27 03:49:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b32f30e3-45b2-33d7-9307-e85c65ab5ba5 | -16.68547 | -49.14596 | 2024-09-27 03:49:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00c7c751-544b-3b4a-8d70-9ecd033e8399 | -16.31017 | -49.2719 | 2024-09-27 03:49:00 | NOAA-20 | OURO VERDE DE GOIÁS | GOIÁS | Brasil | 5215405 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9640ed79-f208-31df-ac0b-a691eef8dc55 | -15.47193 | -48.88387 | 2024-09-27 03:49:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 378bda23-a12b-3ea7-a910-5412919fba4b | -16.69091 | -49.14743 | 2024-09-27 03:49:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e2eabc0-edec-3320-b4a3-5905016c5ba7 | -19.29929 | -49.69396 | 2024-09-27 03:49:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d06fc16-3cc5-3c6a-90aa-68232d4d7253 | -19.29709 | -49.67773 | 2024-09-27 03:49:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d13a9ee4-31bc-398e-8c09-daf05c20a103 | -19.29629 | -49.68145 | 2024-09-27 03:49:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4488b1c4-e981-3b3b-89b2-f14fc4e2c362 | -19.29476 | -49.68863 | 2024-09-27 03:49:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4bed6198-b7e9-3470-936a-aaf621c47540 | -19.29397 | -49.69229 | 2024-09-27 03:49:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8cad973f-6cd7-34d6-80c3-afcdcc698a33 | -19.29179 | -49.67599 | 2024-09-27 03:49:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 175bb11d-54be-379f-b34e-7a466e4dc8f8 | -19.29099 | -49.67974 | 2024-09-27 03:49:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91023f31-eb74-34b5-b3c7-554c16b06440 | -19.29022 | -49.68334 | 2024-09-27 03:49:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b976a3d-fcf0-36a1-a577-2e04cb32785c | -19.28945 | -49.68694 | 2024-09-27 03:49:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fadb3c73-aa3e-31ca-9205-4e0dbe99452d | -19.00675 | -49.4553 | 2024-09-27 03:49:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c57b66da-1b0c-3d77-a2c9-44b4d3fbbd88 | -19.00141 | -49.45401 | 2024-09-27 03:49:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5cd4702c-ecdf-3fc9-b5ae-dbe184f818b2 | -18.39488 | -49.31427 | 2024-09-27 03:49:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 602ee099-985a-339c-b7b7-94129883a215 | -18.39415 | -49.31771 | 2024-09-27 03:49:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b218ba75-77ef-3b53-8333-137f44ad5b87 | -14.56532 | -50.35167 | 2024-09-27 03:49:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 43244b0e-e68c-3c1e-9ef1-b66bd37a4af0 | -14.94675 | -51.46979 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 81cc85b7-ff9a-3ac2-a3d2-517dd9e34e53 | -14.9465 | -51.46439 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2d669af2-6e61-308c-b6d6-5cae669e999a | -14.94524 | -51.47013 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4ed57178-9756-3e04-b5bf-71af36d24eef | -14.94148 | -51.4625 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d3e4b987-4645-3da3-aea0-5c32789b15cd | -14.94026 | -51.46823 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8ebf8941-2fef-368d-a559-ff3916ca4f95 | -14.94001 | -51.46288 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 37bd710b-4b8e-337f-93f5-cb5113ad6980 | -14.93875 | -51.46859 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5946ac9a-a9a8-34ae-b232-8be5be1ce62e | -14.93377 | -51.46667 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 00902268-258d-366c-bc55-454bf7e3d767 | -14.93352 | -51.46136 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 706f2c4f-27aa-3a80-b523-0921acabcd38 | -14.92851 | -51.4594 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e878fd9b-0554-3dc1-9701-f0411240a64c | -14.92728 | -51.46513 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f41e494c-df3b-30b0-93ac-4e765a5b0d77 | -14.92703 | -51.45982 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b511998-6b60-32de-9862-17657871336c | -14.92054 | -51.4583 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d9d11e3-7c68-3774-8bdd-481b4f67b009 | -14.9078 | -51.46048 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 42e8a49c-170b-3406-af46-1006fa90e4bc | -14.87203 | -51.53078 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81d6b4ce-ef4c-305f-841f-606b7f3fd672 | -14.86551 | -51.52924 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7c0739f-30b4-31ac-872c-94eee0144f6d | -14.85914 | -51.47069 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b5db89c-4af4-3dc2-9f92-79caf4ad817f | -14.85898 | -51.52769 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11f66c16-72a4-3965-bb88-e628290938fe | -14.85858 | -51.46691 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3654e31-c31c-3cb8-8787-9b6ebd464ab7 | -14.85791 | -51.47645 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 41e0adbd-dbe0-37df-aea7-eaa2e59ee815 | -14.85732 | -51.47265 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8014a75-96e2-3e6c-b077-cbd659df76fe | -14.85606 | -51.47841 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c7e9c38-e022-3f80-81e4-088100d831cd | -14.85141 | -51.47489 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0423a2d0-1e77-3154-8938-19574cfea9b2 | -14.85082 | -51.47112 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e768a5b-c87c-3802-82a5-6ead70786eae | -14.84956 | -51.47687 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6842c786-d274-338a-a788-a63a2eb275ee | -14.84491 | -51.47332 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1bd9c11-e335-36b8-91cd-ecc9e7e4d36a | -14.84432 | -51.46957 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cef13e38-cce4-3582-ab30-101c7751cd96 | -16.09636 | -51.94864 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a0419cb0-a51a-3f4e-a866-320bdedfb61d | -14.83841 | -51.47173 | 2024-09-27 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ed84bfc-448e-336a-81fc-c637647e6843 | -16.66314 | -50.60234 | 2024-09-27 03:49:00 | NOAA-20 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7992477e-0f5c-3245-a148-16d53975439b | -16.10965 | -51.95078 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5f5562ff-d8db-361b-833d-48ee3745d461 | -16.10846 | -51.95619 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7eb53a51-f454-3fe2-a1c4-8012acdb2dfc | -16.10802 | -51.94823 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e5f87f16-6a48-3448-ac95-0d178f7a0d6d | -16.10723 | -51.96175 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a309fb10-59fe-39dd-8b2e-8b9ca9f733e1 | -16.10685 | -51.9534 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9448cf94-6bfe-3707-85cf-94341100a0d4 | -16.10594 | -51.96758 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4ff8f642-8951-30a4-af13-f88375a67a57 | -16.10562 | -51.95881 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d0deaa88-7c27-396e-805e-dc4b1aca1d80 | -16.10433 | -51.96447 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c93cc9e6-bbfc-3b58-812f-1d988728caf2 | -16.10427 | -51.94398 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0414ffcc-d79b-3609-8246-3a58fe37691a | -16.10309 | -51.94932 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d477cb35-40af-30cc-a2b4-cdc3d0272eb3 | -16.10294 | -51.97057 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f8915b4a-7785-35ef-8efd-1bef1635fe76 | -16.10192 | -51.95461 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 86fb2f74-41cd-306c-b18c-4f9e2ac2b4f3 | -16.10072 | -51.96004 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 3143e41e-57ff-3b5b-b82e-e15e8c12e0ca | -16.09944 | -51.96584 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 38.0 |
| a6215795-31bd-370d-acd4-d6826dd9f96e | -16.09808 | -51.97199 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 8c8d5853-b3b9-3b95-903b-9e4a6a83d2da | -16.09677 | -51.97788 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| fc695348-bb7e-36a5-be87-36ed1406a6b3 | -16.09514 | -51.95415 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8111616f-a852-33cc-8188-86f6fb782fee | -16.09406 | -51.95903 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 454b50e4-361a-32db-9e5b-39cf2423b871 | -16.09291 | -51.96417 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 5193b44b-2470-3c94-a224-5a67e8c35acb | -16.09159 | -51.97015 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| cc7c0a94-36ac-34c4-9069-c295339deb05 | -16.09018 | -51.97653 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| b8fd3dc1-a381-32ba-9f1d-6010f2af4002 | -16.08876 | -51.98293 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f16a18e3-8575-33f4-b8fc-be4037e97124 | -16.08862 | -51.9525 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd61a583-6546-31f3-a317-6d8766e5944f | -16.08739 | -51.98909 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| bc49e2ac-aad0-36a0-be6f-020c22d73a74 | -16.08605 | -51.99516 | 2024-09-27 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 75fe2388-7d82-3b47-9ef0-b392daa78e1f | -15.94403 | -52.37899 | 2024-09-27 03:49:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 1ee38230-acd7-3ceb-980d-68feb4b0896b | -15.94263 | -52.37665 | 2024-09-27 03:49:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9b1d6122-3a01-3beb-9b42-13d92d13bf9c | -15.94128 | -52.38278 | 2024-09-27 03:49:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 57a91d9b-f97f-3545-922d-c75f4001385d | -17.42075 | -39.35372 | 2024-09-27 03:49:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0449e3ee-1a36-3433-b2f0-8334fcd76aa7 | -17.29131 | -39.29074 | 2024-09-27 03:49:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dc89e1a8-bbfc-339b-afb4-d928873bc57f | -17.20169 | -39.51243 | 2024-09-27 03:49:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3ca7b24e-8f5e-3403-a997-15c2a0fd3218 | -16.76374 | -39.32015 | 2024-09-27 03:49:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 374e3d49-a50d-39ad-9450-a5162df23379 | -16.76043 | -39.31958 | 2024-09-27 03:49:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 97093b2a-606d-3c2f-b7b5-78dc7e574d67 | -16.75986 | -39.32318 | 2024-09-27 03:49:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6d0a658e-c073-3315-b2a0-5b1721e4615a | -18.17208 | -39.81993 | 2024-09-27 03:49:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 0d7f49bb-8874-3b5c-8845-af1e6878d6a0 | -18.1715 | -39.82356 | 2024-09-27 03:49:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| fcedb8b1-8e7f-32a2-9f6a-e4cb1281b01e | -19.86143 | -40.11235 | 2024-09-27 03:49:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f3c69bf2-078a-3313-87cd-e86bcb531e79 | -19.83899 | -40.08199 | 2024-09-27 03:49:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 11264abc-35e1-382b-896d-3dbf982152cc | -19.56213 | -39.94312 | 2024-09-27 03:49:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 85fff34e-f5c5-359b-97a5-2445263876d3 | -19.56155 | -39.94677 | 2024-09-27 03:49:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a759c76c-3d68-33eb-837b-99fec6301ad2 | -16.17578 | -40.27174 | 2024-09-27 03:49:00 | NOAA-20 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 26c7a18e-87f3-3ac5-ac10-6500b2a83c44 | -17.06696 | -41.14585 | 2024-09-27 03:49:00 | NOAA-20 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| bd1a3522-1528-3e09-bafd-56c21504e598 | -17.06631 | -41.14968 | 2024-09-27 03:49:00 | NOAA-20 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 65bd3079-9c1c-352a-ac29-cd1be40a4942 | -17.06353 | -41.14525 | 2024-09-27 03:49:00 | NOAA-20 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |


[Clique aqui para ver as próximas entradas](README59.md)
