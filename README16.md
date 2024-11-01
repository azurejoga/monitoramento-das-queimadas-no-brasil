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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0acb6a15-3b1f-36b2-b93d-2f8d6deb21a1 | -3.94409 | -41.51828 | 2024-11-01 04:06:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ea0bed0e-4594-3373-bbd9-d50b1432a7b6 | -3.94271 | -42.63116 | 2024-11-01 04:06:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 40a2205d-3cdb-3ffc-960c-eed86bfe2cc8 | -3.9424 | -41.50731 | 2024-11-01 04:06:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7c00349f-0c8d-3d52-ac7b-3c5eccb90f63 | -3.94186 | -41.51078 | 2024-11-01 04:06:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ee8f69e3-d5da-31c2-bf06-da8d9bf912e4 | -3.94131 | -41.51427 | 2024-11-01 04:06:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ffce7b3b-a5fe-3316-970b-5227367f0acb | -3.56458 | -42.70175 | 2024-11-01 04:06:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a693a8f8-11d5-30fa-96a3-9b62c4d8ebdf | -3.56398 | -42.70547 | 2024-11-01 04:06:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aab13c70-22fc-300d-b355-ee7efd207a77 | -3.56167 | -42.70184 | 2024-11-01 04:06:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7fe5735c-a21e-3fee-a18f-f00f77b519df | -3.56108 | -42.70556 | 2024-11-01 04:06:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 12e43ca4-1495-3fdb-a8ba-e69deefbdd51 | -3.56054 | -42.70493 | 2024-11-01 04:06:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e55aea0-3482-354b-9c78-351f1ef4813b | -6.38243 | -42.75702 | 2024-11-01 04:06:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 61dbb66e-14d7-3d1d-8764-dc4bd8ad702d | -6.37905 | -42.75648 | 2024-11-01 04:06:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c723142c-f68c-3ebe-8e88-b8a77406da77 | -6.31663 | -42.28718 | 2024-11-01 04:06:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 89efac6e-630c-3183-a7e1-0a6be48b2fc0 | -6.31161 | -42.0384 | 2024-11-01 04:06:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4dbeecc3-7328-39a1-a2ef-587764ae5135 | -6.16522 | -42.08332 | 2024-11-01 04:06:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 62a6c1e4-56fb-35b8-9a71-78a7f286f5df | -5.9583 | -42.67879 | 2024-11-01 04:06:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 36cf4497-2998-3c38-8953-6ee581e26d1e | -6.31217 | -42.03488 | 2024-11-01 04:06:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 83f51a26-feeb-3fb6-9a39-905c06a6b232 | -5.94168 | -43.34983 | 2024-11-01 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3e5763bf-b7a6-37ae-b209-a0439e18da11 | -5.93883 | -43.34551 | 2024-11-01 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2dece0f4-08e8-375d-bc5a-fc818785e420 | -5.93823 | -43.34926 | 2024-11-01 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 78151f2f-6a68-3c95-9b3a-b46940344368 | -6.3155 | -42.03543 | 2024-11-01 04:06:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9925c903-ad7e-3860-91c7-d264decedd3f | -5.72518 | -42.18996 | 2024-11-01 04:06:00 | NPP-375D | PRATA DO PIAUÍ | PIAUÍ | Brasil | 2208601 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6a60b6e7-757d-35d5-b8f0-80f2e4ef0cb2 | -5.65541 | -41.88456 | 2024-11-01 04:06:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a05b6531-e64b-3e38-bf4e-0264e28e1da2 | -6.18555 | -43.06808 | 2024-11-01 04:06:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c507e047-6f74-30f6-b0a0-a00422acaf66 | -5.16662 | -42.51369 | 2024-11-01 04:06:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1fce51d1-7534-3523-b0f4-cd4a24436f78 | -5.72853 | -42.19049 | 2024-11-01 04:06:00 | NPP-375D | PRATA DO PIAUÍ | PIAUÍ | Brasil | 2208601 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 8c0ed058-dc89-3482-9430-1d03f6c467d1 | -5.21804 | -42.78127 | 2024-11-01 04:06:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 107b3cee-b265-3221-99e6-f03dd78ddf7d | -5.46517 | -43.17912 | 2024-11-01 04:06:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5cce772f-9122-39ce-b65f-12186ccaf2e1 | -5.46234 | -43.17483 | 2024-11-01 04:06:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a92fdae7-0a3d-3f1d-a173-1c787c4a33ad | -5.46173 | -43.17856 | 2024-11-01 04:06:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25d51e65-9b7b-34ed-bd22-9ea7ab233058 | -5.33841 | -43.10224 | 2024-11-01 04:06:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c537e14e-dbd5-3c8f-966a-391bd41514e3 | -5.33782 | -43.10593 | 2024-11-01 04:06:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf9da454-4d77-3eb5-a55b-db8f2e18cb1a | -5.33737 | -43.10192 | 2024-11-01 04:06:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1e08f42-8e40-3bf6-b2dc-0f818e895f85 | -5.33677 | -43.10561 | 2024-11-01 04:06:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20aa7a4a-8cd0-3e9f-8136-ed626ec34fd3 | -6.72355 | -42.74076 | 2024-11-01 04:06:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 661e2bad-d9e5-3117-8641-20e81f2ef861 | -6.69679 | -43.05856 | 2024-11-01 04:06:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68a27a0b-4756-39e7-b806-74c70db93a2a | -6.58451 | -43.14969 | 2024-11-01 04:06:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eaeda048-0dd1-3228-84ac-c8ec60888459 | -6.58026 | -43.5836 | 2024-11-01 04:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b7c3237-4be3-36c6-85fc-0ae197877ae2 | -6.57429 | -43.14802 | 2024-11-01 04:06:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5fbd5216-b183-3908-99fa-5635c401ed9d | -6.49875 | -42.85659 | 2024-11-01 04:06:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 756060ac-77d3-3706-8f0b-19b5a995f555 | -6.49933 | -42.85298 | 2024-11-01 04:06:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bb891450-db1d-3745-b8b8-e87578328d4b | -7.65998 | -42.83114 | 2024-11-01 04:06:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 21af19a2-735b-3d52-8b93-a4b9692202db | -6.50271 | -42.85352 | 2024-11-01 04:06:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f084b0ed-8df0-3ffd-b223-b58bbb61297a | -6.69737 | -43.05492 | 2024-11-01 04:06:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 894d8d93-f299-3376-96c4-d407e9bee1b4 | -6.50213 | -42.85714 | 2024-11-01 04:06:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 777ad88a-a533-3ec1-89d7-921d08b7858f | -3.57293 | -43.22798 | 2024-11-01 04:06:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b621a62-5f7a-3cca-8bd9-716cda7053fc | -3.57232 | -43.23187 | 2024-11-01 04:06:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9dc2e214-daae-3bbb-8dde-bfa811c248e0 | -4.45319 | -44.33147 | 2024-11-01 04:06:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10e668b3-0769-3381-925c-ebfccee03c08 | -4.12271 | -44.27375 | 2024-11-01 04:06:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b117ebf9-e88a-38b7-835e-45250097c55b | -4.93723 | -43.63056 | 2024-11-01 04:06:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c026d31-ebd9-3f46-b9c9-2ee42f383c15 | -4.93372 | -43.62998 | 2024-11-01 04:06:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0ee8355-b7dd-326e-8a96-e2d94d6b82ca | -4.7413 | -43.25259 | 2024-11-01 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f3b3025-b4af-39ca-bce9-17c20bfaabbf | -4.44926 | -43.65781 | 2024-11-01 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4df8b005-d311-3fed-9ee8-839a8682e0b2 | -4.44699 | -43.64928 | 2024-11-01 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54b810d0-cf6a-3d84-a2c3-7c63fbfb544f | -4.44635 | -43.65327 | 2024-11-01 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8f1c760-19aa-3e20-abe2-664107272be5 | -4.44253 | -43.67712 | 2024-11-01 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15af5ef7-fdb7-3077-96f8-242c17dd090b | -4.43898 | -43.67655 | 2024-11-01 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55992011-c6f6-3a75-8aeb-ee7f374ef2b0 | -4.4002 | -43.46937 | 2024-11-01 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 728bab16-d88b-3e1e-b6d5-a527306289c4 | -4.39958 | -43.47329 | 2024-11-01 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 01cf98a5-9c1c-3f00-a9da-0afec600ce1d | -4.39896 | -43.47721 | 2024-11-01 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 68e5c80b-83e8-3d42-a40e-a799e4bdde23 | -4.39731 | -43.46493 | 2024-11-01 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6d929a88-3662-3712-bf1d-c34e84b33f73 | -4.39669 | -43.46882 | 2024-11-01 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| d1ffe0ad-116e-3288-b313-b706dbdc96e0 | -4.39607 | -43.47272 | 2024-11-01 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 69b1ab1c-62b8-3e29-8986-13df3147ad0a | -4.39544 | -43.47664 | 2024-11-01 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e61675d2-c849-3980-aa73-3abb7bc38e57 | -4.39379 | -43.46438 | 2024-11-01 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bca11d6a-d90f-3406-a35f-6b72cccaa805 | -4.39317 | -43.46827 | 2024-11-01 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 820612bd-88c5-3b73-8f84-b2b445d0ec6d | -4.39255 | -43.47216 | 2024-11-01 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| ed4dcf63-49e4-3fac-8701-3e401f6e890f | -4.39193 | -43.47606 | 2024-11-01 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3077a2d6-bb33-32d4-ad74-1c47e14a1691 | -4.38966 | -43.46771 | 2024-11-01 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 3f6dc814-0c61-3277-9f9d-b4ed11c7adae | -4.38904 | -43.4716 | 2024-11-01 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 1600ec6c-55b6-301b-adf5-fc04c4a9456a | -4.38842 | -43.47548 | 2024-11-01 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dcda1693-3ca4-35f4-8dcf-f342582feee8 | -4.38615 | -43.46715 | 2024-11-01 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd659ce2-e101-36d4-9f8c-2489a943cd8a | -4.38553 | -43.47102 | 2024-11-01 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a2279e3-a070-3246-baf9-ac6da3ef4c61 | -4.26535 | -43.43204 | 2024-11-01 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d3f10e3-07ee-342a-9376-2e389d51911a | -4.26473 | -43.43591 | 2024-11-01 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e13b49b-4bbb-3dce-b994-40c9e00c1e94 | -4.26184 | -43.43148 | 2024-11-01 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2cdf92bc-f684-36b0-a0e0-ca820528d9af | -4.26122 | -43.43536 | 2024-11-01 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0b5787f-d930-366e-b4cc-87d4ffd79f8c | -4.20233 | -43.30757 | 2024-11-01 04:06:00 | NPP-375D | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f62314b7-d4b8-3df1-877a-af6f453ef520 | -4.18019 | -43.78057 | 2024-11-01 04:06:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39890044-0d25-39b2-bfcd-e4be743c082c | -4.17662 | -43.77998 | 2024-11-01 04:06:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5d9cd1e-518c-3904-b691-628a4dfffd77 | -4.08389 | -43.95924 | 2024-11-01 04:06:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 747a81cc-f9ee-3871-b525-d3bde646c84c | -4.06503 | -43.28652 | 2024-11-01 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc14417c-b243-328e-bc0f-6d3ea073301d | -3.89088 | -43.9993 | 2024-11-01 04:06:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fd7235a-0947-3765-a596-611556ce1b95 | -3.8758 | -43.95413 | 2024-11-01 04:06:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83750c0d-565a-31d8-a172-a5fc93aa012c | -3.87218 | -43.95356 | 2024-11-01 04:06:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03e95f81-b3cd-3ccf-9ae9-14562872d659 | -3.76954 | -43.53004 | 2024-11-01 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9c2c7331-211e-3e39-8b2e-63ed6a45207f | -3.7689 | -43.53397 | 2024-11-01 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb513bd6-2184-31fa-8b71-04b98b76126f | -3.76762 | -43.54185 | 2024-11-01 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9dc93232-d1ff-3426-9273-4b9c7998347b | -3.76698 | -43.5458 | 2024-11-01 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fac15cbd-3995-39bc-9fe8-e2e1a809bed3 | -3.766 | -43.52948 | 2024-11-01 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b883028b-a8b2-3ce7-ac61-55f6b7ae18d5 | -3.76535 | -43.53343 | 2024-11-01 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fdc47948-b4b0-3c0c-9a4f-bb6ebe185d32 | -3.76471 | -43.53737 | 2024-11-01 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a4a8f98-5290-3439-ae2b-3a49d924956f | -3.76407 | -43.54132 | 2024-11-01 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31dc3d31-110b-3444-824c-fe6fed911e92 | -3.76343 | -43.54526 | 2024-11-01 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| effe4f41-c9f1-36f0-9749-361f49027ae5 | -3.76181 | -43.53287 | 2024-11-01 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76634d40-e85a-3d17-ac46-13e3dcd54ebd | -4.45 | -44.16612 | 2024-11-01 04:06:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00c408c4-0b10-3c3b-92fd-c4b79bec5705 | -4.44705 | -44.16138 | 2024-11-01 04:06:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d10f02e-7072-3d2b-94e4-f1ef3d1fe184 | -4.44637 | -44.16557 | 2024-11-01 04:06:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9db7510-f76b-3296-be9a-ed247fe16d51 | -4.44274 | -44.165 | 2024-11-01 04:06:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45e3a7ed-e0f0-39cf-bc30-33d81950f7b0 | -3.93125 | -44.0041 | 2024-11-01 04:06:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README17.md)
