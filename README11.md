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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6e742cf-4229-3f2b-8426-3ea0660e68d6 | -13.7373 | -51.9077 | 2025-08-28 01:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| ead513ac-9b24-398b-a815-2f6e6c648e58 | -8.9664 | -65.961 | 2025-08-28 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 4f0fbb28-4ffc-30e7-86e8-fc08a49ce19a | -6.896 | -43.6135 | 2025-08-28 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 81947117-9c27-3336-924f-97d6c594a0a6 | -13.1842 | -45.2633 | 2025-08-28 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 51d5010c-3117-32a4-95d2-50c88e5e8862 | -11.3329 | -43.5452 | 2025-08-28 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| c2f0a89f-740a-3122-8d2c-462e2ea0d1a8 | -8.948 | -65.9429 | 2025-08-28 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 70a2e8cc-639c-3b9b-b8c9-091ed5dd28ba | -13.1837 | -45.2865 | 2025-08-28 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 273.8 |
| 99eebb31-6401-3719-b373-78183a61574b | -9.1363 | -65.2835 | 2025-08-28 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 9db77182-302a-3bf1-ae49-c34bb8f5105e | -9.406 | -60.5711 | 2025-08-28 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 29dc3322-d6f5-353b-9716-c5c24119cdbc | -11.2189 | -55.0585 | 2025-08-28 01:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| e1412c39-2fd3-3718-9336-7e3ca70384f3 | -6.9129 | -62.9366 | 2025-08-28 01:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| c0957c84-41a3-307c-8f01-41976791b57d | -8.948 | -65.9429 | 2025-08-28 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 0e9e75aa-7546-3aa7-aabb-a4dd1f8d380b | -7.3541 | -59.6669 | 2025-08-28 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| af2d71af-cd4c-3ca6-a2a6-2c205326d63c | -10.5378 | -46.6669 | 2025-08-28 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 42655629-fb1f-3dd5-86d9-95333125e86b | -11.3329 | -43.5452 | 2025-08-28 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| ceeb71c4-fee8-3c4b-b890-6fe2469f4ef4 | -10.4738 | -57.9366 | 2025-08-28 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 3877fa1b-e13c-30d4-ad27-8db4c256bf12 | -10.5565 | -46.6871 | 2025-08-28 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| c4c2517f-ca00-37f1-867c-c8a28d589b3e | -6.8772 | -43.6152 | 2025-08-28 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 169.3 |
| 6e04f334-03da-3c34-b1ac-ca4103329553 | -10.5184 | -46.6917 | 2025-08-28 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| ad9a63eb-0c54-3896-9913-03d359345185 | -8.9478 | -65.9802 | 2025-08-28 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| e94da635-bad1-3491-8d2b-bc39b56fb5aa | -13.7373 | -51.9077 | 2025-08-28 01:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| cd2e1e65-712a-3dd0-9c83-148845757ea7 | -7.3357 | -59.6484 | 2025-08-28 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| bac383d4-6987-3ff6-9474-57d08686c0e9 | -11.3334 | -43.5216 | 2025-08-28 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| b47dc45d-8844-3337-9d3c-43e13984e7df | -12.4396 | -45.9551 | 2025-08-28 01:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| fd23991f-22b2-384a-bbe4-1d19bc1a2b8e | -8.9479 | -65.9616 | 2025-08-28 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 125.5 |
| e5ea960a-dab0-3cbf-9226-c179a29342d5 | -4.8079 | -47.2604 | 2025-08-28 01:10:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 3f2c67ef-9a9e-3cbd-aadc-ebe5f7f9dc47 | -10.4736 | -57.9563 | 2025-08-28 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 13566b98-7079-311f-af76-ded9afe27eb1 | -12.8032 | -48.1516 | 2025-08-28 01:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| a0d0d576-517f-330a-aa7c-0fb7eb9df163 | -13.1837 | -45.2865 | 2025-08-28 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 285.6 |
| 1eff9ba6-7908-3eea-b283-c8a28f8ee7f2 | -10.5375 | -46.6894 | 2025-08-28 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 203.6 |
| 759e171f-f5bc-3f35-a5cf-fdcb2fe18c9a | -13.1833 | -45.3098 | 2025-08-28 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| dc855abe-232c-3fd4-acbe-caaf04709ccf | -4.7893 | -47.2614 | 2025-08-28 01:10:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 60277700-6211-3f15-830f-195a110a29fe | -3.2299 | -43.4414 | 2025-08-28 01:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 9d19e676-499f-3f42-9a41-b2fffa55a56a | -13.1842 | -45.2633 | 2025-08-28 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 21065d9f-578b-31d2-a2a3-bb10a32d7528 | -8.9664 | -65.961 | 2025-08-28 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| c438f06c-b14b-37b3-bf09-4f2a17cceccc | -6.8769 | -43.6385 | 2025-08-28 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 09cd5e62-a7fa-3c1b-8df8-b69e147ad7ed | -13.2031 | -45.2834 | 2025-08-28 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| a2571e35-0957-37b6-a40a-d4efb7be6439 | -11.3526 | -43.5187 | 2025-08-28 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 7c2550da-f4ef-3df7-8449-5d05cbf7a571 | -7.3542 | -59.6476 | 2025-08-28 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| becab8db-24cf-3666-b5c0-106fcbcf33ad | -13.7566 | -51.9053 | 2025-08-28 01:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| faebe652-d9ee-3655-b6d2-051286616e2a | -6.896 | -43.6135 | 2025-08-28 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 4b54ad8d-7876-3336-98c0-e5ab436d0b99 | -11.3334 | -43.5216 | 2025-08-28 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 7385807d-5f1d-3d38-82f3-1066ad8ceb1d | -7.3541 | -59.6669 | 2025-08-28 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 5570bcde-dd80-3e8a-840d-46f449215788 | -9.1363 | -65.2835 | 2025-08-28 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 6e0a8541-4bde-3082-9ffb-72b50bdc5a1f | -6.9129 | -62.9366 | 2025-08-28 01:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 0c2cdecd-209b-384d-8b50-ac42bff784d4 | -13.2031 | -45.2834 | 2025-08-28 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| aa6e1ecf-81f6-3d39-88ac-c9d7691c069f | -9.406 | -60.5711 | 2025-08-28 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 105.0 |
| eae045d8-7fd8-3d65-8df1-0a90be19d4a3 | -4.7893 | -47.2614 | 2025-08-28 01:20:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| b45109b2-001e-36f7-92a6-d71e33f78161 | -13.7373 | -51.9077 | 2025-08-28 01:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| f9091b56-b096-30c0-892c-2092744ce603 | -10.5181 | -46.7142 | 2025-08-28 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 22189a6f-2f46-3577-953c-9313b0c81a7a | -9.0971 | -65.7332 | 2025-08-28 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| ddb9d42a-78fa-34d2-8fc3-dfadb1b1e761 | -10.5184 | -46.6917 | 2025-08-28 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 184.4 |
| a2e79fd4-57b8-3e99-bf90-32532960a3d1 | -6.8772 | -43.6152 | 2025-08-28 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 170.4 |
| 0978850f-31ff-3c1e-af19-8d8247f1fc54 | -13.1837 | -45.2865 | 2025-08-28 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 236.2 |
| f6e66ff4-be3f-364d-96e7-59abf0dd0903 | -8.9479 | -65.9616 | 2025-08-28 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 2400289a-fed8-3015-a67c-4db1d499dbee | -11.3329 | -43.5452 | 2025-08-28 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 2b5aff85-0300-384e-aa41-b2ee12480d09 | -11.2189 | -55.0585 | 2025-08-28 01:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 2941f0f3-cc3c-3e75-9af3-c1e549282a48 | -7.3542 | -59.6476 | 2025-08-28 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 192901c8-9b6b-39a3-9d5f-4de007407abe | -4.8079 | -47.2604 | 2025-08-28 01:20:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 15769176-dea9-36dd-9db7-35317fc2fc98 | -6.896 | -43.6135 | 2025-08-28 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| ad7879ee-f01b-3f02-8b20-dc873deb8690 | -10.4738 | -57.9366 | 2025-08-28 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| eaee414b-39d9-3f35-93eb-fd134efdd7fd | -13.1833 | -45.3098 | 2025-08-28 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 9244a406-a348-34ad-95fa-1e59093c8c1f | -10.5378 | -46.6669 | 2025-08-28 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 798e33f0-01be-385c-9ecd-579756f294a8 | -13.1842 | -45.2633 | 2025-08-28 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 64bafc5b-e39e-31d5-9de3-75af2781b511 | -10.4736 | -57.9563 | 2025-08-28 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 94f6fa1b-5551-3e3d-8e22-047bb210cf31 | -7.3357 | -59.6484 | 2025-08-28 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| fdbe9c0f-1baf-3bd1-ba57-13bf698b7deb | -10.5375 | -46.6894 | 2025-08-28 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 516.1 |
| f6a77aaf-29f6-33eb-8dff-cb7ebbd967be | -10.5371 | -46.7119 | 2025-08-28 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 257.9 |
| fa6df4b4-4197-39ab-894b-5a4f9e95c130 | -10.5565 | -46.6871 | 2025-08-28 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| b10dcb21-615d-3114-b973-eee2de552ada | -8.9664 | -65.961 | 2025-08-28 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| df711ab5-a238-34f3-b599-32206c896aec | -12.4396 | -45.9551 | 2025-08-28 01:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 9561360a-5025-3850-a511-3645338c9e9b | -8.948 | -65.9429 | 2025-08-28 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| f5f8d61a-f42c-330e-a889-940bef80aace | -3.2299 | -43.4414 | 2025-08-28 01:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 797e9fb1-58a3-3b73-9af4-4f6c430f3d97 | -12.4396 | -45.9551 | 2025-08-28 01:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| f9cc7801-6ab4-3584-b050-2830fa7b6b59 | -13.2031 | -45.2834 | 2025-08-28 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 62cdc9a4-daf3-378b-b0e5-3035e81d6bd9 | -6.8774 | -43.5919 | 2025-08-28 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| e03d6837-c0ea-3d30-8883-600534228c6a | -7.3357 | -59.6484 | 2025-08-28 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| c3a78e89-acf3-3f04-84c6-2f89bafa2fa9 | -9.406 | -60.5711 | 2025-08-28 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 107.6 |
| d05625e4-5d43-37d2-8442-3d06975f16ff | -10.4736 | -57.9563 | 2025-08-28 01:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 12af47b3-9f84-35c8-93b0-c52e56a3eddb | -3.2299 | -43.4414 | 2025-08-28 01:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 8b078387-b658-3506-b1b3-8ff58df58b85 | -8.9479 | -65.9616 | 2025-08-28 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 6051e7a0-7acf-3a20-984e-74b43948dd96 | -6.9129 | -62.9366 | 2025-08-28 01:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 98bf2347-72f4-3bc7-adbb-9add9e6a49a9 | -6.8772 | -43.6152 | 2025-08-28 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 31361386-cc8a-3155-bbc5-1bde6995ee23 | -8.9664 | -65.961 | 2025-08-28 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 414d0de5-3d35-3b14-ab92-953c4915834f | -10.4738 | -57.9366 | 2025-08-28 01:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| a6cf0b0c-3c13-3d01-a848-823f13b1650e | -13.1842 | -45.2633 | 2025-08-28 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 7dc4ce33-59b9-3fe0-bcc2-9aeaf54bbc06 | -11.3329 | -43.5452 | 2025-08-28 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| b8d74e39-294a-37b7-b786-d9460a6e3714 | -13.1837 | -45.2865 | 2025-08-28 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 4b399f34-0fb9-3068-a847-fb91396679ff | -9.1363 | -65.2835 | 2025-08-28 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 3eed7bae-09e6-39f4-9a5a-457d7cd46a55 | -7.3541 | -59.6669 | 2025-08-28 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| e17ed7da-f59e-325b-93ea-f5194f9e61b4 | -4.7893 | -47.2614 | 2025-08-28 01:30:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 19a23da4-7017-346f-901e-b27e3f1d685e | -6.896 | -43.6135 | 2025-08-28 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 044a1a1b-1490-31c1-8a72-c6f338062c06 | -10.5375 | -46.6894 | 2025-08-28 01:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 02c81568-ae2d-32b8-9293-757d3fb62d74 | -11.3334 | -43.5216 | 2025-08-28 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 40545fae-bf13-3bed-a964-e663020c96a2 | -7.3542 | -59.6476 | 2025-08-28 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| ae02660a-de72-36f4-b94d-4153ae7284f8 | -8.948 | -65.9429 | 2025-08-28 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| e012b5d3-44a8-3dd6-8866-971c6fd2aa18 | -8.9664 | -65.961 | 2025-08-28 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| b510fcd5-30c3-3f8c-afe5-feb729fdc8ce | -11.3329 | -43.5452 | 2025-08-28 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 3e50b736-a61a-3563-9b13-52c7ca242fa9 | -10.5371 | -46.7119 | 2025-08-28 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 3c34be31-16ea-3a9c-8f77-b6b6209dad7f | -3.2299 | -43.4414 | 2025-08-28 01:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |


[Clique aqui para ver as próximas entradas](README12.md)
