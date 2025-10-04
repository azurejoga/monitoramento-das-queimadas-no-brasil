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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1868028c-4af2-3f95-99ec-5c07bf2658a4 | -21.69553 | -50.08226 | 2025-10-04 04:17:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4a7fd305-77af-384f-81de-3ccf03693dc6 | -19.85896 | -42.58929 | 2025-10-04 04:17:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 71ec9746-c3d8-3b43-82d0-e47841637d4d | -20.13646 | -46.42278 | 2025-10-04 04:17:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9fe5efcd-6834-374e-bac1-f59b1711f946 | -15.52824 | -46.82113 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e033c13-9fea-32c9-9082-eb249fab3e2a | -21.68707 | -50.06658 | 2025-10-04 04:17:00 | NOAA-20 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 429392b0-62c6-35e3-9d2e-d493fe576734 | -15.73208 | -46.27202 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74777e64-3d98-3312-b30f-0821e2d5f1bb | -15.58132 | -46.94632 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e0e6cd4-915c-3e3f-9188-324c33e2eb0e | -21.31281 | -45.17986 | 2025-10-04 04:17:00 | NOAA-20 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 77ce36fa-a7da-3429-a867-a5d512c44220 | -14.58289 | -52.48732 | 2025-10-04 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 78bf98f6-3aa6-3630-8ada-29eafec88c7b | -22.28763 | -46.75587 | 2025-10-04 04:17:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8cb33e56-17ba-33ad-8745-26d8f311f6f9 | -15.52514 | -46.79753 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cb35d2e-f48f-3af3-bb50-28bcbb943f69 | -14.57442 | -52.48051 | 2025-10-04 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3f7c3592-70d6-37a4-a181-19b153f706ce | -15.69189 | -46.27279 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40070266-6714-3cc3-b850-ab6f90a0332c | -15.24142 | -49.29955 | 2025-10-04 04:17:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d07baa9-f73c-3d29-8c54-f106d1a75e29 | -20.11859 | -44.39469 | 2025-10-04 04:17:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6281a2b9-7092-3bde-a482-fe9949a2ae0a | -18.45522 | -49.44246 | 2025-10-04 04:17:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 13a6e72a-b298-3df0-9cca-74465c6d1c1e | -14.74949 | -54.64133 | 2025-10-04 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebf49015-ac91-30d6-a6c6-a788152aabbc | -17.06116 | -46.63315 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65af8975-ded8-34de-991f-b4040b022dcb | -18.68542 | -48.17777 | 2025-10-04 04:17:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 245c6a83-d265-3b94-a0d6-88fb32ef04fa | -18.34669 | -52.01908 | 2025-10-04 04:17:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2229f86-1ec4-3c3a-acfb-677331b916b3 | -21.52185 | -46.07671 | 2025-10-04 04:17:00 | NOAA-20 | SERRANIA | MINAS GERAIS | Brasil | 3166907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3959183d-afd5-3138-9846-6ca9288b6d1a | -15.26271 | -49.33471 | 2025-10-04 04:17:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f7083fd2-70d4-3b16-b1ba-dc2ca934d635 | -18.38571 | -48.79485 | 2025-10-04 04:17:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| cf79fd78-7749-3a93-a223-a45d8f4541a3 | -19.35244 | -43.7827 | 2025-10-04 04:17:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e277be1-16ed-3aca-be0a-2a832b379ba9 | -21.67985 | -50.06501 | 2025-10-04 04:17:00 | NOAA-20 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4826c43d-38ab-31e3-95a6-12d49b9a9e68 | -17.70957 | -47.09057 | 2025-10-04 04:17:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 474a8e53-7fa1-3eea-8f86-eaead0d5ac9c | -16.75926 | -43.96708 | 2025-10-04 04:17:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c9e90d3-0959-34fc-a3c5-9e5401ac9621 | -21.80696 | -45.64958 | 2025-10-04 04:17:00 | NOAA-20 | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 38fadd88-114b-3096-9aa3-46d3cded6ca7 | -22.28522 | -46.75215 | 2025-10-04 04:17:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 910148e2-b02b-3bf3-a345-e9bcfca2070a | -22.43115 | -46.88082 | 2025-10-04 04:17:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 045d342b-c4d3-35f5-9bd8-7ce604edbde3 | -15.23978 | -48.71513 | 2025-10-04 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4aa63190-ea1e-3e66-aef4-611ee24ee488 | -15.52421 | -46.82441 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 87f52fe0-5509-35c9-ad5c-2c992694aec5 | -21.35082 | -45.79536 | 2025-10-04 04:17:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 03dc1ff9-d174-3f36-b970-986e9f4d3f44 | -20.35566 | -48.78958 | 2025-10-04 04:17:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f612eb8f-5651-3547-b8b1-287848c24641 | -16.3564 | -49.39675 | 2025-10-04 04:17:00 | NOAA-20 | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d56e1fe-5ae7-33d7-99b0-7e73d28e2f26 | -17.55722 | -46.75701 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 866c2125-79c7-30ac-b986-d1df382df87f | -15.73938 | -46.2695 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7682e06f-f4c1-360a-99e6-6a999d94d6b5 | -18.73384 | -43.1486 | 2025-10-04 04:17:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dfed2948-bfc6-3027-8958-55b539206d63 | -15.58076 | -46.90747 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d712ef7-4fac-382d-a61b-2ae1b1e63790 | -21.69634 | -50.07773 | 2025-10-04 04:17:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 572639cb-9b95-31e6-957e-16e424bcb20f | -17.08691 | -46.24204 | 2025-10-04 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 13cb4bb7-4dd3-3de8-b2aa-5ea424fe36c1 | -15.25577 | -48.06135 | 2025-10-04 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| badd586b-3104-313a-8674-5149a73bb13a | -15.61163 | -46.93256 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d13cbac0-644d-30b2-9322-b5e1f29482ee | -16.09005 | -51.06815 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54b96026-da91-3471-9995-3f9adddae715 | -15.58356 | -46.9117 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de495742-d1d6-3981-853a-21be21aa6c3a | -17.07967 | -46.24451 | 2025-10-04 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fab5ec8-715d-3ac2-9914-44bd075a1196 | -22.27802 | -46.75466 | 2025-10-04 04:17:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 7958b2a8-8214-3a90-8265-f02b17c8acde | -21.78695 | -45.33588 | 2025-10-04 04:17:00 | NOAA-20 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| b5ee3f37-fd74-3a5f-a2f0-b81a8cf17698 | -14.98428 | -49.97381 | 2025-10-04 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 88695915-61d4-3fab-a54f-0c10cc9b9211 | -16.01096 | -50.93313 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7b751e6-668d-331b-aaa2-d20703a51c30 | -18.45889 | -49.44315 | 2025-10-04 04:17:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2b7e6057-cd44-3418-bd3f-9fe251ad247d | -14.98111 | -49.96847 | 2025-10-04 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0abbcb15-49a1-33e4-99b5-3349e6c231e9 | -16.02382 | -44.28255 | 2025-10-04 04:17:00 | NOAA-20 | JAPONVAR | MINAS GERAIS | Brasil | 3135357 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e400863-77fd-3f50-9574-66461702013e | -15.527 | -46.82867 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c51c27f8-11f4-3748-9905-404c858e3764 | -16.05123 | -50.92458 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 539024ca-11b4-3389-9ce1-f5f3299185aa | -17.00788 | -49.14905 | 2025-10-04 04:17:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ed49b60-1a25-3d30-aeb0-53b7537850a1 | -17.61779 | -44.46101 | 2025-10-04 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d151c6e-964b-3944-95a5-37e510e7fa36 | -15.59705 | -52.4931 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e1428b87-e94a-3100-a44c-8a9fb7ca5bea | -16.02202 | -50.94293 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b17b6606-dca9-349e-8ffe-d64692b6a2e1 | -16.40097 | -52.15219 | 2025-10-04 04:17:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66709869-d760-3e66-9203-2864b4b2d582 | -19.46446 | -43.6607 | 2025-10-04 04:17:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d6ab0f03-4fb7-3702-82f4-a5e619acf08d | -18.69234 | -48.17906 | 2025-10-04 04:17:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| dcc4807f-2b3b-390a-88d8-895a16e4b43d | -15.52906 | -46.83984 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f67282d6-cbba-3bdf-aae1-9dac85130414 | -15.53433 | -46.82922 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08604a58-e58c-3117-997e-dbe8782c61f6 | -15.26157 | -47.9636 | 2025-10-04 04:17:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2b32760-d631-3a5a-b5f0-4dfc690b8443 | -21.06882 | -46.90093 | 2025-10-04 04:17:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 726ba995-93d7-3ceb-bcc1-0525bd70702e | -19.59649 | -44.64042 | 2025-10-04 04:17:00 | NOAA-20 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ddb3775-c4a4-3746-bf43-9d14f41a7dd6 | -16.09498 | -51.06501 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4f0ca90-41af-33fc-95da-ed99786ca64b | -16.35033 | -47.07187 | 2025-10-04 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4983f38f-6025-39f7-a822-98299a638418 | -16.29141 | -45.24499 | 2025-10-04 04:17:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| facbcec3-c10d-3df6-ab0b-a2c3d53f3476 | -19.1056 | -44.71185 | 2025-10-04 04:17:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de32827a-14ca-3b15-b634-4be3b12012d4 | -16.04232 | -51.04237 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4eae148e-2727-340f-99fb-0530b34d5ecd | -22.12238 | -42.91291 | 2025-10-04 04:17:00 | NOAA-20 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dd0b80b1-2b94-37f1-bf38-23cb26850dea | -14.95928 | -49.99884 | 2025-10-04 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e5ce5e8-9cfd-336f-b8d4-41890443a877 | -16.29529 | -45.24196 | 2025-10-04 04:17:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c3e8b0e0-89c4-3fde-85ca-9e7b85f52983 | -15.60661 | -52.47707 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 74468ace-9785-3165-9b5b-e834a7bfce0c | -20.84296 | -46.42104 | 2025-10-04 04:17:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0e4871a-e979-375f-a1ae-9a9afec5b376 | -15.30133 | -47.94506 | 2025-10-04 04:17:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c381f32f-5666-3ba9-9901-281b97ef887a | -15.53309 | -46.83663 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 04113072-28f5-36cf-ae87-0b2bc7dd8aa5 | -14.74812 | -54.64829 | 2025-10-04 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcb17a83-cbe3-3f65-ac2c-b58bbcc4a5da | -19.76664 | -43.7917 | 2025-10-04 04:17:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 373f875b-2351-3225-a6cd-7f4d52ee2b9d | -15.60199 | -52.46797 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 491e282c-9268-32ce-b874-a15dec03fd6c | -15.71927 | -46.27366 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a9de0aa7-2673-3d44-9c03-00d346e33438 | -22.18762 | -46.78786 | 2025-10-04 04:17:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 034bc7e4-6944-354c-bafd-e142f4df5be9 | -21.59607 | -45.27722 | 2025-10-04 04:17:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e4683cc3-03c1-3290-ae57-3423d7827995 | -18.46172 | -49.44849 | 2025-10-04 04:17:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 768e54c3-f30b-3822-ad06-8045673e62b7 | -21.55522 | -45.27414 | 2025-10-04 04:17:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a0a0c3d2-d190-3b6a-8619-862909078a62 | -21.19531 | -45.14892 | 2025-10-04 04:17:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| ff3b6e8a-43ea-3cdc-8acc-a60fa6cf0b12 | -17.08632 | -46.24568 | 2025-10-04 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b85ee66-b51f-3825-b58d-0435b17a7e20 | -20.71957 | -49.61069 | 2025-10-04 04:17:00 | NOAA-20 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81bb5533-5922-3c09-ac24-5fc0a088155f | -15.70193 | -46.27452 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2712895-8f25-383d-86cb-4d8bd5d8c33a | -19.5991 | -43.81072 | 2025-10-04 04:17:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a54de1b0-27a7-3917-94a7-84042ed59d96 | -15.58872 | -46.94402 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 450b8664-fa01-3949-be04-aee3e6891855 | -21.25679 | -45.1859 | 2025-10-04 04:17:00 | NOAA-20 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8d8215a5-aa92-34aa-8cab-388afad90f2a | -17.57876 | -44.49215 | 2025-10-04 04:17:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87f92a3e-3e98-3b27-833b-47564a1f46aa | -16.02475 | -50.84848 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ed4a463-a579-3e8b-9fee-a3f7109d62c6 | -15.7293 | -46.27546 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3cdcd04-d52c-35a1-b2dd-5395535036b4 | -15.72475 | -46.28237 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1042e4ec-5cec-3f4f-a6ec-c4a7942ffd6f | -20.47489 | -44.82128 | 2025-10-04 04:17:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4feb725e-b8f2-3c7b-89ce-cdb819605fc5 | -16.04495 | -50.93528 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README95.md)
