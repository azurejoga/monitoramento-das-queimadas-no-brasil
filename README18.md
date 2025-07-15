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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efbd4c67-0dce-3311-bf87-5b985e773310 | -7.06002 | -44.03548 | 2025-07-15 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c9dc6fc-45f4-3df1-bfe0-bf9a323d2f3a | -8.26087 | -46.36383 | 2025-07-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8beb9b7d-8bbf-3ab4-937a-5a9643196fb7 | -5.7842 | -45.11896 | 2025-07-15 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff565a19-3188-3d9c-aa24-5cf5160bc05f | -7.1923 | -43.10316 | 2025-07-15 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b7600bb7-65a7-3c55-ae6f-8df19f81b008 | -6.76654 | -46.199 | 2025-07-15 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd843320-b64b-3bd3-ae62-fe9cc45acc07 | -8.64618 | -47.74773 | 2025-07-15 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58b59629-7ef3-3700-89cc-bacfa1f2ea94 | -5.20646 | -42.5058 | 2025-07-15 04:32:00 | NOAA-20 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 99a36fdd-88af-3fd3-8c76-25b8db160a11 | -8.88315 | -50.15001 | 2025-07-15 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12a57a04-0572-3e68-90bb-693b27818242 | -3.66625 | -48.32497 | 2025-07-15 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c63cb22-5a27-3a47-9d14-2702e812bd79 | -7.08355 | -43.69635 | 2025-07-15 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c26248d0-dd82-3279-a554-c427fff12760 | -7.27991 | -44.03967 | 2025-07-15 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5749fee-e81c-31fd-bdf1-23df82405fb3 | -8.21949 | -44.91516 | 2025-07-15 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f072766c-3c2c-34ae-82c1-3f49ef1b1929 | -6.15082 | -44.08723 | 2025-07-15 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edfe97ef-9ca3-3126-86c7-0733a037ec01 | -4.6838 | -43.25346 | 2025-07-15 04:32:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2705b916-3613-31c1-bc91-1173f00eb32d | -4.27334 | -48.18166 | 2025-07-15 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 25859d4d-e0c3-3df2-a85f-158cd70f353d | -4.78023 | -45.33942 | 2025-07-15 04:32:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 68c6f73f-4ef9-3dd4-bfd6-72fcd4c4ab92 | -4.03131 | -48.05803 | 2025-07-15 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d73ad145-80e8-30ab-92a9-62f8df596be1 | -7.09642 | -49.17148 | 2025-07-15 04:32:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37eb918f-6008-3a52-9132-43a52e49290c | -8.23508 | -44.93291 | 2025-07-15 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd543f8e-048d-37d8-838d-02a9c165885e | -3.2976 | -49.19266 | 2025-07-15 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7d1195d-def4-3754-9cf1-f3bdbd9fa6dc | -9.77836 | -49.1246 | 2025-07-15 04:32:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 525f9167-2416-3b58-8580-16d4163c2ac7 | -4.22366 | -47.76696 | 2025-07-15 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bfbaf3a-78cf-395a-8b46-6948b05bb6ee | -9.61812 | -49.0204 | 2025-07-15 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a60f180b-6c33-3c53-931b-5b145dc6382d | -5.23147 | -56.01661 | 2025-07-15 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f0091e4-0028-3781-bb87-8d89b83274d1 | -7.81324 | -46.56717 | 2025-07-15 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 20536afe-9494-3908-a626-e65e2baec9ee | -7.88874 | -44.49533 | 2025-07-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 674829db-410b-3a11-aa88-f34162fc5edb | -10.64185 | -45.22377 | 2025-07-15 04:32:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f9f1ea7-cf54-37cf-8c90-56cd29ac9254 | -4.03739 | -48.06253 | 2025-07-15 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90b98b34-7612-3d03-a85c-beb5f8b2ed2f | -5.78481 | -45.115 | 2025-07-15 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c503846c-8e77-32cb-8718-004c6b891b0e | -7.30269 | -45.35923 | 2025-07-15 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6d724718-608f-3bf2-9039-a7f7481cb312 | -7.05971 | -44.03292 | 2025-07-15 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94c7f05e-e7a6-3d29-9429-bcb18ca90230 | -3.48448 | -51.18752 | 2025-07-15 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4266ee61-8fc1-3f6d-be63-cb3bad599237 | -6.4177 | -45.32761 | 2025-07-15 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1dfcdb6-8dd1-3795-ab31-9fdc11df6942 | -3.51242 | -48.43762 | 2025-07-15 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9050f34-c095-30b0-ad83-390b4230b766 | -6.43922 | -44.97256 | 2025-07-15 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a730c2fa-7b52-3170-bf52-79ca62660e20 | -8.59676 | -47.43261 | 2025-07-15 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| def6f040-1166-36b0-9ee3-b039304fc1eb | -3.36526 | -49.16553 | 2025-07-15 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0fcdcfe-8efb-3e4c-9c95-e350660c3dfc | -8.90872 | -47.34642 | 2025-07-15 04:32:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd41e228-1951-3696-bd8c-27a991644f6f | -5.98286 | -43.7645 | 2025-07-15 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11038336-14e5-37d3-9d98-8ca5c5fde397 | -6.13591 | -44.08456 | 2025-07-15 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d4a8602-c488-34e0-8022-3b83ad388c81 | -5.78309 | -45.10259 | 2025-07-15 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ade9b79-3aa6-35ef-90a8-1825c99b406a | -3.76182 | -47.11624 | 2025-07-15 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48bd09e3-f979-376b-90ad-84525634da30 | -8.23583 | -44.93107 | 2025-07-15 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01cf2773-3eda-33e8-b57c-62184b58df47 | -7.2761 | -44.03908 | 2025-07-15 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a13cf65-c20c-387d-861b-ae2e520e04e2 | -4.82015 | -44.35663 | 2025-07-15 04:32:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d70e575-ccd8-32c2-b272-ba3e5d26ed2c | -9.62142 | -49.02094 | 2025-07-15 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e82a9281-953b-3bb2-8359-01351bb16701 | -5.53882 | -43.88642 | 2025-07-15 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f413f90d-5563-3499-b32b-b6070f7fbcf1 | -4.72775 | -48.84985 | 2025-07-15 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4708391b-f676-3a77-93f2-765024e31178 | -10.3714 | -47.14889 | 2025-07-15 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d446a991-d29e-32e2-a65b-fd0e2fb26338 | -6.53226 | -42.36956 | 2025-07-15 04:32:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d8e3cda9-bf48-3c9b-82ba-b1822fcf8ccb | -7.28063 | -44.03495 | 2025-07-15 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ae1d8a7-a0fa-3aaf-beb9-e17dba4500d6 | -8.87579 | -50.15255 | 2025-07-15 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9eedc464-be6f-3d4e-adeb-4f20f4fa88a4 | -7.13322 | -43.44411 | 2025-07-15 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6db26149-29d2-3e63-b042-8d119e10a52a | -6.37979 | -43.71812 | 2025-07-15 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a5e743fc-1070-3e90-bbc5-e67bf49efec2 | -6.47254 | -45.37164 | 2025-07-15 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15230654-f0f4-30d8-ba53-68078f1d1569 | -9.36274 | -48.55107 | 2025-07-15 04:32:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20d13639-467f-318c-aa76-b52b79a736ff | -8.22681 | -44.91632 | 2025-07-15 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a10138ce-92ff-3949-9cc0-24092a7c1b30 | -8.38111 | -51.07123 | 2025-07-15 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32057ed9-4b09-395a-ac0f-1c11404fe643 | -6.15765 | -45.85223 | 2025-07-15 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 55b84579-251c-34ca-b200-2deb25d66562 | -4.68841 | -43.24919 | 2025-07-15 04:32:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38563de2-f4d2-3d84-9eee-1a9d9b54dc2a | -8.59621 | -47.43616 | 2025-07-15 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01369554-c66e-3c45-acba-49b107da73c8 | -6.13964 | -44.08518 | 2025-07-15 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 549838d0-e76c-387b-b610-3e60bfd0a347 | -6.8779 | -50.26744 | 2025-07-15 04:32:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 22fae644-58dd-3c2a-a775-08097768ba70 | -8.38397 | -51.07577 | 2025-07-15 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f768f71c-729f-3538-a9d1-71cbe039a91e | -6.54646 | -44.68403 | 2025-07-15 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76ec3b1f-f88e-34a4-a3ea-f2b341192feb | -9.62195 | -49.10327 | 2025-07-15 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bdd8b112-1fb4-32df-b4fc-3747792f1234 | -8.87502 | -46.85933 | 2025-07-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bdb9518-9c97-3769-9ce9-98e38198b6ce | -8.68721 | -51.45828 | 2025-07-15 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| edd16e3f-e717-33c5-ad1a-6a593be92c03 | -8.23649 | -44.92672 | 2025-07-15 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 838702c5-f52d-3a43-ba81-707f8dc5b0b3 | -8.28859 | -44.97626 | 2025-07-15 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3ec61f1-6651-36ed-9110-9c494c9129e5 | -5.57995 | -46.52739 | 2025-07-15 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 55b25d1d-a4da-3537-89d6-368608bde94b | -3.22398 | -46.79888 | 2025-07-15 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 814b7a04-cf77-3342-9d31-722e0dd4b675 | -6.15708 | -45.85601 | 2025-07-15 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| fcc63adf-201c-38c1-a4a5-2209a4c806d0 | -3.33208 | -48.71434 | 2025-07-15 04:32:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb460f9b-a686-30b7-8311-f281d1340570 | -6.71124 | -44.32831 | 2025-07-15 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30f185f1-0b5e-35b9-b231-07685834f89d | -5.78017 | -45.09806 | 2025-07-15 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8030839b-85bb-311b-9472-7c61d1fd6452 | -3.58632 | -47.51792 | 2025-07-15 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c52333a-4229-33d7-b987-e5b02a163856 | -8.81701 | -48.43526 | 2025-07-15 04:32:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dff6e86b-4c54-3c60-999b-7c7e1c35acd4 | -3.92894 | -43.15343 | 2025-07-15 04:32:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d99d2373-bce4-3228-bb51-c525cd624da6 | -5.78492 | -45.09066 | 2025-07-15 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f40b06fe-52a5-3fca-b6ae-4cf184449c13 | -7.19581 | -43.10731 | 2025-07-15 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 18dc7e9e-dfca-3780-859b-bde38f254bca | -6.90998 | -52.85517 | 2025-07-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96a988f4-e40b-31aa-8905-4ae9d8096c34 | -7.09585 | -49.17501 | 2025-07-15 04:32:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cc2ee94b-c8af-39ce-82a1-58332e26b9ec | -6.71868 | -44.32943 | 2025-07-15 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6c460b9-f70e-39a1-8bc6-7cb635b9d81f | -6.24256 | -43.34323 | 2025-07-15 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 478059ab-e5c6-3ae8-8e0d-081e6649f015 | -4.68597 | -43.2506 | 2025-07-15 04:32:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cd495a0-628d-39fa-a767-912212ca6020 | -4.67993 | -43.2529 | 2025-07-15 04:32:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6c1a31e-40a7-372c-9249-11b88cdd3611 | -7.75505 | -40.63024 | 2025-07-15 04:32:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| adeb2b27-6671-34bb-a07e-fdccd66d1e60 | -10.37595 | -47.55766 | 2025-07-15 04:32:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13c6534b-d798-3b71-8893-2f513cbd9699 | -7.30011 | -46.2595 | 2025-07-15 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1910e3e-746f-39e4-b18f-1d2c51c053ab | -4.78369 | -45.33993 | 2025-07-15 04:32:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cb9a1ad-89d4-3757-b906-dfc5215e9928 | -4.6819 | -48.8643 | 2025-07-15 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a5b85e0-ce5a-34d6-b93d-f2f29fae91df | -7.08918 | -49.17395 | 2025-07-15 04:32:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf5c96d7-a450-361a-806d-4eb2cf12f1da | -8.60901 | -47.44178 | 2025-07-15 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5edf76e9-2de3-31a3-930a-0f53a1fe80cc | -6.38433 | -43.71396 | 2025-07-15 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a7903cae-43cb-372b-a055-faf8d752148d | -9.86281 | -47.86979 | 2025-07-15 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5bf1649a-1b31-3d95-8685-cf51ff4f3ac2 | -3.58638 | -49.42822 | 2025-07-15 04:32:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0cf8dac2-36b2-3de2-9410-89e8ebea8889 | -7.3052 | -45.36258 | 2025-07-15 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e16a1c36-b5c9-3917-ad56-635cba52b72e | -9.7239 | -48.32679 | 2025-07-15 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 897171ed-7657-365b-b1a5-2865e0637360 | -6.16451 | -45.87646 | 2025-07-15 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README19.md)
