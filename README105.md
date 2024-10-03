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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15469e4f-5baa-3f38-8e92-84a9843b1926 | -20.6429 | -48.75021 | 2024-10-03 04:29:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| df1f8b5a-775d-3275-9198-50012b80209d | -20.64234 | -48.75394 | 2024-10-03 04:29:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c713fdfb-bd44-38a4-a529-a0646ccb9c0b | -20.63902 | -48.75336 | 2024-10-03 04:29:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7cb7cfdb-7abd-3be8-bf2f-a0d3eaf3d0b3 | -20.63569 | -48.75278 | 2024-10-03 04:29:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d8943146-291c-391b-a291-5e25d2ca770d | -20.63513 | -48.7565 | 2024-10-03 04:29:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3c1891b7-0c29-3684-b16f-c3579a20226f | -15.07843 | -48.94505 | 2024-10-03 04:29:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b64f7aa5-099a-320d-b173-817f9a0dc03b | -14.99549 | -48.59054 | 2024-10-03 04:29:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2939d140-271b-3f8e-a57a-02fd29f4fb51 | -16.42484 | -49.92587 | 2024-10-03 04:29:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c35ed4c-b6bb-3987-8557-2d8e03c0834d | -16.42149 | -49.92526 | 2024-10-03 04:29:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a2ef481-8e9b-38be-ac7d-5856c3f396a7 | -16.11259 | -50.30648 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db010182-4183-3950-8a16-58ce10256145 | -16.10921 | -50.30582 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf24067b-70cc-3f9e-8b18-b3c9c6aecd60 | -16.10858 | -50.30959 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20165451-8acd-3165-96ae-2ba4576805a9 | -16.10814 | -50.27048 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5d1599b-2543-34d9-8598-07350633c623 | -16.10751 | -50.27425 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b6d157b-9b88-30ad-9a58-b314a17cb683 | -16.1072 | -50.27087 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4fb77384-8912-3714-8df9-fe89ab1fb993 | -16.10688 | -50.27802 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0892b9e9-6d9b-3fcc-a2d8-9d7b9897ab65 | -16.10659 | -50.27464 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3e710e7-12a2-3ec8-9640-c741caeaa92c | -16.10625 | -50.28179 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a56dcf65-8711-32b3-b1dd-aeb8e8d6e5a5 | -16.10597 | -50.27841 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71fb2e03-6d6a-3eca-964e-8690772cb097 | -16.10535 | -50.28219 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e097a489-a82a-3f16-81db-4bcdac2a6552 | -16.10445 | -50.2664 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0b1c3bd5-194c-3b37-95dd-5105cba12f8f | -16.10321 | -50.27393 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 202fe6a0-fdbd-36e6-9e3a-bf0e53c6be26 | -16.10259 | -50.2777 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fbcdefb-0172-39ef-940a-e8ada36e806e | -16.1017 | -50.2619 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 99c88eef-36d6-326e-8bed-6597d441a4c3 | -16.10108 | -50.26564 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e0ed71a1-6e03-3e29-b688-259584a9103f | -16.10047 | -50.26939 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 696af238-9c10-38c8-88e2-aac56b18bdc8 | -16.09772 | -50.26487 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a69c0172-ddb2-3cf6-adf0-ac5fd0532ee5 | -16.09434 | -50.26423 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 906790c2-cbd3-3e65-a2bc-5d9c45881aef | -16.09372 | -50.26802 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7590eef-df6e-3cce-8e23-379517e2c752 | -16.09246 | -50.27566 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29f70275-b085-3ca4-aa99-e9587aff6478 | -16.09031 | -50.26755 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e6ffdd5-0e71-34d3-a253-e7c1b7aa0a5e | -16.08906 | -50.27515 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f73e5b4-0d09-3aaa-9daf-f8e2e9997a88 | -16.08844 | -50.27894 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 46c909a7-1764-36a7-9874-01e530486b3a | -16.08783 | -50.28267 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6e71e60d-3341-3e97-be51-c248b93a9588 | -16.08319 | -50.28968 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58991af9-ca98-3bb8-ba7b-3dea16d05262 | -16.08257 | -50.29342 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d04bd8ac-f7d0-3231-80eb-46fda2743b60 | -15.92503 | -49.9878 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1fda718b-9d3d-3fe8-817e-262eb3f4cbb6 | -15.92443 | -49.99149 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a89ecde-d655-3336-88c6-79c059bd73aa | -15.90792 | -50.16292 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1885ff67-b65e-3c00-a7ac-656758132df9 | -15.90727 | -50.16677 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79b174a8-2fc6-34c9-950c-0c7199e39f77 | -15.90695 | -50.16245 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e5ec450-1fe3-3eb3-ae6e-123fd0e90f28 | -15.90633 | -50.16631 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30fd1018-378e-3601-ba49-f86cd759bd68 | -15.90295 | -50.16569 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5174821-6641-3747-927e-8c3dcf4d7623 | -15.89957 | -50.16503 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c0826170-67ea-38db-896c-69d7178190ed | -15.89869 | -50.14909 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 518ad0a5-c2aa-36b4-862b-8c397bbe6765 | -15.8962 | -50.16438 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5e9f1cb2-adcc-352c-bc33-5bd9d56f566c | -15.89592 | -50.14477 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 754af7a4-7e44-303e-88ce-008cdaba6560 | -15.89557 | -50.16822 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93a01e46-6deb-3d1a-ae87-79e8157d022b | -15.89531 | -50.14853 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea22de89-8186-3a80-8c82-a29203b388ec | -15.89469 | -50.15231 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3f53a4db-82c9-38ca-8d98-250f06ffa09d | -15.89406 | -50.15613 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0230fca4-838e-3095-bf5f-6a36dfcbd3b7 | -15.89344 | -50.15996 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a41e2df0-2c73-332a-890d-d23611771bb6 | -15.89281 | -50.16378 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 084a2132-cd4a-3dd2-8d60-69d1ec48b005 | -15.89219 | -50.16761 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58bf227f-3f8a-354d-bd1e-7bcc2fdb5460 | -15.58023 | -50.1604 | 2024-10-03 04:29:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f267db4-c04a-3f24-9683-b6e553cc8f74 | -15.59524 | -48.77914 | 2024-10-03 04:29:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 0ee5ec9b-95fb-3f61-8c98-a9fa389b26da | -15.59469 | -48.78268 | 2024-10-03 04:29:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| d619d648-2d22-3c4a-9e98-32b591d67fbf | -15.59194 | -48.77858 | 2024-10-03 04:29:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| a5dce9a6-21b9-3430-9108-bb210e32a892 | -18.11402 | -49.28924 | 2024-10-03 04:29:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf4d5db9-e782-3d1e-8a43-4b382fb08f22 | -18.11345 | -49.29286 | 2024-10-03 04:29:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae6932a9-edac-3be4-8c20-66ae0db68aaf | -17.16287 | -49.21519 | 2024-10-03 04:29:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1d5791b-c6b8-3bde-b7bd-21f444cd3dbb | -17.1623 | -49.2188 | 2024-10-03 04:29:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54c7af97-47f2-3213-bec1-2ae9391f5964 | -17.15899 | -49.21824 | 2024-10-03 04:29:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ca55f02-8e43-3821-b9e0-1ef67793f7b0 | -17.00727 | -49.7807 | 2024-10-03 04:29:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e9ffcdb-4c59-3f92-b711-0a458221d979 | -16.80735 | -50.12558 | 2024-10-03 04:29:00 | NOAA-21 | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bf55e6c-f670-32ae-bdef-f0604e95f3ce | -16.80399 | -50.12499 | 2024-10-03 04:29:00 | NOAA-21 | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd98528b-39ec-3c0b-a287-d0a9f72bb6e2 | -16.80063 | -50.12441 | 2024-10-03 04:29:00 | NOAA-21 | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b9272fe-e663-306b-8b8e-cd9cf60375a5 | -15.34846 | -51.55565 | 2024-10-03 04:29:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03b63699-0bb4-31c6-b3c4-41edabbc301b | -16.08094 | -50.3246 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b4ee3b22-fa52-3023-9e23-c8094a45e501 | -14.89907 | -51.56843 | 2024-10-03 04:29:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5d7b989-1800-3047-ba94-aff4aa115bcb | -15.08609 | -50.27953 | 2024-10-03 04:29:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b946980-486e-34c4-bfae-f0fb328dfa6f | -15.08546 | -50.28336 | 2024-10-03 04:29:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7c73c29-448d-3ab0-b86a-3c980a34512a | -15.3503 | -51.55512 | 2024-10-03 04:29:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e386d345-2bde-3f71-b768-45779185ed40 | -16.09515 | -50.43184 | 2024-10-03 04:29:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e66e52f2-6ac9-3d4b-ba70-d75c5ec55c95 | -16.09439 | -50.37353 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94ffb44f-78d1-3018-ba16-a7eb8fa932e9 | -16.09099 | -50.37291 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4bf428d2-36f8-3b21-8b22-eda859f480e4 | -16.0904 | -50.37342 | 2024-10-03 04:29:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a40f0a9b-9632-3918-bd42-c9a197541997 | -16.08891 | -50.42716 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d410b8d6-e74e-3e6d-a7ab-a588e73ff7d6 | -16.08547 | -50.42675 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dbe24fa0-5384-3160-9e50-4468ec56e7dc | -16.08347 | -50.30917 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 58696681-1e3b-3d82-aedb-b71b79f2e0b6 | -16.08246 | -50.33657 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c43c627-091d-36e5-8433-e9c922a3b6ce | -16.08202 | -50.42636 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e2d6744c-6dc6-366d-b7eb-33c91543d505 | -16.0803 | -50.32846 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 04da6cda-c34a-3866-97a7-c21e821c7759 | -16.07815 | -50.32029 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 059febd3-fbab-314d-8bf0-f4432cf4ef60 | -16.07475 | -50.31977 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| db40c49a-ed59-3b17-96bf-960af2cd039b | -16.67214 | -50.59942 | 2024-10-03 04:29:00 | NOAA-21 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0124a14e-b80d-3792-8663-cd2f854ed282 | -16.1821 | -51.09346 | 2024-10-03 04:29:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bcb6bfb0-f14b-3882-9d52-b1eb1400be33 | -16.1195 | -50.43286 | 2024-10-03 04:29:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c6fe7687-b6f7-30f5-9df1-77f125c92be3 | -16.11672 | -50.42849 | 2024-10-03 04:29:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3bae7cc-fc48-30f6-a4a0-bf64517b4eb8 | -16.11611 | -50.43216 | 2024-10-03 04:29:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 96fa10e6-2dd6-3a8c-b516-d816530692f0 | -16.11551 | -50.4358 | 2024-10-03 04:29:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4994c488-d2f9-3879-ad89-f62bf24850a9 | -16.11488 | -50.43955 | 2024-10-03 04:29:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 899aad39-4101-3a21-ab79-a7018298039e | -16.11151 | -50.4388 | 2024-10-03 04:29:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c6fb70d9-6e56-3052-9696-0232f00d3f5d | -16.11086 | -50.44268 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 06acbefb-d708-34ce-a8f7-502f407edb62 | -16.10813 | -50.43808 | 2024-10-03 04:29:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2850c9c4-d7d7-3593-ba3a-914f729b5c10 | -16.10748 | -50.44195 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3d36e3ea-593e-3053-93f4-bef3d6ecb9a5 | -16.10474 | -50.43737 | 2024-10-03 04:29:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9dc1150b-877a-3151-9116-edcc23a013e7 | -16.1035 | -50.4027 | 2024-10-03 04:29:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f996ee8-b4ab-30b4-a344-1d33506ff122 | -16.10133 | -50.43679 | 2024-10-03 04:29:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2657306d-6acd-3f0e-87ac-257d85e1e18c | -16.10118 | -50.37475 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README106.md)
