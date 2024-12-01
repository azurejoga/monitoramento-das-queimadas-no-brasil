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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df596620-17a2-3c65-b303-859c583916c5 | -3.08752 | -51.07509 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a6d3489-06a1-3f4d-bdc9-f47fcadef375 | -2.53093 | -53.98603 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e04d06b7-2f2e-3d0b-9188-9f997e56312e | -3.69107 | -51.34211 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8f391aa-be6c-37d5-9852-a38aef0cd0cd | -3.3129 | -50.50446 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35b89de1-cfa2-3819-93e7-770a770066b9 | -1.81894 | -54.86947 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ca4b548-ff20-3469-a75a-08dde6e57821 | -2.43304 | -53.88573 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c122327-ab52-3423-9245-b7284e18797d | -5.54912 | -50.27763 | 2024-12-01 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9efa4c3-e75a-34a8-b833-bea609bdf37e | -2.86735 | -54.03129 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bd26f5d-9743-3928-93a3-37b4efaadd41 | -3.6949 | -51.8045 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1f489e1-c67d-3730-a2a5-103904c1c4ba | -2.62283 | -46.95884 | 2024-12-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7b4a680-841a-35aa-8292-077fdb49f018 | -1.4641 | -52.69384 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13dde99d-9a67-301e-bb95-e200fcf5e41f | -3.70947 | -51.68221 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a698b64-3360-325c-9d5e-b2ea3282511b | -1.779 | -55.27539 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71072bdd-3e12-319e-a40f-69503357afeb | -3.25529 | -53.64774 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92957936-b029-384e-9859-6aba5de7dd67 | -3.09077 | -54.03642 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c7a089f-8067-3b45-b329-a98fb312285e | -2.68484 | -54.24322 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84d2a9da-3a96-32f7-bb7b-7c1ec4f2d9e4 | -4.17603 | -48.61501 | 2024-12-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 7335245a-24ff-3955-a756-3dee0936361f | -1.42844 | -55.2783 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c451bce-5d06-36ae-b2b7-b6e65f0b81d5 | -1.48513 | -52.67945 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 73a9a477-eb5e-35bd-b15f-01a55003ef10 | -6.7134 | -47.27832 | 2024-12-01 05:08:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3c9465b-eaaa-3c82-a81b-9f5a20ad3257 | -3.49712 | -52.12928 | 2024-12-01 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c54137d-fdef-360b-9369-b0f57ae8df8d | -2.81042 | -54.06734 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1c0e20c-ab48-3508-ba6b-285d2bf05b3a | -2.96034 | -53.89404 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d85e8474-ce9e-3cac-9788-8e79ff6bf648 | -3.30612 | -53.83601 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35366fba-eaaa-3b88-a54e-6855356fa4d1 | -2.65453 | -51.86844 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1158cb0-b444-3e71-9717-6462962fd623 | -2.59028 | -53.97169 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9b7d544c-8d41-3c4e-b0e2-c2844ed63d2a | -3.06101 | -54.04385 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39d95f66-dbb3-3a9f-ae61-1db3cb7f2646 | -2.22764 | -53.62712 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bffcc80b-6c2a-3588-b197-c96d3092a5fd | -2.97741 | -53.92814 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9828f998-2d40-3868-bdf4-755a2e4d294a | -1.48048 | -55.37939 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45cfd61d-bd08-3981-9461-c79b50940b74 | -3.76579 | -50.17759 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7d2bf18-1878-3d7a-93fd-c984f9333750 | -3.38027 | -50.11428 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ce9dbc1-9718-386e-b160-c911e17e29da | -3.13074 | -54.52814 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 27c2d2d9-11ea-3536-b82c-4c2159f8a0e3 | -2.95684 | -53.89342 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91dabd1a-cecc-3896-a2aa-dd68dc95d8ad | -3.09045 | -54.13131 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a97f3d21-7e13-3a46-b72c-4efbd4532304 | -2.89837 | -51.57737 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e92544fb-727f-30d7-83a7-e9c9cc986837 | -2.78565 | -51.67223 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62d4e0c6-c126-3930-afac-c63cd895ebc5 | -3.71074 | -53.40762 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1bc44016-060f-3b2f-97ee-2989de6a3826 | -2.76608 | -55.34526 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d41b7554-4c86-3f3d-9971-d78e70c1612a | -3.09564 | -53.72398 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 365958ad-dfaf-3a39-ba0a-a21fbe2b881d | -2.98544 | -45.58379 | 2024-12-01 05:08:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| bac1a510-89ff-306b-a765-25773d872f9f | -3.3034 | -50.79958 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0cc3e4b-f824-39c6-9bae-37e06eaebb9f | -3.03257 | -50.24305 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6455fb8-43f8-33e3-a1e4-54a57bcade6c | -2.36014 | -53.65859 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 572fe566-3bdd-3c1a-b47d-8028cbab33b5 | -3.34162 | -50.74884 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d242e00-f99e-31d6-8aa2-1b87e4b1dbfc | -2.92563 | -54.26675 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93fd9f9c-de1d-39f7-bda4-115a45d0360a | -3.2542 | -53.63097 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 634925c9-c6f3-3c3f-8c4c-b3334dac78ac | -2.44911 | -53.62288 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a81b77ef-1779-3f1e-a4e3-b13c27ddefe3 | -3.71199 | -51.06828 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 449d4741-0d71-32ff-91a0-8695563105df | -2.63863 | -54.29031 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99d3951f-073b-3e87-9620-2317607b2c31 | -3.07531 | -53.25945 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f3588385-2441-379e-9dcc-872fc8da19f8 | -3.82662 | -50.13689 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a21e5906-cfab-33ef-8c4a-fb583a31f42e | -1.56447 | -53.83671 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 678c82bc-b81b-3a7e-be5a-e18c546fe6da | -2.98087 | -53.28891 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2e621df-5837-352e-88ab-6a50f61e92ba | -2.44578 | -53.66729 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86ee8771-118d-3912-b2fa-6f95653e9215 | -2.97808 | -53.87281 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 835bce6f-8998-341c-a87f-a392de2b8a6d | -2.76261 | -51.68963 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fecce4df-84bd-3f2d-9729-1ba52179a299 | -2.52092 | -54.0746 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92df76ec-b082-31e5-bfab-ec010344d003 | -3.68933 | -51.81429 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c60b69a9-a6fe-303e-8f7e-d5112719a808 | -3.30542 | -53.86336 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4c5e28e4-c56c-394d-b830-b7ea5e0cd53b | -3.06789 | -53.8089 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a4e09cb4-73f9-36ba-ae6b-39a8c72e6ea8 | -1.39753 | -53.63789 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1294eb5d-2bd7-3b9f-ab7b-9853436a6e0d | -1.83083 | -54.52816 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fe7eebc-f37e-3741-ae2e-0d4be9ecab0a | -3.03787 | -51.47686 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfda8658-f99f-3079-ac5d-e1ce34e56bee | -3.2526 | -53.9245 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a52d6173-9d97-3739-96f5-219ac9003fa1 | -3.11725 | -53.98087 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7851e46-7cd1-331e-8c0b-c4abf941c1fd | -3.2513 | -51.14095 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b473e306-453e-3f3b-ba3b-033efe2d5ec7 | -3.07945 | -53.75798 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c81b205c-c98b-3960-8ef8-0525812a83f8 | -4.4889 | -48.21531 | 2024-12-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27f2b5ff-8a1c-3544-b157-ae3ad29a7a66 | -3.31602 | -53.86498 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 48ebf898-5107-3ffa-9ea9-e0cff8802144 | -5.53771 | -45.43154 | 2024-12-01 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dadea69d-46d8-31ff-b48b-bf192a193120 | -3.24939 | -53.63855 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8115049-5ae1-35ff-98ed-bc0b0fe3ce26 | -2.88847 | -53.98699 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa414a03-55ac-3a48-8c0c-ea379343d4e9 | -3.03697 | -50.24364 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a6e6b3e-36a1-3959-ad40-bdba720429b9 | -4.5511 | -43.31577 | 2024-12-01 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 25f75fd9-cb85-3f6b-b01b-f7e6627f48eb | -2.84572 | -54.07923 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3670ad23-cd65-366a-abf4-8372f0eadf0d | -3.22858 | -51.50564 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fabd6b35-6191-3f69-8b82-39ad86c7e173 | -4.55404 | -43.29544 | 2024-12-01 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| df29259e-ece9-3d00-b435-45920483a8f3 | -2.75389 | -51.66739 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d57979b0-0e6f-3028-8d83-53fcbb39b7ed | -3.09471 | -51.26495 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 300e42da-98ed-377d-82d4-2dd7052047c1 | -2.73614 | -54.04015 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce25534e-93ef-33d3-855a-21dd23c2d06f | -1.3963 | -53.64587 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 32fb25a9-1740-364b-8f59-c254e1da11af | -3.16988 | -53.63941 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c58764d-433c-3092-a678-228fb99513c8 | -3.70953 | -53.75334 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10de75fc-31fc-350a-9b8d-c9c40c118d17 | -2.85301 | -54.19387 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0eb25d1b-5308-317a-89bd-d93f4f53611a | -3.26428 | -53.63668 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f299683e-99aa-30b3-b200-a52c8bff5cd2 | -2.76991 | -55.3206 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4c54906-1fe2-355f-9563-08fa49dcfa22 | -3.49754 | -54.67021 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7c8c6d5-8009-30a5-98e6-5f44e3d1e52f | -3.02086 | -54.01871 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c7c8cf7-c171-35eb-b841-c5e6e01fafb4 | -2.83693 | -54.10284 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24a86738-ac9d-3bf8-9cc3-e2022a325dcd | -2.81342 | -54.04811 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0b0b319-a111-39b2-a22f-29b63a45141f | -4.17305 | -48.63506 | 2024-12-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c424fa3-d498-3d60-848e-745fd76407e4 | -2.80656 | -54.02339 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca8c1251-45c8-37cf-90a3-8ee70321bcef | -3.05978 | -50.32925 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0caccd21-3e83-39ba-9518-e6389d50dd87 | -3.51562 | -62.76147 | 2024-12-01 05:08:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a172b4e-b20c-327d-86b9-987082979ad1 | -5.43423 | -60.18638 | 2024-12-01 05:08:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60169014-9380-3447-acf4-182c739c016e | -3.69943 | -51.80159 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 888f03e1-551b-3a3d-85d7-7f2afd09276e | -3.14795 | -45.37273 | 2024-12-01 05:08:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 2d9f9170-0d23-3e02-909d-1ddb93e5079f | -1.19097 | -53.86767 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff4901c7-e893-354e-af7c-bd59a6592b2a | -2.10607 | -55.18219 | 2024-12-01 05:08:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README90.md)
