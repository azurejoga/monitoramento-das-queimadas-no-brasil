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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4924da4-fa8a-32a0-92d4-1c1f85a1d957 | -4.60523 | -43.3185 | 2025-07-19 12:29:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| db6b8495-3500-3cd1-891f-6bab481faecc | -2.90388 | -48.24464 | 2025-07-19 12:29:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| f82268e2-271c-341f-934e-1ff8e5c12661 | -6.17156 | -48.04981 | 2025-07-19 12:29:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 826244e1-75bb-33a7-bc29-3421e72458c5 | -4.02862 | -48.06528 | 2025-07-19 12:29:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bf8864c1-5969-3b51-b6cb-13e80d4016e1 | -1.92673 | -47.40042 | 2025-07-19 12:29:00 | TERRA_M-T | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 18318889-1c09-3b26-be9f-865d78be22cd | -8.99475 | -49.65582 | 2025-07-19 12:29:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2be98fe2-8c91-3b0b-949d-0f7e6b03455f | -9.45083 | -46.87341 | 2025-07-19 12:29:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8acd8c43-376c-3fd5-a12b-a45f424b57b4 | -10.03517 | -46.31698 | 2025-07-19 12:29:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 9f16a634-6ae9-35e0-af22-b35d2f10e5b5 | -8.26836 | -46.08757 | 2025-07-19 12:29:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 563b16be-1ae3-32bd-a27b-686cdb11e0b9 | -2.92277 | -48.23831 | 2025-07-19 12:29:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 11944f8e-6dd9-3042-8c36-86fc3b99c129 | -5.25264 | -48.60105 | 2025-07-19 12:29:00 | TERRA_M-T | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 8da4a65b-ee26-3ab5-bebf-fd9b51d6cc09 | -3.12638 | -47.01101 | 2025-07-19 12:29:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| fed25da2-9e6f-35cd-aec8-a5917477ddc6 | -6.18066 | -45.87267 | 2025-07-19 12:29:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fc785f2e-0c21-3f50-85dc-40bf832d776c | -3.92624 | -43.16352 | 2025-07-19 12:29:00 | TERRA_M-T | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7d0249d3-c2b8-3060-aaa0-f6df644fab81 | -7.83697 | -44.20808 | 2025-07-19 12:29:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 176036a7-eb0a-3bf2-a67b-d536fe5d451b | -6.16273 | -48.0486 | 2025-07-19 12:29:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 8f52ec96-415d-3d06-8429-8860d337f38e | -8.46435 | -48.39919 | 2025-07-19 12:29:00 | TERRA_M-T | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cac22cbc-fd86-352f-9669-81e21986b371 | -4.52118 | -42.07426 | 2025-07-19 12:29:00 | TERRA_M-T | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| aa906c7a-7942-3b6d-a9f0-c5bb94e035dc | -6.83694 | -45.32939 | 2025-07-19 12:29:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3e523431-580b-3b3f-b916-634c15c3b1eb | -8.33434 | -47.49577 | 2025-07-19 12:29:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8fa851c1-9243-3900-acee-0e4df6d7aa1b | -6.75055 | -45.51118 | 2025-07-19 12:29:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 364c7bb1-ec6c-3d56-94b1-dfabf60bcb33 | -8.45093 | -46.02271 | 2025-07-19 12:29:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 117db1cc-faee-33d3-8b9d-82fad79bd964 | -4.77876 | -45.35263 | 2025-07-19 12:29:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 849c9a24-ed1d-39e7-aa32-e2dba79b019a | -3.8341 | -47.74233 | 2025-07-19 12:29:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 78d996d8-3f44-3ab5-86d9-73abc887b8df | -7.36546 | -49.62013 | 2025-07-19 12:29:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 277ef6a0-050d-3766-aa62-cc5c0a979d6f | -7.0642 | -44.07134 | 2025-07-19 12:29:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 9c8d4d32-c3cc-342d-9c46-4a70bdbd0780 | -6.83851 | -45.31786 | 2025-07-19 12:29:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 7b73d90a-b3cf-3992-80f6-e092b202da31 | -6.749 | -45.52235 | 2025-07-19 12:29:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| aeb3055e-d9be-3b7a-aed4-8ab670013806 | -3.10859 | -47.00856 | 2025-07-19 12:29:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 620991da-6316-327d-8c5f-4176bd213b4e | -6.05719 | -49.85595 | 2025-07-19 12:29:00 | TERRA_M-T | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 667f8f8c-275c-3950-b945-605714d37985 | -6.79177 | -43.00726 | 2025-07-19 12:29:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| c3b22cc1-59f5-32af-b064-d1f91102cce3 | -8.01124 | -43.67543 | 2025-07-19 12:29:00 | TERRA_M-T | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 26.8 |
| c199cff3-8632-36da-accf-9d112605b8ed | -3.04536 | -49.4308 | 2025-07-19 12:29:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2b74a277-c390-392d-bdeb-fa104e0b5316 | -8.70983 | -47.18214 | 2025-07-19 12:29:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| de1b1ec2-50fc-36b5-a791-a930b681b5c8 | -5.6542 | -43.71314 | 2025-07-19 12:29:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 72832191-bbac-3959-9fc5-e05c8a691260 | -8.98722 | -49.64564 | 2025-07-19 12:29:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| b9041e74-5e6f-3499-8f69-0b92e6518eaa | -3.09866 | -46.7589 | 2025-07-19 12:29:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b17c125d-b4d8-38c3-ad1b-20df6d09ef1a | -6.52436 | -43.64057 | 2025-07-19 12:29:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3cf1e13a-5590-3cc6-b959-7721d7a7fba0 | -7.48478 | -47.5034 | 2025-07-19 12:29:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fcee3c73-3198-3826-bf0c-e839d7101b62 | -7.06453 | -44.84985 | 2025-07-19 12:29:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 84eba737-c8dd-3e65-ae06-ec8e18531d5f | -6.15658 | -47.76083 | 2025-07-19 12:29:00 | TERRA_M-T | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 69a7a992-7ced-366d-9054-1c34d5ec9281 | -8.98592 | -49.65455 | 2025-07-19 12:29:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 9cfce0b8-0ef5-300b-91c6-f8f20dfa5b6e | -6.69377 | -43.05829 | 2025-07-19 12:29:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 14950002-9508-3ef0-9fde-4df14dd45cfb | -10.7261 | -46.7782 | 2025-07-19 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| f64e044f-8a82-368f-8f04-f629011457c6 | -3.1198 | -47.0075 | 2025-07-19 12:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| c98ff4fb-fe06-33a1-94da-efc699292b39 | -10.7257 | -46.8006 | 2025-07-19 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 28269dd0-bf0a-36ff-84b0-c9495c1ffd7e | -10.72753 | -46.78402 | 2025-07-19 12:32:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 85a9655a-054d-3905-9680-532a7d8db6b4 | -16.42822 | -43.72284 | 2025-07-19 12:32:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 148457b4-2720-3b62-80c5-4758948d1be5 | -10.71641 | -46.79355 | 2025-07-19 12:32:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 12116698-0dfa-3e09-813c-cfde430cf41e | -13.83116 | -50.60886 | 2025-07-19 12:32:00 | TERRA_M-T | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 6e780d03-f181-3c28-b334-7d671cbe66c8 | -10.71493 | -46.80437 | 2025-07-19 12:32:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| ea9942b7-dd1d-3ce8-96f0-adad816e4c4d | -10.72604 | -46.79487 | 2025-07-19 12:32:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| f8f79783-1ae8-3141-85b5-c45467d06883 | -13.82233 | -50.60754 | 2025-07-19 12:32:00 | TERRA_M-T | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 28.2 |
| ae27c136-628f-32e3-bcdf-39b965e51474 | -10.71347 | -46.81507 | 2025-07-19 12:32:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f261462c-e720-3ac3-901e-e04818200486 | -14.69374 | -45.06016 | 2025-07-19 12:32:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 24cd98b4-e08d-3850-bdfb-0acb4763d65d | -11.73165 | -48.18216 | 2025-07-19 12:32:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 51d66ba5-f78f-3046-9adb-f31b6f2fb561 | -11.73032 | -48.19173 | 2025-07-19 12:32:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 9ee0ca36-027d-39d6-8c6a-6e7feb49052d | -10.71789 | -46.78273 | 2025-07-19 12:32:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| cc3dab8e-1b93-33ff-b421-b9802c2b37d7 | -11.82887 | -48.21198 | 2025-07-19 12:32:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3eaac9ec-9c19-3a0b-8a59-5a1835a931c5 | -10.70385 | -46.81376 | 2025-07-19 12:32:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 3ffb6ce7-9382-32aa-a499-721db59e1015 | -12.99648 | -46.94048 | 2025-07-19 12:32:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 655003ac-0a7f-3483-9287-c12cb6122142 | -15.38381 | -51.5962 | 2025-07-19 12:32:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b68a514b-9985-366a-acd9-211f83dd2595 | -15.3852 | -51.58685 | 2025-07-19 12:32:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 535bc1ea-8d3b-3584-984b-36946402492f | -14.70534 | -45.06165 | 2025-07-19 12:32:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| d22ad5ec-e3dc-3690-bd7c-9ff87d0e1161 | -10.85893 | -47.16809 | 2025-07-19 12:32:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| c75dd2e2-f7af-3fcb-959a-d0df1dac6591 | -12.377 | -50.33036 | 2025-07-19 12:32:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4f426bc5-5087-3182-b508-a20250c1b815 | -11.7394 | -48.193 | 2025-07-19 12:32:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6f667e4c-d4f7-38a4-bc3d-28e58740f8d7 | -11.54284 | -47.87849 | 2025-07-19 12:32:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 33.6 |
| d9fb9ec6-0196-3cb1-82fc-35d575f26b79 | -11.49253 | -47.31817 | 2025-07-19 12:32:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4b48f9c1-f927-34ea-a4a8-b85f6693bee6 | -11.83803 | -48.20953 | 2025-07-19 12:32:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 0e454a38-8844-3604-9456-0b29df1d7668 | -18.40495 | -44.17563 | 2025-07-19 12:32:00 | TERRA_M-T | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 18.9 |
| d20192af-ff47-3ec3-af82-cb65bfa2fcbd | -12.36817 | -50.32906 | 2025-07-19 12:32:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| ecb3233c-0937-3ca2-bd8d-2ba1ed6138b8 | -14.78223 | -48.28813 | 2025-07-19 12:32:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bdde0759-bc6b-316a-9562-80789e816d34 | -10.68038 | -49.67467 | 2025-07-19 12:32:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 4a678a49-cc30-3704-985a-707307932930 | -10.88659 | -47.1463 | 2025-07-19 12:32:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 5abc7aa7-7451-3ae9-9d87-6a9bfeba071d | -10.68167 | -49.66577 | 2025-07-19 12:32:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 680d2702-5bf8-36d8-a73e-4ce675d1c19e | -10.62067 | -44.75747 | 2025-07-19 12:32:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d2e4d302-eea3-30d1-96b7-09ce60346f5d | -10.70531 | -46.80305 | 2025-07-19 12:32:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 8c614589-1d09-3c4b-ba09-9c858471cf77 | -11.48166 | -47.32724 | 2025-07-19 12:32:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| fb72b735-7951-3884-a3a6-01e80338eeb4 | -14.70734 | -45.04535 | 2025-07-19 12:32:00 | TERRA_M-T | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 5abfa727-594f-3617-9f1e-392457569fcf | -10.57428 | -49.12897 | 2025-07-19 12:32:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a4f79d17-7fa3-3e1e-a4fb-f409a01d6c8c | -11.48309 | -47.31689 | 2025-07-19 12:32:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 18469f44-c77e-3efa-a815-51fd33377ff1 | -11.54417 | -47.86875 | 2025-07-19 12:32:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 2969eb14-68c9-3cf1-8732-64379f5418b3 | -10.80227 | -46.76716 | 2025-07-19 12:32:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| bc08f52a-0525-3d3d-bb84-0cf9927ce98d | -18.40267 | -44.19747 | 2025-07-19 12:32:00 | TERRA_M-T | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 29.3 |
| b82f2541-7c6f-3ab9-b24b-7e7938920bd5 | -22.94571 | -52.76934 | 2025-07-19 12:34:00 | TERRA_M-T | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 79296f7c-caf6-3f93-b11f-3b3a577745f7 | -20.35621 | -42.275 | 2025-07-19 12:34:00 | TERRA_M-T | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |
| 3ceb14f2-4948-3845-b6b8-c1d80d07aca6 | -21.53304 | -46.15236 | 2025-07-19 12:34:00 | TERRA_M-T | SERRANIA | MINAS GERAIS | Brasil | 3166907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| d57f7944-60af-34f0-a97c-d6e7c65a80d3 | -21.53956 | -46.16002 | 2025-07-19 12:34:00 | TERRA_M-T | SERRANIA | MINAS GERAIS | Brasil | 3166907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.5 |
| d935b11e-32d4-3c9a-8d88-a738a1f05b58 | -19.98849 | -47.17442 | 2025-07-19 12:34:00 | TERRA_M-T | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ee3e66cb-f0c1-3781-9d59-5d94ef1a0225 | -19.019 | -54.65865 | 2025-07-19 12:34:00 | TERRA_M-T | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 9a61a760-0f5b-3efe-a633-4a06bfb454d3 | -21.53109 | -46.16985 | 2025-07-19 12:34:00 | TERRA_M-T | SERRANIA | MINAS GERAIS | Brasil | 3166907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 42.7 |
| a3efe5a3-7f91-382a-bb0f-9cd2d2cb4940 | -10.7261 | -46.7782 | 2025-07-19 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| e025aff3-7dd0-37f0-b1ee-6e91d156393c | -10.7257 | -46.8006 | 2025-07-19 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 191.6 |
| b4f5ed74-1bc8-3fea-bad7-8c756a2a287c | -10.7257 | -46.8006 | 2025-07-19 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 180.2 |
| bf36a182-93a9-32e2-8869-70b0c3395806 | -3.1198 | -47.0075 | 2025-07-19 12:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 8fe4bbae-1116-3931-bda2-bd7d15584dae | -10.7261 | -46.7782 | 2025-07-19 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 9febd0c8-90e2-333e-b6bc-22259e61616b | -7.849 | -44.1941 | 2025-07-19 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| b2e75f69-c035-3db9-a6a4-5b47184b60b1 | -7.849 | -44.1941 | 2025-07-19 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 396dc38e-3b59-31c0-94a3-816db3c68fe1 | -10.7261 | -46.7782 | 2025-07-19 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |


[Clique aqui para ver as próximas entradas](README32.md)
