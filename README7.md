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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b524fc2c-b6ba-3fc5-a8a8-752f3370e4ec | -17.125099 | -56.189999 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 49b6172f-b965-3e31-aa2f-aa2bc89a54a7 | -17.126699 | -56.197201 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ad188c2e-003c-336d-9aff-b1f9c5ca43bf | -17.1283 | -56.204399 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ec0bf3c7-8ec4-346e-8403-4cab31fe2888 | -17.129801 | -56.211601 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7d63289f-54a6-3145-97ca-53c26077d3ce | -17.131399 | -56.2188 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a24e2861-6f5e-38e9-93ed-ec4baf80bec8 | -17.115299 | -56.192299 | 2024-09-30 01:10:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eb378c65-bf93-3172-9945-fb8f0b6e0049 | -17.116899 | -56.199501 | 2024-09-30 01:10:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 61aea411-b6c6-3861-b0a8-2874531a9eed | -17.1185 | -56.206699 | 2024-09-30 01:10:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 915dbb3d-957e-3fbe-b2e1-75436d3e690e | -17.120001 | -56.213902 | 2024-09-30 01:10:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| df4239e7-cd53-3e2a-8d16-ac570e203e60 | -17.1071 | -56.201801 | 2024-09-30 01:10:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 801059ea-8fec-3ba5-aa48-293ee041d4e1 | -17.1087 | -56.209 | 2024-09-30 01:10:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 97b46ee8-6d42-3349-babb-b46e45162743 | -17.114901 | -56.237801 | 2024-09-30 01:10:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 45bca829-9a8c-3883-bc60-048e7cf254b0 | -17.0786 | -56.117802 | 2024-09-30 01:10:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e67a963b-378f-3796-b02f-87c4adacfab1 | -17.0802 | -56.125 | 2024-09-30 01:10:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f6dd2477-6b16-3465-a4e7-0effdf588c6b | -17.1035 | -56.2328 | 2024-09-30 01:10:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6d1577e2-8192-3759-9549-b1e4e4ee5d62 | -17.105101 | -56.240002 | 2024-09-30 01:10:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 45206389-44b4-3c20-af2b-e85524d227c4 | -17.086 | -56.1991 | 2024-09-30 01:10:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7016f82c-d117-365b-a093-e4dac7f3b6fd | -17.113701 | -56.374298 | 2024-09-30 01:10:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3e5c7bb0-ccf1-3423-9982-efb84c275ded | -17.0415 | -56.088902 | 2024-09-30 01:10:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 439a2ebd-85d4-3e44-8fea-68965fe97360 | -17.042999 | -56.0961 | 2024-09-30 01:10:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 13f985fb-2c5e-3f26-9343-70e8bb760224 | -17.0446 | -56.103199 | 2024-09-30 01:10:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ccc58934-4b70-3b53-a4e2-d5da1007cd87 | -17.102301 | -56.369301 | 2024-09-30 01:10:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4269b278-f350-386e-9064-dafac9ed8ce6 | -17.103901 | -56.376598 | 2024-09-30 01:10:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ae5e87f4-7a3d-373a-ad9e-1c6459a90009 | -17.1054 | -56.383801 | 2024-09-30 01:10:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 74a44963-b460-35e0-895d-31651ef67fd9 | -17.0301 | -56.084 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0015170e-e226-326b-ba57-1558366edbf3 | -17.0317 | -56.091099 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ef62332c-0f5b-3c67-ad0c-3cf4e191a704 | -17.092501 | -56.371498 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 264c7531-0ba7-3b94-a1e5-7b692bb485f5 | -17.094101 | -56.378799 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a6e620d7-2bc8-3e2e-b4dd-8f31d16f84c5 | -17.0956 | -56.386002 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 28d6a913-e5fa-3c3a-9241-b8dd52693863 | -17.018801 | -56.079102 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e292299c-297b-3ecb-8124-e296e50dcbcc | -17.0203 | -56.0863 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 046a6b86-6239-3c6a-9dc4-160a218670e4 | -17.079599 | -56.359402 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6a43e157-f77d-369a-a334-23217f3c94a2 | -17.0811 | -56.3666 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ef801fff-dd83-3dc0-afbb-1bb2f6f976bc | -17.082701 | -56.373798 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 74e91a4c-8a15-3a64-a63d-17f7530079ed | -17.007401 | -56.0742 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 49fc2d17-e447-3b4a-b6e5-f3f5bbce3dbc | -16.996 | -56.069302 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c596d850-8ad9-34f6-907e-27b132dc74e2 | -17.004999 | -56.1577 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 28dc6c6d-6a28-3400-bbf6-afe0129c800e | -17.0065 | -56.164799 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 77b2ff75-f57f-3480-b1c1-aa58cbff0126 | -17.008101 | -56.172001 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6271f973-fdbe-3c77-8d17-59dd65386df2 | -17.054899 | -56.387901 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 38c50284-2205-3dbb-977f-d8840267b12f | -17.0564 | -56.3951 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6655a7ae-fdb0-347c-8cb0-63012c3a4d09 | -16.987499 | -56.124001 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b2640298-cb61-3d7d-94ce-eec11f2055cc | -16.989 | -56.131199 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2c1e7abb-c017-318e-b061-e8db7196b065 | -16.9937 | -56.152699 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aab1da16-46cc-3b7b-8756-97de2db9eb9b | -16.9953 | -56.159901 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 15218c8d-5233-3dcd-9a1b-ffbefc5925a8 | -17.045099 | -56.390099 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 33201937-0dd3-3edb-85db-39ee9ee533c9 | -17.0467 | -56.397301 | 2024-09-30 01:10:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1a8dfca2-a14f-397d-8190-223b5a88806d | -16.9699 | -56.0905 | 2024-09-30 01:10:53 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0af096cd-aa7d-3c72-be6f-30bfcd1b6f3c | -16.971399 | -56.097698 | 2024-09-30 01:10:53 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d1c34629-6259-32dd-b3ab-b42946824ee6 | -16.973 | -56.104801 | 2024-09-30 01:10:53 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 51f2b8f2-1002-37f0-95a7-43ec2ba69353 | -16.980301 | -56.186001 | 2024-09-30 01:10:53 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fc69463a-558e-3809-bd98-34490ec9e9b7 | -17.0958 | -56.721298 | 2024-09-30 01:10:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aedf9eb8-5362-3f1c-8a79-2fa9e45829d0 | -17.097401 | -56.7286 | 2024-09-30 01:10:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 753e4093-2d68-30a8-80c2-e5e93e85837f | -16.969 | -56.181198 | 2024-09-30 01:10:53 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e5e6a1b8-cac2-3c4f-adeb-1af4551bfb90 | -16.970501 | -56.188301 | 2024-09-30 01:10:53 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| db98dfba-10bc-3815-be88-c37f2711acc3 | -16.972099 | -56.195499 | 2024-09-30 01:10:53 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 896f540a-af4f-3998-a135-2306f727c7e2 | -16.4438 | -53.922901 | 2024-09-30 01:10:53 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 594df7da-a895-3cbc-8cea-2160d093dcc2 | -16.445601 | -53.9305 | 2024-09-30 01:10:53 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a8f40afb-2916-39d8-b864-1aae26fac1b3 | -17.063299 | -56.713402 | 2024-09-30 01:10:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 56f92bc2-c78e-3565-b468-1ac3fc51887b | -17.064899 | -56.720699 | 2024-09-30 01:10:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ed69c594-2e8d-37e5-8a54-ab82dc8c1059 | -17.066401 | -56.728001 | 2024-09-30 01:10:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9f07f969-6cd8-3fe7-bc01-9e4135dfca77 | -17.068001 | -56.735298 | 2024-09-30 01:10:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 53b0ca67-fb1c-3c81-8b6d-ccbabbaa5858 | -16.432301 | -53.917801 | 2024-09-30 01:10:53 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b53dcc81-5662-3ed7-b4fe-bf911eae4551 | -16.434099 | -53.925301 | 2024-09-30 01:10:53 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 78fd3161-c79a-3b98-90b2-2283a64c8e73 | -16.435801 | -53.932899 | 2024-09-30 01:10:53 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 699b553e-2543-3314-8aac-39639bd94592 | -17.051901 | -56.708401 | 2024-09-30 01:10:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 54598a9f-dc15-3d4b-a843-525e158aaef8 | -17.053499 | -56.715698 | 2024-09-30 01:10:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f23943df-b271-3580-a375-146cb93ddc01 | -17.055099 | -56.723 | 2024-09-30 01:10:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3928943c-8224-3767-8b0d-26a0969b4910 | -17.056601 | -56.730301 | 2024-09-30 01:10:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 87ed4934-ea81-3649-a94b-f97a7e1ed0d8 | -17.058201 | -56.737598 | 2024-09-30 01:10:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9866b02c-951d-301c-8c56-db1537323925 | -17.059799 | -56.7449 | 2024-09-30 01:10:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4ecd0f0b-7dd7-30c2-a36a-22732b702e40 | -17.194 | -57.376301 | 2024-09-30 01:10:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 96ab647b-1ff0-3bfa-bc97-552ca984ccf9 | -17.195601 | -57.3839 | 2024-09-30 01:10:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 62daf332-6694-3c83-89b7-9071a0e17e1d | -17.042101 | -56.710602 | 2024-09-30 01:10:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 65690b4d-22d4-3a13-8158-08cacc9b5a93 | -17.043699 | -56.717899 | 2024-09-30 01:10:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 01614202-f67a-37b7-bb0d-535574bfb423 | -17.0453 | -56.725201 | 2024-09-30 01:10:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 23ee141b-640d-348e-80d6-49306853ad32 | -17.046801 | -56.732498 | 2024-09-30 01:10:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3304ad20-a783-3830-b801-8fff69d1e635 | -17.048401 | -56.739799 | 2024-09-30 01:10:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 225e49d0-b2cb-353c-812f-e31e8305cfda | -17.049999 | -56.747101 | 2024-09-30 01:10:54 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 01c1a5e8-d89d-3cdd-8a2f-e47c4065d9f1 | -16.650999 | -55.2038 | 2024-09-30 01:10:55 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5f2adc1b-59dd-33af-82fd-723bc5359b6c | -16.652599 | -55.210999 | 2024-09-30 01:10:55 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d21a461c-5795-3260-ae66-4d73ae47b59d | -16.6542 | -55.218201 | 2024-09-30 01:10:55 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 143f6d4d-ec3c-3136-946f-f01b4fb38797 | -16.641199 | -55.2061 | 2024-09-30 01:10:55 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 059c6762-d270-3ca5-8b87-adc27dd9d302 | -16.642799 | -55.213299 | 2024-09-30 01:10:55 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d33dae83-546c-344f-8a95-9972c380c135 | -16.6444 | -55.220501 | 2024-09-30 01:10:55 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7e886031-1f8a-384d-b561-8559b55e542d | -16.711 | -55.520599 | 2024-09-30 01:10:55 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b67b578a-d59a-3cbb-8aaf-e4148140b93a | -16.712601 | -55.527802 | 2024-09-30 01:10:55 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7cface11-8b9d-3349-8956-5894e1655c0c | -16.7938 | -55.943802 | 2024-09-30 01:10:55 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3ec87a03-cf61-3782-90f4-5ba3918a0072 | -16.7953 | -55.951 | 2024-09-30 01:10:55 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6e65e82d-6911-39d1-af29-4398c713ee45 | -16.760599 | -55.839001 | 2024-09-30 01:10:55 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b28166d2-1061-37b4-869e-15276d7d1463 | -16.747601 | -55.827099 | 2024-09-30 01:10:55 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d793eafe-ed61-3465-b7e0-73b1911b6d0a | -16.749201 | -55.834301 | 2024-09-30 01:10:55 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8dc13f92-bd40-37c9-bbec-54cd20681de3 | -16.0811 | -53.514599 | 2024-09-30 01:10:58 | METOP-B | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 047b8c62-25b9-3e8c-b619-7299c07eb94c | -16.5984 | -55.944599 | 2024-09-30 01:10:58 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 124e1118-b1af-3cdd-81c8-ad3b708da4a1 | -16.6 | -55.951698 | 2024-09-30 01:10:58 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8ffe7369-baff-31fc-81f3-e04ccf1d1c75 | -16.601601 | -55.9589 | 2024-09-30 01:10:58 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 28197ee2-b923-3c5d-bd27-e1c58a797355 | -16.6031 | -55.966 | 2024-09-30 01:10:58 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 00c55d69-38fa-35d3-bc5c-d271dabbce56 | -16.591801 | -55.961201 | 2024-09-30 01:10:58 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 556459c5-2cd8-3798-bec1-c1ecb5d481b5 | -16.5933 | -55.9683 | 2024-09-30 01:10:58 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c23cc64c-637f-3808-a861-62352a130af5 | -16.5949 | -55.975399 | 2024-09-30 01:10:58 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README8.md)
