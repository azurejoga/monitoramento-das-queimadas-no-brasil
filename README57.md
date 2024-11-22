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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f28ca94c-91bd-3613-b333-30d096d5a7d6 | -3.7503 | -54.47602 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e2bf508-7790-341f-8abe-126677d10551 | -4.11303 | -51.06078 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e114536-01e0-30ae-9d35-eff09fdf57cc | -3.28149 | -53.82529 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 11a71301-248f-395a-b1d8-8386dfe48543 | -2.44614 | -53.68139 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 636ad9f3-4dca-36f0-95ed-93fcd9ffcff5 | -3.22894 | -54.25605 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 119e5f76-e5f1-3a00-84d8-f5c11446a466 | -3.34394 | -50.50883 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 36fb38fd-0d25-351c-9769-80ac41ac4ffd | -3.38144 | -52.45537 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6999ed0a-6369-38c3-acc3-de9c70faafa2 | -3.22021 | -54.24952 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f913693a-8b2e-3e5b-a5b1-86549340d252 | -3.85315 | -52.34852 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f6832b4-ebcb-3fc6-b34f-a48b05ddf442 | -4.20361 | -53.49904 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2b0c5e4-65c7-3a00-9d9d-c8574d1aa3e5 | -2.78607 | -51.40778 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7cc7dce4-6863-385c-98d4-86c5b316cffc | -3.20045 | -54.24452 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 42d805ac-8166-3e4a-bc0a-abd49dad7517 | -2.95373 | -53.72139 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 613b8872-2808-3d06-88fb-7b8a19100c43 | -3.23745 | -53.63065 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ba0afa9-d558-3093-8639-b6422e8ae00e | -2.40075 | -56.04019 | 2024-11-22 05:29:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec9aca58-ac5e-31c0-953d-11a354077239 | -3.83759 | -52.25567 | 2024-11-22 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 965344a2-3fce-3e57-b0e2-b1b53570c8c0 | -2.22423 | -53.72601 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d42659f8-7bf1-3a9a-9012-7afd6f12991c | -3.18367 | -54.32352 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a822b0c8-bf62-372b-8be7-153f4e47d9ed | -3.5431 | -50.51941 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 39f0b51b-0adb-3b78-aaf7-7740b043f67b | -3.8321 | -52.25489 | 2024-11-22 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c5ddc1d0-c666-343a-aaaf-27e81ff91957 | -3.53351 | -51.09971 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7fa993a-7efd-3768-84e3-55fe151489ed | -3.18443 | -54.31854 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 96103183-55ae-3a17-a336-bf9be0b80507 | -4.13991 | -54.66323 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2beaaf89-1fb0-34ea-b526-c8da730216e6 | -3.2093 | -54.25801 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 052e3262-725a-390a-ba6a-0318ee464851 | -3.01191 | -51.01294 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd019b75-fdf4-36f9-90f3-da89407d34f0 | -2.91269 | -54.77892 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0e43ebe-a068-3def-8036-2801c760811c | -3.51869 | -54.68277 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12775919-aff6-3f8d-9996-9675fcce75a1 | -3.01038 | -51.30722 | 2024-11-22 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 18610140-8203-3d7e-99d7-243f8dc6cc99 | -3.84149 | -51.14536 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 752a966e-ed2a-3f62-bc0c-187206b3e2c0 | -3.64099 | -54.31924 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2f27e5c4-e8ba-3421-abda-f58e97729f77 | -3.50947 | -53.80602 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| cda26b1d-561c-3067-ba52-a1c3d5e7dfca | -4.07148 | -50.90301 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fdc93ae5-0b7b-31eb-bfed-8978b395eeec | -3.29137 | -53.86036 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 16488a39-835b-344c-aeb6-6e392894efd1 | -2.84956 | -54.00315 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 46d1457f-618b-343a-ab81-9cb010010296 | -3.21476 | -54.25372 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1a22bf6b-4b14-3e1a-88c4-c1e371935bae | -3.27096 | -53.82906 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e93d42a8-3a34-34a1-9a8c-70bc3802c5c2 | -3.52169 | -53.79089 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cda52690-43b6-3b46-b789-728aa564de8c | -3.2012 | -54.247 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5968bc5e-0c6d-3513-8683-9aadd8cdf9a0 | -3.24131 | -54.23775 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ced1eb94-ffd4-33d4-bd88-03920afc221c | -3.21143 | -54.24324 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a6682d99-4000-393f-983a-4b6c3d79681f | -2.05543 | -55.45624 | 2024-11-22 05:29:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8b15ba6e-1d88-3e7c-8b7c-74dbfafd9e3b | -3.30159 | -50.36717 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ccab004-fd07-35c8-8b5d-ef5c20b69989 | -3.83245 | -52.2587 | 2024-11-22 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1ba5a542-8819-3260-8281-b0a726f874a8 | -3.32212 | -54.08733 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2dda63ab-8599-3f19-a288-14c6fb8a6be2 | -2.85012 | -53.96591 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 82965e3c-fbe2-3ce7-a8d2-b5099818d4ec | -3.07146 | -53.29523 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9056519-7232-39da-ab17-f67c6390fc56 | -3.19777 | -54.32588 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8dd31301-61f6-37c1-b75c-c86b1928c5cf | -3.34956 | -50.50878 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ddb6e33-1298-345c-9403-37a14869864e | -2.78277 | -51.71954 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 142bc9ff-c9f0-3b2a-922b-1010507a96d7 | -3.09696 | -54.2908 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c6c4c0e2-d767-3775-ba1d-b4267eadfb0d | -3.09996 | -54.2904 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4b009145-583e-3021-90ba-b96c5551dcde | 2.37086 | -50.77502 | 2024-11-22 05:29:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 99e670f2-2f73-3b73-b748-960969fd1247 | -3.54118 | -50.53304 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b9e55874-4367-3dc2-8484-c9644e53e68b | 1.40144 | -55.92436 | 2024-11-22 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c63b2ab2-535e-331a-bd43-50c419366a9a | 1.94425 | -60.85287 | 2024-11-22 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69b991d8-6351-3f0d-b5dd-6973b25f31f1 | -3.28729 | -53.85417 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8907cb96-4f0f-3eb6-896f-cef8d604885a | -3.56916 | -54.6867 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f510d746-613c-3d30-bcee-ddb54cb3fb01 | -4.01128 | -49.91882 | 2024-11-22 05:29:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3926a03c-0665-3e03-8a25-b0e021bc5332 | 1.94041 | -60.84995 | 2024-11-22 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57a1dbe5-d561-3ed9-8ab2-84f6cd056365 | -3.85859 | -52.3494 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0563b41f-fb17-315d-a433-16806bf1bc85 | -4.08032 | -49.28963 | 2024-11-22 05:29:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be8079ab-e5ab-3218-93fa-d09b5e308eeb | -3.28554 | -53.84622 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a009a0f5-796f-3272-838d-8d9a43621566 | -2.22268 | -53.73652 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e0b0f639-0d0a-32ef-b830-c74816c7c635 | -4.11004 | -51.05899 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c4eeb82-61bd-32a1-bace-5fb715e1bd6a | -4.20403 | -53.49608 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32e69d42-0747-379b-9489-fc748cf7f603 | -3.71208 | -53.75262 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19033ed4-bb0d-3056-9449-8ea662969bbb | -3.00382 | -51.30658 | 2024-11-22 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8dc1c9f3-584d-3154-9063-a140c4432caa | -3.34119 | -53.33804 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb93a5d4-8605-3847-bf9a-97c8f0c753d1 | 0.61353 | -51.77411 | 2024-11-22 05:29:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51f1a869-aec7-3309-8a5f-a944b65e6e6b | -3.22163 | -54.23967 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 779c0922-f7f4-3668-8a51-0570ede76dd6 | -3.57379 | -54.68739 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fc70f59e-26cf-34d2-a5e5-798588949eaa | -3.84771 | -52.34762 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 982607ec-2e9d-3e5e-8b53-aeb99790d3df | -3.34416 | -50.50322 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4d7aaca-ef36-3f0d-a284-57beb0e0d9e8 | 2.37588 | -50.76854 | 2024-11-22 05:29:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cfd394b-5272-38ba-8df4-16450e1652b5 | -3.51443 | -53.80643 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 888ea0e6-35b0-3bef-98d8-8d4062f804bb | -3.14745 | -53.13334 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c245c08c-6408-3c7b-841a-f31dcd9bba32 | 1.40457 | -55.91873 | 2024-11-22 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a81ed91-14cc-3d87-b5ec-a8ac0f82de1c | -3.17579 | -54.31186 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93b5189e-3656-3e47-b854-4eaf7c5825d2 | -3.26608 | -53.82829 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 41c97edf-c4b1-3437-bd0d-77d77e3f7488 | -3.28398 | -53.84257 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6f8304df-50c0-3080-9bbc-94d77a6d8640 | -3.6457 | -54.32018 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aef7ef48-a1dc-33d7-a974-622ce7fa7615 | -3.10198 | -53.98634 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07ed4914-fdd0-3729-ae1b-cf13ead70b68 | 2.38017 | -50.76043 | 2024-11-22 05:29:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7d6a9069-5fca-3d83-9911-4eb8c245edaa | -3.54829 | -50.52407 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 14bf49b5-e93f-3d66-85c1-8804ff837e75 | -3.34203 | -53.33221 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb39c1a3-3f52-39b8-92fd-7810a0deaf95 | -3.24312 | -54.25843 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5830a793-9389-3216-bf4a-c0613c73da96 | -3.20371 | -54.25496 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e175bbd6-422c-31b4-95c5-361980531092 | -3.28068 | -53.84543 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0886a6aa-8583-3817-a8e3-4d0ec282ee0d | -3.27911 | -53.84175 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b7f05eb7-7f8c-3a26-b1fb-bf8de26bfec5 | -4.40432 | -48.84198 | 2024-11-22 05:29:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 279d2a9d-b323-3015-a175-41cf302e9adb | -3.2187 | -54.25196 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c7e39619-6d9b-38ed-94e0-2c285cdbc3f3 | -2.40215 | -56.04166 | 2024-11-22 05:29:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c81f2081-7605-3e75-8a7a-deae26a4152a | -4.08694 | -49.29071 | 2024-11-22 05:29:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 574fbe19-c246-3331-858c-0e248e97d8a5 | -2.74774 | -51.88008 | 2024-11-22 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c5984d06-229d-31fb-9ffa-95b98af7234d | -3.2714 | -51.42868 | 2024-11-22 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9ad07a7-8fc1-3e38-a829-4d20dd4d3c7f | -3.2202 | -54.24212 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 16654c17-e988-3c68-8126-5910ce9a7330 | -2.21862 | -53.73055 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 60da099d-dfe2-3cf1-9fcf-2aab191b3069 | 1.38025 | -55.94319 | 2024-11-22 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ba341ee-4453-35b4-a950-335b89a138bf | -3.11183 | -54.28798 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 72f81399-7184-35cd-9fe1-325caf6fe16d | -3.54219 | -50.52311 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README58.md)
