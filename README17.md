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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b427a12-7eae-3d75-ba55-2933fc1e4560 | -13.02832 | -46.80387 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d5c705db-6c1c-329c-9493-b0ed66f31f48 | -15.00412 | -54.80609 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b7edff67-6ee4-3397-aeb3-2c0139e1ccd0 | -12.9816 | -45.1938 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd2adc9c-8780-3bd4-bd57-db0bc5a8ab67 | -13.40308 | -46.36227 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 28a8096a-a1c2-3e67-b459-3c3b511eace1 | -17.61457 | -46.70272 | 2025-08-20 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 303cda21-cb14-3743-85bf-6868e595e765 | -14.65497 | -54.88807 | 2025-08-20 04:10:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a18e5fd9-eb9f-3981-a81e-5ab3c1ccfe9f | -12.81509 | -48.56547 | 2025-08-20 04:10:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da8f1cd7-25d0-3d14-af0b-d523b3a1feb1 | -13.17777 | -46.8948 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 759601ee-f70a-3787-b78b-171c110df9ca | -15.00617 | -54.80567 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7d86a9f-6330-3be9-914c-df0b18dbf379 | -13.19727 | -50.7424 | 2025-08-20 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb6ab4cd-461e-3823-928a-d8ec91f5109f | -11.31053 | -44.92633 | 2025-08-20 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d66ebb43-e576-3438-a939-32cc7d360b2a | -13.18955 | -46.87022 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5c5df20b-d91d-378d-a11b-1ea3b07e8740 | -13.33642 | -54.42647 | 2025-08-20 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c9bc523d-dfdd-3223-a545-1150785a34b8 | -11.30991 | -44.93013 | 2025-08-20 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b486afe9-551c-336f-8737-11a806fc8900 | -13.34111 | -54.40396 | 2025-08-20 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bf3ea226-b0c4-3b8b-b396-f96ca7846b83 | -14.98853 | -54.82163 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e3cc6c45-fdc6-303f-90a0-c415182178b8 | -15.55062 | -48.56377 | 2025-08-20 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d62e7d6-81e2-3a29-bc56-a24ef3121347 | -15.04809 | -54.83027 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a551f16c-b474-358c-b6e7-b169d1880453 | -15.01901 | -54.82264 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0a0ce44-0cfe-3796-b3b7-42bc5aed3a39 | -12.97089 | -56.87606 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b0f8cadc-7bf4-374f-aeef-15fa3b3c8c65 | -13.03301 | -56.85497 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ffb8d76-ed4f-397c-ac70-a295db6213b0 | -13.03861 | -46.78754 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3452ab0-2894-309b-8242-dcfbcd4890f5 | -12.52944 | -45.61258 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d038019-4ade-3a3a-a476-c61af1c51339 | -13.03419 | -46.79142 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7af2ec91-48f9-3ff7-9ab5-a62b2427f6c2 | -13.58568 | -47.01387 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c4c9e798-44d7-3bac-9e28-83d5bb9a8db0 | -12.97841 | -56.87485 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8b4f5c78-bbc6-37fb-9b73-013fb173225b | -15.00716 | -54.82065 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4fdce2dd-fb50-393c-8d19-8830d9fd4f71 | -13.61078 | -46.88982 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81c52a41-cd3f-3477-872f-fbdbc8efe3ff | -14.99658 | -54.82249 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5aca6982-1341-39f3-a2fd-7d7df5e58944 | -16.22229 | -43.41975 | 2025-08-20 04:10:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 992b3999-fb2b-3d3c-a136-b76f28b54537 | -12.98565 | -45.19058 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1fb08b6-f83f-3883-a9a1-6efb50cefe1c | -13.03003 | -46.81172 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bfaacba8-a934-3bab-97dd-0219eb8a7d98 | -12.47713 | -47.98204 | 2025-08-20 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d62f8a3-9239-3102-a1ef-1807674ca414 | -14.89064 | -48.08872 | 2025-08-20 04:10:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ace4b94e-f92b-369e-b29a-b921f4a5274e | -12.63857 | -46.88354 | 2025-08-20 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31700a38-bae7-3f23-b381-b18762036e05 | -14.69322 | -49.05252 | 2025-08-20 04:10:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e372cb8-a5a8-3842-a759-6c3550e4d6b9 | -12.99124 | -45.19934 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 074f363e-4e5b-3075-8c36-98f2bffa9158 | -13.59882 | -46.9155 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40099eb1-8933-3a01-a053-94d27eb49e3f | -14.96323 | -50.12421 | 2025-08-20 04:10:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a1cf68e-09c7-3a1f-bdc4-cf02fcc40b6f | -13.02678 | -46.81304 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e61c3249-c859-305d-a0c2-54dd3f0370fd | -15.00527 | -54.81006 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f3c0c492-1b54-348b-a0a0-9795410ebd1d | -12.47696 | -46.92279 | 2025-08-20 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cc203d9-7f70-30a0-89f5-58ce2160ba08 | -11.6125 | -51.58906 | 2025-08-20 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2d58bf9-1bd0-329f-8075-93def099b8a6 | -12.66961 | -45.81917 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31eb3b59-b97c-3e69-82fe-ed8e0d4d5045 | -13.87551 | -45.5718 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0f76c78-9c5c-38da-84d3-879f4978b1a2 | -12.87866 | -46.06645 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a04b43c5-0c31-3536-a40c-de4c78ab0a7e | -18.52486 | -45.11153 | 2025-08-20 04:10:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7b8eec70-8df4-362c-bf4d-64d8dbe9067a | -13.03523 | -46.8035 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2610c4b-d565-3ecb-bffb-73cb59f6b9a8 | -12.52094 | -45.59892 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6080b2bd-bd1d-3204-87f6-9ae65e682381 | -11.61307 | -51.58598 | 2025-08-20 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58fb98d4-1b3b-3c33-bab9-d37219a49f5e | -13.48733 | -47.06239 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2165785c-896a-3eb0-ac2d-753e41e3b121 | -13.63735 | -46.88872 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de7d5186-2d32-3ce4-9ecb-9bddc5d6d174 | -13.39398 | -47.49118 | 2025-08-20 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54787b3a-2c00-3d07-ad4a-d5f1cb935d11 | -13.14825 | -54.93106 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 1a2a2458-1a1c-3122-855d-b70026bcbc6c | -13.32872 | -54.41698 | 2025-08-20 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 369de04f-d51a-33bc-9f3c-ab324733f47a | -12.66394 | -45.80996 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 398efe0d-95c1-3fa2-a185-c2bfce3340a0 | -11.56914 | -50.45647 | 2025-08-20 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2834afc8-48fb-3048-9a3c-1bdf7140c6d9 | -13.18151 | -46.87291 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f712d78d-4d19-3ae2-8d4e-482e2033ad24 | -13.6719 | -44.22225 | 2025-08-20 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edd3b4a7-5184-3f34-98ef-d4c0f986b012 | -15.46686 | -49.64554 | 2025-08-20 04:10:00 | NOAA-21 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 889c288b-c367-3edb-bc4b-8ed3c2b6daf3 | -14.30966 | -52.0049 | 2025-08-20 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03c8980d-a6b4-3fdd-855d-5b850a6139f1 | -14.94578 | -46.99464 | 2025-08-20 04:10:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05d00793-4898-31e7-8b11-db98aee4d0d3 | -17.73115 | -44.23534 | 2025-08-20 04:10:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f347a59-7849-327e-8045-4548a2528964 | -11.59857 | -50.53699 | 2025-08-20 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 57cfe9b4-5050-3900-b3a0-00bcfe93f254 | -11.74213 | -48.18921 | 2025-08-20 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 872ecfb4-5fb5-3b9d-9680-0410f211601e | -14.16103 | -45.28656 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e81e75cf-09d5-3835-9fe2-9d7142e86c9b | -13.15537 | -54.92735 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9cd345b8-9f18-3629-8038-5f502faca15b | -12.96754 | -56.85882 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 62c31b37-b824-3db4-92e7-31e3e9c0db22 | -11.44794 | -47.31132 | 2025-08-20 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5d9c1aaf-4362-3e74-932a-a0ec28bcfabf | -14.35734 | -51.99913 | 2025-08-20 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07494cee-344b-38e3-a268-6cfd071247ee | -14.16087 | -45.29071 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59d2d901-8f97-33ce-a068-bdfdc508bde3 | -13.57752 | -47.01714 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 40cb7c7a-08b6-3b10-9590-eae9356c8fd5 | -15.57266 | -50.31075 | 2025-08-20 04:10:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b724f8c-6758-3595-8d9a-f61b1d3df544 | -12.94377 | -46.15297 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f66dfccd-ba3b-3238-95c0-2893ccb28046 | -13.11091 | -51.91272 | 2025-08-20 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b446948a-de21-3099-afec-84e96152e0e7 | -14.74375 | -46.29418 | 2025-08-20 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9956df8f-db36-3f3d-9d28-17fd0315b275 | -12.51962 | -45.60685 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acfda3c5-4bf6-3fa4-9052-908a5159f4a0 | -13.47779 | -47.05136 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a361383e-0ae2-380a-97ca-323d600880f6 | -17.09135 | -48.98368 | 2025-08-20 04:10:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81114a9f-ab73-3e99-ba7c-e32148c4a040 | -13.18142 | -46.89561 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1a48f235-82df-3e2d-9e15-0d8053d69363 | -12.66435 | -44.9631 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f55267f-372c-3e1c-a4f5-34fa6f0ed41e | -13.34496 | -54.39737 | 2025-08-20 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 35de90d8-1090-3cff-9f8f-2860407cc8f5 | -13.16398 | -54.94664 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e6702da-7364-3a0f-bd7c-d39a06f7118d | -11.02639 | -44.60147 | 2025-08-20 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1816ac06-326d-341a-9b80-ab696a0fd331 | -16.11547 | -46.82151 | 2025-08-20 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 66e866b8-1619-3787-bc0d-c6098618662a | -14.16552 | -45.28376 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db86aecf-943b-35ca-a203-e0e96a1c7003 | -13.58199 | -47.01326 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8be43da0-fc4b-391c-92b2-3a46fe33d989 | -13.18784 | -46.90241 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5528f9e7-1460-39c7-91eb-0ea67e2df858 | -13.33278 | -54.42741 | 2025-08-20 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b0616175-06ae-3075-b716-579907ea6542 | -13.15339 | -54.9372 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 705830e3-8b46-390e-9c3c-5f75c1a876c8 | -13.64858 | -43.79071 | 2025-08-20 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a2df94a-f9a0-368b-9ed0-4d3f3416645a | -12.77532 | -48.26525 | 2025-08-20 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7974f1ff-2ddc-3e3e-9e92-fab9a1e5affb | -10.895 | -48.49558 | 2025-08-20 04:10:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d75598f-e441-3de9-abed-bb188ad3887d | -14.89201 | -48.07082 | 2025-08-20 04:10:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 284f2c71-8f8b-3575-823e-b247400ce69d | -12.14851 | -48.01788 | 2025-08-20 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 780916ed-a5e3-339c-9ef1-10d623783af6 | -14.49903 | -45.96056 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d47f583-429b-3c06-b938-1726a5bf4459 | -13.57675 | -47.02163 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d545cda6-731f-34eb-9c64-4357b6d00b93 | -13.1059 | -51.9115 | 2025-08-20 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f272a54-7dd6-34a9-8bb3-0be61a154d15 | -11.75025 | -48.19064 | 2025-08-20 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| de0f6b94-9bab-3e9a-bcf6-223107045848 | -15.00222 | -54.81498 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |


[Clique aqui para ver as próximas entradas](README18.md)
