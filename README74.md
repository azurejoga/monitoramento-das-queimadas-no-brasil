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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 543bdbf8-e8a3-37d9-a99f-23b0cf82abe1 | -2.8254 | -49.23573 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 380500c6-f5bf-38f5-b984-78bbc5d449ba | -2.82477 | -49.23986 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3240052c-d1c4-3e75-b613-d75eac886a91 | -2.82414 | -49.24398 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6b612531-55a3-3200-b7ac-ba0989a2d919 | -2.82359 | -49.2372 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fde0db26-d539-336b-b385-7eb28771c301 | -2.82299 | -49.24132 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c73c9eb8-2b42-3690-88ee-a25d90c7b0ab | -2.81497 | -49.22571 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f13cd772-6ce2-3829-94af-f7b379b1e8d9 | -2.81433 | -49.22991 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93475e75-5fce-35f9-8d00-67ce1937dd41 | -2.81371 | -49.23403 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0598565-e9a5-39a4-bad2-4f1e5b7eb6fe | -2.80849 | -49.22901 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 560096e7-7e32-3b25-8f24-14960f2fa299 | -2.80787 | -49.23314 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d662eff-4cf7-37f8-b20c-9fc28868d002 | -2.7124 | -49.31477 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7425cd8-3670-3e28-9853-0d518b400a8f | -2.71142 | -49.3206 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90ace0d5-c198-3e7f-b160-00faf924008d | -2.71123 | -49.32283 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f403001e-56e7-3a7d-8260-0f036514e0c8 | -2.70719 | -49.30981 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 336c08bd-ed5f-319e-8a83-84b1453dc931 | -2.70684 | -49.31171 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 27c3d021-1d62-38d8-9f41-f104855fbd4d | -2.7066 | -49.3139 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fe861c1e-11ab-3bde-bf5f-a058a4973b94 | -2.70623 | -49.31575 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 349ecd42-9bc4-37b9-93ef-1a664da0d35b | -2.70601 | -49.31795 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 34d294e3-4a09-3c02-b82a-372a7b2f4ae8 | -2.70561 | -49.31976 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0eb72873-ad7b-36ee-af80-0ee6a2507f5c | -2.70042 | -49.3149 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7101e982-7228-3d9c-884c-6c781b78e19f | -2.70021 | -49.31709 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cded40d3-2bf7-3670-8522-8f1d68670f0e | -2.69981 | -49.31894 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb436c36-8e98-39f7-a89c-b2e0a1349316 | -2.69962 | -49.32113 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 28197d1a-9e0f-3ce1-b2f1-07aa8bb4089d | -2.65042 | -49.79334 | 2024-10-28 05:21:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7c5595b-f0ac-3dde-a930-d416db369b62 | -2.63202 | -49.26297 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab11cb60-10a0-377f-8955-cca9a181fc79 | -2.62621 | -49.26212 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb0cc7a9-b6b0-3430-9328-8f58197b49a6 | -2.55953 | -49.82532 | 2024-10-28 05:21:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66540d7c-82dc-36c4-bd49-30b469beb6fc | -2.55898 | -49.82904 | 2024-10-28 05:21:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf9b5ab1-4170-32d3-83eb-270f0ed47d6a | -2.55393 | -49.82449 | 2024-10-28 05:21:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aecf6dc3-426e-3776-bc87-5d343c1c684c | -2.54304 | -49.83746 | 2024-10-28 05:21:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c01f39a2-0bec-3d32-9411-f397b7f0cf56 | -2.54246 | -49.84115 | 2024-10-28 05:21:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6de5e51c-03e5-391f-aa73-cd79f2905485 | -2.54054 | -49.83768 | 2024-10-28 05:21:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 58dc2a77-62ce-352c-9322-44c0878f7d86 | -2.54 | -49.84137 | 2024-10-28 05:21:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e9c6b3a4-3f12-3db4-876b-5375b4b2d955 | -2.53687 | -49.84031 | 2024-10-28 05:21:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b7ca463-88c3-332b-bd05-6081fa598665 | -2.47032 | -49.78843 | 2024-10-28 05:21:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66090779-8fd3-3da3-bfd6-942af4651cd5 | -2.46977 | -49.79209 | 2024-10-28 05:21:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7aaf4d62-e3ac-3bfb-90c1-ea065902d204 | -2.46472 | -49.78758 | 2024-10-28 05:21:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b3f0e44-277d-35a9-b829-1e17f15ec617 | -2.46417 | -49.79124 | 2024-10-28 05:21:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09a8ada4-f2be-3fe1-be95-8ece4d366259 | -2.4275 | -49.16891 | 2024-10-28 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b722f954-85ab-35fa-bbf8-f892db479efa | -2.35357 | -49.54257 | 2024-10-28 05:21:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1d08c64f-b23f-387b-9938-dd5d2e818330 | -2.353 | -49.54644 | 2024-10-28 05:21:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 060a3c04-e761-3ad1-99ea-d131c21e0fc2 | -2.35189 | -49.544 | 2024-10-28 05:21:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9d1bdcc1-ecb1-3d8a-aa3f-5dadb6c7d6ab | -2.35129 | -49.54786 | 2024-10-28 05:21:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7ae8cccc-77df-3d87-a081-bfd624c54b34 | 2.35305 | -50.758 | 2024-10-28 05:21:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a1c3500-4ad9-31ea-bb0f-e4576a060c4b | 0.31703 | -50.92215 | 2024-10-28 05:21:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ef194f4-890d-34c4-b04a-2095174a5b87 | -2.19632 | -50.75678 | 2024-10-28 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b6d74f9-07f5-3e46-bda3-85a7e60eb814 | -2.19585 | -50.75993 | 2024-10-28 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f01147f0-b262-3056-ab6d-64829ba95986 | -2.19533 | -50.59326 | 2024-10-28 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 694396fe-ff9d-3f53-b692-0f37c6ad6440 | -2.19483 | -50.59649 | 2024-10-28 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e545e60e-3191-3c25-84aa-6cd410eb7ce1 | -2.19433 | -50.5997 | 2024-10-28 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a066280d-cdab-3e41-a72b-b987931aa198 | -2.19373 | -50.5928 | 2024-10-28 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a4f460ad-d666-3627-bb47-f7536eca3164 | -2.19326 | -50.59603 | 2024-10-28 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 049fb0d4-7226-3acb-8486-07b912ad5efc | -2.19279 | -50.59924 | 2024-10-28 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 918fca4e-706a-3c70-9e8f-5fc30da0b546 | -2.19004 | -50.59245 | 2024-10-28 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 631b80dc-c092-378d-963e-081cd4a2b361 | -2.18955 | -50.59566 | 2024-10-28 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4adbcac3-bd95-3739-9989-e91ac6b9ceab | -2.18279 | -50.60441 | 2024-10-28 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 742e8e45-ac09-3d4a-b0c3-fc0c5987b7c5 | -2.18229 | -50.60764 | 2024-10-28 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ed07405-ddcf-3954-bd59-9a7574c1319f | -2.29921 | -51.93001 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4cd65bb-4670-34b6-a21f-f33c6131402c | -2.25401 | -51.86929 | 2024-10-28 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c20ee48f-a35f-3b0c-b73f-09c3587b624a | -2.24839 | -50.66055 | 2024-10-28 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20a5fbb9-d818-35ac-aa64-d3aea7fe2f32 | 3.58709 | -51.28086 | 2024-10-28 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 24b9c7fb-2f4b-3013-b0d9-58bd12777d40 | 3.58636 | -51.27327 | 2024-10-28 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f8d4b26f-cc1a-3c51-b37a-608f8ee5708d | 3.5863 | -51.27617 | 2024-10-28 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 62b97527-104d-3f0b-8312-9fb02eb6d886 | 3.47515 | -51.24971 | 2024-10-28 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2ede2ce7-1b9b-3f27-8d64-0c8e3ee78155 | 3.4742 | -51.25295 | 2024-10-28 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f01b2240-d8e9-31bb-8e74-f21cfb9a7042 | 3.47339 | -51.24821 | 2024-10-28 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f7811713-5fb3-3c7b-b794-c27259a0d0f3 | 3.47054 | -51.25047 | 2024-10-28 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 35df6d48-d3ea-3325-b1d1-ec1fd8c839ce | 3.46977 | -51.24572 | 2024-10-28 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 76c52f88-fb27-330c-be7a-5c2a953960e1 | 3.46515 | -51.24649 | 2024-10-28 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0651b7f5-2a9f-3b58-a4a1-95b4130c3394 | 3.46131 | -51.25201 | 2024-10-28 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 879001ed-c268-3ee6-a0fa-45304cc44f16 | 3.46054 | -51.24725 | 2024-10-28 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c0e0cc99-7209-3237-bea5-d87f942017da | 0.54243 | -51.46613 | 2024-10-28 05:21:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3864fc63-456e-3ed7-8ee8-d512acd422a9 | -0.1066 | -51.62445 | 2024-10-28 05:21:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0030f17-5438-3830-afc5-b6df421da9b7 | -0.10607 | -51.62571 | 2024-10-28 05:21:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 662e1e5d-c06c-3339-8dbb-e5a5ffb7d7fd | -2.21587 | -51.99205 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d7ae6fb-0f08-3184-b9fd-44a06a0e6557 | -2.0584 | -52.16858 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ae3b0fb5-3a12-38cd-94ef-dee3d211f4d1 | -2.05755 | -52.16682 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| f176ce6d-9511-3233-952b-900aa0765334 | -2.05678 | -52.17176 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8e8f8d26-876d-3ee6-bd18-50b80ef18e1e | -2.05281 | -52.16611 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 4b11adbd-f9fb-3197-bae5-fd07354bd791 | -2.05024 | -52.08862 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eeda149b-da82-3d96-be99-92258165bb6b | -2.04705 | -52.07775 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6d9813db-9850-3273-866e-aa9115cf793e | -2.04626 | -52.08284 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 767ada5f-ced7-3e23-bff5-5f0de000dd4d | -2.04548 | -52.08792 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7672b661-5c25-36cc-b501-c488a4e02e52 | -2.04229 | -52.077 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b166ae6e-8b02-3d89-8659-2b36d0b1a8a0 | -2.04151 | -52.08205 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b88e72d3-8275-3cab-962f-917ca799e198 | -2.04073 | -52.08712 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| addcf2e0-6c36-348d-ac6b-8379209d5f63 | -1.98792 | -52.08278 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 46ed88c0-e42a-35d4-adf0-3e0f1b17f09a | -1.98764 | -52.08416 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ae1e1676-1e75-332f-bc15-fc33ef4fa967 | -1.98395 | -52.07702 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19d0cd21-228e-339b-854f-e3ff6df10cc0 | -1.98363 | -52.07839 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d0e8b427-3caa-34d9-a4dd-5e8a403485a9 | -1.98316 | -52.08207 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4d374d98-5acd-3f41-a866-173ac31e8772 | -1.98288 | -52.08345 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 97bf8572-f60a-36b6-a775-7a718c0aacdc | -1.98236 | -52.08712 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 72573473-74aa-3d5a-b615-193c5af5b1c7 | -1.97888 | -52.07766 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| bbe5859f-266f-3b81-8e0d-e549a4df3bf1 | -1.9784 | -52.08135 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 1c1276e9-1626-3cd7-baa9-024df78143c5 | -1.97812 | -52.08273 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| fe225b33-7951-39e6-9cb5-6e7186b3df11 | -1.97761 | -52.08641 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 83f730b1-af57-38b9-8bd0-7ed130f85f71 | -1.97737 | -52.08779 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 47c4ad78-9627-3f94-9d5b-672178de9d47 | -1.92785 | -52.1252 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d923d7f-6f04-39de-b690-f845046701a9 | -1.92708 | -52.13022 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README75.md)
