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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fafb8d16-aa09-3aac-8321-95080c8cf5cb | -10.5174 | -43.39251 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2db42f2-90b5-3da1-85ea-4900cba6ea02 | -8.24978 | -44.01936 | 2025-10-17 04:51:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d089c33-27e7-3482-a612-90372889befe | -8.2402 | -44.01809 | 2025-10-17 04:51:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5ac1d34-4646-3b5c-b87f-de99e04f37e5 | -10.66213 | -44.85945 | 2025-10-17 04:51:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce12ff87-d035-33ca-888d-6d6577c6ca93 | -11.13848 | -45.84435 | 2025-10-17 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ce2df96-73c5-37ee-bc19-164eb97663b6 | -9.15616 | -46.62769 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 132e4a0a-f38c-3b4d-961b-85c338c7e29f | -14.92081 | -46.72194 | 2025-10-17 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab6f031f-5099-3905-b02e-7a1a5e225a43 | -8.07548 | -49.89206 | 2025-10-17 04:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b80647e3-ecea-3d1c-9b55-007d5c16a2e7 | -12.16074 | -45.07019 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90a24c27-e22b-3ba1-913f-3f994e58e263 | -9.98148 | -47.01082 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 70b362dd-9e7f-3997-984f-f46a3c42ed3b | -14.91539 | -46.72931 | 2025-10-17 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1ae3c8fb-329f-33b2-b9b7-6762fe01ded1 | -9.01722 | -46.61771 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b987c966-d3e3-3833-b3d8-3cccf411dd15 | -9.31274 | -47.67959 | 2025-10-17 04:51:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 284e5713-aff9-3b67-b86a-f2bf4adccfb6 | -8.96675 | -48.42796 | 2025-10-17 04:51:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 055a5ac9-be7d-3dc9-9379-7f3b1b9220a0 | -12.42757 | -51.29867 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1aaee8c3-3c92-3813-9d22-9b78e84bac7f | -9.05444 | -46.98964 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f145ac9b-ee8d-3a8e-9458-06926a672da3 | -10.28303 | -44.04743 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4023ebed-8c7b-3082-a4e9-49ce97e6ddd2 | -11.47742 | -44.27951 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4b4af3c-ca8e-347d-848f-8d13275cd827 | -10.65013 | -45.25368 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d7e59ff7-b063-3945-896f-3685becfb807 | -9.36585 | -46.98613 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c43d836-0fd4-3086-92c8-234ace52e550 | -12.41017 | -51.29963 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| d33b3358-701e-39e5-a92b-4d78ea4b3408 | -10.43544 | -45.02229 | 2025-10-17 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 9be3d49c-886d-3c83-8276-cd28ef3fe37b | -10.25985 | -44.03371 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2b3ab286-339e-3ea8-a106-30effd90b5ef | -13.23528 | -47.11358 | 2025-10-17 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d31c5655-a359-3c2d-93c9-76b4197c9379 | -11.96817 | -46.555 | 2025-10-17 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f64f393f-a114-3554-8076-c803ffcea320 | -8.6808 | -47.00988 | 2025-10-17 04:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32848a8f-7881-3762-8d62-06e646983531 | -8.93608 | -45.2444 | 2025-10-17 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3e56ead-13ee-352c-a4c3-41ff6ae9508d | -7.80735 | -47.91562 | 2025-10-17 04:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2866c03c-dfbb-3a25-bf3e-a3fc2cb1cd7b | -13.24459 | -47.10761 | 2025-10-17 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 48aa4e15-0aeb-3b83-bf2e-197cc03c40c5 | -8.36472 | -44.77535 | 2025-10-17 04:51:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cbf59a42-92ca-3366-b15a-334b69cc0958 | -11.45172 | -47.29306 | 2025-10-17 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f2fe25c-e5ef-3237-a349-41f7eb4dcf41 | -12.16417 | -45.06765 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49f04588-4fc8-30cc-9733-3e398d55f00b | -10.5062 | -43.43819 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ca130b2a-8f90-318d-b585-3b0d85522ae9 | -10.25831 | -44.04503 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 62599a63-3099-3add-963c-2284b762c77d | -12.44722 | -51.30552 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e53d2964-558c-3537-8f4e-01aec7da1a00 | -14.33463 | -51.43677 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d7437f8e-5fa8-3e31-8432-1ff388fc50cf | -11.39725 | -44.22803 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8dc73ce7-fb0f-375c-9c33-9f99ab5b19d7 | -11.1866 | -51.7576 | 2025-10-17 04:51:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a641ae9-7a5b-3bae-a81b-0a25ffa98f03 | -10.87645 | -55.9935 | 2025-10-17 04:51:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc2b5b45-1d65-3603-b278-e97fe0b3a922 | -10.85299 | -51.29105 | 2025-10-17 04:51:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4f59930a-eb03-3b69-9815-29aae7fd1758 | -13.25301 | -47.13918 | 2025-10-17 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6a2cac84-785a-3e1b-b4e1-0a80600a0770 | -9.70147 | -44.56686 | 2025-10-17 04:51:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5712c61e-fdc9-3df1-bc83-49190433b3af | -10.11438 | -44.5603 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1beb1355-af67-30de-bceb-bfedcc95fa97 | -9.02126 | -46.61841 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1903093a-ed12-3e85-a810-15a118539196 | -9.14237 | -46.63697 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3334c996-91c6-3c71-9fee-e03cbe595b13 | -8.39652 | -46.24467 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1267d8f7-02ca-36e5-9537-b8d9f6645d2d | -8.49615 | -48.49168 | 2025-10-17 04:51:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b09fe4e-594e-3b08-a475-47a288412672 | -8.87001 | -48.87863 | 2025-10-17 04:51:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3041d644-f533-3d54-8b7f-8ad051d642f4 | -10.11212 | -44.62161 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d1404b4-1cd5-354e-8a17-20e2bf9f4c7a | -8.16691 | -46.06758 | 2025-10-17 04:51:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87edb362-b951-3004-bb3b-573c610f2904 | -12.31136 | -47.25698 | 2025-10-17 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1ae7f08-52ff-32ff-804b-c98964d3111f | -10.10458 | -56.77091 | 2025-10-17 04:51:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b85a80e2-9c4e-3c3e-8fa1-240c3197253a | -8.40786 | -46.28271 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9073be91-5292-3996-b2ef-7fe8b58c0886 | -12.60268 | -56.50947 | 2025-10-17 04:51:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ccef7e47-7c95-3fa2-9273-d5204199dd92 | -10.09925 | -44.60995 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e58244e1-45bd-3dd5-a6d5-eb5ce32d1922 | -14.91483 | -46.7335 | 2025-10-17 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e4ffe07b-4a99-3b15-82e8-3135080ac226 | -10.72586 | -47.58708 | 2025-10-17 04:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1147f4a-136a-38f4-964f-ac48aa34c3d3 | -14.33183 | -51.47813 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 302c2afe-2ba2-3a9b-ada0-9df75a7099da | -10.53185 | -49.55488 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 345aedaa-32a5-38a3-8cf3-6d5617c74a81 | -10.11589 | -44.55695 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1db79712-e4bf-31e6-aade-ef8033d1f608 | -10.26892 | -44.04072 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c258c31-8786-3b44-bae7-5c816c842ea5 | -11.18771 | -51.75054 | 2025-10-17 04:51:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5da621f4-af50-3e18-9f92-835b8f096e0a | -9.14488 | -46.64818 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2f85928b-6518-3fd6-9e11-17b175cefa18 | -10.12198 | -44.54748 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82ab2e8e-7f09-3013-a152-2b14ea7a261f | -8.43564 | -48.70154 | 2025-10-17 04:51:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed1b6407-9467-3d5e-871d-82e470fd5240 | -10.92183 | -47.86811 | 2025-10-17 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c606f73e-1c3b-3fff-aa77-da9d48ec1d21 | -8.3919 | -46.2476 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 72bd9cd6-5c0c-3a8c-882c-5ddd252a5a02 | -9.21006 | -61.54319 | 2025-10-17 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0f5058a-a1d3-3a18-97cb-0e55ef9bd39b | -10.01446 | -45.64501 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7952e3bf-89d7-3291-86d1-10c12828ea35 | -12.77488 | -44.89036 | 2025-10-17 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bff6910e-f7d5-386f-a5ad-f6b762953505 | -8.45491 | -46.24809 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 78cee74a-cd20-31b7-a2e5-97471594fcaf | -8.33167 | -46.23825 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 932e850c-0632-31f1-820a-d01c14c14b37 | -12.3067 | -47.26344 | 2025-10-17 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a28f423-e8d4-3466-b819-88cee8e242e7 | -8.44583 | -44.17934 | 2025-10-17 04:51:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4fc3b409-df37-32fd-8241-21e1667460f9 | -12.31977 | -45.6433 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32f2e878-3949-3c05-a1c3-09b55cef0eea | -14.08079 | -43.62218 | 2025-10-17 04:51:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 246b6d60-aeec-37ba-85d7-132f4d493090 | -10.13767 | -44.57453 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 85c24a02-75fa-3b2f-99df-56212159e4d9 | -11.59126 | -44.06464 | 2025-10-17 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e050b637-6e30-3da5-80a9-d783fd376249 | -11.39651 | -44.23364 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 676c6649-2f4a-3102-a3ec-dc722bc9ad80 | -8.56007 | -44.58066 | 2025-10-17 04:51:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0d840be-d499-3b44-93d8-df4fd8d6c73b | -14.33521 | -51.45588 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 862f7cb3-e4a0-33e7-af07-0b69a7dbafd0 | -9.97532 | -47.00703 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1264e5d1-68d8-3d18-819d-359fcc92ef89 | -9.64061 | -55.13455 | 2025-10-17 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3dc86ccc-1af1-3ecc-98b9-d6613c4af974 | -11.48839 | -44.19552 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9f77b450-d8fd-3e14-9ef8-f3f9b194b5f0 | -14.23595 | -54.90968 | 2025-10-17 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c44b9a35-d99a-33ce-aac8-bbd4aa87216d | -13.41575 | -47.93764 | 2025-10-17 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c29aaca1-a1b9-3832-8dd8-f650cd49f059 | -9.14327 | -62.30502 | 2025-10-17 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6e9132f-4aa4-38eb-acda-a001cb242865 | -11.46118 | -44.05254 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a8cd7559-7bd5-3236-9a99-f82909d50c6e | -8.55622 | -45.49191 | 2025-10-17 04:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d84b31b2-e665-3339-9d82-52cb5fe3e65c | -9.34743 | -46.915 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5ee97a9a-20a3-366d-8c03-3bf2ca388a40 | -11.46554 | -44.25518 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 329548ba-21e9-3f6f-bc27-1ac2a1bf0693 | -8.50667 | -44.56978 | 2025-10-17 04:51:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcacfa73-3f22-3b7b-af9d-3a34c5496191 | -13.27769 | -43.13612 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e9de2b5e-de9a-3814-8da6-055e4f90ade5 | -10.47163 | -49.18657 | 2025-10-17 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2998a352-3997-3391-8bee-05a7bc5298bc | -10.2682 | -44.04601 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 357345f7-bd78-3f13-a583-392765b58617 | -10.13632 | -44.58455 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1598dc0e-a0df-345a-b819-8216b759b579 | -10.11819 | -44.61214 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 61435887-0bec-3ed8-aae8-31f4e902f6d7 | -10.13211 | -44.54392 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2fab28cd-deab-30d8-b91b-fa857e1cbb28 | -8.16748 | -46.06376 | 2025-10-17 04:51:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| def1b930-1aab-336c-ad98-d560b4dbf0d8 | -8.45487 | -45.13251 | 2025-10-17 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README96.md)
