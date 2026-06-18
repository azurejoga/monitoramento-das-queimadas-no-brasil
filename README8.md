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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 828faaf6-4149-3626-a5cd-6ee8c0cdbab3 | -11.81772 | -47.34198 | 2026-06-18 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64770126-cfd3-3a3a-ad7a-764382db6166 | -6.87283 | -52.41169 | 2026-06-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e94918a4-6fd3-377e-93d4-d52dab266e3c | -10.15345 | -56.61176 | 2026-06-18 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a3ee1f2-e4bc-3784-a455-dc7d17e67de9 | -10.1556 | -56.62288 | 2026-06-18 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3406f76f-7b76-370e-90d5-29059e4713b5 | -10.98509 | -47.74626 | 2026-06-18 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6f9f063b-79f3-3df2-830b-47062ce889f0 | -7.91917 | -48.24456 | 2026-06-18 04:46:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e82d811d-d6ad-303a-94b3-de051ac84dc2 | -7.83938 | -48.39102 | 2026-06-18 04:46:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7512c6fa-bd9b-34bf-be34-b144f7b51261 | -12.76718 | -44.53673 | 2026-06-18 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 62977d99-71d5-3df9-927d-16cb0a0d65c8 | -12.07641 | -47.55508 | 2026-06-18 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05654f69-519b-3052-93f7-77e9e2dfe233 | -7.84307 | -48.39085 | 2026-06-18 04:46:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f3c3608-19a3-318a-a005-383e8ae6b85b | -11.15612 | -49.23551 | 2026-06-18 04:46:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9147add0-6072-3844-9398-dcf3c6d833a4 | -10.58573 | -53.48115 | 2026-06-18 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c16af062-17d2-3d53-a300-e44141d6038f | -8.2607 | -43.92559 | 2026-06-18 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0bf9cee-ba79-36d7-a343-1a97f6b61cb9 | -10.15165 | -56.62219 | 2026-06-18 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e74f9730-804a-3fa7-a182-b6846830328f | -12.02885 | -47.80607 | 2026-06-18 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8a8f67cf-dff9-3b9b-8b9b-c90d01269a91 | -6.84572 | -46.34241 | 2026-06-18 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1defab2-88ed-31f2-b9de-4b016c8557e3 | -11.26428 | -53.95749 | 2026-06-18 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c457b7b9-4c90-3717-b842-9bb44788c3e5 | -7.36203 | -49.86478 | 2026-06-18 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f3cd6c2-dd0a-3c9e-8ed5-19bd2876e618 | -8.83817 | -44.7923 | 2026-06-18 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5191228-70a8-3f44-8e48-86d8b7e5584c | -10.98823 | -47.75161 | 2026-06-18 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eb9bc6f1-38c5-3793-924f-e981516d94a6 | -6.8417 | -47.91824 | 2026-06-18 04:46:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b91ee878-e32d-3f26-b94e-532fdd39b8bb | -7.79584 | -46.4531 | 2026-06-18 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4904ca6-79f5-308e-b85d-66faceaea6d2 | -5.80861 | -45.08131 | 2026-06-18 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 878655cd-9fc9-30c3-b0f8-c1e8caf85580 | -6.84964 | -46.34302 | 2026-06-18 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1fcdcd0-0c09-3023-81c3-218dbbe13684 | -11.78407 | -46.73499 | 2026-06-18 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b750ac04-f64c-38af-9ccc-c5ce43fca83e | -9.80959 | -48.91879 | 2026-06-18 04:46:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1105d515-1ef1-35a7-baee-ae614e155db2 | -9.00304 | -48.00037 | 2026-06-18 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2df2d201-d343-3acc-9c73-4fb12bd199b6 | -5.13645 | -47.98982 | 2026-06-18 04:46:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4e8fd2b-c74a-349f-b93a-e48373ad4fe4 | -8.80554 | -46.62788 | 2026-06-18 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04376f88-49db-335a-a6b2-565e653aca7a | -11.48279 | -52.9184 | 2026-06-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dfbfdb5-3165-3ec3-96a6-a20fca0107cc | -5.38672 | -49.28827 | 2026-06-18 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9b28fdb-1ec3-3ae9-bb5a-7f76d0ab7eef | -7.83893 | -48.39435 | 2026-06-18 04:46:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 561a6cfe-e7d3-3ee9-81b7-3a38d11c39b8 | -12.84088 | -44.36927 | 2026-06-18 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| a1edc520-faff-32a6-b54f-6dfdac2808ba | -9.59942 | -48.19189 | 2026-06-18 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a8ec675-963a-30be-a432-040249b3846a | -12.76787 | -44.53133 | 2026-06-18 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f39e6fa0-d39e-351b-a76a-7adce5ffbf43 | -7.72474 | -44.1689 | 2026-06-18 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c31b6d8-871b-3f65-8e05-aab84ce39d45 | -12.63107 | -44.60878 | 2026-06-18 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d408ac6-25ee-36f0-a1f8-ac94030e1f0e | -7.36483 | -49.86885 | 2026-06-18 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 540128dc-af93-34a2-8e37-41ded2c8732a | -7.80329 | -46.46222 | 2026-06-18 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9e906707-81eb-381b-80f3-fe6f2760ff67 | -10.58514 | -53.48481 | 2026-06-18 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff84443e-90b9-3732-9122-3bf2a1079312 | -12.07291 | -47.55582 | 2026-06-18 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae6885e1-274b-3c1f-9a65-47a8f11daa8b | -7.80083 | -46.45155 | 2026-06-18 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa6596ed-4b9d-32e7-a985-f45551d6d64a | -8.97991 | -47.97912 | 2026-06-18 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0558e5b2-ef33-3740-951b-c5b73201f73d | -10.71122 | -49.53724 | 2026-06-18 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23028b16-74b2-3559-bf74-33647d2a1253 | -7.36593 | -49.86173 | 2026-06-18 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59f0000f-33f3-33e4-81c8-7425e44f9a23 | -6.8423 | -47.91415 | 2026-06-18 04:46:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b546d3c5-5f4d-32e3-84a0-fe290cc99006 | -7.7162 | -44.16273 | 2026-06-18 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 560b05cf-4b79-33ad-8056-5a6e00880450 | -11.80428 | -52.52267 | 2026-06-18 04:46:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad5052a7-3bd3-32d7-9d33-00465ffddab8 | -8.91022 | -46.96542 | 2026-06-18 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65158af4-16b1-3337-8f37-23166ed8dcb6 | -10.05394 | -48.09938 | 2026-06-18 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b98cb966-83be-33d4-b7c7-d9587871613e | -10.91236 | -46.43225 | 2026-06-18 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 005a7693-30e9-3ee4-b22b-2b7b22947f55 | -8.96818 | -49.15017 | 2026-06-18 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c5e99ba-e6d0-3fe6-84ef-931ee0f4800c | -7.71554 | -44.16751 | 2026-06-18 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9db89ad0-af0c-3941-ab74-75b1579567f9 | -12.23271 | -46.6075 | 2026-06-18 04:46:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae1a28b4-4b88-33c9-b65d-6ba7c19872f7 | -10.91897 | -56.85472 | 2026-06-18 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 8cebade6-d837-3198-9505-ff5d3abdf55a | -10.57588 | -57.31451 | 2026-06-18 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c135bffb-e69d-3f03-8086-ece3d7d12e2e | -9.1948 | -58.0522 | 2026-06-18 04:46:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81e50510-e391-3158-b6ac-80a4ff9f9d9f | -6.15977 | -48.50286 | 2026-06-18 04:46:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f07700b0-d382-3c82-834c-1daa8cbf4e87 | -12.76304 | -44.5307 | 2026-06-18 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4271b4b5-bd64-3f24-8ec1-dfa51e127494 | -9.37058 | -50.53422 | 2026-06-18 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38dd5900-7f28-3c78-b646-532dfb0edce4 | -6.28654 | -43.63262 | 2026-06-18 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6c5201f-b7d9-3ef6-8a3b-5316202f80ad | -11.3554 | -51.40562 | 2026-06-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 005ebf67-61b1-3ec7-a3fc-f8891c65830e | -9.57744 | -53.5647 | 2026-06-18 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d646070b-889b-35e1-b14e-596afe2f67e7 | -10.93208 | -46.41195 | 2026-06-18 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c16468d4-b55e-34fb-b5ec-190651c17192 | -8.99168 | -47.03266 | 2026-06-18 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7f01036-23b9-38c0-99d0-33fc7f088cac | -6.15859 | -48.51059 | 2026-06-18 04:46:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 795b9ca6-488f-3cd7-a486-748e1678b715 | -12.77201 | -44.53735 | 2026-06-18 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8d1e850d-2466-3569-afe6-2ed5c92e3f3c | -10.65523 | -49.19999 | 2026-06-18 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f44b8bd-0343-341b-b93f-d99abe346749 | -5.80553 | -45.07309 | 2026-06-18 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3b46e3db-94a5-3d22-92d8-c885b984f2c6 | -10.5608 | -46.23381 | 2026-06-18 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e553efa-f906-35c8-ab62-e7378d60d4f9 | -11.48667 | -52.9154 | 2026-06-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73d205d5-7449-3a29-b467-6836d840bcf8 | -10.56549 | -46.23055 | 2026-06-18 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c83bd6a2-016e-36bd-a919-4b6274127d55 | -8.32864 | -49.55962 | 2026-06-18 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07d04ae8-bfa5-3ebf-a10e-a4f42e39f55d | -10.04562 | -48.1093 | 2026-06-18 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 51e496d9-55f0-38ce-87f4-46b3aca8ac93 | -9.21552 | -47.92583 | 2026-06-18 04:46:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 55dbbe21-b219-3d9f-8a22-8a646c553b75 | -11.25039 | -46.62784 | 2026-06-18 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95215241-b70e-3c3d-be45-dcd065b5c1a7 | -9.63609 | -49.44389 | 2026-06-18 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64999f1a-156f-341b-8ff7-49b0d4e67b32 | -10.99203 | -47.7522 | 2026-06-18 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 14493b90-f3ee-3d3f-8395-b9529bc76417 | -7.83553 | -55.39751 | 2026-06-18 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d50797d-1444-3504-b78f-d6a1a0bc5ed2 | -10.14949 | -56.61108 | 2026-06-18 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b745b80d-0093-39d6-b230-36f6b8a36f4c | -11.81377 | -47.3414 | 2026-06-18 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 292062c3-1081-3f72-892a-1847cb7b5bbf | -10.91152 | -46.34709 | 2026-06-18 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e46d41e5-8526-3b56-a619-17bc1dd951e0 | -6.56411 | -47.88922 | 2026-06-18 04:46:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3d2e1406-d9b1-369e-aba0-372f34e86a1c | -8.61275 | -45.99677 | 2026-06-18 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 244060a2-3ab3-359b-b138-edb953325ba5 | -10.59452 | -53.5127 | 2026-06-18 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3c9c3a4-5021-3c94-b3b5-939951a103ba | -8.97591 | -47.98077 | 2026-06-18 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f804e0e-be90-3dc0-b99c-fbfa43d13639 | -10.25995 | -47.34364 | 2026-06-18 04:46:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 504b8cc8-7d7c-3533-a407-03fee8b506f7 | -9.80606 | -48.91828 | 2026-06-18 04:46:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5c13821-7dfd-3f95-844b-3a75026e8e54 | -10.80347 | -48.75638 | 2026-06-18 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 72dddcdc-033b-37c1-bb93-4d075bcf55f5 | -11.48611 | -52.91895 | 2026-06-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8e11f36-c561-31db-b3e2-6048c59dfff8 | -10.1565 | -56.61768 | 2026-06-18 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22b6b1ae-1c8c-3fe2-a63b-1b360c96aea2 | -11.54727 | -52.79148 | 2026-06-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 392bb22f-57b7-3586-9e3b-28a6121f0f54 | -9.21857 | -47.93084 | 2026-06-18 04:46:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 66eef535-3ad4-3841-be1f-49e5b3eadbb6 | -10.91104 | -56.85329 | 2026-06-18 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63abccab-93ff-370d-b71b-069262a6c938 | -10.71925 | -59.26943 | 2026-06-18 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e45b524-3719-3400-a13e-6ce38bcee93b | -10.55663 | -46.23321 | 2026-06-18 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 292e9eda-d69a-3a28-8ce1-c742192975ff | -12.0736 | -47.55073 | 2026-06-18 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2dfda68-9943-3100-ad0a-55a19a473597 | -7.60022 | -46.47676 | 2026-06-18 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ed93249b-f6b0-3ea1-b45c-ed1a945b4e6a | -6.56892 | -47.88159 | 2026-06-18 04:46:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e14b1cbd-192a-36c4-b423-6cf41c50e28f | -6.28582 | -43.63776 | 2026-06-18 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README9.md)
