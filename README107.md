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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cee75c4b-08fd-315c-9dcb-8081e62f6e1c | -11.162 | -47.94849 | 2025-10-07 05:53:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9ca2987f-8486-32f5-9161-b3efbb75c744 | -6.59139 | -44.61601 | 2025-10-07 05:53:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d370d00f-371f-3454-be12-facd4a43d97b | -10.58028 | -51.47541 | 2025-10-07 05:53:00 | AQUA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 715f0d41-1f36-3215-8661-889c09ee361a | -13.0777 | -47.82994 | 2025-10-07 05:53:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e1a06d09-c110-3dfa-bae8-96e80debb2df | -6.72024 | -42.80257 | 2025-10-07 05:53:00 | AQUA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 593bfe22-b44a-3e5a-86a1-8a6d2cbf7e1a | -8.85245 | -46.09145 | 2025-10-07 05:53:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3a79e1f3-84f8-3d62-b44a-48b8000d1562 | -10.92123 | -47.07219 | 2025-10-07 05:53:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 994cc51b-dc65-35cf-9d3b-12e6b5400c66 | -6.64578 | -41.97713 | 2025-10-07 05:53:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| e7e32d41-d2f3-356c-8dd1-d7d8589a5991 | -10.89324 | -47.13467 | 2025-10-07 05:53:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a7a91979-dca1-3de0-9bbe-f3175310d824 | -10.18548 | -45.53456 | 2025-10-07 05:53:00 | AQUA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| ec51d7db-8daf-3ab9-b606-c659b928911f | -13.07017 | -47.87801 | 2025-10-07 05:53:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 90de1f10-271c-3539-86f1-aba695c83ef1 | -8.2068 | -44.17923 | 2025-10-07 05:53:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 22e8faeb-5f04-31d4-a068-fa4e099b3d2a | -6.12883 | -44.6159 | 2025-10-07 05:53:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 69c2c54a-f1ad-37d6-97ae-d88f75121ab9 | -10.92338 | -47.11712 | 2025-10-07 05:53:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 67d8bf47-ecdd-3ab9-b697-858bf11d6a80 | -11.80899 | -45.04869 | 2025-10-07 05:53:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6257e373-49e7-3326-8b10-6ee8babdd3aa | -11.77918 | -45.12833 | 2025-10-07 05:53:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 574da120-559d-3322-973d-e74bd55feb37 | -8.65839 | -46.2772 | 2025-10-07 05:53:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 15ad09ab-a482-3759-9bf2-f3f5ea8d1f7a | -13.0928 | -47.85219 | 2025-10-07 05:53:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| db737e73-6ffe-39ee-8b70-fbb49e2aef81 | -8.65699 | -46.28629 | 2025-10-07 05:53:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 37.0 |
| f7183d63-158c-3e5e-a4e9-1f3f60815980 | -5.97791 | -43.51329 | 2025-10-07 05:53:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8df9df6c-2233-3e94-abb3-c120712812b3 | -5.71609 | -44.82826 | 2025-10-07 05:53:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 67aa28c8-4a16-3ae8-ae21-d6dcd60fd687 | -11.9411 | -46.4453 | 2025-10-07 05:53:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c2d5e8c7-6001-30a5-8b7b-095135322407 | -8.1855 | -50.29927 | 2025-10-07 05:53:00 | AQUA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 55a22de1-5e85-3f7f-8bf9-720ad33828d8 | -7.72048 | -42.40091 | 2025-10-07 05:53:00 | AQUA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 8cc8839b-36f5-3011-a24a-b2509adb5a46 | -10.89468 | -47.12529 | 2025-10-07 05:53:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f5948844-43c6-363b-a737-06d6dcc58dd0 | -10.41817 | -50.28618 | 2025-10-07 05:53:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8b7aa1bd-a3f0-3c32-ad6b-4ef7ea5b9d1d | -6.13827 | -42.67173 | 2025-10-07 05:53:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| fb91a43a-97f6-3fe6-aded-0e01c6e5294c | -10.92265 | -47.06291 | 2025-10-07 05:53:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 407607a8-cac3-3978-9c1e-d433efedbcc6 | -8.18059 | -43.3483 | 2025-10-07 05:53:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 3cc4636a-3db6-3e05-92c4-4c64a15e2eec | -5.95923 | -42.76429 | 2025-10-07 05:53:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 5c2e3c3f-a770-390d-87e3-52794cb36d29 | -10.94614 | -51.13458 | 2025-10-07 05:53:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a38622dd-2afb-35f4-8e8a-c7569481e6c6 | -10.42674 | -50.30224 | 2025-10-07 05:53:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| cc9ad81a-19d4-3955-bc17-18d94954d54b | -6.98665 | -42.87 | 2025-10-07 05:53:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.4 |
| 1c340794-39dc-3eef-938f-ef537dab0d5d | -10.8103 | -48.59675 | 2025-10-07 05:53:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 345123e1-d1b3-33d1-a01b-99c22ccc2a4a | -10.86523 | -47.96746 | 2025-10-07 05:53:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d8dada72-232d-39dc-8d84-3b5e600e82e5 | -10.92483 | -47.10785 | 2025-10-07 05:53:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 434103f9-a5f6-3868-a174-848b6470f651 | -10.4377 | -50.30407 | 2025-10-07 05:53:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 3a903f1c-2b2c-316e-a85c-e8e0bddba922 | -6.9881 | -42.86009 | 2025-10-07 05:53:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| f89645aa-955d-3420-b409-4c18c6be75dc | -6.25327 | -43.27889 | 2025-10-07 05:53:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 9929dcad-2ffc-360e-bcde-57631a3a52de | -10.44629 | -50.32018 | 2025-10-07 05:53:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7a4dc1ee-b39b-334e-8d6f-b02b034ef04e | -8.49369 | -46.32339 | 2025-10-07 05:53:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 83ca6b1e-eb8d-32a9-8dbc-00d41bb57e8e | -10.41118 | -45.38135 | 2025-10-07 05:53:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ceb0238a-13e6-3e93-b3cd-68767d7c0d7e | -10.25618 | -44.36884 | 2025-10-07 05:53:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4ae194b4-42a1-3976-ad74-b47524856c93 | -7.68053 | -42.40584 | 2025-10-07 05:53:00 | AQUA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 9f307b6d-339e-384a-b68a-837f2018da03 | -6.36204 | -42.85624 | 2025-10-07 05:53:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 3e31284b-b449-3a91-8d7c-d45d9da8c58b | -12.61767 | -44.75327 | 2025-10-07 05:53:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c1b06c9b-8292-3280-8ad1-972d61cc52fb | -10.58693 | -51.46616 | 2025-10-07 05:53:00 | AQUA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 01a61941-3522-3188-8649-57af05fc425d | -10.4154 | -50.29366 | 2025-10-07 05:53:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 24de34bc-a9e7-3750-86d7-560a6de53b35 | -10.92051 | -51.15807 | 2025-10-07 05:53:00 | AQUA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 26.8 |
| ef9dea56-27b9-3f99-b4bc-8eae56ef79ef | -10.58301 | -51.45895 | 2025-10-07 05:53:00 | AQUA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 88e37cfa-2c3d-3570-9d8a-3f3282be2bd2 | -11.68409 | -45.27411 | 2025-10-07 05:53:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 04929c71-c007-3688-a85d-9eefdc082d43 | -6.70232 | -42.86042 | 2025-10-07 05:53:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| cbc9a511-de2b-3730-a1ce-3b5dbbe3922d | -11.82895 | -45.09838 | 2025-10-07 05:53:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a72d0743-e4bc-37b8-9880-59ef823e2d4c | -10.93181 | -51.14874 | 2025-10-07 05:53:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.1 |
| f364bcfb-e5f5-3c56-97ef-c13fa3527309 | -6.9852 | -42.87991 | 2025-10-07 05:53:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| c0530757-d076-3a92-b458-81e0afb093c2 | -10.41578 | -50.30041 | 2025-10-07 05:53:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 3ac151fb-b0db-3aeb-bded-5fcedf0d04dd | -11.82762 | -45.10742 | 2025-10-07 05:53:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3e8b3c7e-c73f-3743-a7b6-48e26f124337 | -8.4923 | -46.33246 | 2025-10-07 05:53:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 2bab663a-06b1-3317-a751-4bff357ae077 | -11.15539 | -47.95104 | 2025-10-07 05:53:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a36243d4-22a9-3467-8e8d-7c4706e20791 | -12.02221 | -47.77938 | 2025-10-07 05:53:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9d4b5882-111e-37b7-be67-ad854e35ca77 | -11.67908 | -46.34096 | 2025-10-07 05:53:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c59f14f8-3cfa-3f74-bb4c-6c055aadc8c7 | -6.23517 | -43.27619 | 2025-10-07 05:53:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 3e194561-5936-3c6d-9654-33d7bd239de9 | -5.74863 | -44.9832 | 2025-10-07 05:53:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a13e236f-d072-3d48-a43b-9d6904b1cf53 | -13.09132 | -47.86167 | 2025-10-07 05:53:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3d2a64d0-da15-3023-80b2-f4c90d3f5aae | -13.54112 | -42.9988 | 2025-10-07 05:53:00 | AQUA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 21.5 |
| de31416e-53ef-3d5c-89ee-b06974e745ba | -6.59007 | -44.62482 | 2025-10-07 05:53:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| ff5b8527-dc83-30fd-8a0f-bc572e2d19d9 | -10.91552 | -47.10942 | 2025-10-07 05:53:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 28004737-6fdb-3ad9-b9d8-75aae6eac2bb | -6.21629 | -44.33218 | 2025-10-07 05:53:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b7c09e7c-cfcb-377c-9ca4-41939137bd35 | -7.01834 | -42.78331 | 2025-10-07 05:53:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| a0a6967e-f876-3348-9fbe-7babb238dddc | -10.94887 | -51.11847 | 2025-10-07 05:53:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |
| db42bfb4-7d18-3065-a549-ca9d121762de | -13.06873 | -47.8872 | 2025-10-07 05:53:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 42301d2b-e596-31fe-89a7-b03a1bcba1ae | -11.84697 | -44.91368 | 2025-10-07 05:53:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a324f576-dff0-36ff-aa5f-42fb242e522c | -10.40985 | -45.39022 | 2025-10-07 05:53:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a7dca0b1-258a-3559-81a5-1f410c9b0d9b | -10.43532 | -50.31835 | 2025-10-07 05:53:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 3a4874a6-5077-35d3-ac09-45fe06e9bc7e | -7.64948 | -43.89263 | 2025-10-07 05:53:00 | AQUA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 575c3298-5960-36e5-8774-8b29d7810096 | -8.54317 | -46.23802 | 2025-10-07 05:53:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 90d5b690-65b0-3f25-822a-925f74f1a3b9 | -11.12176 | -47.20846 | 2025-10-07 05:53:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c64f828f-924b-336a-b4fc-c9d6cec358af | -8.6481 | -46.28497 | 2025-10-07 05:53:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 88571bf3-61fa-3099-85e3-ff3b32d51bf7 | -11.12032 | -47.21771 | 2025-10-07 05:53:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 419d4193-6bcd-39bd-9a27-3a1674666f9e | -6.25463 | -43.26956 | 2025-10-07 05:53:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 57bb17b2-45c3-3700-a266-c6767cb2aa41 | -16.32056 | -47.9081 | 2025-10-07 05:55:00 | AQUA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7180ee72-22e8-3a07-a136-7af9d496bb40 | -21.43311 | -46.67614 | 2025-10-07 05:55:00 | AQUA_M-M | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| ca55a50f-7f47-3dbb-9152-223d74d1bbcd | -14.64886 | -48.36565 | 2025-10-07 05:55:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 32e29503-a32b-3c8e-9ec6-79edab6e1b75 | -15.58308 | -52.54845 | 2025-10-07 05:55:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 30.7 |
| abe0d3d1-d347-3458-bdb6-1940a59037a3 | -20.12214 | -44.40825 | 2025-10-07 05:55:00 | AQUA_M-M | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 689e4042-5eca-3e66-ab1a-9550d67ba1df | -14.92059 | -51.41098 | 2025-10-07 05:55:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 8a20cf30-77e5-3a7d-b3d2-02554537b1c7 | -15.98712 | -50.93468 | 2025-10-07 05:55:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 315bf208-9aae-3593-81f1-9d2c3f116a5b | -14.93155 | -51.41296 | 2025-10-07 05:55:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 44.2 |
| dd784f1f-1067-3412-a6e1-f18ced853a09 | -14.73837 | -46.03107 | 2025-10-07 05:55:00 | AQUA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 0e07248c-8f72-3f1d-9ed5-e5672db287bd | -15.50299 | -47.92913 | 2025-10-07 05:55:00 | AQUA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9a20c510-679f-361a-934d-5ef5ec6a1e2e | -18.01552 | -44.96481 | 2025-10-07 05:55:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c51c8098-ca9e-3c80-a2ca-ed8504b853d8 | -18.28771 | -45.45516 | 2025-10-07 05:55:00 | AQUA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0ef085bf-c0cd-3f91-86a2-dd318000b96f | -17.98288 | -44.99242 | 2025-10-07 05:55:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7d37d4bf-5476-39e1-ae67-79dbb4d39eec | -12.88876 | -54.74974 | 2025-10-07 05:55:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| f415102d-0476-381e-88f6-8b907bd8048e | -17.34344 | -46.83784 | 2025-10-07 05:55:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7c09b162-a14d-3616-9056-9bb9f76d904e | -15.27405 | -46.3372 | 2025-10-07 05:55:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 2a8e3d99-a2bf-39fa-95f0-7b2ec624ee54 | -13.33417 | -48.02736 | 2025-10-07 05:55:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b66b6f43-1833-340a-a948-20f46ef9af5b | -20.08062 | -49.58194 | 2025-10-07 05:55:00 | AQUA_M-M | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| be1864db-942d-3e74-bb43-fd98719b29e9 | -15.59581 | -47.26448 | 2025-10-07 05:55:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 23e85a50-ccee-3600-b806-2c6aa7ebe750 | -14.93546 | -46.80394 | 2025-10-07 05:55:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |


[Clique aqui para ver as próximas entradas](README108.md)
