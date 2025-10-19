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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57ffb636-43b2-3685-9aab-d3e4d272bb89 | -9.22608 | -61.83213 | 2025-10-19 05:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| baf5cf6a-61ac-3071-844a-26f08ed1dbd8 | -6.64486 | -62.91071 | 2025-10-19 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f45077a-28d2-341d-af80-dedf05691341 | -6.6779 | -58.74762 | 2025-10-19 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 450b80a6-c7f6-3128-b982-8c9782c9376c | -9.22749 | -63.61052 | 2025-10-19 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a43a94f2-9759-3826-8e2f-54b1f3512ccd | -6.52946 | -60.03319 | 2025-10-19 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffb9c21d-be3f-3fa0-ab5c-1fa3e1d955dc | -7.62505 | -60.95192 | 2025-10-19 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba58cdf5-0040-3ec1-8901-1f2c131c9d8b | -7.6211 | -60.91645 | 2025-10-19 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5166e417-2c9f-3501-a0f8-2d25d99e9e81 | -9.64099 | -65.2585 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bcdb44e0-8975-3b03-afb0-e30355365845 | -9.64471 | -67.49062 | 2025-10-19 05:53:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f5e0015-e4f0-37a0-a6cf-57f671b24321 | -9.91952 | -64.09076 | 2025-10-19 05:53:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 75dd4945-5b47-3790-b782-aaa555498380 | -9.69689 | -66.39087 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b5e9f7d-90f8-3817-9963-f5d3c1ea9297 | -9.42568 | -59.01514 | 2025-10-19 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 025bb2f5-8ae7-38e5-9f4a-804f16a59fd2 | -9.6413 | -65.25574 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a1e774e5-19c0-3f24-ac5d-02c4f0ae69dc | -7.81066 | -61.34104 | 2025-10-19 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65e5a956-5760-3e2e-8e3a-55a597eebd69 | -9.55671 | -66.64558 | 2025-10-19 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8bbe62ab-4991-3d41-b506-59c2334f39b4 | -7.62126 | -60.947 | 2025-10-19 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a7177b3-e0b2-367b-b626-1f84608dab8d | -7.62429 | -60.92568 | 2025-10-19 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| e036276f-aa3b-3d81-9c4f-9ba8f898302c | -7.62064 | -60.95134 | 2025-10-19 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30b7ad4f-34cc-396c-9d10-ad454491b599 | -9.69134 | -63.3096 | 2025-10-19 05:53:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88ade55c-7289-3922-a13e-11e3f7922618 | -10.52598 | -68.05651 | 2025-10-19 05:55:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57192474-2b40-3b0a-8568-8e10234f3896 | -7.87864 | -61.18744 | 2025-10-19 06:12:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1eac3c53-6453-3514-aa36-651959ba934f | -7.62124 | -60.93465 | 2025-10-19 06:12:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bdecdc98-2503-3bb2-a525-cf9e0bbbdff7 | -7.6213 | -60.92601 | 2025-10-19 06:12:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6279f6d8-e306-32af-9599-91dac87f6298 | -7.89991 | -63.44899 | 2025-10-19 06:12:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d936dbe-0f1b-3936-a371-b4f556acfa79 | -7.88582 | -61.18279 | 2025-10-19 06:12:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ccd7aba-ba62-3cea-9fa9-b3d9b8007fe7 | -7.88571 | -61.18438 | 2025-10-19 06:12:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1d7d555-e58a-3325-bba8-3eab5358a0b0 | -7.62716 | -60.9325 | 2025-10-19 06:12:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6ed3dc71-a4e8-3bd0-807a-709cbcc715a9 | -7.62197 | -60.92917 | 2025-10-19 06:12:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 84fe734c-882b-3f60-89bc-15f3fe7cbb16 | -7.87849 | -61.18902 | 2025-10-19 06:12:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b0b4aa2-0c94-3b12-8349-fa39883ef834 | -7.45919 | -63.79871 | 2025-10-19 06:12:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 10c9c643-7944-3989-9613-e94cc567540e | -7.46465 | -63.79948 | 2025-10-19 06:12:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3804d5e0-4f76-3ca0-bf79-267a28e053e7 | -7.85874 | -61.60252 | 2025-10-19 06:12:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cf8ddd4-172c-3945-84e5-ee2c4a3ef0be | -7.6206 | -60.93156 | 2025-10-19 06:12:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 526fb2d2-fb90-3588-b0dd-035ad0d0a212 | -7.90043 | -63.4452 | 2025-10-19 06:12:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 839b45cd-8f70-3fdb-bca5-9f45b57b8cd8 | -9.11979 | -65.36541 | 2025-10-19 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a25acd5-56fe-3cd9-ac4d-5c731ba8d316 | -8.60515 | -64.09503 | 2025-10-19 06:14:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9aec3fd2-1c3b-37d0-bafb-f48f844162b3 | -9.73711 | -65.88667 | 2025-10-19 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae77c29e-6952-3dd6-8aef-4b845a9cbdfe | -9.22656 | -65.73682 | 2025-10-19 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 178dec25-98b3-3be4-acee-8125ff34cb70 | -9.56007 | -66.64622 | 2025-10-19 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36eae260-416f-3852-95b0-46379310ffb9 | -9.73788 | -65.8811 | 2025-10-19 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e19c48e-ebff-3596-90f7-27470542b269 | -9.0981 | -65.37433 | 2025-10-19 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 203ec1e8-ba9b-32bc-817d-47d2fe44e680 | -9.09771 | -65.37724 | 2025-10-19 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0741cde-ac45-3f40-894c-650b426199d8 | -9.37947 | -68.1969 | 2025-10-19 06:14:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a19f035f-8966-359a-bb7b-b9224dc7df57 | -8.60608 | -64.08797 | 2025-10-19 06:14:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc13aa4d-468c-322f-8e2b-bcb04389a5c1 | -9.11476 | -65.36473 | 2025-10-19 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16a102c3-adb6-3b36-bb0a-e51e59d79868 | -9.18746 | -61.39006 | 2025-10-19 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 6a714fc4-825d-38a9-87ad-f6989537ded8 | -9.21913 | -61.83046 | 2025-10-19 06:14:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c37657b-7a5f-30ba-9242-9f9d9a665486 | -9.9537 | -66.77349 | 2025-10-19 06:14:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a528f44-f9f1-3624-926d-464e546c030c | -8.71971 | -67.05392 | 2025-10-19 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6117195-a266-3b4a-9bea-4b4643608e2e | -9.18813 | -61.38466 | 2025-10-19 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| bcb9a4de-a692-3468-8e72-e0a1499fa60d | -9.20247 | -67.89563 | 2025-10-19 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae5f5025-ecf1-3c78-9fed-d79b867531e1 | -9.73943 | -65.88892 | 2025-10-19 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 03029721-e669-32e4-923f-611d09d06d5a | -9.74088 | -65.87785 | 2025-10-19 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc92a6e8-0151-3126-aab0-773c8da3a937 | -9.22548 | -61.83128 | 2025-10-19 06:14:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f2d14a7f-5043-392b-bcad-f626998eaef0 | -9.55543 | -66.64559 | 2025-10-19 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 95236fa7-9578-3223-93a6-d96f18d787e6 | -9.23146 | -65.73754 | 2025-10-19 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9bab649-0bd8-3995-91fa-cc4669dd40da | -9.10933 | -65.36697 | 2025-10-19 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b9e180b-b513-321d-a079-f8d9b3bb6296 | -9.74015 | -65.88339 | 2025-10-19 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f344eddf-cf94-3850-b939-02fd8e1ccea6 | -9.11396 | -65.37061 | 2025-10-19 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddbab1d6-e905-3ffd-86ce-f1d9403cd636 | -9.64579 | -67.49313 | 2025-10-19 06:14:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe3befb8-333c-3f64-b9bd-53aabfd8b5d0 | -9.11436 | -65.36767 | 2025-10-19 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46cf14c7-1ee0-3863-9c7d-f1931510e115 | -9.73635 | -65.89211 | 2025-10-19 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aef35bcb-de19-3d1a-aab4-cec6519a2a23 | -8.60561 | -64.09151 | 2025-10-19 06:14:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c36090a-b2ac-3f88-9062-4da8efa7b3e7 | -9.11939 | -65.36836 | 2025-10-19 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e2eaae5-4dc2-3439-b9e6-2ba87e4b2631 | -8.67366 | -66.87183 | 2025-10-19 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e414649f-2a56-3d9d-9f67-57c65a149f3f | -9.73524 | -65.88277 | 2025-10-19 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4a13144-ff82-355e-9650-e36268cab2f5 | -8.94506 | -65.93166 | 2025-10-19 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e03c7afa-528b-3d99-8e0e-185487ae8ab8 | -2.91451 | -52.71944 | 2025-10-19 06:59:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| bd35e7df-d926-32f6-8b42-7e3c984ca9d5 | 1.75207 | -55.93459 | 2025-10-19 06:59:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 909ee56a-3dce-3b34-aa0f-5cd730f05179 | 1.74541 | -55.96324 | 2025-10-19 06:59:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0cd95a95-d7e0-3acc-9554-9a8e6d423495 | -9.21515 | -61.82891 | 2025-10-19 07:01:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4fea4a8b-860c-3deb-a477-ae1c80b153c0 | -7.61346 | -60.91762 | 2025-10-19 07:01:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ff22dc5f-4b8b-33b3-845d-d2db75129427 | -9.18856 | -61.38147 | 2025-10-19 07:01:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 8945d779-4ae7-34cf-9197-60cc75464d8e | -10.75007 | -61.93845 | 2025-10-19 07:01:00 | AQUA_M-M | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a6c5ba38-d2ea-3ddb-ac78-d01e337f6db9 | -7.62107 | -60.93399 | 2025-10-19 07:01:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f9f3451c-c4cc-3c04-8508-ea8098404a12 | -9.17959 | -61.38013 | 2025-10-19 07:01:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| fccb1f77-212a-3d50-9c11-69116c436497 | -6.52679 | -60.02755 | 2025-10-19 07:01:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f2a0b6fb-26b3-30de-8472-d6b6da7aea8e | -7.62242 | -60.92472 | 2025-10-19 07:01:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 8e4ac6f2-3664-3f6a-be1a-db51cfc73de6 | -9.22402 | -61.83022 | 2025-10-19 07:01:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 29e237b6-f9bf-397e-995f-23c43b766c75 | -10.9354 | -60.92469 | 2025-10-19 07:01:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| aa034e50-7359-3432-b8c3-90d1c9c7da53 | -7.61484 | -60.90831 | 2025-10-19 07:01:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4a131ddc-7cd6-3564-92dc-99e34510d95b | -9.73491 | -65.87814 | 2025-10-19 07:01:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f207a281-28a6-3054-bb5c-7c53210deed0 | -9.55083 | -66.63922 | 2025-10-19 07:01:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0bc5f196-8541-3529-bbcc-e2a1cc5cc5a9 | -9.1957 | -61.3873 | 2025-10-19 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 4e59c9e8-f2d2-3244-b95f-7b5675bdec0e | -9.1957 | -61.3873 | 2025-10-19 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 5a4b3f7b-e602-3be2-9064-71c222716bce | -9.1957 | -61.3873 | 2025-10-19 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 4dd21885-4c92-3d61-a29f-295d62f8673a | -9.1957 | -61.3873 | 2025-10-19 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| f43a38c9-b1e0-3981-ab4e-4c4213b0a757 | -14.2135 | -46.0366 | 2025-10-19 09:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 168.2 |
| 0ee0af6b-dd20-31fb-9676-e3dc35cb5c72 | -14.2135 | -46.0366 | 2025-10-19 09:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 129.8 |
| e92e739c-322a-3586-be76-24b6222537be | -14.2135 | -46.0366 | 2025-10-19 09:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 76422c4f-f277-3deb-9d31-68e5601f0ed7 | -14.2135 | -46.0366 | 2025-10-19 10:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 157.4 |
| f5d81542-0bcd-3cf8-9e1a-afa6fce68979 | -14.2135 | -46.0366 | 2025-10-19 10:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 5f42f592-1ee3-35c5-963f-e9760bcd01dd | -14.2135 | -46.0366 | 2025-10-19 10:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 727417d4-ac83-36e4-a0db-8d34403d1395 | -14.2135 | -46.0366 | 2025-10-19 10:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| a5f282a9-e8c6-31e7-92f3-4494405eea7b | -13.8968 | -43.5881 | 2025-10-19 10:40:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| c09f1f4a-48de-37f0-8ec7-43df9536d6e9 | -14.4949 | -45.5949 | 2025-10-19 11:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 11918ede-f93a-3dc4-b4aa-512188ea687a | -14.4949 | -45.5949 | 2025-10-19 11:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 0d1ce181-ea65-3d53-aa34-116d11f2b1ca | -13.9317 | -45.6007 | 2025-10-19 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 172.1 |
| bd877601-9c68-34c0-a3ff-8a791ba59152 | -14.4949 | -45.5949 | 2025-10-19 11:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 27e2f4ce-4678-3b6c-91dd-0b69f54cdc7e | -14.4949 | -45.5949 | 2025-10-19 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 143.5 |


[Clique aqui para ver as próximas entradas](README62.md)
