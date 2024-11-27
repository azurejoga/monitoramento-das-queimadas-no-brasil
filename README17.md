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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67c6729b-7a98-3f31-abf0-f029fbd7a540 | -1.4474 | -52.57961 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 164ace1d-8652-395f-8495-34515ecf04cd | -1.67026 | -52.72688 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| e05e1d0b-10c1-3eee-9401-ea54fc5091a1 | -2.70022 | -45.66826 | 2024-11-27 01:09:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 84.8 |
| f223556c-68b3-3eeb-9717-0ba1eb221738 | -1.3554 | -54.63053 | 2024-11-27 01:09:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3a02cc41-1097-31eb-8b10-5270510f50d4 | -3.26555 | -50.4385 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3f7398a9-dd1d-305a-9847-7a2a0e0727c6 | -1.07073 | -53.37608 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e453775c-b283-3337-9636-a0430147cad0 | -2.60358 | -54.26818 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2ea577b6-db79-304d-8691-1024d4634d49 | -2.60877 | -54.23948 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 63b666e4-660c-3a63-8888-3854e1913bcc | -3.11584 | -53.2499 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 357962ec-62fd-3ad5-bd68-c533f6c57ff5 | -1.3114 | -51.73806 | 2024-11-27 01:09:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 6a3e1c46-7edb-3a74-9ad8-dc107c77f2fa | -3.24252 | -53.03104 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e323c626-0457-382c-90a3-9b734049fdb6 | -3.24893 | -53.4147 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 68397746-782e-32bc-b375-2112a6beba6a | -3.33334 | -51.64018 | 2024-11-27 01:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ab25b3c5-5ae4-3ca3-9ae7-a19eaad9853c | -1.6589 | -52.71036 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 46a03ca0-e602-3f47-acff-88f5981b1206 | -1.19626 | -53.88834 | 2024-11-27 01:09:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f5f9f962-46b2-3965-b045-617c461207f6 | -3.2915 | -50.75838 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f3313a36-5bbc-302b-ac75-4b9a908a8522 | -1.10562 | -52.10935 | 2024-11-27 01:09:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3648dd5b-ebb7-350b-9fea-f443f770aee1 | -2.78314 | -49.21034 | 2024-11-27 01:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 657f9e6a-5c3f-3a27-bb82-126dcb11df53 | -3.81512 | -47.46775 | 2024-11-27 01:09:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ee790abf-2642-3031-8eaa-20c4886d3dda | -2.94023 | -51.53098 | 2024-11-27 01:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 950308a7-d675-3e51-af5f-7aca60dbef73 | -3.75099 | -51.59686 | 2024-11-27 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5430b6e1-4b02-317c-8553-abb2df7e9904 | -1.33494 | -52.62888 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0a29696e-393b-3d2c-bc28-fab2b21a4596 | -3.18542 | -48.42451 | 2024-11-27 01:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| b08e38fc-0369-3480-be74-7b63e02a8993 | -1.62246 | -52.5792 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5cb1db94-f40d-3052-8a74-ca5c3a99194d | -3.05238 | -53.71744 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0c3e7d91-5c3c-32b5-be0b-81fa7f89e52b | -1.14899 | -53.67897 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| bc6e0f89-b015-3613-ad13-e52dc16222a9 | -3.87836 | -50.14584 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a80f76c5-77d8-3fbd-896c-13e11bf15c9e | -3.05628 | -53.27631 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| ae1fdb33-1195-3be2-ad23-8d8cf7e09f83 | -3.23381 | -54.23068 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 71a5fbfe-20ce-309f-a351-0ef848f15aa1 | -3.51849 | -54.63193 | 2024-11-27 01:09:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4612eed5-b22b-33bb-8068-f8369797636b | -1.15784 | -53.67772 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 630bf0a9-e0ed-3f9e-b885-a7c98fc34aa0 | -3.50036 | -53.82509 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b760e38f-b684-356e-ae93-9ac2b31dad75 | -3.51364 | -50.30968 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 3e62f7c3-57e9-35f7-a22b-51ef009913ad | -2.71163 | -53.18752 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0ecba8be-74c9-365d-ba2f-deaaff17b8da | -2.68626 | -45.6703 | 2024-11-27 01:09:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 3f84ff81-76ec-375b-b705-a7d0d7f3b5c5 | -1.2364 | -51.79308 | 2024-11-27 01:09:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 72bd44bc-99cf-378f-9c39-6948435800de | -2.85596 | -53.96431 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 10dd571f-4ab4-39dc-b843-e52fa4423b96 | -3.30654 | -53.75463 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fca1da80-7d77-3bfd-8acc-219807c4f278 | -4.21196 | -50.88693 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 0f2f3e1e-08aa-31f0-92f5-24725ab662e9 | -3.24303 | -53.63294 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 14929ddc-9476-3840-897f-9c85e68eab07 | -3.10502 | -50.37158 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6539fe99-0077-304e-bf9b-32382e909b3a | -1.58552 | -51.27081 | 2024-11-27 01:09:00 | TERRA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 85041009-62e3-3063-badb-bbcc7a504b19 | -1.67787 | -52.44627 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 781cc315-4306-3691-b6b3-8f59c64a4c39 | -3.39394 | -50.32215 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 93d29554-81ca-3352-8a20-3f8863cc4fac | -1.27033 | -52.16763 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| bc4eaeb2-2cfe-3e28-8538-10bf5a7c19b9 | -1.67468 | -46.91566 | 2024-11-27 01:09:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 463b1a1a-01b6-3446-a927-66f3fc30eca7 | -3.1876 | -48.4387 | 2024-11-27 01:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 3a6e7e9b-2fc0-314b-a1be-3294ab642892 | -2.8425 | -46.8193 | 2024-11-27 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 6998e8b6-aa65-3f15-a19c-5b72eb431632 | -2.8424 | -46.8413 | 2024-11-27 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 0988171c-164d-3378-87e0-8b7fa37bbc8d | -3.0393 | -48.5082 | 2024-11-27 01:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 214.6 |
| 21f8563d-b180-3745-b336-8b41b8055137 | -3.5411 | -52.1442 | 2024-11-27 01:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| f7c25e75-bee1-3964-8f49-7feced1a908f | -2.8347 | -54.1125 | 2024-11-27 01:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 05fe66a1-f8dd-3262-98da-8d0d3ee0ea9a | -4.2237 | -48.6557 | 2024-11-27 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 159665ef-b873-3952-b3f1-90124b82474b | -3.9675 | -48.0634 | 2024-11-27 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 21bdeac9-2d44-3673-9709-3aa0596746f0 | -2.8239 | -46.8419 | 2024-11-27 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 853ca733-8178-324e-8b50-4259997a9999 | -1.9376 | -45.7141 | 2024-11-27 01:10:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 09fdd8f3-ba4b-3652-83a7-c9a634cd9379 | -3.6529 | -44.4807 | 2024-11-27 01:10:00 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 39193d74-dd2b-393f-99ac-cae1749c9a96 | -4.1417 | -43.8135 | 2024-11-27 01:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 164.3 |
| d96241c8-9008-373e-84da-0041ba948816 | -1.9562 | -45.7137 | 2024-11-27 01:10:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 4886c3b6-eba3-35a9-bb3f-f37f28ed0cfe | -3.0578 | -48.5076 | 2024-11-27 01:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 9270a42a-b78a-3025-8795-eea74a4e4fce | -3.9674 | -48.0851 | 2024-11-27 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 159.9 |
| da1da431-910d-3250-9369-d2447cbb6b6c | -4.1419 | -43.7905 | 2024-11-27 01:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| e0406812-1d08-39ba-86e2-698c3840d8f6 | -1.6813 | -52.4537 | 2024-11-27 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 00c832ca-4128-3840-95c9-b54c0e5a0c1d | -4.7197 | -46.5605 | 2024-11-27 01:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 45.9 |
| a8ef9356-95ae-35cd-872d-cf442075cd67 | -1.6813 | -52.4333 | 2024-11-27 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 57277d17-d21f-3ee6-b437-0da501162ae6 | -1.9376 | -45.7365 | 2024-11-27 01:10:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 19f3bfb1-f0ad-3eae-9d62-b070f7874f4e | -1.6629 | -52.4336 | 2024-11-27 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 2d666f0b-5a2b-3b4f-89e5-f84ecd2ee173 | -3.1692 | -48.4179 | 2024-11-27 01:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 7c20e831-8362-341f-bdec-e549bcfb8db6 | -1.6629 | -52.454 | 2024-11-27 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| cc945e4b-0728-3d42-aaa7-8c87b63b612d | -2.8346 | -54.1326 | 2024-11-27 01:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| b16cd0b2-b778-362b-8bc6-4970941ec677 | -1.6444 | -52.4951 | 2024-11-27 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 7c85dd69-93f7-34cb-ac4b-8f5a92d505d7 | -3.5226 | -52.1653 | 2024-11-27 01:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| bf3dfe0a-8dd2-384e-b9f9-8bc1313a0d16 | -4.7195 | -46.5827 | 2024-11-27 01:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 19d83d83-8e81-3536-ae22-a8c3e50df9d9 | -2.6987 | -45.6705 | 2024-11-27 01:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| a10c503e-901b-3b9a-b5ea-b321e4e6bdd8 | -2.6988 | -45.6481 | 2024-11-27 01:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 5ab6e435-417d-31d5-a0c6-9dce0557fd49 | -5.9788 | -45.3621 | 2024-11-27 01:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| a31008ba-1fab-3b2e-98e2-5188a5a2dbf8 | -3.0392 | -48.5297 | 2024-11-27 01:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 30afe012-b15b-3b43-99b0-1ddef2c7dda3 | -3.0577 | -48.5291 | 2024-11-27 01:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| aabe3f82-d5cf-3976-80f9-4cdbc1f53058 | -4.2114 | -50.899 | 2024-11-27 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| ed42654a-bb57-34b2-af7e-1d10656c5d80 | -2.9968 | -45.4584 | 2024-11-27 01:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 141.8 |
| 5c5fc2a5-f277-3b4a-8872-c59b039df355 | -3.1691 | -48.4394 | 2024-11-27 01:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 120.1 |
| beb59118-3ded-35c1-97b7-a2ea16c5e906 | -2.824 | -46.8199 | 2024-11-27 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 445b6cf6-c4df-3c58-a5ad-349140dfc4a4 | -2.1928 | -53.7839 | 2024-11-27 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 0793dac6-f4df-3139-af9e-02340411d2fd | -4.2236 | -48.6772 | 2024-11-27 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 64cd18ef-4a44-3c78-b8e9-66253eb1f111 | -3.5226 | -52.1448 | 2024-11-27 01:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 61e867d0-c86a-309c-95b0-dc52bc6204cd | -1.9561 | -45.7361 | 2024-11-27 01:10:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 66a92509-b3a8-3f26-95f2-779942b30425 | -3.541 | -52.1647 | 2024-11-27 01:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| a23e4f4a-2666-37ba-8244-1d67ede179a9 | -2.9967 | -45.4809 | 2024-11-27 01:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 7037b557-1325-37e7-9f58-0809db882815 | -5.9975 | -45.3607 | 2024-11-27 01:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| d8849b6b-d9bb-316b-bb79-1c77500eb2ac | -4.2299 | -50.8983 | 2024-11-27 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 9c6fd290-efc7-3e73-b83c-068ba227a7ba | 1.47349 | -56.06542 | 2024-11-27 01:11:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 21dc2667-dff0-34e4-bfb6-cd50a21e52c5 | 0.65643 | -50.83443 | 2024-11-27 01:11:00 | TERRA_M-M | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f3440d05-4219-34a8-b630-2bbc0198e2ca | -0.26774 | -51.51887 | 2024-11-27 01:11:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e163c878-98da-340c-a0a5-0eab78ff753b | 0.94633 | -50.73417 | 2024-11-27 01:11:00 | TERRA_M-M | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 946dde4f-7c84-3a27-a26b-bc13b2d0a31b | 1.46414 | -56.06401 | 2024-11-27 01:11:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| e1de44bb-c0dd-3595-8ee6-1d90be38fae6 | 0.97824 | -50.12507 | 2024-11-27 01:11:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.2 |
| bcc0c0fe-5348-38c2-be1d-fdac29547fac | -0.02558 | -49.63887 | 2024-11-27 01:11:00 | TERRA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c6188b2d-2198-30da-9f9f-7d2c211654c5 | 2.08424 | -50.63712 | 2024-11-27 01:11:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 40ab3f7d-1127-3b9a-99a3-add8ece8b12a | 2.07406 | -50.6357 | 2024-11-27 01:11:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 04e58630-42df-3d6a-a639-454240912838 | -0.2722 | -51.61849 | 2024-11-27 01:11:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README18.md)
