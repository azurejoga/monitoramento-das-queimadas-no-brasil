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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51f8aa06-2a67-3099-90b7-664cef5daa8e | -12.68289 | -51.17817 | 2025-10-11 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e3b4c662-39e3-3934-b08b-cf8891a07bdb | -13.30893 | -47.98177 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dfc50327-48ca-3757-a06a-33c40675fe75 | -9.44594 | -45.45709 | 2025-10-11 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d187d7a1-1540-3e85-9a36-65c39f8f969e | -13.46013 | -47.69563 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f928e79f-113d-3d1c-a9db-6f34481fbe0d | -13.46173 | -48.09945 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f5b896c-d4f7-3af9-8a9a-6e0fc4f01f48 | -10.38114 | -57.64324 | 2025-10-11 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b2477c2-5436-3d10-b5b3-822018a33c70 | -12.77005 | -48.66684 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 52595350-ee1d-3d13-8479-3fe463d58d3d | -15.40866 | -47.30493 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d12d4edf-113d-3986-9ac5-75004f51c426 | -10.20039 | -44.59637 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 41eb51eb-baaa-31b8-a25a-e665346f1795 | -13.28993 | -47.99376 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 945753c5-e7bb-3351-817d-d304d035bb83 | -12.63718 | -48.31374 | 2025-10-11 04:34:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 71cd50bf-c869-34d6-9cf2-89b894f41ce5 | -11.75035 | -43.38706 | 2025-10-11 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73a87200-237c-359b-8204-b79ee5b7157c | -9.81719 | -45.52114 | 2025-10-11 04:34:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| beffffc9-f400-354b-b8af-5b0b39772e1d | -10.19835 | -44.61031 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| de2a6375-9bee-3401-b7d0-d93e752f0c22 | -13.2972 | -47.9912 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fe6bb89-ee86-37ae-8b91-5d38a6558fb0 | -10.6146 | -47.447 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb2eca1f-6085-3199-92f7-cabcfd4c395e | -14.74683 | -46.13041 | 2025-10-11 04:34:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb6a9fbb-42d2-3570-81b6-105743ccad8d | -14.95362 | -46.74973 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 43110552-fcd0-341d-a4f1-d2e7978b8622 | -14.01877 | -47.06393 | 2025-10-11 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ffda57c-5036-34e7-9a97-5ce75831b7d8 | -13.20643 | -42.34427 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 22.9 |
| 540aded1-8734-3106-8084-1f6f0c63b7d8 | -13.46133 | -47.71083 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1af44dbc-06c9-3eed-a93d-037f5b2d94d7 | -16.30074 | -47.15971 | 2025-10-11 04:34:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a240cc99-dd5d-3804-825a-ee074b091a9a | -14.65681 | -56.20747 | 2025-10-11 04:34:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1f11747-9798-355b-9a4f-1e583a495eee | -12.23667 | -51.13097 | 2025-10-11 04:34:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ccb3966-11d7-3447-8587-1d62fc869f9f | -11.16017 | -49.8183 | 2025-10-11 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a22ce873-d443-33a8-9693-83ca752558e8 | -13.29616 | -47.12453 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6b341ee2-980c-3f32-ba71-5cd671d79eac | -13.27946 | -48.00372 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce04c79f-dd2e-317d-8288-f1daa5c6a524 | -10.20049 | -44.59353 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b038f7f0-fe15-33f5-b3fe-877e5e5f40a3 | -14.32443 | -44.67754 | 2025-10-11 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2cb4a851-83f9-3823-91ed-7be91e82d62f | -13.38021 | -47.7363 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2773d9d8-6dab-3926-b3e1-19a7e4cb98e0 | -15.71026 | -46.6345 | 2025-10-11 04:34:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e59b34c5-d594-3314-b234-486c85fadc98 | -12.74876 | -48.64915 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f032601-f71f-323c-87b7-066d562b0c12 | -11.02521 | -44.64411 | 2025-10-11 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1c0fd87-7cef-3993-a7a6-a445a75d3086 | -10.52546 | -47.34018 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 836e823a-b467-352d-aca0-35f1c0827cd6 | -15.4271 | -44.28204 | 2025-10-11 04:34:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f51647e9-0813-34f8-b2d9-c8d37db6aee7 | -16.29894 | -43.08374 | 2025-10-11 04:34:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ff98713-1768-3f66-bcf1-40132831c753 | -9.51177 | -47.8757 | 2025-10-11 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab947a8f-4c81-358b-8bea-2348ba25c00e | -8.58954 | -48.20715 | 2025-10-11 04:34:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b9ef242-8eff-368c-9c0c-8c191ff2b789 | -12.74822 | -48.65266 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b049926d-7dcc-3f1b-a0ac-71ac5e186654 | -11.87897 | -45.48896 | 2025-10-11 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37d1015a-4f87-343a-a79d-d4717151ed0d | -8.95047 | -48.66231 | 2025-10-11 04:34:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0350d675-c2f3-3e5f-881c-8326b4b10335 | -9.12045 | -45.06971 | 2025-10-11 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aefe3121-8d42-37bc-a93b-db3594e29496 | -14.89893 | -47.22669 | 2025-10-11 04:34:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 590b5031-ff83-3c30-a3e0-70dde61752bd | -11.12118 | -50.57336 | 2025-10-11 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c23567a0-7289-3f53-9863-5d8f05ca905b | -13.49364 | -48.1078 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d90287b1-5da0-3f80-8c1a-1ed97a15b870 | -13.50827 | -48.12471 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00ce6650-f783-3fb8-8392-22126fa13f8e | -13.26378 | -48.01637 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 395f7d0b-a9c1-3625-b973-24b21849cd93 | -14.93049 | -46.75817 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1fa0314-54a7-3831-bb2f-f47952b11828 | -10.51652 | -47.35368 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0f3f2e40-cedb-3869-b723-a34b2a7370e0 | -16.29898 | -47.17205 | 2025-10-11 04:34:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5ae4a163-5e2b-354c-9f41-52747be6dd92 | -12.81574 | -50.51346 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2bbe362f-d02a-34dd-85fe-0acf4eaefa88 | -15.70789 | -46.625 | 2025-10-11 04:34:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8a788f2-67f2-365e-8f89-17852aa39f78 | -13.31229 | -47.98234 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7056d75-d86e-3b20-b625-10d789d0969a | -14.95065 | -46.74494 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1eeadaeb-2800-3b90-8c07-670a79871786 | -9.90659 | -45.55104 | 2025-10-11 04:34:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e16f4460-3051-3b23-bf5b-33b8d0d8d753 | -12.63609 | -48.32083 | 2025-10-11 04:34:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a7496a6-5309-348e-a18e-3308766a2df2 | -13.53677 | -48.11805 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19fc1ced-4d2a-323b-ad97-ee28a8b1454b | -13.41118 | -47.26656 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c256575-73b5-31ca-a490-94d84dcce0e2 | -13.37627 | -47.7395 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 359702e2-3bb8-3da9-ad73-1a72937523f5 | -13.2841 | -47.13427 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1e878b51-2ab1-322f-abd7-5eb726893fc7 | -15.78839 | -43.6558 | 2025-10-11 04:34:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9218b80f-e1f1-3b53-8bce-7342cb7f5205 | -15.58255 | -44.01936 | 2025-10-11 04:34:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0da49da-6c6e-3948-982e-34e47819335c | -13.30833 | -48.48249 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86665fa8-fc96-3fee-93ea-370cca92e790 | -14.28269 | -45.89538 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df6d994b-5ff9-318c-bff9-c79c5e28beb1 | -12.75072 | -48.66011 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e80c36ae-0e4c-3d72-a56b-7cd0c00b70cd | -12.74491 | -48.65215 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59769cb5-a072-341d-8c75-9f08649c720b | -12.7518 | -48.65305 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f71434b9-083b-399d-a92b-13475b4aa8e7 | -9.2604 | -44.37949 | 2025-10-11 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7502c359-c648-3ee2-a638-da8aeecdfaa7 | -13.42031 | -47.25241 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da2c16ca-5048-3e64-a33e-bdb6214b9a90 | -15.7563 | -48.96474 | 2025-10-11 04:34:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e52041e4-3991-3c71-b858-340daeff7bd1 | -14.92988 | -46.7624 | 2025-10-11 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a69357cb-1eeb-355a-8b01-03eacaed8ec5 | -12.22267 | -43.78682 | 2025-10-11 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbcf1671-9bbf-3113-8001-211429cd60f4 | -13.21605 | -42.34315 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 41.4 |
| a8b4df8d-9076-3e46-bb2d-c4aec04c36e6 | -10.42913 | -44.99471 | 2025-10-11 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b6aa76e7-9199-373d-a0c6-17d3cc362866 | -13.38062 | -44.34648 | 2025-10-11 04:34:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15ce8b98-4caf-3e44-ade4-b9e4b9a0a1ab | -12.90569 | -47.03536 | 2025-10-11 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e5e6e2e-b08a-3c10-b57f-a6db3a73fa73 | -15.9093 | -42.56606 | 2025-10-11 04:34:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5839734e-f931-3211-8ebe-32304a184420 | -13.8468 | -45.80717 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e8abb0f-0ec3-3e5e-b6ad-7805604833a1 | -12.23728 | -51.12721 | 2025-10-11 04:34:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2891ea3e-9bf0-300a-8ecf-8ad98c82752f | -14.74315 | -46.12987 | 2025-10-11 04:34:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 169c8d46-495c-3214-a2a6-bdaa2404e03d | -13.30955 | -47.12175 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 30ffe11b-5acf-36b3-8c94-00f8323f090f | -13.31386 | -48.49089 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f448b94-4a06-33d6-97ad-14dd8ec9a039 | -13.40508 | -48.04169 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d25dffce-694f-3f3f-96be-0bb06abc1f17 | -13.8351 | -45.78232 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3342b8b-f1b5-30f2-bb36-82debbf8afcd | -10.55624 | -47.31907 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47762c8e-9e51-380b-9154-fcc1d6c2578c | -13.28281 | -48.00434 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5eedf98-cadc-3c6e-b4fd-71786602a396 | -12.76079 | -45.8819 | 2025-10-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 47e00505-f985-3ea9-afda-4fe4d579a858 | -12.74436 | -48.65566 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 03fc624b-bc24-3782-a8f1-c302d636152a | -13.30362 | -47.12195 | 2025-10-11 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 58cb8075-0194-39c7-8898-e59b263dbc34 | -10.37599 | -57.64228 | 2025-10-11 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49d6a942-c130-3eda-a897-02f86f604745 | -11.9211 | -44.92265 | 2025-10-11 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1a0bd43-70b7-3566-b0f0-f4e7e8c34514 | -13.49028 | -48.10727 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05c86d20-3190-3410-a461-a0861accafd8 | -12.69124 | -51.19114 | 2025-10-11 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fcc6a06-cc1d-3d1f-9bc3-3c1fc283fb99 | -9.40073 | -42.6722 | 2025-10-11 04:34:00 | NOAA-21 | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| dced2e68-68f8-3f8a-b13a-6010b6dd190a | -14.08051 | -47.11621 | 2025-10-11 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d4e9506-6b54-3de9-810d-c46192542b65 | -14.27525 | -45.89441 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9bdbccf-7cad-3b45-8caf-94aa9bf84ca8 | -13.45611 | -48.09119 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d751b23-658a-3821-95ea-315b939d87bb | -10.20283 | -44.60619 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7b048b32-a9de-324f-90a2-ec05cf2f756d | -13.4446 | -43.68744 | 2025-10-11 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af942ae3-f346-37f3-b0b0-fa5d650c762d | -10.6638 | -44.44511 | 2025-10-11 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README27.md)
