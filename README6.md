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
| 820928ad-efb2-3a65-b745-87312bf62ccf | -3.1833 | -49.4429 | 2025-08-05 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 360d56e0-6a96-3f33-b647-1dd1d78e4571 | -3.1832 | -49.4642 | 2025-08-05 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 5c91f410-9727-3a02-ad12-b0c30c7b0bac | -13.0726 | -56.893 | 2025-08-05 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| a0292169-2dde-32ad-a47e-b703390ca5df | -8.9224 | -60.5953 | 2025-08-05 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 4da04417-46a8-37b7-9356-6f5d1a392e4c | -13.0914 | -56.9114 | 2025-08-05 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 622c8131-4954-363d-a29b-b037ec038dbb | -13.0723 | -56.9131 | 2025-08-05 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 109.8 |
| f02e9cdf-c648-3210-8f19-613172cdb6c9 | -8.9412 | -60.5559 | 2025-08-05 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.7 |
| cd396116-3eb6-3bd4-a504-13d22f8a68a0 | -17.2056 | -44.8214 | 2025-08-05 02:50:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 69a94f5c-e516-3257-b183-787cf536c337 | -7.994 | -43.1534 | 2025-08-05 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| 129ea91a-02ca-3b72-bedc-8abfa3885bdb | -11.9203 | -44.9757 | 2025-08-05 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| a5b8ca24-fc07-3919-b4e5-d19d80c20666 | -17.2256 | -44.817 | 2025-08-05 02:50:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 36db8f4f-be45-316f-8ae6-9891d398cec2 | -17.205 | -44.8454 | 2025-08-05 02:50:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 0a4f8a38-786b-3610-a463-f465195ac83d | -11.9207 | -44.9525 | 2025-08-05 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 183.5 |
| 68d0820d-ec43-3342-939b-1d0d045c3e7b | -8.9225 | -60.576 | 2025-08-05 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 937a6a47-b039-397b-b058-a036641ee994 | -17.225 | -44.841 | 2025-08-05 02:50:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 100.5 |
| ac65e714-cd62-31a2-bc2a-6945d58cb0c6 | -8.9228 | -60.5376 | 2025-08-05 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| b938f5a3-2428-346d-abd8-45d89a03c09d | -8.9227 | -60.5568 | 2025-08-05 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 185.6 |
| 274865bf-f4c2-3cba-9753-01774caf4fef | -8.9478 | -46.7354 | 2025-08-05 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 8b51d749-b6da-39e8-aec1-48734e66205e | -13.0538 | -56.8746 | 2025-08-05 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 1179ea24-4151-35fe-bab2-e95bfbc8d967 | -5.13698 | -36.36856 | 2025-08-05 02:56:00 | NOAA-20 | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 11.9 |
| ddd1bd44-fa7f-3676-9c3d-b263b102b592 | -5.13613 | -36.36519 | 2025-08-05 02:56:00 | NOAA-20 | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 8.3 |
| f9e3ae3f-e6e4-37dd-a3d5-7b107f3f42d0 | -11.9207 | -44.9525 | 2025-08-05 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 02663494-1402-3b28-b49a-94f58cc3dd4f | -13.0916 | -56.8913 | 2025-08-05 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| f7b91080-d3cd-3675-94ce-22c5054a3e3b | -17.2256 | -44.817 | 2025-08-05 03:00:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 0fc778d6-44b9-3a17-bea9-35a40c4b9a24 | -8.9228 | -60.5376 | 2025-08-05 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 58740767-a477-36cb-8132-da22ae627ebf | -8.9227 | -60.5568 | 2025-08-05 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 115.0 |
| bef9d0df-9344-327e-907e-2903d7c5a953 | -17.225 | -44.841 | 2025-08-05 03:00:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 4443cc52-15f2-3252-8c4e-1917238e766e | -13.0726 | -56.893 | 2025-08-05 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 2598c70b-3c93-3194-ac98-939bfc1db703 | -8.9224 | -60.5953 | 2025-08-05 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 9f2d84cf-6ab0-3989-92f6-88e31065b1c1 | -8.9225 | -60.576 | 2025-08-05 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 2ac26666-5525-3ea1-8cc6-e53baa0835ef | -13.0723 | -56.9131 | 2025-08-05 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 29c67b40-010a-36a9-887d-f759080aa62f | -8.9478 | -46.7354 | 2025-08-05 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 124ec455-1ccc-3657-8bdb-607275ad5304 | -17.205 | -44.8454 | 2025-08-05 03:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 043c5068-5320-39da-919c-71a1ba6c6f0a | -17.2056 | -44.8214 | 2025-08-05 03:00:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 7d7ef837-a31f-3d2c-84dc-1e90bcc83a34 | -13.0914 | -56.9114 | 2025-08-05 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| bc09b813-d9d1-364b-b065-1b3a70e4f0ed | -11.9203 | -44.9757 | 2025-08-05 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| da5be8cc-1433-3d9d-b0be-df77c03de6d3 | -7.994 | -43.1534 | 2025-08-05 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.3 |
| 9f313cd7-fd72-3cad-90f5-badc2fa87d61 | -13.0538 | -56.8746 | 2025-08-05 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 8bb96679-64c8-377a-837f-d331ad71c627 | -13.0914 | -56.9114 | 2025-08-05 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 82d8316b-4d68-3714-947e-769581ec0acc | -8.9227 | -60.5568 | 2025-08-05 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 154.5 |
| cf1d695a-0b0f-36de-9d76-5d64865fa7ee | -13.0728 | -56.8729 | 2025-08-05 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 10d2622f-1cf5-35df-8cf7-6723c040f7a4 | -8.9225 | -60.576 | 2025-08-05 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 3fe87389-0880-3b38-97cf-f8a520961925 | -8.9228 | -60.5376 | 2025-08-05 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| a325044c-6fd4-31ad-b7bc-6750c55d1384 | -13.0538 | -56.8746 | 2025-08-05 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| f37fd331-ade6-31e8-bb12-425d1699a174 | -8.9412 | -60.5559 | 2025-08-05 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| e20e598b-5270-3b75-bb81-659f9339d6c2 | -3.1833 | -49.4429 | 2025-08-05 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 209c5981-5959-3929-a1c0-08a733d976f0 | -13.0723 | -56.9131 | 2025-08-05 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 92ca6bf4-485f-364b-9807-dba3568d542c | -7.994 | -43.1534 | 2025-08-05 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.9 |
| 44855689-033f-3ad2-b222-82c2556f0cd2 | -8.9224 | -60.5953 | 2025-08-05 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 40b96a8e-9e9d-396f-abe5-99b013479c5b | -8.9478 | -46.7354 | 2025-08-05 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 2fc35b91-6579-357b-9556-943e9aca2017 | -13.0726 | -56.893 | 2025-08-05 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 90d0f911-0709-343d-9f51-fb8afa0a5856 | -13.0916 | -56.8913 | 2025-08-05 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 245940ff-c996-3845-b85a-766e7c535c29 | -11.9207 | -44.9525 | 2025-08-05 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 90f025b5-d226-39aa-a635-9cb89a64cfa1 | -17.2256 | -44.817 | 2025-08-05 03:20:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 276efaa8-b452-317d-b05f-c1e4192cf9d0 | -13.0914 | -56.9114 | 2025-08-05 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 164af5ad-ab3f-3576-8063-826c50ffff8f | -14.466 | -52.0899 | 2025-08-05 03:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 7d8ea514-9dce-35f1-8a79-d9f7e9773518 | -14.4853 | -52.0873 | 2025-08-05 03:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 182.6 |
| 04f024ea-895e-3a96-afee-f54328a2dd60 | -8.9227 | -60.5568 | 2025-08-05 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| b3dce60d-0bc1-3d7e-b63c-df0727661b08 | -11.9207 | -44.9525 | 2025-08-05 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| b70a87b5-8b7a-3407-bcfd-c09ffa588b90 | -17.205 | -44.8454 | 2025-08-05 03:20:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 66.4 |
| aed351f2-3cb1-3be2-bf86-03d1ed1331a5 | -17.225 | -44.841 | 2025-08-05 03:20:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 91.7 |
| c082e42d-2765-38db-9b03-68ce508dcece | -14.5046 | -52.0847 | 2025-08-05 03:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 4a888a03-70d6-34bb-acea-368aa6d4cc34 | -8.9478 | -46.7354 | 2025-08-05 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d5bd6bd3-9a4a-37f4-985f-7fde11af366a | -8.9225 | -60.576 | 2025-08-05 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 66d134f4-057a-34e3-84f1-76b7f77cc0ac | -7.994 | -43.1534 | 2025-08-05 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.8 |
| 02c4d5bc-7408-3818-9fd6-47ef3ef12c13 | -17.2056 | -44.8214 | 2025-08-05 03:20:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 061a53c5-4ba2-3539-abd6-898c2543da26 | -13.0538 | -56.8746 | 2025-08-05 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 6b32f97e-4ede-307e-add1-c2ae1f651ac4 | -14.4857 | -52.066 | 2025-08-05 03:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| f10ef8ae-fed4-3790-b001-570f05862669 | -13.0723 | -56.9131 | 2025-08-05 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 9810d52c-4631-3cb0-a1b4-ca9279b047c4 | -8.9224 | -60.5953 | 2025-08-05 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 43fa60dd-ac70-37d9-b64b-73d47fb8f2eb | -14.4849 | -52.1086 | 2025-08-05 03:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| b78bb8fc-b731-329d-9a48-d848ce5a511e | -13.0726 | -56.893 | 2025-08-05 03:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| b94c97a7-cd77-3f61-a083-2dd8d22be343 | -17.205 | -44.8454 | 2025-08-05 03:30:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 91.9 |
| d20d9c46-b4c1-361b-a400-f9f24cf25eda | -8.9225 | -60.576 | 2025-08-05 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 89cd7e07-93c3-328d-a123-7e49162c8095 | -17.2056 | -44.8214 | 2025-08-05 03:30:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 7bce0b83-a467-36ce-9829-e1a5034d4f58 | -13.0723 | -56.9131 | 2025-08-05 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| f685fe2b-d3bb-35a9-9ea2-585a07fe2cfc | -14.4853 | -52.0873 | 2025-08-05 03:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 201.4 |
| 2fe456e2-41ce-382a-972d-0dff6b63f557 | -14.4656 | -52.1112 | 2025-08-05 03:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| c9741213-2a33-3122-a992-96158a044871 | -8.9227 | -60.5568 | 2025-08-05 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 0e074aaa-1199-3b05-b124-06df11132e92 | -13.0538 | -56.8746 | 2025-08-05 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 7f86e38b-2cc6-3a51-b737-381b8a936d7d | -13.0914 | -56.9114 | 2025-08-05 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 6e57cac0-206d-3229-9b7b-c55dec1c347a | -8.9224 | -60.5953 | 2025-08-05 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 9be05a85-73cd-3eb5-8b21-7f44467a8fab | -14.466 | -52.0899 | 2025-08-05 03:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 147.5 |
| b911c25e-964c-3a3e-95a8-6386c6a3ac2d | -11.9207 | -44.9525 | 2025-08-05 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| dd397d19-5cf8-3f28-99df-b493e7be254b | -14.4849 | -52.1086 | 2025-08-05 03:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 1d95736f-12f4-3410-bd34-a2dcddb29252 | -7.994 | -43.1534 | 2025-08-05 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.0 |
| e1b5fa8c-8f5e-38d9-b1d1-3452288aabdd | -17.225 | -44.841 | 2025-08-05 03:30:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 9f819c69-846d-3770-8433-36f10140aa87 | -14.4857 | -52.066 | 2025-08-05 03:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 39d87321-11ab-30e6-8cb0-a0c98209fbc3 | -8.9478 | -46.7354 | 2025-08-05 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| af1e3806-4441-3258-92d3-e3acb8851c75 | -13.0726 | -56.893 | 2025-08-05 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 393b8d41-0e34-3f71-8ac0-08e1145830af | -17.2256 | -44.817 | 2025-08-05 03:30:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 9faf8811-cc82-3d5f-b7aa-0e216f3bc480 | -17.225 | -44.841 | 2025-08-05 03:40:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 69.9 |
| fbc7c002-e2af-3a97-ad47-4b30ad14268d | -8.9227 | -60.5568 | 2025-08-05 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| e011a2d2-7b70-3695-8c70-63c06927d16d | -17.205 | -44.8454 | 2025-08-05 03:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 48c08901-c3ce-34c0-a806-128d7a1c7098 | -7.994 | -43.1534 | 2025-08-05 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.5 |
| 7745c0a9-f391-3276-bbab-148cf9a1a825 | -13.0914 | -56.9114 | 2025-08-05 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 89059941-7f8c-35d9-9d6e-0a0983aaa90f | -11.9207 | -44.9525 | 2025-08-05 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 000ec9ba-003f-3ff8-89e5-10d747ad1aa8 | -13.0538 | -56.8746 | 2025-08-05 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| ab703d42-3873-3933-ae37-7a871a9c6439 | -13.0723 | -56.9131 | 2025-08-05 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 094f4dad-74fd-36e4-ae85-3e8f8ab77c45 | -14.4853 | -52.0873 | 2025-08-05 03:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |


[Clique aqui para ver as próximas entradas](README7.md)
