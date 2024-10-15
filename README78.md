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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ddbe20f-d0b6-34f8-adb7-ba161e36d57c | -13.37562 | -61.9384 | 2024-10-15 06:57:00 | AQUA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 2bb00dec-41fb-34b0-ac83-ab89125b92e9 | -13.37153 | -61.97334 | 2024-10-15 06:57:00 | AQUA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 2e16ad58-d3bb-3108-aabc-4557f2350b9c | -11.69582 | -65.21647 | 2024-10-15 06:57:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 26ef9e2a-fbf1-39f6-87f7-ba02bd7af986 | -11.69353 | -65.23469 | 2024-10-15 06:57:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 24.5 |
| a088260d-437f-3dae-a9e5-3f9e24ca7ff0 | -10.3788 | -61.1758 | 2024-10-15 06:57:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 429a4c4c-699f-3350-a42a-39635edf17dd | -10.37231 | -61.17041 | 2024-10-15 06:57:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 511e8ad1-0445-3bc5-8714-0046f4d6ac5a | -13.89 | -45.86 | 2024-10-15 07:04:04 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f75b4ac5-05dc-358a-8436-658ecf19b4ee | -13.89 | -45.81 | 2024-10-15 07:04:04 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1a868570-2c59-3c74-b03e-25110fa11a5a | -13.92 | -45.87 | 2024-10-15 07:04:04 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 566af1e5-4525-32df-93aa-2c403b4728f1 | -13.92 | -45.82 | 2024-10-15 07:04:04 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f729a7f5-7c42-375a-af1b-a908c8c3cca9 | -17.8447 | -57.4401 | 2024-10-15 07:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.1 |
| 370e948e-060e-30fe-bc0b-26c298bcdde7 | -17.845 | -57.4195 | 2024-10-15 07:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.5 |
| 59831278-8f7b-3815-baa5-b5e9cdca8a72 | -17.8644 | -57.4377 | 2024-10-15 07:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.5 |
| 10dbecbd-b9fd-3f56-bf11-be3c331f4f98 | -17.8648 | -57.4171 | 2024-10-15 07:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.7 |
| 1ad9a87a-2e27-35a7-aad1-0ceca9503a40 | -17.8845 | -57.4146 | 2024-10-15 07:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.2 |
| 047a971d-3042-3a0b-93b7-5bb3bc299a9e | -17.8842 | -57.4352 | 2024-10-15 07:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.1 |
| 95db60c1-5218-3669-a101-1491e7e42460 | -17.8648 | -57.4171 | 2024-10-15 07:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 159.8 |
| f85d2d28-cc1a-30b3-8619-d00c61c8a67e | -17.8447 | -57.4401 | 2024-10-15 07:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.7 |
| c585d350-e407-3ae2-838b-bd0a6f594343 | -17.845 | -57.4195 | 2024-10-15 07:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 165.4 |
| 36d4d6b5-bfe1-3159-a62b-6f19abe91aa4 | -17.8644 | -57.4377 | 2024-10-15 07:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.6 |
| 5403730e-c2b4-32b0-885c-018c6fc62819 | -17.8842 | -57.4352 | 2024-10-15 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.6 |
| fcc34536-7a12-3bdc-8518-f077830ef2f9 | -17.8845 | -57.4146 | 2024-10-15 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.9 |
| 64922d2b-1b98-3c3d-b4c6-10bf10f1e6e7 | -10.3711 | -61.1935 | 2024-10-15 07:26:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| cc8e2633-9a69-3a29-ae7c-b2ab93cba5fb | -13.3786 | -61.9582 | 2024-10-15 07:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 8c27b230-3540-3d65-bb2b-e5953e283a78 | -10.3711 | -61.1935 | 2024-10-15 07:36:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| de9a3621-32d6-3845-a03e-d6912e7da8df | -17.8447 | -57.4401 | 2024-10-15 07:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.5 |
| 9d7eca30-edb0-33e5-b2bf-a5cd1c6f9a6d | -17.8648 | -57.4171 | 2024-10-15 07:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 164.0 |
| 76e66e2c-2bb6-3b6b-b201-050ce98eab8b | -17.845 | -57.4195 | 2024-10-15 07:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 160.3 |
| 1339a157-b95e-3867-95b8-d14bd641cae2 | -17.8644 | -57.4377 | 2024-10-15 07:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.7 |
| 1815cf03-264b-385b-8e15-7a4f838f3ebd | -17.8842 | -57.4352 | 2024-10-15 07:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.6 |
| c6cdf800-70f1-3266-8fb9-069c9d89dece | -17.8845 | -57.4146 | 2024-10-15 07:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.6 |
| a0d0edb5-e2f5-3f06-abd3-ec71f1e6a37c | -10.3711 | -61.1935 | 2024-10-15 07:46:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| b901f2a3-6883-38f1-97f0-539913bb9936 | -13.3786 | -61.9582 | 2024-10-15 07:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 311bd290-49a2-3d84-bef8-ce3723c72065 | -17.8648 | -57.4171 | 2024-10-15 07:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.7 |
| f48e88af-732f-39cc-9361-57de87d584c9 | -17.845 | -57.4195 | 2024-10-15 07:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 151.6 |
| 825864cd-5c09-34bb-80ab-d4ccc41c5025 | -17.8447 | -57.4401 | 2024-10-15 07:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.4 |
| 761a421e-7873-35dc-9e55-0dc74d187be3 | -17.8644 | -57.4377 | 2024-10-15 07:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.0 |
| 8aa7c16d-9ad0-358d-9166-91ef2ab42622 | -17.8842 | -57.4352 | 2024-10-15 07:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.4 |
| 97a672ee-c144-3071-8399-db3d88da91ab | -17.8845 | -57.4146 | 2024-10-15 07:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.8 |
| a6ffc519-9c47-33ee-b5ab-9ffc9022068c | -10.3711 | -61.1935 | 2024-10-15 07:56:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 45acb4f1-0b47-3dda-8f9f-6f29162a230b | -13.3786 | -61.9582 | 2024-10-15 07:56:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 161bd07d-3ef9-395d-8401-2a4037a40231 | -17.8648 | -57.4171 | 2024-10-15 07:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.4 |
| fee56572-31a0-31bf-81c3-3d11a66e1795 | -17.8447 | -57.4401 | 2024-10-15 07:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 834f709e-26ea-305e-9a2c-fad4e6337588 | -17.845 | -57.4195 | 2024-10-15 07:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 133.9 |
| 59f43374-c95e-3bc7-8aad-7856a3e613f0 | -17.8644 | -57.4377 | 2024-10-15 07:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.5 |
| d4b14abe-e591-30c3-b92f-ea5b3597d89b | -17.8842 | -57.4352 | 2024-10-15 07:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 7f02f2a9-2e42-344f-a683-8c4c5676859d | -17.8845 | -57.4146 | 2024-10-15 07:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 149.7 |
| 988a5395-49f7-31f2-96df-dca9159a7d5e | -10.3711 | -61.1935 | 2024-10-15 08:06:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| c19547f6-f61d-3b7a-a5fa-217a701192f1 | -17.8644 | -57.4377 | 2024-10-15 08:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.9 |
| e2275cf4-57a4-3800-93a5-cd7e5a22d1e7 | -17.845 | -57.4195 | 2024-10-15 08:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.6 |
| d53b5760-fc2d-33f4-8ce6-d7e7794e4488 | -17.8447 | -57.4401 | 2024-10-15 08:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| 2a78c858-b840-3f42-a7dd-2d4c3b427906 | -17.8648 | -57.4171 | 2024-10-15 08:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 136.0 |
| 1e40a9fa-67a1-385d-b3bf-1cdd98ee569e | -17.8845 | -57.4146 | 2024-10-15 08:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.2 |
| cc7e728e-eb2e-3d11-856d-ed3f5e964f47 | -17.8842 | -57.4352 | 2024-10-15 08:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.4 |
| 80b45d93-ae3e-38f4-a09e-12a50163b4e6 | -10.3711 | -61.1935 | 2024-10-15 08:16:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 5964c719-2545-35b1-bb8d-81e8e75ea915 | -13.3786 | -61.9582 | 2024-10-15 08:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 25eb5714-029e-3586-b181-e5cb5297cfb9 | -17.845 | -57.4195 | 2024-10-15 08:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.8 |
| 78dc8a4c-2734-3d9c-b6b2-7044931ef257 | -17.8447 | -57.4401 | 2024-10-15 08:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.4 |
| 32127e75-f4e9-3533-966c-101eea719f85 | -17.8648 | -57.4171 | 2024-10-15 08:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.5 |
| 5147a9cf-d8e2-3b74-ac61-0f45ddbc50c4 | -17.8454 | -57.3989 | 2024-10-15 08:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.3 |
| 6dcb0d6a-21c1-3f4c-a804-2a3b442f97c4 | -17.8845 | -57.4146 | 2024-10-15 08:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.2 |
| 1ae1bba2-ae72-336f-883b-38dba8841b4d | -19.5615 | -56.968 | 2024-10-15 08:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 206f258e-22ac-3fd2-a21f-c1b728f5934c | -19.5611 | -56.989 | 2024-10-15 08:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.9 |
| 81d054a6-e43e-38e7-ae94-e7301cff884f | -10.3711 | -61.1935 | 2024-10-15 08:26:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 1ba682b7-3989-3956-8414-c6e4f9f8f612 | -19.5611 | -56.989 | 2024-10-15 08:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.6 |
| 13a6f3c1-8f33-3630-acf0-4ee41ebfb402 | -10.3711 | -61.1935 | 2024-10-15 08:36:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 2ef1be85-0b4c-390b-a5fe-4fa607ae92e7 | -17.8648 | -57.4171 | 2024-10-15 08:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.4 |
| aea84f6d-f099-3357-9445-81ab3b10b5aa | -17.845 | -57.4195 | 2024-10-15 08:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.6 |
| b7165397-3577-3640-8d33-d4a21d82451d | -17.8644 | -57.4377 | 2024-10-15 08:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| 37ee195b-a48a-3233-9b91-3428c9a30483 | -17.8842 | -57.4352 | 2024-10-15 08:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.4 |
| d6558818-f0e9-30af-b13c-93e275e8f661 | -17.8845 | -57.4146 | 2024-10-15 08:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.1 |
| 728cfc7e-fec2-340e-bc24-34cdf3127862 | -10.3711 | -61.1935 | 2024-10-15 08:46:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| a2d021d7-7283-3b24-8558-9970c6b5a2dc | -10.3711 | -61.1935 | 2024-10-15 08:56:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| e529b8e2-662d-3470-8e2c-8988ff52a6c1 | -10.3711 | -61.1935 | 2024-10-15 09:06:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 39abb6f4-c2a1-3875-8ad1-374cb8af9fcb | -10.2632 | -47.2802 | 2024-10-15 12:06:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 2b1a86dd-2f7f-3b93-85d3-b087c501ef87 | -10.2632 | -47.2802 | 2024-10-15 12:16:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 137.1 |
| af2d3b65-1281-3616-ab65-5a342f114c21 | -9.8883 | -47.0119 | 2024-10-15 12:26:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| f54e9285-0b5c-3c04-bffe-e3429f5bd6df | -10.0495 | -47.6589 | 2024-10-15 12:26:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 1778e29b-4c09-37e1-8d01-bbb5bb32d551 | -10.2632 | -47.2802 | 2024-10-15 12:26:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 272.2 |
| 3a01708f-cc70-3934-9f0a-475d999c9f7f | -10.2442 | -47.2824 | 2024-10-15 12:26:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| e06c8a71-1008-3c0e-a6fa-3cbac4a29204 | -11.2637 | -44.213 | 2024-10-15 12:26:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 025f01a5-41c9-3534-9c44-7d42275bde55 | -9.9607 | -47.2483 | 2024-10-15 12:36:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| a86dff98-9667-3575-9494-a03b548261a5 | -9.9781 | -47.3573 | 2024-10-15 12:36:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 97ac1d9e-ed77-3d2d-8b68-18371dea9dd7 | -9.9796 | -47.2461 | 2024-10-15 12:36:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 202d61ea-a8f1-3b95-b1dc-9f29756dfcb4 | -10.0536 | -47.3709 | 2024-10-15 12:36:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 2fa03228-6c02-3a6a-9514-ec39695faadf | -10.0495 | -47.6589 | 2024-10-15 12:36:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| ed563522-d661-33df-9bea-ccd2fedfa720 | -10.2632 | -47.2802 | 2024-10-15 12:36:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 579e79b7-3802-3ff1-93df-326c026cbab8 | -11.2637 | -44.213 | 2024-10-15 12:36:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 9214074e-2c2b-33da-bb74-3dc885a46e39 | -1.55769 | -47.69549 | 2024-10-15 12:42:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 0448a9a8-5ef5-3a65-baa9-3ab5d5d57efc | -1.07523 | -47.58668 | 2024-10-15 12:42:00 | TERRA_M-T | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b251d4c3-7e79-3da3-ab48-5dd3e803ed73 | -1.1491 | -49.1689 | 2024-10-15 12:42:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 910dece0-01f7-3633-99ff-a9fce5f25c70 | -1.19619 | -47.58117 | 2024-10-15 12:42:00 | TERRA_M-T | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b769f9b3-55dd-37f4-9313-b79543749ad8 | -1.48124 | -47.07799 | 2024-10-15 12:42:00 | TERRA_M-T | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 8452c72d-6d9e-3b3b-ba7f-957d95682000 | -1.48255 | -47.06894 | 2024-10-15 12:42:00 | TERRA_M-T | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 9d940c6b-a6b2-33f2-98b9-2c643be6e63f | -2.11925 | -46.05481 | 2024-10-15 12:42:00 | TERRA_M-T | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ec8b22d0-0653-386d-b38d-0f3554940760 | -2.25375 | -47.66135 | 2024-10-15 12:42:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 7c936348-f077-3d85-806d-6b79f0d74fa2 | -2.25512 | -47.65205 | 2024-10-15 12:42:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| eecafa42-a4c0-3df5-b2a4-8a013bda2a92 | -2.29776 | -46.59539 | 2024-10-15 12:42:00 | TERRA_M-T | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 8284f8b9-2beb-344d-884b-c2dd707d1885 | -2.33429 | -46.48054 | 2024-10-15 12:42:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 3641e6f3-3306-3a65-b432-6cf4c9433fc8 | -5.60547 | -45.19746 | 2024-10-15 12:44:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |


[Clique aqui para ver as próximas entradas](README79.md)
