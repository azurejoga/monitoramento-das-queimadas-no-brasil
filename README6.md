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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9fd733e-4687-337b-a09c-6ae91e76b76b | -2.99274 | -40.38685 | 2024-12-24 04:12:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 063c0dfb-43f8-3ec7-8026-95970eeea1f7 | -2.7674 | -45.10186 | 2024-12-24 04:12:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 8a38e8ad-2827-3a94-9865-27e847d0cc07 | -2.76514 | -45.09331 | 2024-12-24 04:12:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 445a283d-0a05-3b33-84c6-bf27e0e18aac | -2.77159 | -45.09843 | 2024-12-24 04:12:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 24.1 |
| f314cf0a-4de3-3917-a1ee-16c83620313b | -1.64056 | -45.85343 | 2024-12-24 04:12:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 193d425d-6a48-358b-b453-a8c5495509d8 | -2.64324 | -46.10324 | 2024-12-24 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3496de06-6394-31bb-a5dc-c5ae1bc6d795 | -3.64123 | -40.47979 | 2024-12-24 04:12:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 49314c0f-39da-344c-8da8-6ad49b90610f | -2.08998 | -45.36745 | 2024-12-24 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| beb84fba-bf41-392b-bf36-9023f1351144 | -1.94254 | -44.78012 | 2024-12-24 04:12:00 | NPP-375D | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d64d9f0c-fbc8-3be2-a733-82d6337e5519 | -2.9621 | -40.29738 | 2024-12-24 04:12:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7a899809-9f26-328f-a23d-1c709fe0a766 | -2.41019 | -54.21332 | 2024-12-24 04:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a86ab6e4-c657-3190-8ae0-7eb30dc2bc37 | -5.38841 | -42.95417 | 2024-12-24 04:14:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3b24a511-6f4d-3de1-aa90-74d7f4e50f55 | -2.58185 | -51.92604 | 2024-12-24 04:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dff5dabc-8ab5-390b-8c59-e26153fb5265 | -6.21175 | -42.6423 | 2024-12-24 04:14:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 63f7bfa2-8c51-3926-a1cc-df2ff03ef05b | -2.83259 | -49.53095 | 2024-12-24 04:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3636d1cd-3063-38f9-b987-9c0f806afa54 | -6.92096 | -43.53056 | 2024-12-24 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb378481-554d-31bb-9d2f-57836c0f2292 | -6.93759 | -43.5332 | 2024-12-24 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31946fa7-6aad-358f-b7f4-7ab6ba28ea14 | -6.95035 | -43.53878 | 2024-12-24 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f936dbc-550d-3508-b9ea-99a91fb7b34a | -5.31204 | -45.4539 | 2024-12-24 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 639f873b-32cc-3295-8251-34d93ba573cb | -4.51032 | -42.06619 | 2024-12-24 04:14:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 8faf08f6-1698-3dbb-920f-583ad6ba44bc | -2.55502 | -54.76641 | 2024-12-24 04:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6068b6bf-6fdb-35e4-8e01-c682a361c69b | -3.03101 | -53.89839 | 2024-12-24 04:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 584aa913-f9cc-3502-9437-22da73c1e37c | -2.83727 | -49.53168 | 2024-12-24 04:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82b894e0-0a02-3d31-8275-7ee3ad1c69c4 | -7.88185 | -38.54752 | 2024-12-24 04:14:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 4faf7c02-e86c-3a4a-bf03-c0657a5dcfd8 | -3.02755 | -53.89648 | 2024-12-24 04:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdb32950-123d-3620-9c2d-4ddbc077ca5c | -6.91376 | -43.53299 | 2024-12-24 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9da5ebeb-dd9d-3bd1-b725-446486a34b25 | -7.38003 | -37.46428 | 2024-12-24 04:14:00 | NPP-375D | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0402b9cf-751b-3af3-87a6-fd245a531cbd | -2.58245 | -51.92241 | 2024-12-24 04:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aff81cd9-4001-36e7-9810-97a20831a349 | -3.43537 | -53.29197 | 2024-12-24 04:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 312f4a0c-179a-3f01-a7eb-a6c0e6dea88d | -3.02835 | -53.89166 | 2024-12-24 04:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3b17ab1-15f3-3215-a65d-657322798def | -6.23305 | -55.62309 | 2024-12-24 04:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 612c19a8-d207-356f-8d2a-b21f4eb354b1 | -5.4551 | -44.81139 | 2024-12-24 04:14:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adc72a3d-bb72-3334-871b-e58770344f77 | -7.88134 | -38.55111 | 2024-12-24 04:14:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e3fa1742-33d5-3708-be32-902dfee10b23 | -6.97198 | -43.55289 | 2024-12-24 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7bfc30b6-21ca-3292-b70d-db0ba2cd1dc6 | -3.43684 | -53.28323 | 2024-12-24 04:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12f8c809-ba30-3bfa-9f6c-45ecb4b0b1d1 | -2.92674 | -51.58205 | 2024-12-24 04:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01953417-47f8-3f2d-93c9-4eb4b07bc099 | -5.53331 | -42.84954 | 2024-12-24 04:14:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dc374fa5-0360-3704-8e9b-cff36593eedc | -5.3956 | -42.95176 | 2024-12-24 04:14:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5387c408-50fa-3b18-a573-458f82d367f9 | -5.98914 | -45.39639 | 2024-12-24 04:14:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ad03da8-9c3f-310e-a80b-0328d35b6d54 | -3.8388 | -41.55984 | 2024-12-24 04:14:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b0ab5da3-1737-3ea1-9209-71d3998b807b | -5.1292 | -49.40917 | 2024-12-24 04:14:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea14632b-595e-3f05-a280-4350b76f89a4 | -6.20842 | -42.64177 | 2024-12-24 04:14:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| aef973c9-8f34-3cb7-9d6e-bdd084495cac | -3.1337 | -52.12651 | 2024-12-24 04:14:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60ae7e69-41e8-3ccb-8ae0-d2d3bd34a260 | -6.91654 | -43.53699 | 2024-12-24 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 299eea43-f924-3c25-9299-611405ba1757 | -3.35146 | -53.21064 | 2024-12-24 04:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43dd1608-57a3-3ea3-b5a1-b7fd8c31d502 | -6.2265 | -55.62177 | 2024-12-24 04:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5817e87-3ca0-3601-b0af-505fc99168d7 | -2.86405 | -51.65828 | 2024-12-24 04:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a96428be-c2ab-3706-9265-b439bdb4d6da | -4.52356 | -45.82392 | 2024-12-24 04:14:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b71b3e37-a6d1-38d8-8780-947a2be85ece | -7.21286 | -39.94521 | 2024-12-24 04:14:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c0bb8035-1593-3a5e-9837-20e42a31700b | -3.03455 | -53.8928 | 2024-12-24 04:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e315c83a-d1b4-32f6-bfa2-2f0eedc1b99a | -5.45167 | -44.81083 | 2024-12-24 04:14:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6fc506c-60b4-303e-94e2-bc1f2698b0c0 | -5.7327 | -44.10681 | 2024-12-24 04:14:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26f63235-a372-3e7d-8a7b-2d30d7629c6d | -6.97531 | -43.55342 | 2024-12-24 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c52b370-56d5-3414-a21f-86c40c1ef2f9 | -6.25902 | -43.16238 | 2024-12-24 04:14:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9e4622f5-5016-3a3a-b861-fb5e6963d148 | -4.22518 | -44.31452 | 2024-12-24 04:14:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1b3ce71-c8e9-33fc-89f3-3a8966ae3f91 | -7.8961 | -37.57633 | 2024-12-24 04:14:00 | NPP-375D | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 872f54e5-7d9f-3026-a5a2-4dd0b1eb7629 | -5.64136 | -44.30379 | 2024-12-24 04:14:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a580759-3a04-356b-b87a-d1b2b1a9a230 | -5.87748 | -43.88016 | 2024-12-24 04:14:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c87e1b2-c9f0-394b-a43c-2e8d7e8fdabe | -7.38112 | -37.4668 | 2024-12-24 04:14:00 | NPP-375D | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 95872eed-36f5-3c12-86ef-94c739f3b0a2 | -7.9765 | -38.66899 | 2024-12-24 04:14:00 | NPP-375D | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 85efa59a-8947-3721-92ce-8cff0ea4a49e | -4.14637 | -43.64317 | 2024-12-24 04:14:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af90d723-23b7-3a1c-bd6a-508f92b8dca0 | -3.80654 | -51.03261 | 2024-12-24 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbca160f-a6de-34b3-b229-b1ee357ba4d2 | -5.39174 | -42.95469 | 2024-12-24 04:14:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 502939e6-8ccc-3f5d-9a64-f31bea20f336 | -4.57661 | -45.86227 | 2024-12-24 04:14:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efc80cb3-3754-3fb6-bc92-6672d562e4fc | -5.53609 | -42.85352 | 2024-12-24 04:14:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1e2f1af3-4656-368e-8620-f44819013be1 | -6.98535 | -43.27359 | 2024-12-24 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a9c31e99-d793-358b-9fc2-5b43a53d6041 | -5.37443 | -42.50429 | 2024-12-24 04:14:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fefb6191-3c65-3638-856b-2bf4fc83fa24 | -10.79757 | -36.95306 | 2024-12-24 04:14:00 | NPP-375D | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1c569ba7-5ac2-32c5-902c-d201d93fa5ec | -8.13064 | -43.13269 | 2024-12-24 04:14:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6be95dfa-9654-34cc-a867-6f7fc80e2d51 | -3.43612 | -53.28752 | 2024-12-24 04:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a75d9ecc-045f-307c-b804-1a269cb4deff | -4.57301 | -45.86165 | 2024-12-24 04:14:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad289199-b596-3c9e-9bcc-dd00e004e66d | -3.18606 | -45.97365 | 2024-12-24 04:14:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b6f023f-693d-32a7-ac0f-4fc2766a2747 | -4.42846 | -46.13643 | 2024-12-24 04:14:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb5365c7-dc80-3061-a5b9-54bf3ba4ccf6 | -2.86748 | -51.65887 | 2024-12-24 04:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4bd2b32-2cb4-36ff-8091-50de8533103f | -6.19618 | -42.63272 | 2024-12-24 04:14:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 830ba704-c72a-3263-9fc7-fe8d1906b8b6 | -6.64135 | -39.54493 | 2024-12-24 04:14:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0c60dc00-359f-319c-b134-cd44cadf9b0a | -4.43082 | -46.14029 | 2024-12-24 04:14:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d9a1fa8-3753-3da2-9d73-a312230413a4 | -5.39669 | -37.77882 | 2024-12-24 04:14:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 90c08f21-ab6d-3b04-88df-389664fe3778 | -6.9692 | -43.54889 | 2024-12-24 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dcccf43f-20f3-37f2-80ee-9f39b73a4f90 | -3.18537 | -45.97794 | 2024-12-24 04:14:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cca849e-43e4-3a4b-b84b-077424ef0c3e | -6.19951 | -42.63323 | 2024-12-24 04:14:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fb8f19be-cf26-3bb7-8b0a-f3409ea73163 | -3.8112 | -51.03612 | 2024-12-24 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28d6ad6d-e0fa-388b-ba06-f7debfdf7b95 | -4.53394 | -46.35463 | 2024-12-24 04:14:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 793d6eb4-395f-32e8-9a46-6be1cd945f48 | -3.03185 | -53.89359 | 2024-12-24 04:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36afb197-ebd3-353f-90fc-1b6224fa7836 | -4.52649 | -45.82862 | 2024-12-24 04:14:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0cc1e79-5888-3a96-936f-e9922070ebf4 | -5.39506 | -42.95522 | 2024-12-24 04:14:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2463c6d3-ec19-3765-a502-1f26575432b6 | -2.93643 | -49.43706 | 2024-12-24 04:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 547b75da-f070-3318-a509-f2be242b431a | -6.93482 | -43.52919 | 2024-12-24 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf35cd7c-1c6f-3311-86c9-ad612ba1cc92 | -2.58362 | -51.81245 | 2024-12-24 04:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11b978ae-18fc-35fd-adf9-cd123ad21b42 | -5.98692 | -45.38807 | 2024-12-24 04:14:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26f4ea8a-c055-3b6e-9cfe-5312587936b3 | -2.40932 | -54.21854 | 2024-12-24 04:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 45278f6c-b37a-3a89-aa10-81c3b88633d2 | -6.94702 | -43.53825 | 2024-12-24 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a92d5803-e2ef-38d5-b55c-f560a8a6f54d | -6.97586 | -43.54994 | 2024-12-24 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| addb01b5-017b-39f4-8a3c-85e6435461aa | -1.70746 | -54.48881 | 2024-12-24 04:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06efcd09-4ef0-31f8-90ff-8491bf0a5b77 | -5.53663 | -42.85006 | 2024-12-24 04:14:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| af48bd56-11de-3789-9aed-b7358ce94b60 | -7.24146 | -37.43425 | 2024-12-24 04:14:00 | NPP-375D | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8feab8aa-baf9-391a-baf7-6256a7f1cacb | -6.95367 | -43.5393 | 2024-12-24 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fc586a2-7bae-35b1-837e-026fb4d887c5 | -6.96975 | -43.54541 | 2024-12-24 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7696cbf-fe2e-35c6-abf6-1b474eec084e | -5.26558 | -40.66804 | 2024-12-24 04:14:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 14af10d7-0539-3696-9628-5309c2ce2caa | -6.19564 | -42.6362 | 2024-12-24 04:14:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |


[Clique aqui para ver as próximas entradas](README7.md)
