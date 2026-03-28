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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7a77aac-7ee5-37aa-a485-399248113b0a | 2.5071 | -60.6414 | 2026-03-28 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 79.2 |
| d65afe32-3453-3a2d-9212-34b2b227c377 | 2.5253 | -60.6601 | 2026-03-28 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 351.7 |
| 3fe76b3f-9eb7-33bf-8498-bc919ff362aa | 2.5071 | -60.6604 | 2026-03-28 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 176.2 |
| 510d5990-7f89-3625-85f6-3c50fca5e6a0 | 2.5253 | -60.6791 | 2026-03-28 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 277528ee-e04c-37af-8d14-f2f754f2d29a | 2.5254 | -60.6412 | 2026-03-28 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 930d62a4-bfb1-3bdd-b66c-d9df34aad3f1 | 2.5253 | -60.6601 | 2026-03-28 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 295.9 |
| a4162c48-4267-3997-83d4-6239ad9dde1a | 2.5254 | -60.6412 | 2026-03-28 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 139.8 |
| 5da3729d-b7d9-36e4-b4f7-3d5d589897f0 | 2.5071 | -60.6604 | 2026-03-28 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 178.3 |
| 4ec32078-eea0-3ae9-ab25-72e431e91193 | 2.5071 | -60.6414 | 2026-03-28 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 93.5 |
| b6089b08-d8e9-34fa-be9a-f50685fac5d1 | 2.7811 | -60.5616 | 2026-03-28 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 90.8 |
| f842ec44-0739-3674-9d6e-f9c0bc683316 | 2.5071 | -60.6414 | 2026-03-28 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 25887a94-18cd-36e9-9424-41d9044a5582 | 2.5253 | -60.6601 | 2026-03-28 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 238.4 |
| ea19af98-76c1-31df-81cc-c02d296850bc | 2.5254 | -60.6412 | 2026-03-28 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 127.4 |
| 59cb9f57-7039-320d-bf68-0ddd05cc9c48 | 2.5071 | -60.6604 | 2026-03-28 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 172.0 |
| 34dddc72-b580-36f7-80a8-87eca73f5edf | 2.5071 | -60.6414 | 2026-03-28 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 050ae1ec-3609-3457-9133-89fa7568700a | 2.5254 | -60.6412 | 2026-03-28 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 87.1 |
| f76386e7-e80d-365b-a92c-483ddadb2bbc | -6.5631 | -51.1126 | 2026-03-28 00:30:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 7cef4a95-7f55-3d6b-846f-53f43d093133 | 2.5253 | -60.6791 | 2026-03-28 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 6c31de6b-7b9a-3302-b5bb-422a964ac03f | 2.5253 | -60.6601 | 2026-03-28 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 173.0 |
| 2a2a914f-097d-3ddf-8fcb-19029f164171 | 2.5071 | -60.6604 | 2026-03-28 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 89.2 |
| bdef12f1-2db8-331c-a50f-a8e653b5e0a8 | 2.5239 | -60.623001 | 2026-03-28 00:30:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7733d680-f79d-3a88-a8e1-aede84ed7a13 | -20.8008 | -49.794601 | 2026-03-28 00:30:00 | METOP-B | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3f295f3b-d252-37bd-9cb4-047d22f30ae3 | -22.889299 | -43.701698 | 2026-03-28 00:30:00 | METOP-B | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7e54aaf3-12ad-38cf-bd8f-e83486b535bd | -21.020599 | -50.369598 | 2026-03-28 00:30:00 | METOP-B | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4a12a868-378c-3c7f-85da-4ff24ecb7459 | -20.8088 | -49.784698 | 2026-03-28 00:30:00 | METOP-B | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f1af01ee-731f-3fde-b2dc-1985e8776d86 | -24.5459 | -50.6992 | 2026-03-28 00:30:00 | METOP-B | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5f155266-e3b3-33fa-a329-03e421e1d704 | 2.5141 | -60.6208 | 2026-03-28 00:30:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1cd16e89-1ee7-39f1-9089-37ed28c02e8f | 2.5261 | -60.613098 | 2026-03-28 00:30:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4897c38f-d781-36c0-a5c0-36b0a7619b64 | -21.351299 | -47.033699 | 2026-03-28 00:30:00 | METOP-B | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d85cef05-6218-3118-a532-71260fc52c25 | -25.168699 | -49.368099 | 2026-03-28 00:30:00 | METOP-B | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6bd23370-81e9-395f-8289-aa9930929719 | -21.490999 | -48.7374 | 2026-03-28 00:30:00 | METOP-B | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5bd1afec-0b73-3276-aa5e-ff2c2596d545 | -20.799101 | -49.787201 | 2026-03-28 00:30:00 | METOP-B | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4bedf06f-796f-37e4-a136-d73d04cfce37 | 3.4231 | -59.9375 | 2026-03-28 00:30:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4dc73b03-320a-3cfd-8a48-95e3f2e9cbe0 | -22.899 | -43.698799 | 2026-03-28 00:30:00 | METOP-B | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3495a69d-a697-31ff-9dff-ad89f04e8389 | -6.5681 | -51.0723 | 2026-03-28 00:30:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa5fa316-1286-3358-a315-7b287c9119b0 | 3.4211 | -59.946301 | 2026-03-28 00:30:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9eb81e82-c68b-3bac-ae49-25c672b01cf0 | 2.5163 | -60.610901 | 2026-03-28 00:30:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5e2cd99e-eb33-3559-a97e-2ca0862864b0 | -21.4928 | -48.745098 | 2026-03-28 00:30:00 | METOP-B | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 492eb9da-ae4b-316d-b5cf-d78b2635dfbb | -24.547501 | -50.706799 | 2026-03-28 00:30:00 | METOP-B | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 74bf1991-5e85-318e-badf-a72648cc5f92 | -2.6824 | -52.952702 | 2026-03-28 00:30:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cc658e4-93a7-3459-8459-2511c244b197 | -20.797501 | -49.7798 | 2026-03-28 00:30:00 | METOP-B | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2da09c46-f94f-3504-b93b-51dadbd48d37 | -25.171 | -49.3894 | 2026-03-28 01:01:00 | METOP-C | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c09572e4-dd90-31fa-88b9-27a64057f92d | -20.803301 | -49.8013 | 2026-03-28 01:01:00 | METOP-C | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8aff18cc-8084-3599-8f1b-f3b788e490a6 | -20.805099 | -49.808899 | 2026-03-28 01:01:00 | METOP-C | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b169a693-dfb1-3a35-a6fd-297e8c29ccf6 | -24.5453 | -50.729698 | 2026-03-28 01:01:00 | METOP-C | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0a4ac0bf-934b-3ce0-b5c7-f2a6c6514694 | -21.5042 | -48.762901 | 2026-03-28 01:01:00 | METOP-C | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2355fdf6-441a-3dbc-b45a-d7477bcf291d | -24.543699 | -50.722198 | 2026-03-28 01:01:00 | METOP-C | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 015a0554-3c48-3773-a839-dac337014ec4 | 3.4196 | -59.9744 | 2026-03-28 01:04:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2cd28390-31c2-3909-9ce2-97e697e1c710 | -5.81549 | -35.4491 | 2026-03-28 03:42:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a0d1729e-854b-3fd4-b94d-e49f7b3cac2a | -11.54326 | -38.98235 | 2026-03-28 03:45:00 | NOAA-21 | TEOFILÂNDIA | BAHIA | Brasil | 2931509 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 93c5950d-b985-3060-9960-e718338b27f7 | -12.07568 | -40.25635 | 2026-03-28 03:45:00 | NOAA-21 | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f3085fbf-7ee6-36ff-b8c5-d4105c195196 | -8.08023 | -35.73631 | 2026-03-28 03:45:00 | NOAA-21 | CUMARU | PERNAMBUCO | Brasil | 2604908 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0f86ebe8-914a-3eb6-b447-ac460e72d938 | -12.07403 | -40.25419 | 2026-03-28 03:45:00 | NOAA-21 | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6052b58d-868f-3c49-9c1e-5f8daf0020d3 | -24.54456 | -50.73329 | 2026-03-28 03:47:00 | NOAA-21 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 6f39309a-4e58-3275-b177-e9a51fd923c5 | -12.48957 | -43.78434 | 2026-03-28 03:47:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0c3f739-8932-3625-ae04-b549db012eab | -24.85428 | -49.47221 | 2026-03-28 03:47:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 12317ddb-8f1e-3627-9208-a56f714edfdb | -16.92477 | -43.59938 | 2026-03-28 03:47:00 | NOAA-21 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2a12b9f-862e-36ee-9605-fa7613d0e0c3 | -24.54556 | -50.72908 | 2026-03-28 03:47:00 | NOAA-21 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 75f1bb37-92dd-33ad-8134-171f85abb256 | -17.81142 | -42.74177 | 2026-03-28 03:47:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 005475ce-0a36-3331-bea8-5a16d8f9a5ac | -15.91161 | -43.22693 | 2026-03-28 03:47:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dd3c11e6-9034-3a28-8192-66809e09b6dc | -16.92403 | -43.6033 | 2026-03-28 03:47:00 | NOAA-21 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 825aa291-dfe2-3bf3-b467-252478538797 | -16.92397 | -43.60353 | 2026-03-28 03:47:00 | NOAA-21 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac3d1fba-88b6-398e-bc32-771acfe9691f | -18.48349 | -44.80791 | 2026-03-28 03:47:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc493dad-9dcc-36ef-8666-46a84b2da9a2 | -21.36029 | -47.06699 | 2026-03-28 03:49:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b08a2a9-f05d-3b5f-b416-0c21edbb9f64 | -21.3555 | -47.06575 | 2026-03-28 03:49:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b460496-1ae7-3154-a8e7-ecdb3f801d68 | -21.71805 | -47.25442 | 2026-03-28 03:49:00 | NOAA-21 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06bbdf89-b954-3fee-a64c-5f160411fc0e | -20.8055 | -49.81475 | 2026-03-28 03:49:00 | NOAA-21 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 2c772c76-4326-3d80-9f0e-ff5c2ef1fd6e | -20.80649 | -49.81043 | 2026-03-28 03:49:00 | NOAA-21 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 57c58930-dd8f-3247-a21b-b0da9d04938f | -9.26751 | -40.53008 | 2026-03-28 04:14:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| fe6d363f-7c46-39f9-b5dd-37779e4aad9f | -5.81479 | -35.44968 | 2026-03-28 04:14:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0a3ee4a9-ef0a-3d5e-be95-f8be882cc759 | -4.69701 | -38.16192 | 2026-03-28 04:14:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7bb1d5e0-59fc-31ee-9114-fe2620c2b9a9 | -5.43534 | -44.03539 | 2026-03-28 04:14:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 341b1b34-05af-38e3-ac3c-2d5f6f349553 | -3.27283 | -43.54321 | 2026-03-28 04:14:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81e6c402-25b9-37e4-a59c-c5d4beba8834 | -3.27638 | -43.54378 | 2026-03-28 04:14:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3bb83ef-7271-307b-a61d-486bc9ee62d1 | -3.86697 | -54.23974 | 2026-03-28 04:14:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1ee2dc28-4133-3cbc-b4aa-309495c4a816 | -21.35854 | -47.06353 | 2026-03-28 04:17:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ffe5c8d-e77e-3173-82d6-63dbee8a57cd | -20.80626 | -49.81533 | 2026-03-28 04:17:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 44d61230-f0da-3c5d-bde2-d55eb048714a | -21.90284 | -48.51364 | 2026-03-28 04:17:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fcdd1c04-73cc-3435-98b8-08190f4b9163 | -11.79458 | -42.63877 | 2026-03-28 04:17:00 | NPP-375D | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 0d70368c-fa6f-36d5-a151-2cb4e3e314bd | -20.80235 | -49.81446 | 2026-03-28 04:17:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b80c3e63-5c67-34ba-9684-a08ba6020689 | -22.70623 | -43.37936 | 2026-03-28 04:17:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0684024f-5acf-37f1-b977-dc112bfa2947 | -21.71711 | -47.25704 | 2026-03-28 04:17:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 09a9241d-d95c-36e0-b583-ce104f5f620e | -21.49748 | -48.76949 | 2026-03-28 04:17:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd36318c-76e9-3b0f-ac99-019142e49bdb | -21.7112 | -48.43208 | 2026-03-28 04:17:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63fa8083-6164-38bb-9778-57639ce608c6 | -16.92402 | -43.60107 | 2026-03-28 04:17:00 | NPP-375D | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c43788a-735f-3fd4-9bae-8d279fca63e6 | -21.54395 | -48.72207 | 2026-03-28 04:17:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 899d5256-ae49-306c-b994-93cea8f7c6de | -23.40487 | -46.42158 | 2026-03-28 04:17:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a0a4e729-6d3a-304f-b0c3-9ac6dbc26e33 | -21.49382 | -48.76869 | 2026-03-28 04:17:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df51a767-8fc8-3df5-96a8-0edcacd46d76 | -21.35511 | -47.06284 | 2026-03-28 04:17:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b2ca23d-c810-3872-bd64-79951718e9b9 | -10.37367 | -48.31055 | 2026-03-28 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25bf12ba-0720-3ba4-812e-a12ef32b2a08 | -23.38942 | -45.00944 | 2026-03-28 04:17:00 | NPP-375D | UBATUBA | SÃO PAULO | Brasil | 3555406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 306d0cbe-3342-3514-bdb2-553d9f167613 | -21.13913 | -43.95638 | 2026-03-28 04:17:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8cb665c9-8077-35b7-b0eb-6dd2403b9c8e | -23.40821 | -46.42223 | 2026-03-28 04:17:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0a95fd21-6c49-3636-8b45-9b5379ac22fd | -21.71144 | -48.43468 | 2026-03-28 04:17:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09c1e18c-dd99-31f9-91b2-487a7558a108 | -22.52804 | -46.02598 | 2026-03-28 04:17:00 | NPP-375D | CAMBUÍ | MINAS GERAIS | Brasil | 3110608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9897b76a-d007-31b5-a464-289ae0b58f2f | -23.28029 | -46.60272 | 2026-03-28 04:17:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9a156146-2758-3817-8cd5-b185ee46e0b0 | -20.80598 | -49.81146 | 2026-03-28 04:17:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 8fc5bc5e-7a20-3ea8-891c-12a530780171 | -18.48569 | -44.80743 | 2026-03-28 04:19:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35af02f9-0272-35e5-931f-b256a91a39da | -23.52641 | -46.85088 | 2026-03-28 04:19:00 | NPP-375D | CARAPICUÍBA | SÃO PAULO | Brasil | 3510609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2584a622-4b76-3235-84ba-244d0a88ea3f | -18.48237 | -44.80685 | 2026-03-28 04:19:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README2.md)
