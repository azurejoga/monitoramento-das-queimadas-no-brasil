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
| d153dee2-cac5-3582-9c7c-66e98c68cbdd | -5.91507 | -43.86214 | 2025-09-24 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| de8efdcb-093d-31da-8ecf-efa4798f4417 | -9.1072 | -48.90028 | 2025-09-24 04:51:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6a0c396-177d-3d7b-8564-6a87bfeb7d41 | -8.18156 | -46.36233 | 2025-09-24 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ef36ca1-a7a7-3747-8c04-9dc1a716061c | -10.88268 | -53.73943 | 2025-09-24 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2718c21d-989e-3e9b-b733-4b688d25ee3a | -5.51828 | -43.86841 | 2025-09-24 04:51:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 910c9681-7132-3afd-97ee-bd9ecde79e42 | -4.31672 | -48.09121 | 2025-09-24 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 5142e399-25e2-3040-bd70-cd695bce3415 | -7.37303 | -47.03048 | 2025-09-24 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b844e7bb-e91f-3a86-b81a-3fd54a73c2da | -7.28953 | -41.86592 | 2025-09-24 04:51:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 310ff981-c9eb-393e-af46-28232446251c | -8.31758 | -46.22156 | 2025-09-24 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11b40ad9-827b-3112-883c-ef2eace54411 | -9.73298 | -46.66426 | 2025-09-24 04:51:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ae7183a1-a1e1-3e85-9e59-944cefc1774e | -11.52225 | -43.6657 | 2025-09-24 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9fa44e87-687f-3958-bde1-da23138999f2 | -6.53213 | -44.22361 | 2025-09-24 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60a667fe-1b35-3c79-bb6e-8bc773b047e6 | -5.73747 | -43.79721 | 2025-09-24 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9874399c-8daa-3b37-b76d-cd1eba78ea75 | -5.76175 | -42.60032 | 2025-09-24 04:51:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 770ccf46-fbc4-3644-b478-b688c27feab8 | -5.49388 | -39.16935 | 2025-09-24 04:51:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 13edcce9-dd49-334d-9a78-2311b325db51 | -4.48759 | -47.68039 | 2025-09-24 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 604f3556-2329-3387-a996-449eaef794e4 | -5.6452 | -43.91565 | 2025-09-24 04:51:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e3eaa70e-4c9c-3b8e-8d39-d1cd5bf2017a | -11.52522 | -43.66328 | 2025-09-24 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f190540-2693-334c-ae71-66588e5d80c6 | -5.64524 | -43.61017 | 2025-09-24 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc9a36f5-1ced-3eff-adb5-2eb4e97189aa | -10.94861 | -45.59634 | 2025-09-24 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 690764b5-adca-3c32-910b-0678bb6dfc6a | -10.0976 | -55.86275 | 2025-09-24 04:51:00 | NOAA-21 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb7fd972-3124-36e6-8dd4-c02bb1688b74 | -6.07816 | -42.82777 | 2025-09-24 04:51:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 873d4e69-0717-3955-b846-1e93186f3706 | -5.88682 | -49.64127 | 2025-09-24 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b355c4d-e268-38e6-8c28-ce67f8ce6098 | -4.33428 | -48.38629 | 2025-09-24 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fefce4b-2a5a-3718-a55c-e8346e696413 | -4.10742 | -51.08027 | 2025-09-24 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 11dbecd2-c150-3567-aecc-0623ec31227b | -8.54841 | -44.96033 | 2025-09-24 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a02f9662-934d-32f3-8cfb-7feff6fc2342 | -5.73703 | -43.80039 | 2025-09-24 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 047b416e-53ed-328c-9d07-4cb89b6c3045 | -5.3832 | -47.21252 | 2025-09-24 04:51:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70c6ea59-afa2-3a01-8240-276d7f29f8b7 | -5.92709 | -43.92549 | 2025-09-24 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 395c2a05-b870-3790-af05-81a58a101df3 | -12.0601 | -44.81692 | 2025-09-24 04:51:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4bae9fa-5116-30a3-8941-82dac78ecad5 | -8.18039 | -46.37085 | 2025-09-24 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef0c2192-c666-30be-af40-ae22465f633f | -5.63745 | -45.95325 | 2025-09-24 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3355937f-af60-3068-a061-44d530bb4d95 | -5.36577 | -47.21753 | 2025-09-24 04:51:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e11c67fe-a620-3ddd-8f3a-6556bfc34864 | -4.29442 | -48.26274 | 2025-09-24 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e50d063-755b-3f08-9517-0d7b518552c2 | -5.94531 | -45.39591 | 2025-09-24 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 195404bb-8080-3550-93ad-d733c20d24ed | -5.17659 | -46.12415 | 2025-09-24 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 284ef1b5-b62c-3320-a912-1e5c448b5b23 | -10.29025 | -45.23349 | 2025-09-24 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 783a826b-5bb1-35cc-9cce-19898125f04c | -11.69995 | -44.35897 | 2025-09-24 04:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 073d87d4-261f-3eac-b754-74635293d33e | -6.53251 | -44.22087 | 2025-09-24 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21d78902-ccc1-3ceb-aab2-fcca4e51fd9a | -5.49646 | -43.98777 | 2025-09-24 04:51:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32d277d4-3795-38d8-b3d7-7e457e90325f | -6.32394 | -43.62497 | 2025-09-24 04:51:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6b0879f7-e4aa-3124-bfff-3b37e2b7a749 | -5.63141 | -45.72364 | 2025-09-24 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bdccd5ce-072b-380f-a6bc-767ef4fcb5c7 | -11.02846 | -45.9054 | 2025-09-24 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c3199f8-50a3-30a3-b8e9-b8a0fed2115e | -5.17748 | -46.12181 | 2025-09-24 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 896fb0cc-9b5b-3f49-a7d7-1e9c513e9a10 | -6.49763 | -43.26136 | 2025-09-24 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 89d9ac51-e628-38a8-addb-f584fefe8156 | -7.7831 | -46.19231 | 2025-09-24 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f6505c69-1464-31e8-b808-6a3cabc61cb4 | -4.20625 | -55.15428 | 2025-09-24 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 261afbdb-92b8-36a2-88bf-b69b6527f894 | -4.82505 | -46.0063 | 2025-09-24 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac9f9086-0815-37ed-8d4d-ae14066bf801 | -6.41973 | -43.08948 | 2025-09-24 04:51:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 53ee156a-6bb9-3bfc-8d6a-eb32b7273191 | -11.51952 | -43.66267 | 2025-09-24 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f139e958-2ebc-3186-89ca-6dc89938b56e | -7.27217 | -42.98739 | 2025-09-24 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 24706fab-5951-393a-ac89-f0e51ea6819d | -5.76096 | -43.96889 | 2025-09-24 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9586689-769b-398e-9b78-522a43d5a03f | -8.54682 | -44.97196 | 2025-09-24 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb0f4e23-800c-3121-89ce-b255bc42f863 | -5.76891 | -46.76291 | 2025-09-24 04:51:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed372769-6da1-3f3c-93d2-e7a076cce1cb | -5.92098 | -43.93128 | 2025-09-24 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51b76be2-c264-3ae8-ae65-36d4813fc33b | -10.9753 | -52.23374 | 2025-09-24 04:51:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef90111a-e986-372f-9601-44404d3f9d31 | -6.11261 | -41.79314 | 2025-09-24 04:51:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a72eaa84-21ca-399b-b7e9-3fce9b1404a3 | -9.24455 | -44.49409 | 2025-09-24 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2278c000-8c20-3bf8-99dc-64dd15e334a5 | -11.42425 | -44.94408 | 2025-09-24 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c5e8142c-a0bd-328a-8b55-9e0863c17565 | -6.32349 | -43.62827 | 2025-09-24 04:51:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e5d2a7f7-96af-3152-a8ce-b4d6a9e39e46 | -9.58951 | -46.43832 | 2025-09-24 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d1dfadc2-81ec-38c2-9f85-a41dcc3b399b | -8.5289 | -45.02869 | 2025-09-24 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 02e7d81a-52ad-3db8-866b-4a61cbc12449 | -8.17016 | -46.24152 | 2025-09-24 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f44b93f-ea4a-3b8f-8ce2-1c5360bbf36d | -7.64893 | -46.01013 | 2025-09-24 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d9072f6f-1f47-3672-bc5d-a03d0972d836 | -5.85026 | -42.64919 | 2025-09-24 04:51:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 840acfb1-8f3c-3fdb-8588-8409357ec709 | -9.45673 | -48.90466 | 2025-09-24 04:51:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd4c5af3-bec0-3d99-a5a9-dfefe8b23f1c | -7.26864 | -43.01383 | 2025-09-24 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a6c20f27-81ff-3a90-8d50-8e2eb0f0f79d | -5.63527 | -45.729 | 2025-09-24 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fc83eb44-68db-35b5-b31a-d3cdec59cb66 | -12.05971 | -44.8201 | 2025-09-24 04:51:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31d0b257-00c5-323c-8c57-8533367be763 | -10.29646 | -45.22502 | 2025-09-24 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d83c81fb-8515-3959-82db-203f474adffe | -9.10718 | -49.77912 | 2025-09-24 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73a22038-8cf5-3c21-bc30-592d0b3b7fb8 | -9.73558 | -46.66749 | 2025-09-24 04:51:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5ef98d21-8146-36d8-b235-1015f9a383c9 | -7.37729 | -47.03109 | 2025-09-24 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4e4a0249-11dc-3406-95af-d0850f6dd69e | -5.24857 | -43.72038 | 2025-09-24 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ab697fe3-69f1-3a54-9abb-5409cd864eab | -8.52132 | -45.00978 | 2025-09-24 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45498c34-7530-365f-b386-f5fbb3a6a454 | -10.58254 | -44.07851 | 2025-09-24 04:51:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 760c70c5-0961-36d4-8577-93ae5cdd189a | -4.31981 | -48.09644 | 2025-09-24 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6c66fae-60f5-3123-8fac-5b6252bd1916 | -10.29606 | -45.22813 | 2025-09-24 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2841ffb9-2226-3d24-b126-c53103727cc0 | -10.302 | -45.22181 | 2025-09-24 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 62630c43-02e1-3c74-800b-abeaa1647082 | -9.26847 | -46.6286 | 2025-09-24 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6267d107-afb7-3b20-8cf2-cc1712e503a8 | -6.56359 | -43.83086 | 2025-09-24 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c54fe74-2469-3a52-9a95-91b17cede613 | -8.11464 | -49.99215 | 2025-09-24 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ab4d97c-299e-37c0-b119-b2950f5143e9 | -7.37245 | -47.03453 | 2025-09-24 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 760b612c-4a8c-36a2-9fc7-7b9a69734de0 | -7.26305 | -43.01294 | 2025-09-24 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 97c1c3fd-8587-34c2-9227-4d8b5c35a1e6 | -5.64003 | -43.91506 | 2025-09-24 04:51:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ec11318b-859d-367e-a2c1-fc03c2a3ed05 | -5.37284 | -50.90209 | 2025-09-24 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ad46463-994a-3431-9695-0a5e557a0698 | -5.64571 | -43.60696 | 2025-09-24 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53bb2a8a-663d-36e9-87dd-1689d7b90277 | -7.38039 | -47.03976 | 2025-09-24 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26d1b063-2ca7-33e2-962d-f679de87aba4 | -7.77858 | -46.19154 | 2025-09-24 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9f804206-2327-3e0a-be26-ebed6d5309a9 | -5.78474 | -42.55989 | 2025-09-24 04:51:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 271664c7-ba97-3279-9107-6f26a33a5112 | -5.91792 | -43.93016 | 2025-09-24 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db2335db-1ca3-3447-8e92-bf24652eff80 | -10.27582 | -54.26414 | 2025-09-24 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ccdeae4-b856-3b48-9e52-940c02a70bbb | -9.45285 | -48.90399 | 2025-09-24 04:51:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a07c671-d3d1-3d3e-b5e5-136f357d0679 | -5.9231 | -43.93077 | 2025-09-24 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac0fbcc2-136f-34bf-a29c-7439d4b69cc8 | -7.17618 | -42.23952 | 2025-09-24 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9d3138ee-a122-3bfa-82bb-9822861c8660 | -10.88323 | -53.73594 | 2025-09-24 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7178167-30e5-30dc-8799-e1519b388ce8 | -11.67516 | -44.38093 | 2025-09-24 04:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33b1d314-6877-325a-8de4-371287fe4f83 | -10.58392 | -44.06769 | 2025-09-24 04:51:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1232ff7-c142-3ba9-96f6-ac05d5af7f22 | -5.42739 | -41.32092 | 2025-09-24 04:51:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c03021f9-b910-3122-af75-60d61946a568 | -11.52127 | -43.67348 | 2025-09-24 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README17.md)
