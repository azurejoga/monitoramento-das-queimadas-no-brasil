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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2201ee69-5b9a-3b73-9f87-fbff8aa53d13 | -9.57168 | -44.60194 | 2026-01-02 04:27:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 713299a3-9805-3e5b-8603-d4261b697d93 | -11.7508 | -43.64415 | 2026-01-02 04:27:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78a2421f-8f5d-3e26-844b-141199d6980f | -8.70006 | -38.64601 | 2026-01-02 04:27:00 | NOAA-20 | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 695f8c2e-137d-3357-84b7-a17cfb237ed0 | -7.4615 | -35.19195 | 2026-01-02 04:27:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 73fbfa38-baa7-367f-933f-c41abe538a20 | -9.5711 | -44.60585 | 2026-01-02 04:27:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 568f076b-b1a2-3ccc-a8c4-07b89778674f | -7.45467 | -35.19583 | 2026-01-02 04:27:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a447dbb4-980b-3e32-b8e1-4bb18b62ed7f | -7.45528 | -35.2001 | 2026-01-02 04:27:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| c7ef8b1a-188b-34ec-a8c3-636badbdf147 | -12.95245 | -41.18201 | 2026-01-02 04:27:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d612e547-7e77-34c0-9c02-420e0eb27245 | -6.02174 | -44.5487 | 2026-01-02 04:27:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d1ad228-12f9-3bca-adfb-86d061bf41f3 | -10.91807 | -54.24697 | 2026-01-02 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a9630e3-4ab7-354e-80c9-8c7f9b4e32e0 | -8.69542 | -38.64237 | 2026-01-02 04:27:00 | NOAA-20 | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 314e9ec0-2944-3790-bfba-c6292bc85b2f | -11.75117 | -43.64177 | 2026-01-02 04:27:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1938852a-3357-32c9-9e8d-daadfad54385 | -6.01777 | -44.55183 | 2026-01-02 04:27:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c69ddf4b-8de8-3586-aef2-1229d2d4c8fa | -12.49209 | -49.36035 | 2026-01-02 04:27:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87816b71-8c65-3dfd-98c3-3e6c10640ebe | -10.59691 | -44.9709 | 2026-01-02 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d178c83e-630f-3f14-b8a8-390aca889108 | -10.92787 | -54.24416 | 2026-01-02 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fd6c91c-ac77-3ff9-9d07-e66646a75f01 | -10.54811 | -44.68937 | 2026-01-02 04:27:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e26c6660-817c-3568-85d7-f04712c8f1e6 | -7.04512 | -55.43077 | 2026-01-02 04:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94735b00-46ae-3a1a-acf8-d5cb72f01324 | -11.75052 | -43.64645 | 2026-01-02 04:27:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6edbdbd-5084-3fb8-a0e9-670c175351a1 | -8.70549 | -38.64378 | 2026-01-02 04:27:00 | NOAA-20 | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 30b1d3fe-520b-398c-81e2-844a8376be54 | -12.94967 | -41.18268 | 2026-01-02 04:27:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d3bd33a8-d883-37bb-b521-85e9f2516996 | -6.74532 | -39.27194 | 2026-01-02 04:27:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5fe41572-9deb-378b-9ac7-819aa430baa0 | -7.45404 | -35.20064 | 2026-01-02 04:27:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 67e5a0fe-ecc6-3a29-93e8-9fd0e12d188a | -9.35489 | -50.73985 | 2026-01-02 04:27:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ee94d3a-91a2-3690-add9-7b51109bff29 | -8.70045 | -38.64307 | 2026-01-02 04:27:00 | NOAA-20 | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f21f01d3-4b9c-32b3-bcab-dbcfcf546809 | -14.70336 | -48.90079 | 2026-01-02 04:29:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b64e96ad-d936-3b40-8c51-5551e63bb79b | -18.48066 | -53.01186 | 2026-01-02 04:29:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66545804-979b-38a7-9417-73fbefc0e035 | -14.49505 | -52.56199 | 2026-01-02 04:29:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| beef912c-529c-3327-9a5d-2fd4051d6fb8 | -14.35445 | -49.45766 | 2026-01-02 04:29:00 | NOAA-20 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e517ef1-37b3-35f9-b971-46f45129b741 | -15.5117 | -52.29214 | 2026-01-02 04:29:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5bb83f6-3ed9-3245-8722-c2adebf055d8 | -17.05978 | -41.2371 | 2026-01-02 04:29:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 47d6b8e3-c5e7-3f5a-af2b-45896ce02144 | -14.49886 | -52.56268 | 2026-01-02 04:29:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| fc85d50c-2296-3f5f-ae9c-6b2955188b07 | -19.69075 | -42.70204 | 2026-01-02 04:29:00 | NOAA-20 | JAGUARAÇU | MINAS GERAIS | Brasil | 3135001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| ddff1d42-488a-3e61-8ec5-30e4f8a3a802 | -19.7003 | -42.69807 | 2026-01-02 04:29:00 | NOAA-20 | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| bd521971-c342-3bdc-894c-f6c770ba0d36 | -19.69129 | -42.69754 | 2026-01-02 04:29:00 | NOAA-20 | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 66ce49fd-4cbc-3b8d-928f-13ec2b568498 | -14.49972 | -52.55785 | 2026-01-02 04:29:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 738ed9e8-fba8-3360-98ca-c433c99ce229 | -13.50846 | -46.70757 | 2026-01-02 04:29:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0311c024-a296-3e31-b38b-c54bc48a4c1e | -14.49591 | -52.55713 | 2026-01-02 04:29:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4676107c-26ac-3d1f-a333-7af04e46bfd2 | -18.22337 | -42.64993 | 2026-01-02 04:29:00 | NOAA-20 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7bb5e9ed-62f3-374a-810e-6ededd3e3c75 | -14.45019 | -45.50132 | 2026-01-02 04:29:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2405e0e1-0883-3cf9-a4f7-66bd591b7546 | -15.71381 | -46.65021 | 2026-01-02 04:29:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7d75dd3-ef6d-3d52-8325-4c2b88509371 | -17.05431 | -41.24266 | 2026-01-02 04:29:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 209d34e7-3ecf-3324-8614-c3f25732c519 | -15.30074 | -43.86645 | 2026-01-02 04:29:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f9e5fb3-0dcf-3beb-98d5-9a1f65f2254d | -17.05911 | -41.24275 | 2026-01-02 04:29:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 066f2a32-738e-39c3-9438-c370fe51b273 | -15.508 | -52.29144 | 2026-01-02 04:29:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 131c9ba1-0355-3920-a972-b0af45b361de | -15.71665 | -46.65459 | 2026-01-02 04:29:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4dbbbfbd-a7e8-3289-9962-2d82d74523de | -19.69578 | -42.69795 | 2026-01-02 04:29:00 | NOAA-20 | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5174d4e4-0bd4-3601-a5ac-c77301963a5c | -29.65287 | -50.12414 | 2026-01-02 04:33:00 | NOAA-20 | MAQUINÉ | RIO GRANDE DO SUL | Brasil | 4311775 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bc59f4a3-9e78-3109-85d5-dc78e14601e6 | -29.65181 | -50.1268 | 2026-01-02 04:33:00 | NOAA-20 | MAQUINÉ | RIO GRANDE DO SUL | Brasil | 4311775 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8dd21bdf-3565-3a4b-ab6e-b68265da67b5 | -3.65981 | -52.05733 | 2026-01-02 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35ac499b-03c7-39e4-839c-9387ca96f5ce | -2.00352 | -54.31549 | 2026-01-02 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c75cfee-69a7-32cc-b627-38b1a8487cd8 | -3.02437 | -50.51207 | 2026-01-02 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c665870e-690e-354f-96b6-bf82e3ba285d | 3.13169 | -60.72494 | 2026-01-02 05:16:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3480d952-6a97-36c4-892f-2ab1d87a43d8 | -3.02694 | -50.5146 | 2026-01-02 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5872e272-1e93-37a7-93d1-01574c24855c | 3.13236 | -60.72941 | 2026-01-02 05:16:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9435544c-7f51-37d1-bc46-c0d5954ecb74 | -0.08874 | -51.28003 | 2026-01-02 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 58100c05-2121-313a-99f2-edc5fcb9b8f5 | -0.08872 | -51.27772 | 2026-01-02 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 77c9f323-aa33-3b8e-b0fa-147ad3a1e550 | -0.99869 | -53.21235 | 2026-01-02 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e48b47d5-6e68-3f81-9c6d-81a950e9f888 | -2.75515 | -51.6633 | 2026-01-02 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b61753a9-e459-37e1-9160-280cd7bb6538 | 2.54553 | -60.36314 | 2026-01-02 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 477d7103-593e-3d25-add2-d6dba710de66 | -2.86083 | -52.8064 | 2026-01-02 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 082e2796-7296-3e45-a06e-171d9acfba07 | -0.08806 | -51.28206 | 2026-01-02 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| eed9f0f2-bdce-3ccb-a983-ef0486f33d04 | -2.00104 | -54.31742 | 2026-01-02 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4f68bac-c2d4-33e8-b115-5a8c7ba7cafe | -2.75449 | -51.66774 | 2026-01-02 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59c8be4e-8dfa-3253-818f-757cfcde6060 | -2.22552 | -51.95048 | 2026-01-02 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32f8c00d-297d-3239-a68b-c697ca30beac | -1.26161 | -53.48343 | 2026-01-02 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b46bb549-bc44-31af-8f7f-9843867d92de | 3.13069 | -60.72872 | 2026-01-02 05:16:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51b60f3b-2fc9-34e4-ad64-b2ee35136dd3 | 0.68252 | -59.55767 | 2026-01-02 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de473186-cb07-3da8-b443-9f5990caaba3 | -3.86862 | -54.23428 | 2026-01-02 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7571833-f2a4-3466-b37e-4096a0170397 | -2.85786 | -52.79806 | 2026-01-02 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56126574-bb18-31f0-8631-f8cd603b4ddc | 2.54981 | -60.36685 | 2026-01-02 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 77b4d88a-395b-397b-8c34-716f45ffb00c | -3.87042 | -54.23207 | 2026-01-02 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 065ab89c-6cea-31fc-9ef8-517cef9f8cc4 | -1.92639 | -52.11725 | 2026-01-02 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08986176-7930-3ed6-bc55-d05fc5e16ac0 | 1.81987 | -60.46942 | 2026-01-02 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a0e480f-70e6-39e8-9754-8ea5ec7777e1 | 2.54917 | -60.36262 | 2026-01-02 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d2673694-f64f-3567-8041-19b280012550 | 0.41532 | -60.57017 | 2026-01-02 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7102ac4-5bac-36f3-9759-10801e9b81bb | -3.86932 | -54.22953 | 2026-01-02 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee4b2a23-2ac7-3a5b-9f9c-fe616a73b058 | -1.59117 | -54.30808 | 2026-01-02 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64bb3605-0a81-3b20-bff6-d85fd9b763b8 | -2.75067 | -51.6626 | 2026-01-02 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c691584-2ede-368f-8639-3def54b73d81 | -1.06926 | -48.88305 | 2026-01-02 05:16:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 625cc26e-53c4-3780-9c84-cad63af9a218 | -1.92881 | -52.10108 | 2026-01-02 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d779c3d2-e9d7-379f-aa52-4244059b16e5 | -3.65557 | -52.05897 | 2026-01-02 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9368ba04-418b-382c-b093-0574461f4672 | 3.12999 | -60.72425 | 2026-01-02 05:16:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6dd9e32c-a207-32d4-9fcd-aacc8a32f5bc | -3.6554 | -52.05659 | 2026-01-02 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36463d72-e788-343e-8091-54852d20f7c3 | -2.56407 | -53.87574 | 2026-01-02 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c72839ed-e8bc-3253-9c87-ef66644af1f2 | -3.65623 | -52.05468 | 2026-01-02 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42d8d64f-8b04-3d66-af42-fa0a2ac79892 | -10.92717 | -54.24575 | 2026-01-02 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b56b7aff-008a-36d8-80a3-46f978ce1e92 | -6.21576 | -55.65532 | 2026-01-02 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 991573e0-7b0f-3a4d-a835-eb0a5055104b | -7.04873 | -55.43037 | 2026-01-02 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49c2eefa-e3fc-3d06-8644-e9f960a05214 | -7.04758 | -55.42792 | 2026-01-02 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7e9db8e-f945-32be-83a4-d8df7c9dbac1 | -10.92237 | -54.24919 | 2026-01-02 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fbd5806b-9d58-354a-a796-94985f04bab4 | -10.92292 | -54.24516 | 2026-01-02 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f9b4f1a0-1e4b-3475-862f-406f4000e5b2 | -9.8347 | -57.81484 | 2026-01-02 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 870d4e94-d0ba-35a7-a51a-e38a9b6d7ec5 | -14.50207 | -52.55788 | 2026-01-02 05:20:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 44f90063-e0d4-3b58-a456-3f408b3eaf27 | -14.46776 | -59.77172 | 2026-01-02 05:20:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f861b0da-d554-33b8-a6fd-885a2b54ebd1 | -14.49636 | -52.5631 | 2026-01-02 05:20:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7fbfbeae-e50b-38d7-86d3-d2f73ead6f03 | -11.1102 | -54.42333 | 2026-01-02 05:20:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e53c9f65-b5a5-3c15-9db1-d1360e778a32 | -12.29905 | -57.40236 | 2026-01-02 05:20:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 313787f4-a0da-3c2c-95cc-bbe5d2ff3eea | -14.50172 | -52.5608 | 2026-01-02 05:20:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4c3a82b8-ef28-384d-9dbf-e14fac3d80c6 | -14.49706 | -52.55726 | 2026-01-02 05:20:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |


[Clique aqui para ver as próximas entradas](README6.md)
