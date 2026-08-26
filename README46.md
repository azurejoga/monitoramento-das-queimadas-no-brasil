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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4aecbe3-a6b5-300b-89a2-b3da16a3b234 | -13.62042 | -48.9945 | 2026-08-26 04:53:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 146e5611-9aee-3aa9-bb2e-6e1aa9bfb5dc | -12.15549 | -50.59641 | 2026-08-26 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 12005df1-276a-3d6a-934f-2f7769169eff | -15.57328 | -53.14771 | 2026-08-26 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 636eb439-1a93-3cf7-9b29-2ba1367292d7 | -11.26045 | -47.06402 | 2026-08-26 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab0c2e08-f2fb-3817-a89c-0c3f0a516d15 | -9.65585 | -55.09928 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b503d5e-e03e-3c05-a8cc-392e48813954 | -13.9855 | -54.01619 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ced587a3-4ef6-3c2a-bba4-33253e1106bd | -12.76497 | -46.46084 | 2026-08-26 04:53:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 674b9106-d1ec-3f8a-8fa9-f43dce814004 | -11.01651 | -45.07081 | 2026-08-26 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7beda317-0a42-3d50-a76e-5162de3e51bf | -9.67292 | -55.07941 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a4e0cea7-0eb5-3c06-9fe8-e97ba59ab0c4 | -9.65716 | -55.06936 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a26d7ad9-a4a9-3ec4-b54d-7c3f5196cc7e | -10.98566 | -60.79232 | 2026-08-26 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c61f31af-e1c1-34cf-9e91-7946bdebad6e | -12.72928 | -48.38328 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9afc24f-a151-3e1b-a2a8-53552968b505 | -14.39522 | -52.89808 | 2026-08-26 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76bca5a8-300f-38b6-8f74-58c3a79f11fa | -12.66811 | -48.42031 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d511c7a-05c2-3eb0-944e-e65e44bbe1dd | -12.02663 | -46.02156 | 2026-08-26 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e882770e-07cb-33d5-929c-53471cc76cfc | -12.15915 | -50.59696 | 2026-08-26 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae4f91dd-0d9e-37d1-b8ce-2c819e9ac20a | -13.86288 | -54.06166 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fda41e38-7ebd-307f-83a4-ea9274ce7f51 | -9.17881 | -59.58351 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c71b242-d2fc-371e-8126-117102bbc5c5 | -9.67397 | -55.09462 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62d648fb-a456-391a-be8f-f5f5efc4286c | -9.17276 | -59.39122 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b9db29c-e234-312a-8282-da8fae6f6679 | -11.42626 | -44.53246 | 2026-08-26 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 67babe49-defb-3204-ba65-a73c230d7277 | -13.98222 | -54.03751 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7691c46-4f0d-324b-a090-8e1d88d8790f | -14.41842 | -52.90555 | 2026-08-26 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8628619-9fc0-3f18-9e46-6dc4845e0921 | -12.75516 | -46.46292 | 2026-08-26 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 39d4429a-d6cb-3856-a2ea-b34b27eac32a | -11.49447 | -45.10717 | 2026-08-26 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f837bc59-344c-3261-8924-fd568bd6af55 | -9.48842 | -56.91948 | 2026-08-26 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82f6027b-d707-3a12-8240-7a6e339e2194 | -12.68383 | -48.39894 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 22592e1a-2418-3f51-92cc-e79761735378 | -15.56476 | -53.13479 | 2026-08-26 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d585fa21-ea7b-30e7-a646-43e654b32523 | -9.16603 | -58.33082 | 2026-08-26 04:53:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24465fb8-d002-3b0e-9e48-e942d27c9af0 | -11.1589 | -54.00657 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2e6a4f7-af50-3526-8743-351a56a10275 | -13.35689 | -48.23063 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9fd301fa-e339-30dc-9c67-8791a2da859a | -10.91002 | -44.73816 | 2026-08-26 04:53:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23955d4f-c525-378b-9c14-58b94d38031c | -8.82682 | -62.33401 | 2026-08-26 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0f79efa-c872-3d04-84ae-3bbccf592400 | -13.87582 | -54.08889 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65d87517-b108-3c30-ad7b-036318846872 | -10.3864 | -53.50937 | 2026-08-26 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7b73157-a7b0-369c-a644-01856d0a4167 | -10.31565 | -50.40248 | 2026-08-26 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3b6e49a-9e75-330e-b79f-404ff83d6c44 | -13.27749 | -51.45843 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c1e5b8bc-d7b3-3371-afec-7d67e287fa73 | -9.65644 | -55.09559 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75a89d22-409f-3b37-8ddb-e80810d53c04 | -9.45919 | -60.53595 | 2026-08-26 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e9230e6-3b0e-3730-99e8-c713fb62fe07 | -13.85237 | -54.04179 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a97ccc46-20b7-3b5e-be9b-508b8e9da02d | -13.36075 | -48.20134 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ed9d9a50-aba1-3a38-9b54-c777030d2d3f | -13.60979 | -49.01107 | 2026-08-26 04:53:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b9582b4-5351-32d7-8bfb-27f956310109 | -9.59718 | -61.00642 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7d0bb0bb-8f97-3e9f-9599-69662b15159c | -13.28132 | -51.46051 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 099c9f73-7779-3042-88a9-f7eb3ecac50e | -12.89736 | -59.90973 | 2026-08-26 04:53:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0ff661c-52e9-347e-ac57-30743bdcc796 | -12.64866 | -48.40549 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bc7e778-80e9-3789-a471-796e16e5175c | -14.78942 | -48.80297 | 2026-08-26 04:53:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fac52315-49b1-3fa3-8ec1-32e7f1b71ec1 | -12.76479 | -46.46403 | 2026-08-26 04:53:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3177836a-bc6b-3a47-aba9-999d84d82e80 | -12.73036 | -48.37487 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1935f4a9-3b7a-3069-8507-28aa3a326760 | -10.56088 | -50.43566 | 2026-08-26 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 748ae193-1517-371d-8045-09f0a9484d1a | -12.77148 | -44.25837 | 2026-08-26 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3d2b818-6e64-370f-a782-7e16facb0b39 | -12.6728 | -48.41729 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cb476833-f2fa-3510-a896-e0d456b84f6e | -13.24589 | -51.40475 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d29dfb10-e7e4-3be5-8001-7ce890fb0f3b | -13.22513 | -51.37211 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b081d1ae-5812-3590-ab96-b5c4c7c1f7af | -13.24887 | -51.38416 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5cca1c3a-7dba-3f54-89be-b6ad9460fa89 | -9.48477 | -56.91882 | 2026-08-26 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cafc266-18ea-32d4-a241-972be845d46b | -8.81867 | -62.3192 | 2026-08-26 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e52a0cc-5be8-3259-950d-63dd65549232 | -10.16629 | -55.31023 | 2026-08-26 04:53:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bcfa838-fd5b-30c8-b15d-9e3c5148fe0b | -13.23938 | -51.37428 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 87e0a826-d0d7-3a29-88ca-58be4bc572c8 | -13.17876 | -51.34566 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7cadd354-b078-310e-a053-ebad9977b940 | -9.17849 | -59.38377 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5edbb6e-243e-327a-9e7a-3d9a054b8744 | -12.07892 | -64.24802 | 2026-08-26 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88fb0984-5dcb-3909-a40c-699cb742badb | -12.03011 | -46.03339 | 2026-08-26 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 52a840c1-f22e-3ece-87e3-0ec83d4c4424 | -13.27068 | -51.4589 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0775b83d-41cd-3a5f-88ad-d15082ab5a36 | -10.4274 | -61.21793 | 2026-08-26 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8811eadc-dfd9-3db9-a7d7-8b485853e83c | -9.27227 | -56.90949 | 2026-08-26 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 933efb5a-9999-3d08-bf6c-0e970f3280b7 | -9.67794 | -55.09146 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8aef1ea0-ebe2-326d-89b0-ed0e39e94ac8 | -11.49089 | -45.09365 | 2026-08-26 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 203fdbfd-ea4b-3a94-96de-953cc1a85849 | -11.72091 | -47.77407 | 2026-08-26 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04b9a8f4-70c2-3832-b9b2-5edd6c143f86 | -11.18315 | -54.00328 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1765c7b5-7178-3670-85e1-e966070a213f | -12.71659 | -48.37889 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5dee4b00-c555-3fe8-93f4-1f3262f51640 | -11.16385 | -53.9966 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e3774db-91c5-3571-a8f9-3883853eeff3 | -11.11637 | -49.88101 | 2026-08-26 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7870065-82b9-345b-ba92-ed63c3da3058 | -12.95384 | -56.61327 | 2026-08-26 04:53:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41f5f259-d51a-3949-a234-6120a916b663 | -13.85674 | -53.99149 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99cfb1d7-a3f4-335c-9b5d-7e5cca901b89 | -10.76636 | -54.01505 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a38a96d0-f40f-3996-a525-31ac1958fdc7 | -10.99783 | -51.15411 | 2026-08-26 04:53:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b08a39f7-6734-3715-9187-b987d3282971 | -9.46997 | -56.89573 | 2026-08-26 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0154dfeb-35d2-3481-87d1-f6070f456953 | -14.53735 | -52.28988 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd6ba151-8b06-343a-976f-21b22c2f1156 | -11.16054 | -53.99607 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7d0bf48-ae15-3257-a48c-2f4c4674f4c0 | -8.25825 | -63.99437 | 2026-08-26 04:53:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 695bfbab-68f6-3ad6-b864-87822681a1b8 | -12.43457 | -51.17002 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72fc1d86-512b-3056-8cfd-06cc9cb691ef | -10.76688 | -53.9685 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23c42659-b76b-3c57-8d31-d390f4549977 | -8.80876 | -62.31417 | 2026-08-26 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 659d1dd9-607c-34d2-942e-790a71f38777 | -13.30471 | -51.47095 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbafd9ca-d485-3e84-a79f-20ba58d2a80d | -13.18293 | -51.34207 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b6a57d47-8712-347c-aef0-cc66e64bb470 | -13.34104 | -54.33606 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb6bbfa3-092d-3e68-a5a5-c77ea6b270ee | -10.30165 | -49.95485 | 2026-08-26 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d76cc3cb-3303-3203-a1f0-d06941bb4ea5 | -11.68646 | -54.58662 | 2026-08-26 04:53:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b57a81b0-f118-3736-beef-cc47d2febac9 | -10.06553 | -60.50061 | 2026-08-26 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7293e484-1f34-34a1-b3d5-38b7eb0c0284 | -13.23338 | -51.51585 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7392b43e-c82d-37b9-9fe0-e53bb2cb8846 | -11.25262 | -47.05378 | 2026-08-26 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23f70871-b41d-347f-b469-83ad208864c7 | -10.76913 | -54.04062 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| e111877a-f7bd-3b0b-bd67-857a5c998fa2 | -14.55526 | -52.31269 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8751344-4a3f-3b3c-be75-1686b1f73da2 | -14.83978 | -45.52841 | 2026-08-26 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 08d1a49c-4468-3149-a341-807711ca63a5 | -9.6785 | -55.09506 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e38d736-133c-358a-95de-e5238d89e19f | -11.25771 | -47.05013 | 2026-08-26 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e35888a-87b6-3035-822b-972f015961de | -13.61966 | -48.99302 | 2026-08-26 04:53:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ed59168-a117-3c55-b6d8-799ae077581e | -11.28241 | -47.07167 | 2026-08-26 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 925dae3a-9c70-3952-89cd-8aed2b8891de | -11.97175 | -47.75269 | 2026-08-26 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README47.md)
