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
| 5aaa021c-6b78-35a6-9bd0-e77fdf393e89 | -8.47964 | -53.24198 | 2024-10-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83bb789e-bce8-3600-a350-c6b02f1a2db5 | -10.24927 | -52.75328 | 2024-10-13 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd292692-46ad-3fc8-98a3-8828c1339c8b | -10.22412 | -52.68913 | 2024-10-13 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a6142dd-82e7-3d43-b32e-d96f9604b3e2 | -10.22348 | -52.69303 | 2024-10-13 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80133868-223c-339a-b5cd-a93067d74583 | -10.21435 | -52.68354 | 2024-10-13 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8085cfa-4b62-3802-b130-d3b158fc6cef | -10.21024 | -52.68686 | 2024-10-13 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65499828-cc1e-31a0-8d24-26fc6e72e80b | -10.20246 | -52.32844 | 2024-10-13 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9d7be94-bcfd-3547-a89c-32483d175bdf | -10.08456 | -52.59437 | 2024-10-13 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 02b82921-06c2-3699-a5c7-0e5ddf2488a0 | -10.08209 | -52.59463 | 2024-10-13 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3babbd06-1c0f-3b49-b8a1-cd98fd1a020c | -10.08146 | -52.5985 | 2024-10-13 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b8361f43-b3e8-3894-83bf-c96d46b68cba | -10.08046 | -52.59769 | 2024-10-13 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d433e3c2-e22a-3fb1-9d4e-09c359ef312b | -10.07737 | -52.6018 | 2024-10-13 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b66680a-6da4-3148-ad94-d44662a6117c | -10.07675 | -52.60567 | 2024-10-13 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1e5905d-2264-31b1-b965-b3f7fada9f70 | -9.73315 | -52.82642 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a65b04da-52f5-3cd8-a215-c98648c1af50 | -9.73249 | -52.83039 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c97d138-e122-3c54-8e70-52cbd4358d6e | -9.72988 | -52.84612 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9f36876-1792-3ad2-b79a-b45264a0c411 | -9.72965 | -52.82583 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46b5e96e-69a3-3252-9b36-db0152dc2d36 | -9.72922 | -52.85007 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a8ae7ab-9fd8-3bbc-8b58-7c30e5dd3a76 | -9.72899 | -52.82979 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bae4fe1a-93c6-38d7-a13a-a28576259cc5 | -9.72856 | -52.85403 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac3bb5e2-d6f4-3609-ab79-e259e76c15c6 | -9.72748 | -52.81729 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7198196-b27d-3ec6-95da-6ee9759f12e5 | -9.72636 | -52.84557 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37262043-b420-39ab-a9ab-da17aa509ec4 | -9.7257 | -52.84955 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a8486d2-c5ce-33e5-a7c9-7af892a6cc0d | -9.72398 | -52.81667 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce520d76-d219-393f-80e1-1eec51e36199 | -9.72351 | -52.84106 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aadcc717-f5ac-39ec-8fc1-7ea7972e2a65 | -9.72332 | -52.82063 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e01f25d2-eb50-3f0e-ba35-d14edcb775a9 | -9.72218 | -52.84903 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3892315e-8a46-3d9d-aa21-32387e8db584 | -9.72049 | -52.81603 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cf1efaf-b61f-3d90-a889-4b4b5808d152 | -9.71983 | -52.81998 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cb94749-903b-373d-994a-b419d615dad1 | -9.7195 | -52.81651 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1779c41-cc0e-3ec3-969c-c15c9a12a1cc | -9.71801 | -52.85238 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2883368c-f74d-3bff-bdd4-ccc4fc962575 | -9.717 | -52.81535 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c2ef157-86b9-3777-9053-1d687946ce48 | -9.71635 | -52.81928 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 392bd860-655e-3b34-b101-6d9f9bf78b7f | -9.71601 | -52.81582 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf381da3-ac06-3a29-b566-98346831de25 | -9.71537 | -52.81975 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0aba03e-2113-381b-b696-c8085c24bfab | -9.71453 | -52.85168 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 233fdd27-7f18-39b4-beae-aff43955e801 | -9.71386 | -52.85567 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8c3a8b23-d475-3656-9345-d9576f1a2974 | -9.71371 | -52.85223 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6d65b4a0-c599-301c-aff6-d9b003d5668f | -9.71188 | -52.81911 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 66d3d719-45d1-3ea7-a33b-a84f02cb84c8 | -9.7117 | -52.84703 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d4e6e5de-d871-3df4-8d3a-ff5e104e6478 | -9.71124 | -52.82308 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af20a18c-dd73-3b22-bdde-29e118465625 | -9.71102 | -52.85108 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eaa013ea-a535-3649-95e3-b680d4dec8ac | -9.71085 | -52.84763 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 044598bd-a52c-3570-ac85-8e502129859d | -9.71019 | -52.8517 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6e587572-84c2-3fcb-a374-dd40a3620122 | -9.70797 | -52.84317 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aa3dc90a-bdf2-36a3-a410-00d183749b03 | -9.70771 | -52.8226 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5284ba37-82d9-3239-8335-34d4bac7e956 | -9.70731 | -52.84722 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 303fefdf-bb49-3c0b-a69f-c325af649ef6 | -9.70706 | -52.8266 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0724808d-3934-3bb6-908a-b91eb4a457c9 | -9.70289 | -52.83014 | 2024-10-13 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a084699-1d07-356a-8b76-ea17f0f18227 | -9.57813 | -52.16923 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 024a0eed-b87c-3466-817f-6536ab5b9801 | -9.57752 | -52.173 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ddd90f7-49a2-3f89-aa12-5f3a2f3c6b4b | -9.57471 | -52.16867 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 805568d9-9c5a-3094-8755-0dd2ab92f0a1 | -9.57129 | -52.16811 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 421541e9-fc6c-3908-9f0b-5748c1b4fe52 | -9.57068 | -52.17189 | 2024-10-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| e8df92a1-2497-36ad-9a68-c3d09233f31f | -9.57049 | -53.25771 | 2024-10-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 166d5f1f-18e7-32a5-a823-d544641b78f8 | -9.56979 | -53.26189 | 2024-10-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4f820ad-5d6c-321c-b47d-43306a123f4b | -9.56909 | -53.26608 | 2024-10-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 845fadb0-22c4-3730-a6a6-d8159047dae7 | -9.5662 | -53.26132 | 2024-10-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 252c5a16-33bb-3f0d-8d77-d2fc649bb5eb | -9.42587 | -53.19275 | 2024-10-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20251ca2-f1bc-309d-ae1b-9c75f584a0d0 | -9.01203 | -54.51036 | 2024-10-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bbb8a0c-cafa-3e34-a989-6004a2996874 | -9.00816 | -54.50975 | 2024-10-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89635991-50a9-3248-a6e0-263ddc38a80a | -8.63323 | -53.64866 | 2024-10-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48d34493-441a-3c5f-9392-7347a47874cb | -11.27937 | -54.59033 | 2024-10-13 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 629d5436-2ef8-3500-ac21-48232948f67d | -9.33871 | -57.60563 | 2024-10-13 04:40:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85a1705e-e0c0-32c6-8bb0-074e47670f99 | -9.33698 | -57.607 | 2024-10-13 04:40:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e56fa6b-423f-351e-ae7e-b91e20f43a2e | -10.40333 | -57.3138 | 2024-10-13 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e2e947c-b471-3196-8e41-25b6bc8feedf | -9.6751 | -57.21047 | 2024-10-13 04:40:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e59baafe-1aa7-30fe-8b26-c19fcd9efe49 | -10.05681 | -59.00433 | 2024-10-13 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58530d5c-662b-3e1a-bb1e-ae20d83e6aed | -10.05624 | -59.00736 | 2024-10-13 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de366b4f-a17d-3bfd-8c0e-3c7afb9582ab | -10.05425 | -59.00435 | 2024-10-13 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4981b6de-4af9-32c7-8357-4bc52b7e9b82 | -10.0537 | -59.00739 | 2024-10-13 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bf7e96b-3043-34a9-af8b-ab8cbbde160f | -10.05168 | -59.00343 | 2024-10-13 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94c30afe-2b15-3320-84f0-937b6d08d5a9 | -10.05111 | -59.00646 | 2024-10-13 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70837564-f4ff-3f51-9e69-4169ffffcc1e | -6.78882 | -59.35453 | 2024-10-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dde8d560-fcc7-334f-a758-92fc682084cf | -9.85333 | -60.31529 | 2024-10-13 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b7dcab1b-53c8-3c31-96fe-85dbc80572e3 | -9.84772 | -60.31432 | 2024-10-13 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 20404c36-b124-3842-ad17-83a6ee0090e1 | -9.84698 | -60.31819 | 2024-10-13 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 060b5575-b96b-3f1b-9b67-b4c827142c7e | -9.84213 | -60.31323 | 2024-10-13 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c47dfe43-2bfb-3eec-809a-c6b9ea18c3c0 | -9.8414 | -60.31705 | 2024-10-13 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a284896c-c93a-3a26-91f1-ac02c56a1944 | -9.84068 | -60.32087 | 2024-10-13 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 5e71fb71-ec1f-3ac1-afc0-132710ae5849 | -3.05027 | -61.67686 | 2024-10-13 04:40:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| da0d80b8-01c6-306a-8758-75bfe9ea1f6f | -3.04921 | -61.68299 | 2024-10-13 04:40:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| acea5237-b0d8-3e3c-b20a-5b35a518ac56 | -9.10305 | -53.31324 | 2024-10-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 838e766c-34a8-3488-80bd-eb3c21c40a50 | -5.3815 | -43.51387 | 2024-10-13 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca602a96-48ea-3d89-b197-e4357ba559f6 | -11.11301 | -43.34101 | 2024-10-13 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| c6df1ee8-d990-38a4-b2d7-9a9c68930e6e | -8.67282 | -40.40704 | 2024-10-13 04:40:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| f8f40564-1943-31bd-9547-8bfe6ae4cd81 | -8.66735 | -40.40631 | 2024-10-13 04:40:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 0995f79a-cfa3-3623-af2f-6b13eff02d9c | -6.0271 | -40.44852 | 2024-10-13 04:40:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0e914233-5f81-34a3-8294-05622443936a | -9.18998 | -45.78708 | 2024-10-13 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 178e587c-e800-343e-b7e0-334d44c8e22d | -8.72169 | -44.12792 | 2024-10-13 04:40:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0458b92c-8224-3e3c-944c-5b53eaae540c | -8.76218 | -45.6954 | 2024-10-13 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d6d20c52-cef4-3ddd-88d6-6bf2f244eddc | -6.72423 | -43.55989 | 2024-10-13 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6954fff1-2944-3718-a26d-7c4dd14fae82 | -6.46016 | -43.32608 | 2024-10-13 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a7076fc-2c4e-3cec-9e23-43418be112fd | -6.45956 | -43.3302 | 2024-10-13 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14504a9b-ddcc-3708-8119-4da893b1c7ce | -6.51661 | -43.65146 | 2024-10-13 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2773747-ee5a-3371-8f22-b0548e6ced4c | -6.51605 | -43.65534 | 2024-10-13 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f3324481-1847-36f6-9c61-6b1968d36f9b | -8.69101 | -45.26456 | 2024-10-13 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba33fac6-d8e4-3b10-bf80-89e78ce5bbae | -8.53037 | -45.56601 | 2024-10-13 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 856f0e63-7ed2-31cd-b3bb-fbb995527e07 | -6.4282 | -43.93768 | 2024-10-13 04:40:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08c460ac-4d35-3e4d-bcba-c1d53f7d71d6 | -6.04543 | -43.62126 | 2024-10-13 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README58.md)
