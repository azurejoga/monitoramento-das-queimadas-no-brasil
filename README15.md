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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f78a623-663e-3cc8-b2fa-6bbe746bdbcf | -4.11597 | -51.07835 | 2026-09-25 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5dc57de2-8e38-39da-8f61-8c0f48940b1d | -3.21142 | -53.40485 | 2026-09-25 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec1ee3ae-3ad7-3acc-aa97-881127e1e886 | -7.39132 | -44.77853 | 2026-09-25 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e256b28e-a74f-371e-9e93-e86b36a535e4 | -3.23184 | -46.93357 | 2026-09-25 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 708aa3e6-fba1-3d2d-932a-9046b761d41a | -11.14882 | -43.238 | 2026-09-25 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a5224d1-6903-355d-9e5f-582a527585a8 | -4.30731 | -48.06918 | 2026-09-25 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2fa4a17-2cb5-3ec6-9413-ede4318e5c67 | -5.10072 | -45.51882 | 2026-09-25 04:25:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fab47d16-8322-3a07-9679-a20ce9eee888 | -3.49659 | -50.74162 | 2026-09-25 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af56d404-3318-3f03-8eef-d5d2a3c9a2df | -8.32273 | -44.13135 | 2026-09-25 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82d539e2-4eef-39ce-81e5-8f6460906215 | -10.93721 | -43.83313 | 2026-09-25 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dbd2c6a4-c7cd-3e4d-a7e2-b8770c7afb48 | -3.21192 | -53.40745 | 2026-09-25 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3265822-4cb2-3d99-89ff-4915053c989e | -7.40258 | -42.63432 | 2026-09-25 04:25:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4b2c6f1b-c43b-3e7c-a374-b89cd2f5daf1 | -3.23971 | -46.93486 | 2026-09-25 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f33e0245-03a9-366b-b6ff-209ded0277f1 | -3.98313 | -48.43333 | 2026-09-25 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0959a51d-eef4-3677-8fbf-2acdc01d840d | -4.61116 | -42.79234 | 2026-09-25 04:25:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 766a3786-fa4e-3dff-bfa9-96bb5e932f91 | -7.86169 | -40.01756 | 2026-09-25 04:25:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f31bec78-d4ad-302e-a579-31678912930d | -8.79513 | -49.99401 | 2026-09-25 04:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42a86cc1-20fc-357d-9830-ab7b8d363eb9 | -6.42882 | -35.25271 | 2026-09-25 04:25:00 | NPP-375D | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c289f1a6-8e48-3afe-91c0-285f06a9b93a | -3.23775 | -46.92729 | 2026-09-25 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 1058c3cb-5324-3034-9d90-05485a237483 | -9.01363 | -49.6433 | 2026-09-25 04:25:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66b710f6-3230-3d20-9774-d5aa8dc41c62 | -7.3573 | -42.06835 | 2026-09-25 04:25:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 63060ea1-bb86-3c59-a072-0efe0d90e203 | -9.84892 | -44.18665 | 2026-09-25 04:25:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffcc6a99-02b5-3566-9d7f-177a1f121584 | -8.33049 | -44.147 | 2026-09-25 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a61ceb07-299f-34c7-9daf-7ce63d6c5618 | -3.18053 | -48.01577 | 2026-09-25 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6f2fd6d-ef63-305a-92d9-efc23bb5c185 | -3.93952 | -42.99538 | 2026-09-25 04:25:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96edf5e2-1ac3-3115-aa23-2782908f1858 | -7.35393 | -42.06782 | 2026-09-25 04:25:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f83184a2-255e-3a08-af6b-27bb5f1fe45f | -9.63427 | -43.94698 | 2026-09-25 04:25:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e8392156-0287-3f7a-8acf-fb2ac978b844 | -4.28661 | -48.61003 | 2026-09-25 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 821162f8-9f8b-331e-a630-70c1d8933efd | -10.41165 | -46.25912 | 2026-09-25 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| d9c4d746-6874-39b5-87e0-c6fa16bbb552 | -9.47284 | -40.32962 | 2026-09-25 04:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0b48c528-a7fc-3521-a343-432c6e6f55cd | -10.94329 | -43.88105 | 2026-09-25 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 777775b6-bfb7-3ca5-a563-daea8a5ff224 | -3.01228 | -51.53566 | 2026-09-25 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d4a2a4a-4c1d-345b-8330-75b5aa3ae8e9 | -4.12365 | -51.06404 | 2026-09-25 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64fe2f18-e79a-35b7-af9f-ee234f6f2e64 | -7.02304 | -41.54896 | 2026-09-25 04:25:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 15362b23-e73e-3fbf-a916-815a0edd536f | -6.83242 | -43.56549 | 2026-09-25 04:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1416bcbf-ebdc-39c8-b4bd-cc36bd876cb6 | -7.35786 | -42.06476 | 2026-09-25 04:25:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 206828e4-9b75-30f7-a6a5-75e72d9ddccd | -7.0432 | -45.55943 | 2026-09-25 04:25:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f22a6c69-3790-34a0-a28c-0dabee567a36 | -4.61171 | -42.78888 | 2026-09-25 04:25:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fae2d431-9ca3-3c07-9096-a46e8b2a7e5f | -5.12109 | -42.68897 | 2026-09-25 04:25:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| db5ee83a-3dcd-31d5-9e6c-0013a4930cfb | -8.33632 | -44.14414 | 2026-09-25 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8862f016-62a3-3ea3-8a49-c939b5afe557 | -5.45632 | -45.87619 | 2026-09-25 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bcee157e-36cc-345f-8640-96902d7ebd56 | -5.35139 | -49.04151 | 2026-09-25 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c7f4208-72f9-35c3-b767-35524453792a | -3.21068 | -53.40924 | 2026-09-25 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 394cf3e6-0b80-3bd0-b602-c84d96e29c2c | -10.42015 | -46.27252 | 2026-09-25 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcaab87e-7f2b-3532-bbbd-96b5706f3271 | -2.95525 | -48.58642 | 2026-09-25 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa0e0450-80c2-3ec1-b031-d8560682d063 | -6.30633 | -35.24373 | 2026-09-25 04:25:00 | NPP-375D | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 584e9dcf-7895-38ec-ad98-b4365086b671 | -9.63537 | -43.96151 | 2026-09-25 04:25:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9ccfc2b6-359d-3f0a-9e8e-cd023420c3a6 | -4.11905 | -51.06007 | 2026-09-25 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4524a152-6afb-3774-91f0-ef4d4c93bfbe | -3.23577 | -46.93422 | 2026-09-25 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 97e2883e-9ac7-340e-9d48-df922eef3d26 | -3.20993 | -53.41368 | 2026-09-25 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9a29e22-f345-3d01-a02e-97bb99884e6c | -3.94007 | -42.99191 | 2026-09-25 04:25:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea7662e1-eded-372f-947c-dbe77135a813 | -9.62778 | -49.02154 | 2026-09-25 04:25:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b88f50f5-0cba-36a3-8e44-528e2816396c | -7.12848 | -41.72596 | 2026-09-25 04:25:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2e8a49f3-1f63-3d35-a7e5-ddf4233ebf3d | -8.33519 | -44.15117 | 2026-09-25 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f28c111b-19ee-31af-971d-390a9172e305 | -9.62872 | -43.96044 | 2026-09-25 04:25:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 22d39168-499a-39f5-bf64-afbb3c143dc9 | -10.92555 | -43.86375 | 2026-09-25 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17610617-2acb-3bfa-af5d-fd6c738a069b | -3.20431 | -53.4152 | 2026-09-25 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7aa74a30-0f7f-37b4-90ca-0ea46239e60f | -10.41448 | -46.26362 | 2026-09-25 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce2d6c30-5cab-3a7e-a997-baf5389579ab | -3.50217 | -50.73946 | 2026-09-25 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3e79500-f7c0-30e9-8395-a34730546eb6 | -10.41035 | -46.2669 | 2026-09-25 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23c16624-be15-3db9-a676-9439e03aa427 | -7.12111 | -41.7286 | 2026-09-25 04:25:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e5ff626d-ea04-32d9-87c9-09622692934f | -3.20313 | -53.41699 | 2026-09-25 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac998c8b-ba19-39b4-8d6f-e9f26496b745 | -8.33271 | -44.15456 | 2026-09-25 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1be66510-f20d-3ddc-9e98-0b14a5f08e39 | -3.23101 | -46.93853 | 2026-09-25 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 208b0f8d-0d44-3a30-946a-8cf09019883f | -8.92258 | -44.52858 | 2026-09-25 04:25:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f970c033-fe76-3a0c-b856-a5ba4d1ef1f8 | -7.16373 | -45.03991 | 2026-09-25 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06d6d214-8cf4-34a5-a911-e3786a786e21 | -7.39192 | -44.77486 | 2026-09-25 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b9f7f19e-1543-38d2-8142-f5382661a249 | -9.63316 | -43.95398 | 2026-09-25 04:25:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 76e16294-c09c-3792-a1bf-dbacd8bf3584 | -10.40971 | -46.27079 | 2026-09-25 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d45b8fee-bb10-3d25-a7d7-9a42d1daadff | -4.4567 | -47.92109 | 2026-09-25 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c4ea756-f617-3c8b-848e-748fcb069524 | -3.21035 | -53.4164 | 2026-09-25 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d945597d-3217-3815-a3d9-d044914bc39e | -8.59438 | -48.37354 | 2026-09-25 04:25:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 90640232-be85-3a65-ba84-5c8a34e80549 | -3.23742 | -46.92428 | 2026-09-25 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7a78981c-cb56-307a-8886-7e1573d9a007 | -4.11077 | -51.07785 | 2026-09-25 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa776ad2-0208-33d3-8e76-3de2bd7695ed | -8.77816 | -45.59195 | 2026-09-25 04:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 27853e1b-4d2f-3d5a-8ab0-17e957c76330 | -9.75439 | -48.19739 | 2026-09-25 04:25:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b42cbbe5-185a-375c-a0b3-68408aedb4b6 | -4.11026 | -51.08084 | 2026-09-25 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2be747ab-33b4-3da5-a077-25914c11edd6 | -8.83023 | -49.37817 | 2026-09-25 04:25:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc31a8b9-67f0-3896-bea7-7f5b4e9788e0 | -3.4961 | -50.74453 | 2026-09-25 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e048291a-b8f0-3089-9086-503f042ffec5 | -10.94385 | -43.87753 | 2026-09-25 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19fac067-6361-3f6c-b8b2-0d6694daadef | -8.77754 | -45.59572 | 2026-09-25 04:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 65e13a88-d637-3384-832b-47788d582f68 | -9.6326 | -43.95747 | 2026-09-25 04:25:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 90276a75-dc2b-3d5c-88d0-70b53c7ddb8b | -2.93807 | -48.58514 | 2026-09-25 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd5056d3-bf87-3a45-b4c9-1c115030ad0d | -3.94285 | -42.99591 | 2026-09-25 04:25:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a8a750f-b25b-3005-a6fb-17f7d29aedc5 | -10.44559 | -45.11328 | 2026-09-25 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1642af5b-b69f-3226-ba3f-8f20ced8ad6c | -3.6246 | -42.7604 | 2026-09-25 04:25:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c41b5836-2c96-3d11-ae3d-419bb6a5c1de | -8.03925 | -39.89423 | 2026-09-25 04:25:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1f512b20-bf5e-3c7b-aaef-8ab9b55f796a | -4.37793 | -46.23931 | 2026-09-25 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e8c73e9-9ed7-3362-b6c0-aafd48a00184 | -10.411 | -46.26301 | 2026-09-25 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8d871bc0-497a-300e-9888-02ba07039f54 | -5.20085 | -45.37229 | 2026-09-25 04:25:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b40f4be3-7f5e-3ce0-a3a6-d81dd9082b8d | -8.38653 | -36.70646 | 2026-09-25 04:25:00 | NPP-375D | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a1b35338-af41-3dd4-9486-7150a7fd2c76 | -10.44895 | -45.11384 | 2026-09-25 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dea9d346-3356-3d35-a797-984c69d0108c | -5.35208 | -49.03735 | 2026-09-25 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 099afefd-7ba6-3378-961c-27d837fc623f | -8.34853 | -45.61252 | 2026-09-25 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f442ae9d-2a09-3eeb-8de2-1b346c3564ae | -3.01301 | -50.29969 | 2026-09-25 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2c81475-e01c-36ff-8582-49c0bea3416c | -8.33327 | -44.15104 | 2026-09-25 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4034618f-313c-3257-8a74-79e1e52555f0 | -4.11544 | -51.08149 | 2026-09-25 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1726126-108d-33b0-ac5b-715fbf951bc7 | -8.2545 | -54.69176 | 2026-09-25 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| da8c0cd4-cc97-3751-a5f5-bfca1239930f | -9.38811 | -46.292 | 2026-09-25 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19270363-3db7-3132-b03c-b1966b72237b | -2.56613 | -49.08721 | 2026-09-25 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README16.md)
