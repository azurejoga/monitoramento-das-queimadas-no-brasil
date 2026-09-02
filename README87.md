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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 981b8fd6-c4fb-31d6-ae2b-414faf964e59 | -14.5631 | -52.0557 | 2026-09-02 15:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 9ce28ba9-ba9f-31ca-88f1-b18aecbf9e35 | -14.9655 | -54.5688 | 2026-09-02 15:50:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 45059971-4110-3fe9-b210-bfe9621d72ef | -13.4325 | -57.061 | 2026-09-02 16:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 1e2a7a44-197c-3e7b-b4c8-e9acf27dcc3f | -8.3718 | -62.697 | 2026-09-02 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 31185d2f-4189-3859-b3bc-2f5588c74b2e | -10.1645 | -50.336 | 2026-09-02 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| f357ea31-db59-3e84-af38-f3d623c18943 | -6.9513 | -59.0859 | 2026-09-02 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 7f4543f2-e3d6-3914-8f49-ae91a52990cc | -13.4519 | -57.039 | 2026-09-02 16:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 65443524-be6a-3eb1-9db1-810df0e21bef | -13.9853 | -58.6919 | 2026-09-02 16:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 952d040e-6d1d-3ec3-8359-09d8b2739247 | -3.0347 | -61.4846 | 2026-09-02 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| bd20c4d4-f110-34e8-a7ea-386aec0aa27c | -5.9451 | -57.6906 | 2026-09-02 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 4630ee99-1f24-3a7a-9b9c-0d3d13df1106 | -7.2931 | -60.6287 | 2026-09-02 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 50f382e9-66d2-3d67-b010-e84c96ee3195 | -14.9205 | -52.6241 | 2026-09-02 16:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 9aaf78a0-e262-3975-b8a1-0c8711b90cda | -13.6817 | -51.7872 | 2026-09-02 16:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| ddc3fa88-1dd6-3cf3-a015-ab2ff4b8dd37 | -9.8434 | -64.9777 | 2026-09-02 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 93.1 |
| cba449e2-f35f-3fcd-9ab6-ce81a2bbc9b9 | -6.6006 | -59.1196 | 2026-09-02 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 012411cb-4c60-3dd0-b11e-7979c531e15d | -13.5075 | -51.8728 | 2026-09-02 16:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| a8758c0b-c894-3850-8e39-dbe5fb107d38 | -4.2383 | -62.2349 | 2026-09-02 16:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 7feefb25-df3c-3131-a210-a0d69e749f0b | -11.5283 | -45.4933 | 2026-09-02 16:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 9e66bce7-40fe-36bf-96d5-898ebb078105 | -7.1123 | -42.7727 | 2026-09-02 16:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 51.8 |
| 231bd3a0-6928-3f84-a06d-36e5fe43f61e | -13.681 | -51.8298 | 2026-09-02 16:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 7b3c27ad-1418-3110-9623-2bfe2c5e4a2f | -6.7649 | -59.4216 | 2026-09-02 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 9c3970a9-23bd-3e40-b27a-346747481813 | -13.4137 | -57.0426 | 2026-09-02 16:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 47.6 |
| accbfd99-1fb0-36a5-99e4-4e90d43a4c43 | -13.5533 | -59.7377 | 2026-09-02 16:00:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| ffdeb7e5-853e-33cb-8703-781e2e079ff2 | -7.455 | -61.3853 | 2026-09-02 16:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 84578a3d-6da6-303f-a14b-656e83f52c56 | -8.4089 | -62.6767 | 2026-09-02 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 50d6882b-9e89-3c56-bf2e-747f3e12453d | -3.8446 | -59.3977 | 2026-09-02 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| fe6f4d6c-19c3-3864-a44d-651283547eeb | -7.2192 | -60.6507 | 2026-09-02 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| cf316699-a83a-31b3-bf03-d61c629c7bb2 | -7.4987 | -63.7261 | 2026-09-02 16:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| dbc03018-5072-3ab0-863c-e09bc893db30 | -15.4429 | -52.681 | 2026-09-02 16:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 99dc861b-1f3a-3f84-985a-4aba89f6abbb | -3.7953 | -64.1112 | 2026-09-02 16:00:00 | GOES-19 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| ac1cce7c-038e-3585-b109-9d8d13dbf710 | -2.9447 | -60.9002 | 2026-09-02 16:00:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| b2a92f86-a67e-351e-8a11-de6af593c21e | -1.4761 | -54.2365 | 2026-09-02 16:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 6a0c5b79-efd9-3ab1-8b8a-39cf1d162b22 | -3.4002 | -61.3276 | 2026-09-02 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| e683230a-9931-3315-acf8-ab7f3a81e1f3 | -8.8925 | -62.3538 | 2026-09-02 16:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 195.8 |
| 593d6f03-540a-3c4a-8dcb-9c7e62b9c948 | -13.9664 | -58.6736 | 2026-09-02 16:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 541ff722-7c47-3959-b712-dbfd84e6dc3a | -1.0182 | -53.7189 | 2026-09-02 16:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 86ef30c4-b93f-3b41-94d7-4f73c31c224f | -2.9326 | -58.3397 | 2026-09-02 16:00:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 6e674e26-c28e-347d-a3aa-1bd4798071ef | -1.4752 | -54.8157 | 2026-09-02 16:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| ef525d7b-958e-3767-9450-70eeaed97bed | -6.7692 | -58.6679 | 2026-09-02 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| c113bc48-54fa-3317-8bb3-dc29b718d575 | -7.2745 | -60.6486 | 2026-09-02 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 22d11d23-2379-3d63-9518-d61276e34b42 | -3.8263 | -59.3982 | 2026-09-02 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 0eeff926-eac9-38d6-b83c-c5cfcfee28cb | -6.1844 | -57.7395 | 2026-09-02 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 26c3a429-dbaa-3be2-9759-00ceab967279 | -6.6358 | -59.4267 | 2026-09-02 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 5399be30-1f5b-353b-9b4f-7707777e1239 | -10.3296 | -45.3799 | 2026-09-02 16:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 295b77b0-714e-3b7d-b356-7849b0abb2a4 | -13.9855 | -58.672 | 2026-09-02 16:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 8d37b57d-7d00-3605-906b-ae0a054bb2c2 | -12.01 | -60.5345 | 2026-09-02 16:00:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 7fe30715-95f8-3d83-82e7-6b22d09a9d50 | -6.7463 | -59.4416 | 2026-09-02 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| dfb2aa74-ab5d-3c72-b877-4944b1e99a04 | -10.0105 | -46.4161 | 2026-09-02 16:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| ba7af502-0908-3aab-be69-e548139d87c6 | -3.3688 | -59.3887 | 2026-09-02 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 5e844d56-85e1-3497-9a72-8d52ba7198af | -5.9635 | -57.6899 | 2026-09-02 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 15e9ad49-7476-3c1e-a313-518a839e2772 | -13.6813 | -51.8085 | 2026-09-02 16:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 443e4a80-5cb8-3a80-9445-ced98e82eb18 | -6.1426 | -62.5268 | 2026-09-02 16:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| c2058c40-f859-3b8d-a547-fd913e5ccef0 | -4.2644 | -55.152 | 2026-09-02 16:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| d3a5667d-8e9a-33bc-86b0-4688ca13969e | -14.6538 | -53.5433 | 2026-09-02 16:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| a44c76eb-8c3c-36fb-bf4a-8795ffae5e3d | -13.3936 | -51.802 | 2026-09-02 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 5d95ada6-f4d9-36ae-a57d-01958840943c | -3.7533 | -59.3231 | 2026-09-02 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| c6122e78-1d26-3460-9373-deb616a375be | -7.2932 | -60.6096 | 2026-09-02 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 60e23de2-1cb6-369f-8e79-1cb7a0cca16d | -1.4761 | -54.2365 | 2026-09-02 16:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 51c7c18f-4c59-3db7-ae4b-c39967c3452e | -6.6006 | -59.1196 | 2026-09-02 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| a28e02cb-5a76-37b7-ac97-e7251b55b491 | -3.7533 | -59.3231 | 2026-09-02 16:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 7ef6f7f0-2b8c-311f-9ec7-2d630223ea79 | -7.5141 | -60.7346 | 2026-09-02 16:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 4e2ea8ac-d871-3b3e-b1d1-db678b412a5e | -7.4549 | -61.4044 | 2026-09-02 16:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 1ddbcf8e-ecb7-38e1-95c2-b151a022560e | -7.3487 | -60.5883 | 2026-09-02 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| e2f7cf73-673f-308b-83a6-04639fce7a8b | -14.2989 | -51.7072 | 2026-09-02 16:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| fdda1ddf-5c45-3ee8-9bb7-f1af39e65e15 | -7.2536 | -61.1074 | 2026-09-02 16:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| e79fd305-4816-3f85-9c03-517bce3b7138 | -7.1822 | -60.6713 | 2026-09-02 16:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 6fdb6530-45f2-3d6d-bdd1-677deaf4e89e | -6.1844 | -57.7395 | 2026-09-02 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| e1910a43-eb49-305d-9670-b2bacc3a20d1 | -13.5533 | -59.7377 | 2026-09-02 16:10:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 7eb15e2d-5beb-3803-bcc8-e648d8183a16 | -7.2007 | -60.6515 | 2026-09-02 16:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| cf141173-bbbb-3111-a16a-256868f16532 | -3.3505 | -59.4082 | 2026-09-02 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| f3149e45-d39f-3587-905e-21b2b0c7aa68 | -6.6766 | -58.7299 | 2026-09-02 16:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 6786e0a1-717f-33b4-9c54-32411487a47a | -3.0347 | -61.4846 | 2026-09-02 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 9f39a2c7-9699-3102-b9ec-88380dc6c79a | -12.1457 | -44.196 | 2026-09-02 16:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| f92937ba-f694-38a2-bc7e-2c35742944a0 | -15.4429 | -52.681 | 2026-09-02 16:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| cc48bbf7-7b92-3d66-89b9-774f8cf90935 | -13.5343 | -59.7392 | 2026-09-02 16:10:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 29998d32-10d1-330a-9e9c-6be34278c145 | -8.4296 | -54.7262 | 2026-09-02 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| d7228f5b-836b-3c54-9d41-ba92b0917bfa | -6.8019 | -59.4008 | 2026-09-02 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 07fe972b-f0b9-376f-808e-a5b8acc2f427 | -5.9451 | -57.6906 | 2026-09-02 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 1f68e369-4444-3c22-85c7-8b8386eff51f | -5.6199 | -60.2104 | 2026-09-02 16:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| a0616bea-3284-3dbd-a3ef-a529c5f4ed1e | -3.1997 | -61.1799 | 2026-09-02 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 229fc235-3395-32f8-83b1-3bac2893fee7 | -7.2931 | -60.6287 | 2026-09-02 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 37668592-039d-31a0-98a5-99cce07cca7f | -3.3688 | -59.3887 | 2026-09-02 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 66227a6b-6c09-3424-af93-81aef84fc27d | -7.5139 | -60.7537 | 2026-09-02 16:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 144.8 |
| ed6d7b95-4f7a-3dab-b6a0-330945727d98 | -7.5668 | -61.2096 | 2026-09-02 16:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 8692aaa4-5489-3cca-b997-474070216bd7 | -3.0347 | -61.4657 | 2026-09-02 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 9dfc46fc-2c35-36b4-9b44-f23ccf607dcb | -7.5526 | -60.4651 | 2026-09-02 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 75d5991e-f622-3a16-8a80-7f8fb022c3f0 | -12.01 | -60.5345 | 2026-09-02 16:10:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 573008b6-19dc-36fa-b08b-87c1d7405ddf | -6.8387 | -59.4186 | 2026-09-02 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| e49c82e8-dadc-370d-b6a4-5e1211f618d3 | -7.5293 | -61.3063 | 2026-09-02 16:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| bf4aa047-49de-3843-ab9c-0d3e40394089 | -3.8263 | -59.3982 | 2026-09-02 16:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| e8030549-aa8e-32a4-89ed-2252add1e609 | -6.8203 | -59.4001 | 2026-09-02 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| e1b05244-2082-3b2b-81f1-86da7df2a209 | -3.218 | -61.1607 | 2026-09-02 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 0d8030d2-7883-32a0-8ac1-4b01a8ca1dd6 | -3.8446 | -59.3977 | 2026-09-02 16:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| eed25fe0-9c51-32bb-ba93-5f145f397d57 | -8.3718 | -62.697 | 2026-09-02 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 50036e59-306e-30bd-b41a-5470359fc517 | -9.8434 | -64.9777 | 2026-09-02 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| a2e05e72-807c-3a81-ae9d-f6662c61b9d1 | -3.1998 | -61.161 | 2026-09-02 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| be5b613d-50b0-3be5-922f-6fb78b2ca66a | -1.5116 | -54.9546 | 2026-09-02 16:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 8e6f1ed4-ea62-39f9-93ef-b0c52f58ae18 | -6.1426 | -62.5268 | 2026-09-02 16:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 900cae73-d8ab-31d7-95bb-0c48a068f41a | -2.9447 | -60.9002 | 2026-09-02 16:10:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d9a3aba7-017a-30a9-9f24-5992b2ec7c83 | -1.4752 | -54.8157 | 2026-09-02 16:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |


[Clique aqui para ver as próximas entradas](README88.md)
