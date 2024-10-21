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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54b9894d-153c-3049-bd12-f256bb3acca1 | -4.25632 | -50.99454 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d288376-baa5-3107-ba65-86716ea30e75 | -4.25348 | -50.99023 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18c751b1-c8c3-39a2-93cc-2e082db197a4 | -4.25289 | -50.99398 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a23e720-f541-38ef-9acf-3a3f8e36191f | -4.2523 | -50.99773 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a117a4ac-8e50-3b14-bc02-fda4d755f131 | -4.25065 | -50.98591 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4863a71f-3e3b-330f-ada2-83d4e3940db0 | -4.25006 | -50.98965 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3dcd7bc4-1a5f-342c-adcc-1584a6df542a | -4.24946 | -50.9934 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc15512c-9194-318c-9eae-e2f38ec1879a | -4.24887 | -50.99716 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31c50517-335d-3678-96a6-cb91c1ff32d0 | -4.24663 | -50.98906 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68414016-5b03-32b8-8d6a-c1fd891a3dd6 | -4.24604 | -50.99282 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e8e8e17-3e82-3453-a90c-2923b2d2d29c | -4.24544 | -50.99659 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa38b1bf-1823-30b0-9ad5-da7bc58956c8 | -4.24485 | -51.00034 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14489985-65f2-3d19-b3b7-a58debf6623a | -4.24261 | -50.99226 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8731839-c090-3565-b344-057dc65f6fc3 | -4.24201 | -50.99603 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 449957c0-0bf7-3523-a657-2b9584fc6990 | -4.17257 | -51.23273 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1adfad75-9283-3d00-9e9e-73bca4cdd262 | -4.16152 | -51.03697 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8b48060-a99e-31f4-bb18-546bf19575d0 | -4.13682 | -51.10243 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 171b3d78-3816-3acc-bc2b-4673c463505b | -4.12269 | -51.1085 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60b6f33f-67f4-3cd5-bbe1-8f7229540d63 | -4.07706 | -51.12848 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ec99653-d17a-3884-88da-c10011463721 | -4.05144 | -51.02384 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31100d7c-45d5-32c3-90bd-1b28502e7531 | -4.04881 | -50.95444 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57498f0f-4b4c-3ecc-b265-c12a06383b65 | -4.04861 | -51.0195 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 569f4737-d4f7-39c1-9bbf-885db3b9233d | -4.04859 | -50.95423 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f4cec723-fc8c-3957-9bd9-350c20940041 | -4.04822 | -50.95814 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b11eb87b-8141-3956-a5dd-d012bb9b5309 | -4.048 | -51.02328 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f66d554-441c-3971-a41f-c264d9779dde | -4.04799 | -50.95793 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e32b458-f622-3d0c-a5cb-7965b07f9a76 | -4.04739 | -51.02706 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f826735-dbb4-3713-ac83-32412bdb0868 | -4.04538 | -50.95387 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81158807-e4f2-32de-9d66-bc1b21adf711 | -4.0448 | -50.95758 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be6aefa3-ac4a-31bd-89ab-6b931685a1f5 | -4.04136 | -50.95707 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e16d6b7-17b7-34bb-b4a5-2a8070eed959 | -4.02622 | -51.0083 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d28680ff-8fb4-3985-8597-134a83f29b1f | -4.02563 | -51.01206 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6edc0548-ca02-3cd5-82f5-0261666a2f26 | -4.02503 | -51.01584 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dca5b50e-2269-3a5a-a9e2-f2fb94719ceb | -4.02277 | -51.00784 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cffd4f30-0caf-3d86-b2f1-936a85bf3abb | -4.02218 | -51.0116 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ff0cea35-8acf-3eba-9335-bad6067a8abe | -4.02159 | -51.01534 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7815c14c-cf3a-38cd-883d-a66d89fdb8a5 | -4.01873 | -51.0111 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 82aac3d3-5a5c-373e-9831-422953a204fc | -3.94736 | -51.23703 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1942f609-bacc-370d-bb2e-3ff291fd962a | -3.88487 | -51.19327 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f69549bd-1811-38a6-8f1b-55de833ceb2a | -3.88426 | -51.1971 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c6e8d2c-ea90-3665-ad6e-919a000e25d9 | -3.86817 | -51.41221 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9138643-2232-39fa-9934-485e99b0e75d | -3.86756 | -51.41609 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 748c9309-1deb-35de-a52d-ed7bdc0e9721 | -3.80557 | -51.13372 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c2971dc-88e4-3e30-b50c-ff221a39b5f0 | -3.72581 | -51.33025 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| feb5fbb8-c485-33b9-b90c-97f3787838aa | -3.72232 | -51.32968 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2655e11f-471a-346c-867f-2f9cc1716ce4 | -4.66359 | -50.94694 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7af911bc-0eea-388f-9a7a-64f1caf27b98 | -4.663 | -50.95063 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76d787f4-d583-3a37-b829-885ca8c14e0a | -4.66194 | -50.93533 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 185c98be-435b-33d5-b7fc-08f637916055 | -4.66076 | -50.9427 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8906d0ba-abcf-34ca-840c-e48268b3fa55 | -4.66018 | -50.94639 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e826121a-b180-3601-8469-e4e2d8775c82 | -4.65959 | -50.95008 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ded7f12-8f8c-368d-bf04-d10a81ac0fda | -4.659 | -50.95379 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7c0d347-43bb-38a0-b4a1-11801879c1f2 | -4.65794 | -50.93847 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3aa76053-f0cd-330a-83f4-ba398b78f49e | -4.65676 | -50.94584 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97d9342c-de96-3f75-a78c-ee7999400b8f | -4.65617 | -50.94954 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb439b87-2981-3f22-881a-79f5fd5c039a | -4.63688 | -50.93884 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fb21b79-4ed2-3441-ae4c-e1f8176f1886 | -4.6357 | -50.94623 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf1620ce-98fc-3308-bdf0-8251cb6535a4 | -4.63511 | -50.94993 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28cc0811-f55a-3613-85e7-8eb9ff2e8247 | -4.63405 | -50.93465 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13dd2767-56db-33f0-a026-fbc6b7516dd4 | -4.63346 | -50.93832 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db525d15-a59f-36b8-82c8-29cb178045ca | -4.63005 | -50.9378 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f6bd816-e85f-3b80-a909-3dadb253885f | -4.57052 | -50.95917 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| be08294d-176d-3a94-a34d-be264b26e814 | -4.56994 | -50.96286 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51abdbdc-b196-3ca9-9e96-9c132d81df42 | -4.56934 | -50.96661 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eccf3b1d-3fcc-3e27-a54b-f002779028a8 | -4.5671 | -50.95866 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ea93ab9b-f7e6-3894-8a86-c15fb9bb4d03 | -4.56651 | -50.96236 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fc3c2bc-5aac-3135-852b-989320ee14ce | -4.56592 | -50.96607 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 941281ed-60a4-3316-bf4e-30b9eb359e12 | -4.56368 | -50.95814 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea3fc70b-1644-3d29-9ac4-bb46b4bee4eb | -4.56309 | -50.96185 | 2024-10-21 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 016aeb75-474c-3c36-bed6-b2849a0ec550 | -0.59669 | -52.15821 | 2024-10-21 04:36:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6db7292-8d64-3ad6-8edd-b83a94077e50 | -0.59638 | -52.16021 | 2024-10-21 04:36:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c31ecaf3-d5b9-3b61-9acd-18fc2f51593e | -0.18301 | -51.54012 | 2024-10-21 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 56387ae8-ee12-3ac7-b234-8744cf1fea06 | -0.18233 | -51.54443 | 2024-10-21 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 22327e2e-07ed-309a-8968-1e59dc305cd8 | -0.17934 | -51.53954 | 2024-10-21 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 79ef8b92-d56a-3b2f-8be4-bce5be5c014d | -0.16994 | -51.55133 | 2024-10-21 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96e698ff-ff54-39a1-8210-c54fabd6a530 | -1.8015 | -52.05827 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e447fc2a-2a9a-37c3-bb8e-00e781d77f24 | -1.80081 | -52.06271 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c9dc4df-c7fb-3bf8-a17e-d4ad7bc61367 | -1.7867 | -52.05582 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d15750c-eed2-31ee-989e-6589a3c2cf6b | -1.76626 | -52.23493 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e45d232-9b72-3705-87fd-562542da1844 | -1.70055 | -52.69204 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ceda6326-0da3-37ee-ada0-876ede562770 | -1.63822 | -52.65065 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8f1aad1-3da1-38b9-b462-d13e3b8ba86b | -1.63746 | -52.65541 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f81dc587-1ee5-351c-82af-b2011a30553c | -1.63514 | -52.64528 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 941c9fdd-e63a-367e-9cab-83e2c825106b | -1.63438 | -52.65004 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7256bcca-fbbd-3b5e-a8e4-af205d86bf71 | -1.6313 | -52.64467 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b0fb0b8f-5799-377f-b272-4205fbccecce | -1.53215 | -51.957 | 2024-10-21 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5f6aacab-0fc7-34eb-aca3-314a4a419682 | -1.38677 | -52.28354 | 2024-10-21 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0248663-cfc6-3fd1-a711-c66a5b82399b | -1.13433 | -52.23842 | 2024-10-21 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 44431e01-7f45-336a-82e0-52ec7d2ee238 | -1.12606 | -51.92281 | 2024-10-21 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4fa771c-94a1-3997-adf8-f8500599785d | -2.02286 | -52.30657 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97ef0c8e-510d-3f78-b052-007c452a672d | -2.01941 | -52.12543 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 742e7944-b2d2-3ae7-bb54-4a9bf5bf7570 | -2.01803 | -52.12328 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1f70acd-1b92-3e35-a1d4-c1a1eba6a1d5 | -2.01732 | -52.12767 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 768c6ea5-5275-3856-9478-d6c68e113e29 | -1.98837 | -52.12953 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14734d93-2513-3427-9907-e514f0567c80 | -1.93486 | -52.10744 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 45889b2e-efe6-360f-a431-653efa930a8d | -1.93415 | -52.11182 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ef51ab29-8971-3f80-af8d-ff2fe0d0c38a | -1.93186 | -52.10244 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| dc8e60f3-51f1-31e6-b542-0fbc1df9c1d5 | -1.93116 | -52.10683 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b1c55b48-989c-3e98-8155-d5d4b3b20248 | -1.93045 | -52.11122 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4452b913-fedc-313c-b0d0-402c5507081f | -1.92745 | -52.10623 | 2024-10-21 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |


[Clique aqui para ver as próximas entradas](README44.md)
