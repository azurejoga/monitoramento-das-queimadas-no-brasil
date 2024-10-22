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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7d066be-9ecc-37e9-9b77-e10d50fe9a4d | -3.94831 | -41.49881 | 2024-10-22 03:51:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 27b0897a-ff8e-3ead-93af-44d9ccd426e3 | -3.75617 | -42.31858 | 2024-10-22 03:51:00 | NPP-375D | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 70c5d75c-e23c-373f-ad93-81f2cd6e97ea | -3.5244 | -43.61446 | 2024-10-22 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9169dac2-e9f5-39f5-850e-0f6a22977b07 | -3.52402 | -43.61092 | 2024-10-22 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3b97a9e-96b6-31f4-b26c-cd75aba932fd | -3.52337 | -43.61504 | 2024-10-22 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5b37b052-fef0-3c92-8b34-3211e586dcef | -3.52008 | -43.61375 | 2024-10-22 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 45fbb7d4-3b3f-3e0e-a8a5-7b9fd686d0a8 | -3.51904 | -43.61433 | 2024-10-22 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 06481ad1-6603-3a0b-b1ed-6d38f983e408 | -3.45144 | -44.27229 | 2024-10-22 03:51:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 908c857c-f441-35af-a0d2-29a0fa0aaf90 | -3.3142 | -44.14447 | 2024-10-22 03:51:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98fefe8e-2024-3217-8c4c-8771327a017c | -3.31344 | -44.14894 | 2024-10-22 03:51:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5bad92d9-7180-3eb0-89f6-875f73cd097a | -3.31226 | -44.14634 | 2024-10-22 03:51:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1c07bcda-58e7-3500-ab93-21cc47f9aaca | -3.89253 | -43.13941 | 2024-10-22 03:51:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce6d8782-cd3d-3207-9e0c-7abcadafbd85 | -3.77379 | -43.2345 | 2024-10-22 03:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bab4871-e934-3aff-b8fa-4caf3755c78a | -3.75847 | -44.40049 | 2024-10-22 03:51:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2b00348-953d-3a12-9c3b-562c544cf334 | -3.16306 | -45.64331 | 2024-10-22 03:51:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b1026f4-37d2-3422-9073-198645683aad | -3.0665 | -45.32774 | 2024-10-22 03:51:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bb61871-46db-3f53-bcf8-bdeca5070487 | -2.9934 | -45.61388 | 2024-10-22 03:51:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 69c308a7-d3ad-3028-953f-93378aa21570 | -2.98937 | -45.61254 | 2024-10-22 03:51:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c6c2c71f-c8b9-37e7-81fa-1290d7043a78 | -2.98839 | -45.61306 | 2024-10-22 03:51:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2a677df7-7132-379d-9227-a08d0fea99f2 | -2.98742 | -45.6188 | 2024-10-22 03:51:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 420e3e18-6b19-376d-b6ce-e1531ab0f3df | -2.98436 | -45.6117 | 2024-10-22 03:51:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d85688dd-bfcf-3daa-b915-68b581abdcef | -2.98344 | -45.61743 | 2024-10-22 03:51:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6c9b696e-4d4f-318d-b493-a9a5ac3572f1 | -2.98338 | -45.61223 | 2024-10-22 03:51:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| fe2ee797-c8d2-3d8f-8be8-30b8fe040eda | -2.98242 | -45.61795 | 2024-10-22 03:51:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3e5fcfbd-3b19-39b4-8c0b-8a074ccfca9d | -2.85911 | -45.46724 | 2024-10-22 03:51:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a4b81b2-8438-3d71-bf6e-69c41014d57b | -2.85507 | -45.46075 | 2024-10-22 03:51:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| af00d002-871c-35a7-b613-c87145f74e27 | -2.85414 | -45.4664 | 2024-10-22 03:51:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 6d54c763-1a9d-31b0-aab6-de8b698df9d1 | -1.77305 | -46.31725 | 2024-10-22 03:51:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc06d972-05d5-357f-a334-da7d997b5e4f | -1.11592 | -46.8335 | 2024-10-22 03:51:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b6e6f67-94d7-3abc-bbfd-5ee8945e0859 | -1.11032 | -46.83258 | 2024-10-22 03:51:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16df1c49-d75a-3a9e-a651-cf235fa5dd5a | -2.56931 | -45.99437 | 2024-10-22 03:51:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a4acdae-8d08-3694-a943-3d4635d7af50 | -2.56413 | -45.99355 | 2024-10-22 03:51:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 619b549b-e7d1-385d-af52-b7899799873f | -2.56364 | -45.9966 | 2024-10-22 03:51:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f5b8ce9-4781-3efc-ab15-bbd7cb513bb3 | -2.55896 | -45.99267 | 2024-10-22 03:51:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05018ae6-ebc8-3a20-b78a-80f05e3384ed | -2.53723 | -45.99546 | 2024-10-22 03:51:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b859546-deb8-3feb-b6fc-60a52b63a986 | -2.53205 | -45.99461 | 2024-10-22 03:51:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7f4d7e0-9abf-3df4-a467-0708a57b2fb7 | -2.20866 | -46.48922 | 2024-10-22 03:51:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3e66f27-f546-39cd-9a56-102ebc3d57d4 | -2.20328 | -46.48833 | 2024-10-22 03:51:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 427cbc09-9935-3769-88a3-c009075d5bf0 | -1.98024 | -48.68821 | 2024-10-22 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5021e991-d2f4-33ee-8ea5-41edd511f01b | -1.97481 | -48.68237 | 2024-10-22 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73843166-ff67-3cee-b212-736f1a77df0b | -1.97402 | -48.68714 | 2024-10-22 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 647cd8e1-bfc3-3743-b59a-c5d0776ae2aa | -2.96552 | -48.00424 | 2024-10-22 03:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34600c15-a999-3737-b011-2b6eabf2ae3f | -2.96482 | -48.00842 | 2024-10-22 03:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e38d1024-6b49-3fe3-be84-f81209b4a98e | -2.95965 | -48.00323 | 2024-10-22 03:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e68b398-7423-32a8-bdb1-4f74ef0088de | -2.92489 | -48.95841 | 2024-10-22 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 79fdee4a-2237-31af-8fa9-c28155541812 | -2.91865 | -48.95733 | 2024-10-22 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ee146c4-0d29-39a5-ae5b-f5eb422c1b01 | -2.63639 | -48.43639 | 2024-10-22 03:51:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4571a67-9fd1-3448-b68e-a16ed06a48d5 | -2.63563 | -48.4409 | 2024-10-22 03:51:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89d2fe68-09d1-3d28-8433-5b541f905ef4 | -2.63486 | -48.44545 | 2024-10-22 03:51:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c71102f-a3d9-375a-93fc-86ef749ceb6b | -2.62957 | -48.43978 | 2024-10-22 03:51:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed01d57e-42f7-3988-9a06-0d2983f1818f | 0.8887 | -50.68081 | 2024-10-22 03:51:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94852c86-58f2-3228-86f3-277028af495f | 0.88753 | -50.67339 | 2024-10-22 03:51:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 658142aa-5b01-39e2-a62a-744536c54536 | -5.24362 | -35.55442 | 2024-10-22 03:51:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 250f92ef-5663-3fe4-8a8e-88dc1c4fc015 | -5.24012 | -35.55388 | 2024-10-22 03:51:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 13.2 |
| af24d7e6-8003-324f-be7a-198a71cc712b | -4.7188 | -38.85939 | 2024-10-22 03:51:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 06fd1af4-2264-3368-b23d-4a90e0986283 | -4.62335 | -39.67101 | 2024-10-22 03:51:00 | NPP-375D | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5f89bcb5-3166-3acf-b8e6-86e9d4802079 | -3.44577 | -41.26223 | 2024-10-22 03:51:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5a1648a3-7c95-3c29-a44c-047a91fde83e | -3.44203 | -41.2617 | 2024-10-22 03:51:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 438909be-bb04-31c3-9c1b-88891d897a92 | -4.33428 | -40.1883 | 2024-10-22 03:51:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1d591845-15df-3303-b363-10cd0b6f74d1 | -4.00371 | -40.38367 | 2024-10-22 03:51:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cfaedd44-54f6-3957-9920-d1cf94042655 | -3.99953 | -40.38708 | 2024-10-22 03:51:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ac3f8621-be37-3bbf-9a8b-305dc82b31f8 | -3.77646 | -40.98577 | 2024-10-22 03:51:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c88bcbad-911f-334f-bd5a-623b166a7a07 | -4.93747 | -43.0177 | 2024-10-22 03:53:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38089b75-66f5-319e-9fdf-d58118622cf2 | -4.93688 | -43.02127 | 2024-10-22 03:53:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25840da3-9f42-356f-9dce-107eddc87ec2 | -4.93341 | -43.01704 | 2024-10-22 03:53:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d70b0851-dd23-30ba-b752-e5cb15ceef41 | -4.91776 | -43.21182 | 2024-10-22 03:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| caca8e99-33fe-3769-8d93-564cbb533fe8 | -4.46815 | -42.89361 | 2024-10-22 03:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35e74104-cc86-3785-b790-c3b8d44c8698 | -4.46758 | -42.89717 | 2024-10-22 03:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a9528ed-761e-3fe7-ad24-763cba251b51 | -4.46642 | -42.90428 | 2024-10-22 03:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d4e87a42-b555-344b-9d38-f3c14145c974 | -4.46585 | -42.9078 | 2024-10-22 03:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d073d460-5f26-3591-a152-f9ab7de17fcc | -4.46293 | -42.90006 | 2024-10-22 03:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 46cb6a4f-3181-3730-8bb8-76629d11469e | -4.46235 | -42.90361 | 2024-10-22 03:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6567aa37-1dc9-3e52-8442-e90b1e8b8ad9 | -4.46178 | -42.90715 | 2024-10-22 03:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d126862d-1122-30bf-bb73-3f29ec39a763 | -4.37677 | -43.01543 | 2024-10-22 03:53:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb73a84e-cbb9-3946-a3a9-5c41258f1b4f | -4.37617 | -43.01901 | 2024-10-22 03:53:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 148a23ca-1d3c-3018-9cb2-d92a51e84e7a | -4.36917 | -43.01052 | 2024-10-22 03:53:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb9c828b-2101-3c6b-9bfc-0190b7aff26f | -4.36856 | -43.01416 | 2024-10-22 03:53:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 262eb4a2-e5a6-3a72-aa34-17fbeda42d74 | -4.17848 | -42.98407 | 2024-10-22 03:53:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61a86639-c947-3520-80f1-0b857bd504e1 | -4.17437 | -42.98338 | 2024-10-22 03:53:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0bcc248-b6c1-3394-8465-ede1a10d6deb | -5.05368 | -41.94918 | 2024-10-22 03:53:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5f4c2803-032b-3b9f-b5ef-f851b6f00086 | -4.92652 | -41.96899 | 2024-10-22 03:53:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 03926a48-fd19-36e1-802f-76d4a645bdc7 | -4.92271 | -41.9684 | 2024-10-22 03:53:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3d35d929-1a48-303e-9e94-7110f1d49d1b | -4.92195 | -41.97305 | 2024-10-22 03:53:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f514d19b-bac3-3eaf-890e-d3257e7f1c34 | -4.6264 | -42.38446 | 2024-10-22 03:53:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e39eb7fc-0eb4-374d-8461-923f29c94e68 | -4.62247 | -42.38384 | 2024-10-22 03:53:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 02d4744e-5e20-38fa-b101-e7abc85c73af | -4.61855 | -42.38319 | 2024-10-22 03:53:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a327031c-8437-3cf4-9cee-21e2de55c256 | -5.23416 | -43.18469 | 2024-10-22 03:53:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cddeb355-5c18-36ee-9db1-57f23c913e69 | -5.23355 | -43.18831 | 2024-10-22 03:53:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 39e2ff83-8396-34f7-9e4c-da6434c703c6 | -5.23127 | -43.17682 | 2024-10-22 03:53:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be64af35-b625-329c-aa57-a3d06d6dd5d7 | -5.23067 | -43.18039 | 2024-10-22 03:53:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 363fd619-b4c5-3865-a8a8-18472e286f2e | -5.23007 | -43.18398 | 2024-10-22 03:53:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c5ff9f95-2178-3519-a493-59f1982d6a34 | -5.22947 | -43.18759 | 2024-10-22 03:53:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f3516e0d-5d44-3a1a-90d0-46a27a25b638 | -5.22719 | -43.17612 | 2024-10-22 03:53:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb24e276-8b58-3fa6-9da5-4ed1f0fda1b0 | -5.22658 | -43.17971 | 2024-10-22 03:53:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a366eda-d824-392f-8732-451d2e34c2e4 | -5.22598 | -43.18331 | 2024-10-22 03:53:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 28594eb4-2d97-31ad-8dbd-cf8324a2c295 | -5.22537 | -43.18691 | 2024-10-22 03:53:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| faf91076-8dda-3f9d-971a-c8578809288e | -5.0974 | -43.11073 | 2024-10-22 03:53:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1733b06-8060-3dee-a93e-ffd09ffdf073 | -5.09332 | -43.11004 | 2024-10-22 03:53:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd7a80f7-8485-362b-ab3c-6a3c7f67d1d1 | -6.28924 | -42.64692 | 2024-10-22 03:53:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a1135d8f-22f2-3efd-bff2-3b2f9df7ea1f | -5.70225 | -43.14431 | 2024-10-22 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README15.md)
