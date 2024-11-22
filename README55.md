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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c70488f-4dc1-3ccb-9915-1cfb34123c5b | -3.10282 | -53.7454 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe8e614f-a507-38b8-a325-1409a408322e | -0.05035 | -51.23561 | 2024-11-22 05:29:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a4be8480-9329-32c2-b04f-34b4e3452c88 | -3.22494 | -54.24285 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e6c046d1-a016-3bf2-9229-780319c9d111 | -4.08135 | -54.05492 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0beeac19-cf55-32b2-8f00-a0308bb9cf3b | -2.05436 | -55.45518 | 2024-11-22 05:29:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e135885b-5f2c-365a-8713-70c53876ab11 | -2.7945 | -51.71758 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f5b8028a-d11f-31b4-8eaf-0299e9b0bd11 | -3.31275 | -52.85968 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cb608b8-ff54-344e-9db3-6b2712604ca6 | -3.18973 | -54.32697 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 60e0df22-be4b-31b1-b062-f1874b89f452 | 0.44318 | -50.77239 | 2024-11-22 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95b686ba-aec9-3314-aa4e-d0783138121e | -3.23257 | -54.23113 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 5c0731e3-3447-3e67-af0c-8591b7a9ac2b | -3.83796 | -52.25935 | 2024-11-22 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5fce650-6f2c-38e7-bf02-42183071a729 | -4.18681 | -53.58092 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5507b067-d05a-34b9-9811-79e8fabffec4 | -3.96975 | -54.14162 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1d09580-538c-3d11-9f64-f5e06ff33d85 | -2.80275 | -54.02143 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0778fe19-a80b-3f01-8367-6d5dd194315c | -3.51663 | -55.57654 | 2024-11-22 05:29:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bde19988-279c-3c10-9c85-51250464ed8a | -3.28634 | -53.82628 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4d1a9d06-f0f2-3284-ac56-cc740270128a | -3.51249 | -50.80682 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28519bef-c1ea-3c6a-bb61-3555b0b46e71 | -3.80314 | -51.98946 | 2024-11-22 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| edb2bc82-6056-303e-953c-d481ea79a06d | -3.22637 | -54.24041 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 878e5daa-de73-3da0-926e-c09f2ad55066 | -2.69925 | -51.86644 | 2024-11-22 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9f616d03-6f9e-3f38-8582-93dc58e7a6c8 | -3.4076 | -50.98248 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3479d6b-22d2-3997-833e-769278387dac | -3.21001 | -54.25307 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1363907f-b988-3532-ba6e-66a69e94715a | -3.2726 | -53.83292 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb4de67a-ef2c-3fe2-8802-1d4da2db043c | -3.8635 | -52.35395 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c87e80c2-ece2-37c1-949f-aed561a4caaf | -3.67968 | -52.37246 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 844be8cf-ada2-3db8-ad3f-2008b5c50378 | -3.13455 | -59.0187 | 2024-11-22 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbcf492f-60c7-3b5b-b473-03f083c99e04 | -3.58974 | -55.45146 | 2024-11-22 05:29:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0a18420-429a-3dca-87c7-b794992f9bfe | -2.787 | -51.41399 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 05fe57db-d51a-36bd-8481-7c589b18b113 | -3.10679 | -53.98711 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f4a683e-d146-3a67-aa71-b2de4d2cd678 | -2.80752 | -54.02217 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9702e6f2-c314-394e-9404-c1d79943e0a8 | 2.38012 | -50.76235 | 2024-11-22 05:29:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5c5c25e6-4ef9-3ff4-9c39-6cdca9cf7e40 | -3.64495 | -54.3189 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 22a73310-944e-34b3-ae57-7d1ccb572568 | -0.0509 | -51.23203 | 2024-11-22 05:29:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 700fd556-e732-39e0-8a8f-3e9750f03d18 | -3.32546 | -54.09772 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ab10c500-7cf2-38ad-9b30-5b612ee7bc16 | -4.11898 | -51.06173 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d2056cb0-7ea5-39d8-a701-b6cc14410cf2 | -3.31703 | -52.86136 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81bf5620-0f1a-36a3-9de9-4aa6176d2f55 | -3.29544 | -50.36627 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c07f98d7-0099-37ca-8f8d-bc875a5877c0 | -3.27016 | -53.83463 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 711eb7c8-4838-38d8-bde2-7e79fac71da6 | -3.09891 | -53.21431 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19b91ce3-457c-35b0-8142-c4fb27159666 | -4.12762 | -53.97889 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86355f65-c82d-3ccd-a39e-307400279086 | -3.03306 | -53.72654 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ca34f96-4858-351a-ae9b-420d06b0ba4a | -3.57647 | -54.51752 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 931f29ca-b282-36f0-baad-d2800eb388ad | -3.19701 | -54.33086 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7ab1c70d-447f-387d-9bb9-a575ba983110 | 0.43752 | -50.77332 | 2024-11-22 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f26a87b3-b583-38b7-91b0-d91e38367d86 | -3.35003 | -50.50984 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a616875-e9e2-3939-961c-6764e434024a | 1.36579 | -55.9777 | 2024-11-22 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6b0ed3a6-2692-3c87-8c79-e62818d2de28 | -2.85435 | -54.00388 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd41be7f-d6bc-35ef-924e-d8290c11859b | -2.8123 | -54.02291 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2fedc3b5-df67-326b-9d33-34ad9b11b4d0 | -3.25477 | -54.24515 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ab51d06d-8bda-3d82-93f1-61516628753c | -3.23183 | -54.23621 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| b2205a6d-c7c8-3cb0-80f4-ffd28fcfd2ea | -3.19984 | -54.32361 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9bb5967e-3487-30b2-aa40-be6c2c4fb3c1 | -4.11128 | -51.05054 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f357919-fc12-3ea8-985e-5d2c5045e444 | -4.13593 | -54.65779 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 737207a0-7942-3b92-9a17-23b6e408cb7d | 1.94095 | -60.85338 | 2024-11-22 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11a8c110-9ce6-3174-af1e-f6795a8d3bfe | -3.17898 | -54.32273 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bd834598-58ea-3b7d-8e99-8cbb73b2bb78 | -3.06728 | -53.28853 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18cd6049-f1c0-3706-bd21-2c43c86b99c1 | -3.10525 | -53.99741 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c7643418-efd5-37e5-9540-da4a4c13ead2 | -3.50657 | -53.81052 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 39cfb619-d7f5-31b7-bed0-32d4344a4d4d | -3.57562 | -54.68122 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a1a7d25e-7aca-3714-a460-760601e5c224 | -3.20667 | -54.24267 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 46121c4a-d779-3368-a1ed-d71956fb794d | -3.18837 | -54.3243 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 46a2eb10-dd64-3672-b81e-1f3d29ea4012 | -3.50388 | -54.71938 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40e111ff-3a57-3336-810a-3b1f66072695 | -3.68358 | -54.58574 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 536890dc-b7c9-3069-9787-99f82d604d8c | -3.09934 | -53.21139 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6be9859-44e4-3e5c-a3f8-d88cb8758b05 | -3.27746 | -53.83376 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 101b538d-0c2c-3f0a-a4eb-c151f1700bdc | -2.74769 | -54.1281 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2b9da977-e63f-314e-9054-8bc44cb0f459 | -2.78546 | -51.41178 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 045d2ae2-395a-37de-b457-0039324ed798 | -3.39727 | -54.27341 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 49038066-fe9e-34e8-ad97-da811492953c | -3.09848 | -53.21724 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07013eaa-5c3c-325d-bf4f-c347d6c531b7 | 0.42678 | -50.77904 | 2024-11-22 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62012c36-1d5d-331f-a44b-e0448b930287 | -3.07189 | -53.29228 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c39ec7e7-6569-3ab0-b6aa-b470d7dff444 | -4.11064 | -51.05487 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 325f2185-83b2-3e6e-9850-e764bc70fe7d | -3.31794 | -52.86068 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03f3b142-0a9b-3074-b5c7-613036fba639 | -3.30228 | -50.36238 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a55ecd9-fdf0-3fc2-93de-53d7086c2944 | -3.21396 | -54.25124 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 76cfdb2d-594f-331c-89f8-0c3fd3c3ec2e | -2.80747 | -54.02322 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a1d4d58c-8cc1-30ea-ab6e-36a2081941de | -3.20995 | -54.24577 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a0afb6d6-b5d4-3bdb-b7a1-ea5419a404b9 | -2.36984 | -53.83697 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ddec248-859c-3328-9a00-e788c2fbf7b0 | -2.45098 | -53.68237 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e0efde00-408d-38b7-935b-ffee6dcff8cb | -3.86249 | -52.36098 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9fc6e3ff-571a-3ec3-bc1d-820f366132c1 | -4.01052 | -49.92416 | 2024-11-22 05:29:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cecb68fd-e6bd-3681-b89f-a04281fac3ea | -3.22566 | -54.24531 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f0c32af4-1541-38a4-a0a2-0b1111724199 | -3.57871 | -54.50251 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1e6bd65-c690-371b-b07e-3269a279eb3a | -3.22343 | -54.2527 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 095702f6-264a-32f4-bea2-fd1b56403db3 | -3.27742 | -53.81881 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 474cde39-f1b2-3698-876f-93866fbc5b2b | -3.28232 | -53.83463 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6aa24691-660f-37e0-9d80-6f5a29c2a8a1 | -3.22494 | -54.25026 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8e709418-0a1b-3bf2-b59c-99cebd521f02 | -3.20921 | -54.25066 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6ed77c46-d3ff-3c37-93e1-c28e700b49ed | -3.28476 | -53.83717 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7a1c7b33-903a-3533-9361-e7ba4cbdc81e | -3.54085 | -50.53218 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4b27b7d-f926-34c1-b1ed-9458dec7e31f | 1.37319 | -55.9494 | 2024-11-22 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2163555-518d-364c-ac9f-49a086d18404 | -3.00401 | -51.55352 | 2024-11-22 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7403f405-88ed-3c38-9d7e-2329727a75f0 | -2.813 | -54.01879 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45fc545b-a694-3e05-a07c-a67aa174c5a0 | 1.37249 | -55.97 | 2024-11-22 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16ca0c3a-8706-3362-bdd0-7bdf8f469153 | -3.24604 | -54.23853 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 9ee22d25-97a5-365e-b416-57092dbcda52 | 1.37007 | -55.95503 | 2024-11-22 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c76f91f1-7918-3b2e-a119-c9cb30a1e33a | -3.51025 | -53.80066 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c16d10a3-6e59-3dfd-9993-d7d8d77e4d01 | 0.46353 | -51.33861 | 2024-11-22 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 850a62d2-0bab-3d7a-b67a-d1f0536b098c | -3.06266 | -53.28479 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d21367dd-7bff-35c0-bf50-a304b9db3a4c | -3.50452 | -53.80557 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |


[Clique aqui para ver as próximas entradas](README56.md)
