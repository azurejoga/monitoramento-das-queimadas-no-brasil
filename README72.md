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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 824b5a48-b3ec-3e62-ae0e-353ebef7a4ec | -12.94008 | -46.77853 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a7c5c5b-7f9d-3541-a80c-fa86ab1f34bd | -13.02308 | -49.43568 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b1cf165a-1d6d-3e87-8651-0d61f678bab0 | -12.00716 | -46.62561 | 2025-09-29 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b68d7ef4-3937-3bbf-a45d-bded1bb7c040 | -14.75737 | -48.36688 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 453788dd-6d35-38aa-9c6b-9e2128de1969 | -14.66486 | -48.16142 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8e5cb1d-38b0-32f2-b74a-1c28ff321d14 | -12.95469 | -47.21167 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ba2d0405-f1ef-34a6-b102-c28b53a9f3a3 | -15.3251 | -47.91191 | 2025-09-29 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13222d26-47cb-3065-ae9e-6b35b1b02ccc | -11.72145 | -44.42118 | 2025-09-29 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f71891c-11dd-3448-9520-515f87ce45bf | -13.60499 | -48.06822 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 47dc3aff-e80a-3cac-ac6e-8cfbc9801d68 | -15.91567 | -46.21209 | 2025-09-29 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2685f25b-1423-3a60-9c59-8e0a21d8ee7b | -15.53853 | -47.38628 | 2025-09-29 04:59:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b500ee49-2870-3c02-b9d3-22018656f68b | -11.72692 | -44.42653 | 2025-09-29 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d6568d5-6f39-3da4-be66-b5e4f92191a0 | -13.82673 | -47.49239 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c6d761a-5777-36e9-a056-263034cef0c6 | -13.57477 | -48.08044 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d34df368-1d60-3faa-a997-1c1804061489 | -15.27268 | -49.50373 | 2025-09-29 04:59:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d97c399-1aef-3f31-9a16-7b75fcc7f1d9 | -13.83206 | -47.9384 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c39019c8-0f94-3a15-87a2-964d51a491c6 | -16.20919 | -52.8223 | 2025-09-29 04:59:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7927eb1d-fc1a-3639-aaaf-1078080f62bf | -12.64665 | -51.66126 | 2025-09-29 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 81b3a4d5-6b73-3082-93a7-aac9e2e3cd7d | -12.8521 | -46.8831 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ae3e9b1-66df-3d4a-b9b5-9e76c5786e51 | -13.78894 | -47.92516 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f73cab80-d2b9-3451-a55b-5e0f02d1b542 | -15.6147 | -46.25676 | 2025-09-29 04:59:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 63ef629e-d071-36a6-a1be-d7c7c2cdec59 | -13.55897 | -47.26721 | 2025-09-29 04:59:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d33ed673-d0b7-39b3-a21f-4cc2f26e15bb | -13.63168 | -47.33516 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 792c4345-72a8-350b-ac75-eb6003983b97 | -13.65876 | -48.07102 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 62b234f5-8f9e-30dc-be46-a11de3da7c6a | -14.43953 | -44.87671 | 2025-09-29 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8d7c9c66-ff2c-340c-ad8d-13f628d996f7 | -14.59132 | -45.0139 | 2025-09-29 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7520b5e9-e2f0-36f7-9ee0-41a1c071a2ad | -15.06205 | -45.05585 | 2025-09-29 04:59:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f7ad8040-b0d8-38a5-82a0-f2ba18365661 | -13.77725 | -47.85785 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f41c84cd-c712-317b-b740-ef158ad0e828 | -16.5024 | -46.03311 | 2025-09-29 04:59:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c38b0641-8a43-33a2-b6fc-fe8ec84c9591 | -11.45075 | -47.28438 | 2025-09-29 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b487f937-9fc1-369e-8fa6-83ba92556851 | -14.84198 | -45.56657 | 2025-09-29 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89397009-19ff-32f6-aaf4-09e14e07e336 | -17.39575 | -47.12116 | 2025-09-29 04:59:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a0711f2-f3f6-3aec-933e-1e4047080cd6 | -15.22094 | -50.09401 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ab2e8537-c038-3716-b3d0-4fa512c8e6d4 | -12.87016 | -46.96679 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 45f26450-2fba-31cc-a8ee-3d96c22a2b7b | -13.36148 | -47.30097 | 2025-09-29 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f01b9aa3-d8a5-3ef7-a917-0e24c4db4127 | -12.93072 | -46.76796 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20773c2e-c7ca-341e-86e6-97cfdc519d48 | -15.29393 | -49.51646 | 2025-09-29 04:59:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 7a9e511a-b7c9-3900-bbf7-dc7252c77975 | -12.84943 | -46.90474 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f71e849-0227-3835-a9d8-cb0974de57ff | -12.97352 | -46.24831 | 2025-09-29 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fb1759e8-25f8-3e33-918f-e12b9fd7227d | -11.99867 | -47.09979 | 2025-09-29 04:59:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 70fe8ed6-572b-30dd-a5fc-9ab0a2ad0c8b | -12.28706 | -44.10987 | 2025-09-29 04:59:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99a318d9-43b0-379c-89c4-fbd4a4c334b2 | -12.01146 | -47.78948 | 2025-09-29 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| de6cca98-a6c4-3045-af33-4f1c886fd918 | -12.00677 | -46.62874 | 2025-09-29 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 626a85ac-3398-3d53-aa3c-819866e5fb6e | -12.92587 | -47.15257 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b0f71d1-4a1f-3764-a95c-97afd9b05eb9 | -14.57319 | -48.2381 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 35acd57f-f729-39f0-935f-76a76099a2f1 | -13.35651 | -47.29941 | 2025-09-29 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c015d5b-19c3-31bd-a600-fcea7e7af7cc | -14.63129 | -48.28586 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7213eaa1-5c2f-3d79-b35c-03f6aff73a34 | -13.00119 | -49.43292 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb7b5faa-7ec7-346f-8314-54f5d4939bf0 | -13.6056 | -48.06323 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5deae92c-da39-3b2b-977b-65a00e417a93 | -12.98 | -46.84258 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 779e5621-8864-3474-bb2d-3aa7445591d8 | -15.52223 | -47.92526 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d2849b66-fe22-3d5e-b242-b1d39180b067 | -12.89709 | -47.09095 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56290ba8-c732-3462-95e0-583e912a5323 | -12.77521 | -46.85367 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c55ba3b-2998-39da-823e-b13bdfd52158 | -17.08785 | -48.57169 | 2025-09-29 04:59:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b9e0054f-922b-3d01-b644-519d582b9b05 | -15.53189 | -47.92962 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c08eb44-e15c-3c35-8e9a-8e066f066d3a | -16.40753 | -52.17365 | 2025-09-29 04:59:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 312d8db6-fb0c-3d16-8bce-a9b1fa558fe5 | -11.62567 | -52.84894 | 2025-09-29 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3e7a3ff-35e2-3aec-9cf8-21bc1b44fcc9 | -16.48983 | -46.03034 | 2025-09-29 04:59:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbcc6f69-365e-364c-b573-6b10c3aec221 | -13.64298 | -47.32733 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c21f12fc-5798-3257-aa0d-ee7decb20e1f | -12.88317 | -46.98955 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 23da741a-4542-3779-9740-fdc60f6dcebb | -15.07704 | -48.33916 | 2025-09-29 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 252f1358-7cc7-3d26-8de0-6cc055e74e19 | -14.52477 | -48.39744 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a24fd729-c664-3e4d-9680-51a1fa2b6ec1 | -12.65797 | -51.66288 | 2025-09-29 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 06322b90-e13e-373b-a4b5-55e6adfb751d | -12.9509 | -47.18664 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28b06db6-22ef-30d1-9cbd-8d18ae7446bb | -12.20913 | -43.7485 | 2025-09-29 04:59:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8faa8c08-32da-377c-aa7b-2c7bea07311e | -15.27775 | -49.49962 | 2025-09-29 04:59:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79b352a8-d350-3df6-ae31-24f2bb13ae73 | -12.6594 | -46.92279 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9fb5630e-0e73-32e9-9fe3-892bbe7d59c2 | -13.78126 | -47.86602 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c213fb36-a21d-3ed7-87dd-26f0a735aae1 | -15.48147 | -47.92561 | 2025-09-29 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cacb1681-ed17-3a5b-90c2-07f44aec6d60 | -11.03485 | -49.79655 | 2025-09-29 04:59:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9c0c08f5-295d-314e-a86d-f4aebe69d005 | -15.19263 | -48.47394 | 2025-09-29 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1edf997d-8241-3952-8358-6f5273892524 | -15.61558 | -46.24892 | 2025-09-29 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c4ef5bac-eda1-321f-8c47-34cf175c8e14 | -14.52698 | -48.41986 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6195aa2a-556f-3db0-afb8-bebb8ab8921f | -13.59616 | -48.06683 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6718cd35-09cc-3f7b-b08a-ef6dacbc3be5 | -15.28243 | -46.4197 | 2025-09-29 04:59:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cccc60c-8a91-3517-899f-5d5ed2e760fb | -11.97619 | -47.12117 | 2025-09-29 04:59:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2a8c611-b40e-3470-878d-1197b6af6a44 | -16.29102 | -45.85229 | 2025-09-29 04:59:00 | NOAA-21 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e11de26e-c510-3551-84da-ec4f8a91ad0c | -14.53938 | -48.43797 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 6c7d431f-cecd-3e7f-8544-0ce261f24e4b | -11.76321 | -47.5582 | 2025-09-29 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b6af0fb5-53ce-3ce5-9ee3-631c02ffd77c | -12.93035 | -46.77109 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62b4b2c7-20fe-31f5-a414-6a6980d051db | -23.47457 | -52.09556 | 2025-09-29 05:01:00 | NOAA-21 | PAIÇANDU | PARANÁ | Brasil | 4117503 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 12318c9f-47a0-3977-bd2e-6c561d628352 | -17.9051 | -57.61201 | 2025-09-29 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d1dd5acd-406a-3625-87d7-f518a9f73618 | -18.97812 | -48.40223 | 2025-09-29 05:01:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36bbb276-b5e7-3a88-9d46-ec6419d053e6 | -17.73203 | -46.6861 | 2025-09-29 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6374bc7-095f-3ed2-bf40-8d0353a8b50d | -18.19538 | -53.33635 | 2025-09-29 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d391d8d1-6a94-3ebc-9b8d-16614b394198 | -23.22769 | -49.41441 | 2025-09-29 05:01:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 28a24f40-713d-36b7-a0c0-d1fd3eb5d365 | -17.90627 | -57.60472 | 2025-09-29 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9186ce97-9a8c-3552-b88d-b7cd7068286a | -16.00995 | -59.49536 | 2025-09-29 05:01:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7826829-60e9-3354-b20d-b0464018d946 | -23.2292 | -49.39922 | 2025-09-29 05:01:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 8b52b621-9297-3e89-85c0-4fd542865120 | -18.79475 | -47.43399 | 2025-09-29 05:01:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45a47e09-1391-3494-bf99-4afc0c32b068 | -18.21451 | -53.30053 | 2025-09-29 05:01:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 33.8 |
| f3ac003e-ac43-3e5d-93c4-180e9173dbdc | -18.17761 | -53.32917 | 2025-09-29 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 456c013a-a4dd-36a3-bce6-af343f7776ca | -17.75714 | -48.76521 | 2025-09-29 05:01:00 | NOAA-21 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e44f5923-9e8f-39a6-a9e4-0910b17d0ecf | -18.21083 | -53.29989 | 2025-09-29 05:01:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 94cfd416-9094-3e65-9951-29946f2e721c | -20.63339 | -46.16832 | 2025-09-29 05:01:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2101027-2c96-3226-855c-83ad435e2fb7 | -19.73782 | -43.22644 | 2025-09-29 05:01:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0b12a593-96c6-3d52-8a89-dc9ecfbe7534 | -18.19971 | -53.3323 | 2025-09-29 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 477daa8b-567e-37c6-a13f-ba6fa3583e56 | -17.71484 | -46.68802 | 2025-09-29 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37d1cb07-fcdc-3890-84de-7bf89b474c89 | -23.42105 | -49.45862 | 2025-09-29 05:01:00 | NOAA-21 | FARTURA | SÃO PAULO | Brasil | 3515400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0a946d72-aa54-3e0d-aa49-b848bb9d164b | -17.90239 | -57.60775 | 2025-09-29 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |


[Clique aqui para ver as próximas entradas](README73.md)
