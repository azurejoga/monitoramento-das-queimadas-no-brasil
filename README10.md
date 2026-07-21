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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77cf3275-9166-380a-a340-b2e4c7d732cc | -22.15061 | -49.15381 | 2026-07-21 04:32:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c4a22c5-b3c0-3c91-a4e4-98e722a61037 | -22.79478 | -49.341 | 2026-07-21 04:32:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9eef824e-6f14-3fd8-9366-cc1a72a6d563 | -23.19891 | -49.15634 | 2026-07-21 04:32:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d2856bf-34b1-3e86-8cb9-d8871b743faa | -22.61367 | -47.80462 | 2026-07-21 04:32:00 | NOAA-21 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5fc9baf-ccc3-30f6-9f42-ff8efd65be26 | -22.44331 | -47.15561 | 2026-07-21 04:32:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3c7b393-d342-3e3f-8164-6fc42a30a3f3 | -25.11747 | -52.72072 | 2026-07-21 04:32:00 | NOAA-21 | DIAMANTE DO SUL | PARANÁ | Brasil | 4107124 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 93bde221-4b24-38b6-a756-f9ab9939fce0 | -23.77929 | -49.04147 | 2026-07-21 04:32:00 | NOAA-21 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44d3f3b3-a065-314f-a341-003623a5a74d | -23.19613 | -49.15194 | 2026-07-21 04:32:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2c6e048-5723-3fec-b6e9-7918af6bdd39 | -23.42978 | -46.75919 | 2026-07-21 04:32:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dd744c08-7683-3e5d-9451-7c9e2b74c99d | -23.56572 | -47.51909 | 2026-07-21 04:32:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 878f8bda-87f7-3516-bbbd-baf6b713aca3 | -22.79753 | -49.34536 | 2026-07-21 04:32:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e87fadef-9d04-30a9-8c0f-51c0945e7b18 | -23.28644 | -46.83141 | 2026-07-21 04:32:00 | NOAA-21 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 88e51ac7-94db-3c16-8de4-3d71741c113c | -22.85849 | -45.22017 | 2026-07-21 04:32:00 | NOAA-21 | APARECIDA | SÃO PAULO | Brasil | 3502507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0795d1b1-1bbb-317a-b22d-268a07b27f76 | -18.5476 | -56.8135 | 2026-07-21 04:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 160.6 |
| 499a7d2c-999e-31cf-98fc-4a4046f5e198 | -13.3032 | -45.1045 | 2026-07-21 04:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 7374239a-132f-3ce4-84e3-ad1712db2408 | -13.3221 | -45.1246 | 2026-07-21 04:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 7a893dc6-8883-3d18-8d2b-bb420ef9e976 | -13.3217 | -45.1479 | 2026-07-21 04:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 9ccf49f3-6076-3542-844e-9a111d33d05f | -18.5675 | -56.8109 | 2026-07-21 04:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.4 |
| 57c69c85-13c9-39cb-ab97-4e2b4e23e8ad | -18.5472 | -56.8343 | 2026-07-21 04:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.1 |
| 8c545b5e-2456-37b5-be36-26851f333a84 | -13.3028 | -45.1278 | 2026-07-21 04:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 214.0 |
| aefa3dc7-77df-3e6b-8ea0-6aa45df77935 | -13.3023 | -45.1511 | 2026-07-21 04:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 6c8c58f7-8345-36d1-aef6-3be34bb5160b | -18.5476 | -56.8135 | 2026-07-21 04:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.0 |
| 554c86f2-cc7d-3a75-a322-4d27c1c18807 | -13.3028 | -45.1278 | 2026-07-21 04:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 21924520-8ae1-3474-b1e6-14eed948b79d | -13.3221 | -45.1246 | 2026-07-21 04:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 301b15e2-f2ba-35ec-b2bf-044ae06c4480 | -18.5472 | -56.8343 | 2026-07-21 04:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.4 |
| beb3ee60-fe69-30e7-981d-7cff689add9a | -18.5675 | -56.8109 | 2026-07-21 04:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.4 |
| 52960883-2ad8-3892-9835-399f1b934d7c | -13.3217 | -45.1479 | 2026-07-21 04:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| c271b3ef-96ed-31e6-86c5-a83697f2c9f8 | -13.3226 | -45.1013 | 2026-07-21 04:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 39.3 |
| e45060da-416d-3ffc-b6e6-72578a336e95 | -13.3028 | -45.1278 | 2026-07-21 05:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 2ca288f0-f52f-36fa-a258-47f3157e8d59 | -13.3221 | -45.1246 | 2026-07-21 05:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 145.9 |
| d11b70be-166a-3f12-a234-38c8ebd7ca9e | -18.5476 | -56.8135 | 2026-07-21 05:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 138.8 |
| 597031e2-bd27-3ad5-8501-e7f9a272d7c9 | -13.3217 | -45.1479 | 2026-07-21 05:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 3f849b4e-dd2a-3749-90c5-30033d37fd8f | -18.5472 | -56.8343 | 2026-07-21 05:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.0 |
| c9938387-0603-3acd-bdbb-2bf027a287a2 | -13.3032 | -45.1045 | 2026-07-21 05:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| b5ab585c-1573-3f1d-bde2-f014aaf5d84e | -13.3226 | -45.1013 | 2026-07-21 05:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 9e5fd260-f950-3db0-80db-2945869b905c | -18.5675 | -56.8109 | 2026-07-21 05:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.8 |
| fd1c1e9c-ecbe-3154-9e0a-951ae2fe6ecf | -7.83354 | -47.10789 | 2026-07-21 05:01:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c584dd0-faab-3aab-85ab-db7c8abc00d2 | -3.57713 | -43.46474 | 2026-07-21 05:01:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| efe8c784-160d-37ea-a2cf-ccb752e045fb | -6.30964 | -43.65649 | 2026-07-21 05:01:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d3c60f89-134d-3fe1-a726-02b99882bd05 | -2.79431 | -49.52354 | 2026-07-21 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e1ac06b-bc4c-3677-83b3-3b8dd2300a4e | -5.12476 | -43.23929 | 2026-07-21 05:01:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6904185c-e715-3aeb-a8fa-24ca86f0d9b9 | -6.03959 | -43.86643 | 2026-07-21 05:01:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0ff5406-c33e-325b-a8ee-bf7f66dc81b6 | -6.00995 | -47.11072 | 2026-07-21 05:01:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d18ac627-1edc-3f5a-8129-bb9eb2f96d77 | -6.04485 | -43.86721 | 2026-07-21 05:01:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f3545b9-26c6-34ea-b71c-e4240b49b976 | -7.64973 | -49.75512 | 2026-07-21 05:01:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd367d07-fc28-341e-8695-c5722414b06b | -3.24036 | -47.9259 | 2026-07-21 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 209c0684-ce81-3bd3-b31a-5a06edb90dfd | -3.14661 | -48.15343 | 2026-07-21 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fbd07469-d487-38db-9b13-eafb9a17cee2 | -6.53775 | -55.15654 | 2026-07-21 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93a31536-731f-3361-8b08-c8662821625e | -6.31063 | -43.64955 | 2026-07-21 05:01:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d89bdf8-486a-3cfd-a463-eee5479cf6c9 | -5.83053 | -43.47368 | 2026-07-21 05:01:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47941ff0-b348-30f8-9b24-aac4fb97723d | -5.74172 | -43.27126 | 2026-07-21 05:01:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3dcb8d0-60f8-36ca-b91a-c3da7d061008 | -5.3397 | -43.17849 | 2026-07-21 05:01:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 255ef648-2bf5-301d-a144-1643ef271754 | -2.60153 | -51.95053 | 2026-07-21 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9bbb878-be01-3fbe-8a1d-8579efb8417e | -8.01254 | -51.40976 | 2026-07-21 05:01:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47ca257d-1f66-3415-a193-953d8292e04b | -6.59868 | -51.70582 | 2026-07-21 05:01:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8545501c-ff92-388a-91f0-554c4248fdfb | -5.12329 | -43.23602 | 2026-07-21 05:01:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31910ae5-464e-3612-ab5e-a0e4942a61c3 | -6.53837 | -55.1527 | 2026-07-21 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61347398-6be0-3eea-bc7d-cee28ed30938 | -5.91379 | -46.72248 | 2026-07-21 05:01:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fed5c6ba-0ce4-35af-8359-2f956c92238f | -3.95629 | -48.00296 | 2026-07-21 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40dda123-c641-3995-8ffd-d6b3fedef98f | -7.86143 | -45.98348 | 2026-07-21 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e12a88a-7d87-3215-9a19-d5665a847666 | -7.63446 | -49.75721 | 2026-07-21 05:01:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7efe28db-b80d-3dd0-9a6d-e386a86a7770 | -7.83787 | -47.10849 | 2026-07-21 05:01:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afc00da5-f613-3654-b5ae-abc8772205c4 | -2.69545 | -49.0225 | 2026-07-21 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13829174-803c-3740-9faa-7b30453a3ffe | -3.15116 | -48.57941 | 2026-07-21 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38711ef2-277a-3177-b1fd-c4d80dfabefc | -6.54124 | -55.15709 | 2026-07-21 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 880b76b2-6046-3c34-ad69-a00e36f6aeab | -7.73708 | -49.47481 | 2026-07-21 05:01:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 373534c6-5def-39fa-8922-4dde12393f06 | -7.91034 | -48.26287 | 2026-07-21 05:01:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f93ee91-2b45-3dd5-98b4-88a1694bb718 | -2.80133 | -49.52462 | 2026-07-21 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c51c379e-fd4e-3896-ba73-4341ea6f48fa | -6.43002 | -54.71692 | 2026-07-21 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2f31af0-f46c-3e27-b59b-dfe81a9d5fa8 | -3.20498 | -50.7443 | 2026-07-21 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0fe9963b-b585-395d-805c-5f9c9fdeb41e | -5.93799 | -46.35282 | 2026-07-21 05:01:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1a039dab-92e5-3725-a2a5-364c4c70b77f | -5.11739 | -43.23849 | 2026-07-21 05:01:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d8b3c135-0cb8-321c-a843-db8ec8381b75 | -3.14747 | -48.57885 | 2026-07-21 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f25c2fe2-b704-3185-b30b-6ede9cd5c852 | -2.46972 | -49.36092 | 2026-07-21 05:01:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 38052f76-ad80-3bca-81b3-4bb73a688607 | -3.14284 | -48.15285 | 2026-07-21 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b45c8ce4-840d-3f10-9bdc-52889718c7d0 | -6.03343 | -43.87202 | 2026-07-21 05:01:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f282341c-829e-3daf-b9ed-192b5f3dc749 | -2.47034 | -49.35701 | 2026-07-21 05:01:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 832fde4c-b019-36b9-8c14-5824577a020f | -2.7908 | -49.523 | 2026-07-21 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d84ce20-7f84-3e96-ab57-27eaacd3b0da | -7.63081 | -49.75665 | 2026-07-21 05:01:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 8aeef382-e7fd-35ae-86c9-51a131d61226 | -4.16134 | -43.09875 | 2026-07-21 05:01:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9820658-1681-3d6a-85a4-0f9c0333670b | -3.14682 | -48.58316 | 2026-07-21 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a3b2ab4c-733b-340a-a57c-e90ceabd49dc | -5.12523 | -43.23592 | 2026-07-21 05:01:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6faf9ca9-c945-38be-a26b-2ea586cc9098 | -3.1525 | -48.5816 | 2026-07-21 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a47ffd2b-6b02-3b10-bafb-648a15905e97 | -3.5049 | -54.09145 | 2026-07-21 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a7049fbb-b16c-3baa-9a80-58f5c90d6e74 | -1.81768 | -54.47907 | 2026-07-21 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cee2de47-89df-3bd9-99ad-961c7113b956 | -5.1228 | -43.23939 | 2026-07-21 05:01:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f34897ad-70a4-3272-ad2c-7d0ac20cac6c | -7.34897 | -49.60008 | 2026-07-21 05:01:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 47028a2e-98e6-3980-93ab-2ebbbec1aa4a | -7.64241 | -49.75404 | 2026-07-21 05:01:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74c491d7-317d-3b9e-b26b-b65646868aa0 | -5.1282 | -43.24025 | 2026-07-21 05:01:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea3d6360-6d1b-34cf-90de-6330a797b27d | -5.12428 | -43.24267 | 2026-07-21 05:01:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e032a5d-1393-3138-a7c2-70b636852f81 | -3.45761 | -48.81917 | 2026-07-21 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49170a4b-e7be-317d-8f61-71ce285c3912 | -3.98 | -48.42643 | 2026-07-21 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e57fbf1f-8e24-3848-b80f-538bed0a970a | -7.64607 | -49.75458 | 2026-07-21 05:01:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57dd5cbe-97ab-3443-bd2e-dd687333eb6d | -7.6351 | -49.75293 | 2026-07-21 05:01:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6c8cfa09-0070-3f2d-9bad-8b749cadd2b7 | -6.01415 | -47.11134 | 2026-07-21 05:01:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3ce85e1-600c-3e2a-9b9a-0852beae95ba | -6.31013 | -43.65303 | 2026-07-21 05:01:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 197e567a-5360-3313-8de5-46bbe008ce8d | -7.62779 | -49.7518 | 2026-07-21 05:01:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 63efab34-99ae-3574-95a0-5c70e3762595 | -6.13161 | -55.80338 | 2026-07-21 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ead7051-03a0-3839-97a8-3225af4ce46b | -3.97242 | -47.19731 | 2026-07-21 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0dff29fc-6c93-3164-a0fc-5b79f706ff33 | -7.88841 | -46.91176 | 2026-07-21 05:01:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README11.md)
