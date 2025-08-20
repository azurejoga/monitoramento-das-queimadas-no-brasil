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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf986dcc-a12f-3834-b85c-85ab369bf1a5 | -7.65346 | -45.27092 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f8de12d-e1b3-3dc6-9cb7-f0cb602c8eaa | -3.98111 | -42.51304 | 2025-08-20 04:34:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 14c76000-3ec1-30eb-a4f0-7ef01521f774 | -6.13826 | -57.71274 | 2025-08-20 04:34:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c3cc6e73-064a-396b-9301-16a87be61dff | -5.98545 | -42.82364 | 2025-08-20 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8fa8bf39-20bc-3786-89a5-a3640bb47da2 | -8.29993 | -46.34711 | 2025-08-20 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c356107e-ddf2-3c44-bddf-254c7986b98a | -8.0363 | -47.672 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d40ef78-7ac1-3f0c-ab1d-0daa5e2cc133 | -6.17093 | -46.14983 | 2025-08-20 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 43bdb212-d51e-341f-81c2-bd03feb3fe2a | -5.09006 | -47.71508 | 2025-08-20 04:34:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bf966e4-6af6-3866-b0f0-83d2747c145c | -6.05543 | -45.05527 | 2025-08-20 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8db58be3-d5a6-3e76-b395-a1eab8ee5366 | -4.30993 | -48.10601 | 2025-08-20 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f620d66-a838-3fdd-bc10-e8184dc8afb6 | -7.12103 | -44.64705 | 2025-08-20 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a24c618e-d152-3209-8881-e85834e43997 | -4.83613 | -43.19133 | 2025-08-20 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0608050c-1a6a-37e7-b324-9059ed077306 | -9.29348 | -40.23587 | 2025-08-20 04:34:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f86d7e94-5467-3516-b828-b19d58d85241 | -5.88112 | -46.19445 | 2025-08-20 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba844b10-8dd3-3e62-b88e-9a37162695c4 | -4.29937 | -48.06484 | 2025-08-20 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a9e78c7-71a5-34fe-936f-3f08d594b65f | -7.64557 | -45.27909 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c53bbd6c-e422-3c8c-ad20-7a8b80a59651 | -7.59812 | -44.39139 | 2025-08-20 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5e96f572-d10d-3d2d-9280-696417030664 | -2.96675 | -49.30066 | 2025-08-20 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb36fe7f-8b89-3aa4-a671-ed8a6776ae3c | -8.02398 | -47.67032 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8110a7de-7e5a-312e-94ae-c09078716b5d | -5.4045 | -45.18979 | 2025-08-20 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cbadc87-8402-3d8f-a00b-e51b52ec597c | -7.58699 | -44.38982 | 2025-08-20 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e707fddb-cfa5-33fa-b50a-8f075830c5b7 | -5.63569 | -43.40232 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97914ff6-896e-39d4-88f7-42ab79447fb0 | -7.65406 | -45.26688 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c5b3507-f1ba-3eb1-ac32-695a287bda17 | -9.85507 | -44.59227 | 2025-08-20 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ad14ce9-95e7-3efc-b827-4cdf8171d142 | -7.64812 | -45.28239 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f4fafc2-6f3c-3157-aa02-3759d86f659a | -4.48305 | -43.90232 | 2025-08-20 04:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c53c1974-bb43-3498-b048-3359b341b95e | -4.95173 | -43.08952 | 2025-08-20 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1032777a-f291-3d37-a0d5-7645de7ef3cf | -7.64203 | -45.27853 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4bda3c3f-396b-3ba1-afe8-4964f7ff3ee2 | -6.13261 | -57.71161 | 2025-08-20 04:34:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0352e807-b396-396e-82a0-00c5204f2ca9 | -7.20663 | -46.24341 | 2025-08-20 04:34:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 469fd7b7-24d0-35bd-aded-ac556c724ddf | -5.65789 | -43.50319 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6be53eaa-4e73-3787-ba05-84c55d599ebb | -9.86945 | -45.97379 | 2025-08-20 04:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6c29651-480d-30ca-b9f3-a489b9897a05 | -8.41161 | -45.68623 | 2025-08-20 04:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cfb3fc83-64e3-3d17-a377-fc752b0e080f | -4.95559 | -43.0901 | 2025-08-20 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b527061-7aa8-3f28-8fb5-7445c3ddca33 | -3.74143 | -48.92915 | 2025-08-20 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d890b30-2a02-3d57-b25b-ac28b5863c44 | -5.63401 | -43.38767 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ecef1207-9afc-3777-a38f-5424a5c7a545 | -3.53914 | -53.56302 | 2025-08-20 04:34:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7f2d454-0a6a-3e75-8438-5a1e63c4e762 | -6.19976 | -43.56365 | 2025-08-20 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e64d387c-d19b-3994-b16e-d246ad437437 | -7.02422 | -44.59584 | 2025-08-20 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 231ee838-432b-34da-89af-a75ff6e2c198 | -3.87489 | -40.45225 | 2025-08-20 04:34:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ba94d052-2365-3fd2-9cc1-4488b523886b | -3.10634 | -47.50196 | 2025-08-20 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff3e1b4a-a3b9-3fcd-a0cc-4b39988c5597 | -3.23099 | -46.79959 | 2025-08-20 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 1ff4a7a9-0f1d-37d5-b1cb-7b2fc26bf8e9 | -2.38388 | -47.66689 | 2025-08-20 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c648f080-3c09-3f70-a260-6e421d2616b8 | -7.64398 | -45.28584 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae42dfbe-139c-3e47-997c-c6b98eacdf8a | -7.25348 | -50.17855 | 2025-08-20 04:34:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ded38960-a92d-3d7a-ac50-6a70546c4b90 | -5.933 | -43.49644 | 2025-08-20 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c8a98e5-bb49-37ff-8cde-45c3aa175488 | -3.98431 | -42.51868 | 2025-08-20 04:34:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d2372421-5e92-332e-bdf8-41dd075bff20 | -12.52112 | -45.60189 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86dd3bcc-505c-3529-adbc-630d0495e7ff | -14.50512 | -45.96111 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa94b9f6-a801-3eaf-9896-3f9e6cbb7059 | -12.99064 | -45.19979 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6d6a082d-ab13-301d-ada3-61bac3fd7d81 | -12.97434 | -56.84805 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58cd09fb-d0d5-3671-a028-f9db62b7075d | -14.3563 | -51.99764 | 2025-08-20 04:36:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0176cfd2-b560-3c5e-a5d8-d806a719b9a4 | -12.63808 | -46.88278 | 2025-08-20 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2814957c-d57d-39eb-89e5-ccce605b1af9 | -13.4765 | -47.0524 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79c7c27c-65c3-3eac-a395-bded4bc55404 | -11.75012 | -48.18657 | 2025-08-20 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| ec2bb190-127c-387d-a8b7-27b33de76d07 | -10.91734 | -57.51037 | 2025-08-20 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6773c6e-42b9-3906-a383-5da42aff90d7 | -14.63106 | -54.88342 | 2025-08-20 04:36:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2f21e5c-3448-3e1c-826a-04b423476bf3 | -14.37028 | -47.69062 | 2025-08-20 04:36:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ebe040d6-8e3d-38d4-ba47-86e80a7531dd | -12.97335 | -56.87627 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a0d554e-4da6-3a73-ac41-66db657b6551 | -13.33356 | -54.42286 | 2025-08-20 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8956b697-59b3-3b08-a061-1c24892ccd11 | -12.97623 | -56.86464 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d60cd2ba-8654-3672-85b8-c0fc3208c693 | -12.37023 | -54.16765 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f898ff7b-d24c-343f-bea7-7eb167b07873 | -11.31699 | -55.21402 | 2025-08-20 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 385625d4-a0fe-30c9-bc98-94d5edbe70f9 | -9.17087 | -59.61844 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd508ebf-cee2-3dbb-876d-6ea5c3e77ec9 | -13.15481 | -54.93043 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bac61ad7-3603-3ba0-a97c-4e5425caec0e | -9.2316 | -59.59665 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4086c93-a38c-3e62-a238-b7a2f0ec8135 | -10.60332 | -48.60056 | 2025-08-20 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4a3f2e2-8903-3157-8e27-9e6779d425b9 | -12.98372 | -45.19398 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1d311e30-c444-3fee-afc2-169f6fe3751d | -12.98931 | -45.20914 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2a44f0b8-c9d8-32e3-b059-4983ca721384 | -12.97527 | -56.86987 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98c6cfa0-fef0-3bc4-98cb-217c4250fd6b | -11.13257 | -46.97824 | 2025-08-20 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f743528a-6787-3139-983c-8606f6d506ab | -13.2171 | -50.745 | 2025-08-20 04:36:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3b29b3a-7410-3ce3-ae13-ffca4cdef18c | -14.46247 | -48.37089 | 2025-08-20 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 450db8e9-45e5-3efa-8d38-a78e6cdae886 | -12.98817 | -45.18987 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b8cc5c0-9c54-331e-973e-897b3112b23f | -10.82195 | -43.28184 | 2025-08-20 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 6b6c8706-1de1-3606-a9de-12eef4336958 | -12.66347 | -44.9565 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c861f33d-2704-3ffb-a2fc-249b1b74b1c2 | -11.3154 | -55.22263 | 2025-08-20 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1c010e7-43c9-3d6e-9c1d-552f7132172f | -11.56496 | -50.46053 | 2025-08-20 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccb1e83c-43d0-337c-8c23-b0973914fe81 | -13.19296 | -46.89988 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97f9a3ec-79d5-343a-9ae1-f1585756244c | -14.88963 | -48.08252 | 2025-08-20 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2fcc25f2-6199-39ef-ae1d-ed92f7f5fefd | -13.34954 | -54.40341 | 2025-08-20 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| db8d3b5d-8e95-3c98-a453-4e4166cd2d2a | -13.34614 | -54.39914 | 2025-08-20 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9129ed79-4e73-3931-a103-eaa7ed84d8c5 | -14.65917 | -54.88532 | 2025-08-20 04:36:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7f250b82-d305-39c4-9d4c-8d5362b53811 | -13.74328 | -52.01361 | 2025-08-20 04:36:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60198312-438b-3347-ad63-edb506ccc32b | -13.48868 | -47.06624 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa193220-4912-3593-bd61-f06b14f2d2b1 | -14.68947 | -49.04892 | 2025-08-20 04:36:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ca92e86-43d6-3415-9330-433099b970c2 | -13.40576 | -46.36584 | 2025-08-20 04:36:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f14fea56-76bb-3f1a-af71-896f70d41385 | -15.16482 | -49.80911 | 2025-08-20 04:36:00 | NPP-375D | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b60ba215-9476-3bb9-8c85-0a57141f0a8b | -14.50575 | -45.95668 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf9fa447-010c-3d56-bb21-b8892a1350bd | -11.3162 | -55.21831 | 2025-08-20 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ac24e90-b38f-32da-ab2b-53613f8fe9b3 | -13.18303 | -46.87053 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a803907-c579-3595-b11a-da7a65fec5c7 | -12.9771 | -56.88251 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 057d2847-b386-32d7-a8c6-70b7d1e7f75a | -11.31513 | -44.92339 | 2025-08-20 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 439d6a63-a15c-38a6-ab8a-f1ea1ce6ba2b | -9.19122 | -59.64218 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| baceef40-c09c-3013-a577-652e1632adcd | -13.62326 | -46.88564 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6466645-8c17-35c4-94f3-89ef70820bb6 | -12.94611 | -46.15736 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b817a1a-e61f-36e7-8234-bfdfa2347a28 | -8.96845 | -60.5026 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7298403-681f-3955-8de7-bb985dbf2602 | -10.85436 | -48.46772 | 2025-08-20 04:36:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60c08809-7e59-3fcd-acad-3604817c18b3 | -14.89754 | -48.07618 | 2025-08-20 04:36:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3e855a08-b7fd-39ec-98fd-e322b82dc6b2 | -10.69722 | -48.21942 | 2025-08-20 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README32.md)
