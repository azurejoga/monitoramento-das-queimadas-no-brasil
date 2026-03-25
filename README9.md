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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f5f7a37-f4b3-3a7a-913f-19795fd09e6b | 1.84541 | -60.41967 | 2026-03-25 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06e4fe1d-4713-3cfc-95b1-808d7c0188d9 | 2.03486 | -61.10176 | 2026-03-25 05:29:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d852820-6525-3433-bc96-44e4f3ad4ec0 | 0.82269 | -59.36737 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3ac4563-5125-3850-bd4d-f40f877abee4 | 0.81432 | -59.35781 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 0c0ced18-3162-3c0c-8561-1bf335745971 | 0.8093 | -59.36946 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4498350a-36c0-309d-b420-1d2b6d0ce35c | -15.65856 | -56.4288 | 2026-03-25 05:33:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b5c2956-764e-370b-a1b6-5f4eaea656a0 | -22.71453 | -47.11511 | 2026-03-25 05:57:00 | AQUA_M-M | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f9a9314f-243a-325a-b6c3-9128537d6147 | 2.71406 | -61.35218 | 2026-03-25 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f5e77af9-aa59-3ef7-ac52-463965738fef | 2.7087 | -61.35793 | 2026-03-25 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d5bcc4f2-5704-325b-8f13-48e9d853f3ff | 3.84999 | -61.2772 | 2026-03-25 06:18:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10e9f126-8cf6-31b7-a64b-c7d39a674963 | 3.85514 | -61.27652 | 2026-03-25 06:18:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8449cde2-a083-3085-a5cf-2159b17abae4 | 3.8508 | -61.28182 | 2026-03-25 06:18:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3899695d-8429-36c0-9c25-aa518cd92366 | 2.70906 | -61.35599 | 2026-03-25 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fdbec786-2f9c-3b6a-bda6-fd7889c645ed | 2.70707 | -61.34836 | 2026-03-25 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 27a19d69-3ebc-3466-b76b-91c5ebd9c81a | 2.728 | -61.35971 | 2026-03-25 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6f0cc92b-9faf-3587-abf7-dd1db2ee1058 | 3.85592 | -61.28115 | 2026-03-25 06:18:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e33d4856-3809-359c-9cea-798973d64859 | 2.70749 | -61.34634 | 2026-03-25 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7da9b511-1bd1-3a0a-aa7b-29c3d2a3577a | 2.70827 | -61.35118 | 2026-03-25 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d98c2c92-4a35-37ae-8f32-d66fb861fe2f | 2.70287 | -61.35691 | 2026-03-25 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b067a22b-1084-35be-a22d-d0238b19256f | 2.71487 | -61.35699 | 2026-03-25 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1754b5cc-8e26-3e12-8626-6c69e023d3ef | 2.72184 | -61.36076 | 2026-03-25 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 219a3c6f-9f21-305c-9b82-df38483c56f3 | 2.72638 | -61.35006 | 2026-03-25 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7375336f-aac1-3711-954c-79cc56ab475f | 2.70789 | -61.35317 | 2026-03-25 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9ca41351-1533-3151-a5e9-032bee4f9e94 | 2.72022 | -61.35114 | 2026-03-25 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f6470bb3-e596-34b7-b25d-7a68708ba880 | 2.72719 | -61.35489 | 2026-03-25 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ab1e7a2a-f4d1-3069-8dd7-04f0fe6bb3d5 | 3.85161 | -61.28644 | 2026-03-25 06:18:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d095e428-4b20-3024-8c5b-07714c46dfe2 | 2.72103 | -61.35594 | 2026-03-25 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2d4368a9-1dac-3a35-bee3-22cab6682ee6 | 2.70171 | -61.35411 | 2026-03-25 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 299ada3c-552f-3688-a19a-0d215fcc5ee0 | 3.85405 | -61.27818 | 2026-03-25 07:26:00 | AQUA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8f65ce35-a0c9-34e3-bb6f-f807192e5d08 | 2.72702 | -61.34631 | 2026-03-25 07:26:00 | AQUA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1f8a9153-5ea3-3130-82e0-a50da09bf36e | 1.92637 | -60.27987 | 2026-03-25 07:26:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.6 |
| cc86e608-703d-3ee6-9aad-7ea0e5da037f | 1.91552 | -60.27125 | 2026-03-25 07:26:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7ac8965e-0098-3f06-a397-8adc25e794a5 | 0.82061 | -59.35194 | 2026-03-25 07:26:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 7c9ef3ba-6347-3f5e-a21c-c5995a959c64 | 2.7093 | -61.34891 | 2026-03-25 07:26:00 | AQUA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 30d49d50-2f8e-3171-bb9a-7506f43c228b | 1.91704 | -60.28122 | 2026-03-25 07:26:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 952b329b-83d2-3c27-8794-e15242175335 | 2.71816 | -61.34761 | 2026-03-25 07:26:00 | AQUA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ee1d4d2c-6f9e-3024-aa0d-1e66b3b863f8 | 1.9476 | -60.90427 | 2026-03-25 07:26:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 055a0f67-91c2-3699-ba08-4e382be59f28 | 2.67893 | -60.24009 | 2026-03-25 07:26:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 78e81435-d7a1-3daa-aeb5-8472fa10af6a | 2.72838 | -61.35525 | 2026-03-25 07:26:00 | AQUA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 832832a1-18e7-3154-bdcf-784b1104a633 | 2.71952 | -61.35655 | 2026-03-25 07:26:00 | AQUA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 19f5bd1c-2dda-3ca0-aea0-c3180764276b | 0.81216 | -59.35991 | 2026-03-25 07:26:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 13.5 |
| f11c98b9-89c0-3ffd-8919-fdb4b2211946 | -25.06335 | -49.4029 | 2026-03-25 11:51:00 | TERRA_M-M | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| c694c39a-fc69-39ec-a886-49cdf2eadf2d | -25.83117 | -49.28201 | 2026-03-25 11:51:00 | TERRA_M-M | MANDIRITUBA | PARANÁ | Brasil | 4114302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 242d6a8d-3fba-3701-894f-795a669b577e | -25.83277 | -49.27166 | 2026-03-25 11:51:00 | TERRA_M-M | MANDIRITUBA | PARANÁ | Brasil | 4114302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| ce43834a-1c17-374c-9882-ae96471884e6 | -25.0633 | -49.3922 | 2026-03-25 13:40:00 | GOES-19 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 93.5 |
| a26c6075-8ed8-348f-8367-20ef8fc1b8fa | -25.0633 | -49.3922 | 2026-03-25 14:00:00 | GOES-19 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 108.8 |
| bc5c6424-8b7c-33eb-8c5a-07b103e91999 | -25.0633 | -49.3922 | 2026-03-25 14:10:00 | GOES-19 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 134.1 |
| c9c04304-75f2-32cb-b3c9-550084dbb884 | -25.0633 | -49.3922 | 2026-03-25 14:20:00 | GOES-19 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 108.5 |
| 6f53a028-1c02-3948-84ae-975642cb1792 | -25.0633 | -49.3922 | 2026-03-25 14:30:00 | GOES-19 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 115.3 |


