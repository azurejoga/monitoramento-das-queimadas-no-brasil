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

## Dados Diários - Página 409

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e261d5c2-49f3-33b6-98f0-fd8a08ca2844 | -3.1114 | -53.7839 | 2026-10-08 19:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 423415ae-246a-3beb-adc2-0035a8c35c31 | -2.572 | -56.1646 | 2026-10-08 19:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 8d457365-3304-3006-8a0f-75f5d8400936 | -1.1094 | -54.1802 | 2026-10-08 19:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| f93f0313-89df-3187-b854-60b8a95af9f0 | -2.7613 | -54.0941 | 2026-10-08 19:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 454bca49-60ff-3d84-b669-025fc9929388 | -6.895 | -43.7066 | 2026-10-08 19:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 109.7 |
| e12bc62c-87d9-3462-bbd1-493b6f273a99 | -5.9267 | -51.8151 | 2026-10-08 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| c26237c2-f863-3fe7-b894-8a8a2505771f | -8.537 | -66.9764 | 2026-10-08 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 333.6 |
| e4057f38-4870-33cc-a1ad-2bce382d1d6e | -2.4987 | -56.1659 | 2026-10-08 19:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 4ffdb0ae-e706-31f3-b656-28fac21f9ee1 | -7.1827 | -52.6078 | 2026-10-08 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 1fb80494-c634-3f52-96b7-8419cd5468af | -6.0857 | -55.7171 | 2026-10-08 19:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 3f2130a5-77ad-34d7-96f5-2f7d04a197f8 | -3.2955 | -53.7185 | 2026-10-08 19:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| c608d12d-361c-3dad-93c5-d560ae7ca2ca | -2.7428 | -54.1146 | 2026-10-08 19:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 262.7 |
| 5e7d9afd-1705-3444-b25b-6935ac6dc133 | -3.095 | -59.2024 | 2026-10-08 19:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 149.4 |
| 617eb1aa-a0d9-3252-8d55-a870f1c947fd | -11.2259 | -45.3064 | 2026-10-08 19:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 522626e4-4ed0-3fe1-88a6-2d8fcc8f412a | -5.9266 | -51.8358 | 2026-10-08 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 201.9 |
| f439a2ec-c6c1-34cd-aafb-9009595766f7 | -7.0892 | -52.6753 | 2026-10-08 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 265.5 |
| dc17234b-7c5a-3afa-bd44-45f5e85d96c4 | -5.5146 | -42.8399 | 2026-10-08 19:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 116.5 |
| 3f934ad0-6b89-33c7-8283-1cf213807e93 | -8.1985 | -46.431 | 2026-10-08 19:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| d4ca6716-a5e1-3df8-8ae0-9c3ca15e0a63 | -3.1971 | -50.5801 | 2026-10-08 19:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 121.8 |
| f177aac3-dd1a-3f96-9131-2a02535a30eb | -12.2316 | -44.7427 | 2026-10-08 19:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 1cbcb92e-67c9-300a-b971-1b131dd73a28 | -5.0945 | -46.2282 | 2026-10-08 19:30:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 632e9237-7cba-3002-94e8-081c84a5c4eb | -3.8598 | -44.1504 | 2026-10-08 19:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| b22a567d-36d0-3851-81e0-4433aea35a56 | -4.1025 | -44.1149 | 2026-10-08 19:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| e4382476-e449-3f09-9e7e-6a5b4290a533 | -8.9772 | -45.9249 | 2026-10-08 19:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.5 |
| d0ada6d9-793a-3800-9813-585c53734e18 | -6.4905 | -55.9563 | 2026-10-08 19:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 251.3 |
| f41a2bd4-461e-344e-8086-e7d0a73747c9 | -1.3264 | -56.398 | 2026-10-08 19:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 229edd96-0d4e-3ada-81f4-6ffa17800c73 | -2.5492 | -58.0373 | 2026-10-08 19:30:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 157.7 |
| b1227c77-f021-3cf3-979a-663af8bc5d21 | -2.8712 | -54.192 | 2026-10-08 19:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 5c921014-769f-30da-86ee-844e782f6e16 | -11.7742 | -43.5245 | 2026-10-08 19:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 962b773e-ff17-3ddb-a2c5-970c83e16bf3 | -11.2267 | -45.2604 | 2026-10-08 19:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| b081965b-aa21-38e0-bb27-332641bc8c61 | -6.1615 | -47.9419 | 2026-10-08 19:30:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 146793b6-fa8c-35eb-9828-8640587e9ce5 | -3.1951 | -42.9538 | 2026-10-08 19:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| e293be33-2756-3f99-bcdb-4e3a077a8ade | -6.498 | -43.9501 | 2026-10-08 19:30:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| fe7ea441-e84d-3f9f-a958-438a4054aab5 | -11.7738 | -43.5482 | 2026-10-08 19:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| bc8eff11-1688-3819-8e42-0916c3bf66e6 | -6.4413 | -55.0224 | 2026-10-08 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 139.1 |
| e4431157-ae1f-37fb-9a1c-8e4e8fb24468 | -12.2311 | -44.7661 | 2026-10-08 19:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 182.4 |
| f4e4b29e-dbea-37e8-b05b-e49dab5da372 | -9.0173 | -44.3676 | 2026-10-08 19:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 4ca0b0af-1e85-3141-9163-a1a2279fa87d | -3.1114 | -53.8041 | 2026-10-08 19:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| d383eb25-a8af-322e-b9b6-afbbbefdb73e | -3.3134 | -53.8592 | 2026-10-08 19:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 94b74106-581d-3882-8b36-6051806b6baa | -5.6935 | -53.4464 | 2026-10-08 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 165.8 |
| a622f0af-1ea1-347b-b9fa-48248b947cba | -2.1361 | -54.4671 | 2026-10-08 19:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 39504b1b-037d-3b52-bef6-c8c3efc35642 | -9.9208 | -44.7893 | 2026-10-08 19:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 9c98bbf0-acb4-36ee-a818-c242cce62140 | -11.6387 | -43.5929 | 2026-10-08 19:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.3 |
| fce019e0-fd26-38b2-87f7-9450274ffa58 | -6.2541 | -52.683 | 2026-10-08 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 206b87e9-e571-3c7e-9ee4-aecebb64abfc | -7.9086 | -54.7194 | 2026-10-08 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 144.0 |
| 6353d0f1-7031-3b6c-9a75-ca8ee205a086 | -3.1787 | -50.5807 | 2026-10-08 19:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 236.9 |
| edf3b293-afa7-398a-b8ee-2314514c58eb | -5.8599 | -53.4586 | 2026-10-08 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| a4c607da-2673-3ef8-a899-66ed2c97fdeb | -3.1786 | -50.6016 | 2026-10-08 19:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 164.0 |
| 8ee53b26-17e8-374b-b1a8-7aca96606aa5 | -7.7579 | -54.9499 | 2026-10-08 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 828ff6d2-69ee-3d7f-99ce-54d28c93b05d | -1.1094 | -54.1601 | 2026-10-08 19:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 7c84d585-3f7d-3928-a127-7a1c62974721 | -3.2717 | -50.3893 | 2026-10-08 19:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 22fd64d8-4b7d-3f66-a12b-e7137c22cdb4 | -6.2527 | -52.8675 | 2026-10-08 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 155.5 |
| 508970c2-8976-3009-81e6-482bf9256453 | -9.0173 | -44.3676 | 2026-10-08 19:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 35ae7a97-de06-3d16-894b-ea42713faaa7 | -6.4411 | -55.0424 | 2026-10-08 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 363.2 |
| 12ea0fca-5683-3f21-a6fe-8f8a2ade68c0 | -14.4591 | -41.1854 | 2026-10-08 19:40:00 | GOES-19 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 114.0 |
| 10d783c4-bc08-3dd2-817d-127cef453e93 | -3.1115 | -53.7637 | 2026-10-08 19:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| f626f5bc-a5e0-33f7-9138-367d5db14ecc | -3.4312 | -56.9502 | 2026-10-08 19:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 47a753e3-b155-359e-b72e-0fab29b3c4be | -5.9267 | -51.8151 | 2026-10-08 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| d0340736-67df-3398-893a-e8d62dbc56f5 | -6.2157 | -52.8695 | 2026-10-08 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 8fe75871-2809-3fd5-aadc-d73bf3505900 | -3.095 | -59.2024 | 2026-10-08 19:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 124.4 |
| e251638a-a972-3551-9a17-3ccf25aa4d1a | -2.4988 | -56.1462 | 2026-10-08 19:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| bd807e81-8659-3285-b7fd-8201f359f943 | -7.1825 | -52.6283 | 2026-10-08 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 188.8 |
| 71b0b9cd-ecf7-3a14-a8a4-e78f489210ca | -8.0575 | -45.6357 | 2026-10-08 19:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| febc6b70-e648-3014-a2b5-8b64197d164d | -3.1879 | -58.6433 | 2026-10-08 19:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 719cedd5-3ee4-372f-97d4-effa7a44684c | -3.8911 | -42.1187 | 2026-10-08 19:40:00 | GOES-19 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| f86de693-8b48-3693-9d3c-e52a270abe4c | -11.7545 | -43.5512 | 2026-10-08 19:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| b1084e8f-f422-32e7-a8f7-bcd3d945782c | -5.3905 | -44.1968 | 2026-10-08 19:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| c5e9a470-940d-34bb-91bc-f4ee723c4508 | -2.7612 | -54.1142 | 2026-10-08 19:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 544b2cce-3c37-3456-9456-d40804e9db00 | -6.8319 | -39.3213 | 2026-10-08 19:40:00 | GOES-19 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 82.7 |
| 8fa5c82e-bebf-3122-b6f7-eecd8581d34b | -5.9586 | -55.3648 | 2026-10-08 19:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 131.2 |
| 32950d2c-70f7-3864-b63a-a65c71b5f743 | -7.1827 | -52.6078 | 2026-10-08 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 140.1 |
| 69343098-1c4d-3919-8eb1-a3b6c512be59 | -6.2526 | -52.8879 | 2026-10-08 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 75779a3d-78b5-3c30-b183-e73a64fa0ad0 | -3.314 | -53.6979 | 2026-10-08 19:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 79dfba76-8682-321c-8661-874912683278 | -5.8599 | -53.4586 | 2026-10-08 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 139.1 |
| 2c3357a8-a266-361b-8a4d-be5a3743fb7e | -6.1226 | -55.7154 | 2026-10-08 19:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 4937abb2-a562-39a6-a779-d0f31acae624 | -8.2176 | -46.4068 | 2026-10-08 19:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| ce078dfb-b751-374e-ac52-a52fccf54e62 | -4.4216 | -49.6707 | 2026-10-08 19:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 6be6d083-554d-3bac-843c-b1bec465fd7e | -5.8842 | -43.4199 | 2026-10-08 19:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 154.7 |
| d3697e10-a946-3524-aec1-37449e7c359d | -2.5903 | -56.1642 | 2026-10-08 19:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 25218c4a-82b3-3d72-b829-ed471fa94cc6 | -8.5722 | -67.4569 | 2026-10-08 19:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 110.3 |
| f4f11902-b661-3646-8921-455ab07507ec | -1.3277 | -55.4525 | 2026-10-08 19:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 95305b86-5c05-3839-b945-718c1d543a53 | -3.7826 | -44.6113 | 2026-10-08 19:40:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 69a79673-d46f-3079-91c4-d4b05b5effb4 | -2.4806 | -56.0678 | 2026-10-08 19:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 1665315e-0ecc-3018-be05-aadab09df446 | -3.3912 | -58.0017 | 2026-10-08 19:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 6e7f0093-5bbe-3d8a-8b79-8e5f2eec6c94 | -8.1985 | -46.431 | 2026-10-08 19:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 291bde87-2cee-3d74-96bc-ad658e9c443f | -7.7579 | -54.9499 | 2026-10-08 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 693fbd7d-d715-3ce5-a27b-161255b4dc65 | -3.2136 | -42.9764 | 2026-10-08 19:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 143.4 |
| d4faf79d-5b29-30fc-bbb6-cee2cc418d6e | -8.9775 | -45.9023 | 2026-10-08 19:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 0f91e837-27fc-3679-9248-de3093cc1ede | -2.4806 | -56.0875 | 2026-10-08 19:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 547774c2-a9fe-362a-9c9b-21a3f041f5b7 | -9.0359 | -44.3885 | 2026-10-08 19:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 8a9df2fb-c538-3783-8623-f007d55858cf | -14.4585 | -41.2104 | 2026-10-08 19:40:00 | GOES-19 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 116.1 |
| 7d941d2b-eb2d-3609-8ac6-6a4680c7d5d4 | -6.0075 | -53.5122 | 2026-10-08 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 06070a97-d528-39ff-81fc-8cf688aef567 | -3.8598 | -44.1504 | 2026-10-08 19:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 36c5ffa4-9e85-3af3-ab4b-66472c12b26a | -4.6642 | -56.2083 | 2026-10-08 19:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 93399a7f-0541-3ea8-936a-fb6b3ea0a2d6 | -3.93 | -56.0143 | 2026-10-08 19:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 86c3ee4d-1a1b-384d-8c33-424755dff6de | -4.1458 | -43.187 | 2026-10-08 19:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 984fe73b-8e80-3fb9-aded-a29f1abedb1b | -6.0021 | -40.9594 | 2026-10-08 19:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 221.2 |
| 3a45ab64-0ec1-3542-860f-e7025d4ce388 | -6.0857 | -55.7171 | 2026-10-08 19:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 35b13ed9-a82e-320c-9658-08b8a5282afc | -9.9007 | -44.8608 | 2026-10-08 19:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 302.1 |
| 098f6d40-2c0a-3482-ba99-8d2db4f161e0 | -11.619 | -43.6196 | 2026-10-08 19:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |


[Clique aqui para ver as próximas entradas](README410.md)
