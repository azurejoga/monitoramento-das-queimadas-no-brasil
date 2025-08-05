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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b99ae66d-80a7-3ccf-9dc4-7558fa1a42f9 | -10.91658 | -48.36728 | 2025-08-05 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db48a39a-10d7-3ab4-93c4-0ffa0f8be5eb | -10.44975 | -44.38562 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9ec320f-5165-3ec7-a87c-b72dc6f5a633 | -9.18547 | -48.84398 | 2025-08-05 03:49:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 50343006-bbb3-30cc-8f8b-a028179639cc | -12.67965 | -48.12326 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7d812c01-05ee-3887-80bf-ddfea81a5fae | -12.67989 | -48.12758 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c174b4c8-f09c-3f35-b0f3-48751bf9b243 | -12.68536 | -48.12847 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aeeddab1-6f2e-31e6-97fe-0b424bda4551 | -11.74792 | -45.01209 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd6e7540-8b56-3fdb-b96a-1219d9cf218e | -10.78295 | -45.50897 | 2025-08-05 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2369ab3-432e-3802-89cc-c14486cc2492 | -7.85606 | -46.73519 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f744f77-65ff-3625-8f62-8957c100de3f | -7.05515 | -47.46322 | 2025-08-05 03:49:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 142459fc-996e-37aa-96e7-97ae8b924c11 | -8.95767 | -46.74716 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ccba3ee4-775e-3c46-8df4-c3805a64121d | -12.35516 | -46.05896 | 2025-08-05 03:49:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e38ea222-c237-34ba-8382-fbadcb3325c3 | -11.91916 | -44.95886 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| bf9edcf9-dc6a-3daa-afd3-260c99c13a61 | -11.75623 | -44.965 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23585cbd-1543-3f4b-b7d0-1732d1f991f0 | -7.77436 | -45.21619 | 2025-08-05 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f89e4ca6-5a14-33eb-a340-2c0d17905e30 | -11.92442 | -44.95533 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94213910-719d-3731-8ec7-9d6528fc42a2 | -14.05529 | -41.99027 | 2025-08-05 03:49:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 14c419a4-ae24-3c9f-b08d-1a621e4766d9 | -8.25873 | -45.06435 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 401f31e5-feee-3ee0-9a7c-34b2143fb1ff | -11.80833 | -44.26535 | 2025-08-05 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6daf673d-c13d-3578-921e-bf02b12a135c | -11.91997 | -44.9544 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c7d6ac76-ab8e-3dba-89d4-c383d07aed10 | -11.06702 | -48.36224 | 2025-08-05 03:49:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2461df67-5464-3ed4-acfc-2e2bd59de409 | -8.25696 | -45.07135 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 690b495e-6f79-3940-aaa5-89f0381fc719 | -11.91388 | -44.96253 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| eb410632-9c0d-3d80-bb66-65e7cf0e810f | -11.75384 | -44.964 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b83404d7-fe95-34d8-9c1c-d78097fce873 | -7.57021 | -44.8876 | 2025-08-05 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ea2bd71c-dd5e-37fb-9706-61760db97702 | -11.93334 | -44.95708 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 46c92afa-9f3c-3c0a-895e-4203a7225bcf | -11.49929 | -44.26715 | 2025-08-05 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be4ce748-0a02-32c6-958e-2504e65aaf5c | -10.90513 | -48.36538 | 2025-08-05 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7192251e-0918-31d0-9c75-fdac9e865508 | -7.34115 | -44.67844 | 2025-08-05 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ff424e2a-8b55-3384-b204-f6847ed6f667 | -11.74864 | -44.99213 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2694fec8-5777-3a3a-aefb-2a18a613d5f1 | -7.1171 | -47.84607 | 2025-08-05 03:49:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 64d5f1f5-33fd-3684-838c-12f17931bfa9 | -6.56145 | -44.21838 | 2025-08-05 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f0d92f70-a672-3ed6-aa68-fa62c2208d6e | -9.29626 | -40.24343 | 2025-08-05 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 18866b23-d946-37f6-a831-7b8a9de47247 | -6.96397 | -42.86798 | 2025-08-05 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| bd5c426d-3e86-351f-b911-c94fa13f9ec4 | -11.00381 | -37.07498 | 2025-08-05 03:49:00 | NOAA-21 | ARACAJU | SERGIPE | Brasil | 2800308 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c3260340-9de4-3f91-830f-7306e2cb1ddb | -12.67891 | -48.12711 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 252340f5-5d48-3e8f-a0f0-b1b6caa64e3b | -8.94769 | -46.74176 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 068cb615-6560-3f8e-a4f4-0719b1d989a0 | -11.03756 | -47.61865 | 2025-08-05 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 717e328e-0b4a-3e8d-8878-af240646d6f6 | -12.72222 | -46.39257 | 2025-08-05 03:49:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86281553-a80f-30f0-8cd1-aade6cf8c203 | -8.25782 | -45.06964 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d35f9d1-0c38-34e9-b53a-9f56c503cdce | -8.94239 | -46.7408 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| dd890c19-2318-37d2-8be7-391df8197844 | -10.34549 | -44.90828 | 2025-08-05 03:49:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 186e93da-a894-3693-8e5d-fa53d602defc | -7.98813 | -43.15689 | 2025-08-05 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| aa161415-a793-338f-b29b-b21ac730a5e7 | -11.74604 | -45.00621 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b772b0f-0be0-3e29-99b1-28972f26d142 | -9.16587 | -40.59552 | 2025-08-05 03:49:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f460ffb2-19da-3fc5-82be-275e9634c5db | -8.22511 | -45.05851 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 20ffa788-b597-3fa8-8831-eb61dedab54c | -12.68608 | -48.12485 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8fcff6ed-7902-3b50-9adc-9bb6c954b936 | -9.17756 | -48.84523 | 2025-08-05 03:49:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26083f72-e937-3575-9907-91ea5ee863e7 | -8.94359 | -46.73429 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| cc4e0d13-6315-3cf7-8a49-18043cf15d74 | -12.73097 | -46.39948 | 2025-08-05 03:49:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 26cde15b-0129-30c7-9aab-275d29c4c2a9 | -12.33704 | -46.05014 | 2025-08-05 03:49:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6443f99e-83be-3df9-abc9-ec1145418c59 | -11.75428 | -47.54245 | 2025-08-05 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0fef4e2a-c271-3284-bd69-9297b140a4d4 | -8.38429 | -46.54332 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ed3d4ff-caf7-3d82-8b18-0517c811683d | -11.9147 | -44.95801 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6fa6aa11-96c2-3dd0-a804-e2958da01e0e | -7.94842 | -47.59438 | 2025-08-05 03:49:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2928d6e-0251-39b8-abe4-962dfb5fa3fa | -11.92455 | -44.92902 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d57bc735-dd47-3698-80d6-9d5684b069bb | -11.91022 | -44.95722 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c39de72-22d8-3fe6-b4ed-bda9c0cf107a | -11.74507 | -45.00191 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39f99834-da5e-3b4e-b45b-62f6c7a2c0ea | -7.85339 | -46.73846 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ab36f07-0216-3061-8bb4-f7b866c0087a | -11.92229 | -44.94156 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb5da63d-438e-360d-8aa8-d7f0bb8738fb | -10.90898 | -48.36701 | 2025-08-05 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 84e5ab2b-4ac2-338f-80f5-31bc792e32e4 | -10.46913 | -44.37922 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de686cb1-a011-3ba3-8c9c-3470d21783a3 | -8.25407 | -45.05996 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2f0ff3b-9a1b-3aac-9e7f-39e75d02154a | -13.24109 | -46.84996 | 2025-08-05 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 863d11da-6ed4-32fe-8a65-088a95a8fd95 | -8.87945 | -44.78913 | 2025-08-05 03:49:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0121a547-e323-32e3-ad5b-11eab7857c8e | -11.7928 | -45.00469 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4d08c34b-6498-36a3-b585-677bb706eca9 | -8.93903 | -46.73662 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8b7f6fe2-800e-3e0f-b968-99742092e2d1 | -7.99308 | -43.15346 | 2025-08-05 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4057d736-1681-3062-9086-55739304415b | -10.33334 | -47.82513 | 2025-08-05 03:49:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1f480f93-60f5-308a-9e6a-9e541d54d065 | -8.26263 | -45.07047 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2456e7cc-b7f4-3932-9d2d-56076102ac0d | -7.38665 | -44.64227 | 2025-08-05 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d3aa904-072a-3c0e-bc3d-ab911d5d8d65 | -7.75587 | -45.23545 | 2025-08-05 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eac5e194-b78f-3c63-b7fe-211ff9770f66 | -8.71651 | -46.43938 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c0ae725-c7d9-3b53-a95a-de7caa502f44 | -12.7206 | -47.79243 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7991010e-f2fd-38bd-931c-65d1d68022c3 | -10.47516 | -44.37094 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6f5ce54-63e5-35e9-8496-3215f57d28d4 | -10.77384 | -46.64328 | 2025-08-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cabb9625-1725-39af-a928-240418285b5a | -10.44786 | -44.37092 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 10676a97-e663-38bf-9e9f-fb2841a33c00 | -9.0521 | -45.0644 | 2025-08-05 03:49:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44348d97-f98e-3690-be8d-9022bf241624 | -6.9682 | -42.86869 | 2025-08-05 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 1a437d12-d70c-3e6f-9e7c-420f263b2d15 | -10.47595 | -44.36653 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30113212-0f4a-345c-b89f-178a7e02c064 | -8.1545 | -49.14306 | 2025-08-05 03:49:00 | NOAA-21 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ad79e8f-2a7d-34fd-84a1-aaeb4e5a68e6 | -7.53845 | -44.87144 | 2025-08-05 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acc69434-7063-3c47-ab78-67a5a32646f5 | -11.35856 | -41.40633 | 2025-08-05 03:49:00 | NOAA-21 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 84a4d251-2903-3656-aa2b-bec5e231810c | -7.53704 | -45.04765 | 2025-08-05 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4feca9fc-dd52-3f9d-b118-3c39a97a6c75 | -12.67419 | -48.12229 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f269bdc1-9389-333e-b4ba-0c9be0d8ccc6 | -12.44124 | -48.72079 | 2025-08-05 03:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09003bd5-1f7f-393a-8973-e5935e6926c3 | -8.2483 | -45.06448 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68e9a339-5311-37e7-985e-82e97c56c563 | -8.93845 | -46.73989 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 7c82534e-dbf0-356c-acbd-41ef6a92d337 | -7.06807 | -43.69862 | 2025-08-05 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9fea9c9c-71af-3b05-8b70-10ef26735263 | -8.018 | -43.1866 | 2025-08-05 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 80365200-9f1d-3809-ba85-ecfa27e1b9a6 | -10.47877 | -44.37621 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7113a0bf-3cc4-35cd-8c9b-75bd23791e99 | -8.71186 | -46.4353 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18942bd6-96ea-3c41-849b-04990f7be8cc | -6.67994 | -49.79271 | 2025-08-05 03:49:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| be6c4ae4-518f-3d09-921c-4e718da926a5 | -10.46994 | -44.37466 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd47d29b-7317-386b-9eca-bb450ac6b22c | -8.24926 | -45.05915 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dbb9d69a-6014-3817-a9b3-932defa8815b | -6.96128 | -43.31537 | 2025-08-05 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dc887730-bb35-38f2-8d33-c0e93e522d1d | -8.22031 | -45.05769 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 62b6336e-d1bf-3474-9e76-6456e046685d | -10.78403 | -46.64533 | 2025-08-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59474879-7332-3104-8210-32ad5a079b85 | -9.2969 | -40.24272 | 2025-08-05 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 3c531c64-d86b-3785-adf9-8525ce060ea8 | -9.17853 | -48.84747 | 2025-08-05 03:49:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README10.md)
