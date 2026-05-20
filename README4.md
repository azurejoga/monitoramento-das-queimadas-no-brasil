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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbdd3c21-cc66-377c-9be8-9c950da19ad5 | -10.57793 | -46.65458 | 2026-05-20 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73dfc646-c203-360b-876c-e5add65a646a | -14.15772 | -45.31042 | 2026-05-20 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9747e0a0-b245-3fda-a1f9-fefa7dcb1c02 | -8.61334 | -46.00048 | 2026-05-20 04:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0c879d5f-5bb4-3a07-a1d1-0b50d6607f4b | -10.49885 | -42.40742 | 2026-05-20 04:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 165d06d3-47d0-314b-a830-28ad5afef729 | -11.0177 | -45.12842 | 2026-05-20 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 906ff034-d5a3-3246-a46e-da32842412b6 | -11.46298 | -52.9211 | 2026-05-20 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0b40952-2235-3248-be93-0f3b3e75779f | -11.44691 | -55.11164 | 2026-05-20 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47eb1973-b954-3b27-ba88-67c9eef01b34 | -11.01713 | -45.13198 | 2026-05-20 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1af1e650-ee2c-32d9-9a03-569b931fd999 | -11.92771 | -43.86568 | 2026-05-20 04:23:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1ecae03f-9aab-3b86-a144-129ba4435c8f | -11.60878 | -55.32773 | 2026-05-20 04:23:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c0920bb-1efe-35cc-9a3f-f759f668737d | -12.60271 | -44.52033 | 2026-05-20 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 16820735-2fab-3ae7-a8dc-03224e451087 | -12.22797 | -44.26003 | 2026-05-20 04:23:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6dcf7760-e1ac-3ce8-abac-2af036b7d0cf | -8.73388 | -47.98239 | 2026-05-20 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1983f33b-96f0-3c67-90ab-7bd5b7832d37 | -10.06261 | -47.97371 | 2026-05-20 04:23:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 057afd16-5307-37d2-80f6-74580a622353 | -12.88561 | -47.24305 | 2026-05-20 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 466a08c5-8490-3fad-a6ab-44db8d77ccd3 | -11.63688 | -47.88085 | 2026-05-20 04:23:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cbcef29-dd5d-3bd2-89fe-2bcd4c84f4ef | -11.10209 | -46.50032 | 2026-05-20 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b944d2b0-21b2-3ba6-a999-ebb89727fe01 | -12.25411 | -44.6086 | 2026-05-20 04:23:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c91de23-fe8d-3961-856d-cd6257f2bb37 | -12.6066 | -44.51733 | 2026-05-20 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6ce8d3c-bde9-33f1-a72b-b7c643c68742 | -10.5752 | -46.65335 | 2026-05-20 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6a946d0-d0bd-322b-b6a9-15d7248c9f50 | -11.59913 | -55.33492 | 2026-05-20 04:23:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39d9ce69-afab-3f27-aad9-96b5bd5bc6cd | -11.46857 | -52.91913 | 2026-05-20 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3f2c9e8-df9e-3a4b-b5c0-af197f7b166e | -9.0728 | -49.66298 | 2026-05-20 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49527103-3c27-36cc-9456-6d602283692d | -8.55083 | -45.9901 | 2026-05-20 04:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcd5b9e5-6280-3ed5-8848-8820a8f9fc1d | -10.48718 | -49.36622 | 2026-05-20 04:23:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b6a0e4f-bd46-325e-b6d3-a8708e53b211 | -10.497 | -42.40349 | 2026-05-20 04:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 57241c38-aa16-3cf3-a852-2671b38c02af | -10.56678 | -46.65674 | 2026-05-20 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c4db913-5051-3673-8394-5ef92ee20cbc | -11.93106 | -43.86622 | 2026-05-20 04:23:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e5048409-c6c4-3e09-b9ab-029b9bee61f4 | -10.29305 | -43.66736 | 2026-05-20 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bade1ba4-2893-314f-978a-acbe62463f22 | -8.70447 | -47.91243 | 2026-05-20 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75a2957b-dd06-33a0-bf8b-4851b2641332 | -12.05709 | -45.27031 | 2026-05-20 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b6dca80-8aee-3353-bd71-0afa88025dcb | -9.73825 | -37.24848 | 2026-05-20 04:23:00 | NPP-375D | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2e81b359-75d2-375d-a7f0-4435a9cc26d4 | -8.73006 | -47.98172 | 2026-05-20 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 18799ec0-0c1f-383a-8580-62371e5790a7 | -11.07768 | -48.25803 | 2026-05-20 04:23:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a270318c-4339-3269-8bae-c97762c45ad1 | -11.45233 | -52.9221 | 2026-05-20 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 509acf52-aba1-37e7-afb3-6a803b7d1175 | -11.59734 | -47.10433 | 2026-05-20 04:23:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 044d3d3c-8ac1-38d0-96be-17d11253f5ba | -9.9653 | -52.46901 | 2026-05-20 04:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 31fdb224-1206-348b-8113-6bef69a53ac8 | -9.96028 | -52.46803 | 2026-05-20 04:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3d792013-f523-39fc-8202-3102596d5e61 | -10.49123 | -49.36695 | 2026-05-20 04:23:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0f0c963-c0c9-329e-ad4c-f711b70d5968 | -11.61345 | -55.3245 | 2026-05-20 04:23:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a3e4bd1-c394-3f99-b91b-df9ba0acb055 | -11.60603 | -54.18941 | 2026-05-20 04:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef5d5e5c-68b4-34b5-bae5-20f6d86feeac | -11.46268 | -55.12348 | 2026-05-20 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 84f7056e-79b1-32be-9c59-a78deedde98f | -11.61173 | -55.33308 | 2026-05-20 04:23:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e9180220-7d3a-3068-9ee4-abbcfacdd840 | -11.8505 | -48.24426 | 2026-05-20 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f61bba87-711f-32eb-a562-edde45d942a6 | -11.02338 | -42.85545 | 2026-05-20 04:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 80566d37-f09b-3469-9da2-801780a34f8a | -14.15715 | -45.31399 | 2026-05-20 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae497c65-0c5f-3e8c-ada3-46aed980c750 | -11.60794 | -55.33202 | 2026-05-20 04:23:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c0e9a26-4c28-3a91-aafb-2db4392ea755 | -14.08156 | -42.11708 | 2026-05-20 04:23:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5c7c0aad-1010-34d9-8ab2-bfdeafc2a844 | -9.8871 | -52.44196 | 2026-05-20 04:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| be30af36-e34b-360f-b9b3-015a4ec0d068 | -11.9305 | -43.86978 | 2026-05-20 04:23:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 076dc89e-6389-3073-a14c-c3e7f9288600 | -10.57804 | -46.65785 | 2026-05-20 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 40df7bda-1a32-3037-9f4d-f3b3078a2a12 | -8.84443 | -49.87173 | 2026-05-20 04:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ccd04d1-029d-307d-821a-a5471be99da4 | -12.6016 | -44.52741 | 2026-05-20 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0f93ba4-1340-3a98-a7fc-3470ab7ab4e2 | -9.22128 | -46.67237 | 2026-05-20 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87123633-27a5-3658-be0a-785f85cd9ac6 | -8.32432 | -48.00523 | 2026-05-20 04:23:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9fd37dc-b965-309c-bd2e-68bee569a066 | -11.45189 | -55.11699 | 2026-05-20 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfbef63e-c826-3eaf-a734-7f69ce9cf53b | -12.59883 | -44.52332 | 2026-05-20 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c4b6e732-186a-30f6-bec0-5408702dda97 | -13.31195 | -43.02448 | 2026-05-20 04:23:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5a07bf15-2328-3b28-950c-714f3732ab66 | -9.94246 | -48.02143 | 2026-05-20 04:23:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39496bdf-5bb1-3f75-be62-35ea38204b93 | -8.70369 | -47.91709 | 2026-05-20 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf59e078-f907-3d51-92f7-3f25f92918c2 | -14.15601 | -45.32112 | 2026-05-20 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7cdaa314-172b-3100-be42-fcd7ca1408a8 | -14.16437 | -45.31154 | 2026-05-20 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a15ca3ec-ae3c-3e7e-97dc-46dd3c0be96c | -11.33342 | -47.44644 | 2026-05-20 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 609e35fe-5eb3-3c7e-bbbf-dd6bbce7812d | -11.60564 | -54.19262 | 2026-05-20 04:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e25a43f-a6a0-3610-a0d3-01596bfbd0a6 | -11.09863 | -46.49969 | 2026-05-20 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c1e95d1-faab-3cca-aa43-513224c95ec1 | -11.6138 | -55.33328 | 2026-05-20 04:23:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a00ad1ab-a7bb-3a4d-a17b-8e20191a4896 | -11.47865 | -52.92114 | 2026-05-20 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbaa2628-e34c-353a-afc0-030c33a11e08 | -10.49503 | -48.11425 | 2026-05-20 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd488eeb-40b3-3e30-8195-a28239408854 | -9.96986 | -52.41547 | 2026-05-20 04:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c52bd7df-2886-3799-89ce-b6c68817b112 | -8.61396 | -45.99664 | 2026-05-20 04:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d926f0c-2d53-325d-9ca2-cab23c691b9d | -12.06816 | -45.28679 | 2026-05-20 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c0a3a676-6b14-305e-89a6-bd23f0b61240 | -12.05317 | -45.27332 | 2026-05-20 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f91d1b30-313d-3dfe-b5f4-ce2bcbe376d8 | -10.66779 | -48.25672 | 2026-05-20 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61a82f78-6314-3a46-a304-4b1ea8a26fb0 | -13.19805 | -43.3591 | 2026-05-20 04:23:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f4d69ceb-bf47-3f16-94eb-556b42d7d702 | -9.2184 | -46.66772 | 2026-05-20 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0fabfc5-79a0-300f-9a27-7990130ad114 | -11.93727 | -46.92896 | 2026-05-20 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1000993-c861-33f7-b504-3549fd067829 | -12.06148 | -45.28567 | 2026-05-20 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f1b7793-5bbf-3b1c-a134-5356b627e3f5 | -11.6 | -55.33062 | 2026-05-20 04:23:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b1df97d-a0ae-3fe8-8a70-b6aa57116113 | -14.15829 | -45.30687 | 2026-05-20 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 509e7c7b-5ac4-333b-9804-c9090e8a5435 | -10.49581 | -48.10966 | 2026-05-20 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a47344ff-f767-37e8-a229-e5efa56fbab8 | -12.22631 | -44.24887 | 2026-05-20 04:23:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 088e4546-43ae-30b0-be51-60e0636f6bdd | -8.43252 | -46.92484 | 2026-05-20 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 474a101a-0bce-3ca4-af8d-cecfa0a117ed | -11.61259 | -55.32879 | 2026-05-20 04:23:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7945d24a-892e-3227-9663-3a99f7e092fa | -12.22686 | -44.26711 | 2026-05-20 04:23:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ace3a0aa-3a34-351e-8b22-e1753b191024 | -11.95757 | -44.19048 | 2026-05-20 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e64bf5f5-6568-3427-ba16-c98d6b2a2d40 | -9.88378 | -52.44057 | 2026-05-20 04:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 85bd30a2-31bb-34d6-bfe9-427219c4f81d | -10.49941 | -42.40368 | 2026-05-20 04:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d3cef5ab-8b1c-30b5-8fc7-feac803efb26 | -10.39977 | -49.4409 | 2026-05-20 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a5c7eec-b77a-39e1-87d4-90ab451fae0d | -11.04541 | -49.53322 | 2026-05-20 04:23:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 39417a1e-7173-3264-a35e-3d8feb66369a | -9.95947 | -52.47246 | 2026-05-20 04:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e2af8f06-af98-3f84-b0a1-c64d14ffa932 | -8.69987 | -47.91647 | 2026-05-20 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06810dee-ca06-3141-9169-8f308b0a52d1 | -12.45669 | -54.4524 | 2026-05-20 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c68d0d6a-62e8-39f8-9850-afe6f16eddb6 | -11.47397 | -47.34278 | 2026-05-20 04:23:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d59dc73f-488a-3b5b-9407-d1742e948a70 | -10.5787 | -46.65394 | 2026-05-20 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 734cfe39-1c53-3d1b-8733-f095439fb630 | -8.5543 | -45.99065 | 2026-05-20 04:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6364820b-c478-369b-ae6b-86b83c5bee4b | -13.19861 | -43.35539 | 2026-05-20 04:23:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a4e4cad4-bcc7-3e2d-bcfe-94d0a8319db3 | -12.22464 | -44.25949 | 2026-05-20 04:23:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27c18807-4cb7-3bb3-a956-d6fc03eca33a | -10.3815 | -45.13078 | 2026-05-20 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87d29985-8b18-364e-bdb1-15f93784187a | -11.76156 | -48.28635 | 2026-05-20 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0495ab5-d6e4-3c82-ba93-9a7d3b86f6b1 | -13.2948 | -39.34999 | 2026-05-20 04:23:00 | NPP-375D | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README5.md)
