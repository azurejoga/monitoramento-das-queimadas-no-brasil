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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f7aca3a-e7b9-346b-a4f7-659fb23e57f9 | -10.01958 | -51.70796 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1fd042b-a780-30ad-9029-636db05e9c27 | -11.48471 | -49.26001 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a06daefd-a5cd-320f-8955-8132f3f8b22d | -9.96814 | -51.68873 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4de96d38-0e82-3e5f-9a13-a40ca6aee7c6 | -13.58675 | -47.6758 | 2025-09-11 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc2c46cb-cb9a-3839-950c-ab195e6d5260 | -15.81665 | -52.22571 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d878d716-e99f-3d89-bc70-1a1bb963ab6d | -9.98084 | -51.69434 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2e9b65c-c1d8-3f57-b8a0-6d6cefb565ab | -11.48814 | -43.65353 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59d54681-4b2f-3abb-af4f-6dd894aacb85 | -11.82133 | -46.74315 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d31d90e0-d6c8-35ad-8876-404aef2c48da | -15.15455 | -52.40788 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a25c567b-72b5-3471-a1b0-cee5af152097 | -11.20106 | -55.38412 | 2025-09-11 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a3c0d3b-0501-3df3-9c0c-c09d099feee4 | -9.34038 | -48.943 | 2025-09-11 04:46:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7a605ea5-8ece-3f5a-97d0-c4b814025896 | -11.35835 | -46.54501 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab586a01-4c65-32ab-ae56-6323196cf4bf | -11.477 | -43.63623 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 578462ad-c2cc-32c0-952a-4a6343a4acfd | -11.49156 | -43.64402 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1f605df-7c21-368b-9e9b-300b72a193ce | -11.41516 | -43.55014 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 465fa590-f3f9-3993-97d7-792558e86a6d | -12.13797 | -44.8676 | 2025-09-11 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0e1c569f-a976-3c92-bda9-e4af13a01a3f | -15.12409 | -52.40642 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d28e93c7-52e2-38cc-9381-980a246a88fb | -10.88341 | -55.69044 | 2025-09-11 04:46:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4e5e41e-8646-3c7a-9d50-abcf2f886635 | -11.10538 | -51.99344 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db65bba0-7cf8-38d7-a8b6-f5e16fb3c4f0 | -15.13572 | -52.44148 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c73f540c-1008-3a50-9c36-ed90dd4d9f59 | -9.08202 | -50.47049 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0506bf87-e65c-343d-943c-0fbeceac36cc | -11.09993 | -48.43716 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2dbfca1-41d1-3a33-8c57-18f755067acb | -11.48589 | -43.67174 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60762490-d02f-31f4-8d0b-2b667137b31c | -15.15122 | -52.45142 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 480cb022-359d-394e-9130-7d15237e8c3b | -11.4803 | -49.24771 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87d9399c-f684-3901-91f7-88455ddfde6a | -8.58295 | -50.79908 | 2025-09-11 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b70b789-9e8d-3994-b55d-65a8eec16e74 | -13.8472 | -47.34464 | 2025-09-11 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f9b8e039-1e6d-3712-8dad-7b853a3f6414 | -9.99962 | -51.72596 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c70b32c4-21d2-3959-b58a-ae31c0d0fa45 | -9.98002 | -49.06226 | 2025-09-11 04:46:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3bb4c7f7-8e70-3068-a40b-6082a960098e | -15.8117 | -52.28052 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d8fae28-0b2f-38bf-a3f0-f553f98d14c3 | -11.20222 | -48.39953 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e2bd0e94-2cf4-3b03-b362-30e9299598a0 | -15.1324 | -52.41883 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1bbdc79b-5c27-3f30-b498-2f0d3caad1b3 | -10.02676 | -51.72699 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49041a06-fb98-312a-8a72-7a36a73963ac | -15.83169 | -52.23932 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ab852fc-8b12-3841-b3d1-24f7b5dfd319 | -11.7954 | -50.58484 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5be46bfd-7bce-3b9e-92e2-34fe9f88abb1 | -11.13574 | -52.05943 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc9473ba-a3af-3379-a9cd-395273466604 | -12.34702 | -63.64378 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79c429fd-7517-3d6b-8dbd-233a0a672f41 | -14.50862 | -53.95609 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f84c1b6-858e-35c7-9ee1-428d13673b8c | -12.97356 | -46.73391 | 2025-09-11 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2114660-42d5-3cc7-b016-440943742d39 | -9.45657 | -46.41982 | 2025-09-11 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a8da6b2f-21e0-32e6-96a8-5bd7411ade35 | -10.32072 | -48.81295 | 2025-09-11 04:46:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9fef590c-5d6a-3b47-8000-45e3474c58e9 | -10.16763 | -46.17873 | 2025-09-11 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32bad039-3999-3838-ad4e-063b59403eb0 | -11.14181 | -52.064 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e2dcc86-57a6-3106-bf1a-e9140384e561 | -10.27094 | -48.82624 | 2025-09-11 04:46:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3502a749-c6bd-33be-b66c-348ab54c5e52 | -11.21624 | -54.99451 | 2025-09-11 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 812c2576-fabc-3c88-a28a-1aa291657f40 | -8.09339 | -54.75057 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2851163-2f5c-34ae-b3ad-bac604ebfaa2 | -15.61413 | -52.76923 | 2025-09-11 04:46:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f08b216-d154-3ef2-9921-912a13d213f2 | -9.02905 | -49.76849 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5f9269a-cd72-3f29-a6bc-c2d80ef54c8f | -9.90272 | -49.91426 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9daa5339-2cb1-34d6-9170-c75f68cf48de | -13.22188 | -51.76334 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f7753a7-25b3-38b3-b53a-319363b263bf | -12.84377 | -47.96666 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aef11e74-3ffc-3aa4-834b-0d25ea062fcd | -12.98568 | -46.73967 | 2025-09-11 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8f645cd-47c7-3fb1-a817-38225a650f8d | -11.13085 | -48.35482 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d87029a7-9a58-3c3e-9936-9b43ad4b18da | -11.47423 | -43.69696 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 377b056e-0e53-3cbd-8246-fb46a91d288f | -15.94732 | -46.77021 | 2025-09-11 04:46:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4e1d4b1-5cda-3362-add7-bdba02b9b86f | -12.94165 | -54.75886 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fa126fc-6193-31ae-af97-5090345fe235 | -9.68236 | -46.76191 | 2025-09-11 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42492625-9a09-333e-8623-b602196a1443 | -15.12016 | -50.14348 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 112e20c0-1568-3a82-be7e-84bb9de8d0e1 | -16.29958 | -50.06527 | 2025-09-11 04:46:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a25b3e71-37cf-334e-bb40-2c6e531ed90e | -15.1958 | -44.04129 | 2025-09-11 04:46:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 33d1a4c7-5bb5-3057-8cc1-832841ad8c03 | -11.364 | -46.56589 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 16facd3c-790c-35f3-b352-8f474e1acc34 | -15.15399 | -52.41149 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eddc9d2f-7455-35c0-ae82-d7e1883b4f54 | -9.79328 | -61.51698 | 2025-09-11 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0c684f78-b12a-37a0-b8b1-41b2b9ea26fd | -12.91562 | -47.9928 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 746188a7-3eb0-39c0-b695-d17bf0de6308 | -14.8901 | -55.83608 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54848415-396c-31c4-83ce-5158e145b80c | -12.47207 | -47.48352 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7cca1686-5bb0-308c-a9bb-730ab0a596c0 | -11.48985 | -43.68154 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56acd3fc-9657-3ac1-b765-c603f44955b1 | -9.98305 | -51.70184 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4c2af68-ac52-33e1-ad6d-5ec1d528be36 | -12.92719 | -54.76033 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 51947c6c-a490-30ed-977b-e2112976ba14 | -11.12967 | -52.05485 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d8caae8-f1b8-3e51-a58d-3265995e4bdc | -10.48279 | -49.37299 | 2025-09-11 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 554bd387-789f-35da-9684-8fe0d3df51ce | -14.91727 | -55.92926 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d74b49e-bcb4-341d-9eb3-aaebdfd3bb2c | -13.26466 | -51.75182 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83ceebcb-f405-3a45-bec3-61910f554221 | -14.40864 | -47.3307 | 2025-09-11 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c431ec4b-2536-3531-8df5-1d44fe53d540 | -12.4707 | -47.4932 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9d00cea9-ae72-326e-b7e4-28cd5d45ba14 | -10.55332 | -49.86811 | 2025-09-11 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3acb65d-d8a0-3fde-ac50-b6fb01449ec5 | -12.02827 | -47.53955 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a934056a-d94d-3ae0-a5c5-5573397b0232 | -14.2976 | -54.77383 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d5c2e0e-2846-358b-a8e5-96b517f0774f | -10.88926 | -47.25467 | 2025-09-11 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4b2a537-6336-3f72-94c1-b5a3d0c45986 | -11.45654 | -43.59361 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27b0b54c-4462-3b5e-ae1a-6f9c462306d7 | -15.11436 | -50.08343 | 2025-09-11 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d7f5eeb3-648f-3893-8c18-b0cbfed6e72f | -12.92373 | -54.75974 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 831b911a-3a4f-3671-bfce-8e9e211af36b | -11.64949 | -52.24657 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ef8fa54-fcc0-3caf-8fcd-b4baa34c2e90 | -15.80942 | -52.22818 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 78b4fe7a-08a0-3db0-a337-afd6d36cc7ca | -11.47846 | -49.25995 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbef4ebd-3cbc-3b75-bbbe-ddbb9be42581 | -12.93603 | -54.74995 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7aa43bcd-d1b0-3255-83b1-6495a38a3199 | -11.42069 | -43.54767 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c8a6de9e-0be8-3da4-a257-208a666e68ce | -13.27404 | -51.7308 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 838d03d8-5cc0-3d75-9430-f21f30f967e5 | -12.93108 | -54.80095 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fda75f1c-ef0b-32ce-a282-a05fa9bd4f4a | -12.93389 | -54.80544 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa697428-c381-320e-a02a-74081b12d808 | -10.39286 | -48.57891 | 2025-09-11 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdbfdb94-c75f-3dc5-8d2a-9af179423613 | -14.57281 | -48.7695 | 2025-09-11 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68e57722-7c9c-3704-a535-bca1bd0a6b23 | -13.03702 | -48.01095 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de7074e9-601e-3c65-b682-c99bdd65fc20 | -15.55482 | -54.7692 | 2025-09-11 04:46:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 92bcbee5-0011-3929-9021-1240623f5f3e | -11.5485 | -49.04837 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b37d3c18-d01b-3875-ac6e-444f0e8b59eb | -9.90102 | -49.92551 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8130d214-9ff3-39c7-853a-6aea6b190497 | -11.90815 | -50.69287 | 2025-09-11 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ace90a15-0c9f-3639-8045-2b4c68febdd1 | -16.26767 | -46.78118 | 2025-09-11 04:46:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9def6831-e41d-3694-9511-29a45bd242a8 | -12.17847 | -53.87781 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23d48516-ceeb-3945-9534-7ea7af9cdaa0 | -12.82669 | -52.94079 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README104.md)
