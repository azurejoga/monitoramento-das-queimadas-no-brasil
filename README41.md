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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 704b5098-ee98-3753-bd83-4da4f1e9a949 | -2.50893 | -48.31251 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b395939a-4e00-3318-ac98-f4523a2f86d1 | -2.49706 | -48.06073 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2e5b837-55bc-36ee-809f-0d50316d6bf4 | -2.49652 | -48.06417 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 336b48c6-2ca1-3203-a2d2-534f5b33c3ba | -2.49598 | -48.06761 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3839d95c-47f1-3ef0-8622-8176039084e5 | -2.49484 | -48.05333 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ffb4df5b-a94f-3888-96c2-de6471faa887 | -2.4943 | -48.05678 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38db0249-186a-3709-9980-d23c9ec7cd43 | -2.49376 | -48.06021 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2489f189-aa4a-33cf-ac48-0ca8e9faa6fd | -2.49268 | -48.0671 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26c093c9-1433-3ec0-a478-942036735008 | -2.49207 | -48.04939 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e7e9c56-187c-3749-9b52-3ad101bcaee0 | -2.4513 | -48.48611 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3725c754-fcaa-3db5-9d31-30c07d58a4c9 | -2.44448 | -48.76595 | 2024-10-29 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d5e5eccd-7edc-3237-ba15-3ef23937891e | -2.4402 | -48.62128 | 2024-10-29 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 906cbe95-3785-300c-bc05-0083adc077e9 | -2.43703 | -48.66291 | 2024-10-29 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f955b6a2-acbf-3877-8905-fcd76f31137b | -2.43373 | -48.6624 | 2024-10-29 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47b3ac88-298d-392c-9756-c8b92080d40c | -2.42933 | -48.53514 | 2024-10-29 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8ba3e61-e503-37ac-89e4-8ebbc7793bb8 | -2.42603 | -48.53463 | 2024-10-29 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27822c50-7a4a-3478-bb52-b3429dfd6c64 | -2.41649 | -48.63845 | 2024-10-29 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70814384-6c37-3531-9df5-097dfab19197 | -2.41014 | -48.8767 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4cd52f6b-6414-3b0a-9240-c9dfcf1f929f | -2.40793 | -48.54235 | 2024-10-29 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 227036b3-02e0-34a4-b6c0-715c7e683a85 | -2.40632 | -48.55264 | 2024-10-29 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cebdb380-edce-3cf7-99c5-eae5c45a45af | -2.40302 | -48.55212 | 2024-10-29 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 168badd1-61f2-3ec9-b906-91fbd863945f | -2.4008 | -48.54476 | 2024-10-29 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09dd5ed4-6010-3c3f-ad46-1d5f4cba3963 | -2.40026 | -48.54819 | 2024-10-29 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d51baee-904d-38cf-994b-2800eb676836 | -2.39972 | -48.55161 | 2024-10-29 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e740390b-24da-3457-b470-80b7a0dafcd4 | -2.39918 | -48.55504 | 2024-10-29 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fcc6a5d-547b-33c6-8df8-417c1128280d | -2.39642 | -48.5511 | 2024-10-29 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 697439d1-231e-30a0-861d-0ee1ee3c74d4 | -2.39589 | -48.55453 | 2024-10-29 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 898593c8-aa09-3f7a-8b77-e1dd1101f161 | -2.39104 | -48.58536 | 2024-10-29 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7103b129-4fd2-38dc-8b8c-fed35ac79f6e | -2.37518 | -47.66666 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6abced40-2287-3c4f-a301-2f03152229e7 | -2.37186 | -47.66614 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01d22ffa-8c94-3e7f-ac56-cb5bd0d215c1 | -2.37132 | -47.66962 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00a3dbe6-5428-3ab3-874f-5335b4649015 | -2.36746 | -47.67257 | 2024-10-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ae6954a9-b07e-3854-987d-93bf63f4f918 | -2.32117 | -48.14254 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 044e5a86-ba70-381e-9fb5-0133a79f0981 | -2.30171 | -48.39592 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7afa1b8-4b1f-3758-849f-67e17d7d65ab | -2.30117 | -48.39935 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd80fc30-4d90-371e-82e8-e85529c08dbd | -2.29511 | -48.3949 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21c9d34e-c029-3d4b-affe-21dc92954ef3 | -2.28834 | -48.50262 | 2024-10-29 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8320bcd-fd03-3199-9219-39a3b08ba16e | -2.28504 | -48.50211 | 2024-10-29 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bec5ec6-e7f1-3608-b457-a077ae0b3e21 | -2.28204 | -47.91385 | 2024-10-29 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e53107b-b6aa-3aac-8fa6-e6924e5d0ca6 | -2.27096 | -48.07077 | 2024-10-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efe17e60-ef94-328a-8b75-0c887693f29c | -4.02086 | -49.0011 | 2024-10-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 472283a2-7ca0-3997-a737-dec97d4687ea | -3.85593 | -49.0948 | 2024-10-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa9fea54-8037-34c1-ba50-619f84e116ee | -3.81658 | -48.9796 | 2024-10-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a981162a-7279-3b1b-9419-85cad62d18ee | -4.18765 | -48.56677 | 2024-10-29 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9e20a136-8833-3335-ac30-0f340ba6f215 | -4.18712 | -48.57022 | 2024-10-29 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f57b254d-9dc5-32e5-9bfc-2d46ea9674d3 | -4.18381 | -48.5697 | 2024-10-29 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0ac91e7-64a7-3be2-83eb-3be6658dc214 | -4.10502 | -48.50752 | 2024-10-29 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 91ba0f13-7df2-30d9-9cdf-69f5a20b2676 | -4.10448 | -48.51096 | 2024-10-29 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6ead0640-65c2-37a6-95fa-5e67c9090767 | -4.10172 | -48.50701 | 2024-10-29 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2df9c6b5-1a56-30e4-99d3-c1784ed81dcb | -4.10118 | -48.51045 | 2024-10-29 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 263e7587-6504-3f06-9fed-68c49c5138b4 | -4.10064 | -48.51389 | 2024-10-29 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b5e57e42-2f26-3a47-970f-61c2c917a97b | -4.09842 | -48.5065 | 2024-10-29 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 065cdbb0-f036-3d76-aade-5205fbd634fe | -4.09788 | -48.50994 | 2024-10-29 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6bab8108-ba1a-31f8-9022-b6a514e0a8af | -4.22542 | -48.04058 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fc4354f1-aeb7-3c33-9466-a4ff8eae6518 | -4.22487 | -48.04409 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 20aec520-f074-36e7-9bff-e545021f9720 | -4.2105 | -48.04897 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f47ffd3-6704-3cbc-a0d8-f23784b17c61 | -4.20996 | -48.05243 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90120398-1400-363a-9243-529c7136875b | -4.20664 | -48.05192 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c656b15b-69f1-3e9e-98e0-ea7e09fe3466 | -4.14556 | -48.29126 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab1717c2-cf0d-397a-b2b9-15df9fef4fb5 | -4.14502 | -48.29472 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e2c7d03-df7a-3edf-a4d1-0398b6e09792 | -4.14448 | -48.29817 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9054348a-c139-35cb-992a-b9ff057b5659 | -4.14394 | -48.30162 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29b5d82e-a9fd-36ed-8805-b6483c2aa21b | -4.14225 | -48.29075 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a77cd0e1-d0d5-3f7e-aac5-62ec4e461a8b | -4.14171 | -48.29422 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f05959b8-510a-31a2-9fa3-5ae9d6132d8c | -4.14117 | -48.29766 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f38187e6-44ed-3077-866d-670306c68fc2 | -4.14064 | -48.3011 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7426672-0293-37b6-9b75-43caa59294f2 | -4.13733 | -48.3006 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf7761ce-6e31-3636-97c8-652eb7902f95 | -4.13717 | -48.25808 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a80365c0-45d3-3661-990c-67b75f05f564 | -4.13386 | -48.25756 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0904fe1-7fa5-323d-9453-8f56a708ed7a | -4.13017 | -48.30304 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 30d99510-d650-3607-8dd9-96ab82778f37 | -4.11296 | -48.23661 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b76b1130-4cc4-367d-86d2-eda4b2dd652d | -4.08173 | -48.30614 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| eb6278fa-1268-3185-9d7f-128818d06af6 | -4.07235 | -48.30114 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79d2df23-5b91-3ce8-a2af-74478b93a9e5 | -4.07181 | -48.30458 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 225c81bc-0853-387a-b55d-0228f8c73e2f | -4.06904 | -48.30061 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b396c75a-d80d-3bbe-bb17-e3e89b939f2f | -4.0685 | -48.30407 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5615c5f-6bc7-3fca-b824-7d48fc9d0d4a | -4.06681 | -48.29319 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3dd95bc-1b01-37ba-bbd2-1e590d5a5d25 | -4.06627 | -48.29665 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69738293-1eb7-38fc-b316-a28e05d21e8a | -4.06573 | -48.30009 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06448d98-fd01-3c44-8d50-9b9a8a4001ed | -4.06351 | -48.29267 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1e88e0b5-b0d9-3175-97a6-351b70f06365 | -4.06297 | -48.29613 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 35a0325d-eb8a-382f-8fee-dc41b344af3c | -4.06243 | -48.29958 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0578b666-79c8-3a90-a196-9abe6f1eab88 | -4.0513 | -48.10985 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0977ae6f-1039-3441-bf62-c72a278a5fb3 | -4.03103 | -48.30531 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8eda42d-365a-3911-8a35-c5fa9eb9759d | -4.02826 | -48.30135 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00b5047b-77d2-3734-bfc6-f347d7177d79 | -4.02773 | -48.3048 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bb1173e-35e0-39f1-83ea-756f87be5c0f | -4.02549 | -48.29741 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bee17d74-16b1-347e-bf2f-a9f303a36aa0 | -4.02496 | -48.30085 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e88fef9d-a900-3a75-b454-c6280be04af7 | -4.02165 | -48.30035 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93d71ce9-9a74-3b8f-af15-a9f680027bb7 | -3.93659 | -48.34358 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f0a1364-3251-343d-b0ce-51797fc72818 | -3.93328 | -48.34307 | 2024-10-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e400d605-45f8-3cc5-af4d-f114057d8bb9 | -4.11288 | -49.08645 | 2024-10-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4a8475b-262b-3975-b09b-ae19b042550e | -3.9032 | -49.0777 | 2024-10-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 07bae5cd-41f8-30be-b5ce-9ea1afe773f6 | -3.83667 | -48.89479 | 2024-10-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| c1395020-1bf2-3dee-8947-3b370f852647 | -3.83223 | -48.88004 | 2024-10-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 04f0d1ab-2a6b-3033-97a7-d433036f49f0 | -3.83169 | -48.88347 | 2024-10-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c8250cb1-4970-335b-9bb6-928e5ec88909 | -3.82509 | -48.88245 | 2024-10-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a4571d3f-c2dc-353b-a3b6-b44bda1efb42 | -3.82455 | -48.88588 | 2024-10-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2bf3b00e-7114-32e0-8976-f7bd1d97bea7 | -3.82401 | -48.88931 | 2024-10-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2538339a-6f3e-3c52-824a-04e33520a30d | -3.82233 | -48.8785 | 2024-10-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README42.md)
