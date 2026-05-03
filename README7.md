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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc3779f7-f7f0-3c56-9cc3-5bca3fbde982 | -18.05957 | -52.94636 | 2026-05-03 04:44:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ad4c621-42f7-39f5-b45c-d029068c2ebd | -20.62603 | -51.71202 | 2026-05-03 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ed4581d-3817-3cee-b297-c9840f57bd91 | -23.11844 | -47.68565 | 2026-05-03 04:46:00 | NPP-375D | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 90b43d75-41a1-3440-9c1b-2756d00a5889 | -20.62662 | -51.70832 | 2026-05-03 04:46:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d067675-736c-3dd2-b934-fbea4125b3ec | -12.37 | -50.0242 | 2026-05-03 04:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 0595fea6-df1d-3f4d-86b7-f509dd64c372 | -8.33067 | -45.35804 | 2026-05-03 04:59:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a477fd8-a844-3cc8-8424-99b705abee11 | -9.67645 | -43.79528 | 2026-05-03 04:59:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8d0d4e63-004d-32d9-814a-e28d10c662ff | -9.67098 | -43.79 | 2026-05-03 04:59:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fbc6fdfb-910f-3802-991c-b7da56a55175 | -8.32816 | -45.35743 | 2026-05-03 04:59:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ce50423-3758-3d26-9739-dd183fb6562b | -13.22125 | -54.53683 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c84b4f49-0e7f-3b7c-8a9b-f1371ef9010d | -11.63951 | -52.55884 | 2026-05-03 05:01:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01e8e864-f1dd-35ac-8692-d66f8469cfdf | -13.2151 | -54.53214 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d35bd9f9-8e43-3b1f-b551-748bef180980 | -12.35725 | -50.02523 | 2026-05-03 05:01:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 148ab11a-4fa4-3161-85a1-0d26951e2dc4 | -12.38052 | -50.04013 | 2026-05-03 05:01:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 933fcf72-a74f-351e-ae92-4aa69e1d5175 | -13.22181 | -54.53319 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9da55937-ed4d-38de-96e8-236abd5dd672 | -12.29475 | -57.39944 | 2026-05-03 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 840f8ec5-bd06-38d8-88e1-7973a2c693ad | -11.30122 | -54.72943 | 2026-05-03 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46b3f52d-2553-3223-8963-4326d97e1e7f | -13.21901 | -54.52903 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aeb379f7-81e1-382d-9c11-fc08807dba28 | -13.22517 | -54.53373 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac78b4ba-0621-323d-97db-26039908a03c | -11.38085 | -55.1748 | 2026-05-03 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7dab3e07-ca5e-3901-b207-11b114fefa88 | -13.20784 | -54.5347 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21f66087-9598-3ee6-a93a-7e2b079079ac | -12.35622 | -50.03279 | 2026-05-03 05:01:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d0333598-0e47-3935-8c43-7d509d047ef1 | -12.28283 | -44.63107 | 2026-05-03 05:01:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1aa31266-e8e3-3040-ab4e-b28757cc4bf9 | -13.2235 | -54.54461 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd8995c9-f34b-3ca8-8fb0-eef0cbb98470 | -12.27687 | -44.63051 | 2026-05-03 05:01:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccb8a5f6-4c30-3af6-960f-fc9bf472f3cf | -13.21008 | -54.54249 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70ee2d8e-6edb-35ee-92d4-dd1c57fc3a41 | -10.9811 | -45.09903 | 2026-05-03 05:01:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d32fd086-6c59-3124-92f5-663b3e925b10 | -13.2123 | -54.52797 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 269553b6-16f6-3e59-bd2b-8bc2312389c2 | -12.37586 | -50.04333 | 2026-05-03 05:01:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bcf62e15-8047-366d-aa8f-723481a06f39 | -12.28335 | -44.62667 | 2026-05-03 05:01:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e3f6241-4e2d-35a0-8eec-394a124142c2 | -9.56994 | -50.68253 | 2026-05-03 05:01:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98aec7ed-0cc9-3872-b5ee-8c38c7ccab8e | -11.64246 | -52.56343 | 2026-05-03 05:01:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e994b84a-a441-3505-99aa-35d89ad15801 | -11.30509 | -54.72644 | 2026-05-03 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bbd31e9-20f7-3515-96c3-02d1b1adc335 | -15.89264 | -56.53625 | 2026-05-03 05:01:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| daaff770-16d6-3ed7-a1bc-f9c71337923a | -13.22237 | -54.52956 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bba1e84d-bd39-37f4-b7e5-b6a60f6e6ff0 | -13.11033 | -51.72592 | 2026-05-03 05:01:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47c1c356-1451-35b9-b1ea-5d1e8c122d1f | -13.19833 | -54.52945 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6f71a075-1a50-3eb8-b615-48ee034f6861 | -13.20393 | -54.5378 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9ddf970-e290-3ad1-94a4-44a06e495697 | -16.10749 | -49.24218 | 2026-05-03 05:01:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 300bde9b-473c-3647-8a6e-79d44f6989a2 | -13.21454 | -54.53577 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71a01a7c-923a-3288-9ae0-e4221959ef59 | -13.21343 | -54.54303 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eab7f229-ccc6-3d0e-8c6b-e552098c1db0 | -11.88721 | -43.81064 | 2026-05-03 05:01:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8012d41e-5e72-3b07-95db-677393ad8812 | -13.20448 | -54.53417 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6689a9f5-2a24-3df5-ab07-1e76b898f5d7 | -12.37225 | -50.03894 | 2026-05-03 05:01:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 499b2bd6-567a-30d2-a7d5-c4e3dbda6cb1 | -12.28513 | -57.3939 | 2026-05-03 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8628966-606b-35c7-b36b-92f8bea34eaf | -11.64306 | -52.55938 | 2026-05-03 05:01:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48afa418-4b2f-3397-81a8-b6b3a2d70a29 | -13.20282 | -54.54505 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6cdf0fcd-d6e9-3e38-b922-1b2700694842 | -12.36088 | -50.0296 | 2026-05-03 05:01:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 838b22c9-d832-3ab3-9376-d5bd8376bc07 | -13.19778 | -54.53308 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 178d1947-70c6-345f-93e5-79e640859204 | -11.37754 | -55.17426 | 2026-05-03 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a6ff649-9dee-3c00-b47d-aefb8b1f7424 | -12.27739 | -44.62609 | 2026-05-03 05:01:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7584e469-1388-36c3-8384-47170fc2bedd | -12.35674 | -50.029 | 2026-05-03 05:01:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f4179a90-878d-3316-aef6-6e40196b65fa | -12.29816 | -57.40003 | 2026-05-03 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 582d62e1-02cf-31b9-b771-5fd3d2466c0e | -13.22294 | -54.54823 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06ce6071-7008-3047-8bc0-2619ab575fd3 | -13.20673 | -54.54196 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e669acd9-34d0-3ee1-92b1-337fe2928cbe | -12.37999 | -50.04393 | 2026-05-03 05:01:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6059638-d7d0-30b0-8909-817adf8c47b0 | -12.36554 | -50.02639 | 2026-05-03 05:01:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c162d2be-e346-364e-bda1-b69f53abc765 | -13.22852 | -54.53426 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8af4b58-0bf7-35ca-9e93-ba7876521d29 | -13.20504 | -54.53053 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1be689f-2586-35f1-9cc1-a2316d415564 | -9.56612 | -50.68197 | 2026-05-03 05:01:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a0923e0-8d41-34a0-a492-74949cefbd47 | -10.97643 | -45.09041 | 2026-05-03 05:01:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 33549016-217d-3772-9e43-863645a2bb7c | -13.21175 | -54.5316 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acef5b68-096f-3bde-8930-7d572a9f71f5 | -13.20113 | -54.53363 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da1e5ffa-2055-30db-a518-1a2de5d197f1 | -13.20057 | -54.53726 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8825db9d-df0b-31f1-8f68-84aa6edde8fb | -13.22796 | -54.53789 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07a1f175-be06-317f-b01a-1d33a763ac3f | -13.21119 | -54.53524 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de377fd3-b34d-32c8-9086-dc73d09b3de3 | -13.21288 | -54.54665 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0aa13fbf-c0b1-3785-9ba4-8070ef922177 | -13.21568 | -54.5508 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c725a03-5106-3198-8cc2-cff905a05b21 | -13.21903 | -54.55132 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 5478ea32-6b84-3eba-8367-cadc97640360 | -12.35208 | -50.03219 | 2026-05-03 05:01:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7635c30b-408b-36e3-afa9-0eb1b4608cc5 | -13.21959 | -54.5477 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a72e5751-1e00-3eba-8f3c-00d1b0c383fe | -12.37487 | -50.01995 | 2026-05-03 05:01:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f03c63d3-47c6-3700-bef8-7ad786971361 | -13.2179 | -54.5363 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 242f2ed3-ff7d-338a-b5a7-c4b5ed52250a | -14.32402 | -57.73548 | 2026-05-03 05:01:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a497dd7a-d54f-36cd-94b7-94c14abfe012 | -10.98207 | -45.09132 | 2026-05-03 05:01:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ac418c40-5df0-32f7-928a-addfbc202d8d | -13.23132 | -54.53842 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7a66071-7198-3ecd-9435-f6c848e16946 | -13.21399 | -54.5394 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9d4c648-d9c5-32ed-b250-d9b8f0000c32 | -12.28855 | -57.39449 | 2026-05-03 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fee71f4-369b-3c76-82ac-84c5d67c822f | -13.21177 | -54.55388 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70bf9281-f285-3324-8b67-d231b40186e0 | -12.30157 | -57.40063 | 2026-05-03 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db644c9a-8180-3ce3-bd36-6e2a21820360 | -13.20839 | -54.53107 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f990603-7333-30b6-8129-4f3b2f8fa5b5 | -13.21623 | -54.54718 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4739347b-2fbf-3524-8d7d-0593a7bd9b35 | -13.20728 | -54.53834 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 487ffe18-e779-325a-9aa8-15cddea940bc | -13.22405 | -54.54099 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1cdf8cc-6340-332d-b004-42677e3fd3d3 | -13.23187 | -54.53479 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6030a01-8d8e-3093-ac2b-1dbbdca906d8 | -14.31659 | -57.73806 | 2026-05-03 05:01:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1937393b-ba73-3904-aa69-ff2345123e3b | -13.20559 | -54.5269 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 845e31b0-b6cf-308e-b7cc-4b7cbf73d6ae | -11.63892 | -52.5629 | 2026-05-03 05:01:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c12eecc-cb3f-3faa-9587-b5fe42eca50f | -12.28917 | -57.39072 | 2026-05-03 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1a17cef-049b-3d47-8d42-ead75df48a51 | -13.20337 | -54.54142 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45a32888-6e0d-3467-a1fd-06e6c440f2e4 | -13.21734 | -54.53993 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04d32c0c-060b-36f1-9dae-4ac6ca5747ad | -13.20168 | -54.52999 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bb92d89-a1b2-3850-9a7e-2a1e59ea2ffc | -13.21063 | -54.53887 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c62ced1-184d-37bf-8339-1900668e2ec1 | -13.20617 | -54.54559 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff944f74-f086-3f2a-88e3-620a0527a82f | -12.29753 | -57.40381 | 2026-05-03 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc5c7a7c-583d-3895-8070-1473a5c3b0e8 | -13.22014 | -54.54408 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88bff100-b331-319f-aa6e-d022232e8217 | -11.64187 | -52.5675 | 2026-05-03 05:01:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d74eb09d-cac8-3f2b-9da4-d9a7989d03df | -13.22461 | -54.53736 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb5745fe-844b-389e-97f3-0d2e164925de | -11.88663 | -43.81551 | 2026-05-03 05:01:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1891d691-980b-3d40-9174-9e13643cb122 | -13.19722 | -54.53672 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README8.md)
