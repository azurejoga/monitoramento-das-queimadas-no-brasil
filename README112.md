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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d42289c-4ac8-399e-a2ec-319966dcf383 | -15.16685 | -52.47977 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dfe15b0f-5962-38dc-8cd4-e1b544a4d0c8 | -14.73562 | -60.23202 | 2025-09-13 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d9fcd48-bd2e-308e-84bc-cc84ba76a8a9 | -10.1618 | -64.73285 | 2025-09-13 05:27:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 96bda227-5490-38f7-a4e0-9525a77b3625 | -12.87456 | -62.16174 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 030de2ff-0544-3d2d-bfd7-5c4ebd9a88f2 | -15.78481 | -52.25974 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c2e5c8c-1da5-3ac3-a1eb-efb67f5607a2 | -15.86486 | -49.95061 | 2025-09-13 05:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 43e64a26-899d-3094-b99f-53bc2a4dd7b2 | -15.55532 | -54.80466 | 2025-09-13 05:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f45aba3a-207f-398f-9270-218c3a72694a | -16.3382 | -51.53671 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9369ceb3-c70d-3e21-9b41-ce84466287bf | -17.43588 | -49.2554 | 2025-09-13 05:27:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b3e4bab-4c03-3ccc-b893-a5669eb2c6d2 | -15.06836 | -48.02059 | 2025-09-13 05:27:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6e324af1-6e60-38d6-9b7e-b444f92723ca | -14.38986 | -60.31209 | 2025-09-13 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be0a0c53-73b4-3dcd-8350-af68c378e721 | -16.53328 | -51.73921 | 2025-09-13 05:27:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15ad028b-b791-3fa0-af01-4a9554d65d37 | -12.95459 | -48.00495 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| eaea1171-9959-36b8-9b66-4e0121800b20 | -15.59385 | -54.77064 | 2025-09-13 05:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 38396952-f463-3e31-944b-b1069d4af1fc | -12.88186 | -62.11569 | 2025-09-13 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74cbd857-716f-30eb-ab0c-577d6fdbd4aa | -14.39336 | -60.28822 | 2025-09-13 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 362e90cd-1434-3499-8bea-e968a085c935 | -13.23285 | -51.7354 | 2025-09-13 05:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b353f93-2333-3119-958c-981cf80d158b | -16.33221 | -51.5354 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 65c863e7-97e8-333b-a6f7-06f5334cbaf7 | -15.21864 | -56.6891 | 2025-09-13 05:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f627e05f-4880-32af-b31c-9320770964d2 | -15.09333 | -47.99823 | 2025-09-13 05:27:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88406b35-5c1f-3669-b5dd-f1df88210d90 | -15.7115 | -50.58479 | 2025-09-13 05:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b8e88955-8ea8-353e-af21-b55258d1fd21 | -15.17384 | -52.31764 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ca2f0128-4a77-30e9-b6ea-0f61d815ddf2 | -16.37011 | -51.53882 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c717232-14b8-3b26-92cd-f16d24222af9 | -16.34017 | -51.53173 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 800d2542-e608-344d-925c-0c9eb4413664 | -14.71811 | -59.68699 | 2025-09-13 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7898e958-8adb-3844-8ee2-b2d300111786 | -15.14363 | -52.48335 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 055413be-008a-32dc-9172-a6ba08ca1e11 | -15.68064 | -49.90239 | 2025-09-13 05:27:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 72644571-6aff-378a-830d-b4a9e8716269 | -12.94983 | -47.9802 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2d266d6-04b6-3550-bf73-dee0a60a867c | -16.41742 | -49.24297 | 2025-09-13 05:27:00 | NPP-375D | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bc2e672-d04e-3250-ab07-59ac3fb29c0b | -16.49026 | -55.13133 | 2025-09-13 05:27:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| e230a808-2f32-39f1-9188-afd5a1c608b1 | -16.4149 | -49.04069 | 2025-09-13 05:27:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2dadbea6-665a-3819-a69e-a146adf44277 | -17.37043 | -52.90548 | 2025-09-13 05:27:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 711bcf80-4fe1-3675-8566-bb8c81818b60 | -10.15888 | -64.72789 | 2025-09-13 05:27:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f2c80406-7f83-3438-8e8b-5ac4d3b95791 | -15.76954 | -52.23925 | 2025-09-13 05:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8e7ce5e1-5bed-3553-8a6c-1e5aaf21b941 | -10.14718 | -64.73035 | 2025-09-13 05:27:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b95cb86f-6102-3d3a-9783-e687b471e859 | -11.25367 | -61.56886 | 2025-09-13 05:27:00 | NPP-375D | MINISTRO ANDREAZZA | RONDÔNIA | Brasil | 1101203 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c92cb12-52a0-3367-834e-677af9bdafa7 | -14.7362 | -60.22806 | 2025-09-13 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bd33973-c48c-3227-bdce-7456b18935f6 | -15.86707 | -49.95141 | 2025-09-13 05:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8401ae66-85ca-35b7-9144-24abe09c8215 | -17.43841 | -49.2264 | 2025-09-13 05:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4928f327-0241-39b9-b943-ded9c1be7288 | -15.5884 | -54.77491 | 2025-09-13 05:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f1bf7139-3002-3690-a2c8-d78b79f82797 | -14.75866 | -60.22046 | 2025-09-13 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c810946-8dde-36ef-bcea-cc033ba2f5f1 | -15.58243 | -54.75739 | 2025-09-13 05:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 15f9e12c-bc57-3e98-b517-f70ae24b50c7 | -16.35587 | -51.54345 | 2025-09-13 05:27:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d92e585-791e-3ab9-8cd7-e966617834fe | -12.95356 | -47.98923 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9279aa9d-2786-353e-9abd-11975850f22f | -17.30118 | -48.74746 | 2025-09-13 05:27:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1c3f93ab-09db-37d7-b8a5-99f0c504dfb8 | -15.21686 | -56.69227 | 2025-09-13 05:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| af63b8d7-b24b-3fc9-a1e0-37148d6ccc49 | -16.55776 | -49.22765 | 2025-09-13 05:27:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9159aaa8-5064-3e8d-8827-7b0d00e18b1c | -16.64761 | -49.75605 | 2025-09-13 05:27:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3bd92031-0424-38f9-a1b4-3118a9c0e733 | -15.70978 | -50.58981 | 2025-09-13 05:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 53db305a-dc48-36d8-bf3a-4bb42d716388 | -12.94017 | -48.00357 | 2025-09-13 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dd3e09f3-62c5-31ac-90cb-90f0b6dc02d9 | -15.21364 | -56.68359 | 2025-09-13 05:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 805edb5f-44e9-3b80-a10e-70dcd05e874e | -14.39277 | -60.29224 | 2025-09-13 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd198a80-148f-3a94-94a7-a89e35849edb | -17.40866 | -49.26155 | 2025-09-13 05:27:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4aaffd32-af02-3725-b4fd-cdc1f4aa5e20 | -20.83841 | -56.86992 | 2025-09-13 05:29:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b159d2c2-f899-3925-857e-8ecccd0595da | -22.1826 | -49.61719 | 2025-09-13 05:29:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| cb5d9187-7d85-3a40-9c15-947327692696 | -19.34262 | -56.70091 | 2025-09-13 05:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 49e27892-d37f-3807-8706-04ef223d0996 | -21.06459 | -48.94118 | 2025-09-13 05:29:00 | NPP-375D | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a0843276-ae08-343a-b2c3-ebc3599a31c2 | -22.26604 | -56.80629 | 2025-09-13 05:29:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4c71c7c-6a7d-3c8f-9fcb-7b450514eeef | -19.66953 | -57.00622 | 2025-09-13 05:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2b84ac85-78b0-35cc-8609-07f5202c3442 | -22.66454 | -53.11886 | 2025-09-13 05:29:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d2a0eb0e-42db-3734-a608-1047811b3ae3 | -22.65864 | -53.11824 | 2025-09-13 05:29:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c78b5099-4d25-3685-97fa-eab22af246c9 | -25.05328 | -52.08667 | 2025-09-13 05:29:00 | NPP-375D | GOIOXIM | PARANÁ | Brasil | 4108650 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5737d862-fb05-3814-ba6f-01e26e341d7d | -22.65903 | -53.11374 | 2025-09-13 05:29:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7788790e-25b9-3b97-afef-d2fc23de5cf1 | -23.60702 | -51.4884 | 2025-09-13 05:29:00 | NPP-375D | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3b20adff-43f7-3cde-b9d3-560637a42544 | -21.07337 | -48.93681 | 2025-09-13 05:29:00 | NPP-375D | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3594fe0f-0002-36bd-a173-152d461095c8 | -21.06538 | -48.94458 | 2025-09-13 05:29:00 | NPP-375D | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 6ded1e3c-55f9-31ce-8632-fd63ee230c5c | -21.06598 | -48.93636 | 2025-09-13 05:29:00 | NPP-375D | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3066e7c1-bc5b-36f6-84d4-6708ab737c7c | -22.66415 | -53.12336 | 2025-09-13 05:29:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3fc17683-1c57-3fff-8329-bbec62b4f132 | -22.67005 | -53.12397 | 2025-09-13 05:29:00 | NPP-375D | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fa47afbc-8475-37ac-803b-4926f53e042d | -21.97859 | -49.92552 | 2025-09-13 05:29:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 39e8adbf-4718-39fe-b34a-4b5f85451713 | -22.65943 | -53.10924 | 2025-09-13 05:29:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6d49dae1-022b-391e-9e47-9096068f5c21 | -21.072 | -48.94142 | 2025-09-13 05:29:00 | NPP-375D | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 51492692-1f08-3119-9cba-c43b779a37aa | -20.79181 | -56.95383 | 2025-09-13 05:29:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 388f434b-2746-3121-a6e2-fc441d3e721c | -9.2658 | -59.3997 | 2025-09-13 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 260.4 |
| c1f6a4e0-3f9a-3015-bf5c-3d5cb3a9a2e0 | -9.2656 | -59.4191 | 2025-09-13 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| a164277e-911d-3bc3-875a-79521daaa218 | -9.2472 | -59.4007 | 2025-09-13 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 90acb796-5fff-39a0-9cf1-dc23d995fbc6 | -10.1612 | -64.7213 | 2025-09-13 05:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 5ff7ad5f-79e7-3402-b9e3-0d152e8d4b73 | -9.2844 | -59.3986 | 2025-09-13 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 7f3571ad-0b6d-3a63-95bd-4f77affe20cd | -9.2659 | -59.3802 | 2025-09-13 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 2e764f69-eb41-3d79-aefd-83c411f12518 | -9.2472 | -59.4007 | 2025-09-13 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.2 |
| ac21454b-5293-3812-b8cb-cbe22cbd1faf | -9.2658 | -59.3997 | 2025-09-13 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 144.8 |
| a73cd5a5-8211-3fbe-8182-b78725d0018e | -9.2656 | -59.4191 | 2025-09-13 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 7c5513bc-dcad-3fb6-bd2c-1b60ce8e7f9f | -9.2843 | -59.418 | 2025-09-13 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| f54acf3f-5854-32d9-962f-4f7c487bbc8d | -9.5006 | -55.9588 | 2025-09-13 05:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| abdc2d7d-dbdc-378a-9281-2c3ce95e6e8c | -9.2844 | -59.3986 | 2025-09-13 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| ef36612f-58bf-3b2b-8ee1-5f6b3d82003e | 4.33213 | -60.32898 | 2025-09-13 05:44:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5e66a52-fe72-3f90-95b4-1c85c343be6c | 4.33512 | -60.32344 | 2025-09-13 05:44:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6e283f1-e4e6-3f1d-83ea-a4ae6f27cded | 4.33594 | -60.32838 | 2025-09-13 05:44:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bedc634-1299-3bdb-bbcd-45c0150b0e4b | 3.83657 | -59.93438 | 2025-09-13 05:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89ad926e-0403-3bb0-92c3-a33c5cd78550 | 4.33131 | -60.32401 | 2025-09-13 05:44:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce008c63-557f-375e-9715-a74a4dede595 | 3.84047 | -59.93356 | 2025-09-13 05:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e463f39-3545-3b41-a327-869b8daf2640 | -3.44133 | -59.57939 | 2025-09-13 05:46:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 251276f9-2291-35be-a90d-17a137e44d39 | -3.4375 | -59.57428 | 2025-09-13 05:46:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4bc2e8fd-fcc2-313a-a133-6a53642834c7 | -3.76965 | -59.35749 | 2025-09-13 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0e9ae2fe-a96a-32d2-b0bb-6d437bdff34e | -3.9075 | -59.65411 | 2025-09-13 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8196b67d-fba4-3152-b5ce-3dc85968bcaf | -1.38798 | -60.29275 | 2025-09-13 05:46:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf63d686-f9f1-3f21-bb5a-5692e93237fb | -3.442 | -59.57494 | 2025-09-13 05:46:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 997dede6-7c80-32bb-b9b9-7a58dcff54e1 | -3.43816 | -59.56984 | 2025-09-13 05:46:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f5c28370-4d4e-367c-9c6e-bf5b4ba1f6e8 | -1.3838 | -60.29227 | 2025-09-13 05:46:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a334f96-75cb-3cdc-935e-4d9ab54b698f | -3.76505 | -59.35681 | 2025-09-13 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README113.md)
