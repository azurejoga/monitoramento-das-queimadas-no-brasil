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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a07c941f-9a2d-3202-9dd7-2b6d054f5830 | -7.32845 | -48.49367 | 2025-09-06 03:49:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9051e19-4fdd-3788-9469-e45fd3ea73ea | -6.54466 | -49.50322 | 2025-09-06 03:49:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ff1f2ec0-8d0e-31bf-af9f-dcae8b272d92 | -7.69368 | -50.28486 | 2025-09-06 03:49:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ecc4d680-122f-3c80-bb60-d793dd6c7c01 | -8.34217 | -46.95442 | 2025-09-06 03:49:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a4341a2-5b00-329d-a9b3-9cc33819f27d | -11.01401 | -45.92801 | 2025-09-06 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39514982-74da-3a4d-9e1d-24d8de1f80cb | -6.59542 | -44.55088 | 2025-09-06 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8a8dc328-164f-37db-9919-39879e88c401 | -12.8961 | -48.01083 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3144aa0f-89ac-3d6b-b8cc-b5ba87fc9d66 | -10.6041 | -44.32413 | 2025-09-06 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 784e82f4-7b8f-398d-9a5d-8b25ba4daf48 | -12.01463 | -47.78269 | 2025-09-06 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df384b38-3ca7-3264-b9c3-58e606d8ba95 | -9.3787 | -48.18794 | 2025-09-06 03:49:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7d7920f-d00d-379c-bac7-549b3a244ed2 | -12.90557 | -48.01951 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3bf9fdf-5000-34de-b0f2-a8ec2de9607d | -13.98151 | -42.58585 | 2025-09-06 03:49:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d50513c5-1708-3d4b-9c85-505080dd3e7e | -8.9766 | -44.45092 | 2025-09-06 03:49:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46e6a2f0-e702-3fe1-a55a-881036c2d257 | -7.59987 | -44.66704 | 2025-09-06 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 14703d07-f688-3b7e-b3a4-1b26c53bbf34 | -10.06791 | -48.06885 | 2025-09-06 03:49:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 919e54ad-816a-3102-9cd0-152dea2c56a7 | -7.60379 | -44.67255 | 2025-09-06 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f177074c-448e-3a53-9082-38059ccdf9ba | -11.13218 | -46.34873 | 2025-09-06 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40438de8-260f-306d-985e-36b1a3f21e69 | -10.14603 | -46.23385 | 2025-09-06 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b90f2a4f-0b8d-311c-8620-bcbaaa82d79d | -10.74613 | -46.33999 | 2025-09-06 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e49343ae-d09b-3944-82d9-467c3a2c6d3d | -7.34595 | -43.95181 | 2025-09-06 03:49:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 88e91ea5-5af3-3a68-8d58-246f0aaf78c0 | -12.08882 | -45.69449 | 2025-09-06 03:49:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1e41fd0d-8530-381c-8248-d102f2562f79 | -9.40955 | -40.30648 | 2025-09-06 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 02ea9c03-703d-33ef-b874-8b6bf1fd0def | -7.60766 | -44.67838 | 2025-09-06 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e73f4dd-f819-3d38-9a52-101413780f85 | -7.05002 | -44.34835 | 2025-09-06 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4cf00d34-404d-301b-b0fc-017113c58228 | -9.68544 | -51.10427 | 2025-09-06 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 113ad89d-37f9-3597-ac64-50c34eb102de | -9.30655 | -45.4178 | 2025-09-06 03:49:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8db391bc-913b-379b-beaa-b1e7e96fe5ae | -7.83878 | -46.21244 | 2025-09-06 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c3c89b7-07ca-314f-b430-1e0596f3d752 | -6.54361 | -49.50879 | 2025-09-06 03:49:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fce51992-7f5d-3c40-8e16-98f4f7afee2a | -12.00522 | -47.7735 | 2025-09-06 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 55627a3d-6c80-3286-918f-0578e47c27b0 | -9.05309 | -50.45766 | 2025-09-06 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3283c826-a913-3b3b-954c-e51ae5d84ee0 | -6.60512 | -43.97906 | 2025-09-06 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f263b8a-6d5d-3cdc-a8c1-b47c9ff3f42c | -8.64454 | -45.74564 | 2025-09-06 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 072c27a5-d4bf-3deb-b25f-0721260592fd | -10.0318 | -48.13387 | 2025-09-06 03:49:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97e71c03-67fa-3de9-a6d8-9d1d09efdce8 | -7.21192 | -43.98507 | 2025-09-06 03:49:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2ee3d271-8b74-3e60-8ffe-e77e7d2c291c | -12.92802 | -48.04768 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c0ee100-b540-32eb-a877-e8213464506c | -8.4456 | -47.32401 | 2025-09-06 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a69047a4-7216-3c4f-bd39-95a71df5230b | -6.87849 | -45.55568 | 2025-09-06 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed180ccf-c61a-3100-8382-2d181c6f1251 | -10.31988 | -46.41242 | 2025-09-06 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6688a795-20c5-3eba-8544-1fd4dc99a9d2 | -8.0196 | -45.43478 | 2025-09-06 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ef6d9d26-bc6e-3de7-ac1b-07dee6fa3b9f | -6.40062 | -46.09627 | 2025-09-06 03:49:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85a20577-edff-3377-8beb-43a40d5212e2 | -10.61171 | -44.3329 | 2025-09-06 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3350f247-84dc-35c1-8dd6-fb1dbae8ca62 | -10.21938 | -50.52987 | 2025-09-06 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b5b4039-6a73-38da-8b94-9ade14438ba0 | -9.68283 | -51.11717 | 2025-09-06 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 002f88a3-5232-3fe9-a816-3c63f26fb2fd | -9.64258 | -47.09275 | 2025-09-06 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7faf15c-b79e-329c-a9bd-b8ef3a8a6828 | -12.91963 | -48.03333 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 719e9ca2-f0b1-33ef-bec4-cfd3c5a0e6e9 | -10.77797 | -47.75236 | 2025-09-06 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a78c3ba-761e-3af0-9a24-51863e296e36 | -10.77301 | -48.27795 | 2025-09-06 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 59ec672a-e198-33be-aea3-9695ee6a9614 | -9.06074 | -50.45386 | 2025-09-06 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 55e256d8-43fe-3475-8d97-f441e8e25b84 | -22.2424 | -48.7513 | 2025-09-06 03:50:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.0 |
| dbf50802-d2d0-3b14-be09-2f8601a39494 | -14.199 | -53.075 | 2025-09-06 03:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| abee4682-6259-3189-9ba1-1b3302dcfea5 | -22.2417 | -48.7748 | 2025-09-06 03:50:00 | GOES-19 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.9 |
| 9f11fee1-6775-3f8f-b7c5-cbecea75c1f2 | -14.18 | -53.0564 | 2025-09-06 03:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| c30826ec-21a9-3cba-8862-d6952d3d2b7c | -14.882 | -49.457 | 2025-09-06 03:50:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 72.2 |
| bd4e8d49-f65a-3280-8b60-b233482527de | -13.0044 | -54.8282 | 2025-09-06 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 057c72c1-c209-3792-9e0d-b5a756946ffa | -14.9015 | -49.454 | 2025-09-06 03:50:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 148.5 |
| d2f69ae6-46e2-304d-b6ef-fd3c5a9d7ef7 | -14.1797 | -53.0774 | 2025-09-06 03:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 27cc1aaa-71f2-3123-a19a-2363ba1c6660 | -14.1993 | -53.054 | 2025-09-06 03:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| fa064bf1-d59f-3d13-9023-149f6b253595 | -14.9019 | -49.4319 | 2025-09-06 03:50:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 053b2899-25c4-3d53-a794-9fec07a5be7c | -15.67186 | -45.88648 | 2025-09-06 03:51:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff9f6d54-e901-3a93-9326-395dd46a155d | -20.35353 | -48.64289 | 2025-09-06 03:51:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cd26df1c-d812-391b-bdc5-d3a336891c72 | -14.82823 | -48.1839 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 544b7feb-f608-3f26-ab16-eb96e30bcb86 | -19.79186 | -47.92462 | 2025-09-06 03:51:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef3f3d92-82a9-3f90-8907-edbbe3f5b0be | -14.90328 | -49.4474 | 2025-09-06 03:51:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 322914f1-27f0-3b34-a5a5-e38ebd30a0d9 | -14.58246 | -47.99857 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5317f12-c786-3893-a5cc-7186f041beb1 | -15.66958 | -45.88873 | 2025-09-06 03:51:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24cca9ba-69b7-3361-a1b3-f812c503b66e | -14.58202 | -48.0842 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77dfd1d0-383a-373d-abbe-59fa19cd5464 | -20.10584 | -43.82218 | 2025-09-06 03:51:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 143daadf-1851-317e-8e53-1415cd581a63 | -15.57725 | -52.91194 | 2025-09-06 03:51:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4c95d18f-e19d-3f3d-8d5b-3c166a7f18a4 | -14.79848 | -48.11597 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb5ccfb3-7806-318d-a05e-d8fcc24503ab | -17.71665 | -44.49674 | 2025-09-06 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c1789aee-5dbb-3abb-b0ca-9a56e526e8b5 | -16.73914 | -43.02242 | 2025-09-06 03:51:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2616e1b-a4cb-3598-83cb-c015f526412d | -16.31115 | -45.6954 | 2025-09-06 03:51:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f802ff3c-49e7-33eb-a967-e3b7bc4c2e32 | -19.99383 | -50.45705 | 2025-09-06 03:51:00 | NOAA-21 | POPULINA | SÃO PAULO | Brasil | 3540408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f7841cb1-f729-35e6-8d43-1955320a3293 | -19.21321 | -42.88111 | 2025-09-06 03:51:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a5d91dfb-7b8c-33d9-a6c3-9adbc2a37d9b | -17.69496 | -44.50385 | 2025-09-06 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac4206ca-3431-306a-9448-ce269edb330a | -14.19009 | -53.0304 | 2025-09-06 03:51:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b1a727a3-f4c2-3a25-8023-d424027831a5 | -18.44439 | -45.93314 | 2025-09-06 03:51:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2926d490-61a5-36ad-8c79-24bf7fe6ba51 | -14.57081 | -48.03031 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bf36e43c-52d8-3a0e-bc1d-1a22c63baf4b | -14.1864 | -53.02972 | 2025-09-06 03:51:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4c0a5140-73c1-32a7-838c-8e0bc55e14e2 | -14.58721 | -48.00198 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7cdae63-1254-3371-bc78-f8d84e2ff967 | -14.83074 | -48.19866 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44713ee5-afa1-3a4a-ac5c-a829e72abd0a | -21.13666 | -46.27504 | 2025-09-06 03:51:00 | NOAA-21 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2feb5d54-7f47-3f17-b590-032500aeb855 | -18.26297 | -43.02491 | 2025-09-06 03:51:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0d3452e7-1c38-3af7-ae21-7cf63cf52678 | -15.36456 | -46.41156 | 2025-09-06 03:51:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 873086a3-ecd0-3747-bf4f-fbfcd894da4a | -16.30081 | -45.70244 | 2025-09-06 03:51:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6e7b728-b61c-3e27-bb8e-eb9d0e055a26 | -17.26191 | -49.00552 | 2025-09-06 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b31a6dc-aea3-39d3-8997-fff73c5842d1 | -18.56409 | -43.82541 | 2025-09-06 03:51:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75cbca03-dce5-32c9-a961-ae6d028f50fc | -19.62609 | -46.0144 | 2025-09-06 03:51:00 | NOAA-21 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3de99d1-b9a7-384d-97bd-b0ed134fa458 | -14.84348 | -48.18957 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a51bc3e-7f37-3e24-905a-b93ee0b3cfbe | -13.85092 | -46.2674 | 2025-09-06 03:51:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 98a7d92b-5184-3260-955d-93ce829c0405 | -14.79886 | -48.11319 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d8b044f-3133-3071-a592-d273530f2ef7 | -14.96108 | -47.59445 | 2025-09-06 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96b672b2-9fa5-383a-a906-541db4efc87d | -15.71984 | -53.56251 | 2025-09-06 03:51:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d541bbbd-1e54-3af2-bb3f-96d57797096b | -16.28051 | -43.37966 | 2025-09-06 03:51:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86fea738-3062-3fa3-97ce-a6ff3bdf6b15 | -22.03592 | -42.49273 | 2025-09-06 03:51:00 | NOAA-21 | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 297e5c3d-b485-30d1-9a89-93661fd2a8c8 | -14.96168 | -47.59143 | 2025-09-06 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 706887d4-21ff-3e5e-8f02-c1cb3c033263 | -14.8032 | -48.1186 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3de659a9-3088-380f-8783-51a00359b484 | -14.83359 | -48.18442 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39a50430-8fbe-34fe-bed7-6763d2ea86e2 | -18.1281 | -42.71753 | 2025-09-06 03:51:00 | NOAA-21 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 36a6ebf2-600b-3cf9-a129-86ef03bd326e | -16.30245 | -45.69369 | 2025-09-06 03:51:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README27.md)
