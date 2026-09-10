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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8de041f-f0b9-39a5-a2c4-682392955f00 | -7.54139 | -38.43827 | 2026-09-10 03:30:00 | NOAA-21 | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7dd7222f-60d9-3477-9059-7788de915099 | -5.7677 | -45.07481 | 2026-09-10 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| a3947108-63fa-3e9c-a5ab-b1d4a754d87b | -7.50659 | -45.2651 | 2026-09-10 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2cc04c9b-1cdd-3eea-b880-4b5433592421 | -7.11891 | -42.11832 | 2026-09-10 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 377e4605-0342-3dd9-a8c8-94fa6ef17aa3 | -6.82455 | -43.0435 | 2026-09-10 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebc7f208-988d-337c-ac92-098e3d15ec48 | -7.99341 | -43.96034 | 2026-09-10 03:30:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6522acff-5217-3988-ba03-827a14daa479 | -7.12042 | -42.14136 | 2026-09-10 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6f520867-78ce-3ada-b4b0-ec8d95209d84 | -5.76427 | -45.09349 | 2026-09-10 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| f55a071c-6382-3a9b-b359-7c7ffa80cbfb | -7.25773 | -45.35502 | 2026-09-10 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e5dfdb08-6516-3ad8-a8e2-ac7a1f06c051 | -7.11352 | -42.1478 | 2026-09-10 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6f6d376a-6c14-35c3-8c41-ec5f31b21328 | -5.609 | -44.84858 | 2026-09-10 03:30:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f283dbaf-fa6d-3a9a-9881-707372a7c438 | -7.50855 | -45.27375 | 2026-09-10 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 491af847-0d36-3942-8356-d42d7658e84e | -7.50544 | -45.27134 | 2026-09-10 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0714ad09-1e85-3f97-8652-83080b9c7b1f | -7.49103 | -45.27454 | 2026-09-10 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea3fa1a0-e810-3613-9704-45c85d727476 | -4.17278 | -42.43466 | 2026-09-10 03:30:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5b0a3692-6c02-3b4c-ad62-679429205257 | -6.16956 | -44.63436 | 2026-09-10 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 7ba65779-3ad0-30b1-9381-1d36d7265795 | -7.5398 | -38.43817 | 2026-09-10 03:30:00 | NOAA-21 | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 54595331-66c9-3243-8954-3a931be0705f | -7.26136 | -45.35821 | 2026-09-10 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2dfbd022-eef9-32b8-bb23-ec6174ada713 | -6.42411 | -43.06708 | 2026-09-10 03:30:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9a896fe7-4b62-39ac-a60d-d6ebb3ad75ef | -6.90674 | -39.55309 | 2026-09-10 03:30:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5188bc37-f821-3878-be42-ef8515bbc6d6 | -7.46887 | -46.14331 | 2026-09-10 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f4194c70-ed56-32be-9e4b-3e0cb25f4b45 | -7.05011 | -42.71982 | 2026-09-10 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3c4380bf-f564-3356-aa83-8ca5b6673d86 | -7.04941 | -42.72368 | 2026-09-10 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9794cf00-80f7-3404-a22f-244d9cf0a777 | -6.10075 | -44.13615 | 2026-09-10 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dcd9440e-5795-33cc-9ae8-1b84f0844079 | -6.09845 | -44.13914 | 2026-09-10 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4c37f813-cce9-3702-8ac5-af9d33168490 | -5.76545 | -45.08706 | 2026-09-10 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 48b00931-7d1a-300c-b410-822fbaa4ef37 | -6.7644 | -44.56996 | 2026-09-10 03:30:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b5110360-bf51-3746-9727-bdea06e8d787 | -5.55491 | -43.43152 | 2026-09-10 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 29b5fbcd-29b8-338e-bd02-b9e9a89540d1 | -7.46348 | -46.14567 | 2026-09-10 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b787322d-1e7a-3e11-a665-9de9d8778098 | -7.11256 | -42.12474 | 2026-09-10 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 28db0296-e80b-3fad-9bcb-3eb1fc2ad10b | -7.98465 | -43.97317 | 2026-09-10 03:30:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3e34297-0408-30a7-b826-c42924877696 | -5.77111 | -45.09442 | 2026-09-10 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 86f21f2f-043a-3124-b899-f12fd9a84fdb | -7.1142 | -42.14408 | 2026-09-10 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e9348b9a-076f-3a23-93b2-f71c25075c48 | -6.43009 | -43.06794 | 2026-09-10 03:30:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4d24761b-dbac-3548-9be8-24c9b5153d20 | -7.11271 | -42.12101 | 2026-09-10 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5bc5a3ed-13c8-3bf9-bf32-9d70b32975f1 | -7.10638 | -42.12745 | 2026-09-10 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 157aeb37-cee2-3ebf-b5a5-84c4197e3f76 | -6.17755 | -43.01816 | 2026-09-10 03:30:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6925312f-589a-35ef-95cc-a95e11c97cae | -7.26449 | -45.35608 | 2026-09-10 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c61d88f9-243f-3497-8b88-99c3c1f3c6f1 | -7.03941 | -41.54834 | 2026-09-10 03:30:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 630e656d-2d0a-3cb0-8671-4f02572eea3f | -7.98078 | -43.99493 | 2026-09-10 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a432688b-061c-3bf2-a866-2cf9663ab9fa | -6.76281 | -44.5773 | 2026-09-10 03:30:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 624fbc2b-6c10-37ea-b103-3368b1e73a15 | -7.4844 | -45.27303 | 2026-09-10 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| edb7bd6b-6955-3d52-8ec0-45e1867d193c | -5.60794 | -44.85446 | 2026-09-10 03:30:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c4bc7e17-2241-380c-b313-cb864af629ef | -5.76658 | -45.08092 | 2026-09-10 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 84067a69-a0f8-3da1-a569-568af294d86c | -7.48756 | -45.27509 | 2026-09-10 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2e435582-f462-3479-bd44-90de04940ef8 | -6.76332 | -44.57565 | 2026-09-10 03:30:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c1474af1-1f56-32d7-8caa-75968561b957 | -6.42682 | -43.06723 | 2026-09-10 03:30:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 833e150c-68a8-3db5-b62f-265b8b11e407 | -7.97728 | -43.97932 | 2026-09-10 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ebb5c04b-a261-320b-9a19-8e359af82abe | -6.09979 | -44.14134 | 2026-09-10 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fa7e708a-5661-32e1-ad1f-daf711cb4d0c | -8.46431 | -41.25394 | 2026-09-10 03:30:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fafdf5e0-491a-37f4-8ee9-9e51259d5ef8 | -7.98016 | -43.99694 | 2026-09-10 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c9dc40ce-3e21-3d36-9e3e-dbb1fe73c24a | -8.36029 | -41.26094 | 2026-09-10 03:30:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a7dcb2fb-df78-3e0c-b137-76fbc77a0d4a | -6.82379 | -43.04779 | 2026-09-10 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1ed9a53-d13b-3c5d-94ce-435d7ddf8e9c | -7.97641 | -43.98411 | 2026-09-10 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c6e5a6f1-cae0-3b1c-ab0e-9f8440ccf9d6 | -6.4261 | -43.07135 | 2026-09-10 03:30:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 07f174d7-63d6-307d-adfc-6f7923d1de2c | -6.16744 | -44.64593 | 2026-09-10 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a2e42da0-b9c2-31e6-b15f-0965f4a9cfc2 | -7.97991 | -43.99973 | 2026-09-10 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2e1022d2-65ca-3a60-91c1-bc8e2fe30664 | -8.46377 | -41.25703 | 2026-09-10 03:30:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4f29fe72-a2da-3243-9122-88e62c0cc62f | -5.75858 | -45.08635 | 2026-09-10 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 09a8c067-73a4-352d-a3be-762532935383 | -4.17023 | -42.43675 | 2026-09-10 03:30:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 95bf54b6-d1b5-3e28-9676-67ef9a6c16d2 | -8.1362 | -41.12554 | 2026-09-10 03:30:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c2f39dd8-5d60-399b-b8b3-1d672febc9d8 | -8.46195 | -41.25444 | 2026-09-10 03:30:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 385f24ad-7e2d-3cd0-b7cf-3ee79981a040 | -7.99251 | -43.96507 | 2026-09-10 03:30:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fbdbaf47-f3a2-392c-8fae-8db3ee0eb0d6 | -7.48985 | -45.28086 | 2026-09-10 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5566751a-8e09-3b43-aa16-c272eb297230 | -7.97585 | -43.98617 | 2026-09-10 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 10c61b8c-b80c-3a70-a001-bf28f99d3d79 | -6.17146 | -43.01789 | 2026-09-10 03:30:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1f2ebeb4-219d-39bb-92ee-12eec3d3f35a | -7.10583 | -42.12739 | 2026-09-10 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 87f159c1-ce27-3491-962a-5abef3c70351 | -4.16685 | -42.43371 | 2026-09-10 03:30:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0a2b65f2-9b93-3eae-a1b4-6a8ddf316b0a | -7.98423 | -43.97596 | 2026-09-10 03:30:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8bca35e6-338d-3ba4-9269-e83b0fdfaeec | -7.1132 | -42.12106 | 2026-09-10 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3dcddd60-9b50-32c1-afe7-303e0c792499 | -6.09202 | -44.13825 | 2026-09-10 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 073adb17-42d8-3059-8960-283c57434916 | -6.76384 | -44.57165 | 2026-09-10 03:30:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5b5aacb3-7446-316d-86a5-0d28e9fcc744 | -5.68714 | -43.39777 | 2026-09-10 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d9e4f6d-de25-32f7-b0d1-c87091dffe1f | -8.25172 | -42.8945 | 2026-09-10 03:30:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 83632df6-cf26-3eab-9f37-38f9e8e40c8e | -5.75972 | -45.08014 | 2026-09-10 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 93c7c41e-ae93-3885-912d-c52d6febcf34 | -4.17098 | -42.43244 | 2026-09-10 03:30:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2514ed76-237d-37d6-a19a-391408205ba6 | -7.50976 | -45.26749 | 2026-09-10 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 473fa45a-867e-3ae6-b975-5f825302a23f | -5.6622 | -44.29628 | 2026-09-10 03:30:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 10b82f18-bfdd-39ac-a290-af26e54e7445 | -5.77229 | -45.08796 | 2026-09-10 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 5dedc2d9-5b6a-3361-86cc-2faf5fe474e1 | -7.46473 | -46.13899 | 2026-09-10 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 712987c3-da88-3178-b2a5-04629ae1372c | -7.15165 | -39.4143 | 2026-09-10 03:30:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b8321cb3-9cf9-3cc3-b033-d0e52dd9d5b1 | -7.12104 | -42.1415 | 2026-09-10 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 094f5b8d-4aa0-3e7a-9a20-7ea50f209732 | -7.26251 | -45.35205 | 2026-09-10 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1633605e-091a-3ddf-994b-c4524b8b5a53 | -6.16089 | -44.64465 | 2026-09-10 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1484b831-2fe0-3811-8904-749daf9ea705 | -5.66127 | -44.30157 | 2026-09-10 03:30:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2bf97192-c4b8-3582-ae87-ed08b03016ac | -5.41443 | -41.84229 | 2026-09-10 03:30:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 380968c1-3da7-308f-b1cf-1a46e782f685 | -5.41508 | -41.83856 | 2026-09-10 03:30:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f3391cfa-63ef-33f2-aadd-f4e092806636 | -7.26567 | -45.34998 | 2026-09-10 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39ef3d34-53ca-38ba-a6ee-3c0b44a7616f | -7.98163 | -43.99025 | 2026-09-10 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4cb1a84f-86e5-3c96-9670-42bc824f1106 | -7.11485 | -42.14422 | 2026-09-10 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5ae7f96f-aa17-3177-acc5-5e7b8e0463f8 | -7.97675 | -43.98138 | 2026-09-10 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f7098320-4ac1-3432-9eb3-ad36af44be83 | -5.41572 | -41.83484 | 2026-09-10 03:30:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 61acb068-eee1-3d95-ad36-25d6ba75b4c9 | -6.09937 | -44.13399 | 2026-09-10 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fdfe02a2-6bbf-385f-9d40-f8ba0151fb0b | -5.66168 | -44.29823 | 2026-09-10 03:30:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d99d8033-d0bf-357a-8706-a4dcc621f546 | -7.15049 | -39.41675 | 2026-09-10 03:30:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 639f050c-b3f6-3efe-8212-609829f902e1 | -8.98172 | -44.97733 | 2026-09-10 03:32:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a3f46493-34b3-32ba-91ad-41e13c4ab69b | -9.24099 | -40.4991 | 2026-09-10 03:32:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 507a4715-653b-3178-8da5-173dfd6e58e7 | -9.78378 | -43.45669 | 2026-09-10 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d868522-891c-3bd4-ab53-a64d44575e4a | -10.76243 | -45.9637 | 2026-09-10 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1b94dff6-8a22-30b5-a548-fff2c2367065 | -10.22883 | -45.20176 | 2026-09-10 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README13.md)
