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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6df7077-07e3-3c6d-b9ba-680fbc2fc8c1 | -3.23 | -43.4182 | 2025-08-28 00:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| d34c5f48-c87b-3acd-ae51-4d6b28c13637 | -10.8049 | -60.7644 | 2025-08-28 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 8baa4777-3d7b-3358-bb42-ce8dcbfaf8a1 | -7.3357 | -59.6484 | 2025-08-28 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 12e04b49-d884-3f23-818c-7b35570251f4 | -11.2189 | -55.0585 | 2025-08-28 00:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 7fe28c73-297a-364a-85f0-c237974b1c61 | -11.2378 | -55.0569 | 2025-08-28 00:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 052c475b-7af3-3b75-a122-17d15f45ab6f | -11.3329 | -43.5452 | 2025-08-28 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| c520a453-dd37-3157-a683-f0bc48766d09 | -9.6104 | -40.342 | 2025-08-28 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 70.7 |
| c4bfd609-ea7e-3cd1-8235-fb5f25d41367 | -13.7566 | -51.9053 | 2025-08-28 00:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 90a41a42-e87a-3f61-9854-d804b95f44ea | -10.8047 | -60.7837 | 2025-08-28 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 36f056ec-4aa6-3907-b06e-aaaab17ef1e6 | -9.4061 | -60.5518 | 2025-08-28 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 64c29728-1e73-305e-9fec-775af5e3c74f | -3.2298 | -43.4646 | 2025-08-28 00:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 0146a952-0520-311c-b8d9-752452e49d63 | -8.9665 | -65.9424 | 2025-08-28 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 29a1f790-572c-3c36-b3e9-9e88da64e41b | -6.8772 | -43.6152 | 2025-08-28 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 1c36c960-78f2-3ffa-b913-29797006baee | -9.1363 | -65.2835 | 2025-08-28 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 3ac2e388-e126-33f3-a882-4f39669a10b2 | -10.5371 | -46.7119 | 2025-08-28 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 28442a55-4e17-3e87-8b99-bb0c099647ad | -9.406 | -60.5711 | 2025-08-28 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 107.2 |
| b4548630-4b74-3245-9414-7b74da372026 | -13.1644 | -45.2897 | 2025-08-28 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 4727a1e9-45ed-3153-8ba7-f57a7d047ffb | -10.8236 | -60.7633 | 2025-08-28 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| d0031dfd-582c-39e9-b933-66d5151f01a0 | -12.8032 | -48.1516 | 2025-08-28 00:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 44b1e1a3-a247-365f-bd05-301ffcc651b8 | -13.7373 | -51.9077 | 2025-08-28 00:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 9eb4f6cb-cc1d-3091-be7f-c3775a875d22 | -10.8235 | -60.7826 | 2025-08-28 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 521d9f3c-339c-33c3-9972-2fceec55e629 | -9.5623 | -48.7836 | 2025-08-28 00:40:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| dc164152-a799-3088-bef8-53de41d5a096 | -10.4738 | -57.9366 | 2025-08-28 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 8fda8450-d256-3e48-9110-37b3b43b7d13 | -4.7893 | -47.2614 | 2025-08-28 00:40:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 57b61f0e-b472-39e4-98a2-ee214b38d2f1 | -8.948 | -65.9429 | 2025-08-28 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 0fe58860-93a7-3267-b08c-e3e8d639de46 | -3.2299 | -43.4414 | 2025-08-28 00:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 248.9 |
| e7915c4f-5bec-3685-9b42-2e55491ba8a4 | -11.3334 | -43.5216 | 2025-08-28 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| d0751342-77fb-3b9a-a415-da1c05cb5e2d | -10.5375 | -46.6894 | 2025-08-28 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 137.4 |
| e351b55d-e7a4-38fc-9045-ba08e9252010 | -13.1837 | -45.2865 | 2025-08-28 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 269.0 |
| f3483c2c-d375-332e-962d-768a54936de5 | -13.1842 | -45.2633 | 2025-08-28 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 610cd04f-685e-3bac-845f-99e7442096a6 | -7.3541 | -59.6669 | 2025-08-28 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| e1bbfea2-32c8-3ab8-b8af-3b87b4c39071 | -9.0786 | -65.7338 | 2025-08-28 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 496c54a6-7a99-316c-881a-6976345cabd6 | -10.4736 | -57.9563 | 2025-08-28 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| aaa9c2fa-81f5-328d-9717-44160752f5c5 | -7.3542 | -59.6476 | 2025-08-28 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 120f73dc-bc63-3b84-a3ea-c6ef1cc1244e | -3.2485 | -43.4406 | 2025-08-28 00:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 226e6610-e3ea-3df8-b3d4-ef9a1c5530ea | -12.8032 | -48.1516 | 2025-08-28 00:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 1189165d-3da4-3fa6-be29-c92497a2b441 | -9.4246 | -60.5701 | 2025-08-28 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 12542c40-b779-32c3-a814-9c50fb54b064 | -4.7893 | -47.2614 | 2025-08-28 00:50:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 102.4 |
| e6b5933c-aa55-3ce5-93c4-67f6094c1ccf | -15.6541 | -49.7757 | 2025-08-28 00:50:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 90768efa-2acc-3d04-bd1e-e3ee1a6c4e82 | -6.8772 | -43.6152 | 2025-08-28 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 6506a536-c707-3b29-8550-faae9a18a0f0 | -9.1155 | -65.7699 | 2025-08-28 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 263.7 |
| f5419c93-903a-3e67-8316-1f8369d29f3f | -12.4396 | -45.9551 | 2025-08-28 00:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 323132a0-a42b-345c-b1b0-f4e239aac0ce | -9.1338 | -65.8067 | 2025-08-28 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 941001f8-87d8-3115-8db1-5ef47ced24b5 | -8.9479 | -65.9616 | 2025-08-28 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 132.6 |
| c484b5b9-2091-3894-a0c5-b86d344dd65d | -7.3541 | -59.6669 | 2025-08-28 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 8cddc189-574a-3e0a-9923-d1eba3471bc6 | -13.7373 | -51.9077 | 2025-08-28 00:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 7c6e8fc6-e4aa-39da-9350-660a0a964f1e | -13.1833 | -45.3098 | 2025-08-28 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 8d403597-76cb-33cf-a208-1b6dde4cc919 | -7.3357 | -59.6484 | 2025-08-28 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 68b0a602-af9a-313a-82fc-b67cbf2c7f51 | -13.1842 | -45.2633 | 2025-08-28 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 318a5643-e083-3ec5-b972-93dda50e402e | -11.3329 | -43.5452 | 2025-08-28 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 184a2417-8906-375c-83d0-65c90524a516 | -13.1837 | -45.2865 | 2025-08-28 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 243.5 |
| 7dae60f4-9c94-3d5d-8854-835078a63950 | -9.1154 | -65.7886 | 2025-08-28 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 399.9 |
| af40b523-4429-3282-9984-2f5b93429896 | -11.2378 | -55.0569 | 2025-08-28 00:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8ed1d804-9842-3aa5-a7c6-7865a8e1886e | -9.0969 | -65.7892 | 2025-08-28 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| b953797d-82ef-39d0-8872-58c12dd1365d | -15.6546 | -49.7536 | 2025-08-28 00:50:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 203.4 |
| a5e9206d-7584-3b39-a6c7-91ee5f9d8eec | -3.23 | -43.4182 | 2025-08-28 00:50:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 592e980c-a977-344c-8281-14413fcdb77d | -8.948 | -65.9429 | 2025-08-28 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| ed4fb875-9280-39f0-b3a6-d683c781b3f1 | -9.1363 | -65.2835 | 2025-08-28 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| eff92b49-6215-3b80-b260-8868c016cd91 | -10.8047 | -60.7837 | 2025-08-28 00:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| b178a343-e241-3c84-9c04-0eabde37d4cd | -9.134 | -65.7694 | 2025-08-28 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 295.8 |
| af0ffef7-7de8-3b0a-9d10-4fcdb43fbf20 | -10.4736 | -57.9563 | 2025-08-28 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| d10ab5bc-4ffc-3778-8ba1-e52c39b31f31 | -13.7566 | -51.9053 | 2025-08-28 00:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| cf879a2c-2d18-387b-9ffa-670b96fe1aa0 | -4.8079 | -47.2604 | 2025-08-28 00:50:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| ac748324-8992-3e1d-804e-78d0d14368f6 | -11.3334 | -43.5216 | 2025-08-28 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| fdd6b490-fb1f-39da-b5b8-2a00760b85db | -13.2031 | -45.2834 | 2025-08-28 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 28057512-a7db-3c23-95fb-a73a0ba638a8 | -10.8235 | -60.7826 | 2025-08-28 00:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 162381c2-846d-3535-a1a1-c24eed9808e6 | -15.635 | -49.7568 | 2025-08-28 00:50:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 2c07cd6b-b449-39c5-94b7-d596e41e4698 | -9.406 | -60.5711 | 2025-08-28 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 0978fe7c-1228-34ef-8c2e-69743dabe178 | -11.3521 | -43.5423 | 2025-08-28 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| d641866e-5f20-375d-ad12-19c4e64ef80c | -7.3542 | -59.6476 | 2025-08-28 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.1 |
| b536520f-5d0d-3867-a9e1-3a2bd9b9a6ce | -11.2189 | -55.0585 | 2025-08-28 00:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 06498f49-8624-351e-a547-27c4085ccf6e | -9.5027 | -62.7832 | 2025-08-28 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 2b3c8db3-5159-3762-bdcd-2d4295c40511 | -8.9664 | -65.961 | 2025-08-28 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| ba3d89d5-6165-3f3d-bf13-7d099b367b4b | -9.1177 | -65.2842 | 2025-08-28 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 48d45efc-743f-3f5e-b41b-922355d754f2 | -9.1339 | -65.788 | 2025-08-28 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 443.3 |
| 777e3613-bf54-3ff3-9290-6193d8a7fdcd | -6.896 | -43.6135 | 2025-08-28 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| e98bca35-44db-3567-b47e-8a7eabf57466 | -9.6104 | -40.342 | 2025-08-28 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 1ca79454-9712-3c67-afcf-5418bfcedceb | -4.2924 | -40.9432 | 2025-08-28 00:50:00 | GOES-19 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 59.6 |
| bd92ebbc-4e13-3ca2-8453-18b9db725f53 | -10.4738 | -57.9366 | 2025-08-28 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| aa9a5154-9851-37a1-b05f-90fcce616ddf | -6.9129 | -62.9366 | 2025-08-28 00:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 28761c3c-df54-393d-9d58-bed81542e157 | -3.2299 | -43.4414 | 2025-08-28 00:50:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 3f6b2a64-57d0-34ad-90a6-b62e0680c375 | -11.3526 | -43.5187 | 2025-08-28 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 12129afc-29de-3695-ae01-9d59c3b41fe6 | -8.9478 | -65.9802 | 2025-08-28 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 8355c68c-95f5-3d04-97a7-9eddf64aabf3 | -12.9645 | -44.5681 | 2025-08-28 00:51:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b7ce5895-d293-3c1a-804f-d36bacd542db | -12.7982 | -48.151901 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 747f703e-25dc-363f-9c44-feaae180dc39 | -9.4072 | -60.543999 | 2025-08-28 00:51:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 658e61d6-f46c-3592-b7a9-9623408ae8b7 | -2.9831 | -48.604401 | 2025-08-28 00:51:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d35c364e-a322-3748-bc6d-96dcee700b52 | -13.1777 | -45.268501 | 2025-08-28 00:51:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b59dcef3-0dc3-3ca4-985e-c9dc34e2d2ac | -12.7412 | -48.173199 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63acb80f-a5d0-317e-a94b-ce86281a6ec2 | -8.4454 | -43.683899 | 2025-08-28 00:51:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c975e227-da0b-3560-b884-971b7d33a9d2 | -12.7216 | -48.177799 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32a0ca03-a52c-3284-b8d4-b3148966fa9b | -11.8079 | -46.796398 | 2025-08-28 00:51:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d05a773-4b81-33f2-b407-95e53d3d90c7 | -6.2226 | -43.361198 | 2025-08-28 00:51:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a9eb927-9157-38de-be52-0480a94ba843 | -13.5235 | -46.9244 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8db1d827-88e0-3267-b43d-15dd4550c0b1 | -12.7101 | -48.172901 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 244c80e4-8dbb-3b97-8c74-b35472be7d1d | -12.7182 | -48.1632 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7635bc51-95cf-3094-a025-fe3471a98c20 | -10.3242 | -46.773102 | 2025-08-28 00:51:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8534b0fb-40f7-36b2-9e30-b671df570870 | -19.073 | -42.138401 | 2025-08-28 00:51:00 | METOP-C | FERNANDES TOURINHO | MINAS GERAIS | Brasil | 3125804 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 38b13efe-5057-3a7a-b023-70d3372b5a7b | -13.0736 | -46.336899 | 2025-08-28 00:51:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 97f5683e-b227-39e1-a4ea-54eccdab15be | -7.2832 | -49.257 | 2025-08-28 00:51:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
