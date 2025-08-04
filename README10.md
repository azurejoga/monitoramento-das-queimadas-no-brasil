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
| c10223df-6ac4-3b19-a3fe-8810d2e034c6 | -8.36622 | -46.91729 | 2025-08-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62c34227-47d0-357b-9eff-d90a2290c203 | -7.40751 | -45.2658 | 2025-08-04 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40b4ed41-c05a-34d9-8f56-5152b36f93b2 | -5.58907 | -40.60966 | 2025-08-04 04:08:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b24dd2a9-c637-37fb-b715-e3293d7c5c31 | -6.85419 | -41.70372 | 2025-08-04 04:08:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| b4db73c1-baef-33cf-bf41-3e25b4ed1fa3 | -7.01587 | -44.61831 | 2025-08-04 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6c6d3c1-0703-35eb-ab44-00abc505f1b3 | -7.5581 | -44.87497 | 2025-08-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c49cd551-265d-3eff-a322-cecd131b2191 | -6.61089 | -44.0489 | 2025-08-04 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0104db0-1cbf-3178-9dc2-cc423bd2dd47 | -8.35777 | -46.92434 | 2025-08-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b173196-6ed8-33b3-8b66-706ef35784c3 | -8.36738 | -46.91538 | 2025-08-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d569fc6-d522-3fbe-823c-7903619b3b9b | -8.12992 | -49.58986 | 2025-08-04 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ec21be48-7649-3846-a178-75211b3d43af | -8.01235 | -43.17903 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5a3486ad-acf6-3ef0-9126-e67bcf4cdbe0 | -7.78099 | -45.22763 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55f52ceb-178b-3492-a53a-61c19c858a8b | -7.77807 | -45.22279 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2830dfa4-8ff2-36b6-81ce-ce63cf4a61d0 | -4.7361 | -44.43038 | 2025-08-04 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6d69638-15d9-3cce-bc44-1ae6db21e6e9 | -10.59788 | -45.26095 | 2025-08-04 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a9be6f8-1bd7-3b2f-a5de-375f8be96b85 | -8.01512 | -43.18313 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a1168e29-f9a2-3881-a139-59fe562e0277 | -7.55185 | -44.89077 | 2025-08-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 581aa93e-6385-3e6f-a291-8605eaee2be5 | -7.5425 | -44.88088 | 2025-08-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3d6506b-473d-3063-9107-cc92b97c399d | -7.95048 | -43.90886 | 2025-08-04 04:08:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7b3c8d4-2015-3850-9d74-47ed29816298 | -7.016 | -44.61729 | 2025-08-04 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49e67fad-81db-3bd8-8788-07b2e2ee5d09 | -7.77219 | -45.21325 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b473a827-5bed-310b-98e7-feaac983a616 | -8.0147 | -43.14296 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 985bfd0b-2fd8-3682-9469-6cd9db732f5d | -4.74853 | -44.44506 | 2025-08-04 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9aa9ca2b-3982-35b3-b01b-1c610d0ec43a | -4.12956 | -47.64301 | 2025-08-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4b99f631-5bda-311a-9cd2-0eed332f2029 | -7.41114 | -45.26642 | 2025-08-04 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 764584d9-3210-3ecc-bb25-e35b8694e24d | -3.69123 | -41.13756 | 2025-08-04 04:08:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4cbc58bd-b05e-38d8-a8aa-a1cc695a341a | -7.99815 | -43.2096 | 2025-08-04 04:08:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d3573229-7d11-315b-928b-6fc73c50c046 | -6.63393 | -43.6661 | 2025-08-04 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c957ba01-c61e-3e8d-9701-610b0cdbda3d | -6.67223 | -44.36548 | 2025-08-04 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fae406b7-82a6-36fd-b131-968a1b22dc59 | -10.56303 | -45.27564 | 2025-08-04 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| adecfd38-f8ae-3e60-a570-081dcd2e4f90 | -8.00149 | -43.21013 | 2025-08-04 04:08:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 36f362d2-9685-3f0b-ba42-b7c7a9cff4d0 | -7.55743 | -44.87907 | 2025-08-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b18cbcde-f304-3d3e-83a1-37846faa45be | -8.01273 | -43.13897 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dbf3dcfd-59f0-3d12-8b5b-b3589f065fc9 | -8.35636 | -46.90839 | 2025-08-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eeb00f51-54dc-3812-8037-efb0ae65879b | -8.05489 | -43.10574 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 04f442bf-c905-3f54-8b9e-4b43cd6be9ba | -9.39257 | -45.50158 | 2025-08-04 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 44e6e2f6-12de-34a4-8ee8-dbeaaa294fe0 | -6.1981 | -43.75481 | 2025-08-04 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 295fff5a-6c42-3827-9d7b-476841bbdc4b | -7.77739 | -45.22701 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c554c456-6c83-3f0e-9c52-cd3404cf13c0 | -9.61966 | -43.85741 | 2025-08-04 04:08:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 58280a17-761f-322b-90c5-8dcfd4e84385 | -6.52454 | -44.53756 | 2025-08-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c8120d7-403f-31b4-bb87-f452e2be0806 | -7.27199 | -46.16187 | 2025-08-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e68eaf51-51b5-3cbd-bac1-396ce21fbc85 | -7.65255 | -49.84079 | 2025-08-04 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c91f852a-1f9b-324c-8402-aff43d9de1df | -8.36343 | -46.91471 | 2025-08-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7269c34e-8fa7-30e3-a36d-3ee2ffeae578 | -7.41201 | -45.28402 | 2025-08-04 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab069fbe-3e18-3a92-ab38-500f42cff5c4 | -10.57136 | -45.26881 | 2025-08-04 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46161552-0e2a-343f-8d37-abce4b325163 | -4.73772 | -44.44339 | 2025-08-04 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 257182a3-5e26-3081-a48f-846968e6e449 | -7.56322 | -44.88837 | 2025-08-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f848424-379b-3793-80a2-813335d645d4 | -8.03651 | -43.11371 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 56cb70cf-eee2-3021-84b0-cdc1a5cc2e73 | -7.99702 | -43.21674 | 2025-08-04 04:08:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b0cca27e-5b07-3b0b-b0b8-b677e8081ea1 | -7.05594 | -44.3965 | 2025-08-04 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00cacf7c-dd91-3421-8618-69bd89bb9b56 | -7.19608 | -44.49133 | 2025-08-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee68e940-2577-30fe-843a-5f9327d87ef7 | -4.02465 | -48.06175 | 2025-08-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 794da213-71cd-310a-9337-2cb867b25305 | -8.73501 | -46.40428 | 2025-08-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67f99786-f930-3735-969b-1e9ac9a0f00b | -7.62854 | -45.29076 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a19c1f77-420d-3c3d-83ee-2697c1867d74 | -7.33947 | -44.68064 | 2025-08-04 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d6d64c1-3075-3acd-9c1a-a832c462ec4d | -8.00939 | -43.13844 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dda77d0c-9835-30ce-8125-326b1f9c259e | -9.39975 | -45.50284 | 2025-08-04 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c3fc6249-cf1e-3e2c-8688-b0bc03cffde9 | -6.52294 | -44.52501 | 2025-08-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 269be612-8bf9-384e-bb24-5db460f01595 | -8.01797 | -43.16534 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c2e1cb50-e511-320b-a86e-950be006ab94 | -6.60805 | -44.04449 | 2025-08-04 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7ee0c39-ad7e-3264-adac-08fd6bc53dab | -4.12658 | -47.65583 | 2025-08-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af2308fb-884b-34ba-9893-96d080e16c6f | -8.51564 | -44.74212 | 2025-08-04 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fe47bd8-6eae-3aa2-99bf-34ec190ed387 | -4.12293 | -47.65046 | 2025-08-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9e582625-370f-3b72-bad3-7764faa2071c | -7.29042 | -43.40203 | 2025-08-04 04:08:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7abce3be-fefe-3829-9489-bce36db0ac6a | -4.13174 | -47.65224 | 2025-08-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 14246b0b-80ac-36ac-881f-d345dc2b9505 | -6.21869 | -44.3436 | 2025-08-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96f2a31d-5ac8-374e-a1fe-3e4e605cd3ba | -7.9999 | -43.15513 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e60455b3-4f93-33e1-aab1-859c3ec36d07 | -7.7704 | -45.1104 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08774df9-2d75-36af-ba04-a01eba70b692 | -6.17319 | -44.78108 | 2025-08-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9db246a-548c-3747-955e-c2c35443016c | -4.13324 | -47.64334 | 2025-08-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 949472c2-d67a-350d-92f2-34ad2b28bd75 | -6.84872 | -44.288 | 2025-08-04 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e43cc9b-5b28-36af-aa0b-03bfc6cc216b | -9.50068 | -43.17188 | 2025-08-04 04:08:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8becc284-190a-3296-8eb8-7a83abc1db2b | -8.37017 | -46.91795 | 2025-08-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28b1a775-e21d-3353-92fb-942a51053d5b | -8.00046 | -43.15158 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.8 |
| 1b053829-7767-3d20-a5fc-8ce120b8844f | -7.54318 | -44.87678 | 2025-08-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc0999d7-c6f9-3cd0-a454-1e99205ced4b | -8.00549 | -43.14146 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 45.9 |
| 6defe5e7-d893-3aab-aca3-27a8e4b0bb41 | -8.38731 | -46.93647 | 2025-08-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| f5b36737-eb8a-3789-aa71-2e9e2418ccb5 | -4.13984 | -46.45734 | 2025-08-04 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b83c82e-1d5a-35d0-813d-535a45cb40b8 | -7.05259 | -43.83584 | 2025-08-04 04:08:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8ccced1-1aa9-3fb7-b4d1-cf4a35ac0666 | -5.99079 | -45.02596 | 2025-08-04 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3650c927-c0a0-3d56-8e96-b9e4b5f54efd | -7.99265 | -43.15765 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| cd46552a-544a-3929-9dac-1c58184d3667 | -7.13886 | -44.08495 | 2025-08-04 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f058cd02-b1c5-3a45-bd80-d75d9e55c886 | -8.0129 | -43.1513 | 2025-08-04 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| b41415fc-4237-3d69-a5e8-3229b8c4a256 | -4.7346 | -44.4457 | 2025-08-04 04:10:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 0fa673d0-8f16-3e04-8406-3ecc97ced25e | -8.0132 | -43.1278 | 2025-08-04 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.1 |
| f29787f2-47af-336d-a4ad-7399573e0f59 | -7.994 | -43.1534 | 2025-08-04 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 115.1 |
| 24d44afa-24e9-335c-9e01-73fb16eb712d | -6.656 | -59.0981 | 2025-08-04 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| d2643550-bafb-312b-b204-1aee26fff2ae | -7.9943 | -43.1298 | 2025-08-04 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.0 |
| e3902fb4-5ef0-3b12-8c3b-503c6332e171 | -11.50176 | -44.29946 | 2025-08-04 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06077d72-c7e3-357a-a88f-2f482d73c497 | -17.6748 | -44.13156 | 2025-08-04 04:10:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a00118be-5993-33df-b226-16c075f5b494 | -12.64826 | -45.05199 | 2025-08-04 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| facecdc5-013d-3ead-a710-f6110208f18b | -17.36807 | -46.07827 | 2025-08-04 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c83238ae-9cc7-3abc-b819-e2919903262f | -15.56226 | -47.08101 | 2025-08-04 04:10:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57a1ebb0-dc55-3483-8d5b-96bcbcf6daf2 | -11.93524 | -44.94231 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4ffc7b1-d364-35b9-bffe-841331bc07f2 | -11.62629 | -48.4814 | 2025-08-04 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69879443-8569-3b5e-a644-c1867767222c | -17.36677 | -46.08609 | 2025-08-04 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2326f42b-82f2-33a5-acb1-ac1dca6ad533 | -11.7618 | -44.97111 | 2025-08-04 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22731f2c-ecda-33d4-8dd9-d2ac10da0c6c | -13.69071 | -41.36449 | 2025-08-04 04:10:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 03f8dc51-0b22-3823-b7ab-124c785538a4 | -15.56584 | -47.08178 | 2025-08-04 04:10:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c682c357-6ca7-305d-a504-314c6466428a | -10.32736 | -50.0735 | 2025-08-04 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README11.md)
