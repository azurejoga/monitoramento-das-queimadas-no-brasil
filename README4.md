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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b1784e9-d54e-32f0-8465-e0e47e19868a | -8.9414 | -60.5367 | 2026-08-10 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| ddc9e7d0-b32f-3996-8fb0-4bb0dd0ca7ea | -8.8854 | -60.5778 | 2026-08-10 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 92a52bcd-2fec-3ba5-905f-d422297300ca | -8.9039 | -60.5769 | 2026-08-10 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| ca5033f4-0fe8-3167-a13d-928ce1c45c45 | -10.24965 | -45.91801 | 2026-08-10 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c0e9111-d803-34cb-b054-71f84af686dd | -8.32064 | -46.38699 | 2026-08-10 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2845d7b-a2c3-3dcd-a865-ba73c078a477 | -8.3017 | -46.41619 | 2026-08-10 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ab442eb8-dea9-3e57-b3d8-4cc6130825f5 | -11.04949 | -44.28398 | 2026-08-10 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c1aa419-328e-3fc6-9ab9-157f5da08255 | -4.74629 | -40.43626 | 2026-08-10 03:47:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d53ffda9-f544-3ba2-bf85-5d986605d719 | -10.25055 | -45.91335 | 2026-08-10 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e84348b-b74d-303d-9101-ab7dd1f44e69 | -8.28863 | -46.41456 | 2026-08-10 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e183f243-3782-3c29-90f2-60c9a73eb25d | -4.92913 | -37.42535 | 2026-08-10 03:47:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 40425cc9-dc42-37ea-a127-81023c4c406a | -11.04477 | -44.27943 | 2026-08-10 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66630f7b-39c4-33e3-978f-927d9bce1d5f | -4.74165 | -40.43547 | 2026-08-10 03:47:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 83e85e87-027a-3b01-abd7-418334eb2f0f | -11.04344 | -44.28635 | 2026-08-10 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 411e069f-17ba-33e3-87c1-0edae7266af7 | -8.30821 | -46.41711 | 2026-08-10 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 765f22d7-9e6b-36cd-be29-0bc5b675b789 | -7.11297 | -35.11222 | 2026-08-10 03:47:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b5db6415-985a-3cf8-a842-25de33e8396f | -11.05015 | -44.28053 | 2026-08-10 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43e88cae-e053-3eb6-a995-fee5b31b3046 | -8.31314 | -46.39132 | 2026-08-10 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c704034d-2061-37c5-897e-fc340274d55c | -10.25418 | -45.82977 | 2026-08-10 03:47:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fa57957-7146-3cc8-a8a6-a97386ea6f0c | -11.03738 | -44.28875 | 2026-08-10 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d9ac33c8-75b3-30b0-b846-8767a61847c6 | -7.10961 | -35.11166 | 2026-08-10 03:47:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 29334b13-1b3f-35e3-9762-6f0eee33159c | -10.25132 | -45.91341 | 2026-08-10 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94ca212b-3918-30b3-aac1-7b1644f82dc4 | -10.47635 | -46.62023 | 2026-08-10 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 42348050-0a6c-32af-8137-6716ae0710ff | -6.06552 | -35.21111 | 2026-08-10 03:47:00 | NPP-375D | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5dc7e0a0-f087-3044-8f58-e9ef5cb05f99 | -8.31414 | -46.38608 | 2026-08-10 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ea10fb0-aed0-3ce5-88c3-7bd7e4431570 | -11.04411 | -44.2829 | 2026-08-10 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 705ba984-2a8a-3ce1-b17f-4113fa98b77e | -10.25039 | -45.91806 | 2026-08-10 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 309fc01b-241b-3246-8ea8-bb306e52745a | -11.03805 | -44.28529 | 2026-08-10 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c5e615c6-8721-34c9-97e0-fada524a34c7 | -10.26041 | -45.82986 | 2026-08-10 03:47:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 65914c31-92cc-32b8-8002-5d0b4149765b | -8.29516 | -46.41542 | 2026-08-10 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1157ea97-fb1f-399d-9199-c35c522d6265 | -11.04277 | -44.28982 | 2026-08-10 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b1806b8e-0351-3381-8bb1-2d64bc8833f0 | -6.06764 | -42.51193 | 2026-08-10 03:49:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e593919d-cb52-3a7a-b9fa-fb421eee4a48 | -19.86093 | -40.23804 | 2026-08-10 03:49:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1bf7c6ca-6680-34dc-a5b3-8b6737379266 | -17.69134 | -40.14001 | 2026-08-10 03:49:00 | NPP-375D | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 55e682e8-09f5-3695-a210-1c420b06551c | -7.61525 | -42.76258 | 2026-08-10 03:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0ae4a5da-c941-36ac-bd00-315a5eacc77b | -16.14234 | -49.7086 | 2026-08-10 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0db52c30-5e10-3ff6-8a68-25594c00f227 | -7.61637 | -42.75624 | 2026-08-10 03:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d8cb556b-92e5-30c5-b1f7-a5625c9a3c63 | -7.15356 | -43.26677 | 2026-08-10 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 184b22b1-bd2f-34be-9750-b923b75dd2c4 | -19.49975 | -42.61322 | 2026-08-10 03:49:00 | NPP-375D | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| c2da7cca-6ad9-3825-9774-2343152b8275 | -18.80813 | -42.16076 | 2026-08-10 03:49:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6cb92c1a-4518-31d6-9f25-3eb954143e53 | -15.16097 | -41.84843 | 2026-08-10 03:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5298a8c9-9b09-36f5-ac15-2639a6612558 | -6.46211 | -47.85366 | 2026-08-10 03:49:00 | NPP-375D | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9bbd363-7905-3a0b-82b0-2c416b88ec1d | -7.62211 | -42.75403 | 2026-08-10 03:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dc438527-1024-3ef4-bd38-4f16a0582478 | -13.85707 | -43.65111 | 2026-08-10 03:49:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3a4b30e5-1008-3b30-bd16-6d8439414165 | -15.04866 | -46.57327 | 2026-08-10 03:49:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6aac9bf8-cd4e-382e-97cd-39d71ba84464 | -7.6193 | -42.76991 | 2026-08-10 03:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a3ec26f4-372a-316f-8d82-4883c1659ceb | -15.04401 | -46.56655 | 2026-08-10 03:49:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a6af270e-f90c-3887-8d1c-1a854212f992 | -15.6525 | -43.28809 | 2026-08-10 03:49:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5945ed04-957a-31a3-89a3-2be9be046b1d | -15.0456 | -46.55891 | 2026-08-10 03:49:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 31a01eb2-d2aa-3e52-b1da-ad5fdc1a0cfd | -7.14815 | -43.26585 | 2026-08-10 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 34402399-8019-361c-947d-e803ee7920e2 | -16.3326 | -46.89005 | 2026-08-10 03:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d9e1311e-ebf7-3b59-bf1e-b7bcd558e415 | -15.05055 | -46.56415 | 2026-08-10 03:49:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2f0d4b4d-0e8b-324b-8742-911a6122ee44 | -13.86308 | -43.64646 | 2026-08-10 03:49:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffd9b83b-2b31-3caf-89d0-95e7e0cea6fa | -7.40325 | -39.79485 | 2026-08-10 03:49:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5d093e3d-5c8b-3fcf-8a5a-ed621d9de73b | -16.14375 | -49.70233 | 2026-08-10 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed9e8304-a6bc-3b0b-9b12-8e1b13a02f7d | -19.85654 | -40.24173 | 2026-08-10 03:49:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2af0d9fe-f25c-3fab-8f37-b7e0f9f8ba14 | -7.62043 | -42.7635 | 2026-08-10 03:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 524e1d1f-2b69-3961-9110-7a4ae8ebeb50 | -6.06705 | -42.51521 | 2026-08-10 03:49:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f4327841-ed3c-30bf-abee-7e2b3349d32c | -6.06775 | -42.51397 | 2026-08-10 03:49:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 89d5a969-e6ca-3aab-98b4-38c463efea5a | -19.8285 | -43.29849 | 2026-08-10 03:49:00 | NPP-375D | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 270c688d-7c60-3c02-b5ad-61fb26579919 | -7.61412 | -42.76899 | 2026-08-10 03:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 73f2fe73-87e6-3d05-b72b-65bad794db54 | -18.04244 | -44.36655 | 2026-08-10 03:49:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e32d6499-2917-3aba-91a8-be19b315debf | -16.33178 | -46.89262 | 2026-08-10 03:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c2db01a-affc-3aac-9896-b037315c9b3d | -6.46363 | -47.84582 | 2026-08-10 03:49:00 | NPP-375D | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16ce3730-72a0-3bf7-8000-a9a94155f96e | -15.65152 | -43.29309 | 2026-08-10 03:49:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 327ffcd1-1082-3328-86aa-d12056dcabe0 | -7.61469 | -42.76579 | 2026-08-10 03:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 231e64c9-5409-35fc-8479-42309dcd774b | -16.33265 | -46.88856 | 2026-08-10 03:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af2a5f4d-baee-31ac-a779-cc1f3a8c3dca | -13.48258 | -40.30752 | 2026-08-10 03:49:00 | NPP-375D | LAJEDO DO TABOCAL | BAHIA | Brasil | 2919058 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 818c4121-4d08-39fb-8e60-5bca08057bda | -13.48401 | -40.30952 | 2026-08-10 03:49:00 | NPP-375D | LAJEDO DO TABOCAL | BAHIA | Brasil | 2919058 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7bbec299-32f5-36ce-b00c-7bfe79b01577 | -7.30979 | -35.12918 | 2026-08-10 03:49:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f037fff0-668d-38f3-bbdb-a32d443b6beb | -6.98662 | -39.50502 | 2026-08-10 03:49:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 36b9c751-1224-3aed-85ba-c7b6c80668b3 | -12.39369 | -43.65832 | 2026-08-10 03:49:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7e1b9bb-ac7f-39e6-8eaa-a96524d4370c | -7.30856 | -35.12885 | 2026-08-10 03:49:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9f30e06e-d642-3ceb-b0b2-b0eb2b9ca797 | -17.76509 | -42.43008 | 2026-08-10 03:49:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2dbfcee8-211b-3eec-a63d-aca89b58414e | -18.04243 | -44.37115 | 2026-08-10 03:49:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 40f772a8-bf13-3e93-8dbf-461bb8999e7f | -15.04962 | -46.56866 | 2026-08-10 03:49:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b984df7e-d40e-3614-9de8-a626bd1e3a07 | -15.64992 | -43.29135 | 2026-08-10 03:49:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cd581cef-0397-3d3f-86bd-123e61dacf85 | -18.02803 | -44.36414 | 2026-08-10 03:49:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f17fc47-ca0b-3bdd-b60f-e38577947aeb | -18.04345 | -44.36597 | 2026-08-10 03:49:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d7f6dfd5-1453-391d-a617-d4808f60a93e | -15.04484 | -46.56258 | 2026-08-10 03:49:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| bb723ec8-9543-3574-bc92-7ccd9c2568af | -6.96263 | -41.48186 | 2026-08-10 03:49:00 | NPP-375D | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e78dd266-bfc8-366a-9b1e-7addf772cab1 | -19.86015 | -40.24245 | 2026-08-10 03:49:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 79adae18-bb19-3a8e-afa5-494b56066f44 | -15.04316 | -46.57065 | 2026-08-10 03:49:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 706495d1-20f2-34cc-8f95-23b5b2e48dab | -6.96747 | -41.48246 | 2026-08-10 03:49:00 | NPP-375D | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 84f464c7-2758-3a68-aeeb-f6c116c7799e | -7.40446 | -39.79657 | 2026-08-10 03:49:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| eca6b4ab-aafd-33e3-b194-a7ec91e5a6cd | -16.06374 | -50.80593 | 2026-08-10 03:49:00 | NPP-375D | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9d107015-7611-3187-98e1-f13fe8a2058b | -7.61581 | -42.75941 | 2026-08-10 03:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ef0ccde8-22a5-3f44-9d9c-d8f5191c1cb8 | -6.46744 | -47.85552 | 2026-08-10 03:49:00 | NPP-375D | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 073be921-21ea-3cba-b964-265d38a5e89c | -19.82323 | -43.30262 | 2026-08-10 03:49:00 | NPP-375D | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 15968953-1664-3761-b0c1-04eba1c65978 | -13.85818 | -43.64545 | 2026-08-10 03:49:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3e5ba40c-d43b-3ea9-a16e-fc309f6cf022 | -19.82763 | -43.30299 | 2026-08-10 03:49:00 | NPP-375D | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 6d735345-822d-3c3c-b7fd-0a591dd4899a | -7.61987 | -42.7667 | 2026-08-10 03:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b379e3ce-97b6-3075-831b-58fe71bd8e8b | -15.84676 | -48.14179 | 2026-08-10 03:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 63c35a3b-5ade-3b6e-ba33-124fc1e5f622 | -17.76188 | -42.43114 | 2026-08-10 03:49:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 923bab45-21d1-3f01-8e82-e13478b2c814 | -6.46027 | -47.85395 | 2026-08-10 03:49:00 | NPP-375D | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae5da54b-2c76-357e-b9e3-970f74b70dec | -15.58494 | -40.98713 | 2026-08-10 03:49:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8dfdde5d-20f0-3654-84db-ffa0149c18da | -8.8854 | -60.5778 | 2026-08-10 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 55b293f2-3eba-33a3-9adb-1dc721ac543a | -8.9039 | -60.5769 | 2026-08-10 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 32a8deca-4aa6-35a4-bb35-55389b16d213 | -8.9598 | -60.555 | 2026-08-10 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 5537c003-8b89-3b7f-91ca-6df51c87ac5f | -20.50092 | -42.38805 | 2026-08-10 03:51:00 | NPP-375D | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |


[Clique aqui para ver as próximas entradas](README5.md)
