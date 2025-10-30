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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6157ae14-8be5-3b8b-96c7-98ba3bb09fc1 | -9.89183 | -49.11638 | 2025-10-30 05:16:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cd0b2c1-ddce-35c9-a014-885bddb113e9 | -3.47447 | -49.9188 | 2025-10-30 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 227c1041-673f-303c-9d97-2eeb4e4f95de | -4.25427 | -50.66984 | 2025-10-30 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5e1c5192-8a71-38dd-9794-4879f2a5cc67 | -4.63991 | -49.48582 | 2025-10-30 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e5d61fc-28fb-30fe-a220-d9fe859a6f84 | -3.53579 | -47.55256 | 2025-10-30 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d670ad0-85d9-3a48-913d-9a89dabb6de6 | -2.72448 | -58.03086 | 2025-10-30 05:16:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a4aea2f-3371-37e5-8a02-f33653a939f1 | -5.40952 | -46.01491 | 2025-10-30 05:16:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 48829275-0cb4-3010-a6c9-5512ca6c4838 | -2.86797 | -52.79356 | 2025-10-30 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cab19d8-103c-3807-ab18-6015d97c0241 | -14.31746 | -46.53316 | 2025-10-30 05:18:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 61d236ea-084f-3afc-b599-64067bcc89f2 | -12.47967 | -50.56342 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ea647f9-4e0a-3d1c-bb81-6b2449886d78 | -14.33348 | -46.51656 | 2025-10-30 05:18:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 67d28333-5e81-3eb5-814b-a77d21879489 | -13.18057 | -48.43732 | 2025-10-30 05:18:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0d7fb60c-0a1f-311d-8380-1fe85457662c | -12.49147 | -50.55768 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| e3bb5faa-d42c-3d11-b9b7-d0ccfe5c1392 | -12.48557 | -50.56055 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 743f92f6-23db-3d24-beed-b2c5aad00ea0 | -12.47621 | -50.59222 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c97962dc-29ae-333a-bdfa-40af24fc6831 | -12.51883 | -50.56132 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0c1f205f-072f-30be-a587-a47353fc1ed9 | -12.51336 | -50.56059 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b3b19a92-e80f-3cb7-8df6-75d673dd2f0f | -11.06984 | -47.53907 | 2025-10-30 05:18:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d422f53f-3356-37e6-b70e-0629c73d0fe9 | -13.33822 | -54.31991 | 2025-10-30 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1f8521a3-33ff-38fd-9210-f1ac9d294684 | -11.95503 | -49.94117 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c13f311-8838-3337-b4db-4b3f3c5c2676 | -13.07392 | -48.21198 | 2025-10-30 05:18:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7d326513-a985-3238-9c1c-f0f3b3898fa5 | -12.31618 | -48.06575 | 2025-10-30 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e034c27c-9125-3e1e-a9df-a64a34afb1b9 | -12.51839 | -50.56493 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d290de55-36b8-3695-8f12-710b58a3c88b | -13.31997 | -47.47554 | 2025-10-30 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 91ad2f98-9179-3f3c-b050-7df099534a04 | -13.61411 | -47.58715 | 2025-10-30 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 670a09b7-5fc9-318b-a54b-44c6f9ddf737 | -11.07065 | -47.53249 | 2025-10-30 05:18:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57d87d36-4db9-393e-97be-a2a41c86b4ca | -12.47923 | -50.56703 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0ab72789-243b-3ea4-8e2d-9ad1b56c1ebb | -13.47935 | -48.00261 | 2025-10-30 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd70569e-1f42-3543-a49b-843b86f67149 | -12.88106 | -54.74153 | 2025-10-30 05:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ea4c099-f22a-359c-8f32-4645b6c31d39 | -12.49651 | -50.56202 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5088fd20-9860-3ab0-8ab2-382881ce719e | -13.36844 | -54.30945 | 2025-10-30 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c4ccf79e-19d3-379c-8a29-6ec0a02b3a19 | -14.32456 | -46.53459 | 2025-10-30 05:18:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b93147c5-052d-310f-a056-2fa6619d04dc | -14.32509 | -46.52895 | 2025-10-30 05:18:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| eab6235c-1b3e-353d-85eb-b661f0d09d30 | -12.88005 | -54.74914 | 2025-10-30 05:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe9df9dc-028d-3e81-8144-27fe0d94cb71 | -12.29437 | -50.33033 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f21d8bc2-fdbd-36a6-a33c-03b738eae163 | -12.50789 | -50.55986 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0e574b22-68d3-3282-a1cb-60eb09cded70 | -12.31744 | -48.05493 | 2025-10-30 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aed192ae-7b62-3643-b695-84f102d7e394 | -14.32106 | -46.53393 | 2025-10-30 05:18:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 388e4845-e2c4-3155-8e99-524b08209199 | -12.4729 | -50.57351 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| aece1546-1e4c-3244-b3a8-8c2e96e7f0ef | -12.52386 | -50.56565 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ec1a8603-1b38-3bd0-b355-4347a32bf290 | -12.88055 | -54.74533 | 2025-10-30 05:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d69f3e71-806f-3ecf-a447-76dd868ca72e | -11.07048 | -47.53362 | 2025-10-30 05:18:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8985e005-6832-3866-85f7-b11f9eb6daf9 | -14.32998 | -46.51698 | 2025-10-30 05:18:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 90e10d97-53c1-3f26-88ed-453d243a9583 | -12.4906 | -50.56488 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 7ccb754b-8e0b-3c08-b685-461cb94835c7 | -14.32164 | -46.52813 | 2025-10-30 05:18:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d910b331-1f19-3f12-9776-8c78aa2e794a | -12.30243 | -50.26299 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7f484ad-2213-3355-b07b-1c52f299f88c | -12.84712 | -48.62364 | 2025-10-30 05:18:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7140a568-1920-369c-a7a9-5184cd1d89da | -14.336 | -46.5292 | 2025-10-30 05:18:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b2f8cf6e-8cfe-3f87-acd1-dd7016c285a7 | -12.50154 | -50.56635 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0d4f6a8-716b-379b-ba45-5fbf1d3ac070 | -12.3183 | -48.06516 | 2025-10-30 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cafcd582-6524-35a5-9e66-8c94267e6286 | -10.8634 | -47.61575 | 2025-10-30 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11ceeb87-6308-3b9a-ad09-9090697257ab | -12.49607 | -50.56562 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f7a96c4-6d9e-3789-a587-78a2ab34414b | -13.16483 | -48.46388 | 2025-10-30 05:18:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a60c6965-cb9f-3a05-8a96-01e646779465 | -12.47247 | -50.5771 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c090237e-72d6-3519-8239-7b271b3ec548 | -10.86279 | -47.6211 | 2025-10-30 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc7a8982-4862-3797-8d06-2b4caec9def5 | -13.17354 | -48.44299 | 2025-10-30 05:18:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a44d5b9f-d0a4-3b7c-86fc-fa6f51c2f6cb | -13.28512 | -47.73104 | 2025-10-30 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d8e0293-54b6-3954-af57-4c49dca7bbc2 | -12.30333 | -50.25545 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ed4ce08-8ba4-3f87-949e-41e8a6643bea | -13.32772 | -47.46675 | 2025-10-30 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 956a18cb-3d72-3ce4-b3bf-5ab915bb6663 | -11.9555 | -49.93726 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e81e3556-f218-34e0-8ab6-bdc72780867f | -13.30781 | -47.7074 | 2025-10-30 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 19bfe7e8-8748-36c0-a9e0-daa2cc22bb27 | -12.31239 | -48.05989 | 2025-10-30 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 210eb4d8-fab7-3baf-8238-8b8f6d0976a3 | -13.47928 | -48.00198 | 2025-10-30 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d821fa7b-fe69-3e92-8841-94b8e5ed60eb | -12.19112 | -46.70545 | 2025-10-30 05:18:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6c2c740a-0ce2-36b6-b77f-dc99e47f277f | -12.52452 | -50.56781 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c0ab70b5-ad98-314b-a083-f7be8d22a080 | -14.24426 | -47.31223 | 2025-10-30 05:18:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c7cf4bd6-cf65-37db-a9f1-eb5d53c1ad36 | -12.3089 | -50.2562 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 178f119b-21d3-3bc1-b86e-3a59d41db8ca | -12.84811 | -48.62602 | 2025-10-30 05:18:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7ae2a193-6073-312f-bf36-3fa7daf2d72b | -12.36695 | -50.15194 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| becb54fd-62ba-33f2-9fa0-aa1d1921029b | -12.49104 | -50.56128 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b2b696b9-6038-3e6c-a596-d07b725bcc7c | -13.33507 | -54.31084 | 2025-10-30 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9bced45b-8a16-38de-8447-2174a233bddf | -11.8508 | -47.92634 | 2025-10-30 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47ad2748-a518-355e-8d55-706118aa4ca2 | -12.29482 | -50.3266 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 632c7512-0666-3d7e-9683-0a7df91fe54c | -12.5138 | -50.55698 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e4297c55-b8e0-3f38-a78c-c7c10ce8b97b | -12.50701 | -50.56708 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| dd43c1f6-099f-3da9-bd2b-ca85975f9bf7 | -13.27779 | -47.73696 | 2025-10-30 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 97453cfc-de62-337c-b35d-6407c184a63c | -13.48654 | -47.99559 | 2025-10-30 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1f8988d-4046-3879-b7fe-e11d255572d0 | -12.19038 | -46.71223 | 2025-10-30 05:18:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 72e1c5df-9a79-3070-99d9-9114ca1e5eab | -13.31928 | -47.48175 | 2025-10-30 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89915672-edc1-3fb0-b950-432c81e4d966 | -12.47333 | -50.5699 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4c10fe25-fc0f-3875-992b-9d6d9fda22e1 | -13.48666 | -47.99616 | 2025-10-30 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1f6c1ae-c1dc-3996-b6e1-f444be869c96 | -12.50833 | -50.55625 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 659dcf29-f2af-3fe4-8a73-7e14817aed87 | -10.91525 | -47.78807 | 2025-10-30 05:18:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1dcdbfa-95d3-37ff-9a8e-ccb273303669 | -12.52342 | -50.56926 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ff6ca5e2-20f1-32ef-a53f-3a5384ce45af | -12.33054 | -50.17043 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7af6ab89-b093-3f1a-bfac-b99df4a9ac50 | -12.87641 | -54.74471 | 2025-10-30 05:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e111df7a-75ff-31f1-8761-96c654fe754b | -12.69142 | -46.33024 | 2025-10-30 05:18:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dee66af2-f6d2-361c-bb22-3ffc2165a7ac | -12.47837 | -50.57423 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 68ced37b-9780-3ad7-9d70-8f8b19eb6413 | -14.33225 | -46.52966 | 2025-10-30 05:18:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7203c58e-6fcd-32b2-997a-7c4243351ab8 | -14.32932 | -46.52369 | 2025-10-30 05:18:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6a0909b3-d998-32ad-b25f-2b7a33ef25f4 | -12.88258 | -48.64538 | 2025-10-30 05:18:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a297ea84-4c41-3e0a-9d9e-4b943c0ae314 | -12.30198 | -50.26675 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| df27a339-bad4-3eb2-9b4a-3b66b5e10ebb | -12.84761 | -48.63044 | 2025-10-30 05:18:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 88c83eb9-add4-3715-8000-7afa3ade5ca5 | -14.33284 | -46.52332 | 2025-10-30 05:18:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8bbc25c7-e34e-36f0-b4a2-fdc68f6d566e | -13.03383 | -48.46031 | 2025-10-30 05:18:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7c24247a-1dcf-3618-83f6-c7b7d132a0f4 | -11.07004 | -47.53801 | 2025-10-30 05:18:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50f1860c-5a44-3127-85a5-63f85b395c6b | -12.37091 | -50.15039 | 2025-10-30 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cbed0cf-86c1-3954-97d9-2b74702dc0c7 | -12.88301 | -48.64149 | 2025-10-30 05:18:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f1bcf3b-e107-3b36-a6cc-f8e7ccdb3fc1 | -13.3679 | -54.31358 | 2025-10-30 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e9f6afdf-0e2a-326a-8541-6fd83cb2408e | -12.31317 | -48.05275 | 2025-10-30 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README65.md)
