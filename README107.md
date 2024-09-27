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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfa0e6c2-d8ba-36bd-9c55-921e04539703 | -21.01451 | -42.66816 | 2024-09-27 04:44:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0fb75c1b-9537-3a54-aa45-8792aa18fe28 | -21.42068 | -42.98283 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e2f5d04f-0781-30be-9607-61b28e849237 | -21.41427 | -42.97292 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 2b0bbc22-a2b5-357d-9361-9b5e05ef9d50 | -21.40906 | -42.97005 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| e5f88c9e-2812-3cc8-a43b-6f2789ca7fe1 | -21.40875 | -42.97318 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 5b2d5ab4-5d71-36bf-a409-1989bcc75bc9 | -21.3935 | -42.96078 | 2024-09-27 04:44:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 93de6a91-2494-34b5-9354-2a4e16b53ef8 | -21.01986 | -42.67342 | 2024-09-27 04:44:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 835b6210-4286-3eb3-82a2-11127b5fdeb9 | -21.01466 | -42.66945 | 2024-09-27 04:44:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bb7e2763-7b89-3bce-bf5f-cbd1075fe909 | -21.00919 | -42.66829 | 2024-09-27 04:44:00 | NOAA-21 | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c9b03634-37b0-3743-ac11-2c4222cd1bf3 | -22.67601 | -42.85602 | 2024-09-27 04:44:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| b697a594-8c74-394b-bde5-486e35649cc7 | -22.67691 | -42.85305 | 2024-09-27 04:44:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 27.5 |
| bdb34427-698b-3c47-97b0-094d83c55a8b | -22.67654 | -42.85698 | 2024-09-27 04:44:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| 737fe852-cdea-3ad1-b93d-33482dd572ee | -22.55759 | -43.81285 | 2024-09-27 04:44:00 | NOAA-21 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| fd1a49cd-a795-39d5-9239-d3c8f9e69065 | -22.55726 | -43.81621 | 2024-09-27 04:44:00 | NOAA-21 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| aebfe7d9-8f02-39f9-aee7-af9ae88dc60c | -22.41096 | -43.957 | 2024-09-27 04:44:00 | NOAA-21 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 39073dd2-982f-3b64-ab0e-5f3fcef98762 | -22.41064 | -43.96037 | 2024-09-27 04:44:00 | NOAA-21 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 02ff69a4-0f1a-38e7-8b26-752a42862017 | -22.40573 | -43.95719 | 2024-09-27 04:44:00 | NOAA-21 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| be26c483-de99-35da-a8eb-40f44c932c1a | -22.40538 | -43.9607 | 2024-09-27 04:44:00 | NOAA-21 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5f7ecc4c-787a-3ec2-bca5-c807818258c9 | -22.39348 | -43.53675 | 2024-09-27 04:44:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 58a44488-708c-3b0e-b82c-d051f69a8ef5 | -22.38854 | -43.53242 | 2024-09-27 04:44:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| cab7a756-b073-36c5-8d94-aac113b2806e | -22.38825 | -43.53539 | 2024-09-27 04:44:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5ddd80fb-a0ba-3022-83cf-089753800b6a | -22.37741 | -43.95896 | 2024-09-27 04:44:00 | NOAA-21 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4519639e-f064-3a82-b766-15f1a694a682 | -22.37709 | -43.96204 | 2024-09-27 04:44:00 | NOAA-21 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a0d569b3-dcca-31e0-ac8e-d9cef765e667 | -22.35214 | -43.5204 | 2024-09-27 04:44:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 9b2fd0a9-ba24-3238-ba15-b43d20e292c1 | -22.67635 | -42.85207 | 2024-09-27 04:44:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| 56bf839d-54e8-3193-8e05-fd70cd84c50c | -22.67617 | -42.8609 | 2024-09-27 04:44:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| 7723679e-0a50-38cd-8e31-c1ee38892e78 | -22.67567 | -42.85995 | 2024-09-27 04:44:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| 274e53c0-4baf-3718-b469-90c9302335ea | -22.44021 | -44.1325 | 2024-09-27 04:44:00 | NOAA-21 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| def2c684-57d0-3abf-b315-87a91c9a3aa3 | -22.43988 | -44.13576 | 2024-09-27 04:44:00 | NOAA-21 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3d372ba9-0d77-361b-8621-a2e620ade4e7 | -22.43411 | -44.14169 | 2024-09-27 04:44:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 391b4f1b-d4d5-3fcb-a299-8a5f2f0b7ea6 | -22.42928 | -44.13832 | 2024-09-27 04:44:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 72dc9eaf-568b-34bd-935b-635052df5446 | -22.11653 | -44.17213 | 2024-09-27 04:44:00 | NOAA-21 | SANTA RITA DE JACUTINGA | MINAS GERAIS | Brasil | 3159308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f32b256a-69f1-300f-bcb3-e14cfd7075ed | -22.11618 | -44.17545 | 2024-09-27 04:44:00 | NOAA-21 | SANTA RITA DE JACUTINGA | MINAS GERAIS | Brasil | 3159308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 80228ed8-c667-31cd-9a94-bb87c4d762cf | -21.65494 | -43.96462 | 2024-09-27 04:44:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bf2dc6e8-15a7-3c07-8ce6-bf45d76b828d | -21.19697 | -44.87679 | 2024-09-27 04:44:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9d99cd30-5332-322b-9d81-3d18672f31e6 | -21.19694 | -44.87848 | 2024-09-27 04:44:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c62a39fd-4607-3ea5-9cb6-1f0a3772cae0 | -21.19633 | -44.88261 | 2024-09-27 04:44:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d40f12b2-4a19-3bc4-9715-16067ec3f6ae | -21.19577 | -44.88977 | 2024-09-27 04:44:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4ad1d329-a93c-35a2-8237-b3dadba9b033 | -21.19571 | -44.88818 | 2024-09-27 04:44:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 99d16caa-797e-3ad4-8db4-5241a2d66d15 | -21.19538 | -44.93986 | 2024-09-27 04:44:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 24ade737-336f-327b-81a5-ed3dbb9f9df6 | -21.19497 | -44.93818 | 2024-09-27 04:44:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 018e9765-2e4b-309b-b780-7eaaa55049cf | -22.31621 | -45.47746 | 2024-09-27 04:44:00 | NOAA-21 | PEDRALVA | MINAS GERAIS | Brasil | 3149101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 5c0bfa38-345f-36a4-b15d-8de6ac79a401 | -22.31564 | -45.48256 | 2024-09-27 04:44:00 | NOAA-21 | PEDRALVA | MINAS GERAIS | Brasil | 3149101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f1657300-c1cd-3a86-9c96-c243bc00cf33 | -22.31462 | -45.47231 | 2024-09-27 04:44:00 | NOAA-21 | PEDRALVA | MINAS GERAIS | Brasil | 3149101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 222cc53b-b339-3008-b79a-df9e9d7a8005 | -22.31406 | -45.47768 | 2024-09-27 04:44:00 | NOAA-21 | PEDRALVA | MINAS GERAIS | Brasil | 3149101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6bc1e34c-ed7a-3a71-97a3-79e67ca58e05 | -22.31352 | -45.48285 | 2024-09-27 04:44:00 | NOAA-21 | PEDRALVA | MINAS GERAIS | Brasil | 3149101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 3ad5f079-fecd-37ca-aa50-c80e04928eb2 | -22.90554 | -44.73849 | 2024-09-27 04:44:00 | NOAA-21 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b9a3cec0-9077-383e-b3f6-568a150f5933 | -22.90057 | -44.73822 | 2024-09-27 04:44:00 | NOAA-21 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f7de9a0e-4e90-3176-9cba-702412f79228 | -22.74975 | -44.78125 | 2024-09-27 04:44:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 01c22b49-d625-3625-98a0-ec0d710d484b | -22.74927 | -44.78593 | 2024-09-27 04:44:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 1f8bd12a-b117-3744-8b53-1d643f85258c | -22.7482 | -44.79639 | 2024-09-27 04:44:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 4df1f7e7-4d88-346f-bb48-5e4de32acd09 | -22.74767 | -44.80151 | 2024-09-27 04:44:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 0beb89b9-78a5-3678-b374-83213a35aba0 | -22.74715 | -44.8066 | 2024-09-27 04:44:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 69fae005-7466-375d-88df-549c202bd711 | -22.74444 | -44.78439 | 2024-09-27 04:44:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| eee2ee73-b2ac-3aa5-bc66-ef464c98b9a6 | -22.74339 | -44.79476 | 2024-09-27 04:44:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 64618030-526b-32be-9412-4edf328d1736 | -22.74286 | -44.79995 | 2024-09-27 04:44:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 771b2ba3-98e1-3cef-921e-726b6da0af2f | -22.74233 | -44.80514 | 2024-09-27 04:44:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| a25ff56b-083b-35d1-ae0e-1f2e595647d7 | -22.7418 | -44.81032 | 2024-09-27 04:44:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.4 |
| e9837862-c771-39cb-bd80-2ccd579fdf99 | -22.73806 | -44.79819 | 2024-09-27 04:44:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 32a14d34-bb40-3b10-bbff-e33dc4009ec8 | -22.73752 | -44.80349 | 2024-09-27 04:44:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| fe7afdea-0a2c-334d-8c13-f50ee6a66b75 | -22.73699 | -44.80866 | 2024-09-27 04:44:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.4 |
| 18fba2ce-2a1f-3dd8-ae3a-19d17f45020b | -22.73327 | -44.7963 | 2024-09-27 04:44:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 85e04c75-b0ea-318e-bead-c602b88cc42b | -22.73274 | -44.80153 | 2024-09-27 04:44:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| b0810916-9fbe-3931-870b-316f93d0cb74 | -22.7322 | -44.80687 | 2024-09-27 04:44:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 8cab3362-2b44-35bd-b485-2538c3d95830 | -22.64937 | -44.86396 | 2024-09-27 04:44:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 8dda38ce-b680-37eb-b7b4-1977ad6ce380 | -22.64876 | -44.86981 | 2024-09-27 04:44:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f2444604-4648-3a26-bbad-a3b01d8ef6c6 | -22.6445 | -44.86322 | 2024-09-27 04:44:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 7760291e-1e19-30a9-931c-42551daf6143 | -22.6439 | -44.86896 | 2024-09-27 04:44:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 50914b8a-66b6-39bd-8981-0d481c4bddcd | -22.59264 | -45.22191 | 2024-09-27 04:44:00 | NOAA-21 | PIQUETE | SÃO PAULO | Brasil | 3538501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 477dbd07-944f-3bf0-a5e8-a8d007ffe5c2 | -22.51987 | -44.8466 | 2024-09-27 04:44:00 | NOAA-21 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 318d73d9-6b70-3466-8d3f-643e36e3e678 | -20.65659 | -46.30688 | 2024-09-27 04:44:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d34e4ad-3427-34b8-9d9a-d8342cdcd39e | -20.55105 | -46.36486 | 2024-09-27 04:44:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78347c56-daf3-3c65-95a1-71f13093e309 | -20.5338 | -46.36273 | 2024-09-27 04:44:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a2c2282-06a7-3149-917d-3ad76996c935 | -20.52946 | -46.36242 | 2024-09-27 04:44:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| edf529b0-50f2-3132-b134-f868cfbc53f9 | -20.5132 | -45.88923 | 2024-09-27 04:44:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c09740ed-a675-3c92-ab47-2f68bf4b3f88 | -20.50877 | -45.88861 | 2024-09-27 04:44:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 80d9c6b5-2352-35c3-b101-45b6dd33962b | -20.50826 | -45.89299 | 2024-09-27 04:44:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7abd2e8d-887a-39d0-9d7a-cba31f14cdce | -20.50383 | -45.89231 | 2024-09-27 04:44:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41ed8174-ccac-38b5-901b-94ffcabda9be | -20.34201 | -46.16735 | 2024-09-27 04:44:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b47a4b85-c611-3279-9b89-97b6feddd57e | -20.33678 | -46.39667 | 2024-09-27 04:44:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9ddf605-2d5a-3b0c-9320-13dc75fb59b4 | -21.28789 | -46.63886 | 2024-09-27 04:44:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0f066881-c4f3-32aa-98a5-dbfe48d9594e | -21.21197 | -45.78119 | 2024-09-27 04:44:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f62c4625-b8fd-3eac-9695-680a9f605ad8 | -21.21047 | -45.77976 | 2024-09-27 04:44:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4f5ca7b4-711f-30fb-a00c-f849ff9e6f37 | -22.16545 | -45.82911 | 2024-09-27 04:44:00 | NOAA-21 | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 912172a9-6347-32ca-8e27-d1bc99ad1a8e | -22.16478 | -45.82807 | 2024-09-27 04:44:00 | NOAA-21 | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3380ed83-7c3a-3ab1-b87c-685aaa101d2a | -22.16023 | -45.8274 | 2024-09-27 04:44:00 | NOAA-21 | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4251081a-a215-3751-a9b1-5e886a8fe0e1 | -21.96634 | -45.82008 | 2024-09-27 04:44:00 | NOAA-21 | SILVIANÓPOLIS | MINAS GERAIS | Brasil | 3167400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 094fdd24-e3db-3dc4-b32a-c03741f91a2a | -21.96539 | -45.81907 | 2024-09-27 04:44:00 | NOAA-21 | SILVIANÓPOLIS | MINAS GERAIS | Brasil | 3167400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 4c58df87-07f0-3ccc-aa38-02fc29cde7b8 | -21.96179 | -45.81953 | 2024-09-27 04:44:00 | NOAA-21 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 2e485623-051d-3f5d-9b59-e1ee8c2c8aa7 | -21.96084 | -45.81849 | 2024-09-27 04:44:00 | NOAA-21 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b9d1dbbc-c2b7-3e80-8c94-513b9fa87bbc | -21.95672 | -45.82373 | 2024-09-27 04:44:00 | NOAA-21 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2c7cc077-45d5-317e-b10d-06bccdcf809a | -21.95573 | -45.82273 | 2024-09-27 04:44:00 | NOAA-21 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| cbfc47a3-6028-3355-b6d7-38bf87ac0a3f | -21.95218 | -45.82302 | 2024-09-27 04:44:00 | NOAA-21 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0c19efe1-79ae-33f9-9131-ccc0801b3439 | -21.9512 | -45.822 | 2024-09-27 04:44:00 | NOAA-21 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9983b203-eba2-3830-b18c-3a43b99dff8e | -21.92058 | -45.8072 | 2024-09-27 04:44:00 | NOAA-21 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b4434bad-8d4d-357a-af52-39f00d2d8ac0 | -23.33813 | -46.77225 | 2024-09-27 04:44:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ec923feb-c52c-32ea-a72c-d0ee9e8e7a71 | -23.22414 | -46.63844 | 2024-09-27 04:44:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| a02bd0a6-19d7-397c-9d67-5f3dca2e7920 | -23.35605 | -46.25521 | 2024-09-27 04:44:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7019d55b-9b44-344b-93ce-118493fae452 | -22.49249 | -46.11203 | 2024-09-27 04:44:00 | NOAA-21 | CAMBUÍ | MINAS GERAIS | Brasil | 3110608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 307ec5d8-fa27-33b1-8616-1e5072abecdf | -22.49196 | -46.11683 | 2024-09-27 04:44:00 | NOAA-21 | ESTIVA | MINAS GERAIS | Brasil | 3124500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README108.md)
