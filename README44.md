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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68a03303-33f4-331e-b69e-4726edbe880e | -2.1777 | -47.56178 | 2024-11-07 05:10:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f904d4a6-ea3e-3532-80b4-d10e445128fc | -2.83816 | -51.35163 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5853e563-fbb5-3839-83b1-4b8c1cf586a2 | -3.08932 | -52.98372 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94e5c125-6068-34a9-b2e1-c8f258944944 | -1.72512 | -53.28893 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cc35b5b-dd20-326c-82a1-639d1c0e1507 | -3.17983 | -50.5861 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 556efa0d-02f9-3134-aedb-fc2b08dff1e4 | -2.58205 | -51.33576 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c4719c2-fe76-3729-a31b-a6345b700912 | -1.11275 | -47.27961 | 2024-11-07 05:10:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1d08fec-c228-32f5-aae6-579f2714265c | 1.45411 | -50.71223 | 2024-11-07 05:10:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7766d0c-aee6-3bc8-8fb4-c2444d508376 | -2.43276 | -53.66126 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| afccb26e-1cb2-3c0d-b4f8-c30e45afcd26 | -2.94792 | -52.91154 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c715486-9a5b-328c-9a92-3ae62fdc0350 | -4.19193 | -51.01855 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a15609e-b2bb-375d-9b99-0ddf9e50f206 | -2.6732 | -51.82801 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bbc093b9-5708-3c58-8a1c-6ef029fd379a | -2.23594 | -53.67007 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ddf9b485-12ae-3bde-9d54-3ef5f0dff096 | -3.23653 | -50.45034 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0873299d-9c99-3efb-a9c7-5b10e143ca19 | -4.34445 | -46.78155 | 2024-11-07 05:10:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f70fcc56-f7b7-38e9-b647-272c26de0c1a | -2.82663 | -52.94516 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3dd57844-aa47-305e-bc34-1e6dc72a53b1 | -2.73339 | -51.74371 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c0672a2-7968-35fd-bfb3-60630b7208a1 | -2.80873 | -51.80069 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a36d385-eb22-3cdd-839a-e6df83cdafd2 | -1.76811 | -54.18359 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3201287-522b-36f8-956c-7fab6d45a298 | -1.33978 | -54.61324 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 933d423b-2346-3f3c-95a9-c01989cffbdd | -2.88518 | -53.97153 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b82b2d7e-257e-3c47-8162-3c9b87ba85b0 | -1.39218 | -52.18906 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c718e706-43be-3d5b-b0cc-24cf341a62e5 | -2.08139 | -52.04457 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 447b0a23-df3e-3a4c-bc62-4db2a6944d71 | -3.43664 | -50.25741 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91f766f6-8d88-3241-942a-86bbd20830cb | -1.11091 | -46.8339 | 2024-11-07 05:10:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0340a57-1ef2-3b0f-a8fc-bc9501e68231 | -1.2252 | -54.53865 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d2e56db-56b4-3443-af91-07ef2f9fc9f7 | -2.71161 | -52.96139 | 2024-11-07 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c6c5f30-ea37-3a38-b1c8-f5e1739c2c88 | -2.91938 | -49.60152 | 2024-11-07 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84ba990a-81d1-3f06-a3ee-adc59bbc7632 | -1.18053 | -53.69762 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a1afb6fc-2b56-33eb-8411-aebc734e7c64 | -3.02896 | -54.07577 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae866d81-86c7-394e-82be-a5d1fdd37bb4 | -3.7086 | -48.99164 | 2024-11-07 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5cac6a83-e69c-3fd8-a564-432c94e19fe6 | -2.84576 | -51.77118 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 976f24a7-9553-3b6c-8df8-029f59e7bf45 | -2.84398 | -52.90684 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6029c833-43c9-38fb-9050-504ee49b2633 | -1.13509 | -54.10185 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2301b7b-dda4-30d7-8e43-68e1ed3653ae | -1.10266 | -54.19661 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 459fe071-1dbb-3e27-ab84-8a41b5200b97 | -2.88031 | -51.31581 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68ad7f6a-e72b-3c77-8f13-25197ae5a49d | -1.3931 | -52.20832 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ac568817-d10e-3964-8166-084f90ba6f5d | -1.15951 | -53.71743 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 615ac274-a7ae-3260-82db-4c32481c0ab7 | -1.46219 | -52.56273 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36a76acd-9668-3f59-a68d-575a55173a2e | -4.66688 | -46.33813 | 2024-11-07 05:10:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b46ca9f8-db0d-335e-a92c-619ea90f55a6 | -2.99637 | -51.05167 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 781b3a4e-f9a4-31be-a6c2-21cee10fec42 | -2.20671 | -53.71884 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0bea4bc-b996-38e7-8c8f-852be2b26c62 | -3.58888 | -50.22498 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3781898f-f807-3893-9f52-2b9cb96379d4 | -3.13127 | -51.10895 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cde62c45-bdf2-3522-836d-f4bd5d310fa4 | -2.82567 | -52.92674 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b07232d4-bfe9-3226-8e36-d9f70aad64aa | -4.08941 | -51.00939 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c5b49c81-7eff-3f90-b77d-ed6856403439 | -3.0138 | -53.23579 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67e0d163-3ae4-32da-968e-169d3d6607e0 | -3.12289 | -51.10769 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 96cfd9e8-0903-3b42-9d94-3fa069ed1e5c | -1.52725 | -52.16879 | 2024-11-07 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3376555-3ae2-31d6-b0ea-358e9d105ae2 | -1.23996 | -51.7681 | 2024-11-07 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 340e20b3-ebad-361a-b536-51c635a32243 | -1.24203 | -54.17913 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 54fec452-2198-393d-893c-b6219fba3871 | -2.77725 | -52.86945 | 2024-11-07 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c032a29-3c70-3d35-8e94-3bd85ee856de | -1.55397 | -52.27029 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 8413724a-717c-3286-a1b1-b59bfe6698e4 | -1.39002 | -52.20306 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d42600e4-da62-3cba-97b1-4e421fc73191 | -1.22195 | -51.75525 | 2024-11-07 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60052ffe-5913-3267-aefd-abd4809943ed | -2.7684 | -53.22507 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2b13e727-960f-344b-b7c3-c47b813f54f1 | -3.63871 | -50.13574 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acaff1e9-6628-3c29-9083-360b7516fa78 | -2.81583 | -52.9659 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 70c212e2-2695-3807-8584-384a0bbdc381 | -2.7641 | -53.22873 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6560b8ae-51da-3f59-8fd1-46205e872e26 | -1.95596 | -53.07467 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afb45e09-4ea1-36e7-86e0-11f5ba96caa3 | -2.60338 | -51.3054 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d32d9959-0c8d-381f-b00f-3f638ca2fa3c | -2.2061 | -53.72285 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4d8c1a5-cb08-32ea-b8ce-8db329579454 | -3.22389 | -50.38266 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5152295b-1e98-3dd8-a3e6-f44d6ea9bb15 | -2.81413 | -52.95227 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| eb95ef89-ae45-3fa9-aa53-ffc02f62a1d0 | -2.78778 | -52.87547 | 2024-11-07 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 971df719-784a-3b93-84d9-ac327a90fd26 | -3.03731 | -54.20879 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35b162b6-6ed5-34cf-86f5-833fecb050a0 | -1.32962 | -54.61158 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65336ed4-e45c-3895-b5ea-1aba4f784451 | -4.19621 | -51.01923 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25ff9ae2-4727-37e6-ba33-127528d74a4b | -2.03133 | -52.34409 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53b9b04f-da5d-3b17-8fd4-ef0bda3a1157 | -5.02968 | -46.84558 | 2024-11-07 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f2971911-5c61-35e3-a6d0-a2a054ee9863 | -3.45023 | -50.3736 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 92f4cd9f-b2e6-3e2a-9bd2-746f90c37f50 | -1.19061 | -53.89638 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 8d7b549a-a23f-3176-ae52-0a41588ddad5 | -3.11818 | -51.10434 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95b0f048-8a47-333a-86d8-b1ea33c33e48 | -3.24953 | -53.36073 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 519ff118-c395-39b0-9b43-c4f8b2546bf1 | -3.7119 | -49.0032 | 2024-11-07 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 57f757a2-da0f-31c1-9af3-1b0247744975 | -1.13844 | -53.71457 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d7b8678d-95d5-3fb0-a6b1-c2250a82b212 | -2.87313 | -51.31558 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78c23f32-ce53-3f5a-9608-49a2b8de2356 | -1.15006 | -53.73211 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e635dd2-fc36-30c6-9439-7f9c5de21d77 | -2.94655 | -52.92043 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b76b7e88-6fca-331f-b37a-c2355fa9a3f4 | -3.6157 | -51.3358 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0825c9b5-096b-32eb-b3ac-2247c9222f57 | -3.15552 | -50.20469 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce1b7fee-857b-3b59-b28e-17674269c2fa | -1.92694 | -46.47654 | 2024-11-07 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c93dc50f-fb40-33aa-9753-abed280a88be | 0.04204 | -49.52021 | 2024-11-07 05:10:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f4c3425b-533c-34f6-9316-daa800fe1baa | -1.02771 | -47.05672 | 2024-11-07 05:10:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c458b29d-f74f-31fa-bb54-09ca1b4b90ae | -3.24345 | -50.46438 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1df8cdd7-b259-34a3-a775-5540997983af | -3.00868 | -53.24568 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d169b59-eebf-33d9-adaf-5fbd3f66c5f8 | -1.38765 | -52.19314 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41eacb90-8357-3521-99ef-02de3cf02b79 | -2.82639 | -53.97863 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 68ddae9e-08b3-33f7-ab16-c315a67283c1 | -3.12177 | -51.10881 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00c5a4af-897e-3d79-a1a5-6979757ee90a | -3.13862 | -51.20387 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de1e4a6e-8bc0-34d6-b5a2-07060b2bdca3 | -1.02426 | -47.05741 | 2024-11-07 05:10:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b00282a8-1cac-3887-ab60-5655302b6121 | -2.95622 | -53.71871 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46b3ca30-91c5-3eba-9f82-73179d6f9fb2 | -4.39547 | -50.50021 | 2024-11-07 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff6f8afb-d98e-37b1-84dd-ca8fc6e80f81 | -1.3042 | -54.55105 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86f92708-f248-3945-9d4c-1756028e569c | -3.09852 | -53.71402 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e5a1703-6c7f-3143-b462-922ff1d51673 | -2.76045 | -53.22816 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54294c64-63b2-3a2f-8e15-4dd53928c39d | -3.44257 | -56.92933 | 2024-11-07 05:10:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7bd03376-786a-37c0-bfa8-45129314a679 | -1.28013 | -53.17715 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c59b0b3-d019-35b0-9877-6898a02e3178 | -2.66367 | -49.87564 | 2024-11-07 05:10:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cd945dc-3003-3b2d-ac5e-920d87f409bd | -1.32512 | -54.64068 | 2024-11-07 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README45.md)
