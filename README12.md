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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52f50563-b9e5-3750-88f2-25cb9c2454b0 | -5.74543 | -45.17483 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95fb7710-ae6b-36d2-a949-d6e55430b705 | -6.07771 | -47.29474 | 2026-09-30 03:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47cb959f-7ed6-30df-a4c3-68572d687cbb | -8.33882 | -44.16404 | 2026-09-30 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0d642a7-d151-33a8-bdb4-65601b374ad7 | -11.17566 | -44.832 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eb15015e-74a3-3f50-beae-bdbbe90f80c7 | -6.86238 | -40.94359 | 2026-09-30 03:55:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1661572e-1ea9-32b8-8f16-87fc03d0fce6 | -10.70883 | -50.83543 | 2026-09-30 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a6d364e-4aca-3125-a4e9-0522b88eb0cf | -5.82017 | -46.22089 | 2026-09-30 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0eb9ea4-4630-370e-8c28-44759b645b8c | -5.73798 | -45.16391 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 46fae51d-3ceb-3f9a-9a26-2b8a14ed1251 | -3.56648 | -50.25681 | 2026-09-30 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c585b53-aee0-3b19-94cb-d8239f105270 | -11.68301 | -43.52916 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9a64fe2-20b9-3dac-bb7c-f27994cf77c8 | -4.80994 | -45.64196 | 2026-09-30 03:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d2ede250-fe3b-31b1-bd06-31139a0ddf27 | -7.9287 | -45.44204 | 2026-09-30 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 16d5e100-a6a0-3844-bcf5-face2d8b1fdc | -7.07907 | -41.75743 | 2026-09-30 03:55:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| be45342d-9850-367d-bf72-261b2cfba8ec | -11.17619 | -44.77632 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80e1c053-0c5b-3ecd-b3c0-be465fc4c5a2 | -7.02038 | -44.61612 | 2026-09-30 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8792ae75-f76f-3724-96eb-af4ba5d48cfb | -5.7417 | -45.16939 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59de5d6e-e01a-3e7b-ba80-d3339896b991 | -11.18406 | -45.11802 | 2026-09-30 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08170f07-b39b-3865-bf13-700e53404225 | -4.45995 | -47.92398 | 2026-09-30 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 251c30d0-2d09-32fb-ad22-57e78762f48b | -9.06866 | -49.86771 | 2026-09-30 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ad113b51-fe26-3ca5-aab1-3909d188089c | -7.82269 | -45.82744 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 1fd6d0cd-9dce-3923-8444-67f5242e6d44 | -7.02687 | -44.62957 | 2026-09-30 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41303c1b-9d2e-3a5d-9910-dbbff2ab3864 | -11.80989 | -43.31184 | 2026-09-30 03:55:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 234af67d-61c3-3ca7-b636-f04e19d0bcd8 | -9.80629 | -44.83162 | 2026-09-30 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| adb90ed0-c444-37f2-b1a7-39a241241154 | -11.25673 | -43.54108 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67f409c9-be80-3c93-af25-5554f245d060 | -5.55845 | -45.33397 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac79ef3e-cdfa-33df-a3c3-730a2ce0d00c | -11.1682 | -44.8231 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| f0cdc1bb-1a0b-3356-baca-e4f230d5aef2 | -11.62507 | -43.53304 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ab6f850-dc20-3dec-a84f-28fdd9f240eb | -4.12423 | -46.87206 | 2026-09-30 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 71988384-2ad2-3274-ba40-dc2f2affec8a | -4.12948 | -46.87268 | 2026-09-30 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b7266047-5cb9-36f2-a964-7517de18def8 | -9.12415 | -40.64148 | 2026-09-30 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8895109a-1ec1-367d-9b3c-b54f57b67adf | -6.8242 | -45.05087 | 2026-09-30 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| adf4a76e-bd54-335f-994d-208a7989789b | -8.25144 | -45.43485 | 2026-09-30 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 415cdb47-298e-38ef-b7fa-3d404c686887 | -10.1108 | -43.92725 | 2026-09-30 03:55:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ce2fbf7-7833-3f41-ab9d-a41dd0d8fb2e | -9.66509 | -45.11724 | 2026-09-30 03:55:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b4d35d08-ea3a-3cfd-a02e-aabc9f493f9e | -7.81716 | -45.91484 | 2026-09-30 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 413e3644-0bbd-3943-a2ee-a39fb7f92ca2 | -7.85012 | -45.83185 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| b2b443dd-4018-36e4-9348-df5e8e4d0012 | -3.37314 | -50.95916 | 2026-09-30 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ce4c9475-6a11-33cf-a505-f6847d8cfaa8 | -10.08682 | -50.31059 | 2026-09-30 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02d66672-fb49-3b0f-9309-e1e4f460efc2 | -10.73324 | -44.43787 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a880638a-fd84-3f12-b51a-5f344965a479 | -6.9255 | -44.56025 | 2026-09-30 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b806de27-e322-320d-bae0-63812ad95d7c | -11.39588 | -43.47515 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 62351dca-1c40-3b16-81b2-0fc324d5b4e3 | -7.03119 | -44.28951 | 2026-09-30 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a1a3b61-31c6-33f9-8d92-3e4c1417d7c9 | -11.19187 | -45.14618 | 2026-09-30 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a327e489-f78f-3497-a93b-aed1f32096dc | -10.13226 | -45.13206 | 2026-09-30 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d01e3d2f-5fc1-3e33-a56a-9314f1def1da | -10.15155 | -36.24086 | 2026-09-30 03:55:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c050a8bc-bb84-3f5d-8a47-a2c91bad3e5f | -10.07923 | -50.31816 | 2026-09-30 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ad6d3eec-a9f9-36c3-8f10-ec33d04449e1 | -7.5142 | -47.33746 | 2026-09-30 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1f7b4dfa-88f8-31d1-8b3e-74eb60588ccf | -11.38865 | -43.38186 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5dd49f01-007d-36a6-b29d-307f9400e586 | -11.37689 | -43.36152 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 41dace06-2734-3441-88e7-7d8e38a938a7 | -11.12137 | -43.27031 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ae81f77b-b79c-3db3-bf9e-08f88703a73c | -9.79175 | -44.81746 | 2026-09-30 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7175a64-3547-3b18-b229-6b0a74fef572 | -8.98536 | -44.17435 | 2026-09-30 03:55:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04d95ff2-cc79-31af-8a94-23233bc74ed7 | -10.73383 | -44.43449 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a0fde104-24ce-3652-8297-93d936e0053a | -10.21947 | -44.64508 | 2026-09-30 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a81d46a-95c1-3da4-a641-30e4f194bdb3 | -11.62878 | -43.53369 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c770dffb-b441-3111-b462-fb1c6eadacfc | -4.81394 | -49.4637 | 2026-09-30 03:55:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 205bedfb-f86d-3685-99a7-b1324275ed22 | -4.81466 | -45.64286 | 2026-09-30 03:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f6a6408b-fbeb-3128-9f84-44eb6bca2c21 | -4.6012 | -43.54053 | 2026-09-30 03:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6cc9786-ec9e-3cc1-b031-ac03c1e65ebc | -7.53716 | -47.12133 | 2026-09-30 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e5d7f62-b936-301d-9e9b-755096baf8a2 | -11.38701 | -43.45975 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7bddc2c-4b1b-3912-8117-f85c0f671f83 | -11.39085 | -43.39139 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0deb30eb-4560-3d8c-ac07-4a64464fe79b | -11.1601 | -44.77347 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6cac051-8bc7-3068-bf39-e20bda0d6957 | -3.36165 | -50.4683 | 2026-09-30 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47512cab-e11c-3e34-a16c-59d254e0bc15 | -4.46578 | -45.58331 | 2026-09-30 03:55:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3377569-6463-371c-82bd-4d371526337a | -5.12838 | -49.32891 | 2026-09-30 03:55:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0f48aabe-1af4-3b07-b731-8e03d67d1100 | -11.71063 | -43.45558 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3dbcecf-f00b-3b23-8dbb-689b1c70f99f | -11.71138 | -43.45112 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4e25cf9-5f67-305a-83e8-f98a79d26a81 | -7.81894 | -45.82191 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d4559815-85b3-36a8-a3af-dd090ca1f8ef | -11.38921 | -43.46938 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9d86e7e-022a-32ac-9757-60aea5be4748 | -11.71582 | -43.4473 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f65840c2-b405-39fc-9a23-b9eff273963e | -7.52761 | -44.54539 | 2026-09-30 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e006524-ff66-353d-89fa-8cbdf3a6ecaa | -11.25902 | -43.52743 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b43abd98-fd54-32e4-8d65-d859070b2bd2 | -7.48491 | -45.79009 | 2026-09-30 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd6529d9-1865-34cf-9684-b00649544664 | -7.08106 | -41.74516 | 2026-09-30 03:55:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0108ff6a-34e0-34d6-9046-54ad02b27cb8 | -9.15431 | -46.76344 | 2026-09-30 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3b086f08-0b68-3a14-b6de-cafb250bd614 | -7.82893 | -45.81844 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 09f1693a-c54e-34b7-9adb-b9c9f723bd52 | -7.81813 | -45.82663 | 2026-09-30 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 5186b12c-4958-3a4f-9c04-509e3798326c | -11.17503 | -44.83181 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 92e0599d-d23b-3db4-bdb8-82b8e0e689ff | -5.09736 | -46.04506 | 2026-09-30 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1d3bd916-a6a5-33d1-94f3-f81d7a1deecf | -6.70477 | -45.63533 | 2026-09-30 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54aedffc-7a61-34b1-ad65-c515fa4a3ef9 | -5.73688 | -45.06109 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b3e011c6-915e-3457-bea5-cad4c4168d3a | -6.30459 | -43.60297 | 2026-09-30 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 65b26458-ba37-39c6-9aec-0941ead03dcb | -8.25114 | -45.43943 | 2026-09-30 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 61cc5f2e-036e-3b44-99f4-ddb6537b678d | -9.92302 | -50.23043 | 2026-09-30 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a4a4ca8a-9d7a-332e-81e4-7a5a14b26133 | -6.92974 | -44.56101 | 2026-09-30 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c212e5c5-94be-3913-bec5-0acba2d0c8d6 | -5.73267 | -45.16786 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2991142b-d698-3f84-a5b8-e833dfee348b | -6.32697 | -51.16623 | 2026-09-30 03:55:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8fc3eeac-d227-3b94-9283-df4bc267db03 | -11.68311 | -43.50602 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25d0a2c5-80e3-351d-9141-2dd3a0688492 | -10.77861 | -47.72234 | 2026-09-30 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 044791aa-6118-3d82-bfb7-b8bda83292d4 | -4.4606 | -47.92027 | 2026-09-30 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 849a339f-3b92-35e5-81ca-720224191725 | -9.6603 | -40.58708 | 2026-09-30 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 3a6093fd-7a79-3ed1-be89-4d62f14e8aa6 | -11.26275 | -43.52806 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 06efa3d5-ba53-355b-84f7-6c79eccc7a0a | -6.0772 | -47.29053 | 2026-09-30 03:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c766ce3-4e14-3dfb-a8ac-f91ea27f39f3 | -5.73038 | -43.28153 | 2026-09-30 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 203aec79-7477-37d2-a295-b70a04658588 | -7.4887 | -45.79543 | 2026-09-30 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2743bc40-b63a-3474-b9c3-64a70bd68831 | -11.41073 | -43.47769 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 718f3e28-d3f1-3322-95de-da5b9b2d14aa | -11.41596 | -43.42326 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c07b683e-34ed-31b9-a08f-449b6dfb55b6 | -11.42885 | -43.42831 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b508ec0-d5f7-364c-8c68-016a341d8b9d | -11.43179 | -43.43341 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3d0abec-d8b9-3244-8de5-8c8d7e8651b8 | -11.44506 | -43.4449 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README13.md)
