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
| 83922dc2-2751-34ae-91dd-9d4a1cdcdcb4 | -2.47728 | -56.09739 | 2026-10-06 00:20:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 4cf36d1a-df84-3215-a7ba-70b1d2763203 | -1.10428 | -54.15599 | 2026-10-06 00:20:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| dc8c04ba-3322-33c7-b168-c4bda0912a84 | 1.87322 | -55.74831 | 2026-10-06 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 4433cada-55e5-3fff-8afa-bf68ea65622a | 1.7813 | -55.5513 | 2026-10-06 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| df6f79eb-0d3f-3b23-8e61-0b298a5daec1 | 2.47019 | -50.83941 | 2026-10-06 00:20:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 0a66c1a2-6e04-381b-8c1c-d3ffbc23ebbd | -1.09045 | -54.12133 | 2026-10-06 00:20:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| f0beef04-2fdc-34cd-9d0e-18d297fabf67 | 0.54196 | -50.76254 | 2026-10-06 00:20:00 | TERRA_M-M | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9ef2185b-5130-3bca-b70f-0a0b2d815692 | 2.26644 | -50.82475 | 2026-10-06 00:20:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a69593d1-e926-35f7-a94f-180b11ef1bbf | -1.9245 | -52.67822 | 2026-10-06 00:20:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fc4e675f-5271-3720-82a6-4d2236ac11f4 | -2.08714 | -55.12528 | 2026-10-06 00:20:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a19249f2-7dee-3531-bd2a-decf01f21cef | -1.08922 | -54.11236 | 2026-10-06 00:20:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 54352f4a-d6b2-3ce5-b8d8-0207929e6410 | -1.05407 | -53.58955 | 2026-10-06 00:20:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a49f550d-5b81-30b1-ac12-0845256add45 | 0.54156 | -50.75602 | 2026-10-06 00:20:00 | TERRA_M-M | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 12.4 |
| da478c6f-b630-346f-8ac9-0298e9b9ca4c | 1.03513 | -59.45382 | 2026-10-06 00:20:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 849d423f-6be2-3605-aa16-a9a264f7fcda | -2.15511 | -60.0032 | 2026-10-06 00:20:00 | TERRA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 10c21416-277a-388b-8522-05b2b7b873cb | 1.86081 | -55.77334 | 2026-10-06 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 2959ae16-b45f-3d40-bc41-b6c6f40ec237 | -2.04916 | -56.88208 | 2026-10-06 00:20:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 0aa75b01-79fd-3ccb-8092-960659f91585 | -1.10305 | -54.14703 | 2026-10-06 00:20:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 70c2e1a4-d6ee-34ef-8884-e22f5ce152b5 | 2.45877 | -50.83782 | 2026-10-06 00:20:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a516dc65-099e-36f0-a73c-f49b01c6d04d | 1.56466 | -55.98198 | 2026-10-06 00:20:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1ffd0bcd-7402-3c9d-81b8-e5151ce5ba68 | 1.7913 | -55.54377 | 2026-10-06 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 68f83128-5f94-3ac0-bd7e-917a8f8bbc85 | 1.8177 | -55.54745 | 2026-10-06 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8b08b49d-bfe4-3eba-90f8-d603d4b2b019 | 1.7901 | -55.55252 | 2026-10-06 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 4e02fb39-daa3-33d9-adbd-8aa33bbe4a15 | -3.3906 | -58.1953 | 2026-10-06 00:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 7b4af385-47e2-30fe-b85d-6912f8176e57 | -2.8714 | -54.1318 | 2026-10-06 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 51e0358f-06b5-39d1-88d8-9e90ce4c223b | -3.0191 | -53.9071 | 2026-10-06 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 42c81521-6403-3a7b-978b-97507426efa0 | -2.7696 | -57.6847 | 2026-10-06 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 21f0277b-8353-338c-ae2b-cc69998dc711 | -2.7879 | -57.6843 | 2026-10-06 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 29090637-67b5-3e43-bfc6-d429fadf5018 | -9.4767 | -64.0323 | 2026-10-06 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 327736ab-1673-3ca9-aa87-64b2038c8bd7 | -2.8897 | -54.1313 | 2026-10-06 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| c3940b1f-75fc-3006-b8c5-867de8d41546 | -8.7036 | -45.2061 | 2026-10-06 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 8d657950-8505-329f-8f5f-e168d25e7fe6 | -9.7745 | -36.395 | 2026-10-06 00:40:00 | GOES-19 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 67.8 |
| 2d21ff3c-a5e2-3d49-8d36-9afd4154e245 | -2.7796 | -54.0937 | 2026-10-06 00:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 628b8288-ff9c-3de9-81dd-7695583027d6 | -5.8509 | -45.0318 | 2026-10-06 00:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 259c06a0-85cf-3b0c-8d9c-a1591ff23ea5 | -8.6847 | -45.2081 | 2026-10-06 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 5394df20-0091-3df3-be4b-d0fe405f229e | -2.7879 | -57.6649 | 2026-10-06 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 6650d6ce-bfe1-3e56-a496-5396c828dc4f | -9.7312 | -65.0944 | 2026-10-06 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 5ed3a3d7-8e66-3b99-8ac9-387268406df2 | 0.4465 | -60.5442 | 2026-10-06 00:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 55.1 |
| d27d26da-6b32-3b02-b17c-c68b0eeee496 | -11.6946 | -43.6787 | 2026-10-06 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 203.1 |
| ac750a33-5aff-3866-9ceb-00e504c74546 | -2.8897 | -54.1514 | 2026-10-06 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| c477d01f-7ca2-340b-a492-b94a3a2681bf | -9.7313 | -65.0757 | 2026-10-06 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b6f2d8bf-e314-33e0-b461-11d8c2123eb5 | -2.7696 | -57.6653 | 2026-10-06 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 7ef62511-eac7-3eac-9ae5-859819dbadfb | -3.1608 | -50.4347 | 2026-10-06 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| f1ddc4c7-b273-3233-a2e7-ca198ed18939 | -3.6731 | -55.9622 | 2026-10-06 00:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| d03b57f2-3ce9-3a5c-adb0-6915a807eb36 | -3.0192 | -53.887 | 2026-10-06 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 131.3 |
| b82cb220-7031-3d61-ac2b-e8e957916d9d | -8.7033 | -45.2289 | 2026-10-06 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 4bdbe6e1-49ac-3b20-8cea-dfc8529986c1 | -3.3723 | -58.1957 | 2026-10-06 00:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 99f7b2ef-dd67-33d3-8e3d-61e8c74166a6 | -2.8713 | -54.1518 | 2026-10-06 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 162.8 |
| 379a9ff2-afa6-3d27-8a2b-3deeb1f24edb | -11.6951 | -43.655 | 2026-10-06 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.2 |
| dce8674b-28cb-3e6d-a3f8-e1d29cc65baf | -5.8323 | -45.0105 | 2026-10-06 00:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| a8842e63-0eac-39d8-88e4-25047f93fc4c | -3.3905 | -58.2146 | 2026-10-06 00:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| bbafaf4b-60c7-3399-aac6-e6c08ca258a7 | 3.5647 | -61.3246 | 2026-10-06 00:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 7fa5e438-2f60-3982-82de-10165a974115 | -8.5847 | -45.6502 | 2026-10-06 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 77769d2f-9581-39db-9cb3-04f1164e774a | -3.1607 | -50.4556 | 2026-10-06 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| e0b39413-3727-3884-afd0-948caca5656d | -5.8511 | -45.0091 | 2026-10-06 00:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 30922c94-3897-32f4-b5e3-a0795655e2d5 | -2.7796 | -54.1138 | 2026-10-06 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 18102c56-0225-3e6f-a3b6-7e6698a5bb5e | -3.6732 | -55.9425 | 2026-10-06 00:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 9d9ab92e-ef7c-3aee-9383-9775305a0b4a | -3.4955 | -49.8979 | 2026-10-06 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 4d64acfb-2d6b-3b02-b972-32605dd06db8 | -9.7741 | -36.4219 | 2026-10-06 00:40:00 | GOES-19 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 75.7 |
| 54c28e68-8f6e-3817-a3ac-3851fc00eaa2 | -3.6915 | -55.9618 | 2026-10-06 00:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 119.6 |
| d93f5b17-9d16-3b0d-88a9-004ee220e451 | -3.6915 | -55.942 | 2026-10-06 00:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 127.2 |
| f770c6ea-766d-3145-9b60-2a7eb3ccfcc9 | -8.5847 | -45.6502 | 2026-10-06 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 4e04648a-da7f-374c-b189-9a160fceb2e2 | -8.7036 | -45.2061 | 2026-10-06 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 757dbcab-1de1-3e12-8ebc-6b688d23ea86 | -3.0933 | -53.7037 | 2026-10-06 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 05a4130d-0053-327f-be24-72ff16461062 | -9.1336 | -65.8627 | 2026-10-06 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| c9ca927d-16aa-3e64-b03d-a789f5e77101 | -3.6731 | -55.9622 | 2026-10-06 00:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 2ff87340-630c-3d72-8696-ce33b53a327f | -2.7796 | -54.1138 | 2026-10-06 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| bf747b12-dddf-32ef-b9cd-8bf767b87ce7 | -2.8897 | -54.1313 | 2026-10-06 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 7b32fcd3-a1c5-3c16-b3de-c4ea9d24b1d5 | -4.1084 | -49.4084 | 2026-10-06 00:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 40b1a2ea-e926-30fc-aec4-c6b947fd295e | -3.0375 | -53.8865 | 2026-10-06 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| e339fd52-7392-37a1-986f-8a395450f279 | -3.3723 | -58.1957 | 2026-10-06 00:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 7732d5c5-022d-37cf-a368-a1d9b38a6f00 | -5.8509 | -45.0318 | 2026-10-06 00:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| d8f6f13a-1571-3b99-a299-1bbe79c6c8cf | -3.0001 | -54.1086 | 2026-10-06 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 86688db5-95a9-3c1a-a6ce-b2296d96ddf1 | -11.6946 | -43.6787 | 2026-10-06 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 190.3 |
| e1ee1eae-f608-30eb-8265-26e18fc4c405 | -2.9816 | -54.1291 | 2026-10-06 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| f7c9f9ec-7775-3044-aeea-62a8873779e8 | -9.7312 | -65.0944 | 2026-10-06 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.1 |
| abc5ce4a-b1ed-30b4-b219-a6e2b240296e | -11.657 | -43.6373 | 2026-10-06 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| df236b08-4690-3b56-be4b-94c9161b7daf | -3.1116 | -53.7436 | 2026-10-06 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 4bd635b3-b742-3188-a1b6-c1a4ae1f973a | -2.8897 | -54.1514 | 2026-10-06 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 2b27bcae-89ec-36f5-9a81-1720e859ec4d | -2.7879 | -57.6843 | 2026-10-06 00:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 95.1 |
| ec7f5335-e473-3737-9f8a-0af3eac98b5f | -3.3906 | -58.1953 | 2026-10-06 00:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 652246ee-41c5-37f6-a31d-8298b196673c | -5.8323 | -45.0105 | 2026-10-06 00:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 763f7533-4a15-3f20-a820-3e2b944556ce | -2.7879 | -57.6649 | 2026-10-06 00:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 90ed22f2-d0aa-388d-8fd5-ddd7d9bb05e6 | -3.6732 | -55.9425 | 2026-10-06 00:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 131.2 |
| e663dc8a-11e5-3005-9907-b0a8f3b259e4 | 3.5647 | -61.3246 | 2026-10-06 00:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 3b255820-f151-3d80-b8e9-b4cd2b20f36c | -3.0192 | -53.887 | 2026-10-06 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 2907bad2-03d9-3c0f-b48d-8a0fe8298816 | -3.1115 | -53.7637 | 2026-10-06 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| b3286905-a95f-3bcf-9d11-250488d1e887 | -3.3722 | -58.215 | 2026-10-06 00:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 2ae12cf7-53ef-3c3e-90fc-c55e699cd0b8 | -2.8714 | -54.1318 | 2026-10-06 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 137.4 |
| 3d3afa72-89cc-30d5-9018-a181a7a29678 | -2.7796 | -54.0937 | 2026-10-06 00:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| ac909b0b-7bd7-34a4-ac41-81ffea9e974b | 0.4465 | -60.5442 | 2026-10-06 00:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 8958f0ba-1ded-3315-b0ac-e79abdc6d719 | -8.7033 | -45.2289 | 2026-10-06 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 65d476ae-aef3-39c8-9cb9-45184174f236 | -2.9265 | -54.1104 | 2026-10-06 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| eab310ab-efc8-362d-ae9d-80c1212171bc | -2.8713 | -54.1518 | 2026-10-06 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 187.7 |
| 57294748-2cd6-37a4-9975-a0219f40bc7c | -3.0 | -54.1287 | 2026-10-06 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 3fa656a6-99da-330a-987f-ee9216e7b1f2 | -3.6915 | -55.942 | 2026-10-06 00:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 33eb92ff-8a07-36fa-a71a-be1f61177f68 | -9.4952 | -64.0504 | 2026-10-06 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 84c5b80b-e2a8-3430-b77f-afb4182e5d7d | -3.0375 | -53.9066 | 2026-10-06 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 3a932b07-53d8-3c8f-a6b6-9b4945cc9e4b | -3.6915 | -55.9618 | 2026-10-06 00:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| c1cbcfad-2c9b-3974-9183-df8520409431 | -3.1608 | -50.4347 | 2026-10-06 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |


[Clique aqui para ver as próximas entradas](README8.md)
