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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80e187ff-3547-3f7b-87d6-e1e033ebce10 | -7.62293 | -45.54528 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e82a9268-5bee-3883-8440-d105151849bb | -7.62233 | -45.54922 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 25d3cd7c-8e6e-31e2-b74b-2b950898584e | -7.62174 | -45.55315 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4e87181-c5b9-3eff-86cd-3a1e36d59a6f | -7.62062 | -45.53679 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 0135be50-b7ba-3a47-a053-3ed04e657c84 | -7.62002 | -45.54075 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 9a911eac-5937-33a7-9041-8b5828df347e | -7.61942 | -45.5447 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0895655d-7fad-3b36-be0b-0aea69522406 | -7.61882 | -45.54865 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 33564ada-3e56-35ef-9df6-d910df59062b | -7.61771 | -45.53225 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 721ddd04-f456-3d08-bcb8-58e2733b0540 | -7.61711 | -45.53623 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| af0a840e-9822-39e6-ba2c-643265785e1b | -7.61651 | -45.54019 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 437d635b-d37a-350f-bc54-bb843a10c4a0 | -7.6154 | -45.52377 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd4251dc-184f-378f-bcd9-1876635ed783 | -7.6148 | -45.52772 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6e649d0-a175-3b5d-84d3-267b6a5d0e10 | -7.6136 | -45.53567 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 527e1445-5a41-309d-b0d9-5dd264851262 | -7.6124 | -45.54356 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1fecdc6-24fd-36ca-9760-53883cf22c7a | -7.60949 | -45.53904 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ad4a912-7b7c-3494-a124-7a66dc9a3fe3 | -7.22241 | -45.5949 | 2024-10-04 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4d4c467-7484-3757-bacc-34dc37195ce0 | -7.22182 | -45.59875 | 2024-10-04 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c93ed9e1-ea4f-3f97-ac92-c4f5bd2fee4a | -7.22122 | -45.60261 | 2024-10-04 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 053dfc2d-5a34-309b-9cc2-1ee80c2be588 | -7.21892 | -45.59435 | 2024-10-04 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa1e630f-7812-349b-a303-9bac3a7a618d | -7.21833 | -45.59821 | 2024-10-04 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b4d1ffee-4a0f-3e10-9d9d-7b33b4957d17 | -7.16661 | -45.49083 | 2024-10-04 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f71a8ddb-c58b-363e-b4fd-c1bc0f80d9b3 | -7.04997 | -45.33503 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6467aefe-da4f-3576-8ca6-9e9a40b4d15d | -7.04963 | -45.33368 | 2024-10-04 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1a8ade57-a25b-3b57-b3f3-cd2f13204cfc | -9.33545 | -46.56649 | 2024-10-04 04:32:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a813e731-b230-343f-be13-c970809884c4 | -9.33488 | -46.57023 | 2024-10-04 04:32:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e404c29-8488-331a-a063-f4b11d2a504f | -9.33202 | -46.56597 | 2024-10-04 04:32:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 878a3dc5-66bd-3a8b-b71c-786fb1d07ed3 | -9.33145 | -46.56971 | 2024-10-04 04:32:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59304088-f382-375b-925f-0d54abd5b816 | -9.1292 | -46.57027 | 2024-10-04 04:32:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b42b7961-f9d6-3929-b1a5-012b743e8b4a | -9.12577 | -46.56978 | 2024-10-04 04:32:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 838ff705-55ce-3f11-ad08-9cbe9fa33b2b | -8.63421 | -46.52237 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61f36163-5945-37d7-803c-1207abb786bb | -8.63135 | -46.5181 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e03ffe9-5790-39cb-8e33-8188a10a8b1c | -8.6211 | -46.5165 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 678ac4d0-e6ca-35d9-9f9f-2d20c9e451cf | -8.59775 | -46.51301 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f262d8bb-e6a9-34c2-8680-441bfdc191b8 | -8.59718 | -46.51673 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62c34f04-b493-38cf-855b-2ed3e129da1b | -8.59433 | -46.5125 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f981d9c-649f-3557-8472-36c208480328 | -8.59376 | -46.51622 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6fad830-2195-3b8b-a2bf-0ee3a39f5523 | -8.59091 | -46.512 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f673a302-e385-33ff-8c2e-a1185f24cac9 | -8.59033 | -46.51572 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06256d80-c53f-311e-8ac8-e8e13455afbe | -8.58976 | -46.51944 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f433b94-a436-351f-ab09-0ccfe302c1a6 | -8.58691 | -46.51521 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7170769c-9d2e-3e51-b037-4d88823a778c | -8.58634 | -46.51894 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 397049eb-7f0a-32e6-a334-a92816e513e2 | -8.58576 | -46.52266 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fc183e8f-5ebd-32c8-85e6-5b82caa278cd | -8.58235 | -46.52214 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 232eeee5-1fab-3b24-872f-598b3ed906dd | -8.43027 | -46.44234 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb2ccd0b-af78-3352-b452-cb1a5aa47feb | -8.93511 | -47.06098 | 2024-10-04 04:32:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30ba8050-2b04-3baf-b83f-8d8bfb91baf6 | -8.76475 | -46.80923 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5a28b25-49ee-33ca-86b6-789503917c6e | -8.76418 | -46.81287 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 614cf85c-9d86-3390-bfd0-6dd7225010b2 | -8.75458 | -46.80761 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8624659-13d8-3eb6-999f-9f6afc8d6cff | -8.75118 | -46.80708 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4ee3c395-58a0-3dac-8692-e8d010b6061f | -8.75062 | -46.81073 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 09ea1b3b-3efc-3d3d-9868-f94a0f4b68ae | -8.74723 | -46.8102 | 2024-10-04 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| aa995872-c1a4-3f77-b1ee-384259760b57 | -8.41952 | -46.85283 | 2024-10-04 04:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ae131ec-e926-3286-83bb-c19e05e556d1 | -9.84409 | -46.79843 | 2024-10-04 04:32:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d37507e-9c2b-3e9a-bf9d-a82c29672247 | -9.84123 | -46.77141 | 2024-10-04 04:32:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 866ec43b-dd60-3b23-8794-b015a42c798e | -9.84067 | -46.7979 | 2024-10-04 04:32:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eee8f11d-fe40-382e-924c-b784faf1e998 | -9.84067 | -46.7751 | 2024-10-04 04:32:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 909d1d4f-416e-3138-914b-bff372fe0838 | -9.83382 | -46.75117 | 2024-10-04 04:32:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 24a55e2a-9bac-3e7a-94e6-e44913254f61 | -9.83039 | -46.75065 | 2024-10-04 04:32:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4514c806-5e80-3d6f-9079-eae0f34f4f7e | -9.82754 | -46.74639 | 2024-10-04 04:32:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3f0d392-5f45-36a3-be85-4171b0e297dd | -9.82068 | -46.74537 | 2024-10-04 04:32:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a65fbc9-ace3-3dba-a9c8-3af554d3c2a1 | -10.72937 | -46.16306 | 2024-10-04 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc0c891b-ce8d-3cd0-ba04-b1eb143d8ca8 | -10.72819 | -46.17105 | 2024-10-04 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f2e91f9d-2135-3f31-a289-bf7b52500b3b | -10.72643 | -46.15852 | 2024-10-04 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80886f40-14ba-3072-a30a-5361b86aae4d | -10.72583 | -46.16254 | 2024-10-04 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94e1d590-3d08-362f-bd69-f911aef57944 | -10.90967 | -46.30589 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5052c53c-5b84-3232-8c1e-f8570c3038f3 | -10.90617 | -46.30524 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f877f020-9f96-3a31-8e4a-59077f62e9b0 | -10.85408 | -46.3385 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d76190cd-1927-31d9-89ca-d147a509d0a3 | -10.85057 | -46.33799 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6346f86a-1868-3c28-ae5f-0e5b1b8708a3 | -10.84706 | -46.33748 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a04973a-edc6-3951-a3cd-b94adfdfc218 | -10.84356 | -46.33697 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa18ad13-325c-33ef-bc97-2d5d77755fa6 | -10.84005 | -46.33645 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ecdcde0-7d61-3e52-8e45-12d20d29158c | -11.33493 | -46.82772 | 2024-10-04 04:32:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95d19c14-dd22-33bf-ac09-40d5384129b2 | -11.32859 | -46.82288 | 2024-10-04 04:32:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f714c5bf-a7d9-3bc9-9072-f1a5a7cb5780 | -11.29645 | -46.94236 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8d2e7119-567e-313a-98ad-a4c9079e1315 | -11.29357 | -46.93808 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 705e3fb7-cca5-336b-bb0a-e86d31def558 | -11.28956 | -46.91796 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f8474214-671a-3b75-b39d-b7ef1145f0e5 | -11.28784 | -46.92941 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0d1e22d3-b8f0-3e10-ad24-b94f4ce20e22 | -11.28612 | -46.91741 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| f166107d-5491-34f1-a501-aa4f76ddcf6a | -11.28554 | -46.92123 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b11a3209-806e-342a-9dea-e055ea5abb7f | -11.28497 | -46.92504 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cfb24af5-3cbb-326f-8f87-de066c41ff59 | -11.2844 | -46.92884 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8dec2d2-6707-3e61-81a9-40d86c31186a | -11.28268 | -46.91685 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| d3239e4b-ce47-30b7-a2b3-8a36954bdaee | -11.28211 | -46.92067 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 135dfda7-af2d-30d1-9e46-11ad2a37381a | -11.26993 | -46.83704 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3fba0271-010a-3b41-b9f8-40c27a5c94dd | -11.23863 | -46.95247 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b730d6c4-f0a7-3592-bb5b-94536ccdaff5 | -11.22729 | -46.96305 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8448e0a5-40ab-37e8-a3bd-2885f16c7d48 | -11.22443 | -46.95873 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75342f2e-4253-3c66-a0de-22443ed75152 | -11.22386 | -46.96249 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00982302-4499-3ba0-b2d9-8da50f14ca9f | -11.22379 | -46.61119 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3dd25570-7359-3cb4-ab6b-29c2089b4b8a | -11.22322 | -46.61506 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b380440-46d7-3bdb-be65-627e273b68b1 | -11.22099 | -46.95819 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 50856be0-c27f-30fe-bda8-b95da4714a29 | -11.22031 | -46.61066 | 2024-10-04 04:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e30a6b1e-1bd6-30ca-b537-5bc72f7f95d0 | -11.21066 | -46.91036 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f59be5d-a23b-3a21-913e-c3513690a8e7 | -11.20722 | -46.9098 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a6e95a97-ecab-37f7-abf1-fa1570d37bd0 | -11.20321 | -46.91304 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fc6bec34-000b-3dcc-91d4-be8d08cc4c43 | -11.19977 | -46.91248 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a983bbbc-1733-3170-b86b-0e7b1ad59510 | -11.19634 | -46.91192 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5ebfa2f-3e41-3684-9897-480ae9518c0c | -11.19009 | -46.97655 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1d97cf5-5f06-3137-ba06-7012b470d415 | -11.18665 | -46.97603 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0fc1cba5-d0e0-348b-8082-1f9b514d232a | -11.17922 | -46.97869 | 2024-10-04 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README100.md)
