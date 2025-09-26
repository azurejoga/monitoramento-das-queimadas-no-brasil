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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7639cd5-3865-3afc-81f6-f5921ec6a19c | -20.47251 | -45.83731 | 2025-09-26 12:02:00 | TERRA_M-T | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bcee8c4a-2944-3387-82f1-739f90024a6e | -22.14437 | -43.23441 | 2025-09-26 12:02:00 | TERRA_M-T | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 35a719f7-14c7-3757-916b-8ed37c54873a | -20.99684 | -50.00768 | 2025-09-26 12:02:00 | TERRA_M-T | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| fd4d4a3a-ca9b-3d8b-b0e7-e0750341a0e6 | -20.46402 | -46.50195 | 2025-09-26 12:02:00 | TERRA_M-T | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 75b52917-bb82-31ae-9c90-e99dc376ce1e | -21.87012 | -42.10048 | 2025-09-26 12:02:00 | TERRA_M-T | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| d65e8cae-161e-314c-93d7-1a6f17899485 | -20.39191 | -46.0051 | 2025-09-26 12:02:00 | TERRA_M-T | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 5c26751f-f5b7-3b93-b23b-812c08eaddac | -29.4389 | -50.53128 | 2025-09-26 12:04:00 | TERRA_M-T | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 43cfb04f-c559-328b-97f9-eed222dafe5e | -29.43671 | -50.54405 | 2025-09-26 12:04:00 | TERRA_M-T | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 19c8c21d-09f6-3ebd-9365-8c61d91fbde9 | -12.5568 | -45.8459 | 2025-09-26 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 8182a2cb-39f7-3734-87c1-56c39cf5756d | -13.2393 | -50.6895 | 2025-09-26 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 0ab62ea6-0a9a-33da-9c4c-e9a511017436 | -11.4225 | -44.9794 | 2025-09-26 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 214.3 |
| 87138aab-cd3b-340f-9356-96621a9db681 | -10.0062 | -44.1766 | 2025-09-26 12:10:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 174.7 |
| 80700cc7-d085-36aa-ae99-c19f6be822ef | -11.4225 | -44.9794 | 2025-09-26 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 211.6 |
| 031f6950-5588-3a48-8cd6-a80c9dd4efae | -11.4221 | -45.0025 | 2025-09-26 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 633.1 |
| fc1a3cb9-6527-38bd-832f-e8adc81bdedd | -10.0062 | -44.1766 | 2025-09-26 12:20:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 119.5 |
| bed923d6-11f5-3609-875e-79248d729116 | -9.9873 | -46.7103 | 2025-09-26 12:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| e005c0cf-6560-36a1-8e31-c625b88340c3 | -9.9683 | -46.7125 | 2025-09-26 12:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 7e795657-fe7c-319f-a3eb-c252609dfeba | -11.7006 | -44.4049 | 2025-09-26 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| c6ae1749-192a-3194-85cf-a4a470972c9a | -10.0062 | -44.1766 | 2025-09-26 12:30:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| b273099a-51eb-310b-97d8-610a57000d29 | -15.0741 | -44.9751 | 2025-09-26 12:30:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 268.2 |
| 414f6a2a-c83d-3249-b905-177aeca55f92 | -11.4225 | -44.9794 | 2025-09-26 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 325.4 |
| 0ce5e89c-9231-3c5f-ad96-8fee3f367347 | -11.4221 | -45.0025 | 2025-09-26 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 759.2 |
| 131da864-6c68-3558-8289-0c3b593d4c39 | -12.5568 | -45.8459 | 2025-09-26 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 00a5dfa4-9b6b-377e-88a8-1ddd0a9c915d | -15.0545 | -44.9788 | 2025-09-26 12:30:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 96.5 |
| f141cd91-3837-35d7-aab0-b0aa671738aa | -15.0736 | -44.9986 | 2025-09-26 12:30:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 8a0582b6-04bd-3a38-81d4-7776f125bd39 | -11.6238 | -44.4164 | 2025-09-26 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| b237af53-6dda-32bb-ba61-e3b551ca73a9 | -11.7198 | -44.402 | 2025-09-26 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 09f8bc04-4744-3d78-bbed-92cbcf21436a | -12.5568 | -45.8459 | 2025-09-26 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 133.3 |
| e8aadeb6-845f-3de5-8f37-3d02466304bf | -10.0065 | -44.1533 | 2025-09-26 12:40:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 4d906186-2b47-3e88-9ffd-231028565ecb | -11.4225 | -44.9794 | 2025-09-26 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 5ca2ebce-97a5-3596-a477-b5233bc05b40 | -11.7006 | -44.4049 | 2025-09-26 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| be14ac4e-efc9-3f77-a878-2abb7bf18fe2 | -11.6233 | -44.4398 | 2025-09-26 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 4005d83f-36ab-3b3a-84fa-4d78e046a79e | -8.8603 | -46.2075 | 2025-09-26 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 38673a92-fb15-3966-8284-c24de2012bde | -10.0062 | -44.1766 | 2025-09-26 12:40:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 2c519be9-a08e-3cd3-8d49-013b69bdced3 | -11.4221 | -45.0025 | 2025-09-26 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 252.8 |
| e811fd17-eeb1-329b-8635-362dd43e642f | -8.8409 | -46.2544 | 2025-09-26 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 8a59deb4-83a0-3041-b601-9e59b14f62b1 | -11.6233 | -44.4398 | 2025-09-26 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| b21e84d9-74fe-3e83-8bd4-0afa3ab9f5b6 | -11.6814 | -44.4078 | 2025-09-26 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 2366bd32-ef44-3c42-a340-9ae69d86abf1 | -10.0062 | -44.1766 | 2025-09-26 12:50:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 201.4 |
| 21d0e992-c5fa-3ca0-a292-0bf954d32f81 | -11.4225 | -44.9794 | 2025-09-26 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 209.2 |
| fd571d19-304f-3d9c-bf1c-9172a93fc2f6 | -8.0056 | -45.2555 | 2025-09-26 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 69de24e5-f49e-3078-8a1d-9b8eaea86b6c | -8.8409 | -46.2544 | 2025-09-26 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| c25f3404-6d24-3191-8362-975a62dd632e | -11.7198 | -44.402 | 2025-09-26 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| da717710-a305-384d-905a-91dc284073cc | -11.4221 | -45.0025 | 2025-09-26 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 371.0 |
| 368b247f-5b09-3fcf-a600-08ed174d17bc | -10.0065 | -44.1533 | 2025-09-26 12:50:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 113.5 |
| b521fa41-2ded-3519-860a-1fc63ff8c867 | -11.7006 | -44.4049 | 2025-09-26 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| fca41562-ef61-383b-bcaf-ba9b36a17c3a | -11.9655 | -47.8891 | 2025-09-26 12:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 082fde56-0d08-3512-98f2-514faf6749b1 | -12.5568 | -45.8459 | 2025-09-26 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 1001ff0f-bbe0-339a-b11c-eca12c6658bd | -11.9659 | -47.8669 | 2025-09-26 12:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 73965172-d898-3738-a8ef-f2fca870dee9 | -8.8603 | -46.2075 | 2025-09-26 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| e538ce1d-f681-3949-aed4-2fd0c601301d | -7.6775 | -45.9872 | 2025-09-26 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| ddd88104-08ef-34c7-bb5d-15208be384b4 | -6.5801 | -45.1117 | 2025-09-26 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 963d33d8-724a-3f04-812f-8437801b5de0 | -12.631 | -48.1313 | 2025-09-26 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| b547d7d4-00e0-3d50-8761-3933ca98d133 | -5.7775 | -42.7961 | 2025-09-26 12:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| bd9bb03f-4c93-3641-a070-f7855c36cf07 | -10.0252 | -44.1742 | 2025-09-26 12:50:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| ed2acf53-5654-3a25-9fa0-f2436342e58c | -5.4565 | -43.0554 | 2025-09-26 12:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 3a4e630d-eaf1-3de7-852b-d78eadc2c745 | -7.6587 | -45.9889 | 2025-09-26 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 6df16596-da04-38c1-93af-5bf3ac53805d | -11.6238 | -44.4164 | 2025-09-26 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| fa6201f1-4645-3c3d-95ed-f40639bbca1d | -7.6775 | -45.9872 | 2025-09-26 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 3285e470-3020-3d17-88bc-40b7980855ef | -12.631 | -48.1313 | 2025-09-26 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 8d3bf5e9-938f-30c9-85c6-a4f6670917ec | -11.4225 | -44.9794 | 2025-09-26 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 205.3 |
| f1c76979-af68-3701-9236-617563ff9199 | -10.0065 | -44.1533 | 2025-09-26 13:00:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 0cc89507-1df0-3d17-b791-4a0ba4008ded | -10.0252 | -44.1742 | 2025-09-26 13:00:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| b5c35775-3948-33bc-9c2d-8f5b9aecc887 | -8.8409 | -46.2544 | 2025-09-26 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| e89f585e-e992-34de-8dfc-2f96b15b2830 | -11.9659 | -47.8669 | 2025-09-26 13:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 1120727a-bc69-36df-b48e-3c4195ca5fba | -12.3806 | -50.5608 | 2025-09-26 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 11aabcdc-1258-3e3d-bf74-87bdc0c2e493 | -11.4221 | -45.0025 | 2025-09-26 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 330.5 |
| 7d0ce423-1efb-3175-a17f-dce68798f968 | -9.5601 | -47.5139 | 2025-09-26 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 14641b0a-a888-39f1-beeb-ba20e6c54a48 | -12.5568 | -45.8459 | 2025-09-26 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 32fd30b8-3ef4-3fba-9abf-5e44ec1f0c52 | -7.8735 | -45.2911 | 2025-09-26 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| f63442be-be5a-33a2-af91-6c3dd43603a5 | -11.7006 | -44.4049 | 2025-09-26 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| ec6947c1-e757-36c5-8213-c0902860da28 | -5.7775 | -42.7961 | 2025-09-26 13:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |
| 497a1b9d-98c1-3c90-8940-9bdca1945e42 | -11.6233 | -44.4398 | 2025-09-26 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 16b07165-7514-3837-8c85-9c1c336dba0f | -7.5415 | -46.4025 | 2025-09-26 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 0b8b8b64-b8d3-3607-b4c4-e0e74ac294e2 | -8.8603 | -46.2075 | 2025-09-26 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| aa9758e9-cdf9-3f61-ab20-2c49b7bde37c | -9.5412 | -47.5159 | 2025-09-26 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| e5513a3c-7a18-3bb4-8e3b-8ba185e05076 | -10.0062 | -44.1766 | 2025-09-26 13:00:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 264.0 |
| 276ca904-ed83-3b10-98f9-933c427818c3 | -5.7775 | -42.7961 | 2025-09-26 13:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| c3e3801d-70ef-3b38-b6ad-cccf8271bfd9 | -8.8409 | -46.2544 | 2025-09-26 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| ae938ef4-3719-338d-b01a-cc9679346fcb | -11.681 | -44.4312 | 2025-09-26 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 27cf38d9-2294-34ff-9896-c91191aa5c4c | -11.7002 | -44.4283 | 2025-09-26 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| ee9f6852-9be2-3955-b468-b7dc7257a6e5 | -10.3938 | -46.1444 | 2025-09-26 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| ef3448f5-3446-345d-b199-69b16c1f6fa5 | -10.0062 | -44.1766 | 2025-09-26 13:10:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 9002af8f-855f-3325-a8de-9fa4ac5368e7 | -9.5601 | -47.5139 | 2025-09-26 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| a0f3ab8b-27bc-3ee7-a64f-570a9c437b7d | -6.9115 | -45.6947 | 2025-09-26 13:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 431a6266-4886-3abd-877a-e460edc17544 | -11.6238 | -44.4164 | 2025-09-26 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| bef51d19-fec3-3fe4-93db-21e3c19927cd | -20.7338 | -57.8083 | 2025-09-26 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 127.8 |
| 81d5d76d-7553-3e7a-9f09-46aa90cef6a8 | -5.4752 | -43.054 | 2025-09-26 13:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f0d1c40b-a554-30ca-8fcd-db494a464abd | -7.8735 | -45.2911 | 2025-09-26 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 3f957c12-0372-3999-a0ad-32b42f06bd99 | -11.4041 | -44.9359 | 2025-09-26 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 2089dad8-eda6-310c-b6b7-ff71aebafd5c | -14.8304 | -45.3947 | 2025-09-26 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 8aaf3e6c-a4c7-3e85-8908-d1fed244f3ba | -12.631 | -48.1313 | 2025-09-26 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| f315e41f-1b3e-3fd7-924a-5323ee168835 | -8.8603 | -46.2075 | 2025-09-26 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 8220a6df-2930-3ea7-920f-b3f45a3b8a01 | -8.6631 | -43.991 | 2025-09-26 13:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 76361e08-0d92-3116-8a2b-5eda8453d940 | -9.5648 | -48.5877 | 2025-09-26 13:10:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 7adf9365-c086-35a3-a911-fe94f88948ce | -20.7342 | -57.7873 | 2025-09-26 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.6 |
| a081f34c-3505-3665-9ec4-36129df08c61 | -12.5568 | -45.8459 | 2025-09-26 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 36af7305-d4b0-35d8-ad51-9a443cd6f9b2 | -11.9655 | -47.8891 | 2025-09-26 13:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 188e3d48-0f5e-3fee-9748-6c95d97ae635 | -11.4225 | -44.9794 | 2025-09-26 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 92af704c-6c04-3d96-a8bd-98b4c3072800 | -6.7174 | -42.7393 | 2025-09-26 13:10:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |


[Clique aqui para ver as próximas entradas](README52.md)
