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

## Dados Diários - Página 236

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ce04c5e-1e32-3478-a039-a80fa9812646 | -11.075 | -44.0768 | 2026-10-09 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 2a67d899-f5dc-3c92-a23e-a637b04563b7 | -10.9953 | -45.4068 | 2026-10-09 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| bb31d006-8ac4-3929-bff4-9f5ba4783682 | -8.911 | -45.229 | 2026-10-09 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 4c49db9c-b0df-3e62-bfd5-e0920d81938d | -11.619 | -43.6196 | 2026-10-09 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 154.5 |
| ad4ec75c-96c3-3e6a-890c-46c61dd0ced6 | -11.2259 | -45.3064 | 2026-10-09 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 196.5 |
| a9797344-6e00-3813-aea8-f0f9498a01f8 | -8.9775 | -45.9023 | 2026-10-09 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 2f61f609-f360-3840-b980-99dcd9f8f233 | -8.9299 | -45.2269 | 2026-10-09 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 7dfb0a8c-29ef-34b3-95d8-6d51d44cf078 | -10.4334 | -47.3046 | 2026-10-09 12:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 5c4b1c3a-d4c6-3d2f-8c44-ecc7cd48ec39 | -8.9113 | -45.2062 | 2026-10-09 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 98ccd9eb-5d2d-36fa-afc6-02df7edd7a13 | -11.0558 | -44.0796 | 2026-10-09 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 828bdd1c-129f-3dea-8022-9a6137fcf8b6 | -18.0949 | -42.2719 | 2026-10-09 12:50:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.8 |
| fe0642b4-b194-33ab-90e2-c20eadd08eb7 | -11.2068 | -45.3091 | 2026-10-09 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| ddaccc77-f344-3f6f-85df-f6b86d27c8d4 | -11.6557 | -43.7083 | 2026-10-09 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 193.7 |
| e4a7d23e-5489-3b5d-a19d-6ddc28471310 | -8.9684 | -45.177 | 2026-10-09 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 041292ba-3f2d-3c20-9abb-71409f7d4c0c | -11.9865 | -43.4671 | 2026-10-09 12:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1704.4 |
| 68cc4405-cbfc-38f4-bad9-77a0966cbd1d | -11.9861 | -43.4908 | 2026-10-09 12:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1148.1 |
| c87922fd-6d34-3682-9ed0-36577ac0d3ed | -10.4901 | -47.3201 | 2026-10-09 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 350.0 |
| 1579e2b3-5040-30bd-977c-64028c6bd22e | -12.2302 | -44.8126 | 2026-10-09 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 2a116dd5-efd0-3962-82a3-b62f12d494fb | -18.0957 | -42.2467 | 2026-10-09 12:50:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 102.2 |
| b0005571-426f-35ff-9754-fb8a69ab5145 | -11.245 | -45.3037 | 2026-10-09 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 352.3 |
| ca3f9625-c464-3243-a46f-c3510094c77d | -16.1136 | -43.4052 | 2026-10-09 12:50:00 | GOES-19 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 100.8 |
| ae628df9-a5be-3d22-b492-47c2071cb18e | 4.4458 | -60.98127 | 2026-10-09 12:55:00 | TERRA_M-T | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 6e4f3856-3b7f-3634-bdc1-c08ef1d79ef3 | 3.33714 | -60.90739 | 2026-10-09 12:57:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b6ae1194-6044-302a-a4c5-43ff71f0d832 | -3.60243 | -61.62051 | 2026-10-09 12:57:00 | TERRA_M-T | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e40d5e6e-dea5-363d-a56d-70ca4b1a06e9 | 0.06851 | -59.36427 | 2026-10-09 12:57:00 | TERRA_M-T | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| cbf69bd7-af6b-3a82-886c-f2c9142866ae | -3.44903 | -59.54804 | 2026-10-09 12:57:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 19.0 |
| f75ffa02-80ea-32b9-8c09-09fcfdf442d9 | -4.79685 | -56.14179 | 2026-10-09 12:57:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 802d6168-6dbf-3dbf-a71b-a96d1e6713b1 | -2.91273 | -57.20976 | 2026-10-09 12:57:00 | TERRA_M-T | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| a4ae601b-0861-361b-8bd1-c69561772f85 | 3.33541 | -60.89574 | 2026-10-09 12:57:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 36.5 |
| c65d2e04-feeb-3176-90c3-868646e02224 | -0.81405 | -60.50057 | 2026-10-09 12:57:00 | TERRA_M-T | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 04158f19-539b-390a-9739-54623941e481 | 1.21627 | -59.97504 | 2026-10-09 12:57:00 | TERRA_M-T | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.2 |
| eff080d0-ffef-39c3-8c84-591587e8ed5d | -4.74902 | -55.64909 | 2026-10-09 12:57:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 31db9603-a88b-325a-91a1-2949c32a435a | -0.76199 | -60.45813 | 2026-10-09 12:57:00 | TERRA_M-T | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 43561cbe-77b5-3f19-9421-e877fba5c36b | -2.73822 | -57.4859 | 2026-10-09 12:57:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| d7c6e9b0-502b-3c0b-ba62-d8d9696b5049 | -3.53833 | -59.56553 | 2026-10-09 12:57:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| eaff5f38-70aa-34b3-a3ba-53e7945cab64 | -3.35506 | -59.47091 | 2026-10-09 12:57:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 6b341e7b-b1d5-35e1-be3c-3d14b172a4cd | -3.56398 | -59.4717 | 2026-10-09 12:57:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 19.3 |
| a8ad27fc-e908-3b4f-a1f0-f0614cb0b40f | -3.90035 | -55.8842 | 2026-10-09 12:57:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 72d26600-4bd9-3112-8038-8be91c5a6e2a | -3.16615 | -58.6316 | 2026-10-09 12:57:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| e0653ba0-bd8e-3808-a25f-984d6eccc70c | -1.88067 | -56.31176 | 2026-10-09 12:57:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| c0d5e134-92dd-38ee-82a6-88caa3e6f084 | -3.90417 | -55.89151 | 2026-10-09 12:57:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 4e3f6c46-c4a8-38ca-b7b5-8c60a08ddd41 | -3.77611 | -58.58782 | 2026-10-09 12:57:00 | TERRA_M-T | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| f640ecb3-a6da-3f68-bd24-c4b028f32d22 | -4.74557 | -55.69308 | 2026-10-09 12:57:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 7b9fbaa0-24cd-3047-9faa-9bb4c2952a95 | -3.35247 | -59.49004 | 2026-10-09 12:57:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 2c24b844-21f6-36da-9595-d58800f9cf03 | 2.75814 | -60.04252 | 2026-10-09 12:57:00 | TERRA_M-T | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 55cf17cc-bf69-346c-86f0-5822197c9dde | 1.68461 | -55.61114 | 2026-10-09 12:57:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| ae7334fe-7706-3262-98fc-d72fb79e8a7f | 2.83087 | -61.29585 | 2026-10-09 12:57:00 | TERRA_M-T | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 21.7 |
| d50cc260-a695-3e62-8113-291690b17abd | 0.4466 | -60.54087 | 2026-10-09 12:57:00 | TERRA_M-T | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 5bb905d4-21ec-3783-935b-9e0daab5d33c | -1.32377 | -55.44628 | 2026-10-09 12:57:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 50bc39ba-4f61-314a-8364-5d90472d64ef | -4.75048 | -55.65405 | 2026-10-09 12:57:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 8351872a-1c1a-3d34-a69e-5f57ceaddad7 | -2.39288 | -57.89661 | 2026-10-09 12:57:00 | TERRA_M-T | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 26.9 |
| d32d0d33-4624-3395-946a-409482210993 | -3.17155 | -58.62557 | 2026-10-09 12:57:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| c42a34f9-81c7-3ac0-9bc6-2e5ec95627aa | -4.7439 | -55.68764 | 2026-10-09 12:57:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 183.1 |
| 52a72d39-51ef-3f6f-befe-24de5d0b3c92 | -1.32839 | -55.45224 | 2026-10-09 12:57:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 0d00e07d-2e34-3814-8254-2f63c584b60e | -2.50262 | -56.06057 | 2026-10-09 12:57:00 | TERRA_M-T | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 9008f5a3-461f-3bee-8088-9bfbb88dd1a9 | -12.24691 | -57.09963 | 2026-10-09 12:59:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 116.7 |
| ae76130c-bd9c-32ac-baed-731ddac6cab5 | -8.52614 | -67.0276 | 2026-10-09 12:59:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 8779c7c8-34ea-36a5-b27c-c14cddaece13 | -12.22946 | -57.09816 | 2026-10-09 12:59:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 217.4 |
| 2e26001f-720e-36a5-9aed-fa1775814518 | -8.61834 | -67.02863 | 2026-10-09 12:59:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bef7e857-4e0d-3d31-8ad9-a895624acb7a | -10.38595 | -68.90307 | 2026-10-09 12:59:00 | TERRA_M-T | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 0ebfbfe8-4f0f-38b2-b364-45f2d14bc961 | -9.25561 | -60.88541 | 2026-10-09 12:59:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| dc870e86-9ff9-3691-bcc4-285d84b1fa92 | -11.98505 | -57.58563 | 2026-10-09 12:59:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 40.6 |
| b5e9a9ec-188c-33b1-83b0-dd41e4f8cae6 | -8.69681 | -62.41555 | 2026-10-09 12:59:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 23.0 |
| e4a5eece-c00a-3761-a3e9-7284b6f0c34d | -8.70123 | -62.40849 | 2026-10-09 12:59:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 5478304f-f1d0-3f44-a2ca-4483fcbb5ba9 | -8.54423 | -66.98207 | 2026-10-09 12:59:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 36aa5d07-583f-3dc6-a325-3479a3702745 | -11.75181 | -61.0644 | 2026-10-09 12:59:00 | TERRA_M-T | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 5af1b016-ffe3-39b3-94be-1aa80b1cf2ee | -11.53874 | -56.80906 | 2026-10-09 12:59:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 32.0 |
| c1921a90-4b59-3207-972a-91678deba34d | -11.97616 | -57.61576 | 2026-10-09 12:59:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 06dc72a8-ab1a-3ad1-93c9-5307fb073186 | -7.57377 | -61.5396 | 2026-10-09 12:59:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 0730931b-3860-3c28-8af8-03d61fadabec | -10.61143 | -60.46917 | 2026-10-09 12:59:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 152.4 |
| fbff17a8-edbb-389f-a5ae-6219893250a1 | -9.28942 | -64.54346 | 2026-10-09 12:59:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 27.6 |
| f775284a-0cb6-3ddf-9773-65d5bfb4cd63 | -8.52487 | -67.03645 | 2026-10-09 12:59:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 997482bb-5cb8-378d-b6f6-79b920977ef0 | -10.60873 | -60.47552 | 2026-10-09 12:59:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 96850862-2dd3-3c34-9457-f722cdc5a523 | -9.14371 | -67.9395 | 2026-10-09 12:59:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ba899b3c-4e6c-3efe-ae4c-d963e236d7d3 | -8.84308 | -61.4639 | 2026-10-09 12:59:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 4bc62f8e-540d-3d02-b599-3c769ca333d7 | -11.98019 | -57.57838 | 2026-10-09 12:59:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 5a0cd662-34a8-36af-8663-c364a3c92dd1 | -7.59267 | -64.55128 | 2026-10-09 12:59:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 383d35e2-a80a-3726-a267-9e2d40bc8201 | -5.30112 | -60.08912 | 2026-10-09 12:59:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| d1d95aab-7989-321b-bf9a-055e780e50b6 | -4.65488 | -61.14047 | 2026-10-09 12:59:00 | TERRA_M-T | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5e0b0ed0-572d-36c9-96c0-68a91fb4cd82 | -6.49065 | -62.85696 | 2026-10-09 12:59:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 93762605-60fc-3c06-83e8-417b7c4fa519 | -9.96322 | -63.09254 | 2026-10-09 12:59:00 | TERRA_M-T | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f20e7a68-3051-365c-927d-86b01a38c43c | -9.34126 | -65.57569 | 2026-10-09 12:59:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 22e46389-fc73-3ccd-b075-1e0074da563c | -11.53913 | -56.81625 | 2026-10-09 12:59:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 0dfc4d89-17ca-31e3-a79c-a0927563a8df | -12.76195 | -57.71622 | 2026-10-09 12:59:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 1051937b-54fd-3b3f-8200-765060c97e03 | -8.70766 | -62.41693 | 2026-10-09 12:59:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 3f1cc4d9-9b6d-3900-90b9-16c2b8d9cdb5 | -12.08723 | -57.07036 | 2026-10-09 12:59:00 | TERRA_M-T | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| f748ef2a-f0f1-3473-9121-912d3149cf74 | -10.62182 | -60.4772 | 2026-10-09 12:59:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| fe5fed49-5d46-3427-b779-f2ccc8d11b24 | -10.60879 | -60.49022 | 2026-10-09 12:59:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| e4884a8c-d7e8-3e7a-8e2d-4e5683ef3d7f | -10.38739 | -68.89344 | 2026-10-09 12:59:00 | TERRA_M-T | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 7.4 |
| cf4d166d-c349-38a1-808a-d4f3a60f66c9 | -9.25318 | -60.87859 | 2026-10-09 12:59:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| a8cbd4a1-245d-3374-a7b5-ede639b5b338 | -12.24847 | -57.1069 | 2026-10-09 12:59:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 9ac0a3d8-fdd8-3cbc-9f10-85bdbe587848 | -12.23104 | -57.10532 | 2026-10-09 12:59:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 218.2 |
| 4865fc80-132d-36e1-b77f-8b853858ecf3 | -11.5993 | -43.6462 | 2026-10-09 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 4fa1b659-8f51-386b-ae48-c283332c708f | -11.4131 | -46.6671 | 2026-10-09 13:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 150.8 |
| dc2dbdd3-2e1c-380e-8cda-bec6ec3eeb6c | -12.0063 | -43.4402 | 2026-10-09 13:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 348.8 |
| 3ccb65af-2d4f-3bcc-bd83-a1883937062e | -11.9865 | -43.4671 | 2026-10-09 13:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1702.2 |
| f1617ab3-1e3f-3aac-956c-c74b2618219d | -12.2346 | -57.1071 | 2026-10-09 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 0114381d-f3d4-3795-a1e6-1dd1a6fdac39 | -11.2475 | -46.3058 | 2026-10-09 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.1 |
| d55f5c7c-d583-30ea-9375-11d22676f252 | -9.1297 | -45.8179 | 2026-10-09 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 10401e96-9c0d-3e2a-9174-d156557a0536 | -11.1242 | -45.6865 | 2026-10-09 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 177.7 |


[Clique aqui para ver as próximas entradas](README237.md)
