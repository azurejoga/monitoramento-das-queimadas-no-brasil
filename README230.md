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

## Dados Diários - Página 230

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76ff441b-8841-3e07-8790-51c6d4373285 | -2.49501 | -56.1538 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| d10164f8-9da9-3d5f-8129-bccc6526add5 | 1.73373 | -56.07445 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| a9812747-f4dd-3ec7-8460-6c47707de11c | -2.13995 | -54.4544 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e9a406ff-7960-35ff-a65e-4157f2085111 | -3.50384 | -54.64294 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f37b5740-be0d-3a28-9b43-cbd960fb7ec2 | -3.28395 | -50.4368 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 4256ce0b-b0e7-3b8c-aa42-45dd4bd0b7d2 | -1.78429 | -55.03401 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 76e0d4e6-f15c-31e7-8577-22090f4e05da | -3.08021 | -54.28298 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 768cb91b-ce1f-3b36-806d-f3ca61beaa88 | -3.28749 | -54.04997 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 705e7b75-5406-3247-9e13-276e86d1869b | -2.97946 | -54.05476 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| adc7b080-c80c-34c1-8d9b-e4eaeb96409e | -4.7651 | -55.72488 | 2026-10-07 16:39:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e5c84e8a-cb36-3ec7-bd0c-c2fef8775b6a | -3.01434 | -54.06696 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 14572990-5403-3eb5-804c-e8c76c5728be | -3.29242 | -54.04585 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 161.7 |
| c005fae7-fde1-3f1f-b6e9-ece1cfb75a2d | -3.08278 | -54.30076 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 18f784b1-f6cd-321b-9be7-b23944abac02 | 2.32845 | -50.87699 | 2026-10-07 16:39:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 8a7fb055-b395-32db-a28f-c08ec842bebb | -2.84135 | -54.06863 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b4fb6f75-d3aa-3b33-97e2-14008886a5cd | 1.06473 | -52.54424 | 2026-10-07 16:39:00 | NPP-375 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 596b4ab1-4854-3f26-99b4-2030fb583667 | -3.67546 | -55.94809 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 515e22a7-446f-3984-9418-06a7156db459 | -3.03151 | -53.90852 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| d26c7e5a-7c04-3d1a-a89b-79c787eba303 | -3.05459 | -54.14404 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7a522829-0c73-3415-a804-3f9eb64fb966 | -1.29047 | -54.5588 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5f86d662-4aaf-3378-b688-680c38b4c1a6 | -2.94885 | -54.19664 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| dcee9c84-0c8c-3a2a-ae5a-003a53a2984f | -3.27064 | -54.66285 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 2d2e56e6-f022-38a4-aed7-e0848a9355e8 | -3.58331 | -54.65852 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 6c63bd23-b062-3541-a2d0-a5205df55df7 | -3.69775 | -50.6692 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 03dc2c65-1bcf-3f5f-b8a4-1fb07b4285f2 | -3.56394 | -54.48474 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 22a135e1-1b2c-39d9-894a-4f908a053b91 | -3.53208 | -54.63876 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 17701fc6-ab19-3ec8-87fb-b8c87c5e3742 | -3.54315 | -54.49916 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1ab6ae63-2683-3eec-b650-8d9bddb830de | -2.49749 | -58.06984 | 2026-10-07 16:39:00 | NPP-375 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8c1b696d-7d7a-3c74-80fa-4f4df0a5f7f0 | -3.86359 | -55.99454 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| adcf1047-7359-3338-b952-7745659ac872 | 1.62286 | -55.77559 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cb0e0e55-cf9e-34bb-bbf4-05e1cdd8876c | -1.78556 | -55.02214 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dfc7fa4a-e1a7-303a-b4f9-28e86ff57cfd | -3.09169 | -54.2849 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b825b32f-5347-3a9b-8289-2c5ac91a3447 | 2.18468 | -55.93025 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b1047e1e-7399-33ef-85c6-9fdd43d8ebc6 | 1.71227 | -55.61403 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 89196d20-949d-38c0-a7d9-4843ae3c194a | -3.69027 | -55.48725 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 264eac5b-a760-38d5-a1a8-95bca3e04e9f | 1.90063 | -55.70144 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 51bba96c-80c2-34be-8ed7-5e28ad8eff71 | 2.11523 | -50.8335 | 2026-10-07 16:39:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 33612320-c7ab-34e2-98ff-697f9a9d847c | -1.28305 | -54.55702 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 10fb35e8-290b-3333-8c76-f3432c2d0020 | -2.98485 | -54.05396 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f414d7d1-4995-36f4-a508-091ce3d698a1 | -1.55799 | -55.71394 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cc7dc746-3fab-33ad-868c-08e87fc759d3 | -3.50149 | -51.69325 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| df159807-9098-3d75-8d6d-8fa75d545d54 | -3.59288 | -55.56216 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0b680422-67be-3a19-9a6a-adbd59de9bba | -2.92904 | -53.93522 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 067a0fc4-f877-30df-a512-0722e0838c77 | -3.00095 | -54.23808 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 461378ab-16ff-32f6-8724-624dacb0293e | -2.79584 | -54.07141 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| c8b4e5ca-b479-36a5-8328-9fd052794d9f | -3.63364 | -54.60775 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b7d0105f-6db3-3abd-b283-f4eb300acac3 | -1.63661 | -55.42056 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5e7110b8-dc29-30fe-bd10-b4c8324dae23 | -3.85598 | -55.98585 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 07966804-4c20-3a3c-83ed-9bb8d4951c1f | -3.00578 | -54.12059 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 85d7079d-a561-31cf-9c2c-dcc438fd1742 | -3.4772 | -50.08739 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| e1aaca6d-9292-3caf-abb5-0dffd0b466d0 | -2.9361 | -54.14909 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| eb76b96f-40eb-3e4a-ad6f-4f87851b7560 | -3.62156 | -57.04479 | 2026-10-07 16:39:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 898905af-1783-36f8-9a1e-730516c2eb47 | -2.94225 | -54.11668 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6b592841-4fa7-3ee8-bec3-96cd295b3609 | -1.47344 | -53.61267 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 69aa266b-bef1-3b6c-9544-d7768c807c82 | -3.04365 | -53.91696 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 534d8076-dd03-3034-89f1-8c6cad1a049a | -1.56487 | -51.67654 | 2026-10-07 16:39:00 | NPP-375 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 3c70ad53-d7e3-3783-938e-3125ca81991c | -3.5117 | -54.65716 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 946d2bee-2baa-3d21-b364-1fd3c3a90dd4 | -2.45749 | -46.01705 | 2026-10-07 16:39:00 | NPP-375 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d774ae8c-4d4f-33da-9be7-7cddfb5993bf | -2.77581 | -54.08458 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 362b4f8f-ec41-3d25-8fee-e774abb0bf8a | -3.82854 | -55.62374 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1aa7cd02-952e-3d5d-a106-ba73380145f8 | -3.10069 | -54.15576 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 23086cc2-87ac-3a3d-8694-b0baf62d82ed | -3.09552 | -53.71862 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c7838e4e-89a1-3258-a327-3f1125e1f698 | -3.53945 | -50.09682 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 988aca46-a108-33fb-b012-f5aec4948ca6 | -3.29092 | -54.03561 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 2941aca5-df79-321e-96cc-f54eadef43dd | -2.51085 | -56.25768 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 78594bbb-0ff1-3182-91d6-c5e4517b99a8 | -1.52338 | -54.80136 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 797c23f0-24de-3d54-aede-7b73517648c6 | -2.94809 | -54.06617 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a208b7b4-7a7b-3d46-ba50-dc9b04339357 | -3.27517 | -54.04127 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 72cd8819-7f7c-3f9e-8876-b53a6577475f | -3.08418 | -54.2717 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4a4a7328-9e69-3c2a-93a1-fffdcc27ce3d | -3.03199 | -53.91184 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| c2ded988-a85c-30b4-8026-007db020479a | -2.59234 | -49.62402 | 2026-10-07 16:39:00 | NPP-375 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 99a2c46c-18a4-3d63-a3f4-1f43ff83f93a | -3.53777 | -54.63823 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 84d317ce-1641-3c15-a7e0-406300e1e6fb | -3.27576 | -50.4104 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4559f073-398c-37b5-ad15-73d8c0198236 | 0.94282 | -50.20216 | 2026-10-07 16:39:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6998c38b-357c-3f30-9734-c9aa4435094f | -2.99352 | -54.75816 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a553d5b0-0e13-331e-a38d-66f763d70a53 | -3.54171 | -54.6647 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| efea1756-9c90-3ca7-9c13-842f2c7c0efc | -3.65334 | -55.45697 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 34762470-1253-3d26-939d-0d660cace51f | -1.4883 | -55.87589 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 700c223d-db68-30a8-b6f5-b24a45f95363 | 1.4763 | -50.77587 | 2026-10-07 16:39:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 6ef4e3ae-e35e-3c20-9792-ac2e5293dea9 | -3.49544 | -54.625 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 0dd6d853-d495-35e4-b30d-dd52e558664f | -3.85306 | -50.41537 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 2cf92f4f-4c0d-3d25-be61-d0ee925bd922 | -2.79505 | -57.66278 | 2026-10-07 16:39:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 264a8501-22e9-3009-a770-40d38e8b2c9c | -2.94372 | -54.11212 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 23532a21-937d-3d64-8dc2-4b94fb73873c | -2.89285 | -54.08192 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| b21fcb8d-96b1-3273-acdb-691060a44573 | -3.5128 | -54.66467 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d7d6f5d5-9557-32da-be3a-197d0dd3e857 | -2.76066 | -54.09378 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f3454bdb-e7d7-3b66-870d-51dc631d2c06 | -2.75356 | -57.66245 | 2026-10-07 16:39:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 852a7584-00b6-33d8-894b-4ae7fccea4d8 | -3.8573 | -50.41468 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 46dab038-a9d1-3135-8f83-8246e717b524 | -3.46394 | -50.60396 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d0c1defc-8d25-3ee4-bbfc-dfb696f50c9f | -3.19203 | -50.54482 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 56c86fe5-cd94-3820-8720-c3eb4ef56df0 | -1.80761 | -57.12035 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| cdb2367f-7687-3051-93f6-c8b5cf003e69 | -3.20525 | -53.87895 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 252ca74f-1935-33a7-8942-056ec340d105 | 3.21777 | -51.28886 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 34baf609-c16d-3a1e-8b7c-087211ee7979 | 1.77024 | -55.56768 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 04ebb875-7901-3fd5-87bb-b26bb25bca24 | -4.15408 | -54.02675 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0e621eea-2b6d-328a-b67e-7dade6d26b76 | -3.08227 | -54.29724 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| cc254302-264c-36ca-a747-2269624e9f79 | -3.18894 | -50.5533 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 86c6025e-bbce-32c1-9710-b9f463e0e50a | -3.26502 | -54.66379 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 17111fda-31bf-3118-9ae0-7ea716dd9dca | -3.18585 | -50.56178 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c61ee781-3efc-3e31-9b52-88f5d7a10e7f | -3.63066 | -55.28061 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |


[Clique aqui para ver as próximas entradas](README231.md)
