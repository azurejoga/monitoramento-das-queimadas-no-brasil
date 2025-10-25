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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf29ad38-07e4-3180-ba60-260a3f7186e9 | -10.96112 | -50.29092 | 2025-10-25 04:00:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64844f45-c647-33b5-9459-7639915efa00 | -10.84614 | -47.91572 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 528e4045-dda8-3547-b06e-46709c899fc6 | -9.99681 | -47.59851 | 2025-10-25 04:00:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8af3441-7b33-3437-9c92-95142e1c5785 | -10.40887 | -44.74315 | 2025-10-25 04:00:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bda11784-79e1-3e9e-8842-67622240d849 | -10.64561 | -48.06188 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b18f88f0-8c96-31a8-8267-a5d6c3c76551 | -13.65351 | -48.1895 | 2025-10-25 04:00:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de6403f9-6fa9-3479-8a3a-9ce0c351326d | -10.87311 | -48.05456 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b369d7b-45ec-33a0-9f5d-897bc0f85240 | -9.23614 | -45.58324 | 2025-10-25 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 972fc367-6df8-3355-a172-249b2bb3a16a | -14.15856 | -44.31674 | 2025-10-25 04:00:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c7dfcec5-fe93-3004-83dc-f9a9eff52685 | -14.19954 | -47.30135 | 2025-10-25 04:00:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bd2b4f2-f4c0-3928-a75a-8bfe60c4c14a | -10.63796 | -45.23758 | 2025-10-25 04:00:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42993f66-0e5a-36ec-9cd8-816d5ceea633 | -14.86843 | -48.10609 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| e9629fa1-c207-35f0-b2e7-0e13bb888474 | -12.05597 | -46.40532 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3b7ce948-c6e4-3f17-8aa4-7cc1624c13d0 | -13.00432 | -48.5465 | 2025-10-25 04:00:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6caefbf-3f25-3edf-b2eb-f78463b67492 | -14.93649 | -48.1339 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0d7478f8-12d6-3b24-8849-d2732ceb7212 | -14.86211 | -48.08715 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2c98ba50-7118-37ab-8ad1-41bda89b76bf | -10.41989 | -44.49411 | 2025-10-25 04:00:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89579b3e-4f25-3644-a1a6-67881b34d65d | -14.80039 | -42.81319 | 2025-10-25 04:00:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 428bf74f-a219-3357-8e9b-d442217c0220 | -14.46866 | -47.90526 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b5ba993-2ebc-3235-b9b7-a5b55e5fcc7a | -9.24957 | -45.58517 | 2025-10-25 04:00:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75825489-8ecb-3388-b255-d0ee96b3359f | -14.17285 | -47.3169 | 2025-10-25 04:00:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44538847-442b-303d-b16c-3b46103da8ae | -13.04171 | -47.20434 | 2025-10-25 04:00:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5045fbc4-4301-3c72-8aeb-658eb0a4a51a | -12.298 | -47.45138 | 2025-10-25 04:00:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ed008b1-2f1e-3911-ad3c-e3c06befd19a | -9.08611 | -47.81422 | 2025-10-25 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 489601ea-6944-3257-a091-5b6a07b8a09d | -10.7134 | -44.74971 | 2025-10-25 04:00:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e711051-df7b-396c-8f9f-08cb2464d3fd | -14.46802 | -47.90779 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 808cfcc9-eda3-3de2-bbd3-2ced94f55a46 | -10.70928 | -44.74903 | 2025-10-25 04:00:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54c1cab3-e90a-385a-8d82-9fe0bd848322 | -13.06441 | -43.84339 | 2025-10-25 04:00:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28e69845-b756-3bad-a734-5dbf49ad4744 | -12.04653 | -46.40629 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0b50753-f6a4-37f6-9996-f69055dc7d1d | -12.24925 | -47.44709 | 2025-10-25 04:00:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b168678c-85cc-3821-a3a1-9ad96f0526f5 | -13.29167 | -47.49733 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ab371c4-4a88-347e-aa9a-d44893c3272b | -12.22752 | -43.30734 | 2025-10-25 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56d00994-b3d7-3185-b7ef-1f0073fcf88b | -9.64752 | -47.75451 | 2025-10-25 04:00:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3a7d0a76-1301-3174-86e9-b3ccd5f32f0d | -10.95524 | -50.28971 | 2025-10-25 04:00:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a7ac9b6-f82f-3928-89b6-b4e649aa0c83 | -10.26855 | -43.97081 | 2025-10-25 04:00:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0146b7cb-9e2a-3427-97bc-d18124c7221c | -12.05459 | -46.40244 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ffd0761-e361-3d6b-be7a-c460409455b7 | -10.62393 | -47.92203 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b61fee93-c4ea-38fb-8722-95e4323c2a19 | -13.83566 | -48.50322 | 2025-10-25 04:00:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d8f788df-2263-3a20-b33d-ee65af84aee1 | -14.87523 | -48.09245 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd76ba34-07ff-3cc0-b24e-5d6d0e1c7159 | -11.75385 | -45.35903 | 2025-10-25 04:00:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1423444-2d00-3f03-8285-10436f392811 | -11.06026 | -49.62426 | 2025-10-25 04:00:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fa63edd9-125e-369b-9e62-2254ecf20e9c | -10.41926 | -44.49778 | 2025-10-25 04:00:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15c83ad4-7c70-3ef1-b4f4-101f93b2a0c5 | -14.38699 | -51.53547 | 2025-10-25 04:00:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b49d9c59-731b-3c84-86db-d3ace5b12ce3 | -13.90417 | -48.41595 | 2025-10-25 04:00:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| bc07a792-6f33-3ef1-8bcb-0e18b3aec123 | -11.91774 | -44.17546 | 2025-10-25 04:00:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 28a67d13-b89c-36c2-825f-99b7da1fb9d1 | -14.18395 | -47.3085 | 2025-10-25 04:00:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92793210-ada3-334d-bc6f-9452241e87ae | -9.30359 | -45.17156 | 2025-10-25 04:00:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a6f53db-9944-3df3-a06f-d87ed4539f49 | -14.76873 | -43.08688 | 2025-10-25 04:00:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 06005caa-5c91-31ca-b29b-dd68a2505a0c | -12.8322 | -48.63053 | 2025-10-25 04:00:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30fda90f-ac7b-3f88-bc8e-44994c29b738 | -14.92381 | -48.14833 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04676a0f-0bb3-3d5a-9b3e-ba976f82c693 | -11.43335 | -44.67502 | 2025-10-25 04:00:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 27a487e0-76df-32cd-b714-2195f48e641d | -12.07915 | -46.40527 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9212aa9-b19c-37eb-9268-008ecb53052c | -10.83367 | -47.62527 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b60aea91-1bda-37e5-8049-4dc85dd8f034 | -12.2598 | -47.44364 | 2025-10-25 04:00:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ae9e846-6ea6-35e8-953f-705ae401f0b9 | -12.76351 | -46.77565 | 2025-10-25 04:00:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1134a097-6db4-3762-a1db-66c9cced71ca | -14.86928 | -48.09759 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 98b2a60f-677b-30b3-959c-443f6727fb99 | -10.62392 | -42.31804 | 2025-10-25 04:00:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b9bc491f-88d5-3ada-b61c-63b92a7608aa | -12.77823 | -47.37868 | 2025-10-25 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26b85361-576b-3f3c-8501-f7ada4106e48 | -14.54424 | -47.94648 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1552436-5cbc-3b53-a5a3-c7259e59b7c8 | -10.1208 | -47.28038 | 2025-10-25 04:00:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5db90108-dd29-31b5-b921-2e880b399b56 | -14.17384 | -47.31174 | 2025-10-25 04:00:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69d2ba0c-1f4e-3001-8dfa-461e0d9b64a6 | -8.55706 | -49.86057 | 2025-10-25 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6abe19c9-c10c-37a6-bc23-4918dd1dd647 | -10.87383 | -48.05062 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77487ab0-fd89-396b-9875-fd7b4f060285 | -10.64501 | -45.23825 | 2025-10-25 04:00:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df65c193-3a5e-378f-8123-232c0bf96792 | -10.62152 | -52.19125 | 2025-10-25 04:00:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5519ba6-84dc-3929-b5b9-17b3bacf047a | -13.33573 | -47.91527 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33644c87-85a6-39ac-b6ed-803bbda83c03 | -11.1444 | -44.94078 | 2025-10-25 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b772e283-8b30-378b-90d7-96c90a877e7c | -13.33957 | -47.97468 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48b15df2-2203-389a-9ced-16e9be121174 | -12.12794 | -46.72563 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da4260db-bd0e-3911-bf5c-376ab8dbdd52 | -14.89837 | -47.86924 | 2025-10-25 04:00:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff041482-8a18-37e6-8be4-a07908ed224a | -9.49264 | -47.45512 | 2025-10-25 04:00:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52611845-092e-342b-a399-b661aaa36e88 | -12.63819 | -44.30359 | 2025-10-25 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7b4ab8a-a483-3e71-a015-02681aabd95b | -10.64076 | -45.23751 | 2025-10-25 04:00:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 56f1a729-5e2e-364c-a6fc-4fb5774e3e71 | -10.87824 | -48.03969 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1cb7a142-7fa4-3343-b65f-c1717a3a32aa | -12.21523 | -46.50525 | 2025-10-25 04:00:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93cef2c1-af50-322d-ad24-9c7f4b6e9d61 | -14.43688 | -48.06686 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f0ca5b3-fe20-3933-b8f9-e82e51bcc5e1 | -9.32324 | -45.18683 | 2025-10-25 04:00:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70d06e4e-ec09-3962-bc98-b0993a905c8b | -13.45484 | -44.06757 | 2025-10-25 04:00:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0194d90-8927-31ea-a0bf-fadb42e3b193 | -9.60937 | -44.63189 | 2025-10-25 04:00:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c709e8f3-0f6b-3c4b-a9a0-fc7ca16235fe | -14.86316 | -48.0816 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 502a031d-d32a-3985-a7f3-b5ece3351d77 | -13.41546 | -47.95788 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77ddd6f5-4183-3f63-a2cc-0f8524d96e2d | -13.34068 | -47.91567 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b8454c0-f267-3ce5-9a5b-a665541c10bd | -14.56414 | -49.84267 | 2025-10-25 04:00:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1fc5585e-c14b-3755-aac2-ee5bc19ff2e3 | -13.41437 | -47.96353 | 2025-10-25 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0c28e35-783f-3464-8771-461723cd4810 | -14.86888 | -48.07445 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3138e04e-0a83-38ef-8f42-681a30ddc98c | -10.87696 | -45.08065 | 2025-10-25 04:00:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bc99aeb-f8c3-3c86-bdf6-739f7475d474 | -13.06295 | -47.56303 | 2025-10-25 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a8459d6-9498-3377-a426-e90c965461e5 | -13.8836 | -49.05333 | 2025-10-25 04:00:00 | NPP-375D | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ed0818fa-6ded-3f94-886b-a50e4558aa8f | -14.40261 | -51.5201 | 2025-10-25 04:00:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3092aa06-ed1e-3fbb-b6ff-474406d39ddc | -14.86946 | -48.10061 | 2025-10-25 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 582d34b7-eeda-39cd-b5db-0574505f877d | -10.64493 | -48.06562 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 129b41a1-05fe-3b57-bad3-bb36d0838a33 | -10.88182 | -45.07755 | 2025-10-25 04:00:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75c80fe0-1656-3883-8897-9bc96c53a852 | -14.45983 | -47.92609 | 2025-10-25 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d11f806-fb50-3178-815a-577c9dcb08b7 | -13.0328 | -46.61608 | 2025-10-25 04:00:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d82c634d-5499-395c-a726-4b93b19d3a09 | -13.16748 | -40.69457 | 2025-10-25 04:00:00 | NPP-375D | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 85abe748-8b05-39ce-99b2-60dfddab0a24 | -10.84515 | -47.92101 | 2025-10-25 04:00:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5555f8c2-89bf-3fee-977d-ee946d508c39 | -12.69727 | -46.33427 | 2025-10-25 04:00:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23b3ccfb-3787-35f0-b1fe-58e720197cef | -11.5062 | -44.00471 | 2025-10-25 04:00:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 221ceb8d-7398-3091-a940-65bd034a6b59 | -9.86728 | -44.88908 | 2025-10-25 04:00:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82a14e59-9a91-3f87-b829-f2977b053d57 | -12.0828 | -46.41064 | 2025-10-25 04:00:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README20.md)
