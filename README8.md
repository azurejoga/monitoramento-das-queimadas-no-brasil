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
| affaaec1-8c52-3305-a3ca-77ce1f5cd71d | -8.5888 | -47.43732 | 2025-07-15 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe6b6cdd-7265-3588-bf3a-23cdd5d0e2a8 | -9.97679 | -48.08596 | 2025-07-15 03:45:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8e91c03c-4757-3a51-ba92-b877358ffe43 | -11.56267 | -47.31672 | 2025-07-15 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc782cdc-b129-3797-a6b2-2ff8babbf6e9 | -11.46167 | -45.10043 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 30.8 |
| a4c19fe9-6e84-3dc4-b187-11f675182393 | -10.56085 | -49.13796 | 2025-07-15 03:45:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7f73026b-6ce5-38f1-a1a3-20bfa37db7c5 | -11.45157 | -45.09841 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 12303658-ba8f-3b81-80c8-90460593f28b | -9.59941 | -40.61509 | 2025-07-15 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cf336a31-a31c-3cc4-b55c-3cc87837701a | -7.20556 | -45.33244 | 2025-07-15 03:45:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 343f10d1-5c66-3a01-8512-fead211d2163 | -12.08045 | -43.47696 | 2025-07-15 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b990257-781e-34b8-9bdb-93f686971359 | -11.45662 | -45.0994 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 21886706-3113-376d-b958-a5d2fb3d2e4f | -11.45827 | -45.09054 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 13413636-8d69-3017-88b9-5c8a02be41fa | -8.25958 | -46.36272 | 2025-07-15 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 365f5534-d712-32c3-b1f8-3e63444bc6e0 | -11.93842 | -45.76596 | 2025-07-15 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e92d6635-6ff4-34a6-a5e4-0f716837e1b5 | -11.43518 | -45.12989 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce4ed707-b21d-3809-bf78-af0025a43ab3 | -8.59588 | -47.43378 | 2025-07-15 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7f69dfc-d5df-328b-a760-a8eb3ac54c05 | -10.89414 | -49.20919 | 2025-07-15 03:45:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 9c90599a-8425-3a6d-935e-d4bafbc02087 | -7.9296 | -42.89193 | 2025-07-15 03:45:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2f40faa6-146d-3b56-b7ba-bdebd32690bb | -10.28507 | -47.61554 | 2025-07-15 03:45:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1916c136-4a6d-3847-8fb6-e7dc3425420a | -13.13403 | -47.27172 | 2025-07-15 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d797cad-6a53-3d38-8f4a-d0de06365810 | -8.64819 | -47.75514 | 2025-07-15 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0db72e26-8690-335e-88f6-110079b7977e | -14.58353 | -48.116 | 2025-07-15 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 089b2cd7-fc88-349a-bd32-190b5f073c12 | -15.22572 | -46.97063 | 2025-07-15 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c6b3768-b227-34fc-a034-409cbc670a7e | -20.14739 | -41.67302 | 2025-07-15 03:47:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 9c9eaabd-8f7c-3454-b0d3-7d4b8dbe9bfd | -22.57761 | -44.07991 | 2025-07-15 03:47:00 | NOAA-21 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5849f61d-45bc-33c1-9934-d920e986aee2 | -14.58449 | -48.11397 | 2025-07-15 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5432d73-42b9-3c6f-b2cf-15c68dff70dd | -22.08316 | -43.17774 | 2025-07-15 03:47:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3f3f28f9-9ace-33a4-8437-24cbcd1e8e4a | -20.59476 | -45.10921 | 2025-07-15 03:47:00 | NOAA-21 | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 14d619ad-de12-3180-93e6-9d06f1f2aebd | -20.7615 | -46.02019 | 2025-07-15 03:47:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2697ef2f-96b2-32c1-bb2c-f7a7e5e21b21 | -18.73767 | -39.92219 | 2025-07-15 03:47:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| db95f2b7-fd05-3a68-98f7-f344df7b98b3 | -19.65758 | -46.1879 | 2025-07-15 03:47:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c655df9c-e419-382e-882e-0cf9bae32ad1 | -19.16147 | -49.13967 | 2025-07-15 03:47:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1bf88a7f-48e8-3d09-b42c-e39180d3ebfa | -20.59906 | -45.11006 | 2025-07-15 03:47:00 | NOAA-21 | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 53dc9c3a-cde4-358a-9801-06c304a8d214 | -15.22496 | -46.97445 | 2025-07-15 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5992705-4343-3f60-8f96-6f1ebdb31471 | -19.53684 | -44.07705 | 2025-07-15 03:47:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d67ebeb-891c-3ad7-8993-c913496d25c7 | -21.89369 | -41.42189 | 2025-07-15 03:47:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| edb15f9e-8340-3458-8395-78fb4dff6f7e | -22.67554 | -42.85695 | 2025-07-15 03:47:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| d8e3bceb-2ed2-352c-9c15-81b6e6c79097 | -15.23189 | -46.96754 | 2025-07-15 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64bc0b5b-e6d8-382e-b9ce-4f9c13e69332 | -15.24092 | -46.97795 | 2025-07-15 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d1cb111-f527-34f8-8ecc-ca47bc3d97b6 | -14.57752 | -48.11582 | 2025-07-15 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f76972d4-f93e-310a-996e-4540ab849105 | -22.58248 | -44.03193 | 2025-07-15 03:47:00 | NOAA-21 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dae11d7b-7e94-39cd-8239-ba25f30562eb | -15.24004 | -46.98239 | 2025-07-15 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2b96e24-89f7-3f9d-867b-0c3d7b2c538d | -14.58467 | -48.11061 | 2025-07-15 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 07a4daa1-3419-3326-9265-ca47f9371298 | -20.7649 | -46.76873 | 2025-07-15 03:47:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 29102d4a-69c8-31cd-875d-630acffc1e44 | -15.23578 | -46.97591 | 2025-07-15 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b88ee4c7-caca-3ffe-868a-e372ebcceb8f | -20.37504 | -46.56281 | 2025-07-15 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79243bb4-8aab-34f0-96bc-34aaf6d26681 | -20.39464 | -46.53926 | 2025-07-15 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95e32018-8af2-3d6a-b18e-bdd719ee3502 | -14.58929 | -48.11739 | 2025-07-15 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c78bfd8d-bfcb-34e8-97d5-796477262399 | -18.82309 | -45.73858 | 2025-07-15 03:47:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89f6f598-3aff-395f-b211-135a45005fbd | -25.18903 | -49.3279 | 2025-07-15 03:47:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6b2bc820-6d42-3574-ba46-79a3903ac2d4 | -22.85666 | -42.98089 | 2025-07-15 03:47:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3c591b52-07bb-3d46-9613-0f6a61399fe8 | -14.57841 | -48.11417 | 2025-07-15 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b620e74-8083-37bd-9218-5d4dbad7b2cb | -20.14186 | -50.72027 | 2025-07-15 03:47:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a3e903f4-ccac-3e15-addb-c8baacdc2c78 | -20.76248 | -46.01526 | 2025-07-15 03:47:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3991009b-180f-3eb5-ae7b-892be8026fcd | -15.22417 | -46.9784 | 2025-07-15 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3525a432-c877-3170-9eef-d4b259a60088 | -15.74938 | -49.64502 | 2025-07-15 03:47:00 | NOAA-21 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5de2483b-b5bf-3ca1-b114-67c8fda382d8 | -15.22641 | -46.96716 | 2025-07-15 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4bafbc3d-55be-3773-86e5-e0ee6dcb9b9b | -15.23389 | -46.98537 | 2025-07-15 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d0ce596-4bc8-31fb-801b-eed6918ce7e2 | -15.75058 | -49.63947 | 2025-07-15 03:47:00 | NOAA-21 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e25e6a83-1923-30e3-9008-dd4460f19adb | -15.22709 | -46.96381 | 2025-07-15 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 366f6d3a-11be-30a5-8649-3af293df87b6 | -18.8185 | -45.73751 | 2025-07-15 03:47:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8eaf5a50-8d6b-3589-81bb-64879e771ddf | -17.14177 | -45.93814 | 2025-07-15 03:47:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a944fba3-574f-34ee-be89-b38f39e0b8d5 | -15.22781 | -46.96017 | 2025-07-15 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf1dbb94-dafc-38cd-94ec-6c4992b91038 | -23.46606 | -46.73532 | 2025-07-15 03:49:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b74acdbb-cac1-33f2-bc8a-85efe671b106 | -23.51444 | -47.22201 | 2025-07-15 03:49:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4e96f5b9-7361-39c7-ad3a-f3a78cc80b0b | -23.5134 | -47.21833 | 2025-07-15 03:49:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 09a47f48-d3d4-3014-a2b4-2398f06ca5ac | -21.77229 | -52.76637 | 2025-07-15 03:49:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 178a12e1-2102-37f8-9d57-39c0c6566189 | -23.12803 | -49.99953 | 2025-07-15 03:49:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| f71e51d5-8eeb-3a47-b8bd-6167a126c7a3 | -23.33565 | -46.13923 | 2025-07-15 03:49:00 | NOAA-21 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| b1c5e9b8-3f6b-3e66-babe-e1ae58db8060 | -23.67924 | -47.3434 | 2025-07-15 03:49:00 | NOAA-21 | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7657ab3f-2c26-3592-b72b-682a4b2f0e46 | -21.77392 | -52.75972 | 2025-07-15 03:49:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 728a9b33-300b-3339-8844-4e6c92095133 | -23.5035 | -47.33391 | 2025-07-15 03:49:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f8d3b51a-89db-36c4-b614-4c1fadadf29f | -21.77808 | -52.75881 | 2025-07-15 03:49:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03dc49e5-6dab-32d4-8f6f-5a150220cc0c | -22.40062 | -49.79946 | 2025-07-15 03:49:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 9cf74984-2e9b-33ea-8606-a796e414f864 | -23.12772 | -49.9968 | 2025-07-15 03:49:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| f6eff079-54d6-32b7-9f4a-09184452fb8b | -23.40703 | -46.5561 | 2025-07-15 03:49:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5d405410-c09b-366a-a532-62f9829a64c0 | -23.33932 | -46.77432 | 2025-07-15 03:49:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a9565d32-7f89-3df5-a1db-6f857ca8e331 | -22.39414 | -49.8023 | 2025-07-15 03:49:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a21e8323-619a-326c-8d5a-649abcc23871 | -23.12891 | -49.9956 | 2025-07-15 03:49:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 1ea31c0e-5da3-3c55-bb9e-52f685f588d8 | -22.39971 | -49.80343 | 2025-07-15 03:49:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 22f77924-218e-389f-9a3e-235a212a2c27 | -22.40156 | -49.80029 | 2025-07-15 03:49:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 075c1178-ccce-38d1-a060-7283880b0191 | -22.39603 | -49.79903 | 2025-07-15 03:49:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 62fc6f1a-b242-3f49-becb-5342b1d5c5e8 | -22.39514 | -49.80303 | 2025-07-15 03:49:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7471a1eb-abba-3da5-bde2-92fb71259b04 | -21.76735 | -52.75797 | 2025-07-15 03:49:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cb8e60a8-ad0b-3bec-a403-9a19825fd51e | -22.40067 | -49.8043 | 2025-07-15 03:49:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 18f2e1d6-61d2-3346-bb1c-a1969f9c3075 | -11.4584 | -45.1126 | 2025-07-15 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 1458a01a-35d7-3bfd-a0de-5516e84fe4ff | -11.4389 | -45.1385 | 2025-07-15 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 9ece5447-7a93-35da-b35d-ced2a96a3811 | -10.5586 | -49.1337 | 2025-07-15 03:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 59b094d3-d0b3-31d6-83e3-0c907d7c1107 | -11.4588 | -45.0895 | 2025-07-15 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 199.2 |
| f4e47ce7-860c-3dee-9909-62d6a47eaa62 | -11.4592 | -45.0664 | 2025-07-15 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| e3d6cfda-da94-3827-a690-134934fb087f | -11.4393 | -45.1154 | 2025-07-15 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 19fc04e3-b086-3982-a22b-c5787e44be86 | -11.478 | -45.0868 | 2025-07-15 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 4a19f615-a589-36b8-bb1d-142b75390b51 | -10.5776 | -49.1316 | 2025-07-15 03:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| fa44a6c4-cc69-3332-bcdc-00869b23cb17 | -11.4397 | -45.0923 | 2025-07-15 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 56b21d94-3e11-3b10-999e-7085fca76926 | -11.4588 | -45.0895 | 2025-07-15 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 227.2 |
| 45c4adc9-b066-3e94-83f9-2b9bde17b69b | -10.5776 | -49.1316 | 2025-07-15 04:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 168b87fd-f0d8-3168-aa23-bd0920960312 | -11.4393 | -45.1154 | 2025-07-15 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| fdfa2279-a88d-3dc7-8601-fa456d9b1430 | -10.5586 | -49.1337 | 2025-07-15 04:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| fab856f4-8e23-33f9-bd72-42d9c75a2717 | -11.4397 | -45.0923 | 2025-07-15 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 1e431453-da41-3427-916e-eb52b293205d | -11.478 | -45.0868 | 2025-07-15 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 353303ba-d720-3949-ac7c-ddb83d1148b6 | -11.4584 | -45.1126 | 2025-07-15 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |


[Clique aqui para ver as próximas entradas](README9.md)
