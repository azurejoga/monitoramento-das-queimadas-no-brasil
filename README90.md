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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 871d67f8-2983-30b5-ba5e-a762f782c0e9 | -17.73382 | -44.35064 | 2025-10-18 11:42:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 21.5 |
| b896f095-130c-3bae-b555-d98956b6af21 | -17.49951 | -43.46113 | 2025-10-18 11:42:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| fe1aac0d-33fb-360b-95a2-6c42353d2296 | -16.22032 | -41.79871 | 2025-10-18 11:42:00 | TERRA_M-M | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 19c7430f-6973-369d-974e-53927b86ea24 | -19.20936 | -40.06284 | 2025-10-18 11:42:00 | TERRA_M-M | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 24.1 |
| 70ae2790-2b7f-39a7-baff-35b8fd0eb91f | -16.52155 | -44.61879 | 2025-10-18 11:42:00 | TERRA_M-M | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0c65fcb9-93b8-3df9-a95e-8ffb645234e1 | -17.7315 | -44.36457 | 2025-10-18 11:42:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 6158f97b-d046-3254-a0e1-63b414f1cbb3 | -18.05376 | -43.13954 | 2025-10-18 11:42:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 9dc4dc10-d39f-31a7-80ed-e1c83368fe74 | -15.78208 | -41.33684 | 2025-10-18 11:42:00 | TERRA_M-M | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 6d47cfd0-4d2e-3277-b894-6f5b00cc48e3 | -16.88013 | -41.83575 | 2025-10-18 11:42:00 | TERRA_M-M | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 63dd8466-5a6a-31c0-9c0a-d62704aff8fa | -11.6109 | -44.0678 | 2025-10-18 11:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 4fcf1de9-0b6f-33d3-a410-66392da42b25 | -11.5921 | -44.0472 | 2025-10-18 11:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 953b38cb-2a96-350e-b428-7f00f8a89fbe | -13.8573 | -43.6193 | 2025-10-18 12:00:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| baf8032d-4daf-355a-acd2-bc0a08395484 | -11.9516 | -45.3632 | 2025-10-18 12:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| dae865bf-9f6c-3bf3-bc5d-72478fc59464 | -13.9317 | -45.6007 | 2025-10-18 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 1c26c948-19c1-394f-b34a-63aaa6fa9305 | -11.9709 | -45.3603 | 2025-10-18 12:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 266.3 |
| 86698bb4-707d-3057-9c2a-77c9c846f716 | -11.9521 | -45.3401 | 2025-10-18 12:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 204d5629-fc37-32c9-97d6-41854120a8e7 | -11.3794 | -45.2619 | 2025-10-18 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 365e7945-ef0c-3b41-9eea-e74d1def90f7 | -13.9132 | -45.5576 | 2025-10-18 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| d598248b-2558-3fc3-93cf-8bee15862bf9 | 1.7664 | -55.9608 | 2025-10-18 12:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| c2c8e1b1-3110-32b8-a936-4a12ab336427 | -13.9317 | -45.6007 | 2025-10-18 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 8d4eaf5a-49d2-3221-a4fc-94da82fc44c1 | -13.8573 | -43.6193 | 2025-10-18 12:10:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| c9aab22c-8079-3921-8e81-db6b4f1b057e | 1.7665 | -55.9411 | 2025-10-18 12:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 7d7d196d-52de-343d-90d4-f0ce0dd9d1fe | -13.2644 | -47.1007 | 2025-10-18 12:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 95.6 |
| a1d36def-994d-3ff9-859b-c5f752d0b933 | -13.8573 | -43.6193 | 2025-10-18 12:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| a6eb1279-7e65-39cf-8204-76b7716faf0f | -11.9521 | -45.3401 | 2025-10-18 12:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 1ea0027f-9118-3b71-bfde-e4ea221e4b12 | -11.6104 | -44.0913 | 2025-10-18 12:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 9d67f920-4cb9-36e4-8b79-4749acaa3317 | -13.6312 | -42.4106 | 2025-10-18 12:20:00 | GOES-19 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 93.4 |
| 46278d47-6d8f-33bb-998b-d32ebd627e84 | -11.4939 | -44.179 | 2025-10-18 12:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 4213bfa6-57e7-360f-a13a-3b3c058a4c14 | -13.2001 | -46.4312 | 2025-10-18 12:20:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 79.7 |
| d943a252-4cfc-34d4-b0f8-1b7b51a2e528 | -12.487 | -45.4664 | 2025-10-18 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| c8bd422c-bb91-33ba-ba18-3dc5719d2208 | -12.7196 | -50.8622 | 2025-10-18 12:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 9904d4fb-1d7f-326e-aa6b-844987e48d57 | -12.1678 | -45.0771 | 2025-10-18 12:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| f16f5b4a-b738-3a45-b58a-67fd6cd24970 | -13.9132 | -45.5576 | 2025-10-18 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 149.1 |
| e0eff86c-5376-3a24-80af-c741ead10fb8 | -11.6109 | -44.0678 | 2025-10-18 12:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| c606f395-c90e-3ff1-86ec-88d0164e72af | -12.4678 | -45.4694 | 2025-10-18 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| e203a314-7280-3cb2-962e-c75cbd0befd1 | -11.3794 | -45.2619 | 2025-10-18 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| dbfc2277-88d4-354b-8657-d7a921429c80 | -14.1252 | -44.7053 | 2025-10-18 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 89f90d51-5334-3ab7-85df-1bc50ad0f9ca | -14.0282 | -44.6992 | 2025-10-18 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| ec94b94d-2e23-384d-86c4-968023dd84d3 | -11.6104 | -44.0913 | 2025-10-18 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 190.9 |
| 74194ba8-d0ea-3048-8d71-9cfd8d6af2cd | 1.7665 | -55.9411 | 2025-10-18 12:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 2beac165-86c0-3a84-9d0c-dca555976af2 | -11.6109 | -44.0678 | 2025-10-18 12:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 193.8 |
| 1fdfc6a4-07af-3846-829c-05a2c9356f1f | -11.4939 | -44.179 | 2025-10-18 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 8f816366-b6ae-3e9e-8780-d08de0aeee68 | -13.9132 | -45.5576 | 2025-10-18 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 126b533e-1a7d-3c89-9dfb-c58eb0d341d2 | -11.5921 | -44.0472 | 2025-10-18 12:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| b0b42519-d966-3c74-b5ab-06c16b3afe38 | -11.9709 | -45.3603 | 2025-10-18 12:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| fa7fe57d-fa4a-3a49-bdf6-24a073b9714b | -13.8573 | -43.6193 | 2025-10-18 12:30:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 14532604-3a26-34f0-91d0-628065375649 | -12.1678 | -45.0771 | 2025-10-18 12:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| f9406574-a0e0-3684-aa20-aff21aff138f | -12.1673 | -45.1003 | 2025-10-18 12:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 2d2c7aa6-ffcd-3e2d-a40c-19ee17f1db7d | -13.2644 | -47.1007 | 2025-10-18 12:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 121.2 |
| ddee946b-e5e5-3baf-80de-7386042e3562 | -11.379 | -45.285 | 2025-10-18 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| ce704140-8da0-3e77-a959-fd3637dfa339 | -14.1252 | -44.7053 | 2025-10-18 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 5ed714aa-bbc7-3bdc-b69f-7ece9b3489a4 | -11.4939 | -44.179 | 2025-10-18 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 82388957-4054-33a6-ae28-11e61a307076 | -12.187 | -45.0742 | 2025-10-18 12:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 6df190b6-ec7b-3b60-a039-9c5fcc03f58b | -11.6109 | -44.0678 | 2025-10-18 12:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 268.0 |
| ce44b9aa-92e9-3bac-9b9c-bc9659dee529 | -13.2001 | -46.4312 | 2025-10-18 12:40:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 822685f7-e063-3ccf-a48c-c0f8ff61d11f | -13.2451 | -47.1036 | 2025-10-18 12:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 98.9 |
| f3e964d2-8295-3243-89e3-ebfe2ab6b4d4 | -10.8293 | -43.9248 | 2025-10-18 12:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| d33df3df-d9b3-3531-89b3-cc92b2d4620f | -11.9709 | -45.3603 | 2025-10-18 12:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 24e5fef5-d9d5-365a-942b-7b5f0911edb9 | 1.7665 | -55.9411 | 2025-10-18 12:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 706ad869-3130-31b3-88d0-4c25eeb7a527 | -13.8573 | -43.6193 | 2025-10-18 12:40:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| cd8a9bed-1765-3d1f-a3bc-2b505ba2952b | -14.0477 | -44.6957 | 2025-10-18 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 126.1 |
| b14d2be4-0eac-35c4-af06-f15701e07e91 | -12.1678 | -45.0771 | 2025-10-18 12:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 255c9d16-7981-30a6-b3a0-fe5a40e3248f | -14.0282 | -44.6992 | 2025-10-18 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 730db84a-4fe4-3323-b44b-e0ba32cfdc39 | -13.798 | -45.5079 | 2025-10-18 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 8093aeaf-0556-379f-a7dd-2956e52fb6c9 | -14.969 | -47.0953 | 2025-10-18 12:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 125.4 |
| bf92c722-0402-3ba9-8606-119b1fcd7a00 | -11.3603 | -45.2646 | 2025-10-18 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 285.9 |
| 48da5b0c-f820-3486-a160-d10f2e26b5ab | -13.9132 | -45.5576 | 2025-10-18 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 148.0 |
| a83de0f6-71c5-31a1-bb78-4cacbd2a535d | -13.2644 | -47.1007 | 2025-10-18 12:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 186.4 |
| 318c23ab-add5-3323-bd45-207ed79cd9b7 | -11.5921 | -44.0472 | 2025-10-18 12:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 1df786c9-8dc3-3681-8764-40e927f7e35d | -11.6104 | -44.0913 | 2025-10-18 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 233.7 |
| 7289442e-194c-38d9-9086-f43784e7747c | -11.3794 | -45.2619 | 2025-10-18 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 696.2 |
| c266689e-7d10-3ce1-94ef-7bef1afc338f | -13.2644 | -47.1007 | 2025-10-18 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 232.9 |
| c00580b9-b882-339d-8689-69c938ef0dd1 | -13.2451 | -47.1036 | 2025-10-18 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 30cd7df8-6dd4-3c06-a3c8-33e6c7d55a2e | 1.748 | -56.0004 | 2025-10-18 12:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| e98176e8-7742-3f42-b46a-be851d6033b2 | -11.3794 | -45.2619 | 2025-10-18 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 418.8 |
| 853b9685-cc89-37f4-b20d-fbcf06bd2ae2 | -11.5921 | -44.0472 | 2025-10-18 12:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 51c5b846-2fa5-3048-ab2d-a4d014b76d6f | 1.7665 | -55.9411 | 2025-10-18 12:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 175.2 |
| 60a42f06-fec2-36f8-859f-2df760676960 | -14.0477 | -44.6957 | 2025-10-18 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 76b26504-4bb7-3029-8475-a6703ce52560 | -11.4939 | -44.179 | 2025-10-18 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 5398afba-160a-3cc7-b576-cdd4237d7b32 | -13.2001 | -46.4312 | 2025-10-18 12:50:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 7dde6df9-fedf-32d5-8591-336553ccf2ae | -14.0905 | -43.6235 | 2025-10-18 12:50:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| bc2bf557-bc8b-31d0-9289-90be9af0c10c | -11.3603 | -45.2646 | 2025-10-18 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 3f18d5d1-088f-345b-b9b8-9f0958ba0d44 | -11.4931 | -44.2259 | 2025-10-18 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 44440f1b-9968-3a05-9b49-3082de79f28c | -12.187 | -45.0742 | 2025-10-18 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| eaf6b11c-361b-3376-9e74-fa05f1229ce0 | -11.9713 | -45.3373 | 2025-10-18 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 256.1 |
| 4de9d360-2286-33ce-8777-ce85678f3d76 | -14.1252 | -44.7053 | 2025-10-18 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| b545074c-f761-3b9e-850d-d1cea00dcf2f | -11.9521 | -45.3401 | 2025-10-18 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 310048a0-5a65-3d6d-9031-d041226a43b9 | -11.6104 | -44.0913 | 2025-10-18 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 539.5 |
| 6dc1344e-6fbb-3ebf-8c44-a8ed6b473aab | -11.6109 | -44.0678 | 2025-10-18 12:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 392.8 |
| cf4e1a93-6216-3f06-a8f4-ece94cb88a71 | -12.1673 | -45.1003 | 2025-10-18 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 00a22ce8-f9a7-396d-80b8-108969855124 | -11.9516 | -45.3632 | 2025-10-18 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| ece1a22e-d611-36a0-a697-7674a50fd57d | -12.1678 | -45.0771 | 2025-10-18 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 09c6c323-3f88-3167-a6a6-1933c2c54334 | -11.9709 | -45.3603 | 2025-10-18 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 265.9 |
| 425d7cae-df65-3892-8134-1e591208084a | -11.9709 | -45.3603 | 2025-10-18 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 611.0 |
| ddfa9a18-8ea3-3e5b-95b1-5641af09e0a8 | -11.8544 | -45.4464 | 2025-10-18 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 43620630-dc37-3ea9-a2b1-7de2be4af991 | -14.0477 | -44.6957 | 2025-10-18 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 37f93883-07dc-31ef-aec6-ed722f9157da | -14.0282 | -44.6992 | 2025-10-18 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 3dcd4f92-3a7a-3857-8f81-9ec72ba11477 | -11.36 | -44.1755 | 2025-10-18 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| c309a034-c349-338b-8541-e3dd11eef7f3 | -11.204 | -47.8318 | 2025-10-18 13:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| c6d9a21a-4eaa-365d-8742-c5c2040235c0 | 1.7665 | -55.9411 | 2025-10-18 13:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |


[Clique aqui para ver as próximas entradas](README91.md)
