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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d122416e-e4ad-375f-873f-bbb7c182907b | -16.29923 | -47.16208 | 2025-10-11 05:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79905ee2-8d9f-3b00-9102-a207c576fb60 | -15.20882 | -56.7429 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45760e5e-2709-360d-b7f2-2a6712ce379d | -17.48537 | -43.33176 | 2025-10-11 05:04:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c80c490-909d-3295-aeb9-27e37f348ab9 | -17.89597 | -57.66661 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1f7412d3-1d6e-3455-935c-4ec17060d4dc | -15.60853 | -42.67403 | 2025-10-11 05:04:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1351ccc8-3ed9-3139-b7d3-dc65586a93d2 | -18.07446 | -57.52798 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 35d5258c-060d-316e-9fef-eaf331823fa3 | -15.27702 | -56.90558 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 123c0691-1220-3c34-89ae-69fec06fd785 | -15.20976 | -56.86506 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d52f483c-1797-3aa1-9e4e-bf054b1830ff | -15.207 | -56.86087 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6eb7bee8-b2bf-3b12-990c-2f9bef9ece44 | -14.99883 | -45.58268 | 2025-10-11 05:04:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab32aa66-5162-37af-ac35-5d0a09832c96 | -17.8434 | -57.66095 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c31c21a6-f6fc-309f-aaf7-bca66f89a961 | -17.81608 | -57.65966 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| fcd9226d-ab84-306b-9e0b-98cb06bb86b4 | -15.16818 | -56.72527 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8cb990b6-65a2-3f06-9fbc-1b0bd62bbae7 | -16.19711 | -59.33494 | 2025-10-11 05:04:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4728d12-cb58-3af9-a2ff-9151f6811b78 | -12.09536 | -64.23965 | 2025-10-11 05:04:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce5c289f-4d91-392c-84d7-d06643884b76 | -15.74654 | -48.96756 | 2025-10-11 05:04:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8c84373-43bd-3fb3-8dd7-de1504145f5c | -15.70567 | -46.63395 | 2025-10-11 05:04:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fb68151-5e40-3d51-9f7b-acdfc815b624 | -15.28075 | -56.9249 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80b15876-677c-314b-a5e5-9abb835a3340 | -15.31693 | -46.19043 | 2025-10-11 05:04:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9803af6c-dbc1-3de2-be0b-5f5ebcb2ee7f | -15.1964 | -56.86284 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b8177f9-70a8-3297-8623-af53089ad5a5 | -15.17313 | -56.7372 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da6e568e-e054-355a-9c18-0c8ebf70ad05 | -17.84459 | -57.65356 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 95f50a7b-ea9c-3b09-a400-1fe8310bfd2d | -14.92743 | -46.76011 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57fe7fcb-3765-3909-868a-f3724505af6d | -14.95121 | -46.74495 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b2c2aa92-51ee-366a-babe-4be2c221c4ba | -17.84065 | -57.65665 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bd2483f2-1ec1-39f1-aec1-8b3b5d467bb8 | -17.89143 | -57.67337 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f016d133-3851-3d8d-8a64-26294f0768a1 | -17.48538 | -43.33768 | 2025-10-11 05:04:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6694cc85-899e-3e66-92c3-fbaf975e0953 | -18.037 | -57.54745 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 98d4df87-b4e7-3a06-a34a-b4be123d520b | -18.06676 | -45.01946 | 2025-10-11 05:04:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| df072a7e-30ad-3354-b270-95508684e87c | -15.41063 | -48.03768 | 2025-10-11 05:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bba0b4c2-e3a9-3a9d-b34f-bed900f63d19 | -18.06391 | -45.01867 | 2025-10-11 05:04:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b303f19-b149-3cbf-b9d3-7e2cb483825e | -17.26306 | -46.90302 | 2025-10-11 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e293f673-0441-300c-b0d6-b1ad715a2f51 | -17.83397 | -57.65541 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 16355673-4c6e-3c60-9189-85433c2bda65 | -15.70534 | -48.39875 | 2025-10-11 05:04:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1f570311-8d0f-34ef-9e8d-a8a83917f300 | -15.60148 | -42.67361 | 2025-10-11 05:04:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b9c3779d-aa81-3736-b428-278e306925dd | -15.20215 | -56.74178 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e4ae2bf-4310-3a4b-8209-a0dbfa160d4f | -15.86187 | -56.74163 | 2025-10-11 05:04:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d539b7c5-68b0-3dc2-89cf-7fbfc1df2e34 | -18.04403 | -57.56783 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f926ffa8-ddfe-353b-bda1-f49bcc642661 | -17.26856 | -46.90381 | 2025-10-11 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c1991c8-635a-3334-ba7b-16e6512b92f7 | -17.8255 | -57.66526 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 1b50378d-1fc7-3bf6-9e55-89b82b73fd27 | -17.89812 | -57.67455 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7b96626e-6ad3-31a1-81db-7a6555401192 | -14.94063 | -46.75132 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cd23bca-f7cc-3894-a3c7-44b7e94b4e90 | -15.74536 | -48.96972 | 2025-10-11 05:04:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 919d2778-16e6-3f31-a42e-10a053304275 | -18.07152 | -57.54629 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 787c8475-facd-34c7-9ab8-ebb6d7745306 | -15.21272 | -56.73986 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3630691-3160-32b5-93ea-7456f9d88351 | -14.94506 | -46.75039 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d46a317-4e0f-38cd-9d01-ad134fe23012 | -15.7401 | -48.97344 | 2025-10-11 05:04:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef562090-0e6e-33fa-9d90-a8c920983945 | -14.93939 | -46.75183 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 165a7490-2584-36ab-89c3-fc191bfc9678 | -18.06634 | -45.02409 | 2025-10-11 05:04:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 88123722-0db9-3b94-92fb-6cebb4c942b7 | -17.83278 | -57.66281 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a0239ba3-9553-3fdb-84d6-88cfdff919c5 | -16.31069 | -47.15681 | 2025-10-11 05:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cec921a5-2824-34c4-9e61-cb7a9ce9e86f | -16.0179 | -59.54548 | 2025-10-11 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9f21f058-0682-3465-a299-f2200ee36a27 | -14.99839 | -45.58665 | 2025-10-11 05:04:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c6b9228-b3c9-39ae-b014-00c1116448e0 | -18.81606 | -54.96906 | 2025-10-11 05:04:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6677dd4b-60a1-375f-b7a8-90e57db9d58d | -11.84497 | -63.71259 | 2025-10-11 05:04:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c9f4316-a2c0-3ca0-ba3b-b5197c785ef2 | -15.17865 | -56.74551 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e00e38d4-962f-3b9e-a14d-36bc945e487d | -15.68868 | -46.63589 | 2025-10-11 05:04:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59ef4847-1597-3c33-a011-eb05f29f2132 | -17.26776 | -46.90285 | 2025-10-11 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bcf07804-91eb-3c34-b86c-9682731ecfa2 | -14.93365 | -46.75398 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cb31be5-2950-3799-9b4f-675e5cef672d | -15.19974 | -56.8634 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f5af6db-87e6-3db2-9796-bf2e739d0d59 | -16.30386 | -47.16935 | 2025-10-11 05:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| beff8cfb-ff25-359b-836b-2aca47ca3432 | -15.01657 | -56.07872 | 2025-10-11 05:04:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92e6d26b-89fb-3080-9484-59d5e1595923 | -14.01546 | -47.05812 | 2025-10-11 05:04:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d1d8e8c-2dde-36ad-844b-c008fa869bc9 | -15.19364 | -56.85867 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e0b90de-4fa1-3413-83ee-fe19fb07d94e | -14.98894 | -45.56459 | 2025-10-11 05:04:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e549b783-d53b-3aad-9b2d-cc8a08197d46 | -17.82156 | -57.66836 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 2df1ef59-bee4-3a31-98fc-bb8e7479dbe2 | -14.94462 | -46.75406 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b901c627-bc1c-3138-a490-bd1b74d6baca | -17.82216 | -57.66464 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 8a485422-2fee-3e76-8901-9c7c9afb380b | -15.15598 | -56.823 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b22e3a4f-5660-3b6c-afaf-7cf00982925d | -17.89871 | -57.67088 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 333f06f7-3f49-30d3-b4d3-d58c6434a411 | -14.74381 | -46.1321 | 2025-10-11 05:04:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98ffc3b1-3ff0-319a-9936-808c3c7471aa | -17.84006 | -57.66034 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 57cc258b-38df-3632-93c3-8d9c22fd9eb4 | -17.88349 | -57.51006 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 43a5acc6-0347-3e63-ac10-726f2319e9da | -14.74469 | -46.12431 | 2025-10-11 05:04:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b170308-1d46-3b22-aa55-bb3310f96fd6 | -14.92 | -46.77651 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01c26654-060d-361d-8171-43e4e95dc35b | -15.92685 | -56.48326 | 2025-10-11 05:04:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a1a9324-cd54-30ec-8831-c64a4b22d4fc | -17.92373 | -57.62249 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3b4acbc0-f1b4-3807-bdd9-b76e8e4b943e | -15.32018 | -46.18932 | 2025-10-11 05:04:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| bcaa2c8f-9af0-3c87-8c0d-347c808e2436 | -15.41698 | -48.02731 | 2025-10-11 05:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3f37e49-366f-3afb-8eed-fac3371ca1d6 | -17.82138 | -57.62693 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 539ca3ae-9724-3a71-b35c-df7069e7214c | -15.41132 | -48.03203 | 2025-10-11 05:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ccced57-3d46-3f7b-9be7-c37f8c47205a | -11.84391 | -63.71822 | 2025-10-11 05:04:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f70606d-2114-3e40-a531-460d20000c76 | -17.81882 | -57.664 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 369e4345-e7f1-3f4b-b40d-89dd90b084b7 | -18.07761 | -57.55117 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 22a73250-a8d8-366e-8355-43645f126204 | -14.9455 | -46.74676 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87fbda60-f8a6-39ef-bfdf-594663a6f59b | -13.01393 | -61.43506 | 2025-10-11 05:04:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fd9bfe45-5597-34ab-880f-e0c2efc4e9ec | -14.98952 | -45.56705 | 2025-10-11 05:04:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb400f9b-0aa3-3bbe-8e84-e023cceaabca | -17.26391 | -46.89537 | 2025-10-11 05:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ecf0214a-c00d-35d2-adce-598a9a590e14 | -15.69414 | -46.637 | 2025-10-11 05:04:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fafd05fb-8c99-3aee-af2d-21c8ce20df59 | -15.26916 | -56.91175 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8dad4676-4e04-3223-8a47-80139bc6fd5d | -14.92619 | -46.77056 | 2025-10-11 05:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca1e2d3a-d61e-3d0e-8cb3-9e46d7df36af | -17.48593 | -43.33128 | 2025-10-11 05:04:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6786ffac-7562-3b56-ac05-8f6ebeb427b3 | -16.30957 | -47.16682 | 2025-10-11 05:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20df47b8-f1da-3727-8a58-6056accd98f1 | -15.70518 | -46.63814 | 2025-10-11 05:04:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ed53a95-96bd-3da2-b527-0b9cc226e126 | -15.1903 | -56.85812 | 2025-10-11 05:04:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64c33123-0ac2-3f11-b032-1a9fa6bc0cef | -15.20939 | -56.7393 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bdc838a-5e4c-33e3-a3a8-1e9cefe17acd | -15.22272 | -56.7416 | 2025-10-11 05:04:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4ca6b8b-6a56-35f7-902c-a741a2d8205f | -18.03366 | -57.54686 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 6a7e243c-cc5d-3195-b6e5-250b47114f92 | -17.89202 | -57.66969 | 2025-10-11 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| dd160597-371f-37e0-93c3-b687fac0cd30 | -12.09084 | -64.23556 | 2025-10-11 05:04:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README39.md)
