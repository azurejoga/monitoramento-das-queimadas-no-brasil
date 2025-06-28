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
| ba1a698e-5935-361d-b139-e0a53ce77c33 | -9.1205 | -49.4958 | 2025-06-28 01:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 144.5 |
| bb6fb7e3-f2a0-394f-a31b-51e8caef54e2 | -11.0266 | -55.3789 | 2025-06-28 01:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 78a5d3c7-bb7b-3dd1-8e55-3446837c2140 | -7.2028 | -43.0936 | 2025-06-28 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.5 |
| 8aeb61b2-f5ff-372c-bc72-8118fb29f34b | -7.2217 | -43.0917 | 2025-06-28 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 139.6 |
| f51bd6fa-d66a-3902-aacb-f1030df05ce5 | -7.2031 | -43.0701 | 2025-06-28 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| 6b223cc0-9a73-310f-80e6-388572f2f4ac | -6.9108 | -43.9834 | 2025-06-28 01:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 5c5e8c0c-1182-3af6-9b03-6ce707913bbd | -12.2715 | -46.7739 | 2025-06-28 01:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| c93536a2-0f31-30ba-aa50-bea0d80b3246 | -11.0457 | -55.3571 | 2025-06-28 01:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 53bcfd7e-26a3-328f-ab8d-8bb2138af952 | -11.0453 | -55.3976 | 2025-06-28 01:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 5891c70e-77f0-393d-b036-4539a44d7223 | -9.1208 | -49.4743 | 2025-06-28 01:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 83bb5f54-91b8-3b40-8151-893e0f8fa93b | -9.7041 | -56.1843 | 2025-06-28 01:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 83841414-3d57-3a28-b362-5153656dbf9b | -9.1017 | -49.4976 | 2025-06-28 01:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 77788699-9f98-3ac8-b7dc-006bec2b755a | -10.8382 | -53.7648 | 2025-06-28 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| ff9f3326-9017-3d38-ab43-e8c1bbc7eabe | -11.2853 | -52.7508 | 2025-06-28 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 54e76dff-4548-3a13-8778-ca397543f349 | -11.2664 | -52.7527 | 2025-06-28 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 176.8 |
| 1a2d11fd-ef2d-3efa-ae0d-a1a8f683653f | -6.911 | -43.9602 | 2025-06-28 01:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 5edacc7a-b379-3a8b-bc92-17ecd2b93a8e | -11.0455 | -55.3773 | 2025-06-28 01:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 388.8 |
| 24b9c2d1-4bb5-31e8-9429-819d8bd823dc | -9.7228 | -56.183 | 2025-06-28 01:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 46de832a-8352-3fe6-91ac-6c3a0812fc76 | -7.2219 | -43.0682 | 2025-06-28 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 139.9 |
| 5b0538a2-6f9a-3344-b22c-f086cad77761 | -9.1208 | -49.4743 | 2025-06-28 01:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 7b76d239-b4d8-34d4-8b79-65d8893e12e5 | -12.2523 | -46.7766 | 2025-06-28 01:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 7ab81127-c888-3dd9-8ee2-489b8f4fbe0f | -12.2715 | -46.7739 | 2025-06-28 01:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 5dbe194f-3108-36c9-a0c0-e1d820af1c97 | -9.7228 | -56.183 | 2025-06-28 01:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 51876e0f-3316-3b65-b5f4-cc90133a90ac | -6.8922 | -43.9619 | 2025-06-28 01:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 53.4 |
| e379630e-b7e5-32c7-bf1b-0d7afec16dbd | -6.892 | -43.9851 | 2025-06-28 01:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 8fda4b04-27b9-3c58-bdb9-6a604c840671 | -11.2853 | -52.7508 | 2025-06-28 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 572cf4b0-0e94-3630-84a2-99a52d0207f5 | -9.102 | -49.4761 | 2025-06-28 01:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 9e997b38-9ad6-389f-9723-21b90f3798fd | -9.1205 | -49.4958 | 2025-06-28 01:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 307f2364-30de-361f-b573-dab9f9020f88 | -10.8382 | -53.7648 | 2025-06-28 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 01ccc882-3cca-3ad8-ac9f-05bfe64ac69e | -11.0644 | -55.3757 | 2025-06-28 01:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 102.9 |
| dbcb31e3-eaaf-3d00-be74-7d9d28f7a9fc | -7.2031 | -43.0701 | 2025-06-28 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.0 |
| de0f33ac-3904-3a13-9501-98697763c5cb | -11.0457 | -55.3571 | 2025-06-28 01:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 91f2dc22-2d6e-300e-b6bf-d6b8c13e9007 | -6.9416 | -42.8834 | 2025-06-28 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 3dabea81-9b5b-3b83-9c20-b12e055bfd59 | -11.2666 | -52.7318 | 2025-06-28 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| cc38ab27-e31e-3db6-a7de-bad679e65d37 | -9.7041 | -56.1843 | 2025-06-28 01:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 0edfe49a-0569-3e33-b12c-cc6019ee777f | -11.0455 | -55.3773 | 2025-06-28 01:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 302.8 |
| 03df5cf7-e90b-35cf-820d-9dd4ad13806b | -11.0453 | -55.3976 | 2025-06-28 01:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 7ea374cb-c5cf-3052-8e7d-16db166c3b35 | -9.1017 | -49.4976 | 2025-06-28 01:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 9161a97f-f795-3b53-a7ed-998a0bce8b61 | -11.0266 | -55.3789 | 2025-06-28 01:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 66cf8ce0-d045-3426-8bd6-8b2bdf7aece6 | -6.911 | -43.9602 | 2025-06-28 01:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 79412ad6-6e5f-373c-bdc6-a38b94f11296 | -6.9108 | -43.9834 | 2025-06-28 01:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 9a122b4e-ab83-3837-8e45-45053b733dca | -11.2664 | -52.7527 | 2025-06-28 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 152.8 |
| 2212ec40-19a4-3312-8b92-96e0b89fd1ed | -7.2217 | -43.0917 | 2025-06-28 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| ebe03434-d1f4-30bf-a03b-f084590e858b | -9.7228 | -56.183 | 2025-06-28 01:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| fbbe6f90-b36f-3c9f-bdcd-fc1197be3bb3 | -6.9108 | -43.9834 | 2025-06-28 01:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 88ab64c7-de09-3805-8928-77e934b38af8 | -6.9416 | -42.8834 | 2025-06-28 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.0 |
| 8f514654-c7c6-3632-a8a2-f8ea97bb4608 | -11.2666 | -52.7318 | 2025-06-28 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 3ff3c33c-0e2a-337a-8947-4d3871f0c091 | -11.2853 | -52.7508 | 2025-06-28 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 0cbfb8f0-01de-344e-a715-1ae095c99fd2 | -7.2031 | -43.0701 | 2025-06-28 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| 715328f8-7738-3f62-b64f-611441adda54 | -9.1208 | -49.4743 | 2025-06-28 01:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 099e111a-136f-3a78-8434-feefcd5c1545 | -7.2028 | -43.0936 | 2025-06-28 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| ec799e5e-2502-3ff7-8d03-7019e415390d | -6.892 | -43.9851 | 2025-06-28 01:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 2301e990-d2e4-3794-ac19-687f0c9e9515 | -9.1017 | -49.4976 | 2025-06-28 01:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 62114d75-0edb-3c51-b916-f656687dc16b | -11.0457 | -55.3571 | 2025-06-28 01:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 505fe64e-f665-3ee9-adff-f5bd8c258b1a | -11.2664 | -52.7527 | 2025-06-28 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 197.5 |
| a6fb8644-cbab-32a7-a6cd-618272e8d64d | -12.2715 | -46.7739 | 2025-06-28 01:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 140323ca-acc9-3dee-8b0c-28bf484177e0 | -12.2523 | -46.7766 | 2025-06-28 01:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| f5511b3f-6be8-3314-a41e-a36f00b4411b | -7.2219 | -43.0682 | 2025-06-28 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 127.3 |
| de02da19-69b6-370f-9e12-bcaee4bd46b4 | -9.7041 | -56.1843 | 2025-06-28 01:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 038a6978-f1ce-345d-bc86-9c87d2f09e50 | -7.2217 | -43.0917 | 2025-06-28 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 123.4 |
| 0e5e3aaf-5630-38ee-8a69-f95215fd7ce3 | -11.0644 | -55.3757 | 2025-06-28 01:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 8cb0b7cd-987b-33fc-bded-194116e124db | -11.0266 | -55.3789 | 2025-06-28 01:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 3430ca3f-88d3-30bd-bbad-b5488db3f292 | -11.0455 | -55.3773 | 2025-06-28 01:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 315.8 |
| 8e1151c0-8747-32aa-8162-28afaacdf28c | -9.102 | -49.4761 | 2025-06-28 01:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| c90ac634-5b87-368a-936f-584c026d4246 | -9.1205 | -49.4958 | 2025-06-28 01:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 8ca2f6b9-b632-3074-b687-4505c4784f73 | -7.2031 | -43.0701 | 2025-06-28 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 313acd0a-331b-398d-a445-93bc62bc7930 | -6.892 | -43.9851 | 2025-06-28 01:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 107.2 |
| a5212204-7702-342b-a98f-77adb7da87ff | -11.2853 | -52.7508 | 2025-06-28 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 2d9b33d0-d9f2-32cd-9be3-d67286fef247 | -12.2527 | -46.754 | 2025-06-28 01:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 0353d4b3-d341-36f6-acc9-3adeae1af05c | -11.2856 | -52.7299 | 2025-06-28 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| d032c07b-b1d2-3b9d-bbb8-1e9af32eed18 | -6.9108 | -43.9834 | 2025-06-28 01:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 9bedbc50-1b38-3553-bed0-0ffdc2d12104 | -11.0266 | -55.3789 | 2025-06-28 01:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| f0d88ca5-ac8c-338f-9265-efffe1fbbd4e | -7.2219 | -43.0682 | 2025-06-28 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 127.7 |
| a2ddb3ac-667a-3c1b-898b-145d7caad556 | -11.0457 | -55.3571 | 2025-06-28 01:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| d7384cf0-df0b-3508-bf20-6116b35dca95 | -7.2028 | -43.0936 | 2025-06-28 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.7 |
| 4d7d6e3e-a35b-3d27-9564-b236d78ee892 | -12.2523 | -46.7766 | 2025-06-28 01:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| ad4a38e0-7078-35d1-9563-89b187414dc3 | -11.2666 | -52.7318 | 2025-06-28 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| f224e694-2205-336a-b5e3-b682e2209762 | -9.7228 | -56.183 | 2025-06-28 01:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| a60eb7d2-706d-3359-b821-ad5af243c0a2 | -11.0455 | -55.3773 | 2025-06-28 01:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 245.3 |
| 2d1b6972-9261-3736-b607-5ff2352e8c8f | -11.0646 | -55.3555 | 2025-06-28 01:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| bc7b21f6-4fee-30fd-b791-99727bdddf40 | -11.0644 | -55.3757 | 2025-06-28 01:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 122.5 |
| ed266c21-3f70-37a6-bf41-aad91d58065c | -9.7041 | -56.1843 | 2025-06-28 01:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 0c61e6ae-7a9b-3da8-94b9-fdf2a1454cf7 | -7.2217 | -43.0917 | 2025-06-28 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.0 |
| 5d1c76ca-9677-3738-ac3b-76ff2fafa0eb | -9.1205 | -49.4958 | 2025-06-28 01:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 17a3beb7-b075-37d4-89e4-e5890fa81b37 | -6.9416 | -42.8834 | 2025-06-28 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| f46c8644-f040-3212-90fc-0cebfa1fc989 | -11.2664 | -52.7527 | 2025-06-28 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 157533d0-e31a-30b6-887b-977f6181e8b4 | -9.1208 | -49.4743 | 2025-06-28 01:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 8dac143e-191e-322c-9072-60936cde0104 | -9.7228 | -56.183 | 2025-06-28 01:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| bb960b2b-179e-3bf0-aefe-0bd45946f306 | -11.0457 | -55.3571 | 2025-06-28 01:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 02d10cf3-bd2a-36a4-8e2b-30c63200291d | -11.0266 | -55.3789 | 2025-06-28 01:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 6a348de6-7430-3109-bfd5-491f5b231804 | -9.1208 | -49.4743 | 2025-06-28 01:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 33b959c6-b3aa-3c5d-a352-7919ac8b92c3 | -9.1205 | -49.4958 | 2025-06-28 01:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 36489978-23c7-33b8-8500-89de359f84f2 | -11.0644 | -55.3757 | 2025-06-28 01:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 80a16e73-3f18-3f59-a0ae-ccaa2fb1c07d | -11.0455 | -55.3773 | 2025-06-28 01:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 289.3 |
| 120c9b75-4de3-3fe4-93b0-2140466f8f09 | -6.9108 | -43.9834 | 2025-06-28 01:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 2687395d-8203-36a2-bf20-a379681a1705 | -7.2219 | -43.0682 | 2025-06-28 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 116.0 |
| 11979bc7-cf47-301a-aecc-66208d7e69dc | -12.2523 | -46.7766 | 2025-06-28 01:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 36b7523c-f6d8-360b-84d8-e299919d574c | -6.892 | -43.9851 | 2025-06-28 01:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 9df55026-ac12-3859-b13f-5c32b25ab17a | -11.0453 | -55.3976 | 2025-06-28 01:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 4a85155e-2444-3d64-8379-95afb318ad4a | -7.2217 | -43.0917 | 2025-06-28 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 116.6 |


[Clique aqui para ver as próximas entradas](README7.md)
