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
| d45dc58d-872d-31fd-90f4-a885286a5271 | -3.5563 | -51.532299 | 2024-11-25 01:01:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a652336-ed7e-3c5e-8121-66a7a88aaad2 | -2.8298 | -54.103001 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70984c81-2653-327a-a7fe-a261dc031ba7 | -2.8415 | -54.064499 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40331e08-a597-356c-afe8-a3af764ed6fb | -0.9431 | -53.211498 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5824c19-acb7-3b47-ba6e-f4764b4a253f | -4.417 | -49.704201 | 2024-11-25 01:01:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e3d2e00-68e7-350f-ac8b-bcaadea7f380 | -2.8267 | -54.089401 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5967bff-02b9-374d-b5e7-3bfae82a76eb | -3.2712 | -53.824299 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4004bf9-82ef-3de2-a9cb-57e94414fc3a | -2.7034 | -51.990501 | 2024-11-25 01:01:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fdd1ff0-39cb-3269-acf0-d1830f6ee0f7 | -3.5637 | -51.564098 | 2024-11-25 01:01:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edf81905-6a15-3621-83f7-189fe03865b7 | -3.5064 | -53.814701 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c68ac80-f420-3283-a882-ad37330cdf5d | -4.548 | -48.951401 | 2024-11-25 01:01:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 864a3107-731f-3e6a-bd5d-445228a6f1bc | 1.3795 | -55.900398 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db6eabee-9ddf-3bff-b45c-0f0755a1f359 | -1.8721 | -53.3489 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c70f55f8-b88e-3213-b454-fd14ef61dc8a | -2.5723 | -54.060101 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b08d0b4c-9fff-3564-83bc-d38e01ed0609 | -1.7267 | -53.254601 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 459b1090-7e29-3322-9874-7db013027b8b | -3.0693 | -50.946899 | 2024-11-25 01:01:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47ba3647-11fd-3afb-96e5-b28c8ab3e36a | -2.8023 | -52.997799 | 2024-11-25 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f267b8c-5f68-32f4-b03e-05de4dd07936 | -2.8153 | -54.084801 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6e00901-b950-3256-9870-ba2fc5e46f69 | -4.3779 | -48.4963 | 2024-11-25 01:01:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa2c31b3-c072-382a-b956-5a555d62137d | -2.3345 | -52.179298 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c11f656-f8e8-37be-b693-7f815feac2f1 | -1.1219 | -52.1082 | 2024-11-25 01:01:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 3058d530-7c31-3a4d-9a49-d5f7ec7281a3 | -3.1931 | -49.0588 | 2024-11-25 01:01:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e941074-cba0-3be1-8f8d-a30ce0cd2b74 | -3.5048 | -53.807899 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4133d503-0474-304a-8b39-4b447e1c2db6 | -2.7941 | -53.007198 | 2024-11-25 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c192da3-843e-3aa1-9931-fb3a08e2bd72 | -2.6146 | -54.2444 | 2024-11-25 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaef67a1-4190-3eb1-a100-e8aa869b51ac | -1.304 | -51.736198 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3f1f1ec-1308-31f7-9945-885c47e47f8b | -1.1185 | -53.390999 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 608e15db-4988-330c-a4ad-0ff0e1c4eaea | -2.7862 | -54.0481 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb2773bc-8844-3732-a2d4-d648529d53e7 | -2.561 | -54.0555 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e440a730-0f13-3272-9cfb-780206d0f76e | -2.7964 | -51.679798 | 2024-11-25 01:01:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a87e5da8-dadc-3fdd-90ac-4e737bcd805b | -3.5526 | -51.516399 | 2024-11-25 01:01:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3ac7a36-beab-337d-a07a-3f2022529969 | -2.3322 | -53.868698 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 547af98e-35f2-3bd9-8cf8-81bffc45445e | -3.5276 | -53.8172 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a98060b7-25a1-3689-aeb2-8fa48e3fb8b1 | -2.948 | -51.001701 | 2024-11-25 01:01:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 411b9f2a-f3b0-30ca-ba5f-348df6084432 | -1.7814 | -52.7314 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef0cde5c-1816-3d3b-917e-b80b884f815f | -2.8039 | -53.005001 | 2024-11-25 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abfca01d-13c4-3992-8aa7-44661be2fce0 | -1.3811 | -52.337601 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c5302ec-ddf4-30d3-8e97-5ff32043da7e | -1.3793 | -52.329899 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06dd19d0-ed50-3901-b252-97612cd3db03 | -2.699 | -52.908001 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77027b7a-c470-301c-95ef-77db9538f67b | -1.6011 | -52.576099 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 347540ff-3f3c-3155-954e-2daf8fc396a9 | -2.8121 | -54.071098 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63ff0263-ad4c-3847-bdbf-c47cb18ce043 | -21.323299 | -55.945301 | 2024-11-25 01:01:00 | METOP-C | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 29ae4d5e-8624-3078-b21d-0dd98919a96d | -3.2887 | -53.6758 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34a2c438-4cae-3ecb-8e0c-1bf0911dd141 | -3.5178 | -53.819401 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22663573-7442-3478-b635-685abffb6bd3 | 1.3666 | -55.9118 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8288d24-2de9-3b08-a880-930ed9101bd0 | -2.8404 | -54.0145 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fef30f6-765c-3278-976f-c00530174ea7 | -3.1049 | -53.998299 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70600947-79fa-34b9-97de-936c547fb3d6 | -3.6395 | -51.136902 | 2024-11-25 01:01:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31691cfb-b6f1-3c2d-8a13-1ba067ab7550 | -3.9547 | -50.8526 | 2024-11-25 01:01:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8f7a934-866b-369e-9466-d1e2eb1502b7 | -2.3225 | -53.601799 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92c6cdae-0bf0-3f47-abf2-53965895dde8 | -2.3338 | -53.875599 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7726b8b5-1130-362b-bd7f-ed754932ed0f | -2.5436 | -53.980202 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5487c3e9-20e3-32c2-aeda-c4bc1db10bdb | -3.1677 | -51.103699 | 2024-11-25 01:01:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e96ffda4-612c-3b56-976f-2b7cc2f3fb4a | -1.7797 | -52.723999 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f70b42c-ec2f-3322-9e76-6aa0a55a4800 | -2.3211 | -53.862 | 2024-11-25 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| d15fadaa-93f9-302c-aff5-8d443d692117 | -4.2604 | -48.7184 | 2024-11-25 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| e8f01158-c8d0-3884-97ff-61245284457e | 1.8398 | -55.9007 | 2024-11-25 01:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 9170cd32-2d12-35bb-90f2-0a12a27c5d56 | -3.9493 | -47.9993 | 2024-11-25 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 723d8f4a-95cf-3105-a811-daf14b588389 | 1.382 | -55.9061 | 2024-11-25 01:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| a8ef2ba4-f98a-32f4-ab7d-85c7f7be9584 | 1.8581 | -55.9004 | 2024-11-25 01:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| cb6359b9-3d18-30c8-8f11-85818e44788e | 1.8398 | -55.9204 | 2024-11-25 01:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 426ebe22-2e84-346f-b115-de0f27e24b1b | 1.3637 | -55.9063 | 2024-11-25 01:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| fb008c5b-721c-3f2d-8983-303686a077ae | -2.3394 | -53.8818 | 2024-11-25 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 0223a843-f07b-38ea-a681-0e6e529529d8 | -2.3395 | -53.8617 | 2024-11-25 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 04176e15-851f-36b0-9dc5-7c49387eef1a | -3.9494 | -47.9776 | 2024-11-25 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 415aac9e-9ddb-3c49-9f2b-a8e8ac02c4bb | -3.2872 | -51.1194 | 2024-11-25 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 53ba7094-63dc-3fd7-9a4f-1a22efe4f818 | -4.023 | -48.0827 | 2024-11-25 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 6f559b6b-d362-3c28-aabe-e058e8983090 | 1.3637 | -55.9063 | 2024-11-25 01:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 2aa34717-9332-3f23-8015-6f9fff1ff19c | -3.2928 | -45.7384 | 2024-11-25 01:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 27c03c68-f6a1-3ae3-a7ab-e9a6baa51243 | -3.9493 | -47.9993 | 2024-11-25 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 6b458b98-37de-37bf-a029-900e26b3d3c0 | -4.023 | -48.0827 | 2024-11-25 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| d2b29b50-1c26-362b-a649-28ca1a7326eb | -3.9494 | -47.9776 | 2024-11-25 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 66f5318a-758b-3ed9-97c0-68e87e116122 | 1.8398 | -55.9007 | 2024-11-25 01:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| cc84a8d4-5878-3136-a5ad-208934fc4cd8 | 1.8581 | -55.9004 | 2024-11-25 01:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| ef09a81d-8514-3305-98c8-cba5edb1d37f | -2.3211 | -53.862 | 2024-11-25 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 59a5255a-8f91-3fdf-8c49-667703c17a01 | -3.2872 | -51.1194 | 2024-11-25 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| e5867ed0-998a-3d4d-a6df-f56d018325f6 | -2.3395 | -53.8617 | 2024-11-25 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 4970a324-b207-3e44-8f9d-a7cab62c316f | 1.382 | -55.9061 | 2024-11-25 01:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 86e88575-de1b-3e5e-bbce-d02289eadf81 | -22.44468 | -47.68796 | 2024-11-25 01:24:00 | TERRA_M-M | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 16.2 |
| a66256eb-2a69-36eb-a1b2-bf58576b5ac8 | -20.22242 | -55.97116 | 2024-11-25 01:24:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 1eb34339-a39f-30d9-a4e5-f35347162b20 | -21.32116 | -55.95325 | 2024-11-25 01:24:00 | TERRA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 5519b971-2d89-3a12-aae5-ff656325bcb1 | -20.25125 | -49.67938 | 2024-11-25 01:24:00 | TERRA_M-M | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 1b3a3421-e710-340d-8848-72967e2ff0e7 | -22.43003 | -47.67331 | 2024-11-25 01:24:00 | TERRA_M-M | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 382154ad-ff94-3ea9-9765-567868f63efc | -22.37854 | -55.04437 | 2024-11-25 01:24:00 | TERRA_M-M | LAGUNA CARAPÃ | MATO GROSSO DO SUL | Brasil | 5005251 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| d494cd28-e4ae-37f6-8bdc-318cfbc20916 | -22.43306 | -47.69032 | 2024-11-25 01:24:00 | TERRA_M-M | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 7ac8d50b-b092-3926-a329-4f3d11c25d1d | -11.77858 | -54.70167 | 2024-11-25 01:26:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7011051d-6f50-3c27-bccc-88827d7a63fe | -11.77726 | -54.6924 | 2024-11-25 01:26:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 6ac0f43d-63e5-376f-a994-e25b406fac51 | -1.63764 | -53.87275 | 2024-11-25 01:28:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 35622ebc-f847-3e57-a08c-bda118fccc51 | -3.50194 | -50.46903 | 2024-11-25 01:28:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| b74019b4-6240-39e9-843f-c02f3685b512 | -2.61928 | -54.25821 | 2024-11-25 01:28:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f0141d58-8d72-3ec0-a692-8ffce4cb9964 | -3.9528 | -50.87018 | 2024-11-25 01:28:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a30ee79c-ddf9-3941-ac94-5ee5346dddde | -1.77638 | -52.73651 | 2024-11-25 01:28:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 71b49297-64df-398d-b911-e2d155e1ec4a | -3.06405 | -53.22057 | 2024-11-25 01:28:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 1aa9f2c4-ce13-3071-bada-97adb4537ee2 | -1.28983 | -51.73532 | 2024-11-25 01:28:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| fbc521e5-6a45-34ed-b437-9bfaa62c4e76 | -2.33803 | -52.17892 | 2024-11-25 01:28:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 271f4857-415d-31db-825d-f4941b4616fb | -3.04479 | -54.01923 | 2024-11-25 01:28:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5f94c6d5-10e3-33b0-bc47-cf5a38313d61 | -3.70639 | -51.77949 | 2024-11-25 01:28:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| cfff0819-e7cf-3393-aafb-521248ae65e2 | -1.73929 | -52.72582 | 2024-11-25 01:28:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 4451d9e2-03b6-3683-9d1d-552a9a481a7f | -4.26219 | -48.73554 | 2024-11-25 01:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 9de89033-063f-3642-bbcc-c8c3fc783dc8 | -2.93974 | -51.01171 | 2024-11-25 01:28:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |


[Clique aqui para ver as próximas entradas](README10.md)
