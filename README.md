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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3543760-a81e-3f1d-8a46-eb8a3bc10b35 | -12.8548 | -44.3625 | 2026-06-16 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 9d1fa847-85bd-397e-9956-0803a3b1549a | -9.3423 | -45.4765 | 2026-06-16 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 082ca742-6302-3068-9437-18361baca827 | -8.9449 | -46.9582 | 2026-06-16 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 196.1 |
| fa36141d-4d03-359e-a110-2fe36a09e29d | -9.3427 | -45.4537 | 2026-06-16 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.6 |
| bf718241-2c2a-3b80-94cd-9e94719eb14d | -10.1493 | -56.6115 | 2026-06-16 00:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 0460a9f5-2528-3704-8fcc-337966369b73 | -9.3234 | -45.4787 | 2026-06-16 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 1e5b351b-f2fb-349c-a4ac-d26cc892e057 | -6.4021 | -44.1658 | 2026-06-16 00:00:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| b189489d-15b0-3b41-9c9f-84525cfeafb1 | -4.3588 | -47.7636 | 2026-06-16 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| bfea16eb-f0d4-3138-ab6d-df1f0ea22870 | -8.9452 | -46.936 | 2026-06-16 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| f5e51572-b139-321e-aa47-dc2cfc6bb6cb | -11.4787 | -57.109 | 2026-06-16 00:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 58130d18-5131-3504-b3c0-39c250b7d553 | -11.5502 | -52.7659 | 2026-06-16 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 80e2ebff-f6ad-31bb-b41c-322cfaba1d5e | -11.5499 | -52.7867 | 2026-06-16 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 2e91ad0c-93fd-3027-b734-e378ee066c2e | -9.34 | -45.4613 | 2026-06-16 00:05:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| af2b4890-0a96-3b53-bf63-6509e4f821ba | -9.3448 | -45.484001 | 2026-06-16 00:05:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 07d70cbd-6a72-3390-9db5-bad1a18fc4c1 | -9.335 | -45.486099 | 2026-06-16 00:05:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f0e98856-61dc-36c8-ab53-9aed6292111d | -4.3611 | -47.754299 | 2026-06-16 00:05:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f512c372-08c1-3d77-8ddc-3fe701f4e4ca | -6.9752 | -42.882 | 2026-06-16 00:05:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5bc449f1-bb44-3a81-adb2-426cb1372a31 | -5.9244 | -43.471699 | 2026-06-16 00:05:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4019c55a-fe06-3884-b7a8-e182de322e72 | -8.9368 | -46.935699 | 2026-06-16 00:05:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb1c94ad-2d6a-31fd-8df5-ff7d51a2183b | -6.3873 | -44.168301 | 2026-06-16 00:05:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2430d400-bf40-3b34-8700-05c733d7dc5a | -9.3326 | -45.4748 | 2026-06-16 00:05:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 43aa6541-248a-37ac-a182-fbcf8a94db72 | -8.9299 | -46.951801 | 2026-06-16 00:05:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73fce474-7b24-37f0-a685-ed3c9e737843 | -8.9495 | -46.9478 | 2026-06-16 00:05:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe6caa3f-8aef-370d-a929-512a122883a0 | -8.9798 | -47.972698 | 2026-06-16 00:05:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2194dc7d-ec44-35ae-827c-661ade64fbb9 | -5.7991 | -43.785599 | 2026-06-16 00:05:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2b5feca-8d7a-3d3b-bfba-338fc2a7189d | -5.8361 | -43.491001 | 2026-06-16 00:05:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05c4316b-a202-30ab-aea6-cbc368f1d572 | -8.9525 | -46.9618 | 2026-06-16 00:05:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a431c834-9284-31c4-af2d-7909804305be | -5.9262 | -43.479599 | 2026-06-16 00:05:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9700f323-01fb-30a1-926e-8b356b41ae2b | -4.3513 | -47.756401 | 2026-06-16 00:05:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e94c6af-a3fd-3676-a604-32ba646f4148 | -5.5806 | -43.4972 | 2026-06-16 00:05:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3bdb350d-8dca-38c8-9976-1eec07d5d319 | -5.8009 | -43.793701 | 2026-06-16 00:05:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0ab4091-3a74-3521-aec4-3c43b9297f57 | -8.185 | -46.750702 | 2026-06-16 00:05:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1bf39764-3d03-3415-a56b-dbbff1c97c97 | -5.5823 | -43.505001 | 2026-06-16 00:05:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6027b0d7-6887-3033-aa77-6d5331e29b7a | -3.9608 | -43.111 | 2026-06-16 00:05:00 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37bb23a8-414d-3d5f-bd31-14dd81ff4d14 | -7.7187 | -44.1577 | 2026-06-16 00:05:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fe5b7561-c0ce-342a-8fcc-7a4d864b1ea1 | -9.2643 | -48.568199 | 2026-06-16 00:05:00 | METOP-C | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4833e6f2-9bad-3c2c-bb2f-711cf89dbd53 | -6.2996 | -43.633701 | 2026-06-16 00:05:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78f22f4e-e161-3fe4-a8e4-de33b88c5e8a | -7.7207 | -44.166698 | 2026-06-16 00:05:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d8480d68-8339-3b2e-b95e-4fc73e09fff1 | -6.9718 | -42.866699 | 2026-06-16 00:05:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9a6c2dc4-9525-3abe-b3b6-661fec590736 | -8.9466 | -46.933701 | 2026-06-16 00:05:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 19d8364e-797f-3cfd-88b8-5b9d4c9ef122 | -6.3971 | -44.166199 | 2026-06-16 00:05:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f31e4a3b-30cf-3c1c-bbb7-e32d92929709 | -9.3228 | -45.476799 | 2026-06-16 00:05:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1ca6dc61-4718-335d-a849-d8c79d31e283 | -4.3483 | -47.742901 | 2026-06-16 00:05:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1aaa179-55ca-3a84-877d-a5f4464a0e74 | -9.3604 | -46.478802 | 2026-06-16 00:05:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9aca26b-82df-3f49-ad69-8fb079e4119a | -6.9735 | -42.874298 | 2026-06-16 00:05:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 639465fc-f36e-390d-b78c-b0c309238652 | -5.8054 | -45.0644 | 2026-06-16 00:05:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 625dd85d-8346-3e83-9b57-ef56fee9f491 | -5.7998 | -45.085602 | 2026-06-16 00:05:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bbd9d42f-2669-3a05-a7c4-da54cae86ae4 | -5.5921 | -43.5028 | 2026-06-16 00:05:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 071be0f4-034d-3da0-8142-a7e78b32650b | -5.8326 | -43.475101 | 2026-06-16 00:05:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71eb7c79-8080-3b8d-a983-0c5c855c0214 | -8.9397 | -46.949799 | 2026-06-16 00:05:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2941a0c4-1eea-33fd-87df-38449737ed6c | -5.8075 | -45.073898 | 2026-06-16 00:05:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2c6cca8-54f4-30a1-94e3-ece2838db0fa | -5.7977 | -45.076 | 2026-06-16 00:05:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0581e3b-ea3c-37f8-9e32-1e8ab4157d8b | -6.3892 | -44.176998 | 2026-06-16 00:05:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4780b513-da5b-327d-afcf-dfe3e282db71 | -6.3032 | -43.650002 | 2026-06-16 00:05:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12972a4b-598e-3696-9aff-8e281fc8e8b0 | -4.3543 | -47.769901 | 2026-06-16 00:05:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54d2fa2d-c955-30d0-b80b-bc7125822671 | -5.8344 | -43.483002 | 2026-06-16 00:05:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb3d8889-3868-35c3-8b7c-d5b911cc7a47 | -8.9329 | -46.965801 | 2026-06-16 00:05:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0697ec9-4b3e-3be2-b739-467842bb080c | -3.9625 | -43.118301 | 2026-06-16 00:05:00 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e04b8d9c-09a4-3e62-ab05-b13a5f36032a | -5.7956 | -45.066502 | 2026-06-16 00:05:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 620364c6-7f2c-30f7-b2d0-68957fd9031a | -9.3424 | -45.472698 | 2026-06-16 00:05:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ffb20eab-f400-374e-8163-fcee4e92e699 | -6.9769 | -42.889702 | 2026-06-16 00:05:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bde4e32c-f8f6-3826-84ec-2b5a382ce2ec | -6.0052 | -47.099499 | 2026-06-16 00:05:00 | METOP-C | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 819d86a5-5432-3811-876b-0c5df1bfb1ab | -9.3252 | -45.488201 | 2026-06-16 00:05:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1f538740-8cbb-31c1-bf43-7653180429ab | -9.3302 | -45.463402 | 2026-06-16 00:05:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e0260942-48cd-303c-97c6-d32aa784788c | -8.1878 | -46.763901 | 2026-06-16 00:05:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b5287e63-5511-36d8-9a51-b60c6d5627b9 | -8.9701 | -47.974701 | 2026-06-16 00:05:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c15419f4-b6fa-3d91-ad49-3407e9ed9f4f | -8.9427 | -46.963799 | 2026-06-16 00:05:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e053ca39-9939-30ec-aa28-28760c5e6cae | -9.3632 | -46.4921 | 2026-06-16 00:05:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a14aae7-bb26-3dd1-bb25-67c6312b9ec7 | -6.399 | -44.1749 | 2026-06-16 00:05:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d7d4a46-1b8a-35f5-8d36-8f61966a7032 | -6.3014 | -43.6418 | 2026-06-16 00:05:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be4ef3f8-4e57-338f-b9b3-bc341da68ba2 | -7.3547 | -49.8564 | 2026-06-16 00:05:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df9b8963-d0de-3235-b2ec-6b0490561136 | -4.3588 | -47.7636 | 2026-06-16 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 31bd8ee1-4a30-30a7-a9e4-643fc7f909ac | -11.5502 | -52.7659 | 2026-06-16 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 1ec2fd7c-969a-35c6-8dec-c5a28c389ec5 | -9.3234 | -45.4787 | 2026-06-16 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 8f7f3417-2b58-37f9-8cc3-bd56e0a84149 | -8.9452 | -46.936 | 2026-06-16 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 689b0888-3cbc-3b11-ac4e-79836669251c | -11.5309 | -52.7887 | 2026-06-16 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 916b68c5-ea37-32d4-bb77-e36e9e4ec983 | -9.3423 | -45.4765 | 2026-06-16 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 4f07b58f-b31e-398b-b610-e2a743542864 | -6.4021 | -44.1658 | 2026-06-16 00:10:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 909c61f8-7b16-347a-ac02-95372bcd3c6d | -11.5499 | -52.7867 | 2026-06-16 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| e3c6eda6-246a-347e-b15d-4e5368dcbe49 | -8.9449 | -46.9582 | 2026-06-16 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 56ea545c-531f-349e-9afd-43a5e5734034 | -8.9449 | -46.9582 | 2026-06-16 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 27243bc1-997f-3f43-9fee-121da322f73c | -4.3588 | -47.7636 | 2026-06-16 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 9b52f0bd-ba3b-3901-877b-cf928f38edc9 | -16.1047 | -39.2977 | 2026-06-16 00:20:00 | GOES-19 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 52.8 |
| dd795ed9-0564-3776-8070-b5c4791135f2 | -11.5499 | -52.7867 | 2026-06-16 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 481046d0-2a72-32a5-a537-b94d63937a4a | -6.4021 | -44.1658 | 2026-06-16 00:20:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 4dc797a1-ad90-36ad-a1b5-f7d816f97f91 | -9.3234 | -45.4787 | 2026-06-16 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 2fca01e1-d346-32e6-a952-71f49e698c83 | -11.5502 | -52.7659 | 2026-06-16 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 1c6bacad-e814-344e-bf8e-2e035ca6a6f7 | -16.1247 | -39.2926 | 2026-06-16 00:20:00 | GOES-19 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 60.1 |
| 70bbf877-4f64-398f-8787-d3c6dfbf8e8d | -9.3423 | -45.4765 | 2026-06-16 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 81719f82-db3a-399b-9894-f2b71f780a82 | -8.9449 | -46.9582 | 2026-06-16 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 4cf19a80-c8cc-3748-b5a9-d5568b0e44ea | -11.5499 | -52.7867 | 2026-06-16 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 8cd0f12a-7cc5-3062-bd8b-9180dc577aa1 | -9.3423 | -45.4765 | 2026-06-16 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 87c1e478-5c90-32b6-a7b7-5a3b19ff2ddd | -11.5502 | -52.7659 | 2026-06-16 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 5f6e7189-afad-3317-9f4d-233d103ad9d0 | -4.3588 | -47.7636 | 2026-06-16 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| f7a5d7e5-0d43-30d4-b86f-b6c65f706df8 | -8.9449 | -46.9582 | 2026-06-16 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 169392cf-366c-3b32-8344-f3b32977eddd | -11.5499 | -52.7867 | 2026-06-16 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| b6146e86-191a-36eb-bd07-7b50bdbe171e | -9.3423 | -45.4765 | 2026-06-16 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| e61fe781-1bd3-3bf6-a506-736b5f9070ff | -11.5502 | -52.7659 | 2026-06-16 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| d9668973-0e02-30ea-a673-9411ac9f7b63 | -8.9638 | -46.9563 | 2026-06-16 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 88788ea2-960b-3bc2-9a58-7bfe5397fa64 | -11.5502 | -52.7659 | 2026-06-16 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |


[Clique aqui para ver as próximas entradas](README2.md)
