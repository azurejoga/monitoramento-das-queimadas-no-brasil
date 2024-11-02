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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80e04e66-7012-38ba-9025-32398b009659 | -3.25357 | -53.34047 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34be6d0f-4365-307c-b294-afd1e0875350 | -3.25322 | -53.41525 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cc37136b-8313-30c2-9525-b7a9b6ec764f | -3.25244 | -53.41991 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 8d7d6dff-18f2-30f0-8095-3f45e52aa8ea | -3.248 | -53.40953 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c8ef9096-0c9b-384b-80e6-5d3ae24283f9 | -3.24758 | -53.33946 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 537cbc87-65dc-3fee-b3dc-d53ef51ad8a3 | -3.24721 | -53.41418 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 48d594e0-e9f0-324a-869a-299cf511bcef | -3.24197 | -53.4086 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e5eccd7d-b288-38b5-a07e-b6bf2d7bffbd | -3.24117 | -53.41329 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 36bed20e-7c3b-3962-b301-c501a1b7dd0a | -3.23696 | -53.36553 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b7563732-89b7-3143-8a19-b1adaf3e3656 | -3.23619 | -53.37004 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fb6a8a97-a4bb-3785-adc2-2c339ca19514 | -3.23593 | -53.40773 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a0cef9cb-a694-38f0-b4ed-196ac7639764 | -3.23538 | -53.37477 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e9c9e839-8ea0-307f-99c5-afedf90e4b2d | -3.23513 | -53.4124 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 64ad7e93-e7f4-3767-a6a0-7d511ece9efd | -3.2302 | -53.36892 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a8a5c222-5fb5-348a-b1e9-31d76f0aa84a | -3.2299 | -53.40679 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9be255d8-28a4-335b-b281-708de9924e26 | -3.22941 | -53.37353 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ff6398e0-3a94-30d1-91a6-cd515bf145b9 | -3.2291 | -53.41147 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 204dfc8e-fb75-3575-b40f-ead6058add92 | -3.22469 | -53.40106 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3c7c6814-5fa2-3564-a1fa-c44bc1b9d349 | -3.2239 | -53.40565 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c61cd116-debb-3b05-a24f-684ad60a2d6c | -3.22314 | -53.41013 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a114e57a-b58c-3255-85a6-b34a89424e4d | -3.22254 | -53.40187 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7a9bbb57-f998-3a59-ae93-d15378f9badc | -3.2218 | -53.40638 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15ecf2c1-9df2-380e-9e8e-36a5c529c7ad | -3.2187 | -53.39991 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 798ac674-4c1d-31a8-a2c2-ef14f4a14a26 | -3.21794 | -53.4043 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a4474bad-5daa-31e9-9851-87b53db7caab | -3.21658 | -53.40047 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a27bdbf9-88d6-3d5b-aa44-c9f4588ae2fd | -3.21586 | -53.40483 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c081b93-73eb-3600-80eb-def382ef59a3 | -3.21569 | -53.41743 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 36934351-4514-324d-9803-98cafd105dd8 | -3.21515 | -53.40913 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f29ed4ad-566e-3840-ac19-d5d3f080c3e7 | -3.21369 | -53.41803 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5f8b0c34-1173-3f73-97d9-f8fcaedc6636 | -3.21126 | -53.40714 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5cdd1b03-989c-32db-8c3b-f4decd6f6b17 | -3.21051 | -53.41148 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3e1ed8f1-427c-326f-8868-d5d9d2b5582a | -3.20974 | -53.41597 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 13a2ba3b-abbc-3c26-8394-7bc7ad8d3446 | -3.20918 | -53.40784 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8119ff99-39bf-3376-86f9-705ee280cc84 | -3.20896 | -53.42051 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 41390d6d-fc5d-3ed0-9647-58532fba5d52 | -3.20845 | -53.4122 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 375c312e-1742-3d1b-84c2-38241e693885 | -3.20772 | -53.41666 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 44fa555b-dfda-351a-9312-642f50c44563 | -3.20697 | -53.42117 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 9ddd0ad8-6372-3152-afdb-2ba4c1d94bcd | -3.20524 | -53.40612 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2a7b8642-d72f-3f5c-a2a5-a9f439abcc45 | -3.2045 | -53.41045 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 519aa62d-aa35-3dab-95a9-6de991478b86 | -3.20374 | -53.41481 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0b812b53-4cbf-3bc7-8d56-c09cf8267bc9 | -3.20316 | -53.40681 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1969b6e0-4034-3b8d-832e-a44dc4b52b9f | -3.20299 | -53.41917 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 18ac2c90-17d5-3578-836a-18b7cfa11469 | -3.20244 | -53.41115 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6e257c3b-aaae-3a99-b041-3f03c5a428e4 | -3.20171 | -53.41551 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cf937162-a590-3ed3-871e-f110d0d0ff3b | -3.00887 | -53.44627 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc9ac10e-7c23-30bb-a41a-3115431ae95f | -3.00285 | -53.44503 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a19c51af-1684-3b53-9d19-651baf1b432d | -3.00205 | -53.44975 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9665138-c2c8-378e-b154-bda796c884d1 | -2.96537 | -53.28915 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87e7bc5e-191b-34a7-919d-6528273570f5 | -2.95937 | -53.28817 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9318aab5-11a9-398e-b8b1-e51eacd110a9 | -2.95864 | -53.29253 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 994eaa5b-2753-34af-a6ee-4c81b7a78470 | -2.95262 | -53.29161 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d85a21e7-7f74-3ae7-aa6a-642c31f72765 | -2.94661 | -53.29071 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23f6f510-26ab-368e-813a-8a106dde7221 | -2.94587 | -53.29504 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7eb5c7b2-a0a6-35d9-a6f2-ab3ae0e1d4cc | -2.85431 | -53.35061 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3e1210da-84c3-3ace-a5a5-5febaf1d7205 | -2.84829 | -53.34949 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 241725a5-f51d-30cd-8527-47e0f0867cca | -2.36755 | -52.0229 | 2024-11-02 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b3a0be5-0f69-3aa4-bba4-9cbc9bb6775c | -2.36336 | -52.02188 | 2024-11-02 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13833cd4-880c-3faf-baf1-d6b8629fd32a | -2.36197 | -52.02198 | 2024-11-02 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58581039-a04a-3e72-9fa6-77fe127cbd6b | -3.5116 | -53.01443 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7bc662a-30f5-3289-945b-40eaf4800a61 | -3.51083 | -53.01893 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4183db4-6231-32b0-9134-9dd4e6954bc3 | -3.50571 | -53.01372 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6795c25-4cf3-3003-82b9-5cec2f0854bd | -3.50493 | -53.01826 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4deb9c7d-8355-3c25-8284-05bef6d6eed6 | -3.31143 | -52.85988 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1660b4e6-a521-38dc-8ecc-93fa1168f29b | -3.31075 | -52.86401 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1e9d4f94-dcee-3b62-9c15-e3b01266c3bb | -3.31075 | -52.86359 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 44f5fde2-54de-3a4e-81e2-0d0967c268db | -3.27054 | -52.8188 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69240de9-27be-3d57-8a04-41ff120dedd4 | -3.25292 | -53.06921 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8fa78a0-c186-348d-b701-ab543bc54ee4 | -3.2522 | -53.07351 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2056406-9c80-3c35-878f-f86a439ffda1 | -3.25141 | -53.0684 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d95edf5a-54f4-3370-acf5-b9389ed651b9 | -3.25067 | -53.07267 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5616d957-d612-354b-8ee8-e629e135018c | -3.24992 | -53.07699 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 45e1d1bf-8eb4-39f4-9134-2f3fb20e1839 | -3.247 | -53.06838 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7f6ec79-380e-32f0-a68b-a41ae2cc49fb | -3.24629 | -53.07264 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e6ccc03-9297-3d50-b8b0-426983340ec1 | -3.24558 | -53.07696 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6cee6c46-074f-3097-aa5b-fee16c091be9 | -3.05763 | -53.15996 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f078497e-075e-3b9f-beb4-4640fdbe6635 | -3.05688 | -53.1644 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 083469bd-307f-3993-be21-03aaa7cb64d3 | -3.0561 | -53.16897 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ef522d6-082e-316f-b19e-d5e164cb04f7 | -3.05094 | -53.16335 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 063d8aa5-b8d0-3359-af19-9182215e49c2 | -3.05018 | -53.16785 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d24d64b-5e2d-3d36-8aec-2835764cfc38 | -2.99333 | -52.37582 | 2024-11-02 04:12:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7cf83335-49a2-3f53-9146-b26e9b919b76 | -2.98593 | -52.91467 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 63efbca0-d876-318a-8100-b0bb75c66e42 | -2.98521 | -52.91893 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| afdc2690-5aa2-301d-9d0b-05927a4c76af | -2.90746 | -52.59935 | 2024-11-02 04:12:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc640685-a81f-35f1-932f-e3f252be308f | -2.87731 | -52.89392 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e8d64e3-6afc-3e49-96cd-44511d063a0d | -2.87637 | -52.89323 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c431e96-9908-30fc-b6eb-528ac2b94fbd | -2.87567 | -52.89734 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 904cd45f-a6a1-31a1-a22e-442ce542160e | -2.87145 | -52.89298 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3143aa49-9580-3481-8c65-bbbada5438e6 | -2.87076 | -52.89719 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9148bba-8051-3ebd-a827-f93cf683fbb9 | -2.87051 | -52.89229 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d56696f-dbfb-3851-9a99-ef49cac1bbdb | -2.84939 | -52.41914 | 2024-11-02 04:12:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2165da8b-37e8-3939-911a-e4e7896950cc | -2.83833 | -52.87482 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f121aa0e-b199-3cb1-bcbf-28746ef81ee1 | -2.83766 | -52.87888 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 72254ee2-ef6b-38cc-a3c6-aca0892daed5 | -2.83696 | -52.88309 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3d265848-e4e3-3bff-9c6d-21c372211174 | -2.83247 | -52.87391 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c79164d5-ed20-3834-89de-b3e476cbf7d3 | -2.83178 | -52.87803 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| afc323a1-35df-3450-b02b-0b2529ec080e | -2.83108 | -52.88227 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 007b35c8-19a8-32e6-95cf-650906504f80 | -2.81201 | -52.9973 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2dcb2e0-3c24-37e6-98a5-eb8f321b5a4e | -2.81135 | -53.00124 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2bcdaf0-4ef8-3b5e-bd64-c2f9adbcce6d | -2.80613 | -52.9962 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 439c68f3-3042-37eb-8cac-010f9a5c971a | -2.8055 | -52.99995 | 2024-11-02 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README52.md)
