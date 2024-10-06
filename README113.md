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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42941123-c77f-325c-99ee-3362562433f0 | -18.63977 | -57.27434 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 7a6aa0b2-22fd-3735-9173-d20d49eb308d | -18.63917 | -57.27855 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 0b77c2b7-874f-31d4-bcfd-bc179a0af810 | -18.63857 | -57.28276 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| f168c5ce-8f8d-3e07-8e56-4bc97e9f8278 | -18.63622 | -57.27379 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 5d69d3c7-8134-384d-a9ec-d65b31b0e1bb | -18.63562 | -57.278 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 093abc86-39a2-360b-a8eb-0e32731e56d6 | -18.63502 | -57.28221 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 7ed279ac-26e6-3eee-a26e-4f87d82c40e0 | -21.31494 | -47.6089 | 2024-10-06 05:14:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 97700b37-eb53-31a6-bd59-f875865359b0 | -16.52828 | -47.03378 | 2024-10-06 05:14:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bdd33ebc-e585-30ab-8e4f-310abb24aa90 | -16.52764 | -47.03289 | 2024-10-06 05:14:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3b020f77-423f-3fb8-8513-3cb4c9243570 | -16.52227 | -47.0277 | 2024-10-06 05:14:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6bfbba7a-ddce-31e0-9906-2448c9676952 | -16.5216 | -47.02669 | 2024-10-06 05:14:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b41790bf-c9d6-3e8e-9c32-7c1973a4d15d | -16.20806 | -48.71229 | 2024-10-06 05:14:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f87034d-44d6-39c6-9ac2-971afbbeec09 | -16.20216 | -48.71184 | 2024-10-06 05:14:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea61973f-1030-317f-b559-8d7e3fb1dea2 | -16.47387 | -49.94065 | 2024-10-06 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be832c49-8fd4-3d7f-b0cf-2847cff284f0 | -16.47347 | -49.94433 | 2024-10-06 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 003991fa-75e2-3f1c-8e04-a09d5ff2b84d | -15.89891 | -46.87819 | 2024-10-06 05:14:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 11d6f2e7-d4d0-34e1-aa26-69b66030e455 | -15.89792 | -46.87725 | 2024-10-06 05:14:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b0f4594-8619-305f-a240-cfc04aaea1db | -14.20394 | -46.45326 | 2024-10-06 05:14:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 349b054f-b2d6-3215-a616-0558d39d27df | -14.09498 | -45.51639 | 2024-10-06 05:14:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7ba2012b-eb2a-3899-a5d3-57f613cf0644 | -14.09432 | -45.52294 | 2024-10-06 05:14:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 648576da-b997-3156-9b09-f6dfb36a9dbf | -16.95293 | -47.1254 | 2024-10-06 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ac0e53e-273c-3933-80ee-13d28e5d0bda | -16.9159 | -47.17342 | 2024-10-06 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c9866dfa-71e0-3253-bdc2-52fd7af5d717 | -16.91534 | -47.17928 | 2024-10-06 05:14:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5665b0fb-ec9a-3b40-9ccf-2e5713af3729 | -16.91095 | -47.15634 | 2024-10-06 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9edb7d92-7fab-3af6-885e-91eee0bcb2fe | -16.91046 | -47.16152 | 2024-10-06 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5fd72705-3ce3-317c-9818-0504c8c794c1 | -16.90992 | -47.16715 | 2024-10-06 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7b1eeda0-70b3-3ede-8934-8c10597bc750 | -16.90337 | -47.16674 | 2024-10-06 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 64777930-4a58-3388-a6e3-be31595e1f12 | -14.70294 | -45.13163 | 2024-10-06 05:14:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ea9cf7f2-f5fd-3590-8e76-d8ab5e0525a1 | -14.6997 | -45.1284 | 2024-10-06 05:14:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fcdf2803-1765-392e-a364-90559465e89c | -14.69904 | -45.13514 | 2024-10-06 05:14:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| faefbf88-7a7b-357f-af22-3e589241b62d | -14.69576 | -45.13102 | 2024-10-06 05:14:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e3bf6831-2f9a-3202-ad95-ba40155937cb | -17.63099 | -46.96595 | 2024-10-06 05:14:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b9c6bf05-a740-34c5-b0a6-b587665b501c | -14.55845 | -48.81957 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 72667cec-f896-390e-8351-3ec188ee77e6 | -14.55804 | -48.8233 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1a9a817a-0cd2-3905-a1dc-2001222e4f43 | -14.55717 | -48.81413 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 51defb1c-f6af-3561-bae1-7125204c7e87 | -14.55673 | -48.81797 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 973e2a42-1c70-3e06-9931-e2cc088b5ded | -14.55629 | -48.82176 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ff20001a-18c3-3400-8889-d926825616b5 | -14.55586 | -48.8255 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7cf912f4-e2cd-33e3-95ac-187dd324ceb2 | -14.55361 | -48.81059 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 83aaedb7-33ee-3278-8dda-0fa90dd167f9 | -14.5532 | -48.81441 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 644d71db-ba0d-3c16-be8b-0375cdeee6a1 | -14.55283 | -48.80143 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aac3e21a-f9d6-3bf5-97a9-572827e39868 | -14.55238 | -48.80532 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 558eef67-7edd-3678-a110-3ac45d26eaab | -14.55237 | -48.8221 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| accf66dd-6673-3d89-8d9c-a3122f9fcc3d | -14.55195 | -48.82595 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a9a5eb97-458f-32c4-8050-aa0b9db2f47b | -14.55194 | -48.80908 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 19659f6b-586a-35e2-b60e-465d407bd177 | -14.55151 | -48.81285 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b127395-0c1c-3c01-8e0f-771e832604ac | -14.55062 | -48.82054 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f4186e90-1f6f-3542-88e3-fa70f05e0780 | -14.55018 | -48.82439 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 34f99937-fc0e-3a44-b9cb-d838ee8ffa61 | -14.55016 | -48.78865 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df69b306-1aab-3ce8-b572-654c270f66ac | -14.54916 | -48.79803 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e51f5250-57ec-35e0-8b86-488f5fed0d93 | -14.54875 | -48.80184 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a93b796a-736d-39c7-bfc6-3f89923c537c | -14.54757 | -48.79664 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3d33dfde-0779-3d97-b818-be795c3a4972 | -14.54713 | -48.80042 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d410f52b-e6af-3b56-9b9e-41ab286ba0b0 | -14.54442 | -48.78801 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e275f298-f0fa-324f-a451-cf948a2316ca | -14.54343 | -48.79727 | 2024-10-06 05:14:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12088afb-d449-348c-bbaa-6fd4fc2527e3 | -20.46231 | -51.27884 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 33b0ba13-aa3b-3065-8671-3e52af439184 | -20.46209 | -51.28022 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 95f5ae34-7f52-3f64-9bb4-d0724647b384 | -20.46197 | -51.28231 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 4df0329b-a969-3bfe-8c9a-08ea066a0701 | -20.46172 | -51.28371 | 2024-10-06 05:14:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| a598d9fa-2296-3f03-876e-49ef4fd73158 | -10.57794 | -69.06326 | 2024-10-06 05:14:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e1a1277-8414-319a-9217-a60080e298d0 | -10.57711 | -69.0675 | 2024-10-06 05:14:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e2be089-887d-3858-ab7c-faba032d3e83 | -10.92447 | -68.24302 | 2024-10-06 05:14:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 450b2d4a-cee7-3fb1-acff-fb043096ecda | -10.90595 | -68.28114 | 2024-10-06 05:14:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5cfd43d-723d-3dd9-abaa-f30f5d3b081a | -10.90569 | -68.28268 | 2024-10-06 05:14:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd09346c-b120-3e69-8360-a8100c56cf0d | -19.83207 | -46.44258 | 2024-10-06 05:14:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1afb4acb-06bd-3f64-b40e-5c6df482f378 | -19.83155 | -46.4491 | 2024-10-06 05:14:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| acfc1285-5a49-3a10-915f-5be1d9aebf04 | -19.83117 | -46.4397 | 2024-10-06 05:14:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 18b34528-efed-3ca3-8e8f-7f9cbd3df2bc | -19.8307 | -46.44611 | 2024-10-06 05:14:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9901afbc-da87-3661-a454-0684b8acc07b | -14.09 | -45.49552 | 2024-10-06 05:14:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ebeffb21-514f-310c-bb6d-ce904344717c | -14.08934 | -45.50219 | 2024-10-06 05:14:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0b67b335-fbe3-349c-a389-4877932fb3cb | -14.08913 | -45.57511 | 2024-10-06 05:14:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cf36a244-7e62-37b2-8738-86a606d8b1bf | -14.0887 | -45.50865 | 2024-10-06 05:14:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b0803296-432f-3f18-a12f-cdf4e62aeb2e | -14.08846 | -45.58179 | 2024-10-06 05:14:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e1a5a045-21de-3c59-9d7b-f9c16d0679c0 | -14.08806 | -45.51511 | 2024-10-06 05:14:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f7b4812e-f060-3c8c-b535-2a8f022d57b4 | -14.08779 | -45.5885 | 2024-10-06 05:14:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bd8772da-5884-388d-b497-116e0a03a697 | -14.08741 | -45.52168 | 2024-10-06 05:14:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 42dcc07c-308f-3ce9-a0a0-0ce520e32943 | -14.0837 | -45.48797 | 2024-10-06 05:14:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a3883b02-ca82-3e08-85cf-932a2ea4f44c | -14.08303 | -45.49469 | 2024-10-06 05:14:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 88d5f4ac-1586-374d-a955-d6a57c924db6 | -14.07674 | -45.48697 | 2024-10-06 05:14:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 59ad07b4-58f6-3f86-ad8d-c308b27c0457 | -19.07224 | -47.01108 | 2024-10-06 05:14:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 621d76e6-d79f-36aa-8323-14510a897d1d | -20.5302 | -47.49315 | 2024-10-06 05:14:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ee7c5bcf-1f44-3b4d-be89-50a621c4ef72 | -20.52969 | -47.49947 | 2024-10-06 05:14:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 128d7170-81fa-3c02-a98b-b76fdc735816 | -20.52353 | -47.49284 | 2024-10-06 05:14:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 27ac4b9e-9455-3271-a6e6-5f672ef189b3 | -20.52304 | -47.49901 | 2024-10-06 05:14:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 878c7126-a3bb-37cf-9435-edd7b4c21de5 | -20.51737 | -47.48627 | 2024-10-06 05:14:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| cc741868-474c-377c-8d60-d241938edd6e | -20.51688 | -47.49246 | 2024-10-06 05:14:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 76217317-57f2-3392-8236-ae993845628d | -20.51286 | -47.48734 | 2024-10-06 05:14:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ba48289e-6b4f-3b7c-9831-35874640b69f | -20.51234 | -47.49343 | 2024-10-06 05:14:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4d2c3a81-ee9f-3e12-bf88-5e758ff34092 | -15.16165 | -47.0799 | 2024-10-06 05:14:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49b90e56-2ef0-304a-aab0-aa28bcd655cc | -15.16119 | -47.08446 | 2024-10-06 05:14:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2214216-8b4f-3638-a8a6-e3a698f5b9f9 | -15.16023 | -47.07841 | 2024-10-06 05:14:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d62fb22-11d6-36a3-8e1b-49bf7d782e72 | -15.15973 | -47.08316 | 2024-10-06 05:14:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 09525ec5-d0ab-3e5c-a9d7-259ad9c41567 | -15.44123 | -47.70308 | 2024-10-06 05:14:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a122f30-8777-3954-bcb0-f9c3152ac289 | -15.43445 | -47.70802 | 2024-10-06 05:14:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7036cc8-c230-3150-af12-d25facd94e12 | -15.43392 | -47.71323 | 2024-10-06 05:14:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9bfae3ee-5dc1-3672-971b-818f2408defb | -15.26426 | -47.49117 | 2024-10-06 05:14:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bcc49c7b-0c52-3104-a93f-8924d5e30d31 | -15.25797 | -47.49063 | 2024-10-06 05:14:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3ec52df-f68a-32de-b72d-20ad6abb324c | -15.15799 | -48.04319 | 2024-10-06 05:14:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bb69e8e9-7888-3cf8-887a-c47348da1796 | -15.15755 | -48.04754 | 2024-10-06 05:14:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d446d3a3-7363-32fc-88ff-0df9bf5ac9eb | -15.15668 | -48.04222 | 2024-10-06 05:14:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README114.md)
