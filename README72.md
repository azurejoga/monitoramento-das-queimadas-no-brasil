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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7f6fb55-1bd2-30e7-9f9b-526d706cbb48 | -14.81753 | -48.21389 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b3061a9e-fae8-34b2-b52a-53e24406c227 | -15.15322 | -52.38342 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 428ea76f-557b-3490-81d2-d7968318b7f7 | -14.55924 | -53.06464 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 937480d0-013d-3605-93fe-a681d169e63f | -12.88863 | -56.9426 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d4ac3618-094a-3c2c-a96b-0cc44bb778c5 | -12.91282 | -56.9298 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20ca8059-8c41-3ffc-b5ec-72f1bbb03fe5 | -12.90111 | -48.03423 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c8e412e1-4e51-334b-9153-98a9a04ba77c | -11.95425 | -58.72787 | 2025-09-04 04:55:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 735ff423-d301-34a4-8814-bc07027926d8 | -15.04112 | -50.05205 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3fd87119-7cb5-30d8-9844-271f449a4fc7 | -15.03978 | -50.06168 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6fd6648e-c7a2-3373-8da5-fa4989b423fa | -11.53106 | -54.48666 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3687e62b-df16-33b4-ba28-0992b0d1e924 | -15.0581 | -50.04735 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12a2eed3-e135-3dc6-b3d6-9d5588be6840 | -10.45725 | -53.62355 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbff41b6-112e-39c6-a434-64895bfc922d | -16.46902 | -49.51271 | 2025-09-04 04:55:00 | NPP-375D | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 596487bc-70d6-3b47-af1b-aa155380f115 | -13.45475 | -46.93887 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd78670a-02ca-3d4d-9474-9d8f6600f83a | -11.60265 | -47.78616 | 2025-09-04 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 422897dd-e32c-39ec-8036-6c8725c0ddcb | -10.0973 | -54.75455 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84006795-b069-3983-89e3-d051407c14b4 | -11.54166 | -54.48475 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d202e15-7a3f-3c9e-809f-7258e7e0f8e9 | -11.08934 | -52.02072 | 2025-09-04 04:55:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff9987d2-51b0-3c59-922b-697a904cdec3 | -14.58796 | -53.0125 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1db201ef-9bfc-3397-ab81-19f62a809d7f | -13.73653 | -46.94159 | 2025-09-04 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e56cba2-0887-3c66-b7a0-a7a421395906 | -11.59372 | -47.75591 | 2025-09-04 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40dd7060-96fc-3e0e-892e-0b87421648e8 | -17.17854 | -46.23387 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 241bb098-a775-3b74-86bb-9fc6ce7d7058 | -15.17106 | -52.39351 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17b4eff9-fce6-3a62-bf04-c9f265fe4da4 | -14.57195 | -48.07937 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7b145a7e-4146-3306-b02e-eda62565d191 | -14.3963 | -51.67005 | 2025-09-04 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e800f3c-eec5-3f4f-bf70-7857128fd7bc | -11.84622 | -47.54499 | 2025-09-04 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edf792bf-0533-3d98-bc04-3cc768a5f05b | -14.20896 | -48.0938 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2b6aaeae-e8e0-3aed-9a6f-ba3b29327d19 | -15.30066 | -52.74519 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a1d8870-a575-30fc-8875-8a48e1e607b9 | -11.09614 | -52.02184 | 2025-09-04 04:55:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be76bc2d-b9bb-3f70-a44a-c105a52ba0b9 | -13.30517 | -51.77477 | 2025-09-04 04:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 441e7430-15e2-307c-9b23-6af4d6ba92be | -17.15477 | -46.24699 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abb624a5-f018-3ca7-91d3-15c3a1562705 | -11.85508 | -51.44344 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e04209f4-7551-332f-abef-15bba08b30f2 | -12.87043 | -48.02217 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c41d7c0-900d-3b45-a53f-bfa66d3e5a4a | -12.90719 | -56.94154 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 17f5c578-0720-3074-ae74-71e267679833 | -11.10124 | -52.03402 | 2025-09-04 04:55:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37615c0d-8424-3c55-8c4a-153099da4330 | -12.17758 | -53.89129 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddfc338b-b0b2-33fc-94ee-261c7182ed98 | -11.87371 | -51.53443 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8d575039-d300-3fec-af4f-6d2dedf624a7 | -15.19703 | -52.36178 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ab475a3-7350-3a2f-ba27-d4e6afa3effc | -12.52836 | -53.81041 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e8d918d-385f-3b51-91d3-28f78d5201ee | -17.05914 | -46.44524 | 2025-09-04 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d5c8af50-91df-3d03-8896-6d12d14a966d | -11.65456 | -54.52159 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bae79227-74ce-3bcc-9287-802566b16bbf | -12.91213 | -56.93391 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ce05742f-bf1f-3749-b025-ceb9fe54546e | -11.67546 | -57.35205 | 2025-09-04 04:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| ae3c21bd-8afc-391d-912b-bfaa49a99f22 | -13.09108 | -57.11681 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c2e9ab4-246e-304c-95d5-ca539a8fbaaf | -12.61081 | -56.99917 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2527df83-8c7d-3ebb-b5de-fe04209dd7b8 | -15.54691 | -48.40082 | 2025-09-04 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c4c407c-9898-3a52-b732-d3f3cf418e49 | -11.78085 | -50.67532 | 2025-09-04 04:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cecc6ad3-fd62-3d70-9bda-f474dea85ec3 | -12.23314 | -50.15064 | 2025-09-04 04:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| feb7d916-fb43-35b6-b697-6f15bb7dd388 | -14.58629 | -53.02353 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15e07764-5188-36ba-8fab-c684d4763281 | -15.16245 | -52.39291 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b2ececb-7740-3bad-b6bf-358bbad26195 | -11.65342 | -54.52871 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22c419d2-7093-3758-adec-0231feef1d01 | -11.59281 | -52.1502 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab885ebf-54da-3f52-9633-84cd3e40f17e | -10.96759 | -49.75212 | 2025-09-04 04:55:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eea1f073-2822-39a0-9eb8-1592babfb721 | -15.46925 | -53.01448 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4cbc270-a094-336c-9833-eeec0af54ca9 | -11.64389 | -52.20293 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 982dd57c-4d68-329e-9864-7fbf4d78ad46 | -11.62745 | -52.19661 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2beb4718-b884-36a9-8098-ba39c83c137d | -12.89359 | -56.93493 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba07da49-9352-3832-adb8-32842375fc48 | -10.50333 | -50.4397 | 2025-09-04 04:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 030b4e7e-0086-3240-8ba2-9a331dd827d4 | -9.4927 | -57.8153 | 2025-09-04 04:55:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0718fa28-96db-3865-a2b0-a9333fc41531 | -16.96783 | -49.30128 | 2025-09-04 04:55:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b752853a-4ba3-3a7b-9d2e-fb0c8f5ce29b | -11.53832 | -54.4842 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c79771b0-145b-3641-9ea2-2d3e2edcec3b | -11.63765 | -52.1982 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a06dcbc-d752-3adf-835a-6ee6056bb010 | -10.50755 | -50.43608 | 2025-09-04 04:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b3fced7-d016-3314-aa53-09714f539b41 | -11.44338 | -46.92002 | 2025-09-04 04:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d42cb052-bde1-3632-8b74-175afbf515c3 | -15.59595 | -52.89115 | 2025-09-04 04:55:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14292d9b-cdde-3eef-9a2b-c2e26196a4bc | -12.8721 | -48.02174 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11be696a-ec4c-37b4-b701-c546bf570fbf | -13.31044 | -51.76348 | 2025-09-04 04:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a350360-bef3-3ba4-8568-27052f361505 | -12.46137 | -48.08605 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 622f8939-a9cb-39ec-b1a6-782da0c426c5 | -13.50446 | -47.00977 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2816df8-b11e-3a04-9d11-d2c3444bbed7 | -12.91303 | -57.00573 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c267616f-bc96-33cb-b962-0d40b1e7989a | -10.49973 | -50.43916 | 2025-09-04 04:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 76c7f7ce-2a99-3244-a25c-506d29fb75e9 | -12.64619 | -60.15959 | 2025-09-04 04:55:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9c91bd09-bb10-3b87-bcf1-f540f0848c50 | -12.91502 | -56.93864 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3208fd01-e5d8-374b-b29f-cf74d7fc0273 | -10.44782 | -53.61842 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 440e9e44-eaaf-31d8-974a-5dc5bf29a33d | -17.05442 | -46.44152 | 2025-09-04 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc01d967-663d-3663-9e84-ff783ec3bb18 | -10.95718 | -50.92596 | 2025-09-04 04:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 034dbf81-dcc3-345d-a3a2-3d50da1cba9d | -15.14974 | -53.51123 | 2025-09-04 04:55:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89e2ceb6-15e7-3ff3-8816-b8837aca020d | -15.00812 | -50.03223 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea87d48f-bdcf-3137-9f0b-7b1dcb324b09 | -15.73713 | -53.64128 | 2025-09-04 04:55:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f77e43ed-c273-3c39-9f47-3ae49740a41f | -12.11029 | -45.21531 | 2025-09-04 04:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d93dc33-1ad1-30ad-b4f5-ffeecdb46bc8 | -13.09537 | -57.11329 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8a9a6f7-0080-3860-aa72-14ff720fcd53 | -11.73799 | -47.75583 | 2025-09-04 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b45cd406-75a6-3fde-9b1d-95834330b60c | -12.97365 | -54.77177 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8039ce54-beba-3b3f-a9be-bdd60237ad28 | -11.65733 | -54.52571 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3f096806-0061-3b31-aadb-7b1d948bf6fd | -11.64105 | -52.19872 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c8b0509-5dba-39da-b8ef-d8e4cd4159f3 | -15.55124 | -48.40162 | 2025-09-04 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2edc7ca4-6f86-3244-b82b-2bd8087da98c | -14.5727 | -54.54893 | 2025-09-04 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff9f24a7-41b5-33f8-8c56-c2ba5995ef12 | -17.17162 | -46.24899 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 655909ce-6b2d-3763-ba7a-25634eedaebf | -15.15612 | -52.36405 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6562ee62-e212-352b-bb6e-b579e21c2bf2 | -14.99104 | -50.07 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6d407a2b-21c0-3136-975e-3aa9d855ca43 | -17.14448 | -46.24571 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1925a5cd-27f5-380f-8d8e-fe201f73d9dc | -15.19122 | -48.01611 | 2025-09-04 04:55:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c090e37-ea4c-3633-b197-0297d15f0fb3 | -17.15863 | -46.22495 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a10f858-cffe-3233-ab26-5a49cf4d38d8 | -15.3035 | -52.77292 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22f5deb1-5866-3d81-8a4a-c6721576695a | -12.49894 | -53.84553 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d4d4bfc-647f-30d5-b154-61f664f293cf | -14.57169 | -54.51215 | 2025-09-04 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0563603d-8441-3280-95c4-49d3b02035a7 | -10.27358 | -54.26682 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 943de423-e728-399b-bda7-d877e1b7ce46 | -13.57069 | -48.12843 | 2025-09-04 04:55:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2478ce1-8d82-3d88-acdc-cb0b9c3e3ce4 | -12.48674 | -53.83628 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67d12f52-31c4-3f0a-8340-2b71fd879db2 | -15.61763 | -52.88686 | 2025-09-04 04:55:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README73.md)
