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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25e78eb9-336a-3890-8c5d-46cae76c322a | -14.20514 | -45.47238 | 2025-05-09 03:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| aaf0773b-e640-3365-8ff6-3023a76b5299 | -9.61676 | -37.04453 | 2025-05-09 03:25:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0e219743-e39f-364a-9d6b-c1630045d635 | -10.54972 | -42.42608 | 2025-05-09 03:25:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5e59b2db-7bfb-31bf-8169-689ced377c71 | -14.20716 | -45.47197 | 2025-05-09 03:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3fdb64b1-ead3-38e6-83a3-a30d3353e263 | -8.08267 | -43.12157 | 2025-05-09 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 859dd578-a11e-38f5-8ee3-6fbcd1c28c15 | -10.6719 | -44.38249 | 2025-05-09 03:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5c2c6c45-eb31-363b-9e25-41ef5e2974fc | -13.6108 | -43.97311 | 2025-05-09 03:25:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e419130b-a081-3e43-9b20-687b3b12454f | -8.07509 | -43.12056 | 2025-05-09 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.4 |
| 27e5558a-5889-3786-8147-858ffe08199c | -14.22647 | -45.47088 | 2025-05-09 03:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eaf0af63-952d-3ea1-a6e1-cd1392e677ce | -14.2198 | -45.46933 | 2025-05-09 03:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9953baa5-7792-3774-a40e-188f22e27a12 | -8.08051 | -43.12732 | 2025-05-09 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 30bc0cdc-0387-3d78-b8e4-47312fe5fdfa | -10.6652 | -44.38123 | 2025-05-09 03:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1c1f1714-0140-3cd1-8fcc-dbd193b08b28 | -10.96646 | -44.44342 | 2025-05-09 03:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8406dd91-71ff-3ed1-a58e-2350804f5e90 | -8.08064 | -43.1325 | 2025-05-09 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.9 |
| 223bf2f5-52a1-3fe7-a24f-e750feebe118 | -14.22051 | -45.47497 | 2025-05-09 03:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60b09017-bce4-3d6a-b6e2-f32976e5bbea | -10.66641 | -44.37524 | 2025-05-09 03:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d96cca28-94c9-3055-8213-ac343164b9c7 | -14.64544 | -45.14207 | 2025-05-09 03:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 473ea3be-6fa4-3b6f-b1a9-f87370246760 | -14.20851 | -45.46588 | 2025-05-09 03:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bbdbea41-2f9c-376a-aca2-88b1318dc539 | -8.0752 | -43.12569 | 2025-05-09 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| baff23e5-201e-38aa-8293-aa9d8570eb6d | -10.67305 | -44.37675 | 2025-05-09 03:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1055b9d9-6b63-3c12-8e68-fd9bfa9d9395 | -14.22719 | -45.47649 | 2025-05-09 03:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e8d5ee9-16e1-3a5d-9603-0553bc7b505f | -8.07945 | -43.13279 | 2025-05-09 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.7 |
| b8748a98-bf72-3deb-a2fc-d7c81a2a4856 | -14.64088 | -45.12449 | 2025-05-09 03:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de6f47ac-9ec5-3e9a-94c8-c1976c79cef6 | -14.64664 | -45.13639 | 2025-05-09 03:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a9f9321-3bb6-3e49-a107-9d5215ac742a | -14.22852 | -45.47044 | 2025-05-09 03:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49ee2089-716e-3364-ad2c-13ec18f60aa0 | -14.63964 | -45.13014 | 2025-05-09 03:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d305ee1-70df-3e7f-ac8a-cd7826b9504c | -13.61696 | -43.97464 | 2025-05-09 03:25:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d153113-3f33-30ff-b30a-027aca1249e9 | -14.64255 | -45.12352 | 2025-05-09 03:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d02bc18-aac7-3330-b277-f318e60032b8 | -14.20776 | -45.46017 | 2025-05-09 03:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98116310-128b-3ecf-9001-3af2658677d4 | -8.07621 | -43.12024 | 2025-05-09 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| dde4be82-1f87-320f-8421-64b9fde257d5 | -14.22517 | -45.47695 | 2025-05-09 03:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 148d16a2-590c-32d1-b69c-eb53cf6b659d | -14.64015 | -45.13486 | 2025-05-09 03:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fbf4b3a-454e-3b58-aae4-8482aca38be3 | -10.55568 | -42.42725 | 2025-05-09 03:25:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| da007454-20c9-3979-a7f0-a4b5919aec9b | -8.08156 | -43.12187 | 2025-05-09 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.4 |
| 7dc76f86-e3fb-309c-831c-fee3fc0b772f | -10.97311 | -44.4449 | 2025-05-09 03:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a753336d-1a1c-36b3-8be1-6cd264bf2f8d | -22.677 | -42.85846 | 2025-05-09 03:28:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6afe05f3-a632-3a73-b986-027bce41b3d8 | -22.69807 | -43.43412 | 2025-05-09 03:28:00 | NPP-375D | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f330dc72-7903-37e0-840c-eabcea6cfa0f | -19.15782 | -47.8209 | 2025-05-09 03:28:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c1b154a-23da-361b-83ec-6e22c3b9084c | -19.15981 | -47.82202 | 2025-05-09 03:28:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 56abc386-3078-31bb-900e-d87edccad8b6 | -8.07 | -43.1216 | 2025-05-09 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| 4ac127e0-7e4d-3d61-9933-504d6977f1a5 | -23.3343 | -46.96308 | 2025-05-09 03:30:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3a9b27a9-8d74-3327-a245-5e48552508a6 | -23.32808 | -46.96194 | 2025-05-09 03:30:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0681b530-5891-3035-a616-258de044cc1f | -8.0889 | -43.1196 | 2025-05-09 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |
| d662ed0d-c018-3ed9-b6d2-2662d5a2a60f | -8.07 | -43.1216 | 2025-05-09 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 23e630cd-2b86-3436-b025-1e99a14e9a6e | -10.97724 | -44.4403 | 2025-05-09 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c3bdc3be-4f08-3169-aa1e-82908ef7a28c | -14.19859 | -45.46515 | 2025-05-09 03:47:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 71b79e55-02f2-3e7e-814d-307b29de630d | -7.62655 | -46.47993 | 2025-05-09 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 481406d6-9573-38fe-900d-a87a33a8c97b | -10.6674 | -44.37778 | 2025-05-09 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| cd2b5ab5-dee3-3a19-95f5-127cc0c06b38 | -12.58917 | -48.33474 | 2025-05-09 03:47:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89a5c530-25bd-356a-a530-c6f97ca6fd50 | -11.56276 | -47.61783 | 2025-05-09 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20ecc8bf-c73c-3823-bbaa-f9c292255dcb | -8.07161 | -43.11909 | 2025-05-09 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 2157c8d6-52a4-3006-868e-dc179a2c8d9d | -13.61264 | -43.97615 | 2025-05-09 03:47:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a22420d5-80d0-3e58-a8a9-7aef1cdf8fb0 | -7.21099 | -41.33347 | 2025-05-09 03:47:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2ea4b243-c942-3970-af05-60929ee99b88 | -6.97074 | -42.78687 | 2025-05-09 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9b1f6605-2f62-3678-8fa8-6b349f7a5b16 | -10.6666 | -44.38225 | 2025-05-09 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 09443546-6187-3ced-b29c-94b028495937 | -10.97359 | -44.43494 | 2025-05-09 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a523e05f-89bc-38f8-907d-1bf03bb9da6e | -6.61407 | -48.00997 | 2025-05-09 03:47:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec59e435-f530-3a37-b83b-058a98d96aee | -6.69845 | -42.13605 | 2025-05-09 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| a89c2c2d-142c-3a72-b0cb-16e3e74ffc9b | -3.99645 | -43.24794 | 2025-05-09 03:47:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc8ca8a3-2409-3958-ba5f-059543521231 | -11.56419 | -47.61039 | 2025-05-09 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7fcaa3c6-cbac-3c4e-8fc5-a8dd67626016 | -8.01089 | -41.60268 | 2025-05-09 03:47:00 | NOAA-20 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| daa1340b-aaeb-30f8-96ee-5de6479d667f | -5.16799 | -45.10547 | 2025-05-09 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| af00a13d-1b44-3571-b99a-5353f56a9caf | -6.96219 | -42.78543 | 2025-05-09 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f8d29ed0-4c13-32a7-85d9-79866a6027ee | -6.96713 | -42.78215 | 2025-05-09 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 31a26600-bdbc-3cb6-9f0e-cc28b93d0a86 | -7.62491 | -46.48178 | 2025-05-09 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 01b8ba86-2a85-33d4-98fb-884da1d3a31a | -5.77299 | -43.48101 | 2025-05-09 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5799a31c-2947-3f2b-97ad-e9d49684168f | -8.07949 | -43.12472 | 2025-05-09 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.7 |
| 16ee3fa7-1a2c-3a7b-8c2f-62c046987239 | -7.08102 | -43.62386 | 2025-05-09 03:47:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| df576a7c-84cc-3dea-82ef-e5e246e70c60 | -13.24686 | -48.4095 | 2025-05-09 03:47:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eade4911-fdd7-3cd7-9c80-9bcc53619787 | -4.00108 | -43.24871 | 2025-05-09 03:47:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f9db8db-a684-3c66-9f94-73261f87c221 | -4.89323 | -37.52986 | 2025-05-09 03:47:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f98ac9c1-ff85-3fcc-b696-ee1c0d8c2062 | -10.9882 | -44.45643 | 2025-05-09 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1585688f-9d45-38a2-b247-84dcce3531a5 | -11.5573 | -47.61676 | 2025-05-09 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 134fabc9-8a7b-3d8b-9c4b-1b8c2f8056fa | -11.55802 | -47.61307 | 2025-05-09 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26998cc8-600c-3f75-be81-95be6d208578 | -6.97003 | -42.78141 | 2025-05-09 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d5f80b7b-0f80-39b2-8e12-9230297b3c8a | -14.20762 | -45.46692 | 2025-05-09 03:47:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ff4e8b98-ba99-327f-8478-c79765f9e604 | -7.21235 | -41.33066 | 2025-05-09 03:47:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 24f8a41e-5726-39af-b0d4-d2e0ffa9095a | -8.08018 | -43.12062 | 2025-05-09 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.7 |
| 9d9894bc-40e5-3efa-8f77-bd71ce894684 | -6.97013 | -42.80608 | 2025-05-09 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2beb7600-2df6-34f4-af70-276047884e0e | -10.96752 | -44.44307 | 2025-05-09 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0bee76a-7f18-3038-a4f9-20c944df3e79 | -6.50599 | -44.72847 | 2025-05-09 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cb1cb224-1ee0-34d0-bf57-53a90085eb12 | -12.86142 | -38.36486 | 2025-05-09 03:47:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8c92ea13-7308-316a-8fc0-a457619c6005 | -8.0709 | -43.12318 | 2025-05-09 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| cd7863ff-f337-33b5-8881-f2ef5e452b61 | -6.69782 | -42.13977 | 2025-05-09 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| a052ec45-5991-3718-8134-43b48c6da923 | -5.16284 | -45.10448 | 2025-05-09 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3e71e56d-7291-3ace-b9d1-bbd064734304 | -10.97439 | -44.43046 | 2025-05-09 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f1a8601-f962-3922-be34-addf5ec93df2 | -10.97644 | -44.44478 | 2025-05-09 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4092dba3-e47b-3fc9-ab13-35d5b8962492 | -8.07879 | -43.12882 | 2025-05-09 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| d92db77f-f205-343e-b81c-1c73f344313e | -5.16427 | -45.10613 | 2025-05-09 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0a48721f-5969-3da1-9102-0f1a0915f9d1 | -13.61676 | -43.97699 | 2025-05-09 03:47:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ecf5484-4ab7-3b32-8cca-75c5a95df84d | -6.61408 | -48.01316 | 2025-05-09 03:47:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48e68690-0051-30ee-8fc4-8c40dcac48d3 | -6.96286 | -42.78141 | 2025-05-09 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3d417826-a212-37a7-a9d1-75407440c01b | -8.0581 | -36.14765 | 2025-05-09 03:47:00 | NOAA-20 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c9266d9f-47c5-37d0-9ee2-8319aa120ffc | -6.62133 | -44.77499 | 2025-05-09 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 861dd683-9fcf-3664-b6a8-30f05003d9c5 | -11.5651 | -47.86779 | 2025-05-09 03:47:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 608d234e-dc9b-3e76-baad-cd9f61b3f353 | -14.20225 | -45.47074 | 2025-05-09 03:47:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff4e4e85-fa43-3884-8312-3f15e3bd6fdf | -3.99564 | -43.25276 | 2025-05-09 03:47:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ce61c3c-f4a3-385a-95a8-913a3aed5382 | -13.66664 | -43.72718 | 2025-05-09 03:47:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1542539f-fce8-3492-b462-65f9255c0b93 | -14.20397 | -45.46133 | 2025-05-09 03:47:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 435d8dc5-90da-3f34-b333-7ce6ed0855dc | -6.9678 | -42.77814 | 2025-05-09 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README4.md)
