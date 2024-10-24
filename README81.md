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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40cb632f-49dd-33a4-8300-c1a2db9fd072 | -18.16966 | -56.3138 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 7065db85-2cc1-3552-9a07-8a563108f533 | -18.16736 | -56.3139 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 159ab01d-e71f-3cb7-b538-890b21d50106 | -19.577 | -56.68006 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 29.5 |
| 368ac333-e53b-379a-a50f-021ceec7161c | -19.56204 | -56.66615 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| e7b827d8-fe90-3f61-8c4d-e12eac66c3bf | -19.56033 | -56.67719 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| ab44866e-a1e0-3416-bd07-bc0619a288b6 | -19.55813 | -56.66926 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 829b5156-2b9c-31b8-acce-fc153249cff2 | -19.55756 | -56.67294 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f905d61d-d30c-3838-97ac-a9e90ad5d514 | -19.55699 | -56.67662 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 59a26d02-c062-386f-8a23-aab161ae51b7 | -19.55643 | -56.6803 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 262fd671-ace6-335b-82fe-2f2f7762ba0a | -19.55536 | -56.665 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| cc55019f-84f9-3ca4-91fd-4d56ef1ceeb3 | -19.5548 | -56.66868 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 77a35563-6ca9-37c1-a38b-31ecb6de09c8 | -19.55415 | -56.69502 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 70b99144-c58e-3088-8154-f091379e70e7 | -19.55146 | -56.66811 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 627916e4-7c66-3270-97a1-9f4830b3912f | -19.55089 | -56.67179 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| d9267201-affb-3cf9-b325-91a82a6aa9a0 | -19.54813 | -56.66753 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c5e335b2-799a-3418-b1f6-fbc275d9def8 | -19.54756 | -56.67122 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 79730362-2469-3229-bf81-145b9f0a1512 | -19.54642 | -56.67858 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8f348972-7762-3f47-84de-a7e897cb6bc4 | -19.54634 | -56.70124 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 332a9c52-1d47-3503-b063-8158dcc281cb | -19.54472 | -56.68962 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a612b98f-3e30-3bdb-9b49-b5aff2e54f90 | -19.54422 | -56.67064 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 65f74293-72bb-3b24-8c96-b5dcf9dfbcaa | -19.54301 | -56.70066 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 1f62f29c-c85c-35cb-a530-3c00994e1ea5 | -19.53967 | -56.70008 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 2e5786ca-dfa7-39fd-83fa-9c78e34672bc | -19.53918 | -56.68111 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| a49692ab-30f6-3cb1-a8f8-3e2434af45ab | -19.53805 | -56.68847 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 154e28e9-8eb5-37f0-a0aa-d61297337aaf | -19.53748 | -56.69215 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 95ece0fe-ad6f-3282-86b5-3b350d582402 | -19.53642 | -56.67686 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 142658bd-7f77-3e3b-a836-ec0fab84d01d | -19.53634 | -56.69951 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.5 |
| d92d815c-e091-3a0c-b1ca-0064570f1402 | -19.53535 | -56.66156 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c99df319-91e6-3eec-a23b-0b1528ee34a9 | -19.53308 | -56.67628 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| b3020333-a759-3d49-b232-77146f70c79a | -19.52967 | -56.69836 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| e18c77f4-09fe-34c3-bfa3-9b0d22c9d499 | -19.51571 | -56.66642 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| a32ffa5c-0c59-3eaa-9c38-d9e63a89e50c | -19.50961 | -56.66159 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 45ad9f25-1a67-34e0-bcf8-5b9b16ec5169 | -19.5057 | -56.6647 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| a8c3778a-33dc-34dd-ab13-4143909350ac | -19.50237 | -56.66412 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 3842fe8c-24a4-360e-9642-7503d9929a31 | -19.57643 | -56.68374 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.2 |
| 03f5aba6-401c-38b9-887c-814afa65fd12 | -19.56586 | -56.6857 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 22.6 |
| 4c9a1000-4162-3f51-9850-63bd4832b7fe | -19.5609 | -56.67351 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 397f124e-a417-39b1-9ee4-41ac0c724801 | -19.55976 | -56.68087 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 3abd471e-b63f-35a2-b68a-b00c43fa3109 | -19.55927 | -56.66189 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 39540355-7a5a-3970-b53c-e59f57660021 | -19.55529 | -56.68766 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 100d534c-cbde-319b-9f73-ba6929763a48 | -19.55195 | -56.68709 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c6f5422e-db14-3090-8958-6a2e82174399 | -19.55138 | -56.69077 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 45f4c640-9918-3365-8e60-7b5a3c82bcb3 | -19.55082 | -56.69445 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b0afa8ff-94bf-3780-b7c8-830ca03b21dd | -19.54926 | -56.66017 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| fd2cd664-f3f8-374e-b540-64e64b617dbb | -19.54748 | -56.69387 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7fcc917b-fe4f-360a-b2f1-7a28adfabe37 | -19.54699 | -56.6749 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 18d5388e-7f83-3976-a24e-45aa316f27e7 | -19.54691 | -56.69756 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 16265a2b-a253-3032-af46-127ddd235fd0 | -19.54415 | -56.6933 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| dcfdf418-567f-31ff-ac53-700b08b2e574 | -19.54358 | -56.69698 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 48d9f676-9a00-368b-b993-cd1578bc629d | -19.54252 | -56.68168 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| cdf80bdf-9b9d-37d2-a52a-79110ac192e7 | -19.54195 | -56.68536 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 098d243d-c042-3168-9a2c-0e810e0bcfa2 | -19.54138 | -56.68905 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 844b07af-6135-3b2e-ae9e-b1946bab22e5 | -19.54089 | -56.67007 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 2ef71bc1-9707-3a19-b799-794a812f65bc | -19.54024 | -56.69641 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5131014a-bb35-38f4-9439-27ad9e0eaae7 | -19.53869 | -56.66213 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 09202e9d-a75e-3eab-88bf-bc45e19db36c | -19.53699 | -56.67318 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| e4a1f76a-c088-39c9-96b2-4c5f8087b7af | -19.53691 | -56.69583 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0304daf6-8536-3032-8813-50a4fbac543f | -19.53585 | -56.68054 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 6252aa9d-18c7-3b25-9232-eceff0cecfc5 | -19.53365 | -56.6726 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4351cd81-6ae4-39be-b20e-859f2a07d27f | -19.53358 | -56.69526 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| e25b140a-1a40-3df7-8a42-700d7beb0f80 | -19.53081 | -56.69101 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| e80ebd31-d4dc-3ab7-9443-cc14e37714fa | -19.53024 | -56.69468 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 889dcfa9-3f3b-33bd-89d6-8b2284280009 | -19.52868 | -56.66041 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1e044f33-bb30-3d2b-a1d3-38fb8cc571c8 | -19.51294 | -56.66216 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a72e8e9b-32c2-3296-a59b-3392b436037a | -19.51237 | -56.66584 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2c4191e8-9a44-3ac2-adc5-c2efe29cb06c | -19.50904 | -56.66527 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 36b94eda-4ad3-3d1b-9d44-18217c251ff0 | -19.50294 | -56.66044 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| ad107998-034a-3efe-85c0-b8530a94afc0 | -19.49903 | -56.66355 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 1cd7a4eb-6f5e-3f90-8c41-e6a2bad2725d | -19.69059 | -56.77857 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c95ac1f3-4cc5-31ff-bac9-f022a774fe95 | -19.68726 | -56.778 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 82ecdfe4-233d-3c7a-aadc-5586068a297b | -19.68002 | -56.78053 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 051e33cf-0a86-384f-bb88-3226742d04b0 | -19.6725 | -56.85098 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 3f7dd215-6c2d-33eb-94d0-1781030eb3cc | -19.66612 | -56.7819 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 25c4589d-ba2b-3ce4-b6ce-23f916a0dbcc | -19.66526 | -56.8535 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f1abe288-2661-34a9-b9b7-e5eaa776fe14 | -19.66336 | -56.77765 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 36613a1e-1c33-3824-802f-e420bd6c94ae | -19.66279 | -56.78133 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bb841ddf-96c3-3a05-9ef3-54c84de664d6 | -19.66222 | -56.785 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5843c923-a922-3ff7-8c1a-940affef7607 | -19.66136 | -56.8566 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 99ca928a-a113-3282-adee-0a4d42826e17 | -19.66051 | -56.79604 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2523fafb-9b5b-34ed-90c4-ff21f035bac3 | -19.66003 | -56.77707 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 5374bd6b-d313-37cf-be87-58b50c96ca10 | -19.65994 | -56.79972 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 54d661d0-a57b-3ee3-af78-cddca6506b73 | -19.65946 | -56.78075 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8ef27bde-6d75-35cf-a4af-bd89f07fdefb | -19.65889 | -56.78443 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 333555b7-9c5a-3186-ab8b-2669179f607a | -19.65803 | -56.85602 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| b61a441f-2d80-3c0e-afac-2157f1642304 | -19.65797 | -56.988 | 2024-10-24 04:59:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3b5f0b00-8c13-32e0-bcae-be64f162789f | -19.65775 | -56.79179 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1feae974-69f2-3615-9940-db85c897aeaf | -19.65718 | -56.79546 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 853a7ff7-5470-3d18-baf7-f055743175f4 | -19.65669 | -56.7765 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 42c3f6e0-d675-38cd-8317-2d3ff7415e04 | -19.6566 | -56.79914 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1c150c95-0468-3438-8006-3c350436684c | -19.65612 | -56.78017 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 708289ce-7278-306a-957d-ddfb06cacaeb | -19.65603 | -56.80282 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6dbc792f-c423-33c9-b3e4-16cb79d7caa2 | -19.65555 | -56.78385 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 14c55a71-12ee-3445-8190-4e3af3acd7f2 | -19.65498 | -56.78753 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b02ec1c5-04ed-3c1a-a359-348020337012 | -19.6547 | -56.85545 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 033945b5-6d2b-360d-853d-b495c290cb2c | -19.65464 | -56.98742 | 2024-10-24 04:59:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a1e7642d-a3d4-32ee-b43f-77e50a2f6122 | -19.65441 | -56.79121 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 59735559-c60b-3dc8-bd59-983a7411598e | -19.65407 | -56.99109 | 2024-10-24 04:59:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a88193d1-3894-367c-9221-b56e65b834e4 | -19.65384 | -56.79489 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4f73f3bb-9048-3c29-a544-94685deac016 | -19.65336 | -56.77592 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.6 |
| da7e3f1f-cb6c-3502-8d6a-80eccfda9c80 | -19.65327 | -56.79857 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |


[Clique aqui para ver as próximas entradas](README82.md)
