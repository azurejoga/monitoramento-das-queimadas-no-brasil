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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb2b4355-da78-3822-9132-20126be44d32 | -9.44917 | -68.93076 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9c8cc978-4c5c-3f3b-96a5-d60877340511 | -9.42562 | -68.57999 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1badda87-7da6-374f-9644-80268cdfd0b8 | -9.4026 | -68.29212 | 2024-10-17 05:53:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d35d2f5e-f3d2-36aa-8196-5b7bc7e7281e | -9.39991 | -68.6798 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b940b9e2-cb00-3214-9ed3-b106b9cad96a | -9.3954 | -68.29461 | 2024-10-17 05:53:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 925c9f45-e997-353a-88e3-841812ca7e5d | -10.07387 | -68.36063 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77055972-4698-3fe5-b1ad-7c64b494bd57 | -10.01627 | -68.38442 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18a53929-6bd7-3848-a43b-b60a863d4d88 | -10.60004 | -67.87079 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c2103843-ed88-327d-9720-b5a8879aef45 | -10.48179 | -67.91262 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11691dc5-eedc-3c00-8d2a-d41e9eb78d1a | -10.47443 | -67.89281 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 070d3f35-420e-3587-a078-a7c04f4c0b05 | -10.46824 | -67.88808 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03f0d61f-d598-3ff7-88a8-6d50ce12311a | -10.46768 | -67.89175 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85f075f6-bd42-3550-8490-c01e0548aa7a | -10.46204 | -67.88338 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ea97b29-be97-3e88-b875-31262b86a120 | -10.46149 | -67.88704 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1028ca76-55b5-3f71-bf38-90f2604c258b | -10.42559 | -67.90818 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e8ffb5c-89c2-3f81-b86e-d8e635fd6deb | -10.42333 | -67.90037 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3dad253f-925c-34a5-8123-f0558d0cde3c | -10.40988 | -67.9206 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 177d4dcc-5ed5-3977-be1c-1894ff32f69f | -10.40651 | -67.92008 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efabf97f-b997-3ab1-90ef-796e5f568270 | -10.39312 | -67.96264 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3256d54e-4374-3db9-81fc-14dcd704107f | -10.38919 | -67.96576 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36be2c82-e3b9-3ade-8ca0-e39c29a9c21e | -10.3885 | -67.90239 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d929f10e-7828-3706-8ec3-bd81ef543a44 | -10.38568 | -67.89822 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4645e14e-6c77-3c33-a52c-b5590c0ed2c3 | -10.38513 | -67.90186 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29dd67a4-4717-399e-8f51-f6dac3b398dd | -10.37507 | -67.92262 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1234c520-519f-3216-b759-0542fe8b3876 | -10.3712 | -67.94811 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82b09968-1a65-3da0-a82c-09be3144cb55 | -10.37065 | -67.95176 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bfb93db-53c6-3709-859d-101d87159f9b | -10.36999 | -67.91067 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| df11138d-3f67-3b79-9344-0b61c65dad5f | -10.36783 | -67.94759 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc0477fb-4567-36cc-9e27-ad524ebc00a6 | -10.36728 | -67.95123 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ae226c2-4b55-3241-8278-9079629f0c55 | -10.36673 | -67.95487 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20cca1b9-55be-3394-b537-5e23cd0a783a | -10.36336 | -67.95434 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab68ccca-9c98-3373-a7b1-0152a9110f6a | -10.35828 | -67.94239 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c72fd6e-78f3-3564-8972-320f89f9e56e | -10.35773 | -67.94602 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c534909-9dc6-3208-8476-23a63463f900 | -10.35608 | -67.95691 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37675f5c-3d54-3914-b1ff-5647a83818a3 | -10.35491 | -67.94186 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ffe219bd-37f7-345e-a220-737b7d3dcb56 | -10.35449 | -67.99004 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75ef36f1-57b8-35a1-8606-7d2de34f37bd | -10.35436 | -67.9455 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d40a3e6-c953-3fbf-b5c6-29702e7629f5 | -10.35381 | -67.94912 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6acf789-c0ed-351b-a2ce-963d6b2c7a31 | -10.35326 | -67.95275 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77d7ea73-33c8-32fe-a294-6ebeb83a4cf2 | -10.35271 | -67.95639 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9325d724-7dc4-3b51-8849-15cc4ec2d170 | -10.35223 | -67.98227 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23798ecf-6bdc-3e2f-a0f4-1b19e20f64be | -10.35168 | -67.98589 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e27e6a6-73e7-3282-bcdc-76171aa11bb4 | -10.35113 | -67.98951 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6671c0c0-d0d3-3f5c-966c-44f1f3ae8da2 | -10.35058 | -67.99313 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00d12ee0-d395-33e2-816a-665557483bef | -10.34935 | -67.95586 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9177632-05d8-3137-ac34-3c4c87769f00 | -10.34832 | -67.98536 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5d404c3-cd0e-39a7-bdab-7af58d4c94ac | -10.34777 | -67.98898 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 766ff27e-a054-3ce8-abd4-c48f11efe1b1 | -10.34722 | -67.99261 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9467199f-89d2-3093-984b-456092a3a6e1 | -10.34598 | -67.95533 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40abcc74-ea7e-394a-8426-d31b34d053a4 | -10.3444 | -67.98846 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80e74a20-0e8d-38b5-bf3c-63db29444a59 | -10.34385 | -67.99207 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21301df3-b7ba-321f-a8df-a3ce3d75fa78 | -10.33703 | -67.95794 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a8e8c30-fbac-3f7c-9146-a9f6716b6e92 | -10.33366 | -67.95741 | 2024-10-17 05:53:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| edd01980-e5bf-3c5a-8c43-67b8461bffef | -10.30516 | -68.03078 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9048cc7-4a61-3f8e-82f6-652d898b5539 | -9.76677 | -68.80994 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ad677e94-d152-31ea-b8a9-290b583781dc | -9.68462 | -68.59589 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6463176-6e43-3dfc-a706-b7aaae0280d3 | -9.68181 | -68.5703 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15c191b5-0349-3590-b53e-a1bde1ada072 | -9.67849 | -68.56978 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77ede3b1-5de8-378b-bd40-f0add1e37ae5 | -9.67794 | -68.57329 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1da964b3-39f4-3ee3-9828-c365a9b31a53 | -9.67135 | -68.5938 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35fda5ac-cf9b-3a34-a95d-b5d579ddc4cd | -9.66858 | -68.58978 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9ed6729-eaed-37eb-a1be-1e986c1d916a | -9.66527 | -68.58924 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b8d5a2b-d1d2-3f52-9066-39000359f048 | -9.66082 | -68.57417 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25abe330-f11f-3e22-a870-ed013dff4cb8 | -9.65681 | -68.5124 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06715d2f-58ff-33ef-acd6-f1c35b5258ad | -9.65473 | -68.56962 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d80ba22-def7-3d51-a467-1bbfff17a6e1 | -9.65141 | -68.56909 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 43bc0ba6-d8ce-39f3-84b8-ac52296c772f | -9.65087 | -68.57261 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 294a9d05-e1b1-3435-8c77-cdc4a2bf4e6e | -9.64873 | -68.60819 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52ed5262-358e-3645-9d86-a8f0d46f6724 | -9.64755 | -68.57209 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 477c3e1c-4bfc-3a57-a3aa-3aa4069414f2 | -9.63284 | -68.6667 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 826e11f3-d579-398f-b1d7-9274e925bfdd | -9.62898 | -68.66967 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00d2ca58-3fd4-39fc-b074-fdc895e8093b | -9.62651 | -68.55437 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c71439f7-e5dc-37f9-88d6-ade0b7f71115 | -9.62073 | -68.67911 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fb4923a-81ee-39ba-b20b-56ad85f1fc09 | -9.61215 | -68.55931 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9ed3324-5bdd-36c4-933e-5553731ba3c8 | -9.61161 | -68.56282 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26174199-51a5-3d5a-be4c-11efa442806f | -9.61047 | -68.54826 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd017a9a-b291-32dc-86cf-3f8fa360b357 | -9.60926 | -68.73102 | 2024-10-17 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 471e80d5-2ae0-372e-9ba1-b74ec8bf2f6b | -9.6066 | -68.55123 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0dd576fd-f548-3af6-99f7-fd80508e8635 | -9.56487 | -68.60222 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25f4af71-35ac-3701-a847-a5eb80287f36 | -9.83443 | -67.60506 | 2024-10-17 05:53:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d06dbf9f-46de-33d8-bd5f-2184c3df3522 | -9.81292 | -67.56416 | 2024-10-17 05:53:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99f233d2-6528-36a9-8b28-f8e20d182f79 | -9.78094 | -67.68306 | 2024-10-17 05:53:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c0e32c9-a638-37d4-a341-ef927ac37e67 | -9.56038 | -67.43152 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f481df0f-73d2-39ff-8918-812a898814f2 | -9.54923 | -67.71082 | 2024-10-17 05:53:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68dfe5ae-06c6-3fb8-a422-8161de2c881c | -9.52232 | -67.72893 | 2024-10-17 05:53:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 201328b7-2a43-34ee-b65e-1267a08da24c | -9.46126 | -67.73464 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3708a77-be68-31a9-8349-7a1d5f5d9cc0 | -10.11131 | -68.04839 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39f4a87b-af94-3383-a593-c3fbc46cc8f2 | -10.07634 | -68.06158 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49f62653-3299-359e-9476-3da5cac60d46 | -10.07299 | -68.06106 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 43faa319-1416-3073-99c9-c51ea467e9a3 | -10.07243 | -68.06465 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddc64523-2816-3510-b790-8a5566570f7e | -10.07172 | -67.97979 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de0bde41-faa7-3175-a0ab-58a0f8e15d98 | -10.06964 | -68.06053 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1b164df-0d70-3754-96c0-a5060ea031d9 | -10.06908 | -68.06413 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59520a68-ab36-3ea5-84fd-b9df1c07950c | -10.06892 | -67.97565 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40491b77-aea0-30c7-bd88-ce337047118e | -10.06837 | -67.97927 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46826401-b8ed-3c3e-a773-c8ad72096167 | -10.06781 | -67.98286 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6bbd6cb5-0dd1-305a-8e4a-609945876ee7 | -10.06726 | -67.98647 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f05301f-0edf-3c5e-a447-26f40b6d98de | -10.06501 | -67.97874 | 2024-10-17 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9bec3ee-63ab-38b6-8fd8-13e89b84552f | -10.86083 | -68.25288 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a1dc2099-47ca-31d4-9bb3-ff6a9f547094 | -10.85864 | -68.26729 | 2024-10-17 05:53:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README64.md)
