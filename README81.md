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
| 14c1ff97-5091-3a86-9e23-647434a19625 | -10.38044 | -61.20903 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f70b1ab2-9b6c-3104-9fb9-9a3c8eccd540 | -10.38034 | -61.19963 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a3c244a0-db8f-3209-a7c6-9fdf2879b31f | -10.37999 | -60.69019 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e8250775-7c6c-34f3-a3e6-a5d1d2cd7e5d | -10.37961 | -61.2037 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| adbe6169-d701-3afb-92cb-2f52fab071f6 | -10.37887 | -61.20778 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e654d1e6-bc6e-3c49-92d5-33b6c0a1e087 | -10.37325 | -61.17406 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1e7fe6bf-890f-3077-a2ad-02d9010e7c27 | -10.37253 | -61.17816 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 91ada575-d537-3fc4-a7a1-6b119c538dd5 | -10.36897 | -61.1733 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 51aa0b2c-eb18-3ecd-a861-c8c3b3450d25 | -10.34688 | -60.21334 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 128ffd04-c778-3379-98bb-68c33be930fd | -10.19072 | -60.89686 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5ca83f4a-5960-3693-8336-4cc7321faf20 | -10.19006 | -60.90064 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f927eebf-1ac5-3d61-851f-036faca097c0 | -10.18717 | -60.89231 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3b8e24b3-e0b6-3d8e-b3d2-4b34316441a9 | -10.17433 | -59.86661 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 988a87b3-9101-3851-8d23-dd8aa48cb18f | -10.17317 | -59.86868 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a24746dc-37a9-38bc-87fd-a6ee41eccaee | -10.17039 | -59.8659 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9dc5166b-3653-36b1-8dff-797e3af7b43c | -10.16953 | -59.87102 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1f3bc478-6a58-3e8c-80e2-4de1f45921bb | -10.16923 | -59.868 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| daf181a5-6c4b-3464-a5cc-1f1cac8e1c2a | -10.05719 | -61.11554 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d75f351-3d40-3715-a4ae-3cb675bc11a1 | -10.05651 | -61.1195 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb37a40f-ba8b-3f91-8aa9-a463e5275886 | -10.75183 | -60.74834 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e4f0de2-9656-381b-a016-b0bf60a5cabe | -10.74901 | -60.74003 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c4b10a6-55d2-3891-aa40-4cd3be108a33 | -10.74836 | -60.7438 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 173d4123-c730-33eb-8783-97ba8bb1e682 | -10.7477 | -60.74757 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fb4d0be-b23f-3d80-a948-e5f6b7d923ea | -10.74705 | -60.75134 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8d89e6e-3f10-3161-a1de-cdef43c6ff80 | -10.4731 | -61.25031 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e850ed2-649f-3a50-babc-46bd794dbfb4 | -10.47239 | -61.25441 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1e95596-4de0-39b2-9cf0-422ef2b72bf0 | -10.46881 | -61.24957 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 06c77ff6-0282-3d53-9b60-00e36ce489ea | -10.4681 | -61.25365 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 952bde92-7b6c-3b86-b781-c1cfee468ddb | -10.4231 | -61.25764 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a32994ec-1bf2-3098-927d-76931826300b | -10.41883 | -61.25671 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70c25c0d-9c85-3a88-87b4-579d0a3732ff | -10.411 | -61.27589 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 1e70a9db-d4f3-33a2-bbab-bc795fde9bf2 | -10.4067 | -61.27512 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 57cd2a89-2c01-34d6-8096-3604274b51e8 | -10.40525 | -61.23342 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21b609f0-3a0e-3b48-a94d-36100de1b04e | -10.40455 | -61.23738 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e443412b-46cf-346a-bf88-dbc099390b25 | -10.40448 | -61.28759 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc46effa-c10c-3a3c-a2b4-65e55b0b4085 | -10.40382 | -61.26636 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f7c9bcbd-7606-3777-8980-478b7e57ba2c | -10.4031 | -61.27036 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| eced426f-76fe-32bc-b541-e6e2c9108cd4 | -10.40241 | -61.27426 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b63ecde-61c8-3b80-9873-f2fb33694fd4 | -10.40172 | -61.27814 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82eff512-ed9e-311f-94fc-2a72bca4f071 | -10.40097 | -61.28231 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3212a9ef-6aa6-3717-864c-d22672b020d9 | -10.40094 | -61.23275 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6af99fe0-542b-385d-b26b-7ed74ec80d05 | -10.40023 | -61.23676 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9689e10-8d4e-3c8f-ae90-f591da0ca993 | -10.40021 | -61.26166 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 824addba-b707-384d-aac9-ce04ff7b7241 | -10.4002 | -61.28666 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 349ed2aa-4986-3688-9fec-9a4ae1ee08ee | -10.39943 | -61.29096 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4c293e67-4b2d-3cd3-94c3-8326e9eedbbe | -10.39813 | -61.27334 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b42fab5b-9fec-33a5-b2f0-e25cb54bcffd | -10.39745 | -61.27716 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cda05328-9dcd-3016-b93f-0d41e35e4c83 | -10.39672 | -61.28127 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 30934563-58c7-37a6-a0fd-2e5057923e3c | -10.39522 | -61.2648 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 79afacdd-4d4c-31a3-b59a-40ddbe273724 | -10.39385 | -61.2725 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 30e3903d-8422-35c3-aade-24ac19b0e858 | -10.39314 | -61.27645 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 998148e8-c1eb-3f34-af2e-daa9c2f681c9 | -10.39026 | -61.26773 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b2f95238-dd2a-30b9-958f-a3ad95a0dc35 | -10.38666 | -61.26305 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 10da2131-f7d3-39e4-8a84-5e3f5afeff8a | -10.38375 | -61.22982 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea6c080f-a0b4-34bb-922f-5950bb2b2f21 | -10.38303 | -61.23383 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95009484-e7af-32e6-8faf-9bd4ca8a5f4b | -10.38227 | -61.26274 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cc8f1548-aba6-3f33-882a-538893caba73 | -10.38123 | -61.31813 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36441787-e197-3c60-b136-2fb77233f663 | -10.38119 | -61.23035 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 963c5a75-7599-3386-85db-715ca3d93b68 | -10.3805 | -61.23434 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cd5f0eb8-f699-33fb-baed-91652589d8eb | -10.37945 | -61.2291 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 069bdeb5-ec74-389a-b8a5-5355f9144f24 | -10.37914 | -61.24221 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d861a767-3881-3939-af4b-d51b527a7abb | -10.37873 | -61.2331 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 455f4f02-2089-3868-ae27-aa81c456c000 | -10.37865 | -61.25822 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0fb8f4ee-73f5-37bb-86d7-2df3b0807f64 | -10.37731 | -61.241 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3e1ddd54-5543-3acf-abb8-25f3c168fe34 | -10.37698 | -61.25475 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb4f31a1-f2f9-3d65-a0ad-b75679aa143a | -10.37661 | -61.24492 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 836d500a-7f84-36a1-923d-0a40c7c41b53 | -10.37626 | -61.25893 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d42b0ebb-32c7-33b8-8ae3-d4a3fab20a82 | -10.37619 | -61.23367 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5722bb66-9316-39f6-9655-14166988ada3 | -10.37549 | -61.2377 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48b14bfa-474a-3774-9c34-5dc62257a190 | -10.37442 | -61.23246 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b7668165-5aa9-33bc-8cd6-f77dbe2822de | -10.37431 | -61.25764 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 550e187f-f510-3d1e-9d00-a47252541926 | -10.37368 | -61.23653 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4e40dd3e-c95a-3cce-ab43-c363b871b01a | -10.37297 | -61.24047 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 898993ea-51c6-3fda-b43e-c882924481b5 | -10.37264 | -61.25418 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56356e64-8690-3d61-82a2-25adf7b8d857 | -10.37258 | -61.22894 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ad8fb333-1a90-3581-a780-c49686a49149 | -10.37192 | -61.25835 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65bf5d95-78fb-3828-9039-d963d2a30037 | -10.37187 | -61.23304 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 890657d5-820f-36a2-831f-4bc7f06693e9 | -10.37116 | -61.23713 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 79e66fe3-1876-3960-8b0c-6bb72a588b09 | -10.37011 | -61.23179 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 04ab0d9a-f599-3b49-a3af-6422f2c4ed56 | -10.36998 | -61.25703 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc6b894c-4d17-366c-923a-13a8d49b257b | -10.36937 | -61.23589 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9ac4327e-a37b-3ba3-9f45-a3ea7621e60e | -10.36925 | -61.26111 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31114bf6-6394-3e3d-830a-1e805568a53f | -10.36761 | -61.25764 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20498b3f-69e8-39ef-b0e9-8e521c597dcf | -10.36756 | -61.23233 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4be67eb2-f421-3fe7-ad88-f57a434ea83d | -10.36685 | -61.23647 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c1d94288-ff11-32c0-9e34-eceac6309ffa | -10.36567 | -61.25631 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e6ca82a-f040-3e77-8122-66ed2d319ad7 | -10.36495 | -61.2603 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d443619-249a-38d2-ac48-eef618768628 | -10.36401 | -61.25286 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26d28a7e-a431-389d-bd85-09274b259f94 | -10.36331 | -61.25689 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7ea1de2-6991-3f63-87b0-069af60dc50e | -10.36263 | -61.26082 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07cde718-d187-3e04-8204-59530e0fc296 | -10.36254 | -61.23574 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9149a8e3-0575-3034-854e-04d773efd2cc | -10.36183 | -61.23986 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5621559b-4014-35a2-819f-8b70002d677a | -10.36111 | -61.244 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45fb421a-f9fa-34bd-96f0-fba03eba3e1e | -12.15118 | -60.7454 | 2024-10-12 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b211d879-2268-3d37-bd13-2a2a0d761954 | -12.15055 | -60.74899 | 2024-10-12 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a72afd8-31d2-3fd6-9982-d51e4835bd13 | -12.14715 | -60.7446 | 2024-10-12 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87e7e0e1-a04b-380a-924b-0f4dea81ba70 | -12.14652 | -60.74821 | 2024-10-12 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6918276-480b-3b68-85cb-0c8c39ae30d3 | -12.14313 | -60.74378 | 2024-10-12 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4b10945-cf5a-314a-9043-23a90a8790a4 | -12.14249 | -60.74739 | 2024-10-12 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e6365f9-246b-3f49-bdcf-4d38f2fdb6dc | -12.00287 | -61.08864 | 2024-10-12 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README82.md)
