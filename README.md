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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d43787e-e2a3-33fe-b86f-4d93a9a2f832 | -8.0883 | -43.1667 | 2025-07-25 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.4 |
| 6f766390-edf8-3ac0-8af2-1005f53b56db | -8.0693 | -43.1687 | 2025-07-25 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| cb663877-f424-33a3-b9b4-5b01b224cfe3 | -11.9518 | -58.7574 | 2025-07-25 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 148.1 |
| c883eb52-c19b-349b-9c8f-0a9fb6ef07c3 | -7.2597 | -43.0645 | 2025-07-25 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 199.9 |
| fa72afe3-e2f5-3abc-9bf5-78c6cf8d42b5 | -7.8894 | -45.539 | 2025-07-25 00:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 754beb62-fa4b-39f0-877d-5bb0e9c6a147 | -7.2408 | -43.0664 | 2025-07-25 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| ab004299-d5cf-385d-b0d3-6eb3d4e97921 | -8.0696 | -43.1452 | 2025-07-25 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.6 |
| 398ee8bd-4146-3fe5-841a-00084e758c51 | -8.0886 | -43.1431 | 2025-07-25 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 114.7 |
| 41011405-385a-39f7-a20e-5887025d8ccc | -11.4584 | -45.1126 | 2025-07-25 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 215.9 |
| ee35030b-5b4d-3e6b-869e-2d244b0d12cc | -7.2594 | -43.0881 | 2025-07-25 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 7e4b3c1e-663f-3673-9284-d0d18ee66588 | -2.9108 | -48.254 | 2025-07-25 00:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 52fd61e4-7030-35e2-89dc-8d6893bb98e9 | -8.8494 | -45.5995 | 2025-07-25 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.7 |
| dab3e3e7-06eb-3703-a7a2-21e5c3e45488 | -11.458 | -45.1357 | 2025-07-25 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 1a41badb-f26d-37c5-8be4-fb9489898f61 | -11.4393 | -45.1154 | 2025-07-25 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 04ce3deb-aec2-3d06-abf6-d42134f73730 | -13.7169 | -45.6833 | 2025-07-25 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| af54bb0f-aa3e-3b13-820e-8c92d420ae0b | -7.2785 | -43.0627 | 2025-07-25 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.9 |
| 1db74539-2688-350c-a4a2-0be441e5f73c | -9.4054 | -63.5068 | 2025-07-25 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 22f9192c-d6ba-3a93-8307-7580c8cf8197 | -7.8591 | -48.2255 | 2025-07-25 00:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 1a615c82-1cba-3215-b3a8-3c745c414aa7 | -11.4776 | -45.1099 | 2025-07-25 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 4d401941-0c9a-3d9e-a312-99c23506cc22 | -11.9516 | -58.7771 | 2025-07-25 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 82adb8ea-2d32-3961-88cb-256eeb702408 | -11.9329 | -58.7588 | 2025-07-25 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 1a8fd683-455f-3758-afe4-2db3d6f11db3 | -23.2693 | -52.1353 | 2025-07-25 00:10:00 | GOES-19 | PRESIDENTE CASTELO BRANCO | PARANÁ | Brasil | 4120408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 68.9 |
| bef1541f-c964-3305-a7c0-3143233d5e81 | -10.6438 | -44.7645 | 2025-07-25 00:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 51297854-db28-3b22-ae24-20b6759ee48c | -7.2408 | -43.0664 | 2025-07-25 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| d678703f-7297-3129-ba27-eee9900f3620 | -23.2687 | -52.158 | 2025-07-25 00:10:00 | GOES-19 | PRESIDENTE CASTELO BRANCO | PARANÁ | Brasil | 4120408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 88.6 |
| 313aee99-506c-39b9-bba2-7f91c57b7b42 | -8.0693 | -43.1687 | 2025-07-25 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| 08a7eb14-6912-39b6-8c04-4d34ca82c26b | -11.9329 | -58.7588 | 2025-07-25 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| a4f28eab-5ff1-3866-a8e1-c7b2db731dfb | -8.0883 | -43.1667 | 2025-07-25 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.1 |
| 94701bb2-fd77-3ffb-86ec-a0564f5c5b97 | -11.9516 | -58.7771 | 2025-07-25 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| b60ef927-c23f-3136-8db7-2a4882267631 | -7.8894 | -45.539 | 2025-07-25 00:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 262e38f8-bccd-3e42-a475-14c12d72b70a | -13.7169 | -45.6833 | 2025-07-25 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 02f5f34f-c022-3ddd-a396-5ff17fa4031e | -14.9518 | -46.9845 | 2025-07-25 00:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 8d737e25-d799-39c8-8045-5ff5db42c893 | -8.0886 | -43.1431 | 2025-07-25 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 126.9 |
| c860e9ce-ffaa-3541-b4a4-74f39fa75763 | -6.9422 | -44.5562 | 2025-07-25 00:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 862eb7f0-a16b-3e60-8312-8e2400637150 | -10.416 | -47.1955 | 2025-07-25 00:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 9983e4e9-e22a-3fa6-b472-9b16ced05069 | -6.9607 | -44.5775 | 2025-07-25 00:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 9062922f-2287-3ee5-9498-786031b14466 | -11.4584 | -45.1126 | 2025-07-25 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 46a56866-f7be-32c2-9376-1a1f5026cf6a | -11.9518 | -58.7574 | 2025-07-25 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 188.3 |
| bae67c4b-f78e-3a3d-911e-7565ce49e2ca | -2.9108 | -48.254 | 2025-07-25 00:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| b28aae53-bb66-39d3-9f09-4fda244405f7 | -6.961 | -44.5546 | 2025-07-25 00:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 8f07f424-a348-3ab0-89d9-6a3b834722c2 | -7.2597 | -43.0645 | 2025-07-25 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 258.4 |
| f76af3ce-0c99-3ce8-bd01-d83020537412 | -7.2594 | -43.0881 | 2025-07-25 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| c1e87a6a-a8ed-3d9e-a63d-f9f31c568d44 | -8.0696 | -43.1452 | 2025-07-25 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 123.8 |
| c6b54266-6696-37bb-b729-cc900d9ae4a4 | -10.435 | -47.1932 | 2025-07-25 00:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 2505bb56-d669-3e5a-b3dd-a3897f4f5792 | -11.458 | -45.1357 | 2025-07-25 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 0f49c52d-5526-39e9-b80d-da8e4f060e02 | -10.6438 | -44.7645 | 2025-07-25 00:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 80a2a9b5-a350-3239-984d-2394f796c6e2 | -8.0883 | -43.1667 | 2025-07-25 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 136.4 |
| 88888e8c-39b9-329c-aa9e-134f2584149d | -8.0696 | -43.1452 | 2025-07-25 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.5 |
| ebdef00d-2032-3a48-a04c-2d4c41d3582d | -7.2599 | -43.041 | 2025-07-25 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 333fc677-480b-3f58-b8e8-feaae6034672 | -7.2597 | -43.0645 | 2025-07-25 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 210.2 |
| cf5979d5-ec7b-3d05-b9d8-3bff15c7ca4b | -11.458 | -45.1357 | 2025-07-25 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.7 |
| d77eddf6-9c6d-32ec-8fcf-a284d41281c0 | -8.0693 | -43.1687 | 2025-07-25 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |
| af381a8d-24d5-3227-aa20-607f5949efc1 | -6.9422 | -44.5562 | 2025-07-25 00:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 45426ac6-0d1e-3a07-84fe-9ec74dd22b1d | -6.9607 | -44.5775 | 2025-07-25 00:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| e37eb9f1-1668-34d5-886e-5f26bd6abddf | -8.0886 | -43.1431 | 2025-07-25 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 205.4 |
| 51c9e2a9-652f-3d53-9731-d877406038a5 | -11.9518 | -58.7574 | 2025-07-25 00:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 148.7 |
| b601c0ea-c09f-3306-bee0-92d5306db8b2 | -16.8201 | -47.6013 | 2025-07-25 00:20:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 42.7 |
| e66edb96-c32e-3a04-9459-225d8f865906 | -7.8894 | -45.539 | 2025-07-25 00:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| b7a75d89-577f-37a2-981d-7bd72cd6eb8b | -11.9329 | -58.7588 | 2025-07-25 00:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 6290c07a-6ad1-383f-88da-f56c4bdcb84d | -13.7169 | -45.6833 | 2025-07-25 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| ae2f200c-c02b-3862-82dc-7bad2f860551 | -2.9108 | -48.254 | 2025-07-25 00:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 75374ac4-6ae9-35c8-9452-541d39648412 | -13.7174 | -45.6601 | 2025-07-25 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 94214ecb-0262-3bc2-a92e-6248f337b253 | -7.2594 | -43.0881 | 2025-07-25 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| 68f4f840-1f44-3247-8555-17ddfef4f3d6 | -11.9516 | -58.7771 | 2025-07-25 00:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| b6131f05-bc01-341a-8194-2df9b80a8c73 | -6.961 | -44.5546 | 2025-07-25 00:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| c186bed6-206a-347a-b28a-a2a01e31eade | -11.4584 | -45.1126 | 2025-07-25 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 64398199-b479-3037-bc00-6b1f5dcfecc6 | -8.0693 | -43.1687 | 2025-07-25 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| 259701a0-26d6-3563-a5a0-99f6483d64cb | -10.6438 | -44.7645 | 2025-07-25 00:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| bd177f40-75cd-39c0-a0d4-84e4945f5746 | -11.9518 | -58.7574 | 2025-07-25 00:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 149.0 |
| ae4c7f5c-416e-39f1-8ebf-cf94dbc54f98 | -8.0696 | -43.1452 | 2025-07-25 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| f064fb23-9d0f-30c9-8add-dd4e470b6305 | -2.9108 | -48.254 | 2025-07-25 00:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 5653736a-be35-3517-98f1-31bf548a9ef4 | -8.0883 | -43.1667 | 2025-07-25 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 147.3 |
| 2eba6367-9139-30f5-8aa0-e646b07beaa5 | -7.2594 | -43.0881 | 2025-07-25 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| dd75b9bc-cdb3-3f75-ab1d-4a0634911379 | -8.0886 | -43.1431 | 2025-07-25 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 192.9 |
| 89517e60-f7a7-3c96-ab54-9461bbdd09c1 | -11.4776 | -45.1099 | 2025-07-25 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 23acbe3c-678c-37e0-b3ed-400a0f7051d8 | -13.7169 | -45.6833 | 2025-07-25 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| f133f06f-5db8-34af-b8aa-48ed254f1f8f | -11.4584 | -45.1126 | 2025-07-25 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 59d32c99-8cfa-3ef7-9e42-a4339ef4f945 | -11.458 | -45.1357 | 2025-07-25 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 5e2e3127-291b-3074-9e73-4d2046e79b5e | -6.9422 | -44.5562 | 2025-07-25 00:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 5da3ca6b-539c-3ba4-b446-284573c2f26a | -6.9607 | -44.5775 | 2025-07-25 00:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| e7adc59d-8021-3192-9458-34d9c151701a | -11.9329 | -58.7588 | 2025-07-25 00:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| e784cec0-bc59-3967-979d-ed06020c02fc | -7.8894 | -45.539 | 2025-07-25 00:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 6f2b3f5b-9abf-3890-97d7-1264a586c778 | -6.961 | -44.5546 | 2025-07-25 00:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 180e801f-2e30-3121-b92c-d12c3e7a258c | -7.2597 | -43.0645 | 2025-07-25 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 178.8 |
| 20c67419-d51e-3aa1-acc9-4b620c5df452 | -11.9516 | -58.7771 | 2025-07-25 00:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| cc721dab-c03e-371b-bcaf-a66f63f94e70 | -10.6247 | -44.767 | 2025-07-25 00:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| f79df7a4-498f-3f16-b603-6a103b93ee57 | -14.9518 | -46.9845 | 2025-07-25 00:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| a19d77f2-bb74-3737-814c-ce1bc95793b7 | -14.9518 | -46.9845 | 2025-07-25 00:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 4f915e03-dcde-3b0d-a7de-e82c0d7d4f9e | -11.9518 | -58.7574 | 2025-07-25 00:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 188.6 |
| 027d97e0-e4d6-3f7a-8b4b-5fd59ed0a935 | -10.6438 | -44.7645 | 2025-07-25 00:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 73e01f7b-5e86-3a0f-a820-683d63b213fc | -7.9259 | -44.0706 | 2025-07-25 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 1fdd7c4c-ca22-3a75-ac99-b832e8ae76df | -7.907 | -44.0725 | 2025-07-25 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 45f27aa8-e1c4-3402-80b4-d949eb693cd5 | -11.9329 | -58.7588 | 2025-07-25 00:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 99d4a799-a871-3eb8-8e30-112d9b8d04b5 | -7.9256 | -44.0937 | 2025-07-25 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 0473ebbd-822e-32cc-b0cb-6a3b86f9fd5e | -7.9068 | -44.0957 | 2025-07-25 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 38.0 |
| f214533b-fe48-3d99-92e7-9f05ca296bb6 | -8.0883 | -43.1667 | 2025-07-25 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 144.7 |
| c0c795c8-b518-3511-8f9b-140252fb854b | -11.4776 | -45.1099 | 2025-07-25 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.2 |
| daf08e40-232d-3167-b525-b5c1c4d5b905 | -11.458 | -45.1357 | 2025-07-25 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 71687b2f-e554-32f5-b2fc-aaeadacb1656 | -8.0696 | -43.1452 | 2025-07-25 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.8 |
| 115ff593-3700-3429-aefa-87a9cb6baa34 | -11.9516 | -58.7771 | 2025-07-25 00:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |


[Clique aqui para ver as próximas entradas](README2.md)
