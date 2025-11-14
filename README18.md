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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acf81ec8-3132-30b1-923d-00cef4d5af4b | -6.08404 | -41.62212 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5959a039-c4aa-3a73-b16b-ed51aec3347f | -7.93566 | -44.33514 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 635b9019-537a-3e6c-b4a7-47e8f2d943c8 | -7.14786 | -40.29698 | 2025-11-14 03:53:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f4298de9-8f09-3b7a-8bd0-8bd17a3d89eb | -6.11079 | -41.59586 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fc17db39-23c5-3f0e-99f7-4f3744bea8eb | -6.28732 | -41.73339 | 2025-11-14 03:53:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 99bd3172-d33c-33fa-ad00-d977928ade08 | -7.55702 | -47.24815 | 2025-11-14 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 50f938a1-f8e4-352e-b25b-a3d867eb90d7 | -7.35745 | -43.35316 | 2025-11-14 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1de70510-b0d2-3f1a-8ff9-0d86fccd4cd8 | -7.92591 | -44.34159 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05b1cd4a-4bac-3b1a-9313-79ef5f613331 | -5.36712 | -46.28673 | 2025-11-14 03:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3bc11cf2-6f08-3049-8680-65553904a0f5 | -6.13697 | -48.05155 | 2025-11-14 03:53:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e703991-9970-3b64-8dd8-26b5a0e2a35f | -5.75456 | -49.25709 | 2025-11-14 03:53:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 786a2100-5ad2-3b17-bebc-9d7c3f8a305d | -4.53581 | -46.39594 | 2025-11-14 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6d216c1-3ddc-307b-868e-32543ffaf8ed | -7.45633 | -42.56926 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1b675948-dc35-3ba1-a426-6ccffe915292 | -7.36203 | -43.35036 | 2025-11-14 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b05c64d6-3434-3a09-8573-52e617ef6fca | -6.14228 | -43.71027 | 2025-11-14 03:53:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 55b5a238-99f0-386b-8c84-bd2e8605d018 | -7.46618 | -42.58049 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 95307bba-1d2c-3ed9-8d08-49efffa7a362 | -6.15455 | -48.04959 | 2025-11-14 03:53:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fefdbc7b-2532-3522-b7aa-4ed85f5b03a6 | -5.75875 | -42.72735 | 2025-11-14 03:53:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c636b10a-7923-3955-b121-bce4e4b9acf2 | -6.46962 | -39.85819 | 2025-11-14 03:53:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 80185b6b-682a-329e-b17b-4fae67640d6a | -4.67526 | -45.8045 | 2025-11-14 03:53:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b7f0eef-ad3e-3259-84e7-dbeb6d16fef5 | -7.06662 | -43.5837 | 2025-11-14 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 164b1a4d-b687-346b-acb5-65db097a31bd | -4.98779 | -43.88871 | 2025-11-14 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c6e2b3b4-7efb-315a-8e5d-225c7be56810 | -5.03079 | -43.6018 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45e7006f-5c09-3ab3-b4f0-58595f9a85bf | -6.88912 | -42.85644 | 2025-11-14 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 38.7 |
| 14da8f43-b77b-331e-acf1-e39f64dde939 | -4.61171 | -46.55598 | 2025-11-14 03:53:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a57f420-05cc-340d-b25c-5f458c466260 | -7.05347 | -45.06173 | 2025-11-14 03:53:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69ad1bf3-b3f8-3e1d-b8aa-54e3aabfe5dd | -7.48668 | -42.54941 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2a2f39e7-154e-37fb-8b32-cc39b3e5752a | -7.44875 | -42.56804 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9190d6f4-bf07-3d9c-b94e-18bc288783b6 | -6.09711 | -41.61095 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0fc85a9b-1598-35c2-ab26-a6cbc1f092c6 | -6.10717 | -41.59509 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 56b54a27-f67c-3e0e-86b3-7de9299d4a61 | -7.46694 | -42.5521 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6d87d915-9b6f-3b04-9fe2-0f90c5f16b84 | -5.8445 | -47.68218 | 2025-11-14 03:53:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ee6cd075-c4f5-3d94-80bb-17da1bfb5cd3 | -7.84714 | -44.29601 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5fb1bb65-904c-3f4e-8c44-0549eca8fda7 | -4.71177 | -46.44614 | 2025-11-14 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cb526a1b-380a-33d3-9968-338614984f0b | -7.85555 | -44.29742 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a2055bf7-1116-3bba-9d8c-925a187f3d14 | -4.68314 | -45.8602 | 2025-11-14 03:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45e9641c-bbce-36ea-a745-a71f0aeaa96b | -6.65314 | -43.53261 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ef4e9fb9-ede2-321d-a489-b3842d1825db | -6.88116 | -47.24207 | 2025-11-14 03:53:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 952a56e7-73d1-3c50-a4bb-74108d0dc524 | -5.89662 | -42.74667 | 2025-11-14 03:53:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 74d01718-27cf-3cc2-9511-912b5b23a1d0 | -6.55182 | -44.24931 | 2025-11-14 03:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 920d1497-3049-3ba2-b3d6-dc610ff49ae8 | -4.99147 | -42.91418 | 2025-11-14 03:53:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bca0efe-5a29-36eb-8649-cd975346946d | -7.02586 | -46.43779 | 2025-11-14 03:53:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 418b201b-0a22-3b67-82c4-8b0e749bbafc | -6.85566 | -39.5728 | 2025-11-14 03:53:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 20bc12ed-2c6e-3c3c-9b98-6878c3a2949e | -7.35496 | -43.355 | 2025-11-14 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5abc42fd-fc6d-3abb-b02b-b95912ba560a | -6.28783 | -46.95552 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8aa2ec28-1b7d-390b-8abd-e84d537a5722 | -6.57298 | -47.89876 | 2025-11-14 03:53:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bda894ff-c229-3da4-b31a-1c61710032e5 | -7.74939 | -45.89889 | 2025-11-14 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81bce62a-4245-3656-a00e-3336dfbf5bb2 | -6.98224 | -38.62146 | 2025-11-14 03:53:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 00c243fc-06eb-390a-b757-11cc1a9e70ae | -4.10712 | -48.01846 | 2025-11-14 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f152478-b194-33c2-9d8f-60e489f1f316 | -4.68413 | -45.8544 | 2025-11-14 03:53:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd757ab6-0c28-3726-ac72-7b74aae94064 | -4.69878 | -45.68081 | 2025-11-14 03:53:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57477894-1a1c-3064-82da-36028c54ec4b | -6.10007 | -41.70938 | 2025-11-14 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3938ed80-1f7d-3c96-82fa-31e6ee850abd | -7.46771 | -42.57119 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ba8cd069-e543-3ff5-95b1-3c5636a2499e | -7.93632 | -44.3312 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0ffc1cb-a3ea-3216-a42d-3be63bd937a8 | -4.10135 | -48.01759 | 2025-11-14 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b12460c5-c5b0-37be-b897-279b55a0091d | -4.21954 | -49.11512 | 2025-11-14 03:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 46d051ab-b611-305e-8a58-f68d217b8d8e | -5.62823 | -45.04428 | 2025-11-14 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7b0ac64-3614-348b-9879-98448414bf61 | -7.02091 | -46.43703 | 2025-11-14 03:53:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 0377a0ac-1b8f-3b3a-a284-55ef6df93d81 | -4.77485 | -46.44718 | 2025-11-14 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52f491a2-6c40-37a9-8f78-2344cd948ed1 | -6.8086 | -40.09238 | 2025-11-14 03:53:00 | NOAA-21 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ad1f4423-bbd1-39c8-9eea-0c672b1b6e12 | -7.13913 | -40.46033 | 2025-11-14 03:53:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f9d3d45b-6ae1-3948-8a51-058df8df51ee | -14.63605 | -44.2241 | 2025-11-14 03:55:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 157cdb3f-05ed-3338-83d6-8a9a8f9572c5 | -12.7059 | -45.42795 | 2025-11-14 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1f46bd5d-452b-3fc2-b41d-2976579ce034 | -5.0241 | -41.10375 | 2025-11-14 03:55:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e82e8166-e964-374c-b2a7-31f04a2c914c | -3.75191 | -38.58549 | 2025-11-14 03:55:00 | NOAA-21 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a8162c8f-c105-3b43-987a-9a9b761237ab | -12.01227 | -46.76941 | 2025-11-14 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aeceaffd-ee45-3ced-b643-48639e7ad43b | -10.73106 | -44.01923 | 2025-11-14 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7d7520f5-9b6d-3963-9e2d-8d134e07401f | -7.78822 | -49.61962 | 2025-11-14 03:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac5c4ed0-3947-356d-9635-6a143ebee9a7 | -3.13511 | -40.99598 | 2025-11-14 03:55:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 54141026-3b29-33f6-81a3-061e2ba97f04 | -12.72051 | -45.4186 | 2025-11-14 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 10d82a47-6dc8-3cb6-9afe-ac48711702cc | -11.98786 | -44.28919 | 2025-11-14 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f656298d-5599-3609-86fa-834a8371e3ea | -10.74912 | -44.55746 | 2025-11-14 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59287b09-af0a-3638-9fea-6116ffce89d5 | -3.01121 | -49.43473 | 2025-11-14 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 46349b79-c8c4-3f73-a525-6567bc7b068f | -9.50406 | -47.27132 | 2025-11-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56e1117f-f5b3-3672-9102-9d8bbb1ce699 | -12.58669 | -43.36012 | 2025-11-14 03:55:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d80c63be-558e-3dca-9770-be24ab45296b | -14.9451 | -49.79655 | 2025-11-14 03:55:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 29.2 |
| f541e187-026c-30dc-ad66-8874512515d9 | -13.66043 | -44.21289 | 2025-11-14 03:55:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6241d658-f2ec-3d17-a650-da0b702ee12b | -5.09351 | -38.42738 | 2025-11-14 03:55:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 14286baf-0489-3ae8-b191-4cdf0460bf26 | -3.86774 | -42.76254 | 2025-11-14 03:55:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 47fb4286-2153-3b06-a5b7-9abc162d54b9 | -8.90018 | -47.89649 | 2025-11-14 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 371741b4-1b68-36fb-b072-a779d1857b06 | -12.45484 | -43.75922 | 2025-11-14 03:55:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0fb21c4-8ccc-3d34-a96b-0fd08f064d21 | -11.85108 | -49.21369 | 2025-11-14 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 040ad5f0-df5a-3ffb-80e8-559265e52d18 | -4.4751 | -42.87683 | 2025-11-14 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d230aa7-3b32-396d-acea-2a86ed7ace1a | -3.41731 | -42.67786 | 2025-11-14 03:55:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 055bab58-6b0a-3d28-bd98-fa1464b2be6f | -12.62368 | -47.01735 | 2025-11-14 03:55:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 41305e64-d4fa-30a8-aa23-07647d9ae15a | -16.59057 | -42.21691 | 2025-11-14 03:55:00 | NOAA-21 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| e39ffd9b-9288-3a46-852c-36412889f127 | -3.30236 | -50.10727 | 2025-11-14 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 32ac7d47-2027-3c7c-be8b-6319dd6131ac | -3.26714 | -43.12445 | 2025-11-14 03:55:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6356ae5-ba11-3fa9-a508-128db630a3e4 | -11.84966 | -49.22091 | 2025-11-14 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 4fd28349-3177-3d81-b6bf-fbd88ac70535 | -4.81465 | -38.64297 | 2025-11-14 03:55:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5cf72bdf-1820-3953-b1c2-44860579005a | -9.31737 | -47.83643 | 2025-11-14 03:55:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b40a2fd2-98b4-3279-b1f3-1abca99b7945 | -3.53391 | -44.84551 | 2025-11-14 03:55:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b330dbb3-ebea-33dc-910b-127a8ad111ed | -3.75748 | -40.79189 | 2025-11-14 03:55:00 | NOAA-21 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6f690e49-4197-3201-a4c0-2529428f059e | -7.78467 | -49.61726 | 2025-11-14 03:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9802c69f-816a-3ccb-b7d5-c159df575668 | -3.35644 | -46.86795 | 2025-11-14 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dceef81-b5df-396f-a2c7-8510bec40e89 | -12.54971 | -47.8161 | 2025-11-14 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6cdbd45-d2c2-36cc-86da-ff0d9fff92a1 | -15.55605 | -44.48692 | 2025-11-14 03:55:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6e981835-ba04-3fba-839c-2f2110f3b847 | -11.99173 | -44.28674 | 2025-11-14 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ee9cc2e3-394b-3ac3-be97-7d739ced25b0 | -8.93904 | -49.8164 | 2025-11-14 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad5de9dd-21e2-353b-89bd-321e57719c24 | -11.85304 | -49.2273 | 2025-11-14 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |


[Clique aqui para ver as próximas entradas](README19.md)
