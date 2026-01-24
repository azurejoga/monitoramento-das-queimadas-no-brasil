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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd5f598f-e29b-38ec-ae7b-3caaad7f6b84 | 3.23902 | -60.24065 | 2026-01-24 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36b69890-328b-3b17-81d1-f3132b1fe733 | 4.24426 | -59.97287 | 2026-01-24 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78db21a0-43b4-30c0-9f82-2ec08fe412b8 | 4.63799 | -60.42959 | 2026-01-24 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 297c7301-643c-3647-93ac-575fd61d5362 | 2.43065 | -61.14291 | 2026-01-24 05:03:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2888488f-5ff9-389b-95ef-ec614b4980b5 | 0.55223 | -59.85252 | 2026-01-24 05:03:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 14d302d0-e5c3-3c71-a4b4-b767b0958f8c | 0.55994 | -59.84745 | 2026-01-24 05:03:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b6de83fb-e4f8-3237-8b6e-2846ad5efe2c | 1.3546 | -60.05796 | 2026-01-24 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d270ee8e-190e-3a74-981d-c7defd205b5c | 0.5558 | -59.8481 | 2026-01-24 05:03:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2548991b-1dfc-3792-aaaf-1ab3b3ad8320 | 0.78057 | -60.18275 | 2026-01-24 05:03:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9161ed71-f8e7-3b49-af93-6a0142db1071 | 0.55107 | -59.84498 | 2026-01-24 05:03:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b1486b40-54af-31a4-b751-28b01a60a52a | 1.13216 | -60.52314 | 2026-01-24 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12cb98ce-98a3-3c20-9d40-a9e014fea389 | 1.12844 | -60.52808 | 2026-01-24 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e13b8900-768e-3c90-ac99-875f098ca2fb | 0.55522 | -59.84433 | 2026-01-24 05:03:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1776133e-d7b3-317f-acb3-e552428597ad | 0.55165 | -59.84875 | 2026-01-24 05:03:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 86addbf7-3f5f-3b07-8e59-bea7b574af5c | 1.92745 | -61.19736 | 2026-01-24 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b08c784-6636-3dd4-852d-ca4992fb77d0 | 1.02439 | -60.55548 | 2026-01-24 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cec6850-cf99-3582-8d16-cf3d79f4d359 | 1.32791 | -60.41752 | 2026-01-24 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5683408b-b319-31b8-8240-8f258eeae5e8 | 0.55637 | -59.85188 | 2026-01-24 05:03:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5a5899c7-bacf-3429-bc93-37f068b5b74a | 1.32354 | -60.41816 | 2026-01-24 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c930bcd-a47d-3689-9d1e-c62835520f00 | 1.02373 | -60.55122 | 2026-01-24 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62a1328e-07f7-3fd9-a083-0954bd01e8cb | 0.71871 | -59.73571 | 2026-01-24 05:03:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af02412f-aa42-3045-9037-8c0163e48df5 | 0.55464 | -59.84055 | 2026-01-24 05:03:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 859d5bed-6a41-300f-9190-5d21238c9f5e | 1.32856 | -60.42173 | 2026-01-24 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be8d311d-d572-3593-9439-d4dc17e5736b | -1.49055 | -54.07455 | 2026-01-24 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0e5ec55-47f1-34f3-82cc-768fb986a4d3 | -11.52197 | -48.84153 | 2026-01-24 05:05:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 393f0813-4229-33b9-8966-0ac2cdeae0cd | -19.09685 | -56.0594 | 2026-01-24 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9784c3f2-49f6-34fa-a20b-9fcc7d90584f | -14.3148 | -57.59588 | 2026-01-24 05:08:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7adee2b3-f687-3d63-9ecb-51c2c7c8a744 | -16.17423 | -59.45091 | 2026-01-24 05:08:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3aeba0f-c920-3386-984f-e8d22caa736b | -18.81471 | -51.60277 | 2026-01-24 05:08:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 246ee0d8-754d-3a7d-ae57-bd2b86a965e8 | -19.56071 | -54.44028 | 2026-01-24 05:08:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 921bfdee-8bd3-3585-867c-4efc1b29f9f0 | -14.30875 | -57.59126 | 2026-01-24 05:08:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2acd62d7-9ded-3625-9ef6-a904db125f25 | -19.5639 | -54.44595 | 2026-01-24 05:08:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ceef8ccf-b9cf-34c6-852a-fdd5f5560ed2 | -16.30917 | -56.56728 | 2026-01-24 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a621269b-2841-3c2c-84f9-5b26e9e2264b | -18.28431 | -54.6115 | 2026-01-24 05:08:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d821b82b-c708-3a9c-b268-94087158e297 | -14.3115 | -57.59533 | 2026-01-24 05:08:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1be2c3e0-2d61-343a-a442-07903c445686 | -18.31279 | -54.57195 | 2026-01-24 05:08:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bad364a0-4033-3fdf-80a8-2ff34256213f | -16.30973 | -56.56353 | 2026-01-24 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5f26ae46-a5a4-326f-8e8e-8b2e7666784a | -16.44692 | -58.16482 | 2026-01-24 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 70413fdd-ec8a-31f8-a788-465cb34f40c3 | -18.81986 | -51.59845 | 2026-01-24 05:08:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a28a88e-eed9-390d-967f-c118be52e121 | -16.11018 | -56.76953 | 2026-01-24 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f95bb22-cbd4-3972-b32e-8909d95fd722 | -15.25757 | -56.72584 | 2026-01-24 05:08:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2874e0f8-b2c3-3363-bc96-a29b9e910638 | -13.37968 | -54.26205 | 2026-01-24 05:08:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ac8f872-090c-385a-acee-0793f0567275 | -14.3356 | -57.72263 | 2026-01-24 05:08:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20f18366-6239-3e77-8139-76d44acdc30f | -17.69843 | -53.2785 | 2026-01-24 05:08:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd9ca12e-f191-3c67-a377-ac27e51bd4fa | -19.34309 | -54.17532 | 2026-01-24 05:08:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9ef5aad-43ca-36cb-82f4-834be2cfa8bd | -18.81928 | -51.60351 | 2026-01-24 05:08:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6289c09e-d49b-3e91-a11a-8103d82f0e67 | -19.34368 | -54.17228 | 2026-01-24 05:08:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21191432-5b07-321c-9fb1-247cd7dd489c | -18.81815 | -51.61336 | 2026-01-24 05:08:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3515d8b-4b36-3190-b55b-326037ec2803 | -18.76751 | -49.82834 | 2026-01-24 05:08:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3a1c2798-4907-3b6c-b6ae-324599f07165 | -16.26864 | -57.33921 | 2026-01-24 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| b882a33a-6f74-3890-bdad-d4a77b60c89e | -16.17641 | -59.45168 | 2026-01-24 05:08:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02ded715-a1b2-3020-a3b5-0bf9c541eba9 | -19.29824 | -53.17471 | 2026-01-24 05:08:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dfb41788-cbbe-3362-b8ed-4906b8d8937f | -18.25185 | -51.27596 | 2026-01-24 05:08:00 | NOAA-21 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| de11a558-28ef-32ff-b84b-702c98f69841 | -14.33229 | -57.72208 | 2026-01-24 05:08:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1121d34b-9a84-3c32-9df6-a6ad77cb5d03 | -16.3458 | -58.20244 | 2026-01-24 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 1b142170-2419-304b-b96e-4e1ddae951a5 | -13.37818 | -54.26315 | 2026-01-24 05:08:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9da9a88c-59de-3f91-8275-c8f439542960 | -18.25125 | -51.28108 | 2026-01-24 05:08:00 | NOAA-21 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10c4008c-7e80-332b-814b-613d2526cf4c | -15.02132 | -56.48543 | 2026-01-24 05:08:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 230d8324-4f59-3c9a-aa16-9f2af6abd596 | -16.44636 | -58.16839 | 2026-01-24 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ae7ee350-3c4e-37d5-b0f7-56db2936b5cc | -14.3082 | -57.59479 | 2026-01-24 05:08:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d4569dc-3391-3a91-934a-c5e4a3e77cef | -18.81528 | -51.59774 | 2026-01-24 05:08:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c13f599-7e9f-35cf-b48d-f7d59a3d6825 | -19.56457 | -54.44083 | 2026-01-24 05:08:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5143a83-83d9-3b95-88cb-09675c3c7cc7 | -18.30836 | -54.57619 | 2026-01-24 05:08:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c99419d-178a-365f-9e23-a700e5aa9a87 | -19.68039 | -57.19682 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b8968dd1-a177-317f-b09a-e1359dcba0bf | -20.33593 | -57.85051 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 50369547-58ef-38c1-9508-9c62a7c0077c | -20.38037 | -57.86501 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 83f6b87b-c355-3598-b481-33f8346032fb | -20.31914 | -57.84769 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| fbd495b4-12cc-3cda-ba48-e8edd21b16eb | -19.46812 | -55.44495 | 2026-01-24 05:10:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8be64bcb-180c-3310-8b80-3ce2b90021cc | -20.34847 | -57.84801 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c8008a8c-fbdc-3a1b-a447-0856f0c6712d | -19.68963 | -56.86643 | 2026-01-24 05:10:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 531c2b04-9aee-3c6c-9707-7fed7baf9900 | -25.22805 | -52.14246 | 2026-01-24 05:10:00 | NOAA-21 | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 172f128c-bd60-3e48-bc62-5aeb199d78c3 | -19.68333 | -56.86135 | 2026-01-24 05:10:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| c4b15662-e7c9-399b-9cfa-fcbf6e784a58 | -19.68046 | -56.85682 | 2026-01-24 05:10:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d23fbeb0-a8a3-3810-944c-862240b7ba5a | -19.67225 | -57.20057 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 73185e4a-ff40-32e9-83c0-47b519203153 | -20.38652 | -57.86993 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| dacf5769-8fec-3d32-9bfd-f7cbe5a4edec | -19.66957 | -56.85912 | 2026-01-24 05:10:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| acb7eca3-99e8-317f-86c9-07dd3f7eb251 | -22.025 | -56.33884 | 2026-01-24 05:10:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 39cb664a-ae8c-3bf5-9419-a5055cd037e8 | -20.3225 | -57.84825 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| d1925bfb-2c89-3061-a074-c115b51384a5 | -19.67301 | -56.85968 | 2026-01-24 05:10:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f269193f-98e1-3c84-9e66-7745f03b263d | -20.36134 | -57.85405 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a078f0a4-c622-3025-bc42-77d4b7351aaf | -20.34511 | -57.84744 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 25e43c01-b7fb-3d85-8b41-34045485c68b | -20.45931 | -48.67968 | 2026-01-24 05:10:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 995130f0-1e80-3668-bc11-cd6c6bd92784 | -20.35463 | -57.85292 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8881aa80-32ef-3673-8527-d8471c2bf85f | -19.66942 | -57.19614 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| eb351fe9-7490-3b53-b115-f9535bfd3a14 | -21.78268 | -56.28661 | 2026-01-24 05:10:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 543afd40-e68c-30fe-827e-3f9cc8140f17 | -22.19544 | -56.12551 | 2026-01-24 05:10:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13493327-c0c8-3b23-9794-c941888c12c4 | -19.68677 | -56.8619 | 2026-01-24 05:10:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| e9517b44-04d5-32a2-a851-8e12aefc98f7 | -21.28939 | -48.5517 | 2026-01-24 05:10:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74a2e3f2-ef77-3b8f-bd4f-830fc98cffcf | -23.00946 | -52.38802 | 2026-01-24 05:10:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 26e8b358-def5-3f42-9bb8-0a6b696ec581 | -20.38373 | -57.86557 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d15e831d-b3a9-30fc-9167-17f246fd1cb6 | -20.49944 | -55.19588 | 2026-01-24 05:10:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c93b6546-7add-36b8-9d31-2e7ce6e7b78b | -22.03041 | -56.02315 | 2026-01-24 05:10:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48db74f6-7999-3256-a60a-14e06674cbfa | -19.67623 | -57.19725 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2886c710-6caf-3e5c-bfa8-39c2575b1dfd | -20.34455 | -57.85123 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c13608c6-d4cd-3b6c-8311-28ede346f4d0 | -21.78328 | -56.28214 | 2026-01-24 05:10:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da5e458e-da4e-3238-bd68-9dbc2fdad6d5 | -23.53925 | -55.50501 | 2026-01-24 05:10:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9418f12f-b5dd-3722-a9f4-1b0cd8de993d | -19.67645 | -56.86023 | 2026-01-24 05:10:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b8efe8c3-3a67-3f69-9f56-e941309f91ad | -20.45365 | -48.67899 | 2026-01-24 05:10:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f0fc1ef-e019-337c-8fed-e050cd15295e | -19.66885 | -57.20001 | 2026-01-24 05:10:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 6594359b-f2da-36f7-ae38-31ba35ed018a | -23.5386 | -55.51015 | 2026-01-24 05:10:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README6.md)
