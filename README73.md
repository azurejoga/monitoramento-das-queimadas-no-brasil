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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6437754f-0d6b-32aa-8b15-7f28cc97f5cc | -11.27798 | -54.1151 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8aee218a-aa60-39ef-b5fc-28533aa7030b | -12.8955 | -52.0909 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75d7f557-ae0d-38c8-b0d7-15a92acababb | -14.04624 | -52.0551 | 2026-09-22 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0ff42aea-0bf0-3648-85ec-0f1f73878611 | -11.87979 | -46.85178 | 2026-09-22 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f5834f5c-df7a-3958-82a0-3514bbbf276b | -13.86864 | -48.5745 | 2026-09-22 04:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50aacb94-17aa-3fbe-b7dd-3c201bc292e9 | -11.83832 | -47.61292 | 2026-09-22 04:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed0280ea-fc86-3ab2-8cd4-b665bf1e56bb | -12.39818 | -46.52003 | 2026-09-22 04:49:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1f0f7c3f-f568-3b65-860f-7ea62f7e2a20 | -14.16122 | -51.78781 | 2026-09-22 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9f1e20d-6f43-3312-86cd-7b6d89059a5c | -10.90462 | -53.9667 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7e95c9d1-b087-39c6-bd04-6a90a7c69128 | -10.98203 | -50.59452 | 2026-09-22 04:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28701ea6-e023-3d0d-b171-462594735272 | -13.91298 | -48.56531 | 2026-09-22 04:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8b99abfd-f168-3030-ac0a-5515088bdc90 | -11.43941 | -47.34002 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 15a5e12a-8f97-3acb-88db-7ed8ccf8f338 | -11.84355 | -48.84344 | 2026-09-22 04:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c88b4e3b-bba9-35bb-ae74-a8267dc19152 | -10.86904 | -57.17012 | 2026-09-22 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 57f7e38a-9184-3458-921c-131237e4c4e1 | -10.52269 | -56.7877 | 2026-09-22 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ea6bc121-aa41-3869-a3de-87a94282bcb7 | -11.16345 | -51.10607 | 2026-09-22 04:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 77f77e90-8145-3795-b99b-1ff5b803ca65 | -14.17806 | -47.87608 | 2026-09-22 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dfaddc48-9f50-3304-ad0c-2c83c70100de | -9.55957 | -66.02779 | 2026-09-22 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72ee4e5f-f51d-3a21-bd51-01a06e01126c | -11.94264 | -49.77103 | 2026-09-22 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 753b918d-d997-3034-97d8-edaa87786f08 | -13.21885 | -46.93579 | 2026-09-22 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ffd8a21-205c-3c10-b45e-07973e2ca408 | -12.56782 | -45.96527 | 2026-09-22 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 66cb5ad5-cebe-3fb8-b1a7-fcdb2adcc5f5 | -11.28137 | -54.11567 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 195537a7-76c9-30e4-9d68-19a1dbd22331 | -11.68677 | -50.99038 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 144a065e-cc68-3c8e-98b2-0122280d34b2 | -13.87312 | -48.57039 | 2026-09-22 04:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 359bbf24-5f6f-3561-bde8-e57fe2e91f51 | -12.19849 | -47.04283 | 2026-09-22 04:49:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0b27cae-a6f9-349e-9951-b191fb1c5444 | -12.85326 | -54.04293 | 2026-09-22 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ab14940-c179-3554-a771-e097866fb156 | -14.68974 | -45.67802 | 2026-09-22 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f88e5d19-938e-36fc-9a60-d94d3b64087a | -10.60489 | -53.9939 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| db594670-c1b4-3a25-9fa2-5f7e90a1194d | -11.99485 | -52.46234 | 2026-09-22 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7dfffad-c0a5-3913-b2ab-2b836ca03e6f | -10.18319 | -59.44815 | 2026-09-22 04:49:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a067476-3e4c-3bc9-b2f5-548e09d9878d | -12.57057 | -45.97947 | 2026-09-22 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 5788389a-fda2-398f-9f9a-620463d3cb8b | -12.65661 | -50.95029 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9c86422-6c27-3f4d-ab82-6f805776c95f | -13.54265 | -47.66153 | 2026-09-22 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ff900fe-b3d0-3d7f-b6f9-37fc476969a4 | -12.93351 | -51.01568 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43d6d065-2ee6-351b-9df1-0a14c45830c3 | -12.43241 | -47.08427 | 2026-09-22 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d31be12-d5bc-3fc5-a69c-7a1110f4932b | -12.43341 | -47.07667 | 2026-09-22 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d03e8f87-5e12-3e3f-8e71-11bb21f39c5c | -10.95547 | -54.36744 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bfbfd2c0-3d57-3b72-a358-6c59113a8517 | -12.56895 | -45.96731 | 2026-09-22 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 84a9c549-8c1b-3033-b3fc-3d3a006e693c | -10.60709 | -54.00192 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12f9411b-5993-306e-9d16-69daf577b082 | -16.67632 | -41.84908 | 2026-09-22 04:49:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e1dee3e6-7dff-3e91-9a02-7dc802727a7f | -10.59129 | -53.99162 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5199e86-8cdf-3137-8d1a-a3ae1c0f99cc | -13.36723 | -51.30828 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d68436a6-24a5-3f4c-9f73-37526ebf94b8 | -12.40961 | -47.07755 | 2026-09-22 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cca60e54-09ab-330b-a763-9815dcf16501 | -12.53502 | -50.07143 | 2026-09-22 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fadb4a43-2487-3a05-a622-00c1cbdb4fc3 | -12.56611 | -45.97886 | 2026-09-22 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 29b7f467-3821-30ac-9615-86e830e8ba66 | -11.75433 | -50.81706 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7496068-1676-3876-9b40-4e86117d6c6d | -15.35962 | -48.1018 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8dd7e93a-cc13-36e3-8b7e-64f649a35b6e | -12.14192 | -47.39185 | 2026-09-22 04:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 83ac94b7-f3f6-3d1d-9605-b9e2f513fcf5 | -11.00906 | -53.99496 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51b38f30-65de-3499-9a24-267d18593006 | -14.58941 | -52.17065 | 2026-09-22 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd90a8cc-3531-3e43-9c3e-50f006bb3205 | -12.6764 | -50.95718 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 68f6e0f9-e517-31b7-91c3-29c0d6619dff | -12.56268 | -45.98027 | 2026-09-22 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41e7bc60-9902-3022-9c9f-bea4e3039971 | -12.02009 | -47.80622 | 2026-09-22 04:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e6f776cb-56a8-3d0b-bbe1-fd32f34a935c | -10.60889 | -53.99074 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 458c6f5a-0292-391f-9202-81082e22bf2f | -11.32123 | -54.04225 | 2026-09-22 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 08950477-489b-38ee-b4fd-8f41d5a1dae4 | -11.28091 | -54.05464 | 2026-09-22 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e2de834-d708-3486-889e-ea6dbc7a8e5a | -9.39991 | -65.92163 | 2026-09-22 04:49:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ab0a28b0-349f-3e24-97c3-74f06158a6f9 | -11.01397 | -54.13706 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37202cd7-6843-360e-a2f5-8d2a0fe364d7 | -15.83012 | -56.79208 | 2026-09-22 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| baa77f48-bec7-318c-ba13-87ace6d73b4b | -10.90597 | -54.06603 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85d3b279-0177-3ac7-b601-d3d62383b7b1 | -10.60669 | -53.98273 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 2b21fa7c-6fce-36c4-b481-c68b325d21a0 | -13.37115 | -51.30513 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80a20e42-89cb-313f-9ad3-d6ef1096e1fa | -11.31784 | -54.0417 | 2026-09-22 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 83c25460-51e3-39f8-9030-26fe71487841 | -12.84096 | -50.97831 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f7e7005-801a-3ca5-8721-ae16698f1b27 | -14.68097 | -45.67169 | 2026-09-22 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2d78931b-cbb3-3cb6-af4f-4dc4ffa91664 | -9.55536 | -66.04915 | 2026-09-22 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b125f489-064c-356b-8cf9-84d0a544305b | -14.92206 | -49.93994 | 2026-09-22 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d84b4e20-bccd-3c38-b25a-ee24ead94ffd | -11.87668 | -46.84346 | 2026-09-22 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ddf2bd57-7384-380a-a48e-f39bb2a2b2e7 | -12.35023 | -50.17733 | 2026-09-22 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf1cf3ff-2e9d-33a1-9308-cd3848805ea2 | -11.00846 | -53.99867 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe81e872-add3-3a21-b58e-ebe4882534b9 | -11.31864 | -51.35756 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5e92214-9c43-360a-a7fc-35e796e25dec | -9.27913 | -60.62432 | 2026-09-22 04:49:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc666217-04c5-3b3d-bc8f-d44bb2593132 | -12.83756 | -50.97778 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e990a19a-8c02-3f15-8a27-885ddf2b11df | -13.29451 | -51.79221 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f976894-ef0b-3ed6-a826-9f5054a12b0f | -11.41967 | -47.35234 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3b4aba4e-ec70-3538-85e7-73cfdc774ca8 | -9.12367 | -65.86469 | 2026-09-22 04:49:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d6b2ef1f-319a-3bea-bc3f-64ab71940370 | -12.40548 | -47.07698 | 2026-09-22 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f02d3f9e-b83d-3d33-bea8-ed52c1b8e255 | -10.72233 | -54.00551 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7b62276-bb53-32f4-b644-ba96bd28d1da | -13.62883 | -42.48246 | 2026-09-22 04:49:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a3e86456-297a-3285-a99c-5a1aba555077 | -9.12711 | -65.86549 | 2026-09-22 04:49:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b3582893-4362-308d-9fd2-18571370a830 | -10.38394 | -54.40067 | 2026-09-22 04:49:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a3ac25f-3fc3-34ac-9bf2-5e11bc5a2067 | -13.02404 | -50.5961 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4b54442a-09f2-3f83-a8c3-691fc1980021 | -10.60729 | -53.97901 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 0fd414cb-59d2-399d-9784-804dc996fd73 | -11.59445 | -46.78785 | 2026-09-22 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b1ca125-af8b-3f1b-8599-ae78392e35fb | -11.03661 | -54.14851 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 08d83624-455a-3ddb-8294-4e136534e5ab | -11.01216 | -54.14828 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fd4158a-794d-3641-9eae-3171f1759cab | -11.69632 | -50.9956 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 7d3d8863-c8be-386e-92dc-ea5d8f331457 | -13.86024 | -51.84831 | 2026-09-22 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95fafbca-00fc-3853-bc83-11a4832cfb51 | -11.32864 | -51.35913 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29206422-786d-33a0-b457-4e98b0dc6056 | -9.76439 | -65.06403 | 2026-09-22 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2d62389-4234-3bfd-a429-057fa5a6ee46 | -12.84323 | -50.98628 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4032d129-843d-386f-a243-55f81b6a0700 | -10.60049 | -53.97789 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 7d4ae6e7-f795-3a43-9abc-8338d9d3a91f | -10.58228 | -53.98255 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8d11100-e2a8-3a5a-a7e9-e446cecbf690 | -10.61629 | -53.98814 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 6cfb5ffa-7ae5-34d1-86d6-1c7003b05047 | -13.90146 | -48.56357 | 2026-09-22 04:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c82d62cd-2faa-3c46-8a09-c62a1993400a | -10.86964 | -57.16662 | 2026-09-22 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6571540f-3118-377f-844f-3526e14ffaa5 | -13.96269 | -47.8419 | 2026-09-22 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a66a86c-81fe-33eb-baed-50dc2fa2fbfb | -13.62926 | -42.47852 | 2026-09-22 04:49:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 114adf9f-06ef-3842-bad8-ea8a929af2a3 | -12.86773 | -50.94441 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ac29d3d-9e06-311d-a799-dd9fbb970d58 | -9.28069 | -60.62739 | 2026-09-22 04:49:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README74.md)
