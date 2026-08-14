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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3d013b3-172a-3cb2-8229-b009c06c6b1f | -18.42144 | -45.19541 | 2026-08-14 04:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35371e22-1175-34aa-b173-19854e0c22a5 | -11.48872 | -54.6317 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f74eacf8-432c-39c8-8281-e6751bd36282 | -14.21894 | -53.35586 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8221dc0d-77f2-323d-b89a-cb24bce65367 | -12.34967 | -53.13656 | 2026-08-14 04:34:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3728c41-b0ff-3548-8fbe-46ed2a643659 | -10.70423 | -50.52441 | 2026-08-14 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05d92187-1719-3791-b36c-d7aa954e01c5 | -11.47227 | -54.6188 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 501d23c7-55b7-36db-809c-7c3cfadbad25 | -10.5918 | -55.5957 | 2026-08-14 04:34:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4967e6e9-9bf2-310f-ac40-75073e515985 | -13.38371 | -42.39199 | 2026-08-14 04:34:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 1188c75e-10c4-385b-8e13-c6f77472d25d | -18.10929 | -47.92793 | 2026-08-14 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 66d05e5e-1d69-30bd-912b-6a150f0ecc67 | -11.48374 | -45.09805 | 2026-08-14 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0918bfe-6d10-320f-a227-f695d2c2585b | -14.28539 | -51.97145 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f1035819-46bc-34e7-a3c8-f00ea65b934c | -14.3054 | -51.96572 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8099edd6-3133-3051-826a-19fa12ac1393 | -15.15981 | -50.05499 | 2026-08-14 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e342b835-b108-3cbe-9789-f88255048487 | -11.48593 | -54.62127 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 05d7ab90-2a80-3429-8eab-410770661279 | -14.29432 | -51.96382 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 29480056-b241-3d61-a5e2-26818ad7ede8 | -16.35529 | -55.38515 | 2026-08-14 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee2248fb-5df8-3dca-a45c-bd4393a1ba9a | -14.44688 | -45.69682 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6aaa6b54-ff29-3dd7-bc05-1d678b71eb7d | -11.61448 | -55.1788 | 2026-08-14 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b9ece75-886c-3887-b804-ce01d77115c9 | -15.03281 | -47.03668 | 2026-08-14 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c708cf65-f9c9-3acf-9f42-b00d9bc45f68 | -15.16696 | -52.81969 | 2026-08-14 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 095be6fb-7f74-3ea7-b2ae-0c27afc7c0ac | -13.24616 | -54.20714 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85baf011-38d1-3a59-914d-919c6e225bdd | -14.47327 | -45.6915 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ffb40ea1-d407-36b8-84a1-f252baf73eef | -11.42753 | -43.91832 | 2026-08-14 04:34:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e58448ee-d7f8-38bf-9875-84e4433824b5 | -13.25351 | -50.37558 | 2026-08-14 04:34:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fe19b7f-d0aa-3551-87d6-ab0195a1e124 | -18.50401 | -47.01521 | 2026-08-14 04:34:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb2c779b-b819-3e71-b664-cb7c277f9316 | -11.48051 | -54.62514 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eaa42e89-22a3-3bd9-8f5a-b14d406ac12e | -11.318 | -45.21787 | 2026-08-14 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 40867eb4-a89f-39a5-8ec1-852c49bef19a | -18.41759 | -45.19718 | 2026-08-14 04:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98d03120-1fd8-3b87-b79a-1e7d57c8d27d | -14.35648 | -53.08414 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12fd1188-e145-3cee-9e9e-61474bd82e23 | -11.86893 | -51.94343 | 2026-08-14 04:34:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cff417ca-ac98-33c7-84b4-025392f5dab4 | -15.86255 | -43.29595 | 2026-08-14 04:34:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99b84909-7c30-3397-9115-cdd782ffa8a7 | -14.71588 | -52.88217 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95432bb2-3ed0-3ec8-8622-083172a08a4c | -14.43575 | -45.6992 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e53499ae-5919-359a-9c56-c645330462e1 | -14.72061 | -52.87805 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99fdae11-bf48-3946-9fc4-e76d42184db7 | -16.91702 | -54.13577 | 2026-08-14 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0be1aa8-52c6-3a30-8780-25e6c36ed1e4 | -14.07028 | -53.62106 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc6e924c-e536-3982-b3b8-4acd300f4691 | -13.25152 | -54.25143 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1315e415-c71c-3075-bae4-1dda08fd3bab | -15.44638 | -52.99468 | 2026-08-14 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2428554c-9b28-321e-a178-8a083b59108c | -13.27343 | -54.21513 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d205a1df-6e69-3dc5-8cf6-403983ba5d9d | -14.93303 | -46.62804 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 04b3208f-8a09-38bc-91fc-a7bb46b0b7e5 | -14.05411 | -53.64035 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bdac50d-ff7a-3ce0-aa6f-3cbc9f4d593d | -9.96514 | -53.95186 | 2026-08-14 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 323b3da8-7c28-3ec5-862d-65cbd0769b6b | -9.75907 | -60.77209 | 2026-08-14 04:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 077ebb98-0001-30fa-9645-7bb89f44c22d | -12.32913 | -50.86362 | 2026-08-14 04:34:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3f94b6c7-b16a-3e30-b047-997219167106 | -14.7459 | -48.23626 | 2026-08-14 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 688b9931-d829-3a89-a36d-3eb439960ed1 | -14.39459 | -53.16621 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 47d1823e-e3df-39c4-b5cd-092001e8bdce | -13.27543 | -54.22829 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 09cb490e-9d14-3b5e-ab51-a6564564edcf | -14.05751 | -53.64489 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea8b24cf-94b2-389d-b4c9-cda0ad2aa691 | -14.72452 | -47.14954 | 2026-08-14 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 27321e0b-d145-3f92-af70-dc9954b9758a | -10.97112 | -50.53764 | 2026-08-14 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dfe68faf-5ba1-36ae-99ea-0d51d32054f1 | -14.97026 | -46.61371 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30346f70-7654-31d9-92bc-e282a43a0972 | -11.06942 | -50.93929 | 2026-08-14 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 71451e02-8f5e-306d-9091-3abd6f904b38 | -13.7507 | -53.42122 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 832b6fd8-6c91-352f-93a7-146af22c1469 | -12.49136 | -43.77308 | 2026-08-14 04:34:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3c05792a-91ca-3b4a-a307-24897db4de67 | -18.41765 | -45.19501 | 2026-08-14 04:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0fad496e-b927-34d1-998d-21746d1dcf4f | -13.84861 | -53.71329 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74e7fbc4-8f3e-3c49-958d-5cb6cda773f9 | -15.05044 | -46.5214 | 2026-08-14 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f1f2a2e1-6572-3a17-90a8-6af79a68d9ba | -10.97269 | -50.54114 | 2026-08-14 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 071607cc-b950-3f94-9261-777c1314dc88 | -14.44727 | -51.86047 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f34ebca8-3005-316a-bfe8-6f916e9b84bf | -8.89481 | -60.56181 | 2026-08-14 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b16a424e-316a-36bb-8b60-e4ac814e9742 | -14.96152 | -46.60123 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 462b911a-c1f6-3c23-af6d-613b9aaa3960 | -13.86054 | -43.64418 | 2026-08-14 04:34:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f5dca31-5891-3296-87d6-0b94fa0a438a | -22.92317 | -49.20609 | 2026-08-14 04:36:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e96d087-25a1-3327-b40c-039905b7a543 | -23.19119 | -49.15273 | 2026-08-14 04:36:00 | NOAA-20 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 064ca942-c19b-3bb5-bf7e-165f767fad1b | -21.4943 | -48.63519 | 2026-08-14 04:36:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9fb646c2-fd10-3621-b5db-2b9d3c1f44a5 | -22.75639 | -47.07467 | 2026-08-14 04:36:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01e1b6b4-dcea-33f2-a352-8d161e172b90 | -18.47633 | -51.74599 | 2026-08-14 04:36:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9315616f-d3c2-33a8-be14-1ceaddf5c74b | -19.9494 | -45.54975 | 2026-08-14 04:36:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9248b308-1cae-347d-8a0e-eb791b91a4ed | -19.58816 | -46.89634 | 2026-08-14 04:36:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72853d46-4a17-3e9f-96ae-65dd271bc3bf | -20.95861 | -47.20252 | 2026-08-14 04:36:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2f5e679b-2797-306e-82de-ab84f810ba41 | -19.58835 | -46.89959 | 2026-08-14 04:36:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 18e8931c-6495-3497-8aaa-e7b8e442f916 | -19.87238 | -43.23907 | 2026-08-14 04:36:00 | NOAA-20 | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a3676f79-98c3-3b64-a086-8b832ba1eb54 | -20.96778 | -47.41531 | 2026-08-14 04:36:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c638ca5-c4f3-3906-b468-46425d80b3c7 | -22.91924 | -49.2093 | 2026-08-14 04:36:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f0cb87d-1eae-3635-bd87-2158332d304f | -18.68764 | -47.80553 | 2026-08-14 04:36:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6297c4fd-f0ca-3de6-960f-df5d8f6d98c4 | -21.75987 | -44.02762 | 2026-08-14 04:36:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 30781aa0-88fc-3644-9782-d200ef73a9bc | -20.89553 | -50.50821 | 2026-08-14 04:36:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0bd5873d-a83a-3b7b-89e3-acad2a09dea1 | -21.59766 | -43.70436 | 2026-08-14 04:36:00 | NOAA-20 | BIAS FORTES | MINAS GERAIS | Brasil | 3106804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 4c37a65a-2ce9-3d9e-ab7c-158ab2ee31b7 | -22.00618 | -47.21328 | 2026-08-14 04:36:00 | NOAA-20 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7809fc5c-dce7-3a01-9803-a3e61c3500ad | -19.68039 | -45.05759 | 2026-08-14 04:36:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4f63989-fc8d-37a3-b4a5-a6af7fbbc3a0 | -20.26045 | -46.7122 | 2026-08-14 04:36:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3632aa01-4a38-3219-9d92-97071017b186 | -21.89928 | -55.36008 | 2026-08-14 04:36:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 13d22377-6a63-3985-99da-3968c5879f26 | -20.32266 | -42.01915 | 2026-08-14 04:36:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 539a11d8-e637-3786-b433-9bdba285fa75 | -23.08867 | -45.74521 | 2026-08-14 04:36:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e9705185-8121-3f23-b59e-07776291d25c | -20.73504 | -46.99924 | 2026-08-14 04:36:00 | NOAA-20 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5df81f19-47a8-3f79-828e-1aeedd7dfce0 | -21.53841 | -45.6765 | 2026-08-14 04:36:00 | NOAA-20 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| eea7d4cf-b9b3-37cc-8486-4533c2495e32 | -18.54747 | -48.18542 | 2026-08-14 04:36:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 191df8ed-2c4b-3196-9295-9daed5d00a83 | -20.47 | -45.94018 | 2026-08-14 04:36:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f01742b4-0689-31b7-90b7-7af867a5cd8e | -18.47565 | -51.75002 | 2026-08-14 04:36:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b713697a-0567-348f-b54f-08663a8692fc | -18.88706 | -48.58538 | 2026-08-14 04:36:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0ea44bd-f1ca-335c-ab6e-c3f81f78652e | -19.00622 | -46.17528 | 2026-08-14 04:36:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3cfbcd52-6ce8-3129-add7-9de9e4919b27 | -20.26269 | -46.7156 | 2026-08-14 04:36:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a6960ec-f64b-31b7-b63b-94374a58063d | -21.90115 | -55.37185 | 2026-08-14 04:36:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6c7fb2aa-d6f2-3bb9-99a8-89e376e82cea | -21.12221 | -48.91968 | 2026-08-14 04:36:00 | NOAA-20 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8985b416-33ce-32aa-a8b0-3fc81b9bb028 | -21.89716 | -55.37105 | 2026-08-14 04:36:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f67988c5-b451-3e58-b5ca-ab7b850c016e | -18.54803 | -48.18171 | 2026-08-14 04:36:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abe5fe6b-30e8-3de4-bba4-ead7f19aaad4 | -21.49767 | -48.63576 | 2026-08-14 04:36:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a6e8f5d-add8-3fd8-b6b6-84defb3c6f14 | -19.95692 | -45.55091 | 2026-08-14 04:36:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7f034088-c74c-3ccf-95ab-594e971164b5 | -21.90325 | -55.3609 | 2026-08-14 04:36:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0feae76d-76e1-3c4e-8c90-a33756ab3a9c | -19.95756 | -45.54623 | 2026-08-14 04:36:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README27.md)
