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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbb83a5d-6812-39ef-a175-1e8182dd3819 | -11.10306 | -52.01589 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e1312f8-b311-3cc0-b450-14c5cae13f83 | -14.12624 | -51.70505 | 2025-09-06 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8376ed1-2590-35d3-8530-79f1e6fc5e8e | -13.27197 | -46.81331 | 2025-09-06 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a3df9678-ef43-33a2-a0e7-1ed06c664368 | -12.95894 | -54.79667 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c12111f6-f7a1-3f75-92d9-ca3ce9dd40e8 | -12.01232 | -47.78178 | 2025-09-06 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 301dc507-0afa-3721-82d3-d9c0282b2a02 | -11.93352 | -46.64882 | 2025-09-06 04:40:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76d2082e-eddc-3fa8-9734-63cefc174bf8 | -12.97387 | -54.80655 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73861393-2575-39a9-9b53-09ac71777c82 | -13.66494 | -46.95287 | 2025-09-06 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| abcef12f-2bc1-3194-8025-722234949e60 | -9.74081 | -51.0642 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4ecc1f70-a8e1-3b06-92c7-6a1c50656b04 | -12.95505 | -54.81963 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| babc1ce4-af7f-3c7b-9a5c-46abe1360729 | -15.84758 | -52.28353 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9c25915f-898b-34b5-b14a-6e323c7f17ea | -13.54755 | -48.12225 | 2025-09-06 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e50a9cf1-ff07-3113-95b0-f3fa90710349 | -14.33877 | -60.32354 | 2025-09-06 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90ecbaf0-0e83-3b36-a0d6-134a561adcfe | -15.54551 | -48.39455 | 2025-09-06 04:40:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83dd5c64-9238-33f5-a9c1-f1b7455372e4 | -12.48435 | -53.85874 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 737e6e17-2513-398f-b822-2fa8419e9d95 | -12.29944 | -49.9977 | 2025-09-06 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a281d6db-ad80-3634-8ac6-90bfa12189a6 | -12.95072 | -54.79993 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b6fa8d51-4997-3268-93dd-bebbaf00fdf5 | -11.9308 | -46.66766 | 2025-09-06 04:40:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b10769f2-3847-3eb4-8905-c7dece186517 | -11.58743 | -52.18956 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e01b58b3-0641-3754-85a5-91d2b3b3a220 | -15.5741 | -52.91782 | 2025-09-06 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d415d28f-bd2a-3629-9b61-e3778a285371 | -9.22928 | -57.08897 | 2025-09-06 04:40:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c1e7509-78d3-30c0-bf40-391ee4c620ac | -15.71265 | -53.5835 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1bb33fe3-b1e9-37e1-981a-84d74e44f1a4 | -11.60852 | -52.16668 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35a37066-439d-3e03-a9c4-cae0a5020e9c | -9.67956 | -51.10511 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af199af3-6b90-3910-8e08-5441f84d9513 | -13.74724 | -46.92125 | 2025-09-06 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec8b15c7-e5aa-3e2e-b132-7dd96c19cba8 | -10.60509 | -44.32701 | 2025-09-06 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 77bad607-2d20-3c12-a6a8-f04b8d936bed | -15.58142 | -52.91536 | 2025-09-06 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bbd2217-b305-3ac6-be0c-66978f84a8a1 | -15.12749 | -52.343 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 13c43876-bd16-3019-975d-b44f4b61c9aa | -12.95149 | -54.79536 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8f6b5425-66a1-3529-80e3-b776420db6aa | -14.57848 | -48.09253 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 262a3a7c-aad4-39d5-adff-5803ff86769f | -12.99383 | -54.82422 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f60830ea-804e-3fa4-acef-b7e3bd06e345 | -15.36626 | -46.41874 | 2025-09-06 04:40:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c52e75b-967f-3d92-a020-2564ae65d329 | -12.85008 | -48.00102 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce8d121e-8e0d-3618-86be-08926a1dc838 | -12.95739 | -54.80583 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 48a2f2ca-521b-31bb-b281-f053b64c6b73 | -12.96192 | -54.80906 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dbe8b429-70fa-3566-aa69-e7d5f8ca8ed2 | -14.57413 | -48.01374 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5310d967-becb-3328-9646-39ca902984ae | -13.1866 | -44.48816 | 2025-09-06 04:40:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c3b1a65-f7bc-3a22-946e-4f1274ae57c9 | -12.00622 | -47.78189 | 2025-09-06 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3693c5f-63d9-384e-8f00-7dab16cfaedc | -12.48647 | -53.84632 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b6da96a-b81c-3262-9bdc-d4327dfa5953 | -12.96775 | -54.81963 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d1563f2a-f59b-30f2-ae02-e03a522579a4 | -9.57364 | -57.74979 | 2025-09-06 04:40:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b8188d3-3e5c-3e2b-baca-a97a1481300f | -15.17713 | -52.3961 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 685764ba-478b-3b37-83cb-5cda711ad663 | -9.70978 | -49.49414 | 2025-09-06 04:40:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6d1bb22e-8603-397b-8342-333399ea6b17 | -16.32226 | -52.93618 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80092a70-8376-3467-bcfd-32898a9c57b9 | -11.17867 | -55.0455 | 2025-09-06 04:40:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93365c9e-a02c-3097-93fa-f34630836d46 | -13.01167 | -54.83212 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d0997597-f6b9-33a7-b08d-386822f3f30e | -15.14765 | -52.32423 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73ef8619-c1e5-3557-9160-43d8f295a358 | -16.29617 | -45.69093 | 2025-09-06 04:40:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4a12ee0-3681-3d10-8bea-dd77cd7e416e | -10.21983 | -50.52972 | 2025-09-06 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af8a0b79-9ee8-33c7-8328-32cdaa7be0be | -14.80575 | -48.11906 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c0f74c39-07f4-34b6-8fee-d1a5bd0fc9e6 | -11.63072 | -47.80406 | 2025-09-06 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97abd39d-6782-30ae-9995-f3bb4119c177 | -10.44611 | -53.61398 | 2025-09-06 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98567835-0853-32a8-8cd2-d7ccc97e8319 | -10.79453 | -47.74511 | 2025-09-06 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 74963854-3c7e-33f3-a15a-cba6df3a1f7d | -12.49079 | -53.86412 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f74f621-cb3e-3b47-860e-b12e23545075 | -14.53768 | -53.13359 | 2025-09-06 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27952e20-5919-30b7-b39a-7cda904140ac | -12.89624 | -48.88572 | 2025-09-06 04:40:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 30b329c6-22fb-3835-a1db-9186f2558822 | -14.58032 | -48.07944 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea85df36-c6fd-3a97-8b83-361d44fe12de | -14.58274 | -48.03605 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3719dd5a-e1d8-32c3-9400-28aa27258f7d | -9.68106 | -49.28758 | 2025-09-06 04:40:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b78263e7-92ca-30ed-8b2e-66006b3436bd | -15.54333 | -49.82153 | 2025-09-06 04:40:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8031731d-0437-3f35-81bb-c1c074990ab2 | -13.31111 | -51.63853 | 2025-09-06 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20cdb21e-a698-34dd-8a16-ca8f44714be9 | -10.97874 | -46.82134 | 2025-09-06 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb5947dc-92ed-380f-a006-fa4eaed03ec6 | -12.95534 | -54.77267 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18d48a84-3619-36dd-ae81-2c509201fdaa | -15.57498 | -52.89149 | 2025-09-06 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54be044e-4f50-3dfe-8b8e-41e649851837 | -13.25649 | -51.80861 | 2025-09-06 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b96c78de-6d2b-31e6-80c0-2a20d2096914 | -12.95522 | -54.79601 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 913a75ff-3be7-3006-ae14-8f3d49da92fa | -11.21727 | -46.17862 | 2025-09-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 70c7c619-6945-3061-b597-f3b8740989c2 | -11.58067 | -52.18845 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58c936da-ba6c-358c-8839-ac23464c6cb6 | -15.72052 | -53.55743 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2453c239-28da-35f1-9fe7-5cd30a623337 | -9.30175 | -56.81158 | 2025-09-06 04:40:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3eeeca1-0900-310e-b195-9b7684bbaee6 | -14.57156 | -48.03135 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4697bc19-45a3-3fee-b899-2cfe338f0ddf | -15.13082 | -52.34359 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e57a2059-1987-382f-aeee-df72ced6d144 | -12.97893 | -54.82158 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| adae47b1-1740-344f-a671-42041b4c7561 | -12.95878 | -54.82031 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ee4b3c3d-c51e-335f-99f4-3ae4151e77c3 | -9.39417 | -54.74417 | 2025-09-06 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5069d111-968c-31d4-b73a-86ee78c269ff | -9.22018 | -57.08717 | 2025-09-06 04:40:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 351b352b-c9e9-325f-b03b-5feeefc04ada | -13.00282 | -45.21507 | 2025-09-06 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ad839b1-ceaf-3839-b42b-5df9ecbbc8cf | -16.45136 | -45.25553 | 2025-09-06 04:40:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2417748f-38d5-3b38-ab58-cd23f92c7d2d | -12.51005 | -53.85891 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0c8e13fc-8f31-3e84-99cf-583ef6ad0e77 | -11.63058 | -52.22324 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 145e3b00-140e-305b-b000-db721fe53f09 | -12.9598 | -54.79925 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 391821aa-f766-3d28-91c3-b6dc437426d0 | -9.84491 | -48.83941 | 2025-09-06 04:40:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f769b5ee-0a9d-34e9-970e-135435f29102 | -11.01433 | -52.0429 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3741de8f-f4c7-3431-a3f2-8277e16b71a7 | -11.1017 | -52.0457 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a90f3574-8b02-39b7-9d0f-233c5f3e289e | -14.57178 | -48.0044 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0520cc24-d0ec-3816-90d8-b1c5b8aaf865 | -12.49436 | -53.86473 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2fdb454-caca-3334-8611-666664af24f4 | -12.93098 | -48.04601 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a079d565-ea5a-3132-943a-2f5331d97ac0 | -15.847 | -52.28714 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a029c7e5-61d8-348e-a655-8c90ad7d1a7d | -12.96272 | -54.80448 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 68c89755-c760-3f5d-a6fc-de4ef0dd4fea | -13.88586 | -48.02789 | 2025-09-06 04:40:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5c682ca-8ad1-3724-ad0d-d28c5ea91455 | -12.53947 | -49.11795 | 2025-09-06 04:40:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f1bfdd06-b059-3c5b-b86f-e9d332f8b811 | -9.68899 | -51.11028 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87ef827e-4c6f-30bb-bbf1-1ed97ce67244 | -13.26762 | -51.80314 | 2025-09-06 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15591150-5f89-3e28-8ca7-2a68adad1bdb | -11.48318 | -55.54037 | 2025-09-06 04:40:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 406bafa9-1469-322c-bb22-f4c9840976ab | -14.8326 | -48.1898 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b8fd14d-3d7e-3bed-822f-f0b20fe0fe7a | -10.93053 | -50.86786 | 2025-09-06 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3610ed4-a4e9-39c6-81ca-8e854fc728e5 | -13.55946 | -48.11573 | 2025-09-06 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06cd64f4-c8ca-319c-9f83-e7289ec1178c | -11.01492 | -52.03924 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24075122-cad3-3256-b6a1-ab89ce0a1ec3 | -15.12962 | -52.35097 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ba535b5-22ce-32a0-88a7-1bf0a07cb938 | -9.4587 | -60.51239 | 2025-09-06 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README66.md)
