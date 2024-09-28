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
| 1c761472-6e88-3203-8f4a-f6853cd72d0c | -17.05183 | -56.13633 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b47e51ba-f701-37b4-9452-c3acd67219cf | -17.05 | -56.12234 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 04f5ea5d-2418-3dcf-8e69-89de8e3558d8 | -17.04938 | -56.12682 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 71ec9d06-ca19-3f02-85ec-c32420c48d1a | -17.04877 | -56.1313 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0ebefc27-b365-369a-8bcc-e24e1f8ae51f | -17.04679 | -56.12397 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0a19428c-634f-34dc-b510-8ca3d2780bc5 | -17.04632 | -56.12178 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 01109545-793e-3d96-921f-ad223451f028 | -17.04552 | -56.13292 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cb743f08-2fc8-3aad-bdcd-d469ce1d3fa4 | -17.04312 | -56.12342 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0e60595d-f0a9-33fc-ba8e-2dd364fb6b2a | -17.04265 | -56.12123 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2f107218-d3cb-3d49-88b8-0dc9fe1c7713 | -17.04204 | -56.12572 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 23c588d2-e5ca-355c-b0e9-fa5625bfda86 | -17.04008 | -56.1184 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 63cafbda-6381-37c3-ad6c-328727a84479 | -17.03959 | -56.1162 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9722d5de-ff35-3f5b-8edc-a2e78ec10319 | -17.03641 | -56.11785 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d6950b8f-2ae7-3a7b-9e4c-9251292113b7 | -17.03337 | -56.11282 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7210aa0d-dca1-305e-9baa-7b7231f2a542 | -17.03033 | -56.1078 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| defbbde0-5375-3c5a-8b32-872757d76fdb | -17.0297 | -56.11228 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b724fa3d-7e5f-3374-b53a-5e4db2cd2c7b | -17.02666 | -56.10725 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| f2ac4e64-2919-3082-85ae-1de3425c83b8 | -17.02299 | -56.10669 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 9664356b-a82f-371c-a974-5e8e78626f69 | -17.01931 | -56.10614 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 149fe090-bfd5-3e2e-a48f-3fc3786718bf | -17.01563 | -56.10559 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 71abb3df-5152-335d-a82f-3e171068dd3e | -17.00578 | -56.12239 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2b92bde7-2b30-3929-988c-9b714e4133ef | -17.00328 | -56.14027 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 3bc0ad2c-4004-3489-950b-29a1a2aa086c | -17.00211 | -56.12185 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4acdc6ee-5dbb-3a90-9364-7394cd798657 | -17.00149 | -56.12632 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2261a0ec-dd43-3871-a978-9a3c08a2d1ea | -17.00086 | -56.13079 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 001fc088-5660-3e43-9d31-1a338ab2c746 | -17.00023 | -56.13525 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1ccf76a2-fa0c-3c7e-a3f1-ad679b5e2496 | -16.99906 | -56.11682 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8c191492-6d48-3a39-9bb5-bdfaee6e4c04 | -16.99844 | -56.1213 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2f4f7e98-fb6c-311a-a7e2-edc61d0a669a | -16.99781 | -56.12577 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f5c9e257-6a49-3244-9075-c33d5de7e478 | -16.99719 | -56.13024 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9d62f5b9-c0ac-3995-9f85-47c84f5e8ac2 | -16.99656 | -56.1347 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0421ef38-a5b0-3550-93f7-c2ca00760ce6 | -16.99602 | -56.11179 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4354fdb9-24d5-3359-93ca-072fabcf3a51 | -16.99539 | -56.11628 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 979c371b-4b03-32f6-a4e1-a7e78b808bb4 | -16.9929 | -56.13415 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 5c97452b-c9ec-3e4d-8104-3655b01d4f89 | -16.99235 | -56.11125 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2328de63-2f80-3a35-9510-4d1b5bd45fc8 | -16.99172 | -56.11572 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 37fa40aa-bca7-33c1-b019-31a6721205b0 | -16.98867 | -56.1107 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 405d4558-0490-31bf-8f4d-13ca24dc6bf2 | -16.98805 | -56.11517 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| ce4e4afa-8f24-3a91-86b7-d4a6a49c4199 | -16.98562 | -56.10566 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 4705f5eb-2850-3fd1-9c26-234a7453f51e | -16.985 | -56.11015 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| db233e5f-ddd8-3efb-ae7a-b502235833be | -16.98438 | -56.11462 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| d9e5e3c0-4794-3f79-b52a-2ad39d387b72 | -16.98195 | -56.10512 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6e4b0a41-457a-3d8d-aefd-379cf74448ff | -16.98133 | -56.1096 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| d6b25929-fbb2-3c91-942c-0109058fdf79 | -16.98071 | -56.11407 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 019e393c-bdf2-3b47-9b49-08b2e8ae8037 | -16.97766 | -56.10905 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 192f1687-e00e-357c-b957-0cb4679f3c5c | -16.95501 | -56.11021 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2f51f65a-66ef-3e27-8225-0010c4e5b13d | -17.13667 | -56.35986 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cef0d969-87ab-3128-9b44-9c6ed063fa87 | -17.11769 | -56.2009 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 2cfae4c6-3f16-3a02-a0fc-9710b127cb3d | -17.11707 | -56.20535 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| e42ba962-68d5-3b9d-af92-3b78f6abeb90 | -17.11644 | -56.2098 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 19d2fb05-b075-3309-9b9b-707bf1e521cc | -17.11529 | -56.19146 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 917b4b73-4137-37d9-acbb-d85cf8b72236 | -17.11404 | -56.20035 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9950cdcf-c818-3e6c-b09f-7e33967420c2 | -17.11341 | -56.20479 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| afb6a037-6c34-3d79-bd0c-e2a5fb9aaff1 | -17.11278 | -56.20925 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 8a9be862-9f1c-3b50-8c11-245c2ebe8918 | -17.11216 | -56.21369 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 36255389-06c3-3751-a75d-a10e60a05eb9 | -17.11163 | -56.19091 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 6ad69e64-a8ec-3659-bd5e-5169cddc6d7e | -17.111 | -56.19535 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 2bbb74d2-9838-36b0-b4fa-7fa8eef1f297 | -17.11038 | -56.1998 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 78080163-cb70-3d0a-b8fa-fab63e9901d5 | -17.10975 | -56.20425 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 451d5fce-6a6e-3bfb-bb29-075b4b6ee5ad | -17.10912 | -56.2087 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 26f93d7c-8d4c-338e-a02a-9da315dffc12 | -17.10609 | -56.2037 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3bb9be1e-2e84-3dca-99d2-2ce8194608ae | -17.10547 | -56.20815 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 0e956e76-0c57-3844-8a93-2615863710db | -17.10484 | -56.21258 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| a1a6868e-94d7-3a3b-a99d-39179cbb8ecf | -17.10243 | -56.20315 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1c2d37bf-9289-3795-96d3-8371bc8eeeb5 | -17.10181 | -56.20759 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 09800134-bd9f-3571-b491-890a94d36d88 | -17.10118 | -56.21203 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| c1bfec64-14ce-34b9-a8d4-e98415ddc7f3 | -17.10003 | -56.37811 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 939a7057-a396-3b49-8bc2-d7870803c8ae | -17.0994 | -56.19815 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| baa3cb39-4eac-33d1-ad51-4622a8745306 | -17.09815 | -56.20704 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c89089e8-2010-39a3-b7ee-99979abef092 | -17.09753 | -56.21148 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 83e14105-0f77-3063-af04-02622504cf52 | -17.09641 | -56.37757 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 14498c5c-2bc1-3c5c-a9cb-37f7f9c55b6b | -17.09579 | -56.38193 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 51fbdf6e-458a-3613-9fb5-66ebffe5547e | -17.09449 | -56.20649 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5ff45f6b-bc73-300b-922a-924b9843bf26 | -17.09387 | -56.21094 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3d4672cd-2a4c-36ea-8574-c01bb3123eb5 | -17.09278 | -56.37702 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 895cdfe2-32e6-331d-9be6-b29bb66214f9 | -17.09216 | -56.38138 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c1d8b1ec-dee1-3903-b36b-42dcc8436a55 | -17.09083 | -56.20594 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 19.1 |
| bcb8ed0e-ff9e-3d2d-aeb9-c69430c55700 | -17.08915 | -56.37647 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 341540d3-485c-3424-907c-1d21143533d7 | -17.08853 | -56.38083 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0f57ee34-e505-3d6a-b2cf-41d211611919 | -17.0819 | -56.37537 | 2024-09-28 05:12:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bcf1b346-1995-32bb-b2f7-020eadd3254a | -20.59335 | -56.21154 | 2024-09-28 05:12:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0446da2a-d0b6-3d8d-9516-54be0bc7bd8e | -20.59018 | -56.2138 | 2024-09-28 05:12:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c4459fc-b6bc-355b-b060-1fe67e33590a | -20.58953 | -56.21103 | 2024-09-28 05:12:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5292a81b-03e3-3b06-ae3e-40377dfd0229 | -15.92983 | -57.19252 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc0e0906-8e4f-3837-a6fc-97c793e0a907 | -15.92924 | -57.1966 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f2a21e8-d536-32ad-a394-604cfd9aae58 | -15.91357 | -57.19109 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a8d0dea-e729-3441-9b9b-f6211ab64fdb | -15.91185 | -57.20271 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 290b7c38-446e-31eb-8345-b2a18a05b8ad | -15.90896 | -57.19832 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74648e97-bacd-33a5-85ee-edeb8394fa47 | -15.9084 | -57.20211 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c00e7a73-fcb1-3e80-a464-e9e33cdc4353 | -15.78646 | -57.78541 | 2024-09-28 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 497567bd-040a-3220-a879-60cba388cea7 | -15.63674 | -57.47618 | 2024-09-28 05:12:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8a9b564-12b5-35b5-be9b-52e0cdcad795 | -15.63389 | -57.47184 | 2024-09-28 05:12:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec7b942e-dcaf-366c-9f01-4d0007c7a4a7 | -15.63333 | -57.47565 | 2024-09-28 05:12:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5326a168-71fc-3937-8895-df2bb3560fe8 | -15.63048 | -57.47129 | 2024-09-28 05:12:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0127407-76b0-3bb1-8992-15038e799873 | -15.62991 | -57.47511 | 2024-09-28 05:12:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bad93e10-0e53-3891-9e65-a14d70ebbe54 | -15.62877 | -57.48273 | 2024-09-28 05:12:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d82afb8-2178-33c7-b072-93b985045384 | -15.62536 | -57.4822 | 2024-09-28 05:12:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddf494bf-136d-3807-89f4-06dc2ba9683b | -15.62479 | -57.486 | 2024-09-28 05:12:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 478d767c-3aba-3b5c-8a3b-27f6d69007bc | -15.62194 | -57.48166 | 2024-09-28 05:12:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5d8d50c4-2c9a-3dc5-a3ab-5f6fe2cd1092 | -15.62137 | -57.48546 | 2024-09-28 05:12:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README95.md)
