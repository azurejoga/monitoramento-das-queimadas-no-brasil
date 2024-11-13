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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6590c951-e083-31c9-93d3-7abb9ad43d51 | -1.25268 | -51.76387 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82ffc2dd-d11e-3e99-9b5a-8d963de286ba | -1.21727 | -51.74741 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c43b37d0-a2f6-3952-bd99-f97a171c5a5b | 1.59801 | -55.77191 | 2024-11-13 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9da16d17-6d5f-3427-8484-b0a671a74ff4 | -2.26801 | -50.67937 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3325bc7a-5c8e-309a-a352-168c5118cfca | -3.94749 | -46.70905 | 2024-11-13 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66f962a1-8ade-356f-840f-6899e4584ddb | -2.86914 | -54.20651 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c1f1a43-6c19-3fd2-aebd-ef95cf26d074 | -3.14858 | -53.24305 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 177e50ca-04b6-3761-ba63-6b044bbe66c7 | -3.72994 | -51.32896 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4283594-1497-3c34-a7d4-71ede7a995f1 | -2.93242 | -54.4544 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7754d4d7-2b7d-3977-820f-b44a32a55a0d | -3.16691 | -50.45675 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c8ae920-9dae-39b2-a125-801acf833c5b | -0.76556 | -52.49037 | 2024-11-13 04:57:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd39e039-9ad9-394c-bf37-a253c65e3e82 | -3.35955 | -52.09863 | 2024-11-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c79e64f7-c4c8-313c-82cc-05be25dc1be5 | -0.2843 | -51.67039 | 2024-11-13 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9e823b7f-d798-3b85-a1d5-6f163334a62e | -3.40396 | -50.37384 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4705d9f4-15a0-325f-a1ee-9fa36bfd8be6 | -2.61127 | -48.36708 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 493454d4-7a4f-3196-b0cc-230c6c8ccf8f | -2.33555 | -50.57067 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a6bb191-c717-3905-a112-7626017c0b3a | -3.30028 | -51.59329 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e5f9acf-0799-3efe-88e2-8699aa6ea7c8 | -3.69905 | -54.62071 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1290e97-eb36-3916-9aa1-4358e28075db | -3.34969 | -48.96406 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| f44d0056-428b-3055-9056-dda82c184969 | -2.56352 | -49.11428 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cbe13fff-9ffd-32f4-90c4-7215563b837b | -1.42867 | -51.53167 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34ddf6d6-69dd-3b09-af92-49b9a8f836f9 | -2.62273 | -54.28118 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fd2268f-631c-305b-84b3-f7aab6d5c4ae | -3.86132 | -51.91279 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b2d6d7f6-a83c-33a7-95f3-c76b405d3a15 | -2.2533 | -53.75024 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e30d312c-c6cd-373a-b9ee-16bd8b25c246 | -2.4566 | -53.92952 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9f49fbf-c827-386e-9bdd-0ec31eb44257 | -2.9126 | -49.2556 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0b44c6e-dcbf-3bd4-bafd-bda597a5ceb0 | -2.96372 | -49.28313 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89df89a6-c5c7-33a1-b19b-b9e6e072d39e | -3.83773 | -52.26783 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01191e17-ea95-39d8-85ff-b1624ca12d2b | -1.65216 | -52.54272 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e609b305-99cf-3703-8f09-6fcf440b5dc3 | -3.04702 | -50.32948 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| a1bcaf5a-e3db-31bf-abdd-5eda4ce63945 | -2.63794 | -54.37962 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d448f308-a30f-3a99-b899-6a2730ab3ecf | -2.75775 | -49.33965 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aaf38005-6ac5-32cc-8a1c-3f390af884fe | -2.05253 | -52.0868 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38016dcb-f91d-31bc-9cfb-6cbdbb64e94d | -4.02197 | -49.0079 | 2024-11-13 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88793f24-67a5-3fc0-bcb7-e0db37ce12a7 | -2.55888 | -51.23581 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 673bfaab-3a5e-3cba-a547-0b8a8614ca83 | -2.74964 | -54.03553 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdba0db2-821e-3962-aca2-507620abaf8b | -1.33945 | -51.42852 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4eb4d04-ddc3-320a-a5c5-bc34ab9379ca | -3.0275 | -53.23489 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e3754c6-def0-381c-a5c7-7a0c0af99ed4 | -1.98146 | -53.1386 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 795c0e8b-e5cd-3687-a1f7-f110759f50a9 | -2.15658 | -53.65034 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12dbc2a6-fdcd-39c4-9229-325b35ac2b3b | -3.1493 | -54.48147 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 822af50c-6894-3202-8fe0-af6004fb0c6a | -2.17301 | -50.61292 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a661265-c679-3748-a774-ea8ec3e59d28 | -2.3714 | -48.52396 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b7a4a7a-1de9-37a1-82c0-63cf77aaf969 | -1.53815 | -51.11911 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b34dc1f2-5c3f-3608-bcd6-e52b6624cdc7 | -2.7299 | -51.7394 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfdee292-8d43-3541-8817-9869365821b6 | -1.88325 | -54.20135 | 2024-11-13 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 098e05d1-a8c0-3b77-86f9-25e23bea21f3 | -2.28217 | -50.68156 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd0953d8-9f4f-3f9d-93c7-a286e601ff9c | -1.40826 | -52.38365 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| daa828ac-196b-39b1-a36c-298f485a594b | -3.18024 | -51.25247 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0558c886-f3c4-30cc-85b3-45c9b262cc5f | -1.30407 | -54.14214 | 2024-11-13 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e664d478-ddc4-352a-9f31-a2bfb8fe3d5d | -3.5726 | -52.12743 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df3728ac-d918-318d-a83a-328abbd4456b | -2.85026 | -54.00233 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd2b2216-68b0-306f-a49e-d5aa210f96e6 | -2.90134 | -48.2955 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f09bf75-9b33-37b4-ab9e-7ea00c093b66 | -1.38569 | -51.5623 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3fdf4be-79bf-3e74-b295-2c8509d3c37c | -3.35046 | -48.95898 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 7ccf55f5-6895-365d-99f4-94078deca40f | -3.10686 | -54.29721 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35e84099-7272-3fd4-9812-599d8c63dee7 | -3.85845 | -54.07966 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca7b771b-d8f5-36da-addf-d04b8bb50ee1 | -1.53177 | -51.34376 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 669142ce-19aa-3528-9265-c7b5970f2597 | -1.21231 | -51.77966 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a0491c6-2e81-3bde-a872-9d94ef39b8d7 | -3.33519 | -56.95606 | 2024-11-13 04:57:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d17588b3-3f4c-395e-8572-fc988c0c1e96 | -3.39372 | -54.26726 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3cd3b33-7a57-37de-97f6-159258891c6d | -1.20993 | -52.12771 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cf00fec-88f5-337f-ab14-f0e072607651 | -1.47982 | -52.1004 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d245aa5-63e0-3e51-a3fa-19d7ae2f6677 | -3.76532 | -54.65303 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 977e7202-c816-38da-87e8-6641687ff537 | -3.74761 | -50.45195 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0543d1d-01b1-35f7-a9b1-f49144023393 | -1.3998 | -51.99755 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3484cc3c-995b-32cf-b923-6d4df2225548 | -4.02321 | -53.98565 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8390eb2-66ed-3bc2-9ba0-5f2de6d14b9b | -2.459 | -53.6977 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5d8877a-800a-39df-bb74-304530d01947 | -2.62756 | -49.17139 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 179968e5-8b6d-3f62-9077-aff8601b462c | -3.07263 | -50.33672 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 2980a768-6358-353f-943f-55b641246720 | -4.33547 | -50.42743 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8a27b93f-a99a-3b65-9788-8d963ee0e6be | -3.22184 | -50.38792 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a97c11a4-fd22-34cc-ac71-64cceb514027 | -3.05494 | -50.3264 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f3d5a51-8ccc-33e5-a1d2-a7bb5adb83fb | -1.86693 | -48.16468 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a8cf804-d6ba-3da8-bfcd-8efab29462b3 | -1.34967 | -51.43009 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8dd31f46-0fb8-3bb9-91b9-51f1f16a71fe | -3.86445 | -49.11784 | 2024-11-13 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6f19259e-451d-3416-bb23-d291d38350df | -3.05559 | -50.32221 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca51e670-e94e-3290-8f3a-832bd73f9019 | -0.37796 | -51.7464 | 2024-11-13 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 008a6069-dcef-3155-8968-e56494f844a2 | -3.06222 | -50.32751 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f98af514-64dd-3317-85df-e8ab3eb19d6b | -1.23221 | -52.53095 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a1569ca-a1c6-300b-bf78-f100215e4d20 | -3.70481 | -51.83577 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f68c1d6c-12ba-3f1b-967d-09db946e3f95 | -5.35067 | -43.53396 | 2024-11-13 04:57:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a70aa2b-bee3-314d-bc9c-b02495e869c7 | -3.06409 | -50.34406 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ce2d3c9c-61c9-3edb-8e35-883f181d1317 | -4.33914 | -50.42797 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7b805763-ebaa-3e53-836d-ad522e73860c | -3.36924 | -51.6454 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4c162c3-99e7-340d-92f3-78273e56fa06 | -2.71928 | -57.3408 | 2024-11-13 04:57:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83707922-8145-31a9-a960-4a3257b4de4f | -4.06989 | -54.49103 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86d5a9e4-b897-3e31-99f1-75db7fee6c65 | -3.31267 | -54.916 | 2024-11-13 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fd14989-0997-3d89-bd16-1caf43d2aed7 | 1.06492 | -60.60193 | 2024-11-13 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d8d7a908-ef7a-357a-87ff-98b9a029706e | -2.3748 | -53.8641 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da375e63-0bc3-35fc-9b21-b6301fe93a00 | -3.01195 | -54.11908 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02d8199e-9835-3499-abe3-373098b9fd44 | -0.09662 | -51.41065 | 2024-11-13 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1a1a42b-a745-3611-899e-6acb46b8af2a | -3.26436 | -50.43147 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af955c8f-3d38-351e-aeff-64f00e432e81 | -2.18625 | -52.7395 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a913b325-faec-39da-92a6-543245a89075 | -4.26822 | -48.19075 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2cfc81d-8b99-3924-88dc-184d4359541e | -2.71926 | -44.85822 | 2024-11-13 04:57:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6e33785-222e-3ca7-bc17-587a50d58a6b | -2.31112 | -50.68193 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ee5a868-2664-3c79-bcfc-acf5e18a7e0b | -2.46822 | -50.12359 | 2024-11-13 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d8bc1af6-55a2-32aa-a419-a841e4422d9a | -1.28836 | -52.47573 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 986bbacb-e6fe-38a6-88e7-911602d4cb7c | -3.10354 | -54.2967 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README29.md)
