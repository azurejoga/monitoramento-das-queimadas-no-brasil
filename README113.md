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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22473afd-bfbc-3d87-96e5-a821bb3eea69 | -14.19601 | -46.48347 | 2024-10-05 04:40:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba3626ad-abe2-33d0-baad-8d7b9c837027 | -14.19211 | -46.48281 | 2024-10-05 04:40:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 745033b8-602e-3e57-99ba-57dc912d7c22 | -14.19141 | -46.48787 | 2024-10-05 04:40:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c1e25d1-48e4-3029-8caf-be8d3b8fb1a0 | -14.04721 | -46.37263 | 2024-10-05 04:40:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8682551a-955f-36de-b16f-76e35d9639c0 | -14.04653 | -46.37764 | 2024-10-05 04:40:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c77bd76a-7d4c-3794-bc60-b1180e6b3451 | -14.04466 | -46.3618 | 2024-10-05 04:40:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7e920cc-d0b6-37d9-bfe1-585554b08e30 | -15.27205 | -40.32412 | 2024-10-05 04:40:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c836294c-a50d-3f66-b7de-4f610d461a9f | -15.27153 | -40.32878 | 2024-10-05 04:40:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a8241372-ea79-34e8-9235-cf506eb84c6b | -18.56703 | -41.23176 | 2024-10-05 04:40:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7f7efd2e-7644-38fa-93da-9bde907ec945 | -18.5666 | -41.23598 | 2024-10-05 04:40:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ffb2e959-f13b-3ab6-98c7-ee9375688a9e | -17.87689 | -42.6834 | 2024-10-05 04:40:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 31c46206-a29a-3e70-b1ad-955ddba4fa06 | -17.87654 | -42.6866 | 2024-10-05 04:40:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a35dbca7-0da2-35c5-b1d1-ec0eb39a3382 | -17.62543 | -42.01764 | 2024-10-05 04:40:00 | NOAA-20 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 45659262-6f05-3836-a64c-1c3c48547631 | -17.61992 | -42.01699 | 2024-10-05 04:40:00 | NOAA-20 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 82254ba5-a2f9-34c0-8945-3f8955839461 | -19.02388 | -43.1809 | 2024-10-05 04:40:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 58bf1892-1e99-35f0-8c9f-5c4a570b5112 | -19.0149 | -43.16689 | 2024-10-05 04:40:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 969aaa51-8385-35c3-b787-7af39b9eaefa | -19.01451 | -43.17033 | 2024-10-05 04:40:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 57c71a98-634a-3da7-9c5e-acdbdc2a7266 | -18.64057 | -43.14227 | 2024-10-05 04:40:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 4504d1a9-b905-3914-9da5-46406ead314f | -18.64024 | -43.14531 | 2024-10-05 04:40:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| b73cc750-1908-3020-9d4e-3d528ef0e71b | -18.63989 | -43.14854 | 2024-10-05 04:40:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 4fdaa46a-b891-35d6-91d0-0ba3b82c88f6 | -18.55752 | -42.23523 | 2024-10-05 04:40:00 | NOAA-20 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0ae43d6d-cca6-335c-b9a5-8a434378da3e | -18.55199 | -42.23481 | 2024-10-05 04:40:00 | NOAA-20 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| f80ee71c-100d-3f41-b0ae-2a6898500f9d | -18.55157 | -42.2388 | 2024-10-05 04:40:00 | NOAA-20 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 2959f6ef-ad17-3dc7-866e-7fd2ffa7e286 | -18.55117 | -42.24262 | 2024-10-05 04:40:00 | NOAA-20 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| db52bb39-e8ce-3dfd-beda-d3e480f13d83 | -18.52206 | -42.25513 | 2024-10-05 04:40:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 60a7c6bb-333d-30e7-bd33-8dce1a28fe21 | -18.52169 | -42.25866 | 2024-10-05 04:40:00 | NOAA-20 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f938c968-7118-3d4f-b7a3-f2c1249158c7 | -18.41545 | -42.20509 | 2024-10-05 04:40:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b1f4b962-b532-3c03-a1d1-a89642be58d5 | -18.41507 | -42.20882 | 2024-10-05 04:40:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7c176455-7530-37f2-922b-47d81f4baeba | -15.75234 | -43.84353 | 2024-10-05 04:40:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 36ae22ab-b60f-37f1-bf91-c4de64848e8f | -16.34814 | -43.69696 | 2024-10-05 04:40:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e3c96f6-a45f-334b-8e31-971321e1baa4 | -15.95563 | -43.36141 | 2024-10-05 04:40:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 73cb9b45-62a8-38a4-b08c-e82de43decab | -15.95496 | -43.36713 | 2024-10-05 04:40:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 54ca6ba1-3682-3953-bf81-814a8205a4ef | -17.74148 | -43.82761 | 2024-10-05 04:40:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 78630655-9dc7-387c-8976-b7effa938ef1 | -17.69983 | -43.80053 | 2024-10-05 04:40:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 51826bc0-c76f-3d24-8fd6-9436285b2245 | -17.6992 | -43.80609 | 2024-10-05 04:40:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c5704ff-3840-3d5e-b281-73ed87c0e294 | -17.63541 | -44.31927 | 2024-10-05 04:40:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db1cdbdf-77a0-3187-8b94-7316fc2e68a7 | -17.63483 | -44.3242 | 2024-10-05 04:40:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89ebe1a0-80c7-32fd-813e-6002f431fc29 | -17.61883 | -43.26503 | 2024-10-05 04:40:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e3a4d01-68b1-3eda-a845-36a6fcf20ea1 | -17.61795 | -43.2572 | 2024-10-05 04:40:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 121d3bb5-7c0f-3195-b6eb-15252b51fc5f | -17.61765 | -43.2599 | 2024-10-05 04:40:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 359297e2-93b6-3c31-8cbe-b319e1af05b7 | -17.61736 | -43.26263 | 2024-10-05 04:40:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a4d2735-358e-3182-8ad7-55c6d3a4af68 | -17.61705 | -43.26545 | 2024-10-05 04:40:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96baaafa-43cb-3935-85f7-e504cd4753cf | -17.61466 | -43.25649 | 2024-10-05 04:40:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 015a5975-9889-395a-b59b-1586f1479d35 | -17.61435 | -43.25921 | 2024-10-05 04:40:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 580fdd41-ffa7-3a26-8c78-2b8250648dce | -17.61403 | -43.26192 | 2024-10-05 04:40:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 47e36ebd-fb27-3542-a0b2-8041a13b5d08 | -17.61372 | -43.26468 | 2024-10-05 04:40:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3214d48-081d-398c-b64a-73f4a7e24bbe | -19.46554 | -44.1374 | 2024-10-05 04:40:00 | NOAA-20 | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1a6b626-cbec-3b75-86b3-5c5c1d874147 | -19.23922 | -43.36621 | 2024-10-05 04:40:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9aec3961-5760-3a56-b088-b59eaf924d20 | -19.23884 | -43.36974 | 2024-10-05 04:40:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 790772fc-1977-3c08-b845-8d799d6cf9c7 | -19.23378 | -43.36823 | 2024-10-05 04:40:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b57faef-afca-3c37-9729-26177195ab5b | -19.23343 | -43.37161 | 2024-10-05 04:40:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0bf1888-74cd-3e70-956a-21d41cfd8bcb | -18.59759 | -43.95581 | 2024-10-05 04:40:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b03cbf24-5e7a-343e-b151-c2ef9d3d66db | -18.59579 | -43.95493 | 2024-10-05 04:40:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd2beb48-a4bb-366b-b8cc-1d65c7e8bfd2 | -18.5795 | -43.83476 | 2024-10-05 04:40:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd1daf9c-c86a-3ef3-be6e-95dac458fcd3 | -18.88022 | -43.59158 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c4421df4-c8a7-3fe2-91db-ce55ea43de71 | -18.8799 | -43.59459 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 10c4fafc-f8fb-30c0-9852-225898168b4a | -18.87958 | -43.59758 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| cccfce9d-2c90-3bae-a963-027568dde915 | -18.87926 | -43.60055 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 60ac61c8-8d4a-3537-b4fa-c60a700a250c | -18.87894 | -43.6035 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| e89c458d-1acc-3327-8949-91cdfea0eafd | -18.87539 | -43.58897 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 9035909a-0111-3d7a-8a7d-1c51d1d790e8 | -18.87506 | -43.59194 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7b3c95a5-a8d6-341c-9737-9a6447289b3e | -18.87475 | -43.59492 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 2515dc73-814e-31e0-b736-d1d76c98b904 | -18.87444 | -43.59782 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 360ae608-d71e-313b-92f1-f1295bb3be3f | -18.87413 | -43.60065 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7a688e21-5296-33f6-97c7-83d51b6e1490 | -18.87383 | -43.60345 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 4bf183cd-3509-3390-8aed-c01ba329f51b | -18.87144 | -43.58879 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e8aba44a-b444-3fa1-870a-b4de9a90c8cc | -18.8711 | -43.59175 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 671bf2eb-bdd9-34c0-8980-05e3c2b1502c | -18.87021 | -43.58947 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a5ba5cac-4919-3125-8c5d-a7ffcdc2d24a | -18.86989 | -43.59248 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 43356117-4e8e-34d8-9fa9-b47ffb159b51 | -18.86948 | -43.60593 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 67b7f99d-f32e-34bb-b350-0a78552e5b7e | -18.86916 | -43.60877 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| a8e804b2-dffa-3ad3-b522-65e16cfc11b7 | -18.86884 | -43.61156 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 4c0d5069-3571-3577-905c-f03199894554 | -18.86838 | -43.60662 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| a30257fb-1d52-308a-be04-38a63c1aab15 | -18.86808 | -43.60941 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 34884cb2-220d-3562-bf5f-9b46e6e23b0b | -18.86778 | -43.6122 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| d35226f2-5d36-3f75-a581-39beea4268d2 | -18.86659 | -43.58634 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b42ee771-44d6-3896-9978-d0ad498e7a82 | -18.86625 | -43.5894 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1cd1d87d-03bd-3f7c-99d3-7067aa0aff4d | -18.86569 | -43.58387 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b84a9695-b012-31ce-b457-3a185eb98f00 | -18.86536 | -43.58702 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cd0ad3ef-5f00-3778-95a5-18d6bd32271d | -18.86459 | -43.60397 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| cb59a1ca-207d-34e0-bcaf-0f7785417b54 | -18.86428 | -43.60663 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 82293020-bb72-3983-b463-146e031f2314 | -18.86399 | -43.60923 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 67a192df-95fe-3a44-9cf2-9f5095c02bd6 | -18.86377 | -43.60191 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7999d3f0-50d4-3e3c-98be-452c7c3f8192 | -18.86369 | -43.61187 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 779357e2-15c4-3850-b828-1b3b2f46756d | -18.86348 | -43.60468 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| eeda2262-9ebc-320d-8c36-19f4c8e7f5ab | -18.86338 | -43.61459 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| cddd0c60-4d98-35d7-b0b1-0e768499ef54 | -18.8632 | -43.60724 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 25476229-4fcc-3665-80b9-0303dad6eed2 | -18.86306 | -43.61739 | 2024-10-05 04:40:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4a8d2212-fa48-340a-ba91-5099b027c7d5 | -18.86236 | -43.61514 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| dbdf415a-d761-349f-ae70-db857f6ba1cb | -18.86184 | -43.58304 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 443778ab-b5e1-34c0-abbc-858cea4694b4 | -18.86146 | -43.58638 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 805379d1-bb22-3045-840e-e807520c657a | -18.86062 | -43.58337 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 62ecb53a-e747-38af-addd-565e77fe9d09 | -18.86026 | -43.5868 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a60213e1-361a-3bfc-bfef-3b281b5b4f16 | -18.85942 | -43.60433 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 35dee866-dcb0-30dc-8b75-e9701dc8e6b0 | -18.85648 | -43.58519 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 6c55d531-2e7d-3028-92a7-beecef785cec | -18.84574 | -43.58959 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 340e6bf4-0411-3910-834d-a4d716ab6408 | -18.8403 | -43.59242 | 2024-10-05 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 107b5d37-5ea8-302d-8acc-47dfe694b8c2 | -18.63394 | -43.20359 | 2024-10-05 04:40:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9040ad63-ff5d-359e-bcc0-d89258df69d7 | -18.09404 | -43.95789 | 2024-10-05 04:40:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6686c7ad-6227-3f7f-97d2-68d8e6eb184c | -18.0907 | -43.96111 | 2024-10-05 04:40:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README114.md)
