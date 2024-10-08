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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c2d5c61-8e0e-38a2-a737-f19e1274a98f | -14.78142 | -42.84389 | 2024-10-08 03:42:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 131f9765-0ad5-3bdd-b293-ea173c72c968 | -14.01575 | -42.47687 | 2024-10-08 03:42:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 45e814ff-7334-35c6-b7fa-731fb7f81c5d | -14.7698 | -43.50082 | 2024-10-08 03:42:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fac119e6-e3e9-3211-913e-4d4e69f1e3db | -14.53511 | -43.21995 | 2024-10-08 03:42:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ce338a45-ab74-3ee4-8077-6f10a65b9ae4 | -14.53434 | -43.22416 | 2024-10-08 03:42:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 85302c2a-65de-3d04-acf4-965965371238 | -14.53081 | -43.21909 | 2024-10-08 03:42:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 406acdcc-56c4-3fd6-be86-d433330da549 | -13.86611 | -44.63281 | 2024-10-08 03:42:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4bac3127-6bd7-3aa2-954a-e18d1db63d22 | -13.84981 | -44.58838 | 2024-10-08 03:42:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6aaaaec0-5844-3e22-b50b-ed6fd0eee936 | -9.53039 | -42.99339 | 2024-10-08 03:42:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 97117f8a-cda2-37b9-b623-ba1c1e216847 | -9.94326 | -44.11246 | 2024-10-08 03:42:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03065363-6dec-33ee-85a6-d27a0b27f737 | -9.53718 | -44.07537 | 2024-10-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94bb34a2-1120-3d51-ba57-ef69e271367a | -9.42514 | -44.12474 | 2024-10-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f2aaabe-f4a9-3de3-981d-bf3ae7ac3332 | -9.42465 | -44.12743 | 2024-10-08 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35be06cb-33cb-325e-9b18-a3265f4f12b3 | -9.52578 | -42.99249 | 2024-10-08 03:42:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 9c611380-2dc6-3c05-91c4-cdcfe98976eb | -13.75863 | -44.00565 | 2024-10-08 03:42:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5eeee330-e99e-359b-bdb3-b80812b67a75 | -13.72632 | -43.92638 | 2024-10-08 03:42:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8eb20c77-5e12-358b-bf88-71a9d091b582 | -13.72546 | -43.93103 | 2024-10-08 03:42:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebe4b886-8e22-3c43-9951-55f75f299538 | -13.72529 | -43.90642 | 2024-10-08 03:42:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4551af49-8bf7-35c6-8992-7d14fc96d7dd | -13.58138 | -43.79274 | 2024-10-08 03:42:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 053cdeb9-6622-386f-948c-ea707aab7da3 | -13.53326 | -44.02191 | 2024-10-08 03:42:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebabb5cc-3186-3388-9a19-42c44180ae3f | -13.51863 | -44.40739 | 2024-10-08 03:42:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ed493a85-f5f1-346a-9be0-bcf7affe0794 | -13.49414 | -44.38125 | 2024-10-08 03:42:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1d3ee54e-0bf4-3952-bfff-8bb595bb8f9c | -13.48235 | -43.66604 | 2024-10-08 03:42:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e52480ba-ea00-342d-b563-5864a775acf9 | -13.41955 | -43.79762 | 2024-10-08 03:42:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aa5095df-26a6-3826-ab07-77a459ec3364 | -13.41867 | -43.80239 | 2024-10-08 03:42:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 33743fbd-b3db-31ad-8c72-b478bc6db058 | -13.37306 | -43.76889 | 2024-10-08 03:42:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dbc10242-4e89-378d-b8b3-a3a27f142acc | -13.36852 | -43.768 | 2024-10-08 03:42:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58002772-2d1c-3d97-af5b-49e355489e9d | -14.70996 | -45.1578 | 2024-10-08 03:42:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d481b762-39cc-36b5-ae9c-3d6130c06234 | -14.70726 | -45.15837 | 2024-10-08 03:42:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 3ed16875-1141-33cb-80e3-454baf4afbea | -14.70513 | -45.15667 | 2024-10-08 03:42:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c1f9835b-561e-346c-8e23-2bdd557acb9d | -14.70407 | -45.1622 | 2024-10-08 03:42:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 19b67a9c-8d4a-3148-89d9-f98ef3c2216f | -14.69924 | -45.16104 | 2024-10-08 03:42:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dd083d32-e89c-33e8-af98-3f15386556f4 | -14.11448 | -44.10014 | 2024-10-08 03:42:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0d80b455-b247-37d3-b813-dcb9ffc086d7 | -14.11357 | -44.10499 | 2024-10-08 03:42:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 318fbe22-4b48-3585-b55b-2db67413c387 | -14.11254 | -44.03455 | 2024-10-08 03:42:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 34052728-42b5-3334-84ab-313322645166 | -13.95912 | -43.97042 | 2024-10-08 03:42:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb6b2891-4af5-3aa1-88ed-914981ecc6e0 | -13.95201 | -44.62297 | 2024-10-08 03:42:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 820ffe65-5c47-35bb-848b-0dd85b4495f9 | -13.95188 | -44.62308 | 2024-10-08 03:42:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd3dab37-5cac-3124-ba8f-563ddb3267e6 | -13.94827 | -44.61658 | 2024-10-08 03:42:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e7d96f99-13ff-3730-91b6-c7a33c87199e | -13.94818 | -44.61671 | 2024-10-08 03:42:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7a9779b4-9590-33bb-9d5f-876fc8d81e74 | -13.94728 | -44.62188 | 2024-10-08 03:42:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c25975b1-d52b-3a2a-98d4-7a5554d530f6 | -13.94715 | -44.622 | 2024-10-08 03:42:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d7698db6-a4c2-38b9-88f5-87eca87f53d5 | -13.9133 | -44.5926 | 2024-10-08 03:42:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cad23b8d-e2c6-39ef-ab7e-423cff25d90a | -13.91305 | -44.62003 | 2024-10-08 03:42:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1387a26c-bde3-3ac6-adf8-2145398e911f | -13.90955 | -44.58635 | 2024-10-08 03:42:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c28b02fc-ee48-39a8-8a2e-712e46c59bdf | -13.90831 | -44.61899 | 2024-10-08 03:42:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd882bdc-5d22-3753-b1b8-677ae8077121 | -13.90758 | -44.59675 | 2024-10-08 03:42:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff9ab045-1a98-3eaa-a50e-87c00b1d85ce | -13.90285 | -44.59567 | 2024-10-08 03:42:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c81a38a-2c1f-3162-adca-efcc7e90af00 | -13.86031 | -44.58493 | 2024-10-08 03:42:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e56ca8c-b8d1-3345-b630-c8a9880aa45e | -13.85556 | -44.58398 | 2024-10-08 03:42:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1dbccc80-399b-30f6-aa38-1813bb043ec2 | -13.85531 | -44.58619 | 2024-10-08 03:42:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 811e3aac-4323-341e-9b09-770db348e808 | -13.8454 | -43.89606 | 2024-10-08 03:42:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d57c999-9eec-33f5-a9b5-36672468ca18 | -13.84504 | -44.5875 | 2024-10-08 03:42:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d7f2b11-28d6-3a42-984c-60440c5a3fb3 | -13.84474 | -44.58976 | 2024-10-08 03:42:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 517ae870-ccc0-3d6d-b844-8d44c3df363d | -13.84086 | -43.89515 | 2024-10-08 03:42:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c050dbc-6176-31f9-a0bd-b08d78f318cc | -13.81798 | -44.62648 | 2024-10-08 03:42:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8dd2ad82-874f-304d-8afb-7ea9776ce2b6 | -13.81219 | -44.63099 | 2024-10-08 03:42:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f8abdc0-c0c6-329a-a769-5a6b03289cb8 | -14.20595 | -46.4469 | 2024-10-08 03:42:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a0c6d7d-ccc7-3903-8f68-d1854f249cdd | -9.12138 | -45.52729 | 2024-10-08 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab711d21-e04d-3a1e-ad76-3617fa06bdd6 | -9.12108 | -45.52772 | 2024-10-08 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0201436d-5109-370b-9f68-c965a35da4a8 | -9.12071 | -45.53096 | 2024-10-08 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f101977-c242-35b2-9a28-ac9fa9905082 | -9.12039 | -45.53138 | 2024-10-08 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c06cf74-1a66-3544-b6c3-26ae64c14e2b | -10.47073 | -45.11504 | 2024-10-08 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5e9501e-04e4-381a-a966-870af68a5396 | -10.07299 | -45.27427 | 2024-10-08 03:42:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5a7b3137-bb9b-3c93-942e-59e9fd338852 | -10.07234 | -45.27777 | 2024-10-08 03:42:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d694bb95-18ac-37c2-b75f-66d3c6397fbb | -10.06701 | -45.27675 | 2024-10-08 03:42:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 484caf45-37d8-3b85-a742-695601892d9e | -10.06633 | -45.28036 | 2024-10-08 03:42:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 86279c04-7e01-3866-915a-0fa1fd7f8b80 | -10.06099 | -45.27942 | 2024-10-08 03:42:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 260dbf9a-5b7d-320a-af09-4616d01f22a9 | -10.66451 | -44.50909 | 2024-10-08 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98eda3c8-ba37-3ad3-a7fc-39cdce2d3d28 | -10.66397 | -44.51203 | 2024-10-08 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdc31eb7-97e6-3b15-af0e-669f6e24ebee | -13.23318 | -45.5363 | 2024-10-08 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4e3ac0f9-29a5-3d79-8f49-51f6167d1374 | -13.23022 | -45.53552 | 2024-10-08 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| cf93c741-d36a-3f60-88bf-0bb266339b61 | -13.22805 | -45.53531 | 2024-10-08 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 91f91558-fe19-3f55-8f10-ca5f714bad0d | -13.22746 | -45.53846 | 2024-10-08 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 15fa8137-b9e0-35e5-9027-2464d4cfc3c6 | -12.99567 | -46.21549 | 2024-10-08 03:42:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55f81f87-291e-3a19-a4bf-f181e9448f6f | -12.99498 | -46.2191 | 2024-10-08 03:42:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 92609791-6626-3f46-b715-fa4d326c5d1b | -12.99308 | -46.21101 | 2024-10-08 03:42:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e4d271b3-ae89-3414-bcc4-3706486f0740 | -12.99233 | -46.21475 | 2024-10-08 03:42:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| deede07b-cb87-35c7-8bf5-6e51b7e93e22 | -12.99157 | -46.21858 | 2024-10-08 03:42:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 243af7b1-a58b-394d-8a34-cca766448628 | -12.99084 | -46.22225 | 2024-10-08 03:42:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00c106c3-1a1d-35a2-9ac1-7f6c1cf417bd | -12.99015 | -46.22569 | 2024-10-08 03:42:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eccad6cf-b38e-3447-b39c-7f15a7041c7e | -12.98942 | -46.21902 | 2024-10-08 03:42:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cf4acb3e-172c-352a-8652-2747df8f5f12 | -12.98871 | -46.22271 | 2024-10-08 03:42:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aed8476b-f2e4-345d-b94b-2d179586290b | -14.22141 | -46.45294 | 2024-10-08 03:42:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dc8c269-d22c-36d9-93b2-d2cc3d699365 | -14.21673 | -46.4485 | 2024-10-08 03:42:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3206945-9f6b-3315-8d10-ee8b1cc27f5d | -14.21604 | -46.45203 | 2024-10-08 03:42:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2a870da-1d25-3961-90f7-63df4d9dc693 | -14.21131 | -46.44788 | 2024-10-08 03:42:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95129751-1221-3d46-816b-2fdeac300bbf | -14.2007 | -46.44537 | 2024-10-08 03:42:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50acd6ba-3602-30e4-87d3-abdbd2d73fb0 | -14.20002 | -46.44877 | 2024-10-08 03:42:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1e41938-fc29-3d16-a443-ba89ed21a488 | -14.19934 | -46.45222 | 2024-10-08 03:42:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57e4fdb3-8578-3ec8-99aa-f58caae1a201 | -14.19409 | -46.45065 | 2024-10-08 03:42:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92c28f66-cf68-3d16-820d-5a4af444c9b2 | -14.1274 | -45.60575 | 2024-10-08 03:42:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 705c36d7-122d-3bb2-bf20-9ef7c80eb0b9 | -14.12231 | -45.6049 | 2024-10-08 03:42:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12fc91de-2173-3963-8aa8-daa142331521 | -14.12171 | -45.60795 | 2024-10-08 03:42:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5d97966-7d78-3f9c-8e7b-f6dfa4660987 | -14.11783 | -45.60093 | 2024-10-08 03:42:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51489cf2-e11d-3a27-8bd5-b23b89732de3 | -8.52902 | -46.59741 | 2024-10-08 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4dc5d766-ed7a-392b-a1ae-699a8a243a2b | -12.16343 | -47.76202 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 62b3c663-f3cf-315b-a623-593774fc9d66 | -12.1626 | -47.76612 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 23f348fb-6bec-3676-b7aa-8053c18d2923 | -12.16179 | -47.77009 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e272789e-3cf1-304d-8aaf-3dbd1255953f | -12.1616 | -47.76278 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |


[Clique aqui para ver as próximas entradas](README37.md)
