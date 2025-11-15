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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3474e0c-237c-3606-84e9-7578befb982f | -10.4437 | -45.07652 | 2025-11-15 03:36:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc04f069-3719-3334-96ea-e840ae66da10 | -6.28891 | -41.75778 | 2025-11-15 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 04e9db54-b34a-37b8-abe5-61c1e5219385 | -9.81336 | -44.22513 | 2025-11-15 03:36:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 829e9d1f-7edf-36bf-afb3-bc211ef9cf3f | -5.96778 | -42.99016 | 2025-11-15 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 011951c8-9bd0-3a02-a27f-0a1d50756972 | -5.52444 | -41.77094 | 2025-11-15 03:36:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 86d05814-f24b-37c2-8c7c-ece6c740a45d | -7.10545 | -39.07732 | 2025-11-15 03:36:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a179c123-6740-3de3-bc0b-19c06eaab048 | -9.85817 | -44.71568 | 2025-11-15 03:36:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 704816d7-a047-38f6-9554-6b4d6ccca6cc | -7.74996 | -36.95427 | 2025-11-15 03:36:00 | NOAA-21 | SUMÉ | PARAÍBA | Brasil | 2516300 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2d57ffeb-e227-3f05-8317-ac2b375248dd | -5.53004 | -41.76875 | 2025-11-15 03:36:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3cd20794-1490-3ea8-b361-8d43f00d6b7d | -5.51988 | -41.76701 | 2025-11-15 03:36:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d6776879-5a04-31b4-a58c-462f9b1b924f | -10.68771 | -45.17868 | 2025-11-15 03:36:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efc407ce-2f29-33fe-bd2d-f1a3435881d1 | -7.21356 | -35.02708 | 2025-11-15 03:36:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 602f4612-4a9d-3609-88ed-d3086f7a4333 | -10.44874 | -45.08166 | 2025-11-15 03:36:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c7eb96e-da14-339f-a76c-a48e36bdbab3 | -5.23136 | -44.35065 | 2025-11-15 03:36:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| a69fc493-4b9b-3d87-86d3-4f14bc7a281f | -10.43065 | -40.54773 | 2025-11-15 03:36:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2e69a8d7-dc65-338a-ac42-af9de6fcb4ae | -9.48525 | -47.28278 | 2025-11-15 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 508d0cc5-c386-31b9-97f8-d5f2b400792a | -5.42047 | -43.25918 | 2025-11-15 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e721cf6f-4990-38ae-98de-e768c0b5c91e | -5.23657 | -44.35639 | 2025-11-15 03:36:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| d966f561-a89a-3d36-89a8-7d7e193c51b7 | -7.42441 | -43.86797 | 2025-11-15 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 73540da2-7150-3b5d-af7e-307d0934a61d | -7.49174 | -42.55556 | 2025-11-15 03:36:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 8255cb7b-17a3-3dec-9498-4e5fcccfcbb6 | -7.72691 | -45.81307 | 2025-11-15 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec26701b-5173-309c-bcf6-3e2bb27c19ec | -7.42252 | -45.23189 | 2025-11-15 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b78a0f5-8073-3abd-9e72-619498afe043 | -9.81263 | -44.22902 | 2025-11-15 03:36:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09371201-fa64-3139-ba88-4e644cfc24b1 | -6.41276 | -41.46028 | 2025-11-15 03:36:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 300766a0-1e9f-3f13-bdb2-11c35df99d8e | -5.65571 | -41.08709 | 2025-11-15 03:36:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 9c4450cc-5489-3954-8d80-6cb4e301cb9e | -7.43575 | -45.22929 | 2025-11-15 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06c62f3b-4fe5-3595-8117-1c1b92f8d562 | -7.25809 | -40.17882 | 2025-11-15 03:36:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dc80ba27-2147-3ff0-b83d-4d12a7c6b099 | -7.53055 | -47.20228 | 2025-11-15 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9d47ccdc-d239-3310-9076-fecc028c5ea3 | -6.28494 | -44.74724 | 2025-11-15 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8e0a7c9-ce97-3e6b-b765-76715f9d9365 | -9.80625 | -42.21099 | 2025-11-15 03:36:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| c6b38048-3178-3d98-9eeb-ffa59fb9b0ba | -5.88219 | -41.11633 | 2025-11-15 03:36:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5d4b7c88-2fc0-30ee-bc1c-45d809fcc55a | -10.69889 | -44.50671 | 2025-11-15 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e9ce109-e125-34b1-9472-5cca6fc356c2 | -5.59791 | -45.80135 | 2025-11-15 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a9d0aa15-0753-3a7b-b02b-767298be15a8 | -5.77525 | -44.38551 | 2025-11-15 03:36:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08e1097d-b1fb-34e0-b141-937ec0baea50 | -10.42613 | -44.94957 | 2025-11-15 03:36:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4a7666ed-06a6-3a9c-9155-6d6ec94d762e | -10.70016 | -44.50753 | 2025-11-15 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9aec711d-aff5-370c-be34-a84da3d2a063 | -6.40783 | -41.45959 | 2025-11-15 03:36:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e747e903-e9c9-328b-9017-e22bc326d36c | -9.48757 | -47.28395 | 2025-11-15 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8f14485c-19b9-3a71-af72-e53099fc8822 | -10.8902 | -44.93858 | 2025-11-15 03:36:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ed6118b-10d2-3ad8-84a9-0ce778b84148 | -7.72217 | -45.81455 | 2025-11-15 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20676173-6f7a-3e0b-9603-acb20c22b54d | -9.86466 | -44.71275 | 2025-11-15 03:36:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1044823f-11a8-3d3f-91c1-7f78ae98c3e8 | -9.67681 | -37.08901 | 2025-11-15 03:36:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1c6b55a4-d7d0-3c94-bcc5-f749354956f0 | -8.99687 | -44.18457 | 2025-11-15 03:36:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3ad1fa7e-b58c-3eec-b152-492f5c38154c | -6.01677 | -41.96041 | 2025-11-15 03:36:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1c72d899-7711-3a45-b1b8-8cd6bd2c6501 | -5.51935 | -41.77007 | 2025-11-15 03:36:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 24bcd5f3-fb65-3ea7-b70b-332ae4a1480a | -6.10192 | -41.52687 | 2025-11-15 03:36:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 78705b55-2177-3f86-b373-5bddae99087a | -6.28657 | -44.73821 | 2025-11-15 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ec29a2d-b198-34f7-8ff5-71daad95abb3 | -5.38089 | -45.37079 | 2025-11-15 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b054c97c-b5b9-31b6-a246-c1cd5de3f9e4 | -6.88333 | -41.59404 | 2025-11-15 03:36:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2a0f3b07-05aa-3462-a031-106194bd27f6 | -17.15815 | -43.07983 | 2025-11-15 03:38:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd9164ca-8704-3572-98d4-a8a00fdea811 | -12.02505 | -43.72919 | 2025-11-15 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d97c987-5490-357f-91e2-b36b0174d926 | -17.42497 | -41.69043 | 2025-11-15 03:38:00 | NOAA-21 | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ffd25f9f-6221-344d-8919-429d0d37d2bc | -12.75759 | -43.64649 | 2025-11-15 03:38:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22ded229-fd56-3c8e-96ee-eb35ad786b2c | -18.32955 | -47.18877 | 2025-11-15 03:38:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a20b3d86-dd3f-3267-b8a9-53db7014c9cc | -17.57944 | -46.6834 | 2025-11-15 03:38:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 6fa3b50a-572b-3d9e-87f5-23003c4603fd | -17.2459 | -42.66215 | 2025-11-15 03:38:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a1d7272f-eab6-384a-bc08-b68b81015ccc | -12.39133 | -48.10969 | 2025-11-15 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0715c31a-eba0-3abc-bc02-10503010847a | -11.80805 | -48.08125 | 2025-11-15 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc0101b3-353c-37e2-a02c-e1ac18ab168f | -11.71391 | -48.87675 | 2025-11-15 03:38:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75a0f820-78c7-3c6a-96cc-f40f93b8773e | -15.34634 | -47.86229 | 2025-11-15 03:38:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dd107852-3cb3-340d-b709-1e363605ece4 | -15.47442 | -43.19093 | 2025-11-15 03:38:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e2309b45-14f5-3845-844b-807a1672ce42 | -16.4475 | -45.00972 | 2025-11-15 03:38:00 | NOAA-21 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 477ea778-58b2-3645-9d9c-3b3a62da37eb | -11.80398 | -48.07484 | 2025-11-15 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d2847e71-86ee-3ee9-8480-64ad66343f69 | -12.77284 | -46.9519 | 2025-11-15 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91f08461-6897-3ec0-ab6d-461b02fdb0a4 | -14.98661 | -42.41177 | 2025-11-15 03:38:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5448ece6-0b52-3b4b-90e6-06c33c33024d | -12.67661 | -46.76793 | 2025-11-15 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 730f4035-5652-309c-8322-a1b488a25326 | -17.5803 | -46.67939 | 2025-11-15 03:38:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5af72cd7-372d-36be-8220-02dae51afbbc | -17.24502 | -42.66685 | 2025-11-15 03:38:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 31fb0ce6-c327-3e56-8f3d-286140d3ba9c | -12.90311 | -45.10368 | 2025-11-15 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ede5b83-8bfa-382f-bca5-4514c2faa4ae | -17.58593 | -46.6806 | 2025-11-15 03:38:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 914af5d0-c4c9-38bd-b107-2303e5b15071 | -16.56138 | -47.61274 | 2025-11-15 03:38:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93bc7fac-666b-30ec-81ff-6334f2a0d5c5 | -11.75018 | -45.33744 | 2025-11-15 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4419918a-c49b-3128-b9b3-468d18f3c4e9 | -14.951 | -47.50701 | 2025-11-15 03:38:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4ec49004-ca98-34a6-b999-88fb9f628a4e | -12.6786 | -46.75817 | 2025-11-15 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9c99dcdf-52a5-38de-a5f7-1dd8ec15231a | -18.06738 | -42.34808 | 2025-11-15 03:38:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b80ef9a9-6456-390a-a935-d62186caf182 | -12.04021 | -43.7399 | 2025-11-15 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b86a3ccf-8d73-3ac9-980a-0ec0d4eba4f2 | -12.84663 | -46.43335 | 2025-11-15 03:38:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e49d8aa2-a321-3f1b-b184-c9cf17ebe5e9 | -11.3243 | -48.51314 | 2025-11-15 03:38:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ba1f8654-bf3f-3056-bd14-f5c744e5e173 | -17.24593 | -42.66058 | 2025-11-15 03:38:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 34a741ff-f088-3e65-b942-a14b0521b77b | -13.67738 | -42.50964 | 2025-11-15 03:38:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| be6ef783-74ba-38cb-8aed-3184d527486a | -12.75643 | -43.65259 | 2025-11-15 03:38:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d464d081-0c28-3aa8-ab26-862e6b6c8f14 | -13.35365 | -43.74554 | 2025-11-15 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4cc115d5-b0ba-325c-a4f7-8f53aba992be | -16.45124 | -45.01326 | 2025-11-15 03:38:00 | NOAA-21 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41dd892b-35d3-317a-960b-3e71a392748d | -12.46096 | -43.75528 | 2025-11-15 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 35974d7d-7aaa-310c-90ad-fd4d89330561 | -12.68279 | -46.7692 | 2025-11-15 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| cd067852-38a2-30b1-90a9-b477a9dda5b7 | -11.79653 | -47.40948 | 2025-11-15 03:38:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9b215cb-2452-30a9-81ee-00119dbb6f2f | -13.73942 | -44.16001 | 2025-11-15 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51cd3243-76fb-3f46-a444-9332b2522247 | -16.45199 | -45.01413 | 2025-11-15 03:38:00 | NOAA-21 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ea455c8-f932-3b0e-89cf-31c636884850 | -12.45946 | -43.75374 | 2025-11-15 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 01e38805-a8b7-327a-baee-f841e878296d | -12.77787 | -46.95917 | 2025-11-15 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a743ccf-9e80-319f-ae6d-1e84e660e3e6 | -15.36606 | -45.63575 | 2025-11-15 03:38:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa7a6e96-7ced-366f-9883-bf7bfd2b912b | -17.24505 | -42.66508 | 2025-11-15 03:38:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 54b0ccd0-d502-3d0b-ad7e-42d0cfbd2cea | -17.1597 | -43.07784 | 2025-11-15 03:38:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e1440a33-d816-3348-b3c0-0c684ab765a9 | -16.87715 | -42.13257 | 2025-11-15 03:38:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1a2cbf64-0062-3fbe-9ef7-4efc37074666 | -12.66103 | -46.74966 | 2025-11-15 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| cb6f403f-9da4-3ee5-87da-89e2089d5a90 | -12.66204 | -46.74475 | 2025-11-15 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d6dc572a-4a23-3b56-91b1-e8ccaa3627c2 | -12.65279 | -43.2477 | 2025-11-15 03:38:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0c37327f-e72f-3278-911d-39a5e6072249 | -12.02564 | -43.72602 | 2025-11-15 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9396a420-9142-3568-bcb2-3b72f50d53e5 | -18.45218 | -40.1466 | 2025-11-15 03:38:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6d7f298f-a411-386b-8660-3739d283d4ef | -12.4646 | -43.75475 | 2025-11-15 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README16.md)
