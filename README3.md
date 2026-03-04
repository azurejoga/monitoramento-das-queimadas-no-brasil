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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcf20b00-60dd-3b74-9ca0-d9e6547261c3 | -21.16954 | -41.86497 | 2026-03-04 03:49:00 | NOAA-20 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| ffa2854a-b146-33e5-9a75-f1f20d560b4e | -21.31273 | -48.53453 | 2026-03-04 03:49:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db8acb20-3f1a-3178-9221-6c5bc1cbaaa5 | -18.33081 | -43.15803 | 2026-03-04 03:49:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 1f0ab960-9eea-3283-9fa2-01d2669a7f3a | -21.4828 | -48.6604 | 2026-03-04 03:49:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 47ac136c-6a0f-3a75-bcf8-2361b3be4b10 | -18.80575 | -51.60688 | 2026-03-04 03:49:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8265b376-eb2e-35f2-9597-483e67ed6ae3 | -21.12968 | -43.94803 | 2026-03-04 03:49:00 | NOAA-20 | DORES DE CAMPOS | MINAS GERAIS | Brasil | 3123007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| aa1a518f-530c-3f0e-b201-37c9a9111200 | -22.14632 | -47.56454 | 2026-03-04 03:49:00 | NOAA-20 | ANALÂNDIA | SÃO PAULO | Brasil | 3502002 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b289d006-db78-3d02-a636-f2b556b28539 | -19.03415 | -44.60947 | 2026-03-04 03:49:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0130a6a5-0518-3f33-ac06-c1b7f0e186d9 | -18.6976 | -42.98275 | 2026-03-04 03:49:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 354bacef-d44d-3e91-b4d3-3ce381eca57b | -21.95182 | -44.40262 | 2026-03-04 03:49:00 | NOAA-20 | SERITINGA | MINAS GERAIS | Brasil | 3166402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c87191bf-d721-3e31-a573-65636464422a | -20.82177 | -48.28311 | 2026-03-04 03:49:00 | NOAA-20 | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31be19b3-669f-312b-b9bd-d8176c23de68 | -20.91399 | -48.5374 | 2026-03-04 03:49:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a46efeed-364d-37d8-9cfd-5793871a7774 | -21.70564 | -48.43659 | 2026-03-04 03:49:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 023308c9-3d54-33ff-a79f-e735ca356e3e | -17.53966 | -42.05503 | 2026-03-04 03:49:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 11deb195-7512-324f-90c0-e8d29033795c | -20.30082 | -49.58504 | 2026-03-04 03:49:00 | NOAA-20 | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe20c586-b378-35d8-b50a-a83a2d7ffd43 | 1.5047 | -59.9116 | 2026-03-04 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 91acc67b-3ae1-3f6b-b5b5-4f80a94017eb | -27.78539 | -54.23205 | 2026-03-04 03:51:00 | NOAA-20 | TRÊS DE MAIO | RIO GRANDE DO SUL | Brasil | 4321808 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9dc9d8af-75d5-33f3-8db8-0f340c4cd428 | -26.90644 | -50.01472 | 2026-03-04 03:51:00 | NOAA-20 | SALETE | SANTA CATARINA | Brasil | 4215307 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| d238ff0a-c183-394b-931a-4b9ac6158f94 | -25.21309 | -53.28868 | 2026-03-04 03:51:00 | NOAA-20 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ac9795ee-27c6-3ab1-8d83-8ae3c7d93acb | -27.34743 | -51.45105 | 2026-03-04 03:51:00 | NOAA-20 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ea39b5d9-6240-3f49-97b2-b8ab5836a771 | -25.21406 | -53.28965 | 2026-03-04 03:51:00 | NOAA-20 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e62d9ef7-d627-32a1-91f7-929641e1b5cb | -27.72287 | -49.108 | 2026-03-04 03:51:00 | NOAA-20 | RANCHO QUEIMADO | SANTA CATARINA | Brasil | 4214300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 323f2c0a-9b96-38ef-b3a7-347ce241a5d6 | -25.66935 | -53.80895 | 2026-03-04 03:51:00 | NOAA-20 | CAPANEMA | PARANÁ | Brasil | 4104501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 66b9e3d3-b0d0-31b0-b45b-64097edcb972 | -29.79578 | -51.51109 | 2026-03-04 03:51:00 | NOAA-20 | TRIUNFO | RIO GRANDE DO SUL | Brasil | 4322004 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| ac7bd4cf-bdec-3e41-97d9-dd739edf024a | -26.9921 | -50.58889 | 2026-03-04 03:51:00 | NOAA-20 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cc0a2858-7058-3cfd-86a3-d11b1bccd359 | -23.0377 | -47.88057 | 2026-03-04 03:51:00 | NOAA-20 | LARANJAL PAULISTA | SÃO PAULO | Brasil | 3526407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8cf79724-2208-35c0-98f1-0dce2fa5c41f | -23.70146 | -49.9663 | 2026-03-04 03:51:00 | NOAA-20 | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 1bbf8eff-67ec-382c-9c14-2f27d908d5c3 | -25.00367 | -49.30816 | 2026-03-04 03:51:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7dbc4067-92c0-3a74-a42c-8951acfd3bf2 | -29.80092 | -51.51281 | 2026-03-04 03:51:00 | NOAA-20 | TRIUNFO | RIO GRANDE DO SUL | Brasil | 4322004 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| fada8c9b-eaa9-3629-8f06-c59fb365ff08 | -26.19357 | -50.15048 | 2026-03-04 03:51:00 | NOAA-20 | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fd66d297-2c38-3599-8f28-1ab9fb952efa | -23.33343 | -53.26499 | 2026-03-04 03:51:00 | NOAA-20 | DOURADINA | PARANÁ | Brasil | 4107256 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 69289c93-f366-36b1-a6da-57974c1d23c9 | -24.77061 | -53.46849 | 2026-03-04 03:51:00 | NOAA-20 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| b29a5fb5-1685-3a8e-bc1e-f860a73babf1 | -25.00448 | -49.30453 | 2026-03-04 03:51:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 0a706c8e-d385-3b78-bd48-5e9c2f677a88 | -26.19437 | -50.14703 | 2026-03-04 03:51:00 | NOAA-20 | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f70cca80-cd79-330f-aad4-4c044eed8e8e | -23.38882 | -46.23071 | 2026-03-04 03:51:00 | NOAA-20 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| db58cdcd-14ce-3214-b2bb-7e39f5f54d2b | -22.91467 | -48.6121 | 2026-03-04 03:51:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4588aba-e447-39f3-8469-8e62042f5943 | -23.87248 | -49.99763 | 2026-03-04 03:51:00 | NOAA-20 | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 163ec2d5-cfe7-3344-9789-5390511b088e | -25.00014 | -49.29997 | 2026-03-04 03:51:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a1c3ef91-e036-39b3-9a67-87126791508e | -25.00523 | -49.3012 | 2026-03-04 03:51:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 607253ae-cd4a-3933-b4c4-129a2131b14c | -29.03841 | -51.33504 | 2026-03-04 03:51:00 | NOAA-20 | NOVA PÁDUA | RIO GRANDE DO SUL | Brasil | 4313086 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 5f2d1188-bc2a-3109-b33f-11d4eb3aed31 | -27.19029 | -51.76671 | 2026-03-04 03:51:00 | NOAA-20 | JABORÁ | SANTA CATARINA | Brasil | 4208609 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 91b6ecad-3a5e-3fe1-8de7-1da436544011 | -24.73076 | -48.58616 | 2026-03-04 03:51:00 | NOAA-20 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fa68696f-0f25-3253-b957-f53896fdf4fd | -23.47509 | -47.24709 | 2026-03-04 03:51:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 131da83f-65ab-37c7-995d-e3b754c31b90 | -24.03872 | -47.48073 | 2026-03-04 03:51:00 | NOAA-20 | TAPIRAÍ | SÃO PAULO | Brasil | 3553500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| bed10428-9bf5-34be-86d6-fb0f788c7774 | -29.75736 | -50.69501 | 2026-03-04 03:51:00 | NOAA-20 | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| d9de5318-9328-35f8-9fb5-53abad334492 | -23.44519 | -48.92942 | 2026-03-04 03:51:00 | NOAA-20 | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b33e6fb4-2443-3e77-ab03-c199ab11f848 | -23.26259 | -50.42667 | 2026-03-04 03:51:00 | NOAA-20 | SANTA AMÉLIA | PARANÁ | Brasil | 4123105 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 99dd1fbd-ecf4-3a50-aa68-0a6bc7e1f3de | -22.91269 | -48.6104 | 2026-03-04 03:51:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e1f8707-484e-36d6-a1ca-78829a5e1435 | -23.01918 | -49.26878 | 2026-03-04 03:51:00 | NOAA-20 | MANDURI | SÃO PAULO | Brasil | 3528601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e2c8db88-ba58-3587-b8c4-ccd5bc5e5a6d | -30.26184 | -54.16498 | 2026-03-04 03:53:00 | NOAA-20 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| c3a34be8-5f04-387c-9171-c94bf1828f78 | -29.66368 | -52.15346 | 2026-03-04 03:53:00 | NOAA-20 | VENÂNCIO AIRES | RIO GRANDE DO SUL | Brasil | 4322608 | 43 | 33 | nan | nan | nan | Pampa | 0.1 |
| 8dd12832-ef22-3b93-b42a-de8dbc62c6d1 | -31.69727 | -52.63164 | 2026-03-04 03:53:00 | NOAA-20 | MORRO REDONDO | RIO GRANDE DO SUL | Brasil | 4312450 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| b972ad26-4ff3-3dd1-bd31-fe5d61411e18 | -31.32314 | -52.49393 | 2026-03-04 03:53:00 | NOAA-20 | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 9979b31d-eb9c-3dea-9876-41fdd1f397d6 | -31.42213 | -52.98455 | 2026-03-04 03:53:00 | NOAA-20 | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 0.1 |
| 87c1eb02-bd81-3fbd-aeee-5c67a133b971 | 1.5047 | -59.9116 | 2026-03-04 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 17e41a29-060b-3ce6-b98f-622ede8dfd36 | 1.5047 | -59.9116 | 2026-03-04 04:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.5 |
| b93210cd-e5f0-30bd-94c6-e7c7ab2c0332 | 1.5047 | -59.9116 | 2026-03-04 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 7ae43650-65f5-31db-8268-1c9e0fa97c76 | 1.5047 | -59.9116 | 2026-03-04 04:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 1c58b916-71c8-3900-a7e1-94f359988899 | 1.11263 | -59.20321 | 2026-03-04 04:31:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 55051999-c971-3f76-af2f-db16f8e4521e | 0.73334 | -59.90148 | 2026-03-04 04:31:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 27f7996c-b775-3482-9580-780dd4aacaf4 | 0.72906 | -59.90617 | 2026-03-04 04:31:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d2dae0ba-b3dc-3c21-b624-74d04f2732a2 | 1.50638 | -59.91753 | 2026-03-04 04:31:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 67b50375-78f4-349a-876c-ae59453e7a4a | 1.10766 | -59.20339 | 2026-03-04 04:31:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0fe820b-9c43-38f5-ad9c-c5a9b1f16a39 | 1.50526 | -59.91025 | 2026-03-04 04:31:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6f68721a-1a66-3759-90ff-98bddefa138a | 1.11352 | -59.19612 | 2026-03-04 04:31:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ab2dbc0f-6b9c-3745-aed3-dd099e11c293 | 0.73612 | -59.90522 | 2026-03-04 04:31:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf03027d-30b8-34dd-b366-cadf6eeb50ad | 1.21187 | -59.97404 | 2026-03-04 04:31:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 05a3e700-1811-32ea-b0e6-8538c63cd633 | 1.05851 | -59.48836 | 2026-03-04 04:31:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb682391-8520-3c9a-af26-0e3e0ea8a9b1 | 1.51224 | -59.90826 | 2026-03-04 04:31:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6c1fbe24-b5b5-3a85-b9a9-7e59dfe2b9b2 | 1.05926 | -59.49393 | 2026-03-04 04:31:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8d0c6846-256d-3bdd-a793-71829d7489d0 | 1.07856 | -59.25281 | 2026-03-04 04:31:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8d783672-54c2-3152-9bd8-b9b47596030e | 1.0654 | -59.48724 | 2026-03-04 04:31:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ab90a8b-447a-3fbe-b5aa-d0567c57b200 | -1.51209 | -54.52186 | 2026-03-04 04:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eb3dcfee-7cfd-34ae-b4dc-5555db07b5ca | 1.11165 | -59.19703 | 2026-03-04 04:31:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3927cd8a-aaeb-3b68-b104-6ea7f6aabb03 | 1.11445 | -59.20233 | 2026-03-04 04:31:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b36fc6eb-a7f1-3404-9748-dc781895d942 | 1.0595 | -59.49465 | 2026-03-04 04:31:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c35fc6c8-3843-3703-9f69-1d1cf11eee38 | 0.73438 | -59.90821 | 2026-03-04 04:31:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2c0859d4-7dc3-3df7-9d33-0c645178a8a5 | 1.51338 | -59.9157 | 2026-03-04 04:31:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 94d14ce8-5acc-3e76-ad22-03ef3055fb33 | 1.49821 | -59.91175 | 2026-03-04 04:31:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bdd9859a-6e9c-3e43-993f-eb0c64f6224c | -6.2278 | -55.65324 | 2026-03-04 04:33:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5342055-e3c1-3460-87c5-ec76f7e9dc46 | -6.22716 | -55.65133 | 2026-03-04 04:33:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 33c331c4-f99f-38b9-b94d-cec9eef5ebf5 | -15.42388 | -52.19532 | 2026-03-04 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea3ca53a-b95b-3656-9148-51dba9e0b9d3 | -15.42731 | -52.19593 | 2026-03-04 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 58b16339-7bbd-3d88-bb4e-885eff201273 | -16.43932 | -52.47825 | 2026-03-04 04:36:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f4a270cd-3071-3ab5-8627-d8cb566ef570 | -15.42453 | -52.19145 | 2026-03-04 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 024b10af-bb33-3bf5-86b4-308e8ec4a2e7 | -21.70205 | -48.43412 | 2026-03-04 04:38:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 58219a2d-3fc7-386c-a265-dd6c58aeccfb | -22.05313 | -50.76772 | 2026-03-04 04:38:00 | NOAA-21 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bb53d0d7-e1c8-3267-afd7-ae4fcc1b1e8d | -25.00645 | -49.30098 | 2026-03-04 04:38:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 3da12169-407f-3286-9827-59d9a5a801ef | -23.01924 | -49.26593 | 2026-03-04 04:38:00 | NOAA-21 | MANDURI | SÃO PAULO | Brasil | 3528601 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4454c083-d9e8-3e25-acbb-93baf2a2224b | -21.70635 | -47.10426 | 2026-03-04 04:38:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6575ce89-31e9-38a2-9722-08b8e1fd2aef | -21.70562 | -48.43465 | 2026-03-04 04:38:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d5cebe41-28f7-353d-806b-8d5e84872cbc | -21.22337 | -49.92986 | 2026-03-04 04:38:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9947d718-7a11-3865-bae5-2d251100b8a7 | -25.0029 | -49.30032 | 2026-03-04 04:38:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 397be4be-99ab-3506-a0c4-0838d52c4004 | -21.70795 | -56.3215 | 2026-03-04 04:38:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a35bb47b-550e-347e-80a2-3a1aee85fc02 | -21.50584 | -49.13676 | 2026-03-04 04:38:00 | NOAA-21 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ee897efe-f20b-3367-b085-81aad15346cd | -25.00586 | -49.30539 | 2026-03-04 04:38:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3ceeb3fd-185b-3650-bf43-6b2ac184a999 | -20.92027 | -50.52928 | 2026-03-04 04:38:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8608190c-a9b9-393c-9558-6cd5214a5d8c | -20.91694 | -50.52871 | 2026-03-04 04:38:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 638b502f-f0fc-381f-8371-67a463fe28d0 | -22.78378 | -55.39542 | 2026-03-04 04:38:00 | NOAA-21 | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c5e2579b-6992-3bb5-8aef-2af78f896df6 | -21.11011 | -49.26045 | 2026-03-04 04:38:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README4.md)
