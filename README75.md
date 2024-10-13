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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df97cdbb-176c-3b20-8a6b-752881941b67 | -4.5299 | -46.55743 | 2024-10-13 05:01:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 28f40844-be93-3cbb-80a2-1855d2f9c937 | -4.14672 | -46.69278 | 2024-10-13 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d9a426f-a902-3e95-9239-3e708b62dbb7 | -3.9433 | -46.44012 | 2024-10-13 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bdfe2dc-2acb-3a05-bd30-c2ec166de59a | -3.94304 | -46.43989 | 2024-10-13 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 261e8cc0-8aab-340a-8854-1b7f8117dc1e | -3.93855 | -46.43621 | 2024-10-13 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3c948a0-02fe-37b6-921e-620cf976813e | -3.93831 | -46.436 | 2024-10-13 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e3a6a50-c691-3b37-a2ad-92449f646563 | -3.9381 | -46.43933 | 2024-10-13 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0e1c0cf-d9d9-3165-9ac0-80cf2e942d50 | -3.93784 | -46.43911 | 2024-10-13 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 709c8f61-a1a4-3b00-9f31-ae6f2c8a2de1 | -3.93765 | -46.44247 | 2024-10-13 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54c49a46-2c25-3153-99f9-40c25af11dd4 | -3.93737 | -46.44223 | 2024-10-13 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d74c1c51-1a88-3068-bcee-0b9bda417a30 | -3.93426 | -46.42907 | 2024-10-13 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3d2591b2-8685-3e02-90ad-f7991af1cb11 | -3.93408 | -46.42887 | 2024-10-13 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c39ed509-6d46-3100-8523-800e6480636d | -3.93381 | -46.43222 | 2024-10-13 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fe7fd5c8-ecf5-35b4-8677-eef9957d6bcf | -3.9336 | -46.43201 | 2024-10-13 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ffb6d52c-c855-3bda-a99d-0bf2ba938f84 | -3.93337 | -46.43536 | 2024-10-13 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2312b93e-0639-323f-90a7-0397d2bfcd2f | -3.93313 | -46.43515 | 2024-10-13 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0434d07c-5278-3917-98c2-4d880bc4e41f | -3.92843 | -46.43106 | 2024-10-13 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 669a2ec2-1228-3b2c-b966-fa13acbea9de | -5.07031 | -46.84874 | 2024-10-13 05:01:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6438671-4515-3c4a-932e-5e359a91be38 | -5.06989 | -46.85171 | 2024-10-13 05:01:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 074bdb07-2f82-3045-9590-a000b32eca04 | -4.97993 | -46.80444 | 2024-10-13 05:01:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31d52b5d-9b7f-363e-97bb-3ceb2189eabc | -4.97951 | -46.80737 | 2024-10-13 05:01:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5eac9648-944f-3ef3-9c02-5b1cc017e2bc | -4.97479 | -46.80363 | 2024-10-13 05:01:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 207f7509-f3ff-3c5c-b6c2-e7a4c1a03b56 | -6.24118 | -47.38899 | 2024-10-13 05:01:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c4793cee-52e7-3267-9ba1-58e03116a787 | -6.24031 | -47.39496 | 2024-10-13 05:01:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a7607460-f168-38ca-825f-69bb0a522228 | -6.23942 | -47.39561 | 2024-10-13 05:01:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f831094b-b8c7-3aba-9699-af3b312b5ab0 | -6.13582 | -47.27388 | 2024-10-13 05:01:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2e44d42-a642-386b-bcee-dfec22c27b2d | -6.1354 | -47.27682 | 2024-10-13 05:01:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a20fada8-4688-383a-83d3-1070176a69e6 | -6.13075 | -47.27311 | 2024-10-13 05:01:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d8654486-d009-370e-8b18-be3fa9f23540 | -6.13033 | -47.27603 | 2024-10-13 05:01:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 46e684cf-a2ca-36be-bda1-6f0f3d7692fb | -6.73988 | -48.17677 | 2024-10-13 05:01:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a38531e-bea8-3f4e-829a-c50addb5cce5 | -2.09509 | -48.52848 | 2024-10-13 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43886eae-ef01-361a-8dab-95e7b144b9a6 | -2.09443 | -48.53269 | 2024-10-13 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a5801d9-2c82-37d5-ab9a-d1f60b95c053 | -1.05413 | -47.92023 | 2024-10-13 05:01:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 17d18651-f458-3b25-b809-048cfb42e777 | -1.05345 | -47.92468 | 2024-10-13 05:01:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 0345ab1e-273d-3c7a-9299-aebc2be56ea0 | -1.05278 | -47.9291 | 2024-10-13 05:01:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5ee68356-5c10-3e3e-9f56-649dd662f380 | -1.04898 | -47.92393 | 2024-10-13 05:01:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 66d92030-fb93-3430-88eb-b4b7939e2233 | -1.04831 | -47.92833 | 2024-10-13 05:01:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5558aae9-e006-3025-af90-db45add43824 | -2.83226 | -48.45347 | 2024-10-13 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef1ca382-6e51-3942-be4f-8570620927e8 | -2.79039 | -48.69957 | 2024-10-13 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e5d85cc-ad26-3a77-a386-9ab1edbf286a | -2.78603 | -48.69889 | 2024-10-13 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff580246-d607-315d-8e63-3dc0458bb8b2 | -2.7854 | -48.70306 | 2024-10-13 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b323d3d3-b918-338d-b61b-dfb9bcbd6267 | -2.75172 | -48.68943 | 2024-10-13 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d434ca0-0341-3b9e-9bcc-fb86225058e2 | -2.7511 | -48.6936 | 2024-10-13 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d96005e-48c7-3008-beb0-8692d34cc866 | -2.75078 | -48.40322 | 2024-10-13 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fab2dd72-3c7b-3ccf-9302-be15f151497a | -2.7501 | -48.40762 | 2024-10-13 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6aea6d60-eb20-3d2b-8a0a-6cce2ab0bf82 | -2.72732 | -48.73012 | 2024-10-13 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96c4307d-0319-3560-9703-f4ba1da1baab | -2.57711 | -48.04296 | 2024-10-13 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 391fd662-af3e-3b4a-a3ab-f79f87163652 | -2.54869 | -48.4076 | 2024-10-13 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e93c1944-239c-3b57-ba45-1f0f53e4a3cb | -2.47356 | -48.19619 | 2024-10-13 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f675beef-38bd-385d-ad97-c2ac06f7a7a7 | -2.43013 | -48.2397 | 2024-10-13 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 577a731d-4f15-3b72-a16e-fd3a30a8a6be | -2.17239 | -48.8067 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a08ad3cf-6bf7-3b28-ba0c-86e13d3f01ab | -2.17095 | -48.35125 | 2024-10-13 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4879b1aa-7697-3083-9f43-e009cb2e207d | -2.16747 | -48.81009 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bf4db4f1-b20d-37d7-b168-e345e1f85d88 | -2.16684 | -48.81412 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 44d39bbb-ac21-326a-89f4-4d126dda5230 | -2.16318 | -48.80943 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 03e26398-e1b3-3acd-bd9b-3853a2565dff | -2.16255 | -48.81347 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aeee40cd-f0d1-3445-8737-8b7eed8e3024 | -3.22266 | -48.92005 | 2024-10-13 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0be9d949-bfdb-3544-8e4f-60a6b6d4d919 | -3.22204 | -48.92413 | 2024-10-13 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5af61813-c970-3252-ad04-e409b405c548 | -3.21834 | -48.9194 | 2024-10-13 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 56cfd1e9-3823-3742-821a-77d2b7b686fd | -3.21771 | -48.92347 | 2024-10-13 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eb9b2ff3-24d7-3c8d-bd61-7fd9758bb904 | -3.16348 | -48.36768 | 2024-10-13 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1df9d316-d251-3e2d-9922-6ec849b9b80d | -3.15966 | -48.3625 | 2024-10-13 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0e299d76-fe70-3b39-bb1c-e191bc0ba647 | -3.15898 | -48.36702 | 2024-10-13 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 76b99d07-a635-3d08-9bec-d72300d709fc | -3.13453 | -48.97731 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7313db6-c59e-3cbf-bcd4-1ad6db9f2ad0 | -3.13279 | -48.97872 | 2024-10-13 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be49924b-5de3-3344-9a9f-7c0ab1e88819 | -3.12723 | -48.60788 | 2024-10-13 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0714e4e7-e309-30ea-bde6-fbdb2d2c7377 | -3.08708 | -47.77847 | 2024-10-13 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ea1acdf-187d-3edf-b579-65afda3e4cd1 | -3.08637 | -47.78331 | 2024-10-13 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5412b17e-a3b8-3d44-a46a-70b5d8ad9441 | -3.08483 | -47.78139 | 2024-10-13 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c263f058-0eed-305d-b0a2-4527ae265aa6 | -4.78609 | -48.08421 | 2024-10-13 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4f59337-6e11-3895-8ba8-a0af882a965d | -4.48525 | -48.10939 | 2024-10-13 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6c4d5da-a259-3878-93fc-48875649d5f7 | -4.41067 | -48.70794 | 2024-10-13 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 351249b7-d1cd-3bbe-9ff4-551a7dabfe3c | -4.38511 | -47.76459 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 531293b3-7bbb-343d-99bc-c5dfaed647b8 | -4.38495 | -47.76196 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99598308-2aa5-3cc7-807b-5939ecab30bd | -4.31889 | -48.63254 | 2024-10-13 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a130f58-1211-3138-8267-badf3b5182e2 | -4.31375 | -48.63626 | 2024-10-13 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5821f6ae-cb7b-34d6-bc45-3494b15e0194 | -4.31309 | -48.64066 | 2024-10-13 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90352600-8aba-3d68-a6a0-59e353cd16c9 | -4.28747 | -48.6278 | 2024-10-13 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3b2a43f-8c38-3164-9f44-39cb334c7485 | -4.28682 | -48.6322 | 2024-10-13 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfce72d2-dc82-3b94-9b36-a44a9a8f2b6d | -4.28127 | -48.23095 | 2024-10-13 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 41fe35ce-d688-3fc3-ba02-8734e644c3dd | -4.27667 | -48.23019 | 2024-10-13 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6a4b06b-ed6e-35dd-9203-ac935b388260 | -4.27597 | -48.23486 | 2024-10-13 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98756f95-aebc-3242-9345-18f32977418a | -4.27275 | -48.2248 | 2024-10-13 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 013ff54f-a3d7-3b93-97bc-f48574a6c45d | -4.26815 | -48.22406 | 2024-10-13 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efc896c7-4044-3150-903c-0ced3226e3cd | -4.1245 | -48.27711 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dcd01af4-aec0-3ce1-ad6e-84d301538bdf | -4.1208 | -48.2383 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0ebb5c8f-2227-3f0f-805b-8551616dfb3a | -4.12061 | -48.27164 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d1e0b7c1-ba2a-3492-b343-362cfdc7db24 | -4.12008 | -48.24322 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4af560e3-d14b-34b9-8d68-c5d7ab80a9dc | -4.11993 | -48.27629 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fabbdae8-cc77-3e87-895e-edddd361acef | -4.11692 | -48.23269 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5287907b-8291-3998-9c30-275d95edc50a | -4.11619 | -48.23769 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8f502e2a-9332-35ba-8a0a-6df96f9fa0a7 | -4.11548 | -48.24257 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f97581c6-63e7-378f-809b-87e555445a79 | -4.11535 | -48.27557 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9eba3786-ac78-3310-8390-c18aca856e94 | -4.11478 | -48.24736 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| afcf23b4-7400-3399-9f77-2e7b1c882731 | -4.11467 | -48.28017 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1e52e15f-b809-3be2-a7b4-d818774d6f1b | -4.1141 | -48.25204 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 909492df-9391-3abf-85e5-51211fdc72b2 | -4.11158 | -48.23708 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 59c749d5-a26c-33e5-8143-5c7fb4622759 | -4.11088 | -48.24189 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5e2bb496-b0df-3b62-9d0c-b8b8f6c54fa6 | -4.11018 | -48.24666 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 163fc7d1-07b5-3847-aa77-02a6e3c5b598 | -4.11009 | -48.27944 | 2024-10-13 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README76.md)
