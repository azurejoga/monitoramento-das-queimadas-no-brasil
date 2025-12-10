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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b73fc027-e6f1-3b46-be08-777ecce01089 | -3.43787 | -41.653 | 2025-12-10 04:36:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 34b4bae2-7d7c-316e-b995-93896e85e582 | -2.38858 | -45.81956 | 2025-12-10 04:36:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc4bcdd0-3abe-3b6c-8321-b740906066d4 | -5.38871 | -44.82707 | 2025-12-10 04:36:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db6bec66-3277-3d1d-bf42-3042f670e52f | 0.60761 | -51.56585 | 2025-12-10 04:36:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 897dd1a9-142c-3687-beab-f86eab5095c7 | -2.07264 | -49.0065 | 2025-12-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f45077a-53d5-337d-aff7-4b0ea7bf4679 | -2.02945 | -52.05249 | 2025-12-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c98e3bdd-6e80-3bcb-bbd4-ebadb2eeec06 | -3.08991 | -52.7869 | 2025-12-10 04:36:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c52818b1-755d-370b-a3c5-2c67d0f3259b | -2.37898 | -45.61713 | 2025-12-10 04:36:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c18690ba-ac99-3c89-94e3-44dab3a11df2 | -2.3512 | -45.99107 | 2025-12-10 04:36:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7160c8bc-5051-3c60-ad02-5790dd8e611a | -3.67997 | -43.82155 | 2025-12-10 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 45e10650-b038-369c-9944-3969b1f1f9bb | -3.84491 | -50.9674 | 2025-12-10 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 468b03ff-cae3-30c0-8d56-9dbbeb9885f8 | -4.20454 | -47.11494 | 2025-12-10 04:36:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2951b3a-d87a-303c-abf4-8726e1436b18 | 1.16097 | -50.70987 | 2025-12-10 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 355ec775-179d-3e8e-aefd-77e4d1deb6f9 | -5.17254 | -43.11401 | 2025-12-10 04:36:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 395fa3c3-f791-3322-9cb8-d33024dd5926 | -2.80324 | -47.35012 | 2025-12-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10d942b3-58ee-3fa6-91ec-0e54cc9ec682 | -0.97548 | -52.43752 | 2025-12-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f7dc97c-4297-39ca-ab40-051cf8bf7499 | -2.06574 | -49.00541 | 2025-12-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80ea10a6-d5ee-37cb-9810-2255e989bf87 | -2.79937 | -47.35305 | 2025-12-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd8f5405-14a1-3ae8-ad6d-9bdf38dd779a | -1.64202 | -45.72578 | 2025-12-10 04:36:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00d76b92-25d8-3ea4-867c-9efc0066c498 | -2.12826 | -47.65543 | 2025-12-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2786ede9-1829-39d6-8800-fd1f0e22ddce | -4.81045 | -41.83232 | 2025-12-10 04:36:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7a5faed7-04f1-3700-ac44-706395d22447 | -5.35566 | -38.05975 | 2025-12-10 04:36:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 59711c13-3157-3dde-a2b1-fa4604d0031f | -5.67371 | -39.60213 | 2025-12-10 04:36:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 97c55dad-9c53-3234-8656-fcc2bb530f28 | -3.69104 | -43.82323 | 2025-12-10 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 134b29d2-16ad-3aa9-ad5c-b388bf5f18e3 | -2.74772 | -48.38641 | 2025-12-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a83c2a88-422f-37d3-bbed-56c690b56423 | -2.26579 | -46.08604 | 2025-12-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70267b53-fd01-32df-8fa0-996e9a2a6828 | -5.58841 | -39.77283 | 2025-12-10 04:36:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d9ec21c4-aaf3-3e13-990e-da63093870d8 | -2.83432 | -45.84813 | 2025-12-10 04:36:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12a3346e-e4b6-3bd8-b666-1ad3e07c7d2f | -1.41968 | -54.29442 | 2025-12-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c18ae37a-963f-37d4-ad7c-a04813ba32e5 | -0.61591 | -51.82964 | 2025-12-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5102edc6-828a-3e30-bb73-84619169e0cf | -4.91519 | -43.4651 | 2025-12-10 04:36:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4a89c33c-138c-3922-8b7e-d91b985028a0 | -2.80101 | -47.34271 | 2025-12-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa0dc5a9-b358-3f96-a8fa-db2757f07810 | -2.81753 | -45.27113 | 2025-12-10 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e29219b0-67a1-3f9b-bd7d-b06b97026e3f | -3.39795 | -42.10725 | 2025-12-10 04:36:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2dd22167-afb6-36f1-a5aa-d44620d76e6d | -2.85111 | -45.27563 | 2025-12-10 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e35de81f-ebe3-3937-9a31-7dd3b76e2ca1 | -3.42408 | -41.65876 | 2025-12-10 04:36:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3b1a27ba-9db1-37df-b35b-9a2eae40b1f4 | -5.14727 | -43.8645 | 2025-12-10 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80e38182-b633-38bb-8880-82efe016059a | -5.16788 | -43.11832 | 2025-12-10 04:36:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d1ba277e-4e86-3d12-b0e8-86ce7cf7856f | -3.23963 | -45.29615 | 2025-12-10 04:36:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ab0b1c5-1638-3487-b11a-7ceed54efaf6 | -2.6423 | -45.56139 | 2025-12-10 04:36:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe54763d-2f5c-3343-b896-19dc81b0155f | -3.42045 | -41.65426 | 2025-12-10 04:36:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b2940c83-25e3-3071-9eec-09e9f3e16f0d | -3.23447 | -47.47121 | 2025-12-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a243f7fb-2c92-3d24-8cf9-f86cffbc3f1a | -4.31264 | -50.67935 | 2025-12-10 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c37b76fd-6651-3f78-baed-219e738a90d9 | -2.35685 | -48.07527 | 2025-12-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb155ab6-4926-397c-bd23-387e57b4457e | -3.69036 | -43.82756 | 2025-12-10 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e056fae6-5e14-3d8d-97fe-d7af173d1ace | -6.36167 | -39.4949 | 2025-12-10 04:36:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6ae7f8bd-52fe-3987-9e1a-762690f122a0 | -5.5302 | -41.65947 | 2025-12-10 04:36:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 92963991-26ea-34cd-9af6-9b1c556b1288 | -3.46533 | -42.01693 | 2025-12-10 04:36:00 | NPP-375D | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 88a0cb44-4494-324a-99dc-dd1fd74f8d8e | -3.17463 | -52.87499 | 2025-12-10 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e200fdfe-d035-3347-8a9b-a86c31b7d005 | -2.74435 | -48.38587 | 2025-12-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 14aea665-b63f-3849-b8c1-75e8caad6a17 | -4.11115 | -46.48373 | 2025-12-10 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb022779-a8d8-3dad-be28-1751fd96835f | -2.01802 | -45.53244 | 2025-12-10 04:36:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d311ed4-bec1-37b7-abb2-56c2636cce12 | -3.43726 | -40.8288 | 2025-12-10 04:36:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 16719978-764f-3700-8725-065f014e0624 | -2.84305 | -48.90897 | 2025-12-10 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 63722312-d672-3713-8d55-c4582ac11728 | -1.6732 | -45.77731 | 2025-12-10 04:36:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad5741e5-e54b-3aa3-80eb-1499eeb68ad5 | -4.29477 | -45.93578 | 2025-12-10 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc8b14d1-001a-3bd6-8c70-fe68780f4f31 | -2.26082 | -53.7058 | 2025-12-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 264c5988-ae77-32f5-9176-ab3a53322358 | -3.18954 | -52.02406 | 2025-12-10 04:36:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd778ee3-c862-3399-bc17-41c0593c4a0d | -2.26384 | -47.86946 | 2025-12-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4b7391de-0a1e-3550-b818-6d47b9a11700 | -3.70126 | -50.94976 | 2025-12-10 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58620661-f99f-3684-a36c-b8779c4ced2c | -4.02724 | -51.20258 | 2025-12-10 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44f8d3d6-f1a8-3d36-ae3a-da2a7004810c | -2.51313 | -45.43054 | 2025-12-10 04:36:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cacb0f8-556c-3d7f-8763-84f5f91b4e55 | 2.02599 | -55.66926 | 2025-12-10 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c54b27a-9e46-385b-a743-d5a57287b767 | -3.58686 | -41.66702 | 2025-12-10 04:36:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e995bb2f-2285-3f81-b361-897d25d661c7 | -2.12716 | -48.73029 | 2025-12-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6fcb4acf-ad16-39c8-8609-fdccb230e2fe | -3.42466 | -41.6549 | 2025-12-10 04:36:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6561e86c-bb19-3a50-9636-cb7301445444 | -3.686 | -43.83132 | 2025-12-10 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 874c7424-fa91-3abe-ac08-c556e314542e | -3.59107 | -41.66765 | 2025-12-10 04:36:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c2f55f47-4e4d-3bb6-977f-b325f15f2abb | -3.53913 | -53.25704 | 2025-12-10 04:36:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79595e26-2567-326b-98a9-c529404cba96 | -1.53746 | -49.44341 | 2025-12-10 04:36:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89f9ceed-054d-385c-8063-c214aed8ff02 | -4.03542 | -50.38393 | 2025-12-10 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad46b750-4417-3252-b369-5b1cbfc8fbfe | -3.51945 | -47.20888 | 2025-12-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dd2a7eb0-fe73-3f4b-9495-6bd5c40bf7e7 | -2.88488 | -45.23919 | 2025-12-10 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 50eb797c-211c-3df7-be5a-65ad5a076427 | -2.07204 | -49.01024 | 2025-12-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1be42d20-60bd-36b0-b5ce-cd71601e5789 | -2.32037 | -48.59234 | 2025-12-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f84c4b4f-cfdf-3aeb-b88e-2c1af8bce39b | -1.06916 | -47.12022 | 2025-12-10 04:36:00 | NPP-375D | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9324b57d-715b-3bdf-8653-1a95bee8498c | -3.57907 | -52.11095 | 2025-12-10 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62439c21-d287-35c3-8914-7aa4ee9d8e44 | 2.02706 | -55.67617 | 2025-12-10 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e102fa2-4415-36f9-b899-4819133bebb4 | -3.68735 | -43.82266 | 2025-12-10 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f32138fa-0bbc-3aa9-98cb-2b56bab0dbeb | -3.5809 | -52.11377 | 2025-12-10 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3af2da17-e9ec-3b2f-bdaa-0700e1205931 | -3.17526 | -52.87114 | 2025-12-10 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8f36c0f9-ee33-3798-86b5-74e1839aa110 | -2.2956 | -46.10469 | 2025-12-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 802ee130-71ff-3167-a276-8ddff2390fac | -1.08491 | -48.21194 | 2025-12-10 04:36:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2188611f-02c6-3320-9074-cea5ae1e0e09 | -3.42828 | -41.65941 | 2025-12-10 04:36:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8b5165b6-1e87-3bb0-b35f-480a6c2ad971 | -3.41947 | -52.64708 | 2025-12-10 04:36:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c039d24d-03e5-3e27-811a-3957b0f7e94b | -3.6954 | -43.81948 | 2025-12-10 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f23f3e3-7c03-351b-a567-c870e004dd5e | -2.3955 | -46.48395 | 2025-12-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 521df705-e644-3232-8b13-72b5d1f94536 | -5.16863 | -43.11337 | 2025-12-10 04:36:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2fb885a4-fbd4-3d4d-a021-2046c9d2d31d | -3.72644 | -47.12102 | 2025-12-10 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e97ba32e-dd00-39be-b9da-e5d9faf12710 | -2.26139 | -44.61361 | 2025-12-10 04:36:00 | NPP-375D | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c2689fc-4fe9-3f4c-82c9-7bab56ad106d | -2.02083 | -45.53655 | 2025-12-10 04:36:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cfc09eaa-6f62-379d-8745-5e308386d822 | -3.69828 | -50.94469 | 2025-12-10 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7ca0b7d-2251-339b-a13f-d7a3eb68fafd | -3.43652 | -40.83377 | 2025-12-10 04:36:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0cd283e4-d914-32b2-9b13-8ab68fce44ba | -2.6479 | -46.96225 | 2025-12-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cde334bd-73bb-3c93-8d6b-a70a978136be | -3.70199 | -50.94532 | 2025-12-10 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36a7e18d-0f6d-37c0-8e96-fd4fb87392e9 | -2.0214 | -45.53296 | 2025-12-10 04:36:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1508c95d-6c91-3fc8-bd27-48504c6fdac3 | 2.01987 | -55.66649 | 2025-12-10 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 468be12a-3879-3a3b-ae54-a8596c303ae6 | 1.1612 | -50.71196 | 2025-12-10 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17cd6d37-3666-35d6-b58e-30660f501225 | -5.74796 | -42.06585 | 2025-12-10 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5f6914a9-bb78-3ac8-a52b-80e537fde702 | -2.15116 | -47.36444 | 2025-12-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README11.md)
