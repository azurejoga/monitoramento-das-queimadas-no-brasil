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

## Dados Diários - Página 197

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac42d106-9b4d-34b9-b3ab-7b4027ff9263 | -16.86975 | -55.83848 | 2024-10-02 06:29:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 103.2 |
| 7d705ee9-5def-3d30-8285-65e7b37bfad3 | -16.83195 | -55.89977 | 2024-10-02 06:29:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| f93d1225-b95c-3f4e-bea3-c79312a4b216 | -16.82209 | -55.89125 | 2024-10-02 06:29:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 100.8 |
| 35bfe019-690b-3d9f-b03e-be699d916de3 | -16.63814 | -57.19572 | 2024-10-02 06:29:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.1 |
| 909781cb-1127-38c4-9e1b-8acf0c83043c | -16.63541 | -57.22099 | 2024-10-02 06:29:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.8 |
| faa01b37-cd9a-3bf6-a239-45990a05adf7 | -16.63325 | -57.18995 | 2024-10-02 06:29:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.7 |
| d7947b01-0c09-3569-bc32-18f3a2463314 | -16.63035 | -57.21518 | 2024-10-02 06:29:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.1 |
| df932457-ff9c-33e4-87b7-bfbaf3ae7a7b | -16.62401 | -57.19408 | 2024-10-02 06:29:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.7 |
| b3d40dd1-901c-3337-aaf6-a59c02b3e315 | -16.62131 | -57.21935 | 2024-10-02 06:29:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 38.6 |
| 99147b54-9f14-33f4-8402-94800e5e60a6 | -16.5165 | -57.29589 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.2 |
| 07cd3966-1f8a-3e91-b674-f2506cec2157 | -16.5096 | -57.27723 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.2 |
| b4f23e0c-22f3-3acf-9a3c-4257d4b557cb | -16.50695 | -57.30208 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.5 |
| 6da9db12-b269-3ef9-8687-1e8340b0cded | -16.46087 | -57.41348 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.9 |
| bdc8f842-c7be-3837-98c6-67d1253c2072 | -16.44702 | -57.4119 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 33323e30-d7f7-3d15-a540-2ce9eb79fb20 | -16.44433 | -57.43617 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.6 |
| 6cac2148-feb1-3f69-91fb-ffb5af9544ba | -16.43755 | -57.43022 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.2 |
| 6ec91fa5-9ab8-3b5c-8df4-2ddd4115a5c1 | -17.12417 | -56.73669 | 2024-10-02 06:29:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.8 |
| 168782b7-a391-3201-b1a0-1efb7b8019b8 | -17.09168 | -56.76138 | 2024-10-02 06:29:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 138.6 |
| 217689e1-8394-3c0f-aabf-c2ab77c8fd91 | -16.91133 | -57.69091 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.4 |
| 1e92da38-18e5-3082-91b3-941ccecb8a0b | -16.90866 | -57.71429 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 0d93b0dd-7c49-3d40-9a9d-5b4955f1c828 | -16.89769 | -57.68932 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.7 |
| 603cc2ba-ad25-3d4c-93a8-814f90d33efd | -16.89505 | -57.71269 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.8 |
| aef395e7-ffd5-3fa8-841c-e51681cdd1ea | -16.76605 | -57.36956 | 2024-10-02 06:29:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.9 |
| f5a3ce19-e5e6-3b0d-8191-4c26e988bc26 | -16.71878 | -57.4138 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 39.1 |
| 5bf0e86d-36a6-3f41-b8b9-153d473e8a03 | -16.69451 | -57.329 | 2024-10-02 06:29:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.9 |
| 226c037b-4880-38f0-9391-8d45d32c04fb | -16.68493 | -57.33511 | 2024-10-02 06:29:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.0 |
| 470da90b-d75c-3184-8422-60fcdea7f74e | -16.67772 | -57.35209 | 2024-10-02 06:29:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.4 |
| d677260b-63f4-3304-a27a-a677e7904beb | -16.18731 | -58.43517 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.4 |
| 72000770-7875-30a1-b5d0-f8b170d83fed | -16.60646 | -58.19857 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 657bf5aa-c352-3f47-b697-90a2105350e6 | -16.60392 | -58.21976 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 221.5 |
| 175d2c80-267b-3659-8b08-8e38ca3ae0a9 | -16.60361 | -58.20551 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 172.2 |
| 0fbd22f9-7f73-3c11-953f-e81ee0a389c1 | -16.60141 | -58.24071 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| 7e7d319e-b105-39fa-ade9-b1ce7299dfb8 | -16.60123 | -58.22676 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 372.8 |
| 9caf556f-90c9-3359-b1e7-0354a9339633 | -16.59343 | -58.1969 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.4 |
| 55433487-b87c-3616-afcd-34fc99c7774b | -16.5909 | -58.21817 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 816.2 |
| 9394e23b-a687-37ca-8ce3-ae38850a88b8 | -16.59058 | -58.20384 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.5 |
| e86ff542-2a6d-368b-a8ed-08416e091035 | -16.58842 | -58.23907 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 295.7 |
| 335264ee-6a18-3491-937d-1ce909b444e7 | -16.58822 | -58.22508 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 484.3 |
| bb3a2b81-1f32-3697-8374-29cd2140c828 | -16.58591 | -58.24594 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.4 |
| b0222e2b-328f-3e1d-afb1-90f4e3dfc0ee | -16.57791 | -58.21638 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.3 |
| 4dfe620e-ae6e-3764-919e-377625efa763 | -16.57544 | -58.23738 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.9 |
| bde40426-9d43-3cb9-88dc-bb808f2f0c35 | -16.18969 | -58.41523 | 2024-10-02 06:29:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 8e40546d-fac3-3b11-9e9b-c028e1cc13b8 | -12.6484 | -63.1214 | 2024-10-02 06:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 2336d9bc-e6f7-3fef-8ba4-6594061f9a36 | -12.8424 | -62.5333 | 2024-10-02 06:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 0f1ea058-bb9b-3cc9-9c92-cdf764e0a79a | -12.8614 | -62.5321 | 2024-10-02 06:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 06722c53-f1bf-3f0e-82b2-79414a539515 | -12.8615 | -62.5129 | 2024-10-02 06:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 81914156-7782-3116-a699-855d28a74fe2 | -12.8802 | -62.5503 | 2024-10-02 06:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 23b01822-ec47-3550-a869-479e59193e67 | -12.8803 | -62.531 | 2024-10-02 06:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 189.2 |
| 197b8091-8157-3607-8a77-4ad25fa5eb31 | -12.8805 | -62.5117 | 2024-10-02 06:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| e392e1af-99b4-31c6-a821-1502a79b20fa | -16.4533 | -57.4392 | 2024-10-02 06:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.3 |
| 790f64a0-cdcc-397f-b7db-990027f6ba23 | -16.7265 | -57.4287 | 2024-10-02 06:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.7 |
| c400064f-95a4-3b06-9c78-2c3595525d02 | -16.7452 | -57.4878 | 2024-10-02 06:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.1 |
| f102d7a1-c34b-37be-9735-3019ed04ce1b | -16.7461 | -57.4265 | 2024-10-02 06:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.1 |
| 65b81a1f-d82d-3892-8302-c15e88199075 | -16.8292 | -55.9152 | 2024-10-02 06:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 92.3 |
| 355f0a38-1bc4-3127-85c3-a9f681e2337b | -16.8295 | -55.8945 | 2024-10-02 06:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 104.4 |
| 894c5448-df4b-31b6-8fd0-bef4b3520980 | -16.8695 | -55.848 | 2024-10-02 06:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 142.2 |
| f8b3b05a-f28e-361f-9de3-5ac1fea0a9a0 | -16.8698 | -55.8272 | 2024-10-02 06:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 95.3 |
| 929da342-a18a-368f-8c28-a6c951fd9e4c | -16.8891 | -55.8455 | 2024-10-02 06:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 175.7 |
| 78d36ac7-6388-3390-bda0-2f91040631cf | -16.8894 | -55.8247 | 2024-10-02 06:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 107.7 |
| b5d0a14d-1ebd-3c76-a310-0296586a3268 | -16.898 | -57.7153 | 2024-10-02 06:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.3 |
| e84bc545-b557-3c42-aed9-ba53c7d0d735 | -16.8983 | -57.6949 | 2024-10-02 06:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.5 |
| ff1d73fa-270c-3588-a5dc-737635106435 | -16.8986 | -57.6744 | 2024-10-02 06:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.1 |
| 0e1a9833-b214-361b-84fe-8daf881ed7b7 | -16.9176 | -57.7131 | 2024-10-02 06:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.9 |
| 70bf8a0f-c2da-3185-a0ff-2fbbfb4bf41f | -16.9179 | -57.6926 | 2024-10-02 06:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.4 |
| f8fda78d-fcdd-367f-88d6-1c35cf2e2590 | -17.1288 | -56.7455 | 2024-10-02 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.9 |
| d27ca8f9-d1e6-3549-b8c8-97b90f35c9d2 | -17.1091 | -56.7479 | 2024-10-02 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.9 |
| d695d0e2-f674-3e01-9f5a-139aab4a7955 | -17.1088 | -56.7685 | 2024-10-02 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 130.2 |
| 22e6179e-f002-36bf-bce4-703d53293d63 | -17.0892 | -56.7709 | 2024-10-02 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.5 |
| dd4ea340-ecd9-32ff-859d-368c48d7f134 | -17.0895 | -56.7503 | 2024-10-02 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.1 |
| ae2027b0-3ea0-36db-b6b9-8dd1b6e01ee7 | -17.2167 | -56.177 | 2024-10-02 06:36:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.1 |
| f606ae19-95a9-3d7c-a8d4-180c0676d469 | -17.2171 | -56.1562 | 2024-10-02 06:36:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.7 |
| 2d8b6825-d309-3469-998f-006a0c194ea0 | -17.2361 | -56.1952 | 2024-10-02 06:36:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.7 |
| f4a1e9d1-261b-342c-bef7-fe350424e6be | -17.2364 | -56.1745 | 2024-10-02 06:36:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.3 |
| ed7b36b3-04ab-37cb-94ce-370341ec6958 | -17.2557 | -56.1927 | 2024-10-02 06:36:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.0 |
| a1968b97-209e-3614-bea0-afe0cae71606 | -22.3505 | -49.306 | 2024-10-02 06:37:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.5 |
| 4248aabd-185c-30f5-898a-48cb1fe136e6 | -22.3713 | -49.3011 | 2024-10-02 06:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 204.7 |
| d665a7e6-3679-36ed-b481-5bdbdf9db0e8 | -22.372 | -49.2777 | 2024-10-02 06:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 139.8 |
| bdde9942-a32f-3f76-aa04-18b8afff4351 | -22.3922 | -49.2961 | 2024-10-02 06:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 152.6 |
| c187593e-44d7-3195-9335-23165836401a | -22.3929 | -49.2727 | 2024-10-02 06:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.4 |
| 788a3f99-5611-3aad-8a7c-2e23208b40d2 | -9.9367 | -64.9179 | 2024-10-02 06:46:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 71f6758c-9b7c-3cc1-9bef-a6913d056fce | -12.6484 | -63.1214 | 2024-10-02 06:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| cfc76ec6-80a6-3841-81f1-9af9d172f23c | -12.8424 | -62.5333 | 2024-10-02 06:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 36.5 |
| e1e3f432-acbe-3a87-a2bc-fdc62f2456b1 | -12.8593 | -62.7826 | 2024-10-02 06:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 18341b29-d9b1-3010-bc43-4d87f37be590 | -12.8614 | -62.5321 | 2024-10-02 06:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 032ef478-6e30-3d7d-896d-602f26a7aa76 | -12.8615 | -62.5129 | 2024-10-02 06:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 69.2 |
| c5bad235-39d4-3c74-886d-67cdaed3b8d0 | -12.8803 | -62.531 | 2024-10-02 06:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 174.4 |
| b4f963c2-dc99-3bed-997f-e6d1a402b42f | -12.8805 | -62.5117 | 2024-10-02 06:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 83c27527-44fc-34b0-a389-2a29721bd166 | -15.5486 | -56.8873 | 2024-10-02 06:46:34 | GOES-16 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 73f39067-d52e-394b-b373-0d68aa44091d | -16.514 | -57.2896 | 2024-10-02 06:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.9 |
| 06bed3c7-b4a6-3eab-a76a-173f3a82e30e | -16.6322 | -57.2147 | 2024-10-02 06:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.2 |
| c8a38b12-04d4-353d-97fd-5f0a12b7f44c | -16.8986 | -57.6744 | 2024-10-02 06:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.4 |
| adcb3a4a-520a-3927-b361-3fac5d23efb8 | -16.8292 | -55.9152 | 2024-10-02 06:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 89.0 |
| b7d07bc0-61aa-3ba0-9d87-58a6ead9b184 | -16.8295 | -55.8945 | 2024-10-02 06:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 108.3 |
| 1401e7a4-616f-329d-9cff-a46e641f4161 | -16.8695 | -55.848 | 2024-10-02 06:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 154.2 |
| 58ca528a-9987-3126-a43b-f48de937fe3d | -16.8698 | -55.8272 | 2024-10-02 06:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 100.9 |
| cab9c531-e6d3-3127-b152-c009addeee32 | -16.8891 | -55.8455 | 2024-10-02 06:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 223.1 |
| dbcffa7f-993c-34ea-9d90-bd8e47442cf6 | -16.8894 | -55.8247 | 2024-10-02 06:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 131.6 |
| dd8dde28-6f8d-3058-ad51-13852a43a539 | -16.8787 | -57.6971 | 2024-10-02 06:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.9 |
| cb58a7e4-c5f2-3d14-a906-63619f99af71 | -16.898 | -57.7153 | 2024-10-02 06:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.9 |
| e362fb80-4181-3bb9-b529-41608ad5191d | -16.8983 | -57.6949 | 2024-10-02 06:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 135.0 |


[Clique aqui para ver as próximas entradas](README198.md)
