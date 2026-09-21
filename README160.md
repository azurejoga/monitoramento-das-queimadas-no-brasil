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

## Dados Diários - Página 160

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0c110d2-e89d-32e6-a594-a13114a59fe5 | -11.83119 | -50.02614 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f45b0dce-830e-39f8-adc4-d5916e7d322f | -9.5409 | -46.51577 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 47897103-5bd8-3c78-88f4-d4bf88e7e981 | -14.2278 | -44.63362 | 2026-09-21 16:01:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8aa91bf7-b9d4-302a-9e05-cae3b6fddea4 | -11.37176 | -46.77061 | 2026-09-21 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 1ae71a3d-aa69-339a-b557-92740d804ea7 | -10.45698 | -50.27408 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0dccaaf4-f820-3caa-955f-fee1d1fbdfa5 | -10.47729 | -45.08832 | 2026-09-21 16:01:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 54.4 |
| d3cebda2-04d7-349f-ac87-ae494d92dfd1 | -8.76819 | -45.87004 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ebd79974-5e4c-3dea-8f0c-abbec8001fd9 | -7.81809 | -38.85345 | 2026-09-21 16:01:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 3b4c256e-9f77-35bf-8c80-bb00da3d3f4a | -11.79323 | -49.81558 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| b1f93646-0dbf-3ead-beff-81d11b992a26 | -11.8646 | -46.85038 | 2026-09-21 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a57eb948-ac90-3b39-b2f3-64f5ed11a85b | -11.68153 | -43.44704 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 361d3191-551d-38af-b270-c011d5a1be44 | -10.61952 | -50.59167 | 2026-09-21 16:01:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4e949b45-21cf-3963-9a7e-da5e4932068d | -9.76579 | -46.05679 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| dd284a54-0ebf-32b6-9591-a33d40f09a15 | -10.26176 | -50.28735 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 00b89664-ab6d-3b26-8ff1-14eb15d93cfe | -10.72266 | -50.7772 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 391a1eac-2b3a-3273-8000-2fdc95c1b63f | -8.75499 | -44.28264 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| df8660be-e42b-3a70-bf23-bde00667f2f9 | -14.00278 | -42.14066 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 40.2 |
| 207dca96-d1ae-352c-bcec-f3bf71962e81 | -11.51835 | -45.35756 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d60117ea-5a27-31e0-bb04-46d46f012446 | -12.05403 | -50.06915 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| daeeb423-8ffb-333a-aadd-de30de721438 | -10.26084 | -45.49773 | 2026-09-21 16:01:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| b1ec53d1-e270-386d-92cc-6ff70d045b82 | -9.17994 | -46.49764 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3da64377-9ed9-33db-a3d7-ef1e9299aad8 | -10.55888 | -46.54881 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f99f756d-05ec-3d87-a11d-e23627b291a8 | -12.06144 | -50.07713 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| a5483aac-24d5-356b-97d4-a9348ded099d | -10.114 | -48.42909 | 2026-09-21 16:01:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 2b6d2b3c-9e68-3856-8e8d-b4c4e7180eca | -9.57784 | -46.54907 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f222ad1f-af62-357a-b198-6fd61e8b87d7 | -10.69603 | -50.77609 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 88812564-5df6-3662-8f43-4f39ec5d1fac | -8.76358 | -45.87392 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0b2ef294-8f23-340b-9392-259b92daabb6 | -9.01772 | -48.16656 | 2026-09-21 16:01:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cde6fcb7-2409-3ec4-a34e-7fc51b1b88b4 | -11.96245 | -46.50425 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| de388df7-cd68-3277-9786-3b08ef41123b | -10.72191 | -50.77032 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| a131c503-7c2c-3bc3-a44c-e8aeb26fb986 | -11.67318 | -43.4527 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 9d791323-f04f-3882-8562-cc6eee8b7d39 | -9.88904 | -48.42708 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| a0e5cc74-d17b-3ccf-8fac-82392ec66cd0 | -9.82304 | -48.45445 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 8d600c84-d62d-3917-b56a-484573de8df3 | -11.67505 | -43.45652 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 2209fa2a-65a2-3415-992e-cb016d005bbd | -10.55796 | -46.55719 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d6ff8c9b-9134-3706-852e-4a76cd483fb0 | -8.70442 | -45.44416 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 08fed12a-2842-342e-9aa7-4c75e2394d48 | -14.09979 | -44.83538 | 2026-09-21 16:01:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ac9055cf-8373-356f-b43c-43c9b58b5738 | -12.43756 | -47.0757 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| a7d5e622-edbc-3834-946c-c344f3a1615c | -9.88621 | -48.40418 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 7c5af5a7-559f-3cb1-b6fe-583982396f7e | -13.43323 | -43.82385 | 2026-09-21 16:01:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 2d135663-bb24-3667-bee2-940337c8b8d1 | -12.54075 | -50.03197 | 2026-09-21 16:01:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 3c79d425-c83f-32c4-991b-a3eec2bc1d09 | -11.14429 | -42.826 | 2026-09-21 16:01:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 50.1 |
| 8a442281-d7d5-39e2-be73-9ae4d87685aa | -11.10296 | -48.29722 | 2026-09-21 16:01:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e15fed5d-7ae6-3961-bf7c-2a4939c7aad0 | -8.78429 | -44.26055 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 732dbe83-d10b-33ad-bf95-32885d744d8b | -11.3461 | -43.38346 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3487737f-72c4-3e7c-89e7-7f7ce965b190 | -8.58589 | -35.33364 | 2026-09-21 16:01:00 | NOAA-21 | GAMELEIRA | PERNAMBUCO | Brasil | 2605905 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5aab900c-97c4-3fcd-92a0-800289b23931 | -14.10424 | -44.83864 | 2026-09-21 16:01:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c4258d73-1687-3933-bba4-c910b7bbe94d | -12.28063 | -50.15425 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 627f97a8-7687-3dc9-9311-a1a4bf1d10b4 | -9.80806 | -46.09798 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3b900f4f-d825-3307-84d2-8fd5d5631cc4 | -9.24317 | -46.24594 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9ebbdc9f-7046-311a-a84a-cf6d33fbdda5 | -7.98166 | -37.48634 | 2026-09-21 16:01:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 5.6 |
| c60d291e-136f-353b-b528-80839b76b84b | -11.86411 | -46.84646 | 2026-09-21 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 25fc7d2c-be05-375a-afbb-fc853949f11a | -11.94576 | -46.50497 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 766fecfc-a2cd-33c2-84a1-c9b459032b3a | -11.51875 | -45.36078 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 90a50b5a-25d7-3cf6-ab69-df6d7c37a36f | -10.68436 | -50.67376 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 150.0 |
| edee85fc-e500-33ad-8926-3aa49f8570a8 | -9.74394 | -46.06368 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0bc91203-d595-3e61-8302-345392a242e4 | -13.90921 | -48.56825 | 2026-09-21 16:01:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| aa80ea86-622a-3b67-9d74-deaf52dd9dbf | -10.65551 | -50.65591 | 2026-09-21 16:01:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a7105064-62bc-3050-8d76-c07b7144026a | -11.42851 | -45.3709 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4a6595ec-cfe3-3d59-a805-311ecd895176 | -8.8932 | -37.0666 | 2026-09-21 16:01:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 68246731-0ac8-3585-9ae8-3cec39b3b79b | -13.29283 | -42.66953 | 2026-09-21 16:01:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 40138ca7-14f4-36ed-a21e-bb31a53d09cd | -12.27352 | -50.15641 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 577cba94-771b-3d8b-a176-ed2e60ba6a4e | -12.54168 | -45.90102 | 2026-09-21 16:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 9c90ea58-8570-33f9-af5a-7ca76c0eb375 | -12.43669 | -47.03191 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b33f353e-ebe7-31ce-aaf9-b69a4b178918 | -10.38396 | -48.90183 | 2026-09-21 16:01:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 840ad494-a18c-3c5c-8e0b-9ab6e7eed77f | -9.83631 | -48.31713 | 2026-09-21 16:01:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 53759a2d-b9f5-3d21-9705-ca753c02b121 | -8.76719 | -45.8689 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a38ae061-fd96-386f-b84d-9b90f7469cee | -10.48027 | -45.0909 | 2026-09-21 16:01:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| d14c3f00-606e-314a-bf63-d1e5c55afc6b | -9.44972 | -45.41919 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 241.1 |
| 1722a7c3-795c-3ef9-9001-ea8f5e796810 | -11.8495 | -47.61327 | 2026-09-21 16:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c8d8ea79-202e-3353-8dfd-8797eb69cf08 | -10.71177 | -50.78843 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ac287879-6394-329c-8947-6e2fb2a44435 | -10.56349 | -46.54144 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| bab0fe74-b3c3-3fb8-8c6e-4392577ad1ca | -10.95049 | -50.61377 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| ed68c5ee-298d-3c59-afca-eaa3b6424364 | -10.7765 | -46.31435 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 0108f64a-3868-36d5-a5aa-fac7fe4c8dc8 | -9.06454 | -37.29494 | 2026-09-21 16:01:00 | NOAA-21 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 441f89a1-b92c-3398-9d2d-ca9750042137 | -9.7714 | -46.0594 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4bfa3795-67fe-3a58-9930-05913f58282d | -12.33968 | -50.18333 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ea4c4415-3430-3933-a976-ea5b9a575bbe | -10.47683 | -50.26557 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 40511879-850b-326b-bd8a-d9b675231eb1 | -10.54799 | -43.91481 | 2026-09-21 16:01:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7e3d5605-7fe5-3bc7-8b23-8bf7d844c51b | -10.55931 | -46.5523 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5a6cfa27-e3f7-3485-9e1c-3600edb7a1df | -10.76033 | -46.34166 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d9add4e6-ce03-3311-a2a9-1892ba138dd7 | -9.07538 | -48.76671 | 2026-09-21 16:01:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 2615aba4-b8fd-393f-9e40-05e4c2471a10 | -12.06782 | -50.06776 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 03d33b1f-4d0b-31c9-9700-1d27cf46764f | -12.42298 | -45.04652 | 2026-09-21 16:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| eed26f0a-dff1-34cb-bdc5-96bc73b234a2 | -13.61179 | -42.55373 | 2026-09-21 16:01:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 03ec64a2-f77e-3072-9c33-f904254bf49d | -10.95187 | -50.61457 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| d5e72080-906f-3098-96fa-5cf0cfb79dd6 | -12.33272 | -50.18401 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b07eb48e-fe6b-34d2-91a5-ae306c7c4c77 | -11.94659 | -46.51207 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 4cf0ae63-7462-345d-8b0f-8338125a6ad8 | -11.87484 | -46.8587 | 2026-09-21 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 16cc93ad-2325-3ee0-a82a-98c5277fa30a | -11.43621 | -45.39104 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| fa531cac-39aa-3c3a-aaa9-36bfa2618310 | -11.13675 | -42.8026 | 2026-09-21 16:01:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| ae2e9022-1e3d-3d99-ba35-72e984f662fa | -11.39426 | -44.0831 | 2026-09-21 16:01:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 8f1a723e-9d18-3b1c-98bc-97c3af7d718a | -8.69333 | -45.45491 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 120.8 |
| cb499242-7d17-3703-b6ed-3704f64c7063 | -8.45936 | -45.0836 | 2026-09-21 16:01:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 2fee1a23-a5cb-36f7-8daf-403df01d8024 | -10.12952 | -45.93787 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ba1a7075-c8f9-3d2a-bfff-1cc6d21a117e | -9.88018 | -48.4052 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 8ede9572-6c66-3921-b9b6-e9c24440518e | -12.84534 | -44.20393 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f9c7ff63-2271-340e-b623-811cca58c13f | -11.01159 | -49.73637 | 2026-09-21 16:01:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e840d02a-6f8c-3b06-9402-d0ec00789a34 | -9.82578 | -48.3112 | 2026-09-21 16:01:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c19b4c78-5b8e-3da3-94ec-811d18d0f5aa | -12.54099 | -50.03766 | 2026-09-21 16:01:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |


[Clique aqui para ver as próximas entradas](README161.md)
