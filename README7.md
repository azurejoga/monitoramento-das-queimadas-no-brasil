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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b048af0-c0f6-39ff-ba39-26d35f65988b | -6.90831 | -43.59003 | 2025-10-21 03:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9228cebf-0b3b-3703-acf0-c65fd81f98d6 | -8.44349 | -36.2617 | 2025-10-21 03:34:00 | NPP-375D | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 02cf707d-dd74-332c-b62f-966a22c16769 | -6.90128 | -43.59362 | 2025-10-21 03:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 426652a7-c240-312c-9368-27ddd664e79a | -8.20754 | -35.8917 | 2025-10-21 03:34:00 | NPP-375D | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e010157a-fffd-367d-8144-0623a4057019 | -8.55849 | -36.51678 | 2025-10-21 03:34:00 | NPP-375D | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 9f8c1f0e-5e50-3bd7-b978-bb697a30d347 | -18.80066 | -47.01172 | 2025-10-21 03:36:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 928ad750-4b71-341c-8ca3-c6d5db767bfa | -18.79819 | -47.01443 | 2025-10-21 03:36:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0721055e-c2da-3cb9-bdce-34e6659e63a8 | -18.79939 | -47.00921 | 2025-10-21 03:36:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 16cadeec-5e44-3062-9ec5-8704685a4c3a | -18.80408 | -47.01688 | 2025-10-21 03:36:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fac3d168-37b4-34a3-a76c-0c1d1995f2af | -18.7995 | -47.0169 | 2025-10-21 03:36:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| da6f3fcf-6fab-3951-8837-97a5793731d2 | -18.79704 | -47.0194 | 2025-10-21 03:36:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 411895a0-07e5-39a7-8016-75b3dfd74766 | -18.44878 | -46.39507 | 2025-10-21 03:36:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85bf102c-5c5a-38fd-b03c-a6fb1d275fc7 | -20.42484 | -48.03856 | 2025-10-21 03:38:00 | NPP-375D | IPUÃ | SÃO PAULO | Brasil | 3521309 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eab137d8-7cf2-34a3-9622-4654aec3ec0a | -19.91161 | -44.35521 | 2025-10-21 03:38:00 | NPP-375D | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 87e7999d-126d-3d8c-b956-f62ce807f1ec | -20.43111 | -48.04019 | 2025-10-21 03:38:00 | NPP-375D | IPUÃ | SÃO PAULO | Brasil | 3521309 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 913e5b81-cac6-3042-a300-1d33121ea7e4 | -21.04001 | -44.67065 | 2025-10-21 03:38:00 | NPP-375D | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 02a85df2-c4f7-3557-9d96-cf1592240c90 | -20.02408 | -46.13491 | 2025-10-21 03:38:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1276379c-dc62-34b5-ae70-2f6fec0fb001 | -20.42704 | -48.03814 | 2025-10-21 03:38:00 | NPP-375D | IPUÃ | SÃO PAULO | Brasil | 3521309 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69e48419-f0cd-3f2a-8bca-c41cd2cbec5e | -19.91096 | -44.35834 | 2025-10-21 03:38:00 | NPP-375D | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b4e1bbad-836d-3d4e-bb66-179b54744e25 | -3.5153 | -45.8411 | 2025-10-21 03:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 5680721c-653a-36e8-a49b-3bbfc0f8a817 | -17.4135 | -55.0468 | 2025-10-21 03:40:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 101.1 |
| 51cc07ee-9dee-3539-94ef-a58dd11e12ec | -19.0915 | -57.5512 | 2025-10-21 03:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 71.2 |
| 3a8653f9-891f-37b8-86fb-586c07b3e639 | -3.4967 | -45.8418 | 2025-10-21 03:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 4924ea66-8609-3817-9f7e-88ecf626b67a | 1.7119 | -55.7051 | 2025-10-21 03:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 2a35bc5c-7d19-369a-9623-a729df4939d6 | 1.712 | -55.6854 | 2025-10-21 03:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| ec4c3cac-48df-3c7f-b74b-f33a17f9cce8 | 1.7486 | -55.6651 | 2025-10-21 03:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| ff6ca9fe-30fd-3af1-9897-21ce02bc7ef3 | -3.5154 | -45.8187 | 2025-10-21 03:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 1f81e670-8f91-3392-bf49-81a2f704e8d6 | -17.4131 | -55.0678 | 2025-10-21 03:40:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 129.3 |
| d1718ff8-43f7-3d56-bf35-45f555dbd39c | -10.9393 | -50.3407 | 2025-10-21 03:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 743fb5ee-c095-32fb-9770-ff526761dd01 | -3.4968 | -45.8195 | 2025-10-21 03:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 147.9 |
| 9f810cc9-070d-39d9-9bf2-57cc3f81d557 | 1.7303 | -55.6851 | 2025-10-21 03:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 1138e360-f499-329e-af82-41d81bb84e46 | 1.7486 | -55.6651 | 2025-10-21 03:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 3285832c-5862-3e80-937d-ea3a495bd5c5 | 1.712 | -55.6854 | 2025-10-21 03:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 58bf3b06-a696-3ca8-ba80-859c0011c829 | -3.4968 | -45.8195 | 2025-10-21 03:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 261.7 |
| ba75a7fb-aa60-3159-a7ce-dc20cb9096a9 | -3.4967 | -45.8418 | 2025-10-21 03:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 159.3 |
| defb028a-16ab-3a80-831f-351ad0f713b6 | -17.4332 | -55.0441 | 2025-10-21 03:50:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 82.4 |
| bad087d5-3d15-37b1-8106-9bb8b5714c02 | -17.4135 | -55.0468 | 2025-10-21 03:50:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 120.5 |
| 2f5eb582-a353-35d6-a27f-2493093f8deb | -3.5153 | -45.8411 | 2025-10-21 03:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 53262e57-e33b-3c2a-ae1b-89d74443bd74 | 1.7303 | -55.6654 | 2025-10-21 03:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| f2dc0f4b-d704-3fca-a3c7-8b76b011cbe3 | -3.5154 | -45.8187 | 2025-10-21 03:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 132.7 |
| ddd7dd40-b246-3316-9d87-f83c9b225b09 | -17.4131 | -55.0678 | 2025-10-21 03:50:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 118.4 |
| a1380790-098c-30db-bfe4-d11af5a94974 | -2.92788 | -48.30218 | 2025-10-21 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2b424bab-8055-3396-8d3d-78f1cc2a4abe | -2.71844 | -48.83467 | 2025-10-21 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a551bba-1b59-3048-aeb5-43e591068065 | -1.19833 | -49.08591 | 2025-10-21 03:51:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7ed16824-0220-34cd-8d75-6e857f2de58a | -3.96748 | -48.06519 | 2025-10-21 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6615f4d2-a9ee-3064-9d0d-a820aec7b468 | -3.50889 | -45.82914 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 35523924-c2ab-3b46-9322-5fb3b1bc0efe | -3.21185 | -43.33669 | 2025-10-21 03:51:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f5a8144-f63d-3ee7-8987-773ee28a604d | -4.24769 | -46.22336 | 2025-10-21 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0f0c9ae-8f34-39e5-a2ae-223257394a30 | -3.32457 | -50.23153 | 2025-10-21 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1c07571f-0853-32fe-abbd-e4f13812a128 | -3.50288 | -45.83413 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9c97bee7-8dcd-3101-bea6-608aacf2f7d4 | -4.54045 | -38.46721 | 2025-10-21 03:51:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 26de1f6c-1c99-35df-8d23-9046d126f673 | -3.2985 | -43.49966 | 2025-10-21 03:51:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71f20f2d-7523-31e0-98ff-de1087dfd994 | -1.19345 | -49.07969 | 2025-10-21 03:51:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| aa0da475-8c97-33c5-8119-3f969ed8bd41 | -2.95869 | -50.9995 | 2025-10-21 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a1cdf515-c5bf-3643-b542-3c30e3212097 | -3.5084 | -45.83209 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 59bd7b68-efa4-3736-884f-2746f835aada | -2.92714 | -48.30664 | 2025-10-21 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 3e0bb280-abd8-3acd-9a73-04ef9557fdf0 | -3.49833 | -45.83035 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5e7e6ede-340c-3f1e-81ff-6852b964c23f | -2.55786 | -47.65816 | 2025-10-21 03:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16fb47ff-6256-3fb8-9276-a9fbeba2114e | -2.86939 | -45.25193 | 2025-10-21 03:51:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c803f76-2265-3bd5-8e21-551f78bba4c7 | -2.22424 | -48.37368 | 2025-10-21 03:51:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18c9a3d1-e058-321f-b38a-882558337860 | -3.9965 | -43.28162 | 2025-10-21 03:51:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd55f14a-f8b0-352e-b154-abf48d0ffcff | -2.69326 | -49.55582 | 2025-10-21 03:51:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8984235b-3d3e-3bb9-9b18-19649bb41da7 | -3.96674 | -48.06944 | 2025-10-21 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 847cbb3f-ccd1-37f8-8919-e4528e79b969 | -3.49477 | -45.82075 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b5fc7f2e-d82e-3a74-8813-52941fa0b1c8 | -2.98891 | -39.96334 | 2025-10-21 03:51:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8672ff15-e7be-3aed-bd84-30f68f4d3e3e | -3.4933 | -45.82951 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 51d5eb4a-f80f-334d-b6ca-0fdc02794468 | -4.25983 | -40.28376 | 2025-10-21 03:51:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7f225add-3db0-307e-afee-7be7a90c258c | -3.50077 | -45.81583 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5165522e-62b2-331e-8e91-fdcfe1a4f6b6 | -2.84805 | -49.5475 | 2025-10-21 03:51:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a16e7c65-cfd2-3835-845b-75d0a98985a0 | -4.81323 | -42.76043 | 2025-10-21 03:51:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b5dfe815-f79f-3135-9230-18a554f61247 | -4.24552 | -46.21954 | 2025-10-21 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55f976bf-f740-3ac0-a5f9-0a6bbc7ce6ee | -1.19919 | -49.08057 | 2025-10-21 03:51:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f7f1d27f-41cf-3101-8bfa-1a68ed6ef451 | -3.49379 | -45.82659 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 63369f4d-afbf-34af-87e3-9b09b479e1b2 | -4.18904 | -42.98167 | 2025-10-21 03:51:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1233eb50-e522-38b5-9693-8d06d72b1b64 | -3.70271 | -38.86472 | 2025-10-21 03:51:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8828b150-288b-3bb6-85f2-31f2a85b6c96 | -3.49735 | -45.83624 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb95ad78-8a7d-3b44-b9c0-9aacc4dc7682 | -4.8178 | -42.75757 | 2025-10-21 03:51:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5daf1fc5-9516-340b-9bb7-39a2d58992d2 | -3.50338 | -45.83117 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ba3c25f9-f10e-3e21-ba89-4e2a801818f0 | -4.24822 | -46.22031 | 2025-10-21 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20c7d967-85eb-318b-a730-d7336d885576 | -3.49428 | -45.82368 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 7d294a37-4d03-3983-8ed2-30d550fac043 | -4.24501 | -46.22263 | 2025-10-21 03:51:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d2e26c3-01f7-324e-9ead-b4b2e7ac777e | -4.65874 | -44.12273 | 2025-10-21 03:51:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56d4f5a5-5700-34f3-a16c-89ab69ed004a | -3.66693 | -40.48229 | 2025-10-21 03:51:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 31327822-5620-367b-8f1f-dfe030f5caa9 | -3.49231 | -45.83537 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1dbcad44-302d-3c12-af63-ea305e551e63 | -3.59795 | -48.99582 | 2025-10-21 03:51:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb014e37-babb-388b-9214-0be03c0b8437 | -4.18844 | -42.98531 | 2025-10-21 03:51:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc453d16-f980-34c3-8232-bcf52a608e8e | -4.31906 | -38.12735 | 2025-10-21 03:51:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| f704bf25-8835-38af-8fce-dd3f03915be8 | -3.81146 | -43.32426 | 2025-10-21 03:51:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a33ba9f0-c3d0-3da6-98c1-d879e61dd216 | -2.77217 | -48.02135 | 2025-10-21 03:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a9216cbb-4a31-3b9c-bdea-9c94f5654839 | -4.39393 | -43.31371 | 2025-10-21 03:51:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3059a57-f6b6-3666-8f7e-cc81e1f74842 | -4.90818 | -38.93504 | 2025-10-21 03:51:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4085da85-43b4-387c-8bcf-7980ddba8f49 | -3.4998 | -45.82162 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| dfd5ee7e-c0de-3d5e-9aea-33b2f054a742 | -2.87319 | -50.71388 | 2025-10-21 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 572de20a-c459-3837-ba8e-1ecfe47e7bcc | -2.87304 | -50.71875 | 2025-10-21 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 167d8a5c-fd8f-3c28-9c40-cdc3b5f8542d | -3.99714 | -43.27777 | 2025-10-21 03:51:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d77c1788-7df4-37e3-a66d-ea269f8edabc | -2.85367 | -50.74398 | 2025-10-21 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cad5760d-58af-3e9b-a089-ff4f34fcdba1 | -3.97331 | -48.06602 | 2025-10-21 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38097396-341a-333b-ba52-737f4726c3fc | -3.49784 | -45.8333 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8f5d3b7a-0aa1-30f9-ae4a-ced696afdc24 | -3.50938 | -45.82624 | 2025-10-21 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a6820663-c87c-3766-8485-83ac0632ac3d | -4.81437 | -42.7534 | 2025-10-21 03:51:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README8.md)
