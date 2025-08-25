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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4a5aa34-1cd4-3260-b3c1-1b8e976e89ed | -10.6115 | -55.051102 | 2025-08-25 01:03:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 397f1cd3-ce9b-3b49-a3a1-5ecfc89cffa2 | -10.4625 | -59.119099 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d91efc22-5a4a-353e-823f-5b2381b360ab | -6.8185 | -59.4142 | 2025-08-25 01:03:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6bfaccb8-9c7b-3118-a7d7-3050487ef872 | -10.4126 | -64.374496 | 2025-08-25 01:03:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 85f4cb2a-250c-355a-91c8-ba365be2059e | -7.4742 | -61.3102 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d66ab735-24e1-3484-a578-18601dd1704c | -9.0456 | -65.701698 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83b7e53d-0abc-3153-b15d-61dac3a4f705 | -7.0399 | -59.842899 | 2025-08-25 01:03:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 589396e1-70ed-3d1f-a799-c91cc178cbdc | -6.2394 | -59.9939 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ccbc6237-c223-3fe5-9835-6b74c24c4edc | -10.4239 | -64.428001 | 2025-08-25 01:03:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dc89b612-4c23-3150-8cb7-49df7b8e47d2 | -10.6186 | -55.0373 | 2025-08-25 01:03:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ceb8e225-4041-3e46-8300-a8d4e6e2687b | -15.6246 | -52.710201 | 2025-08-25 01:03:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0c4cb2a4-9ad9-3d47-9e86-ee2e773390e7 | -14.2439 | -58.608299 | 2025-08-25 01:03:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bf2a811c-8a6f-3343-9cf0-25f069116fc8 | -7.6623 | -63.509102 | 2025-08-25 01:03:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee1da898-9810-3908-971d-f97ef0471649 | -5.7451 | -63.159401 | 2025-08-25 01:03:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 291a800a-2f92-3c47-859b-89cfac7babfe | -7.9141 | -63.063599 | 2025-08-25 01:03:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c79c6be6-467d-369e-a49a-9359ad8a6674 | -9.6096 | -55.346001 | 2025-08-25 01:03:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bd0c9fb4-464d-3acd-9d99-4c51fdeb4f34 | -8.8775 | -62.441101 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 92ff4c02-fdb6-31d4-bcad-0af1f87eda1c | -6.4379 | -58.2528 | 2025-08-25 01:03:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 237593ff-fbad-36d6-a055-568c4e32a9f9 | -8.0807 | -61.536201 | 2025-08-25 01:03:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ab9807b-e7e6-3468-88ac-4dfd14624825 | -6.92 | -62.984299 | 2025-08-25 01:03:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cf64eef8-76f0-3866-94aa-9d80f3cbfa8b | -6.2591 | -60.035 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| db39fdff-e0bc-3971-9105-85dc8108abe4 | -9.1696 | -59.4631 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb9f19cd-b90e-374b-8c60-66a6a98c8a1e | -9.5226 | -60.523602 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cacb26db-3f86-3e85-9ef8-96f63d7f7a1e | -12.5939 | -60.3526 | 2025-08-25 01:03:00 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5ff11772-736a-3dfd-9acf-f1bb28b00acd | -11.7 | -60.174999 | 2025-08-25 01:03:00 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0606e187-dd80-371f-86c1-1eefd7022b3c | -9.134 | -60.720501 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2f893835-7e6b-34ed-828e-23cb9033e4bf | -6.264 | -60.011101 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af6750be-37c2-3a3e-ae98-295e88c97074 | -9.9596 | -60.175999 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac74f809-70fa-35d8-aada-e2d5c5e42960 | -8.9136 | -62.417999 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| abbc1399-5b90-3305-be79-3c8c0ac709e5 | -8.2197 | -61.374901 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f02e3d2c-2f10-3b91-8c6a-fbd38da4406f | -9.1778 | -59.453602 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| efd2ba8c-8dc8-3212-9c30-3c4c553cfa6c | -8.1158 | -62.858398 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 020773cd-fdf0-3cf7-8b7d-622d2f29449c | -6.2313 | -60.003399 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 13485843-e91b-3ce6-9d47-66d4a432599d | -9.5008 | -56.098701 | 2025-08-25 01:03:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b27f8a26-00c6-307b-9d13-092c3961059c | -9.5308 | -60.5144 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a07e07d8-90c7-3b82-beeb-88047cdd5641 | -18.0725 | -51.384201 | 2025-08-25 01:03:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 72d7d373-da8b-32f4-a4cf-88d31ef76264 | -2.9237 | -53.693401 | 2025-08-25 01:03:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c37884d5-74f5-3972-845b-7a1ab9fb4b49 | -5.7542 | -57.5704 | 2025-08-25 01:03:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57d4c9b2-4fb7-3814-bfa5-2267f4dd5d3f | -10.4197 | -60.298199 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1fc6154c-1397-39d3-bb8d-df8acd29b011 | -8.2326 | -61.386501 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a1bb4e10-f894-3161-af10-a0a3d397fef6 | -6.8329 | -58.937401 | 2025-08-25 01:03:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a400c2c5-e871-3de4-888d-11eebe26b5be | -8.5874 | -62.618099 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e39f6cc5-fc67-33ea-bc25-655c07f29354 | -9.2138 | -59.611801 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84dd0300-cc00-3f80-8b44-9dd2e1167d8a | -7.5295 | -63.794498 | 2025-08-25 01:03:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e5d96ffc-d569-31c7-9dd8-09686e704b69 | -9.1794 | -59.4608 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6ce7114-de93-3ab2-9392-55e20425dde2 | -20.356701 | -46.7234 | 2025-08-25 01:03:00 | METOP-B | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b7fa3737-6725-3152-bcea-cbb7b2c7d169 | -8.9158 | -60.711601 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1aaf6934-abfa-35a8-b251-c545a1720673 | -14.3268 | -49.1012 | 2025-08-25 01:10:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 46.5 |
| a598cc58-8994-30e3-b386-2ced3a73cbf5 | -6.2458 | -60.0365 | 2025-08-25 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 18ea27c6-57b7-3bd3-aa53-99b0a8b005f5 | -11.6304 | -46.2311 | 2025-08-25 01:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 36ee901a-03e0-3264-8de1-fcec05bb710b | -9.0786 | -65.7338 | 2025-08-25 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 520c0a27-3a0a-372a-88f8-3644d6554e06 | -7.6141 | -62.7249 | 2025-08-25 01:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 4d8fa9cb-cd14-3292-a02c-201d9ecda7a4 | -8.9689 | -65.4198 | 2025-08-25 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| e690de31-f386-3a42-9e52-3e24d7a54a32 | -8.8919 | -62.4487 | 2025-08-25 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 9df408e1-2f3e-362a-82b2-56c374a20433 | -6.246 | -59.9982 | 2025-08-25 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 94b19771-8a9c-360d-befb-a77102aba2f9 | -8.969 | -65.4012 | 2025-08-25 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| cc31c528-9222-355c-8a1f-d95e7ab339f6 | -8.8734 | -62.4495 | 2025-08-25 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 4c04f74a-6201-3521-8b74-74a51936cdee | -6.2644 | -59.9976 | 2025-08-25 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 2aafd911-d224-33f1-a7d4-d1db61053384 | -3.4254 | -49.0517 | 2025-08-25 01:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 408e8553-0c00-3eb9-ba8e-96d8f10bb555 | -10.5937 | -44.331 | 2025-08-25 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 8626756a-82dd-3df5-a336-f3f3af0ba03b | -9.0061 | -65.3813 | 2025-08-25 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 28968176-18aa-302e-92bd-ca21737549a9 | -9.006 | -65.4 | 2025-08-25 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| fcb83ade-2e3a-3e63-9f87-f8ebd7730380 | -8.8733 | -62.4685 | 2025-08-25 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 4179e460-44a0-3ea2-9643-107b1691b928 | -9.8101 | -64.2642 | 2025-08-25 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 5e288b76-fd86-3854-a557-2f9c3e5d49d1 | -6.2642 | -60.0359 | 2025-08-25 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| e7924974-8418-35a3-8e77-a4a09b160bd3 | -8.9874 | -65.4192 | 2025-08-25 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 175.6 |
| 2bc87969-07ce-3bc3-a496-b280b4c6a470 | -20.3708 | -46.7195 | 2025-08-25 01:10:00 | GOES-19 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 5c1c39bb-c114-342c-8619-50c66ed70a86 | -6.2459 | -60.0174 | 2025-08-25 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 0a2a19f7-bbd3-3e13-ab0a-e31100438069 | -8.5943 | -62.6315 | 2025-08-25 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 107.0 |
| a68cea85-c2ce-3244-af2a-33b347661827 | -6.2643 | -60.0167 | 2025-08-25 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 224.6 |
| 78e0d454-e521-3ad6-8066-20467e143f81 | -8.9875 | -65.4006 | 2025-08-25 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 2d3b02c5-181f-3ad7-97a7-b1c9477f2aa0 | -8.5758 | -62.6323 | 2025-08-25 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 6f46d822-0fd1-3571-83c4-4c0b31bd16e3 | -9.0415 | -65.7349 | 2025-08-25 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 3f221e7d-3f34-3286-9d19-06cb92b249b0 | -3.4439 | -49.051 | 2025-08-25 01:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 50ee8d46-405d-3264-a4d4-21ea2f3e1868 | -8.8918 | -62.4677 | 2025-08-25 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 73bfafca-1067-3d75-854c-91a70bbb80e9 | -11.0493 | -52.0015 | 2025-08-25 01:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| d3715019-aef1-3f65-8279-876c0cf1e784 | -6.8229 | -58.956 | 2025-08-25 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 398981f3-3ac3-311a-ab7e-76dedc38cacd | -6.8413 | -58.9552 | 2025-08-25 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 19229356-1032-32a2-8b7e-70d64680c4a0 | -22.5307 | -46.8109 | 2025-08-25 01:20:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.9 |
| 2ff3c578-4919-37b5-8066-f185043cc54e | -13.1534 | -53.7397 | 2025-08-25 01:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 259.9 |
| 119d6d2b-4113-33a0-a750-31aa6df83f59 | -6.8044 | -58.9568 | 2025-08-25 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 89fa504d-9115-31cf-acd0-ad5e58051d59 | -22.5518 | -46.8053 | 2025-08-25 01:20:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 143.1 |
| dfde69d3-b7ec-3ff3-8bd3-294e2de6293a | -18.0799 | -51.3908 | 2025-08-25 01:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 21f46dff-81a9-382e-803c-95329330451f | -20.3907 | -46.7384 | 2025-08-25 01:20:00 | GOES-19 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 84.9 |
| d1dd3f9c-d8cc-3807-ba53-98d39f1f879d | -9.1988 | -60.9274 | 2025-08-25 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 6ba844ce-4d61-3f98-bf7e-cb1cb5dd1064 | -8.8918 | -62.4677 | 2025-08-25 01:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 80.0 |
| bc8a7dd0-4a00-30a7-a9ba-1eba2634ba71 | -8.8733 | -62.4685 | 2025-08-25 01:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 2f37a9d7-f399-3611-86e6-984132cc777e | -3.4254 | -49.0517 | 2025-08-25 01:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| f427d09e-c2d7-3a9e-9df7-2f9e49b2d7a9 | -8.5758 | -62.6323 | 2025-08-25 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 188.6 |
| 3f8de9cf-23b7-32de-b2b6-2ad8114f6ad2 | -8.8734 | -62.4495 | 2025-08-25 01:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 31218d5e-04f5-35fe-8df2-3f4bb451e9f4 | -13.1725 | -53.7376 | 2025-08-25 01:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 3baa0ec0-29ca-36c3-bc23-927e690bc224 | -20.3708 | -46.7195 | 2025-08-25 01:20:00 | GOES-19 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 8c874a14-6a53-3e32-b3e8-c4b57baa5052 | -7.6326 | -62.7243 | 2025-08-25 01:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| f09f6f76-b001-3d1b-a1c6-c5817564f054 | -9.8101 | -64.2642 | 2025-08-25 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 81a96059-d102-370c-89dc-25beea77a35b | -9.0972 | -65.7145 | 2025-08-25 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 6e89110e-4b03-35f6-89fe-8e41873fcdd6 | -8.8919 | -62.4487 | 2025-08-25 01:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 99.2 |
| bd79e143-63be-3a51-b815-2a5c549f5463 | -8.5757 | -62.6512 | 2025-08-25 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 057d1307-e094-3bd4-a9ba-f41fb5b274e9 | -8.5943 | -62.6315 | 2025-08-25 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 182.2 |
| 126d9e25-cf08-3271-adff-3ea076093a86 | -9.0971 | -65.7332 | 2025-08-25 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 5ee09d58-f329-3e8e-827c-2e2dc13eb8ed | -13.1537 | -53.7189 | 2025-08-25 01:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |


[Clique aqui para ver as próximas entradas](README10.md)
