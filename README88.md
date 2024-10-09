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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee632905-c0b8-3e77-aa8e-63380dc214c8 | -22.7941 | -46.76005 | 2024-10-09 04:17:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1c9d29d6-3358-3f42-a629-83a1bffa037f | -22.77781 | -46.99448 | 2024-10-09 04:17:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5537edcc-4c3b-3fc0-99e6-fc508ec6e2cc | -22.75566 | -47.00573 | 2024-10-09 04:17:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c4e92b8c-5d33-3b95-81ab-8b13b179fb4d | -22.75236 | -47.00513 | 2024-10-09 04:17:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 5132a418-3a27-3ba1-958f-3f5e27deced5 | -22.58195 | -46.70309 | 2024-10-09 04:17:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 49eed2eb-52ac-375a-8fae-47dbc05b0227 | -22.58112 | -46.66469 | 2024-10-09 04:17:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 25bf509c-f621-3ff5-a4a5-d49db774b69c | -22.57865 | -46.70249 | 2024-10-09 04:17:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e8ff05ef-80e5-3d7b-8b71-f3e1175bb5ad | -22.57807 | -46.7062 | 2024-10-09 04:17:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 86472a69-edef-3de3-a4e7-a5632af1a6a7 | -22.57782 | -46.66409 | 2024-10-09 04:17:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 639a6db5-7b93-3120-9a16-b90a3eccb496 | -22.57724 | -46.66779 | 2024-10-09 04:17:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4317f88c-ff5a-3fe9-b3b3-a252155bc7a8 | -22.57612 | -46.58729 | 2024-10-09 04:17:00 | NOAA-21 | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ce98559e-8a00-3900-b61c-ec0fd2bc956a | -22.5679 | -46.66228 | 2024-10-09 04:17:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b213a0d2-2a49-3989-9431-d9bd9a37a0ef | -9.28613 | -45.31748 | 2024-10-09 04:17:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0eaec76f-c18c-339e-8a5f-612db8f08797 | -9.22785 | -45.67497 | 2024-10-09 04:17:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad70752e-5e7b-394f-9132-e264decd483b | -9.67699 | -44.49598 | 2024-10-09 04:17:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aee85bc2-d0be-3d4d-b206-ea4bba5d3a5a | -9.67643 | -44.49949 | 2024-10-09 04:17:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1df65283-e407-329c-a980-ac0147706ef7 | -9.67312 | -44.49895 | 2024-10-09 04:17:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab7ab323-e2df-3dc4-9961-e38f63262736 | -9.53555 | -44.44456 | 2024-10-09 04:17:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7491b9c3-5206-3938-8ee4-a4bd852fae3a | -9.53279 | -44.44053 | 2024-10-09 04:17:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 379d043e-fef5-3cd5-b57c-490fe84f0daf | -9.52837 | -44.44701 | 2024-10-09 04:17:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7240788-311b-3ed3-9a21-67c694d1a9c9 | -10.80548 | -45.14783 | 2024-10-09 04:17:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14450e2d-9191-3af9-afbc-2344cd1637be | -10.80215 | -45.14728 | 2024-10-09 04:17:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4b17a493-bca7-3e85-b633-eccb2f8d5f43 | -13.54667 | -45.44061 | 2024-10-09 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba5e48ca-dbd6-3af2-814d-2a4bb3301744 | -10.77112 | -45.52563 | 2024-10-09 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b54739be-06ba-37ad-a4c8-f27e69cc4c07 | -10.72023 | -45.02042 | 2024-10-09 04:17:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c95e0b4-3976-369f-9973-7bfb008f02c0 | -10.71966 | -45.02396 | 2024-10-09 04:17:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10d61963-6580-397c-96a1-1c0d25165e3e | -10.45903 | -45.12057 | 2024-10-09 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee9a9ed5-dc51-3bb3-a79a-6b1b001d1879 | -10.45569 | -45.12002 | 2024-10-09 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69514fe5-4226-3f61-a785-0ccf985a3513 | -10.45512 | -45.12358 | 2024-10-09 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff3c79e6-7de0-3d22-8d4e-f675c3928a3b | -10.45122 | -45.12658 | 2024-10-09 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20f32076-44e0-3442-8e14-2eb8ca8e3609 | -10.44732 | -45.12959 | 2024-10-09 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee36827d-96c0-3219-80bf-32e2dd435b92 | -10.44341 | -45.1326 | 2024-10-09 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 576ce79d-695c-38b3-bfa8-951778440cb3 | -10.31127 | -45.4273 | 2024-10-09 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 826c633e-3307-34cb-8fb4-fbc39d8dc896 | -10.12112 | -45.21172 | 2024-10-09 04:17:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 853a119e-6790-3d04-a053-94fb88c80970 | -10.11825 | -45.2296 | 2024-10-09 04:17:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1579f300-367f-3009-aaed-7ebf069a56df | -10.11778 | -45.21114 | 2024-10-09 04:17:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4641c22a-a9b5-37bd-95c6-9e334b9b6515 | -9.83508 | -45.48503 | 2024-10-09 04:17:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afd70a2e-444a-34b8-8b56-33e3fa5003dc | -10.94255 | -44.77818 | 2024-10-09 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e2c785d-72eb-30d8-87e2-87b1d6099641 | -11.65422 | -45.26861 | 2024-10-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27fe8201-a59d-3d3d-a7dd-c4f97f191cd5 | -11.6509 | -45.26806 | 2024-10-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c197499-a153-3644-93d9-429668424c55 | -11.64927 | -45.2569 | 2024-10-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae81dedc-25de-35be-a4a0-a26d0d3aac5c | -11.6487 | -45.26041 | 2024-10-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a5c1f9d-3f48-3f9e-84ca-ec94c6c1d74a | -11.64814 | -45.26395 | 2024-10-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ed5bc60-84e3-3d48-8952-a4239e4e4753 | -11.64538 | -45.25986 | 2024-10-09 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79e1cb6c-d9b3-306e-8156-8c9d0ba61e4b | -11.26951 | -45.01261 | 2024-10-09 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 858d413f-86d6-3429-8282-2ea8ddfc734e | -11.14245 | -45.37935 | 2024-10-09 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63a17a99-cb25-3c9d-bce6-dec155eedc27 | -11.13911 | -45.3788 | 2024-10-09 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3fdde13-9ae0-3ee5-8b3b-dd7cf7a221ea | -11.1291 | -44.95351 | 2024-10-09 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e1b2d603-85f9-3a37-84f7-dfca67d6fe3f | -11.12634 | -44.94945 | 2024-10-09 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 02bedd91-f2af-3126-89cc-ee35e06ac437 | -11.12578 | -44.95298 | 2024-10-09 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 966d4e07-e5fb-3a2e-b033-6ee8659fcf0a | -12.37586 | -44.97073 | 2024-10-09 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7f96d51-0edd-3139-bd94-c83a58777cdb | -12.3753 | -44.97424 | 2024-10-09 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 853886b6-7953-372d-a079-0e160dc9e0ea | -13.54885 | -45.44827 | 2024-10-09 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12e0fd2b-885c-3928-a5c0-f5a99d0587eb | -13.54724 | -45.43705 | 2024-10-09 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35c4bae3-c063-3b63-b36d-2bdfb6c2c138 | -13.54553 | -45.44772 | 2024-10-09 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7da7f42-3ec3-3e42-93ff-bfcd39e137b0 | -13.54336 | -45.44005 | 2024-10-09 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f4694c5-2700-35ff-bf94-b9f6eed6d9cb | -13.54222 | -45.44716 | 2024-10-09 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cdb5db0-b134-3f78-be17-6a1fe0a0bf8e | -13.50167 | -45.67867 | 2024-10-09 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2ddfc61-e617-379b-a8ad-9fdcfa848f91 | -13.24263 | -45.53247 | 2024-10-09 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b59d9f7d-bed2-3e7e-af1f-2c51ffe319d8 | -13.2321 | -45.53439 | 2024-10-09 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d275f679-0913-3919-b63e-329b9a545a02 | -13.22878 | -45.53384 | 2024-10-09 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf76eedb-81cd-385b-8554-6e00ed48f6c4 | -12.99677 | -46.23237 | 2024-10-09 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 540611ee-edaf-397a-8d97-3a3dee1df9aa | -12.99338 | -46.23186 | 2024-10-09 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24b84ac7-06cd-370a-9a85-842ae912418f | -12.99119 | -46.224 | 2024-10-09 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c7658a4-e2e6-3f5d-9fad-e6c3460fcbea | -12.9878 | -46.22354 | 2024-10-09 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d1a6f8f-70bb-37a7-ad2f-6b162240da70 | -12.98347 | -46.20758 | 2024-10-09 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3ac5c1b-23be-323c-a188-177c27f0ec63 | -12.98286 | -46.21133 | 2024-10-09 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 52c37820-81ec-36da-b54b-d799a6210890 | -12.98009 | -46.20709 | 2024-10-09 04:17:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3aa4755-e964-3dd0-9cc6-f5b92beb48e0 | -12.37861 | -44.97478 | 2024-10-09 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ac64c616-dced-3720-98e8-8471ab5d2d78 | -12.37805 | -44.9783 | 2024-10-09 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d628714a-fa9e-38b4-a459-9625711bfaad | -14.18848 | -45.49309 | 2024-10-09 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4380241c-9b1e-3cfa-b428-b6e220754bfa | -14.183 | -45.48487 | 2024-10-09 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7ad69e9-0e26-3d7a-ab6b-f66ea9da29c5 | -20.90756 | -47.4103 | 2024-10-09 04:17:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a9c6840-184b-33c1-a228-9bf01faff231 | -20.8188 | -47.7026 | 2024-10-09 04:17:00 | NOAA-21 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16fb3a00-02d3-3151-a198-fef833deb9d0 | -20.79751 | -47.22607 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 408d7648-8665-39c1-89cd-eed5ba5355ca | -20.79691 | -47.22979 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c3346c3-c2f4-3d40-a28b-fa37e32d54f8 | -20.79419 | -47.22549 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ca5d5e4-230d-3e9f-b3fe-0d5e2be1a8ca | -20.79392 | -47.24836 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 0a0cc875-516e-35f9-ba1f-10e124e43c3c | -20.79359 | -47.22921 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f39cb1b7-b510-3d13-a360-ba8ec3d018bc | -20.79331 | -47.25213 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 095c0bcb-cbd7-39af-a458-518b68bc7e6f | -20.793 | -47.2329 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bda5f9ff-0e87-3350-b9f7-913cc5584a8b | -20.7927 | -47.25588 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bc644646-16cb-3409-84d8-64cdb1ce14aa | -19.75276 | -46.65091 | 2024-10-09 04:17:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32256a4e-c8cc-3a89-ad7f-0e1efbed9f9f | -20.79 | -47.2515 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 30b586bf-1123-38ae-abca-76c47f3c2ccb | -20.78967 | -47.23235 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 346a7822-7682-3025-a795-f3b266143b19 | -20.78939 | -47.25526 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4bad3c49-cb19-3f59-ba65-8a0427c04525 | -20.78908 | -47.23602 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f225e27a-fb3a-3cf8-9b6b-7f036a65611d | -20.78849 | -47.23971 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 611a0859-8ba9-394d-a9db-cbbb44d34130 | -20.78729 | -47.24712 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 135fe9a2-4aa2-3b82-ad53-a3aa925941d8 | -20.78668 | -47.2509 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 01cd8ddc-4546-3ac3-a205-cd59b76175c3 | -20.78607 | -47.25466 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8680eaca-5148-3db7-b501-945bf45f4cc5 | -20.78456 | -47.24286 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 500febcf-db8b-3c44-9c9c-8314a6a5a058 | -20.78396 | -47.24658 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 23366876-cafc-3a6a-9c03-5eb135ff00ee | -20.78336 | -47.25033 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| de9a856a-72e8-3b47-9fb9-b25a7be5b9f4 | -20.78275 | -47.25408 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 07187ee3-89c2-3ffc-9f0a-a546e5c3a2e1 | -20.78124 | -47.24232 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 952dd920-4646-3289-ba6d-e42ac4bd0131 | -20.78064 | -47.24605 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3bde89d7-5611-3259-9616-042bea4a24c3 | -20.77943 | -47.2535 | 2024-10-09 04:17:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05691a4a-fcf2-348f-b8a3-e7ef73f2ccd8 | -20.43647 | -47.97369 | 2024-10-09 04:17:00 | NOAA-21 | IPUÃ | SÃO PAULO | Brasil | 3521309 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a104900-a7af-390f-85c6-1cfde70de916 | -20.37066 | -47.98576 | 2024-10-09 04:17:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README89.md)
