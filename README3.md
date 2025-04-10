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
| 6c11f794-a466-3309-aebb-202193a20928 | -8.10213 | -43.12623 | 2025-04-10 04:29:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 6b298389-914e-3746-965d-aed09712e4e3 | -6.23452 | -43.37971 | 2025-04-10 04:29:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 232669f0-5c48-3a38-9243-8bcf603c0460 | -7.55986 | -45.83868 | 2025-04-10 04:29:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90a37911-99a8-3245-ba9e-6780cbff9799 | -8.10086 | -43.12292 | 2025-04-10 04:29:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.2 |
| 8080644c-7147-339b-9420-70e772ce5fc8 | -6.59616 | -44.78357 | 2025-04-10 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aefd92a5-8695-314c-8dfe-7f378cee3fb5 | -6.23307 | -43.37683 | 2025-04-10 04:29:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8cf2a489-0b78-3f7a-995f-9d4becb91168 | -12.07488 | -45.61956 | 2025-04-10 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fc08bc2-55ed-3e30-bc8d-00cf68c07320 | -12.17651 | -48.68259 | 2025-04-10 04:32:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9fa4ca3b-b334-3fc2-a949-c6c48d1a983d | -11.27756 | -52.45283 | 2025-04-10 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4cd2baf-e0e7-3fa7-a19d-88f2f1657d92 | -12.62629 | -48.14742 | 2025-04-10 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3144b503-2f18-34d3-8580-d240bada13d4 | -12.08944 | -45.62176 | 2025-04-10 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 773adcb9-e51c-3753-b1ca-842a0ea4efed | -11.40134 | -52.95931 | 2025-04-10 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0121599-a00e-33d6-9200-a3673f28cf03 | -10.60857 | -44.76778 | 2025-04-10 04:32:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d632d8d-f2fc-33fa-9323-f323773cbcf0 | -10.53828 | -44.66603 | 2025-04-10 04:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f869337-05f8-35a9-8ffd-97a0aa0c029c | -12.43801 | -47.89279 | 2025-04-10 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6459fa3f-3f7d-365e-84c3-f82f9407bbca | -12.1732 | -48.68206 | 2025-04-10 04:32:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee3c629d-5018-3d30-abed-cb04405ebe7e | -10.35792 | -52.32846 | 2025-04-10 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3942b6be-c610-3a45-9cf3-371337bae58b | -16.60942 | -43.3293 | 2025-04-10 04:32:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b59602fc-c65a-3dea-8edf-b8197a618762 | -12.75135 | -48.34628 | 2025-04-10 04:32:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5174d7c2-110f-38fb-a531-90b9f78deba3 | -11.27312 | -52.45661 | 2025-04-10 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 774ac384-94f7-3665-85c5-43073f92067c | -12.07852 | -45.62012 | 2025-04-10 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfbe91f3-6a18-34f6-991f-12274f76f464 | -11.27681 | -52.45726 | 2025-04-10 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40cd2552-f83f-328d-801f-9509bf4531f3 | -13.1087 | -48.62621 | 2025-04-10 04:32:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1ecff9aa-bb63-37cd-9002-954e004bb6d8 | -12.08216 | -45.62066 | 2025-04-10 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aebf226d-0b70-3f18-b262-9e7e2763ac1a | -11.69481 | -44.62032 | 2025-04-10 04:32:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06022127-6a05-3f95-b8b5-db20ca308c60 | -12.07426 | -45.62389 | 2025-04-10 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8f4d387-7391-3256-b7b3-3d182e011155 | -12.08642 | -45.61687 | 2025-04-10 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7922689d-d08e-313f-87af-77b1b090c55b | -14.88518 | -42.26848 | 2025-04-10 04:32:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 11b64f45-b9d5-343c-874f-0a6d5f806742 | -12.08704 | -45.61253 | 2025-04-10 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9f4630a-76aa-32cc-b602-6de51c7bc79d | -11.39755 | -52.95862 | 2025-04-10 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff217308-84ae-38ad-9f2d-5acad23505af | -12.40195 | -39.24371 | 2025-04-10 04:32:00 | NOAA-20 | SANTO ESTÊVÃO | BAHIA | Brasil | 2928802 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 83bcf50f-b46d-393a-9886-7f0e13b24480 | -12.0858 | -45.62121 | 2025-04-10 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc0fe2ef-6195-3717-98f6-1870fcc1c42f | -11.39836 | -52.95389 | 2025-04-10 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a2a911dc-39af-3d26-b5bf-89b1a70400f3 | -13.02063 | -44.03114 | 2025-04-10 04:32:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3becc2cc-9a93-3982-88d0-de6d2c026270 | -11.26943 | -52.45597 | 2025-04-10 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e317b0ff-79b0-374d-9c4a-86c098972f5e | -11.27387 | -52.45219 | 2025-04-10 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0badc8c-cb36-313b-a5f4-7bef51285715 | -11.73333 | -48.71591 | 2025-04-10 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8261d947-6603-3e8d-a07c-457f889924fc | -19.92764 | -57.19224 | 2025-04-10 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7910b28-1523-3618-bb66-e8a3b3d4c10c | -22.2095 | -49.851 | 2025-04-10 04:34:00 | NOAA-20 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 5db00174-3440-34e7-b9c0-7ee15551185e | -21.27402 | -54.15231 | 2025-04-10 04:34:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 973eba23-cd84-3d1d-a511-a58aa3d37003 | -22.25873 | -53.17679 | 2025-04-10 04:34:00 | NOAA-20 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3a6097a1-fd07-308e-9a49-a611c98ee486 | -21.27831 | -54.14875 | 2025-04-10 04:34:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 34e55be2-cd8d-3286-b01c-cd0d5cd2ac72 | -21.98777 | -57.60563 | 2025-04-10 04:34:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ee67de70-d0d4-30cc-b0b3-8348be24baf9 | -20.14519 | -52.83612 | 2025-04-10 04:34:00 | NOAA-20 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e73ac39-b756-38dc-9e47-fce6b31e3e98 | -21.97342 | -57.58922 | 2025-04-10 04:34:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0fd8caa-8e57-3033-ba1f-6e0a26816cf0 | -21.09197 | -48.6931 | 2025-04-10 04:34:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 93ea0d12-eaef-3d4b-aee6-f5e5896915f2 | -19.93188 | -57.19327 | 2025-04-10 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e71fd8c1-8bac-3110-8815-f4b0d181febf | -19.92922 | -57.19374 | 2025-04-10 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 828c5882-007a-358a-97ec-d6563578577f | -20.59032 | -56.05082 | 2025-04-10 04:34:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c794aa6d-7e8c-3e5f-bf4f-f7e25eebb430 | -21.09545 | -48.69368 | 2025-04-10 04:34:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ee8e8783-2ab8-3278-9b1c-c266334c5593 | -20.59187 | -56.04899 | 2025-04-10 04:34:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eaba0919-2f59-302d-88ad-bca2240df56c | -20.59088 | -56.05437 | 2025-04-10 04:34:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e01db22b-eb11-3e4d-bd83-3880b9e732a4 | -19.63743 | -51.2655 | 2025-04-10 04:34:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 471e93db-3aa5-3b80-b8e5-067942813dd4 | -21.9692 | -57.58834 | 2025-04-10 04:34:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07bd53a5-ef1a-32be-be8d-f4224a3030e8 | -22.25939 | -53.17285 | 2025-04-10 04:34:00 | NOAA-20 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| aea7dc64-e214-3b30-a71d-96701816078c | -21.37132 | -49.15569 | 2025-04-10 04:34:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c5c887a0-cafe-3fb7-864a-315b467815ea | -24.24214 | -50.74003 | 2025-04-10 04:36:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| db28233f-b85b-3b0a-93e3-3bd5296f4d17 | -11.84468 | -58.0457 | 2025-04-10 05:23:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05298a23-7386-35d7-80bf-ec515765e332 | -9.47081 | -63.41602 | 2025-04-10 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 744f7652-d763-37e5-8f61-eed430bd9ef9 | -11.65146 | -62.28644 | 2025-04-10 05:23:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1442f75-c502-3ff2-a2ac-b18e4fa0fd87 | -12.24965 | -63.80243 | 2025-04-10 05:23:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e76e03c-cfc0-35aa-ace5-c36c652d84bf | -11.40077 | -52.95539 | 2025-04-10 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb3b79bc-f420-3302-829f-392b9b066dc4 | -11.40039 | -52.95844 | 2025-04-10 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e62a2732-a9da-3194-8f16-7ed5dac78e83 | -10.31739 | -58.50218 | 2025-04-10 05:23:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ee9da62-4c03-34ec-932a-0e2d47c5f9ad | -11.2762 | -52.45354 | 2025-04-10 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 258ea7a6-4d4a-33bb-b5f8-2d19d6478b98 | -11.27199 | -52.45408 | 2025-04-10 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7093701-ee4f-34f0-8495-50071ca8a9fd | -11.27579 | -52.45692 | 2025-04-10 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2148f61-f1bf-3954-a873-ee49a4ca5421 | -11.2773 | -52.45482 | 2025-04-10 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bfb02578-3ca9-3405-8dce-8539c606a97e | -11.96787 | -63.67796 | 2025-04-10 05:23:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aff05b20-4230-3cfb-9919-2c0aa5bc5b8e | -11.27156 | -52.45744 | 2025-04-10 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af33d18c-2333-3f70-a68c-c0066a0c66ea | -20.59226 | -56.05134 | 2025-04-10 05:25:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 32efbdb9-c7cd-33a9-a2cb-6965ff04b4ac | -19.92869 | -57.19347 | 2025-04-10 05:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6145a502-f86b-3ac9-b0dd-ca9559bf5428 | -19.92961 | -57.19551 | 2025-04-10 05:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 949c6708-0593-34d4-9066-a9780081d796 | -20.59093 | -56.05092 | 2025-04-10 05:25:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d5281ae6-051c-3e85-9594-cfe9cbde4fec | -19.93397 | -57.19609 | 2025-04-10 05:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51a5439f-8cd6-3a9c-b9ee-3b645ff87431 | -8.11392 | -43.11488 | 2025-04-10 05:38:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 38221b0f-05d9-3c48-ad2c-e0fa97047df7 | -6.23384 | -43.37437 | 2025-04-10 05:38:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 772128f8-78c8-30ca-b8f6-963628f4bda9 | -8.1038 | -43.11332 | 2025-04-10 05:38:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| aa6b7274-81ed-359a-832d-a565a94e3926 | -8.10209 | -43.12538 | 2025-04-10 05:38:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 542c16ff-ca60-3587-a0d9-8fdfa52cdbee | -12.07858 | -45.61818 | 2025-04-10 05:40:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 19a36ed4-7876-3b54-836f-9c4277df2f8a | -9.47111 | -63.41495 | 2025-04-10 05:50:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1812be4b-5bea-3b5b-906a-c29b05ec4355 | -11.65239 | -62.28587 | 2025-04-10 05:50:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c7aef52-8c07-3fb3-bc64-a172510d2f4a | -12.24771 | -63.80322 | 2025-04-10 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |


