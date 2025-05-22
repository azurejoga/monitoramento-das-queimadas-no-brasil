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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df6e2676-19e7-3d82-8de1-f03a7776e481 | -11.58212 | -47.6196 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28a9061f-e403-35cf-b174-5dab9af42ca3 | -10.46405 | -49.14727 | 2025-05-22 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 130d6a6d-383c-3f8b-9c84-612585ef2047 | -11.51323 | -48.55503 | 2025-05-22 04:21:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8df022be-ad41-326c-9e4a-636795daa663 | -7.39388 | -45.93666 | 2025-05-22 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22ea2778-30e9-3439-a57a-3fb87d0e4c7a | -10.36795 | -47.97195 | 2025-05-22 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ae560cbf-e586-368a-8917-68d2ac3f0fa6 | -12.3434 | -49.96758 | 2025-05-22 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1524c639-8828-3281-8197-b99ad305572c | -12.08534 | -47.33953 | 2025-05-22 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 2d8c3703-d4bf-3e34-9aa0-7b91d6f02f5b | -11.70853 | -47.78667 | 2025-05-22 04:21:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81912bed-aa4f-30f5-be9c-b75f6e8164cc | -10.68516 | -57.60472 | 2025-05-22 04:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d418a10b-3d3b-35f2-b880-d35e33018657 | -13.53303 | -43.67501 | 2025-05-22 04:21:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ca32b30c-7417-3e48-bc38-c696ff2ba235 | -10.8753 | -45.07317 | 2025-05-22 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25729cac-1a37-3464-b80c-27c1f50334c1 | -12.35182 | -49.9853 | 2025-05-22 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6e3446d1-a7cb-321d-9bb1-d8eae269a1b1 | -10.4633 | -49.15166 | 2025-05-22 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47817086-ae0e-351f-99ab-8d32569c8e67 | -11.91263 | -40.38655 | 2025-05-22 04:21:00 | NPP-375D | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 357ba2b0-79b9-3f27-abce-41a359a8d607 | -9.96108 | -49.81248 | 2025-05-22 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ddacf546-2864-3120-8230-9ca97dcc2862 | -11.11346 | -54.66502 | 2025-05-22 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28924af1-4c38-37e7-90c1-06a8d53ac786 | -11.5575 | -47.44844 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 424029b0-f38d-32b7-8a78-d73466974196 | -9.02219 | -47.7493 | 2025-05-22 04:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef44e0c6-54f0-35ba-bd11-d158c275ecd0 | -10.83017 | -56.9587 | 2025-05-22 04:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fa7df70d-b7b2-3f7b-b0cc-7715c215b47b | -12.36012 | -49.98209 | 2025-05-22 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fd98395f-65cd-38e3-bb9d-869993db5ba3 | -10.09498 | -47.0961 | 2025-05-22 04:21:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b462446d-9767-3c88-b696-bcda317de4d1 | -7.96496 | -49.69535 | 2025-05-22 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e34fe6bf-5c8e-3f1b-b247-86f354006bdb | -7.58359 | -45.85863 | 2025-05-22 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 11366d04-6e2c-3596-9faf-7732598cd11c | -12.08136 | -47.34262 | 2025-05-22 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3e27914-5cbc-35c7-92e6-197bcae41c36 | -11.24839 | -49.49668 | 2025-05-22 04:21:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96c7e6dc-5534-3d07-9d05-64d0590dc68e | -11.57168 | -47.44707 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5bbc0b43-8125-376b-8acc-5c23f61052d0 | -11.08099 | -54.77982 | 2025-05-22 04:21:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5e45315b-ae7f-3fe6-bebb-50b7ace63de6 | -9.96189 | -49.80766 | 2025-05-22 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8503d089-51a0-3431-834e-7821bdcf5fcc | -9.37424 | -48.40985 | 2025-05-22 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2fe60755-11af-3a44-bff0-53351862e445 | -9.02059 | -47.73703 | 2025-05-22 04:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e687318b-6e5f-37b5-9baf-687d479d5cc1 | -11.86081 | -52.27402 | 2025-05-22 04:21:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 33cc21e1-ffc0-3328-8a43-a2bb11811b81 | -10.62135 | -51.79006 | 2025-05-22 04:21:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 493be525-6efa-321a-8d67-ec2e4d4d86fd | -12.35263 | -49.98071 | 2025-05-22 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 06d1dbfe-bbab-3d3e-bce3-9ce55640364e | -10.36446 | -47.97137 | 2025-05-22 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3cfaa8af-9be7-3629-9122-4aca393a2102 | -7.21041 | -45.3529 | 2025-05-22 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 164fad62-fa87-320a-b679-ef1db4230dec | -7.96583 | -49.6903 | 2025-05-22 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 111beebd-c72a-3821-a19b-8f6bd528c6f4 | -10.38126 | -47.97821 | 2025-05-22 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7014ff56-039c-3d34-a851-cb2338e40c4e | -11.64296 | -48.10025 | 2025-05-22 04:21:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b5124220-653e-31ee-b0b4-2d42e32d35b6 | -11.60601 | -47.62366 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26707c27-be22-3dec-a91a-2ba8538b4aaa | -9.96026 | -49.81731 | 2025-05-22 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5fbc19e6-aa1d-3b76-a114-c4068d9356e6 | -12.36092 | -49.9775 | 2025-05-22 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 224feeeb-c07d-3f05-b766-bc71bacda7c3 | -10.02796 | -48.69678 | 2025-05-22 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c5e58ea6-cedc-3c25-8eb8-59a440a3eeda | -11.59979 | -47.61879 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a3a2447-e51c-3e81-85c0-25af35a9218c | -10.55202 | -42.43136 | 2025-05-22 04:21:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7fd04b29-cd0c-3f9f-af64-e3009f0ed09f | -10.36509 | -47.96749 | 2025-05-22 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 871384b6-5f12-3c8f-a482-a985267019ae | -11.58274 | -47.61586 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74b2b0da-82d0-3a94-adf4-d72818444389 | -11.91621 | -54.41481 | 2025-05-22 04:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19a717db-43f1-37c5-a60d-241f7107bde3 | -12.33886 | -49.97151 | 2025-05-22 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 09418b8e-5d2e-3de6-a094-5395dd068d82 | -10.93767 | -55.32247 | 2025-05-22 04:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab6785e6-aff1-3e87-9bcf-149ded651691 | -11.11406 | -54.6618 | 2025-05-22 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 910520dc-30f6-3876-b10c-8f898ec0055f | -11.57974 | -47.87039 | 2025-05-22 04:21:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ccb1371-088c-3887-8123-4023441ec7bd | -13.8974 | -41.30109 | 2025-05-22 04:21:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8655db2d-ee15-3783-803c-6e28ea616681 | -10.65391 | -49.44108 | 2025-05-22 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4ca1cdd4-3b5b-3902-8f9c-c352e4bd6ce4 | -10.62237 | -51.79314 | 2025-05-22 04:21:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a907e589-8731-3e3f-962a-1562418ac055 | -12.07917 | -47.33476 | 2025-05-22 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 11c857b9-7594-303a-953b-ea4c376dd228 | -6.63036 | -55.01262 | 2025-05-22 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d546aba-db33-357c-b4c8-fa7565fdae53 | -11.7995 | -49.33116 | 2025-05-22 04:21:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a35be1a5-5083-3f57-8121-17badcb8d4ed | -12.35638 | -49.98139 | 2025-05-22 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 29747cb2-e198-39d8-8fb9-4379daaefc1d | -11.6032 | -47.61938 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89b9d5f1-051f-3520-99ff-71aa82b0b3df | -8.74876 | -49.75307 | 2025-05-22 04:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f86aea39-a1ec-3789-b1bc-44cf378d4a4f | -10.34188 | -51.69481 | 2025-05-22 04:21:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d82a0edd-9849-3dfe-924b-e75eee2aef33 | -11.80016 | -49.33319 | 2025-05-22 04:21:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f69bb85e-df1c-32ee-8b08-eb27feeea553 | -11.5569 | -47.45212 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| de93e740-06d6-31b7-a046-20d612b34ca7 | -12.07799 | -47.34206 | 2025-05-22 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50a03c47-6b1d-3e21-b24a-8e18bc74fe26 | -11.5541 | -47.44788 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 483d2c67-d157-392a-b48c-5a2d544a6a7f | -13.53598 | -43.67962 | 2025-05-22 04:21:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| d1b85eed-93de-3300-a135-29a93386c825 | -9.04371 | -47.03115 | 2025-05-22 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 192febae-3af7-3447-b9e8-d4c297633dde | -13.53537 | -43.68369 | 2025-05-22 04:21:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd32de73-a336-31b5-9966-807f7df04b32 | -7.9689 | -49.69601 | 2025-05-22 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbb6f723-ba2a-3931-8c9b-05be94c98150 | -12.84156 | -47.39284 | 2025-05-22 04:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7950d974-30d8-35dc-8a3c-d76da4015d5a | -11.55911 | -47.46007 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5533b9cc-abb3-31d4-b8cb-9162a3ed2424 | -11.57424 | -47.45465 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 2c2b8d0a-7ef7-35fa-8cd5-e6c82414661a | -11.5665 | -47.45752 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 772a8e7b-4544-38d0-b277-cd075a6a0bc6 | -8.47679 | -49.60843 | 2025-05-22 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a13f532d-c0f5-35ed-b2f6-a3bf6acc5929 | -11.58553 | -47.62019 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8fa16555-8808-373d-ae1d-28e8221afe09 | -11.57109 | -47.45075 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab0ee20d-3a17-37de-ba5b-54b11b53550e | -9.01995 | -47.74093 | 2025-05-22 04:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8741090-bb96-3f4f-9232-d75d6e2820e3 | -9.96492 | -49.81315 | 2025-05-22 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| adeb4464-366a-3106-ae45-9c56f4c7b428 | -8.74959 | -49.74815 | 2025-05-22 04:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 53949854-7926-35f0-9d32-2da592f91198 | -10.82456 | -56.95903 | 2025-05-22 04:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9a2f174-e8d7-3b18-b557-7ed45894f767 | -11.7965 | -49.33255 | 2025-05-22 04:21:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cc7d1e88-a4ae-3f67-9188-4e91cb5ec25b | -11.08219 | -54.77348 | 2025-05-22 04:21:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d52322c-1f20-392e-8481-e9fb9847a9a9 | -8.90717 | -50.02163 | 2025-05-22 04:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a9bd55b-6814-37a8-b609-8c124ce12347 | -11.58335 | -47.61213 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35be247f-c5e1-3867-a4d7-7641f627d104 | -10.37428 | -47.97704 | 2025-05-22 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 195c9690-eb63-31b1-a2c7-8171f7d84126 | -11.57206 | -47.44672 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e7abde87-c365-3eda-a34e-b60307fdbaea | -12.3392 | -49.96896 | 2025-05-22 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f5bbaf5e-26c8-32b0-9682-b1aa483dfc56 | -12.43214 | -43.72578 | 2025-05-22 04:21:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d55b2378-bf03-3003-91e3-679031c1617e | -11.59918 | -47.6225 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee92401d-fc71-3e9c-88af-9cc33f5eecb4 | -11.55291 | -47.45524 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e6750277-1ada-384d-be30-3e649a6232ca | -10.03226 | -48.69333 | 2025-05-22 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 28df057c-2449-3a0b-82c6-1747472b2916 | -10.12133 | -47.10809 | 2025-05-22 04:21:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa5616fe-7d4f-3040-ad1a-da9141f1483e | -9.02282 | -47.74541 | 2025-05-22 04:21:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e9281ee-ebce-374d-922c-f8dfd46d3acc | -11.97061 | -44.15751 | 2025-05-22 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6185fb2b-a11a-3cbf-86a0-df6515ec86da | -11.91731 | -54.409 | 2025-05-22 04:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d2705ae-4547-3b4b-b7ee-07fa66fa9221 | -8.73761 | -47.98875 | 2025-05-22 04:21:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66c9ae02-a826-3a08-9a8c-f16fa1fb8600 | -12.08474 | -47.34318 | 2025-05-22 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a13b998d-ff9b-3e4a-b9a8-5bf069bbd881 | -8.60079 | -49.51257 | 2025-05-22 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8ff1def-d8a4-3768-ae9f-dbcc695ae690 | -10.83061 | -56.96009 | 2025-05-22 04:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8c21965b-682e-3587-a735-e2787967e734 | -11.79943 | -49.33756 | 2025-05-22 04:21:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README11.md)
