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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c6071a8-3102-37a8-bcb9-3e2c1486c8a5 | -7.69118 | -49.4724 | 2025-10-23 04:08:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 64370677-9038-3f86-8657-546135afc9c8 | -6.80979 | -44.00719 | 2025-10-23 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 118270a2-cf8c-31c3-b5be-175325b9485a | -7.06279 | -44.099 | 2025-10-23 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13d2eb85-782c-33b9-836a-14d6b2091038 | -6.92662 | -48.26484 | 2025-10-23 04:08:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f43cf695-85a9-305e-aa8b-4671887bc8c0 | -9.97564 | -47.08855 | 2025-10-23 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3601f584-8a9b-3d60-b3d0-c29ee8b683fc | -9.97655 | -47.08339 | 2025-10-23 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b7f3899-23a1-3ab4-a78f-a4aa72ece4c2 | -9.92665 | -47.46175 | 2025-10-23 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b03d96a4-07a0-32af-a598-44b91774c61e | -5.92909 | -47.32074 | 2025-10-23 04:08:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89351ef1-a283-3379-bcb8-5e84e5f4263c | -6.84655 | -48.26117 | 2025-10-23 04:08:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6aaf0799-f505-31ab-b0f4-d755ee3c0a02 | -12.67389 | -48.62509 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c66f61b0-024c-36ca-8601-8648a9c236f2 | -11.0749 | -51.57184 | 2025-10-23 04:08:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1e517e4a-e024-31ee-9578-75874ded69bf | -6.36102 | -44.74955 | 2025-10-23 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 183e9e5b-dc97-3151-8a18-30807af7a002 | -6.81328 | -44.00773 | 2025-10-23 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d0cbb0c-4dba-3eae-9f47-461519db1329 | -7.1846 | -43.86478 | 2025-10-23 04:08:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5adf8599-22bf-31c2-bf87-07b8c1dda8be | -11.66071 | -48.46571 | 2025-10-23 04:08:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 58691d3b-e226-36ef-b645-f2feb6525241 | -12.67099 | -48.64109 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd60dff8-29d3-34f6-bde6-69e79d544493 | -7.52844 | -42.88995 | 2025-10-23 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a41dacb3-a5c9-397a-bac5-e061ed9b5327 | -11.36379 | -49.78705 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5e5df3a5-7990-39cb-87c3-a8c0d5b968e2 | -11.80299 | -45.18253 | 2025-10-23 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77e846bb-1ab1-33a0-99b2-f500873bab76 | -11.36208 | -49.79667 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 02cb6602-f793-3f35-9f93-defdf3ba10fd | -6.75076 | -44.07454 | 2025-10-23 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49bb2807-8995-3762-a710-3e29cb22cb13 | -6.78989 | -45.44628 | 2025-10-23 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9011a18c-f87f-363e-8b78-aa1d3bdb392c | -7.56549 | -47.36489 | 2025-10-23 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e900ada-ccf8-364f-8659-6392cf760f96 | -10.28722 | -36.32464 | 2025-10-23 04:08:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 35fb3893-87a9-3264-a99d-d8868ff97bf0 | -7.2178 | -40.75202 | 2025-10-23 04:08:00 | NOAA-21 | ALEGRETE DO PIAUÍ | PIAUÍ | Brasil | 2200277 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 858a2603-2f8d-3c6f-84ee-b38820971273 | -13.59699 | -43.474 | 2025-10-23 04:08:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95b85c18-b68b-3f6a-9f31-b642d887d6c3 | -7.64219 | -42.17535 | 2025-10-23 04:08:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 574c3073-6445-348b-9964-8bea5bdb6424 | -13.29941 | -47.47709 | 2025-10-23 04:08:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0dbe1dcf-47d9-3939-825a-42c8eefacc10 | -11.53676 | -52.23994 | 2025-10-23 04:08:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 329518f7-5334-38b7-85fc-56bb0510629e | -9.98337 | -47.07182 | 2025-10-23 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ded0e1b-a7ef-399f-9735-d3d5fa4f8f6b | -7.06378 | -44.11502 | 2025-10-23 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19378d78-4932-39e8-8350-8f4129568edd | -7.32828 | -45.2851 | 2025-10-23 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d82bab21-e566-3f91-9025-084ea0c266e2 | -6.67358 | -44.69097 | 2025-10-23 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d02a9793-738e-3b57-b03e-2cc6074ea47f | -9.97836 | -47.07306 | 2025-10-23 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e601afa-4c5e-39a8-a34c-b6f8e7301ce0 | -11.86037 | -46.75317 | 2025-10-23 04:08:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 301cf1dd-53d8-3264-811c-f55a2c37fd4a | -6.28912 | -47.01192 | 2025-10-23 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bf56973-dfa4-317f-9f93-d43763befb89 | -13.0145 | -48.45683 | 2025-10-23 04:08:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b20743e8-aac0-3ba5-9704-ef41e1fed814 | -11.99121 | -46.78359 | 2025-10-23 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 936bbce1-d833-336c-975c-4302c9eebae9 | -12.81165 | -48.63314 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a8d18c0-2740-31ee-b3ae-565eaa7b2fbf | -7.63174 | -42.1986 | 2025-10-23 04:08:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 13c404dc-0ace-31e2-b741-e6f4fc22eee3 | -6.32091 | -46.20298 | 2025-10-23 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30229239-3053-3077-a17b-e4ec166e0da9 | -6.24382 | -46.39913 | 2025-10-23 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 173371ba-e73f-39d2-835b-5d3d7b0a4ec6 | -6.73817 | -44.1529 | 2025-10-23 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b97b5a06-7bf8-3508-995a-1482321d1da9 | -11.05627 | -45.39349 | 2025-10-23 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2d7cc453-1081-3e95-bf2e-12f6a221989b | -6.94212 | -44.46222 | 2025-10-23 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e33bb9ee-d239-30ee-91c9-e07bc85b999f | -11.13363 | -44.65493 | 2025-10-23 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b16e333-0c0a-3766-99cd-8ebd91058e81 | -6.96532 | -46.00642 | 2025-10-23 04:08:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5f1102f-563c-3421-a76f-cf4c011caede | -10.91644 | -50.11251 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f840b639-6a37-3a10-aba5-5735760d7748 | -7.59139 | -42.88179 | 2025-10-23 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f9c3703b-a671-3b32-8b57-0255082ce9b9 | -12.88058 | -48.59331 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6c1d0dc-a97e-32e7-a10b-1745ba7763d7 | -9.92601 | -47.4654 | 2025-10-23 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe789315-a317-3afe-b813-2197ad251e86 | -9.45776 | -40.3951 | 2025-10-23 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 29756839-fc81-37c8-b6f9-2f28828bf577 | -11.99952 | -46.78023 | 2025-10-23 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ca254ce4-e52a-3271-a4d9-f302955ffd67 | -11.99278 | -46.77425 | 2025-10-23 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9409839-0425-3e6a-97c2-649caf7632fb | -7.62953 | -42.19114 | 2025-10-23 04:08:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2475da2b-9ca7-3ce3-b975-e18f5982b388 | -7.06029 | -44.11447 | 2025-10-23 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb033454-9628-33ec-8f23-a624e5a87a6c | -6.93977 | -43.57529 | 2025-10-23 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37d2e7fc-679f-3ebc-8f8d-a4a11eaeb3fa | -11.14024 | -44.93283 | 2025-10-23 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c56a7388-7a79-3ac9-9915-c27fcb68d7aa | -11.53676 | -52.23995 | 2025-10-23 04:08:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68039a03-9599-3df5-82d7-fba9c949d9f1 | -7.06628 | -44.09955 | 2025-10-23 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e57ae751-eaaf-3bb0-8bbe-2dd2538f8624 | -7.27541 | -44.22014 | 2025-10-23 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67c2743a-6da2-3580-977c-c205b979839c | -13.0434 | -47.22956 | 2025-10-23 04:08:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 531193f8-7f47-379b-8018-0eace58aca60 | -10.21007 | -46.64053 | 2025-10-23 04:08:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdfec54d-6695-3d95-9c80-3952eb579311 | -10.10348 | -47.74296 | 2025-10-23 04:08:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a24753f6-6dcb-382b-9056-1bbbbe8c0995 | -12.25642 | -49.5896 | 2025-10-23 04:08:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93e2a80c-e5ef-371c-b2c7-930c98bc1008 | -6.78759 | -45.46001 | 2025-10-23 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47170ccb-012b-3f16-a085-78a825bb9092 | -6.93917 | -43.57903 | 2025-10-23 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ab6f5a0-559f-3195-bbf6-07fd459e75b0 | -6.82504 | -44.00141 | 2025-10-23 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b4d358a-8e64-3212-a2a1-3feea06c0c60 | -6.6046 | -44.21698 | 2025-10-23 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 42601009-2752-3d1f-8c41-867a6e7d2554 | -6.29087 | -47.01172 | 2025-10-23 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9a45148a-ed31-3ec7-871c-b3e6e0873f1b | -11.64258 | -44.93971 | 2025-10-23 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c7d89c3-7067-397e-960d-8f35c2a8a79e | -11.99882 | -46.78749 | 2025-10-23 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a94d036f-90e2-306e-8810-2be4a86ade13 | -11.79152 | -47.06477 | 2025-10-23 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e297ae73-31fc-30fc-927a-2aec01c91a7c | -6.60173 | -44.21233 | 2025-10-23 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fdee4dbe-788b-3bc9-bc8b-8a5cac538110 | -7.27636 | -49.98893 | 2025-10-23 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59ec9ee2-db6e-3fcc-b476-ddcdf0ec57cb | -11.992 | -46.7789 | 2025-10-23 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9cfbca93-f21b-3adb-92ee-857a8497eefa | -6.90377 | -44.0983 | 2025-10-23 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3dcbca94-c7c5-35e5-ae62-c0af649fda44 | -11.07612 | -51.56537 | 2025-10-23 04:08:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32bca01d-b74d-32f7-84f8-6f6b5217056e | -12.25412 | -49.58993 | 2025-10-23 04:08:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d45ba15-1629-3053-99ec-59c548b802a9 | -6.96713 | -44.01659 | 2025-10-23 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d253ce7-b2e7-36fd-aaf2-70e37eb448f4 | -8.35091 | -46.18186 | 2025-10-23 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07f5a972-92e3-38e2-8dc1-a828ad29ed11 | -12.9135 | -47.73866 | 2025-10-23 04:08:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8bd5efe5-347e-3dc1-b01d-b32a425bc556 | -6.17845 | -46.7424 | 2025-10-23 04:08:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c3b3ea70-eb79-383c-af95-20e872309bb4 | -14.20918 | -42.86819 | 2025-10-23 04:08:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ac9d1bd2-14a8-3cf9-b12c-e1214d1e63ed | -12.80593 | -51.33169 | 2025-10-23 04:08:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89ad9da4-f8a1-306c-8017-ef15d47f6d81 | -6.79586 | -45.45665 | 2025-10-23 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1863b21a-2402-3c81-ab3d-9c8751dd8bd4 | -7.76279 | -44.90429 | 2025-10-23 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99d0b47e-a5e6-33e1-b483-e1740d648b56 | -7.2014 | -45.30246 | 2025-10-23 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef295d9e-c1d5-34b4-b51a-9aa213d10102 | -12.90777 | -48.49071 | 2025-10-23 04:08:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b371712-6dfe-30b2-9eb2-40cde5904879 | -12.91344 | -47.74092 | 2025-10-23 04:08:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e384f1e3-3942-39ab-a2ad-9047a73aa38c | -12.6884 | -48.64023 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2f074bc6-a82b-37a4-828b-fd395c43b747 | -7.06565 | -44.10342 | 2025-10-23 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7d9990b-9c76-3c66-8229-e68ff70820cc | -13.375 | -46.63997 | 2025-10-23 04:08:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45da01fa-e3db-3ea7-98d5-d2fd75a7223a | -13.12806 | -48.2447 | 2025-10-23 04:08:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a85bd048-74fd-3a3c-85ca-2f042646ffe4 | -12.77497 | -47.38116 | 2025-10-23 04:08:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e51b9401-7276-3386-9326-b082ab5adff3 | -13.21092 | -47.74749 | 2025-10-23 04:08:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e604b694-573f-3eb0-93bc-8b81254389fa | -11.99576 | -46.77956 | 2025-10-23 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 35a64f57-cdfc-3f96-a4bf-b46e3a95d2bb | -10.99416 | -47.80041 | 2025-10-23 04:08:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a749a18-e084-3863-8f34-d9a9b75ffd68 | -7.26459 | -46.17007 | 2025-10-23 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2466989c-c933-3719-ad64-19755664b155 | -10.2495 | -47.99519 | 2025-10-23 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README11.md)
