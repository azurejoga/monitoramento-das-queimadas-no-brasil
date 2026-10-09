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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ba2e508-c7d9-34d3-9eef-fea376112c38 | -5.70588 | -53.4626 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 289181b3-afe4-38f7-af78-bde0c7d1f724 | -3.00151 | -54.7613 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18fdecc3-a1c7-3883-a357-2ff5d9a18152 | -5.28148 | -47.90638 | 2026-10-09 04:25:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a82ad2d0-1cf6-30ae-88a5-5cc5ef1eb38e | -1.15901 | -54.23051 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3b694699-78d7-3920-98bb-1529a91cbecd | -2.73442 | -51.54793 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6e0e739-c0c7-3f94-8492-8e48189cbe3b | -7.11649 | -42.54077 | 2026-10-09 04:25:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| a828a51a-6f14-34e2-a604-c7d58c438352 | -3.93297 | -56.02093 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6fac35f-a96a-3387-9540-a888cca29882 | -4.52336 | -54.86136 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 099071b4-edbe-3709-9278-1071772c5fb2 | -5.34805 | -45.1762 | 2026-10-09 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 31d9ea19-237c-36f8-a24d-d316adaebef2 | -2.82905 | -54.11235 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f70009b-a4fc-303e-a4ea-b77b868e1813 | -3.20839 | -50.54693 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 27355d2b-baae-3bc0-b61e-7eac80f969b6 | -3.02243 | -54.09224 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a83d4e48-c6bd-3882-add5-98b0ff25f41a | -6.0032 | -40.94899 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| f0fd8c24-6c28-34b3-a03c-24252be443d5 | -6.98119 | -45.00946 | 2026-10-09 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4bb74f98-78f4-3e07-a7f4-0ce2c6106fee | -2.83018 | -54.13708 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0cf443d9-919c-3b25-8a0f-a1b4f4a06dbe | -3.01399 | -54.05487 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5947b7c4-d25c-37c6-8429-9cf15a81c299 | -1.10415 | -54.1692 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 51c8d36a-2c83-3efa-9d00-3d1085dee37f | -3.21071 | -50.55773 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 778388d6-e9ae-3658-8425-fe8be0f47815 | -4.09153 | -45.90553 | 2026-10-09 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6279dfca-ebf6-3021-bc06-ba2d74d08f80 | -1.12985 | -57.28261 | 2026-10-09 04:25:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a22c267-2247-3d31-9364-654fdaf59989 | -3.10507 | -54.27523 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4daa06f0-9635-307c-8160-cd23b3dd03de | -3.24925 | -54.0294 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d5e7366c-aeb1-3894-af87-fadc0f95d819 | -6.16797 | -39.44702 | 2026-10-09 04:25:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 7fa0801f-64a7-3e39-b242-7b697883fef9 | -3.58392 | -52.67971 | 2026-10-09 04:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d83c079b-bcf4-3081-9358-b1b97cdb46dc | -4.63459 | -50.95766 | 2026-10-09 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 640bd75c-39d9-36fd-8a7c-539e7e36f2d8 | -1.42601 | -54.62246 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae4ca9a5-09b6-3376-b74d-65817a613da6 | -1.52791 | -56.12348 | 2026-10-09 04:25:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 18d1bc35-4d94-3b5f-9658-06b301a53198 | -4.29482 | -54.80957 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ee96a73-de57-31a3-b1b4-1ebcc7cc79c3 | -3.11876 | -53.79057 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4ec040a6-3c03-303a-8919-21e10c3a7b7c | -1.3688 | -55.6045 | 2026-10-09 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0b00d563-87b5-3514-b2c0-f54d5b5891b2 | -2.81783 | -58.28896 | 2026-10-09 04:25:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| f86ed344-1719-3750-85cb-732455debe28 | -6.38546 | -45.94453 | 2026-10-09 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52bc3e35-b1ed-3b89-bf38-8302ee96a098 | -3.34774 | -50.40671 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2a23dee6-8d2d-3c9b-b575-ef406597461b | -3.01856 | -54.05862 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 142e76dc-0ee1-3811-8e4d-a5969de16220 | -2.8829 | -54.18668 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7faeff2-f36b-3cc4-ad2e-de6901aa90fb | -3.60271 | -54.58907 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| edaf019e-390b-34f1-b7ba-5f8d878e20fc | -3.205 | -50.82449 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 911020fa-08e1-39a1-bdea-d13c5c1670cf | -4.66884 | -46.30594 | 2026-10-09 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 426b726c-b4f6-3134-a791-ccf94cd168ec | -2.99961 | -54.07977 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24e97b88-0a48-340f-87d9-5b17757cf2af | -4.08912 | -44.11803 | 2026-10-09 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93737be9-8964-35aa-8495-ade16b1ac437 | -3.54788 | -54.68782 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 27c00a0b-5c1f-33e2-b3b0-3e1ffbce51fb | -2.73585 | -54.11767 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d0a604ce-8406-3ea7-9fcc-7a3b81f9fff3 | -3.35932 | -50.48541 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 979e9459-0954-3d00-9508-2467ee7d41b6 | -3.25933 | -54.03077 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7f26ebf0-df0d-3f40-921f-93f35c3c66bd | -3.09 | -53.96541 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a31bb57a-6744-3730-a8ba-66fd931eb230 | -3.30983 | -53.69917 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6ee0cbbc-0ada-3214-bbdd-1fc2e055968d | -4.51611 | -47.04107 | 2026-10-09 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c50cdc73-edde-3319-99a4-ff0a22d3f32a | -4.9864 | -46.03952 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e982bc7e-3f9b-3fc0-acac-0eb28e54cb19 | -3.09786 | -53.94884 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c57b9ee1-499b-3261-878e-0e8908eced5b | -3.84324 | -44.14437 | 2026-10-09 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6f1804b-c075-3f57-a0c9-6cdd1c4bd14e | -3.28057 | -53.83509 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2251c6ec-9b9b-3e23-9ea3-6e4a46018cb9 | -2.58003 | -56.18067 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ce88e6c-2ada-3350-bee8-39fb62f1d7ea | -3.5698 | -54.48941 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e5d3fa2-23e7-398b-a15f-c12b1b377199 | -1.38617 | -55.19551 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edc319b6-400a-30dd-a3c1-a56a60f50395 | -3.17984 | -50.54765 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cf520d9-ef7b-3424-a82a-4cd8456ee828 | -1.14995 | -54.22002 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54d65d2a-c429-34cb-b392-cce0cfb2d378 | -5.47743 | -47.55089 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9863a7d9-46ea-3c87-88e3-13003b30f07f | -3.11855 | -54.16394 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4e8eecf9-b719-315d-9ddc-1c62acf5a37f | -2.74389 | -54.10049 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ca5ca27f-2e3d-3e21-89a0-b85c97e0a2bc | -6.90166 | -43.67547 | 2026-10-09 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3c9cadb0-db85-3b15-be3f-1c65201f5415 | -3.65547 | -54.52758 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f4684552-9533-36ee-a86a-998e91de8375 | -5.70348 | -53.47709 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1bd53111-806d-379d-bb2f-246f131c9cba | -3.52535 | -59.35067 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1b59a233-0e4a-382e-9976-f76b4e7ac303 | -4.57873 | -55.72507 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 051f7c18-98ad-3c8e-9e65-842f15e31065 | -5.10992 | -46.22755 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13aac2f1-bbe3-3fd9-b80d-4f44de29b9a8 | -2.93408 | -57.64928 | 2026-10-09 04:25:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c86e6255-20f5-30ef-bcbd-ac91602b2644 | -2.33325 | -48.8705 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbd12da2-1b34-389d-9aeb-a1ba5060ef7c | -3.26127 | -54.01916 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 409bbb7d-9a6e-3256-9498-25e4f2b55cb6 | -2.97814 | -54.11603 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d6d973f-e380-3ff3-8099-2dc26d001935 | -3.10382 | -53.94378 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 82c15c94-cfca-39b8-a1c2-dd1683dfe944 | -2.3289 | -48.49492 | 2026-10-09 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ef69e36-763f-3b13-b662-4913f4192822 | -1.52861 | -56.11917 | 2026-10-09 04:25:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5a7ee4ad-0d4e-3580-9cc3-c7a172409aca | -3.17296 | -58.62959 | 2026-10-09 04:25:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67f1cd10-ba75-3a4a-8752-7630c141c97a | -5.24235 | -48.39761 | 2026-10-09 04:25:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88cc8ddd-a244-3859-8b8d-ceb481d594b7 | -6.74819 | -46.89263 | 2026-10-09 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f0e7263-5d2a-367b-a379-cbebc7990c8f | -3.00624 | -54.09582 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 22d170bc-5103-35dd-ad6f-41198df2b818 | -6.71151 | -45.81778 | 2026-10-09 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 658d2370-67cb-3c05-80d8-cf089b23ce80 | -3.62783 | -54.23097 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1cb3cf87-4844-3c16-8d3c-99a9f24cda36 | -5.99798 | -40.95588 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3716ecde-f5fe-3884-a2f0-5b9143fe59e3 | -6.42044 | -47.72116 | 2026-10-09 04:25:00 | NOAA-21 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19e062a1-c20a-372b-aed9-b2c4d876e80e | -6.89382 | -45.8927 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 139d530e-2f2d-32d4-b6e8-03225a124efa | -3.30016 | -54.00173 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4a9cd973-d3b4-3fb7-9915-f3e72dee5d2b | 0.92505 | -50.25508 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 272e45eb-402a-3956-a33e-ec9af0dc66e0 | -2.88032 | -54.18213 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 24d35105-d000-3f34-a0b1-1bc9875ef827 | -6.82261 | -39.55607 | 2026-10-09 04:25:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| deee2b4a-2c22-35b5-a282-3ee23580b304 | -4.07556 | -59.83938 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1fe52867-2f6e-366b-b35c-31f294a8421d | -3.35479 | -50.41287 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7dd10005-0c0f-3a6e-86dc-a5f5cf6604ee | -6.8315 | -39.38925 | 2026-10-09 04:25:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 07422c6d-a8ec-33a6-9fb4-96274f6572ba | -2.74505 | -54.12531 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a7744e0-6098-3b9c-9b9a-f8e54d50930c | -3.1074 | -53.9533 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3f7dbb28-3f65-3f2b-a7cd-e343099e370a | -3.54319 | -54.68372 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7c56bce-91c7-3984-90d9-dd90a44ad487 | -1.14951 | -54.22236 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c3610e66-2423-33f8-a55d-4a83a08dff05 | -3.02023 | -54.0437 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec81807a-63a4-3624-8f19-ace0cfd2ef4e | -2.50717 | -56.15335 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1f3aeaf0-5f59-3f04-97e1-106d211d9c7f | -5.50449 | -42.85444 | 2026-10-09 04:25:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 482c4ec5-af88-3951-808b-63084ed4859e | -4.07835 | -44.12021 | 2026-10-09 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9506f25-a572-3f2f-8ad1-c64a53f15d97 | -4.74221 | -55.66374 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6de237e2-642b-33a5-8ceb-ea3cf22fbf9b | -5.99906 | -40.94844 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| cddeb291-59a4-3d22-9921-721a37f86063 | -6.8795 | -45.89762 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 902953e3-2d7b-3988-a75d-310cc3bb41da | -4.22228 | -59.54574 | 2026-10-09 04:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README84.md)
