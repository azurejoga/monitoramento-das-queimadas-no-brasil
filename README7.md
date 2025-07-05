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
| 6128d614-a30d-3141-b279-47f466b4aaea | -5.06788 | -43.72956 | 2025-07-05 04:17:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| a2cb26d5-99dc-31ae-b72b-69f23fdbfd2f | -3.51842 | -48.43735 | 2025-07-05 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e17f986-5574-3be9-b100-d06a9493b1be | -3.86428 | -50.08259 | 2025-07-05 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad4842f8-7c24-3a09-99e8-987974146ddc | -3.48535 | -48.44667 | 2025-07-05 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| b432f5d1-348e-3d6b-8b5c-497432d60470 | -4.81725 | -44.35231 | 2025-07-05 04:17:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9eb79c0-503b-3b0d-93f0-bfb8e09226f6 | -4.90344 | -37.36521 | 2025-07-05 04:17:00 | NOAA-20 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2dabe13c-af41-37c9-9805-65252a67a0f9 | -4.00026 | -43.23801 | 2025-07-05 04:17:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9688ebe-cac1-3926-8a69-d2b4e8ebde9c | -4.1115 | -47.93486 | 2025-07-05 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e03d1f45-8bd9-3ccc-9f2c-590fc0aaed8c | -4.10779 | -47.93431 | 2025-07-05 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8a9ebfa-5a1c-3924-b937-c1a0e5c83483 | -3.45702 | -42.99539 | 2025-07-05 04:17:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9e8dc32-36ea-3ff7-96f0-3e0c0cdd35e8 | -2.92188 | -40.41838 | 2025-07-05 04:17:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8cd6a9df-8bfe-3716-bd03-f3a1d63632c1 | -4.00081 | -43.2345 | 2025-07-05 04:17:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 827d0156-690d-3b65-922f-360a4a55f217 | -5.0651 | -43.72556 | 2025-07-05 04:17:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 254bdea9-4dc6-3adc-ba90-740ca6c77f76 | -3.51534 | -48.43196 | 2025-07-05 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05cf5b2d-361e-3972-97f2-30b0afd9a3d6 | -4.82001 | -44.35628 | 2025-07-05 04:17:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 941164e1-e87e-3768-a4b2-31f726502add | -3.61126 | -41.15493 | 2025-07-05 04:17:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 713d1867-08bc-3187-99b8-70b8382d21f1 | -5.06842 | -43.72608 | 2025-07-05 04:17:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d2e1cf9f-8e32-3635-ae53-aab17b27ca3a | -4.82055 | -44.35283 | 2025-07-05 04:17:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a4c7fdf-5955-375d-92e2-c2419120d39e | -2.90946 | -48.2481 | 2025-07-05 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 349376f9-7cfe-346a-a352-b5f56afd99c9 | -5.53852 | -44.95048 | 2025-07-05 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 155937f5-5254-36ee-94c5-aeb1c2db5f9c | -4.58808 | -47.72239 | 2025-07-05 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24dd360f-0711-301e-b4f4-17ba71c9c26a | -5.69841 | -43.65216 | 2025-07-05 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 767e4c38-7e5d-3fbe-ada5-03e402346d3a | -4.00359 | -43.23853 | 2025-07-05 04:17:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9701fc0-25b7-3fc1-b65f-c31ee0a64596 | -5.02751 | -47.97114 | 2025-07-05 04:17:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1895bf8a-5350-3cf7-8528-5d3b11649273 | -5.60461 | -45.17702 | 2025-07-05 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2fde4e9a-0d85-3486-8127-f617c82940b3 | -4.11291 | -47.92618 | 2025-07-05 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e53b684e-6c2c-3afe-803c-ead0af529e58 | -4.11079 | -47.93927 | 2025-07-05 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f7ab3d0-9980-37fe-8f12-d35778eec66a | -4.37817 | -47.63061 | 2025-07-05 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b93e9c45-adab-39c4-91bc-294f00bac966 | -5.06456 | -43.72904 | 2025-07-05 04:17:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e487875-e027-3a58-9a72-0aeb8949eade | -5.60737 | -45.18102 | 2025-07-05 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a185173f-b3a5-3782-bd95-8d70995a215a | -4.11232 | -47.95325 | 2025-07-05 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c62c58fd-05fe-3bb5-af99-f9139cd5fd58 | -3.99748 | -43.23398 | 2025-07-05 04:17:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc62d24e-b781-3a75-bcd5-b573cd66b14a | -3.81018 | -42.54461 | 2025-07-05 04:17:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07941e28-7ea2-36e3-8158-27f3064ea7f1 | -3.61026 | -41.15322 | 2025-07-05 04:17:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 678acc39-4f9a-3b7c-bfba-33fa292864ae | -5.04782 | -43.85823 | 2025-07-05 04:17:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8418b042-fe01-3a30-a610-829192e92029 | -4.1116 | -47.9577 | 2025-07-05 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe6da69c-9666-329a-bafc-82f5d31a86e9 | -4.6738 | -48.87345 | 2025-07-05 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84b693e2-0236-30f9-8a4b-e447d6bd19ce | -5.03091 | -47.96998 | 2025-07-05 04:17:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bbc15ae-5f85-39d3-ac26-31f7d6369d7a | -5.04836 | -43.85476 | 2025-07-05 04:17:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 813e29e9-31f1-3294-9747-beb262a1b86b | -5.78322 | -43.60753 | 2025-07-05 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7588a8a6-882f-38c7-bf87-9e1e34f1a058 | -4.27933 | -48.19161 | 2025-07-05 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d8bac3d6-0ab6-382d-b6aa-bf3d6e8fe4a2 | -3.5269 | -48.43369 | 2025-07-05 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 016fde5f-6803-31c5-b4c7-19447dd72853 | -4.00748 | -43.23553 | 2025-07-05 04:17:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92ccebc8-cdbb-3565-bc05-1d27dd15a07d | -3.52381 | -48.42832 | 2025-07-05 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14a7500f-8880-39e4-af2b-0c21f891b71f | -5.60847 | -45.17408 | 2025-07-05 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb8be181-64e7-3c4d-8e58-8e1c61a2aba2 | -4.39472 | -48.93564 | 2025-07-05 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5f10675-9e25-3937-b51d-a1ab697bdb20 | -4.11221 | -47.93047 | 2025-07-05 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 02d4639c-e70c-3abc-9ac4-ca7a36c8311e | -3.52304 | -48.43311 | 2025-07-05 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9acd0bbf-9ab1-307e-b523-4421c2ba6e68 | -3.52613 | -48.43848 | 2025-07-05 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b2ae065-a16f-3384-a0d3-5a4e1f5e5e01 | -5.786 | -43.61159 | 2025-07-05 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2f139e6-d338-3cb6-a59d-fa45f7a3bcc5 | -5.60792 | -45.17755 | 2025-07-05 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f42a8a7d-9bb8-3f41-8dee-32cac5b85dbd | -5.60903 | -45.17061 | 2025-07-05 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13a84216-41d7-355d-89a2-8a5ec04c808d | -3.52228 | -48.43791 | 2025-07-05 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| faec896c-bb27-338c-a4c6-186222d75c3e | -4.28193 | -48.36607 | 2025-07-05 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0af36206-4023-364b-b60e-d3305356e892 | -3.5138 | -48.44158 | 2025-07-05 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0ebaea2-c21a-3623-9160-954a1c992a60 | -3.42075 | -43.16245 | 2025-07-05 04:17:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 15e80c0e-49ab-3bd2-9708-ff201f5e1adc | -8.99632 | -47.4465 | 2025-07-05 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8b53681-7609-31a3-9965-e535515a147f | -12.76455 | -44.40102 | 2025-07-05 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a02b72ff-e8c4-3b8e-87ff-b647bbbe0018 | -9.78849 | -48.25599 | 2025-07-05 04:19:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 099b98c3-4d91-367a-9ad3-8aff82c7a5d8 | -8.08797 | -45.39516 | 2025-07-05 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9380cac8-0d62-3cb5-99e0-62eb641f26e5 | -6.01233 | -44.53054 | 2025-07-05 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3f29f06-3ef9-3543-8521-cab7b03cbdff | -10.61219 | -46.42527 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6efad3e1-e124-39ec-9305-6fb4e456cf8c | -10.63204 | -46.40709 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0008f006-d4e9-3305-8c70-3c68b50c5660 | -7.9429 | -44.8498 | 2025-07-05 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f8ecc29-db17-30c3-8895-4e00fa17ec9a | -10.55335 | -49.43456 | 2025-07-05 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4442f497-afee-3338-9d6d-c14c8b5aaf81 | -11.86007 | -44.8743 | 2025-07-05 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7adc6465-a387-3ee3-a39f-f874c81a01a2 | -11.87456 | -44.86919 | 2025-07-05 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13ff0444-eae0-3eae-8f68-7f2cf2f4bc1f | -10.65644 | -40.81122 | 2025-07-05 04:19:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f8783829-1719-381a-acbb-8e1de7808d59 | -11.44686 | -45.11381 | 2025-07-05 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91cccfe5-ae19-3232-992b-46ac4b55cb39 | -9.61514 | -49.01931 | 2025-07-05 04:19:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4f9a824-b240-36e6-91c1-c81926f817de | -7.95852 | -47.22659 | 2025-07-05 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b20fe596-aa1c-3c8a-81e9-a3f69eb4e2f3 | -6.99435 | -44.29079 | 2025-07-05 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac87f04c-2dd5-3aa1-b65b-1766a34e16d0 | -5.72604 | -49.10691 | 2025-07-05 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a672ee96-05e6-37a6-855e-13d59ae9ed5b | -7.2448 | -43.08372 | 2025-07-05 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 2e3d4c1b-1f57-30ce-9e19-d332d18afc9f | -7.19201 | -45.32341 | 2025-07-05 04:19:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe9b3810-c071-30c7-9fee-7b796bca7d8d | -10.65307 | -46.40329 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0b6c6274-0275-32d8-bc06-b1a33f9a7994 | -10.35954 | -48.72205 | 2025-07-05 04:19:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfb34c81-c7da-332b-8457-dc50620bca8b | -10.66026 | -46.40085 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea40223f-2022-3154-b732-c405b407ecc4 | -6.79212 | -44.62878 | 2025-07-05 04:19:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb903abb-549b-3023-99bf-60d9b9db18f0 | -10.63515 | -46.47269 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c061f04-0e27-302e-8ad8-2b92ff4c3eb5 | -8.01383 | -49.71715 | 2025-07-05 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 90505239-7ee3-30f4-aad3-f514d8edb2d0 | -9.57043 | -49.10613 | 2025-07-05 04:19:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6b5fc202-c038-3c9d-94d7-1d3bc66ed7a3 | -10.6597 | -46.40437 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57fc44ab-8851-3d61-a164-489508f69ded | -6.98055 | -44.29219 | 2025-07-05 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e45e056d-fae6-386e-8da7-c3a05363b3f4 | -6.29082 | -47.01378 | 2025-07-05 04:19:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d467c20-3ab9-36e9-8407-15d13115c95e | -7.30141 | -45.36157 | 2025-07-05 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c46dfb36-6232-3e9b-9161-9a4a88dfeaaa | -7.23854 | -43.07895 | 2025-07-05 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f36d03ef-ab22-325d-adc9-dcbc05a3d5c0 | -13.04022 | -46.79804 | 2025-07-05 04:19:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2eb7d54f-f376-3e00-ae91-3595a4f9a958 | -11.87345 | -44.87644 | 2025-07-05 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00d10f1f-b50b-3ac3-9fca-aa7a9ecf8b95 | -10.36024 | -48.71794 | 2025-07-05 04:19:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1f30183c-1082-3c78-8599-1735bb353709 | -11.0164 | -56.25689 | 2025-07-05 04:19:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59eaa424-af6a-3c80-896b-503f80bb84b9 | -6.41513 | -43.55958 | 2025-07-05 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e760359-dda2-3d71-9685-6ad3f38a2f97 | -11.87342 | -44.85419 | 2025-07-05 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2791e867-a25f-3697-ac82-856f1918ff18 | -7.63955 | -44.3348 | 2025-07-05 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50b470ca-3b8c-3f47-bc90-efce87154a3e | -7.94621 | -44.85033 | 2025-07-05 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2dc0539d-a095-35f4-9ad2-6caf2fc941a5 | -7.22374 | -43.08427 | 2025-07-05 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e1861f92-a497-3d7e-af12-82a36ac3089e | -6.68034 | -43.15706 | 2025-07-05 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c51998e7-4672-3623-b5b5-218c8ad87fd7 | -7.69955 | -47.2862 | 2025-07-05 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d09bd8f2-9359-35ea-9ced-e8fce45307ed | -5.42754 | -49.08664 | 2025-07-05 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c29f7898-b35a-3756-9d56-9a1fd96b3768 | -10.61275 | -46.42174 | 2025-07-05 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |


[Clique aqui para ver as próximas entradas](README8.md)
