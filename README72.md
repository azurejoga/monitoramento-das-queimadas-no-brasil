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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de18fac7-26d4-3b0c-a19b-a3c4ad256d7c | -2.52329 | -47.44176 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f81287f-df62-32ba-81b6-33126bc7e43b | -2.5218 | -47.45185 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f11c777-3be3-325f-9a91-808abd83b8fa | -2.52142 | -47.45035 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c1544931-1c55-3657-a6c3-87dd7fe0f67f | -2.52107 | -47.45685 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 39675de0-0320-36d7-9257-c673bc50d589 | -2.51853 | -47.44106 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d20c948b-674e-31fc-a8df-3b8fc29a61d5 | -2.51589 | -47.45464 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de4a4ef5-6485-3b0a-96ab-67e4c3462223 | -2.51114 | -47.4539 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 275bba85-7bc0-3913-a82d-b86543544f43 | -2.44992 | -48.48796 | 2024-10-29 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e5eaea1-6dbb-362e-81f8-3d35f7e7ade1 | -2.43626 | -48.66317 | 2024-10-29 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 26fa2533-b5ad-3863-b834-1d96a52c41b6 | -2.40925 | -48.54729 | 2024-10-29 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27ffe5dc-b8b0-3865-adf1-078ddf496007 | -2.40485 | -48.54661 | 2024-10-29 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 604ff205-18a4-32b2-adab-c7c7016a600c | -2.40174 | -48.53743 | 2024-10-29 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb3e3867-5bc0-3143-bbdb-bcba04e0a386 | -2.40045 | -48.54594 | 2024-10-29 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4b7d04d-5ac8-3e02-862c-946269444b60 | -2.39542 | -48.54949 | 2024-10-29 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 629884a1-01f3-3571-b45b-11485e40d6f8 | -2.37562 | -47.66874 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e0febd8-1448-3dc6-8294-7cf916f9d6f5 | -2.97005 | -48.05482 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bbc42c17-05a5-37e0-b7d5-86647a58bb06 | -2.96932 | -48.05951 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dbdee004-9af8-33aa-b3fb-774ad3a18291 | -2.9682 | -48.06112 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3a088257-c1a6-304b-b68f-552585f838ec | -2.94425 | -48.56263 | 2024-10-29 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6cf04fe7-d5db-3bee-a5c4-fa3ba7848a90 | -2.942 | -48.98488 | 2024-10-29 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3eb96fd-d8dc-3651-9c2f-a89b01857e30 | -2.92423 | -48.95736 | 2024-10-29 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0907f8ad-1a56-378f-bb0f-f83219961beb | -2.91992 | -48.9567 | 2024-10-29 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc8ed329-5b4a-3383-b3f8-ebf055f34351 | -2.91193 | -48.95135 | 2024-10-29 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7d1ce87f-e387-34c6-8981-ceda806eb133 | -3.07187 | -47.4862 | 2024-10-29 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9739f622-192f-31c2-aedd-a1ef0f96658f | -2.97348 | -48.05708 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9136a269-39fd-34e6-8a95-907dfee3ba81 | -2.96957 | -48.05175 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f144a25e-057d-38b8-95bf-46ce0ea2a0a7 | -2.96889 | -48.05644 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 791d01e1-f1d6-33ee-b655-e6dc4be01eff | -2.9686 | -48.06419 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a593c16-0dc7-3a20-afa2-eddc5f66846b | -2.9463 | -48.98553 | 2024-10-29 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4dda82b-b9a6-3a64-b01e-34398a3afe01 | -2.9449 | -48.55833 | 2024-10-29 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d5169bf-bbfe-3995-a2da-ae6d956e422e | -2.94379 | -48.98785 | 2024-10-29 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 292cdb54-93c0-3e4c-8fd8-ef3c204da2a8 | -2.91255 | -48.94727 | 2024-10-29 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dbf83e79-c631-3c31-9655-bd5790de6233 | -2.81477 | -48.43842 | 2024-10-29 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2cf3157-2054-3c82-b856-8e9544613ba4 | -2.81161 | -48.43999 | 2024-10-29 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e82dc0b-872e-3b0f-a38d-af2fdcc18d44 | -2.77219 | -48.69274 | 2024-10-29 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 708bb231-4d2b-309a-a981-4f20ddd939ee | -2.77218 | -48.6953 | 2024-10-29 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cda78d15-8f0e-3db3-a609-57b589926cce | -2.77153 | -48.69693 | 2024-10-29 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01cee9fa-5a59-3b7a-8acb-56642e5079e2 | -2.7653 | -48.71149 | 2024-10-29 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5396d87-c6dd-3a97-8587-1aa6cc31d3ae | -2.76453 | -48.71312 | 2024-10-29 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50dc9865-e085-396c-8502-71cba24f01ca | -2.61977 | -48.31984 | 2024-10-29 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a88bb56-a0a4-3418-a9d2-21949d9abf55 | -2.61794 | -48.31722 | 2024-10-29 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ee2d871-473c-3138-97ad-059e4bc5313b | -2.61662 | -48.32608 | 2024-10-29 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cec7e33-7e24-36bb-b246-b12e8d75617f | -2.61391 | -48.32798 | 2024-10-29 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 39cc8946-f6a6-31a8-9804-ca80c8b85eb4 | -2.61007 | -48.37018 | 2024-10-29 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4baef7ef-e9af-3094-a4cc-912b2c59dca5 | -2.59519 | -48.21114 | 2024-10-29 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af451f2b-0865-3fca-8afa-43c4b7afb37c | -2.52298 | -47.44027 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0165972a-a94c-3cd7-9167-81429be4dfdf | -2.52254 | -47.44682 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ebd5188-044e-35a7-bbb2-a84b26fd86f4 | -2.52064 | -47.45535 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc60575f-d910-31cc-a833-621080661dc1 | -2.51779 | -47.4461 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 458c36c9-27fe-33fd-9948-c818ebf619e0 | -2.51744 | -47.4446 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f4c50dfd-d7ab-3487-b13a-2b17d9dc0b67 | -2.51705 | -47.45113 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f1e168a7-66b1-36ef-808f-0b383ae767b4 | -2.51667 | -47.44961 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0bf3fd95-70e8-32a3-ba55-cb8398a18aa1 | -2.51481 | -48.12734 | 2024-10-29 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36819fd2-8288-3c19-ba49-a80e10776dbc | -2.51192 | -47.44886 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 5f6d4928-3067-35ac-9de6-722f66519b19 | -2.44727 | -48.50512 | 2024-10-29 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 290b6e87-c2fc-3176-81c7-63547c4e9c0a | -2.44286 | -48.50444 | 2024-10-29 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d652da5d-48db-3329-8cd7-038394444e66 | -2.43553 | -48.46378 | 2024-10-29 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7d64092-7246-3591-9912-2e44bbb78f75 | -2.4319 | -48.66253 | 2024-10-29 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a6997f4-9c77-354f-aab2-53d0e56efbfd | -2.4086 | -48.55152 | 2024-10-29 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6a71b7b-6b5e-3bb9-b5e7-d6ba5fede5cd | -2.40549 | -48.54237 | 2024-10-29 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9664ddf7-14c9-3204-bdf0-cee871c1fe2a | -2.40421 | -48.55084 | 2024-10-29 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5c65218-0e4d-303b-ae2d-1adc1339cd23 | -2.40357 | -48.55507 | 2024-10-29 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e2f572c-1277-31f4-976e-3a08017bc266 | -2.40273 | -48.44108 | 2024-10-29 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b6c0b91-6743-39d8-ab31-bad577985faf | -2.39981 | -48.55017 | 2024-10-29 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d89f5a37-d583-36c7-937e-2a59073f6a41 | -2.39917 | -48.55439 | 2024-10-29 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3cbfceb-80b0-3a44-94dd-dce209576802 | -2.39478 | -48.55372 | 2024-10-29 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| faa0bade-1cc7-317f-aac5-d469197c34d0 | -2.37095 | -47.66802 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5cb21785-487a-3763-a0a0-5a9f3156f9d2 | -2.36554 | -47.67211 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5df9a074-66b6-3bd7-bf2b-d92a521ad306 | -2.19857 | -48.83493 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8ffdaef6-def1-3af6-90dc-591cadefb062 | -2.1949 | -48.83024 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1bdd18ea-1101-3bfe-95c4-697f77977353 | -2.19249 | -48.8175 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 258fdb13-6363-3289-b79d-078098c79000 | -2.19186 | -48.82154 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4956e903-3e6b-36f2-bc59-92ccaddc8454 | -2.17611 | -48.72334 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 77c7318a-a9d4-3791-890a-7e5da5086d51 | -4.91819 | -48.63467 | 2024-10-29 05:01:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cadaae58-6f0b-339a-9759-1fbd73d45115 | -4.91365 | -48.63403 | 2024-10-29 05:01:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 749552d4-f02c-36ce-b560-cb56f4401075 | -4.91228 | -48.64311 | 2024-10-29 05:01:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5b8f859e-b31a-382a-9e5b-6bd5006b1023 | -4.91161 | -48.64759 | 2024-10-29 05:01:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6bde2d8-1ed1-3aed-85f4-374eff76681c | -4.90774 | -48.64244 | 2024-10-29 05:01:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0449afd0-1e33-3ad9-8b75-b63625945292 | -4.90707 | -48.64694 | 2024-10-29 05:01:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2efad55e-27cb-32c7-85b1-5188b3703e48 | -4.89072 | -48.66326 | 2024-10-29 05:01:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5fab42db-2a75-3db1-b0d7-f9adc1d937c9 | -4.89005 | -48.66777 | 2024-10-29 05:01:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5009f910-6f39-3346-95c0-e4b8bcc1a8ca | -4.88619 | -48.66262 | 2024-10-29 05:01:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fac1785d-c70a-3e0a-942b-3a4b0f73434b | -4.88099 | -48.66646 | 2024-10-29 05:01:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0277255a-828e-3c3d-b6fc-86998af1b898 | -4.84802 | -48.63849 | 2024-10-29 05:01:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ba44cc7-89ed-37c9-b025-479a35e9486b | -4.84736 | -48.64307 | 2024-10-29 05:01:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab79bc51-50a4-3fff-ac5f-859441b6bd80 | -4.57218 | -48.01578 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48c89904-beac-3334-8b6c-ebe2d5d76ab1 | -4.57144 | -48.02073 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ef8fb90-ea35-33d5-8f00-6ae58abbf929 | -4.35636 | -48.15046 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0bc8557-3ed4-3c63-b495-974183bfcbe7 | -4.35424 | -48.15199 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0eab63eb-619e-3d34-83eb-5aa5e321232d | -4.35171 | -48.14972 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e7112d9-b0a0-3661-bce2-e9e2974f03b8 | -4.35028 | -48.14644 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78b4efb9-55b2-337e-ab13-a4c8db39004e | -4.3496 | -48.15118 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7237eeb8-126e-3bed-a91a-c96f6be876e4 | -4.34767 | -48.61285 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73dcbe02-54a5-394a-ae4c-e83af720212a | -4.34706 | -48.14895 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7f7fa1b-a791-3693-9f01-d2ec0dcd597c | -4.32948 | -48.64229 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5fec6d7-9477-3ed6-be0f-f2f8a34218bb | -4.29734 | -48.64191 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 234733fc-647a-3964-9175-50b489ffcbe2 | -4.29606 | -48.65074 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 292be0a1-d22a-3fba-bc6a-4012a08bbaaf | -4.29606 | -48.60732 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 138117fa-57b9-3607-99d0-70a8837ba207 | -4.29538 | -48.61179 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a708571-4d3c-3137-be65-e06c16a3b394 | -4.29399 | -48.62081 | 2024-10-29 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README73.md)
