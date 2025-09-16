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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 819c627e-6a0b-3986-935d-574124e2fb41 | -11.6434 | -46.591 | 2025-09-16 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 15ab802d-271d-39f1-8da0-ed0946e14e64 | -10.7302 | -46.5082 | 2025-09-16 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 243.6 |
| 2872a008-6a53-3c42-b357-fa2ac97a2f6e | -8.613 | -46.39 | 2025-09-16 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| bcd30d13-fc41-3ffe-a377-f39a7acb5765 | -5.8088 | -43.4724 | 2025-09-16 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 127ff3ea-8109-371b-be83-87a722b359eb | -12.8087 | -44.744 | 2025-09-16 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| b04b3777-bc4c-348a-b786-d23d66543dac | -8.6885 | -46.3823 | 2025-09-16 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 416feda7-c733-3eb5-94fc-5ac932c2e116 | -8.22 | -49.4901 | 2025-09-16 14:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| df25a8dc-a194-335a-ac26-3ab5e52757f5 | -3.8416 | -44.0824 | 2025-09-16 14:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 78f7f47d-599d-3b78-a41b-55741f72d571 | -8.5939 | -46.4143 | 2025-09-16 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 9bac1336-b81a-3577-8764-d5336abdc363 | -9.1709 | -46.9792 | 2025-09-16 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 660285d3-d402-35d8-bb08-8b6d994300cd | -4.5934 | -43.3239 | 2025-09-16 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| ec9d144a-2698-3d60-8774-70061639f259 | -5.7873 | -45.8931 | 2025-09-16 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| cf88a00e-5d5f-3d55-99e1-ba5ebb0edb05 | -15.8624 | -59.3779 | 2025-09-16 14:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 98c722d7-6408-39ac-b175-307ebe62a54f | -13.222 | -47.3097 | 2025-09-16 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 964e0b3a-e1d0-3287-9050-b8347dbba152 | -12.1861 | -44.0958 | 2025-09-16 14:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| df447e46-3ed5-3f01-baa7-c38af185157e | -8.9259 | -45.5231 | 2025-09-16 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 0213c38c-e452-3ac1-b85a-31a53b89b394 | -9.7322 | -47.3625 | 2025-09-16 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| e4149fb6-c255-3dff-9aa6-2a1930fb0ce8 | -6.3623 | -44.399 | 2025-09-16 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 1f3eed8e-ee77-3111-a052-c5d7de1054a2 | -8.6319 | -46.3881 | 2025-09-16 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 6ae09354-b238-382b-93b1-a58191d5acfd | -10.7112 | -46.5106 | 2025-09-16 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 61aaea1c-8155-333e-abfc-59ea829f9ee8 | -10.7299 | -46.5307 | 2025-09-16 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 294.0 |
| 53053254-4214-395a-9fa0-9061e6040965 | -9.1053 | -44.8412 | 2025-09-16 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| c199a108-9d2b-343b-9ec0-a3b64a60df6a | -8.3323 | -44.7426 | 2025-09-16 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 98.4 |
| e8e3d793-7242-3a9e-8aa0-a9943d3e916b | -11.467 | -43.5485 | 2025-09-16 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| efcd7960-c896-3ca9-ac1b-f6d0b6bf41cc | -12.6953 | -47.7446 | 2025-09-16 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| f33dbad7-c482-3866-8e81-2864357b7507 | -13.2801 | -54.2228 | 2025-09-16 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 471.6 |
| 90221868-2372-37ca-9f70-3cfb85f12757 | -9.7445 | -47.8468 | 2025-09-16 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 54290e62-23b2-3a92-882a-5fe6ce99b8dd | -7.45 | -46.1871 | 2025-09-16 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 97d1fd44-7a14-3b04-a7ee-d8fe322e4c5d | -5.9006 | -45.7506 | 2025-09-16 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 7e81eb54-3fe5-32b2-8796-1b2481ceb41a | -6.356 | -43.1476 | 2025-09-16 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 283.5 |
| 3d1cdf5a-8bbb-3f0e-992f-59562d95ad78 | -8.7674 | -46.1049 | 2025-09-16 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 7d07c78c-e184-314e-9292-bee9e884562a | -6.6698 | -45.5118 | 2025-09-16 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 9caedf96-9930-354a-91f8-1838c0bd0786 | -11.7147 | -46.8964 | 2025-09-16 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| d8fc6e83-a981-3bbd-9295-594aa0e27b0a | -7.1505 | -47.9786 | 2025-09-16 14:00:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| dabd2625-5649-3a30-a728-5ca81149824e | -5.7858 | -43.9378 | 2025-09-16 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 5593ca03-cab4-3410-9729-bcd8c35d898d | -10.6548 | -46.4727 | 2025-09-16 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 126.0 |
| a5359f08-2644-36e8-8bee-f59f55e72349 | -6.1693 | -41.1872 | 2025-09-16 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 138.2 |
| c0c70d28-1fc6-3a4d-af1c-b132dbdd170b | -14.3944 | -52.9034 | 2025-09-16 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 19356d9b-2bb9-3805-a328-fd3c84ecd154 | -7.6738 | -44.6717 | 2025-09-16 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| a6424856-ed37-3054-99c1-fdc69c2c44b6 | -14.3295 | -46.0626 | 2025-09-16 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 103.5 |
| f2b3a20f-3193-3539-9e9a-5176fe178ba7 | -7.2771 | -46.5814 | 2025-09-16 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 0292eee7-b677-3f34-83cf-ca85c3131a94 | -9.086 | -44.8663 | 2025-09-16 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 175.9 |
| 9b7a868a-eff2-362e-852f-aa57c653527d | -5.994 | -43.7134 | 2025-09-16 14:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| a7046535-9984-3f91-b05e-49dfa37a32cd | -6.381 | -44.3975 | 2025-09-16 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 022e8bd1-6847-30f6-9af3-bb28495e7ef2 | -6.362 | -44.422 | 2025-09-16 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 9f9853ad-8cab-34fb-8043-c067f3f226c9 | -13.2027 | -47.3126 | 2025-09-16 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 163.4 |
| 36163da4-3794-3507-8852-0ac1cd7d6947 | -10.0803 | -48.1616 | 2025-09-16 14:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| c0116fcb-4347-3766-95c3-0e6b43c510a1 | -11.4477 | -43.5514 | 2025-09-16 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 195084f3-8f38-3bd6-b01a-87de10c981e6 | -7.2768 | -46.6036 | 2025-09-16 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 169.2 |
| e38d3cda-702e-3507-af1c-49e0c6efa785 | -6.1878 | -41.2097 | 2025-09-16 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 147.5 |
| 65beaede-d3fe-3af5-afae-f8d865baca3b | -14.3751 | -52.9059 | 2025-09-16 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 74cf0a9a-c20b-3706-9e8a-70690c3e729c | -10.3699 | -50.507 | 2025-09-16 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 568d8de7-291f-39af-966a-ed2bde2fc945 | -10.7489 | -46.5283 | 2025-09-16 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 28d2f7ac-a65d-3d4e-b351-cce7e2b3f3e4 | -11.7151 | -46.8739 | 2025-09-16 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| d9102bc7-9185-33b2-b547-f9f1a22338c8 | -6.3808 | -44.4205 | 2025-09-16 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 83e80b92-ec6f-3786-a70b-db30af2fd4c9 | -10.9671 | -47.1729 | 2025-09-16 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| e6d5240f-df34-30ac-a1f5-8a366ed32c71 | -11.7342 | -46.8713 | 2025-09-16 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 534c7604-f22d-383c-be5d-229a1bfdc9e4 | -9.7903 | -45.9235 | 2025-09-16 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 607ad6f6-a6c6-372b-b88c-e366e694ce24 | -9.105 | -44.8641 | 2025-09-16 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 531.2 |
| 3748226a-a0fa-37e5-bd2d-3fea60f5558c | -6.169 | -41.2114 | 2025-09-16 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 136.3 |
| d15c528f-66aa-3206-8e0e-2976583e1322 | -13.2031 | -47.29 | 2025-09-16 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 4b14d47e-20a3-3322-9da4-ff9bfb668543 | -11.2737 | -50.8163 | 2025-09-16 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 5871eefc-8e37-3fd1-aa4e-012d75ee8c2d | -14.3498 | -45.1093 | 2025-09-16 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 07592600-4ba9-342d-8970-7d2daf185395 | -8.6699 | -46.3618 | 2025-09-16 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 045c6971-7711-3137-8ffa-12825a3ac7db | -13.2798 | -54.2435 | 2025-09-16 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 90e36df3-0d45-3eba-8f08-5280b05aec69 | -14.3295 | -46.0626 | 2025-09-16 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 88.4 |
| ef921db9-0d5e-31b3-8425-309acf9769d0 | -13.2031 | -47.29 | 2025-09-16 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 2c604df2-550b-3a40-8313-fbecfa61b678 | -10.7299 | -46.5307 | 2025-09-16 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 359.6 |
| 4d88c6c1-af98-379d-b927-40e989dea2d0 | -7.6738 | -44.6717 | 2025-09-16 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| d84866f4-e4e2-3c63-a301-4c828ce133fe | -8.917 | -46.2015 | 2025-09-16 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| f8a95c9e-366c-352a-9835-a01e7cdb387e | -5.9942 | -43.6902 | 2025-09-16 14:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 593b7592-8d72-3746-8180-0c8f62afa80f | -7.7229 | -45.3056 | 2025-09-16 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| a8232019-cafa-3b2a-b504-71a58875a5ff | -12.065 | -46.5323 | 2025-09-16 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| d0fffcee-da14-3d33-b71c-aec72794e3db | -9.7445 | -47.8468 | 2025-09-16 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| c2f958d7-f2cb-32e8-b81b-7b749c0b7e10 | -8.6513 | -46.3413 | 2025-09-16 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 116.1 |
| f8fe6dc0-7a44-3fb5-a0d3-807cc61195c6 | -12.6909 | -47.9899 | 2025-09-16 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| fea79e3f-75be-3879-8437-b564c995c404 | -14.6143 | -46.3806 | 2025-09-16 14:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 137fb68a-3368-32bc-933b-311100627444 | -12.4322 | -49.7135 | 2025-09-16 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 02423a61-a3f5-3d16-986b-e990f8db9b34 | -7.1505 | -47.9786 | 2025-09-16 14:10:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 02629b0a-8869-36ba-bc6a-0add76f7d42d | -8.7677 | -46.0823 | 2025-09-16 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| fbee53ee-4b1f-3be1-be28-8851bf2912ec | -7.2768 | -46.6036 | 2025-09-16 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 186.4 |
| 64eafadc-d76d-3510-82a6-53166c61f2e8 | -6.4105 | -43.3301 | 2025-09-16 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| a2241729-6ea7-3dfe-b8fe-cab0624b8d4a | -13.2801 | -54.2228 | 2025-09-16 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 346.6 |
| 4126930d-a413-3875-9f7e-839b5afd9299 | -3.4179 | -43.154 | 2025-09-16 14:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 1015a965-9e9f-39d0-95ee-1b7ed24aa9a8 | -11.4853 | -43.5929 | 2025-09-16 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 8a150492-7914-305f-a8c4-338cf10a6acb | -8.9259 | -45.5231 | 2025-09-16 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 34c5b569-eb48-391a-a7a4-d6425c8c2ebd | -3.8416 | -44.0824 | 2025-09-16 14:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 143.6 |
| e986d3ab-6a89-3fed-aef8-33d001adc07c | -7.5269 | -44.3644 | 2025-09-16 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 21135fb6-91ec-38f2-9b46-1c2d01b3c55c | -6.356 | -43.1476 | 2025-09-16 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 308.7 |
| b0fcefd4-2675-35fe-a7ce-c73aa9f11ebc | -5.8809 | -45.8641 | 2025-09-16 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 5bb0a539-3b75-3cd8-8e6c-40a4e5f984b7 | -11.1299 | -45.3426 | 2025-09-16 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 744a5da8-5dd4-34bf-be86-61ff5a743992 | -10.7493 | -46.5058 | 2025-09-16 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 214.9 |
| 16ebc6bd-9563-3230-bfa4-579671b8fca1 | -7.078 | -44.153 | 2025-09-16 14:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 52a70959-0ed0-3597-b459-085c2eedd3b7 | -9.105 | -44.8641 | 2025-09-16 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 229.2 |
| 7740ec82-1f97-3e66-86f2-dc2435bab148 | -9.0857 | -44.8893 | 2025-09-16 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 188.3 |
| f4f0d283-4faa-3d9b-8fdc-c8128b94a948 | -10.0728 | -48.7086 | 2025-09-16 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 456984cf-a37a-3c3a-8dd7-171bfe658753 | -8.9164 | -46.2465 | 2025-09-16 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| d40d1f03-3473-3017-8b51-e69e161da22e | -9.1706 | -47.0014 | 2025-09-16 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| b5a2a980-d463-3831-915b-628a1eb3c7c5 | -11.467 | -43.5485 | 2025-09-16 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| b05c02c2-9e12-3b28-b05b-61aefa335293 | -5.7871 | -45.9155 | 2025-09-16 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |


[Clique aqui para ver as próximas entradas](README98.md)
