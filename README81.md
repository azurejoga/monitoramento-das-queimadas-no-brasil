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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e22cea87-cac8-3057-8d78-8bd9b1a5f573 | -17.07313 | -56.27599 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.2 |
| 7f9a3d83-fb25-32f6-9311-39884d6c9a7a | -17.07154 | -56.25341 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| c2f46726-24cf-36e9-9663-3902e2bb3e4b | -17.07038 | -56.25861 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| e8ffd7e1-f2a9-39a9-9439-0aee72ffeb0f | -17.06922 | -56.26384 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 329910b6-4fa8-3854-8eb8-e963374f1ae1 | -17.06805 | -56.26911 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 559fe3ce-cc57-3b8d-bded-07ca1606f06c | -17.06688 | -56.2744 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| d0f41025-afd8-3fca-a90a-a0c69c503e22 | -17.0657 | -56.27969 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| d2e65fc5-0627-3087-b483-91015261dc92 | -17.06529 | -56.25184 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| f41afa62-d640-312f-ac01-579986242c4d | -17.06413 | -56.25706 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| e37d55d4-c62d-3cd2-873d-eee4bf4763c6 | -17.06297 | -56.26228 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 7d2622fa-84fe-3dbf-88b1-94de063a61a7 | -17.0618 | -56.26753 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 20aa7ccd-2e6f-3e08-882f-1517df20c346 | -17.06138 | -56.23978 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 671b7a1a-314c-3cfe-a1f1-2bd808e3f67b | -17.06062 | -56.27281 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| bb289d2f-4829-3d9b-8461-07779008c54f | -17.05943 | -56.27813 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 96f5d06c-75ea-3510-a1ff-92716fcb37ce | -17.05787 | -56.2555 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 9e8197d5-f636-3534-8317-9664bd98e9b6 | -17.0563 | -56.23297 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 571f3bc8-2508-3458-912d-20d834ae29d9 | -13.13972 | -48.54945 | 2024-09-26 04:08:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2684643c-9bf7-32dc-b3a2-062782558f1e | -13.31772 | -42.45022 | 2024-09-26 04:08:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7e9c7bdf-67d7-3709-a7a7-5fe8c6526db5 | -13.3144 | -42.44969 | 2024-09-26 04:08:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1acaa9e1-946f-35e1-b080-db468d30cc99 | -14.56146 | -45.70112 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 955f62f0-4e16-3285-b9fc-8d09abf55c92 | -14.5613 | -45.68064 | 2024-09-26 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 073e6d9d-9797-3e1c-b75e-43ac0929fb8c | -13.31386 | -42.45323 | 2024-09-26 04:08:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 59c57f01-b43f-3aba-bbf1-861fc0f2a627 | -12.22911 | -45.53082 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7249b6ef-bdd1-3f47-90a5-25d93950632c | -12.22826 | -45.51392 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77f4cb1f-55c1-3f83-8d2b-cfaf03e68921 | -19.71583 | -40.05909 | 2024-09-26 04:08:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6228fc16-3608-31cb-b6ab-7f77e804be5d | -19.63067 | -40.21027 | 2024-09-26 04:08:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 344371a4-dacc-31c3-a72d-cbbdec3477e3 | -19.55832 | -39.94578 | 2024-09-26 04:08:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 379a952c-caff-305a-aa8d-d5c197f53951 | -17.05646 | -41.15824 | 2024-09-26 04:08:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3d92dcd7-ea66-37cb-bedd-7d1acc87d292 | -17.05353 | -41.15361 | 2024-09-26 04:08:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 0a03c11a-b428-33b0-b8c0-1c5f02e3bb3f | -17.05295 | -41.15764 | 2024-09-26 04:08:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3bf13185-5e2a-3c49-b991-c64be0935634 | -17.05012 | -41.15006 | 2024-09-26 04:08:00 | NOAA-20 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3c0c2eed-7db6-3783-a43b-a83311a43f18 | -17.05002 | -41.15298 | 2024-09-26 04:08:00 | NOAA-20 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| b46979b2-efc0-3a12-a07d-a07b5a42fa35 | -17.04952 | -41.15417 | 2024-09-26 04:08:00 | NOAA-20 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 032c79b0-a372-335b-b4ed-31ae49cd0126 | -19.46546 | -40.90399 | 2024-09-26 04:08:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 335b29a5-7dc4-31af-863a-4b8ea82d73c2 | -19.46505 | -40.90561 | 2024-09-26 04:08:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0fcd2e23-237e-334e-aa9c-ab23acf34e8a | -19.46181 | -40.90339 | 2024-09-26 04:08:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 424c8586-103b-34c7-8f0b-8292221a77b1 | -19.4614 | -40.90504 | 2024-09-26 04:08:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 13ba4dd5-e460-379f-80c7-d7d0ac8454b8 | -19.44077 | -40.78582 | 2024-09-26 04:08:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5fc53c62-2bee-3f84-9431-9b4169c21f47 | -19.4401 | -40.79066 | 2024-09-26 04:08:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 683b778b-9c93-366f-a3c2-12e673d49234 | -19.145 | -41.38224 | 2024-09-26 04:08:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.9 |
| 133af62a-c4a1-3c8b-b9ac-fe1bfc30dcd4 | -19.1444 | -41.3865 | 2024-09-26 04:08:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.1 |
| deca60a1-7dc1-3b71-bded-1ed5cfcded59 | -19.14084 | -41.38597 | 2024-09-26 04:08:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.1 |
| cb8500e2-b63a-369f-9736-d7da6ae5d0c1 | -19.13786 | -41.38131 | 2024-09-26 04:08:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 10a8fbf3-e7bd-3d67-b287-72da08db6f61 | -18.99357 | -41.05276 | 2024-09-26 04:08:00 | NOAA-20 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| b6c34a46-728f-37db-880d-d85e08de4abd | -18.99301 | -41.05678 | 2024-09-26 04:08:00 | NOAA-20 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| f6be807d-79cd-37d8-85b4-efbe844dd4c7 | -18.644 | -41.40521 | 2024-09-26 04:08:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1e450c1a-151b-3c9f-94c3-d75c152bfcc8 | -18.56911 | -41.32222 | 2024-09-26 04:08:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 18f35484-0c07-3aff-9d24-bd794bb2ab72 | -18.56557 | -41.32164 | 2024-09-26 04:08:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6431563f-dc4c-3cbc-b457-223a73fd4ade | -18.25707 | -41.31207 | 2024-09-26 04:08:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| ae8e90bf-ba63-3dd3-abb7-33a7a9be525b | -18.25647 | -41.31624 | 2024-09-26 04:08:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| bb0fe1d1-e12d-3419-a5e0-c39cfc4257ba | -18.25589 | -41.3204 | 2024-09-26 04:08:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 3915db68-c2fb-3ec4-bdab-2a4b3529b9eb | -18.25295 | -41.31564 | 2024-09-26 04:08:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6eb0866c-e403-3bbb-9af5-3a28a420c3c0 | -18.25236 | -41.3198 | 2024-09-26 04:08:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5d6cc2c6-db23-37b6-b629-85a12b6f6536 | -20.64152 | -41.06944 | 2024-09-26 04:08:00 | NOAA-20 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 23e1e8c4-6db3-395c-996b-bb18c69aaa44 | -20.63781 | -41.06921 | 2024-09-26 04:08:00 | NOAA-20 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b69a7948-57a5-3289-ad23-b89d32f1f551 | -20.62243 | -41.21159 | 2024-09-26 04:08:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| db951a16-1744-3939-9d7c-d5a612d8057c | -20.61878 | -41.2111 | 2024-09-26 04:08:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c66ed0aa-347a-3f40-a46e-da9394245aaa | -20.61514 | -41.21052 | 2024-09-26 04:08:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d5190ff7-b349-3b55-ad34-d3217e4bbf2e | -20.61452 | -41.21515 | 2024-09-26 04:08:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6d21809b-0555-3f97-bf12-fe0f19cc89eb | -20.60666 | -41.24609 | 2024-09-26 04:08:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 82be293b-1029-3295-b119-d0d2ba0896f0 | -20.60657 | -41.24337 | 2024-09-26 04:08:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ba9778de-2441-3fcb-ae45-181a1cc00f7d | -20.60598 | -41.24763 | 2024-09-26 04:08:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5f1636be-f628-3bb7-b868-1d723d47b764 | -20.60359 | -41.2413 | 2024-09-26 04:08:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d3e711e0-1bfe-3819-ae7d-996546487e68 | -20.60301 | -41.24559 | 2024-09-26 04:08:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1e209323-cf99-3c72-a190-8b064c04bf88 | -20.60293 | -41.24286 | 2024-09-26 04:08:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 521e3428-9260-3999-b021-8b009f30b18e | -20.60233 | -41.24719 | 2024-09-26 04:08:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b3564a64-63a0-3ddc-be85-441053f062ad | -20.6012 | -41.23136 | 2024-09-26 04:08:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 37a863a1-97fc-3c5d-b9f7-6d4cf421fa51 | -20.60056 | -41.23322 | 2024-09-26 04:08:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ecc95656-9789-342f-beb9-cbdaabe8bc60 | -20.60054 | -41.23635 | 2024-09-26 04:08:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c2d7552a-2782-3ccc-861f-709a3038935f | -20.59994 | -41.24088 | 2024-09-26 04:08:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c0a761cf-e308-38d9-8ecb-c79eb65eda88 | -20.59988 | -41.23806 | 2024-09-26 04:08:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 187df98d-5a8e-3b21-88bd-8de17f1f6aa6 | -20.59936 | -41.24522 | 2024-09-26 04:08:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 43114082-82c2-32bd-95f7-a63598c276f5 | -20.59928 | -41.24244 | 2024-09-26 04:08:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1669c5b8-85cf-3605-bddd-cc0ea64b7dc2 | -20.59692 | -41.23267 | 2024-09-26 04:08:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f9e0b287-d63f-35d8-a615-115301f1adbd | -20.59625 | -41.23748 | 2024-09-26 04:08:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5bf54486-223d-355d-bf3d-b0d2cb99c88c | -20.4299 | -41.88097 | 2024-09-26 04:08:00 | NOAA-20 | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| cc1401d2-fc58-382a-807f-a3ffb66dc268 | -20.4264 | -41.88028 | 2024-09-26 04:08:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 9e7a56f0-1c59-34df-86f2-866fe0b098e9 | -20.42583 | -41.8843 | 2024-09-26 04:08:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 663e8ed6-790f-389c-9ae5-465f6715bb57 | -20.4229 | -41.87954 | 2024-09-26 04:08:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 924b59be-2a46-383d-9bb6-ed68280bac7f | -20.42234 | -41.8835 | 2024-09-26 04:08:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6143268c-07af-3e81-8a0a-94ae5e601455 | -20.41994 | -41.8749 | 2024-09-26 04:08:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 02160c92-b9be-3b1c-b273-7d9dd4bee027 | -20.41939 | -41.8789 | 2024-09-26 04:08:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2b54e189-a781-30ad-9370-e2d2b89c9252 | -20.41641 | -41.8744 | 2024-09-26 04:08:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 02935937-446f-3422-afaa-0a4dfba3e8e9 | -20.41586 | -41.87835 | 2024-09-26 04:08:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d6e904fd-5118-35ec-a637-bdd6aecc6006 | -20.41288 | -41.87392 | 2024-09-26 04:08:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cdd39b13-bdc6-3e8e-82f5-3b26fcb0e148 | -20.41233 | -41.87786 | 2024-09-26 04:08:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 96af7be0-e90d-3675-88bd-550ff8b10197 | -20.40899 | -41.87561 | 2024-09-26 04:08:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6ab6e9cb-4e05-3e57-aff7-7162e488649d | -20.40878 | -41.87756 | 2024-09-26 04:08:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 30a1bd8c-e892-325c-8218-f6368e9931f0 | -20.40841 | -41.87963 | 2024-09-26 04:08:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 3703dffa-8219-3d6a-a90a-0773679b2216 | -20.40823 | -41.88151 | 2024-09-26 04:08:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| dbbfb34b-9583-3c2c-84f8-d22fcb691c7e | -20.40132 | -41.87882 | 2024-09-26 04:08:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| e1d73874-8072-3d13-b868-e2b084244550 | -12.22759 | -45.51798 | 2024-09-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a073dae2-d1bf-3ebd-b5a6-013436bbdda2 | -20.40078 | -41.88267 | 2024-09-26 04:08:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 1d332582-de11-3778-9c74-c6fb296bccdd | -20.39726 | -41.8821 | 2024-09-26 04:08:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 3692c76e-c979-3202-9c8e-9066fd553ea0 | -19.97243 | -40.65021 | 2024-09-26 04:08:00 | NOAA-20 | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ee1717a4-eee6-35ee-950c-43de2a10955d | -13.4085 | -41.325 | 2024-09-26 04:08:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2ab2a1f2-eb3d-38fc-8172-14ec93a60cb8 | -13.40793 | -41.32873 | 2024-09-26 04:08:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5d4adbdf-00f1-34cb-9774-c6d6da8b19d5 | -13.26678 | -41.49956 | 2024-09-26 04:08:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5c27a409-b93d-317e-ba86-a5a42aa30c22 | -13.26397 | -41.49535 | 2024-09-26 04:08:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eccbba65-d141-30c1-9df4-0b2d21a11202 | -13.26341 | -41.49903 | 2024-09-26 04:08:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |


[Clique aqui para ver as próximas entradas](README82.md)
