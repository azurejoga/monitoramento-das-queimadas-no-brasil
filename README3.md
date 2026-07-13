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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4dc1c948-7611-37d7-b7d6-80ef5716b291 | -5.9822 | -43.62099 | 2026-07-13 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 171165af-2019-3386-99db-c188791f7847 | -4.92502 | -41.97836 | 2026-07-13 03:36:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e7c1fa9b-cf5c-31d6-94b4-b44f1f020e52 | -5.79299 | -45.11577 | 2026-07-13 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 35aa2156-8179-3159-ba61-83c4164458c1 | -6.89845 | -43.71016 | 2026-07-13 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b22bd41e-0be5-3064-9716-1b4931515905 | -6.94667 | -43.71867 | 2026-07-13 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4305d034-a779-3453-9071-f1b55c22d4f8 | -6.89913 | -43.70627 | 2026-07-13 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94a1746c-ef81-3f58-9ae7-b2a946d618e1 | -5.8001 | -45.11198 | 2026-07-13 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 046acf11-a4fd-3ea3-a59d-a2d9b7a81689 | -4.92372 | -41.9773 | 2026-07-13 03:36:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a3eddfdc-9caf-38de-a0ab-b648e2e690ac | -5.75002 | -43.26584 | 2026-07-13 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| aaf9bab6-61dc-34cd-b97a-dff9c1137664 | -5.97651 | -43.62008 | 2026-07-13 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53b5466e-304a-3903-a516-daa3dab4818e | -6.94734 | -43.7149 | 2026-07-13 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6e72576d-2033-3925-9ed1-edbd289469a7 | -6.9516 | -43.72355 | 2026-07-13 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a88bd4a9-3018-3aa5-8b91-913ff3960a75 | -6.94599 | -43.72245 | 2026-07-13 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b4cb77e-43f0-31bc-a716-6fe6137c2eb4 | -6.89602 | -43.70988 | 2026-07-13 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db2733d5-907e-301d-b2fc-499629a5e355 | -5.74936 | -43.26962 | 2026-07-13 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9f13d870-465f-3629-b7fa-4f628fa165b5 | -5.79778 | -45.11103 | 2026-07-13 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 03c31c48-bb16-3385-8f94-e64335f3af2a | -6.49142 | -42.22414 | 2026-07-13 03:36:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 167cd3c8-eb69-3ef2-8496-2fee68e38af6 | -6.90237 | -43.70687 | 2026-07-13 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5480c2b-2025-35c2-adf7-d5c906d88ed6 | -6.95227 | -43.71978 | 2026-07-13 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5cb7e29f-fefc-3f33-9d3d-51120fb89231 | -5.79686 | -45.11608 | 2026-07-13 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 62848cf5-44f9-3d00-b981-aab55c969b2e | -6.6689 | -39.16166 | 2026-07-13 03:36:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 39f87014-cb43-39fb-be4e-4b2a4e0e56b6 | -5.79922 | -45.11702 | 2026-07-13 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ae291d06-3ed7-318a-b132-cc26e656a23b | -6.49197 | -42.22092 | 2026-07-13 03:36:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 0430c2ae-a3d6-3cdd-b116-57f31dd4dd99 | -9.36635 | -46.72681 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c71d3ea2-55ea-3f5a-a632-8906b34209f1 | -13.7631 | -46.25034 | 2026-07-13 03:38:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 768cac43-9a56-3641-bd30-871f12361ae8 | -13.75739 | -46.2563 | 2026-07-13 03:38:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e5dbeb6-a6ad-3bf2-8396-5e2c099ddb4f | -13.96781 | -38.94485 | 2026-07-13 03:38:00 | NOAA-21 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 62cd561d-b93f-3c7d-8289-266e3c74349c | -9.35915 | -46.7324 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5f34d334-579d-3561-bd70-92dd3ab66fee | -11.78521 | -41.19809 | 2026-07-13 03:38:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 83385348-0f8a-3f03-853c-46d774ed4829 | -13.7622 | -46.25469 | 2026-07-13 03:38:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 33392fb1-a004-317c-8dfd-fd01ca8268e3 | -13.75822 | -46.25214 | 2026-07-13 03:38:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9caed900-f36f-31f4-a6b1-5421f1915c5a | -9.35652 | -46.74242 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5b24b30d-29f3-3bbe-80f3-5ee66efb8653 | -13.9649 | -38.93972 | 2026-07-13 03:38:00 | NOAA-21 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e7728539-15ab-3efb-823b-b75cf1575084 | -15.3351 | -42.90673 | 2026-07-13 03:38:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e16094c3-fba5-33f6-9b70-346237cd7ac8 | -9.35158 | -46.73674 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc7e8dd9-be2c-3d80-bf69-6f2d7204af8e | -9.37727 | -46.70559 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 27a2003e-a0b7-39e3-9ba9-17d4b3eaba1a | -9.3619 | -46.74938 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 67905bb2-81f8-39ef-b796-611b199bf229 | -8.08307 | -47.09819 | 2026-07-13 03:38:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6503ce13-83af-30f8-b6a0-025daeb0864b | -14.64818 | -45.87099 | 2026-07-13 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c976748-7d3e-35e1-a5a1-b43bd03f7a82 | -9.35589 | -46.74953 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 377f9a09-88a3-3d19-9538-5c6a2d665a94 | -13.19501 | -48.32586 | 2026-07-13 03:38:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 181268a1-ba2b-3cbf-9f57-a8d902bd2afe | -9.63998 | -40.59615 | 2026-07-13 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| d0bd5e72-2b8e-39af-bcdf-df43dc904146 | -9.35048 | -46.7425 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50b0bcd8-bb8e-381c-8dbd-2e282cc28c1f | -10.56455 | -45.69328 | 2026-07-13 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94b4a740-f76e-32ca-8697-474689bef305 | -8.13119 | -47.87316 | 2026-07-13 03:38:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9783e164-c25a-30cf-96c4-56798af6c4c1 | -9.35765 | -46.73667 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 47cd3503-63bd-39f5-b25d-d0d9a5192795 | -9.35539 | -46.74813 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1440d283-d88b-3d45-b56d-8d867b3fff20 | -8.08994 | -47.09898 | 2026-07-13 03:38:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e19d2627-0a22-3e1e-a084-e65cce8fa477 | -10.82276 | -45.13365 | 2026-07-13 03:38:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 56ceba7a-d0d7-3dab-a833-032b8242fc77 | -9.38042 | -46.72385 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 74be898a-b887-366e-b814-9173ba0721b8 | -10.56366 | -45.69783 | 2026-07-13 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd46b86e-c10c-35d7-9833-6129fec03c5e | -8.12977 | -47.88025 | 2026-07-13 03:38:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f6f5819a-f372-33f6-8d94-75b05c4fe84e | -9.38802 | -46.7195 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e0fa5ab1-ef23-3b8e-8cfe-f19b36f3ea19 | -8.09116 | -47.09255 | 2026-07-13 03:38:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba38385f-6b27-3b60-adb8-a158431032c7 | -9.43364 | -40.71315 | 2026-07-13 03:38:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c890264d-7931-391a-b30d-6b43686e7d5a | -9.38154 | -46.71816 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bddd9550-b157-3c6f-9828-97d6190fadfd | -13.7566 | -46.25224 | 2026-07-13 03:38:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8616f731-346b-3eab-8f38-9df8aae539b9 | -8.09143 | -47.10038 | 2026-07-13 03:38:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 120d17be-e305-3de4-8719-28b75ebef6ec | -8.08589 | -47.09275 | 2026-07-13 03:38:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f249a3d5-417b-3912-bfcb-6c265b803715 | -11.78147 | -41.19698 | 2026-07-13 03:38:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e38ed482-ca91-3589-aa69-798ce2871354 | -10.47768 | -42.42343 | 2026-07-13 03:38:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 7459eaa4-ceed-3f48-911b-75c2f2de9e78 | -8.08459 | -47.09937 | 2026-07-13 03:38:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3ac91a9-40bd-3f8a-a4cc-5f5ec77e10df | -10.81697 | -45.13269 | 2026-07-13 03:38:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 270a1352-2862-3b4a-b390-5b7578264431 | -8.12638 | -47.87627 | 2026-07-13 03:38:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 48ac7b76-81f7-32a5-8ba8-bdd68e7bd8e4 | -9.42924 | -40.71236 | 2026-07-13 03:38:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| aa01e591-95ea-32fb-b549-9524f463b2de | -9.3667 | -46.72819 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e8fbb448-e14c-33c1-bfa8-cd62199046ef | -9.63922 | -40.60042 | 2026-07-13 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d3d2011b-dc25-388f-acf0-5e6b41291b59 | -9.35481 | -46.7552 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c156a3b7-10e7-3d0a-a9d7-e15ed8ebf6d7 | -13.96045 | -38.94352 | 2026-07-13 03:38:00 | NOAA-21 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 6ed20f1e-b7ec-382f-9a16-b172c8a9b264 | -10.67526 | -38.28108 | 2026-07-13 03:38:00 | NOAA-21 | HELIÓPOLIS | BAHIA | Brasil | 2911857 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 32e515a2-e287-3087-b36d-d71168bc1b3c | -10.8228 | -45.13689 | 2026-07-13 03:38:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fcbf9fa2-48ff-3a39-b695-c24775b1f1fd | -9.36562 | -46.73383 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 58017689-ae88-3edf-8afe-5aa9c6f6db78 | -9.35002 | -46.74112 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d9a3864c-6371-3290-86cc-13826ffe0463 | -13.19757 | -48.33144 | 2026-07-13 03:38:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a10024e-83d5-34a9-a433-9880c0136580 | -9.37394 | -46.72253 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ea517f7a-3594-3735-bd53-55f359bbe04a | -9.35697 | -46.74384 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0cca369e-1603-3f51-a61f-fc3471a0e808 | -9.35877 | -46.73103 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b04d2ee2-5583-396f-8a44-63e2992b74bf | -14.6546 | -45.86825 | 2026-07-13 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a28dab1-04e7-37ff-9ded-482e2e3a842a | -13.76474 | -46.25006 | 2026-07-13 03:38:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7ddf328-8a9c-306f-bb8d-c090e954ad1d | -10.82197 | -45.1378 | 2026-07-13 03:38:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9bab9cfc-d7f4-3eeb-9686-5d0f311c0c03 | -8.09275 | -47.0936 | 2026-07-13 03:38:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ae3af0e3-1b7a-3c38-8b04-cb073aea0f0c | -15.73582 | -42.27504 | 2026-07-13 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5bf20358-95c3-3fc3-a8a3-2eabd0d0e922 | -9.36524 | -46.73245 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cb4ee23a-6bc6-3aa5-982d-420be8181ecb | -10.81616 | -45.13694 | 2026-07-13 03:38:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 90bbf3a8-0d22-3969-89d9-7e0f6bb7e795 | -13.75907 | -46.24788 | 2026-07-13 03:38:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0439a5aa-2221-3141-bc4e-a66307e3a6c4 | -14.6538 | -45.87218 | 2026-07-13 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e373f592-1bca-3e3c-b8f8-3730901aa2fd | -9.35807 | -46.73807 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f698ffdf-cdf8-3a1b-a343-0721971baf5c | -9.34398 | -46.7412 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 913ad393-e12f-3e38-8c9f-5838fe80dc43 | -13.19881 | -48.32554 | 2026-07-13 03:38:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 56409de8-841b-33e7-9835-3ec076e2afcb | -9.63486 | -40.59967 | 2026-07-13 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 4955976e-d3f3-3961-a28b-1c0c8fd8e5cc | -13.96413 | -38.94418 | 2026-07-13 03:38:00 | NOAA-21 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| eadf747e-ecf8-3040-aca9-3cddc2d13d2f | -9.37282 | -46.7282 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c2faec38-4649-35bb-9fc5-ccb4519b9069 | -9.35427 | -46.7538 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8da15e33-1768-33a6-a569-f5c64a19bec9 | -9.37838 | -46.69991 | 2026-07-13 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 137b9eac-0e9d-3c2e-8403-d7b914383b86 | -8.13349 | -47.8775 | 2026-07-13 03:38:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 607633ae-1a8f-391a-ae8f-6b5873378e65 | -10.48054 | -42.42558 | 2026-07-13 03:38:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 19661877-b97a-3e60-aea1-14f1508e1591 | -19.31143 | -41.39822 | 2026-07-13 03:40:00 | NOAA-21 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 35279aa6-71f3-3bf7-b42d-2d0c2e514150 | -19.83441 | -40.25719 | 2026-07-13 03:40:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 14485cbd-543f-3237-abbf-1d47766a2e78 | -18.23556 | -43.35416 | 2026-07-13 03:40:00 | NOAA-21 | SÃO GONÇALO DO RIO PRETO | MINAS GERAIS | Brasil | 3125507 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28d40e0c-e2b0-3004-b134-67ce372da8a5 | -17.12062 | -40.36285 | 2026-07-13 03:40:00 | NOAA-21 | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |


[Clique aqui para ver as próximas entradas](README4.md)
