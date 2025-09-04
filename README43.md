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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebd5b019-f08d-32f3-bdb9-071368f2fc61 | -11.65957 | -54.5265 | 2025-09-04 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0bacfa7b-4768-3227-99ad-aebe377c630c | -13.58671 | -48.12835 | 2025-09-04 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b142bf7-ad0a-3460-aede-35cdad84539b | -11.59413 | -52.14991 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e517db5a-f1b4-3819-9efe-badd77aa915c | -13.75181 | -46.94725 | 2025-09-04 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e11ea0a8-6fb5-3cfa-8cde-6cd3160ed229 | -6.7633 | -59.66886 | 2025-09-04 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5693f35-f726-3317-bfef-5a4044bdbe2f | -7.68385 | -50.27472 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f5478427-7121-3cf2-b2e1-ef125be891af | -12.92081 | -57.00391 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cdbf6d41-bcae-3670-87a3-5580d6a2f4a1 | -8.97845 | -44.45793 | 2025-09-04 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| def40186-b648-3852-9821-0d8fca753e76 | -10.75609 | -45.26665 | 2025-09-04 04:27:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e63f29cd-3ba4-3ebc-bec0-026446caa1a1 | -12.45783 | -48.08031 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 37a77e81-5d85-3502-9b07-1924c679b498 | -12.91034 | -56.99826 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a53de495-196f-3579-bdda-9bab346d6975 | -13.30835 | -51.78841 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d49004c3-2f7c-3441-8a92-e6db230ed3da | -11.78313 | -51.51782 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c28e94c3-77c9-3bd2-b517-0a8edfdfd93a | -14.53759 | -48.06989 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1c3c15a8-a093-3cb8-9e2c-d3c0f26d481f | -12.89951 | -48.04049 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21f0921b-0ce7-39be-865a-b652e4b4b975 | -10.14958 | -46.25898 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26bc4ec2-2121-391d-bc15-41fb0c4f0649 | -7.36772 | -49.39854 | 2025-09-04 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05e59e41-2252-376a-8000-a3e0b0f6d30a | -10.03137 | -46.09805 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e8ee3b5-f846-3e1f-b4e4-fe7958926f37 | -14.13064 | -46.95462 | 2025-09-04 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27077304-b496-3ae2-abae-cf2cf1e817d9 | -15.0322 | -50.08405 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5ebd97c8-d620-3bd0-9ea0-43dc5c37a247 | -12.90628 | -56.94079 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1a5ff021-ccf3-3496-a29a-9118fffd4896 | -8.37995 | -48.32294 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 640028d7-7867-3808-ab5b-e655d4cc9301 | -7.70242 | -50.25017 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9cfbe635-9c7b-355b-8533-72d682041ed2 | -15.13236 | -48.18203 | 2025-09-04 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2ffb5da-40f8-32e4-9505-80c820a2e95b | -6.7421 | -58.72486 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a966a599-91f5-305f-a6ee-00847b6ebbd3 | -7.74554 | -48.77223 | 2025-09-04 04:27:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 63d6dc53-cdbf-3fcf-add7-c76ea6475394 | -11.67135 | -57.34597 | 2025-09-04 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 1a34cfb8-232e-3a72-a26a-36692e0c66e4 | -10.7327 | -49.59386 | 2025-09-04 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3ca5c5f-688c-306b-8117-0f4dd4e6fe0f | -11.4395 | -46.9111 | 2025-09-04 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1686a720-d870-3b8a-9b60-7f269fff6e1f | -8.07287 | -45.34862 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30857ecb-be7e-3516-98cc-e0ee92fa30d8 | -9.19628 | -45.20008 | 2025-09-04 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6eb8fc07-8bcb-3050-909f-af9c15c5dac9 | -11.12998 | -44.63638 | 2025-09-04 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3f8d026-5c2a-381d-8ddc-0aa95379c74c | -13.85909 | -47.97335 | 2025-09-04 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce24413d-0134-3aa2-a374-9f6996fd44d1 | -14.77764 | -48.14576 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd1fa87d-3c89-3f94-ba3a-0ee17c495ff5 | -14.99572 | -50.06593 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a019e8a8-dc2f-34a8-8347-dab2da6bce31 | -12.91101 | -56.99889 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f153d83e-67cd-30d3-b8f4-3fdc241fe10f | -14.56612 | -49.1404 | 2025-09-04 04:27:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c42a748-c076-3481-95c1-e4d62ae40cee | -15.02883 | -50.08345 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4610c176-8611-351d-a956-6cd932f37f00 | -10.43523 | -50.37198 | 2025-09-04 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 395b3ed7-a275-38b0-96cf-f8ea1fa6818d | -8.37937 | -48.32655 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3286fb74-9a03-39d0-9e84-96d6a1227cdf | -10.4789 | -53.62713 | 2025-09-04 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e0b265b-e422-36a7-8c4d-15adf54388c6 | -10.96895 | -49.75832 | 2025-09-04 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0d69916-b061-33e2-96c0-cfabc620e32d | -11.84391 | -51.41948 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fef10da1-d99e-3e40-b7c5-89406fb18b7c | -14.55411 | -48.05079 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10ec4ac9-8a0b-339e-a7d2-998f82228148 | -13.4595 | -46.83094 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02dd73eb-d268-3dee-9a74-9ae3ea93720d | -10.43234 | -50.36726 | 2025-09-04 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 4933e4ea-8258-33d1-acc5-ac92b5f01769 | -11.64172 | -52.18205 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69868235-9929-378e-9752-546ff901f59a | -9.3313 | -55.20932 | 2025-09-04 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ec70d5f-82df-348b-8f5f-c0cbb0d11254 | -11.7314 | -47.74605 | 2025-09-04 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85daaaab-a1b7-3b68-8245-7d713d2e68b4 | -12.86925 | -48.01754 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a4fd862c-ac9a-3e70-ad7d-e5a170e35950 | -14.55466 | -48.06905 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d1a1132-c801-3a51-ae00-a188dbc194a1 | -7.68722 | -50.27346 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1e8777b5-ffa1-335d-8451-89f37f2ae4bf | -12.23242 | -45.06003 | 2025-09-04 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68ec9c54-0a12-3893-a90e-bc7ae1f47da6 | -12.233 | -45.05599 | 2025-09-04 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09b4c222-ccda-320e-80f1-80a8e871659f | -7.77731 | -50.96765 | 2025-09-04 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65592f16-6048-3265-895a-ca6cd49c51a7 | -7.70273 | -50.29366 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8083fce8-f80c-37af-8980-106fbc745c55 | -11.53836 | -54.49173 | 2025-09-04 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0449aa12-13a9-3249-8fde-614dbb1a8ddc | -15.02 | -50.03169 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f750e235-6c03-313c-b233-da2106e58cdf | -15.05135 | -50.05231 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ed33f1f-be38-3dac-a6af-2eddacfa88b4 | -11.48855 | -48.54854 | 2025-09-04 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98c6c08e-eefc-3a5a-b6d6-a8eea3e1f21b | -10.97608 | -46.85217 | 2025-09-04 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24d43058-85cb-3c25-bd13-9397e10ed664 | -9.72298 | -48.31131 | 2025-09-04 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1fd4e89-f6d6-3b35-881e-c7a8dd41f9c5 | -9.69139 | -49.0151 | 2025-09-04 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f32ac070-1981-3ee4-b36f-619774947dec | -8.89255 | -45.81196 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9dd54d94-6be6-38f2-a04a-c610a620c17d | -8.87262 | -45.85268 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51cf4f92-8798-38ae-99c0-2b6643e66f25 | -12.88956 | -48.08224 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f415553-4a8f-32a1-92d9-0a4e1967bc5d | -9.69379 | -49.00026 | 2025-09-04 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60d5363a-3cf4-3baf-94a5-7adb1462e33f | -14.20155 | -48.08749 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7c6ed61-3128-3682-9a67-dfbc9c89250a | -11.91712 | -46.65588 | 2025-09-04 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 553d7cbd-3dde-3632-9b7a-8eef22fbf49c | -8.86535 | -47.92519 | 2025-09-04 04:27:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b260c30-3a96-3642-801d-2be5b8f2cac2 | -6.74101 | -58.72599 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8e4307e5-3b25-33ba-b5e8-a603b1e96c9e | -12.63798 | -57.00531 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f77f0ecb-d633-38af-9812-102d1e10d577 | -8.86478 | -47.92873 | 2025-09-04 04:27:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1936f9d-696b-37cb-a575-0b5d8491a3e1 | -15.04545 | -50.06702 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 109d8be0-b234-3f44-97ec-2e080b00ab70 | -12.96378 | -48.0659 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85b6720b-4d0e-3af7-a4d4-79f90d8bd7de | -10.50374 | -50.43766 | 2025-09-04 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49f53fc3-0e49-3d86-80cd-d50e7d7de3c6 | -8.36811 | -48.33218 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b34415a-c70b-3235-a91a-2efbd02463b1 | -11.73415 | -47.75008 | 2025-09-04 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6bef3991-cfe1-34b5-abb9-287fa80ddd11 | -12.95717 | -48.06482 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a27db9d-e50b-3736-940e-c1cb5375afee | -7.36708 | -49.40252 | 2025-09-04 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f8e2549-d60a-3291-ad1f-6b19df12c2de | -12.9039 | -48.05566 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e678a79e-fdea-38a3-8518-f4cda2c7080e | -11.03458 | -45.13781 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.3 |
| b48c637e-453d-3178-9fc5-1d635020e5db | -8.36357 | -48.33891 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6e6d3510-5eac-301e-9196-66533b6badfd | -6.66601 | -60.02959 | 2025-09-04 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b34057d9-e315-312c-8292-1507709a36d4 | -11.84148 | -51.42093 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4308656-ffae-3a4e-9067-13585702408a | -12.89545 | -56.93483 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1617c514-0a70-3e1e-9eed-c5aed16d858a | -15.00494 | -50.05199 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5b2f2db-693e-3eb8-872b-5448267863d3 | -8.87208 | -45.85623 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 711ea8c7-f29c-3561-ae32-04589549bf50 | -10.4898 | -53.64948 | 2025-09-04 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42abc2cb-4194-3246-8f63-ccfd92d7d35a | -10.42671 | -50.37904 | 2025-09-04 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f0d540c7-ba98-3802-896f-7d3b7baea1fc | -10.43314 | -50.27456 | 2025-09-04 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75bd3048-2fd9-3231-ab29-58d43fbfa2f3 | -10.42739 | -50.3749 | 2025-09-04 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 93f7d93d-c674-3891-acf8-98a3c8f80236 | -15.053 | -48.36241 | 2025-09-04 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79ae792b-6caf-3ea0-96f8-c65b30982dcb | -8.8843 | -45.84348 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93bd4b23-0b56-3d58-8169-d14ae4e1b623 | -8.89584 | -45.79058 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 164d7f52-85fd-3620-b71c-f8fb7e53898a | -8.89092 | -45.82263 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d810aca-8b27-356c-9972-16c1c7cd2cf4 | -13.45142 | -46.93029 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45afb896-3f3a-3011-b729-983972e4f7d2 | -12.1839 | -53.89029 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2675b1e1-217e-38d6-9208-4e8e5549b01b | -6.83265 | -59.36009 | 2025-09-04 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a9ac6194-41f6-3a18-b88d-0b1669287bbe | -14.82496 | -48.21181 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README44.md)
