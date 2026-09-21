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

## Dados Diários - Página 175

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d7fd025-708b-31e0-ade2-2d6d78a85b25 | -6.17697 | -47.72153 | 2026-09-21 16:03:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d98af1d5-70a6-39fd-bf09-bb02ded1ca4a | -5.74792 | -43.7189 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 53bd07c9-bbd9-3044-87f7-558883c93c27 | -3.33883 | -42.76997 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 282.8 |
| 1e9b7cce-98f8-3869-8131-d94b4a218a7a | -6.49762 | -45.88417 | 2026-09-21 16:03:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| ee7658eb-4e82-3af6-8385-0987a6bd9472 | -6.2305 | -45.44328 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0c128bd7-aaa4-35ab-af49-862fccce31d0 | -2.99582 | -44.30745 | 2026-09-21 16:03:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7e9a912d-6e80-36b7-a509-86470d2c2d0e | -8.41475 | -45.86673 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 123.3 |
| d93bc49b-7005-3e2c-8604-492b0ca8d007 | -6.18401 | -47.61124 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0037981f-4032-3cb9-aaa5-582e8f5a2f5d | -7.57854 | -45.43521 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bfb439f5-3894-3773-9ede-91e3dfde633b | -8.49765 | -47.02671 | 2026-09-21 16:03:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 64eba35b-a7a2-3b56-bbee-8289aec837b9 | -4.98821 | -43.05495 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2afb14c5-0f17-33d1-ad1d-9a0759bd67fe | -7.50949 | -46.23441 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| b37916c2-458b-39ae-94e4-f299c366e4b5 | -6.88353 | -41.70555 | 2026-09-21 16:03:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 10da3aea-7e42-37f0-b3a2-338664d78043 | -6.5512 | -44.85211 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 0c474902-f8e6-3ddb-ba3c-a5d29d6c774d | -6.14745 | -43.84682 | 2026-09-21 16:03:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 54319814-9d90-3b11-a1f2-05e97ba9c2db | -7.29526 | -46.77777 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e497804b-6ee4-371c-8f79-e05fda8b02f9 | -7.11926 | -43.07777 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| e1c02704-506a-345c-b5ab-446992eb3706 | -8.45248 | -48.45501 | 2026-09-21 16:03:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d4e82ba0-c64e-30c3-9147-0282ca1a0bc2 | -6.85013 | -43.71232 | 2026-09-21 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 7f25aef2-7004-3885-b928-f3d316c8a602 | -3.39487 | -50.44199 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 598b991b-7a50-3365-aab9-e18df6433752 | -6.56252 | -45.82813 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 16ac1620-4b96-35d2-bb6b-3f57e302c09f | -5.66267 | -45.48727 | 2026-09-21 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| b30979f4-c248-39a1-89f0-628f0ddbff44 | -6.23806 | -47.59159 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3e883a0b-26ab-388c-ae74-538d54aec673 | -6.55959 | -45.56401 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| b8a0318e-b915-342d-adfe-2dc568f2834d | -4.35216 | -44.31913 | 2026-09-21 16:03:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1d10c907-4b82-3604-a2cb-f549a7e1f706 | -3.38078 | -42.96922 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| dd076a43-953b-3854-8ac5-338a459f570e | -3.1624 | -50.82053 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1a1c296d-22fc-37df-b446-8710c575ef39 | -5.43908 | -47.60907 | 2026-09-21 16:03:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 186013c7-ce6d-3176-83bc-bd1f856e4d0c | -3.72026 | -44.72451 | 2026-09-21 16:03:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e66e5763-f7a8-3abc-bc16-bd496f8d7cb0 | -6.15591 | -44.18683 | 2026-09-21 16:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6af309f4-5377-3c7a-9bf4-275b2d1114ef | -5.57414 | -45.29395 | 2026-09-21 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 83bc7b82-79c3-3669-b051-69e35c96f861 | -3.73108 | -39.35382 | 2026-09-21 16:03:00 | NOAA-21 | UMIRIM | CEARÁ | Brasil | 2313757 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 0b865705-04b2-3679-8755-2410b4c27205 | -7.74938 | -46.72872 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 053d4f5e-de80-31d2-be90-770f229f1a87 | -6.93469 | -42.89718 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| b5a2e1d1-2149-3604-8088-a630568aa2d5 | -6.22384 | -45.92767 | 2026-09-21 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2bb32b45-45c9-3378-83d2-03f2eb5cf8e5 | -7.88925 | -44.84098 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8e05ad4d-0328-350a-a95b-eedd4956d933 | -6.54011 | -44.87213 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1d8111c7-eb12-3fbd-8296-1589de92fa17 | -8.34037 | -47.54168 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b8719ff4-5673-3fa7-b254-6308d2baf427 | -8.39446 | -47.1789 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ab8d0678-64d6-3538-b883-db9e89c15d51 | -8.80362 | -48.7393 | 2026-09-21 16:03:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 17.1 |
| c1058555-7401-3dd7-b17b-0aeeb7f883f7 | -6.37137 | -44.90066 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b4103f63-545f-3e02-89f8-cf2c1176c4bc | -8.34253 | -50.7558 | 2026-09-21 16:03:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| bc611898-b42b-3204-a0f3-ec9b83b3dd94 | -7.56528 | -42.65545 | 2026-09-21 16:03:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 3de6b626-f3b2-3b08-b19e-573154085be5 | -7.02497 | -42.08696 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| de02051d-4e2e-34f6-97d3-4b300598b476 | -7.88282 | -48.9282 | 2026-09-21 16:03:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 6b587a84-6df5-3cdb-8cad-e997e36d0c84 | -3.57373 | -43.47184 | 2026-09-21 16:03:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| b7389916-e57d-332a-b259-9c3be5814486 | -7.9782 | -44.07521 | 2026-09-21 16:03:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 169b3f75-35d0-3ca8-9d9c-50d08d6a3a21 | -7.59348 | -43.43777 | 2026-09-21 16:03:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5def05d6-6dcc-35f9-8d45-e2eceb967a71 | -5.5405 | -47.42979 | 2026-09-21 16:03:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fecc939e-9515-39e0-b9f8-453185960ade | -4.4702 | -38.28958 | 2026-09-21 16:03:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 6f6d4d26-0dac-375c-9954-821122a279d3 | -3.41424 | -43.11108 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 03b0e294-6bef-32c6-8752-2fc650462854 | -7.82851 | -45.26149 | 2026-09-21 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 91c103e2-4493-3506-b35b-e882873886fe | -8.79821 | -48.75256 | 2026-09-21 16:03:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a86e5770-aa9d-3d1b-8e29-17ff7ca406c6 | -5.9827 | -45.07107 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 33767e3e-86b8-35f9-913f-b9251f3fe23b | -8.4519 | -48.45057 | 2026-09-21 16:03:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fdcf904c-00fe-3ed8-b7cc-0673335dc680 | -6.73192 | -44.29034 | 2026-09-21 16:03:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 32ea971f-a372-3b84-9858-7ce0dd61a149 | -8.81049 | -48.75142 | 2026-09-21 16:03:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 75.2 |
| e213c910-8c2e-3705-97d9-c8b6efdf12a8 | -6.78115 | -43.90027 | 2026-09-21 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1a71df2a-d20e-3756-a364-d188cf25aff2 | -4.23099 | -51.23376 | 2026-09-21 16:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| d6ec140d-d657-3273-8d1e-b0958fb2add2 | -3.24617 | -42.79752 | 2026-09-21 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 16d37f45-1344-3124-a535-aa947139e025 | -5.61713 | -43.39382 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e34b3d26-9d02-30d6-a3f1-b7e458b3f9e4 | -3.34332 | -42.77402 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 494d33dd-3090-3606-9995-c0c52ef075b6 | -7.78724 | -44.81361 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 64f73ecc-894b-357b-a1c7-05d766463794 | -7.41132 | -44.70388 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9109f0f1-9d1c-35aa-aa48-a596b6991c17 | -2.6802 | -49.0217 | 2026-09-21 16:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2bff35c5-86fc-36b1-a517-a7fb72314f66 | -6.50251 | -45.88354 | 2026-09-21 16:03:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 863ab6f6-b0c1-33cb-8cd2-5d3f07f9e6cd | -7.57515 | -45.4463 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 5866c3bb-8099-39da-8e5f-a9c9b7e3861e | -6.56913 | -45.56245 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 7ccf8eb0-cc06-3deb-80cf-60cd22dab3bd | -7.54123 | -44.92535 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 899aa938-b6c3-339b-942f-1a3c22482385 | -6.5362 | -44.87738 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 96fcd1c7-cc1b-391f-80f3-9c7c824dc781 | -6.22698 | -45.43182 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 21e47a92-0dae-3233-858f-de859eb0108f | -7.51752 | -46.21775 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f24cb271-8af0-3c4f-a458-6b404266d859 | -6.80682 | -47.88598 | 2026-09-21 16:03:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 10e8419c-20dc-33bc-bc1d-aeab5dff8223 | -5.30023 | -45.75595 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 5702f9c2-6715-3b79-be6e-f23a6268a23b | -3.8444 | -40.60107 | 2026-09-21 16:03:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 1e815a46-acef-3e0f-a2fa-3e4c55993240 | -5.22761 | -48.06631 | 2026-09-21 16:03:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 136e54e1-4174-3282-8e24-f1a3146e88a5 | -7.39725 | -46.16388 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ed7a7ac7-f673-3a9a-82ca-08dd3dc859b0 | -3.6689 | -40.55484 | 2026-09-21 16:03:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 1333a0bb-fb20-324c-bdb2-a54cdb5ba1d5 | -1.14445 | -46.78529 | 2026-09-21 16:03:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 97dd4ad0-2fac-3474-8d40-c2b954e0bad5 | -8.3077 | -45.98141 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 6a859659-525b-3c26-94ae-fbe5343373bc | -3.03271 | -50.43747 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f0fc5647-8936-3b96-a21b-0b9a76ccd4f9 | -7.573 | -45.43065 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b2fa97a6-5a7f-36bd-8685-f6040ffadbd5 | -6.90515 | -42.91946 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 9132c988-b947-3107-869f-3ba07beb69a6 | -2.68253 | -49.02235 | 2026-09-21 16:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 740e4427-de2e-3563-835d-5391076dc592 | -3.61448 | -43.13133 | 2026-09-21 16:03:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7f188e32-d22c-321d-9296-4cee9078567b | -4.28832 | -48.62474 | 2026-09-21 16:03:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cfebc2eb-7b16-358d-952d-4c60611b0b92 | -7.11952 | -43.72326 | 2026-09-21 16:03:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f01f445-d732-324e-ad56-cd619b223b1b | -6.21127 | -45.35639 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 27bf9866-b558-3bc0-9c03-c0713fc4a3eb | -7.09251 | -42.07367 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 999abaf5-d467-34db-9299-d4c63c480701 | -5.14468 | -42.70044 | 2026-09-21 16:03:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5416b3a1-3bae-3103-a65f-5756855a1300 | -5.81743 | -43.86528 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 15a59509-fc59-3d88-bdf2-79f22119c5ce | -6.15536 | -44.18281 | 2026-09-21 16:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 05f966f1-b62c-3bb5-8ff4-01722b418b52 | -3.64495 | -40.58105 | 2026-09-21 16:03:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| de2a231d-59b4-3903-8311-e897fe248042 | -6.50172 | -45.87805 | 2026-09-21 16:03:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 15f9277b-2c66-3e9a-8248-9e4a8b6e4332 | -6.85363 | -45.53296 | 2026-09-21 16:03:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 96ff22b0-6b37-34c0-871a-d16477fa346f | -7.75754 | -44.83074 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f0d75510-cfe6-39af-acbf-924f535ab865 | -7.34448 | -44.45977 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 75861707-f7cf-3181-8da1-07173266e405 | -7.8831 | -48.92606 | 2026-09-21 16:03:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 12.5 |
| ef4d7f48-0b3a-3098-9aee-b1cfc7183e1c | -5.40127 | -45.70763 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 592145aa-9181-3edc-ad9a-d42012bb8b86 | -8.43946 | -45.82351 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |


[Clique aqui para ver as próximas entradas](README176.md)
