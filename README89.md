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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bfd6f37-7f6e-3f42-9feb-f5d5a14b69d1 | -3.45747 | -50.18977 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50093aa8-2d24-3f33-a683-fc9fa2b919fd | -4.09399 | -48.32529 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f063193-8af6-3a88-b3f1-b809c0708b67 | -2.64172 | -51.75092 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3ef5fc2-2269-37b3-9b47-0b6b0125beb0 | -3.23682 | -50.25998 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18d5e6d5-b19a-3158-bf48-477ff473cf4c | -2.38499 | -49.07404 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f613cf6-c986-337c-9412-94fcf8d95066 | -3.98815 | -46.41854 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8365f7be-3a77-3dfd-b9e1-01ba18b477d6 | -2.86365 | -49.39187 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8d17938-f517-3623-93d1-10e819843c06 | -4.1061 | -46.88554 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2353128-6704-36a1-ae27-047c4f0fe94e | -2.87308 | -49.37542 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c8cd6788-a034-374b-821b-85695bed046e | -8.69226 | -47.95621 | 2024-11-10 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 320b1e84-d917-3ced-97d0-26db19bc4972 | -3.22886 | -50.26614 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 776d149b-e083-393f-b59e-129805c016ef | -2.88225 | -49.23029 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae7adb79-45ca-34a4-83cf-39a71504d3c3 | -3.35721 | -50.11888 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c86db78-ea7a-381e-b44c-81d519c14962 | -4.13031 | -46.92685 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c33545f-f15b-3b52-aefe-cc76cbee1782 | -3.44488 | -50.75045 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8de2155-4bd2-3752-a0b0-a34642ef3806 | -3.16677 | -49.09644 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| becc3c7b-b795-30ac-a6ab-494e7351f4b4 | -2.87232 | -49.43608 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6f0bbcac-ab34-336f-b2ad-87dcd710ebc3 | -2.04304 | -52.70648 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1bdbf1ea-54d2-32ea-87ff-84b2389e7e1e | -3.03517 | -51.52872 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a85e6294-f078-3a82-baa3-ae94f029b3dc | -3.26524 | -50.43283 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36537a48-c2ea-38cf-bfdc-0db7cc236186 | -5.32564 | -47.68529 | 2024-11-10 04:38:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b67233f9-3855-3dd4-9613-12bedaf60494 | -2.16005 | -50.72657 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48026478-99f9-3f77-ba82-2e35d76d88a7 | -4.90634 | -45.8608 | 2024-11-10 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8e8ef3ea-194a-316a-9bc2-ebac42109b1a | -2.39643 | -50.31857 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 13aeea42-39f6-33aa-860d-5944b01cb10a | -3.08049 | -50.56438 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d9b08f5-e16b-352a-a8cf-a15a95f36468 | -3.96099 | -48.1766 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8583b387-dccf-3613-a6dc-f51c7f4a7561 | -2.22206 | -50.56051 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8bd7039-1373-3cab-9536-f7fbdb5285ec | -2.76003 | -49.36074 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce31b65a-c3d4-3302-b281-6e99eeae3f8b | -3.57213 | -45.8186 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32b87053-b7bb-3ba9-91f7-1a3177f73f5e | -3.22713 | -50.27708 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 60e96c9f-264a-38c8-805b-6cf8e82c10d9 | -2.15821 | -50.51562 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a7ad068-40af-3afb-b6f3-60cdb0a6d4c3 | -4.27754 | -48.18661 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3274427-b763-3e5f-b6f0-861a2d917219 | -3.98198 | -48.15138 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f810d8e-d5d7-3e35-9dba-4b8174bc7de7 | -3.67428 | -54.04064 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 623cca33-eac4-3e99-94ed-2ed695c6765b | -3.59409 | -47.3488 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84e5f9c4-dce2-356d-b6e0-9516629d859f | -3.30331 | -50.08121 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80005f1f-482f-3894-82e5-a2e4dac3860e | -4.69401 | -49.62537 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fba19de-a918-3443-bc3b-a780de8a6ff9 | -2.37258 | -49.82664 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbaab237-78b3-3eba-a720-70c57557e485 | -3.0827 | -49.562 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdb2fa1f-4556-3d65-9f9b-0bf2e2a9961f | -2.67404 | -48.65847 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0bba79fe-95d8-3fe7-b477-1cf61e5883ba | -3.62253 | -55.51703 | 2024-11-10 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52f8f727-7a05-3a1a-b67c-d5f80e90e77b | -4.12395 | -43.59027 | 2024-11-10 04:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d5a4ee1c-72a4-3b59-aaaa-434474881bca | -3.8332 | -48.90386 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9cbc53e-45b7-3016-92df-0a1ff05a0fd9 | -2.72126 | -51.99837 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 73f1d8db-c0e7-360e-a4be-6519c9ccabea | -8.37779 | -44.12491 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 681c3220-fbd9-3120-aab1-52e5725ac398 | -4.38017 | -47.23129 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0498aa00-ee0e-3d34-b501-a7b646a4e31b | -2.23404 | -50.69386 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 236657b7-7246-3830-94cd-a952cad19b22 | -2.71029 | -49.17785 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd02242a-bebe-3899-a329-9dbd768382e7 | -2.62431 | -51.29829 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a30cd0e1-9655-355c-ab4c-8078ecd23840 | -2.65114 | -49.89865 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4c11e21-7d89-3cd1-8ecb-5bd52c71dce1 | -3.12449 | -50.44199 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 49664af8-3831-3ae8-8161-c4d753f27588 | -2.07026 | -51.40422 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62d9d6f8-50ec-3f79-8e1f-48ab8696a7d9 | -2.59023 | -48.20418 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d42cf049-177d-398f-93bf-6b9965e2dc7e | -3.56544 | -53.9446 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f573c3ac-a4ba-3879-b459-f37c0aa71185 | -6.73736 | -46.38486 | 2024-11-10 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 982f623b-75af-3356-81a9-40df9bb9ed2f | -3.89185 | -51.2018 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed812387-8dda-3d1f-9305-afeefe10e67b | -2.15629 | -53.65135 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f542ffbd-b6c6-31bd-9a06-b5b619668f73 | -3.36481 | -51.84726 | 2024-11-10 04:38:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a783ba01-802e-31d2-a167-46d8c3bf9b41 | -3.10107 | -49.42484 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1d098963-4456-340a-8afb-39672fab7287 | -2.80523 | -49.85683 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62c71c2e-6361-3aa6-bb2c-36348f1fdd74 | -3.51466 | -44.03337 | 2024-11-10 04:38:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 4d5e63b2-3bd4-3ba4-8cbb-d7f762bcea51 | -2.86773 | -50.31912 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b24cbb94-bcc0-3021-a23f-ad80b70e73d3 | -2.31034 | -50.66284 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8971a6c0-357f-3cb8-a45f-d963b2b5af05 | -3.23567 | -50.26723 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa6fdbbc-82c2-3a90-a9b5-2579f5d1644b | -1.48409 | -55.4441 | 2024-11-10 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a2b9c5b3-30ee-3c65-b1d2-c22d5bd3c8f1 | -3.11062 | -50.15494 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5388154-6c09-32bd-90e9-03ad64360092 | -4.12341 | -43.59394 | 2024-11-10 04:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 39d20a8f-f5b7-385d-9ed4-fc286be0ae8e | -3.6719 | -54.65852 | 2024-11-10 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1dec4fad-917c-3766-b85f-b4a2ea7205c6 | -1.52054 | -54.99382 | 2024-11-10 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 062a9cbf-8c68-3300-8de4-4d2c372db329 | -3.24859 | -46.49367 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1acd507c-c55a-3a2c-a6fa-9f3cae1febd7 | -4.24028 | -48.0162 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28882d8e-c4d2-3301-85cb-8027444851d0 | -3.25334 | -48.74185 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd13c445-e068-34cf-af1b-ab77cc5ce874 | -5.11437 | -49.92132 | 2024-11-10 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72aac709-44aa-355d-b9c1-9b122bef48a8 | -3.035 | -48.04336 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d28cead2-8af8-36a2-bfed-6c7cad23c286 | -2.68148 | -49.27329 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27bb0e21-3271-3676-9db9-2cf4c9a6100a | -6.73002 | -40.81188 | 2024-11-10 04:38:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3909dd65-bbe0-3dd8-8432-092d280dc424 | -7.43769 | -39.76275 | 2024-11-10 04:38:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 404da5e0-a55b-3cba-aaef-7292f804080e | -3.35311 | -54.12846 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87379e62-fc0c-3f76-aa61-5e555ae1e00d | -2.83846 | -54.00053 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 920647bd-fec4-3513-80fe-25452e6ca5ae | -3.78345 | -47.7408 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32ccbc43-770a-3671-b5eb-9a14d6f26113 | -3.85012 | -46.61692 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 109a6b98-fd13-364e-a439-58cd8b36675b | -2.73675 | -49.86841 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26d26acf-c787-3a7d-8007-465cb4172620 | -3.09394 | -53.31706 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d665fc49-ed92-3dcd-8699-b25be58042ee | -5.47569 | -44.6166 | 2024-11-10 04:38:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4258d829-20d8-33e0-9137-2d490b1dfa5f | -4.68734 | -49.62432 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17e59643-a9f8-3405-9aef-757e7bc61f49 | -3.12733 | -50.44624 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 49213474-2f9c-3bc8-a255-a5cd23a336f3 | -3.22995 | -50.28127 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 36374605-9d80-33ce-b36c-49da6209cd3d | -2.71083 | -51.34387 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7aa802bd-b894-3ce5-97f7-3a56455bcc19 | -2.68777 | -49.86399 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a3150f47-ccf4-3698-97f3-c5f69e15547e | -3.0485 | -49.52831 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e0a1b41a-0455-3933-b612-bd69a9cbf652 | -3.20204 | -50.30307 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ea8c9c0-3449-35a1-9684-ffd56e840763 | -3.11097 | -48.61397 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0e4589b-44ac-33ec-8d54-cdc5208e27f8 | -3.31045 | -50.08569 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fdc05a7-8a74-35b9-88b2-c549038f0770 | -4.38078 | -45.85878 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 353a8859-5b45-3239-9589-77d6848513b5 | -3.89761 | -50.29913 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a58c604-f17a-3504-b169-aacae84426da | -4.60458 | -47.98325 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae9e1b09-c6b8-3598-b550-881308e59046 | -3.11124 | -45.29782 | 2024-11-10 04:38:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 379e29e8-b261-37fc-bb2c-70c6ea70dc10 | -2.80599 | -46.64918 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ad8bcfd-da01-3f8e-827d-5ea9c04fb05c | -2.57565 | -50.67992 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42adcf64-6d5c-34ae-be30-61aea607db48 | -3.5908 | -49.90266 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README90.md)
