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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4463d9a-d06e-360a-95ef-68ebbaf7a6f0 | -15.16744 | -45.64208 | 2025-02-13 04:33:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 160dbaac-b50a-388e-94e3-a95efb3e7ee8 | -13.55875 | -41.84162 | 2025-02-13 04:33:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3c7b3309-bd63-36f1-8172-55e17a0d9856 | -10.53271 | -44.67841 | 2025-02-13 04:33:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f087ede-d9ce-3644-bae0-022c152a32b0 | -15.0807 | -48.94468 | 2025-02-13 04:33:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f29e3ac9-1296-312b-9c46-089fa64aff32 | -10.65547 | -44.49135 | 2025-02-13 04:33:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc1ddb28-2a83-384c-b09b-9eb366e282e5 | -14.51938 | -45.07236 | 2025-02-13 04:33:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09069c9c-a41f-3e2b-b355-2b64b45a993f | -10.77113 | -44.74245 | 2025-02-13 04:33:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2d0634a-7d4d-3699-a229-019f17bf281c | -9.45854 | -43.01825 | 2025-02-13 04:33:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 838a8b80-23ca-3425-8532-c2af09e94851 | -13.56419 | -41.83685 | 2025-02-13 04:33:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 83fc6d1e-ab37-31e1-885c-f734c528af37 | -9.45671 | -43.01775 | 2025-02-13 04:33:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 305ff805-3318-342a-b4bf-50455783e42d | -10.53336 | -44.67375 | 2025-02-13 04:33:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bbf20112-30b4-3d37-8d7b-d2b97b3b27b6 | -12.66574 | -45.04209 | 2025-02-13 04:33:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cb8a145-75ad-3c54-a004-1455261d3513 | -20.22701 | -46.43118 | 2025-02-13 04:36:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d36922e-88d3-33e2-a4f6-2f2077053724 | -20.95171 | -43.17176 | 2025-02-13 04:36:00 | NOAA-21 | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 484e71ac-62e1-3b9a-a3c5-b84d1f2d0992 | -19.02086 | -57.62366 | 2025-02-13 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 4cbb2c01-d89c-365f-9b66-0ea71dd880a5 | -20.4186 | -43.55457 | 2025-02-13 04:36:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d7a5652c-f855-3d6b-91bc-d5954d523a30 | -21.19403 | -44.93616 | 2025-02-13 04:36:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4d8f58ad-596e-312c-a7d9-135cb81e7ace | -21.96153 | -57.59009 | 2025-02-13 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27926dd0-8ba5-325a-a9b3-9c07a49ed349 | -21.62952 | -55.98586 | 2025-02-13 04:38:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad389b71-8776-3ce6-a1b6-f8c739582b0f | -21.62859 | -55.99091 | 2025-02-13 04:38:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 127e4981-0555-3f88-a00c-485513fde8c4 | -21.07563 | -56.39472 | 2025-02-13 04:38:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55c9c454-34ff-37a7-8202-4663c4c1a8b1 | -21.96572 | -57.59089 | 2025-02-13 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21eb3385-3927-3bcd-b73b-cc016e2ceada | -21.07664 | -56.38935 | 2025-02-13 04:38:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4f6f68f-0f68-344d-8b88-c5b0cc5b13a3 | -21.8781 | -56.26436 | 2025-02-13 04:38:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f3de34f7-fb49-3026-a2a3-eb0c324d9704 | -21.8771 | -56.26966 | 2025-02-13 04:38:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3224fd00-0694-3280-a570-e1cac95a4cfc | -21.96653 | -57.58675 | 2025-02-13 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fd4a923-5c61-3692-9bf9-c11a03543320 | -8.18143 | -44.49294 | 2025-02-13 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 264ad215-a6c0-3233-8113-b3d615ea06bf | -10.47781 | -42.46891 | 2025-02-13 04:59:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.1 |
| ee7b2e0c-0d44-32b9-ba7d-2d0fc65d7d1e | -10.65163 | -44.48693 | 2025-02-13 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 501791b8-5d2b-3cdd-a93f-0a5e85fedcac | -10.53094 | -44.67618 | 2025-02-13 04:59:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ece0ee8-70d5-3681-90b0-11385ca01a89 | -10.53472 | -44.67632 | 2025-02-13 04:59:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb7fe811-d8fb-39ee-b477-fe4533c0049b | -10.4711 | -42.46794 | 2025-02-13 04:59:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.1 |
| ff436664-58a6-36ac-93b8-61098ab9655d | -12.41584 | -43.80457 | 2025-02-13 04:59:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2159b973-304f-3029-ab6b-ee4563982271 | -10.65109 | -44.49137 | 2025-02-13 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b65c59c1-4502-3bc0-aedf-61053a81a4d2 | -10.53523 | -44.67212 | 2025-02-13 04:59:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a5259f3-e7dc-3ac0-8f6a-fe23ece5c47f | -10.53148 | -44.67198 | 2025-02-13 04:59:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5d660a8-4a23-3914-82e5-2c691a91bb23 | -21.62921 | -55.98613 | 2025-02-13 05:01:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 147fe19f-79f5-378c-a12a-5fee588f93da | -21.96493 | -57.59039 | 2025-02-13 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42a789f6-2b2b-3b6d-96e4-99d797517932 | -21.96161 | -57.58979 | 2025-02-13 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f7ae2fc-24a7-3b8f-a3c6-c67425f505a8 | -21.87691 | -56.26326 | 2025-02-13 05:01:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fab8d347-d0c7-32ff-845d-ab0fe1c22adc | -21.96885 | -57.58725 | 2025-02-13 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3da22f7b-fcc8-32c4-928e-17417727608e | -21.0786 | -56.39195 | 2025-02-13 05:01:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4576fac-24a7-36f7-a611-d50a8ec6178d | -22.00015 | -57.55378 | 2025-02-13 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d4b13a7-8e5e-31a6-967b-3e8b139bdd32 | -21.87634 | -56.26715 | 2025-02-13 05:01:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 403b2e87-1114-3e99-b4b4-b8904382db0d | -21.07521 | -56.39137 | 2025-02-13 05:01:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 097c2ad2-aa78-371a-b2ad-ce56444b9a4d | -20.58871 | -55.12601 | 2025-02-13 05:01:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 452fdc4f-6b8d-33da-8b8c-2101a7315200 | -21.87975 | -56.26774 | 2025-02-13 05:01:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 01061bfd-3446-37f8-b8bb-4bfc42a7e78c | -13.59558 | -41.83679 | 2025-02-13 05:03:00 | AQUA_M-M | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d36f496e-c6fe-346e-86d2-55890fedf306 | -13.59409 | -41.84637 | 2025-02-13 05:03:00 | AQUA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 7ccc35a1-30e4-364a-9f56-0c1189c102a6 | -20.57608 | -43.76583 | 2025-02-13 05:08:00 | AQUA_M-M | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| e4d798c9-0ae6-3ce6-bc1a-ce0fad189681 | -8.26379 | -69.66087 | 2025-02-13 05:22:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.0 |
| fbed64c0-ab88-30a0-bf56-54cd214d61f3 | -21.96253 | -57.59019 | 2025-02-13 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 615e8b9a-3748-3381-bd12-0bbb7be4f0ff | -21.96744 | -57.58641 | 2025-02-13 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c16c75cc-05b7-3024-ba0f-0c4d401a848b | -21.07705 | -56.39218 | 2025-02-13 05:25:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3422134e-f626-36ea-a46e-869917cb391b | -21.87598 | -56.26899 | 2025-02-13 05:25:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 557d8808-a205-32a9-b971-d734a61f8879 | -21.62928 | -55.98851 | 2025-02-13 05:25:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |


