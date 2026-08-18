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
| 29e04436-7910-33d5-957e-7607837c1a76 | -9.90298 | -47.73665 | 2026-08-18 11:55:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7e4c356b-a7e9-3596-9d5c-3154ff096e35 | -8.60445 | -50.34021 | 2026-08-18 11:55:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 665ebd88-8ba9-396b-be11-bcd280d3ba15 | -11.10279 | -47.23639 | 2026-08-18 11:55:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6704ba8f-6bdb-338d-97b3-49d66aa9acfb | -9.40014 | -48.24795 | 2026-08-18 11:55:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6d2877cd-5589-328f-a838-904a3da6e0d3 | -8.57625 | -54.71078 | 2026-08-18 11:55:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| ec94afcb-64d4-326b-8f75-016e777632e2 | -9.79665 | -47.30314 | 2026-08-18 11:55:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 9264d5ac-6df3-3a34-9c7e-f7fdb5079541 | -9.8674 | -46.77594 | 2026-08-18 11:55:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| f0c35459-9dcc-35b7-960a-d7d9dec0dd0a | -8.37007 | -46.36041 | 2026-08-18 11:55:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 5a420ae9-8f3e-32f4-a59b-22ece8880e71 | -9.46858 | -51.61035 | 2026-08-18 11:55:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e1f4686c-94a1-31ba-8857-f7c2c9e5aead | -11.35795 | -46.39009 | 2026-08-18 11:55:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 1f755eb0-a43f-3ddb-bb15-27af46c4382f | -8.55989 | -47.39193 | 2026-08-18 11:55:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 914cdc62-8b63-3924-ac2a-3e1455cbe46a | -9.76974 | -47.28907 | 2026-08-18 11:55:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a48f8bcd-8cc8-3cdd-ae2e-dc9f2fc0f673 | -8.57886 | -54.69461 | 2026-08-18 11:55:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| a41a1886-34c6-388e-a03c-0a2bee1642dd | -9.06553 | -50.84348 | 2026-08-18 11:55:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| d1fc0e67-9969-3c61-9681-61b4f385b81f | -8.37159 | -46.34911 | 2026-08-18 11:55:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 655828b4-96cc-336b-a47a-21fa39f3a472 | -9.76838 | -47.29926 | 2026-08-18 11:55:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 19f267df-0d6a-3af9-bf7c-5b5b1b012948 | -8.21827 | -55.02865 | 2026-08-18 11:55:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c973e06c-da6a-3006-8c10-6397ae3e251c | -9.76556 | -46.7008 | 2026-08-18 11:55:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 1c28cfdc-fcfa-3cce-b8ee-7ed8a0d6e348 | -10.31106 | -48.25422 | 2026-08-18 11:55:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 74276318-9ccf-3ccc-b7ad-738c8fb2f9fd | -8.58534 | -54.72903 | 2026-08-18 11:55:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 221.7 |
| a6c7b17a-ff5e-37d9-aa12-2a5146ed6d1d | -11.11953 | -46.49204 | 2026-08-18 11:55:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 0d0de594-0dcc-31ac-9e5a-687feae66d7b | -11.1976 | -49.6904 | 2026-08-18 11:55:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 75c655a9-1b20-326f-982b-44584db11054 | -10.76706 | -50.37131 | 2026-08-18 11:55:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 9811ab6b-7b69-3e65-91e8-c92afc74e69a | -11.19887 | -49.68145 | 2026-08-18 11:55:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fc77a605-fc5c-32cd-937f-a0b8c828d1c3 | -11.35753 | -46.38342 | 2026-08-18 11:55:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 9e6ddaf3-e0c6-3f6e-b1a5-267f69eea235 | -9.71455 | -48.37277 | 2026-08-18 11:55:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 39428dc0-4b9b-3487-a248-891d9c089a9e | -11.10155 | -49.90744 | 2026-08-18 11:55:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| d14239b0-9a85-3474-a7d3-ca6c0e1259f6 | -9.06826 | -50.82473 | 2026-08-18 11:55:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 7f434033-1eea-36fa-a6bf-88a839d7a969 | -10.31236 | -48.24479 | 2026-08-18 11:55:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| baa6d74f-d2bd-30a2-8d68-8d44470f8cec | -9.9043 | -47.72685 | 2026-08-18 11:55:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3007f2ba-fb34-3e78-8689-6e583c59e003 | -8.58796 | -54.71267 | 2026-08-18 11:55:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| c559d47c-8ce3-3ec3-920d-ac25f47d8d6b | -8.50004 | -48.81635 | 2026-08-18 11:55:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 77af0a9c-170f-3a65-87cb-54210d4d584f | -11.03089 | -47.01132 | 2026-08-18 11:55:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| daf9ca12-ce21-3aed-af07-e05e5154c175 | -8.57361 | -54.72711 | 2026-08-18 11:55:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 160.4 |
| 7a72344f-04cb-3086-84f7-1f86c4c1381f | -9.72084 | -46.11141 | 2026-08-18 11:55:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 1f1bfbf7-86d5-3f5f-a718-340be0aa0f39 | -9.0669 | -50.83408 | 2026-08-18 11:55:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| f3d4915d-9475-3ae4-9292-570049275a6a | -11.35632 | -46.40227 | 2026-08-18 11:55:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| aa857dc1-72ac-3cf3-852f-de04ee3b46b7 | -9.00236 | -45.83278 | 2026-08-18 11:55:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 775e4d38-2e1b-3172-bf90-2c7849a43239 | -8.58795 | -54.73927 | 2026-08-18 11:55:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 31ca1ae7-f992-3bd4-b231-bd69c7a5ed9e | -8.5787 | -54.7211 | 2026-08-18 11:55:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 143.1 |
| 2004d6c3-150b-360e-8985-d8defe5c54c9 | -8.59403 | -50.342 | 2026-08-18 11:55:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| a4b870ca-4fb2-303c-afa6-aff405955092 | -8.59271 | -50.35114 | 2026-08-18 11:55:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 61f1aa7f-714c-3bc6-9ed9-974a4d735b20 | -8.63744 | -54.70346 | 2026-08-18 11:55:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b86eef2f-9dc3-38aa-9881-77cd10a0e359 | -9.43491 | -48.26213 | 2026-08-18 11:55:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 2495798d-619c-37cd-a5d9-35a3130b3f32 | -11.35907 | -46.37127 | 2026-08-18 11:55:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 4550e5e7-bf84-30c9-a59b-74ac6ec85c3b | -9.12783 | -45.95966 | 2026-08-18 11:55:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 86cca4d3-78d4-3454-b719-c43583468a23 | -8.73109 | -48.22489 | 2026-08-18 11:55:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8b8ba6f7-5435-3560-a3c6-ec2fc74d8bfe | -8.58275 | -54.74519 | 2026-08-18 11:55:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 27cc5b8c-4698-3b7e-bdff-a3a1e33b9ad4 | -8.59042 | -54.72304 | 2026-08-18 11:55:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 164.8 |
| 07f52dd9-ef63-3b27-b2b9-ee1b8e6c81d6 | -11.3355 | -45.9145 | 2026-08-18 11:55:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 9b099a42-d1a3-3e3a-a39c-71f6a1428b87 | -9.12702 | -46.04471 | 2026-08-18 11:55:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 41bfadf3-862a-3aec-b106-418323ea6420 | -8.49877 | -48.82527 | 2026-08-18 11:55:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 344f6945-0efe-3954-bdb4-652b76c12da3 | -11.10422 | -47.22574 | 2026-08-18 11:55:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| de337ec2-68d6-3174-bcf5-ad52a6d9b324 | -8.60311 | -50.34935 | 2026-08-18 11:55:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 485e0497-a61b-3126-9204-d5149a03fff7 | -9.86596 | -46.78677 | 2026-08-18 11:55:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| eb9e9ce5-875b-3773-841f-6277d9634cd8 | -11.54414 | -46.21418 | 2026-08-18 11:55:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5d5af4bc-e34a-3c2a-b639-7d4e22f73afb | -8.56697 | -54.71919 | 2026-08-18 11:55:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| b1870fd2-7a37-3426-83fd-89bd4f1e19a8 | -9.12625 | -45.97178 | 2026-08-18 11:55:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 304c57bb-1959-381c-a379-9ff7b24c20e1 | -10.77593 | -50.37259 | 2026-08-18 11:55:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8dfdb7a8-a38c-3760-8a14-832e9c7862d0 | -11.35957 | -46.37798 | 2026-08-18 11:55:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 27f31196-af74-3b0c-afb8-0783d71b9dd5 | -6.71283 | -58.94529 | 2026-08-18 11:55:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 5b26a946-d1e6-38bb-a241-6e737d31cab3 | -14.03505 | -53.67526 | 2026-08-18 11:57:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 1ae66561-6776-3780-9d95-d488639cea7c | -16.09266 | -45.12664 | 2026-08-18 11:57:00 | TERRA_M-M | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 23.0 |
| d4c02843-74ce-3336-8705-04c006787331 | -14.81566 | -46.62101 | 2026-08-18 11:57:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 7a5c200c-23c1-32fb-991f-41a58a4ebaf1 | -17.45907 | -47.86107 | 2026-08-18 11:57:00 | TERRA_M-M | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 187bfa55-f63a-3861-ab3b-9b92687e4f95 | -12.78033 | -48.4396 | 2026-08-18 11:57:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 173.7 |
| d2f76680-c40c-32bb-a76c-653561d9576b | -14.19341 | -52.9048 | 2026-08-18 11:57:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 76a386fd-83b1-3da9-8488-3a640d60d3cc | -14.17102 | -53.05238 | 2026-08-18 11:57:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b8ea6371-8141-30f9-8339-1fdefe81fec7 | -19.25553 | -45.33028 | 2026-08-18 11:57:00 | TERRA_M-M | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| cd47d5f6-eb73-3312-be42-48b8a6c2f767 | -16.27072 | -49.29725 | 2026-08-18 11:57:00 | TERRA_M-M | DAMOLÂNDIA | GOIÁS | Brasil | 5206800 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9b75617a-6a36-3556-8e43-7f6b32666f1e | -13.93343 | -53.93067 | 2026-08-18 11:57:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 924d4f93-646a-316f-98e8-ef5cffd9bf82 | -14.17134 | -52.92275 | 2026-08-18 11:57:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 91543e56-b0ac-3639-aa3c-590935800a48 | -12.52788 | -47.86797 | 2026-08-18 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| ba54211c-01be-3a51-b6a1-dd08c427231a | -12.26895 | -45.86627 | 2026-08-18 11:57:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 4f5551d8-d25a-3691-a512-c30690cf9f0b | -12.70647 | -48.51182 | 2026-08-18 11:57:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d96c5979-494c-33cc-9124-10a74077d408 | -13.28186 | -51.65728 | 2026-08-18 11:57:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 4882ed14-802e-31d8-b7fb-dc5e7ea96cab | -13.28949 | -51.66818 | 2026-08-18 11:57:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 82a39261-281e-3763-9641-6030273e8134 | -15.40576 | -51.06711 | 2026-08-18 11:57:00 | TERRA_M-M | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ac1f79c2-25e0-37cf-bda5-ce0b4d22a237 | -14.16189 | -52.92122 | 2026-08-18 11:57:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 154.5 |
| b49110f1-f7ec-3da6-ae86-2be6e24082bd | -16.30152 | -45.10924 | 2026-08-18 11:57:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 37c35045-f324-32c9-a352-aaad729676ed | -12.7817 | -48.4295 | 2026-08-18 11:57:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 38.9 |
| e85e01a9-0271-3a62-adf9-fd4a69121bf2 | -12.78953 | -48.4409 | 2026-08-18 11:57:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| b800f3fe-a177-3da4-b296-6fc0f6be7a18 | -17.94971 | -44.43055 | 2026-08-18 11:57:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 6e2113c6-5e6f-3be8-ae5f-77e0bc358930 | -13.46329 | -51.80076 | 2026-08-18 11:57:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 68d96381-4b3b-32f3-94b3-b6ef547682a1 | -12.77901 | -48.44935 | 2026-08-18 11:57:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 09d5c4d5-312d-358b-8069-253747cc06e0 | -12.54153 | -47.83832 | 2026-08-18 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ed3da18e-6469-39d4-ae21-e49938116907 | -16.09066 | -45.14463 | 2026-08-18 11:57:00 | TERRA_M-M | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8ee6f566-9531-3c6c-8f50-c0afce1b11d2 | -14.16975 | -52.93312 | 2026-08-18 11:57:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 1dc20b62-b433-35cc-9d92-d02755a0755f | -12.77117 | -48.4381 | 2026-08-18 11:57:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 00c3b0ce-afbc-3402-bf97-ae3783a4d7df | -14.18054 | -53.05385 | 2026-08-18 11:57:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4b395039-1ca6-3164-aced-cd58b5f48d5a | -14.1635 | -52.91071 | 2026-08-18 11:57:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 51.3 |
| c1b8513e-733f-3e49-a231-38e53b3838ee | -14.31152 | -47.20396 | 2026-08-18 11:57:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 08bb477d-784a-3eec-abf8-5fb8b50b71b0 | -19.61667 | -46.9665 | 2026-08-18 11:57:00 | TERRA_M-M | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b06dc2a4-098a-3a30-abb3-e8a071e152b4 | -12.30653 | -49.98801 | 2026-08-18 11:57:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1b1d9606-8f48-38f9-86e8-8348bc3c974c | -16.0999 | -45.12176 | 2026-08-18 11:57:00 | TERRA_M-M | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5d2fe81d-505f-3bf5-8f73-787253add8b1 | -16.26937 | -49.30717 | 2026-08-18 11:57:00 | TERRA_M-M | DAMOLÂNDIA | GOIÁS | Brasil | 5206800 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 9a9828e9-04df-3a4e-8663-08eacc693fb2 | -17.19214 | -53.15028 | 2026-08-18 11:57:00 | TERRA_M-M | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 242f8213-5528-31dd-916e-8473694faee4 | -12.46609 | -54.18833 | 2026-08-18 11:57:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 31a51c2e-de31-3bbd-be5a-513bb891884a | -12.26727 | -45.87979 | 2026-08-18 11:57:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 960f1f57-268d-3bd6-950e-3c3c2c944efb | -12.52648 | -47.87825 | 2026-08-18 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 33.7 |


[Clique aqui para ver as próximas entradas](README65.md)
