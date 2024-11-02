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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b13b95e0-af95-37b9-a38b-c07926d5ff62 | -5.19172 | -46.15291 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 157ff667-1a27-3c28-bdb7-6850c72e0015 | -5.19051 | -46.18309 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 047bea9d-ae1b-3c42-923f-6bdd7cf0249f | -5.17407 | -45.70754 | 2024-11-02 04:12:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9edae2ae-e36d-3f5e-a77a-43e2d99ef6f9 | -5.16732 | -46.11585 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19f38464-637f-3508-b832-69b450a531ec | -5.16436 | -46.11108 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de774d7f-ebe3-3bf4-976c-cef99bc01b74 | -5.16369 | -46.11528 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46e2a0a7-9ff0-32a5-8d02-34123053c139 | -5.16073 | -46.11052 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31a55264-6d40-390c-baaf-314dff951def | -5.15214 | -46.11769 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6382b8cc-8656-315a-881d-e1d81b68615e | -5.1365 | -46.07628 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b38d95b-e740-36eb-8e6c-a269a037d53a | -5.12285 | -46.16084 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 14ec9e1f-f990-3b39-900e-5df94401fa5d | -5.11502 | -46.02578 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1c0bcad1-4dbc-3ae2-aa42-6c0e0177031e | -5.11435 | -46.02992 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 60d032ce-dfe2-31b3-9ec8-93e60e408c9c | -5.11223 | -46.11142 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0d808e70-887a-3722-a0c9-b40656b61bc5 | -5.11153 | -46.1157 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97a8ca94-4401-3f59-9a8a-34abe1edfa8c | -5.11074 | -46.02932 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8652776d-7087-3338-8314-2d82494707fe | -5.10712 | -46.02875 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7faf3ad-ff0c-3e9d-9308-7f302c665c06 | -5.09926 | -45.70036 | 2024-11-02 04:12:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 155d2efc-f87d-3cb0-9915-6fa690872196 | -5.09666 | -46.0701 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 532de6eb-912d-32e3-a243-975678d18460 | -5.09597 | -46.07428 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adc09940-b730-3e1a-93ef-ffa37dbef643 | -5.09569 | -45.69988 | 2024-11-02 04:12:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8616a817-c8c3-3681-826d-2ffe9fd5c01d | -5.09304 | -46.06951 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c5e3ab8d-3df0-3ea4-989c-eb3a2e6e8997 | -5.00546 | -46.03056 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef49db67-1d7a-39cb-8c68-09c85566bd45 | -5.00184 | -46.02995 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9cac102-c547-351b-8dbb-38988d321970 | -5.00115 | -46.0342 | 2024-11-02 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 31683215-1cab-32d2-b0db-2746ecea892c | -7.39391 | -45.98684 | 2024-11-02 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6f328cf-15e3-38ad-b957-e5b91cc2bd01 | -7.12414 | -46.37101 | 2024-11-02 04:12:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f879c665-3898-34c7-a7cf-2abe8c605694 | -7.12279 | -46.37921 | 2024-11-02 04:12:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c198898-3b3d-3899-8872-3dfca83d2b26 | -7.12123 | -46.36629 | 2024-11-02 04:12:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9319c75c-9000-30a9-838e-f438e531c933 | -7.12055 | -46.37042 | 2024-11-02 04:12:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 854df745-c26a-3593-8f2c-f074bfa686e8 | -7.1192 | -46.37862 | 2024-11-02 04:12:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84df7e6e-41de-3555-9a70-3c7c643b385b | -7.11764 | -46.14867 | 2024-11-02 04:12:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c431c361-4707-39bb-a65c-f20aee576370 | -7.04709 | -46.31302 | 2024-11-02 04:12:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6774fa7f-67fa-3075-b4fc-3780060acdbb | -3.49718 | -46.30549 | 2024-11-02 04:12:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5081b655-3db6-3f50-b142-0441ada24dc9 | -3.43623 | -46.20831 | 2024-11-02 04:12:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba02e58e-033f-3165-88ef-92a2f8a87959 | -3.39604 | -46.06804 | 2024-11-02 04:12:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dc233e39-951d-371c-a397-707e21d1822a | -3.35752 | -46.04837 | 2024-11-02 04:12:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69021c1f-e77f-3364-a0a7-aba3a69f7046 | -3.30497 | -47.01061 | 2024-11-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a35a626-5d15-3d1d-bef2-d700937d7eab | -3.30415 | -47.01556 | 2024-11-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8b3b70f-ff72-38eb-9d0b-69bc9a1f8797 | -3.30105 | -47.00998 | 2024-11-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88f7c552-7253-3c0d-8f8b-cd433cfdf65d | -3.2698 | -46.24957 | 2024-11-02 04:12:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68514c7d-6b3a-3b51-bcb4-b5ddb8927e52 | -3.22667 | -46.49545 | 2024-11-02 04:12:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4772f767-31b5-3ad7-a307-0536eda9ac41 | -3.21571 | -46.18117 | 2024-11-02 04:12:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da3c302c-f3ea-3740-b9c2-110635a693c2 | -3.21272 | -46.17611 | 2024-11-02 04:12:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a4e4a0db-0840-35c0-8583-0d20bd88589d | -3.21199 | -46.18056 | 2024-11-02 04:12:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 3c4a2269-ff5d-39d8-b6c3-0bb8e0d3406a | -3.211 | -46.17794 | 2024-11-02 04:12:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f0f5c111-c7a9-3bc2-ae8c-6aea6ea33f1e | -3.2103 | -46.18242 | 2024-11-02 04:12:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8013bce3-5b26-3105-9718-853e887ca1db | -3.20959 | -46.18691 | 2024-11-02 04:12:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3da22f7a-44ea-370a-b1ac-96cf397f9cc9 | -3.20818 | -46.19588 | 2024-11-02 04:12:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48ee5b7a-6a70-306b-b539-b64e6d38022d | -3.18344 | -46.5942 | 2024-11-02 04:12:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2a88237a-1ecc-38a7-b78e-260b9ed8a34e | -3.18268 | -46.59892 | 2024-11-02 04:12:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 044b7f70-c5ae-3bd8-a1bd-8f203de930e7 | -3.17962 | -46.59358 | 2024-11-02 04:12:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6ce8db11-8c5d-3e8c-ad51-dc70d3dc2c1c | -3.17886 | -46.5983 | 2024-11-02 04:12:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6709eb7e-16f3-33b8-b055-ecfc02a136bd | -3.1758 | -46.59296 | 2024-11-02 04:12:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bfd14219-1b9d-3abd-8dd6-30ac5422fe5f | -3.17504 | -46.59768 | 2024-11-02 04:12:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 346bb1a4-68d1-309c-8e30-5eb5c8d6113e | -3.12281 | -46.0479 | 2024-11-02 04:12:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b1530da-5cb4-3da8-96dd-0173a7373f83 | -3.05997 | -47.3819 | 2024-11-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13205458-6098-3c8f-85a8-af9bf2b59cae | -3.05939 | -47.38549 | 2024-11-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e14634a-b1b2-30b6-94c2-fb64e9d4700d | -3.03873 | -46.50896 | 2024-11-02 04:12:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6668f47-2722-317e-bd67-5a876ff82d71 | -3.03841 | -46.50608 | 2024-11-02 04:12:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2a88503-6227-39c4-bcc0-22327f144a19 | -3.03764 | -46.51075 | 2024-11-02 04:12:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff7e96e0-c08e-3ad2-a2e8-56416cb5273f | -3.39234 | -46.06744 | 2024-11-02 04:12:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92cba06f-5390-3286-9389-287cedca9246 | -3.35681 | -46.05273 | 2024-11-02 04:12:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f09aa5b0-fd2c-3eab-9004-bb8c8e956235 | -3.35312 | -46.05211 | 2024-11-02 04:12:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c43b989a-bfce-3add-bc77-82c8e0a9c1a2 | -3.99257 | -46.45833 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed86f24c-4b25-3c2a-92d3-be1e09f0aed5 | -3.98884 | -46.45759 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 288be8ed-e2de-363e-bc0c-aa8a9765b28d | -3.98812 | -46.4621 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fc8acab2-748d-3487-9d90-0f21faa77b5a | -3.9631 | -46.37947 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bdac3d06-54f0-3322-8355-477962d91c43 | -3.87831 | -46.4453 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b41e4313-5a9b-37b5-abeb-2e29b2db216f | -3.81378 | -46.48423 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99ddde48-2166-393f-a426-761c8cda6d11 | -3.81225 | -47.47603 | 2024-11-02 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6ea125c7-8b43-3328-8b91-620f2ab53de8 | -3.63483 | -47.3079 | 2024-11-02 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2fc043b1-bf5d-334b-ac98-b67b3b878cb4 | -3.634 | -47.31305 | 2024-11-02 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12ea8826-eb42-3795-94c1-3e1b05d3ac09 | -3.63087 | -47.30722 | 2024-11-02 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bfa18d0c-ba9f-3495-a261-e3c953b8d136 | -3.6269 | -47.30654 | 2024-11-02 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd7e769e-ca5b-38cc-98c9-b822aa80acbb | -3.62606 | -47.31172 | 2024-11-02 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 784e2173-ca87-38fb-abcf-413eb95da864 | -3.62294 | -47.30585 | 2024-11-02 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4aaef831-5e44-31a4-b325-cfd1e37f4aa7 | -3.62209 | -47.31106 | 2024-11-02 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b91d361f-02a3-3f30-996e-3fbe6fd1bfd0 | -3.59349 | -47.31144 | 2024-11-02 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7dd2dd8-b485-3a59-9ef7-1547eb7e0821 | -3.59038 | -47.30553 | 2024-11-02 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 629a14a4-5fb2-3ede-802b-fa04fdd2ca1a | -4.37538 | -46.53944 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa0f711b-c102-3ed8-b58f-eb2c3e124af2 | -4.37164 | -46.53881 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccdf15b6-33a1-356c-80d2-e580d366c566 | -4.30408 | -46.90292 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6618f1fd-c7b1-3ad1-9f78-182d4711a702 | -4.25883 | -46.39054 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2be65a6b-a132-3d55-93f1-b1a81244919d | -4.2577 | -46.38382 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6f92c88-98e1-3e04-ac1a-499a3e4d6f69 | -4.25698 | -46.38821 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b16e8a39-406c-351e-a9bb-b44f1e5bd58e | -4.25625 | -46.39264 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7c6963b6-2fce-3924-80a0-53f97d0da42e | -4.24833 | -46.38451 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d6cb0b8-f017-394a-8f8c-889c062cdfce | -4.22802 | -47.19386 | 2024-11-02 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc6532a8-7bb0-322f-b9d4-ac1a6cb20512 | -4.219 | -47.39374 | 2024-11-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c31685ad-525d-3465-9cda-be527be2b9d5 | -4.19843 | -46.69778 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 786d103b-6e28-3989-bc7f-7afbe884504a | -4.14771 | -46.84352 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| faf1ffa1-4984-3cc8-91ef-4672dd88cf5a | -4.10977 | -46.59833 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44a0b6b4-3c48-36e2-84ee-1674db79a7bd | -4.10536 | -46.60022 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a3f826c-83a9-367c-9185-943e66dac255 | -4.06351 | -46.27717 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13605472-b0b0-3df9-8db3-af0ee41d3f8c | -4.06282 | -46.28154 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 444f924a-d183-3330-8bd5-7c4c3f2d995d | -4.06136 | -46.2793 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| db465f69-cbc2-35fb-a0c3-999bea5b3a9f | -4.05959 | -46.25393 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06ec1201-ec40-3684-96ee-1f0f21cf1c83 | -4.0591 | -46.28098 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c683364-70bd-3b2a-853e-d56a40ff580e | -4.0583 | -46.25176 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58adec54-a3ff-3de7-af69-3e041578ccf2 | -4.05588 | -46.25339 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README41.md)
