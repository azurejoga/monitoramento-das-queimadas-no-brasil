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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 574f429d-2537-3945-8379-1b8d021d0fc3 | -15.03347 | -54.81366 | 2025-08-19 00:48:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 88959013-0947-355c-b1e9-bb2941146bce | -16.62022 | -51.35901 | 2025-08-19 00:48:00 | TERRA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 47d5fe27-9b82-350f-b435-814792169be6 | -12.66429 | -45.8135 | 2025-08-19 00:48:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 6068294a-7e77-34db-9cea-62a0a6bc00a3 | -14.86963 | -48.03137 | 2025-08-19 00:48:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 4dc766f4-e15d-3f36-8b7a-fb43ca409ffc | -14.97681 | -54.79476 | 2025-08-19 00:48:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 3d66d5ac-abfb-3e3a-ab3a-3a768af02236 | -14.98747 | -54.79303 | 2025-08-19 00:48:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5d99c029-175a-393e-82ab-7942f4b9538c | -14.17053 | -45.30902 | 2025-08-19 00:48:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 70f0f105-82f3-3a54-bdd7-34a58f973e3f | -15.69626 | -47.65648 | 2025-08-19 00:48:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d20048d7-56aa-3247-a7e9-7da8ff85db5f | -17.88474 | -48.60313 | 2025-08-19 00:48:00 | TERRA_M-M | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0d15de9d-6cdd-36c7-aa4e-c99c540c546d | -19.29778 | -48.43169 | 2025-08-19 00:48:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 26efbbdd-0275-3cee-8ace-896494beb111 | -12.98053 | -49.36524 | 2025-08-19 00:48:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ebb79aca-6346-3b6d-a671-5134995c7578 | -15.02112 | -54.80161 | 2025-08-19 00:48:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 49bd926f-6163-3e48-abe0-b1f8338e1c85 | -17.41675 | -46.7141 | 2025-08-19 00:48:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 46354402-0baf-3d90-9df2-d1cc04bd104c | -14.96613 | -54.79633 | 2025-08-19 00:48:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 01f24d12-bfd3-3ff5-8def-dbca5326ccc0 | -16.79774 | -50.0947 | 2025-08-19 00:48:00 | TERRA_M-M | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 55b343ba-ccd6-366d-8306-ff14064431c5 | -17.48892 | -45.86177 | 2025-08-19 00:48:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9e0e23d7-37d9-3f47-bf4b-17d664bf9a0a | -14.87121 | -48.04208 | 2025-08-19 00:48:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 4f2a7737-411e-3350-97cd-60bbc5334979 | -15.4152 | -49.5643 | 2025-08-19 00:48:00 | TERRA_M-M | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 68fe8c71-a04e-3de2-8da3-9b5778fd7706 | -17.40682 | -46.7159 | 2025-08-19 00:48:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 69e25560-dee9-3e43-9df3-06bda760a222 | -16.49063 | -45.10035 | 2025-08-19 00:48:00 | TERRA_M-M | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 150734be-9103-3d81-8475-062fec813fab | -17.89516 | -48.61123 | 2025-08-19 00:48:00 | TERRA_M-M | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f2b17043-fa90-3a2f-919d-2c80fae1ca6b | -14.97481 | -54.81492 | 2025-08-19 00:48:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 5a9c2723-5a54-3dd5-8dbd-b2ff89f94b08 | -16.40709 | -49.47562 | 2025-08-19 00:48:00 | TERRA_M-M | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0fa78ae5-920d-3171-a32e-92a9b57222f5 | -15.4076 | -49.57498 | 2025-08-19 00:48:00 | TERRA_M-M | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 285.8 |
| d4bb24c1-4376-345d-a0a9-b897abaa94a3 | -12.99157 | -45.21051 | 2025-08-19 00:48:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| bb3d81ee-565d-3e56-b085-d85d5042c43c | -13.24972 | -50.80898 | 2025-08-19 00:48:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 865ef43d-a78c-3270-b431-9cde8e9b3b81 | -14.97846 | -54.80865 | 2025-08-19 00:48:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |
| baa91c70-56fc-3670-b763-0e7e33b56e62 | -14.97136 | -54.78741 | 2025-08-19 00:48:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| bcc02c41-46d9-309a-9566-f76dd24a71a5 | -13.0007 | -45.19086 | 2025-08-19 00:48:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 5cc49993-c97c-3b01-82e3-8d6faa5640c2 | -13.86313 | -45.53753 | 2025-08-19 00:48:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a999aa81-9dee-391d-b48b-8090033ecb61 | -16.71524 | -47.61988 | 2025-08-19 00:48:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 44826d53-bb4f-3fbe-9c22-0fd1bc98599b | -12.04266 | -44.02084 | 2025-08-19 00:48:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 12241bc9-766e-3d4e-bdc4-8670280bfc6e | -20.3304 | -51.70398 | 2025-08-19 00:48:00 | TERRA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 21.8 |
| d87eb85e-b446-353a-9023-f2aed1de07ab | -15.0196 | -54.8112 | 2025-08-19 00:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| c5d689d5-680c-3952-b252-92115b025c4f | -16.4863 | -45.0702 | 2025-08-19 00:50:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 116.0 |
| a9505537-ad16-3f4e-ab61-538f9bf7eba5 | -5.8807 | -48.1125 | 2025-08-19 00:50:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 79dc9014-59ee-3678-83b3-f55a33bc8bc1 | -4.0007 | -42.5149 | 2025-08-19 00:50:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| b1c43430-d10e-3529-8973-1bab725a1c17 | -16.4665 | -45.0743 | 2025-08-19 00:50:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 23a497bb-bd24-34ed-b506-7d89973a9005 | -16.4659 | -45.098 | 2025-08-19 00:50:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 398.5 |
| 79077349-716a-369d-8543-5b75c29ca330 | -11.8512 | -51.5801 | 2025-08-19 00:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 7b35a139-ed21-3d58-bb36-4f9473a1b020 | -5.557 | -49.0801 | 2025-08-19 00:50:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| f68ac60f-64fa-316c-aea4-b87639fee3c2 | -15.0389 | -54.8089 | 2025-08-19 00:50:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 9d906296-6f79-3314-9270-a901d9896e36 | -9.1895 | -59.6364 | 2025-08-19 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| d981c539-65e6-3841-8b33-068036739158 | -6.9712 | -43.6066 | 2025-08-19 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 102.7 |
| fa385ccf-4f27-3d90-b167-cd8c974c4f04 | -5.7887 | -43.6134 | 2025-08-19 00:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| b8952e86-cd95-38a5-ae0a-d0d93a93bd1d | -6.9524 | -43.6083 | 2025-08-19 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 30bd02fa-85ec-326f-a308-54245ef9ef16 | -9.1894 | -59.6558 | 2025-08-19 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 6a32f13e-03f6-35bb-a550-25ad7771d157 | -6.9527 | -43.585 | 2025-08-19 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 8aaf9bac-9960-3789-beb3-9ac8ab4a6b70 | -6.9715 | -43.5833 | 2025-08-19 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 0a4ae327-0f78-3489-949a-b5e229b041a6 | -16.4857 | -45.0939 | 2025-08-19 00:50:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 358.5 |
| 28f5a416-bc7b-3450-8137-b57a0a32000f | -5.5785 | -44.0914 | 2025-08-19 00:50:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 6ca229c3-042a-334e-ba72-68c10525eca9 | -5.5571 | -49.0587 | 2025-08-19 00:50:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 61cb2c35-106a-3132-94fa-aefb639a106e | -3.9819 | -42.5396 | 2025-08-19 00:50:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 117.8 |
| 8ec5ff6f-297d-3d50-9299-522071ade832 | -5.5384 | -49.0812 | 2025-08-19 00:50:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 50477338-2a06-3e40-859e-5e51f682e8a0 | -16.4851 | -45.1176 | 2025-08-19 00:50:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 4337484a-07a1-36bf-89d7-9790bf6459ab | -14.9812 | -54.7951 | 2025-08-19 00:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| cef9eec3-43dc-342b-b07a-ace09368c01d | -6.9336 | -43.6101 | 2025-08-19 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 9efad407-a2ae-309c-9228-17468083e062 | -7.2602 | -50.1613 | 2025-08-19 00:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 909053d8-66a3-36d1-849f-30e663d8f6b1 | -8.9788 | -60.4964 | 2025-08-19 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 1879d9e4-9462-394f-99f9-bb48c54d22c9 | -12.6536 | -45.8082 | 2025-08-19 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 86007765-5fc5-3004-8803-1a1054766042 | -16.4653 | -45.1218 | 2025-08-19 00:50:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 5444da7d-e1c1-350e-aeb1-25c11871bb07 | -3.982 | -42.516 | 2025-08-19 00:50:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 244.7 |
| 8780f529-5214-32c8-9683-403454b83cd8 | -6.9339 | -43.5868 | 2025-08-19 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 3cb36308-adf7-3471-8a99-29026d5657aa | -11.8702 | -51.578 | 2025-08-19 00:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 5ee6f975-ae1a-323b-a718-b5a705a29c72 | -21.8869 | -48.1841 | 2025-08-19 00:50:00 | GOES-19 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 0b822838-93bf-3689-a21f-d1276c52317b | -13.0162 | -56.8378 | 2025-08-19 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 2065922c-2820-37d7-88d5-05b6d0ab08fa | -14.9809 | -54.8158 | 2025-08-19 00:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 2fe3d6cb-4245-3066-89ec-fb312803bdd4 | -12.9778 | -56.8614 | 2025-08-19 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 59d83c31-56bc-3194-986c-2ec10dd181f1 | -4.92495 | -43.24694 | 2025-08-19 00:50:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 44.2 |
| b10faed0-a255-3346-a88a-e59cd770b173 | -6.93674 | -43.58813 | 2025-08-19 00:50:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 8f373738-853b-3e7e-9cee-fd09468d340b | -6.92144 | -43.59072 | 2025-08-19 00:50:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 32.5 |
| b06762f3-df9a-335e-9a61-fb06ffba8857 | -5.86876 | -48.11262 | 2025-08-19 00:50:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 2cdeed6e-8352-3fc5-9196-6a39d8619bb9 | -9.07825 | -60.41602 | 2025-08-19 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 44c4f9a7-6151-3641-9387-187af4a0e6b7 | -13.15628 | -54.92937 | 2025-08-19 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 01d29d04-adb0-302e-96fe-4cc15bc4060b | -7.21732 | -49.60863 | 2025-08-19 00:50:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 5cedb06f-0bc1-39de-a09f-d879c6757347 | -4.42469 | -47.75801 | 2025-08-19 00:50:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| ed44afc8-5bd3-3f79-a45d-f65e5e82f0bd | -6.92608 | -43.62049 | 2025-08-19 00:50:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 25.4 |
| e9173554-22fd-303b-a915-976d7eb4f151 | -11.86598 | -51.58802 | 2025-08-19 00:50:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4c1e2ddf-5d71-3b24-bbdb-8c894b1b5aa7 | -5.54318 | -49.07504 | 2025-08-19 00:50:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 39eccdc9-8bc0-328d-a65a-263ab6ca5b20 | -9.18152 | -59.66131 | 2025-08-19 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 1ecbb513-d1e5-3c73-83cb-291323a98019 | -6.96855 | -43.60836 | 2025-08-19 00:50:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 169.4 |
| af6e45d4-91b0-3082-a6d0-41f3c22dacca | -9.57354 | -47.41498 | 2025-08-19 00:50:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 5f515da6-e6e7-3d16-b8d8-6169160e2c88 | -7.26369 | -50.17175 | 2025-08-19 00:50:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| f680bc11-adea-3ac5-b462-41a8127644ae | -4.43338 | -47.75111 | 2025-08-19 00:50:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 6c1a13ae-3253-3bd3-9d30-a2a7e08a815d | -6.94845 | -43.58087 | 2025-08-19 00:50:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 39.6 |
| eb0cc5d9-b530-3c86-8df3-32b66605febc | -11.8635 | -51.56999 | 2025-08-19 00:50:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 51.1 |
| dd1feaab-1793-3e70-9440-f24d16238377 | -12.9821 | -56.85725 | 2025-08-19 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 1ca07d7b-d7eb-3b83-8f64-325f81d2037a | -10.36203 | -49.92885 | 2025-08-19 00:50:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 10801344-6d3a-31b6-9b79-5e67b80d0fc2 | -8.97818 | -60.48781 | 2025-08-19 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 6c967bc6-1976-317c-bfde-31a7ef894250 | -6.19189 | -53.51972 | 2025-08-19 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b4f11643-6d1c-3de7-bae4-1a1c880adf49 | -9.33984 | -48.51334 | 2025-08-19 00:50:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8aa7aa8f-8ed1-356b-959c-df8696ee9790 | -7.26936 | -50.16446 | 2025-08-19 00:50:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| c507ee5e-2c17-3d23-bbb0-45c1071d739a | -3.97124 | -42.53432 | 2025-08-19 00:50:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 49.4 |
| d0a08d9e-dcfc-31ed-b0fc-02a42ccdda89 | -13.14613 | -57.15111 | 2025-08-19 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 1aadd86f-3624-3bc9-94c0-e6ffece7aaf0 | -9.19553 | -59.62819 | 2025-08-19 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 16b30ae6-4d73-3f6c-8901-90635c61082f | -3.98775 | -42.53715 | 2025-08-19 00:50:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 296.6 |
| ce346d3d-7a0b-3bbb-88a8-92b288617628 | -3.97032 | -42.53978 | 2025-08-19 00:50:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 35.7 |
| 39986fed-9ef2-35f2-9b5a-2347063a87bd | -9.07888 | -60.44059 | 2025-08-19 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 8dde7309-6d38-380b-b220-a5c0938dbe2e | -7.25439 | -50.1732 | 2025-08-19 00:50:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 65e11254-a7b8-348c-ae29-0867d5ab863d | -8.82672 | -52.04416 | 2025-08-19 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |


[Clique aqui para ver as próximas entradas](README8.md)
