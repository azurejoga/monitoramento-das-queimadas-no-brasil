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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7992dbe-b290-3999-9c9f-353afe40d704 | -10.54122 | -43.64604 | 2025-10-03 04:12:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41e88259-9a21-3d9b-8c0d-73888bc76add | -14.46269 | -48.40076 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4e3e7e0-4dac-3b53-b61f-053b2811d348 | -14.22098 | -46.0899 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14d394c0-84db-34dc-a604-d23347392f06 | -13.24382 | -47.34972 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2f31b992-d431-3ce0-a9f4-03b778b0a8ef | -14.45336 | -46.34195 | 2025-10-03 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 006fbc1f-e94b-3b5f-ac52-cc14650a0c77 | -11.42297 | -43.48857 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04fd9d0a-71d7-3a71-9666-83d227033910 | -12.37599 | -46.51895 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9760d555-ae7c-3c2f-86dc-7c228e0bf660 | -11.11315 | -47.85515 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24ede6fc-97ba-3b1e-8365-f0fb7b7e467e | -14.29462 | -45.9776 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e770b65-10e3-3093-806b-ad8583e803bb | -11.50468 | -43.50563 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c273c40-4660-328f-8198-0ab7413e0c92 | -12.37369 | -46.53248 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca8c3892-e4f3-3075-87a2-3479021237d8 | -11.62417 | -45.03548 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 56ad139c-c303-34ca-a30e-23a8f275edb4 | -12.9386 | -48.44387 | 2025-10-03 04:12:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 344eb0f8-b4da-3b3d-beed-4bccbcc927e2 | -12.79877 | -46.87539 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ff99f60-e78c-30c3-b83d-4153e51d59be | -12.42394 | -45.15892 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afabe776-64e7-3ebf-8f7f-1aa9d505358e | -13.23078 | -47.35675 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 65a8d31b-c393-344b-bc75-7d6c069d3dd3 | -13.97457 | -48.12487 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a364e539-3222-370d-bcc7-8c64dd04c162 | -10.86055 | -45.4197 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e445b19-9b73-37d3-bad1-281ed900947c | -14.43664 | -46.11811 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09e9b6ec-28fd-3ce3-8b81-9c1871dc5112 | -10.9193 | -47.04321 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 42583229-ed63-3d8e-a40a-308c1143e58d | -10.01608 | -50.23076 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c350624-404d-3082-a836-fe041675ee32 | -9.90372 | -43.71703 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e6b813ec-f710-30ce-bac0-ffb1187b926f | -8.54109 | -50.15368 | 2025-10-03 04:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8a12c6d1-3ac9-338d-815c-3f2a93d4e0cd | -8.82898 | -46.77208 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74df7010-af70-3317-903e-9dedf01dd412 | -11.78203 | -46.82602 | 2025-10-03 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c09f430-10cc-38a9-84f9-5f76e35b72c3 | -12.61204 | -46.97036 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 63f7decf-ed34-399a-900e-b50cd89c81c0 | -14.11664 | -45.66161 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3e41412-6536-350b-9632-997fec76203a | -9.94744 | -48.77993 | 2025-10-03 04:12:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 332b9d71-f9cb-32ab-bfd5-11374fee3907 | -12.79774 | -47.01484 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b1c9edb8-cac0-3087-a144-dddb4dbd6a21 | -12.6234 | -46.97215 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4013904-2d8e-3893-b6a1-14210f63b82e | -12.93739 | -46.37923 | 2025-10-03 04:12:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33c15907-4929-3d63-a018-7e493854510a | -9.91607 | -43.72653 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| de9a74ea-2da6-3597-b2bc-11189c7d55a6 | -14.19508 | -46.07769 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0e329b00-0222-3020-9974-3cb4d2333cb2 | -14.20784 | -46.08862 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a64f4992-ce2a-3643-b7a0-8ec76cf67bdf | -9.88106 | -47.81263 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f984bce7-3ab5-3835-aa74-0970c7babfe0 | -10.29676 | -47.93533 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2898b774-fb5a-3d60-b758-7409c37916de | -13.83269 | -44.2037 | 2025-10-03 04:12:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b89bdca-a84a-3afa-a9d3-003bfe7254c2 | -13.33718 | -47.20929 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e2c019f4-f00e-3a56-a399-9eae54b7c4d2 | -13.15246 | -47.89594 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2efa77ad-1770-398d-87d4-4c124fa1c61d | -12.9323 | -48.43146 | 2025-10-03 04:12:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52a1aa25-4f54-3492-9f81-c99b80cbf1c7 | -11.13954 | -43.40227 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 762acd1f-9066-3454-a0b7-0fc1d85827f7 | -13.23078 | -46.43474 | 2025-10-03 04:12:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff416a8b-4c93-3899-b5b4-5c58c31a2bf9 | -13.34012 | -47.21486 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1c74dc6b-2571-38fa-a1c3-cab27ade1d5a | -11.61736 | -48.50197 | 2025-10-03 04:12:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ca3f7d9-4818-3646-918b-d520d3c9768f | -13.68686 | -48.63075 | 2025-10-03 04:12:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d9f36431-21d9-3b23-86c9-b6754891af56 | -13.86451 | -47.93747 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c356458f-2389-3cd4-b967-4baf3b0e83fd | -9.94863 | -43.72462 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cfc36c52-49dd-3c39-b3f8-73e7a1aedd94 | -14.68978 | -45.1806 | 2025-10-03 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c052b00-b5e6-3034-9beb-07c1724daa88 | -11.80926 | -45.01026 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc4b077d-ca20-39b3-97d6-591378208a30 | -10.92016 | -47.03831 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 74df68e0-e544-3b79-b52f-3dd914f0c9ef | -14.60261 | -48.23747 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9243b946-c5f9-35f7-a130-9328d39b61f8 | -13.08653 | -47.06892 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfe81664-7668-3f4a-81b7-fe934f6f93c2 | -10.162 | -45.49144 | 2025-10-03 04:12:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| afeecf7c-c909-3a82-9c9e-2ae7609baef9 | -9.06487 | -46.65378 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b22deac1-e93b-3f23-a655-25f7a6e219ee | -13.77117 | -47.57819 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0f08af52-d346-3697-a83f-cdca0a3e304d | -14.21609 | -44.78998 | 2025-10-03 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 917c9b33-c32b-3a15-a063-6600b591e2b4 | -12.61712 | -46.98616 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 8b638579-8ebf-329f-8d94-07786b072252 | -8.81476 | -46.66667 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fc9afc2b-af49-3850-bf8d-19659793025f | -13.19373 | -47.8243 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74e121e0-7173-39ec-ba84-fd2f15af3745 | -12.86074 | -47.00898 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39ea978e-f31c-3557-904a-b64eaf8973a1 | -11.90585 | -46.29724 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8853b520-2fe6-3a0f-8ecd-32fd0a61b43c | -13.96368 | -48.10433 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c96ebf96-51eb-32b2-9f01-afde61ea8cf7 | -9.16448 | -50.8446 | 2025-10-03 04:12:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e451984e-7615-3a4e-b04b-b16bd398c52f | -13.26814 | -47.24629 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 45f28f48-1475-30e9-b6c4-5c7885666ea4 | -13.73967 | -48.0072 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 71be3595-ca7f-334f-ad6e-5cbd1568b22f | -14.42197 | -46.35331 | 2025-10-03 04:12:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69f4f9a8-9278-3223-8eb2-75206aeb728e | -11.4986 | -45.01119 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7687836b-027d-3087-ac26-f37e50093a42 | -8.72158 | -47.13347 | 2025-10-03 04:12:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26badd02-7c38-30e2-a288-0eeda073e1e4 | -11.92024 | -46.27259 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 687dacc9-579b-3059-be0a-c029d4e7ec22 | -13.12405 | -47.85763 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 414f3192-3eef-357e-a6fd-6ff47575c2ef | -13.05483 | -47.0512 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1406c6a6-fa5f-3e77-af3c-dc8e36aee4e3 | -13.20821 | -47.88041 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9bef222-707d-3a0b-b3d8-497fef033bc5 | -13.15009 | -47.8185 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8ee493ec-4d15-3e47-b268-ec85a1a6b7b5 | -11.47593 | -44.97554 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b83ce51e-990d-3407-b1f4-f031c3ce6fb8 | -11.61083 | -45.02961 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa1e895a-32ad-376b-a33b-13002832335d | -13.26925 | -47.26223 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aef48e4b-2f95-33f6-a5f6-b4691c68c9a1 | -11.5892 | -47.63698 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bee0eb57-bd5a-3bd9-8aa4-517d238f4747 | -12.8099 | -47.01202 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6e76a65-25a8-3460-b18b-de0d85a938ac | -11.47641 | -45.01537 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1d2a661-f6dc-3925-87af-d6da9d71383f | -11.83201 | -45.0022 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c03d7e0a-6f48-3afd-8877-2aa8cce4ef16 | -11.4932 | -43.50019 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e661049-0c62-35a5-8396-175508a63f5e | -11.84005 | -45.03977 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29bebe2d-f533-3c06-85c3-971728b77edd | -11.85924 | -44.967 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff36d992-f8b5-379c-9f68-44f16c49a122 | -13.58742 | -48.18732 | 2025-10-03 04:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 37498e63-e176-335c-ad05-5bf9e516f022 | -13.2052 | -47.87437 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f677457e-256c-3428-bc94-0f22c9f9d90c | -9.93606 | -43.5811 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6438894-5789-329c-8468-15dee51a6dbb | -14.19206 | -46.66933 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a199abb3-732b-3070-aa52-6a9645b4850f | -14.70172 | -43.88763 | 2025-10-03 04:12:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 00e46955-b791-35c2-8f54-c8564923d270 | -11.8954 | -42.82114 | 2025-10-03 04:12:00 | NPP-375D | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 005e9a8b-19d3-324b-8afa-21b3bf7a3491 | -9.94079 | -43.7456 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 655a219c-a810-34fd-b337-d0482c0c794a | -12.80632 | -46.85416 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 860fda85-05b5-3884-ade7-0f41a476ddbf | -13.32654 | -47.20313 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dda3b8ea-2db2-3267-b115-4c2e9c8f43ec | -11.09015 | -47.86626 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 14156852-26ca-3272-9519-7d0828bed12b | -13.05107 | -47.05045 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 495d6e84-1c59-3876-99f8-3a504b84b5bf | -12.41572 | -45.16535 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 609cbe5d-fc82-3d82-8737-258be035c7b8 | -9.16498 | -50.84194 | 2025-10-03 04:12:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a9bd654-0b16-3565-a182-5154151a3a9b | -11.90838 | -46.31937 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 28878815-c3ad-3c74-9871-1cc21752835e | -15.17341 | -43.62386 | 2025-10-03 04:12:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8b981cd4-c1f9-3459-94ae-e1f5036cae2c | -12.93498 | -48.42828 | 2025-10-03 04:12:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fab548ef-383d-375c-b22a-630c6b1c012d | -13.13152 | -47.83814 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README64.md)
