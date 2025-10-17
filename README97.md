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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 090a14c1-9e41-3541-acea-c9442e3f3871 | -9.06258 | -48.84848 | 2025-10-17 04:51:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 792b1664-89e3-3f26-9cdb-0b48ab5a165a | -12.42533 | -51.31319 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2db831cf-46db-3db5-849a-7bef6c823376 | -11.19326 | -51.75867 | 2025-10-17 04:51:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c33fcf0-ccfe-3dcc-8ad1-79a5e237a695 | -12.40961 | -51.30325 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ddf7a2f9-bec2-3e9b-95bb-c38593f8e8ee | -14.23442 | -54.89759 | 2025-10-17 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7e4a8e3e-d6dc-3a57-b42d-b51457ef8454 | -12.16681 | -45.06019 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 496368f6-272b-3494-bfdc-c7efc66860e8 | -11.32678 | -44.93511 | 2025-10-17 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9d32c0a-cd62-33b9-a656-f7fc08dea83c | -10.10222 | -44.57825 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 156e236d-1279-3df9-9041-caddb0a0a9e1 | -8.24499 | -44.01873 | 2025-10-17 04:51:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 262cc7c2-2c74-3e11-8975-9914cd572247 | -13.41895 | -48.58183 | 2025-10-17 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac043c54-af67-350c-929a-880f758ad242 | -13.41832 | -48.58638 | 2025-10-17 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68ade53f-6631-3028-85a9-4e6229448117 | -14.33973 | -51.449 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 04223ba9-122c-34c0-8bf0-f7afdab4e18f | -11.45697 | -44.04546 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 46207120-0232-3c2c-aea4-1e978bfa02d0 | -8.08368 | -45.42265 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fdf8d63c-f449-39ea-b4a7-180a254070bb | -11.96871 | -46.55101 | 2025-10-17 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc911fd9-0f9d-34e6-a03b-927533d288af | -13.28898 | -49.58126 | 2025-10-17 04:51:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fc396a8-ecfe-3675-a989-fd5b897853bb | -11.37896 | -44.21418 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f633a1c-dc9f-327f-b568-c783c85d3b9d | -9.49513 | -47.8777 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7843a11d-27f2-3cda-bf2d-27c7d56835ea | -11.3935 | -44.14159 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93295068-bf1d-317b-8b83-299869712dc7 | -10.81123 | -43.93791 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a862181a-b11b-3633-8e75-9f20bff08ac5 | -14.31937 | -51.44575 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6ab2258a-d109-3b63-91bd-7db1daa0a2a3 | -11.58626 | -44.06394 | 2025-10-17 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e15e79b5-4b3e-3239-8a41-73b1e295fe50 | -10.09804 | -44.60819 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8687209a-eb2b-31fd-897a-717b51929bc7 | -12.06448 | -47.98082 | 2025-10-17 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 499633ca-4564-3508-ac51-929848fc2a9e | -12.42252 | -51.30902 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0270ad5a-c7e7-3d18-a4ee-3315340e1921 | -12.16343 | -45.07311 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4abaf50f-3da7-332f-9e02-42d2022c6826 | -8.43328 | -48.70244 | 2025-10-17 04:51:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac45356d-217e-3095-893b-7937d9bdf08e | -11.40169 | -44.19442 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51d99d0b-618b-333c-889e-d3ba1b40c7d9 | -12.4242 | -51.29814 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dfbbd345-45de-3590-9e27-ff50dcf17d51 | -11.48912 | -44.18988 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2752f57-4e0c-3f16-a490-93912ad36984 | -10.62279 | -42.31339 | 2025-10-17 04:51:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 90981d38-a23d-3a28-aaa2-a84515f0bd24 | -10.39838 | -57.28924 | 2025-10-17 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af8e5c37-ba5c-3196-b29d-6658fa378ce4 | -11.40638 | -44.23497 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 896f3908-761a-38e2-91da-80e8d04838a5 | -8.44875 | -44.74469 | 2025-10-17 04:51:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be9afc70-dda9-302e-9529-3446e897124c | -12.4169 | -51.30069 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 27285ba1-0e14-3981-a483-181532357303 | -13.39971 | -47.20184 | 2025-10-17 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6bc3b5c-e50f-39d5-b162-d79cbd1efd34 | -10.27133 | -44.03064 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3fdbfce6-d34a-30bf-99f7-27444f880222 | -10.4361 | -45.01747 | 2025-10-17 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6969734d-09cc-3675-9b76-d79b505d467e | -13.48806 | -40.33304 | 2025-10-17 04:51:00 | NPP-375D | LAJEDO DO TABOCAL | BAHIA | Brasil | 2919058 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 00c91cf2-25c6-32f0-be19-ed2c7687d35e | -11.75736 | -51.14616 | 2025-10-17 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.1 |
| fa7f3cad-903c-329a-99dd-de0523f537e5 | -8.06123 | -45.41533 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b469d59a-5e91-311b-aab4-cefb6d0929bb | -10.39682 | -57.28801 | 2025-10-17 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d15aad7-97e1-3af2-b39a-a74097a4a935 | -12.42589 | -51.30956 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4fb1db4f-f291-3cec-852f-8e58445e6262 | -10.48047 | -49.36949 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45464476-bcf2-3289-ace1-3a46968fd71e | -10.23652 | -49.86839 | 2025-10-17 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ebc82e01-ded5-3878-9faa-99f1dbe00569 | -11.48343 | -44.19485 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| d810057d-4551-38db-ae44-a6734083f93e | -10.6494 | -45.29191 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 696721b3-a80e-3932-8043-cbd491db6d0d | -10.26323 | -44.04565 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 70e3e083-476c-39b0-8c82-19d0bdc63406 | -11.37963 | -61.21592 | 2025-10-17 04:51:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 023ca71f-faa7-30a6-8d00-f6271a16fb5c | -10.28866 | -44.04298 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 36f4461e-0c5f-36ed-8f4f-1cf3b7608ae2 | -13.07803 | -49.34162 | 2025-10-17 04:51:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5588fe79-c300-3204-9379-6f73c74919d5 | -11.46191 | -44.04679 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b4bf69f-db48-3e77-bb8f-e35ec7d1b88a | -12.41746 | -51.29706 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 39ad2fac-9d9f-3c05-bba6-867ee6239640 | -13.50269 | -47.16774 | 2025-10-17 04:51:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ed96b61-ffca-34ab-8e50-822bc314938d | -9.23573 | -45.27434 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5cc008c-2744-389a-a6f6-9c6a49f8b792 | -10.98136 | -47.89157 | 2025-10-17 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59cb544b-8100-3f23-94f2-d868f68c37e4 | -8.55546 | -44.57994 | 2025-10-17 04:51:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b87ac59b-9b6a-30d2-846b-fd5555dabeab | -8.23159 | -44.82896 | 2025-10-17 04:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1349d68c-eebd-3df3-ba43-47c4c113c53c | -10.14774 | -44.53548 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0dcb0a68-a7ed-355e-a3f5-a2d40706d4a3 | -10.92119 | -47.87264 | 2025-10-17 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84309067-aedb-3854-90c0-9310f48cf5fd | -8.31484 | -47.86289 | 2025-10-17 04:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99825451-7563-3c39-96bb-30036376097b | -11.54271 | -51.40332 | 2025-10-17 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d63b3b0b-e3a4-3ccd-87c1-698046793c7d | -14.32617 | -51.46964 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4aa8131a-c34b-3ca3-91f0-8a01b6bdb2f3 | -10.29457 | -44.04459 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 6e3f5188-2ab1-3511-befb-fe8e6bfff31e | -8.40628 | -46.29372 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c39a5afe-61f2-3d7c-bcde-165cb68f3794 | -10.27553 | -44.03692 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9db922ce-8da3-3225-a14c-122910710561 | -10.62236 | -42.31048 | 2025-10-17 04:51:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5a5c833a-aaca-3dfa-b23e-6fdcc9300842 | -8.78972 | -46.67529 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c4ee6869-1f0f-300c-aa4a-e922eb32254f | -12.45116 | -51.32474 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abfe18dc-8ce9-3261-b739-1b398144fc41 | -11.47275 | -45.08502 | 2025-10-17 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60268364-025e-3cc7-8f72-b254fac71cf1 | -11.38884 | -44.21552 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c70683ff-ba05-31cf-877f-ad63bf552d46 | -8.84269 | -44.39983 | 2025-10-17 04:51:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 108f01a5-8c0f-33e1-9f24-010de653123e | -13.93512 | -48.69062 | 2025-10-17 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27c4206f-c3b4-33f3-aa0b-83f3eac1e507 | -10.1267 | -44.54825 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de42a185-be5d-3635-aa48-c3f1724b6db7 | -11.48765 | -44.20116 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0575694e-3b7d-3a99-884f-8df72ddf63f7 | -8.3832 | -46.24962 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9e84f1d5-8d2f-33a6-bfd2-e42f60050708 | -10.1213 | -44.55257 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5a197e5-5a14-3ceb-9516-098f981e9896 | -10.52542 | -49.54985 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d664dc94-09da-3f2d-a0f9-919f2981d416 | -10.61675 | -42.31629 | 2025-10-17 04:51:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 191d5f54-c8fc-3671-af8f-cc24bc98f7f9 | -10.95255 | -49.77224 | 2025-10-17 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 93503134-42d2-3cdb-bdd4-831203e84eb4 | -14.34426 | -51.46493 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 42a74272-73f3-39c2-a193-05eeceb660ba | -14.34368 | -51.44583 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9f1b2963-7fe4-3f37-a158-83f9ac0755c1 | -14.3058 | -51.44358 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 09a4bf15-68cc-3bf7-b18d-bf4b200f395d | -10.29015 | -44.03214 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 4a21a65f-7128-3396-b760-8f0a921c02bf | -12.41635 | -51.30433 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 1f82bab5-78f2-39ae-9be2-3c0493de9e31 | -10.50435 | -43.41215 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d3ba9de-620d-3e50-940a-ca64450d0afa | -8.08427 | -45.41848 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8d7a37a7-a8b1-39db-8773-6a4fdba8aa58 | -11.97189 | -46.5596 | 2025-10-17 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae3658ea-a99b-31b2-a700-0cc9dc3f0691 | -11.97298 | -46.55604 | 2025-10-17 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9761eec0-8c94-3a11-bb5b-78fcece33f04 | -10.10827 | -44.56946 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 739a9178-f2ec-3869-bf14-ffa2d9b41557 | -13.41646 | -48.57947 | 2025-10-17 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d39adbb-de09-34fc-9abe-dc9d3b93f828 | -10.27124 | -44.02369 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c3fff189-2d09-373a-9b73-98c4c942d06b | -9.87389 | -62.41471 | 2025-10-17 04:51:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4fa89e46-9912-3184-8d36-8cb60ae18767 | -8.1982 | -46.92939 | 2025-10-17 04:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae755d81-3ff0-3962-8cc0-05ec7b1df80a | -10.05344 | -43.86971 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| deaf617e-2e8f-3860-ba2b-f018fa52c2a5 | -12.0599 | -47.98516 | 2025-10-17 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f47f4ad6-82bd-39c0-8ef2-79c863a5b7ce | -10.11049 | -44.56135 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e6ccb2b-cd1f-3f03-a8d9-28d451c0b328 | -8.38778 | -46.24701 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e439088f-b185-3199-8c47-25b6482dd757 | -11.73852 | -55.18143 | 2025-10-17 04:51:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5c0aa0a-db4a-33aa-863f-7136aac033b5 | -12.453 | -54.48624 | 2025-10-17 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README98.md)
