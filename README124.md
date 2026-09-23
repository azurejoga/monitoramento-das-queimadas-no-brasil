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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e390d138-1e5b-364e-8061-31a234e2e4f6 | -3.68599 | -60.55369 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dd311e34-bba9-311c-9857-9d6ea0e45058 | -6.6769 | -58.57505 | 2026-09-23 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 729c7bd4-c0c4-310e-b7ea-9079880c54ca | -5.59826 | -60.20405 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b0f07ef-c884-32db-998c-05056c5c9e41 | -6.6165 | -59.91553 | 2026-09-23 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3035c4dc-0c9a-35c1-bbf8-c7926a2071d2 | -9.16272 | -61.35897 | 2026-09-23 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a4c1e85-e3b6-35de-8e02-3e288e6588d4 | -3.76279 | -59.47852 | 2026-09-23 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7b0c583-addc-3ae2-910c-5b7cd00c592a | -8.52749 | -67.0069 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87f2cd95-360c-366b-b4a0-591dacc09073 | -9.13777 | -67.9446 | 2026-09-23 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3de69cf-d514-3a0b-abcc-55c400042a3f | -6.75527 | -59.05475 | 2026-09-23 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2233f768-0d9b-38d3-977a-ca0e23ff875d | -4.09495 | -62.09475 | 2026-09-23 06:08:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee5912ad-b2da-3f7f-9fff-a9f32faaa543 | -3.22289 | -61.05519 | 2026-09-23 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ae730a9-038c-3415-9a8c-7cc8df438803 | -6.61719 | -59.91029 | 2026-09-23 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 45d4d5ed-8afa-36ee-a451-02626f871c25 | -4.14848 | -63.42171 | 2026-09-23 06:08:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f126783-0f4c-37c9-bcfb-26f9921bc960 | -3.11011 | -60.71772 | 2026-09-23 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba6107cf-f645-3447-92a8-3ea11869751c | -6.62088 | -59.93193 | 2026-09-23 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7f1a1481-1804-3ca0-a183-1cee59611df8 | -4.1493 | -63.41618 | 2026-09-23 06:08:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb080424-9c7d-38db-8e32-dd0ed8262948 | -8.8971 | -66.86004 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47d96dab-6dc3-39bc-ac6f-f3dc1397e77b | -3.68167 | -60.58363 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 53b93b62-c2d7-33ef-bf93-16c2c3a81f27 | -6.64003 | -59.93481 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 2e956523-df49-3515-b02a-1d9d504dc55c | -8.92806 | -62.41779 | 2026-09-23 06:08:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f94ef0ca-939a-3ede-8c0c-2315233c4685 | -9.22157 | -67.39677 | 2026-09-23 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37e47666-de75-3df1-87a2-4b89de2413ee | -6.47102 | -59.96808 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdbf528f-bd5f-31ad-b625-3256eba50be7 | -8.91869 | -62.38345 | 2026-09-23 06:08:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e8d5019-9939-381d-ac8d-34d3de98d17a | -3.90026 | -60.59119 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9877672d-1101-3ded-884e-c5ca69d13d81 | -3.18417 | -61.10298 | 2026-09-23 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 446ff42c-ee72-3feb-bf96-875e3979fcf0 | -6.14795 | -59.93502 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3319bc5-8750-30e9-88a9-a045d84db199 | -3.40179 | -59.52336 | 2026-09-23 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 405cab1c-81fd-31d0-b87e-0f6bbbf26169 | -7.53812 | -61.49973 | 2026-09-23 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 708df40d-deee-3eeb-9614-214fcb9fc411 | -5.60447 | -60.20485 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0921c66d-e042-3f6c-ae7b-907b22893c90 | -3.40347 | -61.29165 | 2026-09-23 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec7d756c-0615-358b-a4f9-942d7f6d4e61 | -6.64712 | -59.93043 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 371ff647-6d6d-3e02-99da-95efe975e164 | -8.23012 | -62.83908 | 2026-09-23 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| aacaca89-3c48-37b7-9cf8-1165ab7bb7e6 | -7.53758 | -61.50398 | 2026-09-23 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccd98517-654a-34b7-84cb-cfd720ac6593 | -8.54385 | -67.03934 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a9c48c9-fb25-34ec-b5d8-cca134abea75 | -6.74054 | -59.4255 | 2026-09-23 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 60581096-1319-38b1-9327-bb2de8b1f0c1 | -7.49929 | -63.87857 | 2026-09-23 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d08472eb-fc99-311b-89ec-f3df8c9f3f05 | -3.68941 | -60.57178 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9160a3fb-e9b7-30e4-a023-94a88b8216c2 | -6.66969 | -58.57233 | 2026-09-23 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 48547efe-8006-31b8-9864-5b48577847f5 | -6.77959 | -59.62786 | 2026-09-23 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f4d374a-47d4-3ea5-90c9-92a511520374 | -3.74819 | -58.86335 | 2026-09-23 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 407185dd-d516-3649-9277-196042ea9328 | -4.15858 | -60.77481 | 2026-09-23 06:08:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4c51b3b-8641-3e8c-acfa-c9145d648182 | -6.46123 | -59.9938 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ed8c6316-ad61-3ccc-92dd-0aa9135721ce | -6.11541 | -59.88816 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbe79b7b-e97b-3366-b7d4-78c6f52ef07b | -6.7545 | -59.0607 | 2026-09-23 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0da55b92-1399-3c7a-bbb4-17fc8c76b3d8 | -3.1836 | -61.10685 | 2026-09-23 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6d8f694a-052c-3ad6-bcd2-6919200beaed | -6.67082 | -58.5677 | 2026-09-23 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 38171370-19cd-3470-86a7-2090f8a8f585 | -6.42214 | -59.97714 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa6cd13f-53e2-392e-bcd5-9362d0888077 | -6.61041 | -59.96225 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8cc10c7-f9c9-3115-9057-4b8aa4dfbf21 | -6.12889 | -59.93241 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4708c2ac-b349-32ab-bd2d-6b920d7fc84f | -8.5239 | -67.00262 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d5d2845-3884-30a9-ab8f-ff801272a139 | -9.10198 | -61.4361 | 2026-09-23 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9fe3e7a0-eecd-38f9-ad7d-db13fadbd21c | -8.23259 | -62.83482 | 2026-09-23 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd3d4c55-e826-3ecb-b6a9-a60aea2f8881 | -4.16503 | -60.77153 | 2026-09-23 06:08:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03b058cd-7715-39e0-8aed-1a84c23ae1d1 | -9.13231 | -67.94739 | 2026-09-23 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07342ae7-7f09-3286-80db-a8463cea2eb2 | -6.62726 | -59.93287 | 2026-09-23 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 75c343d1-ca58-307b-96f0-d3f7b4065300 | -9.15132 | -61.19043 | 2026-09-23 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3b869a10-0f04-324a-ad29-0e45375036df | -9.11191 | -60.95199 | 2026-09-23 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ba030b4-05bc-3a28-b1f7-d2552e847e54 | -8.51981 | -67.00665 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 136254ae-d881-38a2-a51f-0a2de0e9c5d0 | -6.61307 | -59.92611 | 2026-09-23 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| dd9d17f7-c85e-35ea-aa14-e52c38bc8ebc | -3.90554 | -60.59637 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a92ba53-ba96-3d7b-8402-706f11ec5ca2 | -8.64123 | -67.02635 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19a23207-8c76-3186-a30d-35a1ecca66e8 | -6.63364 | -59.93391 | 2026-09-23 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a7e5166f-bb58-3bbe-b4fa-d2232fe890b0 | -8.54793 | -67.03996 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cbc73cd-0d44-3047-b03f-4ca5fc93afaa | -6.45882 | -59.99336 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0f2516fd-2420-3ade-8050-4a443bcdf26c | -6.73396 | -59.42444 | 2026-09-23 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 13b8f76c-ed1c-33b6-99de-efc2ce942e60 | -6.46829 | -59.98929 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6213d07-d0f0-31f2-b8b8-1141ebb3c093 | -3.86042 | -58.81715 | 2026-09-23 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eafd5e6e-8d26-3ca3-9b14-cb168fe28640 | -3.53355 | -59.61464 | 2026-09-23 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5e0d4fa8-d365-31a5-8560-8871f8f63696 | -8.02802 | -72.47833 | 2026-09-23 06:08:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aafe1ad7-41df-310b-96f3-72caef06fcda | -3.8613 | -58.82358 | 2026-09-23 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 6b8f0d06-b652-3630-9dbc-ad6329e64563 | -7.83155 | -63.41231 | 2026-09-23 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff383c23-853c-31c1-8cb8-3d192d34ffef | -6.61582 | -59.92077 | 2026-09-23 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| f96d98f4-42fe-3ceb-8dbf-2f8cf5345684 | -3.72544 | -60.57264 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a685971-73a1-3087-a0f6-b176e9e039c2 | -3.78738 | -60.75786 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc3f36c2-7e2f-3fe9-947c-b3d9c9fb4dbb | -4.38724 | -60.96283 | 2026-09-23 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7beda930-0fc1-3b3f-8c96-3dd117cfd595 | -3.76003 | -59.47796 | 2026-09-23 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e017a953-7fa7-3f89-a71f-a72b1a15fd0f | -6.60974 | -59.96746 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f30c8171-6629-31ea-97b0-82f98c769dcb | -3.68879 | -60.57603 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bb8a8728-efc0-315e-a201-669b1e40370f | -7.84213 | -72.88334 | 2026-09-23 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45969677-116a-33ce-8288-7dea54477b5d | -9.25905 | -65.44335 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47b0ec58-d469-396a-a050-d102492a79eb | -9.22481 | -67.39446 | 2026-09-23 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 399e7973-de5b-33da-854f-c508215962af | -6.64781 | -59.92524 | 2026-09-23 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35ded4ee-4667-3767-b38e-fe9cd95ce40e | -3.39269 | -61.06157 | 2026-09-23 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e293a8c-9cdd-3acd-af04-c3eedf4d1788 | -7.50429 | -63.8793 | 2026-09-23 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a650a44-2f08-39dd-bb2b-59f052cb724c | -3.14165 | -61.39219 | 2026-09-23 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9a2e19f-6044-31cd-82d9-60e4fa134f7b | -6.42853 | -59.97779 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a1513f3-7c36-36f4-b9b2-526e84de55e4 | -4.25963 | -60.00898 | 2026-09-23 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a0bdfe9a-7137-3850-bb6a-23accb69fee3 | -4.09008 | -62.09055 | 2026-09-23 06:08:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 518560b6-df6b-3ad7-900d-1679aa9ae072 | -8.92614 | -62.41568 | 2026-09-23 06:08:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 425444be-78ea-3446-a305-f9e0a9240d19 | -3.11128 | -61.0874 | 2026-09-23 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 691456ed-f770-3887-ba79-f80a44682710 | -3.55604 | -59.05254 | 2026-09-23 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98845057-5773-3aa7-ac13-88cbed1437a5 | -5.46204 | -60.14422 | 2026-09-23 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48c7751a-0daa-35cd-8cf2-99abbb86df1a | -3.07253 | -61.21243 | 2026-09-23 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 88e8e3d3-4458-339a-8cbe-f48c0b507261 | -3.68694 | -60.58883 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 25bda383-4369-37b6-888b-43bb3f71f72e | -3.6829 | -60.57512 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 538bea6a-be5a-377e-b9a1-1f32e77916e6 | -8.53568 | -67.00813 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9a0a8d8-5a62-3fdc-8eb4-4223bc34604e | -9.34098 | -65.72985 | 2026-09-23 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 21947ada-6656-333b-827f-0559441cfac2 | -3.60693 | -60.57081 | 2026-09-23 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a79c7a9-aa7d-33dc-8cc8-ccfe40432a47 | -6.62155 | -59.92678 | 2026-09-23 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bf657c65-b46d-3e1d-bed3-5f5d5d2c3140 | -4.09545 | -62.09131 | 2026-09-23 06:08:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README125.md)
