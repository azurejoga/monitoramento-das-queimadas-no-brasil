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
| e6ffac80-a134-3cc3-907a-637fd0eb44c4 | -7.76089 | -50.75542 | 2025-09-07 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 993c6dff-caf9-34a5-8c93-e1ba11866c9e | -6.19201 | -42.6201 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3e91b7fb-618f-3e5d-9a51-3af172c59bd2 | -6.70731 | -51.41378 | 2025-09-07 04:19:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 35ba0161-25ee-3c10-a1f7-5390433223f3 | -6.53315 | -42.92903 | 2025-09-07 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0665183-739a-3f35-9441-d49bdb4f1608 | -9.39063 | -54.76662 | 2025-09-07 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6dfb46c8-f5b6-3267-99f8-9c25aeacf966 | -11.64007 | -54.53856 | 2025-09-07 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 348386b5-d38c-3eaf-be17-3ecf55d1009c | -10.06924 | -49.2979 | 2025-09-07 04:19:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| de7d667d-963a-39e5-b878-31c16ed89601 | -10.05959 | -48.06679 | 2025-09-07 04:19:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65bea091-3070-359b-89f4-a46baf7c544d | -11.84347 | -47.56918 | 2025-09-07 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2253b1ae-cbcc-353a-a391-2ba12e69ff58 | -6.20053 | -43.37622 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| adb2ea37-fa02-34ec-b79f-62bb38c17ace | -6.59161 | -43.97946 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c227b6ce-abd2-3508-b9f3-eb69d49399a7 | -6.561 | -42.95221 | 2025-09-07 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f638bca-39eb-30ac-b7b5-c8a5461cb0db | -12.87894 | -47.99602 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 466516ce-b8d0-3059-b142-f963f9cec109 | -8.02944 | -43.81043 | 2025-09-07 04:19:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d70e2265-7da9-38ee-a23b-1efc7265fc10 | -7.67069 | -50.26344 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87c7c08d-0073-39fb-8014-136a7d1e2d02 | -12.84772 | -47.9943 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d06f41f9-9436-3ddb-bcef-fa71f599a8b9 | -8.91513 | -45.80927 | 2025-09-07 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abea356e-b2ba-340f-9a33-0b357b6c060e | -6.91925 | -45.20033 | 2025-09-07 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46f4a2b1-aa0a-3d6d-a871-39b5403994c8 | -11.40374 | -43.59436 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c86c9961-c9a4-3fb7-9894-2b048d510d27 | -8.34292 | -48.27901 | 2025-09-07 04:19:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d782f1a-06aa-3abb-8a20-bd70cdc00225 | -10.78695 | -47.74502 | 2025-09-07 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 867e320b-f034-36dd-aca5-765e1ff677d6 | -8.11081 | -45.31261 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 73595fbc-3944-3ad7-bad5-52288c052dec | -12.60932 | -44.60449 | 2025-09-07 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db85bdeb-8bed-3666-a9eb-9851db1d8066 | -7.98752 | -46.3416 | 2025-09-07 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3d59870-d4bd-37a1-9da5-3d423bf11863 | -6.22519 | -43.2845 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f3c07d0-80c0-3e2b-9fcd-a7b677689414 | -10.33319 | -46.39556 | 2025-09-07 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5036fc45-db07-394c-ae9a-f68d81e9b159 | -6.53772 | -44.82049 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00f416e5-f540-3870-b93b-4bedebcf656c | -8.0769 | -52.34512 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e53731a1-3d97-3738-990f-69389ac617b7 | -6.18894 | -53.25647 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0062a6cb-0fb8-362b-9229-be1725585584 | -6.19773 | -43.37212 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4a986ba5-4780-3245-ae79-70d0bb1bd26d | -11.40024 | -43.57006 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5fdaa7f-e621-37a9-ac53-4e6d8848fd54 | -8.12073 | -45.31417 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56d01aaf-e2c3-3d4c-968e-6537026953a1 | -6.89535 | -45.54276 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3874000-7510-32c9-890f-90f26596c286 | -7.53789 | -42.52144 | 2025-09-07 04:19:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 92e5add4-fa8f-3d52-9a68-49218ddcf2b5 | -6.58997 | -43.98998 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba1504d4-95e9-3570-897e-3b815f7e39cb | -6.23369 | -43.30804 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c56b441e-5341-3d0a-8642-824adbe7350c | -7.33908 | -48.50527 | 2025-09-07 04:19:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98f24a3a-4346-3104-bf6f-a757ddd9c11a | -13.18341 | -44.48655 | 2025-09-07 04:19:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f33f2a8-d537-3a96-82d1-759ead9fc82b | -6.37708 | -42.98518 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5057d9c-a07f-37e9-a7b4-1019da28b66f | -7.96902 | -44.96254 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3d5c9a7-b610-347e-a509-44c5387a2d08 | -7.57371 | -44.6689 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3ab22da-86a7-3127-bb3f-f72a0750aa7e | -11.26188 | -46.45323 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5feb32a7-83cc-3745-af1f-92a796b198c0 | -6.19822 | -53.2639 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b13fa63-5020-385f-a018-ae5bab635f35 | -8.10695 | -45.31555 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e22d111-7783-3cde-ada9-cc1d960e1b15 | -6.8853 | -45.6058 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 456a743f-3fb0-3cfd-b8a4-73498c945e18 | -10.32279 | -46.354 | 2025-09-07 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b6cb2f2-cd7f-3638-b1d3-7990ed5788c1 | -7.54427 | -45.35013 | 2025-09-07 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e04a3ff-4605-3a66-955f-73b7d8839009 | -6.18378 | -45.42567 | 2025-09-07 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 77d92494-b744-3b56-9e57-000a90bdb2e5 | -11.00763 | -52.04602 | 2025-09-07 04:19:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0bd33147-f316-36a2-949d-eedf39f99582 | -10.80442 | -47.72458 | 2025-09-07 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f956bf5c-c3e6-3ccf-a1c8-c879e092f7ad | -7.68047 | -50.3051 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 86c04c35-2797-31d9-a28c-19f5c5be4049 | -6.17002 | -43.19504 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| dacdadd4-7b53-3cc1-81fe-174e0a92e0b2 | -9.74472 | -45.37418 | 2025-09-07 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c73445f4-52f7-3641-871a-aa776c2b79f1 | -14.4178 | -60.19769 | 2025-09-07 04:21:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 49155ecb-60db-364b-8f2e-9751bdbdbb38 | -14.29254 | -43.56297 | 2025-09-07 04:21:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3917731d-27b4-3177-8901-011c710203d0 | -19.64039 | -46.06797 | 2025-09-07 04:21:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4cd65ffa-117e-3c64-aa0b-029bd1d98df2 | -12.95314 | -54.77713 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3c1ffa2c-d888-323f-8fdc-f7d78cd5865d | -20.22159 | -44.20301 | 2025-09-07 04:21:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4fa10b47-970e-36f7-bbeb-0b87d3b03f0d | -12.92537 | -48.03513 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57c9c959-aa97-3e0e-ab01-e0a9261f23f2 | -15.84101 | -52.2985 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f72850e9-5659-335c-9121-bfabdbe62926 | -16.9237 | -45.77863 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffed1f1a-1dd6-3d78-b71a-fd7414ad963a | -15.12341 | -52.35505 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4644b47-b580-3670-8bcb-c282cbd123f1 | -14.59278 | -52.16399 | 2025-09-07 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7ab09a2-0347-3678-9e1a-a77dddcd73a1 | -13.91142 | -54.0134 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ee0fd17-e096-383e-8455-614b193cf323 | -13.01593 | -48.08132 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 859e7776-525b-34f7-bf71-a1136b4441b3 | -12.78022 | -52.96062 | 2025-09-07 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf099b20-4bc1-3511-b6be-48ff76ade1c1 | -19.88414 | -45.03022 | 2025-09-07 04:21:00 | NOAA-20 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad2a0959-5dd3-38ef-b4eb-7257e21df791 | -15.54176 | -42.65812 | 2025-09-07 04:21:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 2da63b0a-9068-33fe-8406-33c8242616a4 | -12.94196 | -54.78099 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| cfa59c7a-6b44-3ce1-8fc4-fb73ae6126ef | -14.79058 | -48.10696 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d04d56bd-494a-3bd4-95ef-f0b496ae6444 | -14.54066 | -53.15701 | 2025-09-07 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a309662f-7c3d-315e-9c8c-e66fcc3e31de | -16.92923 | -45.79833 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 772c6866-d2a9-34b4-acd9-24edabb929c6 | -13.83249 | -46.28391 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| d5a91779-4188-361d-8f48-0604ab2b63ff | -17.55428 | -44.40515 | 2025-09-07 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d56243f8-ad81-3894-a396-ab8ffb385d30 | -12.94856 | -54.8013 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06caf724-a512-3110-bf54-25409868f24b | -15.14172 | -52.32479 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f01e8aa-3f84-3417-a222-0061bc2cd3ad | -17.69405 | -43.52009 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ea7c714-df22-3083-9b85-f4132be61f6e | -19.47711 | -47.75996 | 2025-09-07 04:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47708082-2185-39c6-9c01-d70608750e27 | -14.57801 | -48.09776 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fb7f25b-89a1-3155-b856-6e3a7ddeb362 | -17.68171 | -43.55524 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 20ea4434-5f0a-316b-bddc-dc905bdf1a9b | -13.01934 | -48.0819 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd789be0-7ce0-3a46-8c33-36501592aa2a | -17.84897 | -41.52654 | 2025-09-07 04:21:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 23505d68-2bfa-313c-9eef-799a14752206 | -12.94254 | -54.77796 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 292c148d-2fa6-32c1-b0b7-25010b497b62 | -15.54105 | -42.66308 | 2025-09-07 04:21:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 08f8a7b1-1132-3495-9cb7-4b1a7f832b7f | -12.77513 | -52.92428 | 2025-09-07 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 419b2aa7-3f7f-3880-a554-81f1f8740e55 | -14.44827 | -48.46069 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fabcd14e-0516-363b-aee3-1f6dfc23f621 | -15.69481 | -45.04559 | 2025-09-07 04:21:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b991fadc-0ec0-36e0-ad04-f289c916ff0f | -13.81981 | -46.27819 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1d6a8c8f-d552-3436-8a38-1a0e54984b99 | -16.92638 | -45.77129 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfa423fa-fd43-3150-8b44-e8af63fdaf34 | -14.77526 | -48.11589 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55e10f44-fa1b-3040-b446-50d42a79c55b | -12.81336 | -52.91756 | 2025-09-07 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 656bcaed-209c-3658-a2a8-7f6f599d01ca | -19.64719 | -46.06908 | 2025-09-07 04:21:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bcd5e28a-9053-3f11-b255-f21e9a4dc43a | -19.94302 | -43.61119 | 2025-09-07 04:21:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5561d872-48bd-3a58-8e74-949c4bea70c9 | -17.00695 | -49.18051 | 2025-09-07 04:21:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69fc935a-91b3-3a85-916a-a29d2e5cc2d2 | -16.93538 | -45.78034 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83729ecd-b5e4-3b1d-8e71-d5ff8a8dee22 | -17.36649 | -42.64703 | 2025-09-07 04:21:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1037fd9-db46-3046-8523-16ce98142557 | -13.85571 | -46.24414 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07cc2040-292d-3c78-94f5-efbeafc1d0b0 | -13.04989 | -47.12375 | 2025-09-07 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a081faf3-2846-3305-b638-5aed4706c9d7 | -19.47595 | -47.76726 | 2025-09-07 04:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 811662e8-b306-3dfe-acfc-1dde012c79ae | -19.47869 | -47.7715 | 2025-09-07 04:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README56.md)
