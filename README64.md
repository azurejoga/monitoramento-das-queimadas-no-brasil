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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| def2c0b6-ac85-3acf-957b-75542dfb41bb | -5.04118 | -49.77162 | 2026-10-08 04:02:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e3cc1ff-b82b-303c-a2f2-51d8a4f584e9 | -8.60024 | -45.64253 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 226d5474-9f7d-346b-a9c7-dad35fe7a194 | -8.78375 | -41.15 | 2026-10-08 04:02:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 429c209d-6a28-33da-ab68-02dfe10a8886 | -6.93157 | -43.66346 | 2026-10-08 04:02:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4e4dcde9-29aa-35fb-9400-180f1f2fb070 | -7.74657 | -43.81009 | 2026-10-08 04:02:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 688384f9-be70-3666-b25f-a3e98bdf6813 | -7.18572 | -52.6283 | 2026-10-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2b7878a4-aca7-358a-950b-3ce64ae28779 | -8.72259 | -45.17117 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3e9e0688-75ae-3b8b-9514-f92df268d3ae | -8.38139 | -46.28677 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 481e8170-0e89-30e3-a7c7-b6e198f7eb8b | -7.86411 | -44.15036 | 2026-10-08 04:02:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 085430ee-146d-3132-a3d5-55cb1e565a90 | -5.87175 | -50.09665 | 2026-10-08 04:02:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2b08cab7-1c21-32a5-b4f9-29c7fc81318e | -10.24848 | -36.33517 | 2026-10-08 04:02:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ca0d938d-55ce-376b-8670-ba9060dff983 | -8.20671 | -46.33408 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dd7866d3-8a06-34f2-a9c8-395c98e6f518 | -6.15368 | -39.43837 | 2026-10-08 04:02:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 060c4b70-0da1-3ea5-8ed4-446bb0be2b0c | -5.26463 | -45.40569 | 2026-10-08 04:02:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb5e6611-3521-3717-a5f8-cf2955024424 | -9.14504 | -45.82645 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39d2a063-ef8e-3709-a551-0d92ae5d1743 | -6.81426 | -38.53548 | 2026-10-08 04:02:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bf71173a-9fbd-385d-8490-94922184a28a | -7.59826 | -42.38947 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1c5c44c7-6200-3fcb-aa9a-7575dd66c115 | -7.39686 | -44.47907 | 2026-10-08 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97d2127c-132a-3696-add0-417b4d5b5e78 | -9.5572 | -40.33993 | 2026-10-08 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 44275e8c-5dc5-3699-9f07-6c2a8e607e74 | -4.06688 | -51.0424 | 2026-10-08 04:02:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 88fb3b2a-e7d4-382a-a1b7-3e349842f948 | -5.71651 | -41.75438 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0ae17161-3fdc-3f95-8b59-6f0d003a77cb | -11.22026 | -44.86868 | 2026-10-08 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28acc309-ef7c-37e2-8c75-4c4ab3153d37 | -8.98199 | -45.94302 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b6f882e-3b89-3973-a48d-ef2478664917 | -5.75899 | -42.06421 | 2026-10-08 04:02:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4d74f609-83c8-3c6e-997c-806221df1a05 | -11.83466 | -43.5273 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b896e2cd-e01b-3a35-8453-89d31b1de1dc | -7.37411 | -44.03315 | 2026-10-08 04:02:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4cc53742-c438-37d1-bab0-9762e27bae36 | -6.98601 | -40.03469 | 2026-10-08 04:02:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ab748103-5479-38dd-b0ba-a3f4e0a46254 | -3.17942 | -50.56947 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6bf6995-ab61-3df2-b3b9-7ea9700ed107 | -6.16091 | -39.43594 | 2026-10-08 04:02:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| b493ba46-2cc6-3544-a760-7dc47c8ad95d | -9.9134 | -46.79391 | 2026-10-08 04:02:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9690573a-87ae-3d0b-9351-4fd4a92d8e32 | -8.43966 | -47.02336 | 2026-10-08 04:02:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 66d2c016-2bf2-3ff9-bbce-f0cdf5ada029 | -11.23371 | -45.24426 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2074df50-c9e7-313e-9024-1be4e117604b | -7.22694 | -44.28102 | 2026-10-08 04:02:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8644f218-e850-333a-8569-35f5cb92d6c6 | -5.9743 | -41.37458 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| df7fcc06-7ed0-3377-af43-3ba7bac60979 | -8.23569 | -48.58095 | 2026-10-08 04:02:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a26b4636-f684-3d7b-a99d-052b2b4f9373 | -8.71683 | -45.17868 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cec4ae8c-7886-3546-b0d6-816a2d7dd1c2 | -6.31675 | -43.34803 | 2026-10-08 04:02:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bbf36a5b-d8fe-3dbe-b0b7-4d49ae4dd1a2 | -5.75083 | -42.06743 | 2026-10-08 04:02:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 00c80683-2752-3ec7-942c-f7f84db3a5ef | -5.71234 | -41.66627 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 76dc242d-a139-3b5d-8192-1dad0503f02e | -5.75197 | -41.62925 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 39eebfd6-0462-3267-b1f1-d4532f5e3cd6 | -6.13366 | -47.927 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ad8e3c3-7c26-3b75-8487-cd97772835a1 | -5.51452 | -50.02369 | 2026-10-08 04:02:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9890401-2d04-3d5b-9d98-8b04816184b0 | -8.22165 | -46.33191 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35c17052-6756-3244-92df-db7a497bc145 | -6.8894 | -43.69238 | 2026-10-08 04:02:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e80d668-2c7c-34ae-b6a8-fe5cf3edeae0 | -11.74422 | -43.64379 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 01bcdb9f-e21c-36f1-9f00-4008c426df63 | -6.93039 | -43.67046 | 2026-10-08 04:02:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0a28954e-9c8a-3c7a-aac8-c49cefed5208 | -3.19284 | -50.57172 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8fc4997f-8c8b-3cb4-94bc-cc84eb49d4fc | -7.0215 | -42.11501 | 2026-10-08 04:02:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dd982ba7-73b7-3cd2-8c3b-6534df52ce81 | -5.56045 | -43.97219 | 2026-10-08 04:02:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5e7c560d-7124-3cf4-9f9f-dd5264411879 | -11.64626 | -43.69452 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a9c256fe-57fb-380a-8f0b-b0d977e4e5f4 | -7.35049 | -44.36933 | 2026-10-08 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67a3a90d-5c11-36be-8adf-f0c07c99809a | -11.71492 | -43.65735 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0379e829-17f6-34e2-b6c5-156bdaf17df2 | -11.09964 | -44.00355 | 2026-10-08 04:02:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ccfd15f2-3921-3035-aedf-4d4b3a78d68e | -3.47203 | -50.08854 | 2026-10-08 04:02:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 526558d1-60cc-3634-a1e6-6c5d11f173e0 | -5.97073 | -41.37397 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 82f22209-647b-3802-a162-49b4981a7aab | -11.85984 | -43.5589 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49722852-edb9-3bd2-b808-1b4b9daf5499 | -8.38515 | -46.30451 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 4e676639-3a8d-30f8-9739-2f2678ac2528 | -6.95314 | -45.26074 | 2026-10-08 04:02:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2821cec1-e703-3bd8-b9c1-c85ac9279993 | -9.78819 | -47.86196 | 2026-10-08 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17ed6424-0e15-3e70-8e02-5a2e27709d4f | -6.13725 | -47.93862 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1710371-03b7-3a43-96de-5419ba656a85 | -5.73467 | -45.16403 | 2026-10-08 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 13d87e86-1976-3860-b714-bfbf3385723c | -7.65824 | -44.94923 | 2026-10-08 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2e58536-2da7-324e-83b7-9e8b2636e898 | -7.58803 | -45.29866 | 2026-10-08 04:02:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba86608f-7089-3cef-814d-e118391e4422 | -11.64705 | -43.68987 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1287b95f-ec48-35ae-9642-483aeb416ef1 | -3.19954 | -50.55507 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| ddbbd89f-015a-370e-b200-85592d22be73 | -8.88239 | -45.60094 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0f2b9b8-7d4d-331a-a128-1b80c4798738 | -8.97867 | -45.91671 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb56b319-3f5d-390f-898b-daab4d89322d | -8.59736 | -45.63249 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99fb604b-9979-35f1-9043-1cc124801c98 | -4.85536 | -42.99777 | 2026-10-08 04:02:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17bd3e9d-cb84-3d66-8392-8a377bfd36b6 | -11.72481 | -43.42196 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2057782-b086-36fa-bc7c-2d76b3418d52 | -6.88756 | -43.70312 | 2026-10-08 04:02:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d2b3e31-f7ea-30c8-92a0-788d64e31ec7 | -6.31278 | -43.34732 | 2026-10-08 04:02:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e1e52259-b6f8-369d-a1c5-45e3f23dd3ca | -7.70292 | -45.44474 | 2026-10-08 04:02:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ae8166ec-4f5f-33f0-bb5d-981bbb09a059 | -7.38157 | -46.23938 | 2026-10-08 04:02:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82d72571-94ef-3f8e-a49b-d5f0d5572115 | -7.2643 | -39.72046 | 2026-10-08 04:02:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 17f81332-f475-3bea-9453-31b0f8e454c2 | -10.98005 | -45.40136 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dca6f03e-bbca-3d61-a176-abfac06da81d | -6.95235 | -45.26525 | 2026-10-08 04:02:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6fe39a0-5ff2-3fc2-ac60-a4f59ad14a29 | -9.56054 | -40.34048 | 2026-10-08 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 75892d7c-6843-3894-a1e0-a3aa362b0071 | -4.51229 | -42.8913 | 2026-10-08 04:02:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| caf2bc92-3358-3261-ad88-810739a9a339 | -5.3355 | -45.27063 | 2026-10-08 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0717de75-0a66-3dbe-b025-1402cf5e836d | -8.21783 | -46.32606 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 724b48bb-6dcf-3eb1-bedf-be427ba37d79 | -5.73245 | -45.14947 | 2026-10-08 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| b1c2651c-9179-3714-83c7-df8432e1e261 | -6.15978 | -39.44298 | 2026-10-08 04:02:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4c1c70a2-a394-3ba5-a42e-abab04468371 | -6.84545 | -41.76959 | 2026-10-08 04:02:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 90678c20-5b58-3606-9e16-07e8f8d383b5 | -3.2042 | -50.56826 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f1fd8070-39a6-310d-a620-11d11a33a4b1 | -7.88423 | -44.24786 | 2026-10-08 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1d81494-919b-39f5-961f-77d0cd85a1c6 | -5.54497 | -43.22307 | 2026-10-08 04:02:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 41a22941-bc14-3dde-81ce-6fcf9403a82a | -6.375 | -42.90617 | 2026-10-08 04:02:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| da887d9e-4d09-3945-8ac6-9d221872b0cd | -7.64113 | -38.37606 | 2026-10-08 04:02:00 | NOAA-20 | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e670cd90-9852-3b5a-8827-d69f75a07bed | -4.22322 | -46.93756 | 2026-10-08 04:02:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eafdd266-91df-35c1-9dfc-82b78f6012aa | -10.8354 | -48.13791 | 2026-10-08 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49fd9fd2-f540-37cd-a81d-a48563842df9 | -5.7392 | -45.16481 | 2026-10-08 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a04644e6-ba46-36d9-8c59-b3055774afa9 | -3.16989 | -50.44718 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c120337c-d23c-30cc-862d-2a2236619237 | -8.28915 | -50.27459 | 2026-10-08 04:02:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 542cd8ae-cd33-37ad-a6a6-20e0a39c7614 | -6.84613 | -41.76543 | 2026-10-08 04:02:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 64025811-5c1b-3f3e-823e-c031da54e08b | -6.15758 | -39.4354 | 2026-10-08 04:02:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 9df4fc9e-0252-3562-a800-47e69ce6fc3f | -4.264 | -46.38774 | 2026-10-08 04:02:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 767752c7-1fe2-31ac-b88d-589e531e9bf3 | -5.12005 | -47.11499 | 2026-10-08 04:02:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7838f26c-8bd5-3b58-bc44-b20cb53beef9 | -6.35194 | -42.58278 | 2026-10-08 04:02:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 79bdfa9e-32a0-37d1-b9bf-957662027541 | -7.22236 | -44.15957 | 2026-10-08 04:02:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README65.md)
