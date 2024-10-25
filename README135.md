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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba88f41e-3470-3ea4-ba75-1875603fd9ff | -17.2306 | -57.20742 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.2 |
| 29979d56-346f-3861-9797-aca41dc76d67 | -17.22938 | -57.49464 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 605378c9-58af-366e-a280-a0cfb3a68a52 | -17.22717 | -57.22475 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| 9e03da3d-ffd9-3e38-8129-a164c2bc486a | -17.22606 | -57.21469 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 8a214a19-482b-329b-9783-5617bce0000b | -17.22372 | -57.2421 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| a04eb2e3-ae6e-3b2c-999d-5bb91a3d6851 | -17.21918 | -57.24941 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.0 |
| 91778c9b-3cb7-383d-b0b4-5e67a80dada2 | -17.21845 | -57.24268 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.5 |
| 29b3db74-6694-38a9-98ac-2879a7b9e02f | -17.21808 | -57.23932 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.5 |
| 3e63254f-223f-339d-82ee-e64193ce53e8 | -17.21771 | -57.23597 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.4 |
| 21dfb150-c69f-35fa-9795-2fc3e29fef1d | -17.2139 | -57.25002 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.0 |
| 730c4e3e-4682-36fd-9723-1ba9ce8a7962 | -17.21354 | -57.24665 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.0 |
| f9ab1708-4456-3b46-9842-088640e79b77 | -17.20076 | -57.27362 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.3 |
| b0237255-5e77-360a-afb3-206379ba20c4 | -17.20059 | -57.27538 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.5 |
| aeff017a-b0ca-3b55-bcb6-1c87a262a30f | -17.20037 | -57.27024 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.3 |
| da6fa75d-f819-370b-9bd9-40863ea8c544 | -17.20023 | -57.272 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.8 |
| 79425037-d2a8-36f1-b4ee-34550c12818c | -17.19663 | -57.28431 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 38f9952d-769a-31a4-bd5f-b57890668f42 | -17.19586 | -57.27757 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.2 |
| c3fc29ca-c487-30bf-b80f-68c1725eecbd | -17.19566 | -57.27934 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.5 |
| bf2ea465-9ec4-3a46-853f-b755536aa4e7 | -17.19547 | -57.27419 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.3 |
| b323b69e-4e26-364d-8fa9-4f4f8b653976 | -17.1953 | -57.27597 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.5 |
| 59abb96c-5b8a-38be-9ccd-6fed9194f51a | -17.19109 | -57.28669 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 5ea9a743-1a31-3f54-a172-9b870dd122e7 | -17.19096 | -57.28151 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| f9076c5f-dd9d-3a2d-9a7a-21d23e5bfccf | -17.18682 | -57.29223 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 09813419-c57f-36fe-ac2f-df7d52a64b42 | -17.1858 | -57.28728 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| d32343c8-5f9f-3c15-a446-c464ca7c1935 | -17.18247 | -57.49413 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 12a343d5-6390-3b42-b6dd-ba9809bd5d42 | -17.17786 | -57.45247 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| f9e8e2f7-8705-31ff-987a-bd8b3a1fdcd5 | -17.15916 | -57.43001 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| e0b95b84-8bd4-3218-9c87-efc37a83c51c | -17.08673 | -57.39609 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| d4c41eb2-47c2-31d3-a041-e1d04e8e4e7f | -17.08635 | -57.39267 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| 6275f57c-59d9-392a-9704-ae80a6578ee5 | -17.08141 | -57.39667 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| 28e61a62-14e7-344d-b023-b3784cc475d2 | -17.07725 | -57.40754 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 0374c90c-4649-3872-97ee-1444566b6f21 | -17.04946 | -57.44884 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| e58195ff-c239-34f5-99e2-569189989dfd | -17.04908 | -57.44539 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| c49884f7-9488-3fe3-ba61-0ef66c0a6db9 | -17.03599 | -57.52399 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| f76de120-7993-3f4d-9f79-a3e42a1cb4dc | -17.031 | -57.52807 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 3076be99-4851-38b7-9c88-67e3166e6e71 | -17.03062 | -57.52459 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| d6ac3334-2e36-3042-91a6-e1a4fcf8f398 | -17.01041 | -57.38721 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 07bc4db9-e2c6-3af0-956c-d19625da3c1c | -17.0018 | -57.35722 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.0 |
| c1020c5d-7223-3a7f-9110-b809de2490dc | -16.99997 | -57.34025 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 01e0707b-f8a8-316f-9d6e-15bbec84d3a8 | -16.99961 | -57.33688 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.6 |
| d8c889dc-af6a-332b-8517-41e361cb8aa3 | -16.99893 | -57.37332 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 10c2378c-6cd2-3791-8ae6-69bd9fc21a97 | -16.99851 | -57.32673 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 1e6776c1-0f18-38b3-baa4-55070ec8e37d | -16.99621 | -57.34959 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| 58f25f40-59d5-3b4b-9dd5-e471e3256397 | -16.99577 | -57.35101 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.3 |
| edbcb7ca-f27a-39f3-96dc-60f5b4393c47 | -16.99543 | -57.34284 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.6 |
| 8444ac17-f54f-3b54-8bd0-b134796a66bb | -16.99541 | -57.34763 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.3 |
| 0ed5230f-e8ed-3742-b56b-e3869145dd3b | -16.99504 | -57.34425 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.6 |
| 460b4aa6-968b-3b28-9212-7fea0c787509 | -16.99467 | -57.34085 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.6 |
| 67d46d55-1b65-3814-aeac-3231b7997194 | -16.99401 | -57.37729 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.1 |
| 1e66fbf1-a009-3b7f-8e7b-85bed4b68869 | -16.99338 | -57.37878 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 30d23af8-90ce-309a-86e4-b4c041f30663 | -16.99301 | -57.37538 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 437f7992-bc34-3b9b-815f-8780b99709f4 | -16.99091 | -57.35017 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| 3948d9b6-72f0-3b0d-b74d-f68d1c8964f0 | -16.98909 | -57.38127 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| f2a965c9-aca9-31b7-b7bd-86948537027c | -16.97335 | -57.52919 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| 0b75a9bb-4fa0-33e1-b86f-6c237cb83fb5 | -16.96761 | -57.52629 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| 011f89f5-74a6-34ed-9550-3d52771c5668 | -16.92859 | -57.5165 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 3b802ae0-6e1d-38ee-9d8d-3c419f2b2a94 | -16.90766 | -57.50588 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.0 |
| 716be4a1-49ef-36fd-83f2-cc75afc3e1d6 | -16.90726 | -57.50243 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 6cbd3981-7a54-3d6a-b3ff-0a470ea0d61e | -16.90601 | -57.68337 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| f38e83fa-fe78-3ca0-9ef7-3ae34df04680 | -16.9057 | -57.505 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.3 |
| 6a3a20c7-78bc-395b-b2a3-cd13e14a7ce2 | -16.89171 | -57.276 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 434ade89-f319-367d-8dae-45abafc2c3bd | -16.8828 | -57.6715 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 23c06ece-1659-306d-adab-123ae45cd62f | -16.79497 | -57.41417 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.9 |
| e2c02386-b28c-3463-bcc3-b0deb37a1f96 | -16.79127 | -57.42183 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 74f7dd20-9cf8-3ce9-a9d5-7d265cd96108 | -17.89579 | -57.55479 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.6 |
| bfaa5b2a-b0cb-3429-a2b2-153adad53622 | -17.89546 | -57.55165 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.6 |
| f268e335-b8c2-3202-a634-f02ed02f08e3 | -17.89333 | -57.53142 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 3a8a291c-e17b-366b-baa6-e26daf5abc53 | -17.8926 | -57.52449 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| ac7430a2-89eb-3b82-a2f1-f76ceb4d62e6 | -17.88764 | -57.52948 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.7 |
| dfa41437-84e1-3ab2-8cb0-2b0652b304d3 | -17.88729 | -57.52614 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.3 |
| 510eee65-fe07-3dc4-bc00-d55d70c30ce1 | -17.88694 | -57.52272 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.3 |
| c48a912d-1ab7-3976-826a-afa50df66fd2 | -17.88599 | -57.56612 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 59791050-88e3-3229-b6a4-79b2fed1bd40 | -17.88573 | -57.56356 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.9 |
| 057b1f1d-7cec-3355-8b0d-9717c4356722 | -17.88542 | -57.56066 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.9 |
| bf32f183-54e2-31f1-9dee-31951c9c85e0 | -17.88232 | -57.53097 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.7 |
| 76227e4d-f723-3e00-a8dc-6226622a1859 | -17.88199 | -57.52783 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.3 |
| c5d2d367-a815-3fbd-aa56-35b06e836876 | -17.88194 | -57.22136 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 4eac4f20-d09c-3ae1-acbc-6d19aa96cff3 | -17.88162 | -57.52432 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.3 |
| 6f6fb5db-33f6-3b2b-8ec1-1b02be199471 | -17.88126 | -57.52087 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 33.7 |
| 1338c16e-87e7-32c6-af5b-01cde30a5edd | -17.88033 | -57.56453 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.7 |
| 65ea0672-b454-3c3a-abce-59ec0d9a5dfc | -17.87663 | -57.52905 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 749d4db4-fc30-3255-a863-537221a3ea7c | -17.87663 | -57.22193 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 87bedfcd-2513-3967-9ae7-3813066603f3 | -17.87629 | -57.5257 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 9b4efdf0-ff86-354c-9e58-14ba87e537cc | -17.87593 | -57.52226 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| b9953e82-9513-3ff6-872c-6348bdeaafda | -17.87525 | -57.5685 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 85d2ea2b-6785-379b-bdb3-a2c268de544c | -17.87495 | -57.56565 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.7 |
| 388f6b57-bf61-313d-9cef-3f8956090897 | -17.87464 | -57.56266 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.7 |
| d82c09cf-e942-3bed-8dc2-4c6980b77739 | -17.87366 | -57.57306 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.8 |
| 02a9fd5d-bd68-397e-a845-641c8954cf42 | -17.87334 | -57.57016 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.8 |
| 6cf5f5ae-8f27-37d1-8d69-479347a8756e | -17.87302 | -57.56724 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.7 |
| 4b57faa5-61d4-37d4-a1ae-017708a863a6 | -17.87182 | -57.53553 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 7ac0c13e-c8a4-322f-a89c-deb1bd8ba650 | -17.8709 | -57.52663 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 3cb4eed1-9cef-3d44-85c5-48db7366051d | -17.87057 | -57.52343 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| f2e94710-dc47-3c25-a9d7-1153c43561a9 | -17.87019 | -57.57271 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 75e51e7f-ae4c-3227-a48a-0b8bad3b3bdb | -17.86989 | -57.56983 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 8431f8d6-7fdd-348f-aac4-d64c8ba497d6 | -17.86835 | -57.52512 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.8 |
| 9f185d77-811f-346b-af2f-222da11a0f97 | -17.86799 | -57.57144 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.8 |
| 47045ff8-8a90-3259-8f22-cd7cdf41db15 | -17.86584 | -57.53064 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 6a80a9d8-4491-3f70-8c97-1bb5ce52efd9 | -17.86552 | -57.52758 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 09a4578e-17bb-386c-8a51-4b21d9106c88 | -17.86518 | -57.52432 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |


[Clique aqui para ver as próximas entradas](README136.md)
