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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b8cf50d-2328-3053-92a3-a2173eb4e322 | -9.18939 | -59.45891 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 52cf1cbf-7319-3ad9-93f3-ee38e481a819 | -9.16642 | -59.71228 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e56fca1c-4112-347c-a453-0eb1d05139f6 | -9.11537 | -60.33317 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f030002-2c22-3005-a1ca-8c47514294ba | -9.1137 | -60.34367 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df742ac7-3a33-33f6-83d0-ee26bc8da0a2 | -16.61489 | -49.40042 | 2026-08-22 05:25:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07ef5429-256a-3c71-8100-c9796b992e7a | -9.17855 | -59.69994 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 599a88ea-d877-3e19-a717-e70540549463 | -9.16842 | -59.46271 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 442e3fd8-514c-3536-a422-9be9b3896909 | -8.33238 | -57.68531 | 2026-08-22 05:25:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb654c6f-417c-3f95-b96e-8c3356fdef13 | -8.3877 | -62.6819 | 2026-08-22 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 3ac76e40-a295-345b-970d-97163744e907 | -8.89461 | -60.54262 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| f05669dd-9a6b-3d50-8b96-453122a22ff8 | -9.4338 | -51.60687 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98bfb0c4-4931-35c6-a856-ba0dc287d7f5 | -8.89737 | -60.54669 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d5c8b50-0f08-3e50-9a6d-827885a4fcc7 | -9.39459 | -55.97885 | 2026-08-22 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9132f07a-6a5d-383b-b115-04f833d2c671 | -9.41104 | -60.41718 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1dc486a-7d47-3710-80a5-e641ed860ed9 | -16.02946 | -52.17491 | 2026-08-22 05:25:00 | NOAA-20 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 690d27bb-f371-3fb1-8ff6-ff5bf6ebc530 | -14.50303 | -59.81926 | 2026-08-22 05:25:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1643e968-131d-3300-a4aa-fb9cffb8ff49 | -9.3908 | -60.5652 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7dca848-9cf6-334f-9597-1c2088fcf396 | -15.68032 | -53.77601 | 2026-08-22 05:25:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fc55a90-8ebc-3941-b434-152911f7bedf | -9.21255 | -60.76462 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5338914-1dd9-3511-b9fb-ad9ff3a6aabc | -9.21666 | -59.78098 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9afbee65-68a2-3406-86ac-2d9812a89e81 | -9.05206 | -57.0748 | 2026-08-22 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca019e66-4f09-3965-a3e2-3da203ca9bc4 | -15.21272 | -52.77628 | 2026-08-22 05:25:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 368d63da-06a2-325b-9913-9c3dda985f0c | -9.05191 | -65.45483 | 2026-08-22 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47cf19de-f6cd-3346-9e92-b5dd30401df0 | -9.41324 | -60.42472 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68ec6bb2-4204-339f-a5c5-b2fc3fc19887 | -11.59899 | -46.55334 | 2026-08-22 05:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ba2382df-05e9-380f-90f5-529ff7ba924e | -7.86327 | -63.76095 | 2026-08-22 05:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56c21d0e-e212-3dfa-a1e0-0f64ae2f1fd4 | -10.30477 | -48.229 | 2026-08-22 05:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ff15943-a5c5-338d-a7cd-6c2cdbe8d4e7 | -9.21831 | -59.77054 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b3746e8-c0b3-3cd2-a2a8-06bd3182b8d6 | -10.75716 | -50.25721 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1d9fe3d-5d02-38b4-9a15-f4293155005e | -17.56836 | -47.88813 | 2026-08-22 05:25:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fc6c087-d899-3897-86e3-801c9848bda1 | -9.4369 | -51.62135 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05b1351e-df3c-358a-9724-c6cb0e2a70b0 | -9.16071 | -59.46863 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b6cdce2-2f83-381b-b8e4-558509925d93 | -8.9007 | -60.54723 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59606630-43fe-3e0f-92d3-f72438ff0cf1 | -9.40128 | -60.58496 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9818718-8013-3195-aef0-9203013842c5 | -9.39796 | -60.58443 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9e22be8-bf61-3f11-b280-aeb96c4bf3dd | -9.22052 | -59.77803 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d50e0da-babf-3fce-8fbb-983361d5b85a | -16.60575 | -50.79638 | 2026-08-22 05:25:00 | NOAA-20 | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4aa8e744-fb4e-395d-9106-8b489e9f16c3 | -9.17393 | -59.44929 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8e4c424b-df63-3fbd-b001-532bcd7edab6 | -9.44491 | -51.60038 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aab036dd-3fd9-3211-82a8-c379e24f52a7 | -9.27602 | -60.91711 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e250ffa-1b71-3e38-96cf-7eeb30b4c603 | -9.05266 | -57.0708 | 2026-08-22 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b5c0439-76a4-35c0-b042-33e5582c127f | -7.7542 | -61.08222 | 2026-08-22 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b3fead8-73bf-33e1-a7e7-a76ca631b9ba | -9.11149 | -60.33613 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0620a0b-21d1-347f-a81a-2e33e451a7eb | -9.21221 | -59.76601 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91979b1d-7d8a-3973-bf79-debda5ac760b | -10.51674 | -50.8268 | 2026-08-22 05:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 815e821a-15b1-39f2-9e4b-1e84a0bc3b9c | -9.17557 | -59.43883 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c658d464-856e-3f62-8fb8-1e66da7d306b | -11.55542 | -46.94048 | 2026-08-22 05:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5eb87906-c01e-331e-96f5-f13b0ce147e5 | -9.16125 | -59.46515 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5633d431-21e5-37f0-ac21-6a07b7db170c | -9.58697 | -60.50653 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4b578a2-390a-3ac2-a7da-866f16aeaba5 | -7.66994 | -61.12509 | 2026-08-22 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c0dcffe-43b5-3fdb-af58-99cdc656313c | -9.43408 | -51.60577 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a69458e-fecc-37d6-9fad-4102c22a1aee | -8.95 | -60.58056 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fcdae4d4-d7d9-3354-a454-202101c2c109 | -10.80769 | -50.97274 | 2026-08-22 05:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| bf88bddf-9c3f-3f7b-bcc3-0bc0584278e0 | -9.0449 | -60.43319 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| feb2028c-02a9-38d8-8f68-98192f9b1a90 | -9.28779 | -60.90807 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4287d413-5de5-3255-9249-43e02eb2d83e | -9.1756 | -59.46028 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6326b217-fe1f-37bd-a432-1f54024fc7d5 | -9.43874 | -51.60808 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3df68150-6bef-3213-96a8-fc25817254c9 | -9.43763 | -51.61607 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67756164-7ae5-3897-8cda-1c336dafca5d | -9.06539 | -60.43292 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebe611c7-898c-31fa-824f-5c5721537724 | -20.68052 | -57.20306 | 2026-08-22 05:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d60df0fc-934e-3063-9e7c-5ceb94d7f23c | -9.28951 | -60.89738 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb53c5f3-21c4-337f-b5fb-17e7bba3ec55 | -10.68495 | -50.2971 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24fc08fc-147d-3dfe-940e-1185ad981817 | -9.17119 | -59.46673 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97fec652-9d89-37e4-a911-bbaf2ed24c63 | -9.21441 | -59.77349 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39f4da69-0c4e-3c5f-97e3-26f2bac6c15b | -9.06815 | -60.43696 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af3d0430-461f-36e9-bf57-119505bf66dd | -10.52363 | -50.77212 | 2026-08-22 05:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bac49959-4c7c-3860-a159-327d3a2eb465 | -17.55959 | -47.8896 | 2026-08-22 05:25:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58382a5d-76af-305e-83d7-3dd371f52220 | -9.17888 | -59.43935 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9603a445-974f-3152-998d-ea46d3120af0 | -9.22107 | -59.77456 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eeae9e56-a42e-341a-830b-4dcbf36d3154 | -10.51385 | -50.82643 | 2026-08-22 05:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 177b771e-911c-3967-bb08-1674d4bb0be2 | -9.4044 | -60.4161 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a84f6bea-95e8-3069-bc8e-39374395306a | -10.89777 | -50.24417 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ef98401-9308-37f0-84da-792c03b62901 | -9.21808 | -60.7728 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3152ab21-bf27-3a81-ba5b-72e575d8c98d | -9.28894 | -60.90094 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 577bc4f3-6a21-3059-986c-49f0cef9c98a | -9.11268 | -61.59561 | 2026-08-22 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3fb9e36-58e2-3163-8337-171500494ef2 | -8.39352 | -62.69133 | 2026-08-22 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b43a8982-87e2-39a5-88d1-93567896adbf | -10.80314 | -50.97812 | 2026-08-22 05:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 02180759-69c8-3e3e-9a94-09fecf403052 | -9.20886 | -59.65839 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 865b9288-ff0c-380d-b2e5-84886261c8bb | -9.04986 | -60.44478 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6640ce61-158d-32b3-97dd-e74fb2d63628 | -9.1207 | -61.58929 | 2026-08-22 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5456f6af-b78f-3043-9638-4cf3b78ab1b9 | -8.3942 | -62.68719 | 2026-08-22 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| db056efe-2a36-317b-9991-703ab76757ea | -9.41216 | -60.41016 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3af163bb-1fc6-3784-9601-8129c8766f80 | -9.42431 | -60.41932 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2feb6a5d-9338-376d-aaa3-fff73125742f | -9.24804 | -60.79954 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aaa2c0a4-7901-3bab-be2b-9e02188787a8 | -9.39581 | -60.55519 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d793b34e-b39c-3150-80fb-f0b76ae6c0b1 | -9.4066 | -60.42366 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3988a5c3-340f-3e53-8d0b-29fb5180b430 | -8.67347 | -54.76048 | 2026-08-22 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5eca02f5-de5b-307e-b8b5-90deeccf257f | -10.8936 | -50.2782 | 2026-08-22 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b887c73d-959c-3d95-aea9-9f63bcc4a2c7 | -15.24598 | -52.83763 | 2026-08-22 05:25:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09658d12-3679-3f3f-94f3-2c8d45b6c4db | -9.41708 | -60.44334 | 2026-08-22 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75829978-f7e7-39d3-999b-d5db92cbe25c | -9.19698 | -60.88243 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4142d59e-8a9a-3497-919c-e75b31779797 | -9.21386 | -59.77697 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47ddc238-c6fe-34e5-a368-eb1c4f923efc | -10.80194 | -50.97539 | 2026-08-22 05:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19e35263-df0c-3e5c-a6c6-21ebd8d101bc | -8.90346 | -60.55129 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ec0631c-3e2d-3d15-8367-17b6c9283f8e | -8.3723 | -62.73046 | 2026-08-22 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e23576d-819e-3e81-8c35-c5f23dbcea7e | -17.56659 | -47.89016 | 2026-08-22 05:25:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f91bd7d-c950-313b-90f7-f454c42524e0 | -9.51948 | -51.65311 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82c674a7-80c8-3fb0-960c-49e42efc9ed0 | -9.43649 | -51.62429 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe6699a2-bd9a-375f-9bda-516704365761 | -8.39711 | -62.69193 | 2026-08-22 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17930743-db5d-361c-bb3b-4bb03f70af87 | -9.16788 | -59.46619 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |


[Clique aqui para ver as próximas entradas](README75.md)
