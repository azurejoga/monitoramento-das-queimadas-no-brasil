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
| 005d7804-8315-3754-87ba-72eeaba95056 | -8.0513 | -43.1001 | 2025-11-15 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| ac7dd244-b464-38c8-8cd1-a2adf9e6d13f | -11.8486 | -49.2218 | 2025-11-15 05:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 50fe0aed-42d3-3962-a606-9a1016eed881 | -11.849 | -49.2 | 2025-11-15 05:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| b928bd69-e6f7-32a4-9cc8-eb2060ee87d6 | -8.0703 | -43.0981 | 2025-11-15 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 51.2 |
| 9674ba68-b9a3-3a58-8f40-5144dcdf0515 | 0.75467 | -50.77242 | 2025-11-15 05:14:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fa52059c-153c-33f5-8c50-f944e1109052 | -2.73925 | -45.30396 | 2025-11-15 05:14:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 01487d38-f76d-3e9e-b3df-d18bb86e6e4f | -2.73508 | -45.31034 | 2025-11-15 05:14:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 509e40ff-1b00-33ab-9df3-e88bb469cd31 | -1.30504 | -49.05962 | 2025-11-15 05:14:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6623143c-58e1-380e-abef-eff164f17475 | -2.95759 | -45.15152 | 2025-11-15 05:14:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 7200ef09-5bf4-3b2f-bf2f-e8f0dd1336a7 | -1.29619 | -53.76313 | 2025-11-15 05:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8d02c66-2aad-37c5-9755-566a61cddbd1 | 3.54027 | -51.44206 | 2025-11-15 05:14:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91afaabf-5adf-32b5-970d-75a8ef82ab27 | -1.05304 | -48.94275 | 2025-11-15 05:14:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ad566d0-7175-3deb-a0b0-3fdfdf5bafb1 | -1.1117 | -52.59525 | 2025-11-15 05:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2d6a67c7-e2c1-3e5d-a110-aee92144ee2b | -1.29846 | -49.05546 | 2025-11-15 05:14:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 68d11f12-53fb-3e34-9103-15fe4ce64a97 | 0.7591 | -50.77173 | 2025-11-15 05:14:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbd76bed-44b6-3680-b154-6ba87b2f3a4b | 4.02088 | -59.64178 | 2025-11-15 05:14:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a8463aa-8b43-3009-b816-0d5c46a280a4 | -2.15403 | -48.29256 | 2025-11-15 05:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6bd0019-f483-39c7-ae56-1a71e22ed394 | -2.43236 | -48.04914 | 2025-11-15 05:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| feb047c9-11a6-381e-99de-f42581262451 | -1.87315 | -50.95885 | 2025-11-15 05:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de83bf02-ce65-36e5-844d-836515dd5bbe | -1.49821 | -47.80593 | 2025-11-15 05:14:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 761a139f-08eb-3577-ab46-0048581d0d44 | -0.70648 | -48.64413 | 2025-11-15 05:14:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 699e32ed-90c5-3215-9c53-65931bec62e7 | -1.29331 | -49.05468 | 2025-11-15 05:14:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ea2cd807-7540-37c5-b2c7-1fef3fdc43fa | -2.52055 | -47.80648 | 2025-11-15 05:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c734e08c-9903-3168-8717-d46d78b1def8 | -1.29564 | -49.05182 | 2025-11-15 05:14:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 4301b43e-aa0a-3adc-94eb-ea1e5b8693b6 | -2.73597 | -45.30454 | 2025-11-15 05:14:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 336dcfac-901a-3ebe-9941-0fd1ee160c06 | -2.43291 | -48.04538 | 2025-11-15 05:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fadd8c28-d65e-3e45-9596-f068a32a95dc | -1.34119 | -54.60791 | 2025-11-15 05:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6714740c-f3a2-3694-91fb-206b426da75e | -1.10766 | -52.59464 | 2025-11-15 05:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddb532a9-7368-3937-9f17-92dadaa4ad5f | -2.73166 | -45.30906 | 2025-11-15 05:14:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63e4fc80-42b7-3ce2-9199-f4d9a2274ec3 | -0.70597 | -48.64735 | 2025-11-15 05:14:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea837165-7621-3021-b0a0-cf54db630c0d | -2.95668 | -45.15761 | 2025-11-15 05:14:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 27.0 |
| fdc332b2-31c4-39bc-9c31-ece0180e0354 | -1.29518 | -49.0549 | 2025-11-15 05:14:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b9659ebd-460f-3698-9bc6-a606836d8a5e | -1.29379 | -49.0516 | 2025-11-15 05:14:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 65e1d9b8-f3d8-388e-b5de-496df9c64f19 | -1.30973 | -49.06353 | 2025-11-15 05:14:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 00fd2685-9705-3885-962e-9d1d32d7cc06 | 0.14406 | -49.82771 | 2025-11-15 05:14:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bb37a57-dae2-3041-a0d0-a63144b3ef6d | -1.32989 | -49.13895 | 2025-11-15 05:14:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c86fad8-57c6-3a21-bf80-29326be1faa0 | -1.30457 | -49.06271 | 2025-11-15 05:14:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f43e17bc-8903-31ab-83ac-3a82d94f3d46 | -1.29988 | -49.0588 | 2025-11-15 05:14:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7a78a2ab-9be6-3f28-af34-6845b2ffbec1 | 2.34112 | -51.6478 | 2025-11-15 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83b7f3c5-599d-3dbf-a157-d9d1d40592ef | -1.29048 | -49.05104 | 2025-11-15 05:14:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 705791e3-1a53-37cf-861f-3a35c356f5e0 | -1.67891 | -46.92173 | 2025-11-15 05:14:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 56bb1c9e-3683-3156-b84c-f7b981fee237 | -0.37195 | -51.76793 | 2025-11-15 05:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 66104cf7-316f-386c-bca5-08dc30aab4e9 | -1.30034 | -49.05572 | 2025-11-15 05:14:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4be5d6cc-b409-3912-84d4-d36061fd2c32 | -1.34773 | -54.61317 | 2025-11-15 05:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d43afde-9e01-38cb-a5b7-dfcff0b08062 | -2.95081 | -45.1505 | 2025-11-15 05:14:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 5cd6f3f5-0df0-3c90-bb65-eb36353f6a53 | 2.10348 | -60.62039 | 2025-11-15 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c362520e-2bd3-3614-bea4-0e51ed9e7f3f | -1.38154 | -53.83936 | 2025-11-15 05:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbe6b06b-77f1-3c8f-b4a7-d74a262c655d | -2.15456 | -48.28897 | 2025-11-15 05:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4eb95391-37bf-3c81-bc7e-422f195d0380 | -1.34543 | -54.60424 | 2025-11-15 05:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5acff2bd-fef4-3132-9b26-7b45bdcbe479 | -0.70072 | -48.64652 | 2025-11-15 05:14:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 975f01e5-4cc6-326f-99e9-8ebb8130df8b | -2.7401 | -45.29809 | 2025-11-15 05:14:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e596a1c5-c57e-321b-8e42-164a01d6d8c1 | -0.36774 | -51.76725 | 2025-11-15 05:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e3ec1af-9a08-3610-a49d-8e034d9a27cb | -2.15407 | -48.28895 | 2025-11-15 05:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51da20a5-659f-319a-baea-7fc2f4840ff9 | 2.33705 | -51.64843 | 2025-11-15 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 672d0aae-9566-31c4-8813-921a80c8b5c3 | -1.33035 | -49.13591 | 2025-11-15 05:14:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c960c04-ff6f-3e22-9f93-a531610f0e39 | -2.9499 | -45.15657 | 2025-11-15 05:14:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 27.0 |
| e2d1e6ed-bd29-38f9-a87a-3ef689bbe54b | -1.29895 | -49.05238 | 2025-11-15 05:14:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1916ef08-08f8-36e6-b3e6-4db326f30154 | 4.01731 | -59.64247 | 2025-11-15 05:14:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31457490-f8ad-315c-9b82-b0d0ceb7f0a2 | -1.1082 | -52.59111 | 2025-11-15 05:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd4a85e7-8987-3b71-b60f-dd2a02cdd776 | 2.74994 | -60.36585 | 2025-11-15 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7c26a8c1-acac-3a09-9925-bffda5e2aafa | -1.30926 | -49.06662 | 2025-11-15 05:14:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fef1fa1b-56d4-3db5-921e-92d0cdb76d57 | -1.03591 | -53.01033 | 2025-11-15 05:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f638785-3fbe-397e-9228-9920561e44e2 | -2.51935 | -47.81446 | 2025-11-15 05:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ce09890e-9f5c-3d47-ba2d-dab018f4a7d0 | -1.43738 | -52.88403 | 2025-11-15 05:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 60a05acd-4614-3dce-9e44-ef846298111a | -1.05256 | -48.94585 | 2025-11-15 05:14:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ceae8663-48da-373c-9e42-b4f5b0f2ba8d | -1.34478 | -54.60846 | 2025-11-15 05:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d71c0c1-dbf4-3d41-90b8-11a2ef8ce396 | 2.33763 | -51.65213 | 2025-11-15 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 055b14ba-5390-3495-9cdb-f2e9172bac2d | -0.70586 | -48.64698 | 2025-11-15 05:14:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07f1b2e3-76e9-3a6f-8620-48278ff963f6 | -0.97634 | -52.58207 | 2025-11-15 05:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60306f0f-aa90-3b99-8365-a5b29751811a | -1.34017 | -55.65883 | 2025-11-15 05:14:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 636eb317-5c64-3675-87f2-c409e064efba | -2.73687 | -45.29861 | 2025-11-15 05:14:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e032fef-51a8-3e11-ab7e-aba62809c4af | -1.68159 | -53.27873 | 2025-11-15 05:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06068f1b-4892-3e78-af57-335b3043d592 | 2.34171 | -51.65152 | 2025-11-15 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f10b9919-4544-3dc9-8536-47a639ac0de5 | -2.51995 | -47.8105 | 2025-11-15 05:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| cdb80180-ba78-389f-a2d1-08742413a23e | -1.34838 | -54.60897 | 2025-11-15 05:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2f62218-cbaa-357c-8fbc-3dbcc5d16064 | -0.70634 | -48.64374 | 2025-11-15 05:14:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81ea1227-fe29-3d40-85f7-247d0626ea66 | -0.97687 | -52.57858 | 2025-11-15 05:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa3f42ec-d600-3db5-a29e-774dac97df31 | 3.29015 | -60.0551 | 2025-11-15 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 845e3bac-ca36-358d-a9c7-e335ebd53bc8 | 3.28951 | -60.05085 | 2025-11-15 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f215d47-f349-3a77-8610-5f033a9a7e87 | -2.51365 | -47.81352 | 2025-11-15 05:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 76aae27f-8a0d-30b2-8916-4a5096b1bef1 | -0.7006 | -48.64613 | 2025-11-15 05:14:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9329e13a-bf73-3d12-af9f-383fff655049 | 2.74958 | -60.36757 | 2025-11-15 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 214b45f4-3a8c-390a-afe1-19fffc221807 | -2.51425 | -47.80957 | 2025-11-15 05:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 1989028c-4021-3426-8d19-984634d07135 | -1.87342 | -50.96052 | 2025-11-15 05:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 931e2ec5-4466-38bb-917f-8af631f706d9 | -3.86057 | -49.13727 | 2025-11-15 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76db952b-8f88-33c7-a742-885454b80f74 | -1.80912 | -54.65538 | 2025-11-15 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa1248ac-1148-3b73-bf3b-49eacfcb1306 | -6.16126 | -48.03836 | 2025-11-15 05:16:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0a3f3454-324f-31ac-b2f0-96360105d8c0 | -3.17237 | -48.61502 | 2025-11-15 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f903ba15-ec69-39a9-bf57-2e77f2d60fe8 | -2.86796 | -51.47484 | 2025-11-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1319232a-b895-3f4b-a5fd-095063f1422c | -3.22663 | -45.481 | 2025-11-15 05:16:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5ec3d4be-534d-3d57-a64f-99e5bd252675 | -4.41754 | -50.82219 | 2025-11-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9bf16272-6727-3856-aaa5-d049e1b2f0a2 | -3.78115 | -54.47571 | 2025-11-15 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9819fe2-d2d8-32ba-9a64-c752bc808312 | -3.24198 | -52.92062 | 2025-11-15 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c65bc15-ff1f-349a-b083-0b2da6fdec35 | -3.21997 | -45.47993 | 2025-11-15 05:16:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 479269c7-cf9c-3e3e-b39f-b666027eab6f | -3.14363 | -49.23621 | 2025-11-15 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac45f31c-dcec-3a93-a175-19a0234286b8 | -3.9115 | -50.03904 | 2025-11-15 05:16:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8989a86a-945f-3064-a849-71cb440d207d | -7.21936 | -47.98033 | 2025-11-15 05:16:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1379e623-8565-3fae-a223-b5cb8ce0ce40 | -3.59716 | -54.67414 | 2025-11-15 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d71c4d6d-8313-307a-a234-5a46c419cb8c | -9.35437 | -50.7391 | 2025-11-15 05:16:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8da236b8-6ef0-3bb0-81bf-df44abe1af85 | -3.15383 | -50.26466 | 2025-11-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README51.md)
