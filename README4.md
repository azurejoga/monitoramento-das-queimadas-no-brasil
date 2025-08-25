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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0abb3df9-ccb0-3ca6-8f72-4ea1dcde2754 | -3.4254 | -49.0517 | 2025-08-25 00:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| e74ec0d6-8e26-3d10-b009-1a5ab42d62b1 | -8.9689 | -65.4198 | 2025-08-25 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 5c6e036e-cf11-3c0a-8372-f1f3b93c486b | -6.8201 | -59.4386 | 2025-08-25 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| e20c8c4f-c6b8-3182-bc52-ce5cdc5c8196 | -8.8733 | -62.4685 | 2025-08-25 00:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 5eb16735-54b7-3cd4-8765-fbefa3e43ffb | -5.1181 | -43.1964 | 2025-08-25 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 219.7 |
| 8cdd1116-76b3-30c6-b858-9d398b885afd | -8.2128 | -61.393 | 2025-08-25 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 4249f6ea-f9c7-38ad-80bb-69a695c39fd3 | -8.9874 | -65.4192 | 2025-08-25 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 192.2 |
| db5aefe2-629a-3444-bef1-951191778627 | -5.0994 | -43.1977 | 2025-08-25 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 145.7 |
| c1b55c33-595c-327a-bb3f-1a8207f2e0c2 | -9.0416 | -65.7163 | 2025-08-25 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 45d62e99-88a8-312a-bc6c-29e21cf94b59 | -9.006 | -65.4 | 2025-08-25 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 213da2ad-83cb-357e-b237-811149817fd0 | -8.969 | -65.4012 | 2025-08-25 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| aabeba30-458b-3477-bac0-b62990063025 | -8.1119 | -62.877 | 2025-08-25 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 80243886-7066-39a4-a5c3-87c935e5be1c | -3.4439 | -49.051 | 2025-08-25 00:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 2abe1688-a654-33ca-8507-7aee749664be | -9.1988 | -60.9274 | 2025-08-25 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| aaecf54e-c58a-3a12-ae11-ffd89bc0a0a8 | -7.6326 | -62.7243 | 2025-08-25 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 052efe39-2e97-3855-8d47-b9d402792e8c | -9.2174 | -60.9265 | 2025-08-25 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 8db48783-ce9e-352b-abe4-2499756bdef0 | -10.6128 | -44.3284 | 2025-08-25 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 9489c955-bab7-3a99-87a3-35eb23e76a44 | -9.0415 | -65.7349 | 2025-08-25 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 490465cf-df59-36ca-810e-088fa847e076 | -9.1909 | -59.4619 | 2025-08-25 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| ff12afa0-5896-3a67-98ec-2aa49a8cef8d | -10.5937 | -44.331 | 2025-08-25 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 5573ae3e-aa25-35b9-8117-0133ee896b4a | -8.8919 | -62.4487 | 2025-08-25 00:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 7457f624-1395-39a0-80dd-e5285d9834b5 | -9.1906 | -59.5007 | 2025-08-25 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 2e2b80e5-0c0f-3b1e-999f-dc561eebcc91 | -9.1907 | -59.4813 | 2025-08-25 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 2de72772-0d3e-35ff-abba-4e35d19758a9 | -8.8734 | -62.4495 | 2025-08-25 00:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 596be8bd-9afd-3fc9-888f-6e7781d3c1e3 | -9.2092 | -59.4997 | 2025-08-25 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 48aa220c-6dd5-3653-9b03-a46ffb25b8e6 | -18.0799 | -51.3908 | 2025-08-25 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 1e4e1e93-58c0-30b8-afff-61b5bd1f86f5 | -8.9875 | -65.4006 | 2025-08-25 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 9d34cbbd-95ab-3de5-828a-77ed64b97c86 | -7.6141 | -62.7249 | 2025-08-25 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 704a2dfc-e109-31b4-a565-928fec280766 | -5.118 | -43.2198 | 2025-08-25 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 194.0 |
| 9b376ef8-cc49-38e6-84b9-bab1e490d858 | -5.0992 | -43.2211 | 2025-08-25 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 34fb8b3d-de75-3043-b2ce-14786d7bb677 | -9.1722 | -59.4629 | 2025-08-25 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 6609596f-6525-3b27-8c43-42f4c0079608 | -6.7636 | -59.6526 | 2025-08-25 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 59b54718-1ac5-31e2-af81-e6a0becba9a2 | -3.4439 | -49.051 | 2025-08-25 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 30eb90b1-8df0-33cb-92a2-9c03e487631b | -5.0992 | -43.2211 | 2025-08-25 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 134.8 |
| b8d41138-651f-3f1e-b168-b8623b27e605 | -6.7819 | -59.6711 | 2025-08-25 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 7e4e42c9-df6a-3329-a6ea-58fa00a6384a | -8.5943 | -62.6315 | 2025-08-25 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 93afa511-db39-3c0a-a973-6c676deae3cc | -9.8101 | -64.2642 | 2025-08-25 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 456b8604-3b38-3f56-9260-481518b11e34 | -8.2313 | -61.3922 | 2025-08-25 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 0af4fb0f-9e03-3ae6-ac31-58edc2f06387 | -9.8102 | -64.2454 | 2025-08-25 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 3d8b0bf5-1770-34e9-8405-1540ff8900bc | -5.118 | -43.2198 | 2025-08-25 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 129.3 |
| a8baf5a9-02c9-32a2-87a0-c4c0703b2884 | -7.6326 | -62.7243 | 2025-08-25 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 31b7b069-c634-3820-97ae-ebaacbbdd027 | -9.0972 | -65.7145 | 2025-08-25 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 8ffbf6b0-b817-3896-a1c2-209adac448a5 | -10.0232 | -51.0712 | 2025-08-25 00:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| ede8d044-4a7f-333e-bcdd-b1e66e8af08a | -18.0799 | -51.3908 | 2025-08-25 00:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 5fd2c60e-d0a2-31ac-9353-5b1066567e5d | -3.4254 | -49.0517 | 2025-08-25 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| b15bd102-e397-35d7-bc46-cc09b894d1fc | -8.8919 | -62.4487 | 2025-08-25 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 78.8 |
| d6c38a51-37c3-3d3a-b661-8ed1fbbdd85f | -8.1119 | -62.877 | 2025-08-25 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.4 |
| e3c927d0-9e23-3dd4-92c0-49c406973333 | -9.06 | -65.7344 | 2025-08-25 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| fe7a415d-addd-32e6-b223-d4808c07e1ef | -9.0415 | -65.7349 | 2025-08-25 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| b6450323-1b15-3e56-b805-504f8f7ee2ca | -5.0994 | -43.1977 | 2025-08-25 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 7f512273-5f4b-3092-adce-3433a4829e60 | -8.8733 | -62.4685 | 2025-08-25 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 100.4 |
| cb455dc1-5e68-3d19-a440-dc835389b739 | -10.2572 | -59.1081 | 2025-08-25 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 161c1e02-cf71-3409-b74b-e82eb2de5425 | -9.1988 | -60.9274 | 2025-08-25 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 16793a1f-c1fd-3988-aab6-08e5949a37f8 | -14.2157 | -58.6316 | 2025-08-25 00:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 5654b669-02fb-3ef0-8f3b-d7eca67653f4 | -6.7635 | -59.6718 | 2025-08-25 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 302bc667-c632-345c-ae09-4b970e387d5a | -9.0971 | -65.7332 | 2025-08-25 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| a9e86748-6025-3341-bd69-079f3047929b | -11.6093 | -46.3472 | 2025-08-25 00:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| d834dab6-5d7d-3707-aec3-f1bb3cfc07c4 | -5.1181 | -43.1964 | 2025-08-25 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 9d17d517-c5d2-31fe-b8ad-3e5759392013 | -6.7821 | -59.6326 | 2025-08-25 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| a3ca09ba-9136-3f1b-8fc1-b7bf9e957dbe | -6.782 | -59.6519 | 2025-08-25 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 5380bbab-ecce-37dc-b00b-4bbbf9caf9ba | -8.8734 | -62.4495 | 2025-08-25 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 104.1 |
| d632407b-1224-35ba-a34e-b1cc33d85806 | -8.8918 | -62.4677 | 2025-08-25 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 863204d0-ac5e-3c07-bf1e-c2d2d5f59d15 | -10.5937 | -44.331 | 2025-08-25 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 3681a087-1935-3978-9ec7-b85ab72a4372 | -5.0992 | -43.2211 | 2025-08-25 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 141.8 |
| c6ea7543-9563-35a7-9ea7-85cd3fab8e0e | -9.1722 | -59.4629 | 2025-08-25 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| d27e0067-8a9e-3966-bde2-2498506f9a5e | -8.9689 | -65.4198 | 2025-08-25 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 112.5 |
| fb89f261-9dd0-38aa-96e0-7a2955545128 | -15.3257 | -49.6298 | 2025-08-25 00:50:00 | GOES-19 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 8c564f51-4529-3508-ada1-861c8f91d64c | -9.1907 | -59.4813 | 2025-08-25 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| d9de9f58-e6a0-3cca-8734-25241d19a465 | -9.0415 | -65.7349 | 2025-08-25 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| bf01dc6f-bb8f-3cb1-9a2d-4a668d2cca4f | -6.8413 | -58.9552 | 2025-08-25 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 94873ea4-3bd1-3562-9d65-3bb3cbb2122e | -8.969 | -65.4012 | 2025-08-25 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| b680299e-3a2a-31b6-bfbb-525530a773a5 | -7.6141 | -62.7249 | 2025-08-25 00:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 35833b58-c4f2-3c37-aec6-8741e34040df | -22.5518 | -46.8053 | 2025-08-25 00:50:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.9 |
| ff7656fb-c396-3603-a07f-c49107f9ef58 | -6.2645 | -59.9784 | 2025-08-25 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| f2c27909-41c7-329c-aa58-9580fb53a46c | -6.7819 | -59.6711 | 2025-08-25 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| e2869ad9-6fe5-383a-b7c1-8152e05d8d99 | -5.0994 | -43.1977 | 2025-08-25 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 35238248-e20d-300f-b26b-87e57e610c52 | -9.0416 | -65.7163 | 2025-08-25 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 01e22201-8804-3924-9ccb-bdc4c4975248 | -3.4439 | -49.051 | 2025-08-25 00:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 9ebd584f-98f1-3401-abcf-cecbe9761869 | -8.9874 | -65.4192 | 2025-08-25 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 176.1 |
| af26ee06-1451-3235-b1c6-7d6e28e5535c | -8.5942 | -62.6505 | 2025-08-25 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 39068188-82a6-37bd-8b90-a11308be8a59 | -8.8733 | -62.4685 | 2025-08-25 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 4e5ace8e-d802-3622-b69d-bf12715df6e0 | -6.8229 | -58.956 | 2025-08-25 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 15b5547f-ca04-348f-b6d4-cc80b21229fb | -9.2092 | -59.4997 | 2025-08-25 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| a479c4ff-40ca-389c-af42-840e7c8d0fd8 | -5.118 | -43.2198 | 2025-08-25 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 212.7 |
| 948c6872-187a-374b-b51e-7903d26afdef | -7.6326 | -62.7243 | 2025-08-25 00:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| d2d28274-e4dd-3677-a88f-0587250ce5cc | -8.8919 | -62.4487 | 2025-08-25 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 026488c5-6a46-3d7e-ac72-d9c004e26f1f | -8.8734 | -62.4495 | 2025-08-25 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 106.8 |
| d0ea7681-6013-334e-9064-c831e0ebb6bf | -8.9875 | -65.4006 | 2025-08-25 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 114.1 |
| cdac674e-d67a-3b14-9f65-af38f3f2aa7f | -8.5943 | -62.6315 | 2025-08-25 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 192.5 |
| 9a05de2b-65ba-31d4-8be3-6a0990e0c26b | -8.5758 | -62.6323 | 2025-08-25 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 5e34ce29-a904-3481-a675-a454815cf117 | -9.1906 | -59.5007 | 2025-08-25 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| b9fe2c2d-3209-3408-ad70-e4bf22830128 | -9.0061 | -65.3813 | 2025-08-25 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 4c99690c-239e-3565-85df-d2be3bfb3f99 | -6.8228 | -58.9753 | 2025-08-25 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| de5fe181-9a37-33f2-9cb9-3ac1f3486502 | -9.8101 | -64.2642 | 2025-08-25 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 6db34792-8e18-3810-a59c-08d0790cc20f | -9.006 | -65.4 | 2025-08-25 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 314c4b6c-387f-34ce-b554-1924fa70007a | -6.2829 | -59.9777 | 2025-08-25 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| fe47015a-63d2-3eab-b5cc-6f0de5f10733 | -9.0787 | -65.7151 | 2025-08-25 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 2f725572-eeec-395d-b366-369ca40e22c7 | -6.2461 | -59.979 | 2025-08-25 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 6c46bc48-1e57-3f2e-aa5b-e6cb14ce2971 | -5.1181 | -43.1964 | 2025-08-25 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 186.3 |
| f1339314-8000-3c2c-99fa-b3561585e04d | -3.4254 | -49.0517 | 2025-08-25 00:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |


[Clique aqui para ver as próximas entradas](README5.md)
