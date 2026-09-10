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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 980f046e-7e63-337f-87ce-4018cb7118f8 | -9.7885 | -43.5036 | 2026-09-10 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 243.9 |
| 8c7b227b-127a-354a-be53-d2790bb481cf | -6.7684 | -45.0279 | 2026-09-10 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 5bc03076-5c31-3e35-bf97-42351ec1e44f | -3.3687 | -59.427 | 2026-09-10 14:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 61a18869-d9f5-3116-b1aa-d4817644df7f | -6.7863 | -58.8995 | 2026-09-10 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 21a5e08f-094d-31ee-b8be-cac941d843f3 | -13.2282 | -61.7937 | 2026-09-10 14:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 998b0b5f-f97a-3dbf-add7-2878d6f4a0f4 | -10.7578 | -45.9624 | 2026-09-10 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 3d26a969-255a-3ee5-9254-ead59aeddcc9 | -10.2358 | -45.3004 | 2026-09-10 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 49a1c227-5466-3ef9-9b60-9dc5f726681c | -8.8982 | -61.4393 | 2026-09-10 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 0158d7f0-5650-3e79-aeb2-1faa590d4455 | -6.7684 | -45.0279 | 2026-09-10 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| c6a3f9ae-c556-3148-995c-5f4c0eef18af | -8.0026 | -43.9699 | 2026-09-10 14:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| dcd48c35-b353-3543-83da-e7d7af62065c | -10.7674 | -60.7666 | 2026-09-10 14:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 85814400-574b-3403-a559-7928b7ad37a5 | -6.7077 | -45.4635 | 2026-09-10 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| daecb1fa-94db-345e-a243-0446bc65a5bb | -9.6947 | -43.4217 | 2026-09-10 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 87.4 |
| d5a2c2dd-28a0-35eb-a879-1f1c019f4747 | -10.2362 | -45.2775 | 2026-09-10 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 534609fb-931e-3a63-9a6b-72220c76bed8 | -9.7141 | -43.3956 | 2026-09-10 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 111.3 |
| a3d57be4-3b05-3372-99e9-769d675416ae | -7.9837 | -43.9719 | 2026-09-10 14:10:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 09e06107-5eff-3f00-b423-ab1ae195009d | -10.0815 | -45.4567 | 2026-09-10 14:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 2ef7e2ec-57c2-3963-b90a-5f277331b4a0 | -10.6981 | -46.1287 | 2026-09-10 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 260.7 |
| 6ceaed06-c322-3b50-952c-5c9d4d1ef42d | -7.12 | -42.107 | 2026-09-10 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 111.7 |
| c2f53b17-ebfa-31e9-9d5c-d026604bee63 | -6.8226 | -58.9947 | 2026-09-10 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| c4a75100-c9ef-31cb-b7e5-9da162d51c78 | -3.3687 | -59.427 | 2026-09-10 14:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| ec3dcfbd-f59e-34fd-a0da-f47fdb773a53 | -10.1002 | -45.4772 | 2026-09-10 14:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 4847c70c-c12d-3960-a498-969624e1351e | -10.7582 | -45.9397 | 2026-09-10 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 374.7 |
| 9ffc9482-f4e3-382c-b750-00aa1a6ca9fb | -7.4976 | -45.2814 | 2026-09-10 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 7a951f2d-138e-30b4-9bf9-2e7700ab1910 | -10.7395 | -45.9194 | 2026-09-10 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 186.8 |
| 43597d62-00df-3892-95b6-2839f5604921 | -10.1006 | -45.4544 | 2026-09-10 14:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 118.6 |
| d47f9b69-cf88-38d5-9af1-7e06fb5567e1 | -6.7863 | -58.8995 | 2026-09-10 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| ec61df50-28fb-379f-bc40-8aa7562a0eef | -7.1198 | -42.1309 | 2026-09-10 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 139.6 |
| 36299c57-06c0-3973-9208-7c7d77da7724 | -9.7889 | -43.48 | 2026-09-10 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 427af1b5-62c8-3b05-8568-bf9b0296c2b3 | -10.0812 | -45.4796 | 2026-09-10 14:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 72a9be3a-648d-322b-9761-e1d814d2b90e | -10.0697 | -46.2516 | 2026-09-10 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 3d137cbc-8f09-3b51-9300-01e80c9b2013 | -9.0059 | -65.4186 | 2026-09-10 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 03c54451-467a-3287-9491-96ae95ea51dc | -8.6012 | -47.347 | 2026-09-10 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| fde047f5-4998-360e-b1c8-eee992c6a9c8 | -10.7585 | -45.917 | 2026-09-10 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 171.0 |
| a2ecb464-d2f9-3ace-8bd3-11f632ca8d9f | -7.1009 | -42.1327 | 2026-09-10 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 136.5 |
| 7d719ec2-4646-3feb-8efa-de72f0bb9e5c | -6.7648 | -59.4408 | 2026-09-10 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 51361a9b-6bb7-3e79-84fe-2624f36919dc | -3.4058 | -59.2347 | 2026-09-10 14:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 3aa601e0-26f8-3317-8763-d8dc61637c53 | -9.7933 | -47.0449 | 2026-09-10 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 8c54b79e-3057-31d3-b33b-08eddc789a1e | -7.9834 | -43.9951 | 2026-09-10 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 190.4 |
| f2d4b69a-93b8-3a02-8cc9-dfba752abceb | -7.5167 | -45.2569 | 2026-09-10 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 8cdce58e-5a4a-311f-b5e6-fe4b37697409 | -7.12 | -42.107 | 2026-09-10 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 118.7 |
| d0ac15a0-b2fe-3a65-aa9b-4e16e1702d7c | -7.4976 | -45.2814 | 2026-09-10 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| eed210e9-877b-3db4-9757-a1592d4db1e0 | -6.7863 | -58.8995 | 2026-09-10 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 25549e4c-89b3-3708-87ec-9c939137bc28 | -6.7684 | -45.0279 | 2026-09-10 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 816c5423-257b-3280-bb46-cbb3347775ea | -6.8226 | -58.9947 | 2026-09-10 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| cbc203e4-1891-3e8f-aa4d-99dc413a3e60 | -8.8982 | -61.4393 | 2026-09-10 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 3230f0ba-0a80-3e1d-86be-9ad9940c56db | -3.3687 | -59.427 | 2026-09-10 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 05445af1-7771-35c3-9101-dc1eba8bb269 | -7.1009 | -42.1327 | 2026-09-10 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 119.6 |
| be7d02cc-62da-3408-9cfe-cf8512b966bd | -8.9412 | -44.3995 | 2026-09-10 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 7e83d18a-bd1d-31e6-9126-a619bd146940 | -7.1198 | -42.1309 | 2026-09-10 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 132.0 |
| 866af836-c154-3b85-b180-8014d185bc0c | -6.745 | -45.483 | 2026-09-10 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 74a0a387-ef83-3284-8534-c141f4b60fc1 | -6.8268 | -43.0588 | 2026-09-10 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 2f87ab6b-d463-3487-bfc2-3d6889151f0a | -10.7582 | -45.9397 | 2026-09-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 517.9 |
| d4126e2c-ba7d-3d13-a13f-a791fc6db0d9 | -6.7864 | -58.8801 | 2026-09-10 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 8fc5bca0-15ca-3d75-beea-9092e344419c | -7.9837 | -43.9719 | 2026-09-10 14:20:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 44a890da-785c-3120-956f-8934cc473c2a | -10.0697 | -46.2516 | 2026-09-10 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 4cb45910-a9c4-3c39-b04c-e036909ceb5a | -9.7141 | -43.3956 | 2026-09-10 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 137.8 |
| d4000e04-4dfb-3a32-abdf-369fb1dc3ad7 | -10.7585 | -45.917 | 2026-09-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 182.7 |
| c6e221f6-008e-3d7a-a43c-7ad1ef686144 | -6.7648 | -59.4408 | 2026-09-10 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 2efaf2da-70b4-32af-b4c6-5edbcd68a09f | -9.7885 | -43.5036 | 2026-09-10 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 480.8 |
| 3bb33855-281e-3a00-ac0c-813426e65cbf | -10.2362 | -45.2775 | 2026-09-10 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 208.7 |
| f49d1a96-8155-35d4-a18c-9e8029738556 | -10.7769 | -45.96 | 2026-09-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.9 |
| e4662b97-857a-3e95-9ab5-7b1c27f7e574 | -6.7077 | -45.4635 | 2026-09-10 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 177.9 |
| d859a0e7-08db-3517-982d-173b83b90479 | -10.2358 | -45.3004 | 2026-09-10 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 189.8 |
| 43d20a26-c0be-3470-b5d7-ef1eb304ceb3 | -7.9834 | -43.9951 | 2026-09-10 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 422.8 |
| 5f5bea25-4c1f-3a28-b76a-6207cff4f21e | -10.6611 | -46.0655 | 2026-09-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 74598489-6fa4-3189-aa65-f97471cb0f15 | -9.7889 | -43.48 | 2026-09-10 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 189.7 |
| 7ddaf513-fa3e-33c1-9d57-911d882d8a24 | -10.7578 | -45.9624 | 2026-09-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 00f4c9fd-b585-3a09-96b2-eaabdb16c162 | -8.9412 | -44.3995 | 2026-09-10 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 112.8 |
| e131569b-9f20-327f-b454-0d889b368dd6 | -7.5167 | -45.2569 | 2026-09-10 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| fd817040-c95c-3db1-b146-216f4ca1efef | -9.6947 | -43.4217 | 2026-09-10 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 118.0 |
| bda3ce2b-d2b7-3cf9-aafc-feb745e178f0 | -10.6798 | -46.0858 | 2026-09-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 7576967d-2a4b-38a7-8fcf-9cf63550005b | -6.7648 | -59.4408 | 2026-09-10 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 9e698a60-8253-3cc7-a29d-9e227999bb06 | -8.7254 | -62.3987 | 2026-09-10 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| a17c00f6-43ea-31d2-b0b2-f41c5ffbf358 | -7.4976 | -45.2814 | 2026-09-10 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 55225ba5-ac4f-3311-8d6b-5e1c090d1029 | -6.8226 | -58.9947 | 2026-09-10 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 1d7496fb-4c03-3e04-9c87-097434b76c11 | -8.6012 | -47.347 | 2026-09-10 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 174.8 |
| effafbc6-c20d-3fbd-b27f-6cfb5035652a | -10.7585 | -45.917 | 2026-09-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| ca852e1d-a1b7-3649-aa2d-8187dc612669 | -8.6009 | -47.369 | 2026-09-10 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 2490f162-f8c3-3a87-9733-84be3dfbc9ef | -10.2753 | -45.2038 | 2026-09-10 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 21daf56b-dcdf-343f-8847-86222deca1c2 | -8.8982 | -61.4393 | 2026-09-10 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| f6a847b7-c5e8-3449-bd00-11cb9f07b56d | -10.2358 | -45.3004 | 2026-09-10 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 347.7 |
| 751742e6-b7f4-33d4-b423-cc77f41c38bb | -10.6981 | -46.1287 | 2026-09-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 210.1 |
| 81907814-251a-3721-86b5-fa39267a98c1 | -9.7892 | -43.4564 | 2026-09-10 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| bb809297-ea82-3ee8-ba77-3f6642e23f79 | -10.2552 | -45.2751 | 2026-09-10 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 186.9 |
| c65466f0-43c2-30e5-b159-9470bb4f5d83 | -8.7439 | -62.3979 | 2026-09-10 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 45910a7d-a908-36ab-a13c-106fd2d34da3 | -10.2549 | -45.298 | 2026-09-10 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 291.9 |
| 358b2d60-c3bb-3406-8e97-d14fd34cdbd1 | -10.6801 | -46.0631 | 2026-09-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 211.5 |
| da331426-1291-34cc-b7cf-99be036596f7 | -10.7582 | -45.9397 | 2026-09-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 608fbd64-1a00-3963-a3c3-1a85f5da4da0 | -10.6611 | -46.0655 | 2026-09-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 174.8 |
| a1cc56c5-d58e-30ca-bb5b-a23e03aa5b4c | -8.7438 | -62.4169 | 2026-09-10 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 49256a0d-3337-3178-ad52-84d187fab1c2 | -6.5453 | -62.8914 | 2026-09-10 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 03f560ff-985a-369c-abf3-fb83a0e42ee4 | -6.7864 | -58.8801 | 2026-09-10 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 943a6e3a-631f-3321-8012-84a0b643268a | -6.7077 | -45.4635 | 2026-09-10 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 7ef134ad-ee1b-3ae9-b85c-072650e852b3 | -9.7933 | -47.0449 | 2026-09-10 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| da288798-d885-3a0a-9618-a53b20520dd1 | -6.7695 | -58.6097 | 2026-09-10 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| dc6cec51-6ca3-3737-af65-155fdb3f5e50 | -3.3687 | -59.427 | 2026-09-10 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| d67e6853-c384-3d16-8fe0-d1d27125965d | -10.2362 | -45.2775 | 2026-09-10 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 269.4 |
| bbce3f12-4a4e-3351-b69e-a9f2485e2f78 | -10.2372 | -45.2087 | 2026-09-10 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| f8b3bb47-3da4-315c-9f7a-891847a2b0d8 | -9.7889 | -43.48 | 2026-09-10 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 148.9 |


[Clique aqui para ver as próximas entradas](README50.md)
