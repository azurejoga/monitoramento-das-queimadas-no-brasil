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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b365e0e-d422-3633-b27c-24d9b2d5126d | -22.37908 | -49.25971 | 2024-10-03 03:38:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3bf90a47-e665-3f49-accc-e096d9be6d27 | -22.37504 | -43.52345 | 2024-10-03 03:38:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 30f6282e-ed58-3581-ad7e-c654302dbd2e | -22.3679 | -43.40302 | 2024-10-03 03:38:00 | NOAA-20 | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 81ab17dd-2149-3b3f-a4fb-7f2ee6a1229c | -22.36585 | -49.28076 | 2024-10-03 03:38:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 14dea08a-271b-376a-a1dd-3402c48f754a | -22.36149 | -49.2805 | 2024-10-03 03:38:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| b5432f16-cc4b-3954-b772-d85b0ed6780d | -22.36036 | -49.28522 | 2024-10-03 03:38:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 2855e811-f906-3e45-b1a9-75e23b70ce0e | -22.35989 | -49.27922 | 2024-10-03 03:38:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 2ca79209-53fc-3fa0-9f3e-bc13fb7da3bb | -22.3588 | -49.28392 | 2024-10-03 03:38:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d319b3a1-8496-3205-ac79-714c4731d0cf | -22.31357 | -44.06733 | 2024-10-03 03:38:00 | NOAA-20 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| fe4a9e87-de86-3102-b3c0-b228b53e3c02 | -22.31259 | -44.07218 | 2024-10-03 03:38:00 | NOAA-20 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 431be1ed-8b04-32c2-beda-afefe4e68f88 | -22.30574 | -44.06101 | 2024-10-03 03:38:00 | NOAA-20 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e1bc5b7f-e5de-324c-9f43-6e993abe30dc | -22.30096 | -44.06296 | 2024-10-03 03:38:00 | NOAA-20 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9098eca1-5bf5-3218-8c5d-6a0a088b49e1 | -22.30032 | -44.06527 | 2024-10-03 03:38:00 | NOAA-20 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ca1f5432-f101-3211-9026-0fdcfbd89acb | -22.30005 | -44.06765 | 2024-10-03 03:38:00 | NOAA-20 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6fdfd734-b8dd-3818-af0f-53e3bedfbbaa | -22.29939 | -44.06984 | 2024-10-03 03:38:00 | NOAA-20 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| a1fc6885-f83e-3042-b18d-53cba701910b | -22.29916 | -44.07215 | 2024-10-03 03:38:00 | NOAA-20 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| badfd0b7-b5b4-3af8-8a16-0cf6fe5f93a1 | -22.29589 | -44.06461 | 2024-10-03 03:38:00 | NOAA-20 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a7da0485-b847-333c-84ee-f3c404e6d6b8 | -22.29564 | -44.0669 | 2024-10-03 03:38:00 | NOAA-20 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| af087d3f-3a16-3d06-ab23-9a3b688c0676 | -22.295 | -44.06899 | 2024-10-03 03:38:00 | NOAA-20 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 3548ccd9-b807-346e-b2cc-0f94ed21fddf | -22.29479 | -44.07125 | 2024-10-03 03:38:00 | NOAA-20 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1995ddb5-2e35-36ad-8296-e650658549d4 | -22.28899 | -42.48727 | 2024-10-03 03:38:00 | NOAA-20 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 03032f09-d1e0-3e30-9668-95aa1bedd1d8 | -22.28605 | -42.4811 | 2024-10-03 03:38:00 | NOAA-20 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 825c9c1e-2509-3f70-9ef6-6c82df3ad929 | -22.285 | -42.48653 | 2024-10-03 03:38:00 | NOAA-20 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| fd9078d1-a833-344d-a734-f9ca888ad47f | -22.28446 | -42.47893 | 2024-10-03 03:38:00 | NOAA-20 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e8786b2d-512b-34d4-98cc-3fdc901d505f | -22.24718 | -43.8998 | 2024-10-03 03:38:00 | NOAA-20 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5768daca-f613-3a55-aaaa-14aa0db18f96 | -22.22585 | -49.63218 | 2024-10-03 03:38:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9ebe3fbe-474d-328b-8de7-0a935c659439 | -22.22469 | -49.63707 | 2024-10-03 03:38:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e8efc251-bcd3-36ba-860b-1dee1d54403b | -22.18626 | -48.63836 | 2024-10-03 03:38:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| a5e5e1c0-a1a4-343c-ae48-e587bd6c7eba | -22.18541 | -45.04509 | 2024-10-03 03:38:00 | NOAA-20 | SÃO SEBASTIÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3164902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 94fdd42c-9996-3664-b451-4dd8b1268a41 | -22.18525 | -48.64278 | 2024-10-03 03:38:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 4cd9f5b9-481c-306c-bd32-73a0ead84d64 | -22.18507 | -48.64029 | 2024-10-03 03:38:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 042023c8-c19c-3da8-b8e3-7d67508ea9ad | -22.18426 | -48.64716 | 2024-10-03 03:38:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 2c5a17c0-5f75-30ff-8bcb-0a980af6dc43 | -22.18405 | -48.64465 | 2024-10-03 03:38:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 2cd92beb-75a2-347a-b70f-368e43dfe889 | -22.1646 | -42.5436 | 2024-10-03 03:38:00 | NOAA-20 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2dbf6219-2635-377f-8f7f-432fec863f0a | -22.15805 | -42.5345 | 2024-10-03 03:38:00 | NOAA-20 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c824a973-536b-363e-a397-96083e6e51c4 | -22.15733 | -42.53824 | 2024-10-03 03:38:00 | NOAA-20 | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 262c2f03-5d7a-31ef-96ee-12bdae55762c | -22.15662 | -42.54192 | 2024-10-03 03:38:00 | NOAA-20 | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bc36c8a5-4d28-3f05-ad8e-8224bd73bcab | -22.15656 | -42.53589 | 2024-10-03 03:38:00 | NOAA-20 | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d5f73a5d-a6bc-3765-9fb4-cacdd77fac89 | -22.1559 | -42.54562 | 2024-10-03 03:38:00 | NOAA-20 | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 25de7333-787e-3627-8d6d-078c4b960bda | -22.15586 | -42.5396 | 2024-10-03 03:38:00 | NOAA-20 | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e038ac36-35eb-3651-8f34-4861543f5047 | -22.15448 | -42.54702 | 2024-10-03 03:38:00 | NOAA-20 | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 40eece56-5e97-3ecc-a5bf-9e0835067e81 | -22.15185 | -42.54509 | 2024-10-03 03:38:00 | NOAA-20 | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 74aaf7fe-e404-34fe-8fcf-fe777f97c606 | -22.15109 | -42.549 | 2024-10-03 03:38:00 | NOAA-20 | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2a81076e-12ad-3629-bbc5-4c5183802fd3 | -22.15041 | -42.54662 | 2024-10-03 03:38:00 | NOAA-20 | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 750738ba-e712-33ee-b911-33aeb8d00898 | -22.14967 | -42.55056 | 2024-10-03 03:38:00 | NOAA-20 | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1cdffd15-b4e2-371f-bda4-f4de324e5001 | -22.11669 | -45.09464 | 2024-10-03 03:38:00 | NOAA-20 | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| aec4c646-72c9-3781-9db6-523c87970101 | -22.11617 | -44.0981 | 2024-10-03 03:38:00 | NOAA-20 | SANTA RITA DE JACUTINGA | MINAS GERAIS | Brasil | 3159308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 79f97b16-daa1-3b64-87a3-98a97ebb7623 | -22.07783 | -42.08823 | 2024-10-03 03:38:00 | NOAA-20 | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dccdab28-ef80-3031-b723-fbcda295ba03 | -22.07677 | -42.09391 | 2024-10-03 03:38:00 | NOAA-20 | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 37ea22eb-7169-37fd-9e68-3522c37dd660 | -22.07561 | -42.10009 | 2024-10-03 03:38:00 | NOAA-20 | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 55a1540c-aaeb-3ed5-8048-a35c68f35996 | -22.07386 | -42.08783 | 2024-10-03 03:38:00 | NOAA-20 | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 779ae7ba-9ed9-3dc2-82c9-01dbc55dc1b4 | -22.07274 | -42.09378 | 2024-10-03 03:38:00 | NOAA-20 | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c35d2596-7341-3cb3-b743-e0d3c42e4da5 | -22.05775 | -42.9708 | 2024-10-03 03:38:00 | NOAA-20 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8e25be6c-8042-36f6-907d-039461b33dc4 | -22.00651 | -44.50074 | 2024-10-03 03:38:00 | NOAA-20 | CARVALHOS | MINAS GERAIS | Brasil | 3114808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f2057cad-e526-32e8-a75c-48a747742e2a | -22.00547 | -44.50577 | 2024-10-03 03:38:00 | NOAA-20 | CARVALHOS | MINAS GERAIS | Brasil | 3114808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| eff63bd4-39ba-3484-b07a-42092a23856e | -21.93082 | -41.55597 | 2024-10-03 03:38:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7ac1c9cf-c219-3bcc-8d79-4e3ec19820eb | -21.82193 | -44.40331 | 2024-10-03 03:38:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 8e1f84c6-4b6c-3972-ae9e-75721f1e715d | -21.79538 | -42.49405 | 2024-10-03 03:38:00 | NOAA-20 | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bb2e5316-1359-3547-a5f0-a1accf4c6dc7 | -21.79468 | -42.49774 | 2024-10-03 03:38:00 | NOAA-20 | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e75b1f17-542d-3389-9eef-21ad73599e10 | -21.79275 | -42.48595 | 2024-10-03 03:38:00 | NOAA-20 | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ccaa1d69-c838-3911-8091-8f27ad158b43 | -21.79207 | -42.48952 | 2024-10-03 03:38:00 | NOAA-20 | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ed0d49a3-f850-32d1-873c-5cc10b02be2a | -21.79139 | -42.49311 | 2024-10-03 03:38:00 | NOAA-20 | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 29c4e76c-2b93-39e3-a25b-b543140749cf | -21.7907 | -42.49678 | 2024-10-03 03:38:00 | NOAA-20 | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d16074d0-534a-3d46-b7a5-a5de66cdd9db | -21.78877 | -42.48495 | 2024-10-03 03:38:00 | NOAA-20 | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8f6d4e68-0e85-3dc9-93c4-e6ea635f375c | -21.67168 | -43.95243 | 2024-10-03 03:38:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 57f44b8e-2a25-3546-824a-51f2cd6e3bdf | -21.67072 | -43.9572 | 2024-10-03 03:38:00 | NOAA-20 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e67a0df2-f18f-3ee3-a172-5027053d99bc | -21.66111 | -43.52814 | 2024-10-03 03:38:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ab218a65-99f6-335e-9188-11287dd16b73 | -21.65682 | -43.5273 | 2024-10-03 03:38:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ee8e5e59-2d2a-3e31-8186-d78e8fa7c9a5 | -21.64868 | -44.00337 | 2024-10-03 03:38:00 | NOAA-20 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 103c884a-b7b4-3d38-a4b9-2755bbe35721 | -21.64775 | -44.00806 | 2024-10-03 03:38:00 | NOAA-20 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e1915826-e19f-3ece-8878-495c7cd69490 | -21.63089 | -46.42644 | 2024-10-03 03:38:00 | NOAA-20 | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c9bc04d9-5da2-33b9-979b-25c34521c769 | -21.6308 | -42.80818 | 2024-10-03 03:38:00 | NOAA-20 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c6e61fae-a5e2-359e-8ad1-717683bfa733 | -21.63018 | -46.42972 | 2024-10-03 03:38:00 | NOAA-20 | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 63a5b9ed-53fd-3829-8258-1e2f07b31b13 | -21.63 | -42.81234 | 2024-10-03 03:38:00 | NOAA-20 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 84682897-747f-346a-ade4-624436c6e0d3 | -21.6292 | -42.81656 | 2024-10-03 03:38:00 | NOAA-20 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 956beca0-a828-38f4-9f39-2baf93183f69 | -21.62593 | -43.46768 | 2024-10-03 03:38:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6abdb096-c009-3da3-bfb2-a01f8e829628 | -21.61665 | -42.7931 | 2024-10-03 03:38:00 | NOAA-20 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a4dc029b-3b0d-3a4f-a935-7ab6e3cf95f8 | -21.61513 | -42.80104 | 2024-10-03 03:38:00 | NOAA-20 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b167ba51-ec9a-3c13-b5af-497543aea166 | -21.61322 | -42.7888 | 2024-10-03 03:38:00 | NOAA-20 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6a1a9a92-f75b-36cf-8237-49119371326b | -21.61172 | -42.79661 | 2024-10-03 03:38:00 | NOAA-20 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ffc890aa-73e6-36e5-9746-b4b314c8205d | -21.60907 | -42.78825 | 2024-10-03 03:38:00 | NOAA-20 | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 823c5093-e583-3ef9-bfac-5273a361992b | -21.57056 | -41.22643 | 2024-10-03 03:38:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b4229fbe-bb76-3c88-a1d1-b7ae124c9559 | -21.56967 | -41.23129 | 2024-10-03 03:38:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b806dc5e-13d7-3e9b-9d63-26db33351148 | -21.56361 | -43.96947 | 2024-10-03 03:38:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a42e5031-b133-3975-b69d-d2c38b411be2 | -21.56266 | -43.97412 | 2024-10-03 03:38:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 2631b134-3c0f-3133-9ff2-469c8c0d536f | -21.56041 | -41.2394 | 2024-10-03 03:38:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 30efeaad-e31e-3ca1-91d0-4d7607978109 | -21.55952 | -41.24422 | 2024-10-03 03:38:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| e2fc7dbf-ff10-3d4d-a8a6-f654f8a204a4 | -21.55844 | -41.22888 | 2024-10-03 03:38:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f3d78ba6-9b7d-33ba-a8c3-501e177810d0 | -21.55756 | -41.23373 | 2024-10-03 03:38:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| de16493c-8329-3a74-8d8b-f4583fe23785 | -21.52296 | -42.04976 | 2024-10-03 03:38:00 | NOAA-20 | CAMBUCI | RIO DE JANEIRO | Brasil | 3300902 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 74fd15f6-83c2-3b57-8f4f-b56952b9518e | -21.51787 | -42.05513 | 2024-10-03 03:38:00 | NOAA-20 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b0b01b4b-b393-384c-acaa-8b6e4c63f1fc | -21.51667 | -42.06153 | 2024-10-03 03:38:00 | NOAA-20 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 94c7ba03-26f7-3947-be5c-23c7ad42f1de | -21.51384 | -42.0549 | 2024-10-03 03:38:00 | NOAA-20 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7049b522-5bc9-39e5-83c9-fea579439265 | -21.4904 | -42.13548 | 2024-10-03 03:38:00 | NOAA-20 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1a3fb6c9-1a70-3561-99ce-b686ffb610ee | -21.48936 | -42.14096 | 2024-10-03 03:38:00 | NOAA-20 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6c6f42a2-cac9-3882-8ed7-de81df2954a4 | -21.48647 | -42.13456 | 2024-10-03 03:38:00 | NOAA-20 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 16e08046-448d-3685-964a-27f6e36470c3 | -21.48542 | -42.14009 | 2024-10-03 03:38:00 | NOAA-20 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 70167326-d80b-3f6d-835b-67625e348be2 | -21.45361 | -44.57851 | 2024-10-03 03:38:00 | NOAA-20 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| f73fc7fd-4ef4-3c0f-b205-3a171a627b88 | -21.45242 | -44.58433 | 2024-10-03 03:38:00 | NOAA-20 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 41edd824-756e-3d8b-90be-9027364d674e | -21.44888 | -44.57824 | 2024-10-03 03:38:00 | NOAA-20 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |


[Clique aqui para ver as próximas entradas](README69.md)
