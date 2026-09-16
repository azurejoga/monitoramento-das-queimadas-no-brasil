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
| 8cd4e497-29f7-350e-b3f2-1264203bd6d5 | -12.38193 | -51.4149 | 2026-09-16 04:17:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bd163f1c-15f1-3152-b2a3-67c59f3fce57 | -12.36983 | -48.46347 | 2026-09-16 04:17:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78570e35-1a05-31a9-8826-4ea16f685cc7 | -15.27963 | -42.81137 | 2026-09-16 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 0d36ad83-d8a1-3a88-9783-2468c8f86d2d | -12.71546 | -43.20869 | 2026-09-16 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f602ed8-6cad-3781-bed8-4d17db8d7f50 | -10.98736 | -48.31544 | 2026-09-16 04:17:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a7b4d8d-b8c2-3f20-aa09-93f48db52853 | -11.97777 | -52.46523 | 2026-09-16 04:17:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09c0b775-bd0b-327e-9080-bab2b93f7cde | -13.35119 | -46.30446 | 2026-09-16 04:17:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 940f9f66-79c8-3e98-994c-e9a1546af12a | -12.50955 | -45.91961 | 2026-09-16 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 102ebfa7-e178-309d-8e38-31e954ce2202 | -14.6605 | -47.98822 | 2026-09-16 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b961da9d-6b52-3f61-a617-e35a7a835945 | -10.69153 | -54.17815 | 2026-09-16 04:17:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3305f739-bacf-3912-b63b-d4188fbca2dc | -10.93139 | -54.08821 | 2026-09-16 04:17:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a23ece1-9a30-3b30-9236-a91cb3e17f10 | -17.04379 | -41.28693 | 2026-09-16 04:17:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 96c5ee41-ac24-3bc7-97c9-278badc55712 | -10.90114 | -54.01317 | 2026-09-16 04:17:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9227848-2e5f-36ef-ac07-6590d46927bd | -12.5067 | -45.91648 | 2026-09-16 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6201cba3-1727-3ccc-a91d-00687ed46a4a | -15.24977 | -49.10876 | 2026-09-16 04:17:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e490b27a-b355-3c60-8e56-777a625cde12 | -15.45322 | -53.7808 | 2026-09-16 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c594021-1252-33f2-8856-47eddff8f8a4 | -17.54512 | -49.42861 | 2026-09-16 04:17:00 | NOAA-20 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d417aa7-dc98-38c7-b430-3562cea16823 | -15.5075 | -53.85065 | 2026-09-16 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed6436b2-d304-3657-8fa3-4d695016e871 | -11.99219 | -43.78189 | 2026-09-16 04:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d61034d-062a-3dc5-9810-9d1dc98e04d8 | -12.6203 | -50.79285 | 2026-09-16 04:17:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b62585e6-81a2-3780-b3d3-5767df227d67 | -11.89255 | -43.82745 | 2026-09-16 04:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e25d6be2-9dc3-39d6-8a13-d0bf0a0e3955 | -18.21875 | -41.24636 | 2026-09-16 04:17:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 705250db-51d0-3619-b0a3-535fc37e1ccc | -13.55522 | -43.52415 | 2026-09-16 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c110d6ce-b8a8-3158-abd2-f541095f1dfb | -15.60599 | -42.40084 | 2026-09-16 04:17:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5cb93f36-dd4f-3423-acdd-0f9af22a8603 | -12.49794 | -42.80063 | 2026-09-16 04:17:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0fdc431a-d2d4-303a-bf59-271db31f993a | -11.54858 | -46.86127 | 2026-09-16 04:17:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 84f7a721-8023-3196-8828-19ea5b65ed57 | -11.99499 | -43.78255 | 2026-09-16 04:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 028af804-73c6-36cf-9e5e-ee4ca201e08d | -11.89722 | -47.5962 | 2026-09-16 04:17:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bc57f12-dad6-39b6-9134-e2512b633aef | -10.69249 | -54.17337 | 2026-09-16 04:17:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bf0845bb-1da4-37b5-9dcd-fd94768da5eb | -12.15694 | -47.99305 | 2026-09-16 04:17:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03b9ff76-7eb1-3830-814e-28a3fe39093c | -17.03916 | -41.27504 | 2026-09-16 04:17:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4879db36-9a82-3fb1-ba28-14b54e59bb2e | -15.3671 | -42.19592 | 2026-09-16 04:17:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| fc14a449-d741-3d80-8158-4d46e2972bab | -12.41724 | -48.47565 | 2026-09-16 04:17:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7a857d7-f172-32a7-b9e8-9a469a60741b | -11.981 | -52.46304 | 2026-09-16 04:17:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6c5d759-b90e-3e6d-a97d-af127eece10e | -14.85901 | -49.96729 | 2026-09-16 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1ae1b8ed-578f-3510-a11b-51b0bd94bb00 | -10.86784 | -50.82076 | 2026-09-16 04:17:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| effb857d-ec6f-3f17-afcb-5581a862a6ee | -13.75658 | -48.79989 | 2026-09-16 04:17:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 521b4db8-6dbb-3a64-9e3d-8a38594718a4 | -10.68406 | -51.3379 | 2026-09-16 04:17:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 33975421-e3fe-3436-8b46-e82e666562f0 | -11.19635 | -54.12378 | 2026-09-16 04:17:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4bf543d5-fa18-37d0-bb09-7676ec385afc | -12.38563 | -51.41969 | 2026-09-16 04:17:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 38a68f0c-7893-3123-a1ea-02db799a2345 | -11.31478 | -47.24244 | 2026-09-16 04:17:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 787d5449-930e-3fe5-a1b1-f9d240ad1319 | -12.62985 | -50.79641 | 2026-09-16 04:17:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4e78b7ff-082b-3147-8c22-501094f86fd2 | -15.60654 | -42.39715 | 2026-09-16 04:17:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ef5692a-4efe-32db-af12-77c4c44966b8 | -15.88594 | -40.22231 | 2026-09-16 04:17:00 | NOAA-20 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 7ba3b836-b2c0-3690-9437-d9123649e1fe | -16.78131 | -39.46004 | 2026-09-16 04:17:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 337c7df1-60fe-34db-a3cc-befaafbcbc49 | -14.85718 | -48.13124 | 2026-09-16 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9f4f807-f38c-3a3c-bcd6-3dc4187cb992 | -21.068 | -48.55936 | 2026-09-16 04:17:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d0e17a9a-56a6-32fa-b9cb-a84bc774392f | -15.3535 | -48.11036 | 2026-09-16 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb1dbbed-ae83-38fd-aa4c-a25399f542a3 | -15.27349 | -42.80682 | 2026-09-16 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b552731d-78d5-3549-8395-dcbdf93e019d | -14.07582 | -42.4517 | 2026-09-16 04:17:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a9abe0b2-d174-3d96-9937-9c6b259e0402 | -12.3198 | -47.96527 | 2026-09-16 04:17:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 29e92485-52f1-34fa-b2b2-c799636018d4 | -18.22361 | -41.2382 | 2026-09-16 04:17:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 0d18da23-cf03-317c-bc9b-86e6f62ad091 | -14.85536 | -48.12755 | 2026-09-16 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ecbbf55-0e5f-38d6-9fb7-8039cfe7df3c | -13.76663 | -48.81411 | 2026-09-16 04:17:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 32505ea0-097b-3ef9-88b3-428b88ac3304 | -12.22102 | -47.12972 | 2026-09-16 04:17:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28e11c9e-204d-3feb-836e-888e5325bbe0 | -12.54813 | -47.1049 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be0cae3f-5f9f-3400-b4b2-aacbdd4180d7 | -12.52102 | -47.10204 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0adbdea6-fe11-31be-be28-488153b8d750 | -12.66712 | -45.05143 | 2026-09-16 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5dd6c2b2-46e3-3d4e-b87d-d1df8c177348 | -15.29585 | -42.79512 | 2026-09-16 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 12a44cac-f83a-3511-bada-0f09bdab95c7 | -15.28579 | -42.81585 | 2026-09-16 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 129609e2-3e5a-3821-8944-80d001e907d8 | -15.28188 | -42.79686 | 2026-09-16 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76ae0c3b-6381-36dc-8bdd-095a8c5da1e1 | -12.62038 | -50.79454 | 2026-09-16 04:17:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2d4f577f-ee3f-3e64-9da2-eeb32b7d1594 | -13.7614 | -48.79657 | 2026-09-16 04:17:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 361f2e1c-b2ac-3ec0-bcde-9fbf584d263b | -15.56309 | -42.37923 | 2026-09-16 04:17:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d4cf56c2-80c0-3293-ac38-52b1e41f7eab | -10.68463 | -51.33479 | 2026-09-16 04:17:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fd0d265b-53fb-3bce-b508-6edb349d84fd | -13.63245 | -45.97402 | 2026-09-16 04:17:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fca4ab81-1281-35cd-84d0-539b362b07e5 | -12.61934 | -50.79806 | 2026-09-16 04:17:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1b840368-2362-3363-ab46-99b1cdbf2831 | -12.47213 | -41.41848 | 2026-09-16 04:17:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bd9f8bec-6f9a-3341-8786-955cb7e8ceb3 | -10.90591 | -48.36449 | 2026-09-16 04:17:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9906f21-cc24-3b55-94ed-4d7aff4dd770 | -11.41248 | -51.43014 | 2026-09-16 04:17:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59c42ac0-df60-3f9b-8f69-cb38dbaaef85 | -14.66432 | -47.98895 | 2026-09-16 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab97b052-70d2-3cc5-8d6e-5510e550f92d | -15.51732 | -48.92815 | 2026-09-16 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb4fcb32-18c4-3011-87b3-ab119ff76cd1 | -12.38174 | -51.41297 | 2026-09-16 04:17:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67ecdf79-c3ad-3d06-a5a1-dfc121cd90c2 | -13.55798 | -43.52844 | 2026-09-16 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cc11f4f-86ef-347c-906e-af54cc5af0df | -13.76922 | -48.82304 | 2026-09-16 04:17:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11ee7671-ef17-38b2-b0b4-6ee844794b45 | -12.71539 | -48.28194 | 2026-09-16 04:17:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cd497eb-01c1-37eb-8b53-b76222aafe33 | -15.28915 | -42.8163 | 2026-09-16 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 736ac04c-2520-39c7-9453-d3a4789ae6a0 | -15.89569 | -40.23337 | 2026-09-16 04:17:00 | NOAA-20 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4c876e38-8342-384b-a624-c172e3b20171 | -12.32162 | -47.95495 | 2026-09-16 04:17:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2a5396d0-ad23-3d12-9a54-a9ec48b952ff | -14.22958 | -48.51693 | 2026-09-16 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ca3a2632-2f4b-35bb-a4e4-7edddef7aba5 | -11.41754 | -51.43111 | 2026-09-16 04:17:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 109086d5-0190-3227-98a7-25a39bce794f | -15.03427 | -48.56567 | 2026-09-16 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1480bf79-4e37-342e-a138-62fae9a82578 | -11.60979 | -46.95695 | 2026-09-16 04:17:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05842a8d-a368-332f-8cf8-ef89798066e8 | -12.56028 | -47.10178 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 10f6b21d-c980-33e9-8d3c-63c2dba17a9b | -10.86634 | -50.81921 | 2026-09-16 04:17:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0436eaab-a861-3693-929c-0c848693d1d5 | -12.22479 | -47.13042 | 2026-09-16 04:17:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2208f31d-ff73-3530-9a02-49218d967588 | -11.26409 | -54.13689 | 2026-09-16 04:17:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8019480-a851-3f60-9cef-f10ead58395b | -12.51658 | -47.15198 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfc42f2c-bc0a-3633-8f07-905e1dd262c6 | -12.53066 | -47.11617 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8187ebae-4850-3501-b7b7-716f5384a7b2 | -18.2353 | -47.26611 | 2026-09-16 04:17:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7f2a369-3e4a-3df6-a8f8-83a01ef6c8aa | -15.29638 | -42.79162 | 2026-09-16 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37d58a5f-bb7d-3b23-b080-ec8c5e9d88ae | -13.29298 | -51.27774 | 2026-09-16 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2cfb2963-eea9-394c-b749-b77c5e5b382a | -13.18995 | -51.64526 | 2026-09-16 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dd304f4f-7f92-370f-8e05-4fdee239707c | -12.52854 | -47.10619 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1b4685d-8d00-3d39-9492-0df50fa5972e | -11.31861 | -47.24319 | 2026-09-16 04:17:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d36914a2-0ee9-3204-b0a8-3fcc46437573 | -13.09809 | -43.38714 | 2026-09-16 04:17:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be516ddf-8993-32bb-be9b-c72a013eb087 | -15.60936 | -42.40135 | 2026-09-16 04:17:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5928e3ed-df59-3576-8742-ffd6d2d6f753 | -12.32072 | -47.96006 | 2026-09-16 04:17:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 16c8838e-e6ba-32dc-ad2c-d5ace5801d86 | -11.26594 | -54.12759 | 2026-09-16 04:17:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cb1311d-0390-3345-89cf-2d021cacf518 | -17.0415 | -41.28385 | 2026-09-16 04:17:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |


[Clique aqui para ver as próximas entradas](README31.md)
