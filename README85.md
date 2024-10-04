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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d8367e3-680d-38fa-826e-545f62a600c1 | -19.62141 | -42.23948 | 2024-10-04 04:12:00 | NOAA-21 | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7dd2250a-95b4-30e4-80f3-9b3a751aba50 | -19.62025 | -42.24747 | 2024-10-04 04:12:00 | NOAA-21 | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0cc54e16-48a0-3e33-9c97-794c67a1c8e8 | -19.61968 | -42.25142 | 2024-10-04 04:12:00 | NOAA-21 | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4a9453de-e042-3de3-bf71-ab7543a0e6a1 | -19.61507 | -42.25875 | 2024-10-04 04:12:00 | NOAA-21 | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 633ca8c9-7995-39bc-a019-fd177d9974cb | -19.62733 | -42.82003 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b7f2c469-a076-3533-80c8-4dd05c2066a4 | -19.57415 | -42.73158 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4b44e686-1c56-389d-93ec-d6814419740e | -19.573 | -42.73952 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| b909b5a8-581b-3e90-8387-2fe54124f653 | -19.57245 | -42.74331 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 598fb072-baac-31c4-b96f-27cd844aa205 | -19.57188 | -42.72312 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bd0dac77-53b2-3996-8b91-2a2ee1c771c0 | -19.57131 | -42.72712 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e2ee87ea-c0fa-3579-8c96-f7f2b0f4fe0f | -19.57074 | -42.73112 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d279e856-a793-355c-938a-61680759053a | -19.57016 | -42.73514 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0811a6d4-a137-3a47-8229-c70bc0fa486a | -19.56959 | -42.73906 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1e2b7a2a-f525-369e-b73b-3885f6d8fb79 | -19.56904 | -42.74286 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 892734ca-35e9-354d-90c9-1cf7d37d4af8 | -19.56848 | -42.72256 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cf8e60ad-1099-3854-9b5d-9b441f2b63f4 | -19.56791 | -42.72654 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4f638bba-f4e5-3c0b-96cb-c03014c0447f | -19.56734 | -42.73051 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c53b770e-daa1-35bb-984c-e63b24c19433 | -19.56676 | -42.7345 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cf616091-4dc0-3444-b38f-fed22b601327 | -19.56451 | -42.72594 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f8abf47a-1cb8-3445-a695-ec656ef84109 | -19.56224 | -42.71749 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3d07604b-2725-32f1-845e-7adba81457ba | -19.56182 | -42.71771 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 37e69b11-db96-3937-9ce2-e4fd38d73ce5 | -19.56111 | -42.72536 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ed3e470b-e7d5-3fd8-9d2a-00b1c98d5e07 | -19.52026 | -43.21624 | 2024-10-04 04:12:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4c469ec4-c17a-353d-9c98-1cee5ba26e76 | -19.51691 | -43.21561 | 2024-10-04 04:12:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c6305265-a86a-3257-990b-ffe7efad5356 | -19.50879 | -42.88798 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4d27d170-72cb-324a-8382-cf39f33fa1a7 | -19.50823 | -42.89174 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 982b146c-b8e1-3774-904b-b78cbdfd9e56 | -19.50428 | -42.895 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 69a8cc1c-f9f0-3417-a8a1-3e59038ca6c5 | -19.49916 | -42.88281 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.0 |
| 039c0c52-d4ad-3ae9-9cd1-36a691996086 | -19.4986 | -42.88658 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.0 |
| 3f883c7a-2bc7-35ee-ab63-5953900c04c9 | -19.49805 | -42.89028 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 587bf65c-52a1-37a9-97c9-d667641c0146 | -19.49576 | -42.88235 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 4fbd8dab-fae7-30da-9ea8-b5c0d437b218 | -19.49521 | -42.88608 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| abfe71c7-a7bb-364c-84ad-e2f28593deb1 | -19.49466 | -42.88977 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 46.3 |
| 881b81b9-71e9-30d5-9172-dc1f164dc55d | -19.49412 | -42.89344 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 46.3 |
| 6d90ee1a-5674-3755-bf06-39d8b0b178e9 | -19.49238 | -42.88182 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 92ef1c94-4919-3376-9603-0b5ca4235d50 | -19.49182 | -42.88557 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 1d6bb0ff-6924-386b-9cbd-898b42e09ba8 | -19.49127 | -42.88928 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 46.3 |
| 9e64e494-db88-399d-9851-520662dd2474 | -19.48899 | -42.88128 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| ef3fc2aa-ac05-3027-a723-cec837181a23 | -19.48843 | -42.88506 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 1cbb11f6-93c1-3bbf-9a19-6698e4360d9b | -19.48676 | -42.87287 | 2024-10-04 04:12:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 35c9a63e-594a-31c6-a32c-0446ca79b746 | -19.45079 | -43.06928 | 2024-10-04 04:12:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6983184b-e92e-3af5-a7e7-61fcb31bfd93 | -19.44686 | -43.07249 | 2024-10-04 04:12:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d005cf6c-f29e-3652-9034-8111b28a5135 | -19.44519 | -43.08372 | 2024-10-04 04:12:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 972469d3-31a7-3ff5-b2d9-19be40375a13 | -19.44405 | -43.06819 | 2024-10-04 04:12:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c8d9d858-ef70-3f0a-a890-139e0f8dbc5b | -19.44294 | -43.07568 | 2024-10-04 04:12:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 0a81aece-19df-3d36-80ba-3ffd13d2bc20 | -19.44238 | -43.07942 | 2024-10-04 04:12:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 0428ec80-2eb1-3548-b880-4935cf6d5bc8 | -19.43958 | -43.07507 | 2024-10-04 04:12:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| abdb22c4-dcba-3485-8295-1a9b05e8345d | -19.43788 | -43.06329 | 2024-10-04 04:12:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b9ae75c4-1981-3042-bf9f-9afa98d35adc | -19.43733 | -43.06701 | 2024-10-04 04:12:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 520aeb66-2a4e-3e02-928a-3560ca5fd141 | -19.43397 | -43.06642 | 2024-10-04 04:12:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a741a67b-4514-3ddf-8470-b19d19822a1f | -20.50724 | -42.37352 | 2024-10-04 04:12:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bb317cc3-1f59-3b54-b464-c5e35f7ac6a4 | -20.50663 | -42.3779 | 2024-10-04 04:12:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| aa2def35-3500-3655-82e8-ce16a155275f | -20.50438 | -42.36865 | 2024-10-04 04:12:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 22134148-d348-327f-bd79-0531548cbc3b | -20.50378 | -42.3729 | 2024-10-04 04:12:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 30da607b-e519-3df3-90d7-96cae1e2cae6 | -20.50317 | -42.37729 | 2024-10-04 04:12:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| eaa4f81f-a5de-392f-8525-f83cd51d9e04 | -20.50257 | -42.38156 | 2024-10-04 04:12:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| f8b57573-ee2b-34c1-afd6-0844d4f984e9 | -20.50091 | -42.36804 | 2024-10-04 04:12:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b4c787a8-8f21-3e64-ab29-2e6e3bbdc8d1 | -20.50032 | -42.37223 | 2024-10-04 04:12:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 27e251e3-2dfb-3ea4-b078-c2fbd171254b | -20.49972 | -42.37656 | 2024-10-04 04:12:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| de15a0cd-8c6e-3754-b7f8-72b1c54eaaeb | -20.49912 | -42.38087 | 2024-10-04 04:12:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| a2a0bfd5-af9c-3a5c-b8b7-58018148dfc7 | -20.48259 | -42.47252 | 2024-10-04 04:12:00 | NOAA-21 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3d4a723c-a452-31e9-9788-bc41dd66feff | -20.43805 | -42.51996 | 2024-10-04 04:12:00 | NOAA-21 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| f46e45a3-bf75-3ab5-bd1f-4d4492b16f68 | -19.8717 | -42.34278 | 2024-10-04 04:12:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3c473921-86d7-3710-aeb8-8caaad84c885 | -19.87112 | -42.34686 | 2024-10-04 04:12:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| aa3766fb-5d63-3ab3-be08-1ea3ce7daa05 | -19.86824 | -42.34222 | 2024-10-04 04:12:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2a7b1c54-4438-3068-bc98-07974b114eb1 | -19.85967 | -42.3775 | 2024-10-04 04:12:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3b30a201-f283-3cd6-a543-a310b743c026 | -19.85912 | -42.38134 | 2024-10-04 04:12:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 730c4762-b590-3282-b7fc-d15dfd1c1f2e | -19.85856 | -42.3852 | 2024-10-04 04:12:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 70bf679b-22a4-35ff-9564-494fbe7ed32a | -19.85566 | -42.38082 | 2024-10-04 04:12:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 8777d400-3599-3a16-82ab-3724de1ca658 | -19.85386 | -42.36876 | 2024-10-04 04:12:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.6 |
| a8c9ac4a-68a1-376e-bb20-717389031ed7 | -19.8533 | -42.3727 | 2024-10-04 04:12:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.6 |
| 05404843-ef7f-3bc4-a8d3-391bfadd554f | -19.85275 | -42.37651 | 2024-10-04 04:12:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 9c2a75e2-f811-3d34-bae7-27f2a1b2398e | -19.8522 | -42.38032 | 2024-10-04 04:12:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| aaec9245-b6a4-3838-8331-47e615ac9b60 | -19.851 | -42.3641 | 2024-10-04 04:12:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a61d6c0a-c2f0-3822-b34e-13e49f3bb351 | -19.85042 | -42.36818 | 2024-10-04 04:12:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.6 |
| 32cf31d5-4d40-32d3-b287-d9276b1049b8 | -19.84985 | -42.37216 | 2024-10-04 04:12:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.6 |
| cda33466-b35c-3326-85d5-58a3d4f3ed42 | -19.84929 | -42.376 | 2024-10-04 04:12:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| d2118c07-54b8-3018-9cb5-b88b2c9740d5 | -19.84754 | -42.36355 | 2024-10-04 04:12:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 69486da7-a07a-3084-89f2-7e730da00431 | -19.8464 | -42.3716 | 2024-10-04 04:12:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.9 |
| a94d54e8-e784-33bb-b3f7-cd3dea55715f | -19.84584 | -42.37548 | 2024-10-04 04:12:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 60fa0167-703f-352d-a96a-dcb5fa6d75bd | -19.84351 | -42.36708 | 2024-10-04 04:12:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.9 |
| b940adac-3551-3a8c-afcf-9ca996d89b08 | -19.84295 | -42.37108 | 2024-10-04 04:12:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.9 |
| 2fc5bc93-0bbe-3897-a6ef-6bf17c35c784 | -19.84006 | -42.3666 | 2024-10-04 04:12:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d6689f8e-3e27-3f25-8dff-b08362ece87e | -19.65546 | -42.38701 | 2024-10-04 04:12:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e8ee9aaa-2429-3119-95d2-648a44ac59f0 | -19.65258 | -42.38257 | 2024-10-04 04:12:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e9a9b1d8-f6d0-318d-b708-268b342e8e6e | -19.65202 | -42.38645 | 2024-10-04 04:12:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8bfae620-8a6e-3eff-9973-897d7be5da53 | -19.65145 | -42.3904 | 2024-10-04 04:12:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5b60b92a-f272-35d0-a2c4-8ddae0c0dbdd | -19.64857 | -42.3859 | 2024-10-04 04:12:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 00916c62-f761-346e-a945-a5433dac683a | -20.56044 | -42.95383 | 2024-10-04 04:12:00 | NOAA-21 | GUARACIABA | MINAS GERAIS | Brasil | 3128204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2d9d6db4-ba5e-3f32-a2ae-3887e7d3dfb0 | -20.55986 | -42.95775 | 2024-10-04 04:12:00 | NOAA-21 | GUARACIABA | MINAS GERAIS | Brasil | 3128204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 96840541-99ff-3993-8f70-15c31758b4bf | -20.52578 | -42.88015 | 2024-10-04 04:12:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f07c322a-38b5-34e8-a014-d230247d643f | -20.52521 | -42.88406 | 2024-10-04 04:12:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b790522e-5045-368b-9f89-db40e76f7c54 | -20.52236 | -42.87961 | 2024-10-04 04:12:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5c6d5742-b76f-355d-adcb-9e1de5525429 | -20.46693 | -43.1813 | 2024-10-04 04:12:00 | NOAA-21 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7c769c8f-ddd9-3e5b-b3a2-9ac8d86a5a57 | -20.46636 | -43.18515 | 2024-10-04 04:12:00 | NOAA-21 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b3783735-8490-3d66-94a3-af0c3a2fbb70 | -20.46355 | -43.18075 | 2024-10-04 04:12:00 | NOAA-21 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e266c7c4-1114-35b4-8e15-0385ad5e34fa | -20.46185 | -43.19221 | 2024-10-04 04:12:00 | NOAA-21 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 11101a5e-c410-34e3-bc34-4080fa88811f | -20.46129 | -43.19599 | 2024-10-04 04:12:00 | NOAA-21 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5e37459a-2b60-3e51-b650-ebd554c8bbbf | -20.46075 | -43.17632 | 2024-10-04 04:12:00 | NOAA-21 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 55b63c7c-96db-3e89-860f-ca57a5bd8f1b | -20.40165 | -43.10726 | 2024-10-04 04:12:00 | NOAA-21 | ACAIACA | MINAS GERAIS | Brasil | 3100401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README86.md)
