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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09e39820-093a-3cc1-a3f3-0b2ea76cae62 | -8.5217 | -43.2593 | 2025-07-09 02:50:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 65.9 |
| 7f9c97c4-e43a-39ff-816d-21742efc7824 | -11.4397 | -45.0923 | 2025-07-09 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| d73a41b0-8a9f-301f-8ea7-2210e3a8180e | -11.4588 | -45.0895 | 2025-07-09 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 596d9d67-aac5-3282-8e26-faace70eed95 | -8.5211 | -43.3063 | 2025-07-09 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| ce625148-2c8a-3fcf-9bc6-9b5a0e746d44 | -11.4393 | -45.1154 | 2025-07-09 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 143.0 |
| b75960ec-478b-3e77-ba8d-af5750fa237c | -11.4584 | -45.1126 | 2025-07-09 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 7e205063-c78f-3123-8ed2-9e77dfb386ea | -10.5779 | -49.1098 | 2025-07-09 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 653ca747-fbf7-362d-b036-3d697a4e108a | -11.4205 | -45.095 | 2025-07-09 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 5380b1a8-0aaf-3920-844e-040541c981b9 | -8.5025 | -43.285 | 2025-07-09 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 270.7 |
| 4fd55f81-7faf-3b97-b1b5-5d509653575b | -8.5022 | -43.3085 | 2025-07-09 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 05651f18-9b1d-3cb0-87dc-f1b352ced669 | -6.1792 | -48.0494 | 2025-07-09 02:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 6521a3ba-7127-3ddf-9d48-dc3d513cc02a | -7.2408 | -43.0664 | 2025-07-09 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| 72ef8d26-aff7-3af7-9b5a-59cbe2a3138f | -8.5028 | -43.2614 | 2025-07-09 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 137.6 |
| 0a0f1a62-c61b-352c-a898-44d6035bdf90 | -11.4201 | -45.1181 | 2025-07-09 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 8889d9e1-977f-3bf5-89b1-b94f2137c501 | -6.1606 | -48.0507 | 2025-07-09 02:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| a42bef41-a07d-34f5-bbd8-770c2fae68ba | -6.1606 | -48.0507 | 2025-07-09 03:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| c9bcbc95-ea3b-3f9d-9f14-3b93c1605953 | -7.2408 | -43.0664 | 2025-07-09 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| e5582c20-d393-3410-abe9-d6800260c6f4 | -11.4584 | -45.1126 | 2025-07-09 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 222796af-2cdf-3a7d-a910-e7a9a9849c58 | -8.5022 | -43.3085 | 2025-07-09 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.3 |
| a9a7eb1a-c1fc-3d86-b884-763fb4f8ca2c | -8.5211 | -43.3063 | 2025-07-09 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 83aaa01d-0486-30de-a677-a32bbdadd4b5 | -8.5025 | -43.285 | 2025-07-09 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 184.3 |
| 205453c5-40b6-3ec2-9e4b-caccf0eb0795 | -6.1792 | -48.0494 | 2025-07-09 03:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 5351cce7-5487-3fae-84b8-eda919ef9737 | -10.5776 | -49.1316 | 2025-07-09 03:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 73625631-9e05-3e14-b1eb-20f3fe2de0d0 | -11.4201 | -45.1181 | 2025-07-09 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 97b8dd24-e737-332b-892f-d787ae8050ba | -11.4393 | -45.1154 | 2025-07-09 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 0dd132aa-d612-33c2-923f-ee71d3d03906 | -8.5214 | -43.2828 | 2025-07-09 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 205.2 |
| f24dff4a-c9d3-3f56-ac54-7ad29ec30d8a | -11.4397 | -45.0923 | 2025-07-09 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 0b048fb0-254a-33a7-ba11-b158c4937a3f | -8.5028 | -43.2614 | 2025-07-09 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.3 |
| 4a21d73d-8bfa-337d-ba9e-69bc1467ae74 | -11.4205 | -45.095 | 2025-07-09 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 6403a5e6-4e05-31d4-935d-8580071ed97e | -8.5217 | -43.2593 | 2025-07-09 03:00:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| 4d714415-f26e-31d0-93ac-34523e4b7030 | -6.57327 | -38.10964 | 2025-07-09 03:04:00 | NOAA-20 | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f6ec87df-1fa7-3b86-9472-31a686858987 | -9.28697 | -40.24825 | 2025-07-09 03:04:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 514e4a88-e982-3d2b-ad53-2e46c9b7c5d9 | -9.28833 | -40.2414 | 2025-07-09 03:04:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| e77e3a28-0d2c-3ed0-900f-73ca1c41402f | -6.57424 | -38.10437 | 2025-07-09 03:04:00 | NOAA-20 | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| eed1e6c2-504e-342f-8c9d-edbe200c128e | -16.62407 | -42.21878 | 2025-07-09 03:06:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 54df46ba-fdb3-3826-98f7-682f885e97d5 | -16.62645 | -42.21253 | 2025-07-09 03:06:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| bfdf6a32-2de5-30d8-99cf-ccfbc088bfdb | -16.62487 | -42.21949 | 2025-07-09 03:06:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 221b4cfe-30dc-3eb6-8908-30e58029f6f7 | -16.6257 | -42.21183 | 2025-07-09 03:06:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 39842c84-8950-3a49-8e85-8797d175d10d | -6.1606 | -48.0507 | 2025-07-09 03:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 18a009f3-ad70-3422-9fd6-773d7b36e039 | -8.5217 | -43.2593 | 2025-07-09 03:10:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| c74434ea-9b89-3a71-aadd-d89a112ccfe2 | -8.5022 | -43.3085 | 2025-07-09 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.2 |
| 4ecc1069-7750-3ae9-995a-e7f4aec448e0 | -7.2408 | -43.0664 | 2025-07-09 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.5 |
| 4877f0a4-57a5-3dc5-aaa2-32ccb5c736b1 | -10.5776 | -49.1316 | 2025-07-09 03:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| ea0d1a5a-fb1a-3a78-9eb7-712288460af4 | -11.4584 | -45.1126 | 2025-07-09 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 4fa83745-be1b-37aa-af14-a55db0f05654 | -11.4201 | -45.1181 | 2025-07-09 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| d0f22f1e-443e-3842-93a3-d7f659cf1b29 | -8.5025 | -43.285 | 2025-07-09 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 202.4 |
| f1a623da-3f21-32d6-a3c1-f65f7e1acac1 | -6.1792 | -48.0494 | 2025-07-09 03:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 0fd73ccd-5939-344f-a216-9c8f9540d637 | -11.4393 | -45.1154 | 2025-07-09 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |
| f4acffcb-0fd5-3f5b-902c-b5f0c03a9e63 | -11.4205 | -45.095 | 2025-07-09 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| a13ee822-807c-3793-91d3-08a8dc988673 | -8.5214 | -43.2828 | 2025-07-09 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 177.7 |
| e9f9499d-8783-302b-9f61-38dd1a744a28 | -8.5211 | -43.3063 | 2025-07-09 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| aebacaf4-215c-31a4-9d61-151d89c161fb | -11.4397 | -45.0923 | 2025-07-09 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 78dc06bf-bf4f-36c7-973c-ce606f92886a | -8.5028 | -43.2614 | 2025-07-09 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.4 |
| 2e441a3a-6ff4-36a6-b31c-c1023348da6e | -11.4201 | -45.1181 | 2025-07-09 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 1bb5d33d-ef23-3142-b1b8-b326758f4a0f | -8.5028 | -43.2614 | 2025-07-09 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.5 |
| 9e0491a4-6738-380c-838a-b6b5074795dd | -11.4397 | -45.0923 | 2025-07-09 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| d94022ef-42de-3734-95e6-3a88040168b7 | -11.4393 | -45.1154 | 2025-07-09 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 152.8 |
| dd0bdb58-b2d8-37ee-b153-06d8a6f908e8 | -8.5022 | -43.3085 | 2025-07-09 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.4 |
| 8b94ba23-f0f6-3fc3-9128-7f9cc52cde40 | -8.5211 | -43.3063 | 2025-07-09 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 8dcb9ceb-ca53-3adf-a714-e9b3dc528e4e | -6.1606 | -48.0507 | 2025-07-09 03:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| d550dd7d-6979-37e0-bd09-72804ed8e848 | -11.4584 | -45.1126 | 2025-07-09 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 588f964e-c2c9-3f45-bd19-8a1705858fe8 | -10.5776 | -49.1316 | 2025-07-09 03:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| c203daaf-32c5-3238-9fdc-a45e02d550ce | -8.5214 | -43.2828 | 2025-07-09 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 213.2 |
| 61e273dd-eb52-307e-8527-2b1b15422b88 | -8.5217 | -43.2593 | 2025-07-09 03:20:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 93.3 |
| 17a8c452-852c-3205-ad58-a6678d2946de | -8.5025 | -43.285 | 2025-07-09 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 186.9 |
| 4674dd28-4392-3734-973e-152aaefa5b79 | -6.1792 | -48.0494 | 2025-07-09 03:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 2d2c8221-156d-3f65-9c0c-cc1cf725e080 | -11.4205 | -45.095 | 2025-07-09 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 26cfae2c-dc36-31f0-99cc-21c866a45685 | -11.4201 | -45.1181 | 2025-07-09 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| dd4af360-0342-3147-a854-d6540b48dff2 | -6.1792 | -48.0494 | 2025-07-09 03:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 938af713-1f6c-3788-baa4-84e5e8bda839 | -11.4393 | -45.1154 | 2025-07-09 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 94456d90-32c6-3f12-b825-2ea32fa6a082 | -8.5211 | -43.3063 | 2025-07-09 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| cf1bd6ce-628d-34a9-a6ac-2f31d37dfdd3 | -11.4397 | -45.0923 | 2025-07-09 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 6a07bcfc-6ea2-3c02-bd60-931711063600 | -8.5028 | -43.2614 | 2025-07-09 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 138.9 |
| d84b2142-0777-387e-8561-9d99384a22d4 | -10.5779 | -49.1098 | 2025-07-09 03:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 30c38f3f-61e6-3638-9cc2-4b8597403d92 | -11.4205 | -45.095 | 2025-07-09 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 61dcfb48-575f-330c-9adc-2b3050e49377 | -8.5025 | -43.285 | 2025-07-09 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 262.3 |
| 6a14c282-12a9-3b9f-b437-0427af544a88 | -8.5022 | -43.3085 | 2025-07-09 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.1 |
| 92725d82-44ee-3d6f-8ca2-871435deec98 | -11.4584 | -45.1126 | 2025-07-09 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 108a61a0-4c08-308a-bebd-f99605d2fd8f | -8.5214 | -43.2828 | 2025-07-09 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 164.5 |
| 01ce5aec-ae64-36bc-8d88-cad981e92c08 | -8.5217 | -43.2593 | 2025-07-09 03:30:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 70.0 |
| 6752ebd2-f00d-396c-afe1-a6e27c8901f3 | -10.5776 | -49.1316 | 2025-07-09 03:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 2dbd1764-1bd6-3a66-b8cc-0f639a503c6f | -8.5022 | -43.3085 | 2025-07-09 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| 51da37d6-9a6f-39c6-84a5-ff616393eca5 | -10.5776 | -49.1316 | 2025-07-09 03:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| b65c8efa-3327-39b7-a908-231ede420405 | -11.4393 | -45.1154 | 2025-07-09 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 31c7f1bc-4d3e-34d3-b6b4-e76f16f9f365 | -11.4397 | -45.0923 | 2025-07-09 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 5e9eaa06-3890-30f8-8596-96e3f047259c | -8.5214 | -43.2828 | 2025-07-09 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 166.0 |
| a342e2d2-b9bd-3d99-8668-22cd2e4f4b7d | -8.5028 | -43.2614 | 2025-07-09 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.7 |
| bfa5cabb-a17d-33b8-9f2b-c0e67ef31240 | -6.1792 | -48.0494 | 2025-07-09 03:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 3c7e33c2-0822-3295-9662-4d2a9d6b6934 | -8.5025 | -43.285 | 2025-07-09 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 243.2 |
| 45fb2cf9-e9af-319b-a648-292cca5bef88 | -11.4205 | -45.095 | 2025-07-09 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 3833daed-9493-3c6e-a684-8f854974d49d | -11.4584 | -45.1126 | 2025-07-09 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| b6040fb5-8ec9-31fc-baec-ce2251fa69b4 | -8.5217 | -43.2593 | 2025-07-09 03:40:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 68.9 |
| 46987cc6-65c3-3d38-9e8f-128fe1230e11 | -11.4201 | -45.1181 | 2025-07-09 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| dc2e5847-9fbe-30ef-8124-f6dcdfade471 | -8.5211 | -43.3063 | 2025-07-09 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 79764eb9-e11f-344d-b76e-f235808c737a | -8.5211 | -43.3063 | 2025-07-09 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 622a1a41-8abb-321d-ac0f-a469c87784c9 | -8.5217 | -43.2593 | 2025-07-09 03:50:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 91.0 |
| f1094cbf-9f4f-307a-a297-9e1202ec6ced | -11.4201 | -45.1181 | 2025-07-09 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| e9488e1c-0990-3bc6-a924-b6ba5e39825f | -6.1792 | -48.0494 | 2025-07-09 03:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 60dff0cb-fc19-3521-8cf3-ec05d85162d5 | -11.4584 | -45.1126 | 2025-07-09 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 228c155b-ef5d-3f0d-a63e-96de3a6b0acf | -8.5025 | -43.285 | 2025-07-09 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 203.5 |


[Clique aqui para ver as próximas entradas](README7.md)
