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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3ad69a0-2199-3f5b-a2a4-df7013cf5834 | -6.1403 | -57.712799 | 2026-08-09 01:06:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 224b760c-9fff-3a97-886b-c96ca514881a | -6.7164 | -58.924301 | 2026-08-09 01:06:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8c47263-31e7-3ed3-852d-84bba1db02cf | -8.6334 | -66.518799 | 2026-08-09 01:06:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a1e4c9c-ab50-3eb7-bf8a-7e6479eab954 | -6.7016 | -58.9492 | 2026-08-09 01:06:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d5d779d7-8a95-32e9-a303-59ee57c3be24 | -6.8224 | -56.400299 | 2026-08-09 01:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b74703ed-31c2-38c8-944e-576b89e96477 | -20.814699 | -57.696201 | 2026-08-09 01:06:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2b49af4e-3080-3777-9507-7975110eca57 | -8.6479 | -64.102898 | 2026-08-09 01:06:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| decdd463-9296-39c8-8e8d-4156bcf33598 | -13.9547 | -58.1152 | 2026-08-09 01:06:00 | METOP-B | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ec2cdffc-82de-32cd-bb90-91d5b0a85ce4 | -8.6907 | -62.869598 | 2026-08-09 01:06:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 18702758-f0a6-3747-8dea-f2e9935e7613 | -20.445601 | -57.4021 | 2026-08-09 01:06:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a7730dcd-41f1-342b-816a-3e76c014e47a | -13.9429 | -58.108601 | 2026-08-09 01:06:00 | METOP-B | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f63bb6b4-86f9-3434-b3b8-760b97ad11e6 | -6.6992 | -58.939098 | 2026-08-09 01:06:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a1ae09e-c5b2-33f7-80a8-fac25877cfec | -6.1432 | -57.725101 | 2026-08-09 01:06:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 892cf993-f486-3531-9f7e-c48b84444cc2 | -13.9624 | -58.103699 | 2026-08-09 01:06:00 | METOP-B | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1b0d0fb0-2204-352b-b0db-1a7d19921184 | -6.826 | -56.414902 | 2026-08-09 01:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 665d47b9-53cf-3637-978d-a304e820ce82 | -11.9955 | -60.5009 | 2026-08-09 01:06:00 | METOP-B | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8cfbe38e-beb1-3970-a5aa-afaf3ec4191d | -10.0757 | -60.496601 | 2026-08-09 01:06:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14cc14d7-2ada-3556-84c5-c16a41797a26 | -13.9602 | -58.094501 | 2026-08-09 01:06:00 | METOP-B | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 62d58a82-d52a-3d07-8bf4-a1a491650a14 | -6.8127 | -56.402599 | 2026-08-09 01:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5843722-ac20-37f2-9ba2-24186669e017 | -10.0739 | -60.488899 | 2026-08-09 01:06:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50dc278a-7d42-3867-8083-22aa84f3d3b4 | -8.6809 | -62.871899 | 2026-08-09 01:06:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0c9f5630-3d47-33af-87c3-3f8c46f4222f | -6.8286 | -56.383202 | 2026-08-09 01:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd677181-62d2-3991-b9f9-82721fad0b6e | -6.882 | -58.927799 | 2026-08-09 01:06:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e24dcc2-cd52-3974-a76c-4b81073c1410 | -14.0434 | -53.823399 | 2026-08-09 01:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 53d70fd0-4480-32d4-9e19-97072f1e793b | -8.6793 | -62.865002 | 2026-08-09 01:06:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9d8d6aab-694f-3623-bdad-28d57b09f8e7 | -20.8127 | -57.687901 | 2026-08-09 01:06:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cd580e4f-b240-383c-9f1d-c5c380fe9bee | -18.6322 | -49.8433 | 2026-08-09 01:06:00 | METOP-B | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f033898c-7880-38ed-9229-38c52fe58a71 | -6.1306 | -57.715099 | 2026-08-09 01:06:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2aafa4b3-8866-3f43-818a-460c12902917 | -20.455299 | -57.399502 | 2026-08-09 01:06:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 77d3c50d-d245-3d0c-ab79-ba66f74671af | -20.7855 | -57.66 | 2026-08-09 01:06:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c3d62236-a646-3c69-ad33-7975e73ba4e2 | -6.8357 | -56.412498 | 2026-08-09 01:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b6e2f64-d61d-3e9b-90a6-e3695f8c5c4b | -7.3822 | -59.958801 | 2026-08-09 01:06:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 699045e2-4121-3aea-a5ab-87cd0af20a23 | -6.8844 | -58.937801 | 2026-08-09 01:06:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 51bd5b27-620b-3134-86af-e22e1a2a12da | -8.6891 | -62.862701 | 2026-08-09 01:06:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5b9deda9-bbbb-37c7-9638-d25793424edd | -14.0585 | -53.8013 | 2026-08-09 01:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 438b2d39-031e-34f3-8d49-1db28bab29fe | -13.9526 | -58.106098 | 2026-08-09 01:06:00 | METOP-B | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d6c0fadd-4770-38cb-a4ed-137acb97838f | -13.9472 | -58.126801 | 2026-08-09 01:06:00 | METOP-B | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1ea57edd-9e47-3162-8b37-890b48755f57 | -6.8723 | -58.930099 | 2026-08-09 01:06:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 63f6eb36-7506-3944-9d89-ec1d8922544c | -8.6876 | -62.855801 | 2026-08-09 01:06:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a405985d-a020-32e5-b900-43448aaa6adc | -6.8418 | -56.3955 | 2026-08-09 01:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2967d83-5582-3ca6-bc1a-802065e5b1fd | -21.9883 | -56.014702 | 2026-08-09 01:06:00 | METOP-B | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 903efd54-4613-3a68-921c-1ab65cd6758c | -11.4164 | -61.483898 | 2026-08-09 01:06:00 | METOP-B | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 08f66433-9536-3005-aa33-5d3aa8fd52ef | -20.7932 | -57.6931 | 2026-08-09 01:06:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 03032da3-d857-30e7-94f6-4f30fd80997e | -10.9221 | -57.109501 | 2026-08-09 01:06:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14e5fca6-3bfe-3a6a-8357-648c4e5bb050 | -6.1277 | -57.702801 | 2026-08-09 01:06:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2edf16cb-370d-3ffa-ac05-206d6f42ff70 | -18.6227 | -49.846298 | 2026-08-09 01:06:00 | METOP-B | INACIOLÂNDIA | GOIÁS | Brasil | 5209937 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1b03d7e9-134c-3126-a49d-17187ed1d939 | -20.787399 | -57.668301 | 2026-08-09 01:06:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| af876e8d-262d-3d6f-952f-5581f4dc64a0 | -8.6432 | -66.516701 | 2026-08-09 01:06:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 36cb3f53-757e-3409-922c-d06f791f55fa | -7.5477 | -61.1591 | 2026-08-09 01:06:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 25b397e1-f9c7-3588-a10d-da512728df2e | -6.8321 | -56.3979 | 2026-08-09 01:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fea14ffc-a464-33d6-93ac-28ce1f10c7dd | -10.9123 | -57.1119 | 2026-08-09 01:06:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 751d1708-e45a-3c0b-a2b6-45cf8e5cc34d | -9.1441 | -59.6436 | 2026-08-09 01:06:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7311a5f4-c361-3246-bbad-c894fa7a48bf | -6.404 | -55.7789 | 2026-08-09 01:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88482b82-3968-3606-811d-fbf450cc7514 | -9.3345 | -63.444 | 2026-08-09 01:06:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1fe7010e-0a0f-30b1-a689-57a4e9edc618 | -20.4436 | -57.3936 | 2026-08-09 01:06:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d5e66b08-af0a-3664-8620-a5d226da33e0 | -8.6778 | -62.858101 | 2026-08-09 01:06:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| abe1f99e-0929-33a4-adef-f858e31f71b4 | -6.709 | -58.936699 | 2026-08-09 01:06:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9deea773-2830-3809-8a97-72da2c4a0ddb | -8.6352 | -66.527298 | 2026-08-09 01:06:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a2884eac-b616-3040-a048-cd22d0a09279 | -6.8309 | -58.929199 | 2026-08-09 01:06:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b5287293-5b0b-32d0-8e8c-c382eb9c88a7 | -18.6394 | -49.868599 | 2026-08-09 01:06:00 | METOP-B | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 815511e7-bac5-3b68-b27c-2597257e17c3 | -13.9645 | -58.112801 | 2026-08-09 01:06:00 | METOP-B | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b2a9a8b3-294a-3a5c-82df-de298f6e5ecb | -6.7114 | -58.9468 | 2026-08-09 01:06:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ceeb3b65-7b36-3271-a856-fbab6189602e | -7.3842 | -59.967499 | 2026-08-09 01:06:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fd5019cf-ef6c-3da1-b329-71c410780da1 | -18.6299 | -49.871601 | 2026-08-09 01:06:00 | METOP-B | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d1f62396-7037-342c-bf49-b28057b2a1d2 | -8.7232 | -62.8769 | 2026-08-09 01:06:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 70e4f90b-bc14-32bb-a9f7-b672ab945976 | -6.8203 | -56.4155 | 2026-08-09 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 60432b8b-78f1-35ef-bb3b-9c63113d4a63 | -6.8389 | -56.3949 | 2026-08-09 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 3f54e349-10b6-3508-8abe-73cf773ff980 | -6.1476 | -57.7215 | 2026-08-09 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| fb758d44-c917-3d06-b76d-7f14ea1cba0b | -18.6528 | -49.8703 | 2026-08-09 01:10:00 | GOES-19 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.5 |
| b8b3eef2-4a6a-3b33-8363-925d17a9ace5 | -6.8388 | -56.4146 | 2026-08-09 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| c831f305-1793-39e5-8d05-f09e5e7f8dbf | -6.8202 | -56.4353 | 2026-08-09 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 893abb2e-37e6-38db-b2c6-82330d5638af | -6.8573 | -56.4137 | 2026-08-09 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| dd20b872-bae8-31b7-b2fa-07698d8e49b4 | -6.8387 | -56.4344 | 2026-08-09 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 3d21103e-2237-3b75-8bcc-b8fae471c3bf | -6.1476 | -57.7215 | 2026-08-09 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 08abf6e6-e7b2-37af-ac82-fe588f8f9c14 | -19.1128 | -48.3063 | 2026-08-09 01:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 145.0 |
| a37593b4-0c67-344c-960c-6d7e4cfb633b | -18.9769 | -41.1244 | 2026-08-09 01:20:00 | GOES-19 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 99.1 |
| 02e9577b-b09c-3aed-980a-3f12c44f5d21 | -19.1134 | -48.2833 | 2026-08-09 01:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 8583d153-a3ca-3f5b-93ef-cb5f28f60587 | -18.4164 | -50.5824 | 2026-08-09 01:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 119.5 |
| c3676629-e232-3637-b667-6211cdcc31b1 | -18.4359 | -50.601 | 2026-08-09 01:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 97.2 |
| bb5c4171-cb5a-3724-a65d-080b01063c8b | -19.0926 | -48.3106 | 2026-08-09 01:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 8ac422cb-3b48-3406-9bea-8715e6d2744f | -18.6327 | -49.8742 | 2026-08-09 01:20:00 | GOES-19 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.4 |
| c59cb474-85e2-378a-a75d-cf31861f9a22 | -18.4159 | -50.6047 | 2026-08-09 01:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 214.0 |
| 45d8ef33-138f-3d1c-b0a5-bfdfeecbd79b | -18.4364 | -50.5788 | 2026-08-09 01:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 64.6 |
| 0facfe61-540b-33ed-b098-edbda12e8914 | -18.4154 | -50.6269 | 2026-08-09 01:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 70.2 |
| f585b1e8-f664-37fb-b455-eb51536502d9 | -19.0926 | -48.3106 | 2026-08-09 01:30:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 78a7d07d-a4f8-35ba-bedf-7d59f965bf25 | -19.1128 | -48.3063 | 2026-08-09 01:30:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 5f729447-114d-3404-ad3e-3e1e43e4c444 | -6.1476 | -57.7215 | 2026-08-09 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 1c7935e6-6d2e-3920-be17-f347f36a6355 | -7.5537 | -61.151901 | 2026-08-09 01:30:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 35951e64-ebb2-33ab-b973-304b3dd03d0a | -6.8253 | -56.444801 | 2026-08-09 01:30:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc018490-f9db-384b-89a2-f92958909185 | -6.1444 | -57.7033 | 2026-08-09 01:30:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5adb8008-6ba4-30fc-8be8-d3251dd25d4f | -6.1465 | -57.712299 | 2026-08-09 01:30:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddb5b37b-7e45-310c-80b8-623eea4a1ddd | -6.7122 | -58.9356 | 2026-08-09 01:30:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 102cc4e0-a664-3f55-b8ea-041f4ef646b5 | -20.818001 | -57.702 | 2026-08-09 01:30:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7ff5e1a1-55e4-3233-a1c8-e34a4d439d5b | -6.722 | -58.9333 | 2026-08-09 01:30:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d23134cd-ed48-3174-b719-9bfc70d9e3c2 | -7.3853 | -59.967602 | 2026-08-09 01:30:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ffe1ae22-bcc0-3b85-9231-2493bf355fa2 | -6.7141 | -58.943298 | 2026-08-09 01:30:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 340883aa-d496-3fed-88cd-c3a542ca3781 | -8.6358 | -66.522003 | 2026-08-09 01:30:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 073fdc17-064f-3845-8f8e-98bcd8afce9e | -6.8516 | -56.382702 | 2026-08-09 01:30:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce15c0ea-5f7f-34b2-9e52-e3c1fbdf1ad8 | -14.1721 | -53.994202 | 2026-08-09 01:30:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 039c82d9-5c23-3cfb-b157-2c178e856dbb | -8.691 | -62.8643 | 2026-08-09 01:30:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
