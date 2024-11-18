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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0520fef-a5be-3c5e-a93e-f1b055768bf8 | -6.02422 | -35.33355 | 2024-11-18 03:46:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 49785de0-de72-3bee-81f1-e86db3bcbc1b | -3.57538 | -45.20552 | 2024-11-18 03:46:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fd53c5c-436b-3e57-bd52-ec4c75c45b2e | -9.29922 | -46.20882 | 2024-11-18 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6677ab38-5727-38c5-b183-0ae9313adfa4 | -3.16566 | -46.59787 | 2024-11-18 03:46:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8fb4ea16-1a50-304d-bb86-06f74b59317c | -11.119 | -45.2918 | 2024-11-18 03:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f52342b-231b-3703-9c63-d23dc464a56a | -10.43704 | -44.88783 | 2024-11-18 03:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a4a2736f-6c1c-3d4d-a2a9-c55a76b9d1d5 | -3.29775 | -45.67685 | 2024-11-18 03:46:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7f979713-ba85-3051-a71e-02a514dca661 | -2.96087 | -48.00436 | 2024-11-18 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 70d7f8a0-48e6-375a-804d-f75211dd897d | -3.22907 | -45.5533 | 2024-11-18 03:46:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 822ddb0e-defd-39d4-aa7a-f571062d8cb2 | -8.27445 | -45.9544 | 2024-11-18 03:46:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4115c9fd-415c-3734-8d82-b570ba7f963a | -4.95252 | -44.84638 | 2024-11-18 03:46:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 138b0dc9-fdb7-3ed0-aca8-f50c96d8d195 | -4.94738 | -44.84554 | 2024-11-18 03:46:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba412a72-f27e-353b-b73a-0194bd9b03ab | -8.29393 | -40.84341 | 2024-11-18 03:46:00 | NPP-375D | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 949eae9a-78f2-3bda-acf5-f357a5f4d175 | -1.75583 | -45.69149 | 2024-11-18 03:46:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91ef2205-4616-36f0-a10a-ce90df7ac7d2 | -10.87396 | -43.36852 | 2024-11-18 03:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e16f2439-27ec-3715-a422-9248e776f42d | -2.95996 | -48.00975 | 2024-11-18 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 88a64e03-39ed-3b93-8266-f729ab3e7aae | -1.8087 | -46.53418 | 2024-11-18 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9fa4813d-80ee-369d-9431-b764c2c5178e | -3.76198 | -45.94354 | 2024-11-18 03:46:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a1e183b-7545-3b64-984e-59fd52c9a2d2 | -5.51851 | -41.06477 | 2024-11-18 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 748e5050-eeb6-3738-abc8-eca12356605c | -4.81988 | -44.48569 | 2024-11-18 03:46:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9de025c0-6b7a-38e3-a462-43fdbc31aad8 | -5.51373 | -41.06926 | 2024-11-18 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 18771ced-6150-39c9-b5b4-5f7af43926c4 | -3.76495 | -45.94331 | 2024-11-18 03:46:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4df25697-a98e-3763-8bba-0cbc42388b64 | -10.44174 | -44.8886 | 2024-11-18 03:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c82c237f-40e0-3d94-9cca-55c41c861c41 | -2.96014 | -48.00599 | 2024-11-18 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ed8e89dd-a877-3a7b-80ce-6e9bc95cde2d | -7.71303 | -45.66542 | 2024-11-18 03:46:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7b1e0141-3ed5-31ff-be7d-a6307cbd507c | -1.70322 | -45.83432 | 2024-11-18 03:46:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 3b0179ad-0cd1-3063-8caa-1289a2a746f4 | -4.82037 | -44.48277 | 2024-11-18 03:46:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eace3c44-30fe-3351-acd7-c991563f8524 | -3.32858 | -46.01407 | 2024-11-18 03:46:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6debbd93-c256-3b01-a750-0c9d5a46ad08 | -4.95306 | -44.84322 | 2024-11-18 03:46:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c720760-def1-3255-9376-aae64722ec3a | -4.81124 | -42.20939 | 2024-11-18 03:46:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c1641e4d-1593-3333-8e5e-dffe752fe87c | -3.75866 | -45.94614 | 2024-11-18 03:46:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0b52238-5dda-37ab-92d2-9e9bd1b1c0ba | -3.3296 | -46.01746 | 2024-11-18 03:46:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30979980-3de9-30ee-a78d-e2163f3492f4 | -11.76998 | -40.90685 | 2024-11-18 03:46:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1bcb9350-f6dc-38b7-bdaa-952d3706898a | -4.91186 | -44.02922 | 2024-11-18 03:46:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| ad83a4ef-fbd5-3503-8a71-e29bcec030c8 | -1.81474 | -46.53519 | 2024-11-18 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3a752c5e-b5de-312b-a959-f7129b8085c0 | -2.3373 | -49.14165 | 2024-11-18 03:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 98f09b90-19ea-35c3-be92-33572c6f974e | -3.56941 | -45.20802 | 2024-11-18 03:46:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1f5d446-45a7-3159-afa1-708956a844d7 | -2.82812 | -46.66696 | 2024-11-18 03:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de0fe828-a594-3f0e-96fd-08ebbd801476 | -3.29838 | -45.67317 | 2024-11-18 03:46:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 327f5d4d-0f26-3124-a16a-f9ee7bbbd91f | -4.58689 | -44.22976 | 2024-11-18 03:46:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 597eecc6-5b39-3f0d-b37f-29d526a78175 | -11.16318 | -45.10435 | 2024-11-18 03:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 622eac4f-ecae-39fc-91f6-2f5f0fec8bad | -4.95198 | -44.84956 | 2024-11-18 03:46:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5826bf98-af2b-3577-9e39-a580b4480e64 | -4.59185 | -44.23058 | 2024-11-18 03:46:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b72ea48-8b9f-328e-b4b1-5660d1c3a36c | -3.95148 | -46.41247 | 2024-11-18 03:46:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 314822e7-07f0-3809-a623-cf880d733d40 | -4.58683 | -44.22906 | 2024-11-18 03:46:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48fcf224-6bf8-35ac-8ce5-3468c2b0b6d3 | -3.29713 | -45.68055 | 2024-11-18 03:46:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 59bece1c-4dae-3091-a6c5-03d426ee0292 | -11.15849 | -45.10345 | 2024-11-18 03:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e565940-018b-3456-ac1f-4c32f73dee74 | -2.82738 | -46.67138 | 2024-11-18 03:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d200f43-b7cd-3f71-99b2-3a27cfb1ef81 | -2.83338 | -46.67239 | 2024-11-18 03:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28b99e17-dc60-344d-9f41-b864dc081e3f | -4.8002 | -37.38776 | 2024-11-18 03:46:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| add052bf-5981-3542-a38d-86e3890a7574 | -2.34059 | -49.13501 | 2024-11-18 03:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a817ab51-49d8-30c5-9f5c-e6373e5877fb | -2.55167 | -47.29221 | 2024-11-18 03:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5575cc48-174e-3670-852c-70128da48a11 | -1.71031 | -45.82719 | 2024-11-18 03:46:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 76ae4cda-cf4a-3a77-a1ef-6eb0aa7fa2a5 | -4.95346 | -44.50879 | 2024-11-18 03:46:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fcc40e11-61c3-33a4-a82d-fb6bc808bc83 | -9.29862 | -46.21206 | 2024-11-18 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac914f8f-2953-3e2d-abab-eeb3a654303f | -2.85807 | -46.6722 | 2024-11-18 03:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 558653e7-e1e1-3b85-8444-6b98112de073 | -4.81055 | -42.21344 | 2024-11-18 03:46:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cae274ab-01dd-3ec3-93e8-3b4b62d99c96 | -2.83412 | -46.66798 | 2024-11-18 03:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b09fba4a-fe38-300b-b560-a9076751c59b | -3.30336 | -45.67767 | 2024-11-18 03:46:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 5d483699-b24b-3d38-95fe-96f25152100f | -4.90219 | -44.02723 | 2024-11-18 03:46:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1547e168-a377-39af-8bb3-b70555caf3de | -3.75571 | -45.94641 | 2024-11-18 03:46:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf7efd2d-d505-33a3-a5f2-6b69b6c92e77 | -3.17088 | -46.60317 | 2024-11-18 03:46:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 61f159a0-2350-3663-85fc-e54311277416 | -4.82081 | -40.31477 | 2024-11-18 03:46:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 23e18a79-dea0-34ce-ac3b-adf36f5bf1cf | -2.59909 | -48.30706 | 2024-11-18 03:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c4dfc0f3-e90a-30ed-a4d5-d66b3cf09053 | -3.31363 | -46.04203 | 2024-11-18 03:46:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b167e187-ede1-37db-a5db-5079d89ced9a | -3.758 | -45.94995 | 2024-11-18 03:46:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e968f7e-b9ee-3c44-a24a-fc883410e9d0 | -3.76072 | -45.95117 | 2024-11-18 03:46:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 035fe76f-5380-3096-8fe5-138e3306c1a4 | -8.27387 | -45.95753 | 2024-11-18 03:46:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5156eaae-f68c-30c8-a9e1-c9f82f33a86d | -3.31212 | -46.0428 | 2024-11-18 03:46:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8eb75c0-2f14-3a66-a03b-7741bb93318b | -9.29802 | -46.21529 | 2024-11-18 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01ac25ca-d76d-3be4-8413-bb33af31aba9 | -2.33945 | -49.14183 | 2024-11-18 03:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9114f752-d3c6-3338-879d-c33adfd2a63e | -1.76156 | -45.69245 | 2024-11-18 03:46:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54885286-5118-33b0-8f1b-0a282b1d5514 | -9.63156 | -45.21336 | 2024-11-18 03:46:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4b2a0da1-75bd-3e19-922d-440b3cf49a63 | -3.89714 | -46.62474 | 2024-11-18 03:46:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cc1bd7c-7ee5-33e3-b726-b2300d769bca | -4.95481 | -44.50847 | 2024-11-18 03:46:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee696213-d75b-35c3-8075-9eda7ed231d4 | -3.07498 | -48.07108 | 2024-11-18 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e3f42c9-10e9-36e3-aa9d-0d5a5c123b6f | -11.12378 | -45.29261 | 2024-11-18 03:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 421d722b-d8cc-3ea0-8c02-84baefbe781b | -3.57421 | -45.21236 | 2024-11-18 03:46:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b6585e3-b683-374e-b1a1-1cae6d646af5 | -10.51865 | -36.7389 | 2024-11-18 03:46:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5e8c3696-0e49-312a-8919-da2514e882f3 | -3.17753 | -46.59993 | 2024-11-18 03:46:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 513d6b36-df2c-352f-a752-82fd8c591325 | -9.08475 | -40.52057 | 2024-11-18 03:46:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6069e2e7-686a-3ac0-b8e2-f0b464fca60a | -2.67766 | -46.21935 | 2024-11-18 03:46:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| faabf8dd-d062-3851-8204-48f48f34b525 | -3.1859 | -45.44091 | 2024-11-18 03:46:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 638e28c3-3241-3805-8889-490715e287c3 | -3.17233 | -46.59452 | 2024-11-18 03:46:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 34430e50-dd74-3a41-86fb-b967c57d4078 | -3.14421 | -45.98832 | 2024-11-18 03:46:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 207d5b11-168f-3d18-9980-205f60441ea5 | -3.20969 | -46.68019 | 2024-11-18 03:46:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c854465b-90fb-337a-a29a-c7e79c9580e8 | -2.62408 | -46.83583 | 2024-11-18 03:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6896b0f-f001-359d-9f27-fdbf82450372 | -4.9953 | -44.32787 | 2024-11-18 03:46:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5d38692-96af-3bfe-aae5-a7eb5685a43b | -1.76251 | -45.69108 | 2024-11-18 03:46:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cfa9ff7-5691-31cd-95f8-ad46351a85dc | -3.26498 | -39.26609 | 2024-11-18 03:46:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b9173125-fbae-33be-b6d2-0d21d1789e5f | -2.86405 | -46.6733 | 2024-11-18 03:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b16705fb-6b23-35da-a92d-657036b0c83a | -10.87461 | -43.36477 | 2024-11-18 03:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 14c05641-c618-3f7c-8c23-3ff6fe99d877 | -3.92002 | -46.52653 | 2024-11-18 03:46:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 109b605d-e21a-3f4b-bbe9-1fffc0e13941 | -4.36373 | -45.87657 | 2024-11-18 03:46:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4ada2190-ed37-37dd-9a54-092609d068f2 | -2.62414 | -46.83463 | 2024-11-18 03:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afe5cc64-2618-3215-ac35-e844f5f6ae1a | -9.30318 | -46.21659 | 2024-11-18 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37f50634-5242-3e87-a3f0-100007ed7946 | -9.29827 | -46.21496 | 2024-11-18 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 261705cf-3837-3ee3-967b-2e8fcf515357 | -3.32795 | -46.01796 | 2024-11-18 03:46:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be94a14e-1b80-30d9-a859-4a7290944d34 | -9.30564 | -46.20339 | 2024-11-18 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b456d5e-25e0-3956-9989-6274936ac8ba | -1.70454 | -45.82615 | 2024-11-18 03:46:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |


[Clique aqui para ver as próximas entradas](README16.md)
