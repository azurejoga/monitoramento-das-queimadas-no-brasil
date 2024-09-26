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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fade52ec-94ac-34f5-b055-660b14d8564b | -8.8098 | -58.2172 | 2024-09-26 02:45:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 9ead540e-2971-334b-9c55-f6a4af4c7e0a | -9.086 | -61.1245 | 2024-09-26 02:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| f06754cf-2e71-3f96-8a46-76181a555caa | -9.1035 | -61.2769 | 2024-09-26 02:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| b5759d64-7414-3f04-a066-034ca5045723 | -9.1046 | -61.1237 | 2024-09-26 02:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| a721f5c8-a651-30d5-b588-7bb489ebe5c6 | -9.6015 | -50.1566 | 2024-09-26 02:46:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 88f70841-8347-3854-b655-27a0043ab202 | -9.6018 | -50.1352 | 2024-09-26 02:46:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 916606b6-5158-312e-a274-6a105709b9b6 | -10.3882 | -67.8737 | 2024-09-26 02:46:06 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 47.3 |
| f9ce42dd-9db3-323c-bb46-ee43d8958f83 | -10.9105 | -57.4308 | 2024-09-26 02:46:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 7cf85c51-3c88-3953-8aac-68501f169245 | -11.2412 | -65.2997 | 2024-09-26 02:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 40.2 |
| e226fddc-9a4f-36fc-bbcf-ce69df5f2b1a | -11.2413 | -65.2809 | 2024-09-26 02:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 38.5 |
| a3920066-82e7-30a1-95dd-61fea96c501e | -11.2599 | -65.299 | 2024-09-26 02:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 166.0 |
| dd3012f8-0ecf-37f8-8cb5-5519f500e504 | -11.26 | -65.2801 | 2024-09-26 02:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 158.4 |
| 115c8893-a6fc-36f1-bbb8-c8fbdf47e2d8 | -11.2786 | -65.2982 | 2024-09-26 02:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| fb866432-1603-3a24-af4e-40925c7b6521 | -11.2788 | -65.2793 | 2024-09-26 02:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| b752832a-86e5-3f0c-a365-bf3941a13779 | -11.955 | -60.363 | 2024-09-26 02:46:14 | GOES-16 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 2f822f0d-ef31-3f96-a1da-520d1c936a7e | -12.2175 | -45.5074 | 2024-09-26 02:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| ef09ab86-34f6-3504-8eed-f4e1f7898065 | -12.2367 | -45.5045 | 2024-09-26 02:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 430e5724-cbfd-3486-9629-fe2f3c74cc67 | -12.5026 | -48.9198 | 2024-09-26 02:46:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| ed225b68-a020-30ce-a733-a3df3d1c4a74 | -12.5273 | -53.5168 | 2024-09-26 02:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 5bdafd50-6ca3-369b-97cd-34dff69c5359 | -12.5276 | -53.496 | 2024-09-26 02:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 230.9 |
| c052c9f7-f466-351e-b276-1c47a47e3835 | -12.5279 | -53.4752 | 2024-09-26 02:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| e663432f-cc17-3a91-8b5a-09347adccf7b | -12.5464 | -53.5147 | 2024-09-26 02:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 130.5 |
| a7b337ca-0fa0-3483-9979-76f42a4d539b | -12.5467 | -53.494 | 2024-09-26 02:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 223.1 |
| df947cd4-09cb-30d8-960b-11035dba5719 | -12.822 | -62.7078 | 2024-09-26 02:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 89c9c458-3324-3ea4-8006-2118d1893add | -12.8222 | -62.6886 | 2024-09-26 02:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 35.2 |
| c5226b81-7524-3221-a3e9-754992c633c8 | -12.841 | -62.7067 | 2024-09-26 02:46:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 164.3 |
| c7e052e3-4f10-3c0d-a684-1c858ceedba1 | -12.8411 | -62.6874 | 2024-09-26 02:46:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 6bba8dd1-fcb9-3622-976b-a35bd0859322 | -12.8599 | -62.7056 | 2024-09-26 02:46:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 6f9f4413-1a42-303d-869c-c9b0271f61ad | -14.8824 | -51.4992 | 2024-09-26 02:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 20a35540-51de-3762-8c0b-70a7c9d7c305 | -14.896 | -57.9873 | 2024-09-26 02:46:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| ff839306-60a3-3ae1-b379-598b205d90e4 | -14.9153 | -57.9854 | 2024-09-26 02:46:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 9e2defe5-2649-3a3c-9f95-aabc82237c07 | -15.3564 | -58.1632 | 2024-09-26 02:46:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| cfac554f-00ff-3f4e-942a-db552fc3e6f7 | -15.3175 | -58.1872 | 2024-09-26 02:46:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| d004a42c-82d0-3abf-8003-5752141d3c3b | -15.3178 | -58.167 | 2024-09-26 02:46:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 2dfff73e-6cb2-3fef-a146-c6ceee6798a4 | -15.3368 | -58.1852 | 2024-09-26 02:46:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| f0229b96-9681-36c3-924b-cb63ca5e9040 | -15.3371 | -58.1651 | 2024-09-26 02:46:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 3311ec5a-ca26-3bac-a5ff-d976b684d577 | -15.3562 | -58.1833 | 2024-09-26 02:46:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 4ceeb149-5439-3c2f-bd6d-dc75af6bac95 | -16.098 | -52.0111 | 2024-09-26 02:46:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 3ffa2efe-0858-36be-9e31-08bd3a9d5477 | -16.0985 | -51.9896 | 2024-09-26 02:46:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 5761a723-6bb1-3524-aba7-bed6e13ead1c | -16.1176 | -52.0082 | 2024-09-26 02:46:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 191.6 |
| f171553a-4171-3466-b566-0b5bdde05ebf | -16.118 | -51.9867 | 2024-09-26 02:46:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 208.8 |
| 3a37d741-1b9d-3171-a6d3-f8f823c00662 | -16.7312 | -55.9275 | 2024-09-26 02:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 49.0 |
| 373dbe60-0a83-3cf9-b165-4a54844b9470 | -17.0402 | -56.1785 | 2024-09-26 02:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 42.9 |
| 4c7c1b55-59c7-321f-a77b-0426f702e0a4 | -17.0791 | -56.1943 | 2024-09-26 02:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.4 |
| 626225df-b511-31e5-b893-918676d4ee9f | -17.0795 | -56.1736 | 2024-09-26 02:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 43.5 |
| 2dbc6f88-b8f0-361c-b9bb-f658ee19931a | -18.264 | -41.3217 | 2024-09-26 02:46:47 | GOES-16 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.8 |
| 1c8a118f-0bb1-33d4-8ee6-3ca3add1343c | -20.587 | -51.5249 | 2024-09-26 02:47:00 | GOES-16 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Mata Atlântica | 70.2 |
| 04700729-5f19-3122-9122-e35459df7f72 | -20.5876 | -51.5026 | 2024-09-26 02:47:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.4 |
| 1fa8e963-8e40-32a9-b475-82c053f004c6 | -20.6074 | -51.5209 | 2024-09-26 02:47:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 365.4 |
| e105519a-2068-3148-81e9-22cd37c33e5b | -20.608 | -51.4986 | 2024-09-26 02:47:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 330.9 |
| cebbf53c-7b46-342c-84fd-50f315de2072 | -20.6279 | -51.5169 | 2024-09-26 02:47:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 322.9 |
| 1ec37b9f-14bf-3eaf-9343-3f3320a50e9b | -20.6284 | -51.4945 | 2024-09-26 02:47:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 224.3 |
| d6e3ddee-3721-389b-af72-93561cf9d62b | -21.9374 | -48.5688 | 2024-09-26 02:47:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 8f158f11-b604-3574-a51b-6d5bfbc67fe6 | -21.9381 | -48.5453 | 2024-09-26 02:47:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 26c10a81-5496-3f9d-899d-42c72bbc6e0d | -22.2162 | -47.5603 | 2024-09-26 02:47:08 | GOES-16 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.1 |
| c64aefa2-33d3-35fa-a572-f882c6398216 | -2.6785 | -57.531 | 2024-09-26 02:55:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 2676c1c4-6352-3589-afd5-215c85aa6301 | -2.6968 | -57.5307 | 2024-09-26 02:55:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 7b91edd2-713b-3541-9d78-3424546356db | -3.3505 | -53.7775 | 2024-09-26 02:55:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| e17db60d-5655-3157-baa6-d80d7ea76aed | -3.5673 | -50.3794 | 2024-09-26 02:55:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| f092a6ce-f442-3170-b9dc-21f731e537d0 | -3.5488 | -50.38 | 2024-09-26 02:55:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 7d9865a7-34a4-3d42-81b1-690c362344fe | -3.9208 | -46.4459 | 2024-09-26 02:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 78.4 |
| cf93bd01-b109-3b78-94cf-89f1e95620a8 | -6.8024 | -59.3044 | 2024-09-26 02:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| fa71bab0-3cde-3928-b706-93906343c15c | -6.949 | -63.1048 | 2024-09-26 02:55:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 63bd080c-052b-3327-b541-583063a4c709 | -6.9306 | -63.1053 | 2024-09-26 02:55:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 755f61e1-437a-382b-b5e0-68a5c0afb86b | -6.9305 | -63.1241 | 2024-09-26 02:55:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 2d5fb6ba-b528-3d2a-90d7-9a3ffdccb41d | -7.3824 | -55.4924 | 2024-09-26 02:55:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 4b8af837-1d15-3b30-9e81-ba607ed44eba | -7.3823 | -55.5124 | 2024-09-26 02:55:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 176.0 |
| de6454be-eb07-3f07-b48f-e42d84cfb383 | -7.3639 | -55.4935 | 2024-09-26 02:55:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 6f689067-687b-361c-b950-ca8a1a5cd837 | -7.3637 | -55.5134 | 2024-09-26 02:55:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 211.5 |
| 35e5ae1d-7280-3dee-8ef1-8fd675c23d40 | -7.3636 | -55.5334 | 2024-09-26 02:55:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 4fef18c2-314e-3056-9888-74d64e5f68a7 | -7.5894 | -42.2971 | 2024-09-26 02:55:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| c2b03f4c-25bb-3712-ab11-70adc9459d5f | -7.8341 | -54.724 | 2024-09-26 02:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 06815be8-b22e-3d5e-bd3d-e36867e80d69 | -7.834 | -54.7442 | 2024-09-26 02:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 92708d77-1d95-3e05-a442-3cf4ea15b4ce | -7.8156 | -54.7252 | 2024-09-26 02:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 316.4 |
| 94362ef1-447c-384d-b0fd-ec2f51991454 | -7.8154 | -54.7453 | 2024-09-26 02:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 236.4 |
| fd4dff07-55d7-38e9-bd27-232e47d7cec2 | -7.797 | -54.7263 | 2024-09-26 02:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| d21d3d18-ec38-357b-8cd3-d8ab83f1ecf0 | -8.1394 | -61.2817 | 2024-09-26 02:55:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 9507adb1-4164-335b-948a-35c839230436 | -9.1046 | -61.1237 | 2024-09-26 02:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 74e3f7c9-9ace-35a4-bd52-32eb17053a93 | -9.1035 | -61.2769 | 2024-09-26 02:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.4 |
| c40fc527-9379-3e31-80fb-90026c829afb | -9.086 | -61.1245 | 2024-09-26 02:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 153b10c7-3029-3850-b90f-f314c7c7dcc4 | -9.0468 | -61.4325 | 2024-09-26 02:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 0a4a2c62-8bb7-396f-9ed8-ad05ee4a5006 | -9.3462 | -51.0704 | 2024-09-26 02:55:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 8a75ca8d-35ce-36bc-a7ee-4955f6b8973e | -9.6015 | -50.1566 | 2024-09-26 02:56:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 4e7ec20e-face-3ecd-ba53-e5fd521432a3 | -10.0515 | -53.4432 | 2024-09-26 02:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 2e4f0a58-54cf-3a98-9ec6-a646e7f4eca7 | -10.0513 | -53.4638 | 2024-09-26 02:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 03e23f7b-761b-3a98-a0ab-629ef4c2356d | -10.0327 | -53.4448 | 2024-09-26 02:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| e7b26776-f889-3862-bb16-e4904fcd1f9b | -10.0324 | -53.4654 | 2024-09-26 02:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 84d30dba-4d51-387b-94a8-d711dd71f05a | -10.0322 | -53.4859 | 2024-09-26 02:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 192ae63e-d12b-34e4-9da6-2411f5f37878 | -10.032 | -53.5065 | 2024-09-26 02:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| b6bacc6f-a54b-34a1-b4ce-2df7abd51c21 | -10.9105 | -57.4308 | 2024-09-26 02:56:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 1d3b68a0-adff-3269-8e16-70ce7c224731 | -11.2599 | -65.299 | 2024-09-26 02:56:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 62cb0cee-1fb3-3410-86c0-c0396eac2f4b | -11.2413 | -65.2809 | 2024-09-26 02:56:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| cd51e4e1-b0e0-3f53-afde-1a0a33c656a8 | -11.2786 | -65.2982 | 2024-09-26 02:56:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 79.8 |
| e51df1f1-deed-3308-ab06-3e7051d283af | -11.2412 | -65.2997 | 2024-09-26 02:56:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| f1e2c0e2-c9c3-3c73-af40-2105926caeef | -11.2788 | -65.2793 | 2024-09-26 02:56:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 28c987d9-06e9-3ddd-a272-9577b822c81e | -11.26 | -65.2801 | 2024-09-26 02:56:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 139.0 |
| bbfe6f36-ffff-3c56-a70b-715e47b47b46 | -11.6988 | -47.8576 | 2024-09-26 02:56:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 4a210a1d-adfc-3466-a454-895bae387d23 | -11.7179 | -47.8551 | 2024-09-26 02:56:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 44c17c9f-0e45-3636-a8db-511256a04ff3 | -12.2367 | -45.5045 | 2024-09-26 02:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| d25cb0fb-ce12-328b-978c-c507649e8262 | -12.2175 | -45.5074 | 2024-09-26 02:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |


[Clique aqui para ver as próximas entradas](README48.md)
