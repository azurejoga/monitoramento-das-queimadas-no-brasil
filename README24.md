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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e71ed4c-46c5-38fa-a9b6-4fddcc7fd3c5 | -15.58892 | -48.35241 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 3c0a5ae7-4aae-3cb5-a045-6176db16aa73 | -14.81722 | -46.7252 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0237fd47-5e9d-3b75-9604-48f6ecf90124 | -15.3263 | -46.10989 | 2025-09-01 03:47:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9eab05e5-6ee7-399d-bb5a-e885fde69907 | -16.15309 | -49.64101 | 2025-09-01 03:47:00 | NOAA-21 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4b119ad6-7fe4-38a1-8ec3-7a3107529040 | -16.15681 | -40.33938 | 2025-09-01 03:47:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ccb0f8df-5232-3a53-ae16-e92bbb86d76a | -15.59487 | -48.35294 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 77cb2a27-74d0-3f80-9b5c-c5eec21fd51c | -16.97191 | -49.31194 | 2025-09-01 03:47:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22d3009a-4b70-35ab-8c94-32ddb69efe96 | -15.59867 | -48.33485 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 23972ea1-428d-32cf-894b-54344062bee5 | -21.08429 | -48.22664 | 2025-09-01 03:47:00 | NOAA-21 | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5ff084f5-2c05-378a-b5b6-ab180a186315 | -18.12126 | -48.54129 | 2025-09-01 03:47:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 116a3627-8dd8-38f5-9f9f-46d41ea24189 | -14.75038 | -46.7637 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e020e89b-ad26-3927-8bf2-35b286bbd10a | -14.83741 | -46.73428 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3bc101ec-61cd-3dda-83a6-d64b1ee508e4 | -19.12335 | -46.4501 | 2025-09-01 03:47:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0faa8d3e-27de-3daf-a91b-5f8a6ddf6317 | -16.15501 | -49.63843 | 2025-09-01 03:47:00 | NOAA-21 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 6bffdfa1-ed6d-3f62-a6e2-82a8abefeb61 | -14.98423 | -46.70919 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 966ca04d-d32f-3ff2-9f73-462f2d8d7f61 | -17.72654 | -42.89896 | 2025-09-01 03:47:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdf0a9a8-4a4e-3e34-bd09-9b6553e543b1 | -18.11481 | -48.54421 | 2025-09-01 03:47:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b4c68db6-05d5-32c5-a27d-b3384ccf927c | -19.84404 | -44.99553 | 2025-09-01 03:47:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a28eef5b-fb0e-338a-a9ef-2ec9695f802a | -15.77478 | -47.80149 | 2025-09-01 03:47:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 65d40230-009a-34d3-9c3f-9144458f0067 | -14.80136 | -46.72936 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 415bd56e-f466-3824-877e-b0ec9081f004 | -18.07761 | -45.94947 | 2025-09-01 03:47:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4782c9fc-f92d-38d2-9155-666f1a0215d6 | -13.68587 | -50.77151 | 2025-09-01 03:47:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9d9c28fe-624d-3ddd-b419-2a56422f5539 | -19.12227 | -46.45551 | 2025-09-01 03:47:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ec89a3a-9e19-3d0b-b06a-7db8bf4f2d6d | -16.13469 | -49.04955 | 2025-09-01 03:47:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51513d93-20ac-3eeb-9a99-a8a5df8db499 | -18.07289 | -45.94843 | 2025-09-01 03:47:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c576ffb-fbe6-3742-9ba5-5ef2316cf168 | -15.72589 | -48.98988 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e5d6d86e-aa1a-3d25-8516-215c5b0a4c73 | -14.78997 | -46.73124 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e58e9029-6aca-3b0d-8950-edc60932a1c0 | -15.08155 | -48.12277 | 2025-09-01 03:47:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c7e529c-16bb-3599-bece-fb3a1a5f08dc | -16.15432 | -49.63548 | 2025-09-01 03:47:00 | NOAA-21 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 56a705d4-1963-32b9-94f6-bcdeffc4b787 | -14.73836 | -46.74107 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5f934df-8796-3a05-b271-2ced7031e002 | -15.69528 | -48.91753 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d5bb14af-7307-3d5d-a3ac-f70ce08ff65c | -15.5946 | -48.35406 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 7bd6ea64-333f-3538-aa04-1f0d3beb6b77 | -21.0939 | -48.23225 | 2025-09-01 03:47:00 | NOAA-21 | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 50392617-7b64-3860-af47-d130c8d5b474 | -15.58822 | -48.35601 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c386f91f-d28c-3b31-aeb6-2f7789d5b2b7 | -18.66618 | -52.5906 | 2025-09-01 03:47:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| e7af50cc-7061-3096-ac85-1df12c08cbfc | -19.35074 | -44.00127 | 2025-09-01 03:47:00 | NOAA-21 | FUNILÂNDIA | MINAS GERAIS | Brasil | 3127206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09335671-7a8a-3cec-8b3f-7523c9e32cab | -19.84057 | -44.99022 | 2025-09-01 03:47:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f609a366-0326-352c-a884-b1f689173da1 | -14.82169 | -46.73796 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e272a731-5d97-3262-974b-2116b232d506 | -15.5979 | -48.33812 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f3051e89-c837-33df-b2a7-aaf613b4302e | -16.08172 | -43.62471 | 2025-09-01 03:47:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64c2c6c2-6bea-3b30-ba09-141f4b07b353 | -18.65623 | -52.60176 | 2025-09-01 03:47:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| af678ad8-cec7-3941-acaa-1259b5f5e835 | -14.75187 | -46.75628 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 544fc813-9aa8-3109-8cb3-909ba7f3fc0f | -14.75116 | -46.75985 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2498a6f1-a846-33b8-a423-4850a2e3323c | -15.58506 | -48.34223 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4ef49ae8-a844-32a4-8c48-7cfcf7ed2737 | -15.58917 | -48.32202 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a20e4a76-4224-3366-a19a-27a1bb6f3423 | -14.79166 | -46.72272 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 62364f8c-9b6a-39b8-b49b-94fc0623848f | -21.35149 | -49.05453 | 2025-09-01 03:47:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 50a97c9b-82be-3ca2-b78c-49bf5b6d62a7 | -21.09015 | -48.22454 | 2025-09-01 03:47:00 | NOAA-21 | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 18.9 |
| aa74666e-d7ac-3cfc-b449-0741239ac6c7 | -16.16033 | -40.33998 | 2025-09-01 03:47:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2850bcb1-790c-3e2a-b56a-fe36e5facb6f | -13.69275 | -50.7729 | 2025-09-01 03:47:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 95c2d5e4-fbd5-365a-a575-3f509d0a5374 | -16.07823 | -43.61983 | 2025-09-01 03:47:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4fe93a8-ad3e-31a8-a864-b8b738603be3 | -14.77753 | -46.76608 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1c1c21d-088a-3204-8146-e4c1560348b0 | -15.69532 | -48.9283 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f1789334-5e25-317b-898c-23a23de07a39 | -14.77223 | -46.76498 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd497525-7146-3605-92fb-bffe9f497f8f | -15.72487 | -48.99469 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a4a1214b-1cf5-3271-8d0e-427bc07260fa | -14.8252 | -46.74015 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aeaf0afc-5ca6-3371-acde-26251f5a75b5 | -14.78272 | -46.76778 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22801c76-5c82-3ce4-a2ef-30bf7f1e63c7 | -18.66273 | -52.59927 | 2025-09-01 03:47:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| f876b61e-7dcb-30ca-a192-912c417868e9 | -15.69129 | -48.94703 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dc032524-e291-3df0-9088-d72fc9109f72 | -14.76159 | -46.76293 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 172c144e-3a1a-3f79-a78e-c2bd561663aa | -14.81338 | -46.72425 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72e13580-30b4-3c32-ac6c-ff715cbc90c4 | -15.59386 | -48.35791 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ed64d234-eb3a-3353-a7af-5fed96debd42 | -14.83217 | -46.73295 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 650b45f3-1130-3322-a394-bc44cb6fe89b | -19.52025 | -44.1032 | 2025-09-01 03:47:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fc78532-47cd-307d-816e-d758a1d3d1fa | -15.70159 | -48.92812 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7e3fd374-db20-36f9-98d0-838fc78c7ce1 | -19.85969 | -45.01586 | 2025-09-01 03:47:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6cc23dc-27a5-3cdd-bf88-5c644c3b621c | -15.70244 | -48.92415 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8cbc1f02-475c-3544-85b7-72a3c7d9e5ff | -16.07749 | -43.62389 | 2025-09-01 03:47:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ab4aaca-99a5-3eaf-a9b2-9c54b0506096 | -15.58994 | -48.3476 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c209145f-f92d-3926-90e7-ff51243e578a | -14.849 | -47.10076 | 2025-09-01 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 0660e07c-a81d-3691-b12d-b07deac8e756 | -18.65583 | -52.59749 | 2025-09-01 03:47:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 919b4a82-03c3-31cd-83c3-798ed3aadac1 | -17.20704 | -46.06563 | 2025-09-01 03:47:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1107b184-816d-30a1-8b2b-72b714dea800 | -15.72688 | -48.98521 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| cf9dbf9e-3c2c-38be-86d0-b603ec11bfa7 | -14.76235 | -46.75915 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ef043c7f-544a-38eb-8da9-d1379ef15e60 | -18.53206 | -45.025 | 2025-09-01 03:47:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 968b608e-f96c-350e-84b1-a239f8abd403 | -15.69925 | -48.91 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| dbdb5445-101e-3903-aeb1-22691f1f1faf | -15.71668 | -49.00374 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1b2348eb-7e16-3acd-b95a-1976a86a6ebf | -17.83036 | -44.32711 | 2025-09-01 03:47:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6cc3188d-9f48-36de-8a6d-490c7b8ffe9a | -23.51472 | -46.5946 | 2025-09-01 03:49:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| dc2a1ce4-eb35-312c-b214-b035bd5314af | -23.18704 | -45.7487 | 2025-09-01 03:49:00 | NOAA-21 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9e29d1fd-cc6a-3570-991d-6bac27458217 | -22.36123 | -52.13654 | 2025-09-01 03:49:00 | NOAA-21 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 0fc56c97-c5f6-3e1f-8047-45a35a373535 | -23.32138 | -45.97295 | 2025-09-01 03:49:00 | NOAA-21 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 82fddf93-3a40-31ad-a787-8ae9ad3e3347 | -22.37497 | -52.44847 | 2025-09-01 03:49:00 | NOAA-21 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 0af355c3-74ba-38eb-9263-01c8a35a2a20 | -23.19127 | -45.74966 | 2025-09-01 03:49:00 | NOAA-21 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1602a483-a397-3854-a4de-a9a5cd569057 | -22.37589 | -52.44711 | 2025-09-01 03:49:00 | NOAA-21 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| a899632d-967b-3b93-910d-93d1f0670782 | -22.45479 | -49.01348 | 2025-09-01 03:49:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 44b26b79-bd14-370b-bed3-2ebdfb288e96 | -23.17409 | -47.11072 | 2025-09-01 03:49:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 1851ccee-33cd-34aa-8f70-b08ac33b2599 | -23.17299 | -47.11594 | 2025-09-01 03:49:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| a6a7722c-8a7b-38a6-8ba8-dab36230fcd0 | -23.3593 | -46.90857 | 2025-09-01 03:49:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6021ee73-6ea4-3672-8195-b95168af9863 | -23.11008 | -46.61346 | 2025-09-01 03:49:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a703caff-bc28-3fe2-a0cf-a8e3e0fdad1e | -23.51373 | -46.5994 | 2025-09-01 03:49:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ba0cc15e-ba0b-3806-93c5-f307022caa1a | -22.98918 | -46.21883 | 2025-09-01 03:49:00 | NOAA-21 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f89c3a53-f90e-3d65-ac44-f056593d72a5 | -22.37725 | -52.44162 | 2025-09-01 03:49:00 | NOAA-21 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 005110c9-03c2-3404-9d9a-d51afd997d0e | -23.44175 | -46.94751 | 2025-09-01 03:49:00 | NOAA-21 | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 61bfdc7c-9953-343b-9889-f5c3da4dd07f | -23.43219 | -46.80666 | 2025-09-01 03:49:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4ed97577-1297-31ef-b1ef-b9d916073385 | -22.3763 | -52.44301 | 2025-09-01 03:49:00 | NOAA-21 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 73460c69-8a81-3977-9346-6a3bab6971ec | -22.5701 | -47.47036 | 2025-09-01 03:49:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 09ddccd0-a994-3410-843a-11159d0bbfc0 | -21.73211 | -50.7457 | 2025-09-01 03:49:00 | NOAA-21 | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| cd57e3f5-21a5-33b4-bef9-a37264be2f7a | -22.44667 | -48.43186 | 2025-09-01 03:49:00 | NOAA-21 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6c33183-763a-3cde-8a52-07fdcece4d60 | -12.9006 | -56.9488 | 2025-09-01 03:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |


[Clique aqui para ver as próximas entradas](README25.md)
