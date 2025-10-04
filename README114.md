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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0eb250de-5331-331f-962c-6a3890ccd7f8 | -11.91448 | -46.35574 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab928b15-286f-3a9e-a8b2-f3da966d512a | -10.5957 | -54.3511 | 2025-10-04 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 35391908-99e8-3b50-8f25-dabc55c59088 | -15.74124 | -46.26344 | 2025-10-04 05:06:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1fe91567-3b42-3a66-b9e6-2ad8620055a8 | -16.3575 | -49.39914 | 2025-10-04 05:06:00 | NOAA-21 | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2fbdeead-ee7a-3033-aa65-8ea22ef1dfee | -14.74827 | -54.64365 | 2025-10-04 05:06:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46e8ccf7-ae85-36ca-9025-a78f6daf707a | -11.43295 | -55.0598 | 2025-10-04 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25633fdb-3571-3c3a-8640-e0049eb5c6b5 | -11.80305 | -48.91636 | 2025-10-04 05:06:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a598fd4-7a65-3ce0-b369-69a5e78afba1 | -9.18951 | -59.55276 | 2025-10-04 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a25f30a-a8a7-38a6-aa7a-5e67f44c4a53 | -13.67333 | -47.87384 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aacce457-b93f-36cc-84cd-1efcd0fcf74b | -13.27777 | -47.22218 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 059802b9-6313-3cb9-835d-60b7e8dec9b4 | -13.13301 | -47.93712 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb6fa26e-2e1c-3d30-ab9c-c7ccd712672b | -11.79267 | -46.83509 | 2025-10-04 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4456759c-b9ae-3f64-9765-211fb59aba9b | -15.35645 | -47.95385 | 2025-10-04 05:06:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c4a1610c-e59b-32d0-ac6d-78ef597b452d | -10.90145 | -56.19203 | 2025-10-04 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8e6ebda-461e-33d6-9336-3f96c2506681 | -11.93218 | -46.35737 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2d6499c6-e0e0-3c7a-9bfa-f66cf1471709 | -13.56544 | -47.2971 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e10ead54-84e9-36c0-83a7-76b6a9513775 | -14.93508 | -46.85617 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 261e7221-690a-388c-a508-0b77a63e1f6d | -12.59146 | -49.88596 | 2025-10-04 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bee93cff-2a20-3aad-a391-05d759a24e2f | -14.33012 | -45.85907 | 2025-10-04 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ddb6246-48dd-35f2-b1ff-b9ba73039b56 | -11.93107 | -46.35798 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 70763655-f175-3db6-9a93-73de22463c84 | -13.1916 | -50.87267 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e6f1267-8935-3d12-b8fa-57cce5c6c5e7 | -15.35306 | -46.29523 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9a48240b-fd49-3c58-b6b3-8e1ba794ece6 | -10.21153 | -58.25612 | 2025-10-04 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92252452-a748-39ad-a5c3-15be45dcd323 | -13.99339 | -48.20333 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 03c2f57d-4aaf-335a-907e-e8086caadc75 | -12.93904 | -50.98312 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 15e915ba-b068-37a4-aafb-d108ae4a05df | -13.11831 | -47.9455 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 066bace5-fc68-3191-b2b9-6e2b890c5bdd | -14.57587 | -52.47699 | 2025-10-04 05:06:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| daef1def-9651-3821-8cc7-03235278b948 | -12.9434 | -50.98373 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3f996d5-190e-363b-a926-1f5fdb6c79a0 | -9.43608 | -61.9047 | 2025-10-04 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61f7a28a-478b-34aa-bdd5-ddfa3fd471da | -9.62986 | -62.40976 | 2025-10-04 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c418a74f-4af6-311a-bec2-4b0d0a848401 | -11.95873 | -51.47237 | 2025-10-04 05:06:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4487e8d4-6043-3790-ab76-84833fa053b6 | -15.24948 | -56.76925 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ed33a71-5c50-3b19-bf91-7edf51607390 | -11.28213 | -47.79741 | 2025-10-04 05:06:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6cc4222a-ca30-336e-a136-3fb1bc88b590 | -13.17512 | -50.9286 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 9c83f86a-14b5-3198-aba1-a54fa9474223 | -15.52234 | -46.82406 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11ca87db-f87c-37bb-b734-2fa9bf4acfc7 | -14.66771 | -48.28304 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb6e9ca3-c96b-3c00-8577-284f8469b4ad | -14.19497 | -46.06787 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c9732c6-b5ff-3223-b463-8b3611c0bb3f | -15.30832 | -46.30593 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ffd65d3-690d-3f1d-80a7-2a79b6a98337 | -12.95592 | -50.98989 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3535e3b7-a58f-383e-8935-734f99d5cc7d | -11.68585 | -47.49807 | 2025-10-04 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e654e6a7-3383-3091-99c8-3f725606a98d | -12.93246 | -45.07528 | 2025-10-04 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bdcd9652-41c1-3d84-a551-a040fd212ad0 | -11.91616 | -46.38432 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d730481-c5cc-363b-b026-e7b507b23993 | -13.14254 | -47.80652 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 410c462b-d957-3d83-ae14-cfdd3ed86daa | -12.3815 | -54.46386 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39cdbd76-26d5-30f3-b93b-085ff7b8c9c0 | -13.74945 | -51.30384 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee8fc89d-fd1a-3a44-95eb-5a88ddcecd1c | -10.59512 | -54.35501 | 2025-10-04 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 18a49e84-1808-3136-bdd1-5865c8967606 | -11.88267 | -44.99644 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 528c4334-f8f0-34b6-b461-e7c42b87fba7 | -11.55427 | -47.67847 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f3515243-b559-3cd0-812f-730db7c329d8 | -13.10361 | -47.88625 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 270c61a8-36b3-3c0d-8875-039bf79f6c1a | -13.10725 | -47.90147 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0bde0bfd-86c5-36cb-8b0f-53f0560f3b6e | -15.36747 | -47.95572 | 2025-10-04 05:06:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1e40e8e-ceb8-3275-8402-7a014bb93616 | -9.91323 | -56.02838 | 2025-10-04 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ba1ad10-f0cb-3a14-b981-26116ab9d9bb | -10.83681 | -57.17349 | 2025-10-04 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d927ec79-523d-3695-9c8c-ed370c6f4b28 | -13.29619 | -47.59167 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 626b93b8-68ff-3482-b3ff-408c78c7bd25 | -13.75003 | -48.06351 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| daf85e6e-3189-3de9-8bee-58de2855c514 | -14.75723 | -54.63195 | 2025-10-04 05:06:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2890636c-e9b5-35ad-b739-6a3576108608 | -10.41955 | -50.67287 | 2025-10-04 05:06:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85d24916-aca9-3ef8-9c7d-5bf3cc7a249a | -11.92516 | -46.36608 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d955c8c5-abd9-3b2c-ac5e-f1c6f62c3924 | -14.67731 | -48.27415 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1383b27-febf-3a7c-a12b-bc9b72724356 | -13.77964 | -47.81783 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 039811a6-026e-3c39-902c-9c3c8967ce2a | -13.1325 | -47.919 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9fd5863-53be-3660-846d-a18836160b9a | -15.34915 | -47.81921 | 2025-10-04 05:06:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0efc9351-6fd0-3ff5-b836-24ddc571dde0 | -12.91632 | -46.92239 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a2c74c6-16e4-385c-85c8-d4a6d8a83ed9 | -11.78831 | -46.82311 | 2025-10-04 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f84a3497-ea8e-3cd0-8fa4-ba2dc16ae1dc | -14.87127 | -48.36646 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a28e32bf-bf23-3008-aeff-34fd78eda19b | -9.63329 | -63.24174 | 2025-10-04 05:06:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40350904-a8c8-3107-a2a0-06ecf667d751 | -13.6023 | -48.17622 | 2025-10-04 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 506257e0-28d8-3cd2-bc22-7776378e00ad | -9.53007 | -59.38532 | 2025-10-04 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2300a97f-9fde-3f32-899d-6f04536e250e | -11.1165 | -47.88181 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d501979c-38d8-37f9-9ecf-c8748b1cc87c | -10.65482 | -48.47837 | 2025-10-04 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1af4c886-92e1-3f82-9868-555f689f19f0 | -13.33646 | -47.58317 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bd3af6fe-2411-3b9b-a02a-d9812aef0876 | -10.83896 | -47.20517 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1fda15d8-219e-3349-9dd3-df22ca0b4bc0 | -13.55331 | -47.25238 | 2025-10-04 05:06:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f6dd15f-cae6-32b2-a8bd-818f1f273265 | -15.31999 | -46.37636 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae8a84d0-18fe-3022-ae09-ea6613d4e5c1 | -11.74567 | -54.72449 | 2025-10-04 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63aa9634-e9c8-3b01-9341-295e383edffe | -13.93968 | -48.17053 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 20f9313b-93c5-3d0f-803b-1a7f0c63b3c1 | -11.12403 | -55.45148 | 2025-10-04 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd88dda1-93c3-30f3-8108-fdfba4b609ce | -13.3264 | -47.62091 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6e6a7c71-ff2c-3603-a542-23dcdc0ef3b3 | -13.31063 | -47.26508 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10f11717-0d2a-3dd3-a36c-9ad1ad7bc9b3 | -13.32256 | -48.11094 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3bf20b94-7731-32a5-9d4d-d373f71d8f90 | -10.56922 | -48.69806 | 2025-10-04 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6005424-6152-34a7-bb41-e34cee98e444 | -15.58992 | -52.46365 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cd3e4644-573f-3281-ade7-297825cefff5 | -13.74115 | -47.95462 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f78b4d68-462d-35de-932b-f0b2557e4da1 | -10.61075 | -49.15219 | 2025-10-04 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 783598e1-0c0e-395a-94e2-174463d9acfe | -15.73587 | -46.26273 | 2025-10-04 05:06:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0ee8de6-fea0-3c98-a6b1-9c4380c3720f | -14.66609 | -48.29689 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 99ebfec4-0f35-3334-87fd-5bfbe0f03eeb | -11.62134 | -49.83679 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa948b41-8f8e-3548-b842-19eff2c15228 | -11.84429 | -44.93523 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f88f02cd-87af-331a-8aeb-039b3c0bfea9 | -13.99912 | -48.20073 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 218313fb-8a1c-37c6-9f54-cea453feacbc | -9.63775 | -63.24249 | 2025-10-04 05:06:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3119d60a-de4c-346e-be37-1b14eee69014 | -11.8625 | -44.96337 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4cbf44a6-487f-3528-a55d-85f6ad25bdff | -11.39482 | -55.16948 | 2025-10-04 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1badc10c-f6ad-3274-8961-61d83c229fb2 | -13.31618 | -47.61252 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 87084410-2318-3b32-b3d8-e4cb20144f59 | -13.10269 | -47.89388 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eebefbb7-f82a-3fff-a281-ccf732a82b4a | -13.21341 | -47.81395 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1cd93274-aebc-3f37-a5db-da30dafb6c9b | -11.11976 | -47.89874 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6d8a2e9-7ba9-3af3-a351-dd2cced9b245 | -14.89492 | -48.3504 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8acdc480-f07c-31e0-9f48-c5b09670ed03 | -14.94787 | -46.86612 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8d67fa15-ecf7-3cb2-9f9b-3b9049324fcb | -13.13614 | -47.93389 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50d73a11-10f3-3316-bb56-15ebb3408b5b | -11.05912 | -47.78417 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README115.md)
