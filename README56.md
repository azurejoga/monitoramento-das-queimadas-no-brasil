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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43528a78-0caa-34d9-882f-06a9ac2fa120 | -6.36506 | -45.76415 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea65ade5-fd37-3e7b-812e-a46aad32488e | -10.69847 | -44.5537 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 281e8329-ea7e-31ba-a483-8ed9000eed76 | -10.63283 | -45.23254 | 2025-10-18 04:29:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3db3756e-5640-3d98-97ab-d1872bb23e86 | -6.23835 | -44.15182 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 230aa24a-2f5b-3f27-9ae1-b7603da1b0ed | -4.97661 | -48.36318 | 2025-10-18 04:29:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a900690a-734b-34bf-b345-854de5929e1c | -7.344 | -43.86364 | 2025-10-18 04:29:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| d986136f-468e-3e61-99b0-0834ae6dfc6d | -6.83856 | -42.42352 | 2025-10-18 04:29:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ba3ea4b0-b8a5-33ea-a2ee-29d6596a9532 | -10.7011 | -45.03849 | 2025-10-18 04:29:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8bd20d53-ac88-351a-9507-7f9a3fd4f9fb | -4.83781 | -49.47608 | 2025-10-18 04:29:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae44f8f4-e8b2-3c25-86ba-6c00640aca63 | -10.80897 | -44.01541 | 2025-10-18 04:29:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9d00edf-5f54-3234-8920-2493a5fe707d | -7.47195 | -42.74816 | 2025-10-18 04:29:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e501b818-de97-39ad-b63f-5dd043f7508b | -4.95951 | -45.08937 | 2025-10-18 04:29:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dba6e260-bbca-38cb-9538-d71dd1172f2d | -6.22524 | -44.42244 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a7fdced-ced6-324c-a1d9-1878180f082c | -7.86725 | -55.3735 | 2025-10-18 04:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 781acf89-e792-3df5-b578-00b22d767629 | -8.21014 | -46.91222 | 2025-10-18 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dccb175c-224c-3b74-9c0b-bbd7f17a8765 | -7.62194 | -47.83693 | 2025-10-18 04:29:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7553fa4-0d32-3412-9ab2-b1ed1ae8897d | -10.18227 | -44.53603 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 631e32bb-bbb6-3951-9a49-1fdfc23af851 | -4.78275 | -45.30909 | 2025-10-18 04:29:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 099ef5e9-afd5-379d-9fbb-a09af643cbc5 | -10.59495 | -48.00225 | 2025-10-18 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 374b9066-125a-3c09-8c3d-50472cff91f7 | -8.29797 | -43.39208 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2e737d61-a71d-3ce8-a547-0a1d2fc701d7 | -5.204 | -45.75266 | 2025-10-18 04:29:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a82c4e78-dccd-3b90-b78f-477dd8b1773a | -9.64557 | -47.12042 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e2fbd68e-d814-3bec-b52c-c5ca399ec509 | -5.01183 | -46.02409 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 85be8b4b-d723-316a-bf92-60cb4b841665 | -10.17123 | -46.59653 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50a3341a-821b-34fd-8e32-53f9046a3239 | -3.55019 | -53.11027 | 2025-10-18 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6dd0747b-8050-3aaf-872b-39f41eedf6ed | -6.36784 | -45.76817 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02da30ee-3082-3b49-819e-2f4c453b9afd | -7.58944 | -44.9825 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 115b0467-0642-3bba-a8d3-b896cbcf768c | -6.84168 | -42.42867 | 2025-10-18 04:29:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ce79bf27-fb11-3fc9-b4ac-f07df17aaf1a | -5.07488 | -49.84916 | 2025-10-18 04:29:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6afdac43-8571-33bd-a1b9-7d46912c4495 | -9.04313 | -46.97039 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1234f490-34bb-3eb4-8adf-c93df80e2cd6 | -3.80568 | -51.64466 | 2025-10-18 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2239dca1-292b-3237-8c94-acca206ca140 | -6.41803 | -43.46957 | 2025-10-18 04:29:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8403dad2-661c-3c31-8e89-93308c532b0e | -5.01516 | -46.02461 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a1b715f8-93c5-3691-ad5e-f4090d25a0c6 | -5.17125 | -46.19096 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 314fad0b-1bd5-35dc-9a89-1cb8eed00f01 | -6.31626 | -44.32485 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9fb050e-4d70-3cb1-8014-f328de952867 | -8.36507 | -46.23223 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e65c4bb3-b69a-37cf-b5a1-997637b0c2a1 | -8.10796 | -55.08947 | 2025-10-18 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f6b381dd-b963-39b3-83ee-bdef95124f5c | -6.9945 | -43.84162 | 2025-10-18 04:29:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04b6f365-400c-3970-ad0a-01f37774a7c2 | -10.1115 | -44.55569 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0dc9a5fd-9a35-39f2-9010-2c6ac725b5ba | -10.09181 | -47.65632 | 2025-10-18 04:29:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3d45097-b79b-36c6-908f-a317feee4c79 | -7.0647 | -45.61788 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 290ff57b-fe9a-3c22-b239-cfc617d7d8ca | -8.23618 | -46.91995 | 2025-10-18 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6d8ad8b-656c-31b5-aed6-3f6aa445374e | -5.03258 | -45.14023 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 031ccfb7-d1e0-3053-ac85-75b6adb1c05f | -10.15584 | -44.52548 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1a7b902e-4823-3f92-8dbf-de68bb2ce2da | -6.10426 | -45.85134 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4c6bee9-fc68-312f-a0c0-b821cff0e4d8 | -7.76882 | -42.4905 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 954541de-f28e-3bbb-978f-c58d905df698 | -6.23778 | -44.098 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cade7e1a-78c5-3426-858c-b210247fe0ee | -6.56539 | -44.43145 | 2025-10-18 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ccd26b6-43fc-3278-bc7d-e80cf75171d5 | -8.54131 | -49.60444 | 2025-10-18 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96f03330-eace-369b-8558-2942067bfeb8 | -7.44511 | -44.74187 | 2025-10-18 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6cd8b671-1156-3022-a8db-17fd03d6accc | -10.57592 | -44.50732 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 090b6592-f94d-3fc6-9340-46cad832f64a | -10.10207 | -44.57038 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb71467c-c872-3d1a-bf19-a81460df0839 | -9.09263 | -47.78804 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5130604-cf1f-3d62-9666-f90c59292ab8 | -5.53261 | -44.09691 | 2025-10-18 04:29:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1852765a-a72f-396c-94be-013cd7b6ce71 | -9.35567 | -46.98784 | 2025-10-18 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cfb9d51f-d942-322a-846c-efe2598bd1ef | -7.02511 | -41.81119 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6905a20d-fd7d-3d61-a248-e3e5debf313c | -7.36298 | -44.23465 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea4991c2-9b2c-33ac-b73e-3d2d040fc50d | -8.36668 | -46.20016 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6358c4a8-a66b-3839-8909-dc60f69c1543 | -5.62123 | -48.41537 | 2025-10-18 04:29:00 | NPP-375D | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63788fcd-341e-34c6-ba5d-782517de18cf | -6.59718 | -46.6911 | 2025-10-18 04:29:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b9f32dd-1e35-319f-b53b-11234d184d5b | -6.50959 | -43.71616 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ffed251e-827d-3ab3-9f6c-f0b1539971d3 | -10.52039 | -43.40208 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c40d2dff-5f90-3878-82e8-2704a722e348 | -4.96529 | -44.60545 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b68d38e-12e4-3c2c-907f-bc27dd915abf | -7.76641 | -42.48045 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9777b8c3-d081-3581-8303-1577fcfcabb0 | -10.4945 | -43.4079 | 2025-10-18 04:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| c61c8461-aeb1-361a-87cd-8272b1e444dc | -5.0215 | -46.0097 | 2025-10-18 04:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 0cfbdf79-6a75-3cc1-9eeb-68540852e3b0 | -4.4632 | -43.2386 | 2025-10-18 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| a1cd8b16-dc2f-395a-a23f-d74bd21f29cf | -11.6104 | -44.0913 | 2025-10-18 04:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 63e5fa87-1934-3eb3-aa58-d63e6e32c176 | -10.4941 | -43.4315 | 2025-10-18 04:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 92d97228-62f9-324f-844c-f91d86319158 | -4.4445 | -43.2397 | 2025-10-18 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| e683b115-6bba-3cf4-b8ec-4507d94ce48a | -3.1431 | -50.2464 | 2025-10-18 04:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| a36f906f-8e7c-305e-95ab-4c3b776735ef | -11.6109 | -44.0678 | 2025-10-18 04:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 67ad0da0-18c6-3002-bdd7-90a7834fcd6a | -15.53098 | -45.69426 | 2025-10-18 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed7165f5-b879-3f0d-8a19-c9841985bbd0 | -14.93305 | -46.71391 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75a06618-e01e-32dd-a323-058edc2a1c2d | -18.40942 | -41.825 | 2025-10-18 04:32:00 | NPP-375D | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 301c20a9-cbab-3060-8582-357edd4f8acc | -11.59373 | -44.06242 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4370361-2c0b-38ce-b5da-b4c4c65694bf | -13.13097 | -48.02837 | 2025-10-18 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1cddcca-453c-3c2d-af07-2678d18c0973 | -12.80395 | -48.65388 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd001ae0-363b-3f51-bc53-8f4b454aa0ec | -12.16637 | -45.05698 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cabb637f-8b56-3bf7-89ba-2df6efcde604 | -13.25144 | -48.54111 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2414b9b5-a355-3a68-9a63-f7ee6077f75e | -11.50298 | -44.05099 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9560be50-8b39-301b-9bc9-c19ef35118c8 | -13.04262 | -46.95981 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0527697a-d6e3-3af8-b55c-71c7644e4eed | -11.20698 | -47.83027 | 2025-10-18 04:32:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1c7cd547-3d82-3de3-984d-ab9ad744c820 | -11.35416 | -44.1761 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35868a77-4aac-3d44-8539-24bcf45de3ad | -12.6491 | -54.76602 | 2025-10-18 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5b59ebf-a028-3775-b9e0-d81b91733987 | -13.12984 | -48.03547 | 2025-10-18 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 754a13fa-7371-39d5-9ad2-4b76c0bdb1b0 | -15.04939 | -46.60524 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3433852d-6eb6-36a9-949a-ad9cce77f3bf | -13.5143 | -48.00388 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4df8ee18-e741-3d25-8ad4-f7233f1b2650 | -13.41872 | -43.74956 | 2025-10-18 04:32:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e64980fa-222d-3434-8379-93213478f4b6 | -13.86489 | -48.06897 | 2025-10-18 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 563d3371-fce5-3ff7-bedd-2b6dc26f1495 | -13.87588 | -45.46273 | 2025-10-18 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 52f8d190-afc3-3e04-987e-02d4534fce3e | -13.45999 | -47.98036 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5fa07ddd-0e30-3b9d-9268-0b9d2b9ac838 | -14.92965 | -46.71337 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c330c74-8efc-3d5e-946f-a557a9105714 | -13.41262 | -47.98037 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2af2f7c-3a43-3ccc-bc82-9b81661ebd38 | -11.82704 | -45.13765 | 2025-10-18 04:32:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 537aba34-3c30-36c1-a411-a7834eca4a93 | -14.93079 | -46.70574 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2461c2e-0394-3827-93db-df5697137988 | -14.44508 | -52.89625 | 2025-10-18 04:32:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d248664-df96-3f26-9d60-62abe010f2b7 | -12.31889 | -45.60377 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d1ec3920-8cb0-3e81-8fad-b52fb3b4bae7 | -13.76978 | -48.24317 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 83d5cedc-cebb-3bf7-95b3-f4b34e85b867 | -11.64648 | -47.8542 | 2025-10-18 04:32:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README57.md)
