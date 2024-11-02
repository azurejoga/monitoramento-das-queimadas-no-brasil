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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00a3e3d5-208d-35d7-a629-b9cb43f26c95 | -2.88098 | -51.30965 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 865bc9ae-5700-32a7-8ed7-fbf7fb484ae9 | -2.88045 | -51.3129 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5e0698b9-cb06-3b0a-a6a2-0bfc8d08ac1b | -2.87992 | -51.31615 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b991b4f2-fa8f-329e-9450-d008fb17b428 | -2.87571 | -51.30876 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e17ced07-18d9-34fb-8e1c-27e1df33b02d | -2.87517 | -51.31203 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c274eb4-8ee4-36af-a81a-76abe84612f3 | -2.87463 | -51.31531 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d35be8fd-7042-377b-bdd5-3417a66ca22f | -2.8741 | -51.31858 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e52a5f74-c36f-3897-9424-b2d3874594fb | -2.86989 | -51.31114 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 91b459bf-360c-3242-b4c8-db5d879a8be3 | -2.28228 | -51.92401 | 2024-11-02 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da1b9e0f-c0d3-38ae-9e64-5b95e88e2c86 | -2.27759 | -51.92398 | 2024-11-02 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4ea7a11a-8fe4-305a-9112-322b5fdae3ee | -2.27699 | -51.9277 | 2024-11-02 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 51ba4732-6518-3072-8860-dba85c0765f6 | -2.27674 | -51.92302 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3ef4dd7a-a84a-3309-99b5-52a07bcbdbd5 | -2.27612 | -51.92672 | 2024-11-02 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 711c908c-8d32-3def-b0d1-d574a0d308a6 | -2.27204 | -51.92305 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed4745db-d320-35a3-a2b1-a0d8fa444df3 | -2.27144 | -51.92676 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91332549-2d74-3544-b612-6043597ccb6d | -2.27057 | -51.92581 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9dac1a37-6f06-3906-adc2-a6805ac4c9bd | -3.00426 | -51.80113 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2030cef0-f480-37c6-9e65-1ac614642ce2 | -2.89496 | -51.77873 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f0e82c32-7a0d-333d-8473-382ea6984ac1 | -2.88644 | -51.66249 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a694fe2-aa27-3aa6-b8a5-ab738e1b9edd | -2.88102 | -51.66169 | 2024-11-02 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c8a4cf7-f6bb-3c98-bd6f-efcedd692413 | -2.83859 | -51.8081 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbf4779e-0354-3385-8946-18429108b5de | -2.83802 | -51.81163 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb6c2586-2e02-392c-ba28-003b9b80118b | -2.83345 | -51.81151 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0dc86830-6410-387d-a8a9-585c57478a65 | -2.82858 | -51.80713 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 386589e0-12de-381f-82b3-15d8b944c0a3 | -2.82798 | -51.81063 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d14dd073-c3c6-3172-94cf-51e82468d99d | -2.82766 | -51.80631 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 051064af-0c1c-32ff-871f-549bcde91f78 | -2.82709 | -51.80983 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4615cb67-43ea-3d75-b276-368b8f75c79e | -2.82652 | -51.81335 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c175f1e0-a4be-3e17-a8a9-6bbe825a9ecd | -2.80676 | -51.76273 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17e574bd-4e50-3cbb-bd4e-78adac46e8f3 | -2.80248 | -51.75476 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f6a5d2aa-b6bd-3e01-b2a3-ac5524daf5eb | -2.80189 | -51.75831 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f4c6cd94-cad4-36e4-9dcd-38c628c20f86 | -2.80131 | -51.76188 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 49a37b4b-14fd-3676-90a0-c628c5c30df6 | -2.79762 | -51.75032 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 111a5ca2-245d-3adf-8bb3-91030c9653fd | -2.76573 | -51.67369 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e63a65f-daa6-3eb9-b864-339f903c7c5b | -2.76089 | -51.66935 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0f4c9be-32d8-3e8e-aa15-f7124621f9fc | -2.76031 | -51.6728 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 158c0461-17a5-3f21-a48c-f17350ca2d06 | -2.74379 | -51.7378 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cfedf8f8-2ea4-385c-8dee-1b00804d93cb | -2.74321 | -51.74126 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc951c33-32a6-3e68-ac8c-6cd8353558dc | -2.7374 | -51.73536 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 664d6d58-b552-3bb7-b0f3-5c002bd93dc9 | -2.73718 | -51.74379 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf8b963f-5d65-3b6e-8738-9b0b65ec8e4b | -2.73683 | -51.73887 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fd6d468-9d2d-36db-a3b4-f3b2b377c1ce | -2.73233 | -51.7394 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de01a189-e8f5-3bf4-b3ba-786b876b0675 | -2.73195 | -51.73447 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 320c3123-cf56-3060-b7cb-3e919178d82d | -2.73139 | -51.73796 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3ff9f55-a904-3aaf-842b-3b3d011441b9 | -2.72502 | -51.70837 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0de50c7e-33fc-3d47-bd9f-ad5ab94d8558 | -2.6509 | -51.71745 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adb1f428-48f3-3595-a00f-72ca2bb16f28 | -2.65031 | -51.72096 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65227f37-8da3-3054-b99e-7e90bb4ac545 | -2.64914 | -51.72795 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1e39cea-1a82-3444-afe3-36752ae603f8 | -2.64546 | -51.71651 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ec17391f-022e-39f4-af5a-818e194ea047 | -2.64487 | -51.72004 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e9ae74c9-4a5b-3c84-bdef-3de15374b01d | -2.64442 | -51.75611 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b51bc97c-1854-3fd6-9020-232bb8592bd2 | -2.64428 | -51.72354 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| be37693b-42b6-3868-86cc-6e449972e1ae | -2.63596 | -51.73225 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8b76597-1495-3ac7-976b-e26b0082ace5 | -2.58185 | -51.92624 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a21732c5-ca3b-30b5-8b42-90ab4fb55341 | -2.41725 | -50.50182 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e60916e-5cf2-3a0c-b7c3-7ff4fb353d41 | -2.41222 | -50.501 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 863d82fb-9551-3aa8-aac5-04417624aab9 | -2.402 | -51.30655 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a64051d-80e6-3ae5-8316-7e056328668e | -2.39613 | -51.30895 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c9d3d408-5bd3-3e26-9f07-2dfcaf7c0690 | -3.89307 | -50.98824 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 785e0e7d-9b97-3afe-b024-dfdf9f3dd3ea | -3.88801 | -50.98729 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a80b63f9-8d64-3aad-9744-153b4b4932e8 | -3.88749 | -50.99039 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 57a6811c-0127-3312-aeb5-f5ecbe27e820 | -3.88697 | -50.99351 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ffc47751-52fa-39db-b5be-90abdb9408bf | -3.88505 | -51.0364 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f646d200-304a-3cc0-ab39-6981d7622e99 | -3.87994 | -51.03565 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b525e44-0fd0-3165-adb5-577290304303 | -3.81015 | -51.16845 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9c1a561-df07-305f-9622-1b4fa8c481c5 | -3.76869 | -51.05552 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a68e4e45-59ed-344d-b4da-8a592a67b180 | -3.7682 | -51.05842 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0055456-ad00-3a3b-b914-00c8d5ba749b | -3.75698 | -51.06269 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e78c32e-d171-3364-81d7-0652cf4899a1 | -3.75644 | -51.06588 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c03251c-23fa-31fa-a3b8-4d7afbeae473 | -3.69367 | -51.17781 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80605be2-6dec-3f68-afa7-372cef6b45f0 | -3.69051 | -51.17462 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59d37fea-a5ec-320e-8d4b-8fb01b9ea5e7 | -3.68997 | -51.17774 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7771dc78-8e40-374a-b7ea-b4b35dc960d5 | -3.6885 | -51.177 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| faff8323-4f7e-3e56-9d57-024a931feabe | -3.68799 | -51.18014 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c9e1e34-c27e-39b7-9955-d522e6235ac7 | -3.61562 | -52.20899 | 2024-11-02 04:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98907cbc-8611-322c-9f53-e92ab5bedbc7 | -3.61505 | -52.20927 | 2024-11-02 04:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51dcca0a-79ba-395d-86e8-88c0356b6239 | -3.61503 | -52.21259 | 2024-11-02 04:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 073a05e8-48e5-37e4-ad89-d604607469bb | -3.61443 | -52.21286 | 2024-11-02 04:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96fd7e62-593b-3fef-adb4-d42f76c692d8 | -4.12814 | -51.07869 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f13d80d0-48ca-3ddd-8fbe-c02c870c9f12 | -4.12764 | -51.0816 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87041aff-1a31-37c0-9b82-f7c3cf5b2dcf | -4.1253 | -51.07711 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b15fa61d-531d-3dfe-90c7-1c0f10ed8c93 | -4.12481 | -51.08006 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2aa8312-4430-3e21-9276-beec4c53f6aa | -4.1243 | -51.08314 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01ebac21-04f2-3031-98fd-bc6bdfe1d194 | -4.12026 | -51.07593 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 010af8c3-1cd3-3768-b3b5-07309ae6feff | -4.11977 | -51.0789 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c981ed40-4bbd-3c77-98cf-2dee42d7e2d0 | -3.70755 | -51.6181 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa5063b7-1a2d-3a0a-ba26-95b757a1b0d5 | -3.70702 | -51.62128 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e816076f-04f6-37ca-b103-633891d21486 | -3.2668 | -53.40813 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 54e093b3-6385-3f85-b6f2-aef4693bc9e5 | -3.26602 | -53.41276 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| bd01042f-c4c4-3f99-aee8-b81412670c36 | -3.26527 | -53.41725 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 30b1870f-b3ef-3b31-b9df-e70d6d60f93c | -3.26451 | -53.42172 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 75f548e1-35d5-330c-a32a-c2e404a8e167 | -3.26376 | -53.42621 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2cc0f17e-1bde-3f95-b454-5456be0c90f3 | -3.26079 | -53.40709 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b80ab48e-f634-37c4-93bc-0385a41782d3 | -3.26001 | -53.41174 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c6904c7d-c1cb-31d2-be72-5f5e10eabfd4 | -3.25924 | -53.41631 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4278b2e3-89ad-30e5-bba3-a61c33c23b36 | -3.25846 | -53.42087 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ba96ac20-9a6b-3ed9-b657-d4d4b297f6f2 | -3.2577 | -53.4254 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3118bafb-6d02-3318-8ac8-570a844e7e66 | -3.25718 | -53.35547 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2d16a73a-6f93-366b-adc8-eb9eae60d64d | -3.25481 | -53.40588 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9286686c-c193-3245-a8cf-9643b2cf124d | -3.25402 | -53.41055 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |


[Clique aqui para ver as próximas entradas](README51.md)
