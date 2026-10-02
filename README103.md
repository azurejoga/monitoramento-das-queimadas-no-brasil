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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a13e7b72-1b58-3873-8364-14ad80769f7f | -11.47744 | -43.43241 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 213bd04b-def5-3f5d-a28a-d286edadf680 | -10.77283 | -37.69898 | 2026-10-02 15:54:00 | NOAA-21 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 788eb726-0deb-33d8-b42d-84c0461c958f | -7.86975 | -44.16922 | 2026-10-02 15:54:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 8ef2b563-9f28-32c5-bd80-71bd76c6d542 | -11.80451 | -43.56287 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 3472e84d-0af8-35b4-b221-3efa4e0c8dd7 | -9.79683 | -44.79683 | 2026-10-02 15:54:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9159f7b8-6a2e-3edd-a295-99fd317658a2 | -11.81541 | -43.56824 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| ae0021ba-3c1c-38c6-8386-9440e36330c4 | -11.7024 | -43.60266 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 21bdd3e2-36a5-3170-a509-eb5ddd63441a | -11.85046 | -44.74609 | 2026-10-02 15:54:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 968a195b-535b-3012-961a-41ebe36c0d82 | -7.00538 | -40.35619 | 2026-10-02 15:54:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 1ed6d576-eeae-311c-accc-a5d23ad7a409 | -11.66401 | -43.62056 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 87b6797b-e7e3-3bc3-894f-6ac7918e7490 | -11.16384 | -44.61553 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2c1f38c5-8b05-3f74-ab5f-84ac741ce732 | -11.70743 | -43.60079 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 1e6ce900-3ad6-3a18-b371-275d69e4f946 | -12.76924 | -43.28333 | 2026-10-02 15:54:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 094ccf33-4a48-33e8-9e09-019e3a89b816 | -11.72196 | -43.59578 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 07a6fa18-ee8b-34f6-b292-bd8e25467973 | -12.51048 | -44.14712 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 22306135-df63-31b3-abbe-1dda119b66e5 | -12.49021 | -44.15627 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 168.1 |
| 5ca28a4c-d166-3eb0-aa59-ec7df14d9306 | -11.8139 | -43.55662 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 9bcc9037-4d61-3890-a865-adb8dd679a32 | -11.28249 | -43.54678 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 44d2313e-452d-3ec7-a0f0-aca312b9b5f2 | -10.92658 | -43.83988 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 32063109-2754-3ae4-8ec6-19b844bc35d7 | -11.43716 | -43.40413 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 52f998cf-2214-3cac-89c1-fe7b9d823537 | -12.51007 | -44.14383 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 8c6c96c5-91c0-3920-bd8d-8e6711707fcf | -10.52455 | -43.50425 | 2026-10-02 15:54:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e8d0029f-aec4-3a9b-8283-23db1f546dd0 | -12.17649 | -44.65749 | 2026-10-02 15:54:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 86d6a949-917d-3ccf-8062-6b2b0eef826e | -11.4591 | -43.40593 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0765ccdb-1dd1-3cec-8334-7a319dcdca6e | -12.545 | -39.59655 | 2026-10-02 15:54:00 | NOAA-21 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 2a02c0a9-623e-39c5-9702-2b4d48a7bc2b | -12.49548 | -44.1556 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 213.1 |
| e5f5402a-84d5-3852-9e7c-a03a6a5a7388 | -10.69657 | -45.32215 | 2026-10-02 15:54:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0afc8f01-91de-3481-a934-a7093f6530fe | -11.6478 | -43.57297 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| b56c09c3-0d67-38a7-8c7b-0ecea70eb0a2 | -12.54889 | -39.59604 | 2026-10-02 15:54:00 | NOAA-21 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| c0f5abf1-85c7-327f-b1a9-64992968d6d3 | -11.28588 | -42.14583 | 2026-10-02 15:54:00 | NOAA-21 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 20.5 |
| a47ea9a4-868a-36f9-b293-9c1ed2696be7 | -11.472 | -43.44005 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 7e11a6cf-3032-3d45-831a-145dae271e6f | -11.15763 | -44.60932 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3bbd9a7b-6c5f-3277-b8e0-4277245faf9c | -11.80384 | -43.55616 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 7610e320-fb49-3ba8-a092-b2502113a964 | -11.47534 | -43.41545 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 4ea0607e-3cc6-3518-9ed3-52ec9160af21 | -11.48304 | -43.5185 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 248155d2-8681-3f88-aa8d-55b9deaa6f75 | -12.26418 | -42.15269 | 2026-10-02 15:54:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 1a67199f-cc88-30eb-90a9-2103b9d48e0c | -11.25338 | -43.52443 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| ff144736-c752-3e2a-b2a5-eeb1ce5a9bf0 | -12.41849 | -38.71498 | 2026-10-02 15:54:00 | NOAA-21 | AMÉLIA RODRIGUES | BAHIA | Brasil | 2901106 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| c146ba0e-27fc-3815-8a0b-9763f0a29efe | -6.93302 | -38.94484 | 2026-10-02 15:54:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f1517883-3df2-3682-847a-07c0a9a320ac | -8.79408 | -45.81174 | 2026-10-02 15:54:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0233c040-4ca7-3cf7-9afc-2ba3a366b515 | -11.73823 | -43.44139 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 80d9499d-8f31-354c-945e-93c6d8a97f8e | -12.52272 | -43.10121 | 2026-10-02 15:54:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 40406934-9e20-3d43-a801-b4c3941ec44e | -12.79974 | -45.14021 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 20e2facb-c435-3b7e-b30d-182ba717de40 | -11.80586 | -43.57278 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4cd09ec9-275a-3ccd-a88a-fb94427f1145 | -12.48494 | -44.15696 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 168.1 |
| 5039316b-e251-3b2e-becb-1e177b6076b2 | -13.35121 | -43.86002 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 74110100-2397-3407-89bf-5926cf5e6259 | -11.36291 | -43.42712 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a72a180b-39a5-3fca-b4fa-43354d589f48 | -9.9417 | -43.45718 | 2026-10-02 15:54:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 2b6e964b-0fdc-3b6d-86ea-4ca0bf83ea7a | -11.80549 | -43.56973 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 03f3e94b-987d-3a20-b47a-a4a5d362694c | -11.81425 | -43.55801 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 41208751-45f7-39f9-9884-97d1c7294e0c | -11.80382 | -43.55752 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 5ce4eba2-eda4-32d5-b096-20754388403a | -12.4724 | -44.14186 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4b8fc20d-22c5-3b2b-92c0-293f7b76ba77 | -13.33692 | -43.86681 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 67388f56-45b3-3ca9-a341-9e4b4da8f256 | -11.75884 | -43.44457 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| d3891488-ac18-3dc7-b19f-a75eb3054e63 | -11.71202 | -43.59785 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 170970d7-7dc4-3fef-b154-1a83a6a78df7 | -11.46904 | -43.41748 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 5fcadcfc-84c6-3752-8f06-fa9d54a69d48 | -9.00291 | -37.97677 | 2026-10-02 15:54:00 | NOAA-21 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 6056caed-26a5-3133-bf16-3c0f2ea3067f | -11.11653 | -44.58367 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a4d239e4-d670-3f86-b1af-ab1adb22f148 | -7.58141 | -41.29676 | 2026-10-02 15:54:00 | NOAA-21 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 82448afc-f33d-317b-904a-4bffe139f352 | -11.67259 | -43.60773 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5055fed2-ec53-39ee-b230-9fa3e86290da | -12.78594 | -45.16929 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 280af8cd-73cf-3c0b-ad89-79f2b900f183 | -11.4067 | -44.89178 | 2026-10-02 15:54:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d1146316-29d2-3156-80cf-5a2e33bacfcb | -10.14318 | -45.12104 | 2026-10-02 15:54:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5cc4af9b-d250-3baa-b600-6cd9eea02db1 | -11.23622 | -44.30188 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9d353004-6054-328a-afeb-210bee00041a | -11.74201 | -43.59289 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e6246f2a-73ea-3458-badd-5f7f39636c14 | -13.35069 | -43.84837 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 79a3e677-050e-3325-a212-b65974a86169 | -11.70986 | -43.58021 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| aad87501-07fa-3047-8fb4-007aea730e3f | -11.23663 | -44.30511 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4702cb17-e101-3253-829c-1b2227dbf286 | -8.5699 | -44.13301 | 2026-10-02 15:54:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 4f96d912-ea2f-3047-aa11-50367796dc61 | -8.78188 | -45.81672 | 2026-10-02 15:54:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 777204e9-856f-36e1-9614-d92a08542da9 | -11.65539 | -43.59273 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 135ec4ff-c887-3603-b65a-f041ff386d4a | -11.46186 | -43.40108 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| daa0bd10-8bf1-3292-80d8-6df426e05848 | -11.77156 | -43.54426 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 5dfaa5c9-cc1b-3953-9566-071722a6efcd | -13.35223 | -43.86156 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 212ba777-923e-3a92-bce9-81c0856c1bd1 | -4.95129 | -37.43952 | 2026-10-02 15:56:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2cd8e423-1443-3271-adbc-17b083e2f3a5 | -1.03383 | -47.8045 | 2026-10-02 15:56:00 | NOAA-21 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 18d6ee30-2de9-3872-acc1-4bbfda79a607 | -5.74338 | -45.1368 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| bd254350-ada1-35b8-bd30-f20882287aa6 | -1.46157 | -48.90407 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4bccce02-5c65-309b-b064-02b3d79a00cc | -3.06791 | -49.36305 | 2026-10-02 15:56:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d339ca1b-89ad-3076-882b-0a32d93f2af6 | -5.74677 | -45.16093 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 04f1668d-1079-323e-8de6-ac373b46f30c | -4.73779 | -44.32131 | 2026-10-02 15:56:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 588818c6-23e8-3e83-8333-f457e7a8b1fd | -6.62032 | -44.71593 | 2026-10-02 15:56:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4f8bad93-9e79-3a58-a627-b87577d6b7c7 | -2.1388 | -45.86329 | 2026-10-02 15:56:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 1620d018-b6eb-366d-a957-0d50b3536595 | -6.61564 | -44.71922 | 2026-10-02 15:56:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f3e9a56c-22e6-3016-a375-635f6b67846c | -2.90884 | -42.33696 | 2026-10-02 15:56:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4a6c67bc-425b-3dfa-af4e-882dfd727da6 | -1.61343 | -47.48134 | 2026-10-02 15:56:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b1c52192-0794-30f6-9cbd-a48594e90d76 | -1.45066 | -48.91529 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 134a252e-664c-3ac3-80d2-a8b1878eecb5 | -5.14733 | -37.38771 | 2026-10-02 15:56:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 9.2 |
| f7187cc5-dbc6-34ec-8fee-c3373e466522 | -7.20339 | -46.54205 | 2026-10-02 15:56:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| dc182c3b-5a13-3052-aa87-b2ba628ef12f | -3.58659 | -45.48018 | 2026-10-02 15:56:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d352c442-f345-3646-8dc0-9090027e9e2b | -4.3485 | -46.29548 | 2026-10-02 15:56:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 9f88c5d3-6b5c-3a37-83dc-a41a3d35a3a8 | -5.18741 | -39.73976 | 2026-10-02 15:56:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 14.2 |
| a6ee6fb2-6add-3f1e-a72b-1bc7f4d08712 | -5.55819 | -43.96348 | 2026-10-02 15:56:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 1756fcd0-a318-3fa0-ac40-e0d8800c0751 | -4.29737 | -45.04284 | 2026-10-02 15:56:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 3415f732-9915-3558-a239-766711ddd845 | -1.11344 | -49.01236 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 68970dda-64d6-3218-a1e2-d5a4a53eea22 | -0.78511 | -49.28428 | 2026-10-02 15:56:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c64cf39f-d664-384f-a426-af17060b6e55 | -0.98201 | -47.45761 | 2026-10-02 15:56:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fdda0615-00b0-30e0-b987-1c42789883bd | -2.7397 | -45.7732 | 2026-10-02 15:56:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 0ecfaefb-f9f2-3bd8-859b-b229b4f10cf5 | -5.75106 | -45.15423 | 2026-10-02 15:56:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 275560fd-8276-3e19-8cf4-1267db1e95d0 | -6.06971 | -44.80239 | 2026-10-02 15:56:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |


[Clique aqui para ver as próximas entradas](README104.md)
