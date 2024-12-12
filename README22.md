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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c24eb501-f98a-342d-b769-f58bb8e7bc24 | -4.55422 | -43.57072 | 2024-12-12 04:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 85e6301b-cc60-399e-8e0e-e7e6ca7ea7ae | -5.0231 | -46.8338 | 2024-12-12 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 04e8cd26-da49-3cfb-9ae8-99c2dfeb2300 | -6.97177 | -43.00369 | 2024-12-12 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 115e54d5-a86a-3c7e-b51e-b6e1e8a1c3a2 | -4.8109 | -47.22063 | 2024-12-12 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a93de04-eace-38b5-88d2-2ee4d66394b4 | -3.65622 | -45.70404 | 2024-12-12 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8da3e0a1-3776-3b56-aed4-1a644909e38c | -3.98515 | -46.89909 | 2024-12-12 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3fc10ab-888e-3b06-b10b-7b6a47148df1 | -4.50783 | -43.6188 | 2024-12-12 04:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac4d7527-0296-3902-9b04-bf39a8d1579a | -6.05694 | -44.05169 | 2024-12-12 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b21cde35-94de-30ff-b729-094dcfb1de81 | -4.09305 | -46.67044 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e82c1f4-6006-327f-a808-4fd8207ab544 | -3.65259 | -45.70348 | 2024-12-12 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e0a097c-dc31-3cce-97bc-486506afaa96 | -3.97882 | -46.89433 | 2024-12-12 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55f0cf66-1fad-35d2-a661-a083c9c16bef | -3.24237 | -46.87217 | 2024-12-12 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8b6c498f-aa4a-3748-b0f5-f748b1e784cc | -7.71513 | -45.6612 | 2024-12-12 04:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fffd11f4-67cc-3c61-abea-5f7a7882aae1 | -5.14489 | -46.17773 | 2024-12-12 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bba90113-8624-3837-af09-9caf2c53066d | -4.02801 | -46.81623 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d33a1a7-517e-346d-bae4-545fac4562e6 | -3.04628 | -47.96779 | 2024-12-12 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8f1fcc0-8f7d-3882-bf28-4c7ac3b2a37d | -6.94053 | -43.51054 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1ea5849-cbc6-3280-ba40-f1cabad01f23 | -4.80208 | -50.82431 | 2024-12-12 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c05e55a-c65e-3db0-b24a-1cd934b4cb07 | -3.21275 | -53.00754 | 2024-12-12 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 874b9d6c-891c-39ad-8223-152817ac9058 | -2.93921 | -52.42702 | 2024-12-12 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d749298-e373-30c7-b4ee-f09f5419ba75 | -3.60066 | -53.71938 | 2024-12-12 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88ddfaa2-b530-33fd-b00d-8f9ad90d62bc | -5.92295 | -48.05973 | 2024-12-12 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e8ed3fe4-0219-3f77-bf8a-cdff9f3e0298 | -5.92068 | -48.05205 | 2024-12-12 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 726c38a7-5e84-350c-b99a-8d3354d77e62 | -4.028 | -46.88572 | 2024-12-12 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c45ca006-c90c-32f2-9e67-1c4f27bcdcd8 | -2.96 | -53.72308 | 2024-12-12 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37eb25e8-4583-3052-8b63-e2c7dfc67e49 | -7.46942 | -44.73925 | 2024-12-12 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e70c9c7f-7e36-3112-abe9-9be43e09fc35 | -5.34741 | -44.19606 | 2024-12-12 04:38:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68227d43-0c10-366a-84a5-cae76f6711bc | -2.52835 | -51.78684 | 2024-12-12 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87c82367-46c7-3ad9-97fa-deb82dacf377 | -4.06437 | -50.37062 | 2024-12-12 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c7d11a2-ca59-3d50-8fcb-8c94aa926110 | -2.91216 | -52.95698 | 2024-12-12 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fd27b1c-5d28-3513-8942-a64932d9e0b8 | -4.35664 | -48.47777 | 2024-12-12 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af35fe14-d430-350b-a774-9c95b9f9023a | -2.9949 | -48.07757 | 2024-12-12 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 10b9416f-9788-391a-8246-3268aef61735 | -2.95616 | -53.1093 | 2024-12-12 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6d0da3a-3067-3860-935a-9e92895c6114 | -4.07464 | -54.29941 | 2024-12-12 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bb7e91d-035b-34f3-8086-124e0357d7b4 | -6.93321 | -43.53064 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 8fd92a3f-fd52-3048-944c-57c23712c00e | -6.9709 | -43.00163 | 2024-12-12 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d1d52bb0-00f8-3f1b-8d0f-ae60ac90b13a | -4.05122 | -46.66415 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e9c8524-fa8e-3793-b184-4378f752b7fb | -5.87612 | -35.40978 | 2024-12-12 04:38:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 1b77b7cf-a683-34d4-b4cc-743392df85fb | -6.12398 | -42.54187 | 2024-12-12 04:38:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3b5ac483-3976-3101-8d45-c1c5b894129b | -4.01366 | -46.64749 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da6c1294-5a5a-3ed6-a462-0b772400b55a | -3.9537 | -46.75914 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7a13f89-0394-3c56-985f-fc839870e41a | -4.80267 | -50.82063 | 2024-12-12 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 656b4ec3-4d2b-38b4-9ee7-7d0e791a6653 | -2.96213 | -48.61123 | 2024-12-12 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 492d0bfb-ab58-3122-a216-681e971af145 | -3.89478 | -42.55358 | 2024-12-12 04:38:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a10ce2a9-a8fd-31cf-af8f-9d3c6b6f7808 | -2.46866 | -47.83126 | 2024-12-12 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f85cd3d5-8f56-3cd3-84ad-547702581e63 | -4.05017 | -46.66498 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21c99124-9200-3c70-b9df-348d35af07dd | -6.03825 | -42.1583 | 2024-12-12 04:38:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 31a343a2-d86f-34e6-8618-61fc7bd966da | -3.24179 | -46.8759 | 2024-12-12 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| e1e7af8c-8a67-3364-b333-59f4613d7c32 | -4.08793 | -46.61082 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f372b439-878c-33e8-843f-f22fd646b2c0 | -4.02633 | -46.81686 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97f4132c-10a6-31c8-ae55-e665f8e2641f | -6.92194 | -43.5164 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 696edfce-5b26-30cd-a289-9cf7aadfe5ce | -3.84927 | -40.44958 | 2024-12-12 04:38:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| aeaf4a4e-920a-3731-9292-6b6b2492d1dc | -4.0214 | -54.28777 | 2024-12-12 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 945d4c77-4a19-37e5-9c27-3b02f98095dd | -2.91781 | -48.03308 | 2024-12-12 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9b1b5b0-f7e8-3565-b5ec-b1857987e078 | -4.09096 | -46.82186 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03bd77c8-8bbe-3b52-9cda-e517f6d175fa | -4.20253 | -47.79267 | 2024-12-12 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d20c93ed-454f-32e3-acab-0e68c31d9ca8 | -3.00926 | -48.05129 | 2024-12-12 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ae2a17a-a11a-3565-985f-361f5fa8ea11 | -7.60816 | -46.65052 | 2024-12-12 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 027145d1-22ef-3aa9-adb4-a47f63b51905 | -2.67389 | -44.29158 | 2024-12-12 04:38:00 | NPP-375D | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8f06820-2813-363e-89c1-e8c7872d3de6 | -6.09745 | -44.04996 | 2024-12-12 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5678fca-9a68-3f8d-a0bc-aba0f639b070 | -2.46532 | -47.83075 | 2024-12-12 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4783d32a-346a-382c-bc1a-a1335e064f08 | -4.01997 | -47.02967 | 2024-12-12 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96945060-9f6d-3650-8b00-a641ce2d3cf6 | -5.92351 | -48.05616 | 2024-12-12 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e1d82eaa-8795-3dfb-869e-13b49582937c | -3.24807 | -46.88066 | 2024-12-12 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0e603f46-967a-3a54-8dfe-13849a63944b | -2.91602 | -52.95758 | 2024-12-12 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a25e2594-d96d-3f62-b769-58c727ea8daf | -2.33646 | -45.22722 | 2024-12-12 04:38:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a68b1358-3957-344a-bfad-bec22eba12c4 | -5.08757 | -47.88809 | 2024-12-12 04:38:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8e5a7b7-0b39-3a84-8e52-945af5440f56 | -4.83476 | -44.21715 | 2024-12-12 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76db31c8-2776-3eae-adea-afd66266001e | -5.28872 | -44.91122 | 2024-12-12 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1794cf9f-6465-3214-8392-1a100d6b25fc | -7.81912 | -42.97554 | 2024-12-12 04:38:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0034298b-2327-3c63-811d-7cd18257ed9d | -2.58077 | -51.92286 | 2024-12-12 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 774265d4-497f-39c1-b41d-8cc9e1c58d58 | -4.94103 | -44.2789 | 2024-12-12 04:38:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc0637aa-7aac-36a1-ad05-f510b835b88b | -3.98169 | -46.89857 | 2024-12-12 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f86e97c6-b90c-3129-be55-95e0ac456ce8 | -3.24062 | -46.88337 | 2024-12-12 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 030cd8ad-bd7c-3bd2-9669-f0195c31473a | -4.06571 | -47.09726 | 2024-12-12 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6b7e2bc-0a37-3d80-b4e2-d2266f6b9a26 | -3.67667 | -54.30201 | 2024-12-12 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8cf8c46-888b-3a90-8cbc-bf3aca6f471b | -6.9257 | -43.52111 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 0e875ef7-6030-3f7a-9009-98b4f5a30475 | -7.79999 | -46.20791 | 2024-12-12 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2926aadf-eb69-38b4-9bcc-87324226cd4c | -4.0518 | -46.66033 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c5e6c4e7-1bf7-3285-b04a-8dba89ba1e92 | -5.41759 | -46.86416 | 2024-12-12 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1558c10d-4fc2-3ea8-90f4-069c869305f5 | -4.01539 | -46.9679 | 2024-12-12 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 596c8369-54a3-39ee-96b3-3d61ee78e006 | -6.92076 | -43.52467 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 20d7daa9-7756-3044-b40d-a95f312ef227 | -3.891 | -42.54859 | 2024-12-12 04:38:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9a3ef8ff-6563-37d7-a6ce-f21440e4b11c | -3.1256 | -53.09849 | 2024-12-12 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06cc82de-3d82-3bcb-9327-714e3b83941b | -3.99195 | -46.50998 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a6e865c-98d3-328c-9683-3b5a6700663f | -3.01533 | -48.0344 | 2024-12-12 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d90b6cd-a050-31b1-9478-b7aea6c7d470 | -3.78571 | -47.10051 | 2024-12-12 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0aa0bcd-f658-3a3c-8fb2-2973bc50abf2 | -5.90041 | -44.0128 | 2024-12-12 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b25a6b1-4da8-3857-b0a6-39596de7d0b4 | -4.18648 | -42.42466 | 2024-12-12 04:38:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 86b9942f-8ef2-3d97-b661-81147b87674f | -4.08145 | -46.65306 | 2024-12-12 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1fe45e67-1119-3c6c-90f6-70def357d5f9 | -4.64765 | -49.01652 | 2024-12-12 04:38:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| beb6462b-e5d1-3144-a972-f24854751c17 | -2.95537 | -53.1142 | 2024-12-12 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f5db385-1155-3808-866d-841c17a76613 | -6.93064 | -43.51757 | 2024-12-12 04:38:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 7fc1fa3c-5def-31e1-bbeb-207b1d83b732 | -4.17087 | -48.75402 | 2024-12-12 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d8796c4-e54f-34bf-a224-1498c1702e51 | -4.02109 | -46.88465 | 2024-12-12 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f542b4c7-0047-383d-9d2d-cf7986e7c2bb | -6.1233 | -42.54656 | 2024-12-12 04:38:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 985bcbc2-7eaf-3675-a434-e6e16ec750e1 | -4.01883 | -46.96843 | 2024-12-12 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 119960f9-a6b7-35e7-aed2-d8ab7ed58f00 | -7.42461 | -44.7356 | 2024-12-12 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cae8e2b-a7de-32a7-b3c6-82128b78ea9a | -6.14294 | -43.91367 | 2024-12-12 04:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0d5570f-347c-385f-9adf-10e074846dd7 | -3.4299 | -42.98112 | 2024-12-12 04:38:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README23.md)
