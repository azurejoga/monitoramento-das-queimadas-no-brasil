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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80f929f8-42d3-37ff-bc25-51d727baa206 | -2.56382 | -49.08844 | 2026-09-25 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3500f436-642c-386c-8fbe-53eccbff52a2 | 1.58571 | -55.83467 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b395e89-c816-38e2-8581-7ca9ccc8aead | 2.23967 | -50.89936 | 2026-09-25 05:27:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8f9fdf5-9296-3b05-b8f5-72f7342dfb01 | 1.60813 | -55.87481 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a60aa721-beab-37c4-be9b-6d457ee99412 | 1.29665 | -50.8467 | 2026-09-25 05:27:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0d7eaaf-e528-3112-9fb1-8fbdcde84da3 | -1.14209 | -54.10249 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ed1ce94f-03a3-3390-b9f1-cdea956fcb0a | -2.61107 | -51.73954 | 2026-09-25 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 044268cc-61ab-3e6e-80b3-a2b06bb2a35e | -1.14574 | -54.10461 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30b6d4fc-cb1d-3972-86da-4cdfead34930 | 1.62481 | -55.92833 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5c362fb-189a-3419-a500-6aa4e17d5d0e | 2.24454 | -50.89497 | 2026-09-25 05:27:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bfdda95-2739-353c-8db7-582fa32c31ef | 1.62852 | -55.95554 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b41c2b0c-95c5-3ac7-8f4d-f3fabebefc86 | 1.59745 | -55.85837 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf985f63-799b-338a-aba4-bdeb02e34cc0 | 1.61856 | -55.8909 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e7ea6f9-429e-3ab7-b119-897e71c1c90e | -3.50312 | -50.74417 | 2026-09-25 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8a556e6-979d-39ca-aa71-a93e1a9525ba | -1.13897 | -54.09221 | 2026-09-25 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d183f2e7-ba37-37f1-afbc-b5a8754b47a1 | 2.24512 | -50.89849 | 2026-09-25 05:27:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4e16988-e0b0-3ea2-bd9c-b04797077969 | 1.58649 | -55.83969 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41fbe499-24c8-3b3e-be47-98adebbe0fe5 | -1.62173 | -54.93111 | 2026-09-25 05:27:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe291d43-7036-3ffb-ad92-f296cf41c954 | -1.62238 | -54.92685 | 2026-09-25 05:27:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3aa49ad5-5345-3bf1-a1c9-a4892ea9474c | 2.09846 | -50.9769 | 2026-09-25 05:27:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ea42a19-5e63-33b9-b623-8a614c272d6f | 1.62317 | -55.92085 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc4876cc-3917-35e9-a202-6518eff340a3 | 1.57006 | -55.81197 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62e8faee-a9e9-354d-b646-f240fa0adb4b | -3.20568 | -53.41448 | 2026-09-25 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0ebf80da-87ca-3506-8a8a-7e0f5074cf9f | 1.62321 | -55.91843 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc73dae5-1c89-3028-b9ba-5fd78041975e | 1.62569 | -55.95862 | 2026-09-25 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 789473cf-c7aa-383b-a091-3840c5bd9d35 | -3.50091 | -50.74097 | 2026-09-25 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8b0b43e-f052-3a7a-96fb-99789a17277d | 2.01002 | -61.08479 | 2026-09-25 05:27:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 65866a68-0006-3672-980c-725d0efbdcc9 | -8.25171 | -54.69062 | 2026-09-25 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 641a8b6c-6241-3b4e-bae7-dbf8fd35ebca | -6.33645 | -57.75322 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6298cd0-0536-3e8e-a831-d6700fe7233c | -7.38905 | -64.37233 | 2026-09-25 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d380bb48-0f3e-3b8b-a5d3-3fcf38bb2a50 | -6.07354 | -57.79628 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45e9a93c-3a5e-3e04-ac99-7738ae5b463f | -6.34638 | -57.77226 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59dae92d-c106-39a3-a211-667d9e3a9d9a | -6.64647 | -59.94024 | 2026-09-25 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92e26bfd-8979-3187-81e4-527e70d7e994 | -6.63312 | -59.93431 | 2026-09-25 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b35f85a7-fab0-3471-94bc-86f9194ad38d | -8.07967 | -54.74291 | 2026-09-25 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e34042d-2d6e-3a45-814e-eaf174534a41 | -6.23678 | -57.75328 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 168f86e3-f577-35cb-8008-37dd9946b251 | -6.07911 | -57.81217 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a002d12-1bb0-3bbf-91e4-656c305afad3 | -6.23952 | -57.75712 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9daf0114-5aa7-303b-9d77-a54433bcd25b | -6.1954 | -57.78611 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3777f110-1fd1-3f6d-a7af-3ed61f9dc880 | -8.3036 | -54.76707 | 2026-09-25 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| da7d0eaf-f43d-3158-add6-5ee84d4bdfb1 | -6.31159 | -57.75945 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 789f921e-937a-3412-9255-7ad4be6e5be3 | -6.07192 | -57.86067 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71e978cb-d9fb-31f5-be0a-e0a428fefc58 | -6.64298 | -59.93973 | 2026-09-25 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de65134d-9fb6-347d-9882-6bdb3d50ee4f | -6.64008 | -59.93536 | 2026-09-25 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56d5494e-5834-3573-a6e7-b1a0432c3cdb | -6.64357 | -59.93587 | 2026-09-25 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd90cc06-e6db-3361-82e5-a55941cbec69 | -6.06578 | -57.79509 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab44d29b-6c5d-3d8d-aef6-9c70c9c58125 | -8.07712 | -54.74269 | 2026-09-25 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18d14b8a-6265-3a95-81ad-6c04192028b5 | -6.07524 | -57.81153 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c58fddd-fe80-32dc-abc2-d511f9b668ff | -6.61512 | -59.93549 | 2026-09-25 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7c49601-927f-3992-83f5-6394b284b9da | -7.94295 | -63.49372 | 2026-09-25 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebb765ad-3ab9-30af-b418-11aaccf6601d | -7.94517 | -63.50127 | 2026-09-25 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76e21dd7-9a8c-36fb-88fc-cd20fcf8bf08 | -6.34592 | -57.76981 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a28ac3a7-9ff5-340b-94bf-94e42de192a4 | -6.33961 | -57.75877 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1bff5ff-1f42-3977-b9cc-8ac9fcfc4e84 | -6.23636 | -57.75161 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 932c8687-9c98-3c48-a6a5-9da5a0a0ea06 | -6.07037 | -57.79087 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56697f5d-c927-3ddc-8b2b-a2cd1e1e7ffa | -4.11417 | -51.0789 | 2026-09-25 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dcd8a621-2b7b-3578-bb25-167046086bcf | -6.23562 | -57.75654 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6abd3717-916d-3484-a166-32a26e20321c | -6.09052 | -57.62672 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29f2daa0-82fe-34e1-aad7-74267651b323 | -8.27558 | -54.75155 | 2026-09-25 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c07a74e6-9cfb-36a0-9c74-5517855559c5 | -8.27355 | -54.75102 | 2026-09-25 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 935ff9ce-c54a-3372-adee-a9220de9f4fe | -6.19929 | -57.78669 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 418d1d05-43c2-3360-9a65-fde9a26102dd | -6.45026 | -57.77456 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19338e4a-4b7a-3cfe-bf57-a7d7746e4dcd | -6.31305 | -57.74962 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2f5a5a0-3eba-3af8-9f35-1a1e57de673e | -6.30452 | -57.75335 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db6cdea6-2bf0-30e9-a7c1-62d4ed138d6d | -6.08979 | -57.63171 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bba6dd7b-b5bb-3850-aa7d-9a4bdac7b580 | -6.06966 | -57.7957 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ef3ab60-2546-3fba-80fc-9bc4e852e413 | -7.94185 | -63.50074 | 2026-09-25 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 194efcb2-29e9-3211-8c51-ad91bd64a89c | -6.60873 | -59.93057 | 2026-09-25 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9db7e011-c4ae-3728-bb1b-bf591960faaf | -6.20317 | -57.78725 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a41199d8-a047-3eec-a2e1-d6ef322029a1 | -6.31695 | -57.7502 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a94b28d4-7e00-3a81-a639-90c2dc41efff | -7.39246 | -64.37287 | 2026-09-25 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29e31011-f26d-3f1e-a040-31266768bd37 | -8.07888 | -54.74847 | 2026-09-25 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91119147-04f6-330d-90f1-1a7796960eeb | -6.3368 | -57.75566 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aed27708-8a18-3da7-b7dc-d400b456be31 | -6.30842 | -57.75396 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8709f32c-93d7-3c94-b4e4-95164ad25d1b | -6.31622 | -57.75513 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0c1f8c6f-f615-3fbe-bb74-36414942b9a6 | -6.62209 | -59.93656 | 2026-09-25 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fb061a1-be7d-3a73-8ef1-a054fa9d54de | -7.39022 | -64.36494 | 2026-09-25 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c53378d4-2970-3730-8085-adc6098999a4 | -6.63891 | -59.9431 | 2026-09-25 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69c9dafb-2a1c-3c22-8b0e-d008565b6e2f | -7.38964 | -64.36863 | 2026-09-25 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cce5e9f8-88dc-32e2-9611-1be4ae15902c | -7.38623 | -64.3681 | 2026-09-25 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e3b793dd-fedf-30fb-ba68-851f0817e0fc | -6.6395 | -59.93923 | 2026-09-25 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c02093e3-43e0-3010-8f2b-3c82ab1d3b7d | -6.06119 | -57.79935 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1061084b-e8e2-30ac-817a-862aa52ab845 | -6.24026 | -57.75217 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08e2de7a-03c3-34eb-bf5d-e231ec0441ff | -6.61164 | -59.93496 | 2026-09-25 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49e91b8a-8c9e-37fc-bc35-41b00a2aa98d | -6.63601 | -59.93871 | 2026-09-25 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bc08884-80de-3516-902c-d6991ce3b64b | -6.6186 | -59.93602 | 2026-09-25 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1f90125-4862-30b1-84ab-f83cc9d769f8 | -6.6366 | -59.93486 | 2026-09-25 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac9a3deb-0817-3acf-86d2-72fcf20ba308 | -6.63542 | -59.94259 | 2026-09-25 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86a7d9e2-adf2-33a9-8800-e1ac16798799 | -4.11998 | -51.0806 | 2026-09-25 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 404a1f48-966b-365f-9bd7-0e2f5abb9922 | -8.27067 | -54.75073 | 2026-09-25 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f328be39-b162-31a2-8449-466f84fc1d66 | -8.09427 | -54.98347 | 2026-09-25 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f529e832-8eef-3ea1-9421-e997f935d3a7 | -6.31232 | -57.75455 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e9f7b01-69fb-39c5-b59e-2dde6c7cba6e | -6.6424 | -59.9436 | 2026-09-25 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 101f1f39-22c5-3e5c-b2dc-e45d400af654 | -7.9424 | -63.49723 | 2026-09-25 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54bff623-c3e1-3cee-96bb-a7959899e029 | -6.63253 | -59.93818 | 2026-09-25 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abe4b5f3-ab26-36ae-848e-9ceb7f65b116 | -6.24068 | -57.75386 | 2026-09-25 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2672447-9b35-3671-a2e5-cc88c50a6866 | -6.60816 | -59.93442 | 2026-09-25 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33aa698e-2157-3fa8-9b00-9929c0c3ff97 | -12.20877 | -50.73401 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 60c85b28-e5d8-35e6-ae72-1a548b7e870c | -12.21242 | -50.6719 | 2026-09-25 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ed6a10e-4d94-33e4-a78f-b4000599a843 | -12.23496 | -50.74348 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |


[Clique aqui para ver as próximas entradas](README32.md)
