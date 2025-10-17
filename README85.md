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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c5f0e23-8369-3105-ae47-cb705217255a | -3.51406 | -52.49041 | 2025-10-17 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 62baf3e6-52c7-3755-b8ee-334d7d65cec7 | -2.7486 | -49.38885 | 2025-10-17 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 55e4d4f6-5daf-330a-90e9-69a4767cdcd2 | -7.68282 | -42.5598 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1fdc9bfc-fecb-3e48-9c7b-88c25864b230 | -7.03452 | -41.82154 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 67f2aea8-1a82-392f-85ca-93047a2cdf29 | -4.59143 | -46.33791 | 2025-10-17 04:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 290f9d3f-9c31-32e2-9b8c-4bd5f9b7c38e | -8.23029 | -44.02031 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0837947a-c30d-3665-974b-281bc509d3b2 | -7.36305 | -46.54583 | 2025-10-17 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e7757b6-f7c5-3cae-8c0c-e4f4d8e0b62c | -7.33723 | -43.86648 | 2025-10-17 04:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2e63c3f5-ffa0-3596-aa41-f66787c0346e | -4.45297 | -50.89258 | 2025-10-17 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b033385-deb0-37ce-9420-240a9c5ed237 | -5.50206 | -47.30209 | 2025-10-17 04:49:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2f6ec6e-a0c8-38af-88ee-e0bac4948708 | -5.33383 | -44.84445 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59a47766-6cf2-3b81-acb1-e06612f92630 | -3.98285 | -44.69364 | 2025-10-17 04:49:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fbf92ce-1a99-3187-9f8d-ea4452bd5fb7 | -5.692 | -42.6809 | 2025-10-17 04:49:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 212d7390-a96e-3c89-a749-335b92b53fd4 | -6.70211 | -44.37973 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1872304c-ce23-31c8-8733-c6b846a58f6d | -1.30054 | -55.74604 | 2025-10-17 04:49:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 718b0298-c9b6-3b5e-a455-7b918ac1c1ac | -4.39955 | -43.41149 | 2025-10-17 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fca64c9-f0f6-3f2f-92e1-65a3806bcb20 | -3.15235 | -50.17437 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c446bafa-c5df-37bd-b48b-112d920cc88b | -6.40555 | -47.2143 | 2025-10-17 04:49:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d4234ca4-1874-377d-ab62-faed212b68ea | -4.10752 | -48.02275 | 2025-10-17 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 798264f9-64b5-3557-8a78-23393bfcf865 | -6.84442 | -44.39244 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bab9cf1-d007-3210-a095-5223d7b1af1e | -7.03426 | -42.73133 | 2025-10-17 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 27b68900-2455-3643-99da-d1caa95a6c95 | -6.13294 | -41.74064 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8f6dfb69-7d23-3c34-95cb-3314d286cc99 | -6.31798 | -40.94713 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8fa2c8ac-145d-3565-b748-9286e6e827a2 | -5.83407 | -42.24131 | 2025-10-17 04:49:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 21c6e7ad-df5e-3e94-a07e-4ab01398aa36 | -3.65293 | -51.75106 | 2025-10-17 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c74d6bd-9194-3234-a122-53af367b6ad1 | -4.11197 | -48.02008 | 2025-10-17 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 838b8796-f2e4-37e5-ae91-37b360374a1b | -5.59962 | -50.05779 | 2025-10-17 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f2e415f-6f68-3ec6-847b-fdf5bcbe635f | -4.31077 | -48.08526 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 835e7618-3b9f-3427-9325-5093fbec3d32 | -2.88185 | -50.73045 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 130364ca-f21e-3f7c-aa6d-5b6bc8ae3729 | -4.21441 | -48.35878 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 13ed529d-a53b-3bec-b534-37b1b14b8c21 | -3.24024 | -42.07371 | 2025-10-17 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba564361-678e-3d63-b750-b5fcece521ce | -5.63389 | -43.29541 | 2025-10-17 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efb1a6a9-5731-3dd2-99ec-3021676d516f | -4.42059 | -43.39927 | 2025-10-17 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0a0ee422-18f9-3f67-a468-761ea4a4ad7f | -6.13401 | -41.77274 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6181e669-85b2-3697-9811-8846c2c20168 | -5.24153 | -50.95684 | 2025-10-17 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76d95ee4-418b-33c8-92e6-8dd6851789fb | -6.95284 | -47.71968 | 2025-10-17 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 759d2606-610a-3223-84f3-36077532ce56 | -3.73551 | -50.2553 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab083007-b4ba-35ee-ba85-cc21b1745d06 | -6.12514 | -41.75707 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3eae1c18-0d43-3f6f-b01f-2f4a22f06de6 | -7.48956 | -47.02941 | 2025-10-17 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42cfba1b-e3e3-3d14-9cda-27cf16ed7d45 | -4.40859 | -48.94846 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| caa1caf6-7853-3217-8fda-88ae97beb3f3 | -6.0008 | -43.11608 | 2025-10-17 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5d942537-e1be-354c-b5f6-b13f2905c36b | -6.87964 | -44.68925 | 2025-10-17 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed06cabb-c55a-36f8-ad43-f8a3d21fc001 | -6.39382 | -41.47498 | 2025-10-17 04:49:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 026684cf-63f7-3f79-9125-53831afc0697 | -6.51707 | -46.50971 | 2025-10-17 04:49:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55e238cb-05b9-3db3-921d-50d5a41880a4 | -5.49323 | -48.94858 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be4da2ea-8a28-37e9-9c61-621401673e49 | -7.11171 | -44.74343 | 2025-10-17 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef53e250-0c4e-352c-9482-a7ffdcfcf077 | -7.11619 | -44.74406 | 2025-10-17 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ec7f269-04a6-3abb-b1df-2c5f6af0b8c1 | -3.24016 | -45.98015 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 2050a1bc-dd60-30b3-94da-008a3476689c | -5.10123 | -56.15662 | 2025-10-17 04:49:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff3d3207-18be-34d3-9156-40f59b271d76 | -7.32925 | -44.16232 | 2025-10-17 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c9e3950d-e0a1-3099-b8e1-e8e925dcb586 | -3.78174 | -49.42644 | 2025-10-17 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 99063dab-ad12-341e-a391-f741b77351ab | -7.18249 | -41.68103 | 2025-10-17 04:49:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e11b9087-beb4-302a-89c6-284eca693efc | -8.20786 | -43.3148 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| f1ac55e1-e55f-3ad7-9612-c539ba4a9e42 | -4.2173 | -48.36312 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e5c0ad0-e89c-38e6-9ae0-f8080bdcef76 | -5.29454 | -43.54885 | 2025-10-17 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| b2b55488-aa4f-3559-8eab-6022fcb6e9ea | -7.17135 | -42.36527 | 2025-10-17 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f83a1959-ed51-3502-a7ad-42184e5a5a27 | -7.17124 | -42.52116 | 2025-10-17 04:49:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 07c46872-62aa-3dc1-bed7-4cadbd4bfd7b | -5.86471 | -43.91573 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d11c516-96dc-3b4e-9de0-09246e0e8ab4 | -7.17208 | -42.51492 | 2025-10-17 04:49:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c0a721b6-1cc0-3bbd-a3a6-01ac69d211e6 | -6.20941 | -44.432 | 2025-10-17 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| faf17a53-fd74-335e-a868-6fe7afafd715 | -6.82823 | -41.69513 | 2025-10-17 04:49:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 647ffe9c-6ff5-3018-a489-61cc8488eae6 | -7.4614 | -42.14865 | 2025-10-17 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 52657e26-f269-318c-b825-8db38b68278e | -6.70651 | -44.37833 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a264344-54ac-318b-9ccd-cc414518ded9 | -6.2905 | -45.52234 | 2025-10-17 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3aa6b09-92e8-37af-8302-1b7365a555a1 | -6.21029 | -47.87818 | 2025-10-17 04:49:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cc3fbab-2af2-3f87-8f41-05c9dae06099 | -2.73328 | -48.30742 | 2025-10-17 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69640400-4c88-3cf3-89a6-8a79543bbea6 | -3.79118 | -52.30383 | 2025-10-17 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4e2d026-a008-309d-8850-bf0122ced6fa | -4.42037 | -40.17411 | 2025-10-17 04:49:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 39574bc6-22b9-35e2-8cf2-05d5c9400e0f | -7.95295 | -44.12681 | 2025-10-17 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b153f393-24ef-3ec1-b303-3485bb490703 | -4.2641 | -49.69221 | 2025-10-17 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4dfffb1b-849a-3ca1-85d8-5f74ab228b54 | -6.4255 | -46.8832 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b1cde6e-46d7-3407-ae05-f00e3c12fc3f | -6.76392 | -42.38131 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fe34834e-6791-3a75-b43b-7853e7a273c4 | -6.34883 | -41.51551 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 34a2c524-e176-32a4-a098-b9fa859ff732 | -3.98284 | -42.49483 | 2025-10-17 04:49:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b8f58962-0988-3e2e-a3ba-2ee647fd721f | -6.87792 | -44.68694 | 2025-10-17 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abe46160-c074-31d9-a540-5f26dcd880ef | -6.12912 | -41.76822 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4a011af2-a4da-310e-a636-246bb5335c29 | -7.83776 | -45.45917 | 2025-10-17 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a7ae06e-bdf4-32ed-bfcc-2925f5bc6093 | -2.44597 | -49.0057 | 2025-10-17 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dfbf371-28d4-3f37-b725-18614768c790 | -7.90356 | -44.98692 | 2025-10-17 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6a97462-02d4-33ea-a2c8-79832112e9eb | -1.51401 | -51.62574 | 2025-10-17 04:49:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82a45b7f-4b5f-3ba8-8931-2934d1e7cc3b | -4.01833 | -48.96793 | 2025-10-17 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acbf0f92-de65-3107-921a-820748c435ad | -6.15306 | -40.91001 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| da23d69a-1339-3a74-b021-53d85db23cac | -1.70703 | -55.68628 | 2025-10-17 04:49:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9da5663-b0a8-3442-9202-11ebf36f4f85 | -4.04449 | -47.50099 | 2025-10-17 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4057331-4b50-3735-a35d-49266102c286 | -6.36972 | -44.71184 | 2025-10-17 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ddc1241-7fb6-3d7e-92d3-48a34ebc6893 | -5.909 | -44.74268 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e78b860-2630-3a7d-9225-814ac0e442b0 | -2.87021 | -50.73928 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 85bcb1c1-d2bd-308c-a5ce-baed27ca0ac7 | -7.46049 | -42.15538 | 2025-10-17 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d3ea7af7-5b83-3767-973b-81331e7bbde6 | -2.27014 | -47.19153 | 2025-10-17 04:49:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2aafbd0-4c48-3d54-b444-86f2eb6f741c | -6.20659 | -41.767 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1ec8d912-c40d-3849-b843-2814274dcc91 | -3.28907 | -52.54463 | 2025-10-17 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce1d0a22-2879-35f1-9284-d0379837b691 | -4.11136 | -48.02393 | 2025-10-17 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af7f362e-7690-3aa5-90af-7f76d9d77554 | -2.87464 | -50.73287 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f449153-6279-38a6-9923-65f0c8f001fa | -7.83549 | -45.45956 | 2025-10-17 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f94e8380-34a9-3a2c-8072-2840376cfb2d | -5.00306 | -56.07148 | 2025-10-17 04:49:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad9b1f3f-dfeb-36b7-988d-72297bd28ad4 | -3.23863 | -45.96709 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f1a876a5-0c7f-3a4f-b677-ebdd1e4e33f9 | -4.3869 | -43.39286 | 2025-10-17 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b24fccf-971a-31a9-8fea-ac8a3123d218 | -6.83901 | -42.41869 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2f13786d-3acb-3250-b94a-79b92407a299 | -6.23863 | -41.54385 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e30fd96a-3321-3f1e-aa72-d7a7e589295a | -7.28033 | -41.95473 | 2025-10-17 04:49:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README86.md)
