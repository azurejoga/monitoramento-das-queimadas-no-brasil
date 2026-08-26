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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e02b7b6a-2030-3bef-946b-c8874f3ee0e6 | -6.641 | -58.4987 | 2026-08-26 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 117.3 |
| d576d8ae-1a1c-3a15-98bc-75e79a375cf4 | -7.0612 | -59.2358 | 2026-08-26 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| feccb350-02da-31d0-b4a1-877cbb6c830c | -7.5289 | -61.3825 | 2026-08-26 02:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 244.8 |
| ced9f8b6-78d4-3e98-a13c-7650bbefd20e | -7.0796 | -59.2351 | 2026-08-26 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 4ca41bc8-894d-388c-93d7-f792e217938b | -7.0243 | -59.2181 | 2026-08-26 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| b8c2fb0b-e729-3257-b5f2-647fc0255ce2 | -14.7977 | -48.8074 | 2026-08-26 02:50:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 5f078f51-7a1b-3093-b568-3b28fe9742ce | -13.228 | -51.3759 | 2026-08-26 02:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| f05322d9-3bd9-3eac-b155-9234e4c30b66 | -6.6226 | -58.4995 | 2026-08-26 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 6cef7d19-3dc3-38f2-88df-08dc72db235e | -7.0242 | -59.2374 | 2026-08-26 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| f45f5615-fef2-3083-8767-f5ea748a9d06 | -6.6595 | -58.498 | 2026-08-26 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| c4e95929-9f72-3657-8ef4-92651048b8b0 | -13.3031 | -51.4731 | 2026-08-26 02:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 156.4 |
| d1826547-76dd-360a-8243-782f92b5ae02 | -6.2677 | -53.3565 | 2026-08-26 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 49c847ac-b958-32d8-9731-53bd15293d3f | -7.0797 | -59.2157 | 2026-08-26 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 115.6 |
| b6eaf8af-eb20-3df7-a23d-176d36c0c24a | -7.5104 | -61.3832 | 2026-08-26 02:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 169.6 |
| a6c2a2d7-620f-3f71-b804-61a07d2013e5 | -6.6409 | -58.5181 | 2026-08-26 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| b37dc9d0-33bc-3453-9e54-7cb677bc8fb3 | -9.6024 | -55.1078 | 2026-08-26 02:50:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| b35e79ba-a5b8-325e-85ba-81e1f2e49f98 | -7.5288 | -61.4015 | 2026-08-26 02:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 2a1b1be1-dd8c-37f3-aaca-b697725fa282 | -14.7981 | -48.7851 | 2026-08-26 02:50:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 184.1 |
| d0e7bb43-fb38-37bf-8f7d-a2ac13fba1b2 | -10.7596 | -54.0384 | 2026-08-26 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 175.7 |
| c604ae14-932c-3f3a-a7b8-806193ca296a | -6.2676 | -53.3768 | 2026-08-26 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 12e7f23c-60de-3a34-a37b-974af46ccc70 | -6.6409 | -58.5181 | 2026-08-26 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 67e232f6-2bc4-3fa9-bfea-cdcf662b3dd4 | -6.2676 | -53.3768 | 2026-08-26 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| dc435256-ede7-30f1-b891-cd5010323b7a | 1.4734 | -56.0036 | 2026-08-26 03:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| cfbb7414-07ce-39f7-a0da-f56ca107cca2 | -10.7598 | -54.0179 | 2026-08-26 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 7599b0bc-2e26-368d-b29a-c471237679e6 | -13.2465 | -51.4162 | 2026-08-26 03:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 8ce10215-0705-3dff-8456-2ad51caa2c22 | -7.5104 | -61.3832 | 2026-08-26 03:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 132.6 |
| aa9d277e-6a58-3700-b145-14802a0cf003 | -7.5288 | -61.4015 | 2026-08-26 03:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 28379fb7-8f2b-338f-a240-db52dffe3f25 | -13.2839 | -51.4755 | 2026-08-26 03:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 923258b8-137d-35fb-accf-432e1bcaa52f | -13.1903 | -51.338 | 2026-08-26 03:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 003bd183-5a7a-3953-97df-1d4f284e3ca5 | -13.19 | -51.3593 | 2026-08-26 03:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 86ab5495-9e5f-3d64-9737-9204267208ca | 1.4734 | -55.9642 | 2026-08-26 03:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 7b34f1f1-cb41-3075-bc6c-05392e3dd409 | -6.6226 | -58.4995 | 2026-08-26 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| c61971c5-bf31-3449-b53a-697821a6e26c | 1.4917 | -56.0034 | 2026-08-26 03:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 88c858d8-187d-36ab-a61a-325357ebaef6 | -13.3031 | -51.4731 | 2026-08-26 03:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 218.1 |
| 5386e6f9-0eaa-3f49-9ae0-65fb5338dbcb | -7.0612 | -59.2358 | 2026-08-26 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| e6e66b0b-375b-3929-b597-7abed6988711 | -13.2469 | -51.3949 | 2026-08-26 03:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 182.2 |
| 7f551f92-a03c-304d-b203-d31508c6bf31 | -6.6595 | -58.498 | 2026-08-26 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| da672554-1105-3988-bedf-801bb279513b | -7.0797 | -59.2157 | 2026-08-26 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 20ff60e8-490b-350e-95b4-451dcf64e4c8 | -7.0242 | -59.2374 | 2026-08-26 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| ea6ad58c-bcf3-3678-b19f-18e23f95fd87 | -7.0243 | -59.2181 | 2026-08-26 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| d6e60b2a-5ecc-317a-9f4a-02bc61718c58 | -13.2277 | -51.3973 | 2026-08-26 03:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| e276bd84-0cfd-3ccb-9ea7-c6250b65fa84 | -14.7981 | -48.7851 | 2026-08-26 03:00:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 112.4 |
| dec74113-91a5-366e-83df-1106f4d9f8f6 | -10.7784 | -54.0368 | 2026-08-26 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 126.5 |
| aa46ba98-e912-31fd-bdea-05580214f7c5 | -6.641 | -58.4987 | 2026-08-26 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 8fc7702e-7b37-3ee7-9c6a-a88da36a20a2 | -14.7977 | -48.8074 | 2026-08-26 03:00:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 3a5aa05f-7f72-3356-a3fb-2c26d8aca81f | -10.7787 | -54.0163 | 2026-08-26 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| f49baff8-9ec1-3a6d-a044-2689dec98cea | -10.3723 | -45.0767 | 2026-08-26 03:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 56aaf05e-9f2f-3035-9f21-690c9d310c6e | 1.4917 | -55.964 | 2026-08-26 03:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| e6b89225-b4ed-3c46-87a3-1f3e43a72ab0 | -13.2842 | -51.4541 | 2026-08-26 03:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 68fab1ff-bc55-3e39-9ba5-2b6eac39cee2 | -13.228 | -51.3759 | 2026-08-26 03:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 62885442-9fb4-326c-bb1d-20a15a36ea0e | 1.4917 | -55.9837 | 2026-08-26 03:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 30bd8058-e8ba-3d03-9e22-3c91c38b132e | -7.0796 | -59.2351 | 2026-08-26 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| fc3a3a88-6168-3357-8146-fdc65b97d20b | -13.3027 | -51.4944 | 2026-08-26 03:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 14e9540c-b7d8-3170-9e6b-01f29f4c40ee | -7.0613 | -59.2165 | 2026-08-26 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 17ffb01a-0314-31cf-92cd-52ee077d91ea | 1.4734 | -55.9839 | 2026-08-26 03:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| c6f603f3-2e5a-30a7-9335-665445ca1e78 | -13.2661 | -51.3925 | 2026-08-26 03:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 792be586-5c1d-3544-bf9c-2e97fe973d49 | -13.2472 | -51.3735 | 2026-08-26 03:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 830732c9-8117-3ac4-afbe-807f22315ffb | -7.5289 | -61.3825 | 2026-08-26 03:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 242.0 |
| 6857aa7f-350b-3827-a468-d5da159c7f2a | -10.3727 | -45.0537 | 2026-08-26 03:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 97.8 |
| ba4de69e-e02b-313c-9a6a-5bdb575940ec | -6.2677 | -53.3565 | 2026-08-26 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| bbd3e493-0d82-3b9a-9528-c2536c14a167 | -10.7596 | -54.0384 | 2026-08-26 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 307c62f7-97b2-300c-803b-d07ff946d4f0 | 1.4734 | -55.9642 | 2026-08-26 03:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 316a4b5c-3afe-381c-afe6-f0fe60efbfd4 | -14.7981 | -48.7851 | 2026-08-26 03:10:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 93bac9af-8662-3d19-81dc-76fd44b07943 | -6.2677 | -53.3565 | 2026-08-26 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| f291d8c9-405c-3696-a54c-f971bf6876f2 | -13.2842 | -51.4541 | 2026-08-26 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 83fb6a3b-dbcc-3f99-b7fc-c069b9ac72b2 | -7.0612 | -59.2358 | 2026-08-26 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 3a63fb52-62d2-3254-a9f7-c9b9b99271be | -10.7787 | -54.0163 | 2026-08-26 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 88d70093-ee3e-3dc8-84d7-ec89de0c32d9 | -7.0796 | -59.2351 | 2026-08-26 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 6d9bf786-09ea-3e6a-b60d-46a4cf40be5a | -6.6595 | -58.498 | 2026-08-26 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| ec48eed0-7522-364b-9917-b9693a88c47d | -13.2661 | -51.3925 | 2026-08-26 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 7321ae05-8b39-341a-ab4a-8755c99387c7 | -7.0613 | -59.2165 | 2026-08-26 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 28eda9f1-dc08-3ade-9294-52667a1d6ffe | -14.7977 | -48.8074 | 2026-08-26 03:10:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 92.7 |
| f4b5cac9-dc34-353d-a585-981fdb15ba6d | -10.3727 | -45.0537 | 2026-08-26 03:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 5f68911f-ea49-3dd6-a9cd-938a8eda177a | -6.6409 | -58.5181 | 2026-08-26 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 4a41fdc7-e0b3-38b9-ac17-53d73c1eb235 | -13.2472 | -51.3735 | 2026-08-26 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 065c0f80-fd97-3a2e-98b8-a89a19fe7930 | -13.2469 | -51.3949 | 2026-08-26 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 215.4 |
| 27cf9269-eaed-3a74-893c-51d4bce8a95a | -7.0242 | -59.2374 | 2026-08-26 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| e6c7d985-eb67-3a09-aa22-fd4752dbfe53 | -13.1903 | -51.338 | 2026-08-26 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 9250f6eb-a11b-306c-a6ee-ef835d4464cc | -6.2676 | -53.3768 | 2026-08-26 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| fc8cd36e-fb39-34d0-a245-ae6507d5542a | -13.19 | -51.3593 | 2026-08-26 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 9b777141-7cfc-3c83-86df-6438537b3a49 | -6.641 | -58.4987 | 2026-08-26 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 71b43b4d-e1da-3e8a-9957-56a8fef1bc02 | -7.5289 | -61.3825 | 2026-08-26 03:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 176.1 |
| 043cb7a5-6a1c-3eac-9c64-10bea2099eb3 | -10.7598 | -54.0179 | 2026-08-26 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 123.2 |
| b420f8cf-90ff-3389-b481-2ed990e38d2c | -9.6024 | -55.1078 | 2026-08-26 03:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 156c82ee-b520-390b-9262-346e7df253e7 | -7.0243 | -59.2181 | 2026-08-26 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 42a49d17-e8f5-323b-b7d2-11f6158259e2 | -7.5288 | -61.4015 | 2026-08-26 03:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 950e7c7f-2449-3024-93ab-3432fb11d483 | -10.7596 | -54.0384 | 2026-08-26 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 139.1 |
| b1c53a26-f310-3b86-b0b1-0bbf21727ba3 | -13.2839 | -51.4755 | 2026-08-26 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 5138b1dc-add5-381f-9384-c956ff785cbc | -10.7784 | -54.0368 | 2026-08-26 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| ab9c8b9e-e36b-3a72-8345-e92f222d1094 | -13.2465 | -51.4162 | 2026-08-26 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 01a80d46-0596-3af9-870a-9369dbc46f9e | -7.0797 | -59.2157 | 2026-08-26 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 3380d3b9-1428-30f9-96e3-1ab62c7e23ec | -13.3031 | -51.4731 | 2026-08-26 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 123.9 |
| e58fa617-3c41-3eff-96a7-f30f11b75631 | -13.2277 | -51.3973 | 2026-08-26 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 8cc5a3c9-5d35-393b-9039-596b8cf226c4 | -6.6226 | -58.4995 | 2026-08-26 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 4135f326-4cb1-35b6-943f-e5f10178d376 | -13.228 | -51.3759 | 2026-08-26 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 86a87029-4a27-3afb-82ab-71ecfa62164f | -7.5104 | -61.3832 | 2026-08-26 03:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 130.5 |
| c366a202-c713-3feb-9134-9eaff7aaea0c | -6.56835 | -35.17217 | 2026-08-26 03:10:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a8fcb1ca-f6f8-3235-8f7b-f1f2fdd013e4 | -6.85862 | -38.3482 | 2026-08-26 03:13:00 | NOAA-21 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5a8af70e-f791-39b7-8bdf-c1b11947285d | -6.85787 | -38.35242 | 2026-08-26 03:13:00 | NOAA-21 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f420d664-423e-3eef-96a0-18e195d5c911 | -6.85603 | -38.34834 | 2026-08-26 03:13:00 | NOAA-21 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |


[Clique aqui para ver as próximas entradas](README9.md)
