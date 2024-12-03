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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f748bb0-4329-3b7f-b40e-ee5f35f795b9 | -4.08571 | -47.36129 | 2024-12-03 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| c2655d8b-7373-35b1-a88c-5419a6703d78 | -4.55407 | -42.92484 | 2024-12-03 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 56962a20-22ee-3a89-88d3-28d0e97c379c | -3.10598 | -40.08685 | 2024-12-03 00:13:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 514363cd-5dba-3cb4-a70a-95f564ae08a0 | -5.31215 | -39.79725 | 2024-12-03 00:13:00 | TERRA_M-M | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c7262d75-ddc4-3ee0-8925-7d64076ef63d | -3.60651 | -45.58868 | 2024-12-03 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 150ef66c-edf8-37fd-8c43-b9640e22f8d7 | -3.84992 | -46.51421 | 2024-12-03 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 79457728-e431-3ab3-8109-42287a1cbe19 | -6.81586 | -46.78793 | 2024-12-03 00:13:00 | TERRA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| ad248d59-ee61-3b45-a9ce-fdd64ff8e279 | -3.20048 | -45.29021 | 2024-12-03 00:13:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 108.9 |
| bd650748-369b-35a4-9450-d8bf983cf2cf | -6.23912 | -39.50771 | 2024-12-03 00:13:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| f10e4322-f625-368f-9b39-79ab00ac2f5f | -8.1341 | -44.46356 | 2024-12-03 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 44.8 |
| f54c741e-31d2-3f01-bc0d-ddddce105d88 | -4.55584 | -42.93787 | 2024-12-03 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 41d43a0c-4ae4-3c5c-a05b-8638b3050192 | -2.95943 | -39.96385 | 2024-12-03 00:13:00 | TERRA_M-M | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 0f22091d-648e-3ad3-881c-629f87516425 | -4.7454 | -45.70133 | 2024-12-03 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 524de153-618b-3a3c-852f-9b412d0ef157 | -6.11435 | -43.97517 | 2024-12-03 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 93162bb9-5250-3427-89f2-fdc5ede71c1d | -6.04327 | -44.03997 | 2024-12-03 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 84317c8d-b609-31f8-8090-4a28a7a6d6eb | -3.07029 | -44.32772 | 2024-12-03 00:13:00 | TERRA_M-M | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 8b97dfe0-67f5-3035-a793-e91d5e3c0f5e | -4.4829 | -46.36415 | 2024-12-03 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 94e1e342-155a-3bb9-bb58-b9dd30391254 | -3.36706 | -45.84811 | 2024-12-03 00:13:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| a853aa92-e1af-39e9-9a1c-fb6ea8059ebe | -5.14889 | -43.2493 | 2024-12-03 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 535d83a4-2f4a-3b27-8583-5cd26547774f | -4.47562 | -45.734 | 2024-12-03 00:13:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 18c0fcdd-57a2-3854-b9d4-f2ba6c2b9222 | -3.38027 | -45.84636 | 2024-12-03 00:13:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 195f5e8c-8ef4-3cf3-baf3-9f92caca0931 | -6.81241 | -46.75938 | 2024-12-03 00:13:00 | TERRA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 18ae87b2-f027-32dd-9df3-a5bea191125c | -4.16222 | -48.59199 | 2024-12-03 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 23c262b7-98e0-3666-9e4b-7fd7be84adbf | -3.86674 | -43.35248 | 2024-12-03 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 03093aa0-5f54-3961-b74e-c1fe838d3bdf | -4.08397 | -47.35519 | 2024-12-03 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 75b29bb3-f7a0-3cb7-b964-d8826e6e40ab | -3.52989 | -46.1742 | 2024-12-03 00:13:00 | TERRA_M-M | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 2d0a1110-f9a9-34be-b75e-11e0f4a5f82d | -4.74833 | -45.72326 | 2024-12-03 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| a064c473-4ddc-3da1-87c3-f25bbb630468 | -4.54168 | -42.91336 | 2024-12-03 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 497ca5be-c881-3c1e-8d19-371e78c53e58 | -8.13652 | -44.48275 | 2024-12-03 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| ff72bfb3-db69-3dd6-a16d-824c4241d64a | -3.16455 | -40.18004 | 2024-12-03 00:13:00 | TERRA_M-M | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| d33dcd53-46c0-3d55-8281-7d5a4fc8700c | -5.11936 | -43.19598 | 2024-12-03 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 5851f35b-885f-3f53-8ab7-7d685687ddae | -3.08178 | -40.05058 | 2024-12-03 00:13:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a52ea102-fb79-39e0-9860-566e2ef85a06 | -3.07331 | -45.40956 | 2024-12-03 00:13:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 1a17037a-b81a-3d70-b921-8437b5623874 | -4.75003 | -38.46586 | 2024-12-03 00:13:00 | TERRA_M-M | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 952523ba-5974-3e86-b552-47fac95d2a8f | -4.57229 | -45.09216 | 2024-12-03 00:13:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 50061fdd-bfc0-3d2f-99a1-d327767c1eff | -3.85751 | -46.53225 | 2024-12-03 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| ee6244fd-a3d1-3794-a8e1-a5af4e9f1306 | -4.16657 | -48.1968 | 2024-12-03 00:13:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 3ed1439d-7fb2-37e7-86e9-2f9ad3ef5eec | -6.49192 | -44.68413 | 2024-12-03 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| dd40eccf-2de1-3c41-80b7-6f4a8e495889 | -6.81765 | -46.7928 | 2024-12-03 00:13:00 | TERRA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 924bbb00-b922-3c37-aaa8-e37579b79f34 | -5.74131 | -44.43804 | 2024-12-03 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 416b3568-80b9-3b45-8af5-56e6e4e28376 | -3.53296 | -46.19681 | 2024-12-03 00:13:00 | TERRA_M-M | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 2adca7bf-8275-3fd7-b9a4-1b3b2f1b637c | -4.5523 | -42.91182 | 2024-12-03 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| b3769047-c20d-303f-a99c-2c9d35e34a48 | -3.46758 | -41.99469 | 2024-12-03 00:13:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 25.8 |
| f4e4fee1-3467-3c1d-968f-01b6611486bd | -6.17667 | -42.62263 | 2024-12-03 00:13:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 43.4 |
| 250a3494-aad3-3e18-8b22-907ff26a5caa | -3.8686 | -43.36613 | 2024-12-03 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b65fa1c5-7ce4-3cd8-8450-69dd70a12afc | -6.20667 | -39.74211 | 2024-12-03 00:13:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 0d439283-65ad-3a84-9e50-c0cfe74f21ef | -4.55986 | -45.48245 | 2024-12-03 00:13:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 1e4e1bee-1704-3db0-a3ac-9f725ab59888 | -3.45925 | -42.00705 | 2024-12-03 00:13:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 9b94267b-9995-302c-9971-bc5ca5b7f377 | -6.21533 | -39.40598 | 2024-12-03 00:13:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 43f7028f-451d-3b95-ace9-7d46e3357438 | -5.57814 | -44.88559 | 2024-12-03 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 845250d5-8622-3920-b509-182064488983 | -3.3554 | -46.06752 | 2024-12-03 00:13:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 3f76b00e-2322-39d7-af82-308cf2c1fb41 | -5.11026 | -43.21156 | 2024-12-03 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 46a562dd-75b5-32e1-a2a1-b0127fde5bc5 | -4.4327 | -45.79097 | 2024-12-03 00:13:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 5838ce57-daa2-3625-9a5f-49bc739c9a36 | -4.46816 | -46.09576 | 2024-12-03 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 21.7 |
| f992ab74-dc76-327d-ba4b-4a2a102fa64b | -5.14699 | -43.23524 | 2024-12-03 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| e5df7d32-79f5-3395-baec-08319775e0b0 | -4.80672 | -44.985 | 2024-12-03 00:13:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 7a627305-ecc4-3df4-83e5-2d94a1980145 | -4.1676 | -48.58577 | 2024-12-03 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| a355549c-3f71-3d14-a4a2-f4600d3a52be | -5.11211 | -43.22558 | 2024-12-03 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 041cfcfd-7add-32e2-b2c5-86d57f7b780c | -3.35084 | -44.36805 | 2024-12-03 00:13:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8a4ef811-8920-395b-886c-a373cd6b4802 | -5.45059 | -44.81793 | 2024-12-03 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 22b5c303-524a-3412-959a-6480fd4dcd3e | -2.9653 | -45.20692 | 2024-12-03 00:15:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 78351a7a-db57-34bb-a26a-e5131fd7fdd2 | -2.55414 | -45.34331 | 2024-12-03 00:15:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 87ed1fb4-c4bc-3f10-b17d-b38d48366e29 | -2.25393 | -46.02849 | 2024-12-03 00:15:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a6869338-60dd-36c7-a76c-a19a7c0e802d | -2.66031 | -44.99338 | 2024-12-03 00:15:00 | TERRA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 976d6d1d-1d28-3830-805d-db04eb592965 | -2.85536 | -45.82624 | 2024-12-03 00:15:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 29cd669d-fdab-3a77-b281-f0b9e04118bc | -2.29753 | -45.76845 | 2024-12-03 00:15:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 9d079f7c-178f-356c-b8b2-1ff4b293568e | -2.82144 | -45.48188 | 2024-12-03 00:15:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 9820dcc4-acee-3a60-807c-786b2d553f3b | -2.63734 | -45.76451 | 2024-12-03 00:15:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 27.1 |
| e758dbcf-7846-3908-a58a-fc59b104281e | -2.29966 | -46.37256 | 2024-12-03 00:15:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| ca19ad7a-8cd4-3d01-a842-794db01e8467 | -2.00769 | -45.75151 | 2024-12-03 00:15:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 39.3 |
| e2c8e3c1-c433-32b4-8d25-22f1508fc0b5 | -2.49576 | -45.5897 | 2024-12-03 00:15:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 31.6 |
| f7c11f61-27b0-35f5-ae20-42f8419735df | -2.33135 | -46.10334 | 2024-12-03 00:15:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8c2a9709-4cc5-3890-9d67-ff22d8472e3c | -2.2921 | -46.38028 | 2024-12-03 00:15:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 38.8 |
| b620eabf-8550-30c1-8290-2097e638c927 | -3.26878 | -46.9404 | 2024-12-03 00:15:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 62a12c1e-4eab-3d94-90f5-1dd08cee3fa5 | -2.64009 | -45.7846 | 2024-12-03 00:15:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6041cd7c-6772-3d98-a891-4645b93ccfda | -1.90355 | -46.61828 | 2024-12-03 00:15:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 9c303d5a-ec9c-3f8d-bf7f-42eb5389f643 | -2.73232 | -45.21341 | 2024-12-03 00:15:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 6b1de689-d76e-31a7-9736-3b4ce317aa9c | -2.85821 | -45.84675 | 2024-12-03 00:15:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 8a045ab6-cabb-37de-af8a-156218a08518 | -2.35384 | -45.70039 | 2024-12-03 00:15:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 559.7 |
| 60601212-3148-3515-a8e2-a6eff61f6c33 | -2.58209 | -46.03 | 2024-12-03 00:15:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 0b07cb3d-a46d-39e9-9472-a5c038c2116d | -2.48562 | -45.61082 | 2024-12-03 00:15:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 82266b93-354e-3f2e-b48d-6bd92c3a21c0 | -2.25713 | -46.03465 | 2024-12-03 00:15:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 19.9 |
| eee2c91c-4776-3611-9dec-655730c76e17 | -2.47278 | -47.23237 | 2024-12-03 00:15:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 2d664d1e-3e7e-3446-84a9-f89c76cb05ac | -2.28612 | -46.37449 | 2024-12-03 00:15:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 29.7 |
| c6efea34-efb3-3852-87e7-84125d0ec6f4 | -2.38863 | -45.57701 | 2024-12-03 00:15:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 91e6a3a5-35c3-3631-9706-612020581fea | -2.35654 | -45.72003 | 2024-12-03 00:15:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 272.6 |
| 907fd6ed-2106-3b83-821d-1417349862e4 | -2.48316 | -45.59672 | 2024-12-03 00:15:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 424d11d0-c283-3a9a-9543-f868c92e9013 | -2.96273 | -45.18854 | 2024-12-03 00:15:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| e7cf589a-06ec-33e3-8e08-07a37e85d6ea | -2.26931 | -45.45798 | 2024-12-03 00:15:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 36693d36-77ff-30ca-b7a8-94fa608f6d0c | -2.83415 | -45.48014 | 2024-12-03 00:15:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 7bbb7504-cee0-341c-bd4f-76d220030328 | -2.48302 | -45.59145 | 2024-12-03 00:15:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 8104d798-953b-399c-a673-9738958b622c | -1.82206 | -46.58847 | 2024-12-03 00:15:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 704bbf27-166b-386b-aecf-f5977f5c0c11 | -2.68382 | -46.62299 | 2024-12-03 00:15:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 20.3 |
| dbeb79f3-e109-3983-9734-18f6ee0a6daa | -2.96731 | -45.20111 | 2024-12-03 00:15:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| b8b20867-64f7-3b9d-9b77-fa8ab8f3caf9 | -2.65786 | -44.97588 | 2024-12-03 00:15:00 | TERRA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 814cd901-f933-305b-9095-0166cb1db3ee | -2.29877 | -45.77383 | 2024-12-03 00:15:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| e0e044be-df54-36e0-a407-cf6e9fada110 | -2.66198 | -44.96892 | 2024-12-03 00:15:00 | TERRA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 9dd65479-2b09-39c4-8f1e-98d01409ef31 | -2.82126 | -45.48737 | 2024-12-03 00:15:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 396ca4df-b1bb-3c74-b620-7cbe43272f5e | -2.01043 | -45.77119 | 2024-12-03 00:15:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 5d41f97d-9d20-3f05-a909-8cf540fe21db | -2.3888 | -45.57041 | 2024-12-03 00:15:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 24.3 |


[Clique aqui para ver as próximas entradas](README4.md)
