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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 192d2f1d-2732-33c8-a81a-e0e361b25062 | -14.74765 | -46.30154 | 2025-07-18 04:27:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b2cce8f-3f01-339b-8c59-69e28cf9a230 | -11.15276 | -49.70172 | 2025-07-18 04:27:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44011527-c755-3791-a592-114fda48c6c2 | -14.20928 | -45.33937 | 2025-07-18 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 117ae760-50cd-3492-ab93-e96d1733a4f6 | -14.73285 | -45.07948 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d4469b4-1594-3e8f-be81-6c4c6a9cf9af | -9.5011 | -47.56322 | 2025-07-18 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| d9f31f80-babd-314d-bc46-7a52d0678b6b | -11.57003 | -47.07495 | 2025-07-18 04:27:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2a5e1986-2255-38d2-9a15-0a44b7967f1f | -11.85419 | -46.75299 | 2025-07-18 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9c77fd4-e9b2-307e-b30d-facae16694eb | -14.51579 | -48.57049 | 2025-07-18 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc47ac88-afd3-3a97-9104-53f54e5fbefb | -14.72504 | -45.10903 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b038ce36-160c-3479-aac6-6fd2d747e716 | -11.88041 | -40.95258 | 2025-07-18 04:27:00 | NOAA-21 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| bafa1488-89cd-3b78-bbf7-254ccaca7360 | -8.88521 | -44.79268 | 2025-07-18 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a446e3cf-1bae-3729-8450-e15c5f105a4a | -8.88924 | -44.78942 | 2025-07-18 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d5ddaabd-7a5d-33f3-9519-7bb3d58e38ea | -8.06164 | -50.07592 | 2025-07-18 04:27:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2f88fe40-c3f4-307b-ac9b-a21ec2942dfe | -14.72609 | -45.06715 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7299b7d3-915f-3bad-b9f0-58cf73950f5a | -9.76051 | -48.75386 | 2025-07-18 04:27:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 221f2740-378f-325f-a5e4-a8fd4c68c207 | -12.48009 | -44.50212 | 2025-07-18 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a98991d-2761-3435-b2f7-73f9438a8e22 | -9.65993 | -49.35339 | 2025-07-18 04:27:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1731d0d-cdc1-3cda-9bdf-8ca548db0f43 | -9.7639 | -48.75438 | 2025-07-18 04:27:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1330cc31-802b-3728-9d32-2bf1d5899d69 | -11.465 | -48.15894 | 2025-07-18 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e10d87d4-0dc3-3f98-9e68-2fb56511003e | -9.24682 | -48.56205 | 2025-07-18 04:27:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95a242df-c403-3fc5-9c5c-595b0dafc741 | -14.71624 | -45.10974 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfcf20a5-a597-3220-9e1b-4eea3f91af94 | -8.06526 | -50.07654 | 2025-07-18 04:27:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 081f9660-0213-3e11-ac5f-69dd9bc22dd6 | -10.71987 | -49.48969 | 2025-07-18 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 960754ee-bfd8-3b0b-937a-0122c93994be | -11.74187 | -48.19351 | 2025-07-18 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| af9e210f-6aac-33d3-a8c2-cffd89a0e75a | -12.56725 | -44.7514 | 2025-07-18 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fb53b58-9562-3a25-bf27-e4c2b8e27d76 | -8.87931 | -50.15174 | 2025-07-18 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 76f189dd-dc86-30b0-969e-c1e72495dd6c | -14.70802 | -46.18867 | 2025-07-18 04:27:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d985e723-1f87-307a-9979-4ac59f75b7b3 | -14.72547 | -45.07148 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba23b05b-40eb-3825-9182-5d1e4eade229 | -10.93711 | -48.88619 | 2025-07-18 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 307eb91d-44fd-3bdf-87d5-d5d94dca53bb | -14.72184 | -45.07097 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2bc24cf-b1cd-37f0-8f52-b8295529b493 | -14.75921 | -48.27602 | 2025-07-18 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e1651a7-1c47-3300-9c85-e0af4e46a5a2 | -11.56671 | -47.07442 | 2025-07-18 04:27:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5b0d3977-05b2-38bd-b886-b89fccad1072 | -12.3758 | -50.34568 | 2025-07-18 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cabda17e-85fc-3291-8c6d-acf122ee3537 | -8.04029 | -46.61731 | 2025-07-18 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e23268b5-af9c-3a14-b696-b9e9a9d3402e | -14.72142 | -45.1085 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 854c7e00-bf16-3c71-9319-9ebacda5132c | -14.72443 | -45.11334 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0a2064e-c577-3674-809a-3c9651968afa | -11.57447 | -47.09011 | 2025-07-18 04:27:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f1f5451d-1a6c-346f-adc9-c37c5e6e2276 | -11.57393 | -47.09363 | 2025-07-18 04:27:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3a2136b-90aa-32c2-9275-10122bbebec9 | -10.06882 | -46.67088 | 2025-07-18 04:27:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 926c267e-b5dc-38b6-9932-f815cb9076c0 | -14.17316 | -44.7035 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b823225-6939-3148-b73b-129d3cc9ed1c | -15.63929 | -41.25336 | 2025-07-18 04:27:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 797ef842-5268-3cac-9adb-4460f841d993 | -11.36423 | -48.70395 | 2025-07-18 04:27:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 965546da-f5c2-3d6d-b771-cc8e36233fc4 | -13.02719 | -46.79056 | 2025-07-18 04:27:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65e4d299-2ed0-34ae-b473-20da8d6cc353 | -11.56067 | -47.09152 | 2025-07-18 04:27:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 23dbc085-cba9-3b7f-93e9-8a648ab388e5 | -14.72122 | -45.07529 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef78ff7e-422a-3a47-88fe-97c5536a4718 | -11.16276 | -46.25315 | 2025-07-18 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba24c455-8425-3d74-9b41-f33314406729 | -11.7825 | -45.22637 | 2025-07-18 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33dcc095-9b71-3a96-8275-702ada69359a | -11.99448 | -45.30941 | 2025-07-18 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 31dc668e-ea5f-33dd-80c0-97387af86a01 | -10.09202 | -47.24345 | 2025-07-18 04:27:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0665fb43-caaa-3c94-bf54-6c66fab49359 | -11.73967 | -48.18592 | 2025-07-18 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 78e50d20-01c9-374d-b441-0474b1acf8a1 | -9.58808 | -40.35555 | 2025-07-18 04:27:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 92a7167b-9fb5-3311-8839-e52c11cbb21e | -14.20158 | -45.34244 | 2025-07-18 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32306433-8232-3f2c-9a47-8c092c08c9e3 | -12.36946 | -50.34052 | 2025-07-18 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0a1b967-9a8a-3ea5-820f-36d0d0ae2816 | -11.46113 | -48.16192 | 2025-07-18 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c120e69c-0d38-3b5a-ae80-a79ce9b0dc89 | -11.74132 | -48.19703 | 2025-07-18 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 0e4233a1-3090-3368-ba6a-dda4abdaca38 | -9.39252 | -48.39731 | 2025-07-18 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 2f5b4a98-3f37-30bd-836f-ade7a4c72437 | -14.71923 | -45.11455 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc976c95-d18f-37e7-b2ef-85ac206f120a | -13.70712 | -49.39681 | 2025-07-18 04:27:00 | NOAA-21 | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fafb2c8d-f030-3d01-b77b-cd0d87c3df75 | -8.88579 | -44.78889 | 2025-07-18 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| be9dab47-ed02-3284-8017-00b7f91de861 | -9.77006 | -48.75914 | 2025-07-18 04:27:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dc8d88c6-3c3d-3068-9dcc-c7aaba51a212 | -9.86109 | -44.70867 | 2025-07-18 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6778c945-ef36-3a1f-88c3-e94e5492bdb0 | -15.15685 | -46.18337 | 2025-07-18 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b92f8f0-f02f-3429-b583-f6877e4b4742 | -9.38859 | -48.40034 | 2025-07-18 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 8e6fb397-b5a8-372b-8ade-55877f5b2e2a | -9.26712 | -47.90255 | 2025-07-18 04:27:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63cced38-831a-3a03-be4e-e35af4630f00 | -15.15973 | -46.18785 | 2025-07-18 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b4fccbb-66d8-3809-b119-a9612faaa11a | -11.85806 | -46.74998 | 2025-07-18 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66d5349a-30f7-3319-81f4-dfb4b7aad73d | -8.06614 | -50.09404 | 2025-07-18 04:27:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 378cfd4e-2536-3257-8b2a-97604df3ad99 | -13.12559 | -47.25725 | 2025-07-18 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c72aae44-80d0-36c7-a626-b244beda700f | -14.7172 | -45.11234 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54383d2b-6b8a-3bfa-95f2-8564fa3b5f61 | -14.72082 | -45.11282 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf593efd-6a73-34ff-a3c0-c21c9d42d7cb | -15.04114 | -41.409 | 2025-07-18 04:27:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4572a40f-58d1-3283-b2eb-0192600394ff | -10.06551 | -46.67035 | 2025-07-18 04:27:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02e7d4d1-c3fe-3546-a97f-0d1d5faf73b0 | -14.7126 | -46.18149 | 2025-07-18 04:27:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e99633ac-3252-3377-87db-8ff80cf282b8 | -10.71705 | -49.48534 | 2025-07-18 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ac747973-0f18-3e76-84d3-ca96d8c80e8a | -14.72319 | -45.06919 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b1e0f5a-f757-3704-a1e3-f41c06b27110 | -9.80732 | -47.73459 | 2025-07-18 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e185ab5-1126-3942-9681-350376d440d9 | -9.50496 | -47.56026 | 2025-07-18 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6f9106ed-07f0-3b4e-bc8c-2a140f812716 | -12.6645 | -47.09654 | 2025-07-18 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ea39ae34-bb73-3592-8b71-e0a0f516a350 | -10.37617 | -49.89873 | 2025-07-18 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 291ebc87-bdd9-3064-8216-065990ff1665 | -11.57061 | -47.0931 | 2025-07-18 04:27:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 49002343-5921-35b2-9cc5-7389d2509880 | -12.47646 | -44.50157 | 2025-07-18 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf6e296e-093c-3a65-84c4-e278f7804100 | -12.03173 | -48.76598 | 2025-07-18 04:27:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9190c386-059e-374c-b17d-fab7393dbfd3 | -14.72048 | -45.10592 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b7b0d43-7eba-3460-bd92-2d37157a9d0a | -10.83987 | -48.34695 | 2025-07-18 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e19a202a-2ad5-3137-b105-14ff879206d9 | -14.72247 | -45.06661 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce5a19d1-cea6-3ccd-b5d2-3c1de7557676 | -14.71986 | -45.11022 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0278f51-1421-3b26-bbb9-6bd39dcce449 | -14.7416 | -48.25856 | 2025-07-18 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76d34736-0afd-36ee-a31d-37be9ea47315 | -14.70859 | -46.1848 | 2025-07-18 04:27:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fe134b6-687b-380c-9c22-a0adca1d00cf | -12.66118 | -47.09601 | 2025-07-18 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| abe6765d-45f9-399a-847b-502b28ce4ef1 | -9.24008 | -48.56096 | 2025-07-18 04:27:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7c6c076-b92a-38f2-93bf-f7fe1e76ced5 | -12.70506 | -46.80982 | 2025-07-18 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1c9bbfd-0b76-3a63-863e-91b8e383b02b | -14.20572 | -45.33886 | 2025-07-18 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5146b230-9e1e-3c08-ace3-43b95fe998d8 | -11.72004 | -47.77195 | 2025-07-18 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14db5138-d003-3a39-b9a9-feec8f3f4523 | -14.72259 | -45.07354 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1daa71a-86a5-33d5-bf7b-df9078b6ef8b | -9.50165 | -47.55973 | 2025-07-18 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 95e25814-6744-3756-8f54-d433648fc7cb | -14.7184 | -45.10369 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 29d2dbd8-4682-3a69-b9ff-0439fa1a6ea4 | -14.74215 | -48.255 | 2025-07-18 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5062ac8e-eff0-37b0-ace2-49cf04aa681e | -11.5673 | -47.09258 | 2025-07-18 04:27:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a23d30bf-2ae9-3e37-a695-48ee1c730a1a | -10.90249 | -49.20832 | 2025-07-18 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 878fa758-fff3-3fd3-85cc-8df3fb0b155b | -9.80401 | -47.73406 | 2025-07-18 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README16.md)
