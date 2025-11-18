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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e229c44-9037-312a-9036-324d8acd4f36 | -5.36634 | -35.39107 | 2025-11-18 03:27:00 | NOAA-20 | RIO DO FOGO | RIO GRANDE DO NORTE | Brasil | 2408953 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 21001be4-e12d-30e3-9030-f0fa36a0bb60 | -3.3523 | -44.39449 | 2025-11-18 03:27:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7565369e-5feb-3cb4-9c5f-2316070427e7 | -4.19257 | -44.23904 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 67a8e64c-4d27-32d3-b96f-9d1e37e1d330 | -3.25245 | -43.04321 | 2025-11-18 03:27:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0f95e6cf-41d7-31cd-9cb1-eeece74b624a | -3.34544 | -44.39951 | 2025-11-18 03:27:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c6e18582-db79-3bfc-81d6-66426eaecd38 | -4.18728 | -44.24976 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f93c0e64-bc3f-3773-b7f0-95d46b7fac57 | -4.17498 | -44.24146 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 038eaf78-2ba9-3685-af19-f1c12390489d | -4.18483 | -44.24378 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a30f0811-8841-371d-b3a2-ced8f6342891 | -4.1347 | -38.34934 | 2025-11-18 03:27:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f6111cda-2827-3fc0-8375-307836e300c7 | -4.97232 | -41.85518 | 2025-11-18 03:27:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5a8e12d9-0f76-35fe-8f97-6fecf71dd297 | -4.27338 | -44.2485 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd6c032e-7281-3f68-a24c-97225e6f5aee | -3.25077 | -43.05325 | 2025-11-18 03:27:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfceb935-52a7-376b-b4c4-4cfda28827b3 | -3.8693 | -40.45724 | 2025-11-18 03:27:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0d5793fe-81a1-34c2-b031-9f1b4ea02ead | -3.58545 | -43.60303 | 2025-11-18 03:27:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ba29734-eff6-346e-99eb-7a2f6d71af4f | -3.25328 | -43.03822 | 2025-11-18 03:27:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5b50e48b-39cc-3b9a-8cea-d51d7f319f97 | -3.2453 | -43.04724 | 2025-11-18 03:27:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ea22006-fa8e-307a-a155-716759c47602 | -4.97301 | -41.8513 | 2025-11-18 03:27:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5bea875c-74b3-3b8b-a013-3d5b73227a7f | -4.19921 | -44.24038 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f9da296-0c9f-3b8f-bd76-45befe70e77e | -4.18372 | -44.24989 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 476c77b8-9572-3c94-bff0-424de6e894c5 | -5.30452 | -35.70099 | 2025-11-18 03:27:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fd147745-fd0a-3b87-a2d4-16c2621ff825 | -4.19149 | -44.24503 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 57f00db6-7835-3da5-80c2-056a32d9fdc4 | -3.34447 | -44.39929 | 2025-11-18 03:27:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ff705a28-498e-3b65-b819-cddd775b6372 | -3.35221 | -44.40092 | 2025-11-18 03:27:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| af986f7d-8ad8-3da5-a757-15410a7c7728 | -3.34552 | -44.39309 | 2025-11-18 03:27:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f5c6190-6196-33f3-94e2-4dcaf4ad17c7 | -3.60395 | -43.61237 | 2025-11-18 03:27:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 401dc177-a16a-3b5d-a6d4-690ba8baaa75 | -4.18939 | -44.23769 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 46d46b10-adb8-3e4c-bfef-7e55dd791fed | -4.97731 | -41.86012 | 2025-11-18 03:27:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 362f6f76-313e-3ab3-a2e1-b0b451a44b8d | -3.24615 | -43.04214 | 2025-11-18 03:27:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aca2019c-2037-3969-97fb-7196cfd47d27 | -4.1827 | -44.23661 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| d7d822b2-12ac-30f9-8689-29fbef927e09 | -3.59748 | -43.61116 | 2025-11-18 03:27:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 811f26ad-ff4a-3989-9024-99dfe087b73d | -3.34653 | -44.39331 | 2025-11-18 03:27:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8a429693-6436-3722-91ed-8d21aef0f88d | -4.47116 | -38.50605 | 2025-11-18 03:27:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d84f0163-79be-347c-a5fd-1fde3bb4f734 | -4.1806 | -44.24866 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4e9859bf-345a-3443-824e-1510fb54264c | -5.92034 | -35.85012 | 2025-11-18 03:27:00 | NOAA-20 | BARCELONA | RIO GRANDE DO NORTE | Brasil | 2401503 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bedf45eb-3a8c-3aef-b4b9-a89cd6bfc68e | -4.20026 | -44.23452 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93240211-ed15-3316-ad28-3d02a7c6282d | -4.61014 | -41.73378 | 2025-11-18 03:27:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a2303064-e1c2-302e-8e1e-2d63cc8a78c9 | -3.25603 | -43.04175 | 2025-11-18 03:27:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4d254795-aac6-3337-baf7-0f797537a041 | -3.24798 | -43.05074 | 2025-11-18 03:27:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf9bdf35-6b37-36d0-ac51-46408183c91f | -3.603 | -43.61779 | 2025-11-18 03:27:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4c59ae1-201a-32b1-842b-6113baef7b37 | -4.17603 | -44.23547 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 5616a11c-468f-3103-b4c2-6474b1d0fdfd | -3.25517 | -43.0467 | 2025-11-18 03:27:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 549f2466-8302-3182-bb67-3ed4b6937f84 | -3.59741 | -43.61129 | 2025-11-18 03:27:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d05e88bf-8576-35c3-a9ca-2cdbbb989b83 | -3.2543 | -43.05172 | 2025-11-18 03:27:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d80b9ce2-192c-3fb6-80da-20bfb58d2aee | -4.19497 | -44.2451 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7506e724-1b62-3069-a8a7-54b1c5e79a63 | -4.44657 | -44.22141 | 2025-11-18 03:27:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3da3662d-7d99-3c53-8cd3-07bed80eb329 | -3.02564 | -44.48317 | 2025-11-18 03:27:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df67c83f-13ff-3798-8a6a-5af96ad0c525 | -3.35125 | -44.40068 | 2025-11-18 03:27:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8c3c9ea1-a219-3a21-9ec5-dbc286cc2fbe | -3.47116 | -40.229 | 2025-11-18 03:27:00 | NOAA-20 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b636235e-f3ac-3fb1-b2e4-dd710ad2d309 | -4.16832 | -44.24022 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e01c2b6-a391-3469-9bd9-2dcd7d57ff0d | -3.25161 | -43.04824 | 2025-11-18 03:27:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd9b38d5-85ff-3504-9b76-f855440c4b4e | -4.45079 | -44.21972 | 2025-11-18 03:27:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d948d53d-f3b9-3755-9726-eb4f79ef4f0a | -6.66907 | -42.03294 | 2025-11-18 03:29:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 85413dc5-b2b7-372d-92f7-0aeab7739d40 | -10.51153 | -43.95538 | 2025-11-18 03:29:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e2e486d-9c2a-3296-8242-cdd7ca20edf7 | -4.77018 | -44.93259 | 2025-11-18 03:29:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 708a2dca-a95e-318d-8f20-3c8c66d884b5 | -6.67109 | -40.90839 | 2025-11-18 03:29:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dc14a3eb-4040-3556-afc5-fed240519e8b | -10.39151 | -44.9254 | 2025-11-18 03:29:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f309e0a9-beec-3b7e-bc3a-49628ab2c2a8 | -6.70699 | -40.79535 | 2025-11-18 03:29:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 46f6a7d7-747d-3cab-b169-4fb67e4143a8 | -7.43401 | -45.19872 | 2025-11-18 03:29:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4cabe047-b573-3ac7-a0a7-ba35162c26a6 | -6.67399 | -42.03768 | 2025-11-18 03:29:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 2e6e87f3-815e-39db-8a65-36b09f1c70ce | -7.62595 | -42.58731 | 2025-11-18 03:29:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 71c63433-ab33-39cd-a730-e3f966556460 | -8.58726 | -44.1118 | 2025-11-18 03:29:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eaf0dd71-db5a-33cb-9002-30864c0ddf52 | -7.431 | -45.20067 | 2025-11-18 03:29:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67e56601-b4fd-3b90-83db-1045e9e7f008 | -7.37915 | -39.12579 | 2025-11-18 03:29:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ed950d82-ae28-32c2-99bb-edd644186d13 | -6.44311 | -43.82071 | 2025-11-18 03:29:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 443261f8-25bb-3eda-bc6b-b1e446186ea6 | -6.67329 | -40.8959 | 2025-11-18 03:29:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fd802f18-35ce-3055-b0d6-94b334e1900f | -5.47038 | -41.40662 | 2025-11-18 03:29:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7677aa18-04a4-30b8-9782-715f9aec8631 | -5.46015 | -40.98219 | 2025-11-18 03:29:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7733eecc-dc30-36a0-ac31-1a02d24a6218 | -7.4328 | -45.20493 | 2025-11-18 03:29:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b11b3b92-010e-3204-8fb9-ef6cf2a05213 | -4.64097 | -45.52479 | 2025-11-18 03:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 842faadd-50cc-34bf-893d-c27b8a471483 | -6.66835 | -42.03691 | 2025-11-18 03:29:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 8bb69877-4d46-3f3f-b5ef-a23ca2be2d43 | -6.67164 | -40.90524 | 2025-11-18 03:29:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1bfc4be2-8f07-3d2d-a59c-b3d0fee6d8cf | -8.54352 | -46.05331 | 2025-11-18 03:29:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d83c4c31-76f1-3efe-bfb1-971816653f4d | -10.90514 | -40.5377 | 2025-11-18 03:29:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b95d8713-0290-3185-8f20-996657837b83 | -6.43996 | -45.74103 | 2025-11-18 03:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59c56963-b2f3-3d5a-aa53-e5ab666e1287 | -5.42304 | -43.0485 | 2025-11-18 03:29:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b41fe75b-a6c1-3fe1-b97b-d12ea2ea1df2 | -5.46074 | -40.97879 | 2025-11-18 03:29:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5c758e67-1867-3398-9650-f3e7e3f82ed3 | -5.46253 | -40.96857 | 2025-11-18 03:29:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2357ac56-40c8-3023-8e77-1c34914a25ef | -10.61683 | -42.32127 | 2025-11-18 03:29:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0dd0b0ee-ce58-3a65-a0c5-ab121c83f150 | -10.61151 | -42.32023 | 2025-11-18 03:29:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 61e523a3-f882-3a41-8b10-4108ef8e5366 | -10.51572 | -43.96532 | 2025-11-18 03:29:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ef852c18-2cec-3afc-afc8-bee0b4d41852 | -7.96521 | -38.28659 | 2025-11-18 03:29:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1f6803e9-5ac1-37f0-b32b-a0fd5c03632f | -10.50207 | -43.95561 | 2025-11-18 03:29:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7c984575-a081-3f51-bc6a-0a6bfe75302d | -6.12571 | -42.96337 | 2025-11-18 03:29:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3a3629e7-4c75-3a9a-a314-0b3e037761a0 | -10.85676 | -44.09688 | 2025-11-18 03:29:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6d1756bd-e51e-3f09-b993-5a487fa3fbc2 | -10.2401 | -36.2955 | 2025-11-18 03:29:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 252ea2b7-3196-317c-a40b-cac856067d56 | -8.79062 | -44.3977 | 2025-11-18 03:29:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c51adf1-4d30-388b-8d32-6e1872aa6a29 | -8.7402 | -39.1291 | 2025-11-18 03:29:00 | NOAA-20 | ABARÉ | BAHIA | Brasil | 2900207 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 709541db-9ee6-3918-84b0-aced49f2da43 | -6.73877 | -35.1188 | 2025-11-18 03:29:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5b4920ad-0859-3e0e-a8a6-34f18e3d0791 | -5.63075 | -43.93586 | 2025-11-18 03:29:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f229ee3e-7c9e-31a7-abe0-598cad6db45a | -6.72419 | -34.94668 | 2025-11-18 03:29:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5dd4da73-072e-37db-a9b2-67e1fd821db3 | -6.48793 | -39.77016 | 2025-11-18 03:29:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 66262c43-ac1d-31e5-8668-e70be376d99d | -10.50983 | -43.96404 | 2025-11-18 03:29:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9967e229-f282-3788-95cc-9302517964e1 | -8.79686 | -44.39898 | 2025-11-18 03:29:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8f37946-a426-3147-b28c-00ae304c4dd1 | -6.72402 | -35.21903 | 2025-11-18 03:29:00 | NOAA-20 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 99d58f1a-a6f9-3f9e-bb7d-099efa86ca2c | -7.33828 | -46.1774 | 2025-11-18 03:29:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f473289e-f58e-3fb1-872e-766c59b74daf | -6.93313 | -41.53639 | 2025-11-18 03:29:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1fa7dbfb-aa3b-3555-9df6-b8aa9ad5376b | -5.45481 | -40.98137 | 2025-11-18 03:29:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eb82ad1b-6c32-369e-93f8-da5267689e0c | -10.24084 | -36.2912 | 2025-11-18 03:29:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 786339c6-131c-36be-94a7-de52aa0f1a91 | -9.96715 | -38.33973 | 2025-11-18 03:29:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4627fe70-72be-3f06-b8ae-176edaec7e1e | -5.47423 | -44.69323 | 2025-11-18 03:29:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README18.md)
