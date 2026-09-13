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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9069bb99-6aa8-331a-a78d-16b159b1b242 | -10.7532 | -46.2573 | 2026-09-13 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 82f0a283-13c4-39c6-b946-cf5992ed8f31 | -13.3761 | -51.698 | 2026-09-13 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 206.3 |
| 2d9f905c-10c5-3001-ac70-ac876839677d | -5.2723 | -56.0483 | 2026-09-13 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 4e88636a-6936-30e0-b901-1f20741b3db2 | -9.3951 | -50.1121 | 2026-09-13 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| a64efe8a-e482-38e6-a8db-d18ea2337775 | -1.3007 | -49.1464 | 2026-09-13 14:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| dfbd67cc-0351-33d1-a11c-aa517b712ea0 | -5.1439 | -55.9543 | 2026-09-13 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 361406d8-b2df-3db4-aec4-352b343a8199 | -3.8774 | -51.1825 | 2026-09-13 14:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 22018398-9706-3abb-b221-231b07730e31 | -10.8223 | -50.5879 | 2026-09-13 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| a7487cf4-f9ec-3feb-a7a0-39f7ce3c1058 | -12.5137 | -47.1667 | 2026-09-13 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 0d8b859f-8f14-329d-91a8-28976c67845a | -6.0255 | -59.9484 | 2026-09-13 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 138.4 |
| 591d1737-ddc4-34b0-b4b8-f57afeb61fce | -6.0256 | -59.9293 | 2026-09-13 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 8a2916ce-896f-33c5-b39d-f6c71587ad90 | -9.3852 | -49.3847 | 2026-09-13 14:50:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 1d30122a-d450-3270-a10c-c5a3a419996f | -5.2723 | -56.0483 | 2026-09-13 14:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 176.7 |
| 699a8452-301f-347b-858d-6e68d46f6351 | -10.6417 | -46.0906 | 2026-09-13 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 328225e1-7c65-3ad4-8390-00680ef991f9 | -2.6785 | -57.5115 | 2026-09-13 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| d25e0750-54bd-3309-ad4b-178359ab2a99 | -13.299 | -51.7288 | 2026-09-13 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 67968370-4de7-3cf9-9171-33192848e296 | -8.0934 | -54.8488 | 2026-09-13 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 34fba438-1dfc-364d-98f5-459b5a5e654e | -15.3793 | -52.9864 | 2026-09-13 14:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 9c9fd1b8-501a-3928-991d-d2400f9e76e3 | -10.5667 | -51.3349 | 2026-09-13 14:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| be5bfb9e-cb32-31c1-8618-474011238be2 | -11.383 | -43.9614 | 2026-09-13 14:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 613ba849-910f-36ce-b0c7-20b5531d5f85 | -3.6076 | -59.0769 | 2026-09-13 14:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 144.5 |
| dcecd667-f9ea-372d-8ab4-68f03929f315 | -11.3825 | -43.9849 | 2026-09-13 14:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 426.7 |
| a7041e1b-008b-37c5-8a42-db97e2c28fc5 | -9.3763 | -50.1139 | 2026-09-13 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 47c93e68-aa2c-3ce5-b1db-0ab57f4aa472 | -11.0617 | -49.7261 | 2026-09-13 14:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| a0b27980-cdf8-3a0b-9cf2-b85509d7e827 | -8.3733 | -47.545 | 2026-09-13 14:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| dd6925bb-ba76-3731-b699-bea7974aaaa1 | -6.8755 | -47.4313 | 2026-09-13 14:50:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 2ebd8533-391f-3a21-b57c-2f0be960d98b | -10.7274 | -50.6192 | 2026-09-13 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 2adacc16-cc17-3edb-a46d-0f1b09061545 | -6.2832 | -59.9202 | 2026-09-13 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 9a709897-623d-3924-90d9-aa216021a397 | -12.4341 | -47.3349 | 2026-09-13 14:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 03855637-0950-3a32-8c69-72bdd1add638 | -9.3951 | -50.1121 | 2026-09-13 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 981d761b-aae1-3d0c-b17e-8b7affccbb59 | -8.5417 | -54.6985 | 2026-09-13 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 507391a4-8a5e-3609-ab72-2827c2d6db0d | -13.3055 | -51.3235 | 2026-09-13 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| b970ecd2-f9f2-3ffa-8b87-21e8f88fc8b8 | -8.2954 | -51.2212 | 2026-09-13 14:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| bb7d7817-d8bd-3728-8f00-0339a4b04a23 | -9.376 | -50.1352 | 2026-09-13 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 201.7 |
| 0e0b9cbf-6d06-3fa5-b3a9-9cd3dabdc1ba | -11.3532 | -46.8324 | 2026-09-13 14:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 4f532bcd-faaf-39e4-ae68-88d0a34b8875 | -1.3007 | -49.1464 | 2026-09-13 14:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| f58ac3ec-3966-3b2e-a9c6-cd5910353290 | -9.4137 | -50.1317 | 2026-09-13 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 99f56138-78e5-3593-83ce-4041730b8d5d | -6.3015 | -59.9387 | 2026-09-13 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 74f181c5-a1fb-35bd-8b61-3bd867fbd9ec | -10.8028 | -50.6326 | 2026-09-13 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 634b234f-bc9e-39b9-a495-7e45a1d87f32 | -3.5893 | -59.0773 | 2026-09-13 14:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 784678c2-71c5-389c-a851-e66212d6b66a | -6.6524 | -45.3777 | 2026-09-13 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 8aab0703-55ec-3a45-9f25-5aabe5631dd4 | -2.6602 | -57.5119 | 2026-09-13 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 5c9de193-b740-39ca-bbf5-5ccb6ecc04a8 | -8.0748 | -54.8499 | 2026-09-13 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 53a0e62f-f8d7-33b4-9acd-4553385e6604 | -8.4292 | -46.0271 | 2026-09-13 14:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 5581b7f5-ba8e-3eb2-be5c-72a0807e8f6f | -6.3198 | -59.9572 | 2026-09-13 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 2c78ec10-7bb0-331d-900d-82123ceaa0dd | -13.3761 | -51.698 | 2026-09-13 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| e5f7a3ef-9702-3519-98e8-715a6e5b1d41 | -10.7532 | -46.2573 | 2026-09-13 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 1c7d0e76-4ba8-3507-b232-948786f5e105 | -3.4058 | -59.2538 | 2026-09-13 14:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 08e1c457-7a0c-32ef-bfb2-220ba115b0ed | -8.5415 | -54.7187 | 2026-09-13 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 315d1a08-a568-31d1-bd1f-7f46a69c6568 | -3.1697 | -58.6437 | 2026-09-13 14:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| b6a41185-64be-311d-8209-87325aae74d1 | -3.8461 | -58.9178 | 2026-09-13 14:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 90ac1056-99ce-3cc9-82ae-fdc5fc9cfaea | -13.3247 | -51.3211 | 2026-09-13 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 0790e6d1-802d-37a0-8ae4-f41ebedf7786 | -5.1255 | -55.955 | 2026-09-13 14:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 132.3 |
| 68fca96f-a184-36b3-a73f-98f725a87884 | -3.4416 | -59.5213 | 2026-09-13 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 37159ba9-3a5a-3553-85e0-fd4125227aef | -5.2354 | -56.0694 | 2026-09-13 14:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 3239ed15-5e6c-3839-9b8b-82e5d2f61864 | -10.7018 | -54.1458 | 2026-09-13 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 9e339854-513b-3da2-93ce-b03960d2da39 | -15.9184 | -42.5472 | 2026-09-13 14:50:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 149.8 |
| ecf815ea-d63e-3ca1-a1c2-61e91f033425 | -13.3758 | -51.7193 | 2026-09-13 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 2e7c6b37-f50b-3595-b72f-16487a5ef790 | -11.3633 | -43.9877 | 2026-09-13 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 796b65a9-5dbc-39f5-9c02-e4e1273ff6de | -10.5664 | -51.356 | 2026-09-13 14:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 62336095-5b39-306e-8cd0-957f7e8bb47c | -6.863 | -55.5801 | 2026-09-13 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 715b1d1a-51a3-3b76-9af5-39911d88f7e6 | -3.354 | -58.1961 | 2026-09-13 14:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 170.0 |
| 3feac17e-8057-34aa-9e00-9d264881c357 | -2.9395 | -50.3784 | 2026-09-13 14:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| b583150a-b57a-3ab6-8cee-032addab2f64 | -8.6001 | -44.4609 | 2026-09-13 14:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 4db301aa-7f11-36f7-94b9-080608b940e8 | -8.2956 | -51.2003 | 2026-09-13 14:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| c86657d7-66b9-34fa-84ab-e3b5c833face | -4.1223 | -54.0158 | 2026-09-13 14:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| c68aced2-4941-38a1-bfc7-785d031a4818 | -9.3854 | -49.3631 | 2026-09-13 14:50:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 148fec5e-8d82-347c-8e80-5a5a94fce13d | -8.2203 | -55.2427 | 2026-09-13 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| c9dfacac-1e78-3b0c-91d5-52c4d79bb3a3 | -8.1124 | -54.8073 | 2026-09-13 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 1f20efd8-d63b-30da-af82-e009207f8cfd | -11.0433 | -47.1633 | 2026-09-13 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| f0478122-a627-3bd5-9d7c-43f0b8429e12 | -9.6752 | -46.0273 | 2026-09-13 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| be4f2c52-ec23-3828-994e-c8aa0a6d80f6 | -2.6602 | -57.5313 | 2026-09-13 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 08dae583-44f1-321d-9ce0-ee1ea0c6f2ee | -7.12 | -42.107 | 2026-09-13 14:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 141.4 |
| 0dd82820-3af6-34b9-ab22-0d14ffcf5235 | -11.8189 | -46.386 | 2026-09-13 14:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 1ab5239d-bc06-3888-87f7-9d59ba37881c | -9.404 | -49.3829 | 2026-09-13 14:50:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| f7a68ec7-e2e3-3505-8fcd-a65276d9212a | -10.8223 | -50.5879 | 2026-09-13 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 5092a675-d50c-3537-9f03-04a346d09215 | -10.3205 | -49.9567 | 2026-09-13 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 48ec270b-cd04-321a-9f89-580f1c91beca | -12.6636 | -54.6782 | 2026-09-13 14:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| ce449824-0a0d-3e93-8487-f88815a03c2f | -7.9645 | -43.9971 | 2026-09-13 14:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 03d629e7-08c7-38f8-85cf-933dd85f7a74 | -10.6829 | -54.1475 | 2026-09-13 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 400.6 |
| b1bf51a8-56ec-3548-9fea-3e92adf7926e | -9.3765 | -50.0925 | 2026-09-13 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 14c00064-2679-36d9-bd34-3e1d09548006 | -6.3015 | -59.9387 | 2026-09-13 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 130.4 |
| c21e3e8d-a5fc-361d-a28e-ccd4302e2924 | -5.1255 | -55.955 | 2026-09-13 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| e2fc1e6c-91cb-35d8-9ad4-5c35b8e30180 | -9.3951 | -50.1121 | 2026-09-13 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| a8e646af-1bc4-3c97-92aa-99eafaf756cc | -13.3247 | -51.3211 | 2026-09-13 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| c253a06d-6004-3f54-ac76-bdb7ffa384fc | -12.5137 | -47.1667 | 2026-09-13 15:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 7c51dbb5-d891-3373-a0c6-4aa85c0a73f5 | -12.6636 | -54.6782 | 2026-09-13 15:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| c42b9165-48ae-3320-849d-431771c87118 | -3.354 | -58.1961 | 2026-09-13 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 234.7 |
| 22f0052e-ce45-3c9e-8c05-c96a3fc4126e | -9.4137 | -50.1317 | 2026-09-13 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 61ef514e-6cd9-3ef0-a63c-b4d3ebfd50cd | -6.0255 | -59.9484 | 2026-09-13 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 170.6 |
| eb5b9094-c193-3b22-9218-616f1441efb9 | -9.1711 | -49.9835 | 2026-09-13 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 4c900586-f251-33b5-a6f7-44c870a3491f | -2.6785 | -57.5115 | 2026-09-13 15:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 01672158-a4c2-31ad-ad01-e757cbb6b647 | -10.5664 | -51.356 | 2026-09-13 15:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 39009d7a-72d3-32da-89a4-6f0a9b3c178f | -10.5667 | -51.3349 | 2026-09-13 15:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 60de90c6-b8e0-3557-8bec-7cb9bb331329 | 0.1747 | -51.4805 | 2026-09-13 15:00:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 75826ffe-d2a2-39cf-89cc-d6fd44c2cd96 | -13.3949 | -57.0242 | 2026-09-13 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| a50b69c5-6066-3514-8baf-3221bc72326d | -8.7772 | -49.955 | 2026-09-13 15:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 776ae8dd-1b09-3f7b-bcf4-8a27715bdf61 | -9.3763 | -50.1139 | 2026-09-13 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| edf71fcb-fb32-3f52-a4af-b6e2168b26a5 | -6.8755 | -47.4313 | 2026-09-13 15:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| ae3978d3-a2c0-3f37-bdf1-c40333c2e008 | -10.312 | -45.2907 | 2026-09-13 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |


[Clique aqui para ver as próximas entradas](README67.md)
