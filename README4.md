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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f20cab9-8618-3d5e-ac67-de224ee9b183 | -19.62988 | -56.97405 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3921d089-8e31-36df-9845-7f9d3cefe904 | -19.38211 | -55.27388 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 882b9688-0951-3527-8cd7-a962e3a4662f | -19.67613 | -56.98639 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6bccd002-c4b4-33c1-918d-80b8ca588002 | -16.12321 | -56.84234 | 2026-01-22 04:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b6c316a-ecb3-3fd8-b97d-66a56a3ab9a0 | -20.34583 | -57.88012 | 2026-01-22 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f8079ab2-b614-35dc-bd4f-40c51b44b58f | -15.23754 | -60.01621 | 2026-01-22 04:55:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8319fbf5-3bec-37ba-9c35-da520b14fb24 | -15.52095 | -57.49609 | 2026-01-22 04:55:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bf9b9ff-c418-3c43-99ce-b6e009b8b90e | -20.3124 | -57.87069 | 2026-01-22 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5648557c-ebfc-3004-bc34-2054fdb16faa | -20.3158 | -57.87134 | 2026-01-22 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5a95bc5a-7402-3210-a1d7-98f121ee231c | -20.10206 | -51.24058 | 2026-01-22 04:55:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 733529f6-2ca1-30d2-b2e6-d95362e7b12c | -19.18707 | -51.40004 | 2026-01-22 04:55:00 | NOAA-20 | LAGOA SANTA | GOIÁS | Brasil | 5212253 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c7e5175-0ef2-322f-b236-b1fe19470684 | -19.34611 | -54.1742 | 2026-01-22 04:55:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce481d05-15a4-3e93-8699-660ab820ca9a | -15.03153 | -57.63927 | 2026-01-22 04:55:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa141f25-da4d-3a32-92f6-fa6d601715ac | -19.6659 | -56.88071 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 3671773d-2cfc-3bde-b948-2def5c262a20 | -19.65065 | -56.93168 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7f00f436-d11f-3d63-965f-2f5d42f02129 | -18.2991 | -54.57368 | 2026-01-22 04:55:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0381e69f-7764-35da-889e-f45ef91f89e9 | -20.3567 | -57.87815 | 2026-01-22 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b0312840-ba0e-3147-8137-1915b320a98c | -19.32301 | -54.02489 | 2026-01-22 04:55:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fd01519d-c135-3ffa-889e-42b0acc6e1a6 | -20.32261 | -57.87264 | 2026-01-22 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2ddd02a4-cb24-3ff5-8d0f-8a1c175bad24 | -19.62592 | -56.97718 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 09388bdd-e5cc-38d4-a484-ba1519149f7c | -19.65003 | -56.93541 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| c2702150-0103-37ae-9efe-6501612b73af | -19.68199 | -56.88749 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| bfc2878d-a982-3aff-a8fa-4fa9b006d7bc | -19.66924 | -56.88132 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| dac79182-8cbc-3b3b-9862-1567e42b4d69 | -15.67887 | -56.10914 | 2026-01-22 04:55:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3cdc427-9657-3f88-876f-8c9f2140f062 | -20.35395 | -57.87362 | 2026-01-22 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3e656e58-298e-3a07-92df-650b6484f174 | -18.02771 | -53.68148 | 2026-01-22 04:55:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0261e36e-bcea-3f52-acba-38c2ad1db9c6 | -19.6473 | -56.93107 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3314d6e0-3bdd-3514-a1b8-24b9a831ed79 | -20.32196 | -57.87654 | 2026-01-22 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b3846ee0-1f43-37ed-9c59-330711a2cf1e | -19.66759 | -56.99638 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6320b943-1fd6-310a-a323-e5b5b0dc1cb8 | -18.18786 | -54.47979 | 2026-01-22 04:55:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2180aaa5-ce9a-307c-b121-0aec452771cf | -19.62927 | -56.97779 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 9bfe1666-5e9b-3345-a2f4-1518ec38c7d1 | -20.91139 | -56.38636 | 2026-01-22 04:55:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ae7b287e-1190-319f-bca3-d3f29f59853f | -19.66698 | -57.00011 | 2026-01-22 04:55:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d2971936-c56b-3de6-84ad-6da377094c31 | -21.94435 | -52.91247 | 2026-01-22 04:57:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fbc2f4b0-3690-3b9e-9f69-179be614f54b | -22.73058 | -49.34788 | 2026-01-22 04:57:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34d7cc40-3980-35db-90ed-4e14564e9739 | -22.01926 | -56.33831 | 2026-01-22 04:57:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c89285b4-67df-34b5-8187-69e0813eb4cc | -23.14265 | -49.06451 | 2026-01-22 04:57:00 | NOAA-20 | ARANDU | SÃO PAULO | Brasil | 3503109 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c02cc48-777a-33e9-bce5-4ff74fb11a39 | -21.20086 | -56.93289 | 2026-01-22 04:57:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4060492a-3875-33ce-8d37-160b40c8008e | -21.44378 | -54.57508 | 2026-01-22 04:57:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6027f8cc-9a11-3384-a88b-f5bd0c2a41d9 | -22.64597 | -51.05185 | 2026-01-22 04:57:00 | NOAA-20 | IEPÊ | SÃO PAULO | Brasil | 3519907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8e9525b9-345d-3180-9d93-543c411afe5f | -22.03174 | -56.30237 | 2026-01-22 04:57:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6cb3c9d-ca35-3265-9407-2abcfa760fba | -21.19421 | -56.93167 | 2026-01-22 04:57:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c989a12-b89b-3517-8ed6-c256fd76b460 | -26.97782 | -52.52914 | 2026-01-22 04:57:00 | NOAA-20 | XAXIM | SANTA CATARINA | Brasil | 4219705 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 67df4f96-4f67-34bd-9487-7395278c01e4 | -21.19753 | -56.93228 | 2026-01-22 04:57:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc9e637d-2c24-3d1d-af0a-d324a194648a | -21.44038 | -54.57452 | 2026-01-22 04:57:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 850b724e-c328-3836-98b1-feb01de25571 | -21.94499 | -52.90786 | 2026-01-22 04:57:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 131ccc59-ae3c-376b-9486-0e523330ce81 | -22.02316 | -56.33519 | 2026-01-22 04:57:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a18d8b5-9a97-30d0-8af7-b5754627779b | -30.90332 | -52.96341 | 2026-01-22 04:59:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| a1698bb6-502a-3018-ab06-4c01a4bd24e0 | -30.1722 | -55.29851 | 2026-01-22 04:59:00 | NOAA-20 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| d81a103e-1f33-36f7-a2c9-d19eace4ef6f | -30.89928 | -52.96264 | 2026-01-22 04:59:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 60b12e79-36b5-3d71-b13c-e7d6a2f7245b | 3.8657 | -60.95595 | 2026-01-22 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 941f1a10-9aac-3c13-a913-ea4a57a19733 | -9.68296 | -35.85967 | 2026-01-22 05:40:00 | AQUA_M-M | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 6009bf1b-c776-3ac4-a1c7-62429a470e4b | -9.67303 | -35.85828 | 2026-01-22 05:40:00 | AQUA_M-M | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 60797bdb-b9f0-31d6-8d0b-b97670b39172 | -20.32702 | -55.92579 | 2026-01-22 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| aa8e30b1-89e5-3b77-a203-8e15c0832042 | -19.68283 | -56.88589 | 2026-01-22 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 2a03e43b-a8dc-3bbc-8a7b-af596ffbcb54 | -19.64803 | -56.93064 | 2026-01-22 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 9c1ec614-c099-31ce-ba44-ec650176ab69 | -19.63848 | -56.9683 | 2026-01-22 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2c580bd1-89bd-3b9d-9f76-ed5edba12249 | -20.31897 | -57.86966 | 2026-01-22 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| bd2d8448-da8b-3a00-8cfd-aaf64eec84fd | -19.66501 | -56.87899 | 2026-01-22 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 846ef52a-bc3f-3ae6-8c24-4ddc79a712ae | -20.35318 | -57.87792 | 2026-01-22 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| df70880a-47b5-388c-9631-1a8eee49d90f | -20.32652 | -55.93151 | 2026-01-22 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f5361c4a-ab68-3770-b81f-0f94055c1370 | -19.67348 | -56.98671 | 2026-01-22 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b2727355-c291-35ed-a251-da8c03b2d9a3 | -19.67304 | -56.99147 | 2026-01-22 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0b0bb795-f931-3b9e-9caf-d4c79b907eea | -20.32434 | -57.87459 | 2026-01-22 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| fb2c009a-53b7-3499-8b65-fbd483ac6dc1 | -19.6711 | -56.8797 | 2026-01-22 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ed884f72-d42e-3508-9fc5-c76d6ef03bcb | -20.3128 | -57.87325 | 2026-01-22 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 13ca3bf6-ea9f-352f-8359-07a6642d43b1 | -20.31857 | -57.87392 | 2026-01-22 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 9d66e796-1cb1-3a84-acc6-e273bcf4568d | -20.34164 | -57.87658 | 2026-01-22 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 0b24e51d-8128-30da-82f6-4c029ec9832d | -20.35426 | -57.87273 | 2026-01-22 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4061a923-a015-3df3-b33c-4683ef482156 | -20.30663 | -57.87684 | 2026-01-22 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 90c3560b-87a1-36aa-9b66-fdef18228e84 | -19.63892 | -56.96352 | 2026-01-22 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 32d67fc5-41b9-3a0a-af39-34b0bc69f895 | -20.35359 | -57.87365 | 2026-01-22 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 07dc8f3c-25e0-36a9-aa4c-ee0738f4fa25 | -20.35927 | -57.88193 | 2026-01-22 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 48eb4309-65e3-3006-b846-068951d63e87 | -19.67719 | -56.88037 | 2026-01-22 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 0b35ca7e-5b05-30c2-9af6-2884d5b388a7 | -20.32681 | -55.93055 | 2026-01-22 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 18aabb0b-891a-38a4-a357-3e071304545e | -19.68328 | -56.88105 | 2026-01-22 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 26b53952-fe8d-39ec-bc68-4b94f2c87d82 | -20.35895 | -57.87858 | 2026-01-22 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e6c4d5da-b485-3a43-817a-d522e759fd4e | -19.67953 | -56.98741 | 2026-01-22 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 775aa59c-1a97-3947-a5c1-bedb2f16adfc | -20.35965 | -57.87768 | 2026-01-22 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 70aca02c-c295-31cc-bafb-008e0a6adc7f | -20.35388 | -57.877 | 2026-01-22 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8ab5f55a-f6c4-38aa-86f0-9556d0802bb4 | -19.66457 | -56.88383 | 2026-01-22 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e7961040-e23f-3125-9986-f08be51db1d5 | -20.30703 | -57.87258 | 2026-01-22 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 12a62871-6a1e-3d60-9b7f-f4332ae7555f | -20.34811 | -57.87631 | 2026-01-22 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 458d581b-b774-31f7-b4c2-e284503d4292 | -20.34741 | -57.87725 | 2026-01-22 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 409a242c-e395-306a-a3c8-3e753e32301f | -19.32685 | -54.02888 | 2026-01-22 05:46:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 76736e3c-fe49-3cdf-a736-25fae194c28f | -20.90733 | -56.38926 | 2026-01-22 05:48:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98ec6cef-3ad4-366f-ab12-76f5dde4272e | -20.90777 | -56.38371 | 2026-01-22 05:48:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f277ec2d-4e79-3518-ba2e-615c5f8bc07b | -20.9141 | -56.38468 | 2026-01-22 05:48:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 265f1fc3-244c-3775-8a77-c6ce89f0da9c | -21.19859 | -56.93079 | 2026-01-22 05:48:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d66bacec-3594-3631-b452-ece323a1d936 | -20.91128 | -56.39038 | 2026-01-22 05:48:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 28cbf901-47c8-372b-92cd-fa8d48519094 | -20.91175 | -56.38491 | 2026-01-22 05:48:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b87c349f-7ddb-3712-a4c8-fa6813e9ca16 | -21.19818 | -56.93004 | 2026-01-22 05:48:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2fbe3fa3-470e-35e4-86ad-fd6aa0ccb9e8 | -2.44046 | -44.93174 | 2026-01-22 12:12:00 | TERRA_M-T | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 17.5 |
| d87ffc5c-2a76-30a1-80b5-226b1a54711f | -6.02556 | -40.1102 | 2026-01-22 12:14:00 | TERRA_M-T | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 58.4 |
| db35401c-8021-3057-98aa-dbe1261de298 | -6.02745 | -40.10349 | 2026-01-22 12:14:00 | TERRA_M-T | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 80.1 |
| f388c57c-0f7f-31e4-8aa1-994e1af27a9e | -18.94737 | -53.42422 | 2026-01-22 12:16:00 | TERRA_M-T | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e5ad201d-3ea6-3201-b72c-eb52ca7aa00c | -19.67633 | -56.877 | 2026-01-22 12:16:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 40.7 |
| e1cda3b1-5d6c-32cb-8fb3-331c8c77b55f | -27.9411 | -52.92412 | 2026-01-22 12:18:00 | TERRA_M-T | SARANDI | RIO GRANDE DO SUL | Brasil | 4320107 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| a3d0b911-e1c1-3552-a686-d949353d7eae | -23.03315 | -52.25661 | 2026-01-22 12:18:00 | TERRA_M-T | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| 8e59a0d7-4b0f-3d18-8e76-4a469ed2f1c7 | -27.31079 | -49.96684 | 2026-01-22 12:18:00 | TERRA_M-T | POUSO REDONDO | SANTA CATARINA | Brasil | 4213708 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |


[Clique aqui para ver as próximas entradas](README5.md)
