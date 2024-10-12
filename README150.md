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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a60980d-adf0-3ffc-bfc4-63434fd04c65 | -10.65087 | -64.42859 | 2024-10-12 06:35:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e3d12a92-8e80-34b5-8c4c-f08989555e3e | -10.6405 | -64.43668 | 2024-10-12 06:35:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 678d8b7e-f662-343f-8efa-3da9b3d1f072 | -10.61898 | -64.39576 | 2024-10-12 06:35:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 56fcd1dc-5ae4-3e42-b018-a827457fc468 | -10.58755 | -64.48539 | 2024-10-12 06:35:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f529cde2-b257-3bb6-b299-279f8c82809c | -10.57926 | -64.03162 | 2024-10-12 06:35:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a21c141e-99cf-3d85-824b-37b56c18e121 | -10.57789 | -64.04107 | 2024-10-12 06:35:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d490bd5d-80ff-360a-b182-10d2854b1828 | -17.8863 | -57.3115 | 2024-10-12 06:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.4 |
| e94b0fff-d82c-3ea0-8923-e963bdc24f84 | -17.8665 | -57.314 | 2024-10-12 06:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.1 |
| f46294fa-972f-3f24-8a3b-1a9a7302a5be | -17.8668 | -57.2933 | 2024-10-12 06:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.1 |
| 7d591ab1-aaab-397f-b2f4-033f74916b81 | -17.8467 | -57.3164 | 2024-10-12 06:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.5 |
| aae6b738-8a23-3b94-a555-9384941d003e | -17.96873 | -57.36415 | 2024-10-12 06:37:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.0 |
| 760e373d-0c48-3e7c-b059-e6268da7911a | -6.86108 | -70.05719 | 2024-10-12 06:40:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b58f8212-f661-38e9-958b-0675d760d878 | -6.8606 | -70.06078 | 2024-10-12 06:40:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 615381a5-55b8-39cf-b9b3-378011af472a | -6.86026 | -70.05904 | 2024-10-12 06:40:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55dc9bfc-ca89-3ed7-8518-ad0530a4da09 | -13.7346 | -60.6079 | 2024-10-12 06:46:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| e59917ef-ce9c-38c0-a1ff-0f803b4de66e | -17.1761 | -57.4585 | 2024-10-12 06:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.4 |
| 900de21c-8071-3057-b0a8-d455abf14d5a | -17.6467 | -56.3292 | 2024-10-12 06:46:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.3 |
| 90d33b5a-dc58-3cd8-ba17-b8c81d8a7354 | -17.9841 | -57.3612 | 2024-10-12 06:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.9 |
| f9029c0e-2028-39de-998b-32f566740993 | -17.964 | -57.3843 | 2024-10-12 06:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 5420bf30-7f22-3f79-bbba-2cf237321cca | -17.9837 | -57.3819 | 2024-10-12 06:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.4 |
| 0333f167-aaff-34b0-bf2a-c2f9d3b0f2ae | -17.9643 | -57.3637 | 2024-10-12 06:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.9 |
| 9ca472df-5e1d-3b6b-8502-3f3e7d75895e | -13.7346 | -60.6079 | 2024-10-12 06:56:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| df0528aa-ed83-3f78-a19e-1ae05f12f302 | -13.7348 | -60.5883 | 2024-10-12 06:56:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 658d4d5a-53dd-345e-a74a-c0b8d49d5034 | -17.6467 | -56.3292 | 2024-10-12 06:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.0 |
| ec1c238a-958e-3921-af23-4ba14a40c878 | -17.964 | -57.3843 | 2024-10-12 06:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.1 |
| 01a8f91d-f94b-35f2-90a4-21598cb41f7a | -17.9643 | -57.3637 | 2024-10-12 06:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.9 |
| fd5d1091-b9de-34de-b325-47e8e1c657f6 | -17.9837 | -57.3819 | 2024-10-12 06:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.0 |
| 0fc6d492-c330-3169-9c43-1f042ef75e91 | -17.9841 | -57.3612 | 2024-10-12 06:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.1 |
| 95118cad-c5a9-3586-8ff9-00bb17850da6 | -13.7346 | -60.6079 | 2024-10-12 07:06:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 74cd907d-34fa-34a5-ae05-51944853d2c5 | -13.7348 | -60.5883 | 2024-10-12 07:06:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 826a1713-5aa2-3b7f-a954-1ffb5d928278 | -17.6467 | -56.3292 | 2024-10-12 07:06:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.7 |
| 1796731b-be77-382c-9c4d-d41dad4518d3 | -17.964 | -57.3843 | 2024-10-12 07:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.7 |
| 4ad1bba1-a649-33a3-aa3f-cb05f858e431 | -17.9643 | -57.3637 | 2024-10-12 07:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 644da708-9013-38af-9e9a-d3b964a81826 | -17.9837 | -57.3819 | 2024-10-12 07:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.7 |
| 4e185407-cc2e-3b57-a71c-983f977e346a | -17.9841 | -57.3612 | 2024-10-12 07:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 67a118b3-8c26-3183-8344-667e29b384ea | -18.2158 | -56.5249 | 2024-10-12 07:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.7 |
| e1c07ed6-b032-3958-b8a6-da2e87266f6c | -17.6467 | -56.3292 | 2024-10-12 07:16:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.2 |
| bcb553fb-a9cc-367d-982a-9f2ee67eab7d | -17.964 | -57.3843 | 2024-10-12 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.8 |
| c810eb2f-25e2-3dbf-a307-de74406c2b72 | -17.9643 | -57.3637 | 2024-10-12 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.0 |
| 1219e35f-d4db-38d6-b87c-1ab56e466b11 | -17.9837 | -57.3819 | 2024-10-12 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.1 |
| 1defa2fb-092b-3d98-bd23-7d4b7f598a48 | -17.9841 | -57.3612 | 2024-10-12 07:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.9 |
| 2aa1590b-9d42-3bcd-93ca-e724d4631b86 | -17.1761 | -57.4585 | 2024-10-12 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.9 |
| 0cb1c4c4-d9dc-3310-a982-109fdd22651b | -17.6467 | -56.3292 | 2024-10-12 07:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.3 |
| 8cacafaf-091c-3bd1-91ce-d3f5bfb74fdc | -17.9643 | -57.3637 | 2024-10-12 07:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.7 |
| 70edcba3-cf3c-36fd-af82-cd4a36f0f4f6 | -17.964 | -57.3843 | 2024-10-12 07:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.2 |
| 3cadb798-3074-3b8b-b41e-cc960b5bf121 | -17.9841 | -57.3612 | 2024-10-12 07:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.9 |
| f8ab2024-3a84-3396-a4de-3c2d39e71521 | -17.9837 | -57.3819 | 2024-10-12 07:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.0 |
| 0d7033f5-cc2e-3090-992e-08df5a6ef30c | -18.2158 | -56.5249 | 2024-10-12 07:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.4 |
| b698b4cf-07aa-3f82-9315-9d941fba3eda | -18.196 | -56.5275 | 2024-10-12 07:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.9 |
| 2ba79664-a93d-3500-8591-35cf884c140e | -18.1956 | -56.5483 | 2024-10-12 07:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.6 |
| adbd75c1-366a-3d83-a904-c4373ef612df | -17.1761 | -57.4585 | 2024-10-12 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.5 |
| 5a4da5b6-f7d9-3964-8b03-416df18ad5ff | -17.964 | -57.3843 | 2024-10-12 07:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 82c4f38d-279a-34fd-b04f-3d8dd04e7d7e | -17.9643 | -57.3637 | 2024-10-12 07:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.2 |
| a16f1b40-4ecb-3d25-acb6-e9b8389e2393 | -17.9837 | -57.3819 | 2024-10-12 07:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.0 |
| 810db3f8-692d-3819-9cf0-317e4f863cb7 | -17.9841 | -57.3612 | 2024-10-12 07:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.0 |
| 46c8d72c-a97f-32ce-8c2f-7a88f073d978 | -11.8377 | -58.8445 | 2024-10-12 07:46:13 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 98be1909-7429-3cd9-a82b-857736ee95f7 | -13.7346 | -60.6079 | 2024-10-12 07:46:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 7c63b013-f304-34b8-839d-f33dc8d01b31 | -13.7348 | -60.5883 | 2024-10-12 07:46:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 39.6 |
| d749c7a6-ab08-3427-8ae6-c504616cdbe5 | -13.7346 | -60.6079 | 2024-10-12 07:56:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 3a39cb39-ed5e-3f0d-944f-47b85c410e26 | -15.6225 | -59.9784 | 2024-10-12 07:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| bc7149a7-9d3d-3336-99ff-097e3aca6943 | -15.6228 | -59.9585 | 2024-10-12 07:56:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 4aaafba4-471d-3e6a-a4ae-f0168e5d9183 | -16.9805 | -57.4404 | 2024-10-12 07:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.4 |
| 409470bf-b45e-3a1a-a077-27b564be3a77 | -12.4367 | -54.5778 | 2024-10-12 08:06:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 6b9eb9ed-5192-31f8-956f-36cdbc2ec015 | -12.437 | -54.5573 | 2024-10-12 08:06:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| c103e3bb-f4bf-3c0c-86a9-af8f85c33f8d | -12.4558 | -54.576 | 2024-10-12 08:06:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 1faf3435-f6ba-37e5-8bd7-54f47f73cc9a | -12.456 | -54.5554 | 2024-10-12 08:06:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 152.2 |
| 8586b2d9-7f27-31f9-8500-747edfc01efa | -12.4563 | -54.5349 | 2024-10-12 08:06:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 56defc86-7210-3212-bb6b-112ed6ad2fff | -12.8323 | -53.5048 | 2024-10-12 08:06:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 6d9a9488-cd72-38fc-97ab-170cad158e3c | -12.8132 | -53.5069 | 2024-10-12 08:06:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 27c80f80-f7c2-3bcf-9918-c0642a04a67b | -12.9655 | -53.5319 | 2024-10-12 08:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 98ac3759-9f8b-3c83-aeec-bdd2abddf2d9 | -12.9658 | -53.511 | 2024-10-12 08:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 8ea76539-531e-3644-b06e-72222653fff2 | -12.9464 | -53.5339 | 2024-10-12 08:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 8c25cff9-8665-3557-9ba3-ad7b71ae4e2e | -12.9467 | -53.5131 | 2024-10-12 08:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 80f05064-fbaf-3379-8188-a2351b69fcf3 | -15.6225 | -59.9784 | 2024-10-12 08:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| f0673750-fa56-3d53-b284-99db4e183d7b | -15.6228 | -59.9585 | 2024-10-12 08:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 0b502f6b-e22d-3ef8-8f0b-d22b67ed37b5 | -17.6467 | -56.3292 | 2024-10-12 08:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.1 |
| fa190ded-1a4e-3bbc-bfc8-ee92d717ee9d | -12.456 | -54.5554 | 2024-10-12 08:16:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 211.9 |
| d4f77929-8aa2-31bf-8127-dc07de0292c4 | -12.4367 | -54.5778 | 2024-10-12 08:16:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 1da48a6e-7bd9-35c4-bd00-c0c023614c9a | -12.437 | -54.5573 | 2024-10-12 08:16:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 767da0a0-bbec-3446-98db-2e6d5f9a2ab6 | -12.4558 | -54.576 | 2024-10-12 08:16:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 9d80208c-5b93-34e4-b1a1-94ffc924fa8e | -12.6184 | -55.2144 | 2024-10-12 08:16:18 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| e0e459ed-7ad5-329b-8bf1-1ec455e0a066 | -12.8132 | -53.5069 | 2024-10-12 08:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 68d736dc-2385-375d-914d-1fe7d1092bb7 | -12.8323 | -53.5048 | 2024-10-12 08:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 02240937-b431-33b5-82da-d6bfb714996b | -12.9464 | -53.5339 | 2024-10-12 08:16:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| a59ac803-0c7d-3e42-a856-16f4ca442d52 | -12.9467 | -53.5131 | 2024-10-12 08:16:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 2b18f688-0fdb-39cc-a3c6-cda4ea9d5073 | -12.9655 | -53.5319 | 2024-10-12 08:16:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 9eee5066-3e3f-3dfd-a811-330315b60d67 | -12.9658 | -53.511 | 2024-10-12 08:16:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 43475c68-2f61-301c-9e45-16d148aa815d | -15.6228 | -59.9585 | 2024-10-12 08:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| de934299-4475-3e63-9cc0-a7c1f85f6858 | -12.437 | -54.5573 | 2024-10-12 08:26:16 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 5ee9850f-f50a-3a2d-a259-3feaf47dcd6f | -12.4367 | -54.5778 | 2024-10-12 08:26:16 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 68531ed2-1ee8-3f22-9a50-7331570fea06 | -12.4558 | -54.576 | 2024-10-12 08:26:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 0bb43617-5216-38a5-b7dc-529f9b00e9ea | -12.5994 | -55.2162 | 2024-10-12 08:26:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 025a7b62-7ff8-30e1-97bb-9cfcdf19acd6 | -12.456 | -54.5554 | 2024-10-12 08:26:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 222.8 |
| 19bef016-0f4f-391e-878a-68431412419f | -12.8132 | -53.5069 | 2024-10-12 08:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 010802b6-6d3c-3e1f-9945-86539d37df3c | -12.9464 | -53.5339 | 2024-10-12 08:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| a00a8593-f623-3f54-b6f3-953988c8a270 | -12.9467 | -53.5131 | 2024-10-12 08:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 80827417-d373-3085-95b8-18f5171272bc | -12.9655 | -53.5319 | 2024-10-12 08:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| d51bd6bd-1c2c-395c-8a2a-aefedec9b762 | -12.9658 | -53.511 | 2024-10-12 08:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| ce0be8e6-65a3-3616-80f9-4599879fdb45 | -12.8323 | -53.5048 | 2024-10-12 08:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 6b96d3ba-afac-39d8-bc56-e26f3e77abbc | -15.6225 | -59.9784 | 2024-10-12 08:26:34 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |


[Clique aqui para ver as próximas entradas](README151.md)
