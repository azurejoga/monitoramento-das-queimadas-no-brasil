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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22dc9945-39b9-30bd-9a83-7958a754f46b | -12.47273 | -46.88114 | 2025-10-30 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 56a50548-fd31-34c2-9762-83857ae1fa2b | -12.60752 | -43.19951 | 2025-10-30 04:06:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31f8f2a9-9080-377b-9d9e-aeb27054acda | -11.11857 | -42.25809 | 2025-10-30 04:06:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 028eccff-1678-3467-87d0-3dfe96c5b1db | -13.35943 | -43.09096 | 2025-10-30 04:06:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 9ed039e5-08e9-3058-b892-aa2d03dedcdc | -13.58023 | -47.34679 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c6435f6-dbc0-3444-98a6-5e46ba4c3f9a | -12.48041 | -50.57435 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 779fcada-a4e2-39c8-894b-d27dd748d550 | -12.48105 | -50.57103 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3d2ea490-3118-3b1e-b779-ec22d289db29 | -9.84686 | -47.69289 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03c41643-44f5-356d-8ca8-d29ea0256d62 | -13.43683 | -42.98209 | 2025-10-30 04:06:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7ed9e5fe-e4b6-3870-adea-7195ef88e9a7 | -13.4374 | -47.37037 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8288c1d9-e0b1-34c8-9dc6-61bc21c52e1f | -13.58087 | -47.34328 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa559d26-f9e2-3ebf-98a4-7922051686dd | -10.27106 | -48.05656 | 2025-10-30 04:06:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65c580ce-6959-3f90-b7aa-75f7d2c3c58b | -11.84514 | -47.92795 | 2025-10-30 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7283e42c-d95b-3109-a71a-88be77109689 | -12.4745 | -50.57659 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ca4dc53e-2f03-3010-8586-ac5947fb99e9 | -10.97656 | -50.11782 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f264b38-10ab-3e10-ae0e-7bdaa976a918 | -10.75341 | -44.7448 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 918209f3-3bd4-3423-a5b4-7ec42e3eab01 | -10.76624 | -44.73725 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 254d2b33-f8c3-3615-aa3e-fa9ac134884a | -9.28861 | -48.42113 | 2025-10-30 04:06:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0d74c65-6b27-386f-a83a-5c734226326f | -10.27699 | -44.5664 | 2025-10-30 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08eebaa3-bdb1-3c7e-94e4-5adfad5f9236 | -12.50401 | -50.5654 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f09a291-2480-3e1e-a5d2-2b7aa759b987 | -9.91136 | -47.90956 | 2025-10-30 04:06:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 25325f32-7de7-3e41-ba08-afd1df8dc270 | -13.30084 | -47.6896 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9472ac0d-c91c-31ab-9d12-05f0626db639 | -12.47578 | -50.56995 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6e6373f8-7789-368c-bd52-87d08786e12e | -13.46952 | -47.99914 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 297d0864-4436-3251-86f1-38ad3511bb44 | -10.98424 | -47.87572 | 2025-10-30 04:06:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9315ffa3-fa4f-30ba-92e8-dcd396c6e51a | -9.31715 | -43.09543 | 2025-10-30 04:06:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8b34274c-59ae-33eb-8370-186e6bf980b8 | -10.2702 | -44.58374 | 2025-10-30 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bde58259-9e99-3770-9e88-01b6bbd92dd8 | -12.68399 | -46.30384 | 2025-10-30 04:06:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 298b0aaa-8bc8-3eac-99aa-cac56a3fcc5b | -12.9055 | -43.40864 | 2025-10-30 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a3db498c-ef97-3929-90b7-da769d438d90 | -10.64828 | -48.79876 | 2025-10-30 04:06:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2e3f56f-a4e7-3cb9-8b08-35ae82b3b476 | -8.9522 | -48.63478 | 2025-10-30 04:06:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9ae63c68-595b-34de-9335-ff45f7da5c0d | -10.2784 | -44.58061 | 2025-10-30 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1abdf97b-418f-34b5-85bd-85327d70e3b8 | -7.95397 | -46.76165 | 2025-10-30 04:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 39c319c7-1e8b-394c-918a-9a8adcbc3d93 | -12.51745 | -50.57111 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7638af1b-b684-33d9-a0e1-ccd55615edd3 | -12.81011 | -43.4509 | 2025-10-30 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65f1c0d0-c514-3228-82fa-098c89e75f15 | -8.7036 | -47.90986 | 2025-10-30 04:06:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 557c59c9-a038-3725-8779-dde19eba0f12 | -10.97717 | -50.11454 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fc962d7-eb58-354d-bcd0-8fdf9591ea18 | -8.8813 | -49.79274 | 2025-10-30 04:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3feae0a4-2d9f-35e1-bc3f-3405e7112924 | -10.617 | -44.12419 | 2025-10-30 04:06:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6664723b-1ba3-31e6-947a-f5dd4b191c77 | -13.03576 | -48.46222 | 2025-10-30 04:06:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba80f0e7-e769-32c8-b982-4a5b58ae604a | -13.27771 | -47.71848 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08fb6e84-b9ca-3d9f-955b-59569272d19a | -10.74436 | -44.7501 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 858d0114-e029-363a-9696-8c8d8bc1feca | -13.55758 | -47.13478 | 2025-10-30 04:06:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e2b1658-c328-3d03-8936-76dc1208855e | -12.29022 | -50.32665 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 563fdc6c-f47b-39a6-b0b9-6d7c4c0c87ea | -12.0419 | -47.81868 | 2025-10-30 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0de2c500-1e66-337e-ac42-26b2c1b92beb | -9.22071 | -45.59972 | 2025-10-30 04:06:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84d7c1b3-397c-376f-ac36-046a9f8a49bf | -12.49537 | -46.85005 | 2025-10-30 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3606a41-cda4-3b04-9577-b7b4fd858986 | -10.27917 | -44.57608 | 2025-10-30 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01a90427-4a08-3299-9476-a8d8224f52b2 | -12.36648 | -50.15106 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b6d9daaa-2d7f-30f0-b9cd-37afd031b8c2 | -13.82314 | -42.5122 | 2025-10-30 04:06:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3c09d5db-8d7d-3d06-a3c2-34b7509eef82 | -12.19102 | -46.70966 | 2025-10-30 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 189b232e-5f53-3eb8-b1bd-fab4ea6c1106 | -12.6175 | -44.24964 | 2025-10-30 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f198ba49-c83f-378d-af64-e8004b943e03 | -8.18166 | -44.47055 | 2025-10-30 04:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec3dbd2b-53ff-327e-8dcc-ee3b4a3f4f30 | -8.05296 | -45.17126 | 2025-10-30 04:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b0a22f5-f5e2-341c-a86f-c52c799a7dd3 | -8.2637 | -43.92735 | 2025-10-30 04:06:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be0155cb-de00-3442-a441-4b6a9ece3f29 | -12.14493 | -48.01127 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d435926-77da-3e0a-8367-50d4cd277ad5 | -10.97832 | -50.21752 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b1a7a9a-0a69-3fab-b4ca-f40f6bfa5899 | -12.31409 | -50.31481 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 607fc1b3-2d9b-3000-a05b-89b6287d5c15 | -9.60228 | -45.15524 | 2025-10-30 04:06:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3e2c5f5-d578-3677-b3d6-df174fa9d435 | -12.28747 | -50.31274 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dcee18cf-a733-37df-9ad2-742d0d91dcff | -9.60268 | -45.15268 | 2025-10-30 04:06:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e1b4fd5-b958-3db8-a69e-a5a23ba2bc0b | -10.76998 | -44.73783 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a298edf-c4ba-3399-985c-4f8f1b3898ec | -10.26726 | -44.57852 | 2025-10-30 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f009a90e-15c1-31cc-b5c4-6a1fefb90dbe | -8.05126 | -45.18139 | 2025-10-30 04:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 404d0082-a35c-3a50-8a1f-14871e129b07 | -13.61006 | -47.59242 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b85220b-fefb-3bc6-8c43-39827bec10f9 | -13.60594 | -43.56779 | 2025-10-30 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b72f74d-2bb3-37d5-b40c-7327a8ee8c4b | -10.8575 | -47.87366 | 2025-10-30 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2955a3da-13e4-3250-a539-1227a0ad936c | -9.49976 | -40.37712 | 2025-10-30 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 61128251-8b2f-3142-8fe5-fc646c0bf8e6 | -10.39006 | -37.44855 | 2025-10-30 04:06:00 | NPP-375D | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7a3b7712-e85f-3e11-a114-01634a79161c | -10.74445 | -44.75213 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45e298fa-de5b-37f0-a894-e1cac589a711 | -10.74519 | -44.74785 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 912618ce-5113-3bf4-9070-ee0ac48e6ab5 | -10.26355 | -44.5778 | 2025-10-30 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8eacb331-244b-301b-94f5-f624fa9f83a2 | -10.86016 | -47.62278 | 2025-10-30 04:06:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fce24f20-81cd-35eb-87e8-b374b304e9dc | -9.81558 | -47.5793 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0aed55e6-a3f9-32dc-afa1-5711d0b116d9 | -10.48667 | -45.04307 | 2025-10-30 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a554df2-1bf6-3c61-9759-42fbfa7d37b5 | -12.29542 | -50.32772 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a173e1ad-6c42-3d5c-8a00-f537f21f402e | -12.52206 | -50.5755 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 561e60da-4df0-3e90-b425-0ace0a71df65 | -14.38794 | -43.71875 | 2025-10-30 04:06:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d11e2e75-e808-3a5f-8af1-562fa138afe2 | -13.31767 | -47.47795 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b3d9bc3-0858-3ee5-a841-258a644af9b4 | -10.2328 | -47.63902 | 2025-10-30 04:06:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 69638164-45b4-3483-9bcf-2b580ec8f014 | -13.46434 | -48.00269 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 979dee80-65c4-38c2-85d9-96f6dd88bee0 | -12.29185 | -48.0797 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d59b465d-8390-374e-8ee3-9883b04ddf6e | -12.31053 | -48.05333 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 16ff9e40-b503-35b0-adf5-6a0e28a7fd51 | -7.96008 | -46.72665 | 2025-10-30 04:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e7cf52df-b5c4-367d-9321-38d6c0916d4c | -12.50928 | -50.56649 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fcc3bf10-6c90-3083-bf6f-95401752a9a3 | -9.90942 | -44.90557 | 2025-10-30 04:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d1ba831-db8c-362b-86bd-a94d1e912c92 | -10.27392 | -44.58443 | 2025-10-30 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| edf80a2f-0b21-3b4c-90a2-19554f3f166d | -12.81075 | -43.44709 | 2025-10-30 04:06:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdaf1758-f8a2-3953-8584-599a1d07b534 | -12.61681 | -44.25371 | 2025-10-30 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac756b68-f7ce-3cfd-b6f8-6f3cfcf6890a | -12.30308 | -50.25942 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0522496a-e534-33b8-a42d-273488fb3649 | -10.86097 | -47.6182 | 2025-10-30 04:06:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24c9e962-af9a-3700-8509-17718bdece15 | -12.50865 | -50.56981 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8b876900-da34-33aa-b172-96495ef429d9 | -13.41432 | -43.74855 | 2025-10-30 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b900ba02-0f0f-3a75-b8cb-a664db9ac920 | -8.32745 | -47.92802 | 2025-10-30 04:06:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 03f97cd5-77a0-39d0-ad9c-ccb247c78dac | -10.75502 | -44.73547 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f586e280-feba-3ffc-b30c-a5a1f5697f0e | -12.48231 | -50.5644 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89e42407-3697-303b-953b-51897f67b699 | -12.30064 | -50.27217 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d570565-d677-39c3-b947-1b362427fb4a | -12.8556 | -48.62486 | 2025-10-30 04:06:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 970d6f26-c68e-3053-86e3-c0037844fb03 | -8.2915 | -49.31679 | 2025-10-30 04:06:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12ce4406-885c-3b6e-827c-2a96a21f3ca2 | -13.02843 | -48.80846 | 2025-10-30 04:06:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README35.md)
