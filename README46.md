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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09bfbd43-6980-3bbe-80ee-af8e010c9c77 | -11.44569 | -49.75017 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07b93a97-3e71-348e-9924-077116848932 | -14.51652 | -48.34806 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5d37436-3bf2-31d4-8ae2-a910d05f2809 | -13.64433 | -49.45976 | 2025-10-24 04:40:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8062ada-58b6-34c8-87e9-22ef2ed48b18 | -17.37277 | -52.01649 | 2025-10-24 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5743ae95-b7ea-3ba7-9ebc-055474f7d3b2 | -13.34439 | -47.9698 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c038ec6-075e-309c-bcf6-714e9858099a | -11.7422 | -47.61779 | 2025-10-24 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82bc7f5c-d6fd-31eb-ac00-17e2566c509a | -14.63571 | -48.34871 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c18312c7-0fcc-352e-8f56-010dd7e3d15f | -13.28671 | -47.49083 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 015a8aba-4337-3d41-b045-b8d8d8901e3f | -14.46371 | -47.91821 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 33ee7478-7d53-3e07-af6a-b9c56ef042dd | -16.99204 | -51.48011 | 2025-10-24 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e84e2f3f-c2da-309c-a204-c1975f6f02aa | -15.44708 | -48.57603 | 2025-10-24 04:40:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6a24e2b-269c-364c-87ab-1294bf3932ed | -17.65822 | -46.65289 | 2025-10-24 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bcf126e3-6538-3e35-a9c2-de226739184e | -12.82513 | -50.95862 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dfe9a956-4954-3cba-9d51-0ed32e9dd722 | -13.92593 | -48.38797 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc0fca9d-634b-3a0d-9284-3d254162bd7a | -15.35641 | -48.09613 | 2025-10-24 04:40:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cea7e2a9-9e0a-3079-9834-2b925188c2e2 | -13.53619 | -47.54525 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73c86fcf-d50c-3637-89a9-9dc6236c2dd2 | -13.19597 | -47.75359 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bf12ec5c-56ed-36bb-9615-fdff7a32da24 | -12.22647 | -43.31001 | 2025-10-24 04:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb18f70e-ed4b-344f-891a-cb7dbba2d6d0 | -14.42542 | -50.95657 | 2025-10-24 04:40:00 | NOAA-20 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11ccdd7b-1d67-35d9-8341-3695478666bb | -15.59813 | -48.04689 | 2025-10-24 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 987d6bc4-ceba-3d97-8c67-5de7ea19659b | -11.46495 | -43.70836 | 2025-10-24 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31738d84-1b2c-362c-8658-6b205f183bbe | -14.54178 | -48.02427 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6112253-d546-3c14-b6b2-1b032215ce06 | -16.64381 | -43.71115 | 2025-10-24 04:40:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1da2229-2128-310c-ab11-992117001b5f | -11.38301 | -47.65614 | 2025-10-24 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f6b0da1-77a1-3b1d-9f9e-6448545fb3d8 | -13.64095 | -49.45924 | 2025-10-24 04:40:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 404dc36d-bd33-383c-b152-b3afc4f582bb | -16.95226 | -53.22362 | 2025-10-24 04:40:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b9f8d0d-6bd0-3adc-b423-76c64d3aa3e4 | -12.03279 | -46.53214 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aaa32f79-fe23-3cf4-be9f-c688775f9cc0 | -14.23599 | -44.59137 | 2025-10-24 04:40:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 277ae416-ab30-3498-befa-84bb51e88844 | -12.82346 | -50.96919 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e503f8dc-bd26-39f5-ac43-0a916562199e | -11.01736 | -49.84118 | 2025-10-24 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b47c86f-1060-3c00-a33f-bb2eb62f9987 | -13.34794 | -47.9704 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45fd660a-d431-3c0c-8814-3623c5448053 | -14.47801 | -47.92134 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 559c7fd2-d2f7-3a56-84f0-a087ac3b11d9 | -13.89018 | -48.35831 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 84eac0d7-0417-3959-abf2-f521df68dab7 | -17.46443 | -48.40091 | 2025-10-24 04:40:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3ac7eb8-6d74-3754-ba2a-99eb9ad38466 | -11.59328 | -47.60252 | 2025-10-24 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 142c4337-83d6-3a1a-84a8-d28ac794e94c | -13.21813 | -47.75264 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49080f89-aad0-3b37-96b4-1e29ac8d2c88 | -11.02177 | -49.83467 | 2025-10-24 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a71b611f-39e3-38ce-b84e-8a52a5d4d177 | -17.6587 | -46.64919 | 2025-10-24 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7b6cb209-6ae8-3e43-9ffc-3c22049ccb55 | -12.82724 | -48.63361 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f1d62b9-0898-37c6-a542-272e7e37b391 | -11.0486 | -54.15846 | 2025-10-24 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 388362f4-1319-3ec5-96ab-4c64c4bbf15c | -12.81465 | -50.96051 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0bedd13d-6ee9-3e7a-a1fb-b42752b031c2 | -13.07781 | -47.56785 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67bcc10f-4242-3fa5-a12d-02e948b08f7b | -14.02545 | -48.00464 | 2025-10-24 04:40:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e206c8f2-5a6d-3849-a1ad-ef0608cb2c9f | -13.34733 | -47.9746 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d75d2b10-9e28-32f3-b0f3-296deded7957 | -13.25069 | -50.15099 | 2025-10-24 04:40:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 34562cff-422c-3438-bd9a-974dcffbb31f | -11.36039 | -45.96736 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d7b8187-fbb3-3085-9199-402e30927a0b | -11.36775 | -45.94336 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d3b535fd-0d7e-33de-bbea-335112da5137 | -11.55768 | -54.51978 | 2025-10-24 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1005c7ad-3b20-3b6f-a95d-9794c930ac93 | -11.36458 | -45.93781 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 42aa75bd-bf52-3102-9877-ae349e40ae6c | -14.47212 | -47.91116 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac0e0343-f829-3a0d-b620-8b068a192f59 | -12.07662 | -46.44228 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efbfec06-8eac-338a-9608-31c243f454d9 | -11.35791 | -45.95691 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd11bb4c-6ae3-3762-b6b3-49bc6652734a | -12.02245 | -46.9217 | 2025-10-24 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 052dc867-b663-327d-9113-90aec54ff87f | -14.03742 | -48.7286 | 2025-10-24 04:40:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a264e775-f38a-3b7d-ac55-4bf03e5bb5d1 | -11.01681 | -47.88091 | 2025-10-24 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 74233363-9854-3aaa-9a1f-742262a2f09a | -13.90476 | -48.38539 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbee67d9-9c9c-3cda-a46b-4af63c6999c0 | -13.72411 | -51.45964 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c0dca4b-988d-3088-a4d4-15fc82d6b89c | -10.43111 | -55.63924 | 2025-10-24 04:40:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 889c3f19-1c85-3aa5-8678-2f92f6d6b839 | -11.48634 | -54.01199 | 2025-10-24 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fd0828c-699d-3a20-8198-f4feecee44bd | -12.72944 | -46.95382 | 2025-10-24 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62da231d-38aa-315d-a70e-6963c1317578 | -12.77698 | -47.37791 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0ee54abd-d90a-3934-9b60-9a56b22c69c5 | -11.34807 | -55.08331 | 2025-10-24 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bf96efe-de86-3d50-b77d-9ae7f72e8465 | -13.33786 | -47.96468 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 403fdb40-d058-3097-b207-0ba0bd15abef | -12.25032 | -47.45539 | 2025-10-24 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34c6e09e-5d75-3dee-a74d-8d80690c14bb | -12.05955 | -46.42572 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7d212d9e-5d13-33f2-992f-d46968c3ce62 | -11.97474 | -49.17941 | 2025-10-24 04:40:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0f5f00e7-d17d-3f22-a9d1-35f0b1e3e4e8 | -11.02536 | -53.99032 | 2025-10-24 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5dd713c-e38d-330e-a270-b394b6da76b5 | -12.83022 | -48.66076 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3a0c07a-2633-3d1f-9ca3-267ef23a19bd | -10.58978 | -49.64352 | 2025-10-24 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2aeeaf30-cb5c-3d2f-a3ec-caa222c55c28 | -10.85127 | -48.96584 | 2025-10-24 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b2b34cc-a5d7-30c3-8399-7865bb1bccff | -12.82381 | -48.63299 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e597c2ca-3274-35f8-baf3-0e02c86ffd46 | -12.36949 | -51.4718 | 2025-10-24 04:40:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe30692d-173d-3202-9bf7-f90941a9b374 | -12.81753 | -48.62779 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0155386f-edf3-3bd1-a0e1-149f93e1fc9b | -13.40245 | -47.35907 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca74f56c-fbc4-3a97-8aa6-8ce2a4a16201 | -14.54118 | -48.02841 | 2025-10-24 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d262296-7c9d-3cfb-8b08-6be1f8efe986 | -13.33376 | -47.96785 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6046fd38-b7fb-36b2-adf2-fd0c48dd30e6 | -12.81082 | -50.94181 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2abbbe6c-a493-3278-82ba-7aecaf6ed89e | -11.48925 | -54.01701 | 2025-10-24 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 781ff236-479e-30df-851f-d3e90ab79832 | -13.90769 | -48.38991 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10e72ebf-158e-3f53-855b-2bdc4b22b0f3 | -10.6683 | -54.31368 | 2025-10-24 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b861fbd-9962-34a7-bfff-65460bad921b | -11.32983 | -56.20706 | 2025-10-24 04:40:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40b3dd3e-a196-3411-b0e8-69946f0fef7b | -12.29419 | -47.45797 | 2025-10-24 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9f6554cc-a806-3dd8-8a4b-5ffc28ce1d25 | -11.09818 | -54.39014 | 2025-10-24 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2a525be-9533-3354-951c-2df0e79d220b | -13.91069 | -48.36922 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a71bb40-6b16-3d3c-9d6d-b6b0fecce4a4 | -14.38364 | -51.52149 | 2025-10-24 04:40:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62d72f68-71cf-317f-ab62-7a81bc117c2c | -11.36109 | -45.96242 | 2025-10-24 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d50591fa-534e-36fa-8ebf-dcdd10a4e199 | -13.66397 | -47.95463 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 309999e4-8173-3284-a707-7370758fa458 | -15.28537 | -50.77589 | 2025-10-24 04:40:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bad4f5c-1a8e-3f98-ad47-3a0da5d8d34a | -12.80957 | -48.65756 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2fe9ac55-cf51-3c4c-a66c-592f4af12882 | -11.04444 | -47.89512 | 2025-10-24 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 54b27dd1-9a99-3e34-8b79-0b99b70816df | -12.92623 | -48.50627 | 2025-10-24 04:40:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3786e96b-db60-39b6-96f1-4870be8f12af | -14.43977 | -50.95166 | 2025-10-24 04:40:00 | NOAA-20 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27c3803c-c1aa-31f8-9fbd-c91c86ad66ab | -10.66372 | -54.31772 | 2025-10-24 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0043d7af-d11c-3b1b-84c7-e68288acadaa | -17.03989 | -51.49904 | 2025-10-24 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e530f502-a5f6-3a10-ace7-e4fc8086300d | -12.81796 | -50.96106 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab8d2f56-d77d-3bd7-b154-285a5b22ad08 | -16.3732 | -51.54953 | 2025-10-24 04:40:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 896591ab-3bdc-3d37-b18e-70e6729f7725 | -14.20726 | -44.60531 | 2025-10-24 04:40:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d9b4db5-3371-39a5-8b9f-42839e05b5d6 | -15.13109 | -49.5551 | 2025-10-24 04:40:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f15a14db-3a28-3c08-982b-08d6611e0842 | -10.83965 | -49.38912 | 2025-10-24 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 652defca-3f83-374a-b692-8e79152c2bb2 | -14.6959 | -52.82868 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README47.md)
