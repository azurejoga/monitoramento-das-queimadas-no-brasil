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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d106bcfa-97c7-31e4-8ff8-0c3f6f39530e | -11.809 | -50.5642 | 2025-09-12 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 5d78526f-2ae7-3a1e-85f5-ff51d48337c9 | -11.5263 | -50.404 | 2025-09-12 06:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 46.5 |
| dadd8e56-a65c-3c1e-95a4-476a018b1bde | -12.9292 | -54.7538 | 2025-09-12 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| d53ccbba-37ab-35c4-bcc0-9a9383ff7b2f | -23.139 | -46.7413 | 2025-09-12 06:10:00 | GOES-19 | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.2 |
| aa9f3917-4fe2-31dc-ae4a-4919d6309cbe | -15.9268 | -51.7785 | 2025-09-12 06:10:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 97640eea-721d-3dee-a4ae-43db24d2c6b7 | -15.5432 | -48.5299 | 2025-09-12 06:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 809d29bd-3c02-3726-8f68-81746fb689cd | -15.5427 | -48.5523 | 2025-09-12 06:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 2f4c862f-e0ea-33f5-b06e-d3f5ddb9f161 | -18.76984 | -48.53506 | 2025-09-12 06:10:00 | AQUA_M-M | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 14ec7f07-9658-3566-a8d6-a9b98d7d505f | -18.58828 | -47.18641 | 2025-09-12 06:10:00 | AQUA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 861feb5d-c751-304b-96d0-66f30aedf54e | -16.09743 | -49.63485 | 2025-09-12 06:10:00 | AQUA_M-M | TAQUARAL DE GOIÁS | GOIÁS | Brasil | 5221007 | 52 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 15ce6a60-f22b-3a14-bc32-e4008dca0aea | -15.22453 | -49.67513 | 2025-09-12 06:10:00 | AQUA_M-M | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| cf1ada3a-b2d1-3de1-8263-34faaa73c650 | -15.22593 | -49.66511 | 2025-09-12 06:10:00 | AQUA_M-M | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 281f8c94-a7d5-38cf-bd05-af5d69e24872 | -14.17812 | -46.20842 | 2025-09-12 06:10:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 9e250d2f-80ad-39e6-8a8a-520ed1645b60 | -17.36512 | -52.92412 | 2025-09-12 06:10:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ac232364-d873-36bd-9668-90df818d5bf8 | -15.01473 | -50.11417 | 2025-09-12 06:10:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 9c29adad-b5b5-3418-823d-db018147cab4 | -20.00819 | -47.64919 | 2025-09-12 06:10:00 | AQUA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| e788fc70-6298-34a1-a1ab-2dee14742616 | -12.81897 | -47.97595 | 2025-09-12 06:10:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 4b4e88e4-6c54-3078-b861-f66be48c7586 | -17.37708 | -52.96458 | 2025-09-12 06:10:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 1366689d-cfcf-34fe-8f65-85a7d2b7162e | -18.77787 | -48.54161 | 2025-09-12 06:10:00 | AQUA_M-M | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9cd481b6-faa6-32e0-aa46-e91d91152303 | -9.89877 | -51.88214 | 2025-09-12 06:10:00 | AQUA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| f04768b2-0a3e-3e1a-9af4-09a8a40c4a65 | -12.85309 | -47.94542 | 2025-09-12 06:10:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5a8d4eaa-9d96-3ec9-84fd-5d5bcb0f7291 | -10.55313 | -51.53226 | 2025-09-12 06:10:00 | AQUA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7c1dc1ef-f30b-3b24-a91c-3464de0431f9 | -10.08974 | -50.38976 | 2025-09-12 06:10:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 804dea1a-6718-30d8-8e6c-4a1de4232dc1 | -17.13258 | -48.49082 | 2025-09-12 06:10:00 | AQUA_M-M | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 43e9e2d7-d515-3dde-9605-bf9dd349c19e | -9.8926 | -51.86195 | 2025-09-12 06:10:00 | AQUA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 3194e151-4363-3915-bc29-177b3d8d27ed | -16.30265 | -50.07006 | 2025-09-12 06:10:00 | AQUA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1998f9c4-c6f9-3820-ade2-713e55594bdf | -12.86288 | -47.94681 | 2025-09-12 06:10:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| cc33309b-8ee4-3c58-88f0-4b4280e2dad0 | -12.93041 | -54.74372 | 2025-09-12 06:10:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| f9bcafdb-4b5b-32ce-8c7c-1002f76211b8 | -15.91194 | -51.78482 | 2025-09-12 06:10:00 | AQUA_M-M | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 11e5b1d8-d426-3d97-bf73-49b179a01aed | -11.97696 | -46.64243 | 2025-09-12 06:10:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6b6a9545-9eb1-385c-96e0-02d72ebd5e3e | -15.12902 | -50.15636 | 2025-09-12 06:10:00 | AQUA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 31.5 |
| becac07a-d41c-3d70-b351-f9df223d8330 | -11.54109 | -50.38999 | 2025-09-12 06:10:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| c8dbd02c-5fbe-347a-abc5-2a97a822f664 | -17.36658 | -52.91476 | 2025-09-12 06:10:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cdc6e88d-627a-3762-a3d7-f5156f225070 | -11.68766 | -46.61998 | 2025-09-12 06:10:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| a4be1061-2a06-3970-bea9-5981de618576 | -9.90022 | -51.87275 | 2025-09-12 06:10:00 | AQUA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 92089d98-fb57-3f9f-b009-e26e070592e3 | -11.42112 | -43.53417 | 2025-09-12 06:10:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 5f56b493-9bc4-3cae-91d1-54c1ab3de10d | -10.70952 | -48.62853 | 2025-09-12 06:10:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 124c4f7d-0e0a-3925-b151-d7ce9e19b052 | -11.5381 | -50.59016 | 2025-09-12 06:10:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 8d10f680-b3bb-3bb0-a7c6-165e967f028e | -14.93624 | -50.08624 | 2025-09-12 06:10:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 926db7f4-930a-3f13-abe2-38c5531c2d28 | -14.50564 | -53.91726 | 2025-09-12 06:10:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 883443e5-2876-3fac-92af-e32248b0cdee | -12.92217 | -54.79401 | 2025-09-12 06:10:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4f42c012-ffb5-3d05-bd4f-7826bc14f24e | -10.7109 | -48.61893 | 2025-09-12 06:10:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| c104be96-6213-3624-b659-1de34cd933b6 | -14.50738 | -53.90659 | 2025-09-12 06:10:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a80f6cf2-e857-33df-ac7b-8897f75182ad | -15.78083 | -52.23079 | 2025-09-12 06:10:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c9a5b894-e82b-3e46-9511-d63c87495683 | -14.43439 | -48.41901 | 2025-09-12 06:10:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 373ba3e7-f57f-3050-a731-fe9083efb784 | -10.55124 | -51.48528 | 2025-09-12 06:10:00 | AQUA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7e6312d1-ad3b-39e6-8e22-188b54a462c3 | -15.0071 | -50.10332 | 2025-09-12 06:10:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 98d7a9d7-87bd-37ff-8626-798c21e76706 | -12.10228 | -44.86955 | 2025-09-12 06:10:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 95da5164-6de7-379e-a4dd-10abea985373 | -11.80896 | -50.5683 | 2025-09-12 06:10:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 0cd9f651-c04b-3529-840a-2dafc113eced | -16.50662 | -55.12946 | 2025-09-12 06:10:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 808cbfff-9c3e-3c2e-bda3-60dabbb507b1 | -12.08428 | -47.5854 | 2025-09-12 06:10:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| b19ba557-179e-3b21-94d4-78ed368d2c56 | -11.53065 | -50.57991 | 2025-09-12 06:10:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| a7fc1b2d-1911-39d0-89cf-7f14e1f5d3f2 | -10.84821 | -48.16537 | 2025-09-12 06:10:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 18c2a00f-4e6d-3b49-a6a3-3ce4c990fe22 | -11.68256 | -46.57916 | 2025-09-12 06:10:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 01117e6e-09e6-37c9-af79-ad6eb7d1b30f | -10.5353 | -51.52941 | 2025-09-12 06:10:00 | AQUA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| f8988c7e-036c-3a02-903e-c988493dcdf9 | -14.49612 | -53.91581 | 2025-09-12 06:10:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| ff289d9d-7b98-3a40-b412-2935e180f63e | -11.94827 | -51.16853 | 2025-09-12 06:10:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 3bd9b6db-d191-3cbd-b527-7e3d1df79bc7 | -15.10206 | -48.0157 | 2025-09-12 06:10:00 | AQUA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fd22e6ce-8302-3d60-ad8a-4dc013f62cca | -17.83219 | -52.05072 | 2025-09-12 06:10:00 | AQUA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9e314c12-b3f8-344f-a15f-e870e8dde00b | -9.51492 | -54.64057 | 2025-09-12 06:10:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 085e15e4-7ed2-3c92-b945-3d44f9f8b5a6 | -15.11481 | -48.6097 | 2025-09-12 06:10:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 465e3f6a-a9da-307c-9cc0-1726e45b6478 | -9.51723 | -54.62638 | 2025-09-12 06:10:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 84deb787-c721-3c03-8227-bb4a70a68408 | -15.78967 | -52.23221 | 2025-09-12 06:10:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 61b03d73-5d6f-3a2d-9851-fa9ac2b9496a | -11.64103 | -50.57598 | 2025-09-12 06:10:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 64f78a39-0720-341b-9f86-f4276f920906 | -12.92015 | -54.74193 | 2025-09-12 06:10:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 25.6 |
| a6195b95-1b94-3560-9b68-21bd96528e07 | -11.69127 | -46.59399 | 2025-09-12 06:10:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| f1e8bfdd-2201-3ff0-a2af-ea5759cfba12 | -15.10842 | -52.45649 | 2025-09-12 06:10:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 751185a7-16a4-31b9-a653-c1b0a22a123c | -10.33366 | -48.80464 | 2025-09-12 06:10:00 | AQUA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ff16fa85-db76-3ebe-adcf-fe426fe5d411 | -11.53096 | -50.39759 | 2025-09-12 06:10:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 31e68b70-c1c0-36eb-8be9-43785fb3645d | -13.8944 | -48.25885 | 2025-09-12 06:10:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |
| efcd3494-4a70-3627-a524-7d3ac6c9441d | -11.97329 | -51.14143 | 2025-09-12 06:10:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 33e36f0e-4ef5-3f29-b392-9fb8df4b2568 | -13.21902 | -51.75469 | 2025-09-12 06:10:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1ec5d19d-7e03-3c8b-a4c2-8fb0aa5937d2 | -12.82041 | -47.96547 | 2025-09-12 06:10:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 307f40ed-1a76-33e4-b01b-710d27d0325e | -10.07835 | -47.15634 | 2025-09-12 06:10:00 | AQUA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 9bba9c03-55a7-33cc-b13c-3c0a65af589d | -15.53126 | -48.54557 | 2025-09-12 06:10:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 8184a744-b939-30a0-b409-a9826598e8f9 | -11.10494 | -51.97485 | 2025-09-12 06:10:00 | AQUA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 07aa2f72-7a38-314d-8300-d7d4b073683c | -16.43746 | -49.02816 | 2025-09-12 06:10:00 | AQUA_M-M | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ac68d91d-730f-34dc-a639-15118074ba3b | -11.70068 | -48.27893 | 2025-09-12 06:10:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 927db558-821e-3882-8415-3c81eeb136c0 | -11.63969 | -50.5849 | 2025-09-12 06:10:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3f6661e0-843c-3bd5-b653-fbe5995aad7e | -10.56016 | -51.48658 | 2025-09-12 06:10:00 | AQUA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 961c9e6e-2ae0-31b7-a7a1-e4cb9f82188b | -15.00574 | -50.11278 | 2025-09-12 06:10:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| b31be503-1d86-3a8a-9c10-6fad4ce9f9c8 | -17.20421 | -50.14569 | 2025-09-12 06:10:00 | AQUA_M-M | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f592db5a-f523-3fea-a559-86fc2e109417 | -11.18831 | -55.08218 | 2025-09-12 06:10:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| af31e216-f93d-3601-b317-f5d4be0ca063 | -11.97193 | -51.15039 | 2025-09-12 06:10:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ba420bf6-9025-34c9-ae28-9e43628e89a2 | -11.9692 | -51.16831 | 2025-09-12 06:10:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4f96cc35-6ed5-3007-92ed-815a7f968b92 | -13.19248 | -51.75053 | 2025-09-12 06:10:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 7ae5ca9c-269e-321a-b199-01f9b6a719ba | -10.65058 | -48.65372 | 2025-09-12 06:10:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8d4986f9-5a08-36ea-80ed-c79153ac37ca | -15.79107 | -52.22311 | 2025-09-12 06:10:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| ff0d72bf-5786-32bb-9f6b-383fd1ae2a94 | -11.96039 | -51.16695 | 2025-09-12 06:10:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| da9c6c79-78ae-3964-a87f-6cb610b8507e | -9.95616 | -51.68609 | 2025-09-12 06:10:00 | AQUA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| dad30e8d-3d79-3518-b146-dbe78cbe1fc6 | -14.92588 | -50.09436 | 2025-09-12 06:10:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 31aefab1-a064-33d6-ad16-279bc578a57e | -15.91937 | -51.79531 | 2025-09-12 06:10:00 | AQUA_M-M | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 02e8b2cd-a4a8-36b1-95d2-3b43bee2200d | -15.10367 | -48.0035 | 2025-09-12 06:10:00 | AQUA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 47617c5f-5fc1-39e5-9b84-a585e8a3b684 | -15.15293 | -52.46362 | 2025-09-12 06:10:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f699357f-97df-3fec-8c19-fd51bd08844a | -13.27181 | -51.71395 | 2025-09-12 06:10:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 21b07f80-bd6b-3c45-9211-136604015de9 | -11.14319 | -45.23626 | 2025-09-12 06:10:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 76d5efaf-6eeb-3545-8092-682998edf1d5 | -15.21826 | -49.66695 | 2025-09-12 06:10:00 | AQUA_M-M | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 887f1f8e-dbdd-38fe-98a3-9832a9dd6188 | -11.69919 | -48.28934 | 2025-09-12 06:10:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| cf7561e7-ce49-365b-b6f4-3b34da609d12 | -10.43617 | -50.6031 | 2025-09-12 06:10:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 24240003-3ac8-3f56-81c8-4508aac18aab | -9.9968 | -51.72129 | 2025-09-12 06:10:00 | AQUA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |


[Clique aqui para ver as próximas entradas](README118.md)
