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

## Dados Diários - Página 297

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3cdd708a-67fa-34e0-b16d-84148f67b44e | -6.24665 | -44.36271 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ac228120-ac55-3c29-9827-9f9c51b5fe0e | -4.4431 | -41.48023 | 2026-10-08 16:20:00 | NPP-375 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| bd616094-cb48-3687-821d-7102a17c8115 | -3.19904 | -42.96405 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 7beb24a5-510b-392d-b13f-d166c7e4bd95 | -5.95335 | -45.69525 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 55bdb95a-724f-3725-be94-703b3ceb2e42 | -6.67601 | -45.365 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 129480c1-a720-3cce-a363-b98a7bfdc738 | -3.30366 | -49.12073 | 2026-10-08 16:20:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| a4279e11-af75-3f7f-9a73-1364608963cd | -7.7771 | -43.81126 | 2026-10-08 16:20:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 97f93727-78c9-308f-bb26-aba0de588c93 | -6.05193 | -42.59598 | 2026-10-08 16:20:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 45.4 |
| fe534ec2-fa90-3697-9ff9-45b8a124643f | -4.36131 | -40.41647 | 2026-10-08 16:20:00 | NPP-375 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 3ca02a8d-3ea2-3a38-8a59-9f5162ff2a96 | -5.4835 | -45.63333 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1622a68d-22fa-3bf2-8bae-90eb8e7bb65b | -5.70845 | -41.7349 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 9b40d9fe-1c78-3863-9f4e-5556462dd606 | -4.92049 | -40.36383 | 2026-10-08 16:20:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| de7ed3f7-7fe0-3894-a1ec-10067ed02011 | -2.86627 | -54.16182 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| aac71f78-9e35-36ff-95a6-09d35d720789 | -6.16226 | -42.58892 | 2026-10-08 16:20:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| cc18c61f-e5c2-3bdf-9837-270fe8d431eb | -5.77288 | -42.07106 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 0103b713-857d-312c-9ffe-07504f848b89 | -5.45939 | -45.59032 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 692c401e-285d-309a-b857-b262d5448f15 | -7.20624 | -45.35302 | 2026-10-08 16:20:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8a948b9d-224e-342d-b2ca-462bd7d92c2b | -4.32625 | -41.23515 | 2026-10-08 16:20:00 | NPP-375 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a0e00f19-6b2b-35c8-a6e1-47dd934b3575 | -6.17313 | -44.85389 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 7053cb71-d06e-336a-8f45-9cf4e812261d | -6.5007 | -42.0307 | 2026-10-08 16:20:00 | NPP-375 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 35.3 |
| 96b1694d-d628-33a0-8941-63f0124e5962 | -7.70243 | -44.75532 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f057c08-8ed7-30ae-bfc1-325d7169a2ac | -6.53797 | -45.40101 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 1f1f5900-44d9-3ba1-9ff5-db1241fd0ffa | -7.20517 | -44.29141 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7e54f34-7cf1-3377-a271-4c2d7b7ba374 | -6.60022 | -37.89973 | 2026-10-08 16:20:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 77.9 |
| f6cb46c1-c96e-39b8-8063-2b179ea23f86 | -2.07553 | -46.57358 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 562.0 |
| 3f32f7fc-df60-3c8b-8883-1c4b87be0e0c | -6.14657 | -47.9507 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2f53183e-1f88-3d01-b969-a0df5091190d | -6.59569 | -37.89295 | 2026-10-08 16:20:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 5de2cf44-3251-394a-b4a2-281c1e605754 | -5.71086 | -53.45068 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| ab3a9d9e-03a6-3723-8a1d-9f6f51c413d7 | -6.96034 | -45.41469 | 2026-10-08 16:20:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9185519d-a602-350a-9cfd-1c39f66bce8e | -8.35506 | -47.64927 | 2026-10-08 16:20:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 10950f8e-e64f-35ab-b964-f2e25e4e2d94 | -5.84889 | -42.6322 | 2026-10-08 16:20:00 | NPP-375 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a49116e8-0f87-3ba1-91f3-70d62e54c648 | -6.85218 | -41.75343 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 58.6 |
| 5fcc792d-307c-3af5-8977-9c3a8e071799 | -6.33051 | -35.12291 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| ef524841-3b65-38f3-82a9-fa91af10fd8a | -7.6585 | -45.38958 | 2026-10-08 16:20:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ecd4a763-dacf-3a28-bbf2-6317dba7a90e | -4.75288 | -40.50497 | 2026-10-08 16:20:00 | NPP-375 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 609b90f9-853a-3208-8a41-f83498040dd1 | -2.94009 | -54.15791 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 5679e52a-3761-3225-9daa-5bc982c64910 | -6.19581 | -52.87099 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| e6dd5f60-81ca-3657-9547-ad5943624d16 | -1.22415 | -49.33665 | 2026-10-08 16:20:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f93fa77d-7acc-3fbb-a225-188d3030ffdf | -6.96742 | -47.67247 | 2026-10-08 16:20:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ee696312-0a26-3ff7-94b3-58d8047fe027 | -7.06188 | -40.94954 | 2026-10-08 16:20:00 | NPP-375 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| d0c1b603-423b-3ac2-9550-30bdb7fa2db8 | -6.15801 | -42.58529 | 2026-10-08 16:20:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| 5c33afee-3c68-3d74-a033-0d70e4cffd27 | -6.79099 | -45.06148 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 568e5573-4b29-3528-a034-3506285780d2 | -5.74734 | -41.63945 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| fdf3a924-1340-3e95-883a-13e4f26bd445 | -3.20682 | -42.96704 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| d47d3d36-4902-3e3f-bad8-8deb64acfafe | -2.9984 | -54.08888 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c1b9ea0e-7784-31c7-911c-2edb8d6e039a | -7.12984 | -44.08422 | 2026-10-08 16:20:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6b3f9076-4544-3a83-b41a-45e57196b2d7 | -6.16608 | -39.43911 | 2026-10-08 16:20:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 6257187f-e3a5-3734-be09-0733163cfe83 | -5.4677 | -41.22067 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 29.1 |
| 75565e08-7cd0-3be9-b197-227f22b90c19 | -6.79042 | -45.05738 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 21c09fd3-c081-3b03-aac1-51030d1f6547 | -5.49112 | -41.39806 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| c30eb7e4-1a22-324c-b156-714ca1bb7a9c | -5.93267 | -51.83524 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 143.8 |
| a22d8a09-c865-3afe-be1d-95c58dc3a3d7 | -3.79979 | -40.45835 | 2026-10-08 16:20:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 0dacc62d-553c-3c9e-8824-a99364ba273f | -6.13939 | -47.95063 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2ad9abde-a0a7-3a30-8be7-ca1a19d81c48 | -3.25267 | -54.03131 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 760b422c-73b6-3380-aa01-4cb9846c023c | -4.09897 | -44.11256 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9f2a45dd-d719-345a-ab35-b8289a9966a8 | -6.25895 | -45.32898 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| c2306606-ab93-3ab6-8c39-ca4558069796 | -6.89953 | -45.89495 | 2026-10-08 16:20:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9bfab002-419c-3f7b-9555-3ebe82ab74ec | -4.4339 | -43.90047 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 2260271e-3ed1-30e7-bae0-2b6f4fd64115 | -3.78858 | -41.6703 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 3ae08a54-6322-3078-bfe6-9a70a3f2ac32 | -7.70185 | -44.75128 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d6c49cb1-9ca8-3d26-9f34-8a2d90f251bd | -6.20114 | -52.85689 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 2da6c0ac-cd13-3831-81ae-600897d25cf1 | -5.45419 | -42.9073 | 2026-10-08 16:20:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 38.3 |
| 77609275-a983-39fb-927a-d2a9b272fd9f | -6.19544 | -45.40989 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c67da874-247c-3a12-ba16-b7752cbf48f9 | -6.83153 | -43.64404 | 2026-10-08 16:20:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 71047e21-d1be-3245-9989-ae7b70c4320b | -5.72655 | -41.64252 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| b931da36-845b-3ad3-92f2-ceac5a9b5632 | -7.78877 | -44.58052 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2886bb85-1e69-3ec4-9586-5d75e6f98ecb | -3.08291 | -53.94986 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 253e7dd5-b420-3def-90d7-f6ba44c51ab3 | -6.57828 | -41.60617 | 2026-10-08 16:20:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 24a79604-e0f7-3acc-97f5-b62f8c92d994 | -6.41458 | -44.94826 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 36a8ef4c-c214-3038-a28f-39906f9b9c9c | -7.53547 | -45.8742 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 6f7ea587-d48a-324b-9d43-cef4317752a0 | -8.20585 | -46.41832 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 9269fcb2-c295-3d84-ae28-7fdf842e5320 | -6.24345 | -52.87688 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b7f710b5-3afd-3607-9511-90eff8cb9ae5 | -5.73439 | -39.64575 | 2026-10-08 16:20:00 | NPP-375 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 2eb9b8e9-9ad4-3bb8-b365-3ceabf708c55 | -5.7019 | -53.4455 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 9b009501-78fb-3ea3-8df9-42723b0de7b7 | -3.08278 | -53.95872 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| dda5fe2d-5e7e-3154-a4b2-c13d9c7a710c | -6.83312 | -39.55685 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 5e12773f-1835-3288-91fe-ada47d1a8d3a | -3.25881 | -54.02689 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 4fb5e8c6-27c4-3a06-81ed-8a4b292af967 | -7.56106 | -46.70662 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0c08d043-f792-367f-a337-de5a5c2983ad | -3.9838 | -42.8601 | 2026-10-08 16:20:00 | NPP-375 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 62717546-e9cf-3aee-97e3-eb40ed1ecbad | -4.8416 | -40.39801 | 2026-10-08 16:20:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 11.4 |
| ea7a910b-1596-34b5-8596-9285730e2300 | -4.36464 | -40.41597 | 2026-10-08 16:20:00 | NPP-375 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 360cedf1-47a3-3cb7-9d40-90642e4c2a3d | -3.65968 | -41.44429 | 2026-10-08 16:20:00 | NPP-375 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 7c358e8b-9a8c-3482-99aa-9d2ebe1a7bf9 | -6.63401 | -44.88988 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 66ea3cbe-5db4-382a-9fd6-22df12645a09 | -7.54344 | -42.09083 | 2026-10-08 16:20:00 | NPP-375 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 83a3e514-5c83-331c-a032-7dabfd2e4c5a | -6.69635 | -45.29067 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2ffecd0b-672c-3d66-bfbe-5de417d2a8ca | -3.59766 | -39.13922 | 2026-10-08 16:20:00 | NPP-375 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8b6a4d72-8c99-3e4d-b4a5-97b2ff7bdd52 | -4.36816 | -43.90536 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 14e3fa2e-b1ca-3eae-bacd-0c82450d27d7 | -4.29494 | -48.60098 | 2026-10-08 16:20:00 | NPP-375 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| cccd633d-49e1-35ee-96ab-1973544a34e6 | -5.97534 | -40.90767 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| a792b8e0-1d9a-365d-b210-3824298eaa78 | -6.17423 | -44.86156 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 2b19214c-c50f-38ea-b04a-5507c7582e3d | -5.66333 | -43.62421 | 2026-10-08 16:20:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4955963f-5b42-3a4f-b90b-9d4c4a6e3a12 | -5.98426 | -41.36573 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| cd33c1f9-7059-3325-8f79-79a178bb3884 | -5.94893 | -45.69572 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| b0271cf5-e635-3466-8058-2023e199b31f | -3.30867 | -53.70327 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 9ef55f31-f022-337e-b03e-78684998590d | -6.05099 | -43.14379 | 2026-10-08 16:20:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 9f47d7ca-8524-3705-8a4d-7487f5c4ae26 | -5.08257 | -43.05865 | 2026-10-08 16:20:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 680395d0-1cb9-3eae-ae92-573967f9c263 | -5.32489 | -40.89377 | 2026-10-08 16:20:00 | NPP-375 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 67b0d286-5a0f-3c09-8ea3-0cd0585b1f8e | -7.30892 | -44.00335 | 2026-10-08 16:20:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d79e9dce-cedf-3483-9ab9-3624b3b3e2f5 | -2.08119 | -46.58147 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 267.9 |
| 9149c7a9-96ca-316a-9a5a-e8d7db57d165 | -6.28627 | -46.43443 | 2026-10-08 16:20:00 | NPP-375 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |


[Clique aqui para ver as próximas entradas](README298.md)
