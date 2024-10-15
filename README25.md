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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89d32c06-69d7-31aa-b3c1-dd6784c3d192 | -5.48294 | -42.77486 | 2024-10-15 04:02:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 604f5cca-92ed-3cc7-8a19-91fcb73dd8b1 | -5.48029 | -42.79145 | 2024-10-15 04:02:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 61afa2f5-24de-3c8d-a0f7-7105de65d050 | -5.47961 | -42.79565 | 2024-10-15 04:02:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b8e69859-c8a2-3f50-ab4b-4e8e1f0307c0 | -5.47511 | -42.7779 | 2024-10-15 04:02:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a5e67fb5-8afe-34cc-902e-d5560574e8f1 | -5.47444 | -42.78203 | 2024-10-15 04:02:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 18844049-36cc-3408-b6e3-b97735227874 | -7.1766 | -42.60634 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 950cf9d4-470d-3888-a12b-20608cd5ec1a | -7.17654 | -42.65042 | 2024-10-15 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 236bd27a-18df-3399-bed5-b071d9772a29 | -7.17438 | -42.59803 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7c2f9e67-c216-3656-8f19-a4113c6ce67b | -7.17239 | -42.65381 | 2024-10-15 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 13091d23-3eb7-3c6e-b04f-b5c57b559fdc | -7.1584 | -42.65158 | 2024-10-15 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| cd2358a0-6d20-3ce5-acaf-62db71d465f0 | -7.14577 | -42.56585 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 45ea1b2e-60b1-3763-a16e-7c59de910e83 | -7.09096 | -42.66092 | 2024-10-15 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5491ed6b-c908-3bf1-babf-1baa3c0ce846 | -7.08569 | -43.02901 | 2024-10-15 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b4fe43d2-6566-3be4-9d72-f663594d6356 | -7.08503 | -43.0331 | 2024-10-15 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 85b4cc4c-184a-3325-be05-1bd19ec0bdbd | -7.08437 | -43.0372 | 2024-10-15 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a291f02d-348b-33ce-84b2-00d50106d7f5 | -7.0843 | -42.6357 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d53fae49-cdf0-3dab-b983-3cfd29705aef | -7.0808 | -42.63513 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 61a1dd44-9e5b-3998-9f27-05262a770e0c | -7.08052 | -43.01575 | 2024-10-15 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e0967721-ae8d-3294-9e42-6895d9167adb | -7.07987 | -43.01979 | 2024-10-15 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 530c55c7-a273-3eb9-9255-b0a9e24acb70 | -7.07916 | -42.66713 | 2024-10-15 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 88923bcd-2f31-3990-81d0-cf823b41f500 | -7.0773 | -42.63458 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d75163af-5a18-38aa-af7a-6d7a1c55d862 | -7.07725 | -43.03605 | 2024-10-15 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0e034c7e-c575-3f4b-b110-d9ef63e8b74b | -7.07659 | -43.04014 | 2024-10-15 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d91c9564-a2e5-385c-991b-a8660ab41b60 | -7.07501 | -42.6705 | 2024-10-15 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 560db0d8-f77d-30f2-8286-834a5eefd40e | -7.0738 | -42.63404 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 04b1e069-83df-3f31-936c-a3a9ea6cb13f | -7.07316 | -42.63795 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cb6a8a8d-dcdc-3512-ac9e-effd73351f21 | -7.07302 | -43.03958 | 2024-10-15 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 068bfe9d-7044-33d5-b283-6e889c3157bc | -7.07152 | -42.66991 | 2024-10-15 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| bc566ba9-e6cf-3cbc-8544-1e6d408d8045 | -7.06931 | -42.66143 | 2024-10-15 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d4c4c84d-426c-3285-a1be-726b6a01260d | -7.06645 | -42.65694 | 2024-10-15 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 88e90aa3-c3d2-3d84-862a-4fe2fc03e93a | -7.06581 | -42.66085 | 2024-10-15 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b98dc0e4-3f93-38b3-8a2c-e640f8748ae9 | -7.06136 | -42.64415 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b9b38481-7ea4-3e04-8a39-bbd3ecdab024 | -7.06008 | -42.65195 | 2024-10-15 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c4f9e04a-7c72-30cd-a48f-bec4160c2f19 | -6.80615 | -42.78288 | 2024-10-15 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d10703b7-dec7-3c19-9f8f-d492ffe7fd35 | -6.66188 | -42.23324 | 2024-10-15 04:02:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 467523a3-ba7c-3504-8485-0e166cf07491 | -6.66128 | -42.23695 | 2024-10-15 04:02:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0a7a94de-9e23-3088-be61-617f650cec7c | -6.63351 | -42.18948 | 2024-10-15 04:02:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b6baa7cb-dfcc-3dcc-ad38-ba53090eda2d | -6.63006 | -42.18893 | 2024-10-15 04:02:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7afb1cee-e0a7-3ae4-9a2b-2a69418752fd | -6.59321 | -42.24151 | 2024-10-15 04:02:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 82675ec8-0e17-3c87-b669-38eea918b938 | -6.59259 | -42.24532 | 2024-10-15 04:02:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 915959bd-cee8-324c-bc57-56e045ebdb53 | -7.95619 | -42.67783 | 2024-10-15 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 341bddec-2d43-37f8-b9cc-b75ad67a2bb6 | -7.95335 | -42.67342 | 2024-10-15 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d6111744-3c27-3e26-965a-8d5b54ce2c8b | -7.94987 | -42.67289 | 2024-10-15 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 33c93cc2-455d-30a7-aeba-42df8b28e462 | -7.76565 | -43.31024 | 2024-10-15 04:02:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ebecc547-496c-36b2-a5e7-c9c4329c6e46 | -7.76274 | -43.30556 | 2024-10-15 04:02:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e9f985b7-3047-3caa-b870-ff093b3f4f84 | -7.76206 | -43.30968 | 2024-10-15 04:02:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a4f8e170-01b7-3aae-b8bc-547b543cb7bb | -7.75915 | -43.30499 | 2024-10-15 04:02:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 909f3dd1-f03d-31b2-a828-53772513efb1 | -7.73123 | -43.20744 | 2024-10-15 04:02:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0c474448-8362-3f76-8f9d-fb11a123d8ab | -7.73055 | -43.21153 | 2024-10-15 04:02:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fd9ade3e-da94-348f-a649-b4d8209c2a50 | -7.72987 | -43.21561 | 2024-10-15 04:02:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 97a6ec9d-350a-33f9-a58d-208265141370 | -7.72919 | -43.21969 | 2024-10-15 04:02:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 873cfd9f-5ccc-3412-a310-c0e5d270cde4 | -7.72901 | -43.19874 | 2024-10-15 04:02:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fe471110-c5f8-39ed-a868-8dd0f8477919 | -7.72834 | -43.20279 | 2024-10-15 04:02:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dd5f4686-e4d1-391c-8c46-53f0d24a8da7 | -7.72766 | -43.20687 | 2024-10-15 04:02:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 588bc288-adb8-378d-ad58-0093dee93288 | -7.72545 | -43.19817 | 2024-10-15 04:02:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 47bcd580-c7b0-3dbf-a812-c489da3b6f95 | -7.72093 | -43.18546 | 2024-10-15 04:02:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ca71d17f-d4fb-3c25-89fc-e2ea0c3fefa9 | -7.70886 | -43.27569 | 2024-10-15 04:02:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 9dbdc67c-252c-37d1-b638-1355b99c07c6 | -7.70817 | -43.27983 | 2024-10-15 04:02:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| c2c2c7ab-7735-3d51-8b7c-5298ca3ad052 | -7.7077 | -43.26756 | 2024-10-15 04:02:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 199021e4-6820-344d-bbc7-ed0514b05de3 | -7.70637 | -43.27584 | 2024-10-15 04:02:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2adfeff0-f446-3d0d-876f-411233e6cf02 | -7.69732 | -43.17325 | 2024-10-15 04:02:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 587d1889-54e3-3c1f-936c-a2e14838d90a | -7.69696 | -43.26587 | 2024-10-15 04:02:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e0fd3f47-275b-3b96-8fbe-078d1808b444 | -7.69666 | -43.1773 | 2024-10-15 04:02:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b13348d6-1f02-340c-8529-18753c3dfcca | -7.69629 | -43.27001 | 2024-10-15 04:02:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d52e82fa-5526-36da-a278-8582df574b79 | -7.69405 | -43.26117 | 2024-10-15 04:02:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1681f0b7-b278-3ce2-968d-3a9c23b428f8 | -7.69338 | -43.2653 | 2024-10-15 04:02:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d7744725-f9fe-34ec-a1fb-9a792da59382 | -7.54583 | -42.90162 | 2024-10-15 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 20dd87b9-03e4-37f1-ad72-c32938b88b3c | -7.54516 | -42.90237 | 2024-10-15 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1dd63fc1-374b-39f8-af0a-ef3114b2a875 | -7.4414 | -43.00509 | 2024-10-15 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6e221a87-a70f-3072-9c78-21a73c907d1a | -7.44073 | -43.00916 | 2024-10-15 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ce4a0275-b672-31e3-8f9d-0a76c6106460 | -7.44005 | -43.01322 | 2024-10-15 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e8d21834-0f72-323a-b84b-5be0f6cbfa73 | -7.43938 | -43.01728 | 2024-10-15 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6c783053-3098-3e9b-be6c-0b6c54086089 | -7.32289 | -42.22935 | 2024-10-15 04:02:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 44108317-cfbe-3d5b-ad97-fc8d46c656c3 | -7.28795 | -42.22757 | 2024-10-15 04:02:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 58e1ac52-c6a4-34e7-a765-439eea901e79 | -8.07201 | -43.82133 | 2024-10-15 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e0a2cd21-2d3d-3e70-822c-dc51c4c7d029 | -8.06835 | -43.8207 | 2024-10-15 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7b6e393d-c184-345a-a79d-12cbb3c5ce21 | -8.44981 | -42.47412 | 2024-10-15 04:02:00 | NOAA-21 | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 37793235-4738-30a8-ba71-129f9b4ef634 | -8.34098 | -42.7499 | 2024-10-15 04:02:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 15eedc11-1294-36cd-a924-48e2bd3f3125 | -8.34034 | -42.75377 | 2024-10-15 04:02:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6a3d8315-27c7-3597-920e-276b42a8407a | -8.3397 | -42.75764 | 2024-10-15 04:02:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8f97c3f9-0924-3e02-977e-bf5d83e69829 | -8.327 | -42.78007 | 2024-10-15 04:02:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6ca2a537-1812-3652-8aed-e6e600dcb7eb | -8.32352 | -42.77951 | 2024-10-15 04:02:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e46febae-5c51-367c-996b-ce2ec3e8638f | -8.3229 | -42.78341 | 2024-10-15 04:02:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 465ac08a-9a65-3e32-a7e5-ed97f00491d7 | -8.14988 | -42.39555 | 2024-10-15 04:02:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 20134c0a-5c36-3316-915c-5b712f0cf12e | -10.57726 | -44.22796 | 2024-10-15 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8124512-163e-30e7-9e92-8353659753a4 | -10.51196 | -44.1951 | 2024-10-15 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a8e84b80-c220-3982-b6a3-ab441f368ab7 | -9.83335 | -43.78191 | 2024-10-15 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9a59cae2-8291-39a5-b452-cebb2dde0436 | -8.00018 | -44.81413 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0120d540-cb0d-3ba2-87b1-5d170141e468 | -9.72257 | -43.85853 | 2024-10-15 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7cedce31-fc24-3854-b717-aeb5e6728205 | -9.45389 | -44.18437 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6b5ec5ed-b4b9-3ab8-bd47-9da6132df2c0 | -9.45165 | -44.15279 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2e0b6277-3993-3d8c-adae-0dd214cdb2ed | -9.45021 | -44.1838 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 9a0eb779-adea-3312-8f2d-7b9157aa8fdd | -9.44727 | -44.17886 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 21fa43b7-3ab1-3a5a-a0db-f54a84415498 | -9.44433 | -44.17392 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 54f69d61-2414-3e05-bc94-e37d10134ce6 | -9.44359 | -44.1783 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8fb63c28-5e3a-33a9-9484-7a791826957b | -9.44359 | -44.13353 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f20e7254-73d2-3b72-b81d-5d27aae1ed94 | -9.43772 | -44.16837 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5d76c1f7-d202-32b0-8ac8-187b3bedec23 | -9.43699 | -44.17272 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e8d622a6-b4e7-3e56-849e-c308f6e00431 | -9.43406 | -44.16775 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 205613da-9d71-329d-8647-8a4e8a61b090 | -9.43332 | -44.1721 | 2024-10-15 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README26.md)
