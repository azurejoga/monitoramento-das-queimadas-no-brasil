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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7dc48b7-5a78-39b5-9df5-08d9d14fa7a8 | -11.1379 | -53.9429 | 2025-06-18 06:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 85b2ed10-d42e-3ab5-a7ac-75e0f0d508cc | -11.1379 | -53.9429 | 2025-06-18 06:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| e5aa3834-da34-3687-b251-35f9c15c0cbe | -11.1382 | -53.9223 | 2025-06-18 06:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| a2e19331-73b0-37bf-9903-923bd9894958 | -3.03564 | -49.42322 | 2025-06-18 06:10:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0fcc00ec-3fac-3c19-b126-f78ed42829ee | -11.13268 | -53.92928 | 2025-06-18 06:12:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| fd85f9aa-4d5f-3307-b0c5-06e598e3ff22 | -8.0778 | -43.10643 | 2025-06-18 06:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 40.5 |
| 495968e3-0f3f-3d64-a755-d6ef2a1f845f | -8.07473 | -43.10158 | 2025-06-18 06:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.7 |
| 26198947-7f99-35db-b87b-f01961f59b3d | -11.14148 | -53.93061 | 2025-06-18 06:12:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.9 |
| b64ee9c4-8d25-3bcb-9c62-ef70ad5ea17a | -9.49489 | -56.08434 | 2025-06-18 06:12:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| cbf877b8-d53c-3c3a-ad6b-e5f5ecb48fae | -10.92333 | -56.83731 | 2025-06-18 06:12:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a62a1d73-e677-33bc-80be-29e301a62679 | -5.90276 | -43.43192 | 2025-06-18 06:12:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 44.4 |
| f56f9b92-a596-3eff-a8bc-1e266a1e09ba | -10.65496 | -49.37077 | 2025-06-18 06:12:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 1fb434f3-9df2-3206-a800-68970fa140a6 | -8.71737 | -49.02171 | 2025-06-18 06:12:00 | AQUA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 0ac8ff6b-e8be-37c4-b9c4-abffca071576 | -11.13134 | -53.93819 | 2025-06-18 06:12:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| e6e56921-7104-3b44-a7e2-4fbd8e24da3f | -9.2634 | -50.03733 | 2025-06-18 06:12:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 52f1e966-2a1b-3080-8984-1d727c45193d | -11.12254 | -53.93686 | 2025-06-18 06:12:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b41fb141-6198-381d-8b26-2e1067c7b4c4 | -5.91063 | -43.4378 | 2025-06-18 06:12:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| de8f008b-b78e-3922-afb5-cf5091ec0661 | -10.65691 | -49.35663 | 2025-06-18 06:12:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 30.3 |
| f0948e16-08bb-39f7-be65-39b4669e3dc0 | -10.65791 | -49.36366 | 2025-06-18 06:12:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 682d89ad-1593-3a43-a1b9-97634b53db3b | -9.49155 | -56.07697 | 2025-06-18 06:12:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6f02c892-78be-3c67-9b1d-bcbd54fe5fa0 | -9.48995 | -56.08735 | 2025-06-18 06:12:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 24a8db91-26f2-3365-9370-a00d95f2f3cd | -11.14015 | -53.93952 | 2025-06-18 06:12:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 78527fa8-8da0-394d-bb71-bc5ca800c185 | -12.50173 | -55.73473 | 2025-06-18 06:14:00 | AQUA_M-M | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4f4db6a7-f48e-34e6-adb5-73299215ce44 | -11.96131 | -58.72607 | 2025-06-18 06:14:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| f09e8195-8303-37cf-a537-b1e2dd5a0838 | -12.50028 | -55.74417 | 2025-06-18 06:14:00 | AQUA_M-M | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5d0931f8-991c-30b8-954c-28ff9557f3e0 | -14.02876 | -55.12169 | 2025-06-18 06:14:00 | AQUA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7bf1ceda-0bab-3508-8181-6cb88a91fc74 | -12.50728 | -58.35028 | 2025-06-18 06:14:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2fe47827-fb21-390d-ac80-9f03254ec15b | -14.06585 | -53.37997 | 2025-06-18 06:14:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 4695e0c8-bcff-348c-adfe-daea6f3f2e30 | -12.64483 | -54.12088 | 2025-06-18 06:14:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 14532fd7-3ece-3a85-acd9-998579da9e37 | -18.99277 | -52.08743 | 2025-06-18 06:14:00 | AQUA_M-M | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 391d72cd-b58f-3fc4-b64a-ae935acb7e96 | -14.0672 | -53.37053 | 2025-06-18 06:14:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 72cdbf16-ab8c-3362-8213-eaa061dd8925 | -11.1379 | -53.9429 | 2025-06-18 06:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| aba08f56-6a0f-3012-8f72-e9dd82a8912f | -9.96093 | -64.97443 | 2025-06-18 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01a6ae55-402b-3a8c-89ae-9e69d125d054 | -9.96627 | -64.97937 | 2025-06-18 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89a8b7e3-4434-32f8-b214-58e4b3c69f65 | -11.1379 | -53.9429 | 2025-06-18 06:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| bce581a5-8ca1-3d91-b288-9be5279ae08a | -11.1379 | -53.9429 | 2025-06-18 06:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| c6de24ab-ef78-3bf6-bab5-7a1c8fbec172 | -11.1379 | -53.9429 | 2025-06-18 06:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 1834f480-e444-3074-9a07-17f62c0e25a3 | -11.1379 | -53.9429 | 2025-06-18 07:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 807ad7a6-4260-39fe-bb47-4a35b832e67b | -11.1379 | -53.9429 | 2025-06-18 07:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 0f1e968d-b526-3472-be17-fa1658b15aa6 | -11.1379 | -53.9429 | 2025-06-18 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 2bcdb2f8-c1ef-3bbe-b2a6-2c9d1864f5c3 | -11.1379 | -53.9429 | 2025-06-18 07:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 867a70d3-14a2-39ee-b6ec-3a3165ae35c3 | -11.1379 | -53.9429 | 2025-06-18 08:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 71c799f3-7877-3f99-8308-47d1a426a1bb | -20.6981 | -49.5892 | 2025-06-18 09:00:00 | GOES-19 | BÁLSAMO | SÃO PAULO | Brasil | 3504800 | 35 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 64cf026b-5156-38f1-a2f8-a0c15d481ff9 | -12.2236 | -44.22412 | 2025-06-18 11:47:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 84ee26e0-884a-3ea9-9365-2dbb1351cf6a | -5.90661 | -43.45302 | 2025-06-18 11:47:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 74e17b2b-8b3a-3a9b-b835-bebf0fe9835f | -5.90477 | -43.45883 | 2025-06-18 11:47:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 4cee3a83-994a-3316-bd5b-54ef7297e502 | -7.08654 | -44.37243 | 2025-06-18 11:47:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 30f75346-5aae-3d8d-9aa8-554334ce71e6 | -12.22656 | -44.20581 | 2025-06-18 11:47:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 43d2c8e8-8e53-33ca-a6ad-0fb474630b0d | -5.92095 | -43.44046 | 2025-06-18 11:47:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| ea5f8a3a-5704-3373-ad9b-4b53914fcdf6 | -12.22986 | -44.21234 | 2025-06-18 11:47:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| f9159e9a-4e90-3efd-bff5-84739d0c5a8f | -6.86433 | -45.56287 | 2025-06-18 11:47:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 1cac5a73-be66-3bb1-b51c-cd863ed57c07 | -12.88672 | -44.2951 | 2025-06-18 11:47:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a844d47f-2b2a-38f2-8afe-509a43da6501 | -12.88367 | -44.31322 | 2025-06-18 11:47:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a24f0799-395f-39b8-a115-69b962745102 | -5.90805 | -43.4383 | 2025-06-18 11:47:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| dbb96773-0841-349b-a28d-74debfb2313f | -12.22676 | -44.23062 | 2025-06-18 11:47:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 1412ef19-c3cd-376a-bbd4-a616c550931d | -19.74386 | -43.95006 | 2025-06-18 11:49:00 | TERRA_M-M | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0bd997db-1dab-34eb-b516-ea91774b5549 | -19.0711 | -53.4599 | 2025-06-18 12:20:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 110.7 |
| e716672d-922a-3017-b74e-b0e6c2834e94 | -5.7713 | -43.4752 | 2025-06-18 12:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 352c59f3-4c4e-39c6-a100-80a1c3261629 | -19.0711 | -53.4599 | 2025-06-18 12:30:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 89.3 |
| a873572b-1847-3937-aa6a-230438af9a04 | -5.7713 | -43.4752 | 2025-06-18 12:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 5e3d143b-c245-3fa6-b84d-f6371a3fcf68 | -19.0711 | -53.4599 | 2025-06-18 12:40:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 106.2 |
| a0d0c307-6132-3da8-8d99-4ecd5ad49eb2 | -11.658 | -44.644 | 2025-06-18 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 276.3 |
| fa9d17c5-2bd3-38b3-b28a-c25aff3eae2a | -5.7713 | -43.4752 | 2025-06-18 12:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 173.2 |
| c74118d8-6475-3e3b-bed0-0ada734af9af | -5.7713 | -43.4752 | 2025-06-18 12:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 1d459edb-2b48-338a-88ea-3fd5987481bc | -19.0711 | -53.4599 | 2025-06-18 12:50:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 114.1 |
| fd721625-54eb-31b4-95fa-42c0841be9bf | -11.6584 | -44.6207 | 2025-06-18 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 9f06a294-69d1-318d-929c-5f30d7efe5a2 | -11.658 | -44.644 | 2025-06-18 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 437.3 |
| 07ac3344-1fce-364e-b39a-c5765dc2bb3e | -5.7713 | -43.4752 | 2025-06-18 13:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 244a11e8-3296-3f4b-a429-f2f1adcbdd95 | -11.6584 | -44.6207 | 2025-06-18 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 219.9 |
| 74f460b5-cdde-36e0-a2fb-7f2195ed3c28 | -19.0711 | -53.4599 | 2025-06-18 13:00:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 78.5 |
| e9ad19a9-b905-3e8d-9f00-2bcd6fbf82e9 | -8.5909 | -51.5746 | 2025-06-18 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 2a02595a-d015-301a-bc07-92231e5d3ae1 | -11.658 | -44.644 | 2025-06-18 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 608.2 |
| be2ffa2e-162d-315f-af7c-9aedd3852885 | -8.5909 | -51.5746 | 2025-06-18 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 7631f038-3891-32d7-a0fa-1d786c162dab | -5.7713 | -43.4752 | 2025-06-18 13:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 3e2a1bcc-6986-3e45-9e92-3ca3086ddffb | -19.0711 | -53.4599 | 2025-06-18 13:10:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 9385fe0f-f942-3e1b-b43d-6a23d506747c | -10.8571 | -53.7631 | 2025-06-18 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| bb8a8634-08a2-39fb-92d3-f6340b177a4b | -11.658 | -44.644 | 2025-06-18 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 827.2 |
| 11b520f5-f208-3bda-aba5-8bb795a1c35c | -11.6584 | -44.6207 | 2025-06-18 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 443.0 |
| 729f031f-115c-3a05-b491-3ffe96bff5db | -4.8377 | -43.1685 | 2025-06-18 13:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 8d295e91-e956-3171-830f-04e8c4336256 | -5.7713 | -43.4752 | 2025-06-18 13:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| fda801fb-9949-387e-8b45-927e608a4ae1 | -10.8571 | -53.7631 | 2025-06-18 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 0a53a8d4-36f0-38f2-905a-3918b03301c4 | -11.658 | -44.644 | 2025-06-18 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 504.0 |
| 2408ada5-d72a-338b-80bf-1fc7884bd6d3 | -19.0711 | -53.4599 | 2025-06-18 13:20:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 82842563-38bd-3ea3-86c0-b587dd02ddaa | -11.6584 | -44.6207 | 2025-06-18 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 191.1 |
| 837be48e-d238-3ba9-acc1-358bf839b999 | -11.6584 | -44.6207 | 2025-06-18 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 6c84cca2-8227-3d60-99a0-1cd738ffbadc | -10.8571 | -53.7631 | 2025-06-18 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 9dd50aa8-3443-3fd3-ac9e-39391b89d55e | -11.658 | -44.644 | 2025-06-18 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 261.4 |
| 118e83fc-3da5-3744-9788-d805df5186bc | -4.8377 | -43.1685 | 2025-06-18 13:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| b1e92faa-fe7f-309a-bc36-3d8caa084031 | -5.7713 | -43.4752 | 2025-06-18 13:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 29933733-bf1e-393e-99c9-5aec310480bb | -11.6458 | -54.1418 | 2025-06-18 13:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 8acc083c-4e4c-3aca-aa0a-0aaa89eeea51 | -5.9028 | -43.4418 | 2025-06-18 13:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 3ce54eeb-2c5c-3ddd-b342-e1949c704a17 | -11.1379 | -53.9429 | 2025-06-18 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| ea13f342-b955-39ce-a729-5ae222454eca | -10.8571 | -53.7631 | 2025-06-18 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 2a251cd7-6768-3bdd-b3d4-6128d5791337 | -8.5909 | -51.5746 | 2025-06-18 13:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| a8e23964-d3da-3fdb-9289-102d99e77f3b | -11.6584 | -44.6207 | 2025-06-18 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 10d01472-56af-350f-88d9-6c3f3fb683e1 | -6.6938 | -43.1882 | 2025-06-18 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 97.7 |
| 4a06aa3c-e1f3-3adc-97f8-9ec116c1d7f1 | -4.8377 | -43.1685 | 2025-06-18 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| b51713a8-487a-3f14-8a6b-52c99c5ab5a0 | -5.7713 | -43.4752 | 2025-06-18 13:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 41d5780e-fade-31d5-95dd-8bcfb79ad249 | -11.658 | -44.644 | 2025-06-18 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 187.1 |
| 368e1131-930f-391f-9474-614467ede63e | -10.8571 | -53.7631 | 2025-06-18 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |


[Clique aqui para ver as próximas entradas](README26.md)
