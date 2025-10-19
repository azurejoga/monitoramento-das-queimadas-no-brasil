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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec3bdeef-05d2-3b31-8e77-f1c5095cc388 | -2.97786 | -50.30164 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07e8b8b3-aba5-3cd7-b7d7-6feadd69b992 | -10.01073 | -64.01798 | 2025-10-19 05:23:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9c7dc44-b757-37a5-bf86-7aed24357fa1 | -5.64171 | -46.5869 | 2025-10-19 05:23:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e92e7c3-8d08-3b7b-96ba-237c2147e657 | -2.98002 | -50.29746 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d20d3e28-8ee3-318d-b302-c7140f3a5540 | -9.91302 | -64.08409 | 2025-10-19 05:23:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7314136-55d0-37af-806d-c15a407bc499 | -3.16043 | -49.1658 | 2025-10-19 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 968f56dc-113b-3a09-9d0c-d54b1322619e | -2.87661 | -50.722 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 569c0565-3cde-30c0-b68a-87b088dc6f3a | -5.08027 | -60.2207 | 2025-10-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79398fe3-12fa-3772-ae6a-1ef0617aace2 | -6.66675 | -58.73861 | 2025-10-19 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd3dd2c5-ef68-3ae3-a4c0-63fad0fdecc2 | -9.71158 | -64.97153 | 2025-10-19 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 913c17a0-45d6-341e-9bc4-99494c364720 | -2.8771 | -50.71875 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 05062066-84ca-3c0b-aaf4-1e955f681a79 | -4.15995 | -51.09091 | 2025-10-19 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1db2ea53-559f-3a61-a0ad-9fed5db18c84 | -2.69932 | -49.55006 | 2025-10-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 55f4d80c-366e-3357-905c-fa01d9ea8d1c | -2.81161 | -58.29037 | 2025-10-19 05:23:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0260909-9c0b-3c0e-a893-c9c333e03d97 | -9.42359 | -63.49801 | 2025-10-19 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e6c31f75-bbda-324d-b203-848679ea5d07 | -2.74037 | -49.39002 | 2025-10-19 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85b1ae24-3744-3234-bb94-e5385e92481c | -2.68551 | -49.54984 | 2025-10-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| da9c0dcd-b5a2-3469-bcfb-cf54c561912a | -9.55237 | -66.73449 | 2025-10-19 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b48582f-c7df-33c5-aa72-ab784fdeaa1e | -3.52497 | -58.35893 | 2025-10-19 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3edda905-3ae5-32fb-aedc-83bdad8124f8 | -3.40113 | -54.06065 | 2025-10-19 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86f5e147-1389-3088-8fc1-db850ce8582d | -2.86365 | -50.73668 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e6e647b-8122-30b8-936f-1f619540a7d7 | -9.95584 | -66.77029 | 2025-10-19 05:23:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd0dddb1-3b06-30cf-893b-5d79388c7257 | -1.93251 | -56.82487 | 2025-10-19 05:23:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3a7a5cd-2a33-3ee1-8b29-93bd5e672ac1 | -9.90881 | -63.58017 | 2025-10-19 05:23:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bc0f92d-a345-32d0-94bb-b0a96229fbd8 | -4.10238 | -48.83907 | 2025-10-19 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f1fcf077-0382-3df7-9df9-89adf116d28e | -4.16465 | -51.09537 | 2025-10-19 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca38e52d-be47-3c3f-bdc6-0c9d89aab3e7 | -9.85023 | -68.11137 | 2025-10-19 05:23:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4326c743-3b27-3cc7-9a85-a756af8ffd21 | -3.82219 | -51.7066 | 2025-10-19 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3774c04-a7f8-3585-866e-2fd9846a4374 | -2.25366 | -51.90704 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e7d39441-ae6a-3fef-b87a-cc500a4a2f64 | -6.00924 | -62.48622 | 2025-10-19 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 561a7c31-d2a7-3ffd-9003-4fd094602309 | -11.64279 | -44.08101 | 2025-10-19 05:23:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f7f322ee-ccb5-3fa6-bc38-e83cf3c32ce9 | -3.15951 | -49.16308 | 2025-10-19 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36e6263b-0b93-3322-a366-1f798c4ad41a | -4.76031 | -50.69773 | 2025-10-19 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ab05cc0-1a8e-3e35-9fb5-e998bb3db650 | -5.07697 | -60.22019 | 2025-10-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84a1d048-f932-3578-84a2-b8e5d1dab8d3 | -2.97952 | -50.30093 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd56591f-a450-3364-8df4-4c0fb3d5222b | -3.81566 | -51.3236 | 2025-10-19 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34db59ac-ed4d-3ce3-9c2d-f21882c28102 | -12.14784 | -45.05202 | 2025-10-19 05:23:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 86ca16c0-c6c9-349e-81a8-1f0e6b2e575b | -3.81803 | -51.70005 | 2025-10-19 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a885c6d0-1624-3d4a-a0c1-3687c9e11f91 | -3.09244 | -49.22007 | 2025-10-19 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3fb20180-dff4-3091-8f76-9f51a2698213 | -7.41222 | -40.07487 | 2025-10-19 05:23:00 | AQUA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 7.4 |
| d5d1528e-bbff-365d-9e8c-e0ae46d95610 | -11.90204 | -62.5232 | 2025-10-19 05:23:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f624f25a-812d-3ef8-9c9d-403bd0578797 | -2.87134 | -50.72118 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c4c11efb-3e01-325f-b334-137028a75e23 | -2.81273 | -54.38428 | 2025-10-19 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1725f3c3-ae4a-3256-bae6-e472fc27dde6 | -10.01549 | -66.78479 | 2025-10-19 05:23:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d96cc72-9ed4-30b8-9a28-a1d90e70ecb9 | -10.15391 | -42.20652 | 2025-10-19 05:23:00 | AQUA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 36795cd7-5b71-30e6-864f-a6c8283e9d7e | -2.87565 | -50.7285 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89edd533-63f6-34ca-b6fa-fa3d3868e287 | -9.10001 | -65.37368 | 2025-10-19 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c513761-67d3-3ca8-8611-eeaa7847786d | -8.61634 | -40.18699 | 2025-10-19 05:23:00 | AQUA_M-M | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 308877bf-8092-3b7b-9385-1eb5453ac69e | -3.80283 | -51.93947 | 2025-10-19 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 425e38ce-fec8-3d8e-bcc1-506c9b731a27 | -3.03316 | -61.43183 | 2025-10-19 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c87b315-20a8-3d8e-9cdf-eed3dfb54aad | -3.64243 | -49.97017 | 2025-10-19 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1f24a10-6876-3e43-a32f-9534b556d05b | -9.91655 | -64.08468 | 2025-10-19 05:23:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ef91fb3-3ca3-3d85-bd94-69cee9b4f7fb | -3.39627 | -54.06643 | 2025-10-19 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae79f16e-5584-3074-9569-8ed9db1466c0 | -9.7996 | -60.14548 | 2025-10-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b8dee5b-c476-33e6-91d4-0fa33c85b2c9 | -2.15739 | -51.95974 | 2025-10-19 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27140620-4c62-3c12-8979-082e25e23a9e | -5.23754 | -50.95364 | 2025-10-19 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42a41eff-35e7-3c84-9a18-aaa62e36743d | -5.10573 | -47.79464 | 2025-10-19 05:23:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| aed69b04-32a9-36d1-a9a3-5d98e26f0fc7 | -9.91941 | -64.08928 | 2025-10-19 05:23:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1050a4a7-cd23-3608-9c3c-3bac8ba5f524 | -10.88416 | -46.08592 | 2025-10-19 05:23:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 56c89128-c9bd-3ab1-b545-5daaf91326c9 | -4.41622 | -49.7605 | 2025-10-19 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18b0356b-bfd1-3724-8056-63190d554829 | -4.97223 | -56.27323 | 2025-10-19 05:23:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 044180da-6110-3acb-bcc2-44a2ecee07d4 | -4.15964 | -51.09367 | 2025-10-19 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6f914a3-c481-398d-b73d-99074bc0b335 | -11.61037 | -44.05815 | 2025-10-19 05:23:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9e731385-cf8d-33d9-b80b-bb1ecf04c951 | -3.1499 | -50.25037 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13d81479-193d-3c1d-8332-b406f2bafa6f | -4.76217 | -50.69801 | 2025-10-19 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9acd5549-fd4b-3485-b50b-605d926e7c2d | -11.26604 | -60.89152 | 2025-10-19 05:23:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d6c9162-5936-319d-8d20-d22fa4da8c10 | -2.88189 | -50.72281 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acffaa9f-8e5f-3341-85c8-4b729e0d5455 | -12.14457 | -45.07113 | 2025-10-19 05:23:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 34a4706f-b08b-3ffc-aaaf-7f35f42fbef2 | -9.65823 | -62.07644 | 2025-10-19 05:23:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa5faaa7-3062-3977-9c19-8b12c1fcbcba | -2.98328 | -50.3026 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd9481cf-e88a-3f84-bd6a-09a8a3a1c743 | -6.50291 | -54.88864 | 2025-10-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e410156b-c4cb-3a1f-9085-d4786681d9f6 | -4.76082 | -50.69424 | 2025-10-19 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 17a5d08f-f027-366b-80ba-820ed8d98adc | -2.44066 | -49.36467 | 2025-10-19 05:23:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7874fd82-3931-39cb-9b9f-87112023ae5a | -9.53474 | -62.96 | 2025-10-19 05:23:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7d3c6e9-2e14-3a1f-b5dc-2f860377c77a | -9.89822 | -64.17277 | 2025-10-19 05:23:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 19f59470-8db8-3af3-99fe-aab87da03aa6 | -9.85104 | -68.10677 | 2025-10-19 05:23:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 490c6c9f-f392-3bd3-bb94-2fd80a8a7b4e | -8.56581 | -48.51701 | 2025-10-19 05:23:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 70cd0edb-1acc-3e03-a2cb-733924d6fb49 | -9.22855 | -63.6098 | 2025-10-19 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10f8d935-8784-3ffc-84b1-00a12e432e94 | -4.22356 | -50.62443 | 2025-10-19 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 955ca7bf-22bd-39aa-b7e1-6f815375495c | -9.20412 | -67.89348 | 2025-10-19 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d5af8e5-03f5-3f0f-ae24-931a364a5647 | -9.60773 | -61.83801 | 2025-10-19 05:23:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4124097a-8ea6-3897-b3b1-acd8c3ce0613 | -6.53131 | -60.03643 | 2025-10-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00a721fb-db53-30b0-9d54-8a97114db5b5 | -2.81387 | -54.38156 | 2025-10-19 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16f588a5-ebea-3325-bcab-a6d1ab636bf2 | -3.55235 | -46.4373 | 2025-10-19 05:23:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 61a171c3-d0ea-3f8f-a1f6-a11ac0049146 | -9.72169 | -65.87434 | 2025-10-19 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 313c2a6d-2125-3edc-8723-27f9ef799fc3 | -1.65815 | -54.4127 | 2025-10-19 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75bac4df-1e27-3853-8c5b-5d51fcc4eae1 | -11.19838 | -61.52675 | 2025-10-19 05:23:00 | NOAA-21 | MINISTRO ANDREAZZA | RONDÔNIA | Brasil | 1101203 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a11294a-2fd4-3619-ba01-91e519618056 | -4.30505 | -48.0669 | 2025-10-19 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6cf3e151-5c4a-32c1-b71c-add6f68a26f2 | -3.03654 | -61.43236 | 2025-10-19 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6d02e12a-1dbc-36ab-b344-499e07009ad1 | -9.698 | -66.39325 | 2025-10-19 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6a8aebb-64d8-3fc4-95e9-48fb35a15be5 | -2.86892 | -50.73753 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc843f7d-1702-3fa7-a11e-d4cdd002c443 | -4.96779 | -56.27722 | 2025-10-19 05:23:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f47b9469-676b-3892-a163-aae029e79c0a | -8.56749 | -48.51487 | 2025-10-19 05:23:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a9e6a9ed-780a-3d4f-9804-3824e6936edd | -4.97291 | -56.26871 | 2025-10-19 05:23:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6d4c63e8-f694-3037-a12e-17044f3ca36e | -2.43016 | -57.69533 | 2025-10-19 05:23:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7573a007-d0ef-3b45-bbb8-d8cdde6d9a78 | -9.72528 | -61.9329 | 2025-10-19 05:23:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 549b48c5-6894-3af0-9e3c-ef1f3e6efdb6 | -9.22405 | -46.07003 | 2025-10-19 05:23:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| a25dc9ff-cf6e-3b34-8bbe-3dcea001c0f1 | -9.64431 | -65.25855 | 2025-10-19 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3f7e450a-19d7-3a9d-a907-d8389e77be37 | -2.12177 | -56.60844 | 2025-10-19 05:23:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfa23151-d6ff-38a4-8776-10a7636d4f85 | -9.11687 | -65.36674 | 2025-10-19 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |


[Clique aqui para ver as próximas entradas](README56.md)
