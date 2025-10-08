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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af5934c2-b1df-340a-8773-11ecb73947b4 | -11.14427 | -47.75021 | 2025-10-08 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5cf2fde-4e02-35f7-a6b0-1520c571122f | -13.36035 | -47.55678 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a24505f4-6bb9-3cc2-826d-2e7de7358e0a | -9.79583 | -47.74082 | 2025-10-08 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c7da124f-d9c9-3e4f-82b8-ff3f9e0232ba | -3.11393 | -48.78585 | 2025-10-08 03:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05708b5e-802d-3ea5-b4db-4d1986bfd50d | -14.79574 | -41.62646 | 2025-10-08 03:49:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f085c50c-791a-3df2-a24d-32137a13b0fa | -8.22716 | -44.16887 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e9261eba-d0f1-32af-a369-41e57b196fb3 | -8.61255 | -44.90483 | 2025-10-08 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 08794abe-c635-32ab-8cc4-171acebbbf91 | -11.15064 | -47.7466 | 2025-10-08 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdc58b6d-0eb4-3e32-a29d-5999845ff62c | -8.23071 | -44.17163 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f3a85f95-b512-3e88-9ef8-1163d3506ea7 | -12.93441 | -46.85631 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| fe375c29-c493-3f4e-941d-edeaa6098348 | -13.39411 | -42.70039 | 2025-10-08 03:49:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ca2e13cc-0224-34b7-b206-f1e58b80a512 | -12.0252 | -45.20645 | 2025-10-08 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 60766c47-c9b4-3825-bbdb-7472c9ac6544 | -14.36422 | -45.24028 | 2025-10-08 03:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46f695d8-7747-3d47-925f-4881cbed7ffc | -13.80215 | -45.80838 | 2025-10-08 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 432fe652-f226-3ba5-986d-aa7d7c7d342a | -12.23483 | -43.77915 | 2025-10-08 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eca98fc9-dd41-363c-bb3f-34260b70823e | -13.7341 | -45.7135 | 2025-10-08 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b8cf3ccf-ca98-3b40-9eb5-4b4d89732c08 | -11.72746 | -50.96108 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 27.3 |
| bc5027b5-3117-3352-941f-cbdf0fa0ebcd | -9.18318 | -47.80033 | 2025-10-08 03:49:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 67769b01-69fa-33f1-862f-e1b62069ee85 | -3.34977 | -42.32734 | 2025-10-08 03:49:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e55d309-9334-3022-9991-fbcb2785f0bb | -12.39332 | -51.13255 | 2025-10-08 03:49:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 41705be8-72f0-3aa1-8616-5448fb119004 | -13.30537 | -48.02725 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6becbdab-9cca-3313-90ce-aef2486ed5c7 | -9.77478 | -48.29071 | 2025-10-08 03:49:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab3e6a5d-dd6c-3274-918d-cbd6fde88a63 | -11.69316 | -50.96018 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e4affe93-b7a2-3296-bae4-c5ebdbcd66d6 | -8.18469 | -43.33455 | 2025-10-08 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| afd57f54-f2f8-38a3-a1ea-7ad24d5e2162 | -9.39392 | -45.93823 | 2025-10-08 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3eaf70e8-d386-3613-9273-07c95f0aad33 | -14.96107 | -46.82646 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68302b47-40b1-3d6f-a109-5b44413d5019 | -11.78316 | -45.05682 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08cb7e66-f4e5-3a20-bba8-2905d6caddba | -8.51917 | -46.28196 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4748926-a1f1-31fa-8dfb-6194a324df54 | -11.72991 | -50.94934 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 6d68871d-8d0d-36cb-b4c9-0a0671700ec3 | -10.04646 | -48.28295 | 2025-10-08 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81cfe322-ad2d-3131-9f9e-b96d20840ee9 | -9.97808 | -48.78461 | 2025-10-08 03:49:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 08aef28d-1ed5-37c1-af83-43a13d00513a | -9.00292 | -45.5042 | 2025-10-08 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59c8d6c1-df17-352d-9a29-18c7f100ea36 | -15.07412 | -46.62587 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2c2d9c29-90cc-3278-9cb8-791bf8088f7d | -12.25075 | -47.87052 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 73b94a46-ba8d-3c21-acd2-a6bc3e19077f | -8.56026 | -46.2361 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 106b5299-236a-3b63-a48e-cc45d7b5ca1e | -13.29031 | -48.4785 | 2025-10-08 03:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b78313c-5dee-3c6e-a484-79179a012c52 | -14.69051 | -48.41633 | 2025-10-08 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 573a9d1c-0c9d-3843-9f63-eb6d608cc7eb | -3.23702 | -46.78815 | 2025-10-08 03:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0f10dcc-4e86-3e80-b31c-34a5df507299 | -12.94609 | -46.84959 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3b1d678a-abda-3cad-8fa1-db4b34e7118b | -14.72094 | -46.03312 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f169179a-b026-3d03-93f8-f3fecf299b0e | -2.14564 | -47.50532 | 2025-10-08 03:49:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e44e2344-8e31-3bbf-8d89-d99791dc5ec9 | -15.94469 | -42.59833 | 2025-10-08 03:49:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 82a1c96e-3685-3473-8ee4-88375c9c7fac | -11.78847 | -45.0535 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49c1f353-d266-3c23-95c1-78265977d00c | -3.44539 | -45.59546 | 2025-10-08 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f72d1302-0345-38ef-8725-62fa2de7e822 | -13.06156 | -47.95264 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5159f63c-89dd-3bc5-b882-87401a295910 | -8.47327 | -46.29694 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 11de97fc-af13-321c-be12-60cb9862884e | -3.29074 | -42.62698 | 2025-10-08 03:49:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2595a659-c7ef-3356-92dc-7063fa1962b2 | -15.94835 | -42.59897 | 2025-10-08 03:49:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 91a40862-f86e-37a2-8200-2803ca17c0e7 | -14.79033 | -42.33298 | 2025-10-08 03:49:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| df24e6c0-7b10-30ce-a346-9b804cef0d44 | -8.93326 | -46.59464 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3ef4f0c-4f24-3240-b643-680acd94cabc | -10.22408 | -48.17368 | 2025-10-08 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| beba521e-97b7-3aa1-8eab-d8c641d51d81 | -10.41851 | -48.09434 | 2025-10-08 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab775dfc-a091-3160-bf2d-e53126f570b7 | -13.07291 | -48.01006 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6093f4d9-dea2-3b46-9fa9-e7d227f21ce0 | -13.32913 | -48.02024 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f65f42ed-c27d-37e5-b65f-be129d9e4f67 | -10.50379 | -49.14249 | 2025-10-08 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3ed70cc-b309-370d-91d9-4dc7db92ccbb | -13.27129 | -48.04771 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 98746fe9-2a58-3631-9966-d862b4b153ab | -11.72085 | -50.95972 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 39.0 |
| d4665718-f10b-34da-aa63-d321cfb00293 | -14.69773 | -46.08024 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ceb54ec6-9a4b-33fa-b45f-5421df79fd5b | -15.66743 | -43.65586 | 2025-10-08 03:49:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19ffac28-30db-3dac-9738-2589fe3590d2 | -15.24187 | -46.36389 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e72e6466-4237-3795-b865-683e1712245b | -13.29172 | -48.03959 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c5b4f4c-7694-3acb-aa0e-42f8feba64b9 | -3.45684 | -45.59375 | 2025-10-08 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e372292-baf9-351e-955d-37b0a8afe998 | -3.24151 | -46.78732 | 2025-10-08 03:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 22e4e22c-de3d-353b-b1fc-117d989b1b70 | -14.74587 | -47.86372 | 2025-10-08 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ead5142-5e67-327a-836d-91b2bea9db6a | -9.17551 | -46.92043 | 2025-10-08 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a8bc631c-6aaa-3e75-9e90-86a2f6187f8d | -13.27749 | -48.04459 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bacdf04b-313b-338e-8f3f-fc9b532adf23 | -8.12235 | -44.77446 | 2025-10-08 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4d765526-46bf-3a0c-8462-24b626044db2 | -12.33405 | -45.35356 | 2025-10-08 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8e65d810-bc86-33f3-9055-b4c2152d15a2 | -14.40566 | -39.84035 | 2025-10-08 03:49:00 | NOAA-21 | DÁRIO MEIRA | BAHIA | Brasil | 2910008 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 43bd6996-83a1-3fbe-b2eb-9734ca21889e | -14.71252 | -46.07802 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 744eeb9f-a122-3268-a876-8b5dbca12a4a | -15.25164 | -46.35212 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6396041d-d211-34c6-b6c0-95195183542b | -8.47617 | -46.2808 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 232bbe3e-f7ff-3e27-9bae-09561585285f | -13.25489 | -47.78947 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 142981b8-d9d8-3990-b62c-0758b761de5f | -2.52375 | -44.1233 | 2025-10-08 03:49:00 | NOAA-21 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 579356a6-d332-3dac-b830-ca82bbc4d024 | -11.45546 | -50.21271 | 2025-10-08 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7fe7fa4a-fcf9-30f9-a6a2-7ce46b2ed18d | -14.70496 | -48.39993 | 2025-10-08 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fdcf1cee-5ecf-3f90-b143-3a8e2a30e92f | -14.71166 | -46.05709 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c552f11-dfa1-3d88-beee-d11b881afef5 | -15.19241 | -43.73373 | 2025-10-08 03:49:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1494fc5b-ae09-376f-b7c5-132ec8022b83 | -12.11973 | -45.12956 | 2025-10-08 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cdf6720e-206b-3a1a-9514-2ad961b7b4c1 | -13.26222 | -48.04692 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13d0f9a3-b4ce-3add-bf25-44eff296a47f | -14.9339 | -46.79186 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2645c549-47f3-321e-9572-060b85ec25d5 | -12.41784 | -45.62212 | 2025-10-08 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a1ca2a73-1354-3786-b077-895e7f7dfc37 | -11.99764 | -46.77108 | 2025-10-08 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0cf92099-f408-3d3e-893e-1c9852e21954 | -13.06895 | -48.01109 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af984662-5f5d-3805-b556-064f6aeabb9a | -13.06463 | -43.59462 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 74f3a56d-b413-300d-898a-fb712a41e630 | -14.94969 | -46.80769 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9b644fb-bb34-3e7d-8442-2a25a3d4119b | -13.08455 | -47.93294 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 905f28f3-9186-3944-80c6-f33364d89cf8 | -8.79222 | -48.00059 | 2025-10-08 03:49:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d81b3d2-34e8-3e40-8b9d-8b5bbb8ffd6f | -3.24078 | -46.79156 | 2025-10-08 03:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0eed1642-dc62-32c5-bec6-6c11d82589ce | -14.908 | -46.82275 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2a25eb2b-2569-39bc-a90d-cdc084af0dbd | -10.53122 | -42.76779 | 2025-10-08 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3e3116b8-e8d6-312a-987e-7b32135735bb | -10.73467 | -47.65643 | 2025-10-08 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a750c126-8453-3d71-b922-cf7fec68e030 | -11.45757 | -50.202 | 2025-10-08 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7ee145b5-3462-3b33-9ad7-d811972da7f6 | -10.88629 | -47.10073 | 2025-10-08 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 94a05bc6-40e7-342f-851f-d02a4d7433a6 | -13.25383 | -46.47509 | 2025-10-08 03:49:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a9efdb5-b2dd-3845-9594-c80dd5887403 | -11.68006 | -50.96864 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0f430f59-70d1-3a1a-ba3d-aa08a4b1956c | -8.40959 | -46.80511 | 2025-10-08 03:49:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 923a0266-0a18-378f-a5e9-35e9388494eb | -13.72767 | -45.6995 | 2025-10-08 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 462d0a21-7db0-3f69-8fdd-f6a4fe94c65f | -8.22402 | -44.15589 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd1cd017-9341-3bed-b18a-71b574043789 | -11.15659 | -47.74568 | 2025-10-08 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README21.md)
