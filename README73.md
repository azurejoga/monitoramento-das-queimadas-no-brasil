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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad4fb9d8-485e-3598-b603-2ba33d784ff2 | -1.38013 | -55.88161 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe14530d-fed9-303b-b443-6a8cefbbef14 | -2.98306 | -53.88504 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d5a960f-6d96-36c7-bda3-f1cd7faca0a0 | -1.44335 | -55.20993 | 2024-12-02 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81261379-6707-3daa-99c8-16194dbc7f99 | -2.26571 | -53.61408 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ab409bf3-76f0-3d78-9912-290792b5e97b | -2.9857 | -53.88637 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1aa7297b-3f7a-365f-b065-a71d277da5a6 | -3.28097 | -58.53469 | 2024-12-02 05:42:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 183957c0-e33c-33aa-b413-73cfd52a283c | -3.262 | -53.62143 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b13497a0-82d8-39ae-8fbb-64d0088cee88 | 1.21378 | -56.00748 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b05fce9b-6cb0-3f3b-b777-d5bdac1a0e87 | 1.1275 | -55.98441 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 753ed7f1-f9d6-37a8-9a87-4d8d08ffbd20 | -2.63577 | -53.3555 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f9fa3cd9-c8e4-3ab4-b9f0-15d681376c00 | -2.62928 | -53.35911 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 76252fc1-2c08-31a2-b52f-20155fe37cb2 | 1.12566 | -55.98822 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5f7a7a00-b900-33fd-8329-6320f1ba75a6 | -1.25123 | -54.53735 | 2024-12-02 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fbf42337-bc65-353b-a06f-e66d65cbebe7 | -3.96411 | -52.18087 | 2024-12-02 05:42:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13b7665f-2e19-3cea-b180-56458fbfff93 | -3.29268 | -53.84776 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 882edc09-fa75-35d8-a8dd-cb074936a3c4 | -2.89295 | -54.16277 | 2024-12-02 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 82d5c52e-b06d-3044-94b3-07864e3d7702 | 0.64948 | -59.66163 | 2024-12-02 05:42:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7925ef1c-8e23-38d9-86d3-398a68d73e9f | 1.13857 | -55.97497 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 369a0e7a-f8bc-3c6c-9a9d-46a05f058f27 | -2.05038 | -54.67076 | 2024-12-02 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37ee8cb3-c2ca-3f37-b12f-985b5c5efb5f | -3.47289 | -52.24781 | 2024-12-02 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 48253e11-cf29-3f7d-82e0-6a5c9e3af8d4 | -2.63437 | -53.36512 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8ed66024-739c-364b-9c65-a568a9db1d2c | -2.71209 | -54.95837 | 2024-12-02 05:42:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4f1714b5-b322-3f95-a39c-5516c9df6d04 | -3.03093 | -51.54021 | 2024-12-02 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 11942aea-1398-33df-86c2-1e2e392b3b2f | -3.64339 | -54.67803 | 2024-12-02 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 909473dc-402b-3d27-b602-13619a9296db | 1.10074 | -56.00563 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 116ebc16-2d0e-3288-b177-b59ca13cebad | 0.89191 | -59.54549 | 2024-12-02 05:42:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b43be935-b29f-3c52-9afa-c01b2b9def3a | -1.09736 | -53.65244 | 2024-12-02 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cf8afe9-c70b-3d4c-a143-8c40ca2ac467 | -1.25068 | -54.5411 | 2024-12-02 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 80cfc90c-befa-3919-ad27-7f9d59cb2290 | -1.26831 | -54.54951 | 2024-12-02 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51fb6738-156a-3938-bc41-e6e6dffc8fc3 | -3.7435 | -52.26872 | 2024-12-02 05:42:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef53a941-7aff-3245-8996-2d0b51d379f6 | -3.96492 | -52.17504 | 2024-12-02 05:42:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d4e45d9-9df6-3540-891d-b7d95bb76f6d | -1.07552 | -53.45308 | 2024-12-02 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fe3157c1-7040-3d01-bc25-6de8e1134ab4 | -2.92277 | -54.12421 | 2024-12-02 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b945ca2-3394-38de-81f7-09fa2669c414 | -1.43674 | -55.43027 | 2024-12-02 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c973c553-2926-36ec-929f-ed9b872f6b73 | -2.30948 | -53.89622 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3a015cf-3d42-376e-a496-f9d1f7c1a414 | -2.63542 | -53.36018 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 22828943-43c0-329e-887f-d283cf9e8183 | 1.11857 | -55.99144 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e5bb116d-da9b-31f7-aecb-df37cf93d1c6 | -2.71568 | -60.01505 | 2024-12-02 05:42:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9f1cdf6-5394-3036-99b7-c5d8e55b83bf | -2.89848 | -51.57885 | 2024-12-02 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c27d801-9bfa-3eb7-a9fa-ea4ac234ee47 | -3.25536 | -53.92162 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75841264-5d45-3f02-8a50-09fc440a5091 | -2.78398 | -55.35598 | 2024-12-02 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a98c18ce-0ff5-3ef6-b01d-10e89a927bea | -1.27391 | -54.55034 | 2024-12-02 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 430fa50d-1b95-3e01-80a2-544eed55eb2b | 1.1119 | -55.99606 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| efee5ec8-5def-36ca-ae9c-b9e358893bfd | -3.2971 | -53.84748 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 03eec218-a4eb-375a-bf91-c45cd242a442 | -3.26608 | -53.63643 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 94a582b4-7a8b-3ff8-acd9-4cc79a279946 | -2.63795 | -54.19866 | 2024-12-02 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f0bc209-5091-3189-9a96-b02098176d1d | -1.79937 | -60.07055 | 2024-12-02 05:42:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd78e134-69c2-3a9f-b1e5-9856d50d66ae | -2.38899 | -53.71261 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 24607ec7-9d01-395a-a12c-c39d589d01f4 | -3.42332 | -54.0243 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 581c7eee-736d-3563-a2f9-a51c7f90bc71 | -2.27315 | -53.60539 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aeee8509-da97-3515-b5c6-bec42972bc53 | -1.07481 | -53.45773 | 2024-12-02 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 172d853a-728f-3031-816e-78dec6626a35 | -3.29979 | -53.82947 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5dc99fe6-c7a1-329e-aaa3-039f2397ff10 | 0.64873 | -59.65687 | 2024-12-02 05:42:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56556130-6886-36b4-baef-6554c009ffa5 | 0.86205 | -59.68178 | 2024-12-02 05:42:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3acf2dcf-03b5-381a-9ef2-15ab27a13638 | -3.43953 | -54.60829 | 2024-12-02 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcd4da08-c473-3c70-9e2e-29e2fcbdada4 | -2.64122 | -53.36136 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2d062f44-24a2-3909-9688-e7d3ab96fd02 | -1.07586 | -62.64545 | 2024-12-02 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9bb58910-c219-3c65-8952-9da113cdb3ca | -3.6857 | -51.69709 | 2024-12-02 05:42:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c10c1b73-0611-39d9-90b3-b400126511bc | -1.45182 | -55.19051 | 2024-12-02 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3738c955-fe31-34ee-a080-02c122cceab9 | -3.33548 | -53.5449 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53f83084-b2cb-3d86-876c-ce9aa5f13589 | -1.44202 | -55.43113 | 2024-12-02 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0e27467-3b87-3e2f-9a82-a54b6e0bc4cb | -3.75102 | -54.50829 | 2024-12-02 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 00b90aa6-412b-3efe-886a-ac251f4da088 | -3.75994 | -54.65298 | 2024-12-02 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34408dd8-6016-3c16-8c1f-fabdb1b3ac10 | -2.63507 | -53.36032 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c4a555cb-603f-308a-8998-0cffd34045bf | -3.49999 | -53.83608 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3444630c-1f6d-3dc8-bd66-5e11f7ccf024 | -3.18228 | -54.33621 | 2024-12-02 05:42:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 76bcc443-79d0-3114-bbe8-95b8b0ed6b07 | -3.4306 | -53.88864 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 333c4ab5-5614-383f-adaa-d7a5cfc9d9ac | -2.81712 | -53.05954 | 2024-12-02 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a6d9395e-d2f5-3200-b45e-fef904df6a3a | -3.50783 | -53.83354 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 755017c4-9e67-31b4-9cde-11384a22f110 | -2.35159 | -54.37091 | 2024-12-02 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2d7cbf20-46a4-3395-b6ff-ec275364e9bc | -3.26063 | -53.63092 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ba387fa8-6ebb-3b1a-b4f8-371b46340e0a | -3.25352 | -53.93413 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 557fd6c5-a56e-3051-97d2-304732b31d1b | -1.25644 | -55.89944 | 2024-12-02 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3bd3529-c0c0-30b2-8c38-d5c41237876f | -3.75044 | -54.51239 | 2024-12-02 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 888ef856-3993-3704-9a73-67733f3f6998 | -2.9046 | -51.58212 | 2024-12-02 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 79048a99-0f4f-3108-9522-a23e4ff96504 | 1.11678 | -55.99525 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b587175f-3955-3087-a24e-e141b07ecd7f | -2.02037 | -54.31299 | 2024-12-02 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0979836e-855c-354e-9407-362a2427cf23 | 1.09267 | -56.01808 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 408fdd78-c779-3765-85b5-8c6b4d67ada1 | -2.45652 | -53.63156 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12f76501-de64-3e66-ba9e-c5c9513599bf | -3.55036 | -51.45672 | 2024-12-02 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc19e32a-babd-36c4-aac3-f53f68479010 | 1.1079 | -56.00231 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6026ba6-a775-3c53-b188-f983d9c6dde3 | -1.56806 | -55.3358 | 2024-12-02 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e39a147f-052f-3200-982e-a7ee23c02c77 | -2.35068 | -54.37096 | 2024-12-02 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 51e5d49c-8460-351a-8093-286a0ee30268 | 1.04913 | -59.54106 | 2024-12-02 05:42:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 751eb1aa-fb1a-3da4-921f-3a7155334686 | -3.65554 | -51.12273 | 2024-12-02 05:42:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bc5d016-1cb9-3521-ba84-da180479b81c | -3.77794 | -52.03341 | 2024-12-02 05:42:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 8d99588e-4d2b-307e-92d4-7547fcba846e | -2.27016 | -53.61365 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4a115ef9-2fbd-3b57-8140-22f3eccc426b | -3.29332 | -53.84327 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cf5f339f-f4a3-333e-9e9c-ef814e235d9b | -1.56946 | -55.3387 | 2024-12-02 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64a1f2c7-faa3-323a-82ce-bc7a2a430e77 | -2.35129 | -54.36695 | 2024-12-02 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fee0ea8b-4d34-3036-b935-25d72ce8c34d | -2.05095 | -54.66699 | 2024-12-02 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7f288c2-b885-3bda-92c6-007b3176a184 | -1.06851 | -62.64804 | 2024-12-02 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4e65111c-2775-3e2d-a57b-068350e65b13 | -2.02097 | -54.309 | 2024-12-02 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3199354f-4a81-3442-a1ae-87daaf99a03b | -1.49885 | -54.95636 | 2024-12-02 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88a6929d-d4d2-38c8-b202-9f06b87fa647 | 1.21368 | -56.01807 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6ef7f20-6b0b-3ed5-87c1-6a0345291ce6 | -2.27088 | -53.60893 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0968e921-bae5-38b3-8a71-3710fc3ab030 | -3.42272 | -54.02847 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9124693c-fc95-3b49-bd8a-ee6ec9a1bdde | -2.77855 | -55.35521 | 2024-12-02 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 18c59b09-ee4f-384e-8b26-f906eaa26f99 | -2.62823 | -53.36404 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 86650f54-3776-3ad6-b5cc-18ffe0eedc1d | -1.24537 | -54.54969 | 2024-12-02 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README74.md)
