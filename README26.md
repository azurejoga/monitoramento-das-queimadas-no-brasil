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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60bec561-5fc0-3fa9-894d-c9c8aac38dc8 | -7.63809 | -45.24711 | 2025-08-22 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b49c2bad-612d-3628-8d7f-70b637e8317d | -9.18691 | -59.63598 | 2025-08-22 04:19:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4515c15f-488d-3b8b-8f9b-5e383611f11b | -8.81142 | -45.3245 | 2025-08-22 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9c74e7f-c3aa-34dd-8692-f120f7f47276 | -8.77459 | -45.4504 | 2025-08-22 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e60e89b-7eb8-3f2b-b962-4d2361532338 | -6.26706 | -53.69107 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d90713aa-b475-3490-afa6-8565c4e07930 | -6.94438 | -44.28104 | 2025-08-22 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ffbb3543-eebf-3a61-b520-0d0c34bbc953 | -6.76778 | -44.32481 | 2025-08-22 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e27f278c-12a6-351e-af36-259ccf05fee2 | -7.86213 | -46.98742 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8d000309-264f-3903-a432-f2c8e5834d8e | -7.63203 | -45.24259 | 2025-08-22 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 60cfb7f0-8d01-3031-be55-54476ef66982 | -7.03738 | -44.61923 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4096a2db-c4f6-33d5-bf97-5aaad07c463d | -5.88528 | -53.62333 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9892bfa-fe49-38b3-8ea8-3b4b414e77d2 | -5.97051 | -52.22281 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8b64478a-c22c-334b-b135-e37fa2ed0d3c | -11.11906 | -44.71618 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f640a00-5c0e-3c2f-a2ae-4a470e755c14 | -10.85699 | -45.20654 | 2025-08-22 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b8a895c-11cb-3080-936e-ec2d25866f38 | -9.58708 | -43.32729 | 2025-08-22 04:19:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a78a664b-b6ea-325a-ab97-65dc264774c5 | -10.28174 | -46.75694 | 2025-08-22 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5a14318-9ed0-3736-954f-0c3df1d2d7f8 | -5.88001 | -53.62249 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6404e675-7368-31ce-9c54-3a9f6e78ee1c | -6.28131 | -43.87336 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91d983cc-db84-3308-b58e-98eafb7a1bfd | -6.02416 | -42.83918 | 2025-08-22 04:19:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f2b7b373-9028-31f8-86f4-58a90681e261 | -8.79552 | -45.42523 | 2025-08-22 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60df4db8-23e8-3442-ba9b-f025835e0d6e | -11.31091 | -44.94805 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43717432-b4bc-384f-8a8e-7178ee122b62 | -7.17222 | -44.6692 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5a451bf-fbcf-36e9-b426-34c4d6a61176 | -8.78739 | -46.71059 | 2025-08-22 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e3027bf6-de5b-3507-88e4-f8f3d6f3ee2c | -11.81488 | -44.25546 | 2025-08-22 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b8f707b4-88d2-38ff-9250-56238ec743c9 | -9.06621 | -42.99955 | 2025-08-22 04:19:00 | NOAA-20 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fc6db2a0-25be-3f65-aeca-38775e4ba3fe | -7.61165 | -45.26426 | 2025-08-22 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68516b33-3807-324e-85ed-c65315e1b10a | -6.49704 | -43.11346 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee51eb9d-3629-3517-98ee-5a2f3f4f7703 | -6.42352 | -44.67799 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68f4e0c4-cf6b-341c-afdd-5b852e0279a6 | -6.09708 | -44.35765 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c4b456d7-9cae-30d2-82da-f9d2f02db63f | -6.03128 | -44.36473 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 850cef7b-af04-38c7-ae29-f7dfd7f16e2f | -8.75806 | -45.46914 | 2025-08-22 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4aaea85-bb71-38fe-940c-5ebe28a349c2 | -7.11149 | -44.4496 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78124efc-5eac-36a8-b6fe-d35435ef0e17 | -12.09327 | -43.34455 | 2025-08-22 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a4e20fb-dae6-3175-a123-35531493497e | -9.2108 | -59.46766 | 2025-08-22 04:19:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 21547a2b-1bc2-3739-a874-32fe2297dd63 | -7.85408 | -46.99379 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ee58160d-c357-3e1d-9ce2-2abf2ab99339 | -7.14728 | -43.23334 | 2025-08-22 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6df317ea-004b-328b-9391-5f5b71536f17 | -7.46432 | -44.45156 | 2025-08-22 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06ae94c7-12d1-3c27-9512-64ac2daea83b | -10.28844 | -46.75796 | 2025-08-22 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b40d9702-6d08-3c9e-a8aa-1ab01f2dd13e | -6.4219 | -44.23446 | 2025-08-22 04:19:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47474dbc-d04f-3285-8667-54967a809a3a | -9.16063 | -59.60665 | 2025-08-22 04:19:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbc9243f-ef73-3557-99cd-bad4482984d4 | -7.09021 | -44.5636 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b4b95d9-7408-3831-8b16-e1a10bc8f8e1 | -12.58785 | -47.08482 | 2025-08-22 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4039244-e0ec-34ba-9e18-f7ac5e97b555 | -12.71717 | -44.78704 | 2025-08-22 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 11980c24-a898-31bc-b393-a800aab8127b | -8.14359 | -45.55244 | 2025-08-22 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39cf1da5-92f1-3800-9505-6f092ac5256a | -9.71757 | -45.62999 | 2025-08-22 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef177afe-7908-32ea-a019-7f2bc38afbbc | -7.5125 | -44.96799 | 2025-08-22 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af2394d4-d4e8-3872-9a97-6095bad6f437 | -10.70889 | -48.21977 | 2025-08-22 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7a614fc-69a3-3806-a5f9-883016863b90 | -8.12637 | -47.15161 | 2025-08-22 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36adc716-3ec2-3e84-9b5f-18726959bfb6 | -6.70408 | -48.99897 | 2025-08-22 04:19:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95fe2e01-6285-3f18-82cd-ca180c3fe74b | -6.71337 | -43.20887 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c48a473c-8800-3618-9e4a-6e4e574dc4a0 | -6.94529 | -44.16678 | 2025-08-22 04:19:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d490b6c-dd1f-3ff5-a67b-8fbf8e6f8ca3 | -8.21096 | -44.43273 | 2025-08-22 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7fe88e3d-17ce-30ee-824c-634678fe38c2 | -6.44441 | -53.3899 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91c5186b-d51c-3bd2-ac2d-bfd1a4564f14 | -6.26764 | -53.68779 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f03b20b0-3724-35aa-a34b-a28990ecd302 | -6.16529 | -42.71936 | 2025-08-22 04:19:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 21257200-590f-393a-9d5c-0da7441fda05 | -12.09739 | -43.34106 | 2025-08-22 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71e48e4e-2dd9-3292-810a-3107179ad7a7 | -10.27503 | -46.75597 | 2025-08-22 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fbca917-6ed2-39b3-985b-b94a826e7b96 | -6.49088 | -42.85563 | 2025-08-22 04:19:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e039ca5b-0a52-35cf-9329-d3096a118473 | -10.71795 | -48.86081 | 2025-08-22 04:19:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| badb8249-5d86-3e92-b217-68dcb05aed2b | -10.28509 | -46.75744 | 2025-08-22 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35b9e86f-030a-3f43-a8d2-5e74167cc097 | -12.00136 | -44.66821 | 2025-08-22 04:19:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4a33b4d7-798d-3b6b-bfd0-abce9990ffbd | -7.27997 | -49.28993 | 2025-08-22 04:19:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb1b270a-1e7e-30f5-b970-ac0d475cd308 | -6.49031 | -42.85933 | 2025-08-22 04:19:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| becd7676-47de-310d-90bc-b73084131f90 | -7.62439 | -46.24773 | 2025-08-22 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb3ff44d-f3ca-32f5-acef-cfaad9c48b69 | -6.57652 | -44.46146 | 2025-08-22 04:19:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f72e803b-4813-376f-92fb-354865893061 | -6.93665 | -44.28698 | 2025-08-22 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d220b5a-ae1c-3a67-ad72-203df78c6d0b | -6.03736 | -44.36923 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93550803-1a32-31fa-b1af-e67fb9a2b41b | -6.44548 | -53.38387 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dceb65f8-ed42-34a9-8f03-f420083aa2c4 | -6.43583 | -44.51352 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bed58c97-3874-3e97-b83c-8c94d28ddc6f | -8.1198 | -47.15168 | 2025-08-22 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6914a24-48e0-3099-83c4-c651cb3f1bf2 | -6.22005 | -44.13551 | 2025-08-22 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f34193d2-1aa3-3d74-995c-0e8f9e69f274 | -6.20347 | -43.56526 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9e1964c-d127-3397-82dd-af10891e5a1a | -5.97105 | -52.2194 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d5c6edd-5c89-37d2-b083-9986ddbe2f37 | -6.52005 | -43.86684 | 2025-08-22 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c86ea88-7872-3a1c-84e5-8e7b3d727a56 | -7.94248 | -42.6614 | 2025-08-22 04:19:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| de9aee5f-558b-3113-b3b1-6d77769cf478 | -10.886 | -48.48479 | 2025-08-22 04:19:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0cd38012-5d37-3307-9c3b-6d62842b108a | -8.11952 | -47.15044 | 2025-08-22 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e284860-9f9b-361b-bc66-b52824266a5d | -12.6797 | -44.96395 | 2025-08-22 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01b39b38-b7a2-377b-b14f-6e3bcad5a2aa | -11.3015 | -44.96479 | 2025-08-22 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7015b765-a605-358f-8641-1ffeed49b326 | -12.64478 | -45.32326 | 2025-08-22 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa8d2d4f-083b-3fc2-a55d-3932b3a41977 | -7.6238 | -46.25133 | 2025-08-22 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe8e8dcc-f955-3790-bcd4-b67ef19f4e38 | -6.44494 | -53.38689 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6b36c46-7922-39ba-864d-b45b4ac91b50 | -7.15124 | -43.2302 | 2025-08-22 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4ed164a2-ad66-3d32-87c6-0a22d950158c | -6.84523 | -44.41523 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 433c55a1-b671-3204-83a4-23bdb7ac8c9f | -6.48962 | -43.45284 | 2025-08-22 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6900eac5-f1a5-3110-b313-e80a7447b71e | -7.63533 | -45.24311 | 2025-08-22 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3047ceeb-2e0c-3ad6-b408-efa11f8e5cf8 | -10.865 | -50.83647 | 2025-08-22 04:19:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7f4fe89-a1f9-37e3-8ae6-472773df9a2d | -9.72033 | -45.63401 | 2025-08-22 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f91f6121-7bac-3d72-8b4b-ea27b2ec12db | -11.30593 | -44.95823 | 2025-08-22 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb9704b3-2910-3214-a994-a537d244a466 | -9.18839 | -59.62881 | 2025-08-22 04:19:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 63d2b655-41f0-33b8-b36d-c7e72092412a | -11.27724 | -44.9502 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2912716-7677-3ad4-82fd-fbb05e602e8d | -9.27057 | -50.24793 | 2025-08-22 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 116fcf20-be58-3fdf-9ed3-75ddc7f38c87 | -10.27897 | -46.75282 | 2025-08-22 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f662800b-f1cd-3030-90dd-a7b7e5a2989a | -5.87887 | -53.62901 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6f1563b9-3d2b-3a12-9a98-e7f204b9f07c | -10.45605 | -48.80777 | 2025-08-22 04:19:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fab9c0b-75ad-3d78-b5e8-bd196e5589b0 | -6.03495 | -42.83712 | 2025-08-22 04:19:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 71d42116-fd11-3dd9-b47e-d1b173b006c4 | -7.8575 | -46.99435 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 04b72880-4875-3c3b-960b-918554a675e3 | -6.97559 | -44.16763 | 2025-08-22 04:19:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cd75e13-d960-3062-b5ae-304748306c32 | -6.29083 | -43.70203 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0f1d720a-2767-3f4d-ab75-515e6ec84825 | -5.87831 | -53.63225 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README27.md)
