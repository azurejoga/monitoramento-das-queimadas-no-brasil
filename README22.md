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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 915aba78-371b-34e1-8da7-1d3945fd0bd0 | -3.8391 | -55.7799 | 2026-10-10 02:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 616ed9aa-b22d-30da-9d4c-697e14928b6e | -4.4025 | -49.7774 | 2026-10-10 02:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| a233bcc7-3998-3e5d-b538-e931e1b43477 | -7.9086 | -54.7194 | 2026-10-10 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| e814bd28-04fd-372f-ac31-7924cbf04f7a | -3.5864 | -54.5942 | 2026-10-10 02:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 99a5628c-3737-3385-b022-bd02ece95010 | -10.6201 | -60.4658 | 2026-10-10 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 35780fcd-8936-327e-9180-fbc54ea4f6ed | -10.9097 | -44.8206 | 2026-10-10 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 206.0 |
| 5959bf95-7190-3560-85e3-9e3ffe6d9a26 | -10.601 | -60.5056 | 2026-10-10 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| bf4147e7-f474-3773-9ad3-8cc4146ac14a | -7.0228 | -47.661 | 2026-10-10 02:00:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| d8627837-b28f-304a-aff8-2ab25f02c21d | -3.9912 | -59.356 | 2026-10-10 02:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| c41303c2-f2ab-329f-84c8-952f727d3c57 | -4.4507 | -47.9112 | 2026-10-10 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 8ba30098-644d-37be-af47-8eecb25df25c | -4.5929 | -55.7366 | 2026-10-10 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 9d3df1f8-c168-3205-a949-4606e7fcb40f | -12.2154 | -57.1287 | 2026-10-10 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| fe029aba-fba1-37a3-938b-22a4edee97b1 | -10.9093 | -44.8438 | 2026-10-10 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| ed7c87db-4cfd-39af-9804-4d39a026b4b0 | -3.2204 | -49.4205 | 2026-10-10 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 6dcf13a5-d7bf-3131-8475-4b9c09f082c2 | -10.6199 | -60.4852 | 2026-10-10 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| eaa7b285-4355-3517-a4ff-b03148c1426e | -3.2571 | -54.1824 | 2026-10-10 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 4b95b6a0-c8e4-3393-9775-abb086199b46 | -9.9384 | -44.8791 | 2026-10-10 02:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| e091c7a8-b024-3476-b9e9-b3657ba2cb98 | -10.6012 | -60.4863 | 2026-10-10 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 191.6 |
| 9cdece48-6b40-3082-9a80-b4c17fdf7b28 | -7.9272 | -54.7182 | 2026-10-10 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 55482cdb-1f71-38b2-9eeb-54b6ec733b40 | -3.1284 | -54.1857 | 2026-10-10 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| a5ce0a78-a2fa-3aaa-9329-ccff0bd8fa9d | -3.5864 | -54.5942 | 2026-10-10 02:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 39268d90-b46b-34e4-bbc5-6671dedb9bd9 | -3.5491 | -54.7351 | 2026-10-10 02:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 2f957310-e669-3eab-8ab0-dfe44484115a | -3.839 | -55.7997 | 2026-10-10 02:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| c4b94038-3231-3d42-bfe0-91be216ef2f6 | -10.9093 | -44.8438 | 2026-10-10 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 258.3 |
| 08d3386a-9600-3517-a3ef-defb8db91264 | -3.9912 | -59.356 | 2026-10-10 02:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| e289e928-7100-3c2a-a85c-da0f9539e967 | -12.2877 | -63.3711 | 2026-10-10 02:10:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.9 |
| e77c48a1-b3a4-3901-ad01-8ed09cd74ec2 | -3.6048 | -54.5936 | 2026-10-10 02:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 6b22a428-2e75-3ec0-bf53-833481bfa565 | -10.6012 | -60.4863 | 2026-10-10 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 209.4 |
| fe7cd392-9a21-3e5a-8ae2-bc9ae3baf4ec | -7.2283 | -44.1622 | 2026-10-10 02:10:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 59c52695-5205-3fd6-a301-495b92b09dec | -7.2471 | -44.1604 | 2026-10-10 02:10:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 092c263c-a680-318b-a2c5-7fd5eb8bedaf | -11.0137 | -45.4501 | 2026-10-10 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 50db5422-c500-3ec1-ab48-aa621d37000c | -10.8902 | -44.8464 | 2026-10-10 02:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 123.1 |
| ae5d5b0c-5dd7-3741-b372-3cf4545a31ea | -10.8909 | -44.8001 | 2026-10-10 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 73bf6e8e-4dc9-30a3-a41d-cf8fc066526a | -10.6013 | -60.4669 | 2026-10-10 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 9d87e92c-8597-30c1-900f-5c691efbb8c3 | -7.535 | -45.3006 | 2026-10-10 02:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 5305cd1d-66bb-3568-a0c8-d5608c254c31 | -7.5162 | -45.3024 | 2026-10-10 02:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 599ba655-f101-3340-82dc-85e9ccdff876 | -3.2203 | -49.4417 | 2026-10-10 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 28ec2f77-82cc-3e44-a134-bc83e93cfc3b | -9.9384 | -44.8791 | 2026-10-10 02:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 123.2 |
| f48dadbb-326f-3875-8b7b-8759414d1633 | -4.5929 | -55.7366 | 2026-10-10 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| a8f6a1be-0911-3d95-b61f-cdb51bc07c1e | -4.5929 | -55.7168 | 2026-10-10 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 9a46fd49-1ead-3002-8ba5-07f810fad3ba | -18.9222 | -47.9105 | 2026-10-10 02:10:00 | GOES-19 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 7cf7770d-6fa7-3a70-ad62-f08053c643ee | -7.9086 | -54.7194 | 2026-10-10 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| e74aa408-2933-36b1-bbf3-1dfd2e7fd245 | -7.4975 | -55.0055 | 2026-10-10 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| bf44aab9-5901-334d-b6ac-66a6ece5b765 | -5.7378 | -45.1307 | 2026-10-10 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| be084a97-0ca4-3c61-8fe6-730333f088cf | -3.2204 | -49.4205 | 2026-10-10 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| caecd05a-5e78-388f-b54f-d9d5de96b331 | -5.7565 | -45.1293 | 2026-10-10 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 2bc8df55-b546-3e5c-92c2-8dada1254033 | -11.0335 | -45.4016 | 2026-10-10 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 757de2f3-0c62-3596-ac55-9594128bebcb | -6.4411 | -55.0424 | 2026-10-10 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| fb7b9212-2f5b-3160-9c54-aeaa965876c3 | -18.3327 | -42.3849 | 2026-10-10 02:10:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.1 |
| add44503-00d3-3951-ba41-eb14f44768f9 | -13.386 | -43.8945 | 2026-10-10 02:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| cdb4ce78-f1a9-36c1-b4f2-f38437ccf2ef | -7.5347 | -45.3233 | 2026-10-10 02:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 9f10540c-13b2-3fd5-bb04-b1da2e365031 | -10.6201 | -60.4658 | 2026-10-10 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| f2b4bb13-2ce5-3907-afe3-787764dfa876 | -11.014 | -45.4272 | 2026-10-10 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 06b89389-4ae2-3985-8ebc-a15b929d6a49 | -4.4025 | -49.7774 | 2026-10-10 02:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 5bb49670-7db1-383e-be1e-6216baa02bfa | -7.5687 | -64.585 | 2026-10-10 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| d0542cbc-7cbc-3031-803a-8e1d6b3f850b | -13.3666 | -43.8979 | 2026-10-10 02:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 3bec79c7-2e64-37f0-9d0b-649649d78770 | -2.9451 | -54.0698 | 2026-10-10 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| fa208240-ec88-3e76-83b7-8ec27590cf1d | -6.9318 | -59.2605 | 2026-10-10 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| c5af322c-ba75-322e-b228-34aa31545bf2 | -11.0933 | -44.1209 | 2026-10-10 02:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| f922d316-146b-3818-a976-dcb9edc97ecc | -3.1114 | -53.7839 | 2026-10-10 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| c49f2148-f8d9-342f-adf0-b82bdbab21b3 | -3.5676 | -54.6946 | 2026-10-10 02:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 8b1fe052-23c2-30e5-bb66-c9e8deeddb2f | -3.7494 | -60.6014 | 2026-10-10 02:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| a098a86a-c76c-3ef0-8a77-d67996f8c71d | -3.6397 | -60.6226 | 2026-10-10 02:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 2b348151-4d04-3113-aa17-717cb331fad3 | -3.1285 | -54.1657 | 2026-10-10 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 5345b13f-2f30-3cdb-889a-3bf15c1af94b | -11.0328 | -45.4475 | 2026-10-10 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| f4b8f091-133f-3452-b3d2-009e5176531a | -3.9911 | -59.3752 | 2026-10-10 02:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 4622d75d-94ef-3f32-bc38-7f4b063f6fdf | -10.8905 | -44.8232 | 2026-10-10 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 321.6 |
| 0e2e9683-3606-3eac-9d7f-dafa4d043a41 | 2.727 | -60.2586 | 2026-10-10 02:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 6e269ef5-4abd-3d30-b46d-a5a618545ebb | -6.9319 | -59.2412 | 2026-10-10 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.3 |
| a69bb81d-4bda-3cab-bc8f-2a802c22d52d | -11.0144 | -45.4042 | 2026-10-10 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 08f92e44-98d6-3e00-925b-eead4e714b2d | -11.0332 | -45.4246 | 2026-10-10 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 50b738c7-1fc3-34ad-827b-33c9e246b93a | -7.5871 | -64.5845 | 2026-10-10 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 210a20d3-8bfb-3bd2-b3b1-2de73e4a3911 | -7.5159 | -45.3251 | 2026-10-10 02:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 9699ce52-2431-3b33-994e-e3480d5cb063 | -10.6199 | -60.4852 | 2026-10-10 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| d043c644-550a-3d62-a06e-43712be24825 | -10.9097 | -44.8206 | 2026-10-10 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 644.8 |
| 7298b26e-becf-3699-9c10-2e98e6711e66 | -10.91 | -44.7975 | 2026-10-10 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| fe1e751f-4d95-31b9-9c78-edb461169d85 | -10.89 | -44.83 | 2026-10-10 02:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fc02f91b-0c17-3171-ba4c-7defee87aa68 | -3.9911 | -59.3752 | 2026-10-10 02:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| b5b2a971-fd1d-3eab-96cf-554be6188afb | -3.2204 | -49.4205 | 2026-10-10 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 28d7289e-ba4a-31d7-90b9-ca117a2e18c5 | -7.927 | -54.7384 | 2026-10-10 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 2bcbfe02-0352-33ee-820c-f91044e92fdf | -7.9086 | -54.7194 | 2026-10-10 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 2cc77d09-2108-3074-ab29-df2ca7b9c0b2 | -12.1015 | -57.1583 | 2026-10-10 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 4d3b7d3a-5231-33e2-83fb-300b80da0918 | -18.9222 | -47.9105 | 2026-10-10 02:20:00 | GOES-19 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 781a1bb5-d5a4-3ab2-a095-d7380f5f2120 | -11.0332 | -45.4246 | 2026-10-10 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 33973031-3e5c-317b-bbdd-418409b719a7 | -6.4566 | -55.5008 | 2026-10-10 02:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 28dc2e50-7b07-3489-9277-db03ae8c0c38 | -3.2031 | -53.8621 | 2026-10-10 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| f4a27f54-b02c-3205-b8b0-3fe676092ee0 | -9.2787 | -47.389 | 2026-10-10 02:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| ea9757f8-a4c9-3187-99fd-5669a0a71ca4 | -10.6201 | -60.4658 | 2026-10-10 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| e2346018-09d8-313f-9e72-621d12475329 | -3.2388 | -49.4411 | 2026-10-10 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 394c9d27-f01c-3119-a618-a73499787273 | -3.5864 | -54.5942 | 2026-10-10 02:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 3a5f512d-bd87-346b-a5e4-c8805ca4f807 | -7.5687 | -64.585 | 2026-10-10 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| a14ae312-3da6-36e5-83eb-e32b3490b4b4 | -3.9912 | -59.356 | 2026-10-10 02:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 2ad14e68-111e-3f46-8423-7c5aa7f2e2b6 | -10.6013 | -60.4669 | 2026-10-10 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| e76fc0a7-3730-3f0b-a21d-e948c5e98c3b | -3.6048 | -54.5936 | 2026-10-10 02:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 08395eac-6018-3fb0-8184-f2d724669667 | -3.7494 | -60.6014 | 2026-10-10 02:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| a77361cd-a5d8-3617-8bc3-c5bc9eed03aa | -10.9093 | -44.8438 | 2026-10-10 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| d3b8ae61-b635-3ee0-ad75-2d10732c55af | -4.5929 | -55.7366 | 2026-10-10 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 030c238d-615b-355f-8afc-e7ccd3d6855e | -7.2283 | -44.1622 | 2026-10-10 02:20:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 4aaeb013-7d27-3830-a2e8-23c34f8c29a3 | -9.9384 | -44.8791 | 2026-10-10 02:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 8b41388f-2a5b-3e9c-a9e6-47769831a6e8 | -4.4025 | -49.7774 | 2026-10-10 02:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |


[Clique aqui para ver as próximas entradas](README23.md)
