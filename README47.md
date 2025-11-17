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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c965420-6fe3-382a-b65b-9305853bae9d | -10.42756 | -58.21523 | 2025-11-17 05:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22418c61-f1b4-3ca0-ac69-7cafe0cca420 | -12.87269 | -46.43508 | 2025-11-17 05:10:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b13d036d-7263-3611-b619-f73ab2f635e6 | -12.70324 | -46.77036 | 2025-11-17 05:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 585bf3b2-0748-3e64-91e1-ad9244cdce22 | -12.89109 | -54.72597 | 2025-11-17 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 13891691-371f-39ed-a4af-00d30c93c2d5 | -11.83931 | -49.2115 | 2025-11-17 05:10:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be9130c4-34f0-313f-b3e2-a2cce89ea66b | -12.29757 | -61.9604 | 2025-11-17 05:10:00 | NPP-375D | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7f7a492-314b-3147-9250-525f9b9e6275 | -11.81588 | -47.58892 | 2025-11-17 05:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 798ab1dd-cbc5-3979-8322-daecc1ce2611 | -9.44204 | -59.20613 | 2025-11-17 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcfb944d-2ecd-335c-aa6c-f2f04134b263 | -12.87456 | -46.46953 | 2025-11-17 05:10:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6fd9203-cc6b-31f2-ba0d-c20e4cbd201a | -12.29361 | -61.95967 | 2025-11-17 05:10:00 | NPP-375D | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be494142-5ae4-3982-97ee-19ae12fcb279 | -11.70619 | -44.45107 | 2025-11-17 05:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b61ce9ad-f80a-32dd-93c3-535d561410e4 | -13.55348 | -47.38404 | 2025-11-17 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c94f0a98-6e6b-3a7c-908b-ad36b25aef0a | -14.6499 | -46.53526 | 2025-11-17 05:10:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 857297e4-2a8c-3ca5-9a8b-05e14ff0bee5 | -12.69744 | -46.76962 | 2025-11-17 05:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9e7236f-7a33-34c0-a28e-1f66b8c089db | -11.15817 | -49.44634 | 2025-11-17 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48f92d07-cf0b-3439-b5d3-9521484d6152 | -11.62211 | -43.90719 | 2025-11-17 05:10:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b40fe975-fd6c-3b5b-8872-b837dba2cc0f | -14.6507 | -46.52821 | 2025-11-17 05:10:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6375ef83-3572-3052-a26a-a7c87efb96bb | -9.4441 | -59.20919 | 2025-11-17 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db542d54-698b-3508-80b5-3db5b315be75 | -13.54794 | -47.38254 | 2025-11-17 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93b15d79-a0a7-3798-b4ab-2975ebcc8190 | -14.54153 | -53.76892 | 2025-11-17 05:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a3bafdb-05b4-35c6-b8b0-29354489eaa4 | -12.80005 | -46.43837 | 2025-11-17 05:10:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aea88d91-e8c4-32bc-95d4-2d4045d6e237 | -14.64906 | -46.54269 | 2025-11-17 05:10:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 00607298-c13a-3dfd-8d68-8ae3f745b7d4 | -10.51505 | -58.57921 | 2025-11-17 05:10:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f3272c7-5d43-3e2e-a10d-895f5f2571ca | -13.28191 | -47.28909 | 2025-11-17 05:10:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85ec73d3-ef55-317d-9121-6897435de2bd | -11.39715 | -55.16269 | 2025-11-17 05:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d12bbd16-a6cd-35d1-a128-6b1fb90fead3 | -11.71153 | -48.8636 | 2025-11-17 05:10:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6e63414d-e957-3449-9bcf-ce4ef99361d7 | -13.3196 | -47.37884 | 2025-11-17 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33b1fdf3-7353-3a8a-8d24-c0b9f80e60ed | -12.88145 | -46.46233 | 2025-11-17 05:10:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0b1284e-7db1-34da-9f36-7399e38b7477 | -16.00985 | -59.9032 | 2025-11-17 05:10:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 906e890c-2d60-3591-a7b8-5fb2ac222f96 | -12.66121 | -47.16495 | 2025-11-17 05:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bdc8c87-264e-3f2e-b60f-4927146e6e0c | -11.6128 | -48.57084 | 2025-11-17 05:10:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db0f9a6c-faee-3ffd-8051-0e9556d982be | -12.70226 | -46.77855 | 2025-11-17 05:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44e41ab9-6f18-3ee3-adf3-f6cc2ac4edb2 | -12.6725 | -47.16644 | 2025-11-17 05:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bbacc14f-09ef-3a48-9f90-f7d7e7e897d3 | -12.80059 | -46.43365 | 2025-11-17 05:10:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a9245b2-7963-3185-bb5f-851052a899a0 | -14.6503 | -46.53175 | 2025-11-17 05:10:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8543df62-ccc7-3d71-bd1d-fb1ecbc9a6fa | -12.20945 | -49.61187 | 2025-11-17 05:10:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6d15245c-3a57-3b43-bcd5-de505a04ce35 | -11.81675 | -47.58182 | 2025-11-17 05:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63cdb346-cf33-3b20-bbbe-4829fb7512be | -11.15749 | -49.45145 | 2025-11-17 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb2cae36-2cd2-3174-8d3c-03bab7b41c1e | -13.27538 | -47.29574 | 2025-11-17 05:10:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a85b8e35-fb69-3c5e-9767-7f9e8c492b07 | -12.96819 | -49.9722 | 2025-11-17 05:10:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 717dcbde-45ed-3fdc-b857-219cf0b9cb1d | -12.69695 | -46.77373 | 2025-11-17 05:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 08911f9e-aba8-3018-8fcc-d276232f8864 | -11.82093 | -47.5927 | 2025-11-17 05:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dcb847c4-2d5e-3cad-b430-78a1ccd99d13 | -12.88836 | -46.45497 | 2025-11-17 05:10:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0059f1c0-d9f5-3e9d-b140-8cf1139139e2 | -14.65118 | -46.5332 | 2025-11-17 05:10:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 37d5dd61-d823-3f73-a8ca-bde3ebaa14f9 | -11.83862 | -49.21681 | 2025-11-17 05:10:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0222076e-60b3-3f28-a5fb-8a19686541e5 | -10.91939 | -49.41348 | 2025-11-17 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b2cd72e-1570-3b57-841e-37169f386652 | -11.1602 | -47.46356 | 2025-11-17 05:10:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddb2a85a-bf65-3cd5-a211-f5acd4934546 | -12.80606 | -46.43839 | 2025-11-17 05:10:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11bd7768-869a-32b3-b025-837e269f6a3e | -10.9149 | -49.41381 | 2025-11-17 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 90d88aa6-d7aa-39de-9241-0ca4a33ff630 | -10.39111 | -59.18542 | 2025-11-17 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8df0310-a7e9-3fbe-be3a-a41e66e3efca | -14.65156 | -46.52965 | 2025-11-17 05:10:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7b1eae2f-ad66-3608-9713-e7be8c2e7f00 | -11.71228 | -48.85792 | 2025-11-17 05:10:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44a0a6b4-253a-30c0-8735-307527b4fdf5 | -11.15479 | -47.46272 | 2025-11-17 05:10:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c0e0e70-4ea2-3047-8791-3880f14877d5 | -12.89461 | -54.7265 | 2025-11-17 05:10:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 097bd742-6fed-3d3b-9ce2-eee5809d4d10 | -11.20162 | -49.41068 | 2025-11-17 05:10:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71fc7e3a-18bb-3554-bcde-304abcc20b6b | -11.71078 | -48.86927 | 2025-11-17 05:10:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 999e9662-eb65-3603-b2a1-1db88111931f | -12.40269 | -47.58653 | 2025-11-17 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ebd8fec-a921-35c4-9b1d-d55e9f5a3321 | -11.70156 | -48.86239 | 2025-11-17 05:10:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5aae2191-9bb9-3be9-b119-6c68cf31deae | -12.87405 | -46.47382 | 2025-11-17 05:10:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae205a23-8424-3500-9116-f06e00db7b1c | -12.88785 | -46.45913 | 2025-11-17 05:10:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c8465a4-d4c2-3490-833b-86b7e2dfaf5f | -12.02063 | -55.51182 | 2025-11-17 05:10:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65219efc-655d-30e1-9bbf-6d8122353c9d | -11.73248 | -49.84653 | 2025-11-17 05:10:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d36bd08-ecf4-308c-ae97-ebfffe01baf5 | -12.63909 | -45.07548 | 2025-11-17 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4571a1b4-fefd-386d-ad9f-8f3a133493e4 | -13.72705 | -51.45839 | 2025-11-17 05:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea13c01c-eb0f-3b6b-9286-5c2f0a0beb5d | -11.20637 | -49.41137 | 2025-11-17 05:10:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7004928-0036-3308-99c0-a8df9e9d1a85 | -12.19923 | -54.2683 | 2025-11-17 05:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a9ac4e6-1f5e-35dc-9ae0-15d67b040b20 | -13.27486 | -47.30009 | 2025-11-17 05:10:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 306f639a-ae25-3a61-9a82-89f6d71ff875 | -12.85102 | -46.46529 | 2025-11-17 05:10:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9d5592e-541f-3610-94d1-43f91502ae66 | -11.82222 | -47.58223 | 2025-11-17 05:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 05478b91-d6e7-39a9-8e7f-89c050f6d260 | -12.20676 | -49.63258 | 2025-11-17 05:10:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f7d074f-7817-353c-b200-ae092dc8850a | -12.70275 | -46.77446 | 2025-11-17 05:10:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 690ea53c-a763-35b2-bf22-0b71b88d53bc | -12.43921 | -44.75332 | 2025-11-17 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a7663ad0-2a8d-3516-9e19-5b16243a6345 | -12.872 | -46.47287 | 2025-11-17 05:10:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c5efe90-9f9d-3519-ac56-f542b40fc7af | -12.19507 | -54.27186 | 2025-11-17 05:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52459d2e-8118-3bcc-bb67-3836935358e2 | -11.39373 | -55.16216 | 2025-11-17 05:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6572886-6e34-34fa-a535-1efe3d62a3ef | -10.51163 | -58.57864 | 2025-11-17 05:10:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e410fd90-c8b6-30c7-a3cd-97cc83e5f1b1 | -11.71577 | -48.86985 | 2025-11-17 05:10:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a668706d-4cca-33a0-b950-1beb13da7d2c | -12.86988 | -46.43843 | 2025-11-17 05:10:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aaa7f498-ade1-3ee5-8123-07bbb10c0f84 | -10.91962 | -49.41458 | 2025-11-17 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49a58920-9da6-32cd-9135-e83c254d8a3d | -12.88095 | -46.4664 | 2025-11-17 05:10:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9caf873-57a5-37be-aabe-2e36a0d2e34b | -12.87216 | -46.43952 | 2025-11-17 05:10:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6a0b2b3-631c-3ec2-a130-de3ebdbec104 | -11.85027 | -56.89791 | 2025-11-17 05:10:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 755fede4-defe-326d-8cc9-4e5b1afbc4e8 | -11.78795 | -44.64778 | 2025-11-17 05:10:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9530ef7-134c-3aac-972b-177bea99818f | -11.80946 | -45.30941 | 2025-11-17 05:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 00034435-ea35-3dca-ae94-07fa570d3682 | -10.91556 | -49.40873 | 2025-11-17 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f16aa1c-0561-3f56-8186-5ffea06e2970 | -12.63265 | -45.07466 | 2025-11-17 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd461113-b537-3a07-8367-52ef1d1f12eb | -12.202 | -49.63197 | 2025-11-17 05:10:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25ccb310-d80b-341f-972c-3603b1064d78 | -12.87839 | -46.46952 | 2025-11-17 05:10:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1732967-1287-3da0-86c5-d5c0198609e2 | -11.70231 | -48.85667 | 2025-11-17 05:10:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 154801af-da52-356e-b867-38ed5ca3a5f0 | -12.9041 | -45.10986 | 2025-11-17 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02645a14-8178-32ee-8730-781368552634 | -12.22441 | -49.60867 | 2025-11-17 05:10:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 572f0fe5-7c49-3d28-bab4-84aebd959ab4 | -12.85053 | -46.46941 | 2025-11-17 05:10:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1c57e71-210d-391c-b88f-1830420c6f9c | -11.96791 | -44.29696 | 2025-11-17 05:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4806d8b-ab92-368d-a7db-31acff16ef06 | -11.78731 | -44.65329 | 2025-11-17 05:10:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93d0f0cf-61a9-3da3-b824-2000a43cd5aa | -11.84972 | -56.90144 | 2025-11-17 05:10:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2050527-73d5-3a25-8201-ff2ca4ad0b45 | -11.61786 | -48.57158 | 2025-11-17 05:10:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ecbe93ee-f745-3acd-96e7-fcab2461da0b | -12.88522 | -46.46239 | 2025-11-17 05:10:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc4d5c46-2d79-3ee3-a16a-a97c6bb5f100 | -13.20817 | -53.32608 | 2025-11-17 05:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3227f45f-6539-391f-af67-a3178d15d75e | -11.82136 | -47.58923 | 2025-11-17 05:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fd91d413-d7b7-372b-8035-07ca7f9bdaf8 | -12.19567 | -54.26777 | 2025-11-17 05:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README48.md)
