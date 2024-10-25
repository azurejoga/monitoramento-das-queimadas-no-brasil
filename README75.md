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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3feec93-62ab-3939-878b-321b128137e7 | -17.21122 | -56.67577 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f62bdd86-c1ac-3729-89bb-9ded122b6c17 | -17.20822 | -56.66978 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2d8219ae-a55e-3da1-bd8e-9fdeb685c26f | -18.33566 | -56.23236 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| b3628733-5975-3cdb-89c5-0ec19f3108b5 | -18.33103 | -56.2364 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 79d0864a-5afc-33ee-8064-5e4e99960463 | -18.32316 | -56.21503 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| afcc38f2-245d-3a1c-b8ac-55818fbd7210 | -18.32249 | -56.17545 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 84835493-f627-3d98-9d56-6071cba470cc | -18.31886 | -56.23894 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 90684755-dc2e-3af5-ab24-1bbcebdd1a0e | -18.30378 | -56.23597 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 12a9d4f5-9d32-3afb-8f94-d6f7b9151a22 | -18.26319 | -56.0289 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f8f4c267-4125-382d-8d19-435504a21d0f | -18.32641 | -56.24044 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| b084ef14-5ced-32a3-b9c0-370a879570ca | -18.3223 | -56.21981 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 0b49e87b-bcdf-359d-ae99-db1da514eb19 | -18.32178 | -56.24448 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| f0adbb08-7bec-33dc-93c6-4cd4ce733a95 | -18.32163 | -56.1802 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 8d4621f7-e92f-3e9d-b87b-66332d76e151 | -18.31854 | -56.21907 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 4f6356ee-9da0-3aa2-a8d9-035aeff0e861 | -18.31787 | -56.17946 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| bf3de92c-c899-3c13-a8c3-6d069cb55e07 | -18.31682 | -56.22863 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8863e03c-9b69-37cd-9f7c-1cad5786f601 | -18.30746 | -56.17248 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| a525cf9f-c6a9-35fd-be92-456489fa0bad | -18.30261 | -56.22087 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 07053431-63a5-36d0-a4d3-673f805073ce | -18.30174 | -56.22565 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.6 |
| 6449511f-4dbd-3dae-b917-1f2b030d9a1b | -18.29884 | -56.22012 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| a37f4381-22f7-312a-be39-4cae01b8b746 | -18.29594 | -56.2146 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 0aa526de-0a63-37b1-b64d-74a08314dbcf | -18.26402 | -56.02422 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 878e928b-4f77-38e8-9d46-00e93a953471 | -18.34078 | -56.20372 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 317599ed-c18f-3032-a63d-cc466fccbf15 | -18.33189 | -56.23162 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 9a0ea292-2491-31ac-b663-1b79d4d26d3d | -18.32264 | -56.23969 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 376a42fa-c2de-301c-873a-2ff0b4b1a00e | -18.31596 | -56.23341 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| b114e9bd-736c-38e0-8555-22865c49e57a | -18.31121 | -56.17323 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| b8e55214-f80d-3d72-95f4-e6fe6e8d30a5 | -18.31046 | -56.24224 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| cd3d2a4b-b3b5-3195-b869-5c8885d7483f | -18.30669 | -56.2415 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 25f0ef64-057f-393f-a3f1-5aba7201a2c2 | -18.32726 | -56.23565 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 8b4476a1-0d4b-37a8-bb70-4684c4f10359 | -18.31801 | -56.24373 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| b47a6c5a-0692-36ce-95c4-8afb112c7c22 | -18.31423 | -56.24299 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| fa85d6f2-b400-3012-b2c6-d5995356a8e9 | -18.3096 | -56.24704 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 321e57f3-84cc-3ff4-88ef-73aae683af2d | -18.3066 | -56.17724 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| d803be77-e46a-36bd-994c-6b282899511d | -18.30582 | -56.2463 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| df900632-d93b-3326-8e42-b4740acba2aa | -18.30284 | -56.17649 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 03ffd503-6409-3bab-9d98-020f28d8957c | -16.60179 | -57.07165 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 16ad4000-590a-3ef9-a7b2-1a8ed844ce99 | -16.60111 | -57.0754 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0cb9c8ab-b532-3ba0-b922-eaef6760e0fb | -16.6009 | -57.07201 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b782c10b-b537-39e5-b02e-3abf95cd64dd | -16.60518 | -57.07621 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 098230e9-c452-3723-bb55-9309a3e246e6 | -16.60497 | -57.07281 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d9a580b2-f204-3db6-a290-f4448cb6023f | -16.60427 | -57.07655 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7939a1f9-113f-3d87-aa46-6ea8a8145e03 | -16.6002 | -57.07574 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a7849d4f-5b53-398f-a3db-c0b048b569b3 | -17.78106 | -57.37313 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 78839259-63a8-3478-b7f2-e78623ff3fb2 | -17.76412 | -57.37357 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| f0fa2a62-d417-3e97-98fd-24542cc27b9a | -17.70303 | -57.4838 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 76b32f53-a6b8-3fb0-bcba-f00c26e17bf9 | -17.69617 | -57.33738 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| b92b1e7f-1a9c-3787-ac69-6deb037ce712 | -17.69142 | -57.34029 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| cac6911a-f874-372e-9f3f-077e03497f8a | -17.67917 | -57.47496 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 74637708-13ab-3951-834e-5ca066507809 | -17.67099 | -57.47327 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 7b9397e4-a777-3e6a-8c53-482c430f9b1f | -17.66226 | -57.45175 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 2fb6c1b6-4da8-3a73-8764-5f9cd2c0aaf5 | -17.66013 | -57.46315 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| bb67a897-3409-3fce-a815-24edb55ae1d7 | -17.29298 | -57.28493 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 13f0f2cb-58ef-3c9d-81a2-17c65381d6ef | -17.28207 | -57.29834 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a9fcc112-188f-3549-8394-2db87a1bfc6a | -17.27799 | -57.29752 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6ece327a-5bbb-3e51-85b9-ec39bd6a2ccb | -17.27202 | -57.26121 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 33cdafaf-506b-3e5d-8e86-551a07f1a794 | -17.26122 | -57.50442 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| afa91663-0437-38f3-a698-da295e53ae8a | -17.26051 | -57.50829 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 9932bece-596d-30a2-bc6e-b338b14e1fd3 | -17.25638 | -57.50745 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| ef500923-5c8f-390d-a476-4fca3031f2bc | -17.25597 | -57.21144 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8933b843-0ef1-3109-9d8e-0b744e654dc4 | -17.25225 | -57.50661 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 0e77aac1-1f64-3f77-bfb4-f567251c52d1 | -17.25154 | -57.51049 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 1b5d6efa-2450-3606-947f-f598cfe5e109 | -17.24883 | -57.50188 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| b237e9c9-af07-310e-b7b1-f8d3bd6f36ef | -17.23219 | -57.22599 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 949044f6-865b-327a-8865-d95b622c59cb | -17.23149 | -57.22973 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| dc9902e5-c349-303c-840b-1e78cb5bf8ed | -17.22819 | -57.22972 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 09c2fea4-f043-3760-aeb8-efb8d0216210 | -17.22798 | -57.24842 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a1738778-9e7c-3354-ac32-c58ec9f22d0b | -17.22751 | -57.23346 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 61ccb4b5-f4b1-3594-90c0-a972c45b4337 | -17.22684 | -57.23721 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| cfca5e59-d4d0-3156-bb6e-f462a7138516 | -17.22673 | -57.23264 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 2a49ea41-19a1-3f1b-be3a-9604561958cb | -17.22616 | -57.24095 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 2cfb26ce-89d5-358f-801e-4a1c46c5b1fb | -17.2255 | -57.48908 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ac75f699-9d27-3d76-b733-97a0cad6761c | -17.22548 | -57.24469 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| c261fd90-f294-3cb6-8a97-60563508ae91 | -17.22532 | -57.24012 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 4c92e427-87e7-3dcd-b5d6-8fde90d27f6d | -17.22478 | -57.49296 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ab6fcc5b-2374-3ffc-8c41-f1269352c5dd | -17.22405 | -57.49684 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6f006601-9f1a-319e-a756-a553867e09c6 | -17.22392 | -57.2476 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e63ddace-c135-3691-a5c7-e6be2f24357b | -17.22333 | -57.50072 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 760073e2-b6e4-3890-b944-bb533a9467d1 | -17.22281 | -57.4805 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| e8eef774-f44f-3902-b655-d9c8c4a950c1 | -17.2221 | -57.48437 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 06280c66-1fc6-31cc-aa5d-3b1ca382a7c9 | -17.22196 | -57.23556 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 11c2b93e-45e8-3ad9-bb79-e18e8afd4a53 | -17.22137 | -57.48824 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 5a108a65-03a5-3a1f-93df-b666272aaa43 | -17.22055 | -57.24303 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 3cc21c60-7024-30b1-be73-505d8467e8c7 | -17.21985 | -57.24678 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c9b36727-7856-3381-bb4a-8a2a6c2037de | -17.21667 | -57.24681 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 645d7b58-17d8-313e-81d0-eda8495435f6 | -17.21652 | -57.49128 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 4c92b6b3-1fe1-3ca6-8c66-8f53d18d31ec | -17.21598 | -57.25056 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1def57a6-980c-30cb-bc1b-7d278feef3cc | -17.21384 | -57.4827 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| d1f77065-ce23-3101-9d57-9de31224c782 | -17.20971 | -57.48186 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 0c76e81d-c727-39bf-b16a-286b0485929c | -17.20558 | -57.48103 | 2024-10-25 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5b7e2372-a177-3674-9123-42543061dc3e | -17.19283 | -57.28493 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 4789e0e2-ab8b-3d6b-b0bc-abce6102477c | -17.19214 | -57.28871 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 043fe95c-2382-36ec-aef9-730e084b1d19 | -17.19145 | -57.29249 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6b59aaea-1e39-394e-b4aa-547fd4860da9 | -17.18806 | -57.28788 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1bc6b184-ac59-3761-aa93-898785fae0cd | -17.18668 | -57.29544 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d9853ba3-281c-37ac-87d9-5bf8cd6e9fa9 | -17.1823 | -56.74604 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 13fd93dd-3915-3a53-897d-a3608340c0aa | -17.17835 | -56.74525 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 468f43e3-3d8b-3de8-ad99-a95459717bef | -17.17563 | -56.78304 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6659fddf-bc29-3a95-8f4f-efffe9d6f913 | -17.17072 | -56.78754 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1e64127b-e847-3bb1-80f5-4dc21e63e3b3 | -17.1635 | -56.73685 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |


[Clique aqui para ver as próximas entradas](README76.md)
