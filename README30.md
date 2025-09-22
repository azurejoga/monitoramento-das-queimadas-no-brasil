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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48fb34e2-9911-3810-8ba0-760a186c0831 | -12.96445 | -46.94049 | 2025-09-22 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2990e70-934b-31fc-8bb8-4def1b5daf67 | -11.26561 | -47.47802 | 2025-09-22 04:40:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a94d997c-96d6-3bd6-83f1-aa6a2e76dccb | -12.06413 | -44.82214 | 2025-09-22 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c2ba6d81-ba7b-3aff-b166-f304b378d955 | -11.64125 | -52.85789 | 2025-09-22 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| deb0f9e4-21b8-3090-a023-b251e7394fa0 | -12.97468 | -46.37662 | 2025-09-22 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c2a7d24-3b7c-3241-bf4e-19eef9276739 | -15.03568 | -55.29296 | 2025-09-22 04:40:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e428bc0-2e4a-3566-80ee-29a357f4ac1b | -15.83672 | -59.51268 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b21e6fd7-b914-31a5-80b4-914a0dbd0e71 | -11.28639 | -47.51111 | 2025-09-22 04:40:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2fe31f9-6d57-3922-b450-93461403f57f | -18.38226 | -46.4694 | 2025-09-22 04:40:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a761e1cc-a594-3325-943e-dddd43f4ea5c | -13.71282 | -47.57881 | 2025-09-22 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd9eb9d7-f8c0-315b-ae77-55fb991b73d5 | -14.61716 | -48.27402 | 2025-09-22 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61b826b1-8f4b-3ea9-ad7d-fe881f05508b | -11.86538 | -64.9345 | 2025-09-22 04:40:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6514e3d1-e0ee-3fca-8020-9f6ff9d670a3 | -12.07681 | -44.85653 | 2025-09-22 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97e31edb-3bb9-3d25-8658-d9fd5bac3592 | -12.06518 | -44.81431 | 2025-09-22 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e94a726b-9664-3899-87f2-e0f72613591c | -17.4278 | -42.37407 | 2025-09-22 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72e8ba5b-8e97-3197-b915-77542e52e89f | -18.40108 | -42.85373 | 2025-09-22 04:40:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9b207bd0-69af-3f68-8b8a-b85149c5252a | -12.72519 | -46.83105 | 2025-09-22 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4347bdce-75d2-300e-a594-5b93db999a40 | -15.82666 | -59.59124 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9434d75-3c9a-3e69-a995-77e33f0d1841 | -15.76721 | -59.41061 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dd5f535b-e57d-3d3a-b47c-78b6a158260b | -12.85424 | -52.99545 | 2025-09-22 04:40:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5f556c1-0c8c-3e40-8cb0-5033a8143745 | -14.6244 | -49.74857 | 2025-09-22 04:40:00 | NOAA-20 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| faf79a6e-39e9-3264-bac4-66b9e25742e8 | -11.46523 | -51.48248 | 2025-09-22 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 417e4b4a-6e41-36ae-8205-e1c0d7907b99 | -9.10122 | -64.0147 | 2025-09-22 04:40:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 37ae37b0-b219-32ca-9aa3-7df66f69d9de | -15.94837 | -59.39365 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5180de41-58c1-3923-a29e-d6dbafde20d5 | -15.77189 | -59.41198 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 78dc3677-db37-39b6-9e9e-5403a8fe2166 | -15.76765 | -59.40867 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 66f25cf3-601a-38d8-8f0a-7ca64466ff0f | -11.46268 | -43.53778 | 2025-09-22 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2230f255-6689-341e-9435-37a8069c8c19 | -17.42273 | -42.37051 | 2025-09-22 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3cfe6c5-5947-34e3-8780-a311e4233740 | -15.30217 | -56.79886 | 2025-09-22 04:40:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab27009a-26fa-3d86-aabf-8f1aa22aa76c | -11.32325 | -54.35044 | 2025-09-22 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 723386a0-00e0-3e33-88c4-169051169632 | -15.44836 | -55.9918 | 2025-09-22 04:40:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23d01598-dd77-3c22-9642-87bc8cda4ac2 | -11.50485 | -43.5702 | 2025-09-22 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fc044182-da55-309c-bbfc-f8f89c34f066 | -12.98173 | -46.38291 | 2025-09-22 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ae40bd4-25c9-305b-8573-70ef0db4f2ee | -14.97795 | -44.41506 | 2025-09-22 04:40:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0024828-c68e-357e-9d1a-b3681719422f | -16.01844 | -59.46637 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 478cce42-201b-3d6d-973c-c554c01acb65 | -9.10266 | -64.00765 | 2025-09-22 04:40:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4ddda413-94dd-3724-95a2-4968943d4c7f | -11.63023 | -52.85996 | 2025-09-22 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cdad6548-3732-3a2c-98c3-0364879fa904 | -14.63496 | -48.27727 | 2025-09-22 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ee54032-c4d1-3a4a-a77a-742b2ef0ea4f | -13.07673 | -47.02005 | 2025-09-22 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| daf0a859-7422-3fcd-b625-86fbd4fdef18 | -11.30913 | -54.34314 | 2025-09-22 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13a2bf86-25cb-37bb-b998-7341bba03559 | -15.76936 | -58.69752 | 2025-09-22 04:40:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1477c477-f24b-3ce6-abfa-90890eccba10 | -17.27315 | -43.44006 | 2025-09-22 04:40:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04ee24ac-45ca-352e-a394-3d8ce29c1e6f | -13.70634 | -47.57558 | 2025-09-22 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82d7b72c-04da-3ae9-9c18-37ed350abe1e | -11.78406 | -64.93124 | 2025-09-22 04:40:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fb32577-21a9-3e80-b295-f2ce2b9d8229 | -17.40057 | -44.27914 | 2025-09-22 04:40:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7db7b2d9-0e6f-3973-bf26-374be99a960c | -11.47133 | -51.48714 | 2025-09-22 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49f9fe4e-34aa-32fb-bfd6-8793441c7cb7 | -11.31362 | -54.33927 | 2025-09-22 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 355be751-fff0-35c9-885b-c7dfcfcd27ea | -16.1205 | -45.67557 | 2025-09-22 04:40:00 | NOAA-20 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef5b20ae-b0b3-3100-9424-03ab5b908caa | -11.73478 | -47.79769 | 2025-09-22 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ce2cfe94-be88-3542-8889-642d8545b2a5 | -9.0978 | -64.01452 | 2025-09-22 04:40:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b45f10f-8e57-30e0-8007-0526fd7f31bf | -11.46731 | -43.53564 | 2025-09-22 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70f7bfc7-12ca-3490-a8b3-d0241dcfffab | -12.06993 | -44.81113 | 2025-09-22 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba5f5a5a-4230-31a1-b8a0-321ea43ffa06 | -12.07468 | -44.80804 | 2025-09-22 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df318461-a1f9-3874-8e0d-238b6e3313cc | -15.30144 | -56.80284 | 2025-09-22 04:40:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f79884d-99e4-37f8-b002-4e0a4b360a7f | -11.67913 | -61.16898 | 2025-09-22 04:40:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 56f1e950-aa3c-337b-b50e-5971e1103605 | -18.4013 | -42.86024 | 2025-09-22 04:40:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 642153e0-bcf4-39c6-9e7a-fdb82ddfd5a9 | -11.08267 | -50.74966 | 2025-09-22 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f634c299-6020-35da-9634-c57d2fe96aaa | -13.68303 | -47.7099 | 2025-09-22 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d676a05b-0cf9-3f1c-aa15-5f5bd72c8460 | -18.0962 | -44.26933 | 2025-09-22 04:40:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6c55524-e26b-3227-8ead-bb1924341093 | -12.71216 | -47.71149 | 2025-09-22 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b029bc17-25b1-38cf-bbab-23e270ca3d44 | -13.31031 | -47.29736 | 2025-09-22 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39d60736-f6b9-328d-92fa-99d4240bfbde | -16.01481 | -59.4596 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b3a943bc-da7b-3fa1-a487-1a7cb103986f | -18.8491 | -42.19318 | 2025-09-22 04:40:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3ff91d22-6a3c-3062-b2f3-6d88f5657553 | -12.85016 | -52.99871 | 2025-09-22 04:40:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a277bca2-4813-320b-8462-fe656d0f5a18 | -15.16291 | -49.58524 | 2025-09-22 04:40:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fe2b362-f5d6-3f37-9ebe-7cf8e9cfc007 | -11.51691 | -43.6197 | 2025-09-22 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29ca21a2-0324-3147-9993-2da718fa58e3 | -13.86258 | -44.19801 | 2025-09-22 04:40:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aa9334ac-5748-3cbf-b64f-d6f2e789a3f3 | -15.93273 | -42.19071 | 2025-09-22 04:40:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9e1faa28-b0c2-3c05-bc23-7dd0f6e0423a | -14.35523 | -47.7814 | 2025-09-22 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 127ae213-e900-31ce-bf71-4d09cbc99d1d | -14.97856 | -44.41034 | 2025-09-22 04:40:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91e10089-ebd9-32ec-927d-941cfeb46e48 | -11.52476 | -43.63052 | 2025-09-22 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67c5d93a-bfa5-3183-be0d-27c5645c4cd1 | -15.25606 | -43.09081 | 2025-09-22 04:40:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ccc0ce06-e2ab-3020-9105-78871853bcd7 | -11.64189 | -52.85404 | 2025-09-22 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 393bba3a-de69-371c-b86a-fc555aee9ce5 | -16.25222 | -48.51858 | 2025-09-22 04:40:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4e9793c-81b9-3c85-b038-50243dff9280 | -11.64471 | -52.8585 | 2025-09-22 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41b3f159-1ed6-33ab-9905-e40c514b4343 | -12.07573 | -44.80015 | 2025-09-22 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cdbd3e3d-f203-3410-9da4-7a0e96891501 | -15.31296 | -56.80876 | 2025-09-22 04:40:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1250678a-97b3-31f6-9f45-f5cfed348ead | -11.64689 | -52.86681 | 2025-09-22 04:40:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25df1701-ec28-3efc-901d-08b58f1e5283 | -14.61958 | -48.28263 | 2025-09-22 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 490355d5-74b3-399e-8a89-2cacbdf2d053 | -12.68482 | -46.84402 | 2025-09-22 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 154d0d67-5d0f-3694-b828-33cba5622a35 | -14.97462 | -44.40498 | 2025-09-22 04:40:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22d57a49-f48f-364c-a743-0af0de32ca8d | -13.61765 | -47.41488 | 2025-09-22 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5d1f07b6-610e-3a8a-9651-06c4e755f2b9 | -15.83676 | -59.50805 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dbfbe930-8236-3d09-ae56-d0c8fa887f91 | -11.52084 | -43.62509 | 2025-09-22 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f00bdfc1-c459-3182-aeaa-bb889700c42c | -17.40608 | -45.02036 | 2025-09-22 04:40:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1d044d1-50d2-30e4-a60f-38566b53e406 | -15.83734 | -59.58772 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91af1e94-7625-309d-b28e-d17de5a486dd | -11.86384 | -64.94174 | 2025-09-22 04:40:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2134143d-ece4-31ee-b905-babddf6e247e | -15.40752 | -58.78522 | 2025-09-22 04:40:00 | NOAA-20 | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84631283-c7dd-31f3-960b-3ee0ee151eaf | -12.98245 | -46.37786 | 2025-09-22 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b399668c-0cd7-3e36-b4a4-84aba733bc17 | -12.07732 | -44.8527 | 2025-09-22 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 432775ca-a1bb-3489-8037-5bc4e7e20eeb | -15.84028 | -59.51542 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| da09f8e7-0113-37c0-a90e-276c92ca6a8f | -11.73744 | -47.80826 | 2025-09-22 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2a3f622-0818-3826-82f3-5bf0394a7e85 | -15.94935 | -59.38858 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 132f86c2-e51a-38ae-98b2-9babf43fde36 | -14.44481 | -46.52396 | 2025-09-22 04:40:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 36d8f22a-87c8-32c9-9d1a-2e0ee106b22c | -16.01372 | -59.46521 | 2025-09-22 04:40:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| de22747c-a47c-3c6e-a1c9-d33a32bb08d6 | -17.26846 | -43.43872 | 2025-09-22 04:40:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28858882-7ac1-347c-b3dd-b08074452bcb | -17.34631 | -46.82357 | 2025-09-22 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 88a6ee5c-50e1-37e7-ad53-fa533d385dbc | -10.86885 | -52.07285 | 2025-09-22 04:40:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e946bf39-81b8-3e4a-b82a-6b421e12df9d | -11.07938 | -50.74905 | 2025-09-22 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b7ee036f-e477-3d15-acb2-be6400bb74b3 | -11.2604 | -49.2425 | 2025-09-22 04:40:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README31.md)
