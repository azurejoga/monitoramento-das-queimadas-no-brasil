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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 966ca1a5-364b-378f-ad9c-ead1a1937c04 | -13.3462 | -47.82895 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1ab56b3-e4a8-33f3-9e60-e5b9cb24ef38 | -12.84393 | -46.99156 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 91e16397-ba11-301e-afa7-f26e1f695eb9 | -8.87724 | -46.64088 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6d30f099-3936-3898-905b-9eb7a1678893 | -10.65591 | -48.54467 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 09c01d7a-2f1b-390d-be92-cb6b60338c16 | -11.67956 | -44.30125 | 2025-09-30 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71683ad2-50f1-3847-bd45-77e5b75fc0d7 | -10.62462 | -48.54047 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cbd4cc4-ac5b-368d-b513-df6fc7edfdf8 | -13.79526 | -47.87462 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7700d9aa-6f3f-32d1-a3b5-630c486a8363 | -13.80412 | -47.96824 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c02ee26e-b29d-3e26-8781-b3dc14038760 | -12.94557 | -46.75856 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8a39cb23-f938-305f-aae2-c5f8112045f0 | -9.24025 | -48.56208 | 2025-09-30 04:40:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1189fc42-cc37-30e6-bf8e-9275f4498082 | -9.06484 | -46.71437 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7fb67bdd-0463-3797-9584-39bd26ed0daf | -9.13071 | -47.64114 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f38cd686-6718-3bc4-812d-bd3d56e3f8b5 | -13.39286 | -48.06652 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0ebef802-078d-365d-bcd2-eec825bf8736 | -10.17833 | -52.57525 | 2025-09-30 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7bb3919-95e7-3614-a246-f4b047c430d6 | -11.65165 | -47.48659 | 2025-09-30 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8f6e602b-ff58-3d22-87d0-286b80492a97 | -11.25963 | -47.23253 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b4df7889-75a0-3ab6-8bce-ea72dee4629b | -8.14621 | -46.37117 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d386de70-ef70-32dc-b838-c881db235672 | -13.73232 | -48.68718 | 2025-09-30 04:40:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0154e4f9-9d84-3fdb-ad2e-e8056a03facb | -13.80836 | -47.96432 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a6cee76f-8b4c-3254-a401-7669e221966c | -13.7555 | -47.92076 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ca79bee8-3706-34b4-b80f-fa7eafb0f2d8 | -11.15501 | -54.12765 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 9a8e262e-5e90-3674-8d03-27f5c9b93514 | -9.40046 | -46.56952 | 2025-09-30 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd0253fc-e3ed-3bcc-b35b-8376ac066e49 | -6.32537 | -53.17273 | 2025-09-30 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd832f65-dc54-35b3-a545-081f179f1e19 | -11.43379 | -55.03706 | 2025-09-30 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80ec254c-0b8e-3d82-9004-d01b2b2dca02 | -8.96499 | -47.44812 | 2025-09-30 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0efd57bc-47ef-3366-99f5-a2117ca186c0 | -9.75817 | -47.19497 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 33d24047-6090-39f4-9610-c29da8e3632c | -10.39682 | -48.14217 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 70cb9c78-d336-3ffd-8fff-8287c6cfe06d | -13.15607 | -47.42918 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff37de83-41a9-3e7a-9f4e-ebc1ffa25f93 | -10.07581 | -45.63627 | 2025-09-30 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0e0f60ad-7fa8-3c93-83dd-631ca7a0b90c | -12.85588 | -46.9884 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1e0b43e1-ed18-374a-8a9d-4d5f40fd48af | -13.37134 | -47.30691 | 2025-09-30 04:40:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 579626eb-b645-3203-9eec-2e2becae6028 | -13.42058 | -48.19601 | 2025-09-30 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee99c1ca-79fc-3b2d-9c05-0a82a493d3d4 | -10.19762 | -44.89963 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 58fb1cfb-8787-3cba-b626-302ba8557f0d | -13.40001 | -48.06754 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e57dabee-a63f-3f41-9dc1-b3932e8d028a | -11.9658 | -46.58197 | 2025-09-30 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8e67f4b3-c917-37f1-bc35-7eba6c39ce19 | -13.62944 | -48.03206 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f07bf86-2557-37da-a6f0-374b91357324 | -11.1057 | -47.72663 | 2025-09-30 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e0e8e0d8-4b81-3131-9a05-f91c3f75bf6a | -11.00068 | -57.05078 | 2025-09-30 04:40:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 50df5a5b-41d4-37d9-9e30-25fdbae0a7e1 | -13.57507 | -48.10406 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57873c0d-2d58-3b30-b802-c9bd1ce074fc | -8.25792 | -45.51323 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ef6c976a-c61c-372c-91b6-2701d0ec65d1 | -11.3751 | -45.0666 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 473291d3-2149-37fd-bb27-dce044cff086 | -14.39299 | -47.13607 | 2025-09-30 04:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b4d0c234-7111-35d8-a8df-72aa64b8ad8e | -11.14477 | -54.12226 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3a5b8f51-56bc-3eaf-9e00-9b392c158637 | -10.73155 | -48.17831 | 2025-09-30 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 432ee389-0582-363d-9446-856a030c2058 | -7.50495 | -45.45044 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf414d5c-f638-3c36-bcbc-f14405c7feb7 | -13.78325 | -47.85469 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf1cc4a2-1f0a-353f-b419-55d9efbe142a | -8.67315 | -47.72109 | 2025-09-30 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| afb58500-2b7d-3ce5-9c16-cf5e22208505 | -12.21817 | -43.75232 | 2025-09-30 04:40:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6d55e24e-1155-371c-a8f3-3762d6e64f24 | -11.44226 | -43.50428 | 2025-09-30 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78297f16-8a36-3d1b-ba76-4187ac797795 | -13.74355 | -47.91666 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f0efc88-75c4-35c8-af8d-51de4af1dfd7 | -12.8358 | -46.9948 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dfb042f8-87e9-39c2-986a-52326cb5f1b0 | -7.91622 | -44.63023 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 719437c7-073c-39a7-9462-3228ec5cf09b | -10.6252 | -48.53979 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2f4d61ed-8500-3c36-8060-4ff876e26059 | -8.24565 | -45.51622 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a575d83d-793b-3b90-91c2-6aed05a9be08 | -8.2428 | -45.52345 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0bcc3851-45b3-3b92-b094-1df9e0b27cd6 | -13.71716 | -48.64468 | 2025-09-30 04:40:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2d8678dd-edfc-3774-af46-871fef663c52 | -10.18955 | -52.54966 | 2025-09-30 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e8bf44e-8fe7-3b91-9650-431d8171aff6 | -10.88405 | -49.39845 | 2025-09-30 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1998cdce-9cb5-38f6-ba0b-0d5acdfbbc09 | -11.45655 | -44.97744 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4df1b91f-1bd9-3168-8d4c-55603a289a90 | -11.15992 | -49.81667 | 2025-09-30 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b148a5e-28a9-331a-9c47-51a9789c28d0 | -13.7329 | -48.68328 | 2025-09-30 04:40:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3d44f215-106d-33fe-9808-3d2cf5435ba0 | -13.81619 | -47.49109 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f09adc1-6974-32e1-842a-11dcc3e92d15 | -11.28766 | -47.81843 | 2025-09-30 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0e90aff9-fdb1-338f-a1e8-4f4a0160cbf7 | -9.51066 | -54.66375 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12b985af-5b31-38bc-95f6-907cc984cd3c | -11.79221 | -47.60675 | 2025-09-30 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 348bbcf2-4297-3582-ad78-21c492ac01a5 | -8.24402 | -45.48847 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3ce766fd-3ee9-3fcd-82ba-bf2e38fccedb | -13.21382 | -50.94042 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 1ec69114-5d6a-356e-a3c5-1e27e5f4f9b4 | -8.94829 | -51.68778 | 2025-09-30 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 611b15fe-53d1-3265-aa54-c9005cd929a7 | -11.2527 | -47.2241 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 92db3e93-bc4f-3947-b9cb-a00e9ad5942b | -8.86557 | -46.6699 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 403a2d94-7f56-3476-ac0e-e661f05a6464 | -11.22977 | -47.20287 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b2e8998-11bc-34fd-8b10-62b1e66db755 | -10.08777 | -50.21635 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a8e96338-7097-35a6-9a63-9de3fcfecb19 | -7.47752 | -47.0815 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e74fd4b2-6d15-3cb7-8b0c-2e761d86faee | -9.02918 | -47.74879 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e0e6b0a-c726-377b-bf50-6d8d39cbeb87 | -13.01422 | -49.44191 | 2025-09-30 04:40:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9aa515e-3aee-3f43-b7cf-d6a48937cbf6 | -11.38344 | -44.97337 | 2025-09-30 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd800ff0-21f9-3133-b4a3-b14b13401a0b | -9.12833 | -47.64366 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68cf4842-09f4-3ab1-a501-d589e80f298f | -11.93959 | -43.92037 | 2025-09-30 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b8d4267-c800-3017-ad9f-5884a3ec44a1 | -9.95181 | -49.29329 | 2025-09-30 04:40:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8fc3d4a5-faf1-3fb7-9a87-90086f27281f | -9.77372 | -47.75699 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c35b63a2-885c-33c7-85df-d6049c4ca0a9 | -11.06271 | -47.8238 | 2025-09-30 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 87d66275-c078-3c09-a161-a2fccbd1a6a2 | -13.85451 | -47.9604 | 2025-09-30 04:40:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1f3b779-38ed-3171-b2ad-989692b6244d | -7.05105 | -45.19927 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2032a668-ef3c-319f-ace2-ecdeb7afd9cd | -13.21931 | -50.92687 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e48ed84-8ed1-3832-a8f5-1e2ebe88615e | -10.07733 | -50.21825 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 86d842fa-bcde-35f9-a741-ff320d76120c | -9.05923 | -47.61821 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 545b7f4d-42ec-34ab-b1bd-4a1f86fbc2a7 | -11.46072 | -45.01037 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 16e7d833-ef21-381e-b23f-1e2105a4177d | -9.0612 | -46.7138 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9561b751-23fe-3819-9547-6c0d0b181e4f | -11.44017 | -44.96407 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f35ab3a-514f-307e-8db5-2925aebd255c | -13.60274 | -43.46009 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0d156384-8be3-301c-b50b-7df2fa31d69b | -7.34729 | -50.48164 | 2025-09-30 04:40:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00220cc2-1ada-3ace-8d5e-ee8471c050bb | -10.19401 | -44.89524 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 44.9 |
| d74e99f7-768d-334d-8789-90dfc56f1e45 | -9.5533 | -54.63375 | 2025-09-30 04:40:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| daf206db-f111-35ff-a923-9f2418f44b23 | -11.43397 | -44.94708 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d3cd9d89-ac46-3b63-ace6-4b61615c16d2 | -11.26698 | -47.20687 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63d1e07f-cebf-385b-b9a4-c19ec508415a | -10.61657 | -54.9486 | 2025-09-30 04:40:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1504971-0f78-33d0-ab5d-3534baafea0d | -11.25783 | -47.21897 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2060e68c-1e99-3102-9492-ac7ba23e176d | -10.75909 | -45.37488 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d0238cf-02e2-3bec-934c-a5c4d4f8682e | -7.80292 | -46.16508 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff6120a1-4ccf-39cd-b152-c54650cbcf99 | -7.81663 | -46.99092 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README56.md)
