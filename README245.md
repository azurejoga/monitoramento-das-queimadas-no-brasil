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

## Dados Diários - Página 245

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2615dda9-f6dc-347e-b202-2cc2f136a0ab | -8.9495 | -71.553 | 2026-10-07 18:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 2a321374-16f3-3af3-b870-da34bea29fe5 | -12.2132 | -44.6991 | 2026-10-07 18:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| a9852fc1-4d59-3dec-872b-f66d8155b7fc | -5.9649 | -40.914 | 2026-10-07 18:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 145.1 |
| 2a78d301-49f2-38b4-92b2-d28b5f438f67 | -11.8508 | -43.5361 | 2026-10-07 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 78ee6c1d-a8c4-3d52-a2eb-e304860b5b4b | -5.7304 | -53.465 | 2026-10-07 18:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 176.9 |
| c053b937-2f65-3273-88ff-4e23125325f1 | -3.0192 | -53.887 | 2026-10-07 18:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| bc858299-e43a-3b35-b489-9de1d6655078 | -5.9838 | -40.9123 | 2026-10-07 18:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 127.9 |
| 57744b8a-05f9-3b44-8e18-c576cf1250dd | -2.9819 | -54.0488 | 2026-10-07 18:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 303.1 |
| 64e189b3-fec3-38a7-8bfc-8cabec9e143a | -7.3935 | -46.2144 | 2026-10-07 18:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 3c4ff0f6-e465-3cca-983d-c0680127d2c9 | -9.8059 | -65.0354 | 2026-10-07 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 1172e013-3c4d-3d51-8a02-4f45284ea93d | -11.8503 | -43.5598 | 2026-10-07 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 67aba944-22bc-3454-b0d4-3f345bfb66fb | -9.8245 | -65.0348 | 2026-10-07 18:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.0 |
| ee87c7c4-5886-3560-9e15-45a9820a0d18 | -2.8714 | -54.1318 | 2026-10-07 18:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 25e37dc9-75c9-3250-bdef-3f4a935c6ebc | -6.3618 | -42.5822 | 2026-10-07 18:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 44.5 |
| 6dcec202-9851-30ae-8570-4039b03e95d3 | -7.8146 | -45.5009 | 2026-10-07 18:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| d1b51947-46ed-3f3b-9436-bd7007cf074f | -9.2451 | -45.6692 | 2026-10-07 18:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| b24e8a54-aa5b-36b8-89cd-897edfa36145 | -3.0002 | -54.0483 | 2026-10-07 18:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 381.5 |
| e18322c3-2e36-3250-b1d1-6ee38d8422a6 | -2.9271 | -53.9295 | 2026-10-07 18:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 6cd612fa-a9c6-3c0e-b691-ce291cc6b662 | -9.3566 | -65.7436 | 2026-10-07 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| a5581519-6678-3b5a-8922-2faeb62b211c | 1.6937 | -55.6263 | 2026-10-07 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| b9e50dd5-b7c5-3a43-84da-0957991f36c1 | -3.295 | -53.8597 | 2026-10-07 18:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 207.2 |
| 8b983a11-1cfc-34c8-a46c-6511ae6e4bc2 | -6.9925 | -45.1223 | 2026-10-07 18:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 6ee39852-e735-399a-b441-88b13bb72778 | -6.9328 | -43.6799 | 2026-10-07 18:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 2dd7e4a8-8ea3-34e4-9088-93cff23cbf8d | -7.1827 | -52.6078 | 2026-10-07 18:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| f0409154-6aee-3ffb-9e7c-c8d8b4172801 | -11.6382 | -43.6166 | 2026-10-07 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| aca184a7-7a5c-3c5b-a2c5-eade28465bed | -10.3731 | -45.0306 | 2026-10-07 18:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 218.9 |
| 1a2fe8d3-bcec-3772-85d4-0cd2b63df3be | -9.0988 | -65.3596 | 2026-10-07 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 3202e191-f531-3fc0-bee5-fa2a02c6f3c3 | -5.7659 | -42.0389 | 2026-10-07 18:00:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 187.7 |
| c0fc9e5d-fc4d-3db2-bead-8de989fc0be9 | -2.7612 | -54.1142 | 2026-10-07 18:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 641.5 |
| 92adaef5-c07d-3a71-a835-35c87b8adc4a | -2.9633 | -54.1095 | 2026-10-07 18:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| dc7cf5af-240e-3b69-a4d4-6f759d7c4fc2 | 1.9681 | -55.8792 | 2026-10-07 18:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| c0b36627-9a6f-3027-8df9-6f9d6e900a5c | 1.6385 | -55.8047 | 2026-10-07 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| aea73404-0725-3ed4-a5d6-cd82cab1e3ef | -5.9647 | -40.9383 | 2026-10-07 18:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 226.5 |
| 3805aad7-de73-3e2c-89c1-a091ab9300bf | -3.4994 | -41.9489 | 2026-10-07 18:00:00 | GOES-19 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 121.6 |
| 7866c99e-b89d-3d36-8d5c-355f27c95c4f | -2.8164 | -54.0929 | 2026-10-07 18:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 564994b7-2b58-3c20-8bdf-b4d52cd04d25 | -9.8245 | -65.0348 | 2026-10-07 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 515c468a-3e19-3b31-8ec9-19389577040d | -5.9644 | -40.9627 | 2026-10-07 18:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 170.9 |
| d63a8a03-54c0-3be4-90df-b374f2c44ea3 | -6.914 | -43.6816 | 2026-10-07 18:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 7d861042-7524-3bbc-baa9-32c88314f076 | -5.7305 | -53.4446 | 2026-10-07 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 8ef2c370-0011-333e-aace-c11ea174ed84 | -13.3671 | -43.8742 | 2026-10-07 18:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 390.4 |
| 3bfe63b2-0870-3ac6-ae57-6a2f88eab49a | 1.6385 | -55.785 | 2026-10-07 18:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 71cd1d7e-5f5f-3165-83bc-d9b305718dc3 | -6.9328 | -43.6799 | 2026-10-07 18:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 104.3 |
| af57bd4f-07bb-32ed-bf2f-9acd7a24adb9 | -2.0447 | -54.3085 | 2026-10-07 18:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 224.9 |
| f6221313-0484-3b47-990d-98acbcbc284b | -5.6932 | -53.487 | 2026-10-07 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 750.8 |
| ce9d884e-80f3-3e8e-9064-2e8e01b5623e | -2.7613 | -54.0941 | 2026-10-07 18:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 555.5 |
| 89ac836c-dc00-3619-9e44-ca36852a9e7b | -3.0192 | -53.887 | 2026-10-07 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| e142af54-4416-32d1-afa4-6eaba94aef70 | -10.3731 | -45.0306 | 2026-10-07 18:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 281.0 |
| 501f79dc-a858-3d7d-baef-9a8dfd71f180 | -9.5469 | -64.8008 | 2026-10-07 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 5e5f6711-0b1c-39ed-9da8-55a472f6cebd | -5.9699 | -53.5953 | 2026-10-07 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| b7631a10-9c78-3b0d-8cb5-48bd2fb97472 | -9.9589 | -43.5516 | 2026-10-07 18:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 315.0 |
| 7c443d98-572f-35b4-8f83-54311a5a11a1 | -9.6591 | -69.0587 | 2026-10-07 18:10:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 2741e694-9542-3d6c-9a22-413e8feb6a5e | -9.8059 | -65.0354 | 2026-10-07 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 4adb2c82-6a55-3df3-8dbc-5aefc1e636c5 | -5.9647 | -40.9383 | 2026-10-07 18:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 284.4 |
| c23881b4-b648-31ed-ba2b-ee1e22be58e3 | -9.8061 | -64.9979 | 2026-10-07 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 278a855a-7f81-3132-91f3-9f34cbd7386a | -5.9838 | -40.9123 | 2026-10-07 18:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 159.5 |
| 6a08e3d1-8820-379d-9326-306ea1c4acd9 | -5.7376 | -45.1533 | 2026-10-07 18:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1507.1 |
| 12673d76-982b-3cc1-80cf-17350b59f33b | -11.2267 | -45.2604 | 2026-10-07 18:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 3926be9a-82f9-3ad1-bb16-6e63863d6304 | -3.0932 | -53.7239 | 2026-10-07 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 7f3de397-932e-3a62-9d7d-fbd99743d5ea | -3.1116 | -53.7234 | 2026-10-07 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| d2e533fa-3c21-38e6-993a-3805683da21c | -9.7126 | -65.0951 | 2026-10-07 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 09fbed94-014f-36c8-a89a-56952c7c84ef | -9.806 | -65.0167 | 2026-10-07 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.3 |
| e0cff285-2ecc-35f4-8baa-50142d7a3a72 | -3.1655 | -54.0844 | 2026-10-07 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 6d14b2d2-7773-3e7b-bb29-da7dd2af3ef1 | -5.9835 | -40.9367 | 2026-10-07 18:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 235.1 |
| b284f89c-3e74-36cb-9fa4-a1caa8c15775 | -3.1471 | -54.0849 | 2026-10-07 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| c8bf5bc9-2103-3af5-b4ac-07524e565472 | -7.992 | -70.5943 | 2026-10-07 18:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 6cf0a16f-cafb-327d-9da4-a11fa59a34c0 | -5.496 | -42.8178 | 2026-10-07 18:10:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 132.3 |
| 49894d7e-90be-34d6-89f5-e4d98b2c1d8d | -3.0002 | -54.0483 | 2026-10-07 18:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 521.8 |
| 339b1e56-1fff-30b1-94d4-55e6e6761943 | -7.8789 | -72.3492 | 2026-10-07 18:10:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 6dbd4b43-7e20-389e-9727-f859ffd12a1b | -9.8844 | -64.2802 | 2026-10-07 18:10:00 | GOES-19 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 3bd832f3-dfcf-3ed7-ac55-d578987ffcab | -5.7927 | -45.2626 | 2026-10-07 18:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 0b7666ef-c971-35fe-861f-98671ca4303c | -7.1825 | -52.6283 | 2026-10-07 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 0109d329-4b1f-3c15-9fbc-cc49567d9b0d | 1.7671 | -55.5859 | 2026-10-07 18:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 0c519863-aa7d-34ef-9a28-e01ca6e06b36 | -5.2473 | -50.9149 | 2026-10-07 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| fa063f5e-88e6-3db9-9510-999a08f33760 | -6.1402 | -53.0574 | 2026-10-07 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 727899bb-bfb1-36a7-98d7-eea29bf6367b | -2.9819 | -54.0287 | 2026-10-07 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 23857b54-b7c8-382f-b03e-62345982bbc5 | -9.9205 | -44.8124 | 2026-10-07 18:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 249.7 |
| c1f9b738-2c61-3fba-bd5f-62df5d1c8469 | -3.8081 | -40.4608 | 2026-10-07 18:10:00 | GOES-19 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 116.7 |
| cfe817df-ee86-37f3-a92e-e56fb14f2492 | -6.8292 | -39.5472 | 2026-10-07 18:10:00 | GOES-19 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 104.1 |
| a0aa3e4b-4578-383f-a46f-1a259f4ccf8d | -2.7613 | -54.074 | 2026-10-07 18:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 181.8 |
| e6d7a30e-55a7-3c9c-867e-53a805dde60b | -7.3085 | -73.0269 | 2026-10-07 18:10:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 85f6daaa-d6fc-32b4-a497-523a06385911 | -9.8246 | -65.016 | 2026-10-07 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.2 |
| b19b986a-64b1-356f-8ea3-b221f2686786 | -12.2132 | -44.6991 | 2026-10-07 18:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 457f4c7e-d0a9-3b17-b861-d97ea944ceb9 | -7.3935 | -46.2144 | 2026-10-07 18:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 222.6 |
| d1925651-0890-3279-97fe-b061dc1b1d6a | -2.9271 | -53.9295 | 2026-10-07 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| fd12015f-6aca-3dcc-b333-6043bce6868d | -6.6037 | -53.0321 | 2026-10-07 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 181.4 |
| b60eface-82c6-38cf-bb42-36419e87abfe | -9.0988 | -65.3596 | 2026-10-07 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| c0e2f291-2712-3885-9bf3-93095be55fc5 | -5.9702 | -53.5547 | 2026-10-07 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 74016d42-fb2e-321f-bb2a-1175050961fe | -9.5124 | -46.8534 | 2026-10-07 18:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 12cb9075-b56e-3132-affa-8bb274914f5c | -8.2184 | -46.3396 | 2026-10-07 18:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 826613ca-52d1-3339-8ee0-c753067c3399 | -4.1367 | -54.917 | 2026-10-07 18:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| ab54aeb3-dd16-3b88-80a9-87febb886b80 | -3.4762 | -50.0883 | 2026-10-07 18:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| c3b8acd0-ae7d-3f34-87fa-c34c6856a8ac | -3.203 | -53.8823 | 2026-10-07 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 3d43214b-69cd-3975-872f-bafdef642aa7 | -3.5684 | -54.4946 | 2026-10-07 18:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 539d71f1-3882-3c45-bf8c-b47bec91ee75 | -9.3566 | -65.7436 | 2026-10-07 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 9135d5c2-af5e-3603-9961-54514b8b3040 | -9.5468 | -64.8196 | 2026-10-07 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.6 |
| ee39e96a-52db-3dac-956a-882eb6994ef6 | -3.295 | -53.8597 | 2026-10-07 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 151.4 |
| 36d43912-04d1-3eaa-a085-3b83185b111e | -3.13 | -53.7229 | 2026-10-07 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 9d15fe60-645e-3cb9-b978-acb165cced5f | -9.5425 | -65.6815 | 2026-10-07 18:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 118.2 |
| b6c25abf-12d3-3417-94b7-76e30e07db6c | -12.0457 | -43.3864 | 2026-10-07 18:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 0dcd5d7a-f82e-3c08-ab8c-5645566f47fd | -11.7362 | -43.5068 | 2026-10-07 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.5 |


[Clique aqui para ver as próximas entradas](README246.md)
