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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c39185a-0c6d-3653-9b68-ad1cb93c466b | -1.27983 | -55.41233 | 2026-10-03 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6cf0277-3640-3af8-b412-e2e297bacbe1 | -2.26315 | -54.80337 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48e2ca8d-5983-38d4-9f4b-cac2548bc177 | -3.71452 | -53.39465 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99162679-64a0-3143-b079-73c4cdde8738 | -3.29262 | -53.83634 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c207f5b4-5f57-3e61-801c-736577b712a7 | -3.11672 | -50.28251 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 847d0dbc-c340-3173-b965-0759ba4d605b | -2.17532 | -49.76799 | 2026-10-03 05:16:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8813e7a9-7b0a-3354-8c73-0518b54651a6 | -2.54893 | -57.40277 | 2026-10-03 05:16:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bde6b54-4f1c-35ff-93e8-94f21a51975e | -4.29491 | -50.78053 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2298930-7924-370e-9cfc-625cb6b9c739 | -4.56816 | -46.58641 | 2026-10-03 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2dd274d4-a3ee-3963-a808-323fdbbc29cd | -3.17011 | -54.09885 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7837b3f5-a9a4-3191-81d5-afdddd98acb4 | -5.36762 | -49.59128 | 2026-10-03 05:16:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 644ec0aa-1805-3c85-8c04-7f3e2dfa166e | -6.20513 | -53.26516 | 2026-10-03 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8396b3c2-f5cf-3acf-a44b-e2369b792183 | -3.71472 | -53.39453 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 392c4c34-2817-3cf3-a863-1d9e09990e4c | -7.46445 | -55.01287 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8bc4e879-9f64-3408-be2f-07a18a448c23 | -2.56925 | -49.1115 | 2026-10-03 05:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c0ae0d9-056a-387e-b442-5107c0078c77 | -3.11977 | -48.67403 | 2026-10-03 05:16:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22886eb6-e5a6-3844-9ae1-72c2d740e966 | -3.17534 | -54.07853 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eed1ff74-59e5-3556-9c7c-6afecf44673a | -3.07315 | -51.27851 | 2026-10-03 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bbb50ef-25b3-3f59-8753-920211669be6 | -3.29037 | -53.85054 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95e5f765-d4bf-3750-9b16-0d61d4ad055d | -3.11464 | -50.28053 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ffba1e0-c1e4-30f6-9012-f549cc08b99d | -3.00287 | -54.23429 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4217d42a-ffa9-332c-80bf-f03243e6b613 | -4.78637 | -55.71972 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07b2df7a-4dd3-332e-968c-13fdf72c9032 | -3.87706 | -51.89531 | 2026-10-03 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40d2badf-85c8-3fa2-977f-b7321db4fd57 | -3.12898 | -53.74842 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7071254f-bc78-3ab5-b7f5-afe3f0aaaf91 | -3.18319 | -54.09415 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 500969d5-ddce-3aea-ab8b-6a48ee8d8b3c | -3.28308 | -53.83119 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c6b95001-a70b-3369-8e1f-d2b78933bc5a | -3.00676 | -54.23133 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e73f63a-62e7-3560-b41e-2787a82aa6fe | -2.89746 | -54.14982 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a81c5e6d-cf23-3157-8cf9-2d0db86538b3 | -3.28757 | -53.82462 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d14f39f7-0677-32b0-8dcb-8cb8f7c0cd5d | -4.65829 | -55.99534 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5298100-1b07-379c-9761-d1adc2333e46 | -2.8896 | -54.11276 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7121315-b750-3f23-905e-9656f0404231 | -3.24493 | -54.51821 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3972b693-e524-3549-99d5-d993b7e64c3c | -3.23088 | -54.31311 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f462782c-2b65-3743-9cf7-72336aeef631 | -2.97034 | -54.09305 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28ae99cf-adae-3719-a615-a41bcde3beae | -6.05106 | -59.9281 | 2026-10-03 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24013a32-ac67-38dc-a9c8-151b54bb1954 | -6.21125 | -53.22584 | 2026-10-03 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47aa6bda-76ff-3678-943e-59b44716ac42 | -2.1093 | -49.00156 | 2026-10-03 05:16:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6dac455f-f399-3238-aacf-16d1d8214fc6 | -3.22754 | -54.31258 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b90bc4f3-249e-327d-b5cd-7fb83d2c0a64 | -1.25902 | -54.56016 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9640f8b0-0ef6-3f0d-99bc-8c9bb5189b40 | -4.79305 | -55.76352 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de28467e-a1db-31fd-9c0d-c7be971edfc1 | -5.97154 | -55.37435 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d3fd3ee-86dd-39ec-ae61-ff92dd698c3c | -3.13235 | -53.74895 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cabf448a-5a0e-3dbb-a717-655ed4d92f29 | -2.97313 | -54.09708 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1cc2a02-7530-3391-aad5-dc3f69fc8d36 | -1.27927 | -55.41583 | 2026-10-03 05:16:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 592f6c2d-314a-376b-a7eb-64564b47357f | -3.14021 | -53.74287 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 425c5a9e-8bc3-32ed-8b74-73d9f1e77a11 | -5.9721 | -55.37087 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6d9ca36-39db-342b-8fc5-a7b46aee2b30 | -3.13851 | -53.73166 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4485bf5b-4b38-3095-8df9-11d67a0b5371 | -4.26493 | -50.7406 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 981fc920-c032-33fc-b5a4-850a612a6a1a | -3.56417 | -53.06066 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcd37958-fee8-3d7e-a83e-9a80deb96e8a | -2.97691 | -53.27158 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc538811-174a-372d-ab25-ff14e03e0b28 | -6.93058 | -49.62339 | 2026-10-03 05:16:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 105a9a80-3024-395d-be66-742a5d10c514 | -2.88768 | -56.82282 | 2026-10-03 05:16:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b5a9d67-1519-3a40-8c60-2c8b52953042 | -4.44996 | -47.92297 | 2026-10-03 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b117c76f-f0c7-3287-abd0-09cee56be44d | -3.19214 | -54.10271 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9439b955-d168-342f-a5ac-f9105eb29f57 | -5.7261 | -43.28077 | 2026-10-03 05:16:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e05f64b-8677-3f51-9ade-7a033b979e61 | -4.40685 | -49.96561 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1908564-b0a3-37f9-a513-cb20a2cdcbcc | -3.13458 | -53.73469 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4f9d4a84-d84e-3988-95e9-5a1391863add | -1.22228 | -54.54045 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9aa83f3-be94-3d91-8df2-e7a64e2b2677 | -5.13393 | -45.57576 | 2026-10-03 05:16:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 301bd175-a90d-379a-8f19-4ad0ee1d0330 | -2.25148 | -51.93086 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bc475a75-4386-3ad1-924b-6c355ac0c904 | -6.34949 | -51.70552 | 2026-10-03 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c7eeeb9-16c4-33f1-b493-147f4649a52a | -2.92583 | -54.10048 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cdacdb91-b9e7-33b3-a287-0a47bba71c0b | -5.95061 | -43.65342 | 2026-10-03 05:16:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 66c84443-2124-3bda-9cb3-70530551d6d2 | -4.42593 | -55.75158 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3450000-b7be-3baa-ab43-b841749c2956 | -3.70689 | -50.65794 | 2026-10-03 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e3cebac0-d657-3ab2-a731-5b922d0dff0f | -4.68662 | -55.79621 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe38db63-72f7-3eb3-a0a9-7c074fe17f96 | -5.98097 | -55.3794 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90b8488d-c31c-390c-be7d-8b97a9e77f86 | -2.29025 | -47.87776 | 2026-10-03 05:16:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba59fcdc-68dd-343e-8c47-635677e52b70 | -4.73704 | -43.27246 | 2026-10-03 05:16:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3116095a-3ecf-3804-b098-4eb6229886e3 | -3.13909 | -53.75 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a27a7bb-8d4b-3f9f-b653-36e6f1473cc5 | -3.12334 | -53.74025 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 74287456-6aed-3c32-8dba-9ffdd71d8e74 | -6.73462 | -44.14692 | 2026-10-03 05:16:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b040fcf1-c22e-3439-97d1-3d39df265681 | -3.13009 | -53.7413 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f34b4ddf-eeb1-3b8f-b73c-7382322d443a | -3.02833 | -51.27157 | 2026-10-03 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f8fbb32-e33d-3476-90e3-d760552dd107 | -4.29416 | -50.78542 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a92e5fd-356a-30fe-b2ed-d58c902d9df4 | -3.0035 | -53.88186 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 585c60a8-860b-3816-af7e-9620dbce5572 | -3.18824 | -54.10571 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1ddb4fff-5ebd-3fb1-9f30-02529c09a75c | -3.7757 | -52.14118 | 2026-10-03 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 023a3584-5f06-3377-a6a7-c9710f44c28e | -2.93642 | -54.09855 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 672b8a18-91ec-3810-90a5-5ed07e3278bc | -3.05643 | -54.16726 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db754b66-df58-324e-a512-58466feb9f55 | -3.13739 | -53.73878 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 045a26d7-4388-3dfe-9e9a-abc2193d07e6 | -2.92248 | -54.09995 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| af75e6e8-afed-3f2c-acf5-745078f61e8a | -2.15475 | -59.22691 | 2026-10-03 05:16:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0a0024a-113d-3928-8ab7-5d6acfe2a281 | -3.88071 | -51.89587 | 2026-10-03 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0ca36aa-8e3c-330e-829b-68f3996ec9e6 | -1.27563 | -54.56277 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65c3fa92-7d11-3afc-8af3-64a9f1419b66 | -3.51567 | -54.60664 | 2026-10-03 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f7f6b403-ccb6-3582-8b57-359d0cf39abe | -3.41981 | -48.33717 | 2026-10-03 05:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 588c4037-e1a7-3679-8885-b2d906315d71 | -5.88524 | -55.4887 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f2381071-1fd4-3f31-bf56-f2f0b413f022 | -3.12449 | -53.75503 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 02198ec8-5433-371c-9df3-d21300a27377 | -3.2242 | -54.31206 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b778ee49-ee53-30ed-b789-d9317bfb14c0 | -3.95564 | -55.32551 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cb3494d-52e3-3f75-97a1-17eb1648c73f | -3.12053 | -53.73616 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c89dae5c-bf3e-34f8-83cb-4f4fa920b896 | -3.1059 | -50.28439 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91683ba8-2a4d-3a34-8876-89fb652688c8 | -2.48697 | -56.09772 | 2026-10-03 05:16:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 772e8afd-43b5-34b5-bdba-2ade061e6205 | -4.29251 | -50.77009 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3d06f63-430f-3aec-b4e8-af73a2ee7064 | -4.98579 | -45.64419 | 2026-10-03 05:16:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f0f5661-3c32-3bd8-a2b5-cda272c155e9 | -3.0175 | -53.88042 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 756aa490-40ca-3d42-aed7-bb76432ae99b | -3.70182 | -50.97919 | 2026-10-03 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e120ef0-26cb-381a-bfa8-8e04525375b1 | -3.64425 | -55.49962 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| be7a8fa0-ba17-3133-917e-aa44a6f2e444 | -6.0181 | -53.54242 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README32.md)
