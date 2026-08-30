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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1851d31c-62a1-3e27-9ccc-faef34fe9e6e | -10.7752 | -44.8852 | 2026-08-30 06:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 7a50adbf-a845-3e2d-a100-ec20c4b628bf | -9.8927 | -60.2752 | 2026-08-30 06:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| e8e8f05f-4314-3578-a6a2-ac52a5afdbff | -4.9604 | -55.8424 | 2026-08-30 06:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| d3a6aa39-a338-3a43-ae81-ed0dbe20b1d9 | -11.8021 | -51.0343 | 2026-08-30 06:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 4841795f-75e4-39f6-af29-e2cfab32727a | -6.86574 | -41.66088 | 2026-08-30 06:12:00 | AQUA_M-M | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| ea5119d7-1731-3fc9-b284-11c68c0d4d1a | -4.36399 | -47.77499 | 2026-08-30 06:12:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 9763bbb1-4815-324c-8c34-1aa02e2fd72c | -4.57945 | -37.73159 | 2026-08-30 06:12:00 | AQUA_M-M | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 23.8 |
| d8bb4915-4c0f-3170-8e83-63a46828d9d6 | -6.91569 | -41.63361 | 2026-08-30 06:12:00 | AQUA_M-M | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 3d5d6e3a-620e-3543-b051-1d401efbf2c4 | -6.86416 | -41.67098 | 2026-08-30 06:12:00 | AQUA_M-M | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 5d1105a3-93a4-3873-83ab-853a2bb4dd83 | -6.34315 | -44.08744 | 2026-08-30 06:12:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 09081a19-3404-3990-9edb-098381ac8094 | -6.8626 | -41.681 | 2026-08-30 06:12:00 | AQUA_M-M | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 50.2 |
| fff1f93c-f5cd-32bb-907a-c6d956e3ed73 | -6.34088 | -44.10199 | 2026-08-30 06:12:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 530b4a79-2fd0-3370-b1d0-037695fdf01a | -4.36981 | -47.76828 | 2026-08-30 06:12:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 042a75a9-ce18-3763-b3d9-c961f25cec91 | -6.34464 | -44.09326 | 2026-08-30 06:12:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 15d041ac-84db-3d0b-bebf-8bb198c41369 | -6.90747 | -41.63672 | 2026-08-30 06:12:00 | AQUA_M-M | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| d3997333-6f35-388a-b377-628f506261de | -3.6335 | -60.55556 | 2026-08-30 06:12:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7bf6a9d6-619e-3a4c-8f59-346c0d820138 | -4.1521 | -60.6964 | 2026-08-30 06:12:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3fd16312-c3eb-3267-85e3-5ff8d1a54507 | -3.62695 | -60.559 | 2026-08-30 06:12:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 057d6d57-3dc6-35f7-9884-ca463e862035 | -3.63287 | -60.55982 | 2026-08-30 06:12:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| aace1f86-83fd-37ab-b638-c2af379c5e0f | -4.15739 | -60.70148 | 2026-08-30 06:12:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8683174-72e5-37ae-a843-48f4dd8d17a0 | -3.62231 | -60.54955 | 2026-08-30 06:12:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 54196a8e-0189-370e-a395-7e7f44a86473 | 0.14771 | -60.39995 | 2026-08-30 06:12:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81f238ca-6b07-3ddb-b009-041d1731a24c | -3.63223 | -60.5641 | 2026-08-30 06:12:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a775effd-ec7d-3232-abfe-dd7fa7781341 | -3.61703 | -60.54437 | 2026-08-30 06:12:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d15d4848-8c01-35c6-a540-419374c33e1d | -4.15864 | -60.69301 | 2026-08-30 06:12:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a8d94a18-b488-34f7-b2a4-fb0d1826d203 | -3.62758 | -60.55474 | 2026-08-30 06:12:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9d11429a-3f8d-3a0f-a72c-34f9381cce9d | -4.15273 | -60.69216 | 2026-08-30 06:12:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a7bb3c46-d3f5-3b47-87bd-38efe2f84a1c | -4.15801 | -60.69725 | 2026-08-30 06:12:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df3efd3c-e44a-334a-bbf7-bb03178583a9 | 0.14477 | -60.39958 | 2026-08-30 06:12:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd86a7eb-2855-3cb6-9164-8cd4bb89a733 | -3.76192 | -59.33596 | 2026-08-30 06:12:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 850f40cd-307a-3d21-84fc-e9672368c7bb | 0.13912 | -60.40046 | 2026-08-30 06:12:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee93f3a6-f6cd-3f89-b47e-109fc09997e3 | 0.15043 | -60.39875 | 2026-08-30 06:12:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa1b7ab6-f1bf-391c-a6b1-d625459b05a0 | -3.76832 | -59.33691 | 2026-08-30 06:12:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 67885b27-c8de-3129-9280-e441a4b59235 | 0.13972 | -60.40426 | 2026-08-30 06:12:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a308a092-7e92-3b84-8f6a-2f8d0cb3bcf2 | -3.62822 | -60.55045 | 2026-08-30 06:12:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ae459686-86a7-3f13-b83e-c5cb4a53180b | 0.14537 | -60.40343 | 2026-08-30 06:12:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72a87606-6b0f-3fd3-97a4-82471f1259a7 | -11.78934 | -51.02911 | 2026-08-30 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 153.5 |
| d02cfdc7-9d39-33a0-9207-847ccb72a8bd | -17.41955 | -42.63099 | 2026-08-30 06:14:00 | AQUA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 77bbed4a-452f-3814-ad98-2e04f2880d47 | -10.94432 | -43.03326 | 2026-08-30 06:14:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0fe81959-9d9d-3666-b11d-652a5e149357 | -11.80257 | -51.02749 | 2026-08-30 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 0a363d05-c89f-3987-a543-170872d72131 | -11.80641 | -51.03246 | 2026-08-30 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| d2a34c82-a8c5-3695-9356-6cf227b1bb95 | -11.34583 | -45.1633 | 2026-08-30 06:14:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 295ce70c-180d-39fa-9df9-51e241f2b2e4 | -10.94859 | -43.03968 | 2026-08-30 06:14:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 45c8162d-476a-3ed1-8628-d74d32e25e43 | -19.87003 | -44.61263 | 2026-08-30 06:14:00 | AQUA_M-M | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| faa70a18-8d0e-324e-a6ee-df54626e3a0c | -17.42099 | -42.62172 | 2026-08-30 06:14:00 | AQUA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d27fd86f-9a5e-314f-a98e-45d83e31d32e | -15.13663 | -50.62769 | 2026-08-30 06:14:00 | AQUA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 33.5 |
| f2858dd8-1f1d-3f28-bfdd-1ace8f3e7631 | -11.34379 | -45.15717 | 2026-08-30 06:14:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 37ae21b3-0edb-3517-820a-6822342821b5 | -10.78463 | -45.33317 | 2026-08-30 06:14:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 605018ff-07fc-313d-ab59-a6a1b87dd930 | -11.78551 | -51.02408 | 2026-08-30 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 0355338b-42b7-3113-bbe4-24b2d6322b09 | -11.53288 | -45.55897 | 2026-08-30 06:14:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d376d50b-18bf-346c-9c25-2c81104be63d | -16.28132 | -42.57078 | 2026-08-30 06:14:00 | AQUA_M-M | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9219524c-fd7f-3569-8295-edf711137007 | -11.35679 | -45.16529 | 2026-08-30 06:14:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9a4f8733-02c8-3021-8f5f-e58298304402 | -11.34837 | -45.14841 | 2026-08-30 06:14:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b66a9e58-6621-3054-88e5-e6711a78c37d | -10.7872 | -45.31796 | 2026-08-30 06:14:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 84ade7a9-0333-328a-a2e9-bec4283f6f70 | -9.0616 | -65.41684 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6b49695f-e58b-38ce-8e13-cba0d85527dd | -9.02898 | -68.508 | 2026-08-30 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c8796ef8-3b81-3b17-a6dc-9f8dd8b42d75 | -10.49465 | -59.61232 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bbe740a-6f3c-397a-8cd0-2c9be6463c0a | -9.06963 | -60.48669 | 2026-08-30 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ab8a5de-60b2-3c21-a832-5e6174484ce0 | -8.60026 | -70.21379 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac0543ba-c3b7-3a46-a8d6-76644d0b55de | -9.15812 | -59.51971 | 2026-08-30 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbde4cb7-709e-37a9-8892-cf51e3075cce | -9.84973 | -60.27711 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 740fb74c-b960-364a-beef-0b3f2eb7cea7 | -8.42377 | -70.20303 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63c301f9-7051-3d18-996e-beeaaf626333 | -9.05631 | -65.42099 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ddf323a8-0b84-3c45-933c-23e9a08cdac6 | -8.15147 | -64.00075 | 2026-08-30 06:14:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 716dd348-8e84-3da3-9251-f3135fbd5653 | -7.56221 | -61.31691 | 2026-08-30 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6ff048e4-e233-328b-b99a-d88723649be5 | -8.94895 | -62.37216 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6ea6456-d7d6-31ea-89f0-2ac6ee56ac46 | -10.48707 | -59.61767 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6149158e-f14a-3f97-9595-2d5e18d480e6 | -9.93821 | -60.52482 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2b83e0c7-cd89-3eb3-868f-a823f5fd6b08 | -7.46083 | -70.13634 | 2026-08-30 06:14:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 832a77ec-68a7-39c4-a26a-ecab636a1cf5 | -7.97507 | -70.02811 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b75fd540-7c83-30f1-977e-680a2caf900c | -9.05563 | -65.4258 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 993d917d-4d87-3de0-b948-aa113ed922fb | -8.26016 | -62.75537 | 2026-08-30 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a8058de-badb-3391-a72b-de4546bde01d | -8.14606 | -64.00294 | 2026-08-30 06:14:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a25971e4-cfda-3aa1-b1d3-2ee20cebb255 | -8.95485 | -62.41613 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93769447-085f-3668-b9dd-d4b80af0868b | -7.39753 | -60.58435 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cabe984a-9c43-39f2-a0ff-c81843a6781d | -8.67187 | -66.51273 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63efcd21-8035-3229-832f-927b779b59f5 | -9.64941 | -58.94114 | 2026-08-30 06:14:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 669d1eb5-766e-337e-9f49-8a1a24519a26 | -9.93303 | -60.51329 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f32c218c-1163-34d3-85b4-37acb9ffe92d | -9.51557 | -65.57986 | 2026-08-30 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1602c79-9c10-3d07-bb30-b0a1448e7c59 | -9.60283 | -68.62736 | 2026-08-30 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0afae1a4-f924-383e-b173-99a6fdf01837 | -7.55149 | -61.30648 | 2026-08-30 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ea21caf-ae30-37e1-8878-9e6ba621239a | -9.50638 | -65.5786 | 2026-08-30 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0682908c-dfd9-3b8a-8565-abd4e78de533 | -7.32578 | -60.61034 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc4cf050-c0f9-3a5e-9a38-f4b8f652a29b | -10.48553 | -64.50802 | 2026-08-30 06:14:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 60960bff-39b2-347a-800c-ddbca5c1eafd | -8.91524 | -66.95325 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 745531c1-9234-38ff-a316-21681cb5fecb | -8.94496 | -62.38241 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30edc9d6-96cb-3bc5-be79-47e321966d78 | -7.23602 | -60.63061 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6d622f83-3b6c-3a06-aaca-8db4db458537 | -8.15649 | -64.00144 | 2026-08-30 06:14:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31a15fb0-40db-3502-9734-4c27a33b9d45 | -8.94846 | -62.37601 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a5d9cc5-0bd3-3ba3-a124-74baa7f61f5b | -8.5872 | -66.95332 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f748060b-d717-3563-889a-8a01a311c6b7 | -9.05305 | -65.41075 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d3b78b84-0f18-3f7e-9a47-57ce3c91411f | -7.39797 | -60.59099 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0df99d1f-bc20-3b29-ab09-b68a5fca0d4e | -10.48781 | -59.61132 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d5386fab-8f8d-3e7f-9f52-a73913c1f55f | -8.95733 | -62.39677 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf3dae38-4909-3dc0-b3e7-c1214047bfdd | -7.9741 | -70.02766 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a7a29c4-22d5-3aba-9cbe-9ede1bc59f34 | -7.70197 | -61.15829 | 2026-08-30 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a1aad34-1382-304f-bfb3-4108e259c34f | -8.95462 | -62.37294 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73a7533b-b2b0-3f7e-8d33-3ec6cf43d455 | -8.24794 | -62.75762 | 2026-08-30 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29981657-e161-3de0-8264-470f0e17e990 | -8.2597 | -62.75886 | 2026-08-30 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a220380f-e551-306d-b673-df73c7b6c7b1 | -9.05766 | -65.4114 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README72.md)
