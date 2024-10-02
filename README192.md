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

## Dados Diários - Página 192

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78495b02-ee13-3454-b7bb-0236e55064a6 | -18.71832 | -57.33805 | 2024-10-02 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cc435167-092a-3264-90a5-650890b6609b | -18.71757 | -57.33703 | 2024-10-02 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| be814de7-8209-3b7a-9848-4e9497f24f57 | -18.7172 | -57.34032 | 2024-10-02 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0751dba1-0688-3190-9f61-859afc43a279 | -18.71311 | -57.33741 | 2024-10-02 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 55a9a34f-a811-34d9-9f95-ae55730303c1 | -18.69926 | -57.31146 | 2024-10-02 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 392e763a-7683-3fcc-baf1-daf94a5a1f8a | -18.69889 | -57.31476 | 2024-10-02 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| bf0e3825-7d80-3a6f-819f-1e364e9dea59 | -16.59 | -58.26 | 2024-10-02 06:03:52 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d3f31776-a56e-3720-b517-41e244c3505d | -9.9367 | -64.9179 | 2024-10-02 06:06:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.5 |
| fdb0b8d7-a3c4-3e51-8c4b-513d455426e9 | -12.6484 | -63.1214 | 2024-10-02 06:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| bbecfa0f-3504-3ffe-ba50-22cdf89b936a | -12.8424 | -62.5333 | 2024-10-02 06:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 33.8 |
| e7fc7bae-9fda-3956-a3f0-ec2402300e2d | -12.6484 | -63.1214 | 2024-10-02 06:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 0c83cff2-5453-3b8f-9afc-109366a7a074 | -12.8615 | -62.5129 | 2024-10-02 06:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 7e5eadf8-9772-3445-ba54-08acfd3b18f0 | -12.8424 | -62.5333 | 2024-10-02 06:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 36.0 |
| cdb901e5-eeca-3516-8a45-b281209e1e91 | -12.8614 | -62.5321 | 2024-10-02 06:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 7f80013c-1e86-3d10-a3ed-ea1bcfdb436e | -12.8803 | -62.531 | 2024-10-02 06:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 02946112-9d67-352f-9af6-464db9060b7c | -16.898 | -57.7153 | 2024-10-02 06:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.0 |
| b567af9d-b49a-3fed-8c74-7e90b4ca61b8 | -16.8983 | -57.6949 | 2024-10-02 06:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 141.4 |
| 731deba0-4a32-3114-be8d-fd2039f55dce | -16.8986 | -57.6744 | 2024-10-02 06:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.6 |
| 463f60e6-bcd4-3581-a9db-1860a980c90c | -16.8787 | -57.6971 | 2024-10-02 06:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.3 |
| d451465b-8b60-3425-a114-6ad3b034a0d9 | -16.9176 | -57.7131 | 2024-10-02 06:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.8 |
| 9f01fcc7-a12d-39a6-8561-19403033d704 | -21.3661 | -55.6807 | 2024-10-02 06:17:05 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 26.4 |
| e345ef18-5b13-30ad-895f-3e3af491fa2d | -2.88042 | -61.87074 | 2024-10-02 06:25:00 | AQUA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| f0aafd5d-b0ca-3914-8034-9dd952599623 | -2.87911 | -61.87952 | 2024-10-02 06:25:00 | AQUA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 69794f4a-b59c-376c-b6c0-c07855266d90 | -6.97705 | -59.09298 | 2024-10-02 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f5b0e992-b982-37b6-9a50-c2bb39245b06 | -6.96966 | -59.09794 | 2024-10-02 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c9e87668-51f1-3ec8-8ce4-3f4fc3337e2c | -6.7079 | -59.12511 | 2024-10-02 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 7c656058-eda8-3fcf-9fe3-45978e91ea85 | -7.28878 | -64.65619 | 2024-10-02 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 894c70d0-c6cc-355b-811a-2c100067ce62 | -7.29237 | -64.66214 | 2024-10-02 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b3fa157b-e330-369c-853e-3375425f90d3 | -7.29307 | -64.65694 | 2024-10-02 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| efe23ee4-2e11-38de-84f3-e0b930edcf6b | -7.29449 | -64.66235 | 2024-10-02 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1e6b33c7-203b-39d5-951e-7220257f17c4 | -7.29515 | -64.65714 | 2024-10-02 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ff4442b-f4d2-3b9c-8e1a-88f6c6bb716d | -12.6484 | -63.1214 | 2024-10-02 06:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 834de2ae-ef77-3de3-b117-1c8e30092701 | -12.6486 | -63.1022 | 2024-10-02 06:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 41.2 |
| a01c8b8e-f99d-3032-80fa-2ecbad73d2a7 | -12.8614 | -62.5321 | 2024-10-02 06:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 3a629992-97c9-37c5-8baf-a85f5ce9ca1c | -12.8615 | -62.5129 | 2024-10-02 06:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 0ac19032-8e6e-3a8d-a976-45d696bc029d | -12.8803 | -62.531 | 2024-10-02 06:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 165.3 |
| 437eeedf-4d30-3a94-bc5e-29d5d57efff2 | -16.4533 | -57.4392 | 2024-10-02 06:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 8b938d10-92a9-32ff-a380-6e5982c29584 | -16.4746 | -57.3144 | 2024-10-02 06:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.5 |
| 5ae541af-292d-32c8-8d6d-7d5166cc07bc | -16.6887 | -57.3513 | 2024-10-02 06:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| ce6dcbc2-d986-3970-8b8f-bc77277bdd9c | -16.7265 | -57.4287 | 2024-10-02 06:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.2 |
| 27807f7d-8808-333c-802b-f212f79e5d3e | -16.7461 | -57.4265 | 2024-10-02 06:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.9 |
| 15bb0735-53e4-3f4e-9fc6-c0702bf86df1 | -16.8787 | -57.6971 | 2024-10-02 06:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.0 |
| e7cd783a-cb32-3956-b7d3-255a0e367245 | -16.8894 | -55.8247 | 2024-10-02 06:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.6 |
| f15befa4-3c33-366d-a9f9-c114b7227537 | -16.8891 | -55.8455 | 2024-10-02 06:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 170.1 |
| 305db651-2a74-366a-bc41-91242a9a15d0 | -16.8292 | -55.9152 | 2024-10-02 06:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 93.3 |
| 0139d054-f26b-3196-baa3-6beca5f9692a | -16.879 | -57.6767 | 2024-10-02 06:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.7 |
| 7c5c0298-a6d1-3dee-b8d9-67733467fa06 | -16.898 | -57.7153 | 2024-10-02 06:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.4 |
| ca5c5111-24ad-361e-8546-ac1cdba1c348 | -16.8983 | -57.6949 | 2024-10-02 06:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 145.6 |
| 053b926c-07ce-3181-b2a6-5370d0d7592d | -16.8986 | -57.6744 | 2024-10-02 06:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| d070508b-a78b-3596-bb43-c67a4ac79be2 | -16.9176 | -57.7131 | 2024-10-02 06:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 69481ba8-dd10-3477-974a-c8e65368eaf5 | -16.8698 | -55.8272 | 2024-10-02 06:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 83.7 |
| 0b39bc72-7074-319b-8538-c04e838dcbfc | -16.8695 | -55.848 | 2024-10-02 06:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 144.5 |
| 740109a4-fd80-3f7e-9b81-0306e89566e0 | -16.8295 | -55.8945 | 2024-10-02 06:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 104.3 |
| 08e23425-5795-3512-b1af-3fd48636646c | -17.0892 | -56.7709 | 2024-10-02 06:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.0 |
| fe48ac7c-c261-3182-814b-0139d7577175 | -17.0895 | -56.7503 | 2024-10-02 06:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.2 |
| 085d1b3d-7ba5-31a4-9ba7-de9656db66d0 | -17.1088 | -56.7685 | 2024-10-02 06:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.3 |
| 35d65167-9aab-308d-83e2-49d7d4a58293 | -17.1091 | -56.7479 | 2024-10-02 06:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.2 |
| dc67085a-c6f1-3e02-bad0-c3c00e2ab076 | -17.1288 | -56.7455 | 2024-10-02 06:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 95ffba99-9d57-31c4-8973-8fd1440d16e1 | -17.2364 | -56.1745 | 2024-10-02 06:26:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.0 |
| 3eb3c5c0-03c9-376e-b596-03c91ac88ea1 | -17.2361 | -56.1952 | 2024-10-02 06:26:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.8 |
| b4dc4a7e-c120-3b3d-b702-6879c171548b | -12.85733 | -62.78474 | 2024-10-02 06:27:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 0e62f897-439d-312c-9b26-d2b751fe8535 | -12.86777 | -62.77659 | 2024-10-02 06:27:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d81cf682-043b-3a71-abfb-5bffa1196891 | -12.8488 | -62.51943 | 2024-10-02 06:27:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 26.3 |
| d10683ec-0d8c-3463-82b3-6364e1b2bef5 | -12.84826 | -62.78341 | 2024-10-02 06:27:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 21.3 |
| ef28cf63-73cc-3578-b594-827a9fc86374 | -12.84689 | -62.79289 | 2024-10-02 06:27:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 18.6 |
| a3bc0e6f-7f10-31eb-916c-207a48cdfe2e | -12.84469 | -62.54844 | 2024-10-02 06:27:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ad016ae1-1f7f-3021-bd5e-5c55defd3e3b | -12.83964 | -62.51809 | 2024-10-02 06:27:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 52f2a8e7-6c96-3b19-9a27-037b1501497d | -12.83827 | -62.52777 | 2024-10-02 06:27:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 14.8 |
| f8efdc3c-7c49-3524-b76f-906a3d2503f3 | -12.83782 | -62.79156 | 2024-10-02 06:27:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 47b2d06d-fe18-337c-a0b4-8fa99059b59d | -12.8242 | -62.886 | 2024-10-02 06:27:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a7d1802c-f015-3da6-9957-d649cc17d648 | -12.82156 | -62.51958 | 2024-10-02 06:27:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 52405aa1-80df-3358-bb8d-91546fea8350 | -12.74687 | -62.90715 | 2024-10-02 06:27:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b962d4e5-bf77-3161-8765-3ee0ca536d82 | -12.70446 | -63.07249 | 2024-10-02 06:27:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d6b8043d-0c20-3d2a-a444-7dce270cd779 | -12.65378 | -63.10572 | 2024-10-02 06:27:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 97b63817-9062-317a-90c3-be6ce72006cb | -12.65242 | -63.11498 | 2024-10-02 06:27:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 5b98ee9c-1d39-3851-a422-4fd716ec5741 | -12.64481 | -63.1044 | 2024-10-02 06:27:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 452f509b-4c0b-3280-a9f2-ce71b4009ad0 | -12.64345 | -63.11365 | 2024-10-02 06:27:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| b70b5911-d108-3d74-9202-8f95b3dd0f2f | -8.46801 | -62.71257 | 2024-10-02 06:27:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c7bcc19d-d178-3053-9687-90099fa6b788 | -8.46668 | -62.7215 | 2024-10-02 06:27:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 85651b98-0d44-3539-85ed-fdce52a1539d | -8.45956 | -62.64737 | 2024-10-02 06:27:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a3d94552-e4ac-36fe-93c7-3757ef4ce535 | -8.45914 | -62.71127 | 2024-10-02 06:27:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.4 |
| fd0882d8-2881-303f-b0bc-12d307ca9862 | -8.45781 | -62.7202 | 2024-10-02 06:27:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 64d78590-df4e-3f90-a41c-85c200eab8d9 | -9.95836 | -62.99241 | 2024-10-02 06:27:00 | AQUA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fcea6564-9b98-3554-a6a5-91a333299025 | -9.54314 | -62.80781 | 2024-10-02 06:27:00 | AQUA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 2628215c-46b5-3f54-a43b-dd80c627c6f2 | -12.31596 | -63.71408 | 2024-10-02 06:27:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9b24088a-9656-3588-a89f-cb4f2d085c19 | -11.75319 | -64.19871 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4d9d5224-b060-3d2d-91bf-47626f61cfa5 | -11.62422 | -64.01694 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 20.1 |
| f125e1b6-2e77-392a-a6a9-702076626b9d | -11.61594 | -63.95141 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5efcdf3a-d74e-3aad-bc58-562311a245b6 | -12.87628 | -62.52343 | 2024-10-02 06:27:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 120.1 |
| ecb250e1-0cc8-3923-bb8a-f065b295b780 | -11.61172 | -63.66877 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ab9bd7b7-c653-3a4a-9004-ac79546d83ca | -11.56025 | -63.77116 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2a59ac2f-9af8-341d-95cf-92cd4550aa46 | -10.99798 | -63.57031 | 2024-10-02 06:27:00 | AQUA_M-M | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4a79ca9e-e09d-3eeb-ab83-f972a4b94b87 | -10.98125 | -63.93967 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0c343959-ec0c-3ebb-b454-018ff7d881cd | -10.97991 | -63.94862 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0fa2fca6-445c-33a8-ad6c-e06e518fae73 | -10.88786 | -63.88309 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bf11228a-5a42-3a19-9a94-44a59e2542b9 | -11.71836 | -64.12901 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 347b38bc-1ac0-3c0d-88cc-4c9b3990f80a | -11.67464 | -64.04293 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 45351438-aaa7-3d8b-a69f-58d3350e1903 | -11.63307 | -64.01828 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 83d502b6-e50b-38e7-9501-f5ca39a3c469 | -11.62287 | -64.02592 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 605323d4-738c-373f-bec6-c06f8512c421 | -10.97856 | -63.95756 | 2024-10-02 06:27:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |


[Clique aqui para ver as próximas entradas](README193.md)
