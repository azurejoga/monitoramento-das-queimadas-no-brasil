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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6388c004-f8c4-3475-b42c-9fc66abd3e98 | -16.29612 | -45.24276 | 2025-10-04 03:53:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96ac43dc-1585-3b04-b3c5-cc3210c0b257 | -12.092 | -45.15181 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e4591ea-36df-32c7-b2af-48388741c9d0 | -14.20336 | -46.07431 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4063fc35-5ff1-3d6e-bdb0-cdfefe7a89fc | -16.75607 | -43.96214 | 2025-10-04 03:53:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 020f1ed8-404b-3dbb-97af-b3fb12762265 | -13.1355 | -47.82977 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d486068f-10a7-3fea-a94a-1ac84565aee3 | -13.13369 | -47.81077 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8de121e-6d49-3b85-984d-bc71c9e72a1c | -11.80488 | -45.02588 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55979a7a-04a7-3c69-ae0e-f5dc4aac0263 | -13.32104 | -47.18317 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43747a5a-c387-312d-8e20-03b2096eeef1 | -15.95851 | -43.32877 | 2025-10-04 03:53:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 01abab2b-52c5-3401-9f74-598038255999 | -13.96937 | -48.12095 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a00fa78b-2aee-3e7d-a1fb-fd6f64b85cac | -17.07872 | -46.25277 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b9efa92-8206-39be-af7e-c96f17fe4afd | -14.89507 | -48.34874 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1376989b-6b6d-3588-aa48-b975a2c4cd44 | -13.51974 | -47.24498 | 2025-10-04 03:53:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5af6632-15bb-32e3-aafa-bf44fa4629c5 | -12.59281 | -49.88932 | 2025-10-04 03:53:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00add026-6600-3be1-923a-bc83b5baaeb4 | -13.31606 | -47.18135 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8dae3d75-110c-3b3a-b755-2a4aa3bc143f | -17.07552 | -43.36174 | 2025-10-04 03:53:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eba35da8-a20f-3f4c-8e56-1121d31e4f4f | -13.74436 | -48.05384 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b86903d-048f-3fdf-a5de-2d37058338e2 | -12.72565 | -48.55938 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 263be14f-3801-3c07-a7e2-d6ebc33064c9 | -15.03104 | -49.44947 | 2025-10-04 03:53:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f580267-7f65-307d-8a71-d5c5eb94182d | -13.25035 | -47.24521 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0c5d7009-854a-30a2-ac6c-29699ec078d2 | -13.32674 | -47.62846 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 89a89899-8a95-39ed-9d26-3918a3fc630d | -11.78219 | -46.81908 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d30d212c-7478-371f-9b60-b2ff286a7585 | -12.86492 | -43.33443 | 2025-10-04 03:53:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9fbb9fc-3733-3282-9310-9fd82d154555 | -13.33232 | -50.94086 | 2025-10-04 03:53:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8292840b-2f12-3814-80c4-e70479cdd107 | -12.52917 | -45.98585 | 2025-10-04 03:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 258b35ac-7e23-3cb3-b4a7-83f06289c6a0 | -15.595 | -52.46664 | 2025-10-04 03:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4118f0bf-3977-313b-bfca-e3c41aa32081 | -14.43498 | -46.15335 | 2025-10-04 03:53:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa5d25a6-50af-3f41-8c8a-8d2d8b27f7cf | -16.36194 | -49.40232 | 2025-10-04 03:53:00 | NPP-375D | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7852894a-c518-32ec-898c-9151abb5d5ec | -15.16242 | -44.0721 | 2025-10-04 03:53:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0f35008-d07a-3405-94ee-dedb93c4fa55 | -12.80652 | -46.85607 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d71bc94-5cdb-3fc6-8858-091cf70e6416 | -13.57629 | -48.18338 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 55b29620-45ba-33a2-b1e4-b2c03cf43e46 | -15.72968 | -46.27944 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8450543e-45be-3bc2-9a4b-acdea840b417 | -15.72405 | -46.28377 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c0c8fc7b-190e-3898-b4f8-d6c8c4316f2b | -13.32702 | -48.09477 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b06028c3-a6de-34a1-be64-75b1e5c3a651 | -13.29398 | -47.8255 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 460848e9-b35c-3a04-81ca-e5671f0a26bf | -16.02449 | -44.28505 | 2025-10-04 03:53:00 | NPP-375D | JAPONVAR | MINAS GERAIS | Brasil | 3135357 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 475f49c2-4fea-3db3-8381-18114c670228 | -13.16313 | -44.63702 | 2025-10-04 03:53:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dca2cd6d-c8b5-37a9-bc03-4711800b7cae | -13.1194 | -47.8547 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 643cf7ef-2875-3bd7-9f14-4ead7a2f712f | -15.26575 | -44.12179 | 2025-10-04 03:53:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 665b861d-4c6e-37a3-a17b-746ab1dc7892 | -12.59403 | -47.00465 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 651dc87a-c9e3-3732-9b66-796bc4bb2525 | -15.32306 | -46.37572 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e084400-e27a-3e48-8e2e-0694a8df9ce4 | -13.73135 | -47.9239 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f7d68e7-64c8-37dd-848c-918927b11de2 | -14.29511 | -45.87693 | 2025-10-04 03:53:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96390d98-85bb-357a-bf12-3bce2a7ef6bc | -11.88576 | -45.02243 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95f97c95-42e2-33a1-8894-68966b91fd80 | -16.35663 | -43.41861 | 2025-10-04 03:53:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c979695-bb6b-3b0b-94c6-40c3fa3ec987 | -12.41469 | -45.16241 | 2025-10-04 03:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1dde4017-6b24-39d7-a4e2-9194763f677c | -11.92444 | -46.35706 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d6e2b66-c9e4-3d29-a4fc-b93741f6a5f2 | -14.28661 | -47.41858 | 2025-10-04 03:53:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| acc6c9c9-a940-3563-9d39-41ed98110171 | -17.08692 | -46.23491 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d25883ec-f04a-3339-9a1d-44278bc421cb | -14.44467 | -46.10278 | 2025-10-04 03:53:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c545b31a-c9c5-323f-941d-74382aeb4cb5 | -13.74986 | -48.05433 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 49f7d0ef-8835-3880-bd4f-51202ed78f82 | -11.49871 | -46.75434 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfb137ae-9b0d-3bb5-81d5-9ff7cc78469e | -11.69445 | -47.50549 | 2025-10-04 03:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2431daea-3aee-3d79-9d09-3981690aa99d | -13.33582 | -47.58154 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1bad39a3-36ce-36e9-91a9-5feb4a77cfe2 | -13.12967 | -47.9159 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9786fa02-e1b7-3e7d-b3ed-82484d3a7104 | -13.32537 | -47.19436 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95dfd906-79ff-3ae9-aee0-8d42f4097e3f | -11.80031 | -45.02507 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b04e59ed-9f14-38ea-9201-eb88e44e2a5d | -11.49353 | -46.75349 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 496d307f-8d7f-36fe-be80-c613e92bc2e2 | -11.9234 | -46.36258 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a61ba91d-8f3f-3edf-a552-3d4c847d9f32 | -11.66401 | -46.98913 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b736f262-949e-3515-83ec-ee56e3cbdaff | -13.69368 | -47.35234 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 129a7982-1101-3e65-af3a-d2d119a83dd9 | -16.36744 | -49.40389 | 2025-10-04 03:53:00 | NPP-375D | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4667a994-7903-3391-a22d-8db5eedd9bca | -15.59726 | -52.48873 | 2025-10-04 03:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3a3e106e-df0a-308c-98ab-30d2c3f4add5 | -13.69894 | -47.35284 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dc158b44-0e7b-37e2-beb4-4df5c7885468 | -15.72866 | -46.28475 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f61f1b3a-bd8e-383d-8a15-257dd56a38c4 | -13.60405 | -48.1862 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e1ab0d9-2509-32e7-8356-784f6e7d678c | -11.90964 | -46.75256 | 2025-10-04 03:53:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd0514ba-8478-33e7-a102-a4992f73bf48 | -14.92639 | -46.86397 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5c12f3d7-8da1-341e-a9f7-c21e6d8a74c4 | -14.92085 | -46.88553 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 24455f73-ad70-36a8-9ed9-d67cb9708ea9 | -12.72471 | -48.5738 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9023769-0edf-3e01-a655-3d062f5a4e18 | -12.03768 | -45.19284 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b390d790-d45c-3d06-b483-4219fc26b197 | -13.1397 | -47.80855 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fc7385b7-04a3-3d73-a2b6-9e0f259d9cec | -12.04228 | -45.1937 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3d00cfa-9035-3683-bb0c-8cc7110d45f8 | -16.01725 | -50.94071 | 2025-10-04 03:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c1739506-4dd7-3503-8e31-eb3477bedf8f | -16.03054 | -50.939 | 2025-10-04 03:53:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a9aa0e33-9744-3808-b2e6-6ed635856092 | -12.59573 | -49.88423 | 2025-10-04 03:53:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 242cabbb-704c-35f0-8d79-d0f798c272ed | -14.22083 | -44.80115 | 2025-10-04 03:53:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1d40b59-88a4-386b-8408-f4453eca4bc7 | -14.68393 | -48.26906 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0d11465-4bf5-350b-b3a7-5b545b79ea67 | -12.22219 | -43.76839 | 2025-10-04 03:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8707cc6-6206-381f-b576-30fbb0ac5c1b | -13.81772 | -43.17595 | 2025-10-04 03:53:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 31b75bbc-7149-330f-857d-b5dda48e5b57 | -15.37851 | -47.95993 | 2025-10-04 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ecae4bef-488c-3d9a-ae56-ec38bcf0761b | -14.20418 | -46.65894 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf663806-8c4c-34ec-b963-672194bffe85 | -15.79663 | -46.25499 | 2025-10-04 03:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c06b99f-2be0-36d1-8043-97867e5e8536 | -11.70383 | -47.51487 | 2025-10-04 03:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 79dac7fd-7fee-39af-aa64-aa22acdc80a8 | -14.91488 | -46.89027 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8841f66a-14b0-3434-88af-0d96c84b04ff | -12.8485 | -46.85623 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 342daf91-a5fb-399c-bc3a-bc3f420b49c0 | -13.73604 | -47.92821 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2347aa5-2937-3d53-b17f-795b5a2f8745 | -13.09869 | -47.89449 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b5656dc-f9df-3f4e-a78a-e756e4c4d957 | -13.20931 | -47.8225 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d06ae5d-3bb1-3b7e-94aa-d3f1e4317a07 | -12.72073 | -48.55442 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9d64282-6740-3b02-bdc2-015bd900a522 | -14.86565 | -48.35594 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d906909d-5f16-3917-a8bd-dae76f9b6aea | -12.03416 | -45.21199 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 8a51412c-b3c5-3c4b-9003-05672e719313 | -13.33588 | -50.95784 | 2025-10-04 03:53:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 175aad2a-8c89-3604-ac69-a0bd7a524a67 | -14.94526 | -46.87108 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 267030e1-5645-34e4-85d2-df195765d3e7 | -14.66706 | -48.29729 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 3674448b-5e25-307d-809b-912cece75703 | -14.23961 | -46.09324 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 767c9072-af86-305a-879f-357398ee3258 | -12.83466 | -43.8078 | 2025-10-04 03:53:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 44abe6c1-e30d-3cc0-9efa-d321e93c4b63 | -13.89026 | -46.51377 | 2025-10-04 03:53:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 68a5b7be-8648-334e-a57a-af1ce1b82e0f | -16.07136 | -50.89962 | 2025-10-04 03:53:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9da02921-e650-32d7-b026-bb6d3cfb81c0 | -11.24692 | -47.79967 | 2025-10-04 03:53:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README44.md)
