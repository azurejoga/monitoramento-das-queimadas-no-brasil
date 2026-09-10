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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17dfb6e7-cac4-3812-b96a-146d2932d216 | -7.50715 | -45.26732 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a95cc71-a49d-38b0-b10a-779555cdea7c | -6.28131 | -41.69918 | 2026-09-10 04:25:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1ef17b70-d649-36a4-a891-f3f8046d40e5 | -3.24412 | -47.24996 | 2026-09-10 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4eec12af-97e1-3b36-be49-2dd70dc0afa2 | -6.24253 | -51.68399 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4b37b79-c151-3977-95a3-8b74883248cf | -6.17443 | -43.01954 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b10c3a25-8d86-310d-aebd-83546f84bd42 | -6.76527 | -44.56721 | 2026-09-10 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cd7a7c3-b19d-3a8a-ab36-dc338cf55b0a | -2.72888 | -57.63618 | 2026-09-10 04:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| aac8defb-1f80-35c8-ab36-5108501e6676 | -9.30537 | -44.34937 | 2026-09-10 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe6e3b19-3892-33d8-a770-110211c95507 | -6.82056 | -58.98924 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ef1f2111-54d6-3df2-a502-91a817746955 | -6.42237 | -43.06866 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58a18ba7-1b39-3768-ae74-1e9e909c8bb9 | -5.41081 | -41.83989 | 2026-09-10 04:25:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3a2aa077-b80a-3db3-a365-cfb721ad554f | -7.10517 | -42.13034 | 2026-09-10 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f0145998-eae7-3668-b57c-d61a2ae2877c | -9.3275 | -45.63398 | 2026-09-10 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a595563-53f6-319a-98f5-bd7ec5ffe2d3 | -5.75963 | -45.08403 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 407f8c13-9fb4-379f-ba94-722faad7efce | -3.24052 | -47.24939 | 2026-09-10 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bf3602d2-4e1f-374c-ac19-8c880ee942dd | -5.7679 | -45.07469 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0c4e448f-97ce-34a2-b955-0f5bde1e8827 | -9.71393 | -43.4009 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 53823248-3005-3bc4-b72e-5b86440aedc2 | -9.68797 | -43.4322 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4c3e4853-6719-3f46-abb0-5145c3114650 | -6.71838 | -46.32849 | 2026-09-10 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef8843ce-8cf5-3b10-98eb-dddf64ffaffb | -2.94139 | -50.46232 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90aca46c-6353-3554-ab36-04220bb71c9b | -6.51021 | -43.96533 | 2026-09-10 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12d8b7dd-09f6-38d0-bf80-e322203f13df | -6.26522 | -46.36734 | 2026-09-10 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f42f666-cd02-3535-9b56-1cddad36ead1 | -4.00549 | -51.03012 | 2026-09-10 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 779bfb7d-382c-3508-b67d-a21169f74334 | -9.69893 | -43.4064 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ffcf4131-411c-3842-8179-92cd96fd0dc1 | -9.69317 | -43.46816 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 50a4ca26-037d-36af-9df7-5a8cd0ee0bab | -7.1134 | -42.14817 | 2026-09-10 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 21db909b-5300-3c13-9da0-b88be1989073 | -8.82409 | -46.92646 | 2026-09-10 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca5fefff-7a70-30ce-b26c-7229dd9e65b9 | -9.30482 | -44.35293 | 2026-09-10 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 398b5df7-0119-3a55-9482-d2c03b8a9477 | -6.2658 | -46.3637 | 2026-09-10 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bd3b9e1-6f1c-3683-91f7-ff5a35513e66 | -2.93556 | -50.47023 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bcd4369-3c35-34e3-a6d5-bd388cd1e96e | -5.27956 | -55.96072 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26998d41-1be3-382d-a30f-6ecb7b777a5d | -6.23957 | -51.67383 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 093be4e4-b55f-38e8-aee7-1d52d05ac178 | -7.75092 | -49.1981 | 2026-09-10 04:25:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 836b32f6-1d18-3480-a322-b6bcfc3b8948 | -7.56775 | -47.20584 | 2026-09-10 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b9d2051-cff2-37d2-9131-3b40443deb75 | -7.66789 | -42.16359 | 2026-09-10 04:25:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 57f1a828-a803-3153-add5-8f7f72743770 | -9.33633 | -45.64258 | 2026-09-10 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a53d8b2a-4dab-381c-89c4-7d0f35286fc6 | -4.86166 | -56.0102 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b28599dc-6f72-31c0-b727-6dddb76c9e26 | -7.12612 | -42.11269 | 2026-09-10 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 31e98175-f650-3ede-9f32-5645764b9c1b | -2.72302 | -57.62815 | 2026-09-10 04:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bacb5825-d83b-31b7-9e4c-c92595aa8659 | -2.73349 | -57.63675 | 2026-09-10 04:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4af3f2d2-f428-3335-8f39-afc880d92006 | -6.16316 | -44.63874 | 2026-09-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 84c98c1c-3350-335a-ad2b-f3b1f7a376ca | -6.16709 | -47.08198 | 2026-09-10 04:25:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 398cdda6-6315-3da7-b300-b737bdeb2fcd | -5.77231 | -45.06829 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83088f22-dac7-35b7-8d12-53071f43f244 | -7.68516 | -44.31109 | 2026-09-10 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b380a32-8b01-3c83-9187-3d0969d27a32 | -2.93997 | -50.47098 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a784cc82-b8a5-3464-90e6-f20b497d163a | -3.95815 | -49.015 | 2026-09-10 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de76e6dc-fffe-3303-8702-7938006ea17b | -6.82571 | -43.04146 | 2026-09-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60b85473-daee-3844-bcdb-af99e15d382a | -7.10036 | -42.13793 | 2026-09-10 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ecacfffa-4ef7-35b8-8203-05ffec7e3bff | -2.70659 | -49.51032 | 2026-09-10 04:25:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b21447c8-20f8-3d5b-8829-485a4d8e8afe | -5.14643 | -43.84916 | 2026-09-10 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 119a22b6-b263-3f61-8104-6def4c5e3e16 | -4.85954 | -56.01552 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f5d6e96b-6608-3057-9f53-57182c2baeba | -4.03408 | -50.88822 | 2026-09-10 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9295b42d-6391-37c4-99a9-38d2aa8f449f | -3.54635 | -48.18403 | 2026-09-10 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f4391a0-a0d2-3e96-ba28-34ab16352700 | -9.5926 | -40.36019 | 2026-09-10 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2aeebd2f-57ae-3572-8ac2-d353effc350b | -7.9812 | -43.97552 | 2026-09-10 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b2ad8c0-3250-3caf-b88a-2f80b31be93d | -5.55332 | -43.4361 | 2026-09-10 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04b6ebb7-44cf-3945-ae73-6e05f06893d9 | -2.93187 | -50.46517 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4df2b73-42d7-37b6-9ba4-23202de6caa7 | -4.73513 | -44.94592 | 2026-09-10 04:25:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf34ddcb-3634-30b6-907c-405c35195ac1 | -4.85326 | -56.01498 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5f8d7fa0-b68b-34f2-9f9e-b54048b99315 | -7.57404 | -45.68067 | 2026-09-10 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b8bbd44-9a5d-3f26-bde5-0cd3fffd0353 | -7.74638 | -49.20207 | 2026-09-10 04:25:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 88e9613a-e955-369a-9d7c-af76e72bb567 | -6.77736 | -58.90691 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82df91e4-5dec-3717-86b1-dc6b9d854b53 | -9.30817 | -44.35345 | 2026-09-10 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 252bfdfa-b407-32e0-853e-3e92c8975ba3 | -8.09008 | -54.85621 | 2026-09-10 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8773bd1b-cddb-367b-a5fb-625337cd5c60 | -8.0853 | -54.85149 | 2026-09-10 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9359828d-2d95-3a54-8ee3-090ccda5aebd | -4.3615 | -47.77544 | 2026-09-10 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e02f2bf2-cdae-3e25-88da-38738ea602e8 | -6.76196 | -44.56668 | 2026-09-10 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7988ca9c-d014-3e1a-b30d-65c657536aa9 | -8.69012 | -47.9812 | 2026-09-10 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 526dbb94-1485-308c-878f-d3631fc7c9af | -7.1182 | -42.14061 | 2026-09-10 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b7d6ff26-fb8b-3e29-b78b-114d66ea0a36 | -8.7119 | -44.7136 | 2026-09-10 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3af7ad26-c8c6-37fa-b57e-3509898f7b1f | -3.24771 | -47.25054 | 2026-09-10 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 854955e3-85f8-371f-8b14-76db17c6becc | -8.83239 | -47.08894 | 2026-09-10 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a237bbdd-ae46-37aa-9340-798504cc0bf6 | -2.91429 | -54.1125 | 2026-09-10 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff081398-a4e3-3d11-b171-cf05e95c8556 | -1.70648 | -53.6958 | 2026-09-10 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17fd29d1-2591-3c09-810f-1b692f52e659 | -7.25881 | -45.35525 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| be38aaaa-340c-31fe-87b3-abece0b4dcc5 | -4.03854 | -50.88895 | 2026-09-10 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b591034-1af8-3de7-b73d-b0bbd1deb4de | -7.99349 | -43.96273 | 2026-09-10 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9cda5580-1489-39fc-ab98-05afbe414089 | -9.32364 | -45.63693 | 2026-09-10 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aeee78e3-9b68-3d3e-9a18-077705311f2d | -3.54709 | -48.17945 | 2026-09-10 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8a9bfb4-bc11-36cf-b3f8-fccdf8d47d8e | -7.52953 | -44.99729 | 2026-09-10 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 220eed47-f72a-33fc-b026-985ef7c42f7d | -4.49521 | -42.55455 | 2026-09-10 04:25:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ed7c80ab-d8b5-34f7-8296-bb88dbe0fbb6 | -3.36898 | -50.74491 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af21d7cf-540b-352e-a999-b0da54a47a98 | -6.17726 | -43.02383 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b36a525-9c21-3a1b-9888-7df87e928bb4 | -5.60964 | -44.85155 | 2026-09-10 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14325321-1035-3ac4-bbb9-9d74824c26e7 | -9.30147 | -44.35241 | 2026-09-10 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0da666f1-87ef-3fb5-adcc-6bad16cf6fe5 | -5.60743 | -44.84413 | 2026-09-10 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d48cb60-1ffd-346a-b408-a247cbcf74bd | -8.97821 | -44.40104 | 2026-09-10 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb17d253-2665-3e9f-8658-5e140ffda304 | -9.7768 | -43.4454 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb9ae70f-ac95-3912-8581-2cb23f170a7f | -6.0959 | -44.13727 | 2026-09-10 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6345724b-dbe2-3ba8-afc8-fe90eacc719e | -8.97487 | -44.40049 | 2026-09-10 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3baee315-c90c-3f0d-9ef2-c82ff3b8a63f | -2.82686 | -49.22772 | 2026-09-10 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bdfd8b7-731d-3377-b35b-ecd9bc88d6ec | -5.55723 | -43.43307 | 2026-09-10 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ba7eee2-97f2-34bd-b786-41eefe02f525 | -2.35744 | -52.69371 | 2026-09-10 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d2807d5-d980-337f-9f7a-423cc48e1b01 | -8.83578 | -47.0895 | 2026-09-10 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 309079e3-a3e2-3e5a-8189-751710dbe1a9 | -4.8604 | -56.01075 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 69ffb59a-c7d2-3100-9edb-b696fc657cc7 | -7.98235 | -43.99035 | 2026-09-10 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bd5fd72-3c8d-329a-a552-f478c8431eac | -6.74915 | -45.48367 | 2026-09-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1744b01a-abc9-37ac-9fb5-a09d06b2215c | -8.09139 | -54.84886 | 2026-09-10 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ac18ab1-79c8-3042-8f2b-35309005a48a | -1.7009 | -53.69475 | 2026-09-10 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f952639-890a-3b3d-afc9-bbda249028b0 | -6.46644 | -46.29558 | 2026-09-10 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README24.md)
