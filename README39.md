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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a3d8963-ff1c-3c39-b5fe-a392f6cf2d85 | -21.57911 | -47.81677 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 60c3b31d-b56f-3bc9-8a3b-c6a13ecf832c | -21.57828 | -47.79165 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 30.2 |
| f0b2eadd-7f38-394e-9947-5c31e76c6cf0 | -21.57787 | -47.879 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.5 |
| bcb96ba6-286b-3e79-b60a-fd1c37498bab | -21.57689 | -47.79727 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 43ad969f-311e-31a5-bea4-1521dfeb4048 | -21.57601 | -47.85792 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 471e39a2-2488-3e85-9f5a-7da06bd7ff37 | -21.57554 | -47.80275 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.3 |
| f3043a27-a017-3e12-ba81-5d3712e67fe0 | -21.5741 | -47.8086 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 654ca97f-078e-3bb8-9d0d-78bee9c930a6 | -21.57288 | -47.87066 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 19.8 |
| bf396f5a-2258-3536-aaee-172f09612b44 | -21.57256 | -47.81486 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6bed83ae-e11d-3812-aaa6-c5fba52d43c2 | -21.57134 | -47.8769 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 1452b781-51fa-3499-b762-3cd4180c0c98 | -21.57116 | -47.84905 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 23ca3afd-8989-3211-8b26-def7cd6069ee | -21.57032 | -47.79545 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 30.2 |
| ad5f7ba6-7e44-34f7-8a60-b314c0b5f1cb | -21.56761 | -47.83493 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1c2f99fc-1b9e-3758-9b44-b44cc45f2146 | -21.5675 | -47.8069 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 9d7520d3-38b9-36bf-bf94-83a274b8f638 | -21.56639 | -47.86842 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 049ea608-34be-3194-a03f-381977ab046d | -21.56439 | -47.81948 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 40c97063-11ad-34a3-8d56-1d22d3443b24 | -21.5599 | -47.86618 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 12cc2833-d500-3d49-8e0a-d2506bf231ef | -21.55936 | -47.81142 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b1eff3b9-ea5e-3e37-9b94-53ca42850999 | -21.55814 | -47.84478 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 10299b6e-c637-37e9-95a7-838f5eb06aa5 | -21.55668 | -47.85072 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0d59458f-6e56-3265-acf1-0143a2f1e88d | -21.55508 | -47.85718 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 41ac463e-f7e3-335d-a68e-6a1e28fc6f37 | -21.55337 | -47.8641 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c1692c87-7ff6-3757-94c3-4632b54305cb | -21.55297 | -47.83725 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| be99ca11-2a4e-3e73-89d9-d8083ba1c0f1 | -21.55179 | -47.87047 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4a9074dd-7c9c-3d17-a8e1-79f93745b2da | -21.5503 | -47.8765 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 570e065d-a9a6-3e7e-9f8d-2d29799dcf58 | -21.54859 | -47.85496 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3e3cc07f-6972-38de-a6c3-68b8a58ddfb4 | -21.54813 | -47.82842 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 393235a1-da10-3834-8d0e-549bc21ec113 | -21.54692 | -47.86172 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ca48b55-d751-3a20-810a-686b46703fd9 | -21.54534 | -47.86808 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc4ac1db-df89-3ef7-bb03-e2e6765a93e8 | -21.54201 | -47.8531 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 14f20f3d-2516-3a5c-8908-e7f46b04d368 | -21.5388 | -47.86605 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1e8ef22e-54e2-337f-9585-2a09283bbffe | -21.53559 | -47.87899 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dd9be87a-d278-3cd8-95ce-e755d8adf59a | -21.58231 | -47.8323 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 44497111-f9d0-363c-a1d6-1b02f7394380 | -21.58179 | -47.92048 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a386f85c-108c-3db3-808f-92804b55897a | -21.58094 | -47.86651 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e185c3b4-a373-322c-b583-4c7087f35607 | -21.58025 | -47.92677 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b5b27cec-a7e6-3d43-bde1-b83768ab096b | -20.63329 | -48.7515 | 2024-10-01 03:28:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 0f8090c9-d750-3143-9ca4-fefa0f81b845 | -21.57987 | -47.88423 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 2fa12f5a-c915-32ef-929e-33139daf15a4 | -21.57983 | -47.89972 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| fd60d78c-8a77-367c-adb9-470fa7be4d32 | -21.57962 | -47.85728 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 7c94e421-6c12-37bd-8b94-df1b5cad3cfc | -21.5794 | -47.87276 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 723ce901-b216-3134-8bd3-7972d5cef68a | -21.57913 | -47.84522 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 72096793-d691-3061-a71a-497813d4dc97 | -21.57887 | -47.9443 | 2024-10-01 03:28:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62a056a3-1bed-30c3-899e-f9f03a117da6 | -21.57829 | -47.90598 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 0a3c0dd9-c07d-3644-bfa0-2c95ed0d7ddf | -21.57804 | -47.86354 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 9d728d7d-2782-38e5-853b-f76e16cb3580 | -21.57756 | -47.85161 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e89cc1e5-19b8-38f3-afed-6ee034e7c214 | -21.57749 | -47.82334 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 82.5 |
| fdeae39c-03ac-3a6d-b292-1a25595dc23a | -21.57698 | -47.9237 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 85e676bd-21b0-3634-9a74-cc0f297f3d3d | -21.57676 | -47.91222 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8c3bbebe-dd01-3f0c-b54e-7d1c01f579a1 | -21.57647 | -47.86978 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 08e321f3-e876-3d4d-867f-4185c97c9fdb | -21.57582 | -47.83012 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 00e01f46-295d-37f5-bff2-fb51d0713443 | -21.57539 | -47.93002 | 2024-10-01 03:28:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6784a294-6717-3700-ad53-1e77bea29b3d | -21.57521 | -47.91854 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 718ccbf1-bcae-3f38-8d90-5c12391384a0 | -21.57515 | -47.90294 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 1822950f-84c9-38ce-9d0f-9fc5da96b66f | -21.57489 | -47.876 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 93169081-6ef7-30d8-a533-a80836c58301 | -21.57447 | -47.86419 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 91c8d0c5-fe5f-3cdc-a189-1982520968b5 | -21.57412 | -47.83703 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 6b77af6d-1fe2-31b7-9785-091c3ace382a | -21.57383 | -47.93623 | 2024-10-01 03:28:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a966bcb5-9246-3286-a85a-365087742566 | -21.5736 | -47.9091 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5dfa77b3-6772-3c12-b38a-a5cee854220d | -21.57332 | -47.88223 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 212541bb-3513-3bfd-8d20-0021a757b130 | -21.57264 | -47.84304 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f3eadaa2-ae68-3c6e-99cd-b9f1bada0b0a | -21.57233 | -47.94217 | 2024-10-01 03:28:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6feb23f5-6e95-313f-824f-62556fb484db | -21.57209 | -47.93124 | 2024-10-01 03:28:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0abb9a41-1e31-3192-ad33-7667119d5c1d | -21.57202 | -47.91535 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f72b8fe0-3526-318d-9920-9288cc9f026b | -21.57174 | -47.88848 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 6b79d788-ed36-3c8c-b54f-41fa027b9b20 | -21.57173 | -47.90398 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| f2a761d4-cb8c-39b9-8117-256dfdd515e9 | -21.57093 | -47.82147 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b7c35af6-55c2-38f3-a3e1-30c04778dd9b | -21.56981 | -47.88314 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 66c4348c-db3c-3c31-a0b0-30012f1e45a5 | -21.56962 | -47.85529 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 26ed5574-d5e8-3b02-85d2-beff535fb721 | -21.5693 | -47.82808 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 90a4c386-92ee-3d8a-a672-6aa50fb57efc | -21.56895 | -47.80104 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 44c6e87f-cbca-3a6a-938c-e1a171d8f69f | -21.56829 | -47.88932 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 3e61bbce-d576-3021-a5da-1910da6199c9 | -21.56804 | -47.86169 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e97b612d-34d6-35d8-b6fe-17807b579763 | -21.56726 | -47.93419 | 2024-10-01 03:28:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e009c12a-dbcb-3a84-b050-bb9ce00fbf9a | -21.5661 | -47.84105 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d4076cd0-fd70-3546-b596-43854173f320 | -21.56597 | -47.81309 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 15be8703-6423-3ea2-97c8-271d8d9c0ed0 | -21.56576 | -47.94016 | 2024-10-01 03:28:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca39137f-7466-3ead-afdf-9147b8996ba2 | -21.5653 | -47.90144 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| caf3a5dc-fbf3-372a-bfcc-184efdb7df98 | -21.56482 | -47.87479 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 19.8 |
| eed8f69b-d572-3752-877a-12709e43ea43 | -21.56469 | -47.84676 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 336a5778-13a3-3b30-833d-7fa49becee64 | -21.56384 | -47.91973 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c81bb73c-c446-36e0-8282-de2bc2866842 | -21.56377 | -47.90764 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a10d66a2-e14b-3177-8c8b-6864f50e7a60 | -21.5632 | -47.85279 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 00634dc7-75c7-3cdd-8aa8-36380c486d10 | -21.56182 | -47.88696 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 41d6d61e-56e0-3a0a-82ee-217c4b2c1971 | -21.56159 | -47.85933 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 04a7f05d-05a7-39f6-8d3d-dadeff26a1ed | -21.56052 | -47.92087 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b49c157-9660-3b6d-84f2-e7bb71121f52 | -21.55954 | -47.83913 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a326ff38-d89d-3293-9421-8d9be6ef47e8 | -21.55901 | -47.92697 | 2024-10-01 03:28:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36884ae9-9607-3bec-bd41-3ffd26d840ae | -21.55829 | -47.87269 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 566283cc-38b0-3255-b24a-2a2d4d6c0ea5 | -21.55728 | -47.90535 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 31c950e2-9c74-3435-9a94-ca79a053d91b | -21.5568 | -47.87873 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a0304ef6-a02d-37c6-a9b2-cb38b616ce76 | -21.55533 | -47.88469 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5ae3028f-6dcf-3344-b9dc-98e55ce5cc3b | -21.55384 | -47.8907 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3cffb9d3-13d3-369a-aec2-223ddc72b442 | -21.55244 | -47.92498 | 2024-10-01 03:28:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07b7825f-af2c-3191-ad52-e5a660d52fa9 | -21.55231 | -47.89688 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a92dfea7-b82e-341b-8b2e-e9bd8776e777 | -21.55155 | -47.84301 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 54337aad-b1ef-3c76-a509-559f022da9fc | -21.55071 | -47.9034 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7d88bde9-6ba3-393c-a4cd-567f221c0ba3 | -21.55011 | -47.84883 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8f4875ae-ad8c-34e4-9930-b7ce5849359e | -21.54379 | -47.87432 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5956fd5e-0f52-3a65-ab1c-397e907109bf | -21.53234 | -47.89206 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README40.md)
