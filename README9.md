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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29e52bb9-7c81-3041-8d18-33af5e044bdc | -15.0865 | -59.6487 | 2024-12-11 03:00:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 9a4ac789-7dca-3f5b-8d9d-4303fd13902e | -6.1178 | -42.5559 | 2024-12-11 03:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 12652e69-0f06-3623-aa58-708a97f5d4c5 | -2.8196 | -53.0629 | 2024-12-11 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 99a70e48-1157-3c38-8393-13449bbdc346 | -6.97 | -42.99 | 2024-12-11 03:00:00 | MSG-03 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 08f15a90-eafa-35da-8ecb-16492b63c44f | -6.9 | -43.51 | 2024-12-11 03:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8aed85a6-c215-30d4-b94d-9cabc3481b4a | 2.7444 | -60.6381 | 2024-12-11 03:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 32ad0d87-8001-367d-b4f9-c6a64ec7e7f3 | -6.1178 | -42.5559 | 2024-12-11 03:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 104.6 |
| 7f71397e-689e-3d62-9499-c1f13643a8ed | 2.7627 | -60.6378 | 2024-12-11 03:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 5a7697dd-8382-3747-bb43-6695098600a3 | -17.7129 | -40.2695 | 2024-12-11 03:10:00 | GOES-16 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 136.2 |
| 721b389e-1b0c-3c51-8b10-29342a86921e | -6.978 | -42.9977 | 2024-12-11 03:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 165.1 |
| ca2ed0c5-073f-373c-9a84-73dca000ee16 | -6.1368 | -42.5307 | 2024-12-11 03:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| d7150595-78d4-37de-b4e7-070f152f0ff6 | -6.9594 | -42.9759 | 2024-12-11 03:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| f9e0f9bb-f70a-3ef2-ba15-7fbe6da1ebbe | -15.0865 | -59.6487 | 2024-12-11 03:10:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| ecdfc1bf-4329-3fcd-95e4-1fa5b32f59f0 | -6.9161 | -43.4952 | 2024-12-11 03:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 337f17ef-6997-3eee-9ed4-f4fbb99dd41b | -6.118 | -42.5323 | 2024-12-11 03:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 144.2 |
| c4d5446e-c960-32dd-919a-728ff0fd3bf5 | -18.0261 | -52.9829 | 2024-12-11 03:10:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 8f883e05-0787-3fe4-ad61-266c654b282d | -2.8196 | -53.0629 | 2024-12-11 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| c65e323a-bed2-3b33-8bfa-f3340ac78d4d | -6.9592 | -42.9994 | 2024-12-11 03:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 169.3 |
| 76edf295-73b2-315b-8199-73007855ad10 | -6.1366 | -42.5544 | 2024-12-11 03:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 486c1aed-d76a-3263-b564-1187c5ffc96c | -6.8972 | -43.4969 | 2024-12-11 03:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 96552a7e-0fcc-395e-9ed8-24831cf8e444 | -6.9158 | -43.5185 | 2024-12-11 03:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 198cd877-4be4-35a9-9d7b-6eba98083258 | -6.9783 | -42.9741 | 2024-12-11 03:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 57b803de-e297-3b5e-a80a-da16a4b17f07 | -6.897 | -43.5202 | 2024-12-11 03:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 202.5 |
| 243ea4fa-ebb0-3bcc-8553-0552288f1313 | -8.03561 | -38.18386 | 2024-12-11 03:17:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2802c0b7-08c0-3246-9333-89fbc82bc940 | -7.21211 | -39.77269 | 2024-12-11 03:17:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| dfff23c1-3597-357b-81fa-5e1f716d1b0b | -8.28263 | -35.29431 | 2024-12-11 03:17:00 | NPP-375D | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 13899e86-909f-33b4-905f-5fca06fe2b91 | -7.15263 | -40.26232 | 2024-12-11 03:17:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 736f4f52-0089-31bb-83ad-d7ef52231403 | -6.12473 | -42.5505 | 2024-12-11 03:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1a7c8047-a9f1-3b77-8b99-119e485497a8 | -7.86589 | -35.20478 | 2024-12-11 03:17:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c1189f77-1b41-388e-b662-11634e9c8d6c | -6.95987 | -42.98853 | 2024-12-11 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 8d35de91-16f2-3620-8e12-0a06259aac4b | -12.85236 | -43.81719 | 2024-12-11 03:17:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02086bf4-1219-361b-918d-fefafb272ba3 | -7.93001 | -35.20154 | 2024-12-11 03:17:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0c1f3c09-02c9-3e12-988b-cc07e69e0be1 | -13.25729 | -41.33911 | 2024-12-11 03:17:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d5ff64ec-dc59-33cc-ae6c-a32000972476 | -7.37708 | -35.1966 | 2024-12-11 03:17:00 | NPP-375D | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d779a835-b56d-3ee3-8c1e-e3018fb6b8c0 | -3.07637 | -40.04836 | 2024-12-11 03:17:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| da01e901-1d12-3e08-9f2e-d72bb9f457c8 | -7.37273 | -35.19588 | 2024-12-11 03:17:00 | NPP-375D | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 02f99003-24d9-315f-90d1-cd8263968de9 | -6.97428 | -42.99089 | 2024-12-11 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 90c6f253-109c-371c-821f-9f604dc71eb7 | -3.06987 | -40.05426 | 2024-12-11 03:17:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f5468ebe-83cd-35b4-899d-3488a1a61c45 | -5.94998 | -38.3298 | 2024-12-11 03:17:00 | NPP-375D | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 766110c9-4b05-3cda-9868-9a8d7454afd3 | -13.25643 | -41.34335 | 2024-12-11 03:17:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e90e00ec-2bd9-3762-a56f-cb08ce010e6e | -3.07549 | -40.05361 | 2024-12-11 03:17:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 8b402ac1-68b7-3b17-9b4a-0d2476969a97 | -3.07171 | -40.04376 | 2024-12-11 03:17:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 05ed8755-ebf1-3faf-b3af-5aa542e90a2b | -6.9729 | -42.99813 | 2024-12-11 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 18c5966a-ff29-3c5a-9e43-15b4ed9f0b6e | -6.94935 | -42.99591 | 2024-12-11 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 11096cde-541d-30b7-9cbb-ff4b79e180e1 | -3.07079 | -40.04902 | 2024-12-11 03:17:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 00dffeb4-5631-3646-bec5-206df7859f43 | -6.96708 | -42.98968 | 2024-12-11 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 45118ce1-5557-3d2f-930e-ce245142acbb | -8.51226 | -35.13812 | 2024-12-11 03:17:00 | NPP-375D | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0175c112-4b00-354d-89c5-f52d91309932 | -7.47732 | -34.84494 | 2024-12-11 03:17:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1c4c85b9-ec0c-3665-be73-8f01275a8792 | -7.60268 | -37.57709 | 2024-12-11 03:17:00 | NPP-375D | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4eeca1e0-9059-3864-b2b6-9831b5b71b32 | -8.10989 | -35.06662 | 2024-12-11 03:17:00 | NPP-375D | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| eda8a0c4-b65f-3924-884d-18582f70c61a | -7.78461 | -35.22915 | 2024-12-11 03:17:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bc296185-bb0e-341e-927a-c145e8f032c7 | -5.07314 | -37.71827 | 2024-12-11 03:17:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0f7443e2-f74d-3e7e-9436-a9307c8c0f29 | -7.92571 | -35.20082 | 2024-12-11 03:17:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 60503b23-cde9-3e5a-9813-69ed67e43b9c | -6.12237 | -42.54133 | 2024-12-11 03:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d3a740ef-a8fa-38e2-b97d-7da490dc24d8 | -6.54418 | -39.28866 | 2024-12-11 03:17:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 125edd4e-4c3e-329c-a379-0c1251ec320b | -5.95057 | -38.32669 | 2024-12-11 03:17:00 | NPP-375D | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 11749030-a565-3891-a0ac-c70bddc9ab92 | -7.7853 | -35.22504 | 2024-12-11 03:17:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2b96d927-82cf-31d1-8893-9c853bdf1209 | -7.75307 | -35.25764 | 2024-12-11 03:17:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 24e83986-de8e-3983-9a7d-e35ecebc4bf2 | -6.98008 | -42.99943 | 2024-12-11 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 460f80aa-29af-3428-9228-2049bed885ce | -6.96568 | -42.99699 | 2024-12-11 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 01491109-5507-3752-8613-7b29b7e2fd9d | -6.11712 | -35.27961 | 2024-12-11 03:17:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b432fa26-322d-3d5e-a9e9-0162cd6ec1bb | -7.78614 | -35.22917 | 2024-12-11 03:17:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 641191b4-bc83-377a-83b2-1b193c84f55e | -7.59762 | -37.57607 | 2024-12-11 03:17:00 | NPP-375D | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fcd3a8b9-0f79-3ba0-b0f8-36e3de15c51b | -5.42407 | -39.52686 | 2024-12-11 03:17:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 207c7453-6b4a-35bb-bed3-000297540aba | -5.94995 | -38.33029 | 2024-12-11 03:17:00 | NPP-375D | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a85fd1f0-07a8-3880-9602-26134cd0a484 | -6.17982 | -35.30104 | 2024-12-11 03:17:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0c79acca-5e0d-39ad-9d48-30da18634411 | -6.87616 | -35.28249 | 2024-12-11 03:17:00 | NPP-375D | CUITÉ DE MAMANGUAPE | PARAÍBA | Brasil | 2505238 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dfbd233b-e29e-31cb-8f75-8c4427a13fa0 | -6.95711 | -43.00294 | 2024-12-11 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 0146bdad-0116-3c46-9afe-a11beace389b | -7.26765 | -34.93634 | 2024-12-11 03:17:00 | NPP-375D | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 43945434-41f6-3272-b3c4-271388c2f5f1 | -8.11413 | -35.06742 | 2024-12-11 03:17:00 | NPP-375D | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5773893d-fff6-306a-bcdb-3f53d2234e93 | -6.95849 | -42.99575 | 2024-12-11 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| a61630b3-8dd5-3fe8-aebc-65c7c8b1a1ad | -3.06907 | -40.05254 | 2024-12-11 03:17:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a6c93b14-e5be-3a2d-8b18-44f9fd535b91 | -7.78893 | -35.22992 | 2024-12-11 03:17:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 38300b8b-78cd-3125-99c4-af60b6c976a2 | -3.06995 | -40.04728 | 2024-12-11 03:17:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| e2e015f5-4c51-3e35-be6c-ab339cdfdea9 | -6.53843 | -39.28737 | 2024-12-11 03:17:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0e7cf140-15a2-3e6a-bf68-472cd7e0d7d6 | -7.52709 | -35.10751 | 2024-12-11 03:17:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| db5cf72d-5300-353b-b0cc-bfb7f03154ba | -7.59943 | -37.57841 | 2024-12-11 03:17:00 | NPP-375D | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2b24d56b-913c-3411-ad1b-ddd13e827186 | -5.95063 | -38.32619 | 2024-12-11 03:17:00 | NPP-375D | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 373c250d-889d-3582-81c2-1eaa3ec35d6b | -8.10922 | -35.07053 | 2024-12-11 03:17:00 | NPP-375D | MORENO | PERNAMBUCO | Brasil | 2609402 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 749dd1d0-e577-3733-a25f-f2dce24ee67f | -6.96431 | -43.00417 | 2024-12-11 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| eb1586c0-44fb-31e5-b1d0-e1d940add8ff | -6.94992 | -43.00167 | 2024-12-11 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 10c154db-62bc-3cb4-a4e6-dd340346d527 | -6.95131 | -42.99441 | 2024-12-11 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 657b5f4e-e772-30a6-9f44-4d1467c0c719 | -7.21429 | -39.77438 | 2024-12-11 03:17:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| fee048eb-9eeb-354b-86dd-b6b3e54576b0 | -6.12103 | -42.54829 | 2024-12-11 03:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b3be25c8-31f2-3d4d-88fa-d272fed2a7f4 | -12.41372 | -43.80113 | 2024-12-11 03:17:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bc4467a4-cfd1-3910-ae3c-a1e2ffb83b7b | -6.948 | -43.00323 | 2024-12-11 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| c1370aa5-7f6e-3b7c-b357-68b2924b1bea | -8.51293 | -35.13424 | 2024-12-11 03:17:00 | NPP-375D | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3d770d7f-a53e-3f92-8d9c-a40545db6421 | -5.42328 | -39.53124 | 2024-12-11 03:17:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 103ba974-ecd9-3f20-a458-5567ded4d28b | -7.9214 | -35.20012 | 2024-12-11 03:17:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 1c8a6156-4214-33ad-9835-a0eba4cb5190 | -12.85101 | -43.82348 | 2024-12-11 03:17:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cafb1394-b3a9-3a86-a46a-6670df7c2d3a | -6.12815 | -42.54944 | 2024-12-11 03:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f15b7c68-9dbb-3017-876a-4d2b19714efa | -3.07721 | -40.05006 | 2024-12-11 03:17:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 4c1df427-dddb-3f01-8f01-6b04b295bb5d | -8.04086 | -38.18483 | 2024-12-11 03:17:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 257951c6-0837-373a-9130-63271bbedb08 | -12.41321 | -43.8017 | 2024-12-11 03:17:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 08ed1498-ff9c-38ae-b109-55fa36f2b5d9 | -6.94274 | -43.00031 | 2024-12-11 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 70f1f376-e183-36da-b173-af3732538a24 | -7.69391 | -35.2132 | 2024-12-11 03:17:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 60f3b849-bf29-394b-b43b-4acd067afe65 | -7.21493 | -39.77075 | 2024-12-11 03:17:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 23dbec2e-3561-338f-91b2-7633046c46d2 | -8.23659 | -35.00668 | 2024-12-11 03:17:00 | NPP-375D | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b2b023e6-70cf-3850-8500-2cf9a26cb674 | -6.97866 | -43.00692 | 2024-12-11 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 903afc51-89a8-3634-9850-60ed05b4994a | -7.92212 | -35.19599 | 2024-12-11 03:17:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |


[Clique aqui para ver as próximas entradas](README10.md)
