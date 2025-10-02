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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3cf0999-86f7-381a-a785-a0e1b64311ee | -11.08578 | -47.84922 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd939d58-4e37-312a-bdc1-9f3c0c85239c | -8.89879 | -46.6236 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dddba5f2-4e96-358a-9b16-6833822a8024 | -9.03583 | -46.68108 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab5cfc8d-71a4-33e7-a1da-b124f90ac161 | -6.32427 | -43.02483 | 2025-10-02 04:29:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74f832be-3960-336d-aa6a-bfbe178013a7 | -7.26474 | -45.48803 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80a03da0-1f89-305b-b133-7015a38517f7 | -10.2312 | -50.32088 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 404e9306-41ef-33f7-8258-c99d5661af5a | -6.96637 | -45.31872 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b60a9b24-9e31-3e2d-abf7-9de8c9424061 | -9.94976 | -43.70768 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8ffa2cc-d9ae-3ae9-8dfb-f65621abf639 | -11.09029 | -47.82095 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7a15cfd-0aa4-33df-a4a0-f2fc70e05b8c | -7.71518 | -44.96651 | 2025-10-02 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06a9e0d2-7262-3070-9cca-3362fff62a5c | -11.10604 | -49.80369 | 2025-10-02 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 662a2a36-6948-3c9f-8ba8-c22412a951dd | -11.46501 | -45.13374 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 082d8742-63d8-32ef-9b31-0b7c94b2b641 | -10.99986 | -46.59513 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9ddf0f1e-d718-3e43-b020-69ac7da3fa45 | -10.34474 | -48.19524 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e40de59-62c9-3a2b-81f9-e005c0bb03e4 | -5.86007 | -45.73689 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 367046fb-4085-3364-a551-e25f508920e8 | -11.53117 | -46.95577 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcb47ca0-a98f-3f6e-8eac-98e16841ac12 | -11.09691 | -47.84375 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f67f4ea1-21fb-3ee9-9d18-7a0c3dcc51b3 | -10.2507 | -50.3156 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 3bb8bcb1-8b98-39bb-86b5-d2af766a74bf | -6.27837 | -44.05979 | 2025-10-02 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 863522d5-5383-3788-ab90-a5b745d88a35 | -7.54426 | -46.89042 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1cdaf8f-37a2-35ac-8e42-d99667a0e993 | -11.42426 | -43.49501 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d619b94-fbd7-3eb5-9a7d-898d7257c5fb | -6.35656 | -43.29903 | 2025-10-02 04:29:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 224c4965-0221-3c85-9483-ec640c01cc28 | -6.32474 | -43.04649 | 2025-10-02 04:29:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b4c4c3ff-86ba-3909-807d-39762151a583 | -8.68266 | -47.69281 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e58f86d3-b59b-36e8-b3eb-422f3cd3012a | -11.58935 | -47.64156 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5760fab0-eaf1-3c6d-ad6b-9fec2215cdb9 | -9.89663 | -45.95056 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0f672b7-f358-3a5f-8ce5-7afac47f0b82 | -11.86643 | -45.0015 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 59eb8247-805a-3c77-9784-a3df12ae2659 | -5.58089 | -51.56763 | 2025-10-02 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| afeae6d4-f0be-3799-8113-38a3861a44bc | -9.08131 | -48.02357 | 2025-10-02 04:29:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13f8111a-8ab9-356e-9dc0-28a054d193b3 | -10.84089 | -45.3828 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 068f98c2-5342-347c-bbac-0846ab36c0d4 | -10.44324 | -48.08302 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8c17105a-f08f-3293-b61f-202121a3d312 | -10.80282 | -44.24354 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 53ebce23-f20b-3a98-849b-a3549a3d7df8 | -5.48135 | -51.22656 | 2025-10-02 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06299f7a-86de-3e67-a693-97b05c18f4d4 | -11.52816 | -43.54632 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9efc1ea-52b4-3ead-9c3d-b6ffc449f403 | -11.86056 | -44.99246 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84d2878f-71d4-304e-9251-8ff5cb2b014e | -11.00097 | -46.58801 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a49b3b62-4c81-3e73-9297-572d795420a5 | -11.8205 | -44.97138 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 755eb72e-87cc-33eb-9a2d-ccf9b7acb29b | -10.22183 | -50.33225 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3ac24aeb-9bbd-35d7-8b6b-1bbaea326f4b | -10.87129 | -47.81463 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92a56f09-1930-3659-9eba-3358365f32d4 | -10.8234 | -43.66378 | 2025-10-02 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d1bdc45-a066-3b05-a8c9-8cf582068a9e | -9.94738 | -43.69849 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c8f515b7-5d0f-34ea-9520-aea71ad8d350 | -10.22254 | -50.32805 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3155dc13-3937-3288-87b5-e27ed7b6aec3 | -9.56459 | -50.94042 | 2025-10-02 04:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e35015c3-e761-3edf-8306-99adc2dcbac1 | -9.42175 | -47.35977 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee43216e-56d6-3ad9-85d9-4c915a7e6333 | -6.35752 | -43.29756 | 2025-10-02 04:29:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e6c75f7d-7ce5-3267-b809-a28e39eca2a9 | -11.47179 | -44.99411 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af45df13-188c-3f17-815c-794497dc9c86 | -10.30531 | -48.2477 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0837e3c7-d0fd-3d8b-a81a-fe50b5c56086 | -8.90293 | -45.0391 | 2025-10-02 04:29:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ed8e399-c963-38e5-ae85-053ae4eb5e0a | -10.1337 | -45.67874 | 2025-10-02 04:29:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9edc1c4c-21a8-339e-a5a9-a98b1cdd79ae | -9.94073 | -43.76788 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 0fdb5b44-1647-3654-8b55-f0fc6480e431 | -6.68998 | -46.69399 | 2025-10-02 04:29:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f08cb56-b780-3042-bdfa-0abb51ae10b9 | -6.82645 | -41.62606 | 2025-10-02 04:29:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 890d3147-4b79-38ef-9742-babb60139937 | -11.62226 | -45.04725 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db51a9f1-e801-3529-b940-94868256a8e2 | -8.52217 | -47.25481 | 2025-10-02 04:29:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fecda072-f039-364f-9c66-735d65c6d916 | -11.75208 | -46.82361 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71366f01-eb0c-3d9f-a887-b136ad2fe230 | -9.93405 | -43.76245 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9dce1e56-dae1-36dd-ac8f-bc03e09568a2 | -9.9504 | -43.70337 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d52393f8-239c-3bdc-b90a-52c114471f04 | -10.35067 | -43.73435 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 987501d0-330c-3b1f-a00b-0f1de2b23f4a | -8.64041 | -43.98006 | 2025-10-02 04:29:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06e31562-0fc9-307d-aa2d-f94b383e69a1 | -11.44226 | -43.88039 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6488b78f-1349-34bd-bb64-f964d61b844e | -11.03658 | -47.82332 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e4aef5be-1dbe-3861-ab07-f04b4aff20da | -11.48257 | -45.11514 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c888f15-31cc-3b31-bc6d-36e181cfc5a0 | -7.72143 | -46.22222 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c297f50a-712e-3fb4-b3ca-31459d42739e | -9.33645 | -45.69796 | 2025-10-02 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95b695e0-f266-3867-997c-59cc661be57c | -10.81509 | -46.62415 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a6ef90d-3743-31ae-959a-e2c291b00a0f | -6.70231 | -42.81145 | 2025-10-02 04:29:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5acf2f89-67bd-35ac-823e-bd7cab4790b2 | -11.35969 | -48.33912 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6972ee3d-7a92-332e-adf1-9ba507ffdf65 | -7.72697 | -46.20872 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 178a4642-7800-3c02-a0e7-34d932ab286c | -6.70058 | -42.79773 | 2025-10-02 04:29:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8197e925-e69c-33d5-9dfd-5e6a63d7d9c7 | -9.40698 | -47.58092 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| ed065f88-6bd7-3fda-8b75-4a3746de6e47 | -8.8253 | -44.79231 | 2025-10-02 04:29:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9292d6ae-6d76-3470-8a6b-02692c4d3ec0 | -11.81242 | -45.02574 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b6c2757-9699-3deb-9c51-24f140ed3784 | -10.20287 | -50.266 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3f68086f-5f66-3d74-adab-6c506bf3e50f | -11.06421 | -47.81303 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 757472cd-8b21-3adb-ba6b-be7d4a41186c | -10.70375 | -48.0012 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33159b43-a81d-3ee4-a238-4a90d9be4dab | -9.42841 | -47.36084 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9141c472-76d3-3278-8dcc-a566efd2b557 | -10.83848 | -46.62789 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 052e5b61-c66b-35e7-8ac8-d9c66389407f | -12.27621 | -44.1263 | 2025-10-02 04:29:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8e143c40-4c5f-38b2-9236-87af81af4aa4 | -9.93134 | -43.62921 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac7e1c61-88fb-3d92-ace2-239888ede7b8 | -11.17681 | -47.18856 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93911159-b780-337b-9ac6-67d04bcfd2bf | -10.2238 | -48.20852 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 923fe217-2719-32c1-a8fb-f6f820198348 | -11.80768 | -47.58632 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84f23ce3-62a6-3345-9a10-cab4faeef657 | -11.47003 | -45.00578 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68991bff-0776-3046-83ee-6b835d48d787 | -11.82367 | -47.67938 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46d77381-2c96-3c89-a374-afa41961d9b6 | -9.42366 | -47.58364 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a91117f7-65f0-38d6-9c69-b1d7ad3fcbe4 | -6.7246 | -44.60599 | 2025-10-02 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4da7babc-c8f3-3bef-8970-837e35d1a8af | -11.47131 | -44.97343 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b1bc4f4-6b9c-3836-afac-428836d614d3 | -9.80062 | -47.84747 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 36152ab1-be2b-3ae4-b803-f495b1039f90 | -8.57114 | -48.64436 | 2025-10-02 04:29:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5728a4d0-b0d0-3ed0-bc5c-235978f5a7ba | -11.43559 | -47.17974 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49b2e96a-5fef-35b0-a125-d742695243a7 | -8.55871 | -44.64476 | 2025-10-02 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5ae562e-7275-34dc-b784-59563cae9199 | -11.46884 | -45.01366 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6a2e74f-11a7-3d05-97c4-1690a0da91bd | -11.87288 | -45.03085 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 81ad9931-9017-3e35-8554-6b77f1932af7 | -10.14054 | -42.13663 | 2025-10-02 04:29:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 502f0fa5-75c5-3035-85b9-249155db63f7 | -10.94716 | -48.55924 | 2025-10-02 04:29:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11b2b405-4660-38f5-a89b-b1d00b5e2f2f | -10.79982 | -44.23883 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae4ab48d-f4d7-3a8d-8665-4eef75fd6d1b | -11.00321 | -46.59565 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64b3b35b-fec1-30b3-b086-fcb1ce37b04a | -6.69992 | -42.80213 | 2025-10-02 04:29:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e4f6e6bb-e500-30dd-a5f0-844f29e53279 | -10.834 | -46.61263 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61011cba-6fd6-392c-85b6-5b1147627210 | -6.32793 | -43.02537 | 2025-10-02 04:29:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README66.md)
