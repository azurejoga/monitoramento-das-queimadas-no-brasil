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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29f66d0d-8254-36e9-bf13-ba7f8fe572dc | -13.09078 | -47.30849 | 2025-07-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a42faedb-5381-337e-b36d-3ae6c19ced10 | -13.00961 | -44.89062 | 2025-07-29 05:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a80446c-f633-34de-aa48-0e7b194b6fcb | -13.48099 | -45.59626 | 2025-07-29 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2407ac8-edcd-3f43-be49-ddf612e49523 | -14.3755 | -50.32649 | 2025-07-29 05:12:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffb9a180-9319-3c21-b2bb-6e200dcfd9f6 | -15.12795 | -45.33129 | 2025-07-29 05:12:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43ca8b24-f7b1-3550-b48b-8a96c4166afb | -13.11892 | -47.38207 | 2025-07-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1fb0bf73-0fe9-3b57-bf1f-f97eb2f4d321 | -14.50534 | -46.54792 | 2025-07-29 05:12:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c49f545b-f7f4-3ae3-9eda-623c61e56f20 | -14.49936 | -46.54099 | 2025-07-29 05:12:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 455dc012-b338-329f-944e-7e1ea069d371 | -11.64235 | -55.68584 | 2025-07-29 05:12:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b862eaa1-9774-3e27-b333-cbecceb9e5b9 | -14.37843 | -59.344 | 2025-07-29 05:12:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2217adde-f2c6-3243-8ba5-fdd6e6a3368e | -12.99805 | -44.90369 | 2025-07-29 05:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 265922fa-683c-37cf-81a4-791720a05462 | -10.7469 | -58.00799 | 2025-07-29 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 433ca837-3b8c-3628-9e0b-8496a94a7c60 | -14.50598 | -46.54199 | 2025-07-29 05:12:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3d8fbd2-4fd2-3cda-a963-9dab7f664b13 | -14.50378 | -46.54052 | 2025-07-29 05:12:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7b3e049-7511-33d2-bd5d-f936d70e416f | -14.37512 | -59.34346 | 2025-07-29 05:12:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61be9bc0-b137-3f2c-bb2f-0a1435d25401 | -14.35639 | -59.33307 | 2025-07-29 05:12:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 88a5dbc8-391f-3e89-8496-370e6306cb28 | -11.99552 | -46.97538 | 2025-07-29 05:12:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 013486b3-5662-32c9-8a6a-f9a22b90e787 | -14.32187 | -54.15826 | 2025-07-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3ebefb0-64ae-3621-9b24-4bb7e86549cb | -13.00312 | -44.88293 | 2025-07-29 05:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fe524060-0b67-3002-8594-8a2c9fc4a44b | -14.32253 | -54.15792 | 2025-07-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8608d92-c99c-3369-8406-4ba92065189b | -13.00162 | -44.89754 | 2025-07-29 05:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3d4e52d-c5b6-3f99-ae78-76c7f2a409ca | -13.01038 | -44.8832 | 2025-07-29 05:12:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07a49255-bf18-3838-a162-4eb23ee083e8 | -11.99871 | -46.97419 | 2025-07-29 05:12:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 788b554a-57cd-36dc-831c-def8fc083169 | -12.27819 | -63.80571 | 2025-07-29 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5e4141c-a0b8-3668-9681-58f71affb191 | -10.74745 | -58.00448 | 2025-07-29 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d531e180-5568-3687-8f92-8dfc2dee02fd | -14.87921 | -48.39519 | 2025-07-29 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cfd543f0-aba1-3f0e-a2f3-1db9b3f2150f | -20.29257 | -54.07609 | 2025-07-29 05:14:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5bae16d9-b487-3dcc-a0b1-6984b2e4aee0 | -18.44689 | -54.65921 | 2025-07-29 05:14:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d1a46517-5334-3c5f-93e3-82ad2236c699 | -21.33731 | -55.63272 | 2025-07-29 05:14:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f20ad0d-4f48-3444-bb5a-44d6fc18dd50 | -18.45103 | -54.65979 | 2025-07-29 05:14:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2a24bdf5-014e-335d-8d46-78c5b50b4ba6 | -18.44792 | -54.65131 | 2025-07-29 05:14:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c925d5b-5fc5-3bde-85d1-7197a3487f73 | -18.44637 | -54.66318 | 2025-07-29 05:14:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 88e0b790-5211-36d7-9dc2-1aa9de0979ac | -20.29312 | -54.07146 | 2025-07-29 05:14:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b72ca3b-44a9-3857-adf0-caa89a029725 | -18.45051 | -54.66377 | 2025-07-29 05:14:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 65166df7-3f03-3714-9c19-45ed7b798870 | -18.44741 | -54.65524 | 2025-07-29 05:14:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 542ec2d5-c2f6-352b-a767-fe0b727285fc | -21.77533 | -52.75046 | 2025-07-29 05:14:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ef2b652-4eb3-38e9-8d34-57624ea0db11 | -20.29754 | -54.07201 | 2025-07-29 05:14:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f04d99b1-b07a-3911-a961-c875ba791b36 | -18.44999 | -54.66774 | 2025-07-29 05:14:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 94d8439a-99d9-3c9f-8c7d-ce10d55a5eb8 | -21.33326 | -55.63216 | 2025-07-29 05:14:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06e5c387-66b5-33b8-a5a9-3f6ed8bbbbbf | -18.44585 | -54.66716 | 2025-07-29 05:14:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dbf420da-c4d7-3771-a7c1-234901100513 | -18.45155 | -54.65582 | 2025-07-29 05:14:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1530c007-a3ac-335a-b887-ce153dbe938d | -20.29698 | -54.07666 | 2025-07-29 05:14:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f4e4293-7ec5-3483-8bf3-40fee8bc74a0 | -21.77833 | -52.75003 | 2025-07-29 05:14:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b37db5b-6f59-31f9-8f0c-a9e209e4796b | -21.33684 | -55.63641 | 2025-07-29 05:14:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac8aff22-1a67-3c0b-9918-2ba9aaaba32c | -11.4197 | -45.1412 | 2025-07-29 05:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| ba94cbb7-aeb7-3dc5-8a9d-ca5bc2340c8d | -11.4201 | -45.1181 | 2025-07-29 05:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| f4c75981-16fe-3567-ba26-14158d13bf4d | -11.4393 | -45.1154 | 2025-07-29 05:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 02f6385a-b39b-3d3b-a76b-04779a235845 | -11.4389 | -45.1385 | 2025-07-29 05:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 11cf0ab6-f27d-3cd4-97b6-d6e227d9fabc | -11.4393 | -45.1154 | 2025-07-29 05:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| a4f9d8dd-75af-359b-a72e-0463bd64310d | -11.4389 | -45.1385 | 2025-07-29 05:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| d67e4ec8-8175-3958-b669-114a99072d3c | -11.4197 | -45.1412 | 2025-07-29 05:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 251e6523-d3a0-34cf-8dd6-8c3df4bdcacf | -11.4201 | -45.1181 | 2025-07-29 05:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 7ddaf4a2-9324-3d4b-a180-e8869f37d7a1 | -18.4486 | -54.6674 | 2025-07-29 05:40:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 5754ab01-6ba3-350f-a93f-29ad7e104649 | -11.4393 | -45.1154 | 2025-07-29 05:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 1e9cf201-151e-3d7c-a422-9fb66c3cfb69 | -11.4389 | -45.1385 | 2025-07-29 05:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| c152c295-53c3-3571-894d-7f8b2d10f573 | -11.4201 | -45.1181 | 2025-07-29 05:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| f21fb6f8-4277-3787-a566-5da3dbf60a39 | -11.4197 | -45.1412 | 2025-07-29 05:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 5e2601ee-4906-385e-bb59-1c0ddfa781c7 | -11.4393 | -45.1154 | 2025-07-29 05:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 5d1300aa-7ee4-38dc-81ff-227ea4198d8b | -11.4393 | -45.1154 | 2025-07-29 06:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| fee94e4a-261f-34e3-b234-cdfba432fe24 | -11.4201 | -45.1181 | 2025-07-29 06:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| fb09bb91-2e0a-393b-a5db-2cf95421ec34 | -11.4389 | -45.1385 | 2025-07-29 06:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| eaf85263-874d-319d-8270-1b21b4f9bf4a | -14.3988 | -59.3316 | 2025-07-29 06:00:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| d952a7bf-35a1-38fc-a822-cb9afbe92e30 | -6.17639 | -58.07395 | 2025-07-29 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf1f3e96-5e30-3bd1-82b4-9e35003071e3 | -6.17733 | -58.0715 | 2025-07-29 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 297f0fe3-2a1a-3024-a8c3-1ec4b5b8908b | -14.40087 | -59.32738 | 2025-07-29 06:03:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3f95dce1-d52a-3a23-a3f0-cf1e1085be23 | -14.39904 | -59.32889 | 2025-07-29 06:03:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dfc1f097-f76f-3901-964e-3a3228828f14 | -11.4201 | -45.1181 | 2025-07-29 06:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 1a8d828e-e7bd-3522-a616-a97d54d53a2c | -11.4393 | -45.1154 | 2025-07-29 06:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 9339d26f-da54-344c-8647-7a8c1f29ebb1 | -14.3988 | -59.3316 | 2025-07-29 06:10:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 94c76869-d0c7-3864-aec6-2517053511bb | -14.3988 | -59.3316 | 2025-07-29 06:20:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 5226a0ac-11f9-33aa-9fee-b32b9eb3033a | -14.418 | -59.33 | 2025-07-29 06:20:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 2a5b5f06-9502-34a3-b1ef-9c4c2ae6f728 | -11.4197 | -45.1412 | 2025-07-29 06:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 263868c8-981d-3853-8886-e5b384db5450 | -18.4486 | -54.6674 | 2025-07-29 06:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 0739c056-8b9a-3ae1-a2fe-3f7ecbc250c4 | -11.4393 | -45.1154 | 2025-07-29 06:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 80dbc383-9953-3b32-ba60-4dec751e3f09 | -11.4201 | -45.1181 | 2025-07-29 06:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 5f032280-e9dc-35b1-9101-b9f421642404 | -2.89764 | -48.26808 | 2025-07-29 06:29:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 7ba9b5f7-4092-32e8-a1ba-dd5508bdf039 | -2.89108 | -48.28902 | 2025-07-29 06:29:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 8c08ab24-9a99-32fd-9399-9f9720824b13 | -2.89395 | -48.29432 | 2025-07-29 06:29:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 8aa6c9f7-3be8-38a8-a737-7f7c54ef6050 | -11.4393 | -45.1154 | 2025-07-29 06:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 809c5ffc-973c-39c8-90f6-3f73687a8f8a | -11.4389 | -45.1385 | 2025-07-29 06:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| d90e629a-b964-3307-801f-bc8333e4e3bb | -11.4201 | -45.1181 | 2025-07-29 06:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 88c481c4-e380-339d-abcd-4f71cb3465ad | -6.49795 | -56.2132 | 2025-07-29 06:31:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| bad1d0b5-2421-3fc6-bfa5-dd7221e8559d | -6.49929 | -56.20427 | 2025-07-29 06:31:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4377e1b7-0f7b-3eeb-8bdd-fe56ffa5da51 | -6.4891 | -56.21189 | 2025-07-29 06:31:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 05f65e81-7f40-352c-b21d-1f12dc678f1f | -6.49043 | -56.20298 | 2025-07-29 06:31:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 52d956b9-9874-3f80-9019-be9ace12378a | -6.51857 | -56.21297 | 2025-07-29 06:31:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 818e6949-a195-3c53-9af8-72935d14502c | -14.3541 | -59.32875 | 2025-07-29 06:33:00 | AQUA_M-M | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7e1d7333-f64e-36b4-adb3-d130dc248843 | -14.39245 | -59.33127 | 2025-07-29 06:33:00 | AQUA_M-M | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3d8b1e47-6ec0-315f-88d1-fe2272e49dcb | -18.43312 | -54.65626 | 2025-07-29 06:35:00 | AQUA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 4bf0056a-02b3-33b1-8392-826b8abd10a4 | -18.44242 | -54.67338 | 2025-07-29 06:35:00 | AQUA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 7797f993-1f18-3330-8e6d-da15dfabb381 | -18.44432 | -54.65778 | 2025-07-29 06:35:00 | AQUA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 0989ed57-64a6-36aa-abc7-5af366df11a0 | -11.4201 | -45.1181 | 2025-07-29 06:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 80d5de05-04eb-3114-8963-7816eeffe9bf | -18.4486 | -54.6674 | 2025-07-29 06:40:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 52.9 |
| fd728f6a-21a8-3d86-9e5b-dde5baec456f | -11.4393 | -45.1154 | 2025-07-29 06:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| e7d757db-6c65-32b4-a5c8-59685b6f76ad | -11.4389 | -45.1385 | 2025-07-29 06:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 7d6b61d9-d099-3819-8b84-a42b6c6bca8d | -11.4393 | -45.1154 | 2025-07-29 06:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| a7e8e47b-b82f-30f0-94ea-291295a38237 | -18.4486 | -54.6674 | 2025-07-29 06:50:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 093076e9-c3bb-3215-b3da-32d7ccef2c6d | -11.4201 | -45.1181 | 2025-07-29 06:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| ee18acd2-e06d-3415-a327-e7cc151665c5 | -11.4389 | -45.1385 | 2025-07-29 07:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 35b2f52c-a522-35fa-b911-372db6940199 | -11.4393 | -45.1154 | 2025-07-29 07:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |


[Clique aqui para ver as próximas entradas](README24.md)
