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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d803fcb-cc99-3ca7-ae94-df8856e8da09 | -11.72781 | -54.54932 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 367eac93-14bf-3d32-bfa5-d2f8c24d1d5d | -14.15547 | -52.82246 | 2026-08-28 05:12:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b162c6dd-cb8a-37d0-9641-2bc622b0837e | -11.17102 | -55.82003 | 2026-08-28 05:12:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcc6de4f-77c0-3fb8-9652-06fb8a834e5d | -13.46206 | -54.01983 | 2026-08-28 05:12:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ba49901-918d-3434-82df-66f730980b06 | -10.75827 | -54.02739 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4b8bd6d8-8202-335e-80f3-b89f4af1b550 | -8.63177 | -66.54266 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5389f59-df57-3ae1-8ce3-35b31026546b | -10.5067 | -64.50844 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| add0379f-d394-30fd-ba1b-66eede34578f | -10.76085 | -53.98564 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a6fc6cc-d2c5-3eec-96a5-40eca646f844 | -9.88383 | -60.26472 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a1c4e16-ad2a-3c77-a6bf-6bbf7059e20b | -11.27129 | -54.02187 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e74ed222-7fc6-30cc-ac23-00cee0b310b2 | -14.86949 | -52.60234 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8650e44e-16e2-3056-9cfa-57f20bde6cf2 | -14.32759 | -51.70872 | 2026-08-28 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 261fab54-14e8-394a-a9e5-54c6e9c8dff6 | -14.89263 | -56.32893 | 2026-08-28 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 16abf7c2-0465-3569-91ab-4fa961427a1f | -14.96591 | -52.59284 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0fabb14-e8e2-32a8-a0c3-1fea7608be44 | -10.75224 | -54.0433 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3baf24cd-d95b-36fd-90a3-cded611bc3b0 | -11.77357 | -47.63262 | 2026-08-28 05:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0c67553-0037-3c7a-9197-02fa117674cb | -9.86919 | -60.26218 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ca6286b-7098-31f3-8550-acfa40e0159b | -13.45838 | -54.01926 | 2026-08-28 05:12:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 961ea413-3131-3989-952a-36b923e60fe4 | -11.16312 | -51.20238 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a06b6d14-7720-3c9f-b8da-5e95ddd92711 | -10.78747 | -54.0276 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a6c457b-cb72-3c41-a517-7944c0394741 | -9.87945 | -60.26839 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 478e9076-27d2-38ed-9fa4-80dbe6e9045a | -11.20972 | -51.23629 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 2feee6f4-ea36-3fff-b480-2a0053e4d18a | -10.77982 | -50.63693 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4fdce859-12d6-3657-b8ba-14acbd390b95 | -10.8006 | -50.64864 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d51070a-bb36-3cc8-b756-ae56d751da8a | -9.8494 | -65.02235 | 2026-08-28 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d306d8a7-8b2b-39ae-bbb7-1e5fc478bc8b | -10.79621 | -50.64803 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae0e0ce8-a169-36ce-92b2-dc28a764383a | -10.75913 | -53.97264 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71ac462f-1884-3e18-934c-1b50db8b81d1 | -11.0099 | -49.65454 | 2026-08-28 05:12:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 32027d47-8018-3a63-819b-dcb22682aa41 | -14.41131 | -52.58821 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f40d06b6-25c1-3af1-a5ad-7f535ff60ec1 | -10.76271 | -53.9732 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 885ac32a-9d7a-3369-95ba-645e97d7d8a3 | -13.48085 | -57.0476 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3393d361-c1ba-3bc0-860b-69156479e480 | -10.8894 | -50.5216 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4f1bb6e7-8251-3b91-96a3-f0544657b568 | -8.99631 | -65.44762 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c9ea41ff-eec6-3d64-850a-d2565aa25ec8 | -13.41203 | -51.41556 | 2026-08-28 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 692a013e-e447-3051-a8e8-c41baa34a34d | -10.38791 | -61.23878 | 2026-08-28 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 751099de-4de3-380d-9f5e-9d8eddf6d594 | -12.42727 | -43.41985 | 2026-08-28 05:12:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 6b06190c-c742-308c-a96e-f88e02ae33de | -13.61617 | -51.84549 | 2026-08-28 05:12:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e11dd7e-b8fd-3700-a50b-0ef8744a9e7e | -9.52069 | -67.16679 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 573d1f2a-267b-396a-a518-d876d1dfaa69 | -11.227 | -53.99813 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb7bbd40-2924-34f7-b506-61a33784e145 | -11.7284 | -54.54531 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69a1eeb1-985f-30c6-b433-d93b6e6bb753 | -13.58866 | -45.78288 | 2026-08-28 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d82acc99-0b74-370a-9fcf-f32c0665e632 | -9.85153 | -65.0109 | 2026-08-28 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ae57031c-76d1-3455-bef0-6466cf8af879 | -11.2833 | -54.01522 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 60415eac-7364-30c1-a462-891c2d4d9f9e | -11.20005 | -53.99553 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57d0eb07-93cc-30ea-ae4c-8fdf2fc25aa6 | -11.28566 | -54.02411 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7173e54b-5fe8-3e2f-a708-30d4354af767 | -11.75726 | -54.52097 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abd37c1d-315f-320d-aa8c-c1ce95c7e9dd | -11.28504 | -54.02826 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28c834c1-4641-3950-8a3a-df38a640fa13 | -9.2754 | -68.78181 | 2026-08-28 05:12:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2150e548-61f1-3c73-a9ee-5004776778dc | -12.77854 | -46.44483 | 2026-08-28 05:12:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4cd0eef9-c530-321d-b983-b4482e63aecb | -12.28677 | -50.5877 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8cd7e811-ee01-3204-8b05-52e24647ad77 | -11.23052 | -54.01288 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0de85258-d072-3858-973a-3df27986875a | -11.72194 | -54.54023 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e7c16dec-4f51-3d01-a9d3-807b5e3dab1f | -9.87579 | -60.26776 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d979fde-1b6d-3ee3-93d1-819ea28f5c00 | -10.79539 | -53.99937 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d32aa59a-54d3-36e2-a7c9-b69e4c8c6be6 | -11.22646 | -53.99096 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93952825-9e3f-31f3-a911-b8bf06ac8b33 | -13.46783 | -57.04536 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dee1980b-a1d1-3bbb-83b0-fff7c4f86673 | -9.84407 | -65.02165 | 2026-08-28 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 888f5fb3-50db-3c70-aff3-6e527162f23c | -12.26544 | -50.57541 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| e68130ba-b676-30ff-b3c0-08ba5850398b | -14.86241 | -52.62358 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08492d69-5713-3ba0-bd48-8c5ee67fe4f6 | -14.88682 | -52.59747 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 772d6804-24a5-31a9-b8ef-2cfa764c0a77 | -11.20547 | -51.23568 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 222bf2da-1a73-37e4-b2f6-c46f07af785b | -14.89843 | -52.5986 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f43853d-d17e-33ee-9c6d-af9c2e83c587 | -10.78809 | -54.0235 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0303a581-d79e-3362-b693-48c8348e92ea | -11.19806 | -51.22646 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 2be14646-786a-3eb1-b301-6c1ac88253a6 | -10.77551 | -54.03421 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1fa8174-30b8-32f0-93a3-eb19215fd39a | -13.45774 | -54.02366 | 2026-08-28 05:12:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be8f0b48-156b-3348-a1a8-dabf133fda44 | -11.76719 | -47.63907 | 2026-08-28 05:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94e1e5ea-3c82-3568-af03-3dd42dcf4b26 | -10.93697 | -50.53725 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 0c7e5825-5ca1-3c92-935d-3c19c1281ed4 | -10.79646 | -54.00661 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f258147b-4d05-3ebb-910e-204e9b6be1aa | -11.20917 | -51.24029 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| ae46653b-d9ce-3d2b-9ef5-b5536ca440a5 | -11.76994 | -47.66082 | 2026-08-28 05:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 22bce725-7af8-312d-be4a-7029a6c059f6 | -14.98587 | -52.59939 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 392079e9-c116-3792-9ddb-84262fb3483e | -11.2288 | -53.99986 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a700c9ba-e491-3387-9438-5c02c2d9bcd4 | -10.77194 | -54.0337 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 718536ac-c39c-3d0a-92bd-598ada60aa12 | -10.93254 | -50.53663 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 01d1a8a1-8013-3457-ac5a-370676aa7f4f | -11.8269 | -47.21514 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 37bcc111-41cc-3646-be1c-42a4a839eeba | -10.79056 | -54.00709 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96500b23-66a2-3453-8004-aad566810679 | -12.20405 | -50.57343 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b254113f-7fdb-33ab-aded-c6e0b48f39fe | -14.154 | -52.83313 | 2026-08-28 05:12:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 84792f50-8099-3aa7-8279-b9374e239cb8 | -8.59574 | -70.20634 | 2026-08-28 05:12:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b8d58702-6d48-3768-aefa-adcbf947f055 | -11.77466 | -47.63317 | 2026-08-28 05:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1973976d-f017-3ea0-91f4-19a4e8cd5c0b | -10.4972 | -64.50677 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 1f0b0388-f2bc-3747-9d66-fd6678d00026 | -11.72488 | -54.54478 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bed24a8-2f54-36de-b581-a967c44e1c85 | -10.85024 | -50.51813 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b732ad77-8746-3c51-95ee-1848884ca5b9 | -14.97818 | -52.5946 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8cc7139-bd89-3743-9166-b47c05b7b7c8 | -10.49816 | -64.50158 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 24ae5171-3f0b-36f6-a07d-ff93b9d78dcd | -10.78041 | -50.63262 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f93e8df-b93f-38af-af15-ecad5344df4e | -14.60533 | -47.97836 | 2026-08-28 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b846375-bc48-31a9-b651-66e9299f00a7 | -14.41845 | -52.59661 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75753450-38a1-3b79-8c47-b50ddeb87397 | -12.27325 | -50.58584 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d1f9e27-0bfb-3202-9a19-4373a116c357 | -14.16815 | -52.81905 | 2026-08-28 05:12:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d280bb50-38f1-3e2c-ba2b-601ee35133ee | -11.78268 | -47.6481 | 2026-08-28 05:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b890fc41-b14b-3e8d-ae95-d1cb9878a89f | -15.62721 | -55.97319 | 2026-08-28 05:12:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ab0ceeaa-3243-3c04-a32e-e71bc7c10e75 | -8.6014 | -70.21452 | 2026-08-28 05:12:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d8d6f313-78cd-3616-97c4-b4099ca4d3e1 | -13.43573 | -53.99337 | 2026-08-28 05:12:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08e468e9-dc10-3cc3-a6b4-28e43599bfbf | -11.28145 | -54.02772 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 90b9c32b-53f5-36e4-99e6-db7a4708832b | -14.87317 | -52.63609 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ac4d5dc-1cbf-3152-9d38-b3a60c779021 | -11.65721 | -46.73526 | 2026-08-28 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56724aa3-7c04-3b7f-b8bd-5c520dde0c6b | -13.60747 | -45.78575 | 2026-08-28 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a944e83-770f-36dd-b4a0-648cea2288a7 | -13.83873 | -54.04095 | 2026-08-28 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README56.md)
