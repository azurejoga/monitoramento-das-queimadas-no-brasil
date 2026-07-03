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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed496dd3-3d2c-3654-a647-5483ceb4220f | -10.12219 | -52.0963 | 2026-07-03 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1b67fe6-56dd-3ddf-922d-e2f0d758bf8d | -11.63094 | -59.01733 | 2026-07-03 05:06:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d039aa93-cacb-3ee7-9edd-ae434075ee79 | -9.0267 | -59.53636 | 2026-07-03 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcab31e9-8bfc-3d90-9024-179d27ec320e | -9.17952 | -58.07013 | 2026-07-03 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a64d690a-0f40-36f9-a4e3-5a824a1d88bc | -8.69622 | -54.58025 | 2026-07-03 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 500279fd-2f2d-3490-b89e-d4e90201adb4 | -12.75455 | -44.52851 | 2026-07-03 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 7b409b0e-7a77-32cc-916b-9d2f903fb5a9 | -10.30191 | -57.12946 | 2026-07-03 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 335d3563-b6f3-395d-bf33-26d587f17deb | -11.41408 | -56.06026 | 2026-07-03 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 69842954-967b-3806-a326-85a32eeb8a1f | -9.18069 | -58.06277 | 2026-07-03 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f2a2ee5-066a-3530-803f-30e7af2035c8 | -11.43523 | -46.5364 | 2026-07-03 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 366d241d-11e6-3598-91d1-d1735e8f19c1 | -11.35355 | -55.40518 | 2026-07-03 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 578a8cd3-e5f6-3e31-a3fa-77ee74d4441f | -10.82151 | -58.01869 | 2026-07-03 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bf2a776-3a3d-3885-8298-16732587ea3b | -10.94765 | -43.04689 | 2026-07-03 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.8 |
| b0059ab6-8104-32bd-9e4b-b346bc889606 | -11.31299 | -54.47357 | 2026-07-03 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9a14fdb-7a33-394f-a1af-e3b6ee73809b | -10.78841 | -54.10567 | 2026-07-03 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f0c3f80-f0c6-33f6-8d82-c787d9a483d0 | -11.88747 | -57.11004 | 2026-07-03 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a25dd3aa-1e23-3f29-beeb-466b9eeac1c6 | -9.02309 | -59.53577 | 2026-07-03 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ca17b40-f9a2-3a3a-bdef-2cedff3af12c | -12.74755 | -44.52038 | 2026-07-03 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 78021787-2a63-3a5c-b70f-36c00e8fcdf9 | -11.35301 | -55.40881 | 2026-07-03 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0a8665a-4763-3e06-9901-0eb084d0ab11 | -9.95506 | -49.28237 | 2026-07-03 05:06:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b30a32a-2758-3927-933b-2d0543bf65c7 | -11.63499 | -59.01408 | 2026-07-03 05:06:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 398a459c-7ef2-3175-bbfa-6d7352e7d56c | -12.75582 | -44.5171 | 2026-07-03 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 7bbf550a-493f-3007-a098-a19a40ba9bd0 | -11.6275 | -59.01675 | 2026-07-03 05:06:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73ce6b4c-2bd2-3b6a-91cc-010c460de130 | -10.12923 | -52.10236 | 2026-07-03 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ec3ecb9a-8ad5-3c16-bff8-0efad289a516 | -12.75414 | -44.52124 | 2026-07-03 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 9d113aa3-98d6-365a-aacd-45466bdb530c | -10.58398 | -55.41638 | 2026-07-03 05:06:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ad8ea87-3ef1-30ea-918f-2416d770959d | -12.75293 | -44.53277 | 2026-07-03 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| e4ee5166-0914-3735-b58d-49deffdd4fa2 | -13.99003 | -47.44255 | 2026-07-03 05:06:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4305206-f03d-3e17-82db-ea048f2a45d8 | -12.75473 | -44.51556 | 2026-07-03 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 3e4fbf86-8163-3a00-92a1-7dbeb469f8e6 | -11.3452 | -55.41502 | 2026-07-03 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd1d5eaf-70eb-3f87-976e-4298799d3bfb | -13.30102 | -43.55566 | 2026-07-03 05:06:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3dd9413d-74a6-3837-9992-e1e4b8a0f68d | -10.90313 | -56.85375 | 2026-07-03 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ba1d648-b7e6-3440-a48b-c883f3274f3d | -12.75172 | -44.54435 | 2026-07-03 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1c965daf-8255-3a2f-b1c9-8bfbc8147811 | -11.35528 | -55.41661 | 2026-07-03 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5de9fb1-9663-3af4-a035-c6da7d1cae72 | -9.25895 | -57.86507 | 2026-07-03 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 567ad908-f04d-3b7e-98b6-2a3ed5e3b9a6 | -11.62892 | -50.36803 | 2026-07-03 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4a8c592-308c-3525-a2ae-432c6b24d3e4 | -10.94614 | -43.06059 | 2026-07-03 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 3dfa9cca-8288-3c4f-82b6-cc60d3ce4bf1 | -12.42852 | -58.41652 | 2026-07-03 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f8f1ee5f-001d-3aa7-b11b-0a567ef390ec | -9.18746 | -58.07121 | 2026-07-03 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f6f8f3b-bec6-3cc2-b616-2e072e1e88de | -9.75848 | -47.881 | 2026-07-03 05:06:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2525df3c-63d2-396c-a446-ccd7ee8e09ce | -8.70974 | -54.58235 | 2026-07-03 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| eb053fa9-7755-3ef2-a71b-3de0e51c2bd0 | -9.18981 | -58.04917 | 2026-07-03 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa938354-6e9c-34db-84bc-91f6af2201ba | -11.35973 | -55.40984 | 2026-07-03 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b2dda29-3507-32dc-8697-3d14bc392d00 | -10.9418 | -43.0541 | 2026-07-03 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 59a11e01-62d1-3ebb-9407-5bc37e650979 | -11.3541 | -55.40154 | 2026-07-03 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 105090fe-5d6a-3b0a-bed3-b5e543578d8a | -14.18734 | -58.76901 | 2026-07-03 05:06:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edc90c8e-880a-3f69-85e5-f99031f0af81 | -12.74924 | -44.51626 | 2026-07-03 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 53049e6b-43af-31ef-9c25-48230a578c41 | -11.56164 | -52.80187 | 2026-07-03 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcd01fef-84d7-3957-b203-3dc1970ed5fd | -11.41794 | -56.05727 | 2026-07-03 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a2d00dc-1fe0-3c7f-a1f7-e0c9e1e5ef70 | -12.67057 | -48.2197 | 2026-07-03 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 792316a8-a683-3b9f-a0f6-9e46d1753829 | -9.02601 | -59.54058 | 2026-07-03 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fea19dde-405d-33a3-9d62-78d5297a5881 | -11.36309 | -55.41036 | 2026-07-03 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40e05ed2-0bc5-36d3-8451-6752ce49055d | -11.3491 | -55.41193 | 2026-07-03 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c26f2256-81ee-3910-aa7f-3aff3796c754 | -10.94803 | -43.0618 | 2026-07-03 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 6df9aa11-bd86-36d3-8b2e-427892cdffa8 | -11.62688 | -59.02058 | 2026-07-03 05:06:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ccdf6ad-207d-3309-8840-e6e67c56f943 | -8.70298 | -54.5813 | 2026-07-03 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 712c67d5-f07d-3810-bd14-df4eb4bc37dd | -11.44096 | -46.53706 | 2026-07-03 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b229a6bf-edf7-33f2-ab30-367066300540 | -12.49742 | -43.80909 | 2026-07-03 05:06:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8aec1862-869d-3992-a62b-8427aa3a79a2 | -10.12357 | -52.08649 | 2026-07-03 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e409c596-6912-3f8f-b715-694bcea64dd9 | -11.92004 | -43.38529 | 2026-07-03 05:06:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f83b2aa7-8333-3da4-be92-b3b7ed840e5f | -11.8487 | -48.24533 | 2026-07-03 05:06:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3bca95b5-92e7-3b05-932c-f9f637b5a3cd | -11.84908 | -48.24224 | 2026-07-03 05:06:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e15cbea1-2f2e-390e-8fc8-3e353cc2ce1f | -11.44049 | -46.54086 | 2026-07-03 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| b4ab117a-4a15-321d-b3d2-5a07a10862d1 | -11.85422 | -48.24291 | 2026-07-03 05:06:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b918b221-3d1b-3a1f-81ed-9fced57ada83 | -11.4357 | -46.53255 | 2026-07-03 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 655c8a58-0f90-356f-beab-d0b5061018a7 | -14.17671 | -58.77097 | 2026-07-03 05:06:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8aa4a03-1382-3e46-aab2-5a073c212ec1 | -10.94883 | -43.05496 | 2026-07-03 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 4fc19791-70a0-398c-9937-4ff9fc4564b4 | -10.94061 | -43.04602 | 2026-07-03 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 56e5b5b7-7ef4-3c6d-9f34-8212dfbf2f34 | -12.74635 | -44.53194 | 2026-07-03 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 648ca8e1-ec28-3d97-9640-0f7080871f39 | -11.41685 | -56.06432 | 2026-07-03 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b57c6261-a311-386b-a68d-48d75c2deab4 | -8.69677 | -54.57661 | 2026-07-03 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d66e630c-8438-3455-bd81-fae34ef22371 | -14.1834 | -58.7721 | 2026-07-03 05:06:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdad05b7-1280-303a-94fc-e0d8910f90a6 | -14.41076 | -44.59019 | 2026-07-03 05:06:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09179d39-d884-37c8-939f-e911b7e1dd5e | -11.35019 | -55.40466 | 2026-07-03 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b201d43-f6b7-3ea9-9eaa-73ce33c795db | -8.70636 | -54.58183 | 2026-07-03 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 804bf63b-2f4c-3cd8-b23a-36a9b402622b | -14.21224 | -58.73568 | 2026-07-03 05:06:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac1c115e-4838-3792-884d-3a6b2528db91 | -11.34856 | -55.41555 | 2026-07-03 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f414e2e2-53b9-386d-a880-6edb0ea9e4ca | -11.63032 | -59.02117 | 2026-07-03 05:06:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ea2605f-7b3c-3e87-8563-70828891c465 | -12.09321 | -57.14365 | 2026-07-03 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e13c5c74-ce60-38bb-9502-9cfdfbd5c933 | -11.34466 | -55.41865 | 2026-07-03 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1044810-1fc9-3ce6-bcf7-cb3b617f8a56 | -11.35246 | -55.41245 | 2026-07-03 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 721385dc-cfe3-328b-b01d-69f551b99f20 | -10.56451 | -49.13598 | 2026-07-03 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 431f53f7-73e9-3325-a04c-a0850a963f15 | -12.50426 | -43.81002 | 2026-07-03 05:06:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6de02d7f-2314-3f54-b00e-f021f1e8a73a | -10.6236 | -53.89489 | 2026-07-03 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1efdf387-7e9f-33ce-93a1-ca00ba80ede0 | -12.74815 | -44.51466 | 2026-07-03 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| a9d72df4-51ac-3832-b4dd-d062fa6cce24 | -12.75326 | -44.54009 | 2026-07-03 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9426c68b-3a92-3796-884a-45b9d5f84aaa | -11.9193 | -43.39192 | 2026-07-03 05:06:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4cd4ced4-dfcd-33c6-acc6-f169d424624e | -10.90651 | -56.85846 | 2026-07-03 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2cc0ec5a-2c3a-3d8b-ab43-a1782080d43d | -9.18806 | -58.06752 | 2026-07-03 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d2fead2-df5e-39ee-8460-d44aa91730eb | -10.58452 | -55.4128 | 2026-07-03 05:06:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0fc0957-6603-347b-8041-bae73c0ada68 | -12.74797 | -44.52772 | 2026-07-03 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 50572ae8-d796-3377-90ae-937f27f0de20 | -14.18005 | -58.77154 | 2026-07-03 05:06:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fc41800-8dc6-34e2-90d0-fced8b380e5b | -11.35582 | -55.41297 | 2026-07-03 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b12c8cd-e9e3-333b-b7a4-f3915a9744f2 | -11.98417 | -58.06883 | 2026-07-03 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45cf63c3-b612-38c9-9f1d-aa82093cb116 | -9.19104 | -58.04916 | 2026-07-03 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03b9a962-bbd8-3969-b8e7-ca9eef0c688a | -11.41963 | -56.06839 | 2026-07-03 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30ef0fd7-5b65-3ba5-ae3c-a27ca718e39c | -9.16993 | -58.06482 | 2026-07-03 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d8288b0-1f43-385b-bf02-ffe9d353c706 | -12.50774 | -48.27687 | 2026-07-03 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14e534ad-40b5-359f-8bd7-1cf77183adfa | -9.75809 | -47.88396 | 2026-07-03 05:06:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83c0cc59-7a81-396f-825e-7671e9f16e0d | -11.08928 | -50.80876 | 2026-07-03 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README17.md)
