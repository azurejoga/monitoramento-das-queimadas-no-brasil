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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e514bd4-c0ed-3171-8ee8-8d0ae7a3000c | -10.17323 | -43.97865 | 2025-11-14 04:23:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f8d5d35-8a99-3276-949d-9e63fdb0d3c5 | -5.02397 | -41.10434 | 2025-11-14 04:23:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2112a738-a225-30a9-8bd1-ffd5d3e52d9c | -7.71906 | -42.36689 | 2025-11-14 04:23:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 45921934-a239-3ec5-81a3-f4766227cb2c | -9.31972 | -47.83506 | 2025-11-14 04:23:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0d95119f-9566-3cde-8404-4d146dd7929a | -9.09371 | -44.32256 | 2025-11-14 04:23:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8eb1aaff-23d3-374a-9529-25724807d62a | -9.18964 | -41.02899 | 2025-11-14 04:23:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8ab33633-a011-3938-ae26-6d7631f3e14f | -7.88323 | -44.31774 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e759c9ae-7edc-3a9f-b3ed-4d7b4b1b6554 | -3.74818 | -44.27498 | 2025-11-14 04:23:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5e0a6f6-239f-332e-81f2-7c0053eef00d | -9.31145 | -47.83851 | 2025-11-14 04:23:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d519d42-4df3-372b-87ab-8c2b868b35ad | -10.80286 | -44.85194 | 2025-11-14 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| faba23ba-e91f-34a7-8ff7-1128c2121633 | -3.36227 | -48.4049 | 2025-11-14 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4adcd982-612c-3d07-bd9d-9a5cf1f1cc0c | -7.84039 | -44.28582 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bba2aa0-12db-3dc0-8175-d90bb3355bff | -8.76016 | -45.66558 | 2025-11-14 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95dae039-e55c-3cbb-988c-b08a29db5be4 | -2.95987 | -45.75663 | 2025-11-14 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 623f8302-babd-3ca1-b470-9f690ce89b1a | -2.51567 | -47.80347 | 2025-11-14 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c577c010-f521-3752-8e11-6b8298605c9d | -7.85542 | -44.29897 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7fa83c14-428d-3b00-8d28-1ebed9904a7c | -2.7997 | -45.49199 | 2025-11-14 04:23:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84905718-5816-3e79-ade8-0c59fa337227 | -9.34886 | -46.59601 | 2025-11-14 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ed45a869-f2ae-3ce2-9370-a329af79c346 | -4.03898 | -46.98396 | 2025-11-14 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06a45d72-853e-31ac-b2b1-e46e50f61ec5 | -4.22499 | -45.44925 | 2025-11-14 04:23:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 137530e8-0732-3cc0-a662-831fb8ebfc6a | -1.8332 | -53.80623 | 2025-11-14 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d786745-0fe1-3f15-860d-f9385353c1f8 | -3.35604 | -48.39397 | 2025-11-14 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56d494ec-95b4-3de7-9663-2ac461e5094d | -10.63012 | -45.01008 | 2025-11-14 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3de83f5-17fb-3455-a7d9-c67432cc50a7 | -7.86711 | -44.31161 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fec6a1ea-7875-35ab-803d-768c3c5a98b2 | -3.15652 | -49.16544 | 2025-11-14 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16e84e52-c361-3c20-ae4a-0d404aaf2d33 | -3.01294 | -49.43222 | 2025-11-14 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1ac1d40-91a7-3c16-8445-743d47b31b03 | -4.30582 | -46.27319 | 2025-11-14 04:23:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d70da6f-858e-30b8-90da-55a79630346d | -7.88268 | -44.32125 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0894fbc2-58e3-3056-8dae-02385df06ecd | -4.05163 | -46.44019 | 2025-11-14 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3593cb2-e830-3d54-9730-7855862ec01e | -7.93449 | -44.81239 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1373a396-11d9-3cda-9ccf-c3e1229eb822 | -9.85132 | -44.16424 | 2025-11-14 04:23:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb8d0415-717e-38d5-8963-b2d1b26bd530 | -4.24138 | -42.32916 | 2025-11-14 04:23:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 345b7011-ddf3-3d20-b74f-e946f6882a87 | -7.85318 | -44.29143 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d5e2c45-81da-3761-a998-9f4459e15aa4 | -2.51946 | -47.80409 | 2025-11-14 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c31c204d-61ef-3d16-b1ae-18926c5fe9ca | -2.11501 | -45.35947 | 2025-11-14 04:23:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5acb41f7-a3cd-3183-b4eb-4713a3cf7387 | -4.5335 | -43.39268 | 2025-11-14 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b70a807-0ac3-3faf-a45f-cfe0afae3219 | -4.6137 | -43.38359 | 2025-11-14 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b71187aa-c8a6-33f2-8521-8c8d4f9656b7 | -7.93117 | -44.81186 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdaa1dbb-792a-3503-b4c1-a7f7b497052e | -2.95357 | -54.56389 | 2025-11-14 04:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a255eab-44eb-3fbc-9dc9-01e4ac00a8cf | -8.90897 | -41.07088 | 2025-11-14 04:23:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| de9380bf-f25f-3293-a96e-09a49d8eb47f | -2.11386 | -45.36674 | 2025-11-14 04:23:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7af0bfce-fc84-3f84-9a56-d9ae92039fe7 | -4.29154 | -41.81176 | 2025-11-14 04:23:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6a030e18-fabc-3862-b333-3e3db6ccdd1f | -2.9653 | -41.58048 | 2025-11-14 04:23:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba21fd94-cdc3-3dc2-af8a-24585f719522 | -7.85208 | -44.29845 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 84429421-11dc-3c1f-9d80-239ea1e5b251 | -3.3541 | -46.8703 | 2025-11-14 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25993539-dd4c-330e-a0b2-78284d530ba0 | -4.89844 | -42.90668 | 2025-11-14 04:23:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc8ca010-90aa-3e44-a8ae-5bd881c36094 | -8.90067 | -47.89906 | 2025-11-14 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f98db32-acca-3287-b7f1-5d8e7fe95639 | -7.45463 | -42.56884 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c8b73b2e-e416-3510-836c-e5875d6e8d95 | -9.04834 | -48.71641 | 2025-11-14 04:23:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d06c4ca-4ddc-3fb1-ab82-74dfe24d96e7 | -7.59236 | -46.75918 | 2025-11-14 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ac073f0-4e3b-325f-ad8e-590df2e1f13c | -3.7657 | -46.007 | 2025-11-14 04:23:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97cdd254-89c5-3408-8855-b0fbd9160ed8 | -7.93245 | -44.32539 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5d274fb-63d4-32da-bf17-4eb3ee252ddd | -4.47706 | -45.88385 | 2025-11-14 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0058d09e-46c2-3754-874f-6a49e1ab0628 | -4.89565 | -42.83604 | 2025-11-14 04:23:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d3a0af72-e132-30d5-81eb-6eb187822a4d | -3.62637 | -45.23532 | 2025-11-14 04:23:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ff84523-0e32-3d7e-a0e0-47d92faf02e1 | -2.9633 | -45.75716 | 2025-11-14 04:23:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c6c0218-194b-376f-a89a-9f3275fc2675 | -8.91281 | -41.07145 | 2025-11-14 04:23:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eb9f72d8-a0e3-31df-830c-7a208eeb68d3 | -10.52033 | -45.10107 | 2025-11-14 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4859b47e-02e2-383f-8612-913bfe6d192e | -3.78882 | -49.56974 | 2025-11-14 04:23:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a83eb13b-691c-3180-a92a-6a11fc4083ad | -7.85651 | -44.29195 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df616369-f9a9-3ff8-9dd7-90898fda1069 | -4.46154 | -43.91626 | 2025-11-14 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 483269ba-2beb-3c2d-86da-13d14ee53b7a | -9.00795 | -44.17735 | 2025-11-14 04:23:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0763c6ed-80cc-3797-8a8b-09a1a8d1fe84 | -7.9319 | -44.3289 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0c4c7cb-366b-3333-aaf5-39df2716f279 | -7.49552 | -47.03594 | 2025-11-14 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c21b76ea-8538-3486-9dc8-c5202978599d | -11.17025 | -43.57098 | 2025-11-14 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| efb0b109-a6ac-3895-9d0b-ad9d6fc90beb | -3.80083 | -40.96329 | 2025-11-14 04:23:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a6b53c58-40cb-37cc-8dbc-e64c8be2de10 | -9.68119 | -47.89723 | 2025-11-14 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a415a8ea-6f47-36d8-b986-e71f69daf52b | -10.26225 | -43.96556 | 2025-11-14 04:23:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d12ab4a-8f60-322b-8ccc-371c05b62b84 | -7.2535 | -46.73534 | 2025-11-14 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| efe92dd9-f725-38b8-aa84-bfed3a4d4705 | -4.60566 | -41.73785 | 2025-11-14 04:23:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c4760d0c-17cd-35ed-9bf3-33c274d6b397 | -7.45812 | -42.56937 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 098c4cb3-17a1-3d1f-ac74-4cbc78c4437f | -7.87323 | -44.31617 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a16d3b0-18f8-3ccd-867b-267870945eaf | -2.63235 | -47.29686 | 2025-11-14 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3b228f8b-a7e1-3d69-95b9-f54b33311cc4 | -9.14229 | -45.17622 | 2025-11-14 04:23:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da266434-51bb-36d4-af33-3e52d44f400e | -4.45582 | -45.82098 | 2025-11-14 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f8a53ab-34a7-348a-b50f-517469d12605 | -7.01889 | -46.43754 | 2025-11-14 04:23:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ecfe9081-b7a0-31b3-8b78-d2d38dc7373a | -7.93523 | -44.32943 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0e02b6d-f909-30ac-8842-f1c5339402db | -9.11728 | -43.94826 | 2025-11-14 04:23:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8a12fb3-948a-3b3f-9c96-831743d08b80 | -3.98681 | -48.00022 | 2025-11-14 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9b95be16-5588-3ae3-88c5-e9eab8e971b0 | -3.01649 | -49.43667 | 2025-11-14 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d0d83b20-4456-3c09-a563-712bfccfef5e | -2.38076 | -48.67666 | 2025-11-14 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 38c8201e-2416-392e-abcb-13ff5f7386f0 | -5.16481 | -37.57743 | 2025-11-14 04:23:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| db730a97-be60-312e-a899-b81b2525704b | -10.75316 | -44.91708 | 2025-11-14 04:23:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f7f3204-0fca-3a1d-aa11-c0ca0a74278d | -3.76863 | -46.00698 | 2025-11-14 04:23:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6425489-aa71-32b9-a87c-b37b77febfad | -3.35915 | -48.39946 | 2025-11-14 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 311f81d7-91f8-3bf3-9bb7-21bb846e5248 | -4.61314 | -43.3871 | 2025-11-14 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bea61d0-5df9-307c-834b-875a231537c6 | -3.9139 | -44.32217 | 2025-11-14 04:23:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9206fc9-62cf-3a84-b630-af670c491bd6 | -0.86472 | -47.3142 | 2025-11-14 04:23:00 | NPP-375D | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eff68b04-9c28-3ee1-9de6-9ef8d0a98717 | -10.75705 | -44.91406 | 2025-11-14 04:23:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa836f92-144b-3916-95f3-628570fecae4 | -3.08089 | -49.27792 | 2025-11-14 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 687d6dd1-804a-3193-ba16-dc8cfd0c0cf5 | -7.06667 | -48.36489 | 2025-11-14 04:23:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d0b573a-1ec1-37d5-9adb-ca2b1d2ce466 | -2.17237 | -48.36703 | 2025-11-14 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| def57cbf-8fbf-3147-9124-7567e35ccf9f | -3.74486 | -44.27446 | 2025-11-14 04:23:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdf7d2b5-6661-3a88-b247-bb4ae8033c0a | -7.05818 | -46.64734 | 2025-11-14 04:23:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49e68161-35f8-3a85-921d-6ac8ed62f3fb | -7.79254 | -49.61911 | 2025-11-14 04:23:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5a04c0f-d4ca-3aa4-8b47-7b60cd71f5b3 | -8.27861 | -55.08014 | 2025-11-14 04:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82f77bd5-e544-3c8a-952d-d0e0178634dd | -9.98548 | -45.14934 | 2025-11-14 04:23:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0faede0c-dc5b-30e9-ba3c-9d9ab820ded9 | -3.4658 | -43.18755 | 2025-11-14 04:23:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 729baeb3-8357-32b3-aa42-1d4d98362ca0 | -7.88602 | -44.32177 | 2025-11-14 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d5236dc-9386-30c7-877e-06c4e3f3d1f9 | -7.47033 | -42.58311 | 2025-11-14 04:23:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README29.md)
