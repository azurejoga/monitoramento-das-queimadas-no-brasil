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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e825929e-8ba2-3db1-a393-a2533dcb2ddb | -15.881 | -59.4362 | 2025-09-18 13:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| a5ec3b0c-d4a8-35ab-aaf1-2d57eafa1e44 | -8.3334 | -44.6507 | 2025-09-18 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 41f91920-1354-3cd8-99e4-6573a0bd99a4 | -10.6741 | -46.4477 | 2025-09-18 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| f3f4bb77-db4c-30b5-8e63-4b148609ad0b | -3.2691 | -43.0674 | 2025-09-18 13:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 1d42de8b-e71a-3772-97f1-13a20c9fc8ae | -7.5601 | -44.7514 | 2025-09-18 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 27aa9ff1-8524-338a-bcf2-3bbbad44358e | -10.6551 | -46.4501 | 2025-09-18 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| e47f6068-f10d-3ea0-b695-f338d734eedf | -6.0786 | -44.6733 | 2025-09-18 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| c7fa9208-9885-36ac-8837-15c24cb6d775 | -8.7073 | -46.3804 | 2025-09-18 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 188.2 |
| 9e624cb0-bec1-39f7-8fcc-d116b9ac20de | -11.1869 | -45.3577 | 2025-09-18 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 583d5a40-352a-35f4-9596-58951fbe4fb4 | -6.0071 | -44.3124 | 2025-09-18 13:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| f9ed03b2-f464-3e09-bdf3-e702c9df0b97 | -9.0202 | -45.5355 | 2025-09-18 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 210.7 |
| 5ca9c7f9-a702-300b-a213-a667580a7f43 | -11.5045 | -43.59 | 2025-09-18 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 7c14492a-5838-3463-97ac-48e62e5f70e3 | -19.5872 | -57.7557 | 2025-09-18 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.9 |
| 69632a55-415c-30b9-b34c-391f6b2a308a | -6.5942 | -45.5856 | 2025-09-18 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 5df705da-4d87-38f0-9dd4-d56db6aff285 | -5.8058 | -45.9142 | 2025-09-18 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 1aa5aeb2-7eff-3872-8983-d9eaa8e9ea59 | -9.1886 | -47.0662 | 2025-09-18 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 514c5983-7db6-38f8-877d-8fb8703060a7 | -6.9978 | -44.62 | 2025-09-18 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 2552a497-6864-3a83-b029-5f9dea856b61 | -7.5412 | -44.7532 | 2025-09-18 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 94e08f60-86bf-375b-a2c6-6e5723ad8749 | -7.8509 | -45.6105 | 2025-09-18 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 1f72ab41-2c9b-3884-b781-3889173112ca | -5.6365 | -43.8796 | 2025-09-18 13:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| da4143d3-fe88-3f2f-b5bf-f08041a8cd3c | -6.9024 | -44.7656 | 2025-09-18 13:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 8a9e1db8-e923-32fc-82c8-dcc18343bd48 | -9.1895 | -46.9994 | 2025-09-18 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 10871e0f-db61-3c5f-92dd-0200fdf1cbc3 | -7.5162 | -45.3024 | 2025-09-18 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 529df676-2b3e-3fbf-8caa-1484acb3ff89 | -8.7262 | -46.3784 | 2025-09-18 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 2503239a-dd69-3153-a591-a864da978a53 | -6.0597 | -44.6976 | 2025-09-18 13:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 6929b0fa-8096-3e4c-bbbb-898a3d0d8485 | -8.7076 | -46.3579 | 2025-09-18 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |
| d2106197-ccf6-31d8-9e08-15d4e1b89286 | -3.2692 | -43.0441 | 2025-09-18 13:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 47525c9a-87fa-3ee6-80bd-c503d4abfbc4 | -19.5869 | -57.7765 | 2025-09-18 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 146.2 |
| 15b72923-6434-3c2f-963e-ef54f6500f4a | -8.6885 | -46.3823 | 2025-09-18 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| ea4ffc80-c47f-3e7a-a283-d0310d746107 | -8.7863 | -46.1029 | 2025-09-18 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| cf076b9a-8e68-3eec-9d7c-03e05789b583 | -8.0196 | -45.662 | 2025-09-18 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 8d606549-14b0-326d-93fd-d0966cf4d7af | -7.6386 | -44.4686 | 2025-09-18 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| e505dc4c-ed00-3207-b8e2-094b7aa9bfc6 | -8.899 | -46.136 | 2025-09-18 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| c8f1ac6d-8d97-3465-b5fc-97a76eb9c398 | -8.0199 | -45.6394 | 2025-09-18 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 72857629-9273-3d21-a759-ac7911be8994 | -7.8698 | -45.6087 | 2025-09-18 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| da506167-51d6-344d-89ce-0556a9785f64 | -8.8801 | -46.138 | 2025-09-18 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| f3358f79-0523-3473-ae4e-c285b2f8243e | -3.8659 | -43.1554 | 2025-09-18 13:40:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| e99f93d5-e84a-38f7-b555-9e6c2bc254e0 | -15.8233 | -59.4016 | 2025-09-18 13:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 00c01d81-5f27-37d6-a131-62046ca81a6b | -8.9638 | -45.519 | 2025-09-18 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 6c6b5842-d6e7-3a10-9446-14a2cf060f82 | -8.9344 | -46.3119 | 2025-09-18 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 38a4608a-70c6-3000-bb14-a20dd9fc99bf | -8.6268 | -45.3054 | 2025-09-18 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 2beb0689-fd81-3207-8788-ba1755e99d68 | -15.8813 | -59.4161 | 2025-09-18 13:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 983de406-e814-3232-8841-b3bebcb44e63 | -7.5818 | -44.4971 | 2025-09-18 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| d66f8172-d5fd-35db-ba30-7f0c0ab4508e | -9.2084 | -46.9974 | 2025-09-18 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 421.7 |
| 4e1d9644-586b-3556-8317-feb6861fd46c | -10.0371 | -47.1952 | 2025-09-18 13:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 32616e93-257b-3203-b0c3-620263141691 | -8.352 | -44.6717 | 2025-09-18 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 53.8 |
| ee49a451-bd20-309e-babe-9b5e48d83103 | -6.9212 | -44.764 | 2025-09-18 13:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| e6d9c849-d341-3048-af06-6efcad8de74d | -9.1895 | -46.9994 | 2025-09-18 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 9755190e-8a34-3236-b56f-e67acdf41d6f | -15.8233 | -59.4016 | 2025-09-18 13:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 1637475d-72ca-3085-800f-e6d94d68eaa7 | -15.8236 | -59.3816 | 2025-09-18 13:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 162.5 |
| d0284bf5-0038-354f-b9f6-bb68daca9a3f | -8.9536 | -46.2874 | 2025-09-18 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| b75cf4fa-5710-3688-9775-93e7554d79ba | -9.01 | -46.3039 | 2025-09-18 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 5a2d213d-d93f-3962-91d0-8b80969ff719 | -7.4478 | -46.3884 | 2025-09-18 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| e1aab148-4805-38b2-b610-42aee6450b2d | -8.9911 | -46.3059 | 2025-09-18 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 56a2550a-f659-300e-adfa-b7fdcf21cadd | -8.9353 | -46.2445 | 2025-09-18 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| cdb990a2-a463-3908-94c6-eb2210d97da4 | -11.4477 | -43.5514 | 2025-09-18 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.9 |
| ad0bf82c-e8de-333b-9a43-c5f69a0f2be2 | -11.1869 | -45.3577 | 2025-09-18 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 337b3905-a0b0-3cd2-b270-90202f8f6c54 | -3.2691 | -43.0674 | 2025-09-18 13:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| e1c42830-a716-3968-b4d2-3d3c068c8e05 | -8.0092 | -44.9589 | 2025-09-18 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 1d4fb72e-4326-36a6-a132-1c280262d1e6 | -8.0199 | -45.6394 | 2025-09-18 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 8241a967-2aef-38ad-8951-272736a229f8 | -8.9161 | -46.269 | 2025-09-18 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 9cabe93c-f4a6-348d-8467-843e3cd6fce1 | -8.935 | -46.267 | 2025-09-18 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 1d7a0579-23be-3871-8925-3129e824d11a | -19.5869 | -57.7765 | 2025-09-18 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 142.7 |
| 9dcd5996-fb23-3650-b24b-2792ad81f2ba | -15.8813 | -59.4161 | 2025-09-18 13:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 6c73c2a4-380c-39cd-87a6-d4b12b8f215a | -10.0374 | -47.1729 | 2025-09-18 13:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 5564a340-4e96-309e-8093-715179c952d8 | -3.1562 | -43.2587 | 2025-09-18 13:50:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 038bf94d-d4c5-3241-8147-1e10117b01dc | -7.5162 | -45.3024 | 2025-09-18 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 73d3a13c-3a3f-370e-895e-ed5a59826fb1 | -8.4831 | -44.7495 | 2025-09-18 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 447d8e96-8cd2-381b-a81c-634778b30fc1 | -6.9024 | -44.7656 | 2025-09-18 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 7b8fbe32-e9bc-39c4-a6e3-717c34361245 | -15.881 | -59.4362 | 2025-09-18 13:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| cc9b28b1-e7cc-3ac2-8954-6cf0c1eb2b06 | -18.5781 | -45.0334 | 2025-09-18 13:50:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 104.4 |
| d52f370d-a1cb-329d-acc3-ba6f8d77d810 | -6.921 | -44.7869 | 2025-09-18 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| a36c9edc-e33a-3fc4-8067-30232c18dff7 | -19.5872 | -57.7557 | 2025-09-18 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 158.0 |
| dad3bcfe-6275-346e-b966-f7156498b897 | -6.6508 | -45.5359 | 2025-09-18 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| f63fec44-f301-37cc-9491-3a14b5b47da1 | -6.9978 | -44.62 | 2025-09-18 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 136.8 |
| cfb70076-6fd5-394c-8cd1-75e9278632ec | -8.4645 | -44.7286 | 2025-09-18 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 96d0808e-e5e7-37a4-a078-0660415a2265 | -11.467 | -43.5485 | 2025-09-18 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 7c811f63-6b0d-31f0-a9e5-77d370825f8e | -3.8659 | -43.1554 | 2025-09-18 13:50:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 4971c96d-2f27-31c7-9484-cc4fd625a2c0 | -7.5164 | -45.2796 | 2025-09-18 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 82662931-479e-314f-bd3f-ac9a62078241 | -6.1876 | -41.234 | 2025-09-18 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 108.7 |
| 38407c18-7959-3b72-8a9f-e261d63a3bfb | -6.3261 | -42.3959 | 2025-09-18 13:50:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 112.3 |
| 12b9e4f7-2675-311d-9ef8-024c85510c4f | -10.0368 | -47.2174 | 2025-09-18 13:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 515fb782-ec69-3f95-b319-12b8b7ddf94b | -9.2084 | -46.9974 | 2025-09-18 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| c7d9e286-5bf2-3095-91a3-7722729677d7 | -8.0196 | -45.662 | 2025-09-18 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 94995241-32c8-35dd-b009-0b0f257be0ab | -8.9449 | -45.521 | 2025-09-18 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 1dded0e7-25b4-3287-a409-2d547601d705 | -6.0071 | -44.3124 | 2025-09-18 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 7d0bed59-fe61-36e8-a6ff-7ed682d530bd | -6.9212 | -44.764 | 2025-09-18 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 5ab1192b-aa83-3208-942f-cb81ce7c523c | -10.0371 | -47.1952 | 2025-09-18 13:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 0f43b019-3d36-3ca5-8991-8b3aacadb8ed | -8.9164 | -46.2465 | 2025-09-18 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 599e434b-2847-3b9e-ac39-24c9febab478 | -6.0786 | -44.6733 | 2025-09-18 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 55696b3b-978f-3ec5-a72a-2aca1ef5c813 | -8.3334 | -44.6507 | 2025-09-18 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 3e8b0700-efa2-3565-b2ad-b73685a74cc2 | -8.899 | -46.136 | 2025-09-18 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 584a6cf0-5a4a-3d1c-af06-e2f06acdf04a | -11.5041 | -43.6136 | 2025-09-18 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.6 |
| eccdd5fd-91b1-3594-a2a3-b354eccac98e | -8.6268 | -45.3054 | 2025-09-18 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 26270f21-ab94-335e-b961-65998bfef1e8 | -5.8646 | -45.5958 | 2025-09-18 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| ee68e4fa-efd7-3b67-9675-273d17079950 | -10.6551 | -46.4501 | 2025-09-18 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 9df78367-ddc9-3131-b870-15ef11735044 | -8.8801 | -46.138 | 2025-09-18 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| d2f0f02c-bcc2-337e-91df-b5126a5a3d91 | -8.352 | -44.6717 | 2025-09-18 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 211.1 |
| f618e965-8931-3c09-b7ab-fc9f8aa46cdf | -8.3523 | -44.6487 | 2025-09-18 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 282.9 |
| 91f7817b-0732-3bc0-a79f-ad9fbb1008bc | -8.0281 | -44.957 | 2025-09-18 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 826.4 |


[Clique aqui para ver as próximas entradas](README37.md)
