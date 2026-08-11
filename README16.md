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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d54917e2-8e51-3190-a791-477da665f38d | -10.10669 | -46.1991 | 2026-08-11 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f472c00f-c1e1-3505-b661-f02e94d2ce51 | -13.56736 | -46.29102 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| e7d1865f-67a5-33ec-8817-3050eb008fbd | -8.89993 | -60.55898 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 997940ef-1b2c-3b44-82af-9c91701cedd4 | -13.60918 | -46.23807 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 343985a1-f6f0-3513-adae-61f8b596d4a4 | -9.63701 | -45.51102 | 2026-08-11 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4bd5cadf-cdf2-31f1-86de-fef369ab93fc | -9.1502 | -50.9027 | 2026-08-11 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15353b97-e224-3054-8581-bf11aaf6d7dc | -13.56067 | -46.31178 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6850bc45-9cd8-382e-8e7c-ec1e2a2f9218 | -11.45775 | -46.67439 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3c4ecdd5-d9c8-3177-8d51-261b70d19f52 | -13.64842 | -46.24911 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fdff745-0b55-3ab1-905e-92b0145982f4 | -7.62582 | -42.77109 | 2026-08-11 04:34:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f05c9e36-e65c-3cc9-a8c5-80373bd894de | -11.23107 | -54.85295 | 2026-08-11 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3611c0b9-5349-362b-a30e-be954f7ddf21 | -11.19248 | -54.85021 | 2026-08-11 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3973f5a4-0127-30b3-acb7-6fe86eef0fe7 | -12.47657 | -45.32299 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 83819748-4a34-3346-961a-eb416e3cb055 | -11.95319 | -46.33383 | 2026-08-11 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 95010eaf-a62e-3e80-bde2-6b9f1dd14232 | -13.59531 | -46.25136 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 475ca0d2-5c17-3e2a-87f0-365a13b4f6f5 | -8.95752 | -60.54453 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0a3bc796-223d-39fa-aecb-89a593f53444 | -12.46334 | -45.33518 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7090c5ad-cde3-3c0e-b4ff-60d2df5c4a68 | -10.60588 | -50.60999 | 2026-08-11 04:34:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5af527e-7765-3db3-99e4-44d616f5b134 | -13.56859 | -46.28249 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 207af99a-7df6-3ec9-94a0-e8ce9aabd421 | -8.89703 | -60.57451 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 82b5df9d-7e43-3f29-8174-ccc25a45549f | -9.47159 | -60.53172 | 2026-08-11 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 79bb1282-8462-3fa2-9474-e89be60fda14 | -11.29158 | -44.87693 | 2026-08-11 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e39525d5-fd5e-3b73-8c8a-19737f17439f | -7.918 | -49.07362 | 2026-08-11 04:34:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eab2a4f7-917b-3bab-b955-aaaff4b6edd3 | -10.41673 | -46.67574 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1b4815e-4402-306d-9fb5-8e76028bb2b2 | -12.45712 | -45.3247 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2a107ad-8922-3e83-aed9-37c7d137cfdb | -10.42066 | -46.64923 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 863bf9b6-1e36-3292-bbdf-b22017540855 | -11.3114 | -45.22426 | 2026-08-11 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 450b4c41-75bf-3624-8b13-6fe6d61d85c7 | -10.22052 | -45.79456 | 2026-08-11 04:34:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f55b2a4a-f37d-3ed2-a0c7-148b64acda03 | -8.95558 | -60.55469 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 73f9e74b-e281-31bb-8ab8-4e060b55ad84 | -12.55815 | -48.35406 | 2026-08-11 04:34:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1618dabe-a95b-3d07-b03f-9de1084f03ef | -10.42307 | -46.68062 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1fce53c3-2add-3e51-a603-f5260752724c | -9.47257 | -60.52663 | 2026-08-11 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5c51905a-ebd5-36c7-b1af-1e18f074535d | -8.9041 | -60.58307 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1430dcb0-10c2-3250-a84c-32bf01272551 | -7.59588 | -42.77401 | 2026-08-11 04:34:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ba63e341-c3b1-332f-a727-96094b06e72c | -8.9425 | -60.52018 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 41feba26-d662-3f55-b428-387ffc419039 | -11.46412 | -46.65551 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eba287e2-bc04-3dde-adf8-7b20bf89779c | -6.95659 | -42.00036 | 2026-08-11 04:34:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f2a8f6da-56d6-3e40-93ad-8b2da42555eb | -7.61549 | -42.78456 | 2026-08-11 04:34:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 25df626a-d53f-3bd9-820d-c5992d9ae3ff | -11.47983 | -46.62196 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 96703b75-bc45-384e-8fb1-f0b0fdf7c855 | -6.30966 | -51.13177 | 2026-08-11 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f76e1d16-c31c-33de-a73c-97f1c6e2d88f | -8.89573 | -60.59224 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ed008001-1a62-328b-b7f9-adbdb62416b3 | -9.06904 | -49.49716 | 2026-08-11 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea86c2ee-e321-3be9-a22d-c89bdc368c05 | -10.23896 | -45.81844 | 2026-08-11 04:34:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f3f28fab-3450-342a-8e4c-6cfd502e2b52 | -8.94645 | -60.49963 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d49a09a3-bc82-3f18-bf2b-bd8f56e80c2f | -14.73086 | -56.35636 | 2026-08-11 04:36:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74e223e2-fc8d-3b61-aa24-f598e6b0054c | -14.76078 | -56.3661 | 2026-08-11 04:36:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0495ec8f-9142-3de3-95b9-8888ddc1cb4c | -14.28052 | -45.31277 | 2026-08-11 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31465adb-6e3f-31ab-9c86-e17563056dc1 | -14.25614 | -51.96445 | 2026-08-11 04:36:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d280d84-5826-3b62-8d0f-a731e2a21e45 | -17.89186 | -44.47077 | 2026-08-11 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2365e9da-6cb3-3178-b614-f0abade59b03 | -14.00354 | -53.97902 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f65b6bb-242d-3908-8129-2211955ff321 | -15.04624 | -46.5281 | 2026-08-11 04:36:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2b89a2b-a994-3d2b-b0f6-33445e525c04 | -17.1404 | -51.65514 | 2026-08-11 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 511abf6f-6c64-3fcc-a50a-bf2afa2e75ec | -15.77684 | -48.71449 | 2026-08-11 04:36:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 658a04b8-75bb-3cc2-9f25-f5434981b048 | -15.02253 | -46.56444 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 649b93f5-348e-3d6c-ae75-f1b3aaa8c9c4 | -14.45825 | -45.68231 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f47998e0-3d6c-3a80-8343-95a21c48f024 | -14.45447 | -45.68175 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 84dbcbd4-d06a-319d-8684-c007c68ba02e | -14.125 | -45.63577 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| dc63ef1a-ed72-3dad-abb8-6659d57dcf97 | -13.8639 | -53.80001 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d89405c3-afbc-3c7e-bad6-211a4360c083 | -18.4285 | -45.49463 | 2026-08-11 04:36:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d8ee268d-eed1-3a6c-936c-1daae59c2630 | -15.03879 | -46.58048 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f409fa88-8538-35b2-9256-656e001c007d | -14.31263 | -54.91766 | 2026-08-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f14a05a-b855-3ece-ae10-1d13f34cd257 | -16.66063 | -43.63877 | 2026-08-11 04:36:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 23.4 |
| f148cf59-2b27-328d-aa53-a62c09cdcfa9 | -13.43691 | -57.03712 | 2026-08-11 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8a94117-8da5-32c7-a265-ae3d518ae851 | -15.03397 | -46.58829 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 660e237a-d167-32ba-a5e7-e4cd54507c18 | -17.73085 | -46.21817 | 2026-08-11 04:36:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 87194c06-bc9f-3258-8c1f-fb64bc34c2bc | -15.0219 | -46.59504 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e7a7f89-0a02-3e25-9761-052ceb8328bb | -15.00073 | -46.58775 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff417974-7e47-3845-8fdc-ea099aeeb227 | -14.25334 | -51.95997 | 2026-08-11 04:36:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11dbb4c4-91c2-3a27-8aaa-15243e8f2050 | -14.65551 | -47.6554 | 2026-08-11 04:36:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f2c5143-052a-35d7-b8cc-28b336467d17 | -14.467 | -45.70292 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| afd4228c-38ae-37d6-a6d3-afc61cb4e46a | -14.4469 | -45.68063 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dfd1ddff-6a46-3e5a-b90a-77c9b0f6c25a | -17.45674 | -47.14486 | 2026-08-11 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3768bf4-954f-3ebd-947a-f96bb0cbb562 | -14.63601 | -47.66821 | 2026-08-11 04:36:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66fc8c6c-f5c5-30e4-b2fc-b834bad1e5ee | -15.10378 | -44.98562 | 2026-08-11 04:36:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27eea747-63b5-3122-a69f-db6a001fa15e | -14.73168 | -56.35192 | 2026-08-11 04:36:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94b08a73-b2cb-3bc1-bf75-8734341f3106 | -14.46009 | -45.69707 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5ace8c53-c695-3029-b259-10135b7e9f7c | -13.51013 | -51.79884 | 2026-08-11 04:36:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 62af2f6e-d937-3b1b-a5f6-4cd90f778ab8 | -18.25242 | -42.3817 | 2026-08-11 04:36:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 335b8d1e-6a47-3401-b7e2-ab6a16c7be79 | -18.35272 | -42.3044 | 2026-08-11 04:36:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3cfb0d08-a3a6-3d31-9fb4-4d8a413620c5 | -20.09423 | -44.31745 | 2026-08-11 04:36:00 | NOAA-21 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b6d878ea-fab7-3667-8c6a-e629be50d67b | -13.59659 | -55.21597 | 2026-08-11 04:36:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32d23fbf-3899-36a4-93f9-cf1c953db63e | -14.25679 | -51.96056 | 2026-08-11 04:36:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37aff48f-e963-3d50-b219-056b0f926908 | -16.66561 | -43.63485 | 2026-08-11 04:36:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6114971a-ddd2-3f19-ad21-33f6b6b6f41c | -14.00736 | -53.97966 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f32b9bb-17c5-39a5-b949-b1b9ed0799f9 | -13.84117 | -53.68515 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c89ad6d-8562-3fb3-bf96-1a90e05f8ada | -13.85494 | -53.78428 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a24bb6a-5da9-3d66-bd0e-1eb5e930f4eb | -14.09469 | -46.3658 | 2026-08-11 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46d096e0-d876-37b4-9840-d9daa3bafb9f | -15.00915 | -46.58053 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d206676d-331b-3ea7-91b2-461545fcf8b1 | -14.31136 | -54.92479 | 2026-08-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ba5e6fe2-f3a2-31b5-81bd-9e237fbef529 | -13.87228 | -53.79671 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da5a6554-5c96-3894-90a3-f87b15c2250f | -14.10375 | -54.02925 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aadff170-532d-3d62-8d8b-a148cf65ffce | -18.50749 | -51.66567 | 2026-08-11 04:36:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9309e7a2-49f8-3e9d-9ecf-30cca4dba545 | -15.52413 | -42.66312 | 2026-08-11 04:36:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 89c90fb8-26de-3180-b2f8-328ffb522ed8 | -13.87308 | -53.79209 | 2026-08-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 10037d09-1258-360f-b883-8c7872473882 | -14.46203 | -45.68288 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ccf40e34-95a5-3961-b0b1-60740798f961 | -15.05096 | -46.57311 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fedd7831-252c-3e4d-ac45-8a4dbca6a2c5 | -14.45382 | -45.68648 | 2026-08-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9fcaa3e1-7b5f-356a-8e96-046fe89b6aee | -13.43853 | -57.03961 | 2026-08-11 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31450c55-832c-383e-a876-1fbb66290553 | -14.30734 | -54.92405 | 2026-08-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e406c680-7a6a-3129-b395-698631efa01f | -15.01893 | -46.56374 | 2026-08-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README17.md)
