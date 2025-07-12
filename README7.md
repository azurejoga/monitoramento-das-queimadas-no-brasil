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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e31e230-9bc2-34cc-b36a-b9e837086d68 | -10.67107 | -49.50381 | 2025-07-12 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fd410f32-346d-32f9-b649-28df6745c5ea | -4.54472 | -48.012 | 2025-07-12 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b75b764f-bf8a-356a-951e-243b6753180c | -10.56935 | -49.11558 | 2025-07-12 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 92836f8e-0823-3c72-9294-76e17041dddf | -13.1289 | -47.27719 | 2025-07-12 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79d7370e-8ea9-38a2-9a80-483d8c7d11bb | -9.8524 | -47.87537 | 2025-07-12 03:49:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da0db417-0390-3710-b33d-d9c466c3b772 | -11.42007 | -46.41055 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63b744dd-aac3-3760-a77d-622352676481 | -10.56793 | -49.1311 | 2025-07-12 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1dbcfbdb-10a3-3078-9cb5-7368c393352e | -11.83792 | -47.50782 | 2025-07-12 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fd8f7a1a-8278-3774-92cb-44b077f492f5 | -11.94814 | -49.2948 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8e5d9e3-986e-3781-977c-e8ee2c3aa0f1 | -11.4271 | -46.40042 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f21e2fb4-d02b-3ead-98cb-fa78c80138e1 | -10.57266 | -49.13082 | 2025-07-12 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 83c8a1e1-7fa7-32aa-91a7-c97971c44204 | -10.8435 | -49.11248 | 2025-07-12 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d16cbe8e-832a-3e59-8f7b-5d941944fa08 | -10.88893 | -49.20642 | 2025-07-12 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| de4dc05e-0f3d-3438-9dc7-8d16e41f52a2 | -11.83857 | -47.50443 | 2025-07-12 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d39fa351-97d0-3974-a2f0-4536e0309219 | -12.41926 | -43.49017 | 2025-07-12 03:49:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 51885e60-e461-35f7-a279-f2d1329025c9 | -11.73114 | -47.47061 | 2025-07-12 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 239b6aaf-ff8e-3e84-b97d-f1b29b65af2c | -6.18179 | -42.14662 | 2025-07-12 03:49:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9789720e-5d65-3668-9718-f10d0605badd | -10.57449 | -49.12128 | 2025-07-12 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 460f8c74-09f0-3d30-9b5a-df4737dec92e | -13.15757 | -47.26627 | 2025-07-12 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbc9b38d-57de-374a-9137-60588ac5af3e | -9.91588 | -47.83181 | 2025-07-12 03:49:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b98f080-e63d-312e-b633-ee4c8e9c239d | -11.44706 | -45.11843 | 2025-07-12 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4c01207-e68b-3597-9707-2bdcb4e9fc4b | -11.73053 | -47.4738 | 2025-07-12 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 625faa8c-110a-3e76-8c84-43a7165dc990 | -16.83905 | -48.52481 | 2025-07-12 03:49:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fede44f-b0f4-310b-ab1d-651daba97111 | -9.79933 | -48.5721 | 2025-07-12 03:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c729f24a-83c6-3d7c-805b-b9829acc3b1c | -11.42837 | -46.39341 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d761dee5-fbaa-3d2c-8378-de6f23dc6612 | -12.41555 | -45.34784 | 2025-07-12 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fdacf55-9432-3ac7-b3f7-2c5887911d96 | -13.0056 | -46.27994 | 2025-07-12 03:49:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba449eaa-0471-3c6a-a58b-96661f194d5a | -13.12246 | -47.31015 | 2025-07-12 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10808823-6d09-36b9-876d-6c47717ab9a6 | -11.93989 | -51.68983 | 2025-07-12 03:49:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05302f16-1021-3c89-a3cc-058702a46fdb | -11.73307 | -47.46047 | 2025-07-12 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df197ec7-8933-3f76-8921-dbdb013c87be | -11.73722 | -48.53163 | 2025-07-12 03:49:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24d64fef-6ee6-37ea-a5a8-f951b3e5da44 | -14.74625 | -46.29854 | 2025-07-12 03:49:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01544afc-33cc-339f-a48a-a5c0ad4c1c43 | -11.60175 | -47.61145 | 2025-07-12 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccaee925-5abb-3035-9705-328e9027d6f2 | -6.28439 | -42.37293 | 2025-07-12 03:49:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dead74ce-a627-322c-9445-c49368779b18 | -4.385 | -41.91501 | 2025-07-12 03:49:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d22c42ab-32b0-3dec-b41a-47b3893aa64f | -13.01471 | -47.83004 | 2025-07-12 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91df5892-77a5-3348-93f6-d813a1166a2b | -11.71987 | -47.47192 | 2025-07-12 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6f4f698f-6adb-39fe-a1f2-edf3978ec588 | -11.4405 | -45.10236 | 2025-07-12 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ac9e1c4-780f-30c2-8143-2c9a3c4f8d2e | -10.8486 | -49.11822 | 2025-07-12 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ca5dda20-ecf7-32e9-a497-a0119bad7643 | -12.47229 | -44.49754 | 2025-07-12 03:49:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a24ea04-9bba-374a-b983-39ee0694e3fd | -14.77954 | -48.20968 | 2025-07-12 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbc339eb-50b4-3fa4-b182-e77b38c87039 | -10.66493 | -49.50257 | 2025-07-12 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 04f3271d-94e8-3b0b-9db5-a15e57052ef5 | -12.61092 | -48.36969 | 2025-07-12 03:49:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 29530a18-9462-3dd5-a437-059369f10c49 | -11.72647 | -47.4662 | 2025-07-12 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 63011c4e-47c9-3674-97b5-a231a8ee80d5 | -11.27648 | -46.40511 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6dfe6571-5324-3acb-aa1b-ba8e82d99bc8 | -10.56846 | -49.12017 | 2025-07-12 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4a10daf5-df77-332b-b1a4-283b5680ffd0 | -12.411 | -45.34691 | 2025-07-12 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8ddd884-e66f-3a92-8515-065ad27241ba | -11.42669 | -46.40256 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0007849-e846-359c-a1af-a57043836dc5 | -10.89307 | -49.21004 | 2025-07-12 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 64047e75-ef05-3feb-8f39-13263ab0f882 | -13.15241 | -47.26556 | 2025-07-12 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e798998e-9b99-32ba-8655-496a9195e70b | -12.99806 | -46.26727 | 2025-07-12 03:49:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf695b90-98e2-39a8-9857-1c9a85e503fb | -11.72776 | -47.45945 | 2025-07-12 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 7dbd026f-520a-3c0c-b648-a73900467548 | -12.41588 | -43.48577 | 2025-07-12 03:49:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb009973-bacd-31e5-a615-676ec826e999 | -10.89912 | -49.21107 | 2025-07-12 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6a2cc0a0-b8b6-336d-a96d-d428ad58b1fb | -11.60709 | -47.61265 | 2025-07-12 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 346963f4-c406-3922-851f-fc0ba77cafde | -11.83922 | -47.50104 | 2025-07-12 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7a0bab10-5f42-3258-add6-182531745555 | -12.15517 | -43.98873 | 2025-07-12 03:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98d311f4-c0a3-3d89-b553-e9a33f25cf17 | -10.57539 | -49.11662 | 2025-07-12 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 47877754-304c-3919-b146-6c7f59aa4e59 | -13.11895 | -47.30089 | 2025-07-12 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46806535-8de4-3f5e-b8bc-04b84c49fdd6 | -12.99198 | -44.87696 | 2025-07-12 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ede21a77-178b-3cb8-8b78-955f21e9964f | -12.47305 | -44.49336 | 2025-07-12 03:49:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 471205c5-0ecb-396d-bdb1-91ee3f0402fe | -4.38439 | -41.91878 | 2025-07-12 03:49:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| defa4879-8036-3a40-9700-3f6881fc4960 | -11.42725 | -46.39952 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c27e9e9-d72d-3996-a06d-6e6ba4b20c6e | -12.41377 | -45.35739 | 2025-07-12 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c0674f5-380e-3bab-98c6-875cb92e7c80 | -12.98073 | -46.33186 | 2025-07-12 03:49:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 735eb2c7-d1f1-3d88-914d-dd1b5d751ac1 | -10.89825 | -49.2156 | 2025-07-12 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3ae42a6f-e8e5-3980-9a46-cfd434ef4423 | -11.46244 | -45.11156 | 2025-07-12 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7dfe961d-ee44-316e-8d2c-fc65d30e2ed5 | -11.94726 | -49.2993 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88bc6889-fd8a-3e26-b094-2577b041a019 | -16.68114 | -43.88599 | 2025-07-12 03:49:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0beb627d-918d-31de-a84a-d318aea7c911 | -11.73178 | -47.46723 | 2025-07-12 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4684e3c7-b98d-3ad5-978d-3eaac16e2298 | -11.73243 | -47.46383 | 2025-07-12 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea816e48-2067-33fd-8f74-34292e2f9191 | -13.13806 | -47.2847 | 2025-07-12 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 62761e00-b679-3af1-8b3d-b92724f68e14 | -15.06248 | -47.59948 | 2025-07-12 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 902d4079-34a2-338c-8c4e-598f16f62d05 | -9.91663 | -47.82786 | 2025-07-12 03:49:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69941ad7-5cea-3f80-8ca1-5ce9ec46bf69 | -13.3508 | -47.7757 | 2025-07-12 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 26c96db3-e599-33fe-ac93-0138afecbe72 | -13.90585 | -46.87001 | 2025-07-12 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4ca60f22-00d2-3806-b523-dbb9f29573ea | -11.93305 | -51.68843 | 2025-07-12 03:49:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aebffc68-7dfe-39c8-b543-7d11ada1e35c | -13.13257 | -47.31293 | 2025-07-12 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5aca26b0-0551-3478-8139-b1f108c5903d | -10.5698 | -49.12175 | 2025-07-12 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| bd8ace09-c854-39b2-982a-10b8200cb6c4 | -12.98661 | -46.32722 | 2025-07-12 03:49:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3160f74-5146-3f65-ba4b-2380d20b5c3a | -11.9317 | -51.69483 | 2025-07-12 03:49:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ae31a016-4d78-3a78-8b31-2623ce49181d | -10.89395 | -49.20549 | 2025-07-12 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 76d36774-cf0a-38b9-a3f0-129417a25a30 | -11.41616 | -46.40376 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aa3a5bac-b433-3c39-9c0a-6ee2c9b64c22 | -11.72519 | -47.47289 | 2025-07-12 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f68cfd30-6e79-3e0f-9fb3-c0179b4545ef | -11.77794 | -45.21921 | 2025-07-12 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fbf9fd9-4718-37ac-bba6-10fbf312dbbc | -11.8935 | -44.89378 | 2025-07-12 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea5253b9-1098-37ac-a6e3-e9bf80febeb7 | -11.83728 | -47.51122 | 2025-07-12 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b148c81c-321d-3545-9593-2612ef6e3e57 | -10.89404 | -49.21214 | 2025-07-12 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5dff61a8-5b88-3f1d-910b-22a68f2c3e25 | -5.75281 | -40.44679 | 2025-07-12 03:49:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 175fdaeb-cf38-39ed-8783-7c6044de7838 | -11.84258 | -47.51236 | 2025-07-12 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8ffa296-9205-36ee-9af6-e2b175fdb62a | -12.10856 | -44.9826 | 2025-07-12 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eca36f41-4e18-3278-baf1-5b0ad5702702 | -10.87352 | -45.07995 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 476a91ca-68e2-399f-8474-730a04ff3baa | -4.54555 | -48.0072 | 2025-07-12 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a11c7a59-5bd9-320b-9c20-3a40e83d0fed | -11.41669 | -46.4009 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0f1e3f7c-bcf6-367e-a5d4-08550b6c1b9d | -12.67478 | -43.90891 | 2025-07-12 03:49:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93cf8edb-48ad-3493-b5ad-aeb27e3c42a0 | -11.4206 | -46.40768 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 986fb4ab-d4a0-348a-aa83-4b51bbe0e255 | -11.72712 | -47.4628 | 2025-07-12 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 6a114dd5-a4b7-327a-b03d-091583f7c179 | -11.94134 | -49.29798 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44d9ed1f-94e2-3ffd-ab78-cd3d947b6494 | -11.89793 | -44.89481 | 2025-07-12 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7b160bc-79db-36bb-a0b3-2546112193c6 | -13.15283 | -47.26337 | 2025-07-12 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README8.md)
