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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28452437-f487-34a4-b29c-8ab74b75d79f | -1.7499 | -54.9516 | 2026-09-20 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 9c15f2e1-f9e6-36ca-9e7e-86a2d58a30d8 | -7.5704 | -57.6766 | 2026-09-20 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 163.7 |
| 65e53cc8-1332-356e-930e-5c51fbf345a9 | -11.4714 | -47.776 | 2026-09-20 15:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 9fc1844c-98c2-30d6-96df-c74549347fc5 | -10.2598 | -50.2624 | 2026-09-20 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 8d7c5182-b727-37ed-be8b-703ac790a421 | -9.2567 | -46.2098 | 2026-09-20 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| af6a4319-61e2-3ba9-b0e8-1b6fc47108af | -10.9692 | -57.208 | 2026-09-20 15:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| fe944bd9-c90e-32ec-9e4b-6fef075e853c | -5.9795 | -52.2046 | 2026-09-20 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 312.8 |
| a7e81028-451d-3427-8c08-da1587414ce1 | -9.6665 | -54.3332 | 2026-09-20 15:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| e66dccf2-09c5-3e58-848a-711e296712cf | -5.8088 | -55.7095 | 2026-09-20 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 80a6e8a2-cff7-3739-a431-cce9a8e72d8a | -8.0892 | -55.3511 | 2026-09-20 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| aac7394d-6c98-3196-b22d-15251ca147bd | -7.3259 | -55.6153 | 2026-09-20 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 154.9 |
| e82c4b51-f895-3bb5-8447-c75cc80df6a1 | -10.8364 | -50.9479 | 2026-09-20 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 270.1 |
| d1397936-e916-3f8d-99fe-7c41cb7c92e9 | -11.3612 | -51.3374 | 2026-09-20 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 161.1 |
| 647ade7c-5fe7-3467-b19e-9c7a69d80810 | -11.041 | -54.1567 | 2026-09-20 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 196.6 |
| 3af57c3c-7299-3d03-b2d1-d3e321de6e0e | -6.7666 | -59.1129 | 2026-09-20 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 155.8 |
| 4f50c22f-3dfa-3bdd-a970-2da5d24e7803 | -11.0065 | -48.3187 | 2026-09-20 15:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| fcbb5e7b-4b01-3413-b58b-fda9c6da41f3 | -7.3073 | -55.6163 | 2026-09-20 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 3e056df5-6e0f-309c-8c3a-731ae46bd847 | -10.8177 | -50.9286 | 2026-09-20 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 50446cbb-85b6-3fc9-b636-3aa50a36371c | -6.3471 | -58.2973 | 2026-09-20 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| c23a6960-a385-3028-9735-babbac51c53a | -7.0619 | -47.4826 | 2026-09-20 15:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 88f87c63-1115-3b9f-b920-c2ada01e58f3 | -6.4941 | -58.3884 | 2026-09-20 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| a76dfd32-2209-31ea-99ca-65f724c0e618 | -10.2787 | -50.2605 | 2026-09-20 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 3945d111-be86-37dc-8cd5-b7f766822ccc | -9.7148 | -47.2536 | 2026-09-20 15:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 49d060a5-b6c3-3408-8a8e-7bac7e1b1bf8 | -3.7347 | -59.4002 | 2026-09-20 15:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| fc9c8f98-d835-367f-8f71-aebe3007b4ae | -6.3656 | -58.2966 | 2026-09-20 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 70915db9-aac2-3d40-8c98-65c9c60e82b7 | -9.8313 | -48.4073 | 2026-09-20 15:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 226.4 |
| 9eaddc61-b09a-3641-b2aa-58d9eebd6167 | -7.0286 | -45.2554 | 2026-09-20 15:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 4fe8b2da-59de-32d6-9e25-06243bb6eaa9 | -6.0927 | -57.6457 | 2026-09-20 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 47aee645-140b-3216-bd47-101dc78ba768 | -3.3311 | -59.8101 | 2026-09-20 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| f434757f-1192-382e-9caf-b71b333cb96b | -9.84 | -46.4136 | 2026-09-20 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.3 |
| b3939f58-4e79-349b-959a-fa4d7f17e0da | -7.1203 | -42.083 | 2026-09-20 15:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 118.4 |
| 08030249-a972-3bf4-a757-738626c6412a | -9.0353 | -48.7704 | 2026-09-20 15:00:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 107.1 |
| cef7f9b8-b2ae-363a-9784-3509259a1985 | -9.8136 | -48.3218 | 2026-09-20 15:00:00 | GOES-19 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 0bada17a-3a66-3a1f-b115-a78726410990 | -7.3724 | -44.7233 | 2026-09-20 15:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 8a02b58c-eb4d-3132-8d5b-aea7df001c00 | -11.6624 | -50.1954 | 2026-09-20 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| bfa7f783-2b38-3039-825d-52a9f0516435 | -11.0407 | -54.1772 | 2026-09-20 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 144.4 |
| c5fceeb5-2bc6-31b5-8cad-4cf7a5b070e5 | -12.0263 | -50.0447 | 2026-09-20 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 837387b0-8697-3cc1-8040-7b29817fb462 | -9.6668 | -54.3129 | 2026-09-20 15:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| c7fcea14-111f-3226-b921-6c9a573f06de | -10.8854 | -56.2362 | 2026-09-20 15:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 377db68c-ce2b-3f05-9d40-ad848d869144 | -6.8032 | -59.1693 | 2026-09-20 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 882b1c53-b210-377f-b790-c1c8b4d5d364 | -8.0894 | -55.331 | 2026-09-20 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 6a56b877-aa69-3eee-9a4a-97d7bb01f17b | -11.9112 | -50.1016 | 2026-09-20 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 053670c2-b627-36c8-a886-36c31b205ce9 | -11.398 | -51.418 | 2026-09-20 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 132.4 |
| ff3ef7b2-6871-3d99-9ad0-dc1e7a322eaa | -3.3821 | -61.2901 | 2026-09-20 15:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 5422d76e-cfad-3050-ad0a-536b02ecccac | -10.0975 | -45.6597 | 2026-09-20 15:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 9827ff3f-e29b-3395-8f3d-3c5f616967ee | -11.9112 | -50.1016 | 2026-09-20 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| a9f77204-fa58-3749-8ecc-567b70aa7eac | -11.1222 | -49.4818 | 2026-09-20 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 9d50887b-53ae-3e46-b8db-c84a5b3a0c09 | -7.0619 | -47.4826 | 2026-09-20 15:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 2de57cd4-3922-3eb5-a1e7-72830a65712b | -10.8759 | -57.1355 | 2026-09-20 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 8482c9bf-aa78-317d-8135-f7d5ff157f21 | -6.8032 | -59.1693 | 2026-09-20 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 95d82137-3edd-319e-b3d8-c91157b34ce2 | -11.9681 | -50.1164 | 2026-09-20 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 201d6502-c79f-37bc-bf3d-5bae5bf63c67 | -3.4003 | -61.3087 | 2026-09-20 15:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 19a71c5b-e476-3ec7-9850-f43b7b03f53e | -2.9157 | -57.8177 | 2026-09-20 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 5a77e1fb-6156-37fb-910e-d670f794ea39 | -6.8031 | -59.1886 | 2026-09-20 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| b114decd-cf36-37da-9746-d6451d1f097a | -12.9084 | -51.01 | 2026-09-20 15:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| f7149972-b863-33ed-8343-ae40955e0c91 | -3.6077 | -59.0577 | 2026-09-20 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 650689ab-bfb0-3080-9b2e-5aae6cd2e2cd | -10.2793 | -50.2177 | 2026-09-20 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| a0ffa2e6-d46e-3dc4-8e47-f02a9ba336f1 | -3.331 | -59.8292 | 2026-09-20 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 68a8b019-9df8-3c74-8038-6288c2b52130 | -11.0407 | -54.1772 | 2026-09-20 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 84b87ee1-707c-3840-86f9-22cd3000472c | -2.8792 | -57.7796 | 2026-09-20 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 003b3a18-d558-3097-aff2-547d8c712356 | -3.5356 | -58.6939 | 2026-09-20 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 8b2473ad-a27a-3149-b711-35c59530ee41 | -6.1109 | -57.684 | 2026-09-20 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 96f48c29-5874-3d92-9f08-943e6afd1d23 | -3.3494 | -59.8097 | 2026-09-20 15:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 3c15c2a1-df7c-3fb2-87d8-dd51f415f740 | -6.5948 | -45.5179 | 2026-09-20 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| f8b897eb-aaac-3d85-b870-be3b0f386e99 | -5.6411 | -43.3687 | 2026-09-20 15:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 0e2c409c-8d47-3dcd-b2d4-1e6d854dad69 | -11.9543 | -49.7728 | 2026-09-20 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 396b8426-c568-34cf-a732-d40bd2335f80 | -6.1046 | -55.6367 | 2026-09-20 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| f086a44e-432d-394d-8072-d0e3fc8b37ea | -11.2336 | -48.3791 | 2026-09-20 15:10:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 469452db-4901-3b4e-9dde-6568a4bc2475 | -2.8779 | -58.2828 | 2026-09-20 15:10:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 17d19730-d580-37ff-aab9-95a02f573b64 | -11.0614 | -49.7477 | 2026-09-20 15:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| b6abcf9c-5ba9-3699-afff-f308a0b80a57 | -8.0708 | -55.3321 | 2026-09-20 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 338c0184-8c45-398f-9f24-94b5cf3ba113 | -9.6205 | -45.8755 | 2026-09-20 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 90cf3dba-512d-307b-8fb5-58cc6af5ede4 | -11.6621 | -50.2169 | 2026-09-20 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 656d8d7e-3571-36d0-9f04-4aedbf419e4e | -9.8136 | -48.3218 | 2026-09-20 15:10:00 | GOES-19 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 5f9d3e01-ffa6-3537-b162-909f1dbedb45 | -9.2563 | -46.2323 | 2026-09-20 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 75ea77c7-9b07-3b03-95fd-644f9f5b67ad | -2.8962 | -58.2825 | 2026-09-20 15:10:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| c4977d98-3faa-3e88-8db9-3ea90bd20c2d | -11.9349 | -49.7968 | 2026-09-20 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| c4e4969c-fd27-3c32-9680-1c3f25495862 | -9.2606 | -45.9164 | 2026-09-20 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| f1de6cef-4cc2-3401-a321-cfab6c608fa0 | -11.1225 | -49.4601 | 2026-09-20 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 1a01e894-1a78-3ae2-b429-5c9eee4fc49c | -7.5703 | -57.6962 | 2026-09-20 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 148.6 |
| b3796fab-fa28-3f70-ac22-2f60e1307896 | -11.3612 | -51.3374 | 2026-09-20 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 2f77308b-1d87-35da-a56f-26dc38859070 | -10.7466 | -50.5959 | 2026-09-20 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 6b55d59d-3c00-3917-a24e-005b41440cdb | -1.75 | -54.9317 | 2026-09-20 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 481e85fa-9b39-3983-8588-d32ef111b5e2 | -10.8757 | -57.1554 | 2026-09-20 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 5efc9f8f-4579-38c1-bb4f-09e003aba1d4 | -9.8313 | -48.4073 | 2026-09-20 15:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 175.4 |
| c23c3ccc-d5a2-3da9-9d15-ad72d853d677 | -11.7162 | -54.5654 | 2026-09-20 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| c4683f75-f7a3-3eeb-a856-d9dd581811ca | -12.5036 | -50.0291 | 2026-09-20 15:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| f97c8f68-b1a7-3091-b8bc-59d5bacb51ea | -3.6945 | -60.6405 | 2026-09-20 15:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 01ae81fc-f80a-3468-aaf4-e36ecdb5860d | -8.169 | -54.7231 | 2026-09-20 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 4e811a06-4eb8-33ea-a475-acefc86bb9be | -10.8553 | -50.9459 | 2026-09-20 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 295.6 |
| 43ad3bb3-8565-3165-a2c7-f25c3fb95102 | -10.8854 | -56.2362 | 2026-09-20 15:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| f90b137d-5e0f-31a7-9042-3e060291a372 | -11.8487 | -46.8781 | 2026-09-20 15:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 96be47aa-2d74-334b-8490-3c9627903cd3 | -10.9694 | -57.1881 | 2026-09-20 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 8ba17580-1853-3fa8-b230-65114b39f4d4 | -6.3014 | -59.9579 | 2026-09-20 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 02a24747-e7f5-37a3-b29a-0993479dcd63 | -6.7185 | -55.0684 | 2026-09-20 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| eb6279bb-21e9-3992-820b-1a44e669f10a | -12.8704 | -50.9933 | 2026-09-20 15:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| edab673c-795f-33a5-af9d-1b88f5e228b5 | -9.2603 | -45.939 | 2026-09-20 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| dac86ea5-1305-3b95-bef7-8f24a4ec8d3f | -9.2188 | -46.2139 | 2026-09-20 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 3d988bbf-bc60-3d0c-903c-1512a9c987a9 | -3.3359 | -58.1191 | 2026-09-20 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| ed7901be-6f17-3044-8eca-52f3918b90d4 | -13.5907 | -51.4794 | 2026-09-20 15:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 188.4 |


[Clique aqui para ver as próximas entradas](README135.md)
