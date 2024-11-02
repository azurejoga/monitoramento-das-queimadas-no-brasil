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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77ab5fd6-c206-3671-bba7-e6f8c9652008 | -4.34694 | -48.60413 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d3b1066f-38fa-3d17-84a4-8fc883674de9 | -4.34628 | -48.60807 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 357fb8bb-7d15-3dd4-8efd-14bed953d572 | -4.342 | -48.60738 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 445bd210-c610-321c-9e43-d2cd82bb1e70 | -4.33666 | -48.59626 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22af824d-0297-3c5c-8e5c-2d698f60761d | -4.33616 | -48.58985 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9905fc08-1b6b-3278-b3bb-9a7a55e8f1c4 | -4.3355 | -48.5938 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ac74aa8b-cecc-389b-b369-5af574b23415 | -4.33302 | -48.59159 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3903f648-49f7-313c-a419-120ec62acd80 | -4.33189 | -48.58915 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 82459d57-9bca-37f2-ad99-bb3b92fdf7b9 | -4.32938 | -48.58689 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3eec6046-9b20-388d-a4ff-2c68a1e0426a | -4.32874 | -48.59089 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14bdd8cb-6dd6-3101-a311-0123b430137e | -4.32665 | -48.64625 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4c7fca54-a887-3866-8aa7-746012c73216 | -4.3252 | -48.64017 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fb60e7c-23a1-32c5-be79-130e767e97e1 | -4.3239 | -48.64822 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1672a6bd-fa09-3b41-9495-d3644c1c0016 | -4.32235 | -48.64563 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d3b4a5e7-5e02-3122-9396-a1bacf6b5ecd | -4.32166 | -48.6497 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9b3b7fdc-b624-3b00-aa2d-2353a1649698 | -4.32025 | -48.64353 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1db90ddd-f6b1-3cfe-b6aa-f574048caf59 | -4.31804 | -48.645 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a3996047-c56d-31fb-9632-c18c96f2f424 | -4.31529 | -48.64696 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2b88cb38-2448-3cdf-b4ba-d42cce9aa1ca | -4.30078 | -48.62775 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c624cc0-51c9-385e-bef8-d5c63a9956dc | -4.29286 | -48.6223 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61397d3d-0d7f-322b-b1fa-8e1506e31fef | -4.2922 | -48.62637 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b357035f-2ec1-38d1-9e8c-2008bfa52b3e | -4.23552 | -48.55128 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e217d1b9-ecab-337d-af1b-a905371fc731 | -4.23539 | -48.04958 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b24ae8b6-f349-38e6-9cb4-de92d1acce6d | -4.23511 | -48.54652 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f8472d4-584d-3beb-9995-dab3a531b56b | -4.23478 | -48.05326 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c5396cb-1b04-304f-a436-a6269401230b | -4.23416 | -48.05702 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34055c53-7c20-3a2f-8d6d-78b97d846fc2 | -4.23306 | -48.03804 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc0f3e51-5ca0-3cfc-ae96-dfcc5ea248ea | -4.23062 | -48.55447 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a4d2fba-2555-3a17-b92b-28bceb3e5c25 | -4.22952 | -48.55363 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6429b8b4-75f9-3506-b999-0f375204e83f | -4.22952 | -48.03386 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e38e889b-73a4-38ee-a4c3-26321cbc205d | -4.22504 | -48.56193 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac426845-1a01-3f3e-b19f-9f3a0da7f1cf | -4.22456 | -48.55702 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed6c6fad-09a4-3ed2-9a34-3aa05f5a23bd | -4.12008 | -48.27367 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fec74ea8-8374-3ed0-bb2a-f08df6079210 | -4.10266 | -48.51395 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9e8c438-4501-3818-ac4f-2c757197fba6 | -4.102 | -48.51803 | 2024-11-02 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bf2f8d9-09b4-3906-a86a-b415591cf669 | -4.08717 | -48.31617 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67de9be8-a48c-37f6-9d1e-7fa0081879d7 | -4.08652 | -48.3201 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c7dbb4c-e29b-3907-bbeb-f6e439a60e11 | -4.08299 | -48.31532 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e7e63df-fd6b-39c1-8094-d991b4bed550 | -4.08234 | -48.31923 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76886696-e624-3fd7-bcb7-fc49d6b067b6 | -4.07618 | -48.27828 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b135f6ba-e14d-3555-abd7-fba8c5c94ef2 | -4.07163 | -48.30553 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22fa4fea-ea7b-3afc-b3f1-c3652b73a8e6 | -4.06741 | -48.30492 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1c6f49a-0cb4-31f4-a471-5e57699f7e2b | -3.95144 | -48.13652 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1540d646-a4e5-31fb-9715-366d13af3ea7 | -3.94565 | -48.35805 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| e97f864b-e291-386e-871c-b251a5d693c0 | -3.94297 | -48.35055 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a24b334c-ebb6-3e09-9cf3-82c547a1a8ae | -3.94275 | -48.34942 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dc23355a-b784-3e95-a8be-07c416d68b57 | -3.94233 | -48.3545 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 41e2af2d-0137-3f56-ada5-70aa6c0c1b30 | -3.94209 | -48.35334 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 457c209a-2593-3344-b070-865475004450 | -3.94142 | -48.35733 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| aa8c5888-5f33-397b-b5c5-6200401af2a6 | -3.94105 | -48.36254 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48ee7690-e94a-3735-8206-4c91537c54db | -3.93852 | -48.34868 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 325c9d2c-f48a-3268-84aa-9133e23e75bb | -3.93811 | -48.35375 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a6b06df8-2558-35b7-8396-1b5f7184f5fb | -3.93652 | -48.36065 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51b7b48e-7c40-368b-959e-d48a1ece9964 | -3.93323 | -48.35704 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e0ab381-b2bd-38b1-8aa4-2bc9a3675d2e | -3.929 | -48.35632 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 013bc05a-055b-3401-954d-73727f94a370 | -3.91757 | -48.34633 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49892678-f70d-3545-be9e-2972e81d85d3 | -3.90035 | -48.37206 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8434b005-a804-32ba-801b-3366bc71487d | -3.89187 | -48.37066 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbf5884b-6e6f-3702-92c9-7063b20b64d6 | -4.94319 | -48.56762 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ed7e024-9c6f-3b8e-aa2c-2551de9a0c9e | -4.93996 | -48.53463 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 001d4d90-bbaf-303d-9414-b93c8f0fc230 | -4.93415 | -48.51743 | 2024-11-02 04:12:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7155c01-1f9c-3166-a035-71d574109106 | -4.92996 | -48.51661 | 2024-11-02 04:12:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d341fe84-7971-3592-abe7-101bb8b67149 | -4.9236 | -48.63346 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9b432e10-ecaf-3828-97fc-36e978919389 | -4.92295 | -48.63739 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e79c4f3-c44e-397a-ae47-805b58eb161d | -4.92001 | -48.62878 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b755a51b-9539-39a7-bc7f-adc76d39ba48 | -4.9187 | -48.63666 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| baa0aae1-67e9-3b91-aef0-e1b2634dc1cf | -4.91577 | -48.62804 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 851e7c91-5096-3a2b-aee7-76b679e1d9a4 | -4.91511 | -48.63199 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e423eb5e-d8fd-36ab-b03f-ad97cead3d8b | -4.9136 | -48.56271 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4088148c-26a9-3749-897a-e66c2e986cb5 | -4.91245 | -48.64801 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea503136-806a-39a8-bca3-581ddeebc3be | -4.90888 | -48.64323 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1dde73fd-2e9c-3cdd-886c-ce706be02b47 | -4.90714 | -48.54942 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b98e6c5-ff3b-35ac-a850-c61c1f066284 | -4.90586 | -48.76711 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1db0a094-1648-33af-a5b8-856d66c2a969 | -4.90542 | -48.58559 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3d02d45-3281-384f-b032-17c634c36a5e | -4.90476 | -48.58952 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b2ef906-92f5-39f3-923c-52033c5e2abf | -4.90382 | -48.07074 | 2024-11-02 04:12:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a48ee9f8-b5cd-3ef6-a7ea-f29657376f80 | -4.90186 | -48.58089 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3617ef00-02b0-3c7c-893e-ac1957d20631 | -4.90036 | -48.06623 | 2024-11-02 04:12:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 644ed1e0-7712-3cf2-82b4-9a83248d0abb | -4.89972 | -48.07011 | 2024-11-02 04:12:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c886830-6267-352b-942d-ac27798f2934 | -4.89764 | -48.58008 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 307724a7-5838-314f-953b-49d63d0f6221 | -4.89342 | -48.57932 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48381f79-0a80-3445-8284-ea2d005bf99b | -4.88984 | -48.57472 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d28a28d0-4a45-3fe1-a362-bee6596078ee | -4.88698 | -48.64352 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dcc2c05-da95-3d08-ab0b-beebc66be93c | -4.88631 | -48.64748 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e983dba-8938-3e5c-995f-2e25ab1818c6 | -4.88564 | -48.65149 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 040549a8-253b-36e6-91f8-f7d5af2f17f2 | -4.88382 | -48.4263 | 2024-11-02 04:12:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 249c2ac6-3479-3ca5-8a4c-2c864d1b0df4 | -4.87964 | -48.42553 | 2024-11-02 04:12:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d64792e1-2609-32f6-906d-9915eccf1516 | -4.87948 | -48.58656 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5aa27794-47b6-396d-8467-d003ed3bb778 | -4.8794 | -48.58502 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e0d394d-bda1-3f65-b812-44929fd9101b | -4.87884 | -48.59054 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f63db09f-0ec6-39f6-a964-4cf4299bbf8e | -4.87873 | -48.58895 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7a61613b-8986-346c-b880-866e0d045c95 | -4.87782 | -48.56864 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f717b0a6-792c-38dd-9e25-7165dbd7c517 | -4.87778 | -48.57016 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a397d569-6929-3d85-b4c0-6098997f7b3d | -4.87715 | -48.57257 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8eff2df3-41d5-3707-aae7-ef9391375a3d | -4.87714 | -48.5741 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0276f1ed-b515-37cc-b6ce-9431582c849e | -4.87361 | -48.56785 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02f5af56-40fd-3210-ab40-014237bea746 | -4.87356 | -48.56936 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 518e9c75-c3dc-36d0-9db4-03cf8a8cac14 | -4.87294 | -48.57178 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 590c2003-b818-3c2d-906a-e5a109954915 | -4.87292 | -48.57332 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 000ba97b-8ab5-3ef9-8a5d-3be3fff36984 | -4.86871 | -48.57248 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README45.md)
