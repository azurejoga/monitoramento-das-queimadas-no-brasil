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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01f7970a-6684-3455-994e-926ed8d359d1 | -12.1354 | -47.07086 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 82c4831d-5634-3485-b494-a3778f1b57df | -11.31684 | -45.15053 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b127320-331b-31e6-91f5-d580b1842bc0 | -10.7855 | -44.76142 | 2026-09-02 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 6a718a1b-a440-33bc-ae38-2d28b7db9d81 | -13.40606 | -43.8782 | 2026-09-02 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 319c67c1-26fa-356b-8edf-06bb7163f5d4 | -14.9658 | -48.11076 | 2026-09-02 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 84b0a7e7-48f8-32fb-9994-0f4808d399c9 | -8.44501 | -54.69681 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ad069a2-1651-310a-8ff5-1a5bb9f16d5c | -10.30128 | -49.99187 | 2026-09-02 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1451dfc-133c-3b19-932a-40c4d214ec96 | -11.17293 | -45.59982 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca7142d1-d5da-3915-b3cf-3a2520fbe839 | -15.64815 | -45.90497 | 2026-09-02 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80ac8fa9-2732-3d96-a0d1-253f7aee3eb2 | -9.82671 | -46.35598 | 2026-09-02 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e2152aa-ba0c-3f01-9d28-02d78de7489e | -8.44407 | -54.73286 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c426fef4-09ba-3967-bc0b-2d9a644df30e | -8.46628 | -54.73312 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40445f53-7182-3b6d-bad2-ab05aa71c0da | -14.96641 | -48.10704 | 2026-09-02 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| d6c04f33-04fe-3951-a251-45ef0e772dc7 | -8.45507 | -54.70259 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47941f8a-be60-315f-9359-28c17591510d | -8.9975 | -50.77782 | 2026-09-02 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 13d2376d-5c55-3e33-a6f6-6c7ad89972c7 | -8.47093 | -54.69135 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a952796-e222-33ef-806f-4abd837d3574 | -11.32829 | -50.58364 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4efe0761-8e16-34e8-b939-e0734b3ea674 | -12.12159 | -47.05029 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5ae8887-2414-3193-9c73-276a481e742c | -9.72273 | -48.14117 | 2026-09-02 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d608f18c-394d-34bd-92cd-e567102af21d | -11.67451 | -46.73935 | 2026-09-02 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2993bdab-587c-39f4-bc7e-5dfedc9d7eba | -12.87548 | -45.82191 | 2026-09-02 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 60066e73-9f4c-3fe4-91d7-4b764fe7f167 | -6.73444 | -56.3423 | 2026-09-02 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10d9985d-9986-3037-b169-ba8671a4b191 | -12.14861 | -47.24603 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3596929-31f4-35ee-b008-35e266dd5927 | -11.63585 | -50.19647 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5a8e2d1-0839-31ee-97b0-cd9a2585debc | -11.65563 | -50.19504 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 87affea7-6ebf-3e97-90a5-990ea06bc4a4 | -12.10027 | -47.0981 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bc19abb1-8ea6-361b-980c-3dc32407cda7 | -11.35183 | -45.40928 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3d709983-4caa-34da-8801-972b77eb20db | -9.14463 | -40.50839 | 2026-09-02 04:21:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8302800b-ca9f-3913-980f-84aaaebcf833 | -8.46447 | -54.72606 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62327ea1-2e54-3f6e-b5b7-e736abc55a77 | -8.28131 | -54.91163 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f861dc94-17df-3c22-b114-5fab0cf6dac3 | -12.4212 | -48.00174 | 2026-09-02 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5f77caa-d9b0-312a-a590-30bc4a659382 | -12.12922 | -47.0882 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0b551c2-4bde-3089-8b27-4da731eb69a5 | -12.14527 | -47.24548 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7aadf006-e892-3fc5-aead-e620e8c6c94e | -12.14352 | -47.1273 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a576c854-104f-3c68-b7e8-413e9a78f8be | -11.35642 | -45.40271 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e3adc60-e630-3aa1-a65d-e33d7e04b30b | -14.98344 | -48.02349 | 2026-09-02 04:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b800d12-4837-3355-8e0a-9b0c43bc1e47 | -8.44947 | -54.7338 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| db0696e1-52cb-3490-8e28-0076fedbc489 | -11.30199 | -45.18083 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3803ca9a-b4a1-3f82-b9b3-1d452aeed8d8 | -12.14523 | -47.11654 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6a56850-feb0-3016-8011-b72fb01ce76b | -8.47475 | -54.71678 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 95a342de-c4fe-3b45-919e-fc7e20ebf21b | -12.13904 | -47.13391 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 7b84c9af-cb79-39ce-89fe-3aae0bbb88f1 | -11.84202 | -46.06292 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d899ec9-041e-386d-9a31-bbfb4d6c45a0 | -10.90183 | -45.33029 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 92125064-5a1e-39e9-bf5c-6517b217cd7c | -10.31385 | -50.03354 | 2026-09-02 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50e74afb-2921-3bb2-a38d-60d1c58d9544 | -14.97406 | -48.12355 | 2026-09-02 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54521a9c-272f-35dd-a7e5-ee192b937536 | -12.15093 | -47.08076 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1200f87-b943-32e9-9a4c-5b7d92656a1f | -11.29751 | -45.16556 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dee3ea14-a9ec-3423-ad72-75d7154290ef | -12.13342 | -47.1477 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 39b3aadc-8b44-3619-9b65-a342855bb98b | -12.13399 | -47.14412 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| a600c11b-5800-3d34-bf11-9bb7f1aec98f | -9.72204 | -47.77102 | 2026-09-02 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 46065d12-20bf-3774-af02-6a6ff576c54c | -15.19571 | -49.04078 | 2026-09-02 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5776907e-3d28-340b-a891-16599467a484 | -10.89689 | -45.34031 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 8a261ae8-ae74-351a-bf81-7d836b5b6b58 | -10.67966 | -52.50477 | 2026-09-02 04:21:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 383d36a6-f487-3ed1-af14-68899af535a0 | -11.90502 | -45.05985 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0493fae7-4fe3-3fb3-bef2-89a12ebd4308 | -11.90612 | -45.05267 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9b90496-698e-32c9-a244-28f0e1badd25 | -12.14791 | -47.14272 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1e8e4242-bd9a-37b0-811c-be640236b852 | -11.95172 | -45.04521 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 81a8500a-90ae-3d31-acc6-76d71ce3e951 | -11.5307 | -46.91649 | 2026-09-02 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80332a2a-e3f7-38ea-b529-317329c72e0e | -11.69132 | -50.51148 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de6d92c6-40e0-3e09-93d0-bdab91dc02b0 | -10.31702 | -49.10366 | 2026-09-02 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5ae80285-4e4a-3c5c-af48-bd71cad413aa | -10.04959 | -48.69786 | 2026-09-02 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 189fd060-34bf-3212-a3d4-2d01d75a1113 | -11.8205 | -46.04868 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fe0a1c4-88ac-3860-aa5f-1fe13a90006c | -12.09693 | -47.09755 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 24e46262-cd10-3cdb-bddb-b3a55ceb7abc | -10.77937 | -44.75677 | 2026-09-02 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| bb6c8cfa-51bc-3ae4-964c-c7664ab8b760 | -10.38095 | -49.98589 | 2026-09-02 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80c42190-69df-3443-8728-eade274e6df9 | -9.7042 | -47.20824 | 2026-09-02 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 370a090f-8f3b-3d3a-9c73-b453e7f2a1a6 | -8.70258 | -47.56144 | 2026-09-02 04:21:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b66913e2-3f84-37f6-b644-48e4a899430b | -11.36197 | -45.41081 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f8e490c-6691-3f15-b0cb-52d44d2ea28f | -10.89798 | -45.33329 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7159a098-48c4-30fb-8cf0-0c5fb2187a7e | -8.45984 | -54.70697 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ecbfeb4d-c7b3-34cf-8b2a-bf1154c761e7 | -8.48261 | -54.70376 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| d9f1c610-524c-3f59-924e-d33891262c84 | -13.37961 | -41.34723 | 2026-09-02 04:21:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 34c0d409-7972-37d6-ac3c-c68aa22c1732 | -9.21923 | -47.9848 | 2026-09-02 04:21:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0acda58-c593-3ab7-9a84-72da92b52ff9 | -8.46923 | -54.73038 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 738ac81a-9bd0-3b8b-a52b-b5addf2a1524 | -7.93499 | -47.24454 | 2026-09-02 04:21:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4020918-8cba-39bb-9fd7-2456e954ec49 | -15.37809 | -47.68748 | 2026-09-02 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3ce19a0-fa8b-3f66-ac56-89af6f0e7c68 | -6.76056 | -56.33805 | 2026-09-02 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3e28d3b-3cd2-3dfe-8c60-92504f086507 | -15.6476 | -45.90867 | 2026-09-02 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9efb1f1-8ea4-332e-94af-8176cb5124dc | -12.12817 | -47.07334 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eaeb693b-6a3f-37f4-a2fb-f0421e0750f0 | -12.13008 | -47.14716 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| db59cbb9-4459-3e48-b9f6-2f890b6648d6 | -10.43738 | -46.73096 | 2026-09-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a19ea0be-0681-3b4b-959e-e9afdc74ccc0 | -10.89581 | -45.34733 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f73ed7f5-9e05-324e-b517-7cc105a31a11 | -10.50224 | -59.62314 | 2026-09-02 04:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0f6e59ba-ac10-37b2-87a5-ded9b9085eac | -12.13532 | -47.09287 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f5abcf3-0538-39f1-8988-8724f6ae9e6d | -12.07174 | -47.12654 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb4f5a74-d565-3aba-b8a5-8494e2397a15 | -11.82878 | -46.0608 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 576d3f4a-21a4-3df3-933a-24eb0ba2de64 | -12.38023 | -48.14546 | 2026-09-02 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94ddbd9f-a66b-37ca-a45b-0b7ddef1034d | -12.1454 | -47.07251 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4e51e616-0e84-3c79-8e8d-8f85f29c09fd | -11.53607 | -45.44907 | 2026-09-02 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2eb05bda-e060-35b7-8ba7-6ec2d88663aa | -8.78434 | -46.47395 | 2026-09-02 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d855e0f-295f-37cb-9d83-b91d51c293a0 | -13.39157 | -51.38588 | 2026-09-02 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eb510ce8-e3b6-33fd-aacc-bcddaa1f4aa4 | -11.30857 | -45.16003 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 66929297-85de-355f-aaa9-b2404cce2302 | -15.06425 | -45.31313 | 2026-09-02 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d7a381b-64dc-3045-897e-5f50b6e18b51 | -11.27955 | -46.56959 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b425161-cad8-3a2b-9efb-70d04ff4f545 | -15.18007 | -46.21522 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66061764-d631-35db-9b41-9d3b7c56376c | -8.7704 | -46.47541 | 2026-09-02 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90f78ca8-f63d-330f-84cd-4843fbc8242c | -10.89635 | -45.34382 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8a7ff62e-8215-3d3d-bf0b-9faf2cddf10b | -11.61948 | -54.564 | 2026-09-02 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 81b342cc-f8f5-3268-bf1e-5548a2478250 | -14.97372 | -48.1045 | 2026-09-02 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e073e819-c032-3329-85fc-73b241bf4186 | -8.46462 | -54.7113 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |


[Clique aqui para ver as próximas entradas](README24.md)
