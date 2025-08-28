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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa5eb185-a7f1-3e68-a8ca-50d045f558d1 | -9.1154 | -65.7886 | 2025-08-28 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 474.9 |
| e456952e-6dd3-3116-8284-544431f4491d | -6.9129 | -62.9366 | 2025-08-28 02:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 47f714e6-f79e-3957-8963-7fb09cc327a4 | -10.8236 | -60.7633 | 2025-08-28 02:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 191d554b-b3e8-36d8-b07c-2e301bcd9f42 | -6.896 | -43.6135 | 2025-08-28 02:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 2f9b3d83-8334-3fd5-ba48-e58df16f7812 | -9.1153 | -65.8073 | 2025-08-28 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| eb486590-33cd-3a4a-bc99-6322352ec101 | -10.5371 | -46.7119 | 2025-08-28 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 184.3 |
| aff0b518-73ec-3093-99ad-72639a4a28be | -9.1339 | -65.788 | 2025-08-28 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 285.2 |
| 6f2fafed-9131-3bbc-aed6-0886448a7061 | -11.3521 | -43.5423 | 2025-08-28 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 5997c3d8-4831-3b3c-a04e-6903b5a11006 | -17.7423 | -42.6837 | 2025-08-28 02:10:00 | GOES-19 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 56.9 |
| e71b71e1-b976-3064-90de-1272f8fbc9ea | -8.9479 | -65.9616 | 2025-08-28 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 76dcbb0e-b541-3672-b20c-98b0f5408e66 | -10.8047 | -60.7837 | 2025-08-28 02:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 2276d42b-310f-3a06-915e-207bf692d2f4 | -11.3329 | -43.5452 | 2025-08-28 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 0de6a74f-3a52-308b-98af-ced45a170a28 | -7.3542 | -59.6476 | 2025-08-28 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 1d8cda1a-e296-3932-8e0a-e0ba5a1e50de | -8.9664 | -65.961 | 2025-08-28 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 4bcf9597-015d-3abe-ad7f-932d429fd0e9 | -12.9662 | -44.5781 | 2025-08-28 02:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| f7d001f5-1337-35ca-9df9-4af87cf93e8a | -6.8774 | -43.5919 | 2025-08-28 02:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 5befdfb6-1e25-3665-b858-9347d7d9ca15 | -10.4549 | -57.9576 | 2025-08-28 02:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f877c8cb-17ea-329a-9fb0-b59a78e52633 | -13.1837 | -45.2865 | 2025-08-28 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| c3f42e78-7f3d-31f0-81b9-66a5a5320fb4 | -10.4738 | -57.9366 | 2025-08-28 02:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| c12e0998-30fc-3dac-b735-2e8f0db07778 | -9.406 | -60.5711 | 2025-08-28 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| c528e0a8-001a-3dcc-be90-c0523e06d6f7 | -9.1155 | -65.7699 | 2025-08-28 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 285.0 |
| 54e97bfa-3fd9-39e8-82de-5648efde7c36 | -10.8235 | -60.7826 | 2025-08-28 02:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 17e39379-1090-3514-a1c8-c74e07bdcca2 | -9.1363 | -65.2835 | 2025-08-28 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 88f4375f-6741-3ce2-8e20-a06806e55e6a | -7.3357 | -59.6484 | 2025-08-28 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| e40e3ba4-48a4-3cd2-9f09-aa7e9ca4c80d | -4.7893 | -47.2614 | 2025-08-28 02:10:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 0d27c2c0-91bf-3eb7-8959-c9b4231c3af1 | -9.134 | -65.7694 | 2025-08-28 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 199.8 |
| c8a114d8-1afa-3eb3-97e6-b271469d25a3 | -11.3334 | -43.5216 | 2025-08-28 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| cfd43a57-5282-3d4a-a901-54ff42526a83 | -10.4736 | -57.9563 | 2025-08-28 02:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 59e7cf31-110e-347f-b4df-3b4b56c73fea | -6.8772 | -43.6152 | 2025-08-28 02:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 186.7 |
| 46938b56-6f12-303c-8a6c-067a6a229f04 | -10.8235 | -60.7826 | 2025-08-28 02:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| d2c7b3db-27a9-3a1f-b53c-750404a564bc | -6.1672 | -47.2858 | 2025-08-28 02:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 09f9378c-7b87-3815-a6bd-729c64644cf5 | -9.0786 | -65.7338 | 2025-08-28 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| a2484137-667a-3451-af0b-f05b10f1f8ee | -10.4736 | -57.9563 | 2025-08-28 02:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 9a2e995f-077a-35c8-897d-8886cb3fa490 | -23.6978 | -51.7916 | 2025-08-28 02:20:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 81.4 |
| 0c553b61-2cde-32b1-b1e5-d0acbb1818d0 | -6.8774 | -43.5919 | 2025-08-28 02:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| c258f414-34eb-3203-af30-7fb2b8cecba4 | -6.8772 | -43.6152 | 2025-08-28 02:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 182.4 |
| dbd627e3-a3b7-3ceb-bb48-6bdb3d08990d | -9.134 | -65.7694 | 2025-08-28 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 189.2 |
| e6ae70c1-c086-3334-91a6-d70d7153aabf | -8.9479 | -65.9616 | 2025-08-28 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 1a5f140e-9d5d-30d9-8f51-b9c6bd6cd2ad | -6.9129 | -62.9366 | 2025-08-28 02:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| fc61599c-86c9-30e7-be18-d102467abd93 | -11.3521 | -43.5423 | 2025-08-28 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 205.9 |
| ed0c274e-b4bf-32d3-8321-19288f94be56 | -9.1339 | -65.788 | 2025-08-28 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 256.1 |
| e231036b-b35a-3646-a6a6-1b18c1e92742 | -13.1837 | -45.2865 | 2025-08-28 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| d3ce8615-c556-3c27-9e53-238878025662 | -9.0969 | -65.7892 | 2025-08-28 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 8388ab41-16b6-3515-ba5f-264bd2934b4c | -4.7893 | -47.2614 | 2025-08-28 02:20:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 87.7 |
| cbce19f9-1b41-3cdb-abc6-fdf9a87cc087 | -12.9662 | -44.5781 | 2025-08-28 02:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 43958124-86d8-3939-8b6b-e95421d52560 | -8.9664 | -65.961 | 2025-08-28 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| ae9431d6-30c4-334a-a5d8-01b702c7d234 | -10.4549 | -57.9576 | 2025-08-28 02:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| c501ba29-4abb-372d-b2a1-5fb96ed19df1 | -10.8049 | -60.7644 | 2025-08-28 02:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| a925a2dd-b8b2-3a5c-bdcf-4ceb57bed359 | -23.6767 | -51.7964 | 2025-08-28 02:20:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 62.8 |
| abc1618e-aa87-3532-a00e-36fc8756d239 | -10.8236 | -60.7633 | 2025-08-28 02:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 3cc5a793-5b2d-38f9-b046-f44c3df15c91 | -6.896 | -43.6135 | 2025-08-28 02:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 104.9 |
| b36f921f-5877-32c0-a2ef-4a90c1d26bc1 | -9.406 | -60.5711 | 2025-08-28 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 0d9e4b36-e580-3b7d-8572-cb244f9afb48 | -9.1154 | -65.7886 | 2025-08-28 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 503.7 |
| 4bad037d-9750-39b3-88a6-092a1d0d00f9 | -11.3329 | -43.5452 | 2025-08-28 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 269.7 |
| 0e92c8b3-335c-3196-8526-f2b7797855f3 | -11.3334 | -43.5216 | 2025-08-28 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 4dcc9fac-ca05-3b60-8479-1f75e617709d | -9.1155 | -65.7699 | 2025-08-28 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 320.4 |
| 96d7882f-9b2d-366c-9bb1-bd8aabc58c5d | -10.8047 | -60.7837 | 2025-08-28 02:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| d9d8477f-340a-3768-bfb0-7f8cb6cd9b28 | -10.4738 | -57.9366 | 2025-08-28 02:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| fdc2d28b-0b1a-3c87-b13e-5a90339c9927 | -11.3526 | -43.5187 | 2025-08-28 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 92592d11-f57d-3cc0-a599-64be4e75c75f | -9.1363 | -65.2835 | 2025-08-28 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 7d9de1d5-11d9-3fa9-90b7-2f51edc8834c | -7.3542 | -59.6476 | 2025-08-28 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| f4fbbc19-a9e3-360f-ac88-88c24144dc32 | -9.0969 | -65.7892 | 2025-08-28 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 17723b2e-4eb7-3101-be79-0f6f6f085096 | -9.406 | -60.5711 | 2025-08-28 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 40cef773-c7c8-30ee-bce3-770df8801003 | -9.1154 | -65.7886 | 2025-08-28 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 420.4 |
| 025a89ff-3da4-3c24-b43a-e8bb73e85818 | -4.7893 | -47.2614 | 2025-08-28 02:30:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 9fa626bd-74d3-3fbb-977c-1ed9dc695fd3 | -9.134 | -65.7694 | 2025-08-28 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 264.7 |
| 67b5afb2-53aa-372f-b377-9a06732996c9 | -6.8772 | -43.6152 | 2025-08-28 02:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 191.9 |
| 19ae8496-9550-331b-a92d-881be031155a | -11.3521 | -43.5423 | 2025-08-28 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.6 |
| cdaf7dca-506a-3120-9ecc-6548d46e6139 | -9.1155 | -65.7699 | 2025-08-28 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 279.0 |
| 964182b0-eea2-352e-bc8a-5a39a350c42d | -8.433 | -41.4559 | 2025-08-28 02:30:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| 6eba430f-b1ed-31fd-a215-91fa6da32c74 | -10.4738 | -57.9366 | 2025-08-28 02:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 4e7a1d55-a483-3ea7-9d6b-050b4d2bea66 | -6.9129 | -62.9366 | 2025-08-28 02:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 597c8ad8-cf6c-39f4-869d-1e87b79cd48f | -8.9479 | -65.9616 | 2025-08-28 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| d246496e-a79c-3c18-af91-8bc425248d32 | -6.896 | -43.6135 | 2025-08-28 02:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 6123f256-8802-3a09-a689-3bfc8d471231 | -9.1339 | -65.788 | 2025-08-28 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 382.0 |
| 5335976e-2dcc-3557-ba41-3cd89696c0cd | -4.8079 | -47.2604 | 2025-08-28 02:30:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 534473c2-2534-3ec4-b04b-b8c0942f90d3 | -6.8774 | -43.5919 | 2025-08-28 02:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 22296081-0152-3b93-897d-790f387b1c67 | -8.948 | -65.9429 | 2025-08-28 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| d06fbfe6-761c-3ad7-a01a-c800544de4da | -11.3329 | -43.5452 | 2025-08-28 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 944e22fe-54d9-334b-a777-169b70b4812c | -8.9664 | -65.961 | 2025-08-28 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 8babe31b-2b25-33db-82fa-87ef8614b1ed | -7.3542 | -59.6476 | 2025-08-28 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 07b51d85-a558-3353-bbf3-1bd5ca3fc9d8 | -12.4396 | -45.9551 | 2025-08-28 02:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| ab3de0d8-4057-3771-9f55-b448bbdaec7b | -13.1837 | -45.2865 | 2025-08-28 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| bf46e61c-d62b-374c-9108-44c478bf8df7 | -11.3334 | -43.5216 | 2025-08-28 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 58a2ba89-4003-39e2-92b4-1dbc71604bdb | -12.9963 | -56.9 | 2025-08-28 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 4c7872c6-4a18-39dd-9f64-c44b8e8a64da | -11.3526 | -43.5187 | 2025-08-28 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| b1b63228-236c-3fc8-b66d-ed1df753eae5 | -7.3955 | -39.6845 | 2025-08-28 02:30:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 59.5 |
| 0e2856b4-a9b6-3e3e-9422-0e80be97082c | -10.4736 | -57.9563 | 2025-08-28 02:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 57b66d11-c4b8-39a8-a187-f69b9e246582 | -9.1359 | -65.287498 | 2025-08-28 02:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a6d86025-0d2e-3a37-b4f7-459f8a957b1b | -8.9663 | -65.9785 | 2025-08-28 02:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ba7caa4-174b-3c48-8a09-74b21fcee311 | -9.1337 | -65.791199 | 2025-08-28 02:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bc8bb4fa-f50e-3227-ac13-fa6827871a1e | -9.1182 | -65.771103 | 2025-08-28 02:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2126eaf8-60d8-3247-9d18-766b009559a8 | -9.1086 | -65.773598 | 2025-08-28 02:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3be38c10-a329-35d2-ac4e-c919cdf5a79e | -9.0871 | -65.730598 | 2025-08-28 02:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ad67b08a-ef91-3847-8333-c882f8e21038 | -9.13 | -65.816299 | 2025-08-28 02:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d805568b-4481-3703-9a8f-8f37330359fc | -9.1241 | -65.793701 | 2025-08-28 02:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6b6897d4-a7f9-3244-b517-87cbd054cc97 | -8.9606 | -65.956299 | 2025-08-28 02:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 853d9789-cb82-3dfa-83c3-5febaddd021d | -8.9548 | -65.934097 | 2025-08-28 02:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f50fcf2f-afec-3771-b615-330e30bf0d25 | -8.9567 | -65.981003 | 2025-08-28 02:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0a5f0762-d266-3b3f-80b9-d1996a878313 | -8.951 | -65.9589 | 2025-08-28 02:33:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README16.md)
