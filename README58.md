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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2a3b0a5-945a-32bb-95c4-25fb10880915 | -3.34248 | -53.54249 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f3f62747-b651-32fe-b2fb-0896f0ba99fe | -3.33809 | -53.54186 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5142a918-beb0-3f63-8431-043b5dc889d9 | -3.33745 | -53.54617 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c513d064-4955-3572-923c-ff155171a46d | -3.42443 | -52.7728 | 2024-10-16 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6d41bea-6a8a-359c-82e1-7591abcc48a0 | -4.30825 | -53.71186 | 2024-10-16 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 297ddebc-dd0c-360c-9227-c6252ea02237 | -4.26426 | -53.67437 | 2024-10-16 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8276d631-9b5b-3473-8930-52af17b40520 | -4.0163 | -53.80121 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7289444-e4c5-3e33-92fb-9668945754ee | -3.79813 | -52.29709 | 2024-10-16 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bf5bfb1-9c33-3d70-a176-7af1533dc917 | -3.79332 | -52.29635 | 2024-10-16 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef410d8b-fb73-3a6c-b865-eabd2dd1f895 | -3.7928 | -52.29676 | 2024-10-16 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42aab0a8-43b8-3a1f-a83e-450c6f551ef7 | -3.73164 | -53.41394 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e858204-ee17-3527-a7a9-d72dea037530 | -3.8223 | -52.39786 | 2024-10-16 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4845da75-7dc8-3fab-9896-423e7d263266 | -3.79762 | -52.29751 | 2024-10-16 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b42f3f52-443b-3e55-9aa8-c4bf9b60e22f | -1.51412 | -54.51758 | 2024-10-16 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1005f28d-ec03-3868-a79b-db8ee655f1d5 | -1.57113 | -54.76814 | 2024-10-16 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2311bd93-cef4-3446-b1f1-f0660e27349d | -1.51856 | -54.79582 | 2024-10-16 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f5d336f-36c9-3598-b267-fabb62b4ffb2 | -1.51779 | -54.80082 | 2024-10-16 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bcb9b873-a719-3750-8342-d94302881e7f | -1.51639 | -54.51741 | 2024-10-16 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9941cc12-4976-3bc8-bc28-ead8b038823b | -1.51238 | -54.51685 | 2024-10-16 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6eeb721-5f82-304e-a6ab-10b7c96e7c32 | -1.13101 | -54.11546 | 2024-10-16 05:23:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| edd9a2a0-c000-324d-b042-8bc79f007509 | -1.1298 | -53.68686 | 2024-10-16 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 736ec8af-c9fe-3581-9677-6fdec16019e8 | -1.11845 | -53.70501 | 2024-10-16 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3969de00-151b-3046-a50d-7a34d106a137 | -1.11788 | -53.70877 | 2024-10-16 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4e60532-464e-3f03-a508-a9beaed1a08e | -1.02326 | -53.73202 | 2024-10-16 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b880df0d-434d-38d7-8f26-22ccec1ecdfd | -2.20785 | -53.65934 | 2024-10-16 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2b806613-d7b4-3c50-a448-557a8b95f954 | -1.24269 | -53.37888 | 2024-10-16 05:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fac705c5-e9fa-36ff-adfd-cf1afa42889b | -1.12693 | -54.11487 | 2024-10-16 05:23:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7454f965-fe43-3574-84df-d148e271a3f2 | -1.09844 | -54.21684 | 2024-10-16 05:23:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74e83000-bf9f-3f01-9d38-04fc0de56291 | -1.02388 | -53.728 | 2024-10-16 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bff192fb-9daf-3d4e-aab3-7ecc03dc3f9b | -2.98333 | -54.62479 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57af7baa-d023-3518-bf23-359c1c70665d | -2.93309 | -54.81891 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 457d4684-eef0-35f2-ad3c-0adacee889ca | -2.86779 | -54.5083 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84b0546d-41c7-3e40-9150-91782d97deb7 | -2.75531 | -54.9013 | 2024-10-16 05:23:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4c49af8-8c70-3e54-b591-a35fa86aea5d | -2.19835 | -54.84476 | 2024-10-16 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 315b30a0-cad9-3553-9d83-c7d7a70382fc | -3.27195 | -54.18223 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73980846-09f3-3038-a650-90813d46d857 | -3.26775 | -54.18163 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78fcdcd1-016a-3947-b9c5-a8b216302358 | -3.15338 | -53.93636 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a34ed761-e636-32e8-a7e6-898dcad37184 | -3.14971 | -53.93177 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2ae2274-616c-34de-b1a2-239006eee99d | -3.14912 | -53.93571 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c02e182-1e5c-37b0-b0af-553dd908bb5d | -3.12571 | -54.23559 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9d88a57f-8a0a-3dde-966c-94477f0d80c2 | -3.12455 | -54.24326 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 48c7c94e-c795-32e1-9ffc-d4d7c91c1195 | -3.1227 | -54.22725 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0b1bec3b-f365-3419-b998-dd0574c5f9d4 | -3.12213 | -54.23107 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 755e00fc-3833-3268-b8ab-0384cfa24eb0 | -3.12155 | -54.23492 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 1efe33f6-4dbe-326c-8d69-1946b5dfc7bc | -3.12038 | -54.24264 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ef91ae16-2a04-3085-aa57-5b67b0a2e301 | -3.11873 | -53.73886 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 518e836d-cab4-34d5-b0d9-ddfc69d4fffb | -3.11853 | -54.22662 | 2024-10-16 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 7a652b8f-80d1-3a47-a3f6-099e2eddedd6 | -3.1181 | -53.74295 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f916bdd2-b5e1-34db-b5d4-1ef30ff8f573 | -3.11796 | -54.23042 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 80f3ea0b-c543-3b4b-9d6d-aa45e2f1b4e5 | -3.11629 | -53.72589 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 304cacaa-b167-3557-8eb3-97c8df7ee558 | -3.11604 | -54.21475 | 2024-10-16 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c0666a1-0bea-34a5-a909-73854b921d04 | -3.11567 | -53.72998 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bccf0adc-4eec-3149-8ce1-c5132a56fbc5 | -3.11548 | -54.21852 | 2024-10-16 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9c87c91c-31a9-38be-b4f6-de09bfd9d446 | -3.11491 | -54.22229 | 2024-10-16 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e4dc9191-868e-3f69-aced-2587d7064f24 | -3.11435 | -54.22603 | 2024-10-16 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| d756157b-d7fd-3293-8339-de39cc053eb9 | -3.11379 | -53.74229 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 047d8ec6-3b13-3636-9032-ae351d97de7c | -3.1132 | -54.23367 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 0fe6e023-b9ba-3266-ac25-d299a1d85e26 | -3.11186 | -54.21414 | 2024-10-16 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d05a08ac-cc22-30ad-9698-1f65eb63851a | -3.11073 | -54.22172 | 2024-10-16 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8262bbe3-3319-348a-aefa-b6f266ae1382 | -3.11073 | -53.73342 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83be3753-1d98-30f4-b31e-41401d4ddd3a | -3.11011 | -53.73753 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb3ff788-6a8e-3a36-8f88-5ba39fe79e1a | -2.87138 | -54.17473 | 2024-10-16 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2557125b-5378-3b46-92b9-e1cce19b9812 | -2.86946 | -54.17585 | 2024-10-16 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61dc60f0-8a7c-3a9b-a1d5-f2a1cce38cd3 | -2.62295 | -54.33336 | 2024-10-16 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0427bec2-90df-3334-9ff1-764c6891db39 | -2.43468 | -54.36852 | 2024-10-16 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85c01e28-3ae8-3182-aea1-7d1c1867f1f8 | -2.39249 | -53.72568 | 2024-10-16 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42d70125-1040-3380-9e12-ad63646eba97 | -2.38898 | -53.72678 | 2024-10-16 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80203eda-a86c-383d-b2a1-3f170f7f5bdf | -2.97928 | -54.6242 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f8c2105-7b38-3aad-9c43-12d3a6a98928 | -2.9494 | -53.70589 | 2024-10-16 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31cc7b94-f692-3035-b72a-98233f49e439 | -2.93708 | -54.81962 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76fb1515-5ec5-3e53-a5e0-78f6d3d0622e | -2.87081 | -54.17855 | 2024-10-16 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35928391-cc85-3df6-af36-545e65b6c571 | -2.86724 | -54.51195 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f390b25-cf0e-315d-93f8-1f878b7512da | -2.84122 | -54.0814 | 2024-10-16 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 549baee1-e35c-310e-8b5f-28eddc54d0cb | -2.82275 | -54.7238 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d8c8f9d-3de2-365a-b16d-b9a0d0baec07 | -2.81698 | -54.01424 | 2024-10-16 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8207cac7-c73d-3a4a-b4c5-0954d12ae1fc | -2.81394 | -54.47876 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60fcbf17-df14-363e-8ea1-5b3e620d4ab5 | -2.51465 | -54.95607 | 2024-10-16 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0c9c5144-76f9-30cc-8025-2c527a58685e | -2.43413 | -54.37215 | 2024-10-16 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18c59b59-3d0f-3db9-aa81-10d43294299d | -2.38822 | -53.72499 | 2024-10-16 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f1f96eb-6062-3a12-8081-9940a0e74c9e | -3.49177 | -54.45666 | 2024-10-16 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e565fe04-46db-3d99-9303-24a8ae74461a | -3.49122 | -54.46043 | 2024-10-16 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3018b94a-bc13-336b-9b24-aaac4412f1a0 | -3.13484 | -54.28775 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3737838f-f67f-3d78-865c-0317d72dff5f | -3.13068 | -54.28716 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3401666e-dabe-337b-b16b-ccb7aaa37d3c | -3.12709 | -54.28277 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 951214e9-5c54-355f-9912-e97ba19d3067 | -3.12652 | -54.28654 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbd18d0c-321c-3424-98d8-0e63cbe1f3ce | -3.12513 | -54.23942 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| aebd8802-54c8-3cc7-b53e-0374954cf07d | -3.12294 | -54.28214 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b60d2d8-ef1f-32ee-92d0-df4c3b4e046c | -3.12096 | -54.23878 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e124a9d5-e0f5-339e-8011-d8bff4edeb44 | -3.11966 | -54.21908 | 2024-10-16 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c77e06a1-588d-308d-a94b-102febf7513f | -3.1191 | -54.22285 | 2024-10-16 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1f0e6476-75bc-333c-82e8-5b2e942b77fa | -3.11738 | -54.23429 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 7d8a4385-9af7-3e1c-8260-d95733298140 | -3.11679 | -54.23816 | 2024-10-16 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 72a755e0-4faf-3a35-a34f-acdcbc5f0954 | -3.11504 | -53.73409 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e54ccb73-48b0-3375-baef-dc4e711cfb3e | -3.11442 | -53.73819 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3505d018-e499-3006-be34-8ee8fce95281 | -3.11379 | -54.22979 | 2024-10-16 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| d415a535-564f-3408-9755-539d2c1d71e8 | -3.11317 | -53.74639 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 93236128-e528-3cc7-8a2a-bc7377bde3e1 | -3.1113 | -54.21794 | 2024-10-16 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 24f85c81-4062-34e6-893e-5df88a160adf | -3.10949 | -53.74163 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97b2b9f8-cf70-3285-9d5b-11c983506e7a | -3.1058 | -53.73686 | 2024-10-16 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df33cf4c-5341-3491-857a-9f580a67e113 | -4.04454 | -54.77332 | 2024-10-16 05:23:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README59.md)
