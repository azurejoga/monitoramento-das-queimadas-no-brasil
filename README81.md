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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 924ddfe7-0298-32db-8c83-2b686b7b6968 | -2.50537 | -54.58354 | 2024-10-11 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d01305f-a50d-3a9a-85e4-09678e064f54 | -2.5051 | -54.58561 | 2024-10-11 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13a3b408-88d6-36b7-a1e3-fe56de831bc5 | -2.16868 | -54.45962 | 2024-10-11 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34576422-db5a-3f75-991a-baea7b8c14d3 | -2.13827 | -54.84417 | 2024-10-11 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 086194d3-49a3-3d95-aa39-7fedf2828d88 | -2.13762 | -54.8483 | 2024-10-11 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab320ea8-4e3f-3bfb-b704-b3f165e7da25 | -2.13602 | -54.84647 | 2024-10-11 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a6f97d5a-193e-3d09-9bb9-efe68940b861 | -2.11013 | -54.8356 | 2024-10-11 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3d296b0-4547-3a33-812d-51ba67015b6e | -3.67073 | -53.95248 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65c9525c-a360-3612-8c33-61305348740d | -3.67 | -53.95723 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b68f6df-459e-3540-9a6a-8e7fbf3eab1f | -3.65301 | -54.16502 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3747a4f2-5c22-3a30-8806-9fb954893e50 | -3.65075 | -54.15814 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ed0dbe6-1f09-32f6-898a-9f60e376ba97 | -3.65004 | -54.16275 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59d63483-29af-3b44-8aab-5ff2898f5e60 | -3.6499 | -54.15971 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ea8f776-28d8-38d5-8fe1-1f38139836c4 | -3.64929 | -54.16756 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c35c55f-5d48-38ab-b9ff-13929350f7af | -3.64921 | -54.1644 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 025e87d0-c624-3780-88ea-74f8d3864fd8 | -3.61554 | -53.89908 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92ff54bb-8831-36b9-bd26-1f8019be7127 | -3.57645 | -54.53908 | 2024-10-11 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50a9440f-b60c-334b-a10b-bed02555dc6c | -3.56353 | -54.34795 | 2024-10-11 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 68036dbf-b884-39d3-b67e-c6f89675f6a3 | -3.27599 | -54.17429 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b365b8a2-fcf3-3f5f-bed6-91a54b281a31 | -3.26319 | -54.182 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf2312b6-70ca-384c-b24f-9f252f58bf25 | -3.2594 | -54.18146 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0fc3e8f-6c8a-34db-9d40-7813e77adec3 | -3.25868 | -54.18618 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ed79e7b-7cfe-354e-87be-f6ebb0a2c77b | -3.25797 | -54.19088 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f0d50d5-59d4-382e-be2f-dbc26541485c | -3.25726 | -54.19555 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 026f438f-cddb-334a-b46b-1710028db7fe | -3.2556 | -54.18091 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 539642c2-63d1-3875-a03e-8b8899a1962a | -3.25489 | -54.18567 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a9ea2b67-e0e3-3937-8bc7-bebba965ac7e | -3.25418 | -54.19036 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 23a92354-ae49-3247-a632-653e5867449d | -3.25348 | -54.19498 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4dd3285a-82fc-35dd-88e1-f0b13029aaae | -3.2511 | -54.18512 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6a5d1872-81a4-36fa-8dc9-26270b2e04c9 | -3.2509 | -54.77895 | 2024-10-11 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd1fd490-cab9-3f85-8d8a-ee39b482d80b | -3.24369 | -54.13117 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fc6f868-053f-3cae-a739-b519b79c4ab3 | -3.15336 | -54.63533 | 2024-10-11 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3398b06-7396-3616-912b-d0af4ebcf479 | -3.12991 | -53.73457 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13e7f99e-f2c6-3794-a51e-ce438b9105fd | -3.12528 | -53.73886 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d74f30b6-fb85-3a60-b11a-fde0eb79d1f7 | -3.12139 | -53.73827 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc059678-f12f-3a66-8f73-50c0074a0426 | -3.11825 | -53.73278 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01b1250c-d86e-38ca-89eb-b31d2ba6f0f8 | -3.11751 | -53.73767 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 985751eb-ed21-3b25-864e-c3f0388c61cc | -3.07434 | -53.91847 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2857b056-39b5-3fa7-97fb-dfdcf85afa2d | -3.07051 | -53.91788 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5790b47a-d697-3e52-82eb-fc17f73cdac0 | -3.03978 | -54.27395 | 2024-10-11 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56d3e631-b7d6-32e3-965a-dd503f6ec6d3 | -3.02194 | -53.85955 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a538e39e-2cb5-39d2-9808-f002785e64ee | -2.88519 | -54.06795 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9cd7096-3815-36c3-8cb3-38ed5f6ed676 | -2.88204 | -54.13832 | 2024-10-11 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbd7e917-368a-3954-91cc-1c719549509a | -2.85199 | -54.4943 | 2024-10-11 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8a1630d-0b98-38cd-af1d-890160301654 | -2.81277 | -54.36333 | 2024-10-11 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dea3735a-5b31-3a26-8f7a-1aac6b60628c | -2.81206 | -54.08981 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0f31f31-d3a8-3f1f-a069-9c03d634420b | -2.80541 | -54.08143 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2506b0be-47d5-3a73-8e4d-2d52c744682c | -2.80518 | -54.084 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b6edaac8-8ccd-3cc1-abeb-15bec2a83a00 | -2.80474 | -53.98622 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 43d3e0b5-97a6-3236-8b12-874ea53cf613 | -2.80209 | -54.07878 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 42bb2d53-1926-36d9-9bc4-8f0caa836502 | -2.80163 | -54.08084 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a673091-2e2a-3cee-84dc-c4d5fc5a8c28 | -2.8014 | -54.08341 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3fe33da7-24e8-3d7d-b455-fc942a563033 | -2.8009 | -54.08545 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 390d8e7c-0994-33bb-9aed-cc5add361b77 | -2.79933 | -54.09726 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9aa6aa36-5aa9-3f3c-8c13-2eebe6110d52 | -2.79874 | -54.09927 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db7810c3-d74b-36cb-96b2-c34dd6141ba2 | -2.79831 | -54.07819 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9628afd2-6e33-3ca1-9dd7-73109c8b781f | -2.79761 | -54.08282 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 290436d1-ba65-3317-b030-6b8e947479b4 | -2.79712 | -54.08487 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad933cbe-1d56-3321-bc43-6f41ab923706 | -2.79692 | -54.08745 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ae2d4eb-f729-37e5-80f1-35b96048cd99 | -2.7964 | -54.08949 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5af69d41-c18d-37c3-b7de-9bbb11ce7c1e | -2.79554 | -54.09668 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35a8b2da-b439-31c7-97a5-7edb3abe9157 | -2.79496 | -54.09868 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cbefefd-3bee-3487-a110-3ab89366ab86 | -2.79245 | -54.09147 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 768e6a6b-6ec0-399d-a2f8-3323fcbe276c | -2.7919 | -54.09349 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a093abf9-308e-39fd-83e1-0ff9721cda58 | -2.79176 | -54.09608 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4aecdb54-1076-3160-b157-0d07dce43c32 | -2.79118 | -54.09809 | 2024-10-11 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42fe8f1a-3e6e-32f9-ad30-4df295d8d202 | -4.47701 | -55.08946 | 2024-10-11 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba30044b-8224-3b2a-9d47-c17e9d70161f | -4.46971 | -55.08836 | 2024-10-11 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e91944d8-e015-368d-b5c7-1769161bbc51 | -4.46905 | -55.09264 | 2024-10-11 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20fb55e1-2b80-3ba0-9cf2-6698db701879 | -4.45192 | -55.48146 | 2024-10-11 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28adf9f9-32e3-309d-a299-7bf101c3b780 | -4.44773 | -55.48498 | 2024-10-11 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3168060-c3f5-317f-b943-a27845fc736b | -4.44416 | -55.48441 | 2024-10-11 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe5a6579-645d-313b-9f6f-ad6dd2c2825b | -4.42104 | -55.23616 | 2024-10-11 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 704eb07d-d557-327a-a1d4-5fca286e81ae | -4.2685 | -55.15841 | 2024-10-11 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb95197b-09b2-3f17-8680-9a908f19d407 | -4.26487 | -55.15786 | 2024-10-11 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7195688-10a3-30b1-870a-3aec9b19eeed | -4.09072 | -54.60276 | 2024-10-11 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d881c6ca-af47-3d39-a14d-348fdcca9847 | -4.09004 | -54.60719 | 2024-10-11 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de1f3cfe-1a10-3d75-bb28-2242ac9975f4 | -4.47336 | -55.08889 | 2024-10-11 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c347093c-3405-3d1d-ab58-a38d1ffdaa5d | -4.4204 | -55.24035 | 2024-10-11 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e498118b-efb2-3d4f-9c77-620ccb8fae42 | -4.32937 | -55.1976 | 2024-10-11 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee9829b6-199e-32d4-84d2-60e4cc19fe0e | -4.26808 | -55.15578 | 2024-10-11 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84f806d6-a3e3-3de3-8094-ce216ffda421 | -4.26744 | -55.15994 | 2024-10-11 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ae59933-de52-3f5a-99ea-ad0a13519961 | -4.26549 | -55.15368 | 2024-10-11 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b8fc442-15f6-39c3-8c3a-99a7ed2a67b7 | -4.26502 | -55.45024 | 2024-10-11 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eca80ef5-5ec2-33f9-93a3-3d30046bb870 | -4.26445 | -55.15524 | 2024-10-11 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4059e4f0-fa1e-3cff-b1dd-3aa94e8b2632 | -4.26381 | -55.15939 | 2024-10-11 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fe75b9b-e4f1-385c-90af-09a2944ab1a4 | -4.05564 | -54.78307 | 2024-10-11 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 126dddde-a337-3ec7-ba52-89b33a762acf | -3.97552 | -54.08879 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 474729d7-7c35-393c-b8cd-e66525be6835 | -3.90898 | -54.16519 | 2024-10-11 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3863df5a-9b0c-3292-a67e-e4b8c0f4f6ad | -3.90516 | -54.16457 | 2024-10-11 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 118c7b4d-d675-30b9-a962-de6aac838e8b | -3.77907 | -54.22933 | 2024-10-11 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd03f5c2-8f28-344d-9c75-fb97ab89d812 | -3.70828 | -53.92527 | 2024-10-11 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99d37a83-04f5-3876-a4d1-24e7999b9a39 | -2.06201 | -55.2137 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37fcab58-50b3-3c38-b553-08178c65bdab | -2.06139 | -55.21767 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c92d2e05-cc53-3e42-a170-693397589bfb | -2.05786 | -55.21712 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64c5aaa5-002c-3985-8c6c-caad276e8f3a | -2.00457 | -56.0291 | 2024-10-11 05:16:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3a114c85-04ce-3292-a2c8-6ddc0dc24596 | -2.00173 | -56.02489 | 2024-10-11 05:16:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85534129-346c-3723-a914-4dcc01dee64f | -1.78393 | -55.41707 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a63dc960-6755-335c-90e0-54e11ead217a | -1.78343 | -55.04726 | 2024-10-11 05:16:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88cc9439-a4fa-3a4b-8972-1462b68300dd | -1.75748 | -55.33361 | 2024-10-11 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README82.md)
