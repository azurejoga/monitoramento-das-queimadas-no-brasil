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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e41f059-068e-369f-8d40-f5d6b51a7662 | -2.5311 | -51.1816 | 2024-10-27 05:55:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| c9fca045-d1bf-3cc2-bc15-11f989ee9b3e | -2.5495 | -51.1812 | 2024-10-27 05:55:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 68f39f47-131e-3f50-9371-14bae044e07b | -2.9215 | -50.274 | 2024-10-27 05:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 91169542-6350-36ee-8233-f388d3d033c4 | -3.77 | -43.5786 | 2024-10-27 05:55:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 7b271cef-b18a-39e0-8771-1b274cd932d2 | -3.7887 | -43.5777 | 2024-10-27 05:55:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 1413dcb4-6723-3974-be99-744406282447 | 2.71741 | -61.4945 | 2024-10-27 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f03b992-59a6-3450-b9db-7415a7b7202f | 2.30593 | -61.33371 | 2024-10-27 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8775e74-0ab9-3e3d-9b75-025c8f677b9b | 2.30135 | -61.33743 | 2024-10-27 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8dee4e70-ed59-3501-b069-a209cd537a1a | 2.30077 | -61.33395 | 2024-10-27 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59b7f3d4-a7d1-3fb1-abdc-a4e8b954f665 | -3.15715 | -68.06648 | 2024-10-27 06:03:00 | NOAA-20 | AMATURÁ | AMAZONAS | Brasil | 1300060 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cfd61208-6423-3e21-8593-e5572a5ba35d | -3.13722 | -67.94007 | 2024-10-27 06:03:00 | NOAA-20 | SANTO ANTÔNIO DO IÇÁ | AMAZONAS | Brasil | 1303700 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70844a9c-3762-36f9-8990-7e132a64bd6b | -8.1223 | -71.36815 | 2024-10-27 06:05:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 96c8809b-1364-3ab0-acd3-d215cfb9f88a | -7.82524 | -72.78176 | 2024-10-27 06:05:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68e8b52d-990d-326a-98ff-242a427984ca | -7.82468 | -72.78527 | 2024-10-27 06:05:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4d65950b-6ed9-3273-ae39-747aad67aff7 | -7.82192 | -72.78123 | 2024-10-27 06:05:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e51293f8-3e20-367a-98d6-a9f65613d179 | -7.82136 | -72.78474 | 2024-10-27 06:05:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b450830b-6d30-3264-b216-24d3730ae25b | -0.9815 | -53.7192 | 2024-10-27 06:05:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| a4b21619-6ab0-316a-ba62-40baa48ac7c1 | -0.9815 | -53.699 | 2024-10-27 06:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 070d3841-02fe-30f2-b2cd-10baa87807bb | -0.9998 | -53.6989 | 2024-10-27 06:05:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| f7521fd6-4f40-3669-a668-e03d6c7d3bcb | -2.5311 | -51.1816 | 2024-10-27 06:05:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 0bd2831a-b61f-3403-8fad-828ffb809915 | -2.5495 | -51.1812 | 2024-10-27 06:05:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| f717239b-4594-32ad-8a1a-92d18a83f322 | -2.8329 | -49.2626 | 2024-10-27 06:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| a564d7db-0ebb-3baa-a96c-6039bbd69ac5 | -2.833 | -49.2413 | 2024-10-27 06:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 0bd067ef-3936-3326-96c2-173815cbb9b9 | -2.8514 | -49.262 | 2024-10-27 06:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| a7f475ef-6ff9-3acb-b13d-90e51cc0b2ce | -2.8515 | -49.2408 | 2024-10-27 06:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| fc452464-e89f-3aff-95c9-98a69d290136 | -2.9215 | -50.274 | 2024-10-27 06:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| bb96e429-ef51-32ed-8bf3-988b518dc36e | -10.4359 | -69.75595 | 2024-10-27 06:08:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f2aa6c3-0cfb-322a-bca2-5ed33acb683d | -0.9815 | -53.7192 | 2024-10-27 06:15:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 05facfd2-ef30-3f22-9682-e67cd025017a | -0.9815 | -53.699 | 2024-10-27 06:15:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 0ab383b3-45d1-3658-b887-1fdfcc2be533 | -0.9998 | -53.6989 | 2024-10-27 06:15:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 4a198cb3-ca43-3f8b-907f-c68bcd32f762 | -2.5311 | -51.1816 | 2024-10-27 06:15:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 0d9540df-fc4d-3843-8ebe-b9fb58d220e0 | 1.7775 | -50.468 | 2024-10-27 06:24:55 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 357e27ef-f919-3a0e-96e7-024b62168e44 | -0.9815 | -53.699 | 2024-10-27 06:25:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 84877e92-61d9-3922-832e-0a2a1c8493e4 | -0.9998 | -53.6989 | 2024-10-27 06:25:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| c6961369-2035-30f1-8100-2a234ed1475c | 1.7775 | -50.468 | 2024-10-27 06:34:55 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 93960b16-f2d2-3ac5-a297-3a3f94ed093c | -0.9815 | -53.7192 | 2024-10-27 06:35:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 1babc29d-f288-3339-b69d-542fb8968987 | -0.9815 | -53.699 | 2024-10-27 06:35:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 5251c1df-f8f2-31b1-a328-40361b62aec6 | -0.9998 | -53.6989 | 2024-10-27 06:35:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 965b8a46-a326-3d0c-a8ab-0e21e183cd58 | -0.9815 | -53.7192 | 2024-10-27 06:45:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 30bd7d66-6869-35c3-a474-4ae2053972e2 | -0.9815 | -53.699 | 2024-10-27 06:45:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 8f1997bd-e3a0-34be-a4bc-f09f05f76986 | -0.9998 | -53.6989 | 2024-10-27 06:45:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| d0a1386e-1f09-3361-a82f-8ca14892da38 | 1.7775 | -50.468 | 2024-10-27 07:44:55 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 6d080ac5-8c35-3998-8408-0c908bd7044a | 1.7775 | -50.468 | 2024-10-27 07:54:55 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 100afb6a-e7c9-3ba2-9e6d-ea5d2acb0708 | 1.7775 | -50.468 | 2024-10-27 08:04:55 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 35.0 |
| ef6ed7a3-2d9e-33d4-8636-2bd78bf25b26 | -12.8883 | -44.6143 | 2024-10-27 12:06:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 146.3 |
| da51831e-c7f5-362b-b2df-70723e19e07d | -12.869 | -44.6175 | 2024-10-27 12:06:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| c52a833b-19ef-3aa0-842b-c79e352652e1 | -12.8883 | -44.6143 | 2024-10-27 12:16:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| f32a5fd5-9866-3f5d-8e49-997c159cd9db | -12.8883 | -44.6143 | 2024-10-27 12:26:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 4d8ccfe9-d5d1-33f7-8eb3-9220f96e9750 | -13.7529 | -43.0642 | 2024-10-27 12:26:22 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 136.0 |
| b0bd76e4-3ed5-3251-8ecf-f56b1d7b62ca | -5.69105 | -41.64685 | 2024-10-27 12:32:00 | TERRA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 2d3cff75-1b8d-3c34-bca6-7256b18d0b1a | -5.32201 | -43.07598 | 2024-10-27 12:32:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 483d9847-5e65-3a31-8f24-6837e24fd273 | -5.27965 | -42.72984 | 2024-10-27 12:32:00 | TERRA_M-T | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 2538d1b7-577d-30f6-b9ce-599fdddd6c3d | -4.93417 | -43.72211 | 2024-10-27 12:32:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 17e79d0f-a3c6-36f0-bd02-7d61c2f5edfe | -4.78997 | -43.70514 | 2024-10-27 12:32:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 53e980e7-4613-3c5a-921c-bcf99d115663 | -4.70928 | -43.87731 | 2024-10-27 12:32:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d32fdbcb-14c2-3b35-a9be-b92c67adcea6 | -4.708 | -43.88616 | 2024-10-27 12:32:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| cf7216c4-8e27-37e7-be66-7517bfb6ae44 | -4.63005 | -43.39965 | 2024-10-27 12:32:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c6a8c2c5-e47f-3dd4-985e-054148e2f9e7 | -4.37942 | -43.54391 | 2024-10-27 12:32:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 634b97c1-6c89-3052-8ab9-6d08da512008 | -4.34152 | -43.03682 | 2024-10-27 12:32:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c2cc7ac9-7cd9-3d5d-a9a6-8831844bc8b7 | -4.21934 | -43.62694 | 2024-10-27 12:32:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 94f82392-4fb2-3600-a7d9-1ad4ec54ea64 | -4.16973 | -43.26812 | 2024-10-27 12:32:00 | TERRA_M-T | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9634857c-4091-3bd3-bd5c-a95aec998edf | -4.02374 | -43.64137 | 2024-10-27 12:32:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 305310a6-5708-32e0-a031-dcca0269c248 | -3.82061 | -43.19479 | 2024-10-27 12:32:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 63393208-ab86-3d31-9946-474e4154ee12 | -3.78212 | -43.33546 | 2024-10-27 12:32:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ddc0d53e-6533-340f-bbf9-135c22d1025c | -3.76815 | -43.30623 | 2024-10-27 12:32:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9699d4fb-25a9-3864-b6f0-550666f7fb9a | -3.75924 | -43.305 | 2024-10-27 12:32:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f9582a57-7bb9-33e1-95fc-3e29b1253e1e | -3.72428 | -42.7768 | 2024-10-27 12:32:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 8f7adb90-8b72-3594-8c98-fb49628988fa | -3.72012 | -42.41891 | 2024-10-27 12:32:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 24.5 |
| c6403b8a-bcce-39f5-8144-9563191b8ee8 | -3.71231 | -42.40822 | 2024-10-27 12:32:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 2398c947-2b3f-335e-b211-a7bb51935c6d | -3.71097 | -42.41763 | 2024-10-27 12:32:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 34.3 |
| 6560bdeb-2b9e-331a-87cd-39107e3613a8 | -3.56975 | -42.18158 | 2024-10-27 12:32:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| d3f41100-925a-37f2-800c-d898b4f6e65e | -3.54887 | -42.12954 | 2024-10-27 12:32:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 790d4633-76dc-3ce3-98dc-8e3154d4d32e | -3.54263 | -42.03964 | 2024-10-27 12:32:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 5ac74ad7-56cc-33b1-b4da-443c21a1ba9c | -3.53543 | -42.04205 | 2024-10-27 12:32:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 28.0 |
| 5280c11c-0be0-3fcd-ae25-5eb305b83881 | -3.50806 | -41.96843 | 2024-10-27 12:32:00 | TERRA_M-T | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| d824e88f-4300-30e8-9f1a-d3bc71f5da3e | -3.50666 | -41.97824 | 2024-10-27 12:32:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| fb94469d-d6aa-37b7-8b31-ead92cf4387d | -3.42759 | -42.53162 | 2024-10-27 12:32:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4846972d-1cc6-3fca-ae6d-36019941ac2a | -3.42412 | -41.91065 | 2024-10-27 12:32:00 | TERRA_M-T | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| c5a87f31-b02a-35c5-8f04-9d871ff1aba9 | -3.42272 | -41.92053 | 2024-10-27 12:32:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 5c3ebc18-836d-3df7-85db-379dcc765432 | -3.38404 | -41.61325 | 2024-10-27 12:32:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 35c1ac0a-d25e-3c1e-9469-f4f5e33e8f13 | -3.36687 | -42.18012 | 2024-10-27 12:32:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 79f54f1d-ed15-3b35-931e-ffb6fda2d188 | -3.36551 | -42.18971 | 2024-10-27 12:32:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 13.0 |
| b6f86b8f-1ad1-37f6-9b8e-0b984ed00077 | -3.32854 | -42.19781 | 2024-10-27 12:32:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 54.9 |
| 7a94c051-217d-331d-82fc-4675e33e8f17 | -3.14786 | -42.29293 | 2024-10-27 12:32:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 06840685-1599-31d6-957e-223c4867cfb4 | -3.14652 | -42.30239 | 2024-10-27 12:32:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f9ae6443-289e-30fc-a87f-86ecb242986a | -2.9752 | -43.23958 | 2024-10-27 12:32:00 | TERRA_M-T | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 44d3f8dc-6e31-308b-bb56-e75cd5366aa9 | -5.35867 | -46.25092 | 2024-10-27 12:32:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d1e93552-4d40-313e-8ef6-51e5e8c41097 | -5.08847 | -45.01591 | 2024-10-27 12:32:00 | TERRA_M-T | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| dffea3f8-a613-3071-a605-5810b21c191e | -4.27602 | -44.32272 | 2024-10-27 12:32:00 | TERRA_M-T | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 69bc8ba8-15c3-3da2-a41d-eac206ef264f | -4.13646 | -44.13773 | 2024-10-27 12:32:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f7a4228d-b86c-30e6-888a-1002e2581305 | -3.89978 | -44.56075 | 2024-10-27 12:32:00 | TERRA_M-T | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 51fb0132-14eb-33e6-8387-3d9a43d17615 | -3.87801 | -44.64839 | 2024-10-27 12:32:00 | TERRA_M-T | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8da24483-a248-38f3-8f02-85c399c7a8e7 | -3.86912 | -44.64714 | 2024-10-27 12:32:00 | TERRA_M-T | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 8d608d89-950a-3aef-ad3f-133893a1c4be | -3.86782 | -44.65604 | 2024-10-27 12:32:00 | TERRA_M-T | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 577f6354-5a75-3152-a3d1-8b440479ae96 | -3.7029 | -44.58398 | 2024-10-27 12:32:00 | TERRA_M-T | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bb8886bd-21d0-3f80-8b01-02c4ae02489a | -3.694 | -44.58274 | 2024-10-27 12:32:00 | TERRA_M-T | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8cf52bbb-97d7-316d-99f5-fce2863a5962 | -3.56555 | -45.08762 | 2024-10-27 12:32:00 | TERRA_M-T | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| ebd0d172-9dee-3f5f-8eda-4d1bba883c3e | -3.54796 | -45.07902 | 2024-10-27 12:32:00 | TERRA_M-T | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a8f99d0f-ff40-3812-88c5-cd309b3349c6 | -3.45299 | -45.41386 | 2024-10-27 12:32:00 | TERRA_M-T | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| b146f5dc-3de3-3cdd-a62f-edbdee5684b8 | -3.45161 | -45.42321 | 2024-10-27 12:32:00 | TERRA_M-T | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |


[Clique aqui para ver as próximas entradas](README65.md)
