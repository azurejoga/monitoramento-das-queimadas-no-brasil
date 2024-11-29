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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6dad820-ad0f-30ca-9b16-0a421a82a517 | -1.68003 | -52.4282 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23760054-02a2-3c09-b68b-2e8764caac2a | -2.03245 | -53.50173 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5f5af8dc-529a-3e71-bb8e-75eab5d5a39b | -1.58829 | -52.28423 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4b7b0d3b-7613-317a-8549-c8364367416a | -1.25139 | -54.54465 | 2024-11-29 05:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06387548-6b61-3d82-8c12-6134c1d50ec9 | 1.97771 | -60.91625 | 2024-11-29 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34d36382-049b-352b-94a8-5a5a3eee7f91 | -1.19096 | -53.87631 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7ef35d47-8caa-390f-a362-dc68a89388e0 | 1.28109 | -55.92163 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 088d1236-dc00-304b-82e6-f32b7518780e | -1.20166 | -53.72083 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 63fcde98-936c-3d15-9a60-63f783ab9995 | -1.15638 | -53.58098 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7cc2fafe-0ecb-35e3-a816-3ff7c631edc0 | -1.15569 | -53.58543 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6c36a17d-5771-390e-9149-7d710fee730c | -1.24271 | -53.36293 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0bbb01f-5ec3-3e46-818f-0d5fa5b67d29 | -1.2203 | -53.55486 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 60df0623-b98b-39de-81ec-60a121f0b347 | -1.69297 | -52.43688 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6cff0ef-d760-3418-8bdf-411d0aa93f09 | -1.70355 | -52.64869 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bcb02a0d-78b1-3e0a-ac5b-15f0880671a3 | -1.19738 | -53.87673 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5ceecb3c-77c8-31f4-b946-2e3c9b21f23b | -1.21354 | -53.55362 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9572759-8a1c-32fe-a3c1-225b0410a38e | -1.59431 | -52.29197 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f916ff83-f28a-3102-b289-cde0c46d8c8b | -1.35025 | -55.00782 | 2024-11-29 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d50f0be-5b54-37ba-9de9-c8646da0c2aa | -1.49598 | -52.43676 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71e3e7c4-486b-37bf-8228-69f34550e097 | -1.24476 | -53.35642 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45edd4a9-e32c-31ee-b38f-aa7120c9a1aa | 1.22925 | -55.94001 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04b67e66-96b9-3df8-a464-8b6633d6d0e6 | -1.42615 | -54.30567 | 2024-11-29 05:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9dcdf9d6-3d54-3f93-bd76-2ea99bca76f9 | -1.67308 | -52.42712 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c5a35a3-78ac-3a03-94e3-795b07f23c29 | -1.71294 | -52.49317 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9e83a64-4f7b-3cd0-b096-48c941af9be9 | 1.2115 | -55.95411 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c682f624-e121-3dec-b6b5-ce34889aedde | -1.42682 | -54.30129 | 2024-11-29 05:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ff13267-f989-342b-991d-56079d04b593 | -2.50474 | -54.16658 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b5d8900-16ad-3932-a11f-528e92983dac | -1.98877 | -54.90126 | 2024-11-29 05:44:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8eba1854-e640-35e6-9771-eae118139450 | -1.71234 | -52.63708 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 64a1e2f8-c188-3756-8ba7-3780394f6d24 | -1.60131 | -52.29306 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d2a5ed8-d183-30d8-9857-28d38356bbda | -1.69287 | -52.44175 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 04e3ea79-600c-3523-accd-4322d6a04c18 | 1.21468 | -55.97438 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4e1e1521-5d3a-301d-aebf-9eebf68f1289 | 1.97393 | -60.91684 | 2024-11-29 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd2f9a34-ad96-383b-941e-ae0c62b70dda | -1.57979 | -53.84937 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9fdfcd9d-5b34-349c-b3a7-4e9189e5019b | -1.43956 | -55.16043 | 2024-11-29 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64a45aa6-8311-31a6-8b2f-a095501864e1 | -1.72147 | -52.48594 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a6a42500-6deb-374f-b4da-55b94b2974ac | 1.22871 | -55.93667 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28b8c996-57c5-32d4-9822-b6c1e7eaa14e | 1.20586 | -55.9643 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1b25f5d-0670-3d79-9c4b-437eacc80535 | -1.21279 | -53.55835 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6abbffa2-d10e-3626-87e4-980f49f45ae9 | -1.16804 | -53.67505 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c372870-6f5f-329c-b075-53183ee9b2e8 | -1.69779 | -52.4558 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 350f2163-12bd-3f9f-9371-2438fad667ff | 1.25808 | -55.91492 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b645b269-5511-3f4c-a409-40b16da3c118 | -2.59748 | -53.98124 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e88e4ba-34e9-36fd-aa73-ba4633c04523 | -1.21298 | -53.55954 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 008f60de-32ca-309f-a4ef-5daed1aa1f9e | 1.28751 | -55.92752 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbbbe0d3-7037-3f5d-b0d9-a74887f35332 | -1.3056 | -55.74857 | 2024-11-29 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba5bfc55-dd1b-3728-a40d-3f2bfb2b87ca | -1.09665 | -54.13024 | 2024-11-29 05:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ed7b499-6848-3845-bbab-918253f1a098 | -1.63678 | -53.87263 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6c320bc-529e-37fe-ad4a-285dee6903be | -1.4271 | -55.28033 | 2024-11-29 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbb66076-9e27-33bc-a100-886705d25c60 | 1.20934 | -55.97519 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0fc5a4b5-bf08-34bb-a95f-e0cce7466da1 | -1.69764 | -52.64132 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b658dc97-9a4a-3d4a-b657-1a6a046af11b | -1.71987 | -52.49424 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3af258d4-13cb-3467-8e6a-abd50718eb06 | 1.21911 | -55.94502 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 482315e1-8cd7-3222-b498-54ad770cebeb | 1.20721 | -55.96167 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4619501d-7f9d-3d6f-90cf-7e970fbb388b | -1.53121 | -52.66521 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2a81c43-4bb1-32b9-8236-c64ffd8003fb | -1.53805 | -52.66627 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 31e15fa8-e092-39ab-ae03-2a3f2192381c | -1.32403 | -55.83757 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf4b1477-05d2-3a94-adfc-921ca9ad6ef2 | -1.16902 | -53.67665 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df034f41-6d76-39d3-801e-0d703569ab15 | -1.59015 | -52.28484 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c9b37772-bbd5-31b5-8c41-8332efc2f437 | -1.5814 | -53.83905 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 27cb0f00-42b1-3d9b-a311-1e9252a003aa | -1.60033 | -55.42987 | 2024-11-29 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddebe52d-7294-38f0-acef-4270f2845c5c | -1.36029 | -54.65981 | 2024-11-29 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e0ac6962-667b-3ec9-a992-cbd8dd630f47 | 1.21287 | -55.97364 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bdef1450-8a71-31b1-9e88-a79f7d412475 | -1.53182 | -52.66544 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5af57f23-495e-3757-acaf-8545f9df5382 | -2.59185 | -53.97501 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb7c5bf1-a97b-3984-a515-34866946c8bc | -2.25414 | -53.74681 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40065f74-89b8-3aa5-8d44-654acac1ed99 | 1.22446 | -55.94419 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b9d07da-2133-3bf7-980e-d3612e432862 | 1.30435 | -60.4146 | 2024-11-29 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42211ede-b907-3daf-8b6c-706e6fe69633 | 1.20987 | -55.97857 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fe8e8b4b-0576-3d97-8e53-869f3a408ea4 | -1.16066 | -53.55339 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd055551-fa7a-37b1-8b7c-77f6a3af8b26 | -1.68098 | -52.42663 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 13f9bc2f-8691-30af-9d4c-998eea67ca49 | -1.6988 | -52.4493 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| c1ca08be-f273-3657-89fd-bd3bd838d7f3 | -1.58323 | -53.8382 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 1aa67a62-72e4-3138-8e07-5da30e8ac9f3 | -1.59612 | -52.29254 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5c6c67df-115d-32a1-9740-1f133207f6b2 | -0.26962 | -51.63375 | 2024-11-29 05:44:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49cc4d85-2a82-3802-ac79-adb39169bad1 | -1.16289 | -53.58157 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7f66f535-f9fa-3a4e-86c1-316a4f7e7899 | 1.20774 | -55.96504 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f652c8af-2221-3540-911a-d8a0928486cd | -1.36099 | -54.65511 | 2024-11-29 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c992df4c-0964-3f18-9831-c11f61923bf5 | 1.21033 | -55.99138 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bbdc2ad8-a5e3-3a0a-8784-e496bfa8fcdf | -1.72182 | -52.4813 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4562a50e-0a3e-3ac0-9992-b31db72b5c21 | -1.9137 | -52.88975 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2e54603-be38-390c-a2d6-01ebe941ee77 | 1.21342 | -55.97701 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d38522b-a15f-3ae3-b24a-9186e32572f9 | -1.25786 | -54.54779 | 2024-11-29 05:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d74b99c1-03f1-312c-b86a-bde5af65ab08 | -1.59971 | -55.43391 | 2024-11-29 05:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9798c718-c9c5-31f7-a6b1-e5722ba95844 | -0.27078 | -51.62669 | 2024-11-29 05:44:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb912e6c-5d16-3b73-a0a5-3b9c50a014db | 1.20614 | -55.98962 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5100c80-fc82-3baa-a76f-e82981f9dea3 | -1.07933 | -53.64435 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4723829e-c778-342b-85b1-aeebd81e01a7 | 1.21255 | -55.96084 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6154a82a-b365-36e5-b397-f211ad48cd39 | -1.20683 | -53.72003 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 649a5cec-b610-31aa-a8d2-37ba58f6725b | 1.21543 | -55.95596 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d3247da8-9851-325a-9f4c-641edb9311e1 | -1.67403 | -52.42558 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 857a25fe-4d16-381c-9135-2794887653d1 | -1.63112 | -53.86695 | 2024-11-29 05:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 784ea338-875a-3578-8076-99d2b653c5c9 | 1.25754 | -55.91154 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fe43870-89ed-3a63-af31-a7717c28504e | -1.91955 | -52.89691 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c233f73c-2f59-3ea9-803f-a64274e4e62f | -1.697 | -52.45751 | 2024-11-29 05:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| d18c536f-803b-3534-94eb-23ac39536992 | 1.20641 | -55.96769 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efc4c824-5c5a-3a20-8652-836f9b6bf996 | -0.27277 | -51.6338 | 2024-11-29 05:44:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14a13c30-a5e3-3a7d-9e2a-bcb473b04ba8 | -1.53866 | -52.66653 | 2024-11-29 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 910fa64b-b822-39d8-9257-061bc63d7d04 | -0.56411 | -51.70709 | 2024-11-29 05:44:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eeac8e77-af3b-3462-ba61-77eb5e3dc05a | 1.2112 | -55.96351 | 2024-11-29 05:44:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README105.md)
