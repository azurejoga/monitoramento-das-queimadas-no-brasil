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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0dbc5c8f-8e54-3b03-9a13-2fd5bbe42457 | -7.67084 | -44.49947 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 61282ae1-957e-348c-927f-b9ffe9dcc63a | -3.73742 | -53.73589 | 2025-09-16 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7de5f77f-feb9-3205-b2d0-3eb9182df395 | -7.67709 | -46.29999 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 113d24da-f68f-3d7c-9888-b5487828dea8 | -6.82635 | -47.85728 | 2025-09-16 04:49:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a38d13b0-62b9-3b44-81bf-711d124559c0 | -5.98096 | -45.79427 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4d025e8-1f84-32b2-9b65-5553158a5513 | -3.64859 | -54.05147 | 2025-09-16 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 997a1cd2-f28f-3846-b00a-a5332d48dec7 | -8.11413 | -48.26964 | 2025-09-16 04:49:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2e51ae2d-2fca-34b9-8e59-087b0b4778a4 | -7.2765 | -46.59004 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dcab2af6-f0d0-3610-a0e8-74f94a7f3f52 | -5.97573 | -45.8307 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afd9331a-b9f4-3b70-9e26-66ac756676af | -8.20894 | -45.55117 | 2025-09-16 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3acf18ba-ebb4-3a01-8a58-5e62a23d0714 | -5.89803 | -45.75164 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbd227dd-6470-3197-8533-121d1e2d968b | -7.43867 | -46.17286 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b13e0764-7a91-3c5d-91d8-ccec7ced5617 | -5.11942 | -46.12894 | 2025-09-16 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2bb42ea-9b8d-3c66-b825-62824c7952d1 | -7.38937 | -49.99918 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b97e7727-77cd-3cdd-9c0b-04003c50c116 | -3.83085 | -44.11395 | 2025-09-16 04:49:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1132f206-9aad-3d56-bc5c-ee81d72774bd | -2.30593 | -48.14788 | 2025-09-16 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 760e96af-a0ba-35f9-a130-e9e4c02b2e94 | -7.39587 | -50.00429 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33bdd3dd-0b71-3934-bd2d-93071e4d86de | -3.57133 | -51.56219 | 2025-09-16 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 584313b7-a3e5-3de6-8fa8-c920c3be4b9d | -6.44785 | -43.31549 | 2025-09-16 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 518572ac-0c30-3425-95c7-e79869406120 | -3.48144 | -52.86166 | 2025-09-16 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d246c59-6d9e-34e4-9d04-170b9d10560e | -6.34507 | -43.1642 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1c49c9e-5fd9-3bda-a2c7-fa7916e16854 | -6.07699 | -49.5496 | 2025-09-16 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e2b5cde-0069-3079-a893-941c7585b341 | -6.18497 | -43.47262 | 2025-09-16 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a90009e5-1fda-3478-8f9c-b19ee0ce4c75 | -5.17218 | -50.77265 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f6f1078-4174-345c-a9ff-c487bf162589 | -3.17714 | -52.44657 | 2025-09-16 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 947c19da-936a-3e67-999b-b58e801faee8 | -3.8809 | -55.35555 | 2025-09-16 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73b733a4-ef78-357f-9b1a-fbd049853100 | -6.17808 | -41.21132 | 2025-09-16 04:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 23adebf7-8e9d-327d-9c0b-8c9e5beb2252 | -3.82911 | -52.29766 | 2025-09-16 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e397ee83-bacd-3eca-a9f1-7a253cdeaf2b | -5.67181 | -51.13921 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c16d0eb-7e16-37d0-bf17-02b2f8d53431 | -7.27035 | -46.60195 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 10f30ea7-a0ab-3a1e-9f31-7bfecd931eed | -7.51047 | -44.66584 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76e2e982-8602-3369-b241-2e8a9aa22513 | -4.18083 | -48.57206 | 2025-09-16 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 68f23c48-7c9d-3e2e-88a9-ec5936d6aeab | -5.76734 | -52.37084 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85bdd699-cb09-3507-add4-d062fa97c3aa | -7.13701 | -47.97698 | 2025-09-16 04:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a9ddc255-9310-3c83-983b-00f86e44dd0f | -3.21455 | -47.12178 | 2025-09-16 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7db88bd5-417a-3beb-b56a-6fb8cef2a35d | -5.34402 | -44.81482 | 2025-09-16 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f748c61-b67f-3ec9-9c6f-f02128fe175e | -7.28028 | -46.59472 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a6330b4-f95b-3817-a00c-f18273bb4f4e | -8.11487 | -48.2645 | 2025-09-16 04:49:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c01a9438-ae52-3738-a549-0bfc2e4947ce | -7.69479 | -44.66068 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d32add4-8cae-3779-a3b5-458179f1d057 | -7.05741 | -44.17202 | 2025-09-16 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c339ce12-1171-3313-8c4a-543fcc75b7b0 | -7.71628 | -45.3059 | 2025-09-16 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3d42b6de-3cf5-32bc-b84d-4fa7bcfab942 | -7.44508 | -46.15996 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0bca52c7-2597-381c-ad65-565488589801 | -7.38314 | -49.99551 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71f18ba4-c74a-3daa-b96e-9e91fb8e122c | -3.8047 | -41.57135 | 2025-09-16 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 593453a0-d9f5-3aa3-a804-8a6a6ea85dd4 | -5.89747 | -49.10455 | 2025-09-16 04:49:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26859026-039a-33e1-ac76-51c2fbcf8712 | -6.46609 | -46.00701 | 2025-09-16 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8bb0bfc3-f24c-3ccb-bd69-5b514b29a587 | -6.0955 | -46.49546 | 2025-09-16 04:49:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65652cc1-9ac2-3df2-a786-6f6f4a9545fc | -6.52546 | -51.19324 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b9d0373-a080-34c8-920c-2c0b9c5aa31d | -4.06172 | -46.94083 | 2025-09-16 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 866cc0ce-caad-361f-9071-0c45585bb223 | -7.79138 | -46.15786 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3472242-569b-31e4-b792-b84c16089dbb | -7.40418 | -49.99733 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93b380ac-9406-3ea3-9df4-466e366ca420 | -6.35099 | -43.16156 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ec7ab69-0660-363e-a40e-63659ec2e9f2 | -3.83981 | -44.09999 | 2025-09-16 04:49:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd331301-31eb-3985-a297-39947442c789 | -3.48647 | -52.80862 | 2025-09-16 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 964f7207-bada-38b9-b299-5bd8e66fa210 | -7.13611 | -47.9725 | 2025-09-16 04:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4bef8acb-b21a-3630-a283-543813e01062 | -7.66317 | -44.47988 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1cf8910a-8f82-3589-aa2e-3870bf5d2988 | -4.06226 | -46.93721 | 2025-09-16 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f459288b-9a3b-34ba-8151-6a650bcebb7f | -2.0735 | -52.71967 | 2025-09-16 04:49:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2988143-8818-34ed-8526-150fc3f547e4 | -6.18942 | -45.12163 | 2025-09-16 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 377e6f03-1da1-3411-9ad2-394281d4a1e4 | -6.17974 | -41.20473 | 2025-09-16 04:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f328a889-a276-37c1-8790-2a54474aecc0 | -7.13861 | -47.9834 | 2025-09-16 04:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ed7b2f73-ba0f-3c37-beae-a315f027eb3b | -7.44959 | -46.16057 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9655baae-562c-3148-804a-186c24b1d449 | -6.18864 | -41.1863 | 2025-09-16 04:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6007ccee-01bf-3342-b8be-a8a75a1b249f | -7.06292 | -44.17006 | 2025-09-16 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| def7ffed-3fbe-3a2a-97f6-bf52b2b17e46 | -6.35148 | -43.158 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f24f926-b7d6-32b9-9e00-4f74297d3b94 | -6.40328 | -42.6544 | 2025-09-16 04:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ab602fff-137a-37d4-aa20-a31c817da4a3 | -3.75096 | -51.80251 | 2025-09-16 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b7afc75-9ce4-3d63-bcf4-2cb17667f0c1 | -7.40599 | -49.9852 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae8159ef-8fe3-3caf-9081-8e277a71ea90 | -5.77747 | -45.90207 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ee25117-a774-3c1c-9026-940ed947864f | -7.56218 | -50.46064 | 2025-09-16 04:49:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 144f60ff-b350-31f8-9f78-30eaa55cc051 | -6.98486 | -44.77353 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 070ffe4e-ba67-3574-a027-744ee9b45240 | -7.1402 | -47.98269 | 2025-09-16 04:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| dad0b1a5-f4f2-34ba-b51f-6eea8400da03 | -8.12672 | -48.26626 | 2025-09-16 04:49:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a9569e72-e1d6-36b5-8877-5c256f3d20a0 | -7.46121 | -46.14355 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed135d3f-add2-3436-b52c-67c3b3ff7d8c | -2.64606 | -48.0517 | 2025-09-16 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a252f53-b25a-377a-a889-2adbbb536020 | -5.83502 | -44.16034 | 2025-09-16 04:49:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0168c410-3527-3397-831f-5fb0199c5c41 | -7.99206 | -45.66721 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d8a6864-a21e-3832-b9a2-a674a0b0eaa9 | -7.08252 | -44.54765 | 2025-09-16 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| facb2022-358d-30d4-9380-bfa79a1d7d1e | -7.71076 | -45.31036 | 2025-09-16 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9e83fce2-81f7-3731-bf74-17738e9e1032 | -8.08653 | -46.83004 | 2025-09-16 04:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab5a4003-aa50-3406-a384-c229637caefc | -3.83659 | -44.10923 | 2025-09-16 04:49:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 156a2671-e1ee-36e4-93bd-01f3620b1d83 | -6.82607 | -47.83207 | 2025-09-16 04:49:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d1e638a-92bd-3378-83cb-2c8fd1c20d05 | -5.53228 | -42.65617 | 2025-09-16 04:49:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 1505e6ca-2205-3fc6-aa83-66abc1995b95 | -5.99862 | -43.69663 | 2025-09-16 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28182a3b-3e63-39b8-a3be-1b38acea43d4 | -3.73659 | -49.0461 | 2025-09-16 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1aa51cb0-e903-3eef-beae-0220b662ade6 | -5.93385 | -45.19039 | 2025-09-16 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6786f10-5c30-372c-b7d3-ce2ec20cbf8f | -7.68209 | -44.67844 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 177a1760-e8f4-3c76-bfaa-316d72812136 | -5.79337 | -45.91811 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f76749f-b546-32d2-8a33-263e62e8c0fe | -6.83185 | -47.84782 | 2025-09-16 04:49:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d93361e9-9ae6-32e8-afbe-d180c0a57485 | -7.43439 | -45.84012 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f28f62b-60a6-3777-9e35-75f362f3890d | -4.60052 | -43.32194 | 2025-09-16 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f7f2bf7-3c6e-3c3e-9ace-da6fa8edc5e6 | -6.34604 | -43.15718 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4da2eb03-1b07-3313-8988-df77d68bac09 | -6.5453 | -44.00352 | 2025-09-16 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58a6001f-1e07-3f37-83b2-be5498432d7f | -7.38607 | -50.00009 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b392dcd-4db9-3190-95f7-a76ae0594ff4 | -8.4223 | -45.7477 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 960a669b-402c-3243-bb5c-a2f9572141aa | -7.71797 | -50.35987 | 2025-09-16 04:49:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6cecfafd-e731-3c40-a720-b4c344cb4a48 | -5.09537 | -43.83093 | 2025-09-16 04:49:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3600cac-42b4-3c90-b363-2592d72261ae | -5.79272 | -45.92256 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a6d9724-6a70-3d92-b513-2195f88d22fd | -6.17479 | -46.81285 | 2025-09-16 04:49:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da9bb494-e784-3b2d-82f1-13c3da26bc12 | -3.52865 | -49.96615 | 2025-09-16 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README67.md)
