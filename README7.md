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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20862e92-e827-3385-bcba-ce84cebf31ff | -3.39537 | -54.27569 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9810d619-8f3d-3b71-82aa-76010d44978b | -3.45788 | -45.90002 | 2024-11-22 01:06:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 75.1 |
| b49035e4-4326-375f-82cb-540897fa23aa | -4.08144 | -49.2987 | 2024-11-22 01:06:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| da215d83-4666-3d42-90c6-625ab48889ad | -3.753 | -52.33084 | 2024-11-22 01:06:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 50338fbd-27df-3803-af25-1dbc5f18f01f | -3.28864 | -53.84165 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 994977c6-ab27-3311-8bba-73e5271795c3 | -1.25358 | -51.77894 | 2024-11-22 01:06:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| da3eb665-2d22-39c1-bd9c-93ecaea24f5f | -1.13015 | -53.40842 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 691094dd-f70a-3137-aeba-821b57ea68c6 | -3.00301 | -45.13382 | 2024-11-22 01:06:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 12bdb363-6d6f-357d-a2bd-0b84f16aa4ff | -2.58164 | -51.9222 | 2024-11-22 01:06:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5688bb27-0271-30a4-aa68-8c8463f16dad | -1.10862 | -51.92985 | 2024-11-22 01:06:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eb8883fe-010b-3757-a6e2-a7386e04489a | -2.94137 | -45.14886 | 2024-11-22 01:06:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 9ffc507f-ca3d-3f9b-b800-85cb9e84f31d | -1.23931 | -51.75079 | 2024-11-22 01:06:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 360f4466-0e72-3234-a289-25f3308ce186 | -0.30913 | -51.54961 | 2024-11-22 01:06:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 025ba145-0867-3542-9450-f3afb8314c1d | -3.28426 | -45.44533 | 2024-11-22 01:06:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 46.6 |
| b02e32c2-c252-35ff-90b5-46047da9808b | -2.00083 | -54.52062 | 2024-11-22 01:06:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b50aacd0-1ebd-392c-8759-0af889f388ee | -2.70848 | -45.24778 | 2024-11-22 01:06:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| b35215ef-c960-382c-9385-f6d70a71596f | -3.51537 | -54.69333 | 2024-11-22 01:06:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| d2a071da-2e91-35f0-b801-ee3e5eb9aead | -3.20041 | -54.33578 | 2024-11-22 01:06:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a2df0b34-2b20-3e9b-8183-2dde3d482a34 | -1.22914 | -51.7431 | 2024-11-22 01:06:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| b674bf3d-e804-3380-96c4-58cc9e2b8b64 | -3.1099 | -54.00242 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7188be3a-1b3f-3a71-b48b-055394c9ad2a | -1.63886 | -52.76603 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6413509a-dc98-357d-8325-8a5c88e2f42c | -3.57328 | -54.68552 | 2024-11-22 01:06:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 7a75f66f-c1c8-3e50-98e5-3b1e4a316ee6 | -3.75118 | -46.12651 | 2024-11-22 01:06:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| ca078cac-cec2-3d99-84c4-a101562be8f3 | -1.73231 | -52.71109 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| a1ae8021-c8e6-3fc3-b4a7-4f22fe0fb45b | -2.74017 | -54.12778 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| e6ceb191-11c0-386b-93c3-1dfc507a44af | -3.7663 | -46.11795 | 2024-11-22 01:06:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 9d0c89aa-fa26-397b-8b99-c7cc3649a26d | -3.43688 | -50.21452 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 8703a0cf-0f13-3ce7-86a8-03ea991693b8 | -2.95047 | -53.71985 | 2024-11-22 01:06:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d3a34c81-ab45-3e63-aa3e-aa42c0c37de7 | -5.08863 | -45.94325 | 2024-11-22 01:06:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f69502b0-f59f-31c0-b355-d90983fae40f | -4.24896 | -46.10724 | 2024-11-22 01:06:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 41.8 |
| e195c223-b1df-32ae-b1d5-66a901bcb3ec | -4.26229 | -48.70446 | 2024-11-22 01:06:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8cec134f-9939-352c-aeda-735b02b43454 | -3.3008 | -50.3544 | 2024-11-22 01:06:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ea4163ff-e530-3cfc-8844-9f51500e799b | -3.51495 | -53.80772 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 64710b94-380a-385e-948a-4df4116c4878 | -3.86243 | -49.9031 | 2024-11-22 01:06:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8d7676e5-d652-3d6b-979f-7a025bdcc1a6 | -2.69787 | -46.25821 | 2024-11-22 01:06:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| f8e51fe4-d91f-38f8-9d31-319f3c2afa92 | -4.25161 | -46.12501 | 2024-11-22 01:06:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 48.6 |
| c4dbdbdb-785a-365c-97fb-317cb76332f6 | -2.69517 | -46.23994 | 2024-11-22 01:06:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a6840cd8-34b9-3ef2-b272-0f5fc8cce885 | -4.57431 | -48.02338 | 2024-11-22 01:06:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d64429c6-35ba-3327-8b0c-18b2a6534702 | -3.32286 | -54.09387 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 87e5806f-ebbf-367c-94a7-6b631dd56000 | -5.24685 | -42.6287 | 2024-11-22 01:06:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 88ad3e6a-37dc-3eed-8d94-4310b9124720 | -3.73564 | -50.43647 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b66422a6-070b-3635-92f6-e65fee7fcdad | -3.44034 | -51.60422 | 2024-11-22 01:06:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d261ca23-bf69-3c4f-894d-7462b1a7f35a | -3.76093 | -46.10674 | 2024-11-22 01:06:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 40.1 |
| a6976815-5336-3ba2-8778-d62401c55c9a | -3.5044 | -53.79924 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| fca79944-ac35-3b36-ae46-350913313dcd | -1.67336 | -54.9921 | 2024-11-22 01:06:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7be5cd47-5e20-3d53-8c87-3542818fefae | -1.44067 | -53.39271 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 7cfe8b2c-7b9f-3025-94eb-0c62db752338 | -4.12006 | -51.06713 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f5098ec8-a3cc-3a85-bf45-b6b127957694 | -2.7076 | -46.23814 | 2024-11-22 01:06:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 1a99d9b1-4597-3b7c-b489-a09aa6c42067 | -1.25591 | -52.06596 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 30f3eecb-16c3-3c2d-af37-28b515cb321a | -3.14503 | -53.12944 | 2024-11-22 01:06:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| fca043af-12d1-329a-9fe5-bf06b70a48d9 | -3.86912 | -47.59114 | 2024-11-22 01:06:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| d460db7a-38d8-396f-9cc6-0777303faaa9 | -1.77417 | -53.6048 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 97491c19-108c-3970-9c72-fb6db881d280 | -1.51662 | -52.08289 | 2024-11-22 01:06:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a5aee0e9-0743-3847-9db7-e46b0c44e4a5 | -3.53469 | -51.10133 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 2c9421c4-5e8f-3dc0-896f-b0603e7f04d2 | -5.94816 | -48.05194 | 2024-11-22 01:06:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f0151d57-468c-3aff-8525-75437d0d8a89 | -2.70286 | -51.87214 | 2024-11-22 01:06:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 2ef7f12c-bfb0-386c-b09d-a45f7986ab67 | -3.58208 | -50.25668 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 51503c2c-8a2a-3832-8c81-6d79d4fab8da | -2.76609 | -54.059 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f8100ecf-37fd-375a-a1f3-3e187e1f8edf | -2.17663 | -52.12706 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7151ae04-4ab2-3cdb-bf01-151858fa66d9 | -3.34009 | -53.34109 | 2024-11-22 01:06:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| c80de139-4ebd-32ea-b6a4-6b669917e8ec | -2.20905 | -52.23026 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| fb620fc3-59cd-35fd-a6ce-5981edce0955 | -1.50547 | -53.13099 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e977ed1a-a631-324c-9205-03f883da32b0 | -3.64932 | -54.32495 | 2024-11-22 01:06:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 67aa6ac5-d8f3-3101-943e-da8c8bd1cbd8 | -0.77291 | -51.77386 | 2024-11-22 01:06:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bf852be5-68f0-3960-a275-410c8e62141d | -3.49257 | -49.96048 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 0aedcca9-8b6f-3102-8c89-29ca5c946977 | -3.76405 | -52.41045 | 2024-11-22 01:06:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fde3ed36-dde6-3114-8146-95d8cbfc056d | -3.85747 | -52.35526 | 2024-11-22 01:06:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| ab75f7a3-0e25-36ec-a7cb-76690fd7dfb2 | -3.96277 | -51.12927 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 5a5b0407-a0a0-3c53-ace5-c35b49cf0f30 | -0.64261 | -52.35723 | 2024-11-22 01:06:00 | TERRA_M-M | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a0cf3c9b-ec98-31be-b9a1-8f510eb1c9ed | -1.96355 | -48.3796 | 2024-11-22 01:06:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f6a5d193-1749-3c12-9ea9-36c32b9ae8a5 | -3.06538 | -53.28585 | 2024-11-22 01:06:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 8e4ebfc0-fc41-3cdc-bb88-9581236b0bc2 | -3.22557 | -54.24046 | 2024-11-22 01:06:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 7d54f053-8c9d-368c-a79a-103d027b6be5 | -1.19787 | -54.03244 | 2024-11-22 01:06:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a304943c-7ef4-3e3f-ac65-c45b83b960a4 | -3.54481 | -50.19312 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 981f9630-fb48-33fb-b0c2-0d868e0a66db | -1.59112 | -53.81115 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 694fd01e-50d7-3a86-a813-eb7a9ce9f1ed | -3.68572 | -54.59328 | 2024-11-22 01:06:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f1b591b0-352c-32f8-ac93-0b80bf302942 | -3.10267 | -54.29366 | 2024-11-22 01:06:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1455ae63-7a6c-367f-a5dd-d2d63797aea5 | -3.87304 | -47.59872 | 2024-11-22 01:06:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 8f700b1b-641a-37bc-84a8-0f5c62ebed99 | -3.22696 | -54.25049 | 2024-11-22 01:06:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 168.3 |
| 4d3fc4c4-b07b-307e-989d-71db5efca0b1 | -3.43034 | -50.03586 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1eeba3e3-2891-3bec-bad3-9f6248d69e5c | -6.26878 | -44.56358 | 2024-11-22 01:06:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 8f0cd635-c480-3e9d-a55b-c20b9be11b78 | -3.06005 | -45.69109 | 2024-11-22 01:06:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 86c82ccd-c516-3e28-8fe5-43c7fcf15487 | -1.90432 | -54.27999 | 2024-11-22 01:06:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f782682d-c2b3-314f-b4a9-8acb128f55fb | -1.91247 | -53.34181 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 772bbbed-1afb-3ad3-81c4-863963d986ba | -2.50453 | -48.99962 | 2024-11-22 01:06:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| d8c5eaa2-e44e-35ec-aff0-77ec45caf808 | -3.30946 | -52.85573 | 2024-11-22 01:06:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 32be2c56-1c50-39b3-b882-73ca065da367 | -1.80901 | -48.7788 | 2024-11-22 01:06:00 | TERRA_M-M | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9a2eac06-0522-3f01-aec7-b8d6549ab537 | -2.60956 | -48.24293 | 2024-11-22 01:06:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ab33d72e-74b9-36af-bf00-a8ed783ae089 | -4.19004 | -47.90823 | 2024-11-22 01:06:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c009f14f-7aba-31c1-8c4b-6c18bdd8b9c5 | -3.51243 | -50.80974 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d7a9d612-12dc-3513-9ce8-957a90fedc21 | -1.78507 | -53.61609 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 362f565d-a134-34ae-8c27-3fe71d8bd231 | -0.40883 | -51.60399 | 2024-11-22 01:06:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d1caebeb-6049-3aad-9eb8-a0891c366e66 | -1.19666 | -51.96586 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e7c773f2-2e74-342a-8872-a42796cc8a88 | -0.04456 | -51.23686 | 2024-11-22 01:06:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a822020e-3f6d-3107-9c74-cae3dbd99c88 | 0.16837 | -51.23111 | 2024-11-22 01:06:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 411ae118-c734-3ca9-83ad-619b5ba83787 | -2.15932 | -53.79009 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 01d9cb53-2965-3e00-bad5-b754e41de152 | -3.76351 | -46.12477 | 2024-11-22 01:06:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 71ce8cdb-5dff-35ee-b9c3-1f69d29dbf74 | -3.52283 | -53.79684 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 3aae6d4f-7f4a-3db1-9645-3c23d02b89de | -5.0922 | -45.93678 | 2024-11-22 01:06:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 267cc8bf-be0e-3127-8947-3155979fa922 | -3.21759 | -54.25184 | 2024-11-22 01:06:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |


[Clique aqui para ver as próximas entradas](README8.md)
