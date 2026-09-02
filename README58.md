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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb882f66-30f3-3292-8566-63535bd6115d | -9.04708 | -65.43684 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6588492-8b37-3749-bc7a-60f42b9fd835 | -10.90436 | -45.32179 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d660f10a-79d7-3078-9242-c14c463282a8 | -7.93271 | -61.75957 | 2026-09-02 05:18:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 199f9f00-30e3-36b9-81d1-083b925232a0 | -10.44181 | -46.72454 | 2026-09-02 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 4fc58f1a-4a8a-3bfb-b72c-636150fe2ff7 | -11.8315 | -46.05724 | 2026-09-02 05:18:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b778dd99-5175-3cd9-9661-a977671da485 | -10.90281 | -45.33529 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 75d63ff6-d640-3107-b656-9f12d4d41320 | -12.13425 | -47.1444 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a846b247-f1e4-308c-a761-cebeb9b11653 | -8.90226 | -62.36433 | 2026-09-02 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d33b22b4-549f-32e3-890a-141eb0d2ebbc | -8.26713 | -62.75965 | 2026-09-02 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 04d14f73-f751-3d59-bd05-7e68d44c278c | -8.56498 | -63.18803 | 2026-09-02 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 89a88442-6f7d-3dbc-8e4a-0ecdb8ba2ec2 | -9.94982 | -53.99257 | 2026-09-02 05:18:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 261e2da8-6960-35b5-ba0e-cff8f9cb09ff | -11.30559 | -45.17476 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a0e4d8cf-b6f9-3715-bd0e-15118661d0cc | -7.68507 | -67.12565 | 2026-09-02 05:18:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e574427-cc33-358f-a375-bcaa69bfc38d | -11.66453 | -50.18614 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56ee3f0e-19ae-3864-8df0-671ab0c8cab0 | -12.07267 | -47.12688 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b10ce3a9-98bb-3dd7-a416-bd8516b0775d | -11.32667 | -50.60279 | 2026-09-02 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 70a12393-9954-3ba1-a7cc-75bd58c1891b | -8.62155 | -54.84919 | 2026-09-02 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4559e53-a95c-3115-9408-248e150ed9b0 | -8.78482 | -62.48521 | 2026-09-02 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45484e13-d678-3391-b2da-96b52be4e30c | -9.94796 | -53.99474 | 2026-09-02 05:18:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a96b3b7-df9a-3025-9334-01ae28c5494c | -9.47708 | -60.46197 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83d02085-ddb8-3c5f-a6d3-35310af23afb | -12.14051 | -47.125 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54f0c42b-38b4-3c28-8c57-e7e1dd922c0c | -9.46933 | -57.03396 | 2026-09-02 05:18:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ec7a3c7-f093-36e8-99b5-6e935c053dce | -10.43424 | -46.73417 | 2026-09-02 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 244e5438-b7db-39c3-b0be-9c572e10b148 | -9.01252 | -65.41521 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea0a7405-2924-32d5-a46a-65a20fa124b3 | -12.13784 | -47.11445 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3d1f4e4-a308-323b-8c00-e99b37c6a563 | -9.87324 | -64.97779 | 2026-09-02 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ff08e267-ff60-343f-bede-1d43db76b962 | -8.56034 | -63.19089 | 2026-09-02 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a99438f7-09e8-3c68-b271-8b4d61a72aa2 | -10.31993 | -49.95843 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66140102-ed68-382a-87f3-674ac7dbc891 | -7.72993 | -60.9709 | 2026-09-02 05:18:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81ce60b8-14b3-33b0-9e7d-a11bd11ec047 | -12.14232 | -47.13017 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| daf82281-5690-35ce-bafd-28f64294ca4b | -12.14622 | -47.13084 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| abb45e3b-991c-3f3d-8e4b-6f6e50df017d | -10.67735 | -54.047 | 2026-09-02 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 58e77ded-8e5c-3ddb-813e-859260632182 | -9.69705 | -47.20702 | 2026-09-02 05:18:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bb1136c-a29a-33fc-983e-506806108c48 | -15.34259 | -47.04155 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 06c409c2-8e1c-36e4-954f-438cd025cc32 | -7.68263 | -67.12185 | 2026-09-02 05:18:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 179416a1-811f-3b26-b193-7e9edf660687 | -9.94095 | -53.98868 | 2026-09-02 05:18:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 82881d65-bf63-3136-acf4-39a7fcf1baa2 | -10.52647 | -57.43371 | 2026-09-02 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 003e3724-94f5-3ac0-98a2-95e320ee2cf6 | -8.56559 | -63.18445 | 2026-09-02 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e163c917-cb8e-3be1-bc57-b6e45f872a41 | -11.30809 | -45.1626 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 405f8fa9-eaee-3cb9-8f55-2f835c706718 | -11.30725 | -45.16978 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f093193f-2d33-3bfe-ace6-3d36ab1914a0 | -7.75988 | -61.19907 | 2026-09-02 05:18:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 606acc67-1cd5-3ef5-8269-7765790879f6 | -8.56902 | -63.18873 | 2026-09-02 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e53402e8-e993-346e-a1ba-f35f4c3ac573 | -7.75625 | -61.19844 | 2026-09-02 05:18:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cfea825e-c0bf-34b5-8b43-538505571524 | -9.45609 | -56.73917 | 2026-09-02 05:18:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9043cb27-0345-3333-aa62-1942387f6be1 | -9.08609 | -65.37839 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 09e6ce7f-3bcd-3f98-acfc-c50554209cd8 | -8.91451 | -62.36157 | 2026-09-02 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03f2cd4a-1a31-3a15-9246-c242b14084e4 | -9.92815 | -60.48729 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57e0f370-205d-3be1-9c24-1b3c7c853cc0 | -12.00885 | -60.53606 | 2026-09-02 05:18:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf98a0df-f654-3ce8-a5ea-b015eefe224f | -8.6209 | -54.85342 | 2026-09-02 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 844fa5e4-0909-3ec3-8fc9-b0d707af6ec4 | -9.39457 | -60.57437 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b69497fc-073a-31d5-8c6d-28558d74def5 | -10.50096 | -59.6184 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6eadbe33-21a3-3017-aa82-886d47f01a96 | -12.10184 | -47.0953 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fde380dd-3276-399c-a1d7-feefe228d141 | -11.05108 | -51.53122 | 2026-09-02 05:18:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f19a648-18ad-378e-8cf6-298c4d5533be | -8.26013 | -62.75313 | 2026-09-02 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa005ff8-696c-342d-b527-49e62ed5ec09 | -9.0203 | -65.45229 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 672929b2-0444-3d64-9f1c-61fcc0b2113f | -9.70824 | -54.33559 | 2026-09-02 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a71f67d-c600-39da-a610-2a390bce3ef4 | -10.43332 | -67.84308 | 2026-09-02 05:18:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41b49b42-30da-3feb-a3c1-7c3f100299c3 | -10.40563 | -50.00132 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2f0b170a-79cd-31d6-83f0-b27c7b2243f2 | -8.91833 | -62.36223 | 2026-09-02 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d17c9fb-b7dc-3713-ae73-694b50de99c5 | -11.34224 | -45.41164 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dcde8451-eaec-3f6e-a360-192922473778 | -10.43364 | -46.73911 | 2026-09-02 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| a5fdfeac-dddf-3651-adbd-aff6e77ff34b | -8.61728 | -54.85287 | 2026-09-02 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 386601e5-2405-365a-a441-40dc95346b36 | -9.95368 | -53.99315 | 2026-09-02 05:18:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d05e0933-099c-3926-a495-85dede068a34 | -10.90172 | -45.33985 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f5da59a6-c4ce-3ad7-97d0-871b36c5c57b | -7.68855 | -67.11951 | 2026-09-02 05:18:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95740d31-e3a8-37f8-a719-ee51e3db03b7 | -12.13183 | -47.05762 | 2026-09-02 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4d8c596e-96d0-3bf2-aaf1-837740ca8d38 | -12.13393 | -47.09378 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9fa739c4-44f4-3eae-9274-fe1ab4f7594e | -12.11924 | -47.0559 | 2026-09-02 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab5f60b4-f898-3c15-af24-bf228d77e6fb | -8.5563 | -63.19018 | 2026-09-02 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2160e0c7-46f3-39fb-98a5-823b4e68b7cb | -12.12703 | -47.09805 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72e48160-a27b-3399-9607-8c73e0ef74a5 | -9.86514 | -64.97175 | 2026-09-02 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84b38273-9072-3f35-a950-36cfc3c4adf0 | -9.93953 | -53.99838 | 2026-09-02 05:18:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cfa0162-cb62-370b-9192-e32a7684ed73 | -10.43485 | -46.72917 | 2026-09-02 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| aaeef767-7266-3241-a2e8-46da538c5575 | -11.32172 | -50.60212 | 2026-09-02 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| da7fd3dd-2de3-3801-b64e-38cc172eb78f | -12.1313 | -47.09353 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 158f304d-92af-36d9-8139-8ec98228be4e | -12.14792 | -47.11588 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c28b0907-6b98-3556-b76c-219ab5026efe | -12.14043 | -47.06905 | 2026-09-02 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d93f81c6-ae56-34a6-8d7a-5f7d574be105 | -7.72634 | -60.97031 | 2026-09-02 05:18:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6680f79-207f-3f90-8956-24056adc641c | -8.91568 | -63.28547 | 2026-09-02 05:18:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 15.3 |
| fb1c4e69-609b-3dfd-bab1-91e426bd9735 | -8.82998 | -62.31097 | 2026-09-02 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82a52706-c1a0-3674-942e-700da796b196 | -9.08964 | -65.376 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f509db23-b45d-3ff7-96e2-083300efc79a | -9.92845 | -67.84348 | 2026-09-02 05:18:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9fd0f3c5-127e-371f-9114-4d5aea068523 | -9.08524 | -65.38325 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51a83c2e-ad94-3391-b26d-20aa985defac | -10.90896 | -45.34256 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 8264ed64-662d-370b-a356-62c4385cc728 | -10.94195 | -61.42875 | 2026-09-02 05:18:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dedbf69a-79d9-35d0-be96-e7d6e0c0d5d7 | -8.77713 | -62.84097 | 2026-09-02 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb91354e-09af-360d-b390-bfe45db97adf | -9.8264 | -63.01003 | 2026-09-02 05:18:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd282e7e-0e21-3bb5-b168-c21ab595da2c | -8.75692 | -62.81655 | 2026-09-02 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 706e70bf-87c4-31f1-9b09-18ffc2a23a1e | -11.0016 | -45.07698 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8b8aefc3-414a-3e68-9942-38af1bfb0cab | -12.13469 | -47.06328 | 2026-09-02 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8bfd2ca6-c8a6-3016-bfcc-2659910f7eac | -10.3834 | -49.98844 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 69604ced-7ae6-3314-8ca2-57bcbcfc947b | -10.44245 | -46.71927 | 2026-09-02 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 418b2deb-b537-37df-a53c-bae7b1f91c03 | -9.92553 | -60.48753 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7862ed9-9d8c-3f0a-bbea-94bc9f7293d2 | -12.14799 | -47.13602 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 34daebe5-a038-3d3e-a52c-5d4214c2abd9 | -10.40681 | -50.0069 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51aed227-d910-331f-bd66-d9bf343172b3 | -9.01476 | -65.45638 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c13d588a-5c89-30d6-a460-286d7cc8ba83 | -11.05175 | -51.52638 | 2026-09-02 05:18:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 760090bf-c6d4-398f-98d4-9020f3588d10 | -8.56438 | -63.19159 | 2026-09-02 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 973638ce-a20a-3987-86bf-2bd822d5f4ed | -10.88079 | -45.34467 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd13912f-f25a-3f65-9efe-a87b87321cc5 | -12.13485 | -47.1394 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README59.md)
