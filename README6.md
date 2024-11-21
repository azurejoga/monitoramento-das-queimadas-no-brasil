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
| 4da21504-c088-3a38-ab54-096eea4deb09 | -3.2951 | -53.8395 | 2024-11-21 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 0781336e-f300-37f5-9085-80e960922eda | -2.7491 | -52.1255 | 2024-11-21 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 168761d6-afaf-31c5-bdbc-78b9d6b5a1d9 | -3.2954 | -49.1841 | 2024-11-21 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 2a334c83-00c1-3665-b143-2c3fdc789611 | -3.3923 | -52.4767 | 2024-11-21 00:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 94b44ca7-ce9d-323a-a360-871df08f9ffc | -17.6106 | -50.1959 | 2024-11-21 00:30:00 | GOES-16 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 592dae10-3b14-3d55-b733-66f86e7265ae | -4.58 | -48.0132 | 2024-11-21 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 199.7 |
| f938d4a1-fc30-3258-b9c2-f064b1fa24aa | -4.5984 | -48.034 | 2024-11-21 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 84ee0c2d-8cc9-3016-8586-fac58e222eb0 | -9.9172 | -35.965 | 2024-11-21 00:40:00 | GOES-16 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 77.8 |
| 55bdaec8-9129-3c54-a4ac-5d503ae7769e | -6.214 | -46.2202 | 2024-11-21 00:40:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| bcf1c19d-649a-33a8-b5a3-7638733c2a41 | -4.5799 | -48.0349 | 2024-11-21 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 70d0e303-9173-3de9-aac7-a7affee816db | -4.16 | -43.8818 | 2024-11-21 00:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| d401dc69-3d1a-3bd1-9c43-76fc5ecb9dd3 | -10.1223 | -65.0237 | 2024-11-21 00:40:00 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 1ac31a73-214b-3563-bb56-bbbf324854c1 | -3.2951 | -53.8395 | 2024-11-21 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 016ea997-1e27-3b30-899b-c7f74e62c47e | -3.3739 | -52.4773 | 2024-11-21 00:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 1cb3758d-0cd0-3a8a-9c9c-0c49c573f3ec | -5.0998 | -43.151 | 2024-11-21 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| dd7b6a80-4229-39ad-a78e-b0424b0fa89c | -2.7491 | -52.105 | 2024-11-21 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 0ad022d6-389b-332f-b7ab-137f04c2993e | -3.3924 | -52.4563 | 2024-11-21 00:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 161.9 |
| a16b7ada-e58b-336a-a4a7-3c71fba08c54 | -4.1413 | -43.8828 | 2024-11-21 00:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 145.6 |
| e044d9e1-c074-3a92-a6a5-28d0e5ae1a9b | -9.8984 | -35.9412 | 2024-11-21 00:40:00 | GOES-16 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 61.0 |
| 195c7ccf-814c-37c7-9fda-62d95379b257 | -3.374 | -52.4364 | 2024-11-21 00:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 4fe157d6-288a-3bcd-9bc6-2344d25ba2e6 | -3.2767 | -53.84 | 2024-11-21 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 95227dfe-77b0-3e4e-b047-6dc785afe5ca | -3.5831 | -43.634 | 2024-11-21 00:40:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 5cd903c7-cb97-3d0e-a2e9-e58313149dcd | -5.0996 | -43.1744 | 2024-11-21 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 205.8 |
| 3f1e777f-6607-33e7-9da9-66bbe17c7f8b | -6.1182 | -42.5086 | 2024-11-21 00:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 52.2 |
| ad47f957-9851-3129-9a07-69b0f018c0c7 | -1.7372 | -52.0639 | 2024-11-21 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 7aabf9b0-9d38-310c-b9a7-2ef3b13f5f60 | -2.0259 | -54.5289 | 2024-11-21 00:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 34269b49-ac4f-3414-aef5-8fe577a12313 | -4.58 | -48.0132 | 2024-11-21 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 257.5 |
| bbb9f482-61a2-381e-bf2b-cedb22233daf | -3.2768 | -53.8199 | 2024-11-21 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 97919494-8d56-3edc-ad6f-400d85804d76 | -3.0354 | -49.4688 | 2024-11-21 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 102e3a36-971c-3c39-9dbc-4d4cd8343a07 | -4.2388 | -46.1197 | 2024-11-21 00:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 3e133468-4397-31c4-a83f-132dc12b8e2d | -1.7556 | -52.0636 | 2024-11-21 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 520c5493-132d-3e51-aa51-c3f35d34fc4b | -4.0635 | -50.9049 | 2024-11-21 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| d70cda29-38bd-3a51-b734-f35fe45931f1 | -2.7676 | -52.1045 | 2024-11-21 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 138.5 |
| a33bbb92-e92b-37e7-b884-29437fef0ad2 | -3.374 | -52.4568 | 2024-11-21 00:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 242.1 |
| 9136079c-c60a-3502-b9c3-a8f354090254 | -3.3923 | -52.4767 | 2024-11-21 00:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 047fd5c1-e1b2-3758-aa37-a6b600b92569 | -2.0075 | -54.5292 | 2024-11-21 00:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 8d12e497-2c3a-3c80-9e43-c9382884ba32 | -5.1183 | -43.1731 | 2024-11-21 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 9b7b50f7-b514-3625-8d29-f5c813432680 | -2.7675 | -52.1251 | 2024-11-21 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 731d3fcb-408c-3c60-98bf-570cf13017b8 | -3.2014 | -54.3243 | 2024-11-21 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 3d5d47b8-6781-3343-9e81-66227ef8484f | -4.6446 | -49.5544 | 2024-11-21 00:40:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| a7ffc49f-de0f-38d2-b164-ebeea5aabe82 | -2.7675 | -52.1251 | 2024-11-21 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 627afe54-e8cd-358e-9121-55efbc81b64d | -5.1183 | -43.1731 | 2024-11-21 00:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 184.2 |
| cd633be5-f652-33ed-8d85-0d6c4a7c52f9 | -3.2768 | -53.8199 | 2024-11-21 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| fd564bad-2c70-30fc-b2e7-dec7492d6668 | -3.3923 | -52.4767 | 2024-11-21 00:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 6991b797-020c-341e-8a75-b443d58acc92 | -3.8167 | -52.3403 | 2024-11-21 00:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| ad7c29a4-6d06-39bb-9b03-a09f2da89ed9 | -3.3739 | -52.4773 | 2024-11-21 00:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| c4ebaa74-958b-390b-bb85-f546c5ead830 | -10.1223 | -65.0237 | 2024-11-21 00:50:00 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| d6c04eb8-11c0-384d-a124-2a9a8415ce94 | -3.2767 | -53.84 | 2024-11-21 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 77d0a4e2-9a77-3768-861b-e7402db0b3bd | -4.16 | -43.8818 | 2024-11-21 00:50:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 374d6a1c-12d6-352e-b821-3f0cd3a2f5a5 | -2.7491 | -52.105 | 2024-11-21 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 8fec6ca1-1c8d-3115-8078-f6759990ee77 | -4.58 | -48.0132 | 2024-11-21 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 193.2 |
| 96be6d99-655d-34b8-9cf1-735a1ebd87bd | -4.1413 | -43.8828 | 2024-11-21 00:50:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| f2eb1483-8e0d-3458-98ea-9c9482863c29 | -2.0075 | -54.5292 | 2024-11-21 00:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| dc8ec2a5-6a13-3170-9583-821825c2f458 | -3.1831 | -54.3247 | 2024-11-21 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| fbe21db9-6f0c-3383-a190-01be56d1947e | -6.8258 | -46.7737 | 2024-11-21 00:50:00 | GOES-16 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| b25fa381-b364-31c8-af56-9c71408e560c | -3.6018 | -43.6331 | 2024-11-21 00:50:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 712bd91e-6e62-3bd1-93b7-8ed7d2d1c4aa | -4.6446 | -49.5544 | 2024-11-21 00:50:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 966009ce-1144-385d-b2f4-56614cbfa809 | -2.7676 | -52.1045 | 2024-11-21 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 6a146692-7acf-30d1-98d4-3fbc907427da | -3.374 | -52.4364 | 2024-11-21 00:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 1412babb-ec7d-3b34-9c2b-06cff420ced8 | -4.2575 | -46.1188 | 2024-11-21 00:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 889009aa-1a0e-313c-940c-99ff63e12711 | -4.5614 | -48.0141 | 2024-11-21 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| a12cba8a-f80c-3d62-9fa1-773a02afd53a | -4.5986 | -48.0123 | 2024-11-21 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| dc305594-7c63-3bce-87aa-403afa8a35e3 | -1.7556 | -52.0636 | 2024-11-21 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| aca206e6-7285-350f-8b36-bd1e367bdf35 | -3.3924 | -52.4563 | 2024-11-21 00:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 241.0 |
| ad6f95ff-2014-3477-ab20-760a970b5899 | -4.082 | -50.9042 | 2024-11-21 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 9061b8ba-8edc-38c7-be1c-329625e159d4 | -3.2014 | -54.3243 | 2024-11-21 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| c9ee18a1-9628-366b-b7d2-72965941f6d7 | -2.7491 | -52.1255 | 2024-11-21 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 56d1235a-f35c-3d54-a54c-94c8051bf441 | -3.374 | -52.4568 | 2024-11-21 00:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 215.8 |
| 5c0a6926-9257-319f-b1b3-c1775d6b4871 | -5.0996 | -43.1744 | 2024-11-21 00:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 196.9 |
| 33795325-b96c-3021-8571-7621d8d5725c | -2.0259 | -54.5289 | 2024-11-21 00:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| e1cbdea0-09be-372b-85ce-474c65ee0c8c | -3.2951 | -53.8395 | 2024-11-21 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 7480a0c9-f3f5-3dab-a707-a8a83f387851 | -4.5799 | -48.0349 | 2024-11-21 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 50772d87-0179-39ba-ba0f-6da5a6fe9106 | -5.0998 | -43.151 | 2024-11-21 00:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| a5a18411-44f5-3833-baf6-18a430d7a909 | -5.1185 | -43.1497 | 2024-11-21 00:50:00 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 8323bc34-406d-31fc-8748-30cf4e34d281 | -10.1223 | -65.0237 | 2024-11-21 01:00:00 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 68.0 |
| f15d8070-1fc0-3e7b-8a5b-5bc6a5a3a1df | -2.7491 | -52.1255 | 2024-11-21 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 870f0344-0512-3c06-a667-e1e1a57b1038 | -2.7491 | -52.105 | 2024-11-21 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 2a8e8947-1737-3b93-b997-ede169e34ee9 | -5.1183 | -43.1731 | 2024-11-21 01:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 302.7 |
| e6c8c200-3dbd-36e3-af6e-4bd691ed0355 | -4.1413 | -43.8828 | 2024-11-21 01:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| d6a2bf2f-9d03-319f-b6cd-2ddc84a37bfa | -5.0996 | -43.1744 | 2024-11-21 01:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 267.7 |
| aade1561-4ce5-339a-a09c-a5f302041c43 | -3.374 | -52.4568 | 2024-11-21 01:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 262.4 |
| 85c534fe-4bbd-3e1d-963f-bfbe3a075bf7 | -5.1185 | -43.1497 | 2024-11-21 01:00:00 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 137.1 |
| af1c073d-7cef-34ec-b08f-8fe9eef79a58 | -4.2575 | -46.1188 | 2024-11-21 01:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| d2eeef9c-9dde-3744-8305-004a94041482 | -4.16 | -43.8818 | 2024-11-21 01:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 6c762445-c8c2-3e6e-9b06-fdac52871c16 | -4.5986 | -48.0123 | 2024-11-21 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 0561d3e3-531a-3049-87f8-fb3e0143cdf7 | -2.0259 | -54.5289 | 2024-11-21 01:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| de4662ab-1f4d-36fb-8973-2fdba5194fd9 | -6.8258 | -46.7737 | 2024-11-21 01:00:00 | GOES-16 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| bc21f427-8f40-311b-91dc-5e3a96be04ca | -3.2951 | -53.8395 | 2024-11-21 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 85cc35ae-df54-31e1-ac76-838d5f31b4ee | -4.58 | -48.0132 | 2024-11-21 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 185.5 |
| 4e3b902f-d694-3024-9bfa-61fac767edeb | -3.2767 | -53.84 | 2024-11-21 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| d198a495-d89b-3046-a9c9-20242e96369d | -3.8167 | -52.3403 | 2024-11-21 01:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| e9ecae38-0b1b-347a-b7fd-e8b3c1aa4254 | -2.7675 | -52.1251 | 2024-11-21 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 3b8dc753-7a53-3f44-8bd2-02a8b5e1cde2 | -3.2952 | -53.8194 | 2024-11-21 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| a39e7c51-c33c-346c-ab19-3e1d1829ac33 | -4.5799 | -48.0349 | 2024-11-21 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 120.4 |
| b92376b4-6cbf-3ab5-92e8-8d20e36ac354 | -4.5614 | -48.0141 | 2024-11-21 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 1f84fb69-bea8-30d3-bff7-cfd09b3db115 | -3.2014 | -54.3243 | 2024-11-21 01:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 6a2435a6-7184-3315-9f30-5034d1ae41cb | -5.0998 | -43.151 | 2024-11-21 01:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 33646558-eb68-3fff-8b39-71240e116e4a | -3.6018 | -43.6331 | 2024-11-21 01:00:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 2dc1f79a-3ed1-32a6-ac55-0f13759af512 | -3.374 | -52.4364 | 2024-11-21 01:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 9369d84f-442e-3212-aec5-598e645cf4ce | -2.0075 | -54.5292 | 2024-11-21 01:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |


[Clique aqui para ver as próximas entradas](README7.md)
