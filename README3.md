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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb3163b9-cb36-3205-b99f-1e1b9d0ea177 | 3.61356 | -59.85924 | 2025-02-02 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55ed96d7-7303-3aae-8b47-09d2458f9ab2 | 3.64279 | -60.54222 | 2025-02-02 05:27:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e63c54df-913c-3a6a-acb8-0ba42324ce59 | 3.72739 | -60.49722 | 2025-02-02 05:27:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62de87bb-33ec-373d-8071-4ccd4a8df9b1 | 2.45301 | -61.31628 | 2025-02-02 05:27:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c907ef04-fc0e-3cc5-8611-4b1d53897652 | 1.94693 | -60.84211 | 2025-02-02 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c7adf8f6-f402-3a06-b132-37fc58355b10 | 4.60916 | -60.70487 | 2025-02-02 05:27:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c28ea9dd-5d9f-366b-aa31-7ae14cb7d4cc | 3.55119 | -60.36901 | 2025-02-02 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5d914c2-75e1-3a3e-978f-cdca23395e3d | 1.42091 | -59.9606 | 2025-02-02 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49f04457-8a78-321e-bc1f-18f4bc141fa7 | 3.64828 | -60.79402 | 2025-02-02 05:27:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f578413-dc7f-3d24-8307-5df282fea119 | 4.60862 | -60.70138 | 2025-02-02 05:27:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 70378fe3-bae2-3fdb-9d1b-94e5ffb38088 | -11.90314 | -63.87983 | 2025-02-02 05:31:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09d07bb7-99dd-3ca1-ab68-6340cd786784 | -19.7918 | -55.33932 | 2025-02-02 05:31:00 | NOAA-20 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44e5b873-4d58-3733-a887-a329c855a228 | -12.40186 | -63.99025 | 2025-02-02 05:31:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40e01e04-7fd1-36ca-8bd6-16202df0b173 | -19.78587 | -55.34307 | 2025-02-02 05:31:00 | NOAA-20 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba3b6cd1-8886-3c02-8d7b-7acc75fcbafa | -12.4013 | -63.99379 | 2025-02-02 05:31:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32a17380-5872-369d-8a36-3cac1e76bbf6 | -11.88991 | -64.00421 | 2025-02-02 05:31:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1087fad-174d-3c88-bdc7-fda693b9be19 | 3.92458 | -59.72811 | 2025-02-02 06:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6bcce88f-8d70-3527-a196-ddfa8cf3d0a7 | 4.31203 | -60.60207 | 2025-02-02 06:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 134b595a-553e-3b9f-888c-00829edfb483 | 3.92664 | -59.72607 | 2025-02-02 06:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c28c1d06-64c2-302f-8cfe-5a03c04269a6 | 4.30662 | -60.60803 | 2025-02-02 06:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cedee219-710a-3e0c-a636-4adef1455ee9 | 4.30894 | -60.60784 | 2025-02-02 06:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1fef6569-2ebf-39b4-b410-98dfa0a2b4df | 4.30799 | -60.60218 | 2025-02-02 06:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 17db6c18-e4fc-3567-b417-dfea3950e476 | 3.93121 | -59.7269 | 2025-02-02 06:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63bf9707-9e8e-3f22-836a-c6e770ca9416 | 3.61578 | -59.86171 | 2025-02-02 06:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d6dd6c9-2436-3362-ae63-8bb75ac7024a | 4.30566 | -60.60254 | 2025-02-02 06:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 392964b9-06e7-35e9-9f00-90ec06733146 | 4.31304 | -60.60787 | 2025-02-02 06:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b25fa021-e36a-3311-b838-4634d9d3954d | 1.94231 | -60.84077 | 2025-02-02 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f7672e3-05a4-3649-bd25-f99985928c8c | 2.45407 | -61.31557 | 2025-02-02 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d733701d-ce03-31c0-be62-374fd9fdf4ba | 1.94957 | -60.84503 | 2025-02-02 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ab90dd7c-a5da-3493-ae11-1136a902b8d7 | 2.45486 | -61.32043 | 2025-02-02 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 920634a1-806a-376f-839a-a2c8c9c91706 | 1.94871 | -60.83976 | 2025-02-02 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4c2b5ece-d694-39bf-8eee-5e259920fba7 | -5.53404 | -38.5807 | 2025-02-02 12:08:00 | TERRA_M-T | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 3e6e5d7a-fce8-336c-9cde-1c897034f6d9 | -12.08133 | -38.07223 | 2025-02-02 12:10:00 | TERRA_M-T | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 72311d44-7f98-35d7-b0f4-34cbb8bf7544 | -13.59077 | -39.15163 | 2025-02-02 12:10:00 | TERRA_M-T | TAPEROÁ | BAHIA | Brasil | 2931202 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 54601b2d-badf-3311-b322-79081fa3616d | -13.69962 | -39.42345 | 2025-02-02 12:10:00 | TERRA_M-T | NILO PEÇANHA | BAHIA | Brasil | 2922607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| c1269d40-2c3d-3e36-b6e2-aad6cff82bbf | -13.65057 | -39.85821 | 2025-02-02 12:10:00 | TERRA_M-T | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 5419f349-b953-3634-93ee-3e7bb9038bed | -13.69103 | -39.62944 | 2025-02-02 12:10:00 | TERRA_M-T | WENCESLAU GUIMARÃES | BAHIA | Brasil | 2933505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| deb7b9a3-1260-32af-8107-ee46c034d36f | -13.41835 | -39.67605 | 2025-02-02 12:10:00 | TERRA_M-T | UBAÍRA | BAHIA | Brasil | 2932101 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 49a99135-74f3-326c-934e-929e80df020b | -18.4404 | -39.82802 | 2025-02-02 12:12:00 | TERRA_M-T | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| b1ec25db-d64c-318d-b290-d5703524f765 | -20.20328 | -40.31073 | 2025-02-02 12:12:00 | TERRA_M-T | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |


