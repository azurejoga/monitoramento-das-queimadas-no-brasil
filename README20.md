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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2520ae10-78d2-3a1e-92a7-9b3ae0d04058 | -13.12813 | -47.43754 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0aeb7e6f-056d-3a83-9dc6-d08bb535096d | -11.8403 | -45.01426 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 417b3d5c-e10a-3499-aac4-620ea4bedf59 | -12.39134 | -44.76722 | 2025-10-01 03:30:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41316041-1301-307b-96ea-c8b5f89ca9f7 | -13.77232 | -47.96929 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| fbb7ad0d-5f32-37f4-9f14-37d5b10b2787 | -12.8388 | -47.04362 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c337a2a5-e85f-3334-88bc-ce8a140eabd1 | -12.88321 | -44.68833 | 2025-10-01 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e4eb500f-bbb0-34bb-98d5-5573ab3f2b7f | -12.75838 | -46.91736 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83a7e0a5-1285-3c54-b936-62835ecd1b3e | -12.78329 | -46.86675 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f7dc9291-636b-3000-9b68-168b89957203 | -8.54648 | -44.64716 | 2025-10-01 03:30:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| da189881-b934-3066-b3a8-4b87ac31cee2 | -10.90374 | -46.5168 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 30a8e8cd-2d2d-369c-af80-c4650a10bb6d | -10.90292 | -46.55192 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 46649131-03c6-330e-b5e2-4b1648c1f0bd | -13.82191 | -47.4649 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d61897ba-c300-3675-98d4-6bf2fa77a6f3 | -11.46125 | -45.08234 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 55f0c06c-2727-3388-b771-fbb66ea773f9 | -11.83432 | -44.9799 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3bce4d6b-c37f-3146-bd96-263ce2865138 | -11.68501 | -44.29825 | 2025-10-01 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7badab3e-dfe2-3724-b7dc-d1b880d89106 | -8.53652 | -44.70049 | 2025-10-01 03:30:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6de25790-c971-348a-81b7-53e9171da913 | -14.05288 | -45.02435 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 628ccacb-ff05-353c-8f4f-52099537faba | -12.58639 | -41.29081 | 2025-10-01 03:30:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d97257c3-c392-368b-85c3-73cc83e6bfae | -11.81175 | -44.99549 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ae12b26d-7b86-3c0f-b7a3-25fff63693a1 | -11.76502 | -46.87618 | 2025-10-01 03:30:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 463b189a-483d-3458-b526-1bdac2f29689 | -13.21687 | -47.34702 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 45479441-3f56-35bd-95e6-4749b0dcb4e1 | -11.62553 | -47.49939 | 2025-10-01 03:30:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 56f27706-d54e-3980-a8cf-8a25feb87922 | -11.39311 | -44.90257 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0738c078-0674-39db-9120-5275b82fc85f | -13.65863 | -48.04522 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1ecf728f-87ca-344e-9fc9-1c2e28c5c77c | -11.99957 | -46.64666 | 2025-10-01 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe9cc717-9e4f-38e2-93d3-6165e62e5472 | -10.81386 | -46.63778 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b0902d8c-8d34-3aaa-ad88-b7762f6cfc93 | -13.3268 | -47.85378 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 528395a9-5ac4-399b-b230-5ef96365a9b8 | -14.18251 | -46.13407 | 2025-10-01 03:30:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 446c2440-14d1-3019-a47e-9758737cfe66 | -12.83858 | -46.87729 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a419a165-c559-3082-8a7f-f31af778a1a9 | -13.58947 | -48.04281 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a8b42045-86b0-3b3c-bfff-935bb629c6ba | -9.92753 | -43.69331 | 2025-10-01 03:30:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31cbdc47-d9f2-3de2-9d43-f42346adc914 | -11.81024 | -44.98109 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f2f99038-ef18-3d1e-96a8-d4ed4b19aa92 | -12.95028 | -46.41745 | 2025-10-01 03:30:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 56eecc94-a85b-353b-9095-341d5b2c783e | -14.70569 | -42.31941 | 2025-10-01 03:30:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3af205dc-c592-30be-82e3-a383bd8e32fb | -10.97715 | -46.54066 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c51eda0f-0f1b-3bfc-aa96-b7105e4c033e | -13.32777 | -47.33725 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5d348922-4a53-3b79-8ea1-6dad23571b7b | -14.21488 | -46.107 | 2025-10-01 03:30:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1335d707-67c2-3213-987d-4776a33d2590 | -13.46256 | -44.37613 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5392a3c4-4b34-3788-b587-b128060c68ca | -12.83933 | -47.04153 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 588eab44-24ce-3382-9968-ccd78f8ae227 | -10.9052 | -46.58002 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e3f7172-ce52-3834-ac24-957da148a1c6 | -12.66149 | -46.87026 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96d09b38-7674-3360-a715-f5a828558f3a | -8.56211 | -44.70688 | 2025-10-01 03:30:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4d3ec3c6-2a79-345e-9c68-540f3e55e009 | -10.73669 | -45.38466 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 085ebea2-4c4e-33b9-95c1-5c47ae79c0a9 | -9.9233 | -43.68338 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eed08ed9-32f2-3b71-9ee9-3ef9d3e8834f | -10.90639 | -46.53895 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 838103cb-1ea6-3f68-b0d2-39eadfd89110 | -11.84146 | -45.00851 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96cfeeab-8618-3c28-9c67-c50881f0097b | -14.18384 | -46.12783 | 2025-10-01 03:30:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| abc907aa-00de-3434-852a-b3f77b5b7aab | -13.33425 | -47.82032 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1b22064e-198c-36ef-9331-f97e9b6ece5a | -12.78128 | -46.87904 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6a221b6-29ff-39e8-a509-4b696c2f2aae | -11.94447 | -43.92224 | 2025-10-01 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20fa3d32-bcd5-3c27-a89e-c5f06cae9b3d | -10.90863 | -46.52484 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94ab001a-40b7-3ac4-a14f-a1667f818c89 | -11.44866 | -43.51038 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90060102-5589-3168-8947-815232e4e3d3 | -8.55254 | -44.72188 | 2025-10-01 03:30:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b57aa5f4-1776-3fd9-8f2c-689ee79cace8 | -8.5385 | -44.68991 | 2025-10-01 03:30:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c6e253d-6b4d-3f01-90f1-3d05a92b9ab9 | -11.4597 | -44.97655 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c20937d4-9fcc-3f21-921f-50c072e1c1f0 | -13.20953 | -47.3474 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4810f32c-aa72-34c9-975a-33707a8dd1b4 | -10.32865 | -42.46172 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7eb78db9-4a1f-38eb-b26a-f33f64a79908 | -9.93344 | -43.66272 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5275102-76dd-31d4-9e85-bb6beb43a408 | -11.38687 | -44.90141 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba69cc95-26bf-3dbf-b747-91a88439b784 | -12.41428 | -44.09818 | 2025-10-01 03:30:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87920ffb-81d8-3d05-91f5-0c91f39342fc | -11.64983 | -45.3247 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc96d7ff-f840-34e2-ac9b-7aa2aee4c4d4 | -13.33002 | -47.87281 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c805d517-90f6-356b-9430-e6ae97343290 | -9.92837 | -43.65723 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c28fd4d2-241b-3ea1-937c-b4dc90314274 | -13.31768 | -47.34425 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7c21a197-eff3-31a0-991c-fa39edcde57f | -9.92923 | -43.6845 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d645b5b-427a-3643-a37d-f8a4eb1aff6b | -12.87443 | -46.77566 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 051f07f5-b6be-3cae-bfc0-626dc76d08fd | -13.6568 | -48.08735 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c290290-af52-3193-b974-30440586d92a | -13.58179 | -48.04364 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7bc0dce8-e3ec-3dda-88b9-76f5b48a8fb9 | -12.58155 | -41.28984 | 2025-10-01 03:30:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 865171ce-f210-3c2f-b6c2-3ab535c0934c | -11.94041 | -43.91226 | 2025-10-01 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcdbfd06-faaa-33a7-bdb3-7b48d9886a83 | -10.81549 | -46.63619 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01040ebf-08bd-3036-9c10-8d7097f1da7c | -11.76381 | -46.84761 | 2025-10-01 03:30:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 509b1914-685a-3961-a5d4-4c0d15a8102c | -8.55259 | -44.7564 | 2025-10-01 03:30:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f3972285-f0aa-36f5-9933-4c6c55be3bf4 | -10.73732 | -45.38367 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa8d9ce7-3dd9-3e69-9bfe-74059d4ef471 | -12.87537 | -46.90502 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9206c84b-dba7-3edf-a5d8-ee6b7c3d6d5c | -11.46026 | -45.10137 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b8c3e052-029c-382c-8252-5577db570354 | -12.66757 | -46.87196 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13974cd4-ad3f-3ced-8ff8-795073bcd1d7 | -11.48568 | -43.50997 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6b14dfc-aced-3d9a-b224-0143e4f47344 | -11.81123 | -44.97607 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c5ec16fa-31a2-377f-95c0-2b419f7174a4 | -11.44923 | -43.51437 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd766ee4-e020-37fd-9bb1-bf7d5c870d2a | -12.35724 | -43.21523 | 2025-10-01 03:30:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad32e676-19b1-3bfc-bd95-ae95048a15c2 | -11.9982 | -46.65315 | 2025-10-01 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de493dbb-ea8c-3ce4-b2f2-1bc8d5531583 | -14.19017 | -46.12935 | 2025-10-01 03:30:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 984e02f6-40e3-397e-8a72-3a279a645cb4 | -13.97544 | -44.91683 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38727a0b-836f-32c3-be6a-5212a0d0b1b6 | -11.46649 | -45.08893 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 87d0ef80-9142-3376-88f3-c574cadc3141 | -11.3799 | -45.06409 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 91d36bc5-68de-306c-91d6-280fa2984469 | -13.52471 | -44.85374 | 2025-10-01 03:30:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf7a3cde-1cbf-3a55-b227-3896de451711 | -9.92838 | -43.6889 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 492db519-901a-3fda-b55e-844c43fb3045 | -10.96898 | -46.54541 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21d62d15-cb5f-3399-93fc-1d56113d818d | -14.70508 | -42.32245 | 2025-10-01 03:30:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 828f3d3e-e2e3-3945-b73e-7b1a1e85c2b7 | -12.84923 | -47.02868 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c1d2fe7-cd03-328f-9c27-4b59e469b2fb | -10.77308 | -45.37128 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc03d3f8-32cc-3933-9cd4-e7e169758eca | -13.98137 | -44.91816 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 64644d35-8757-3d1d-9808-64daf3ffbcd1 | -11.81282 | -44.99026 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2bec902d-729f-30a8-a62e-1d77d9eee677 | -10.81503 | -45.36322 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6eb1a1b4-05a4-3096-be75-e8bef9536043 | -11.19055 | -47.20162 | 2025-10-01 03:30:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc188ad3-4d68-38d5-abe2-ceb42227d276 | -11.80975 | -44.97366 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5879a048-0316-3ef8-b4fe-06072b4ae011 | -8.22869 | -45.51447 | 2025-10-01 03:30:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 64b1d5e6-28ad-3f0d-b599-5de64513df86 | -8.89708 | -45.05204 | 2025-10-01 03:30:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f285716-09eb-3d2a-9d6a-4ad29e9c2134 | -9.92585 | -43.67025 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README21.md)
