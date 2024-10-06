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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b329bb6b-8f50-3fa5-93a6-f8b7ae8a9905 | -17.09638 | -56.80582 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3488d1e9-1bc7-32c3-9aac-ac5fdcfc79c1 | -17.09423 | -56.8164 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f322b3a6-b97e-3065-9b82-a3c0c03296f6 | -17.09364 | -56.80473 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ce290585-4adc-384b-a82b-f057022fcc89 | -17.09106 | -56.80458 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e41bf516-781e-367e-adc2-b5bc2be7bfca | -17.09034 | -56.8081 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| b545c346-9111-3000-899f-707ff02cd14b | -17.08832 | -56.8035 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2289e4c0-e4be-3976-a891-1718b10af09e | -17.08757 | -56.80701 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| cfe8190a-a879-3db6-9985-a51d3f87cdc6 | -17.08683 | -56.81052 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| b8dd585a-843c-37ff-98a8-652e701d6d35 | -17.08574 | -56.80333 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 905093c3-de3c-37df-9842-18c98c7b3665 | -17.08502 | -56.80686 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 948e6071-504b-36ba-9a5b-ac768308e639 | -17.0843 | -56.81038 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 3bed765a-1440-3b8b-aa88-c7d5c51d26f2 | -17.07969 | -56.80563 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| d3ae5689-90ef-389f-a675-fdf3ee3d8f26 | -17.07897 | -56.80916 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 4b1fee75-3925-317b-b05a-05ec9f9cf299 | -17.07825 | -56.81269 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| e44d1eb5-9a97-3fe3-a0cb-2877c2123585 | -17.07436 | -56.80441 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c748cf6b-06e0-34fd-967e-22e76949c88e | -17.07364 | -56.80793 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 06d2cf23-58fc-3a55-93aa-60ad86f8e05b | -17.07292 | -56.81145 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| a45df116-926e-3f81-846e-4adaceaa3eb9 | -17.06831 | -56.80671 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 551bba99-0d62-3838-9e0a-9e24f7c2373a | -17.06759 | -56.81023 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 3dd25d59-1cfd-356b-91dd-f8b0b1e6d0f5 | -17.06687 | -56.81376 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 8b86e2ec-fb70-365a-a73b-ebfce45de25e | -17.06226 | -56.80902 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5a23f27e-b27d-3c95-968f-882b3cef5522 | -17.06153 | -56.81254 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 29d77cf3-239e-351d-8713-539784621928 | -17.05694 | -56.80775 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b072d5fd-06d6-39fd-bf79-f6bebe8ede11 | -17.05621 | -56.81127 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8f5be3c4-3daf-3fb2-8300-ab37c3ac9700 | -17.05234 | -56.80297 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| fe30518d-e71f-3ced-b0aa-e89cce3a88a2 | -17.05161 | -56.80651 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 0e85e050-88bf-3720-bd12-51ea35f709de | -17.05088 | -56.81004 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 99adec06-8828-3fc8-9128-38fac3220d08 | -17.05015 | -56.81358 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 6b619f07-ad63-3549-b1f5-3a1881dc3068 | -17.04627 | -56.80532 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 54fd4cdf-d6ac-32d6-90d9-34438279cf06 | -17.04555 | -56.80883 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 6aa85586-55ee-395a-86df-5835c7c77ac5 | -17.04482 | -56.81236 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 918764f4-687c-3af2-b003-69214ea23e3e | -17.04409 | -56.81588 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 945cebc3-bd41-31e7-9588-b99939b7f5a4 | -17.04095 | -56.80408 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c6a97dd9-a54d-3609-9b6f-27d8a18103bf | -17.04021 | -56.8076 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4b3ba80c-f083-376c-b52d-7c262c79d8fa | -17.03948 | -56.81113 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 50493942-978d-3a80-9adb-a06e7ae9ffcd | -17.03875 | -56.81466 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 98f02fc5-4d9d-332e-857a-604a6dd573d2 | -17.03803 | -56.81818 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f1491d2a-1381-3ee6-85f8-1eaea44af2ba | -17.03489 | -56.80638 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ed6938ee-552f-328b-8590-634f50038194 | -17.03342 | -56.81345 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 5417ee15-6e8e-3c6b-9232-0a845d41ddbe | -17.03269 | -56.81697 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 47f07f3d-9f90-3b6a-8e0c-f067456f7418 | -17.03196 | -56.8205 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d2a46395-08b8-311f-93d6-1db33ece7755 | -16.9987 | -56.73932 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| fd9ba20c-3e91-34aa-b3f5-dbb4e8c2ba49 | -16.99733 | -56.73085 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 8ddd3ea0-e08e-3830-b8c8-7818dd2f02ca | -16.99557 | -56.71218 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| b9e2c4d9-aa44-34ec-9e21-40fb6b377f11 | -16.99413 | -56.73462 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 176618c7-113e-3c7f-a32b-faf03ed988ae | -16.9931 | -56.69702 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| b7f8964a-e69d-398d-8f30-bab0b656226b | -16.99131 | -56.73314 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e06cc656-5b24-33ed-8b2a-ffd9915df318 | -16.98561 | -56.76116 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 2bbb62d9-86bc-38cf-8eec-9cfaba27cedd | -16.98457 | -56.73892 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 938862c5-9c8b-3ee8-8561-7d8b1617a028 | -16.97957 | -56.76344 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| f19b4091-1949-3171-b942-643d0c269433 | -16.97885 | -56.76697 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 4b6ccc43-8e70-395b-a374-58e002370106 | -16.97568 | -56.7552 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fc0e5ea3-3cd6-3da3-ab00-90a8f4b1f9db | -16.97496 | -56.75871 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| df62f402-8ff6-34c4-9f7e-b6d24188ea49 | -16.97425 | -56.76223 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 80792fb0-21cb-35e7-adc7-6abb95488251 | -16.96892 | -56.76101 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 5c7158f5-a91f-38d6-8efa-4e59174349ca | -16.96748 | -56.76804 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 7a5c0522-eac2-3cc7-8525-8909c62e4907 | -16.96216 | -56.7668 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9ad5f47a-74e8-306e-b1d6-cfc247b584fe | -16.96144 | -56.77031 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| d73f1eff-0abf-35cd-95f0-02dead93cb7b | -16.96 | -56.77735 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| cb110141-1217-3ef7-a6b6-e8f6f10e7760 | -16.85849 | -56.71585 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b2f7dbbc-c9f2-388a-8a55-42e57cb6e510 | -16.85777 | -56.71936 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| efa71bee-c3f7-3a0f-a10c-c5571573d373 | -16.85417 | -56.73692 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 749cd36f-724c-3b35-b667-3eb15cf3ce79 | -16.85317 | -56.71463 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e3d8a449-5868-3c1b-b7fe-4b423c422de3 | -17.01902 | -56.72203 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 06609cdb-f678-3ddf-8e27-e230cccb3de6 | -17.01829 | -56.7255 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2e682de7-8212-313e-b95b-c512739ec472 | -17.01735 | -56.70344 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| aac6e3ac-eb4c-3732-8116-4dabd99c0926 | -17.01684 | -56.73246 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 06720efc-5a71-34e0-b179-819be512d556 | -17.01679 | -56.71706 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| cd39a5ac-d41c-3b8b-914a-0039767502c3 | -17.01611 | -56.73594 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 90fd9b35-3211-3f2c-9163-9ed573d463bd | -17.01608 | -56.72055 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 0fe143e1-ea70-3baf-836f-acc693c3bbe9 | -17.01517 | -56.71387 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| d1986918-1e9f-33cf-a6ab-605774ab574e | -17.01501 | -56.6984 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8fa238e7-488d-30e4-87e2-a04a1390ac83 | -17.01444 | -56.71735 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 9d9232e2-7492-3929-8d1a-e1b84cc7deb4 | -17.01372 | -56.72081 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| f24346b9-0daa-393d-a83b-46054e393692 | -17.0136 | -56.70538 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| dff48bd0-5701-3a88-85c9-986d6955d6ef | -17.01327 | -56.73451 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| cb7f0f57-e2c0-3024-bacb-6261305eeb0a | -17.01299 | -56.72429 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| dd9b36b0-250c-303c-acac-4bac432cd57e | -17.01289 | -56.70887 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 79c6ce66-afcf-300a-a927-6c828669fe10 | -17.01226 | -56.72776 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 30f1d425-cb42-3931-9980-bfde094352cd | -17.0108 | -56.73473 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1a889506-0a2e-37ef-92c1-ff1b71805f97 | -17.009 | -56.70066 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 302cb42e-15cf-37dc-a020-5581ad280edc | -17.00866 | -56.72979 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ced92507-1ff2-36d0-b8f3-de0029954be0 | -17.0083 | -56.70415 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 5df94f5c-e82f-31de-8a47-e994a818017f | -17.00796 | -56.73329 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8f2bbcf6-3d71-3a18-83e1-e768dc913bba | -17.00759 | -56.70764 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8234ce77-5225-3c40-bdb8-446ec5d92682 | -17.00748 | -56.69756 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 282d1b6b-4bb7-3c18-84ae-8614ecd74ac9 | -17.00695 | -56.72655 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 02e63c0a-f46a-3e24-b67c-f0f538ad5a4b | -17.00689 | -56.71112 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 120a7f8f-162f-3845-a2ae-8027fc340ed4 | -17.00618 | -56.71461 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 084aa521-81cf-3d4b-a6fc-f23b8f5654bf | -17.00549 | -56.73352 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 7b1eba4d-3dca-3bc6-86db-d0c690911ce1 | -17.00529 | -56.70798 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 21bebee7-6449-36b0-b5e0-ba5d4a5f22cd | -17.00477 | -56.72159 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 840f63a5-d72f-379e-b84a-a44ed49e020a | -17.00456 | -56.71145 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 2ba008f6-704e-3eba-885c-2aafede5de3c | -17.00383 | -56.71492 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| da6d745a-2a7b-3826-a70a-fde353b0728e | -17.00159 | -56.7099 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f1f0b6df-ad1d-3e3c-8dde-57559b721aa7 | -17.00122 | -56.73908 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 24a43f23-52cc-34c2-9edb-1b8c7dd8b76d | -17.19006 | -57.35259 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0591066c-3c11-3f5a-8e18-d173e24cd69a | -17.18929 | -57.35136 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fb3feec6-dc3f-3cb7-83a9-15a9a398a1cd | -17.18927 | -57.35639 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 55918eec-3ccf-3384-b90c-7c890bb02d3b | -17.18847 | -57.35516 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |


[Clique aqui para ver as próximas entradas](README88.md)
