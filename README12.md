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
| 64532d74-ba04-3c09-aa59-8cf7e23f5026 | -1.75799 | -45.51157 | 2025-12-10 04:55:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 503b5e4a-534d-37e1-89db-a407a4a83329 | 1.11416 | -51.33147 | 2025-12-10 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4043dbd7-916d-326e-a493-dd958ec5dc72 | 3.01813 | -60.14785 | 2025-12-10 04:55:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3c9143c2-d93b-3fca-af61-2084e872a211 | 2.02974 | -55.66981 | 2025-12-10 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3f4fe08b-8f17-308d-a6c0-3ac91c97ab34 | -0.32795 | -49.98571 | 2025-12-10 04:55:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 200478ab-2dfa-360d-b3e7-ccb84c105724 | -2.212 | -45.41886 | 2025-12-10 04:55:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27fe4ccb-ef32-38d6-ade5-6e10945c6d60 | -1.73536 | -46.50734 | 2025-12-10 04:55:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e6f0896-d829-3870-8de0-8256a53aff5c | 3.37859 | -51.27192 | 2025-12-10 04:55:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c36e27d6-4649-36ae-a9d7-e206fab74a55 | -1.21091 | -52.57045 | 2025-12-10 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 181dda78-31fc-37d5-a3bc-730e32ced69b | 2.01822 | -55.66734 | 2025-12-10 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbef303a-9049-36cd-916c-409bd062fc84 | -1.01419 | -53.72992 | 2025-12-10 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81fab7ed-b998-345c-b222-23dbdbefc719 | -0.87334 | -52.62015 | 2025-12-10 04:55:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb2517f9-7507-3812-8bab-17acb29e48a1 | -0.99223 | -52.32026 | 2025-12-10 04:55:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cddf8e40-2515-30f7-9133-2d0dff373a3a | -1.01528 | -53.72302 | 2025-12-10 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5c778da-8a81-338c-b2b0-90dc13b04490 | -1.75908 | -45.51503 | 2025-12-10 04:55:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2da15497-bbd6-3347-a3c5-ca75c037cbec | 0.79358 | -51.96606 | 2025-12-10 04:55:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7bcdaceb-b96a-3972-8a29-001e5401b7aa | -1.08462 | -48.20982 | 2025-12-10 04:55:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cb61770-4832-3a00-b955-e7a9c16e1dbf | -1.01642 | -53.73733 | 2025-12-10 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 1b8eaf81-3f27-3f4b-b55b-bc6406a7c012 | -1.01365 | -53.73336 | 2025-12-10 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 241e3c18-bae9-3018-8f0c-3600e4e4bc29 | 1.16218 | -50.70999 | 2025-12-10 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 778b3ecd-95fc-3a67-8150-187e9b6d54f3 | -1.01474 | -53.72647 | 2025-12-10 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 321846c8-3752-3b84-837e-6270adabec06 | 2.02907 | -55.6655 | 2025-12-10 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0c9c6fec-7015-3a0b-9110-318506932e07 | -0.50757 | -49.17268 | 2025-12-10 04:55:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 237c7452-8b53-3dac-8bfe-eeefabe7ccd8 | 1.98448 | -55.67162 | 2025-12-10 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f49f95e2-3382-35e7-8114-8c9269b77041 | 1.15876 | -50.71053 | 2025-12-10 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2bcd562-745c-3c9f-81bf-84cb7237414f | 2.03101 | -55.67805 | 2025-12-10 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4efe10af-7e45-3797-afcc-69b94a95dea5 | -2.06034 | -46.49857 | 2025-12-10 04:55:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11c94d80-b14c-3c83-b4b7-c8dbcfea590a | -1.10959 | -53.68484 | 2025-12-10 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff5fb4bd-86b4-36d3-8376-af1427c782cd | 2.02545 | -55.66611 | 2025-12-10 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f86d73c8-d4a5-3679-8cb3-7fa31a55f05b | 0.65254 | -50.7458 | 2025-12-10 04:55:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da780088-4a35-3503-bd51-ebeabd85dfc1 | -1.73326 | -46.51397 | 2025-12-10 04:55:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc3337b1-f663-3685-a044-4dffaa289e0b | -3.68014 | -43.83023 | 2025-12-10 04:57:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de0c772f-9977-3bc4-bbbd-f188836f1e60 | -2.74382 | -48.3871 | 2025-12-10 04:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5679503d-0469-3673-a0f8-a38bfdd2f445 | -5.32635 | -43.56401 | 2025-12-10 04:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2ab45773-09a4-3582-b9ce-4c469e24e087 | -2.00686 | -54.13523 | 2025-12-10 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aac97382-241d-3650-a044-b0d47dc1f078 | -3.398 | -42.46081 | 2025-12-10 04:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 7.5 |
| e7029f83-c9ef-3c21-b98d-44b44a672778 | -3.68069 | -43.82647 | 2025-12-10 04:57:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ed044c3-4954-3463-ad9e-142952549927 | -3.5386 | -53.25716 | 2025-12-10 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a950bea2-4514-3445-96f1-ca5e30e632b4 | -5.32576 | -43.56813 | 2025-12-10 04:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 12cf31e1-945a-362b-a8a2-6e37bf59a9b5 | -3.46141 | -42.01669 | 2025-12-10 04:57:00 | NOAA-20 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9b42fd3e-dc0e-31ef-bc4b-24206ab51f76 | -3.83718 | -51.29673 | 2025-12-10 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58107cee-5064-3b9e-b810-a0a4a6eaa3fa | -5.15475 | -44.10004 | 2025-12-10 04:57:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3125677a-e286-3e2f-bc29-de316d3f11c8 | -2.74788 | -48.38769 | 2025-12-10 04:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a84a5baa-5645-3b60-a9eb-68b830ea5dcb | -3.6204 | -50.98978 | 2025-12-10 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79773d33-7fb2-3387-924e-cb623c38c7dc | -2.63425 | -45.3958 | 2025-12-10 04:57:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2bea4182-5e11-38b7-b154-4aee0288cedb | -2.35434 | -48.07343 | 2025-12-10 04:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 80cdb740-345e-3b1f-a465-6a9c798b46c1 | -2.88836 | -45.24362 | 2025-12-10 04:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7b41acf-3bdb-39df-b61d-7df572017a05 | -3.39287 | -42.11087 | 2025-12-10 04:57:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 42abfb27-fe22-3a5e-b502-a4e0d42a4f03 | -3.69358 | -43.81688 | 2025-12-10 04:57:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c99cbf1-3a45-3bc8-990d-b40f63eeba63 | -3.42594 | -41.65971 | 2025-12-10 04:57:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| eb4bae40-fece-38be-9611-3c5455f81c11 | -1.59086 | -54.12341 | 2025-12-10 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f23cdc8-92ae-3849-8162-6e25153a5dd5 | -1.34405 | -54.60447 | 2025-12-10 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c220427-6bd1-3d0c-aa07-222ab1f94564 | -3.46303 | -52.8302 | 2025-12-10 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31fcc1f4-dfe4-3dc3-9280-af7930224a6d | -1.71151 | -52.06957 | 2025-12-10 04:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c63c9d2-090d-341e-90db-dc64c79b1ab9 | -1.18484 | -55.68956 | 2025-12-10 04:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fdf7952e-6b23-3b60-a3f8-2335f4494adb | -3.01438 | -52.68154 | 2025-12-10 04:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e64e6d14-bf73-341d-bd72-296fa19e0f0f | -3.23047 | -47.47883 | 2025-12-10 04:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e3f26a1-978c-35a1-ab9f-375c6daef882 | -2.74739 | -45.39714 | 2025-12-10 04:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b7442f1-8f28-38b5-b5bd-dd7ba8bc08fb | -3.9615 | -41.529 | 2025-12-10 04:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4d357f45-254f-3437-84ee-54b14a1c99f4 | -2.77339 | -54.52806 | 2025-12-10 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c566826d-4832-3647-a495-7d36b102961a | -5.17009 | -43.11873 | 2025-12-10 04:57:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 51da1c83-3a23-33a1-92e5-23b89e9d797c | -3.72439 | -47.12346 | 2025-12-10 04:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c1bd2456-6b27-33fe-b548-a274b91d798c | -2.07089 | -49.01142 | 2025-12-10 04:57:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fbba80d6-d870-3eee-8cb6-272d47ce6992 | -5.16348 | -43.12217 | 2025-12-10 04:57:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 86af41fc-4297-3b28-8623-1fcd9eeeeaaf | -1.58421 | -54.12236 | 2025-12-10 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 458fc8f5-d7cf-3273-8519-9ca3e874665e | -1.59141 | -54.11992 | 2025-12-10 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2a06ab4-7931-3276-b133-ea5f5f60ace7 | -3.42499 | -41.65672 | 2025-12-10 04:57:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ee8724af-3fc5-3cab-9005-000a63a3e740 | -4.47651 | -44.07886 | 2025-12-10 04:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f437da5-3208-3ad5-a9f6-81e5913281bc | -3.68631 | -43.82727 | 2025-12-10 04:57:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 501f4b01-ef6e-374b-9773-599506fe59a4 | -2.79624 | -47.34661 | 2025-12-10 04:57:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09bfa0de-7607-3a92-9a53-292f788c040a | -2.81631 | -45.27724 | 2025-12-10 04:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85a5ae97-0f26-3263-8567-0bc4823c3324 | -3.08419 | -54.73168 | 2025-12-10 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6195aa02-de42-3eb1-aaac-d01722e77c7a | -2.38815 | -55.53182 | 2025-12-10 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bf20633-a72d-390e-9f63-36b09cd9577c | -2.71934 | -53.19513 | 2025-12-10 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a22e04dc-77ac-3f30-a605-9999c8bf1c06 | -5.33825 | -43.43722 | 2025-12-10 04:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af42cfb3-2ff9-32f1-bd10-22bb8a290818 | -2.81588 | -45.28013 | 2025-12-10 04:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27e0519e-2934-3b76-84d6-65845ff4e638 | -2.88881 | -45.24071 | 2025-12-10 04:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d3e7009-1f7c-3c60-887f-c9913730bdd1 | -5.33767 | -43.44133 | 2025-12-10 04:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5518560-f0ed-3c92-a5e6-5e548ebf0669 | -3.4403 | -41.65112 | 2025-12-10 04:57:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9786f8b6-84e0-3bea-93e7-464ca0e031d6 | -2.1263 | -48.73516 | 2025-12-10 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0730a904-4b4e-3bba-8b86-ae052f5640e3 | -5.33223 | -43.56464 | 2025-12-10 04:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 451de759-ec54-34ad-849e-73112d4c4b03 | -2.86189 | -48.77895 | 2025-12-10 04:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30963617-64cc-312c-8f62-350eb0b3bcbd | -2.41987 | -48.27286 | 2025-12-10 04:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6aa52cbd-5ec9-3cbc-a9d1-1e890443d3c9 | -3.74643 | -50.94643 | 2025-12-10 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8ff3a1c-a3aa-3fec-a62c-65f3bc409dc5 | -2.64691 | -52.27599 | 2025-12-10 04:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a828c7a-7fe6-3da9-a94b-e94237a456b3 | -8.09944 | -55.00968 | 2025-12-10 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d585bd37-acaa-31e3-b6db-b3ab46bfc34c | -2.88834 | -45.23944 | 2025-12-10 04:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b828bf3-8737-330b-b1de-0bc219cbf705 | -6.89648 | -42.83892 | 2025-12-10 04:57:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 70cbde9c-d30c-31ca-8990-ee1a83220760 | -3.95574 | -41.52261 | 2025-12-10 04:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f871a5f6-dda9-342e-a6fc-c751070c1b04 | -1.57879 | -53.12503 | 2025-12-10 04:57:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d06191c3-f7b1-3767-82e8-32e8267879ab | -2.72206 | -53.17793 | 2025-12-10 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 900f99e6-f812-3550-9aed-a3bdda0aabde | -3.96225 | -41.52369 | 2025-12-10 04:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a6da1a74-6031-3b62-8932-540a7c1185d4 | -3.67961 | -52.53313 | 2025-12-10 04:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f16bf74e-f44d-3edb-8415-c1d4259db78e | -1.47264 | -54.20481 | 2025-12-10 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b164d107-924f-3d59-9547-91ce2616feef | -5.16411 | -43.11771 | 2025-12-10 04:57:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fc6913a6-2428-3fdc-a5fa-51db6a1b9398 | -8.09834 | -55.01662 | 2025-12-10 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ffeba4a-13c4-3d22-b36a-e83e14cd0f3c | -2.8222 | -45.27229 | 2025-12-10 04:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cc972ea-570e-35f7-adc4-ef8b65e00811 | -6.68794 | -43.68818 | 2025-12-10 04:57:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92f5e8e7-4ffc-3fee-a477-a7de992d75b7 | -2.26198 | -53.70447 | 2025-12-10 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 02903a6a-551c-39d3-bd7d-1870cb97e784 | -1.24823 | -54.16228 | 2025-12-10 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README13.md)
