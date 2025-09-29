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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5f4488c-4931-370f-91be-8ddf9196e0f2 | -11.99688 | -47.11458 | 2025-09-29 04:59:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 131b017d-ee2d-3741-b4a1-7d0a441f8591 | -14.5795 | -48.26741 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 86165b5f-f918-32af-b855-44f682eaa838 | -14.5794 | -48.22736 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3ad8b46-1726-30f0-8970-2c5856dfb369 | -12.87469 | -46.78563 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c5e24b2-01b8-3552-ae9e-5f899fadf634 | -13.8321 | -47.49045 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2854a233-1331-3547-a7c4-bdaddd26cff9 | -15.55315 | -47.87789 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3a8b8e3c-0164-3d08-80db-938891a6f26d | -13.25157 | -48.44487 | 2025-09-29 04:59:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d10d946a-9b9c-307e-b9af-2f242effce11 | -11.93778 | -48.02497 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2c444200-40ea-39e0-b6f9-5c53c4cdc4e7 | -13.6196 | -47.34964 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 68937506-b116-30a9-8ec0-714920dfbc90 | -12.6531 | -46.93126 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3ba517fb-5eed-3599-82e8-39ec87fb8744 | -12.35352 | -54.1503 | 2025-09-29 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ff38ed0-e67c-3aeb-9a3e-ade8670a729f | -14.53999 | -48.43291 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5458b3a6-2227-328a-860d-112f163560d5 | -12.97569 | -46.24879 | 2025-09-29 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34477e3d-d830-3942-ba8f-72fff5bc04f0 | -12.76865 | -46.86399 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34e56206-9eac-322b-aecc-c1dc5aa62a08 | -14.54539 | -48.42847 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9a7a4140-e680-35b0-8aba-093795fd01cd | -13.82883 | -47.4751 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a56ed7c8-ff4b-3a9c-b457-e6c0a4aaa406 | -15.28894 | -49.51981 | 2025-09-29 04:59:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 696e6543-835c-3ec4-a5ed-1ca3a1b00305 | -13.75081 | -47.9112 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 97a77821-7321-3102-9ecf-b209c12652fe | -14.54957 | -48.43402 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b8fff377-03c6-3a45-a61f-fcf9d1f9c074 | -13.80077 | -47.94999 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1d0e918d-ab64-3200-aa52-67fb1570e570 | -15.50403 | -45.87817 | 2025-09-29 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e64fce44-d513-327d-bb9e-4b0c1cdb79d6 | -13.61106 | -48.05873 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c5f18820-9a7b-3f99-8f84-94b3f18d5a8e | -11.99014 | -46.5913 | 2025-09-29 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2d0ba56-03f1-3411-aa43-bf67b250d6d0 | -13.63279 | -48.04219 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c39c4a2e-4830-31fc-9e43-0c225cb79250 | -17.0885 | -48.56591 | 2025-09-29 04:59:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 65b5ba5c-7989-3da7-8517-41b0c96e693f | -15.61397 | -46.24628 | 2025-09-29 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3cf0ab5-499c-35c9-a817-4a8f509effeb | -15.60999 | -46.24805 | 2025-09-29 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90a3362f-7b65-3ded-89e1-b04aaf9388e3 | -15.91616 | -46.20768 | 2025-09-29 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57bc6bad-f4a8-3606-a29c-42530adee1b7 | -15.03068 | -46.97303 | 2025-09-29 04:59:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa8eff66-db21-309d-81f9-fc62561d10b1 | -15.27044 | -48.75951 | 2025-09-29 04:59:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| acb39891-fe59-31c1-bc99-8b0d9241798a | -15.18785 | -48.47301 | 2025-09-29 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| eb9a636e-6a42-3e71-b686-d1be5ae5caac | -15.27743 | -46.41405 | 2025-09-29 04:59:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c7edb4e-a827-3990-a78e-1748f118163e | -13.81251 | -48.01439 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8366b23d-e375-37d0-8270-bd2e3942b205 | -13.83747 | -47.48844 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5fdbda0-e8fc-3c00-88a9-9162536777c6 | -11.6274 | -52.86145 | 2025-09-29 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a303e8d-a378-31c7-9306-273c67860119 | -16.50708 | -46.03236 | 2025-09-29 04:59:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9414b256-087b-35bf-91a7-2452d0a232b0 | -11.76251 | -47.56377 | 2025-09-29 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9bed3ffc-8b52-3a20-9f04-6cc47b69fb2c | -13.8223 | -47.48672 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f96c5272-aed0-3c0f-931a-8fac840bd321 | -12.6542 | -51.66236 | 2025-09-29 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 902f44bf-5e38-31fc-8fd1-1be8d6cad170 | -15.32566 | -47.91016 | 2025-09-29 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01bb5448-b130-30ec-93e5-5b9fefc2c299 | -10.99691 | -57.06118 | 2025-09-29 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 05a29b12-676d-3d5e-a7d3-1e51f306ead5 | -11.44898 | -51.49075 | 2025-09-29 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f35139a-c1e9-3386-b13c-99326f0d3674 | -16.20572 | -48.26504 | 2025-09-29 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 46bd776f-f02e-3fa3-89d9-c1606a2e52ea | -12.94081 | -46.77246 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5e6e6251-8f1b-3d5a-8f91-6f2632dc32d4 | -14.54798 | -48.40702 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ecc736d7-b4fa-3763-8937-dbddf1433835 | -15.6191 | -46.25155 | 2025-09-29 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dabef5dc-76e4-3898-a2fd-b34e08364cd2 | -11.83241 | -51.78978 | 2025-09-29 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ee98156-69bb-36cb-baf6-104989dca081 | -11.71387 | -44.43398 | 2025-09-29 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1dcd8f6d-cde0-3af5-98eb-60462deb67e1 | -12.87507 | -46.78259 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ee8be2d-7f67-32de-aaa7-704e7a0abcba | -11.80829 | -51.79997 | 2025-09-29 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7059f4b-6d25-38b1-8142-e041354d0caf | -12.01628 | -47.79018 | 2025-09-29 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4d36e445-f4ca-3fc6-96af-d4d8631bf27b | -12.3496 | -54.15345 | 2025-09-29 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cb8129a-ce30-3a5a-a21b-c9fa8c4221a6 | -12.16484 | -47.77536 | 2025-09-29 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0f9d800-150f-3c94-9b3f-340fc9a2e0a6 | -13.2563 | -48.4452 | 2025-09-29 04:59:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a42186bf-62ff-3450-9fd7-c7e987e23799 | -14.53584 | -48.42705 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 50a396dd-af1c-33f7-b4ea-e1b089f49c49 | -15.41578 | -48.22992 | 2025-09-29 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5e1ed0a-86a3-3977-a30c-23bbfa36c6d4 | -13.84049 | -47.97361 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e50b5c3-7499-3985-89c1-973c8ba9546a | -13.65452 | -48.06553 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 92646b83-ff3e-3135-bb43-3d027b150f73 | -13.17364 | -49.99914 | 2025-09-29 04:59:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0001c294-ad04-313e-a9cd-4d001a1cacb3 | -11.71335 | -44.4385 | 2025-09-29 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 888b22af-efad-30fe-aceb-700c25076de3 | -15.55378 | -47.87504 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 28c7621a-fdb1-305c-be82-075c5908a0c0 | -14.70356 | -45.20833 | 2025-09-29 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9afab262-2c72-34cc-8216-275222984fa5 | -12.79447 | -47.76553 | 2025-09-29 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5d20b92-5ae5-3df1-b276-9c0529f6b606 | -17.40196 | -47.11451 | 2025-09-29 04:59:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 309dc6d8-10bf-3420-935a-0fefe1c82db2 | -17.39653 | -47.11385 | 2025-09-29 04:59:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8ac18e1-1dbc-304a-8de5-96bc03a5af5a | -16.5013 | -46.03193 | 2025-09-29 04:59:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8224d97f-f07f-3ebc-9aa0-02c06fa027f1 | -11.45517 | -51.50111 | 2025-09-29 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| e56dc9b6-df6d-3ad8-b53d-a222e1cf8f3e | -15.19682 | -48.47973 | 2025-09-29 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e9924bf-8ada-3f3e-9238-b259e0e0b1df | -15.17374 | -50.0853 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2bd8146c-0231-3090-8469-15cd10dcf304 | -16.2055 | -52.82173 | 2025-09-29 04:59:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe9c19c2-dd08-39a8-842b-856e3b4e2bda | -15.54873 | -47.87455 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.5 |
| bb17ad50-7bda-333b-bbb4-84b544c9a01f | -13.626 | -47.33935 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 02290f7f-6d60-30cf-a0ab-a593b81f19c2 | -13.60075 | -48.06266 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1d3427e9-bc16-32b9-a422-a597836408c2 | -13.5905 | -47.29014 | 2025-09-29 04:59:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9e63a9c-7c31-3ca4-b688-5a5bc6d1c455 | -14.49301 | -48.54257 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b8f9c65-cb87-3454-9329-39e962bf1caf | -14.52413 | -48.40249 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6a0c224d-f170-3991-9144-03efa8d1efba | -15.53835 | -47.87585 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9aeac9d-69bf-3d34-bd55-eba915e70d62 | -10.39861 | -54.31355 | 2025-09-29 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7a65a19-7c2f-31de-894d-82c6d83f0ff8 | -15.61274 | -46.25799 | 2025-09-29 04:59:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 51c7eff1-119e-3fbb-ab93-6a04e852ddba | -11.62448 | -52.85692 | 2025-09-29 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba8d574a-e116-311b-a971-9e9d3bb3ac21 | -14.54292 | -48.44888 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 20d5494e-60b9-3319-b382-9c5f2b737cdd | -11.69485 | -44.44065 | 2025-09-29 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee48aea9-cd37-391d-9c68-6804f238ab1b | -11.83358 | -51.80824 | 2025-09-29 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20029dc7-a39c-337c-9661-8fd5367381d9 | -15.9109 | -46.20348 | 2025-09-29 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| daf89a4b-514b-3818-9cbc-cbd787b5d712 | -12.76349 | -46.86308 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8df8f460-217f-33f8-8e8b-061bf5e59f59 | -11.62389 | -52.8609 | 2025-09-29 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e371b806-26a8-3d3c-815b-501741bde88b | -13.811 | -47.90792 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a73366b2-ccee-3a3f-b383-a81c5fb34da2 | -11.93219 | -47.95537 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 462a9e99-831d-3cc6-a24c-8ac2988f59b7 | -15.16555 | -46.41302 | 2025-09-29 04:59:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 39d0ea5d-bcb9-3130-b9d3-26ac8a20ee34 | -15.60912 | -46.25586 | 2025-09-29 04:59:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 27df032b-d759-3a41-9b36-c6c445dcd8bc | -11.83612 | -51.79031 | 2025-09-29 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 306d04ba-1374-3b87-85c6-262681646f50 | -16.50173 | -46.02798 | 2025-09-29 04:59:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32df9103-b762-3726-9a8a-e70bf32f1fa3 | -11.86356 | -48.245 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b4da351-581f-3a75-a13b-dc936a59b320 | -13.57691 | -48.10229 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 822b9c63-3955-317d-92e4-7ec8734c40a8 | -13.57957 | -48.08135 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ec14ac5f-b44f-3134-83af-8f9e5c67843e | -12.96315 | -46.24309 | 2025-09-29 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a6c3bab-7c3a-396a-826c-454b9ff8a5e2 | -13.49523 | -47.40979 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2a6ec72-f664-3c7b-8827-27257abf2d9a | -15.0887 | -48.32384 | 2025-09-29 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a609eaac-faff-38b1-8cc1-8c5358971aad | -12.96264 | -45.17111 | 2025-09-29 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2458ab0-921a-35e0-b652-b4b1195b6536 | -11.92006 | -47.97461 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README71.md)
