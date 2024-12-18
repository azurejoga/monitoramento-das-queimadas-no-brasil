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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7553135-8707-3645-950c-bd212b6cf0d3 | -9.3069 | -40.2365 | 2024-12-18 02:30:00 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 85.8 |
| 4c956801-a1d4-3c59-9387-689a8cc84596 | -5.9371 | -48.0437 | 2024-12-18 02:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 35451c30-b0d4-3832-80f7-56204c3b6700 | -3.2503 | -46.8709 | 2024-12-18 02:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 3c0aa942-7516-3ded-8d75-0b17c9191a40 | -4.9645 | -43.695 | 2024-12-18 02:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| aed77068-a4d8-3047-be95-c42d2bb2f928 | -4.9641 | -43.7413 | 2024-12-18 02:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 59cdbd45-7e49-33f9-bcdd-f05afb169b61 | -6.9908 | -43.5349 | 2024-12-18 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 3fbe304e-dcfb-3043-8495-af4c043eeaef | -3.035 | -45.2321 | 2024-12-18 02:40:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 5ca20f79-2b34-34de-840e-9fbc3b16b61a | -6.9718 | -43.56 | 2024-12-18 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| b790d38f-2baa-31da-adc6-fbb5c76b7b7d | -3.0164 | -45.2328 | 2024-12-18 02:40:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 68.9 |
| b1bb11d9-6f24-33ce-b1b4-8f9e8060f272 | -6.9906 | -43.5582 | 2024-12-18 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 101.2 |
| ed0b9153-fa00-3d83-ab9f-44c2c8913a0d | -6.9715 | -43.5833 | 2024-12-18 02:40:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 55.9 |
| c967b6cd-750a-322c-8c10-a7301d7645af | -6.9903 | -43.5815 | 2024-12-18 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 53.1 |
| dd9a92bf-ca87-3e42-9deb-736e8a4c8693 | -3.2503 | -46.8709 | 2024-12-18 02:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| ed287eee-f8ba-351b-8e55-cb100e55d8a4 | -11.8648 | -43.8172 | 2024-12-18 02:40:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| e7e27185-2ed8-3cdf-a615-f99073a42161 | -6.33841 | -35.12587 | 2024-12-18 02:47:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 9a8ce6b3-dd61-3280-9f47-57d17ae9a7bb | -7.71754 | -35.09745 | 2024-12-18 02:47:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 5e5321b9-ea2c-323c-be8d-b4df14efb40d | -10.04538 | -36.13575 | 2024-12-18 02:47:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| b1b39e3e-fe70-307f-bd6c-86215e6e52d4 | -6.74608 | -34.97338 | 2024-12-18 02:47:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 34f50acc-5f10-3cb6-a7b5-766e91324d45 | -9.70258 | -36.17679 | 2024-12-18 02:47:00 | NPP-375D | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 0e374bb5-e322-3d73-a96d-51e17f1234e0 | -7.71495 | -35.09469 | 2024-12-18 02:47:00 | NPP-375D | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f7cfc40d-18c2-3e00-a30d-b90fc2e32a06 | -10.05263 | -36.13708 | 2024-12-18 02:47:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 6a9724e5-1ee9-33d5-802b-0b2337132cb0 | -7.71187 | -35.08894 | 2024-12-18 02:47:00 | NPP-375D | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a77c1e64-d6cd-3253-8de0-93eb7f45f4a6 | -7.71898 | -35.09014 | 2024-12-18 02:47:00 | NPP-375D | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| b4714dcd-312b-3138-a8f4-05a9fd6a904a | -10.04432 | -36.13779 | 2024-12-18 02:47:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| c0918d20-10ff-35ec-99de-26463cb2edba | -6.33905 | -35.12932 | 2024-12-18 02:47:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| d1019868-8630-30a6-8bca-bdae183bf7c4 | -7.08258 | -35.03461 | 2024-12-18 02:47:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6cadbecc-ef4b-38e8-90df-e1bc9dde4d4f | -9.70414 | -36.16936 | 2024-12-18 02:47:00 | NPP-375D | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 66b97283-3195-3c5e-ac58-e71fcbf8ddb6 | -6.34044 | -35.12202 | 2024-12-18 02:47:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 6340780e-b645-30db-907a-51823fd1dc5f | -7.08391 | -35.02754 | 2024-12-18 02:47:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6c5453b0-d2ad-331a-9990-b92bff8f9771 | -7.07553 | -35.03284 | 2024-12-18 02:47:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 1e1622fa-5dde-3ec8-9bea-bd538efdac71 | -10.05155 | -36.13927 | 2024-12-18 02:47:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| cb9e00af-96a3-3ac2-b45e-a39fe0447f69 | -9.70353 | -36.16965 | 2024-12-18 02:47:00 | NPP-375D | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e3abcd3f-5302-32f2-b460-4f152cd2eb6a | -7.71635 | -35.08732 | 2024-12-18 02:47:00 | NPP-375D | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c3a921cf-2b91-3a2e-9254-06b7838c324c | -7.0768 | -35.02608 | 2024-12-18 02:47:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c441d042-62f3-3f69-b946-fde85fdd3b83 | -7.07809 | -35.03191 | 2024-12-18 02:47:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 73ebcff5-31d8-316b-949f-2f5053e4d7f6 | -7.08524 | -35.03312 | 2024-12-18 02:47:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| ff616ef9-f77f-3afb-bf8b-88a9658811e2 | -6.33976 | -35.11858 | 2024-12-18 02:47:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| edf51d74-bd9a-302f-90af-9241029dd41e | -5.9369 | -48.0654 | 2024-12-18 02:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 368406d1-7af5-3a18-a073-5317a44fc287 | -5.9557 | -48.0425 | 2024-12-18 02:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 15a06957-4453-3b1b-9d38-b78b54ac15f2 | -6.9718 | -43.56 | 2024-12-18 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 187.0 |
| 0fac79b3-4107-327e-837e-607c29bda23b | -5.9556 | -48.0642 | 2024-12-18 02:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 587d74a9-3498-345d-b87b-4a7823e283c8 | -6.9903 | -43.5815 | 2024-12-18 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 114.1 |
| ece8f21b-3912-3728-ba73-a7640b08d611 | -6.9715 | -43.5833 | 2024-12-18 02:50:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 102.7 |
| b3e19b4a-9444-35e1-9c66-d6386fd5fa4c | -3.0164 | -45.2328 | 2024-12-18 02:50:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 54ddbfda-8ae1-3ea9-964d-0a86e7cbb69f | -5.9371 | -48.0437 | 2024-12-18 02:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| a1d75700-364b-3957-884e-144361523707 | -3.2503 | -46.8709 | 2024-12-18 02:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| efab8c1b-4080-3071-b663-984456d15543 | -6.9906 | -43.5582 | 2024-12-18 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 202.5 |
| cff56ba2-3561-3c78-994c-5e7bcd6adc5d | -11.8643 | -43.8408 | 2024-12-18 03:00:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 10ebca64-870e-3b2e-a2cf-7215ee72d933 | -5.9369 | -48.0654 | 2024-12-18 03:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 0168a60a-9a74-330f-80b9-03c25050839f | -5.9556 | -48.0642 | 2024-12-18 03:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| ff5ba669-952e-3145-ac98-199c90915550 | -11.8455 | -43.8202 | 2024-12-18 03:00:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 3ac87625-007d-3a1b-ab51-a98a42a40b75 | -6.9906 | -43.5582 | 2024-12-18 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 142.6 |
| a67443cb-a1c2-3006-a016-dcdd303239b9 | -3.2503 | -46.8709 | 2024-12-18 03:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 0f4b7771-f135-3f94-9c5a-5f55af90211c | -6.9903 | -43.5815 | 2024-12-18 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 32dc211a-ca22-3854-8607-42bb3aed19a6 | -5.9557 | -48.0425 | 2024-12-18 03:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 880c7f65-39b5-3cde-b96b-58a42cfba0b6 | -6.9718 | -43.56 | 2024-12-18 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 105.4 |
| cf4d6d6d-926c-320f-ae2a-dc271eee0b93 | -5.9371 | -48.0437 | 2024-12-18 03:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 40789859-5a75-395a-9768-a9ada314779f | -6.9715 | -43.5833 | 2024-12-18 03:00:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 0a845d16-9a61-3126-8c7d-1af76bf1b481 | -11.8648 | -43.8172 | 2024-12-18 03:00:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 113.3 |
| dbbd360b-a521-31d6-9013-c9e69e320987 | -6.95 | -43.57 | 2024-12-18 03:00:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 10a52435-3d7e-3a15-871a-e4bdf8776821 | -8.84339 | -35.69971 | 2024-12-18 03:08:00 | NOAA-20 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bc38b5a1-837f-3f5e-8bf8-10b5cf972226 | -6.75896 | -35.31611 | 2024-12-18 03:08:00 | NOAA-20 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0e49c435-550d-32f0-9e8f-e6f9cf90c074 | -4.44627 | -38.06683 | 2024-12-18 03:08:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0c38a014-0c8f-3627-94fb-0bc274894a40 | -4.44631 | -38.06283 | 2024-12-18 03:08:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 4a900a09-f3d1-3145-9d86-c8d9408e0bb7 | -4.44707 | -38.06211 | 2024-12-18 03:08:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 587a3c1e-2d6d-3b55-983e-5d3c3609c5e9 | -4.44548 | -38.06754 | 2024-12-18 03:08:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5b78350e-0e44-31da-8c0e-353f3043f9bb | -7.08207 | -35.0275 | 2024-12-18 03:08:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 7ae25259-6a55-3f3a-b2e4-b230bb01cff3 | -7.25296 | -40.1693 | 2024-12-18 03:08:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9cfb5ea2-2886-3b21-bde3-5b13f55bf249 | -5.95468 | -39.67784 | 2024-12-18 03:08:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7d884e12-ddc1-3432-96d4-1930aa3887e4 | -7.24628 | -40.168 | 2024-12-18 03:08:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a0a01787-6fd9-30f1-ae08-cfa61c8e9e33 | -5.95362 | -39.68372 | 2024-12-18 03:08:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 72c00dbd-2b66-3a58-98de-5fd19ad32179 | -8.8483 | -35.70057 | 2024-12-18 03:08:00 | NOAA-20 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bcd6d35e-5977-3d37-99a3-b3aa8282f8a1 | -7.69094 | -35.2572 | 2024-12-18 03:08:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 8a6ec8d6-4c9e-36c0-af99-e518c40fdea2 | -3.06985 | -40.05946 | 2024-12-18 03:08:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6b7ed389-040d-3dd8-8667-c8ed0a5121ac | -5.95182 | -39.67787 | 2024-12-18 03:08:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d97e0bd9-9bd3-3467-b4c7-360802b4e6da | -8.84488 | -35.70126 | 2024-12-18 03:08:00 | NOAA-20 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ea704038-16ff-342e-8dd2-fb7b22d6219a | -8.47701 | -36.31261 | 2024-12-18 03:08:00 | NOAA-20 | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 22fff4f1-171b-33b9-9fc0-3ea4fcd10018 | -7.90164 | -35.23254 | 2024-12-18 03:08:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 25b1e65a-ea02-3506-938b-c2a0011e72bd | -7.25497 | -34.82389 | 2024-12-18 03:08:00 | NOAA-20 | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2d44b48a-3ac4-3e63-b477-d0fe50b3aaba | -8.84243 | -35.70518 | 2024-12-18 03:08:00 | NOAA-20 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 008926fc-b4fb-3090-869e-97ce817edbd2 | -8.11183 | -35.07282 | 2024-12-18 03:08:00 | NOAA-20 | MORENO | PERNAMBUCO | Brasil | 2609402 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| a306e911-7123-35ba-a224-5cc5dc03fd75 | -5.95072 | -39.68375 | 2024-12-18 03:08:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d09ed2ef-85e8-3f71-831c-cb84a4b81900 | -8.84733 | -35.7061 | 2024-12-18 03:08:00 | NOAA-20 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d35e9b8b-f8c9-3409-b02f-94e7a874529b | -7.25411 | -34.82893 | 2024-12-18 03:08:00 | NOAA-20 | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bf99e11e-c703-34db-b5bf-9abc66fba5fa | -7.90072 | -35.23775 | 2024-12-18 03:08:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 7954641c-49c3-39f9-985f-34cc063b67b9 | -8.47756 | -36.30952 | 2024-12-18 03:08:00 | NOAA-20 | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d8e939e4-9f0f-3ad2-bf2a-03ac70a6bc66 | -6.666 | -38.59176 | 2024-12-18 03:08:00 | NOAA-20 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 67c245de-b220-3bc9-b6be-4fa0b78e3904 | -7.69001 | -35.2625 | 2024-12-18 03:08:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| f8e1ff98-8ae8-37e0-bafd-b73b40e65064 | -6.66685 | -38.58701 | 2024-12-18 03:08:00 | NOAA-20 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2543a249-6922-3685-8309-c10244cdf3a3 | -8.84389 | -35.70672 | 2024-12-18 03:08:00 | NOAA-20 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a6493c1c-ca8c-3ef9-8f54-c531abeb78c4 | -9.33484 | -36.0074 | 2024-12-18 03:08:00 | NOAA-20 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 816db2cf-4b6c-3124-9956-1f259652f246 | -8.39097 | -36.24819 | 2024-12-18 03:08:00 | NOAA-20 | TACAIMBÓ | PERNAMBUCO | Brasil | 2614709 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b77a9179-1574-3b95-8364-d17a1f31c969 | -6.75353 | -40.13345 | 2024-12-18 03:08:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7e013bd1-acc9-3dd3-956c-940e4422179a | -8.8459 | -35.69574 | 2024-12-18 03:08:00 | NOAA-20 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9915a995-f917-31e5-8989-99b975b07e6d | -7.25509 | -34.82557 | 2024-12-18 03:08:00 | NOAA-20 | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e65293f7-546b-36e4-ba36-4485dc1ba9e6 | -3.06398 | -40.05136 | 2024-12-18 03:08:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| b525d47e-ae21-3d4c-93b1-e0fe51e32fa5 | -7.08114 | -35.03286 | 2024-12-18 03:08:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 0e4fe8e4-6b1f-3dbd-9aa0-4e24c320d332 | -6.7595 | -35.31726 | 2024-12-18 03:08:00 | NOAA-20 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 60a3d4f6-2f5e-3c03-818c-d499a218e323 | -6.7602 | -40.135 | 2024-12-18 03:08:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cee6ad25-50bb-3e2a-a054-ba0c39328150 | -5.9556 | -48.0642 | 2024-12-18 03:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |


[Clique aqui para ver as próximas entradas](README8.md)
