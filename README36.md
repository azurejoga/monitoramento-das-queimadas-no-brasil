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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c42af812-b2ce-319f-a665-41aeaea89ebb | -5.78321 | -57.61041 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ee34892b-9656-3865-a073-c17dc5777dc9 | -8.07382 | -44.64522 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 97d807b5-12cb-3b1f-ad26-83ce98661810 | -4.47312 | -54.80926 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0be7cfaf-2f1b-3281-b0b7-05046a2c7c85 | -8.22232 | -54.99756 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28c96436-76e4-3346-804e-2080cd2cd2a5 | -9.68892 | -46.05327 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9904df9-04db-3fdc-8581-6a4b27f6bf7c | -6.32555 | -44.8551 | 2026-08-25 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bcabd58-6f89-35b5-9fcf-48eddff26af0 | -5.9361 | -57.73693 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79e66f0a-2a00-3bb3-9226-653fd027842a | -6.35277 | -54.76173 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e118ff6-64b4-30e5-9da3-551cb271d693 | -6.33136 | -54.7627 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30214430-8c35-35a2-8d12-15252df09b7c | -6.97217 | -43.76125 | 2026-08-25 04:25:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35cd8f92-8a92-3850-85c1-916ee5c7822c | -6.34451 | -54.77556 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfdb6ef2-bda3-3e49-873b-9fa50cf1bcaa | -6.84186 | -52.50806 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 538ff69b-2ad7-3b4e-9d2b-b69cde71bd46 | -6.4464 | -41.55217 | 2026-08-25 04:25:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6aa1a9ce-4731-3677-bca1-d11705887d15 | -6.32692 | -54.74559 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3632f159-8cc2-33b8-89f2-3dfac42228e2 | -6.0954 | -53.41693 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e64ab5d-b7c8-39df-a4f0-f7865c30ca54 | -6.4345 | -54.97086 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bbf2921c-9dc2-3eb5-9aed-740e9cad6ff4 | -8.60404 | -47.44455 | 2026-08-25 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3636fbc4-08b7-3fe8-a118-0dd3fd7773bc | -8.21811 | -54.98931 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b14c1c63-8775-3752-9f5c-6a5f5065f342 | -6.1483 | -57.70691 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8a0e82e4-c5ff-325a-9023-9672eb5a83f0 | -7.19714 | -42.75343 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 96afe911-264f-374a-b028-dbd9013df41b | -8.07659 | -44.64925 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c25475f1-e3cf-3cd7-9e9e-0c9f327ca2ab | -5.52304 | -46.60995 | 2026-08-25 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21206cc4-30db-3a9c-9421-fd064b05c363 | -7.14796 | -42.74969 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a2de779f-61e3-3588-83cb-375ecf4098b6 | -8.59031 | -47.44222 | 2026-08-25 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b1c5842c-05bb-3f69-b68a-6b6a09fc9493 | -8.59504 | -54.7386 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fca46dfd-5cac-309d-a1fd-bec88ece33f7 | -3.54189 | -48.17979 | 2026-08-25 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 11592388-5ca9-38f2-83b1-06e400b694b1 | -9.9607 | -48.32057 | 2026-08-25 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8849dc0-c78a-3631-bea2-77d7fd1f7873 | -6.33201 | -54.75897 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e2700cd-ab56-3ccd-a21f-efe7f7835909 | -6.19101 | -53.48736 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6062c9e-2540-3749-98c0-780a871ed3ba | -10.71326 | -47.76324 | 2026-08-25 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4be1b202-d3ff-38aa-bfdd-dad9f1dbd303 | -11.30508 | -41.8828 | 2026-08-25 04:25:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e0126717-c691-3772-9679-c7a382669ebf | -3.53884 | -48.17464 | 2026-08-25 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| f5a9d505-9815-3c23-b18b-49e030f48193 | -8.11135 | -47.47861 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c2d95cd-6355-3613-a5c0-262c197ed3a6 | -6.22279 | -55.48039 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8a8ba18-d17a-3a6e-8d7e-28e8babd8650 | -9.60758 | -35.90155 | 2026-08-25 04:25:00 | NOAA-20 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| fe6cd6bd-612b-3718-85dc-74d55ff01a28 | -6.17835 | -53.52964 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f54f5b3-e013-3014-b251-5ee16939defc | -6.35362 | -54.78898 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fbdc60c-5fc9-3fa2-99ce-01460d6d7108 | -7.27805 | -45.36177 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 84db582f-004c-3dad-9c9e-571edbc9f751 | -6.4415 | -54.96434 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68e473a1-128d-36eb-92fe-238aa840ad1d | -7.4406 | -43.10321 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 49c8b9c1-d7e2-3856-a671-5286a8386c07 | -6.29903 | -43.7951 | 2026-08-25 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54eac5aa-9a67-3f90-b5b3-4ceed3125f6c | -6.24095 | -43.70636 | 2026-08-25 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb0799da-7151-3b1e-a00f-42119ff8a349 | -7.2626 | -45.37352 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 82cedf7e-a489-3c4e-a78f-9df463a01825 | -7.76085 | -46.14859 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a842027c-6f58-3aea-9572-1ffa332c9438 | -8.76543 | -45.79298 | 2026-08-25 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac49c520-0c77-384f-9eb4-ca4f92b967d8 | -5.34297 | -45.35135 | 2026-08-25 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98282cdf-d50c-3766-b59e-40902fc97b33 | -11.14124 | -44.47338 | 2026-08-25 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a2e8c638-bc1f-3f84-b772-43cfa9a32cf7 | -6.83453 | -52.49702 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 65f3bce4-1619-3b38-89a9-70b37a84b8d4 | -8.57441 | -54.84867 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 32f18d23-a68d-3fb2-a245-303ba116d46d | -6.17778 | -55.43556 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 86802452-244a-3945-a453-cdd3e69adcb3 | -6.93993 | -52.79271 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75a5fd3f-411b-3a51-83b5-f2e046e26830 | -7.27749 | -45.36523 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c4b06d0-d893-38f5-be28-7a5f706f91e6 | -7.24832 | -43.1246 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b53aa4ca-dc8f-3dff-a1c5-efead9ee5f8c | -7.70175 | -38.1611 | 2026-08-25 04:25:00 | NOAA-20 | MANAÍRA | PARAÍBA | Brasil | 2509008 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ac73cf7d-0731-3eba-a0cd-a2d971244352 | -6.25821 | -55.4178 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3d3aa88-94bf-3408-ba5d-802a95bf8067 | -7.8953 | -46.388 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 222fc7ca-87db-391d-b3b4-686362057120 | -7.90485 | -46.37137 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c7fdfbb-3949-3fec-b8c4-f76e1a262190 | -6.0117 | -57.66559 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bba5743-5b7a-3845-b39b-3b25dc7a0dfc | -7.06164 | -42.92766 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 19fc65b4-37f6-3946-8755-73a3bce58f2c | -7.26446 | -45.85228 | 2026-08-25 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a03ae3c6-64c0-3692-8947-b2e54595f4ff | -8.58969 | -47.446 | 2026-08-25 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5ad4bdc7-d613-3612-9fdf-ee6ad0eafe34 | -6.18641 | -53.48337 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f94e48d-6751-3768-a65f-d0b90a8e401c | -6.16963 | -53.70313 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00b8d6ee-3af9-35f6-aa3f-39c20d9a12e6 | -3.53507 | -48.17406 | 2026-08-25 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 17e97936-43a0-34c1-9554-5d2290aed9eb | -6.32839 | -54.74677 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc472740-eb5f-3307-b0e4-c03f3bc401c2 | -6.22711 | -55.48991 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fd75416-23dc-384d-97bc-c518e8e858bc | -6.18351 | -53.53056 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0f7a4b7-ae75-3ae9-b093-79d0f5a9f315 | -3.54171 | -48.18215 | 2026-08-25 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 5f46bae2-f37b-36ed-9b43-2d5b464d62c5 | -8.08723 | -47.51794 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 944b6317-1c84-380f-b281-153f19963bc1 | -10.37156 | -45.0619 | 2026-08-25 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5f45d200-f3c0-3240-8be8-370d0b7ec9be | -9.63973 | -48.33078 | 2026-08-25 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4242271e-e427-3126-8089-2a5dc7574189 | -6.32224 | -44.85458 | 2026-08-25 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c15adb16-6bfc-32c7-bbbe-94425ab81d6d | -8.09153 | -51.6782 | 2026-08-25 04:25:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6cf93e16-bb27-3889-959d-e2edc5ee0a07 | -11.1373 | -44.47651 | 2026-08-25 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 35fa50fe-04e3-396f-8fec-8b18722cd9a8 | -7.90371 | -46.37849 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a41bdf4-e316-31e6-b7ec-4f73dbbe9563 | -7.13926 | -42.76022 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 86225d9b-db4d-33a5-8c02-e2692d231d3f | -7.14449 | -42.74915 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8864634b-11d9-3f3c-bd96-944d3f8d78fd | -9.44535 | -51.58757 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80d1a7f8-7d11-3cb9-8b68-9064015b43e8 | -7.24948 | -45.86065 | 2026-08-25 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e9b32ad7-8571-384f-af3b-47e4a8d141d3 | -5.77554 | -45.79456 | 2026-08-25 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 288d62f1-a11c-391d-8606-42200511e6e0 | -7.48851 | -55.35561 | 2026-08-25 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4be87e81-6bcd-36b5-83d9-2b5d29349a9b | -7.29899 | -43.00193 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a9ef3953-73cd-3980-8fc9-c445401f3bb9 | -6.35565 | -54.7777 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 612f79da-f8e0-306b-b226-ad54f9442dd5 | -7.88998 | -46.33592 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b864dba-ca59-3303-9b9d-36766c8eff70 | -4.47443 | -54.80513 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 012e3dc1-424e-346a-80c1-75c4e337f26b | -7.48728 | -44.4667 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24b5a5da-22c0-3e2f-9338-4e8655c84331 | -6.44879 | -41.56116 | 2026-08-25 04:25:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d33259db-6042-3576-b906-ac9c9ac77282 | -3.04374 | -48.98368 | 2026-08-25 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ce32910-f493-329a-a6df-e29fcc8dff79 | -8.54101 | -55.30173 | 2026-08-25 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f3f4e16-9d42-3603-aa3b-afd97b08f1e0 | -7.31342 | -42.97238 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 69e2463c-64b1-315d-a56c-b90695023250 | -7.32051 | -46.13964 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 13d64c6c-ebe7-3c7a-b1f3-34e2411d9f6f | -9.04897 | -50.78878 | 2026-08-25 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7f20b1b-e5d1-3e27-a2c9-47b321b8d114 | -6.20075 | -53.49226 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4acc7710-5b2f-3d0c-9e81-f960d203dd17 | -8.15734 | -46.69898 | 2026-08-25 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fb0f214-8e90-3e39-ba61-da5bfd8ea89d | -8.22218 | -54.99818 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9bac57d4-ef4c-388c-85fa-59f2f24cbda4 | -3.00883 | -51.05011 | 2026-08-25 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa61b42f-a58b-3459-9308-ab8be9c1ed57 | -10.30266 | -48.20574 | 2026-08-25 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32ca42af-dc6e-3ddb-acd0-e3e48218a19c | -7.28301 | -44.07837 | 2026-08-25 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 231caf24-7a63-3001-b514-4b3740b65ca0 | -3.72724 | -50.16411 | 2026-08-25 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5475acec-ec37-381c-8e38-2885f16d591a | -7.26113 | -45.85175 | 2026-08-25 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |


[Clique aqui para ver as próximas entradas](README37.md)
