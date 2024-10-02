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

## Dados Diários - Página 168

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8843d11-c71c-3b74-bf60-b27519ad09b2 | -9.19126 | -58.20327 | 2024-10-02 05:33:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4872612-fb51-3e3b-8f9d-f66df3996553 | -10.72119 | -58.51884 | 2024-10-02 05:33:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d208de8-ff27-3d4f-abff-e1d562c8632b | -10.72061 | -58.52296 | 2024-10-02 05:33:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5c8e153-723c-3484-9f26-f6ad1034ddfc | -10.72005 | -58.52706 | 2024-10-02 05:33:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cc364e9-0ec9-3c64-8f58-e7b741f535de | -10.71688 | -58.51819 | 2024-10-02 05:33:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05b290ee-feda-31dc-aa4f-5f3d5880d611 | -10.71631 | -58.52234 | 2024-10-02 05:33:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b248c3a-7a77-3cba-b1ab-951d667a3036 | -10.71574 | -58.52644 | 2024-10-02 05:33:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea3cc550-680a-34cb-9e24-def0e175bf18 | -10.71517 | -58.53055 | 2024-10-02 05:33:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3539c0db-bd87-369b-a851-98a2ac737860 | -10.71087 | -58.52991 | 2024-10-02 05:33:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca957eb2-cb46-3be6-9c9e-262f7df1cba4 | -10.33605 | -58.47379 | 2024-10-02 05:33:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e2386b2-ed8b-3a35-b2f6-c258d2adf24c | -10.33424 | -58.47224 | 2024-10-02 05:33:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d220745b-bd81-39a1-b6ea-54599ae3ce8a | -9.96763 | -59.60573 | 2024-10-02 05:33:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17cbae80-7670-39cb-8701-650ea3f983b3 | -9.96526 | -59.60462 | 2024-10-02 05:33:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f948b35-921a-38f0-b94d-b5348a257ed2 | -9.96364 | -59.60526 | 2024-10-02 05:33:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7af32a3-4b82-3c00-8dba-6faa1f2bf12e | -9.71428 | -58.44192 | 2024-10-02 05:33:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55ac4770-7fa4-3567-975f-fee36feb6c5f | -9.70946 | -58.44534 | 2024-10-02 05:33:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fb646c6-8c3b-364d-9f24-da0cdcd13e43 | -9.56857 | -59.10604 | 2024-10-02 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5729e9f-72c8-3261-b02e-38c0306397cc | -9.56449 | -59.10545 | 2024-10-02 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| afc1c936-4cac-366e-9c25-760422430453 | -6.98297 | -59.93876 | 2024-10-02 05:33:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 971a40ae-40e2-37e2-9823-2b6b9404ff2e | -6.95695 | -60.14346 | 2024-10-02 05:33:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4e80491-5a80-39ef-a42d-cd122a1f7ef1 | -6.95109 | -60.13963 | 2024-10-02 05:33:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 132dbcc4-c8ca-3ad0-bc62-f57287fd727a | -6.71549 | -59.12765 | 2024-10-02 05:33:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7e984b9f-d39a-34bc-82a7-be56c10168d3 | -6.71476 | -59.1326 | 2024-10-02 05:33:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 687e76d7-4f24-3e57-a789-d296842309bf | -6.71157 | -59.1271 | 2024-10-02 05:33:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a447f610-2061-3718-8484-f3b19f7825a9 | -6.71085 | -59.13206 | 2024-10-02 05:33:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2d523eec-8429-3a26-87d5-74f59752e701 | -10.20736 | -61.27213 | 2024-10-02 05:33:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd14bd87-dd5d-3c77-a244-52d20bc7bec0 | -10.19458 | -61.30882 | 2024-10-02 05:33:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edd95d28-cf10-3627-b06a-6859f347e312 | -10.19397 | -61.31296 | 2024-10-02 05:33:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d2d8e3c-2951-39b1-a115-63fe292eb434 | -10.19098 | -61.30822 | 2024-10-02 05:33:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43e2088f-0d55-3831-9a0b-d81c26656826 | -10.19037 | -61.31239 | 2024-10-02 05:33:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe3ee67a-78df-3824-8d8d-7c86660eeac5 | -10.17717 | -61.30178 | 2024-10-02 05:33:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 067b12f5-c642-3b90-abb8-8335d2511111 | -9.84877 | -60.73893 | 2024-10-02 05:33:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3b5c37b-ff40-3cc5-8b3f-68342fd2bf5d | -9.84812 | -60.74338 | 2024-10-02 05:33:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68b14a4e-dfd3-3750-ae55-1b4f0667efd7 | -9.84747 | -60.74781 | 2024-10-02 05:33:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2af5f13-9647-3a4a-bc1e-405128ea88a0 | -9.84442 | -60.74282 | 2024-10-02 05:33:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2d4b300-5887-3f04-be1e-7a101f2ad115 | -9.84295 | -60.77874 | 2024-10-02 05:33:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35083aeb-a23a-37e2-9cc9-1f6acd54f036 | -9.39653 | -61.04599 | 2024-10-02 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd3c9a2e-3d6c-3417-ba5d-3682ef29ad0a | -9.39589 | -61.05022 | 2024-10-02 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4bea4f92-5f83-3a5b-99d2-044e5a878f5d | -9.3929 | -61.04544 | 2024-10-02 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0fd23993-2bc3-3162-84d8-7d82e35705d7 | -9.39227 | -61.04967 | 2024-10-02 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1187a09b-8121-312a-a647-4cec9dcc31a0 | -9.93011 | -59.9302 | 2024-10-02 05:33:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8e11d392-73b6-37ba-93cc-5d8eafa96a12 | -9.92581 | -59.90437 | 2024-10-02 05:33:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 494db69b-8656-372b-9b8f-5f4ed8ac7e39 | -3.18799 | -60.54897 | 2024-10-02 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e8e08d4-e2d6-3ff8-a6b6-5774bf072389 | -7.92779 | -61.55778 | 2024-10-02 05:33:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cc37a390-0cbc-300c-8c71-7a6b8bc779d5 | -7.9243 | -61.55724 | 2024-10-02 05:33:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 32c01fb7-d57c-37bd-8670-70745d201426 | -7.92097 | -61.27178 | 2024-10-02 05:33:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8657f8c5-b374-304e-b0c2-533c137f0671 | -7.91852 | -61.54842 | 2024-10-02 05:33:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4d5d3aba-b16e-3ffe-89e0-d8c249a33103 | -8.57987 | -62.42339 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b837daf-ac88-3d25-bbbf-f1f0b313fb9e | -8.57647 | -62.42288 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c921954b-68f8-3ceb-bd2e-a3e6116a9f56 | -8.56081 | -62.48052 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 778d2145-a1ea-3371-bbef-67ed453171a9 | -8.55742 | -62.48 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 642a0eb8-8c6c-30c8-baea-99fdab2d6520 | -8.06854 | -62.37635 | 2024-10-02 05:33:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9400e6d4-0945-38e2-ac4f-d66e5d444599 | -8.58326 | -62.4239 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02316e3e-a186-3386-a5a5-382692f5c01b | -8.56026 | -62.48418 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37596f0d-a13a-3d41-86eb-285f35a15267 | -8.55687 | -62.48366 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86ae8c1b-12d5-3ad5-86b6-5dd3f294f1ca | -8.55633 | -62.47988 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 005fab3d-0889-36ea-9546-dac5f2777348 | -8.55576 | -62.48354 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b049092-ac37-3a1e-b381-07e0374e4770 | -9.28002 | -62.16578 | 2024-10-02 05:33:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efb4b874-9386-3f5f-9dc1-0571a13e3d68 | -9.27945 | -62.16956 | 2024-10-02 05:33:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34818c96-464d-33ba-967d-30b3e2614c9e | -9.14378 | -61.26234 | 2024-10-02 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20653e80-5348-3ea0-8cfa-28b0fb67bbd2 | -9.13668 | -62.42014 | 2024-10-02 05:33:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 671b0379-8d80-3a26-b72e-28cffd934782 | -9.09276 | -61.13651 | 2024-10-02 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da71e579-006e-3f18-9756-d9134a464cfd | -9.08917 | -61.13595 | 2024-10-02 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13298a98-d950-3d61-9f8c-76fb63cb1a05 | -9.08064 | -62.35118 | 2024-10-02 05:33:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fa1c47b-4eb1-34b4-9542-a68aaabb24b4 | -9.05501 | -62.3358 | 2024-10-02 05:33:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6a3eb2a-50ff-37f4-8ff3-17127b02b005 | -9.17865 | -61.89289 | 2024-10-02 05:33:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c5f51bf-52d2-3f90-b76b-1c3855ea479a | -9.17806 | -61.89676 | 2024-10-02 05:33:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fdab0f2-f10f-3819-adcf-a3908df4f7cd | -9.08007 | -62.35491 | 2024-10-02 05:33:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e098f56-bdf1-3ed4-a6d3-16058332c746 | -8.95169 | -62.39293 | 2024-10-02 05:33:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97c881c8-af0a-3f56-8c86-5b2ed363ca3d | -9.96552 | -62.53994 | 2024-10-02 05:33:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 60a54f68-225e-3fc8-a5e4-576af6d42415 | -9.54443 | -62.43137 | 2024-10-02 05:33:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0811e77-98fc-3f23-a75d-8e3d987c2667 | -9.51296 | -62.45439 | 2024-10-02 05:33:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c0b15f7-04ec-3840-b278-619063d34d74 | -3.30822 | -61.64548 | 2024-10-02 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1bc8b3b5-6032-3742-885f-f4cc68f37f1b | -3.03224 | -61.6758 | 2024-10-02 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7efdf42a-d10a-3abb-a531-a516844da17d | -3.02945 | -61.67176 | 2024-10-02 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34b6e2b7-8f2c-3aff-ba58-e190023b2150 | -3.02222 | -61.69595 | 2024-10-02 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f6088d1-e180-3346-b24f-9da8adfc06a1 | -2.98765 | -61.38835 | 2024-10-02 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 840cb926-80f1-3489-9902-f2ad9352f8e0 | -2.88643 | -61.89083 | 2024-10-02 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0e7c67d-b953-3cb7-b733-f9fcb4701483 | -2.88529 | -61.87633 | 2024-10-02 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d7d4a970-2e95-34b1-b5a5-3e10e755e8ff | -2.88474 | -61.87983 | 2024-10-02 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 08deaa7a-a782-3d90-9bee-a3a2b4639c5e | -2.88196 | -61.87581 | 2024-10-02 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9f27ed0e-8ddb-3638-bc39-a151c7ecc606 | -2.88141 | -61.87931 | 2024-10-02 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 908801af-aa8e-3af6-9a70-1daa6cfc38e3 | -2.88086 | -61.8828 | 2024-10-02 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b733d01f-ac08-3a0c-9ec0-1c18932e0463 | -3.03169 | -61.67933 | 2024-10-02 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fceca991-b564-32d6-915a-7d5cda113d01 | -3.01887 | -61.69544 | 2024-10-02 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b1b6e51-cbe4-3822-9cbd-1ddcd5d3b8cd | -2.98884 | -61.42522 | 2024-10-02 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a4e4b54-70dd-36ff-8ca8-0240050efd59 | -2.98829 | -61.4288 | 2024-10-02 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca1f5e5e-6e8c-3bf1-a51c-8a223bb42b49 | -2.90841 | -61.83323 | 2024-10-02 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90e2972f-f20c-3967-8644-8f3fb94568dc | -2.88862 | -61.87684 | 2024-10-02 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bb7a2d3-7d80-3575-bb5e-57439ad7315b | -2.88807 | -61.88034 | 2024-10-02 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fece73a-92d8-373f-9667-eaa0b9774047 | -2.88752 | -61.88383 | 2024-10-02 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bfe49c3a-9b2d-35fb-bf4b-d6f7f4fc170b | -2.88697 | -61.88733 | 2024-10-02 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4ed1c98-9bfd-33a3-9ec4-407202578864 | -6.85333 | -62.90969 | 2024-10-02 05:33:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7850c6dc-d1cc-34a9-be76-9f599abdc9ab | -6.85278 | -62.91319 | 2024-10-02 05:33:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33d8af96-d31b-32bb-8bbb-de7b4950e2eb | -8.7749 | -62.83999 | 2024-10-02 05:33:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f584f663-fb4b-3359-9b17-290ce96df59c | -8.49222 | -62.62642 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c47c43a-35a0-3bed-9c62-e47a5ef13512 | -8.49122 | -62.70026 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30d57b98-82b4-3d2f-be6b-681e4cf46fd6 | -8.49066 | -62.70387 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb38f2fe-4005-341b-a37f-e3f65af41c66 | -8.48001 | -62.70591 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf47dba0-1992-3930-b9cf-1f58ca65c22a | -8.47945 | -62.70952 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README169.md)
