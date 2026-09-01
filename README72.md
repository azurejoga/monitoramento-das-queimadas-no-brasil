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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc102300-fe95-3d7b-85b6-fa3105747ff7 | -7.5894 | -60.4827 | 2026-09-01 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.3 |
| dfaf88f2-6651-3304-a9c2-eb74a0aae0d3 | -7.3487 | -60.5883 | 2026-09-01 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 2f31904f-ac76-32f2-9e4b-b812fd42d6ca | -11.296 | -50.5794 | 2026-09-01 05:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 181.2 |
| af457ece-009d-3e24-aa83-3be32b5a508a | -7.571 | -60.4643 | 2026-09-01 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| ce71a914-fbd1-3463-b7bf-ff8ae831cdc2 | -7.5895 | -60.4636 | 2026-09-01 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 84873935-8236-3420-8a9c-a78ea101ccb6 | -7.5709 | -60.4835 | 2026-09-01 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| b3b6a4cb-ccc6-380f-95df-f7393fb2d307 | -17.22941 | -53.26737 | 2026-09-01 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e694f139-23c8-342a-a9b6-e141301f7bf2 | -18.25495 | -52.73547 | 2026-09-01 05:21:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e1f25c77-1999-3e39-9b14-04143e12964c | -17.94346 | -54.01667 | 2026-09-01 05:21:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f19f89aa-5fda-34aa-9dbf-1e528fe2e28f | -18.25442 | -52.73956 | 2026-09-01 05:21:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 06360387-08e5-3a36-85bb-acc0a29f1ae6 | -17.72585 | -49.22898 | 2026-09-01 05:21:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d749bda-e6d0-3bb5-a8c6-b1cd50c8c822 | -18.25113 | -52.69771 | 2026-09-01 05:21:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af35cea9-bf20-3b3c-b8ae-21fe28c6eee3 | -18.25547 | -52.73138 | 2026-09-01 05:21:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d0a2583a-2800-3ea2-af19-5ac4804c24f4 | -17.22536 | -53.26692 | 2026-09-01 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3d47670-7608-3902-8195-9f9a0cee232c | -17.72053 | -49.22844 | 2026-09-01 05:21:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfaf3a32-6fdf-3118-9509-4756b693b5b8 | -19.57195 | -45.71809 | 2026-09-01 05:21:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dd3fcbf7-4863-3f2e-ace3-83af52404935 | -17.5472 | -50.64238 | 2026-09-01 05:21:00 | NPP-375D | SANTO ANTÔNIO DA BARRA | GOIÁS | Brasil | 5219712 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 304d1375-3860-36cd-bc0f-2a4c4584e347 | -17.88195 | -52.1633 | 2026-09-01 05:21:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e5503f55-b0e1-3bea-b6ba-ddc570d4683d | -17.18765 | -54.30918 | 2026-09-01 05:21:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14931604-28f2-3b24-9796-74d515973bd4 | -18.51605 | -48.23392 | 2026-09-01 05:21:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dba0298d-4a4d-3d1e-9ff5-4fac80e9133f | -17.18651 | -54.28945 | 2026-09-01 05:21:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b8cb96d-578b-38b4-b1a5-a06512154f72 | -17.9033 | -52.09933 | 2026-09-01 05:21:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ffaf81c-b877-3d0b-b88f-95726e20af2a | -20.54215 | -47.80178 | 2026-09-01 05:21:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2eca9f4-8ff5-3b04-8d68-958ed30d9bf6 | -18.25061 | -52.70181 | 2026-09-01 05:21:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fce68d57-1561-3966-8804-13db48c66db9 | -17.94736 | -54.01722 | 2026-09-01 05:21:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11272d70-3da5-370f-8a9b-07eabe4aaf11 | -18.2507 | -52.73498 | 2026-09-01 05:21:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f27ad1cb-725a-3c1b-b36b-ccc416ec829a | -18.51411 | -48.2354 | 2026-09-01 05:21:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad933391-8219-39e1-805f-de2b0e036f4c | -18.25866 | -52.74014 | 2026-09-01 05:21:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f4fc892-bca4-3cb9-b245-5e146d3f930a | -17.19147 | -54.30958 | 2026-09-01 05:21:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bca82c20-b9bf-3194-9b74-b0fdf6337e39 | -18.25122 | -52.73089 | 2026-09-01 05:21:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a2e17663-f530-39b6-96ad-1a7c2fac095d | -17.22583 | -53.26336 | 2026-09-01 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26012475-a32d-3462-a732-47d807c3db87 | -17.88852 | -52.1105 | 2026-09-01 05:21:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff3efdec-6c54-3c00-8ee6-49360549668a | -24.5633 | -53.79727 | 2026-09-01 05:23:00 | NPP-375D | TOLEDO | PARANÁ | Brasil | 4127700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b02d2478-a6b2-3685-9a25-524f936c64f8 | -24.56759 | -53.79794 | 2026-09-01 05:23:00 | NPP-375D | TOLEDO | PARANÁ | Brasil | 4127700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6c36ea64-be12-381d-957a-69a4c9cc1779 | -6.9551 | -55.655 | 2026-09-01 05:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 1d5b0947-ef1a-332a-97e5-dcba83c3f01e | -11.315 | -50.5774 | 2026-09-01 05:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 45ba315e-485d-321e-96a2-68c4062fd863 | -16.0547 | -54.3908 | 2026-09-01 05:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 1acff9d8-3906-334c-8ca2-35ecf25c9542 | -6.9736 | -55.654 | 2026-09-01 05:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 97b0599a-2d54-3457-aaf4-d1b2845998f0 | -7.3487 | -60.5883 | 2026-09-01 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 30bc765a-be0d-311d-897d-41a29f89d465 | -6.9552 | -55.635 | 2026-09-01 05:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| ba3f6304-99fc-3c29-96d0-2eaabe92248a | -3.1304 | -61.17879 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da3e7610-0f3c-33dc-b586-bc45ab63d228 | -3.61125 | -59.07642 | 2026-09-01 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70aeef08-00ee-33a7-b249-a131557b35b5 | -3.60897 | -59.06802 | 2026-09-01 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12c91611-de6c-3fa2-a867-19b996b558dc | -3.20993 | -61.16953 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72ca0125-80ad-3766-b6d2-a495b215b169 | -4.14971 | -60.69868 | 2026-09-01 05:33:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2ce4813-db95-3cc2-ad63-c01b27edb9c2 | 0.00928 | -60.60041 | 2026-09-01 05:33:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3c4a6fc-1eff-34c8-bff5-6b153d492675 | -4.95889 | -55.85581 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13769c4b-e224-3875-90ac-a6cbf1f66840 | -3.13426 | -61.17587 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16decf33-8a7a-38e9-ab7b-845b04d357bc | -4.1603 | -60.69672 | 2026-09-01 05:33:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40506d1c-b2ae-3cef-ba6a-d638f9618fa3 | -3.79325 | -59.34586 | 2026-09-01 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04e616b4-e50d-31e2-88be-066195ce9ea2 | -3.8339 | -55.56147 | 2026-09-01 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afa8f941-5653-3491-97b4-dc726ced2429 | -4.79824 | -55.9723 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d1b261c-25b4-38d1-b9b6-f19277bfd3cd | -4.1564 | -60.69973 | 2026-09-01 05:33:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 981cb676-dd91-3523-99ec-b6938132ff94 | -3.13317 | -61.18277 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cc2d29f-9cd4-38ea-a28d-11d4c561d5c7 | -3.25692 | -60.65774 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42b6217a-1e02-30a8-810d-baa28411ef07 | -3.18977 | -60.15371 | 2026-09-01 05:33:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| def10476-015b-31ed-a177-d566a931a656 | -3.87687 | -59.56475 | 2026-09-01 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75540847-7c90-3eb4-9821-1b7456d908e3 | -3.87801 | -59.56553 | 2026-09-01 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af300d33-69a5-3048-a69a-ed50af37551e | -4.15644 | -60.72142 | 2026-09-01 05:33:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c49dab48-8a7c-3a0d-afb3-869f61d3715c | -2.66737 | -59.37296 | 2026-09-01 05:33:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 684fdc69-baed-312d-a19e-e6e0ae28757f | -2.66796 | -59.36921 | 2026-09-01 05:33:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7da895d-9cae-35c8-adc3-2d0e70d3c17b | -4.15695 | -60.6962 | 2026-09-01 05:33:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da6b5824-c3b4-3ba0-a14c-c09567fa359e | -4.15026 | -60.69515 | 2026-09-01 05:33:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20818d37-3928-3165-8ba9-0c14f6facbea | -3.12223 | -61.23052 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 457d23fd-929c-37d7-b302-4b940016fcf6 | -3.40024 | -61.31985 | 2026-09-01 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6836553-2ee3-33d3-be44-685b546d9544 | -3.1123 | -61.22897 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 989444cb-740f-316e-9462-e570933351ec | -3.11285 | -61.22553 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0a47ef0-0007-329a-90ca-6d83339a1d38 | -3.11176 | -61.23242 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcf75ba4-86bb-3c93-9bb6-f2558e940a7f | -3.11892 | -61.23001 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88d9d595-dcad-3c8d-b443-32a25cf66604 | -3.34523 | -59.43187 | 2026-09-01 05:33:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf2251fa-8f7a-3f69-bbdd-9274f7d407bb | -4.15081 | -60.69162 | 2026-09-01 05:33:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d14ea407-5c44-33d2-96ec-df4ca37c173a | -1.46759 | -54.23493 | 2026-09-01 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9e975e1-b88f-3b36-8b1f-a7042928b907 | -1.46686 | -54.23968 | 2026-09-01 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 118a3ca7-1637-3800-b8ab-87b9de3404a3 | -4.14636 | -60.69816 | 2026-09-01 05:33:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b001ed7e-38ef-38aa-ae2a-10f30e5efef0 | -1.46224 | -54.2391 | 2026-09-01 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acf2188e-3813-3d44-bd54-646009c422eb | -3.61187 | -59.07249 | 2026-09-01 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c80efd17-5b6e-376a-8a8d-cec7481a0e02 | -5.24413 | -55.90603 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aca1557f-39eb-32b6-8438-b01b1b97524f | -3.12986 | -61.18225 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c757d790-f27c-3573-bbd7-d8e27aa5088f | 0.1439 | -60.39929 | 2026-09-01 05:33:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 623f7fd7-354c-3577-9c3a-8fe5c1326be7 | -3.61601 | -59.0691 | 2026-09-01 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8f18e78c-a05a-350f-859c-0326e7dece92 | -3.09679 | -61.19829 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92a07966-431a-36e9-a4cd-dea086b42cab | -3.41353 | -61.34312 | 2026-09-01 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9e95a14-f0d2-32c2-aeb6-95e348722f80 | -1.47221 | -54.23551 | 2026-09-01 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94b16333-96fa-3b6c-a7c5-bf59fb87727f | -3.41022 | -61.34261 | 2026-09-01 05:33:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ebaebc3-225d-3dc9-bef9-f7cb4a76d23f | -5.24911 | -55.90248 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86fe1de3-e981-3540-802f-33458762c68d | -3.06962 | -61.2184 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ef5e108-055a-30b8-a643-59ad68fa9320 | -4.79761 | -55.97651 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0e441a62-cd76-30a1-be6a-8838e5e374a9 | -3.96835 | -60.01623 | 2026-09-01 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a5eac39-3c5a-3a5b-bdb9-0128e85e92b2 | -4.1525 | -60.70273 | 2026-09-01 05:33:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9877806e-f5aa-3b2a-9854-ff83be09a4a9 | -3.11561 | -61.22949 | 2026-09-01 05:33:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6560a360-9fcb-311b-8002-b15c44f7b6eb | -3.63599 | -60.55424 | 2026-09-01 05:33:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b97e6cbc-db90-3d16-961b-cd668ed842ea | -4.96577 | -55.83974 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cf00e0c-22e8-359f-b40e-32195baecee0 | -1.47369 | -54.22585 | 2026-09-01 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 777a632a-3b6d-3873-bd90-bd780898a1e8 | -3.63803 | -59.55264 | 2026-09-01 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 393bf2d2-e885-3727-b6be-2cdc091603fc | -4.96951 | -55.84445 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ae22d02-f03c-33c3-8614-15db531b8cbd | -4.1536 | -60.69567 | 2026-09-01 05:33:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 917d3c91-63bf-3fa4-86bb-11bb57e33fb2 | -4.29157 | -49.10714 | 2026-09-01 05:33:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 97e14232-9389-34eb-81c0-9a4aa9bbd5a5 | -4.0672 | -60.72933 | 2026-09-01 05:33:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4e5801e-9753-3610-86a4-5596d6647bbd | -4.85514 | -55.82885 | 2026-09-01 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81210f6d-a096-37d6-9227-0b9c42eae777 | -3.6198 | -60.5481 | 2026-09-01 05:33:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README73.md)
