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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 773bac0f-480c-3e0e-af8e-d11ba20b6809 | -10.54904 | -46.51188 | 2025-07-17 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84f1399d-34b6-3369-b997-4ccf4800808a | -8.87751 | -50.15028 | 2025-07-17 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f97a671-6348-399c-843a-59a33381a5d3 | -7.19222 | -43.11785 | 2025-07-17 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 138b4a5c-1ab6-3a81-bab6-18a434449e97 | -6.71881 | -44.32795 | 2025-07-17 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3999e567-a33d-3e78-850d-b1ac6b3a2a08 | -7.14208 | -43.18405 | 2025-07-17 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1b7f0cde-bd6c-3109-afb5-c6fb715083dd | -6.84688 | -44.76725 | 2025-07-17 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e32704b8-1f84-3439-810d-10add7b45137 | -5.91727 | -43.47936 | 2025-07-17 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89da2dc4-79bc-3c1d-b67f-073933906a25 | -8.88295 | -44.79329 | 2025-07-17 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6f3d2c34-8ba0-368d-a0e9-64e61c3efc18 | -6.97431 | -42.80919 | 2025-07-17 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| db5bf17e-4e4c-3122-be93-9066cde327e0 | -8.10223 | -43.15177 | 2025-07-17 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 28019b9c-1fe1-3be0-815b-b98ae92e1cee | -6.85445 | -44.77005 | 2025-07-17 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c4a8065-c55f-32ad-873d-f195005dc133 | -8.70603 | -50.05305 | 2025-07-17 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6e750d2-c1f7-3e35-8542-33fdfd17d7c5 | -7.94571 | -43.86581 | 2025-07-17 04:46:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f9427730-36bf-344b-a325-bdd83c5760be | -8.05818 | -50.09324 | 2025-07-17 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eaca84e7-5b7a-37c5-8989-7427306fb1e9 | -7.50863 | -55.01265 | 2025-07-17 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 34bee4f4-2a68-3a49-8ebd-e6ff59b50c28 | -12.02574 | -47.77645 | 2025-07-17 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 949798c1-f8f0-3b02-aea9-d904bd01a276 | -7.70509 | -45.87951 | 2025-07-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86f6eac4-824e-3dd0-b967-0cb824d7957d | -9.24201 | -48.55939 | 2025-07-17 04:46:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 98ff7b23-ef88-3f14-973a-4fe710d08559 | -6.29742 | -43.41599 | 2025-07-17 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 766e8ed0-aebe-3396-9dea-246e7dddf4dd | -8.11825 | -43.14804 | 2025-07-17 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 11998a76-6f75-3e21-9e1a-0de2c7da5c1c | -12.10038 | -48.19569 | 2025-07-17 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6c199fd-83f5-3745-96e0-2510a6f5f53e | -6.67746 | -43.03191 | 2025-07-17 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5be31155-c8ca-3322-9782-f4a5d3ba84f5 | -6.84557 | -44.76854 | 2025-07-17 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c24d89cf-4143-347e-a59f-b15fd4fb8308 | -7.9417 | -43.86407 | 2025-07-17 04:46:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5b2070ce-2a00-3c19-a06f-271d8c9d0e81 | -8.63358 | -50.04244 | 2025-07-17 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09a7b808-f4a9-3482-8c92-b01a76adc4ca | -9.23776 | -48.56316 | 2025-07-17 04:46:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b577cdf7-bfad-3eea-b0af-86d08c1075de | -11.58235 | -47.30075 | 2025-07-17 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2cf7a3f3-dbdf-3389-ac90-b8cf318c424a | -8.75067 | -46.59866 | 2025-07-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f9c225c-7062-31d8-ab4e-58926ec01331 | -7.35121 | -44.19741 | 2025-07-17 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 69a457d0-f970-385f-86ec-642b9031fa74 | -7.59438 | -46.33734 | 2025-07-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fdf68cb3-57da-3bc9-91b1-b9205795c599 | -8.10811 | -43.14656 | 2025-07-17 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| fae6bec0-308f-3968-b5a3-1b905345c41d | -9.10848 | -44.30081 | 2025-07-17 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98c41d51-74e6-3c0d-a14c-cb842c4c1c4b | -10.11033 | -58.21949 | 2025-07-17 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80914b4a-6666-332c-9f22-b6f0ecceeda6 | -9.24501 | -48.56423 | 2025-07-17 04:46:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 4b788425-68e0-3c53-bc43-dc69be499584 | -5.79289 | -45.08411 | 2025-07-17 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 763978fd-11a1-3929-8ff5-253f0889fa70 | -9.31049 | -44.84823 | 2025-07-17 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ffc7f072-6b23-3a16-957c-413d07983980 | -10.05772 | -59.10133 | 2025-07-17 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0f369cb-e161-38a3-afa0-ad580749c0ea | -9.8083 | -47.73758 | 2025-07-17 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 317406fe-046c-3d60-a573-63d4c55e20b1 | -11.3623 | -48.73259 | 2025-07-17 04:46:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a417b28-6cc2-3226-8573-e318f80b53bc | -10.00718 | -48.12979 | 2025-07-17 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 842256d1-05a0-319a-b78f-58ac6a6b0de9 | -5.66326 | -43.71468 | 2025-07-17 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 37.0 |
| e88d96aa-c7d5-35bd-8dce-adb340961b92 | -6.71099 | -44.31691 | 2025-07-17 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 155bf8a9-bc22-3cdd-908f-d15a9a6bb848 | -5.8811 | -43.45786 | 2025-07-17 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d070ae4-b0b0-363d-a8e9-63a3488aacec | -6.46359 | -45.34375 | 2025-07-17 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12fe5395-ad69-3e53-a67f-83f85ff266e3 | -11.36163 | -48.73111 | 2025-07-17 04:46:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87aa6fde-2ad5-3998-a825-1bfe952f6cc0 | -4.74326 | -48.01918 | 2025-07-17 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4465c141-e39c-3423-b7df-b7e69c5d721e | -7.59279 | -46.31621 | 2025-07-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8a03a36-3324-3ddd-8742-9145e2eabb5a | -8.1077 | -43.14954 | 2025-07-17 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 08a71cb8-ae42-3663-82b7-eb896d989eef | -5.9716 | -52.20046 | 2025-07-17 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 472fe280-78bf-3d9f-bfe9-757851cde37b | -11.5652 | -47.09116 | 2025-07-17 04:46:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1fdccd86-36c0-3015-8755-f9953e81a13c | -10.10601 | -58.21877 | 2025-07-17 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bfcc4bb-ab3c-3980-87fb-66189ef1b6c4 | -8.88428 | -50.15131 | 2025-07-17 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32abb646-078c-32d0-b1c6-1c7ae37965fd | -7.15097 | -46.09377 | 2025-07-17 04:46:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59e104af-1c78-305c-9891-e4bca56c1adc | -6.98598 | -43.7393 | 2025-07-17 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93ebc2ea-90fb-3175-806e-f6e19b7e916a | -11.4958 | -48.07446 | 2025-07-17 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1615e9c-dfd2-3be8-9246-f0dfd04dfcd9 | -8.88234 | -44.79794 | 2025-07-17 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ad7b424f-0db8-3226-85e0-dd4797b2137a | -11.36294 | -48.72819 | 2025-07-17 04:46:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea40ffad-8f0f-3adf-92ed-a91611fb9caf | -7.23789 | -43.50141 | 2025-07-17 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0b179a82-6b13-3fee-a8bf-75ebcae5dc09 | -6.37722 | -44.74745 | 2025-07-17 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a871d483-8da5-3ae8-a8b4-684f102e260a | -11.15125 | -49.69794 | 2025-07-17 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b4ff090-91aa-3b17-904c-d5813098471d | -11.58187 | -47.30431 | 2025-07-17 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4416fc43-e93e-30d5-84d9-316dffbeea08 | -11.5859 | -47.30486 | 2025-07-17 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3da6d07-f5ee-3cf9-b17e-5a53dbdfb869 | -9.27299 | -50.26275 | 2025-07-17 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ae18696-60b1-3001-adf4-e456b1c823a4 | -10.56771 | -49.13723 | 2025-07-17 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fd066e32-a34f-3c51-be0e-376c15b88b95 | -9.41658 | -48.4125 | 2025-07-17 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e24230b-b076-3d4a-8fd8-ab08dc5b3139 | -10.68025 | -56.54449 | 2025-07-17 04:46:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 557a1165-fdbd-391f-8bf8-be4dc591cb47 | -6.85576 | -44.7687 | 2025-07-17 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 379655ac-be8e-359c-ba10-93f0b25efc99 | -6.54651 | -44.44929 | 2025-07-17 04:46:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 323e2796-0125-34f5-8747-a406248ada13 | -6.73189 | -44.33474 | 2025-07-17 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 09ffcd5f-f6ed-3795-a352-03a12e12ad21 | -12.413 | -50.04501 | 2025-07-17 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5395b2e7-ceed-3e4f-8a43-4d958336916c | -13.61633 | -47.93863 | 2025-07-17 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59b85d8e-14c8-37c4-ad1c-b1b3ce8f8a79 | -12.4785 | -46.91503 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5205c4bc-78ae-3222-86a8-14f89015f9b8 | -12.41649 | -50.04554 | 2025-07-17 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 86e9f669-f719-325c-a833-67c4e5102b54 | -13.06174 | -47.80768 | 2025-07-17 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 098b2392-7565-3ca3-a57f-c77caefa27f1 | -12.47326 | -46.92218 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c78aa6d8-31d9-3ddc-b599-37591e4f9054 | -12.47986 | -46.91389 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3da318a0-9ec4-3e2f-af6e-e2cfae54c0b4 | -12.99995 | -44.87616 | 2025-07-17 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 314d6cd7-c1b3-381c-ae69-3315c8959f69 | -12.49504 | -46.92804 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61181920-88ec-311d-8501-64453a9454ae | -12.43107 | -50.04373 | 2025-07-17 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4375b09-59e9-322f-a814-58689fac3b74 | -14.52047 | -47.67225 | 2025-07-17 04:49:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec418ef0-3790-3e88-b716-224476c15734 | -14.7497 | -46.29812 | 2025-07-17 04:49:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d78de9d7-6f01-3b4e-96e9-31bed488f490 | -14.31977 | -48.64968 | 2025-07-17 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7861162-7d13-3c0d-be58-53abcfe8ff1e | -12.48268 | -46.91564 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0705be0d-0e34-3b11-8a16-a25ba116eed8 | -12.50156 | -57.78582 | 2025-07-17 04:49:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a2ee4a67-bc50-375e-8dd0-218ceee7a44b | -12.37402 | -50.3821 | 2025-07-17 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0d3ef5bc-022b-3745-a7f3-74a02c3b7d43 | -12.47904 | -46.91113 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db65865b-4c6a-3f20-abc1-65e52935215f | -14.50985 | -47.68922 | 2025-07-17 04:49:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c869588-aee7-3c12-a7d4-aa813e43b3be | -15.87986 | -44.82162 | 2025-07-17 04:49:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48f5681d-382c-347a-9eed-ed86b95ca2ad | -12.49815 | -57.78152 | 2025-07-17 04:49:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7b5a7a2-ccb3-3ea3-bf78-62f3f8bd5b93 | -12.47582 | -46.93444 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecfc43fd-0dac-3d1e-8d96-a0f37cef699e | -11.87465 | -55.45197 | 2025-07-17 04:49:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 323f9579-b8ee-3e1a-83fb-6d05ff99d3db | -12.40507 | -50.48094 | 2025-07-17 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5306659c-f8f6-3744-8ea2-1af7ca3ce707 | -12.48771 | -46.91901 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b586227-9154-3dda-a43f-03f656022760 | -12.47732 | -46.93335 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6dc8a28a-482d-328e-9cf6-27ceb7de2a5a | -12.70902 | -46.8083 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1ad1d729-e867-3369-bec8-ca07b9a00095 | -12.48353 | -46.9184 | 2025-07-17 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84e37697-4ffc-30ee-8549-90bbdf96b8b9 | -14.25237 | -42.84368 | 2025-07-17 04:49:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 05941b56-8bfa-3baa-a98b-feff082e015e | -14.02052 | -51.22641 | 2025-07-17 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff71586a-e2ad-324f-817f-8240e8d24507 | -13.05779 | -47.80688 | 2025-07-17 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1fbeb649-dcb7-30c6-ad68-f7359afe0f21 | -13.02022 | -45.06422 | 2025-07-17 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README24.md)
