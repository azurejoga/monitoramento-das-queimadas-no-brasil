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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63e1eeb1-6e0c-3d21-8d1b-b233d772b030 | -9.4769 | -40.3365 | 2026-05-14 04:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 112.9 |
| ff94b246-59dc-3f93-ab48-ef6a81bb18b0 | -9.46158 | -40.34304 | 2026-05-14 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 0c2ee994-4979-3a58-9df7-578c8b09b324 | -5.44647 | -36.79374 | 2026-05-14 04:02:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4bb07d80-ef06-3c26-ba7f-951c7230fce8 | -9.29462 | -45.47542 | 2026-05-14 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f12db080-09cf-3c34-9bbf-acda8d7baed5 | -8.10536 | -44.18172 | 2026-05-14 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83c0a3c4-7ad1-31bb-b6a1-02280487a76f | -9.29801 | -45.47963 | 2026-05-14 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3c4a4f5-3713-3dcf-a9b6-122d84699fa4 | -8.54149 | -45.98729 | 2026-05-14 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57e11bb7-72a7-3c9a-a17f-df5c49b6780f | -9.46489 | -40.34357 | 2026-05-14 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| e374590e-8a90-3a49-a4f9-a6074f017119 | -8.54636 | -45.98403 | 2026-05-14 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46f32614-aeea-3d40-80c6-f2f9e399719f | -9.302 | -45.48034 | 2026-05-14 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d5fe23c-5bab-3e64-8256-3164ca5e211e | -9.816 | -48.52168 | 2026-05-14 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79d57478-5552-38aa-872d-54a60be7dba6 | -9.46267 | -40.33609 | 2026-05-14 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 0e517f48-5ef6-39b6-a817-06dab41bbfed | -9.46543 | -40.34009 | 2026-05-14 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.0 |
| 78880ae5-5deb-3a8b-9fde-74ffe8915335 | -10.55359 | -42.44714 | 2026-05-14 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 816097b1-fc4e-3042-98dc-a16b5248a0c4 | -9.47258 | -40.33765 | 2026-05-14 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ac3aa564-9927-37ff-a983-15295e422072 | -10.55757 | -42.44402 | 2026-05-14 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 39a8e03e-f9e9-3825-bf07-1713ccce233b | -8.1016 | -44.18109 | 2026-05-14 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa998d0b-03ce-33c2-a828-eaffdc301b02 | -9.45936 | -40.33557 | 2026-05-14 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| d4fc3e33-63e0-302f-b212-870e49603cb0 | -9.46212 | -40.33957 | 2026-05-14 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 690c6654-9489-36e8-bd96-5cc6d07a410a | -10.11999 | -47.94094 | 2026-05-14 04:02:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 724b09ba-bcc8-31bb-99a3-b6458c926230 | -9.46321 | -40.33261 | 2026-05-14 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 4f2ab3a6-71f5-3c06-ad07-8ea900290ba4 | -9.46873 | -40.34061 | 2026-05-14 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.0 |
| 7be80d01-7fae-36f8-af9a-8adbceac8ad5 | -8.53799 | -45.98264 | 2026-05-14 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17e69e21-c90d-350f-95c2-7e677667ce9a | -7.13478 | -44.05859 | 2026-05-14 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1cbe71a-cc55-3368-adcd-399707522730 | -8.11288 | -44.18297 | 2026-05-14 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a7431ee-5c72-3c7f-87e3-85b1d48ceefa | -8.54286 | -45.9794 | 2026-05-14 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| decbb47f-fe89-3ee6-9489-b99a401a80d7 | -9.45606 | -40.33505 | 2026-05-14 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1bb741f9-eaf6-3591-b52d-5df32147d736 | -10.55698 | -42.44769 | 2026-05-14 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d76d834a-556e-3e7b-95d3-fe002228806b | -9.5629 | -44.57997 | 2026-05-14 04:02:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4fd7a84c-3c03-381b-a283-e8a570f8f5d0 | -9.39447 | -48.43538 | 2026-05-14 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd992fba-8dd0-3974-9c74-a074ae367a24 | -8.11664 | -44.1836 | 2026-05-14 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9539ef27-3c76-3871-a77b-ec9cf334450e | -9.46651 | -40.33313 | 2026-05-14 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 1e1ab7c8-d382-3871-b17e-5db3f7a2f1c1 | -10.12187 | -47.93896 | 2026-05-14 04:02:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d3f7f57-65d6-3c69-ad03-3535149c6c5c | -5.44707 | -36.78976 | 2026-05-14 04:02:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1db30a27-9bb0-30fd-a1ae-e875c02332fe | -9.3054 | -45.48455 | 2026-05-14 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf102726-929c-3561-a17c-55f382991902 | -9.46705 | -40.32965 | 2026-05-14 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 9e520b1f-677f-3e5b-9995-c00d6e0e455e | -10.12088 | -47.93603 | 2026-05-14 04:02:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ef2dce4-eb00-3b9b-99b6-c0ad254ed6b0 | -8.54568 | -45.98798 | 2026-05-14 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae828aaa-1a49-3387-be42-f9e1963d6690 | -9.46981 | -40.33366 | 2026-05-14 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 192afdbf-fb8e-39fa-a448-1d5e9e745ade | -9.46927 | -40.33714 | 2026-05-14 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.0 |
| 01998529-a0ac-3e24-aadb-d180ada8a44f | -8.10912 | -44.18234 | 2026-05-14 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f1bf6a7-239b-3db5-a464-905f50be449d | -10.5502 | -42.44658 | 2026-05-14 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6023bea6-eed0-3b7d-9b17-dc9662b75a98 | -11.42031 | -47.09143 | 2026-05-14 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5a1d4cf-3b1d-3a16-85c0-bc843ae32fb4 | -12.04951 | -45.28441 | 2026-05-14 04:04:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e78abe76-5a9a-35ec-8bde-6691eafa0f10 | -11.4246 | -47.09217 | 2026-05-14 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db023af1-1db3-3693-ad2b-033510f86cb7 | -14.30487 | -49.24986 | 2026-05-14 04:04:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f0de69e-f37a-3f6a-b27a-06d4443f7574 | -11.79935 | -43.62119 | 2026-05-14 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c5f066f-44d5-3a95-846d-65e7dcba9e05 | -12.05411 | -45.28037 | 2026-05-14 04:04:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f547ddb-1b64-30a7-b60c-37efba1950fd | -11.74132 | -54.24249 | 2026-05-14 04:04:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2cda57e-f1b5-37a9-a191-547cd58431f7 | -18.56086 | -39.86727 | 2026-05-14 04:04:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a62c5b3b-7692-3101-bf57-baa60b74eefd | -11.92696 | -43.92538 | 2026-05-14 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ce2399a-51f8-3fcd-8026-640d6c53458f | -10.66733 | -49.71412 | 2026-05-14 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08f0c56d-98fe-35ad-b11a-ae12ad95ae2d | -12.8557 | -43.75765 | 2026-05-14 04:04:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c64baffc-c7fd-34be-bf11-91a6ddc4a813 | -12.74954 | -45.94983 | 2026-05-14 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f394c52-ac35-3dfe-91ee-82d893688e6c | -14.11988 | -45.28787 | 2026-05-14 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd10eb6c-80bd-3fe1-be62-b088189a9f56 | -15.05727 | -42.95409 | 2026-05-14 04:04:00 | NOAA-21 | MAMONAS | MINAS GERAIS | Brasil | 3139250 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdcc237a-0999-3ff3-973f-be6b067795f3 | -14.11097 | -45.29551 | 2026-05-14 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58874c81-74dc-3076-8171-b7ea4b0b911b | -14.15786 | -45.35485 | 2026-05-14 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 275d526a-5955-3261-8dc8-51908d3e0e34 | -11.9706 | -46.78867 | 2026-05-14 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0b5f1de8-c8ab-35a7-8899-5c3b987e4507 | -11.76402 | -47.06774 | 2026-05-14 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c64bb872-d11b-3563-90ed-6a4517a740c7 | -14.0001 | -42.5419 | 2026-05-14 04:04:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 3fffe456-51de-3863-832c-8588428c5d9d | -11.97006 | -43.84118 | 2026-05-14 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c34ac3ff-7d9c-3373-b885-5a01453ff3c4 | -15.05393 | -42.95354 | 2026-05-14 04:04:00 | NOAA-21 | MAMONAS | MINAS GERAIS | Brasil | 3139250 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3eca801-ff33-3f47-9d80-6f386e0dfc44 | -12.61641 | -44.51503 | 2026-05-14 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74f00df1-2372-339b-9399-c45d92f2bb0e | -11.63276 | -47.88493 | 2026-05-14 04:04:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97555ad3-899b-3b42-8182-199d2ff8b646 | -11.31215 | -54.03242 | 2026-05-14 04:04:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e979fbd0-4fa6-3943-9afa-e59345e79d26 | -12.45841 | -54.45054 | 2026-05-14 04:04:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9c873b3c-3652-3789-b3a4-539ed083bf05 | -17.3716 | -42.69727 | 2026-05-14 04:04:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 00eeea02-2852-3f5c-9de0-49c804a9796d | -15.90059 | -43.214 | 2026-05-14 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e2ed3071-64f2-3a2e-b763-543a7be43f0d | -11.97425 | -43.83774 | 2026-05-14 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c7c42d41-15d8-36dd-9af2-c23d0e0b9398 | -12.11512 | -43.64443 | 2026-05-14 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 05c03576-8782-345d-b434-bfdcae1fcaa6 | -11.6381 | -47.8811 | 2026-05-14 04:04:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25b2e1a0-e16b-3f4c-b3bf-c5cfea3a05bf | -12.03121 | -47.80581 | 2026-05-14 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7faf6e4a-b0fa-3782-b408-5469bad8b419 | -13.95889 | -46.03255 | 2026-05-14 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6abc134b-9e5a-39a0-af98-03ecd50dbe79 | -11.93683 | -54.09943 | 2026-05-14 04:04:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1a882ae-bf4b-312c-bfb2-07a7c3a3bae0 | -11.74516 | -54.23742 | 2026-05-14 04:04:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c634bfd9-11b8-3078-a9c9-8701ef0e15c1 | -12.46126 | -54.44935 | 2026-05-14 04:04:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9907f656-496e-3ac5-9c25-0eb43b552b32 | -17.36111 | -42.6992 | 2026-05-14 04:04:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0c323859-d1e9-3e8f-b4cf-4ce32158a9aa | -12.62001 | -44.51567 | 2026-05-14 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b584c8b6-a3a5-3329-81c3-420dca7b3abe | -17.36054 | -42.70279 | 2026-05-14 04:04:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab81a869-f4f1-3530-8ccb-a7f801fa0ca1 | -11.74255 | -54.23636 | 2026-05-14 04:04:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ce3527b-7996-3ca4-a8f0-f26f32f52884 | -11.97358 | -43.84177 | 2026-05-14 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3d9e1814-d2e2-3ac3-82ee-324e10f6e21e | -11.93592 | -43.36619 | 2026-05-14 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6149f701-e192-3e05-b1c4-8355ca662288 | -15.05669 | -42.95772 | 2026-05-14 04:04:00 | NOAA-21 | MAMONAS | MINAS GERAIS | Brasil | 3139250 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79e09b97-16f9-3358-8067-c04d13841dfa | -11.73607 | -44.52079 | 2026-05-14 04:04:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bffc0449-ee5d-3142-a379-fbdf3fa20c0f | -12.61569 | -44.51928 | 2026-05-14 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b56e2ad6-6b1f-3b1d-91d5-3a130231a1a5 | -14.12356 | -45.28853 | 2026-05-14 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff9e7872-9a6e-332d-aae9-7e754f20768c | -11.9353 | -43.37001 | 2026-05-14 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cb0350d6-5a17-3fe3-9741-fbf37117122b | -11.73533 | -44.52514 | 2026-05-14 04:04:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44987f16-69d2-34ff-a2ec-bd85a1cba89b | -11.92627 | -43.92949 | 2026-05-14 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c8f11be-4d73-3482-ad0e-12e827a5b650 | -10.39746 | -46.64738 | 2026-05-14 04:04:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cbb521ff-e95b-3438-b1c8-dde6aca6f76b | -11.78233 | -43.65894 | 2026-05-14 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9e56ebd-98e5-3556-a623-d09628c41f89 | -12.0533 | -45.28506 | 2026-05-14 04:04:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3493bc18-7f5e-310e-ad9b-8fbfa91bb8a2 | -11.76047 | -47.06296 | 2026-05-14 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9c06ba7-95e0-3042-85d6-ffdd7124fb01 | -14.11911 | -45.29234 | 2026-05-14 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4cb61be1-105b-3ba4-a912-d5625d7e7a38 | -11.76473 | -47.0637 | 2026-05-14 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c195e2b3-48a2-3fb5-bc22-00b6cebf2a3f | -15.0847 | -43.88358 | 2026-05-14 04:04:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6831201d-fc75-3f4e-a92b-8ce2fb7f8e90 | -11.96644 | -46.7879 | 2026-05-14 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69b56a4e-2d56-3274-ba71-996f7669272d | -12.64833 | -47.08831 | 2026-05-14 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80b6e8ce-45a6-3405-b79d-3f7bad8d705e | -14.62819 | -48.01845 | 2026-05-14 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README3.md)
