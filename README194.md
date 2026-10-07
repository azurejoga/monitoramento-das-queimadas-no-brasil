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

## Dados Diários - Página 194

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21e2e8e6-22d3-3dcc-892d-f443df8fd481 | -5.88154 | -53.62678 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 884b3e47-522a-30d6-9f9f-f304f4d746c4 | -7.88405 | -44.23142 | 2026-10-07 16:37:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bc1d00a8-d308-369d-b207-563f453f13f3 | -5.63926 | -40.09292 | 2026-10-07 16:37:00 | NPP-375 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 34.9 |
| 67742474-4104-3288-8a28-0bffaad853da | -11.09591 | -47.61884 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 24117236-2fd6-32b9-8e8c-38ad1d63cbc8 | -9.6428 | -45.73523 | 2026-10-07 16:37:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b6358eac-10fb-3684-b291-fb28d3ba770a | -6.14264 | -52.65528 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eb7a6c54-dad9-3094-82dc-3811f0ad6d78 | -9.93718 | -46.80449 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| eb8dfabe-f0f4-346a-88c6-fee95fe6fa1d | -7.43217 | -44.47872 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fe2f369e-e1e5-3ed7-8de8-5994539346f3 | -7.04763 | -44.33179 | 2026-10-07 16:37:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| a7748046-372e-3f27-9eff-dd8e08015277 | -15.43331 | -39.93287 | 2026-10-07 16:37:00 | NPP-375 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| ca58cf55-12d1-30d5-a074-e330e22ad9fb | -6.94495 | -45.28638 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| fb5cfa5e-e77b-35de-9724-a68b9e63d321 | -5.94035 | -53.48362 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 096798f0-024f-34a1-a834-4c398c61a22f | -8.06244 | -55.29723 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 2c1de4f7-e1d7-3c27-a6bc-fb1fc1ba1d2a | -3.76405 | -45.05577 | 2026-10-07 16:37:00 | NPP-375 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 186cb6e6-d2b3-3c16-954c-5617f758313e | -9.79059 | -45.61117 | 2026-10-07 16:37:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00a23fa8-c505-3464-abb7-446fbc213402 | -8.76579 | -45.76571 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b6251ae1-7a63-37f5-9e99-c87755db7b7a | -6.46071 | -43.238 | 2026-10-07 16:37:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| e29b6bf3-f1f8-36c4-af70-4967ca46bc8b | -7.25732 | -39.71664 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 50.1 |
| 92ba6501-c00f-3200-958d-3a47be82cae5 | -3.752 | -44.29391 | 2026-10-07 16:37:00 | NPP-375 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f14660a-f854-3503-82a3-065669dca352 | -6.70257 | -52.58273 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b2f36cb5-a482-336f-a738-7c1a13d660f1 | -10.99363 | -45.47455 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 133f624a-8ed2-360b-8797-be1e21f87a3a | -10.12863 | -46.84672 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0c471860-1c73-38f9-b458-0b12a4ea9181 | -3.63003 | -45.19453 | 2026-10-07 16:37:00 | NPP-375 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e0819b09-f5d2-30a1-8fe0-757066da84e3 | -3.88548 | -44.10264 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e84d1fc7-7b88-32e9-9d3f-94df02df99c7 | -6.0929 | -55.7324 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 56f25d3c-a707-35bf-92a0-22fd183bb7b4 | -8.76132 | -47.58241 | 2026-10-07 16:37:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 886e663c-c3f7-31af-a319-356bc58c1ef0 | -6.60463 | -53.03041 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 76887774-6c9f-3623-bd0e-e487c4d89dee | -8.91424 | -47.25974 | 2026-10-07 16:37:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c0e6494d-5cc5-3ce6-a695-f07d250af3bc | -8.83833 | -45.81372 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| a1d806c8-69d8-323c-9c64-9ff297ad880c | -9.58643 | -54.63433 | 2026-10-07 16:37:00 | NPP-375 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 2d8a7234-ca00-3ecb-9aa1-ef526a27ed4f | -5.35128 | -45.73007 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 0eeeacca-b76c-320b-8878-5afa57248dec | -6.20855 | -52.78999 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e834da59-abf2-3dd9-be62-2dea82551b5d | -9.64139 | -46.09599 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7e692253-95bd-3fcc-a3d7-791f6ceb90ab | -7.87545 | -54.96609 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| f38d827b-54ff-38f4-a546-68757295aa72 | -7.79572 | -37.6685 | 2026-10-07 16:37:00 | NPP-375 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 15.0 |
| a0c3d068-804a-3339-9cdc-89484cdf33f4 | -7.20662 | -55.12632 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| f0623614-88f0-31e6-b22c-8824c67b9f57 | -11.20579 | -46.27605 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fe3022c6-dd11-3b7a-8d36-b895a1dda4b7 | -8.03037 | -47.95783 | 2026-10-07 16:37:00 | NPP-375 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 91fb99e0-4d1f-3882-a384-32b19a746b91 | -9.96515 | -43.49216 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b4fb42cf-44c1-3c32-a0ae-c682cf1c1ed5 | -11.10344 | -47.58694 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8f884ae8-9e0b-3ccb-a926-4a2e769f84fa | -6.58072 | -41.59795 | 2026-10-07 16:37:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 29.7 |
| 91809799-6c19-31f2-afd3-611f24c328de | -16.64706 | -45.50949 | 2026-10-07 16:37:00 | NPP-375 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d2239c35-248b-34fc-86bc-cbbf88f194b1 | -6.69136 | -44.9468 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8c668acf-237b-342c-9fa9-4f20a09480ed | -8.9072 | -44.56148 | 2026-10-07 16:37:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 82d1c12e-5033-3090-b047-676e049195ec | -7.50274 | -45.77511 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c4a4185b-40bc-39da-83ad-f4d07ac336e3 | -8.68253 | -41.20227 | 2026-10-07 16:37:00 | NPP-375 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 36.1 |
| 974706eb-ab2e-30b9-bd4a-9bc7aebecb05 | -6.81155 | -55.30016 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7ce923f5-d438-301f-9732-a3e894df15d6 | -7.88341 | -54.97937 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 230eb914-767a-3e53-bf9a-5c8e1d4ff101 | -7.87247 | -44.22245 | 2026-10-07 16:37:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| f33475ec-5c6b-36d1-939e-07c8f5eceed6 | -6.29458 | -44.91228 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 40d1596a-cfb0-34ba-bb81-f6b6d43b2a18 | -4.96882 | -50.90891 | 2026-10-07 16:37:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 971867f6-d08d-363d-b71d-baba55d884f9 | -9.82572 | -47.47961 | 2026-10-07 16:37:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 2048ba0c-26b1-30fa-adac-11c2b4b4f936 | -7.05456 | -37.91447 | 2026-10-07 16:37:00 | NPP-375 | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 8.1 |
| cc77c1d7-fc86-3c8a-b3cd-9808ffc859a1 | -7.27799 | -46.16839 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 7e64a8fe-b61f-35fc-95bd-901cf306e6c1 | -8.1988 | -46.33818 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8696c46e-85f7-3097-b2ce-253df7935864 | -7.40447 | -38.85206 | 2026-10-07 16:37:00 | NPP-375 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| ccbd3df0-58e8-32f4-9e55-b3b194a81267 | -5.71817 | -41.73182 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 32728f45-6981-3c28-9768-40ac669551a0 | -9.9543 | -43.55478 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 0b8aac14-b611-3d9f-a424-159d6e50e3dd | -3.38787 | -42.59947 | 2026-10-07 16:37:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 39766118-cbf5-399a-8753-ef7b57a013cd | -6.03524 | -42.27522 | 2026-10-07 16:37:00 | NPP-375 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 6d054dbc-1fed-3e24-8cc8-662838cc82f0 | -5.24276 | -38.54475 | 2026-10-07 16:37:00 | NPP-375 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6f519310-1393-3377-863d-1159057044c4 | -6.02321 | -38.42999 | 2026-10-07 16:37:00 | NPP-375 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 40a6e7f2-8747-3424-8795-454fa29582ff | -6.11904 | -51.73923 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87d1d401-c079-33a8-8bf3-592c638539e1 | -4.76997 | -43.74441 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 370bf775-251e-3352-beeb-3663a1d6f53b | -5.76037 | -42.0409 | 2026-10-07 16:37:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 8bb11d57-fc8c-32f6-90ca-823a3652e801 | -6.68147 | -52.96902 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1dd75af4-639a-35f4-9db7-26a2d13f0ff9 | -3.89653 | -44.10806 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e72b17e2-4b9a-3a63-a424-2dc7f6051172 | -6.67089 | -52.97054 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| dd332c4c-2884-3beb-884e-54024b6d4f90 | -3.73404 | -39.52693 | 2026-10-07 16:37:00 | NPP-375 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 876875e3-674a-3e35-ad04-6ac88fabdf9a | -9.86108 | -46.31103 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e284bbee-7686-3c7f-8520-d56993945b1e | -5.81805 | -53.86009 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4aaa5e44-f495-312e-9d1f-b178af603254 | -5.68359 | -53.49702 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6d96e0c9-b03a-3251-995b-468184883e7a | -6.36947 | -55.15473 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a30def11-ada8-3831-871e-2a1b3e58e9a4 | -4.63478 | -48.85923 | 2026-10-07 16:37:00 | NPP-375 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 14a0e73e-c02f-366c-a177-1c6e4fd9f4f5 | -6.74808 | -55.09684 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6185cadc-cc70-3a6c-af0a-5f81e4a45957 | -5.71025 | -37.71057 | 2026-10-07 16:37:00 | NPP-375 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 62b842c1-305f-306f-9c1a-46d5ba18d6cb | -9.58758 | -54.6427 | 2026-10-07 16:37:00 | NPP-375 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| d091a2d0-b555-3feb-a3be-4d66794aedd0 | -4.57146 | -43.88273 | 2026-10-07 16:37:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 14669476-f49c-3191-82ef-447c21e81480 | -16.92772 | -42.10641 | 2026-10-07 16:37:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| 80b10ac1-9ba8-3a62-8d33-4052aa3f0cbc | -10.99545 | -45.41365 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4d417ba1-7fb8-3957-ad96-1aebdd7e7709 | -6.14736 | -52.65148 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 9a1fd4d1-2aa4-3ed4-a206-364e3db827a2 | -5.38111 | -45.92226 | 2026-10-07 16:37:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c4b4c9fa-bd7b-3e75-bc65-0ad7bc545d94 | -17.01793 | -45.90868 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 4d243e6d-b45a-3ddd-b20d-40f0d315347e | -9.6177 | -43.1246 | 2026-10-07 16:37:00 | NPP-375 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| b57c88de-3638-3dc8-9bf0-a4c4d4651865 | -5.24225 | -50.90391 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 8fddb288-8bdc-3f87-b739-6686a78c0f33 | -7.34301 | -38.73083 | 2026-10-07 16:37:00 | NPP-375 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3a778305-85f5-3af7-9fed-29fe451e3f4c | -5.7283 | -41.7502 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| ed6d1b06-6bba-3a86-a3ed-47602979fce7 | -11.14665 | -46.12008 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9ec1904e-9dee-3e5c-b9b3-11dc8da95f2e | -3.73971 | -39.53644 | 2026-10-07 16:37:00 | NPP-375 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 7606e52a-04aa-3c90-8bf0-095f634cd512 | -6.83281 | -39.54874 | 2026-10-07 16:37:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 5c64c57a-12a5-307e-b558-225c2be1f55b | -8.7574 | -44.15113 | 2026-10-07 16:37:00 | NPP-375 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 580ed1cd-6c61-3cf8-a0b3-f183e337eb65 | -8.25171 | -54.6503 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 83e06ed7-9d85-3ad8-84ab-2f5bc812cef9 | -3.88309 | -44.13143 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 25daea01-cada-3353-b054-36f5fe2facf2 | -5.6822 | -53.48715 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4de752da-ac4a-3952-8d2c-ac3b1880a558 | -5.68412 | -49.21565 | 2026-10-07 16:37:00 | NPP-375 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ac1ccac5-3cdb-3af7-a3ef-7311b3d34772 | -5.3533 | -45.68953 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d95e0a6a-9af9-302a-9c2a-1c0dae3ee402 | -5.5024 | -42.84018 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 15020475-5802-3685-b79a-a5bef53bb295 | -4.91937 | -43.22234 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c1261aab-8678-3b0d-877a-54a405152d3f | -14.57962 | -39.22045 | 2026-10-07 16:37:00 | NPP-375 | URUÇUCA | BAHIA | Brasil | 2932705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| bf958b00-a51b-3944-a41b-8a84fa0f0a04 | -6.0431 | -42.59113 | 2026-10-07 16:37:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |


[Clique aqui para ver as próximas entradas](README195.md)
