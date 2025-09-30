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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b1b7415-4f87-3e7c-82a2-5046796b8760 | -14.5522 | -48.4684 | 2025-09-30 01:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 18de03ce-594f-3819-829c-761a99d86c1a | -15.7251 | -59.5108 | 2025-09-30 01:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| f074fa1f-1ca7-39f1-8a30-ce283b12f2f5 | -13.0144 | -44.1006 | 2025-09-30 01:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 264934b5-fd46-388e-ad8a-81500f2bf6db | -11.1735 | -54.1242 | 2025-09-30 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 21fd2955-9ed6-37fa-9697-2fc52da14e8d | -11.7524 | -44.7228 | 2025-09-30 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 882801ff-9e1d-3d70-aefd-c50062dd971b | -13.2154 | -50.9715 | 2025-09-30 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 4c5bdfc0-e0bc-3426-abcc-d873ca90a2ef | -14.6603 | -46.9663 | 2025-09-30 01:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 121fd400-5383-3877-a7bb-1711ae87553c | -12.8429 | -47.0063 | 2025-09-30 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 279b7ae1-f99c-3462-b1a9-f8d069caadaa | -10.1851 | -44.8939 | 2025-09-30 01:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 208.7 |
| 0dee568f-50ae-35a9-ae42-28b0153c161c | -10.2041 | -44.8915 | 2025-09-30 01:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 50231e64-c90e-3fd5-aa5d-ee8b2b55d876 | -10.1855 | -44.8709 | 2025-09-30 01:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 8e2636ee-2f2a-32c9-8f91-31af8f574b10 | -8.2659 | -45.5244 | 2025-09-30 01:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 36.1 |
| d4518dbc-c131-36c0-8be4-0f84efe192d1 | -11.2326 | -47.2285 | 2025-09-30 01:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 140.1 |
| fffcb954-e731-32fe-b6ff-1df91f0c55fb | -10.1851 | -44.8939 | 2025-09-30 01:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 49ac5b07-95c2-39bf-a201-694be2a593df | -11.2516 | -47.226 | 2025-09-30 01:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 56e781c3-a199-31da-99e9-13c0f8e82430 | -4.354 | -45.5773 | 2025-09-30 01:20:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 143.9 |
| 0ab3a9b0-caac-33a8-a585-3b45f3224091 | -11.8868 | -48.0323 | 2025-09-30 01:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| bb2a1026-6a40-3560-9905-a3360418bdad | -12.8433 | -46.9837 | 2025-09-30 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| fb10e5df-6af1-3743-a5c7-a6889930fb9e | -11.2513 | -47.2484 | 2025-09-30 01:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 6e4cdca7-50d8-3a2a-a83f-385b27331ebf | -11.1548 | -54.1054 | 2025-09-30 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 864f55a5-0ffc-30a7-aa78-939bd9e5fb67 | -3.1013 | -47.0082 | 2025-09-30 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| c7d23b48-7b42-3b7e-98b9-9b672e3c842a | -11.1357 | -54.1277 | 2025-09-30 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 78a00e6e-351a-3927-9dc1-4b903cccaf94 | -11.2135 | -47.2309 | 2025-09-30 01:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 4c8bbde0-e000-35b2-a2b2-15329046cea3 | -21.0357 | -45.6936 | 2025-09-30 01:20:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 58.6 |
| c084d6ba-7286-312f-838f-08172635704c | -11.1546 | -54.126 | 2025-09-30 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 226.5 |
| 9f16377c-7a57-32d1-b781-60f5380418bf | -14.5522 | -48.4684 | 2025-09-30 01:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 2406e773-833f-3ad4-ae1f-d2bab5d02ecf | -11.1735 | -54.1242 | 2025-09-30 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 11cc79d5-2032-34a0-88ae-d7d7ed3504c9 | -10.2041 | -44.8915 | 2025-09-30 01:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 193.7 |
| a8cc4537-4557-39eb-8972-10c004f58dfb | -17.4049 | -47.1431 | 2025-09-30 01:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 4aaccb47-f8e3-3b0f-986d-0c477524ea42 | -14.5327 | -48.4715 | 2025-09-30 01:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| f24dd2c7-f12a-3ccc-854e-8180df7e4c86 | -14.6603 | -46.9663 | 2025-09-30 01:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 856d40f6-79c6-3e1f-becc-c3448f4757e8 | -11.8864 | -48.0545 | 2025-09-30 01:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| ebe98bed-4321-3351-8854-147bb5544ddc | -13.0139 | -44.1243 | 2025-09-30 01:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 5db99801-6bd0-3e83-8473-abcf8e9c9a13 | -10.2045 | -44.8684 | 2025-09-30 01:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 349592bd-75b8-3308-9f78-61ad6fd78648 | -13.3812 | -48.0685 | 2025-09-30 01:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| c0f11f65-f7b6-35bb-938c-364d8126099e | -14.5141 | -48.4299 | 2025-09-30 01:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 87302098-39b5-364d-acb8-6cfb9e2264fc | -11.2138 | -47.2086 | 2025-09-30 01:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| b5c11c96-cac9-3ae2-ab59-a2f812daf160 | -11.2322 | -47.2508 | 2025-09-30 01:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| cb380bf3-09e9-3e23-b393-87e5b65dfded | -4.3538 | -45.5997 | 2025-09-30 01:20:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 022eae60-66f1-35fd-b3c0-6d80c406d942 | -5.5243 | -43.8647 | 2025-09-30 01:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 235e64ba-d3fc-361a-b17d-d36965b578f1 | -14.6408 | -46.9696 | 2025-09-30 01:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| d8f1917b-71b2-3dd0-bf4d-524a92c8a93c | -11.7519 | -44.7461 | 2025-09-30 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 21bf9cee-5bd3-3b67-8200-cc7ae94fb329 | -11.7524 | -44.7228 | 2025-09-30 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 3ac252e8-11a2-3593-b7a9-527f3fad1b67 | -5.5241 | -43.8878 | 2025-09-30 01:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 97acca73-5a5d-32dc-bfa1-f24a5bab7c1e | -5.5243 | -43.8647 | 2025-09-30 01:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| b8e73bdd-ea5f-3eab-81b6-a6c7306f29e2 | -11.8868 | -48.0323 | 2025-09-30 01:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| ae758d30-4645-3e05-923e-6174be06e726 | -14.6603 | -46.9663 | 2025-09-30 01:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 65.5 |
| cda757e4-6829-3ade-bfe9-bce63978a634 | -4.354 | -45.5773 | 2025-09-30 01:30:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 25.5 |
| c145513f-66f5-35b0-bccc-2786c80911e4 | -10.1855 | -44.8709 | 2025-09-30 01:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 0784e97f-9bf1-3368-867d-d3bc0c2da0e9 | -15.2463 | -49.7083 | 2025-09-30 01:30:00 | GOES-19 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 9b5fe4ad-b372-3049-86f6-df5123673742 | -14.5141 | -48.4299 | 2025-09-30 01:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 1e7740b8-6021-3ac1-bba4-58d1af6b228e | -8.2471 | -45.5263 | 2025-09-30 01:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 36eaabfb-7009-31b4-bd35-6f5e7718b989 | -11.1548 | -54.1054 | 2025-09-30 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.0 |
| e7d71be9-2333-3f26-a892-ceb059da2c75 | -11.2326 | -47.2285 | 2025-09-30 01:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 147.1 |
| aadae575-2a02-3123-861e-af1541c27056 | -15.2658 | -49.7052 | 2025-09-30 01:30:00 | GOES-19 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 56.5 |
| c500ef1f-49b8-3a66-b680-d334f1ae4e00 | -11.8864 | -48.0545 | 2025-09-30 01:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 4f68fe7d-3c5d-3e08-819c-9923c656c6d3 | -11.252 | -47.2037 | 2025-09-30 01:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 6ec6bcfe-2df2-34db-8460-219c5e87dc33 | -5.5241 | -43.8878 | 2025-09-30 01:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 338cbe75-8e8b-3683-9ef1-9cd66b09ea7a | -11.1546 | -54.126 | 2025-09-30 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 211.6 |
| 2d65c09c-d5ab-321d-ba19-136dffa85e22 | -12.8429 | -47.0063 | 2025-09-30 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 85857c1d-c381-3599-b363-0172b94290e9 | -11.2513 | -47.2484 | 2025-09-30 01:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| a7494189-3bcc-362a-b793-b78ac00264e2 | -14.5522 | -48.4684 | 2025-09-30 01:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 81.3 |
| fc68da03-4ac5-32d6-8d75-b62713127415 | -17.4049 | -47.1431 | 2025-09-30 01:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 1bae2d05-f071-39f6-ac2a-d10a0e956c77 | -14.6408 | -46.9696 | 2025-09-30 01:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 73.8 |
| d37ed5fd-5763-341b-97a8-4ab203146e6f | -12.8433 | -46.9837 | 2025-09-30 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 30a52a64-cefb-3ab3-8ea3-7892009829f4 | -11.1735 | -54.1242 | 2025-09-30 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 6df8b35b-0117-3655-af58-01bec989c893 | -10.2045 | -44.8684 | 2025-09-30 01:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| d99b3dcc-3ae4-3ef2-a791-77afe8d232ea | -11.2322 | -47.2508 | 2025-09-30 01:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| d21f0ac9-bd46-3a9d-8478-3da02ab584a5 | -11.2516 | -47.226 | 2025-09-30 01:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 36d5394c-2c22-30ba-aca4-12bdc4fa8d33 | -14.5327 | -48.4715 | 2025-09-30 01:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| bee7da7d-ffb8-3a0c-8e2c-3cb418ab3aa3 | -14.5137 | -48.4522 | 2025-09-30 01:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 80b2554e-f815-3055-8c9d-a79d8e96a09e | -10.2041 | -44.8915 | 2025-09-30 01:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 829b747c-56f9-3d09-a409-1bbb7c17e2b3 | -11.7519 | -44.7461 | 2025-09-30 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| cdbaa1d3-58ac-3eb8-9f03-53a99187ec6a | -10.0717 | -50.2173 | 2025-09-30 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 9fa08580-5e5d-3252-ac80-e851dbea76d8 | -10.0714 | -50.2387 | 2025-09-30 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 305112a0-18ff-3a99-a338-fce3d04b59f8 | -10.1851 | -44.8939 | 2025-09-30 01:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 157.0 |
| a3802f08-79c8-3e36-b98f-f6057a30233d | -11.7524 | -44.7228 | 2025-09-30 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| da4f8fd3-8bd1-3a17-9901-3af20f4b802a | -11.1546 | -54.126 | 2025-09-30 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 214.2 |
| ca5f2870-c27f-3100-83dd-a2e0fe91b1e7 | -11.7519 | -44.7461 | 2025-09-30 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| fb609de3-69e5-3535-925f-020293d5c0ba | -10.2041 | -44.8915 | 2025-09-30 01:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 56ed3f83-f8b7-361e-9fe0-9f49e2b34189 | -21.0564 | -45.6881 | 2025-09-30 01:40:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 52299fd9-53ee-3888-92b5-927f8f017701 | -10.1855 | -44.8709 | 2025-09-30 01:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| d284737d-c21b-366e-9f52-0df2ddeb2985 | -11.1735 | -54.1242 | 2025-09-30 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| d597d642-1476-338b-8bc1-80a26d524295 | -14.5752 | -48.2865 | 2025-09-30 01:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 2e4145ad-bf1a-3cf4-9590-736050345905 | -8.2471 | -45.5263 | 2025-09-30 01:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 0a7f9aba-08ca-3693-8e33-5ac352cec9d8 | -14.5137 | -48.4522 | 2025-09-30 01:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 498a156e-b95f-350d-81fd-cecb2c73af93 | -5.5243 | -43.8647 | 2025-09-30 01:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 5af4801d-2482-3b4d-8b53-66bb897721d7 | -12.2121 | -43.7383 | 2025-09-30 01:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 77628753-186f-3824-8002-ec136d57770e | -15.2658 | -49.7052 | 2025-09-30 01:40:00 | GOES-19 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 289fc40d-bb36-3d3d-ad68-65db6e675e8b | -15.2463 | -49.7083 | 2025-09-30 01:40:00 | GOES-19 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| d14639b1-7b4f-36b9-ab4e-67bb4abd9206 | -11.7712 | -44.7432 | 2025-09-30 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| ec8db1fb-2622-3cac-8e35-ce88a98b5014 | -11.2322 | -47.2508 | 2025-09-30 01:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 215.1 |
| c9581d79-d03e-38d2-8baf-65393b78ee94 | -10.1851 | -44.8939 | 2025-09-30 01:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 159.7 |
| 257c9bd0-18ab-374b-b40d-e37e7786f524 | -11.8868 | -48.0323 | 2025-09-30 01:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| a807bd5f-e8f5-3daa-8de2-1f244ce55d02 | -10.2045 | -44.8684 | 2025-09-30 01:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 55a657f0-822a-3a88-9d02-f857cb6cb734 | -14.5141 | -48.4299 | 2025-09-30 01:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 90629461-f3cf-383c-bbda-30ec63e012fa | -11.071 | -47.8262 | 2025-09-30 01:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| c81229a7-dfdb-3cb9-8892-3a86d696a7a4 | -5.5241 | -43.8878 | 2025-09-30 01:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 92ed565e-40c9-3db5-8236-e42461778113 | -11.2513 | -47.2484 | 2025-09-30 01:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 593f7005-efbf-38e3-9fa0-58b41f3168b7 | -14.5522 | -48.4684 | 2025-09-30 01:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 73.2 |


[Clique aqui para ver as próximas entradas](README13.md)
