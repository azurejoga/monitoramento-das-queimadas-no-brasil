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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82be233f-f2d8-34dc-942c-d1d5eaa5af78 | -3.1859 | -49.247101 | 2026-10-09 00:06:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd8d5ca6-a1b5-3482-ac44-6e4265fa871f | -5.9822 | -40.965 | 2026-10-09 00:06:00 | METOP-B | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fcb11aa7-3232-3b1c-95e8-c1b62985f9cd | -10.8825 | -44.799099 | 2026-10-09 00:06:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8407b2fc-9a0d-396f-89a3-f0ab88493e1f | -3.2647 | -54.009399 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9e0f3db-aa41-3b42-8257-d1a6b0c6ce14 | -5.2433 | -43.987598 | 2026-10-09 00:06:00 | METOP-B | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d6588eba-17fa-3513-98a1-3b235d54f699 | -11.7914 | -46.770401 | 2026-10-09 00:06:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e96c1f4e-6209-3661-8bf2-eefa30a70c48 | -12.0407 | -43.450699 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4700fb5e-1ec2-30b5-9022-79814e596699 | -1.7398 | -52.248901 | 2026-10-09 00:06:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a045c10a-85e5-3af5-8276-05be7ebb03f0 | -2.5115 | -45.391701 | 2026-10-09 00:06:00 | METOP-B | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 96cd8a2b-b8bf-37fa-83a9-44d3635917f2 | -6.4619 | -46.027699 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f99ca239-76f9-3781-9d26-14c2fa9645a0 | -6.729 | -55.055401 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14a72ed6-f8e5-3a5d-a6f0-b7841a253e08 | -7.9027 | -54.7178 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0e0d5e9-ebdd-313e-b314-541c7882d044 | -12.9324 | -47.443401 | 2026-10-09 00:06:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a4c54ee3-b3a6-3164-aca3-7d1a559fcab8 | -5.7474 | -45.3494 | 2026-10-09 00:06:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d333228-ad61-38a4-9677-23d4042965d1 | -6.3944 | -55.258099 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84a829cb-41be-3c52-946b-d0f6a8fe79ce | -3.1886 | -50.5378 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2c5e878-cf48-3dbe-9083-ba00097eb1fa | -3.5337 | -54.667702 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 181eaa4e-56ff-370c-9673-16c5e2c07324 | -6.1471 | -51.9445 | 2026-10-09 00:06:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86e79388-3456-368c-93e4-f98d98891a15 | -15.9636 | -40.8302 | 2026-10-09 00:06:00 | METOP-B | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2b6626e9-6675-3b8b-a539-2a63d86a6e88 | -3.57 | -54.693298 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be6a3b48-bfd8-3076-8dce-c2b2ae5ea9e5 | -3.8475 | -44.139301 | 2026-10-09 00:06:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c54258a5-1559-3459-9bab-06b3ce939c88 | -3.0945 | -53.936901 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6834b408-6335-3a1d-befc-b30dfa88c3a8 | -11.8538 | -43.576599 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1955fdc3-b8d8-3c57-a189-8d47684168a1 | -5.9591 | -55.323399 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3ebcf33-bed1-35a0-8903-a673163a3a1d | -3.9221 | -56.0145 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10760b66-d72d-3f8b-aa42-1100448b51c4 | -5.7057 | -53.491402 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8ad3f84-e674-30c8-ac91-ca5645426f48 | -5.0908 | -42.646599 | 2026-10-09 00:06:00 | METOP-B | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aa789785-68fc-36ac-b3c2-ea1aaa648254 | -5.3443 | -45.167599 | 2026-10-09 00:06:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55370408-e4a7-3092-9116-d40a2323f030 | -11.0023 | -47.476601 | 2026-10-09 00:06:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b94e26e2-93a5-30bc-ac00-dcfd294466a3 | -2.987 | -54.099998 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63a29aa4-3f3f-3286-a87d-3f5992f3e630 | -12.9308 | -47.436401 | 2026-10-09 00:06:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b609c363-4e97-33e7-960b-c95441e5b7b6 | -8.3293 | -49.113098 | 2026-10-09 00:06:00 | METOP-B | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a75d247-1d3c-382d-8692-4680c71ac920 | -0.3976 | -51.779598 | 2026-10-09 00:06:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7ee41435-1122-3888-baf4-5117899f8526 | -13.1886 | -48.136501 | 2026-10-09 00:06:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1bc413a8-78b4-3dfe-a179-1aa3b9c952ea | -11.2541 | -46.2687 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1d6d2138-cc89-35e3-85b2-443ab8978204 | -5.6341 | -45.7939 | 2026-10-09 00:06:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64a5dc52-eccc-3526-9e3c-bf9e5636b54a | -2.9579 | -48.741699 | 2026-10-09 00:06:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fc21913-d228-35f1-acc0-df91e61d056e | -3.257 | -54.021099 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a42e6c13-5513-30d2-a326-f0961b0272d2 | -5.7092 | -53.460499 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f141cea6-29f2-3476-a10e-a795f4213ae0 | -2.8478 | -54.1203 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22670002-5af3-377c-b398-ef63cfc3578c | -6.7451 | -55.131001 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 920505c2-db2b-3818-aa10-d14155f9ada5 | -10.4249 | -47.293701 | 2026-10-09 00:06:00 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f788756-75b2-3829-9ec0-c069420a7286 | -4.6185 | -49.2001 | 2026-10-09 00:06:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9aa91204-071e-31d4-991e-d9c555c10bc1 | -6.5002 | -55.3708 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2a9f1b3-a9d3-35cd-8483-0fbf8efdd947 | -10.3692 | -45.121201 | 2026-10-09 00:06:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e4db2181-e45e-35a9-86ae-56d5a2fc74a4 | -6.4075 | -55.175701 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 228dfc80-a77c-3034-8fc2-50e761dbccba | -13.8071 | -44.185501 | 2026-10-09 00:06:00 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 71eefa2e-1645-3a7b-857a-92a45573ad40 | -18.383801 | -43.4632 | 2026-10-09 00:06:00 | METOP-B | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f5ce76e4-2a16-30c7-bf72-4c26a3c5651c | -6.7397 | -55.105701 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bddc31f0-3cbb-331d-937d-45ab7ae86787 | -9.91 | -44.791901 | 2026-10-09 00:06:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 186c98b3-264b-3c96-9165-62429e573dde | -18.630301 | -41.339802 | 2026-10-09 00:06:00 | METOP-B | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9c8b79b7-df01-3791-b077-355bf6eeaf06 | -11.0074 | -45.422901 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f4c16788-d506-34a2-96fd-f02a133713eb | -3.0521 | -54.207699 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ad197d9-98f0-3bfc-bcf3-f01f732e6aa1 | -3.5836 | -54.568699 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77a41f06-c8ca-3013-be0e-a7dfcb551909 | -13.209 | -54.186298 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f050250-0f28-3cf9-80e7-97bd5d0ef150 | -7.2903 | -45.4188 | 2026-10-09 00:06:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e6187fa-2382-35ac-83e8-f6781b60c257 | -2.5137 | -45.401299 | 2026-10-09 00:06:00 | METOP-B | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 305d1d16-be0d-33a3-b38e-42fc4c5a5593 | -5.099 | -45.665199 | 2026-10-09 00:06:00 | METOP-B | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a40c7c68-e815-39e1-8437-934afa384e2a | -9.2706 | -47.4333 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b6967da-0440-3b86-a275-9e8e8279f4a5 | -9.282 | -47.438 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 889ff1b8-6c21-3657-b5df-78df789fc606 | -3.1162 | -54.173199 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bf9b15e-dd2e-3062-b0ed-374822d9edc8 | -12.2218 | -57.080799 | 2026-10-09 00:06:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f626d07f-1777-3780-8a4e-d8be4ea64904 | -8.5598 | -46.894001 | 2026-10-09 00:06:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 024b0f4a-74de-3759-b8f9-84d7f3a5e406 | -6.4682 | -55.4599 | 2026-10-09 00:06:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84d2e35e-877c-39d9-bee8-bd1e3ad3c791 | -9.1324 | -45.840199 | 2026-10-09 00:06:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 624a829c-1a23-34cd-85fe-aebaf773a18f | -8.9992 | -47.737099 | 2026-10-09 00:06:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3e561905-3e91-3423-a4a5-65880b9fa0a5 | -3.2686 | -50.389801 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 969c108c-626b-342a-9682-7d88888f3ff2 | -4.5285 | -47.037399 | 2026-10-09 00:06:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c1af46d1-96f1-3d99-9bf5-1b4afe31860f | -5.6855 | -49.040699 | 2026-10-09 00:06:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64a1d8ec-b0e5-3de2-971a-c1df79581400 | -14.2517 | -43.660801 | 2026-10-09 00:06:00 | METOP-B | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e6368738-d4f5-36b1-8b4b-be48d2acc12f | -3.4483 | -59.533199 | 2026-10-09 00:06:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e7003a99-4f93-3020-a460-be56525c23ca | -3.022 | -54.0723 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 080ab258-26cd-30aa-8826-64c5999225ec | -8.3324 | -49.126999 | 2026-10-09 00:06:00 | METOP-B | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a32360a2-79b0-3c8f-b8a4-a5d5111666da | -11.6155 | -43.704201 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b8fdcfb1-39a6-36bc-b6cc-bd85c70e8526 | -13.1875 | -54.335602 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c18cf0b-0ff2-369f-8f3f-0a0453aa1c6e | -5.4901 | -42.854401 | 2026-10-09 00:06:00 | METOP-B | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0628dd03-7cef-3c12-8380-ca7e13cf03ab | -7.1968 | -55.143101 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e42db067-7ade-371d-a58e-e3af255e540c | -7.2288 | -55.149899 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7cfa2ff-6eb0-30f7-962f-c2abce978664 | -4.1273 | -46.8615 | 2026-10-09 00:06:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 08495f60-9f14-39e4-84a2-965f9f62725d | -11.6545 | -43.694599 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d6f52327-1fe7-3658-be08-1f0262220872 | -2.939 | -54.160999 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40eb2998-128b-35bd-a81b-53fa5602f327 | -3.8866 | -58.936298 | 2026-10-09 00:06:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a13c1ef5-89e8-3313-82d6-62f3a5b52307 | -4.7938 | -45.771702 | 2026-10-09 00:06:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fcaec75d-652a-358c-8580-8e651d295c27 | -11.7881 | -46.800999 | 2026-10-09 00:06:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eab4eedf-a77d-3cad-a68d-ec4796cb1a93 | -16.5135 | -42.518902 | 2026-10-09 00:06:00 | METOP-B | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c8512f69-617f-377d-a8d7-a58204f4b145 | -5.6968 | -41.740101 | 2026-10-09 00:06:00 | METOP-B | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b6d39c2d-6e3c-3f55-a199-bbb67ceada0c | -8.0422 | -49.395802 | 2026-10-09 00:06:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 077b0fd4-830f-3a75-8b02-75e3062a96d3 | -8.3012 | -45.727402 | 2026-10-09 00:06:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0fe5c820-17b2-3f0c-a756-1c3d58ca4981 | -2.4588 | -56.0606 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a430e3d-fa0d-38f1-9780-1d5c9ce981ee | -2.2174 | -55.436401 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fb25f0b-5c6e-37c5-9912-0ad78588bf78 | -4.5066 | -43.613899 | 2026-10-09 00:06:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1bb75b83-8630-3698-a20f-e7f8b2cdac5c | -3.435 | -54.546398 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd36a4f6-54d6-3005-8ea1-1628ae841be1 | -2.7763 | -54.075802 | 2026-10-09 00:06:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8953f66c-a821-30a4-b205-11513cf886b1 | -3.0339 | -54.0797 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b6a3341-ef63-39fc-99ca-ea66779b7e0f | -7.259 | -48.066399 | 2026-10-09 00:06:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ddcb6650-6fe4-301a-9b7e-e53fec9ee54c | -11.3974 | -47.5835 | 2026-10-09 00:06:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f58fbc58-d333-3279-a0fe-78599afd80ad | -13.3424 | -43.9688 | 2026-10-09 00:06:00 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e13c1480-0b0a-398c-8976-d0a6893343d5 | -11.7599 | -43.5299 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2267fb74-9e16-3a99-8cf1-45cbd9500b07 | -0.9998 | -47.6548 | 2026-10-09 00:06:00 | METOP-B | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d02903a-843a-34c3-8162-2420179c5e69 | -9.8659 | -47.466 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README13.md)
