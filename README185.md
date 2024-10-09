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

## Dados Diários - Página 185

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25435e88-1025-3c70-9adb-76cd8ab7696e | -12.87723 | -62.79364 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5d6c7185-837f-3ea0-99cb-f13b4cbe8182 | -12.87655 | -62.79746 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 580607e8-cc93-394a-99d9-2450f630e486 | -12.87627 | -62.44731 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fc925e2-7e59-31e4-8158-ce10053eff55 | -12.87586 | -62.80127 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 94bf7d9b-5454-3d9d-9b3d-6e8f9be6a68e | -12.87173 | -62.8005 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 284cbcdd-0617-3778-b463-b18bf9191121 | -12.87036 | -62.80814 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 506d9e89-ef52-3afa-bdac-3aad9e020f98 | -12.86623 | -62.80737 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f06d1114-9a9c-3983-a06f-8eb7a46d3ac2 | -12.85796 | -62.80582 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 830e8a99-d023-36b0-8d0b-2855fc3fea38 | -12.84494 | -62.483 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fc44aef0-0806-39aa-a736-8685b7cab5fa | -12.84486 | -62.80735 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| adfcb976-40a5-3018-b3ca-ce58e2935564 | -12.84003 | -62.81041 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3286070d-0e89-3090-96de-623604095ff8 | -12.83659 | -62.80581 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2776b1e-a942-39d1-a82e-fb2f83204c2c | -12.82739 | -62.90359 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c594c8df-dd6b-37d8-b60b-ad04323cb7be | -12.8158 | -62.45866 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d277dfca-1699-3818-bcfa-2f5c66074b92 | -12.81515 | -62.46233 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ffd91299-00a5-3bac-999d-58ac47c49ff4 | -12.81449 | -62.466 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ef215a8-8cb9-3c6e-af1d-44e5b7ce9341 | -12.80848 | -62.4762 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d9bc5a36-a73a-37a0-ad7b-69e0afc6bd75 | -12.76507 | -62.76544 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79a88c4d-8d9b-3156-a0e7-82d545e820dc | -12.69458 | -62.93663 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b55a718-b374-3d26-aa7a-6763c120b61c | -12.6904 | -62.93583 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b9b010e-01f4-3c88-aae2-260d9d601101 | -12.68971 | -62.93976 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51feb878-9ccf-3f3a-9c0f-48120829c9d3 | -12.68902 | -62.9437 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ab5fabcf-fbe3-3a58-8823-efbab22993f0 | -12.68833 | -62.94763 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ffc3c12d-925d-395b-ace6-789af8386b54 | -12.68484 | -62.94288 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| db30786f-7465-3261-a43f-59272c7f4483 | -12.68414 | -62.94682 | 2024-10-09 05:04:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 88f3bb40-3fd3-3ee0-9d22-9706b97f0000 | -9.38457 | -63.41385 | 2024-10-09 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fdc91313-02db-31c0-9796-8a54f69e766d | -9.3837 | -63.41867 | 2024-10-09 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d8cef6a4-9aec-3427-9def-da2de2fb7f86 | -9.31508 | -63.74729 | 2024-10-09 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d92de59-bee6-3866-bebf-0992b6364e87 | -9.2916 | -63.21492 | 2024-10-09 05:04:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6a95b57-5b50-34db-8d64-1d9dd78490d0 | -9.25323 | -63.41058 | 2024-10-09 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5ba8a79-c16f-3bef-bd38-e55f718a334f | -9.05336 | -63.23545 | 2024-10-09 05:04:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2f408d0-1dbf-35e2-ac58-e667535848f8 | -9.05252 | -63.24011 | 2024-10-09 05:04:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c0b87093-6f78-3789-ae12-9745d47e2ab1 | -9.05228 | -63.23787 | 2024-10-09 05:04:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e2315f72-ef98-3533-9f8b-9c6d248b18f0 | -9.05147 | -63.24255 | 2024-10-09 05:04:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5afc161-ddf5-3255-a93c-d90a21489bd9 | -9.04774 | -63.23705 | 2024-10-09 05:04:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d8bc0670-6067-3c93-8dd9-69bbd0ee0087 | -9.04693 | -63.24173 | 2024-10-09 05:04:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eee1e607-238c-337c-a9d3-e58aa98f253a | -9.03331 | -63.23926 | 2024-10-09 05:04:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88097d33-86ea-343a-b105-9a71829841de | -8.76721 | -63.22567 | 2024-10-09 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6d3c596-9ea0-3f07-9340-2ff5f27536fe | -10.64413 | -64.54414 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f915c1f0-1114-3db5-94c8-3e034279ca1c | -10.62438 | -64.4341 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e5785d1a-2895-31ca-b070-c3bab957fd2a | -10.62334 | -64.43979 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d9f3b7ee-109f-3c00-802e-f35a9d5b644a | -10.62051 | -64.42819 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd8bacbd-ce87-366e-8bd2-3446ecbf69b6 | -10.58537 | -64.40415 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06f7d15d-0d8e-35d0-874d-5d1e8616bb3f | -10.5699 | -64.49341 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 43374a07-b78c-3787-8d46-0d6bf1bde90a | -9.79487 | -63.89482 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8a1a8f4-ef00-3b7e-bf84-a70506f3a0b4 | -9.72978 | -64.23466 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c6c3a47e-f142-36bc-ab2d-a492b723bbf9 | -9.72403 | -64.23914 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 47e180ab-0d9d-3f64-89cb-e9826dac7db2 | -9.57889 | -64.11309 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cb70840-410a-310f-8de9-fa036adcf3ac | -9.57413 | -64.11216 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bfc0204-2cfa-36d2-bcc1-434bdc943078 | -9.56984 | -64.10973 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a79f0bfe-3ad6-397a-96d5-ad8fc5a76e6f | -9.56938 | -64.11118 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f53c523b-2695-3610-9562-da01327a2641 | -9.56893 | -64.11494 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0938957d-8436-36ba-9082-5751727768e1 | -9.5205 | -62.93211 | 2024-10-09 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7938152d-b419-338f-9987-fbdfcf7a2bad | -9.52002 | -64.05744 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4850063c-b9f6-3b7b-aae1-84c417a03bff | -9.51974 | -62.93649 | 2024-10-09 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf35b46f-549c-31a0-bb02-94f4e4c634fd | -9.40259 | -63.66101 | 2024-10-09 05:04:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a2a298f-f345-349b-a8a8-a7eef7b7e82d | -9.39883 | -63.65514 | 2024-10-09 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e36d9289-a192-3478-87c5-3711a76a6cee | -9.39795 | -63.66018 | 2024-10-09 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c1e0f93-8112-3903-9017-e90388c38ec3 | -9.36167 | -63.81142 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0aac7ed2-ed12-3982-897b-230760c51f3d | -9.36084 | -63.8161 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1e348c7a-2230-3efc-bd01-126e945935c6 | -9.35614 | -63.81526 | 2024-10-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fe4ea83-0f12-377f-b662-97a42a77f55c | -10.71301 | -64.16133 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad9992c9-25e0-3694-a77c-d3acdff9c0d3 | -10.70924 | -64.1553 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ca9e7f5c-8bec-309d-a316-373e3ad9327d | -10.70827 | -64.16075 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a5fefb7-7787-356d-ab57-0fdc887fcb2e | -10.70456 | -64.1544 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0a4cac7-6d2a-3c59-8224-a873813a25d5 | -10.70427 | -64.1291 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 343bab45-0c31-3555-9bcd-da570f66bf77 | -10.69792 | -63.63887 | 2024-10-09 05:04:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e44581a9-c3b5-3f2c-a2a4-233c831dfcb4 | -10.69704 | -63.64383 | 2024-10-09 05:04:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d0c15c8-4369-3f5f-81e0-e21ede61524e | -10.69255 | -63.64276 | 2024-10-09 05:04:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 012d4138-56b7-3521-9d15-ca878ebffee1 | -10.69167 | -63.64773 | 2024-10-09 05:04:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 930c0420-24a3-3d1a-a624-8ee1a01f80e8 | -10.64794 | -63.97335 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 815fa90a-d56a-3bb6-9990-23331a7b7490 | -10.59457 | -64.02967 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a8151f42-907f-383a-a5d5-f653284ddd93 | -10.58996 | -64.02852 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8357dae7-ec89-3f8f-a0cc-56869df0101a | -10.58911 | -64.0332 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ccc3c5a9-05d3-3eda-8e9c-ac1c30a7ad31 | -10.57808 | -64.04079 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 73ab70a3-28a0-3762-8f4a-3b9b9c405a6b | -10.14034 | -63.67154 | 2024-10-09 05:04:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bff53b79-9798-32f0-b768-fc9144f9f939 | -10.13486 | -63.6757 | 2024-10-09 05:04:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43e7f993-937a-31f4-8703-5564cb71cb8c | -10.88899 | -63.91748 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3842098-aa42-3486-a0cd-c34a047f28e5 | -10.88857 | -63.91449 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9d9f8e9-e4c3-371b-97a7-e4458f9e92c0 | -10.88814 | -63.92226 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a03463bf-f48c-31d2-bbd2-feeab7592a17 | -10.8877 | -63.91916 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 90060e45-b4b4-3d54-864f-a33cdbba1192 | -10.8868 | -63.92403 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 32073833-02b8-3c5f-ab44-18ca7ff4af00 | -10.8844 | -63.91653 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d1e08ab-9641-3bca-a17a-b4a95083bed9 | -10.88356 | -63.92131 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 14fbf564-ff68-3cc3-b6aa-1d30747dab4d | -10.88311 | -63.91828 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2a7f9b5d-1ef5-3973-8580-63750663ba8a | -10.88266 | -63.92635 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d4f68028-a79f-3c1f-92b2-d58fce06498b | -10.8822 | -63.92315 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8d3e20f2-e364-35cf-a2a1-d2b54fb50031 | -10.88127 | -63.9282 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3bee604-9e26-3d19-9cc7-448478880c1d | -10.8798 | -63.91567 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f88d738d-6650-3443-961f-5beab1e3c744 | -10.87895 | -63.92044 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6a19f5b1-56d3-3acb-83e7-fa26827b2daf | -10.87806 | -63.92549 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b509e1f8-b97e-3f31-9d0b-91a864c223e6 | -10.87603 | -63.91015 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d63a8990-dbf5-3c09-9a00-3dba1c78f987 | -10.87344 | -63.9247 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 175ae71d-c8d2-3f1c-9548-44cc48ef7fa7 | -10.87251 | -63.92994 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf8b830b-0245-3d74-b068-c8ec8d788bf1 | -10.87218 | -63.90513 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 2d04dbbc-2636-315a-af4c-f9b16db47810 | -10.8714 | -63.90944 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5eb8ed04-8f82-3fd3-b585-59e5d81654cd | -10.86883 | -63.92384 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc49bab5-5847-3605-9ed8-0979d4161515 | -10.86838 | -63.8998 | 2024-10-09 05:04:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6f270888-e8a7-3bad-b399-9e615298e37e | -10.86753 | -63.90456 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 65510cad-b5d8-300b-b11b-9d866c0f959c | -10.86674 | -63.90894 | 2024-10-09 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README186.md)
