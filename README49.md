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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44e8bfed-c236-3506-9410-e9cdb6411002 | -9.69094 | -47.05339 | 2025-08-30 04:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e51e2bc-bef0-39f4-911e-4d5bddf00709 | -11.34172 | -43.52707 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33c591c5-cc97-3575-8655-0a4da32d98c6 | -11.73591 | -51.75281 | 2025-08-30 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 048e5757-f7d8-397b-af26-ae096f113a2f | -11.33633 | -43.2843 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 974b350e-bad1-32d4-ae4d-a9c51d330cc6 | -11.06885 | -52.03945 | 2025-08-30 04:49:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42a5faff-9f4a-33a9-8c1d-498be1207fd7 | -9.46601 | -62.33539 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| af302324-ba71-32cb-8b6a-1171c3bb07ea | -10.36917 | -59.20351 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5993d81-b80b-3240-ae94-e1a7ed2bd893 | -8.4627 | -43.63612 | 2025-08-30 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 920e6b69-3c6c-3ca6-91e5-94b845dbfbf6 | -11.83802 | -46.44628 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a334b767-bd2b-3633-bca4-78636b5d6ab4 | -8.24137 | -47.2013 | 2025-08-30 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bbb35df1-823a-38b5-9f57-370d0a983db0 | -10.37049 | -57.82375 | 2025-08-30 04:49:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43b54f43-6525-3bc6-bcf0-1bd37cc6beca | -11.29879 | -43.57744 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25130656-f789-3ef9-9265-2e926720cf31 | -11.58248 | -46.36871 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 345510da-9969-3be2-8beb-a8510e29817a | -9.44822 | -60.54416 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0417597e-883d-3996-8b0f-3d92ced5cdc6 | -7.60197 | -42.71847 | 2025-08-30 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 55b44613-7825-3237-b0fd-670a16bd2a8e | -11.35531 | -43.58189 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d694f831-9422-3034-bfb2-046051b3310f | -11.32549 | -43.61145 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2702c9d5-a886-3742-95b7-57116950f437 | -7.62509 | -42.66564 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a9b49c75-41b1-3cee-9bc9-2301e0ce7a2d | -9.43661 | -60.54866 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bc675277-597d-3093-9e20-e4802637fb0f | -9.17448 | -59.57713 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 563942df-fa21-3c85-b672-ca50b817eda4 | -9.43895 | -60.56564 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| be1820e6-f350-3ab7-9d9b-4217f9902a83 | -9.44261 | -62.33073 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aaa8e4ea-86ac-3a81-bb01-eddb14112181 | -10.02415 | -46.02862 | 2025-08-30 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cbcca0a-15df-348f-bbee-b0948bdc53c6 | -6.8825 | -44.44188 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f2c372b-c892-3f70-a5b5-6b341f1c6e8a | -10.44299 | -51.35529 | 2025-08-30 04:49:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 957dbdc8-7ac5-3d48-87fb-ee74e456386d | -9.22136 | -60.86974 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5198690c-d2d9-3bf9-8590-11a43a65f66f | -9.44928 | -62.32762 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 1df59b7b-4c15-31eb-a459-08a642ac0333 | -10.37331 | -57.83264 | 2025-08-30 04:49:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa497232-e569-36e7-981e-30e7d6b85a39 | -6.07585 | -57.93264 | 2025-08-30 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06eddd61-f202-3937-96aa-3fbaa0b3cb90 | -11.35797 | -43.57932 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30285cab-b7c9-340c-8750-fab41f4c5025 | -8.87707 | -60.73301 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| defbf867-8885-35fb-bf26-76cc4c4b573f | -11.35951 | -43.56697 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7abd6f06-4760-3baa-868a-1bdcce53f170 | -11.83113 | -46.86501 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5ef34393-1d8f-3c1c-a0f5-caf409f1f976 | -8.55711 | -63.0311 | 2025-08-30 04:49:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dd38598c-6fd1-33f4-99f5-96808c365112 | -8.68259 | -50.40768 | 2025-08-30 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5a6668a-a8bc-3e0f-8398-c34664c661c3 | -6.80397 | -59.96679 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9c3e949-dde4-3cf1-b06d-f15aea4517e8 | -7.60497 | -42.73435 | 2025-08-30 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f2151173-590b-3957-97b5-16f6346366e1 | -7.12038 | -44.59888 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| edc90c72-6794-332f-a608-32c67455d8b9 | -11.33797 | -43.59525 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64dde115-8be1-3742-9491-ffd8e130aef2 | -11.83629 | -46.45342 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3c21732e-1f4b-3a0c-a603-1fac1b6797c5 | -8.88485 | -60.7335 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 380809a2-d2d1-3713-9719-e213ac426132 | -9.45032 | -60.56135 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34704a5e-27e8-33cb-81f7-52f3df604223 | -11.82573 | -46.47237 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 8cc20b3a-5502-340c-9777-9b1b9706feb3 | -11.86695 | -46.44961 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c9de9883-c2cf-306f-96b7-a83d71616772 | -9.45856 | -62.34259 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 11488325-36a9-3542-b974-f3bd8ec02271 | -8.6692 | -62.43576 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5d00605-4d80-31c8-898a-f81111d14899 | -9.6491 | -48.33591 | 2025-08-30 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d5cb3943-8d0e-3866-b534-82a7ffb162d7 | -11.30165 | -43.63557 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba9afc20-c9b6-3257-85f4-278c26ce37a4 | -11.33591 | -43.28758 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a879e026-5273-3145-8624-8dabd1820b89 | -11.86593 | -46.42535 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| adc23094-2769-35b0-9f5c-19b8bdffbc3a | -7.40728 | -44.29152 | 2025-08-30 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 106bf225-b796-3341-89b2-877ad0d6e820 | -7.39777 | -45.93085 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 38d76523-822d-3f84-b822-cccd17947053 | -9.12503 | -65.814 | 2025-08-30 04:49:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a06ce90f-641e-365e-b197-d041a75d9a8f | -9.78425 | -64.24474 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1fd39c9-9732-3b37-a8ce-446abcfaaef9 | -11.07662 | -52.03349 | 2025-08-30 04:49:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41baf45e-4b5e-31d3-8d65-c1e4900ebf4a | -8.11264 | -45.0034 | 2025-08-30 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7467380-9658-3ede-84af-8ff44f67ad3f | -11.83216 | -46.45731 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| a14f02d5-4835-33b3-87fa-33db3ed0d7ec | -11.32038 | -43.65042 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6d48015-fc6e-3d00-bae3-958cf1ec4339 | -11.84103 | -46.45014 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c33491bd-bd66-3417-a901-91904ee18ea9 | -7.16928 | -44.162 | 2025-08-30 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c56b8cc9-9963-3362-9e62-011f5cae5918 | -11.88349 | -46.39149 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 63602570-10da-3064-8390-df14a432121f | -7.11719 | -44.58936 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd360528-e2d8-3386-a17f-acf030020a85 | -11.32154 | -43.64162 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c17d1fa7-8e70-3b6e-91e0-06ef32c57319 | -8.5956 | -60.58311 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 938a0109-50b6-3a60-8f7f-f9dfbd306087 | -11.82995 | -46.47292 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 85184cb8-1626-3414-b99e-3a89bf8d8e47 | -10.67793 | -47.06795 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a11aecda-deac-3f9d-a367-53df491adefb | -11.86638 | -46.3901 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c31b850a-ef98-3047-b4ba-8d5ba010a5e8 | -11.77829 | -47.55656 | 2025-08-30 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f27a8020-6001-39a4-89b8-3f380ceb6a2d | -9.31794 | -40.21421 | 2025-08-30 04:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5b0205e4-a7a9-3ef2-a43a-08d29c385b5b | -9.105 | -65.7645 | 2025-08-30 04:49:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 5b27ef74-b89e-3322-883e-686f76df6a81 | -9.76786 | -64.25894 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6430084-83dc-3ef1-963f-19253c024bd7 | -8.55219 | -51.30952 | 2025-08-30 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8457b294-afdf-3da1-bceb-24f6f691169d | -11.84244 | -46.38426 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 98907f6b-4489-39a5-b7d2-639cce195634 | -11.32393 | -43.62336 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c4b7ef94-9561-3ace-93e1-397c6a280de3 | -7.60752 | -42.71614 | 2025-08-30 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c087c1d9-eabf-3f37-bd0b-16e0c34a0473 | -5.72571 | -51.68316 | 2025-08-30 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24234f22-efe9-3e4f-9979-426f95c190ed | -9.28001 | -60.46302 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72a42361-0173-3d67-856b-3b50957a225d | -12.39241 | -46.4332 | 2025-08-30 04:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b0caac0-3050-3a2e-a6d9-55e68690bf1c | -9.57574 | -54.48116 | 2025-08-30 04:49:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ec2f96e-477b-3a9e-8c64-ed500c31fa62 | -7.76807 | -45.46373 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 13635066-456a-327b-a913-52ddac98499d | -11.33718 | -43.60132 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0f60462-4e66-35fb-8843-8c375dd28319 | -9.4481 | -60.54437 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 39c3468f-ec5f-3d64-ac41-a8dcdc2d0166 | -9.65878 | -54.43689 | 2025-08-30 04:49:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 948bb4d6-8344-3fd9-abd4-74765eb5d546 | -9.44099 | -62.3391 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ae6f1e3f-e272-36bd-b0c0-8e7d368e3c49 | -7.7243 | -50.26683 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f62ecbba-4c61-3182-9719-19ea6b017bd9 | -12.37342 | -46.39057 | 2025-08-30 04:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cbfe964d-875b-3797-bbcd-14df53c7e0a5 | -9.63299 | -48.29964 | 2025-08-30 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67a325ac-a52a-3933-b2af-4702b382dc9c | -8.55883 | -51.31059 | 2025-08-30 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 96e023e7-b731-3f86-900c-8b15d1369210 | -11.07717 | -52.02998 | 2025-08-30 04:49:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08a09dd8-76f6-391a-a4b6-96be308bf9ad | -11.22522 | -45.02253 | 2025-08-30 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e779027e-0d96-3f0b-a362-63c642a96ccc | -8.17723 | -61.38115 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7335d84a-dfaf-37df-bc50-b4980282a59d | -8.50982 | -54.71719 | 2025-08-30 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a44ad09-7a09-3a38-94a8-369afc31db6a | -9.70441 | -49.46783 | 2025-08-30 04:49:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8771d487-2bc7-3639-8269-d269b7878bd7 | -7.77291 | -45.46039 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f559aca6-29d4-30bd-8a2a-5ed82d6006ae | -11.35937 | -43.55123 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 309b6b71-c3c7-3f1b-b3c3-ca62ea2ee0a1 | -11.22313 | -45.00298 | 2025-08-30 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 841752a3-8691-3a44-a160-93a2886775d1 | -9.94055 | -46.35071 | 2025-08-30 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1799a8e-624d-3c1a-8f9f-a1fbb7f5282d | -11.22398 | -45.03172 | 2025-08-30 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd4197ef-5340-39f9-b455-7f4c11f3e9d9 | -7.57901 | -45.13609 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9118e409-a0ad-30ca-8539-48d2ffdb32b2 | -7.17475 | -44.86932 | 2025-08-30 04:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README50.md)
