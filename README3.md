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
| 3d5828a2-38fb-3f38-8580-57cc287b5ce3 | -9.7031 | -51.0802 | 2025-09-05 00:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| bd367789-e9c1-3b74-a8cc-ba510496ce4d | -7.8923 | -45.2893 | 2025-09-05 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| afda2fdc-2792-3b60-94ed-91083a55a228 | -12.26241 | -50.15525 | 2025-09-05 00:30:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ebfa58a5-50b8-38d9-9c01-7fc8a8019321 | -11.58247 | -52.17225 | 2025-09-05 00:30:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| a6805708-9929-315d-b519-77f5028e0f67 | -12.97791 | -48.08104 | 2025-09-05 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f5a5bf06-cd85-3f08-9e6b-cbdc24e05719 | -12.9843 | -54.80831 | 2025-09-05 00:30:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 324.3 |
| 9de43ceb-82ed-3fbc-957a-025f97f29107 | -13.00461 | -45.23027 | 2025-09-05 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2c7dfbd2-d068-34b6-a589-3ca3f9314df1 | -11.00397 | -45.93699 | 2025-09-05 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8793bb87-cb0d-30fc-a345-1008f5372cac | -11.64601 | -54.52001 | 2025-09-05 00:30:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 56fefdbe-fc2d-3846-85a1-8cdfb1ea5c41 | -10.47098 | -53.62533 | 2025-09-05 00:30:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 630295b6-cd96-3863-b3c6-8330e3237f8d | -10.98666 | -49.77386 | 2025-09-05 00:30:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4b0c9423-c891-3148-811e-9a9721b14d29 | -13.11388 | -57.13728 | 2025-09-05 00:30:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 636dd57e-76c0-3e58-8845-c600b88e572f | -13.00322 | -45.22065 | 2025-09-05 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d9a05618-47ae-3ad0-b1af-e9cdd0f6b7ed | -10.24049 | -50.54274 | 2025-09-05 00:30:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 66245eab-5333-3e7c-a6b0-c173ad3b8c65 | -12.83601 | -44.44625 | 2025-09-05 00:30:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f0a3522d-c274-36fd-b1e8-9e415a81385c | -13.31839 | -48.56203 | 2025-09-05 00:30:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 24e383cc-f2ae-3c32-b9be-887a348205d4 | -12.98202 | -54.81532 | 2025-09-05 00:30:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 279.0 |
| c8ed10ea-a1d5-31e1-98e7-c699f41f143c | -10.49178 | -50.4327 | 2025-09-05 00:30:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 1d131d5c-a445-3395-b71b-c2e3652d1162 | -12.97903 | -54.78897 | 2025-09-05 00:30:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 5ac59510-f400-38f6-a2cc-4f6422a3b9c7 | -12.64385 | -49.46491 | 2025-09-05 00:30:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6ab5248d-e37b-3ee4-9960-ba5169f02bb7 | -11.13795 | -44.64998 | 2025-09-05 00:30:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a89eed3f-7d74-3b7a-86de-112493f9d1d6 | -11.58445 | -52.18791 | 2025-09-05 00:30:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| c8329de5-c1ea-3578-8350-c00e73d94c68 | -10.98497 | -45.99697 | 2025-09-05 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 92d7cb3f-f12e-3f67-91aa-492af1226c6b | -13.10732 | -57.10168 | 2025-09-05 00:30:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 1eca81f8-d60c-3844-8273-001d9e836813 | -11.0013 | -45.9183 | 2025-09-05 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 59d3444f-31b4-30b5-804d-f6dc1964bdfc | -11.40006 | -43.60305 | 2025-09-05 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| c6e2eaa0-b224-39b4-bde6-fdb9fdc0c680 | -10.32762 | -47.81922 | 2025-09-05 00:30:00 | TERRA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| dc10185a-7672-37f9-9430-cbf4a15494eb | -12.96706 | -54.78358 | 2025-09-05 00:30:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 282.7 |
| cfe96e5c-9b62-3bd7-9a47-1971c7240256 | -11.99564 | -46.7518 | 2025-09-05 00:30:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 701e1be3-ee21-31e1-95a0-c7b7601ed5a0 | -10.03109 | -48.34568 | 2025-09-05 00:30:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b816afaf-0429-3e94-b804-e4ca7065859b | -12.99877 | -54.80673 | 2025-09-05 00:30:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 6fab53c5-b9e4-3acf-aec1-c6c15fe69585 | -12.32149 | -47.04292 | 2025-09-05 00:30:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 2a6d0951-c669-35e4-a1e3-ea4a006b01a1 | -10.76871 | -48.28566 | 2025-09-05 00:30:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| c7a0b7f9-82e8-3b6b-a835-8669b9b92e31 | -11.39823 | -43.59088 | 2025-09-05 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 5b10927b-76dc-332e-91ba-f3c3a9f03850 | -12.83753 | -44.45665 | 2025-09-05 00:30:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 3ee9d884-657b-354c-874c-a226cb237396 | -10.76995 | -48.29482 | 2025-09-05 00:30:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| fc4b959d-e9b4-32f7-bbfc-c8331bc7f3fc | -13.10994 | -57.09642 | 2025-09-05 00:30:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 38dd2295-47d0-374a-8289-79b0eb56378c | -10.32885 | -47.82817 | 2025-09-05 00:30:00 | TERRA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b55b0e0a-8909-3475-98c6-95ae1b74e541 | -13.11153 | -57.14259 | 2025-09-05 00:30:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 5d6b2d92-a5d9-3e03-86ff-aaed3af1f7fc | -12.10096 | -44.72668 | 2025-09-05 00:30:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5dd1da40-2708-38d4-b9ce-bac8c5a338be | -12.96457 | -54.79043 | 2025-09-05 00:30:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 334.2 |
| 108b1d13-b70c-3fa6-9852-8e41cfadb9e2 | -12.29442 | -50.01149 | 2025-09-05 00:30:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 30c257cb-2901-3f54-9323-9f62ff37aec6 | -11.9969 | -46.76078 | 2025-09-05 00:30:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ff10cf13-1cc0-3b77-b435-fa31039a4ec1 | -11.3964 | -43.57874 | 2025-09-05 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| fc0304db-eba2-370b-8cbe-ca8508924139 | -11.02543 | -45.06993 | 2025-09-05 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 7fce86ac-bbaa-3891-8920-7dcea375edb9 | -11.86081 | -51.4493 | 2025-09-05 00:30:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1c847965-92c9-3799-91f4-784809e997b4 | -9.63908 | -47.10059 | 2025-09-05 00:30:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a2062d7e-e5a2-37fc-a585-0e4e6e8b701c | -12.98151 | -54.78209 | 2025-09-05 00:30:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 8cac6b4b-31c0-381a-a48a-bb9aee6c88bd | -13.00162 | -54.83329 | 2025-09-05 00:30:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 74705dc8-a9b0-3d3f-a9e3-97cc805eb3f7 | -12.96758 | -54.81714 | 2025-09-05 00:30:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 243d3c0d-7834-35c5-8fe4-ceeeab6b1a4c | -11.00264 | -45.92766 | 2025-09-05 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b4630ca8-6906-3886-8d90-849a668ee1fe | -13.30435 | -46.82187 | 2025-09-05 00:30:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 08af62e8-eea8-3cea-a605-48713d7b9bff | -10.96619 | -49.76593 | 2025-09-05 00:30:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c7d634c5-7644-37d5-910a-c230ea31de63 | -12.4357 | -44.75412 | 2025-09-05 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 6f05c742-6887-35a9-915a-91cb0f32ac52 | -11.58231 | -52.18191 | 2025-09-05 00:30:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 930622a5-7d31-3164-96d9-472cd6352dcb | -10.99795 | -46.02356 | 2025-09-05 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 516d1fe5-031c-3b99-9ee7-bab55919c0a8 | -12.29296 | -50.00019 | 2025-09-05 00:30:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e88c189e-a479-3a2a-87d0-73401e385cdd | -13.27137 | -51.85913 | 2025-09-05 00:30:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| f730104f-5297-3c06-b6b1-1f93ab35c304 | -11.63188 | -52.20721 | 2025-09-05 00:30:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 2491fee0-3419-3434-86f6-24788c7a098a | -11.97044 | -46.78019 | 2025-09-05 00:30:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 9fcb976f-f005-3672-bcdf-6120afa2e2ec | -12.09005 | -44.71786 | 2025-09-05 00:30:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 22a7744c-7a73-39b3-ae05-d5bc3b31bb83 | -12.33155 | -47.05061 | 2025-09-05 00:30:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b86b1167-f132-3e92-9238-7f7c0ab0f99e | -11.38808 | -43.5926 | 2025-09-05 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 13862feb-78f0-35c5-b846-0bb02a82d5f8 | -10.24892 | -50.53006 | 2025-09-05 00:30:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1cac905b-2851-358d-9290-54eabf56adb1 | -12.24094 | -50.15269 | 2025-09-05 00:30:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 82462579-4880-3ed1-8fff-7e748fbeb0c7 | -12.99648 | -54.81366 | 2025-09-05 00:30:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 269.9 |
| 2bb49a78-34df-32cd-95a1-1bdaa5b57b0a | -9.8065 | -48.31525 | 2025-09-05 00:30:00 | TERRA_M-M | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e07d637d-8e73-35f9-a851-781289d947bf | -10.97263 | -46.82933 | 2025-09-05 00:30:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3e9f0c23-a8e3-35f4-b219-bea96d468b34 | -12.98715 | -54.83507 | 2025-09-05 00:30:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 2dfef90f-8a93-3571-9f7a-1520ebec49d1 | -12.12064 | -43.35102 | 2025-09-05 00:30:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1981714b-2b3d-3105-8972-7e8f17253e8d | -12.2738 | -50.16547 | 2025-09-05 00:30:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 49d4f3f8-8063-326b-b062-a923ae9271e5 | -12.44587 | -48.09216 | 2025-09-05 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d81b3be4-cd9d-3e30-b050-99e66cbc6f8f | -12.11866 | -43.33778 | 2025-09-05 00:30:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1b30b0e2-57a5-304b-98bc-8cf87d0c0192 | -11.2632 | -48.33585 | 2025-09-05 00:30:00 | TERRA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 699aeaea-201a-3e99-a857-9e8689a2bf34 | -10.07596 | -48.06587 | 2025-09-05 00:30:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 74d69bdc-f8c0-393b-a9fe-9985ad8f6aa7 | -13.29927 | -46.85025 | 2025-09-05 00:30:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3a448166-d5db-3f25-8a28-66306709ea37 | -12.96986 | -54.81012 | 2025-09-05 00:30:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 256.5 |
| 1b04f4a6-c468-3330-b16f-142b16f76b2f | -9.70371 | -48.98825 | 2025-09-05 00:30:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cf5068ec-1a3b-3130-b2f3-13e3f1d69be5 | -10.97465 | -45.98903 | 2025-09-05 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 377996b6-dbb6-3ba8-ae7d-85880c8631c2 | -10.97599 | -45.99836 | 2025-09-05 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ebc8465c-6b03-3776-8694-7cbc8b7fa281 | -11.02394 | -45.05978 | 2025-09-05 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f59c0397-11b8-3f36-816d-d015743b0bea | -12.08438 | -45.69072 | 2025-09-05 00:30:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 214d5dca-b6a6-35d7-ba63-84f9afd8aa40 | -11.83307 | -51.43149 | 2025-09-05 00:30:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| fcfd5e1c-8f35-3ed7-8125-3f92368a5ee6 | -11.38992 | -43.60475 | 2025-09-05 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a7cd2131-2554-39dd-bfa3-6f0bf4f1895a | -10.47186 | -53.61879 | 2025-09-05 00:30:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 7faf3c09-b8fb-305f-a9ef-e4f0395e0484 | -13.00305 | -48.06182 | 2025-09-05 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 424d376e-94f0-3024-874f-1ee8c71f56bf | -11.64876 | -54.54377 | 2025-09-05 00:30:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| ea27ea3c-5650-3757-9b79-09aecfd57214 | -12.96891 | -48.08231 | 2025-09-05 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9509f8ef-7d57-32f5-b4ed-94dbe085b627 | -12.85766 | -48.00836 | 2025-09-05 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bac0fe4c-580a-346a-a7b9-2263989b4968 | -12.41115 | -47.49865 | 2025-09-05 00:30:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e591229c-034a-3e52-b001-d7accbf314a8 | -10.23901 | -50.53138 | 2025-09-05 00:30:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| cbd8439f-ecd8-37a5-98d1-fa82adfee9ff | -10.97829 | -45.95031 | 2025-09-05 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d5a6f56d-9dd4-39e3-b1a9-f4ddc2b99854 | -13.30311 | -46.81289 | 2025-09-05 00:30:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c3f275f2-8522-3d5f-96b4-367537ea495d | -12.8769 | -48.01525 | 2025-09-05 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 184349d4-42a9-3e48-bb12-7bde36e16247 | -12.53413 | -49.10402 | 2025-09-05 00:30:00 | TERRA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d8ff8018-3d1a-3898-95a1-7cfe683f56e3 | -12.43418 | -44.74394 | 2025-09-05 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| eb724909-42f1-3ea4-b2f2-86cd8cd1b8ad | -11.6338 | -52.22294 | 2025-09-05 00:30:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 45b43705-976b-3b45-bb4f-cbf3310dd283 | -12.99955 | -54.84037 | 2025-09-05 00:30:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 115.7 |
| d519a85b-a4ef-3539-a98e-7f1ff5fb161f | -11.96919 | -46.77121 | 2025-09-05 00:30:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a7c596be-95bb-3d4a-b316-1e64b403f790 | -11.74549 | -47.75425 | 2025-09-05 00:30:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README4.md)
