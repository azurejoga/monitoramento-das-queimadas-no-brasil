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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e06f5fd8-7312-3967-8c3c-eb0da7e0ee5f | -5.88033 | -41.94609 | 2024-10-12 03:40:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d0ee3bea-b6c2-3f78-be71-1d9bc16f85a5 | -5.85389 | -41.96148 | 2024-10-12 03:40:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7747d9b2-9291-3155-8a44-db984028481e | -6.36493 | -44.40416 | 2024-10-12 03:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b09490a-8b2a-38c8-bb3b-7a78b48d8b84 | -6.12303 | -44.94574 | 2024-10-12 03:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45ac832d-2f7c-3a66-8a8b-f866a60114e2 | -6.12237 | -44.9495 | 2024-10-12 03:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e722077-a153-351c-8893-dea278e19b8b | -5.55518 | -44.69577 | 2024-10-12 03:40:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1d151791-d04b-3418-9140-b75b09ab3ff3 | -5.55451 | -44.69955 | 2024-10-12 03:40:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7afd1c85-cf32-34c0-90fc-6bbfd6bb7976 | -5.55266 | -44.69281 | 2024-10-12 03:40:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6772b323-7d5f-3e5e-a640-68dc4e3d336f | -5.55202 | -44.69657 | 2024-10-12 03:40:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0e2b0956-14e8-3ae7-b77f-43e0bf13544a | -5.55137 | -44.70036 | 2024-10-12 03:40:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3cf0ca7c-3666-3f96-8216-a91af4f1e0e2 | -5.5503 | -44.6908 | 2024-10-12 03:40:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2acc8390-fd62-348e-b00b-1f833f289492 | -5.54963 | -44.69452 | 2024-10-12 03:40:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee22bd6a-5b57-3d1e-a6f6-77b0ead1f9e6 | -5.54896 | -44.69827 | 2024-10-12 03:40:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f29c0ff-3861-3823-8684-3a83ed05fcd2 | -4.85638 | -45.68283 | 2024-10-12 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a71c9d38-6f53-3154-b807-b6fe11ded54e | -4.8555 | -45.67998 | 2024-10-12 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9e13f7d6-7f18-3fe4-8446-15f07e8e8379 | -4.8547 | -45.68464 | 2024-10-12 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1629268a-4d88-3e97-88d3-636c2efbfb3d | -4.85033 | -45.68187 | 2024-10-12 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9be5ae1e-1cfb-338e-8a6e-da0b6ddef6e8 | -4.84943 | -45.67915 | 2024-10-12 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2e933d9-c1bc-3313-b93e-11a65588f13a | -4.84866 | -45.68364 | 2024-10-12 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7487f3f-ab6a-3792-8d8f-f7898817effb | -4.59466 | -45.62917 | 2024-10-12 03:40:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28e29e4e-0627-3a12-804f-bb671f422fa0 | -4.59392 | -45.63343 | 2024-10-12 03:40:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1da7e9d6-db4e-3d5b-9e92-716d86883452 | -4.58863 | -45.62808 | 2024-10-12 03:40:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d428850-a43b-3c89-a58f-3e2b6b0a1525 | -4.58789 | -45.63233 | 2024-10-12 03:40:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dbbea4de-3029-3274-af7c-b2d2607b9a13 | -4.04268 | -45.81193 | 2024-10-12 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 778e92dc-fe29-308a-ba6b-5092d75a7b84 | -4.04187 | -45.81661 | 2024-10-12 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 19483c4c-240f-3683-88d4-a8a99346d8a7 | -4.03654 | -45.81073 | 2024-10-12 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9bddd95-05db-3f89-889a-a0830bf3f2fc | -4.03573 | -45.8154 | 2024-10-12 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 058c2c11-8d4f-3b11-8011-79e96467a27f | -5.88393 | -46.37382 | 2024-10-12 03:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 296ba20f-68bc-341a-99dc-2f12ec4acdec | -5.8815 | -46.37444 | 2024-10-12 03:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a200a30-e4da-3103-bcd6-25d599ccf2e4 | -5.87773 | -46.3727 | 2024-10-12 03:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6eee14af-1f80-347b-b65a-a96fe6f9f6af | -5.87529 | -46.37342 | 2024-10-12 03:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8f7dc38-576b-33b0-a464-94611a03c68b | -5.84526 | -46.2338 | 2024-10-12 03:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e39f200-9f52-369c-8721-11cf2f0ea592 | -5.84443 | -46.23837 | 2024-10-12 03:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1152fc53-3567-38f5-ae0c-27e7a5890528 | -5.66047 | -46.41437 | 2024-10-12 03:40:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58ef8189-d9d4-39c3-8449-c73d75b248cc | -5.65959 | -46.41918 | 2024-10-12 03:40:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a3fb5cf-73f9-3d95-88c0-758886450516 | -5.65705 | -46.41343 | 2024-10-12 03:40:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc90494e-5b82-345d-bd38-feccb57909e0 | -5.6562 | -46.41825 | 2024-10-12 03:40:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bf0b9b5d-9ec0-3f99-8341-ba49914b1507 | -5.65412 | -46.41389 | 2024-10-12 03:40:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c1796d1-e66d-36c8-b2d2-1fe7eb0a85cc | -5.44657 | -45.40354 | 2024-10-12 03:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6258e2a2-97fd-3d46-882e-f6f82ee66993 | -5.39702 | -45.35362 | 2024-10-12 03:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 86409ff3-4c0c-3033-9c46-6936b60e147b | -5.3963 | -45.35778 | 2024-10-12 03:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 662acbed-a1bb-39f8-a6ca-bb520dfce518 | -5.39558 | -45.36188 | 2024-10-12 03:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| fe62dada-8cf5-3163-bf41-765640f69085 | -5.3912 | -45.35242 | 2024-10-12 03:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| bc7b69af-0485-3fbc-b84c-b2d8de3f1e4b | -5.39045 | -45.35667 | 2024-10-12 03:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a4465c50-0441-3911-8bfb-7b2164ac3e86 | -5.38972 | -45.36081 | 2024-10-12 03:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 20bc478d-0d0d-3730-b8d6-45e70c12b15c | -5.31563 | -45.414 | 2024-10-12 03:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8cf15bcf-5c88-38ab-99f0-2469852a4cb5 | -5.314 | -45.41195 | 2024-10-12 03:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3a1c90f7-8086-3b7c-89b0-7216b41d11d2 | -5.31324 | -45.41617 | 2024-10-12 03:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7eceb67b-c83f-3aa6-b979-04ff03c3728c | -5.30975 | -45.4129 | 2024-10-12 03:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af9a329f-7c41-34ce-af30-cabc7365a2f1 | -5.11158 | -46.18781 | 2024-10-12 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ceaf715-a601-32ff-8e55-6f75c4c42656 | -5.10543 | -46.18642 | 2024-10-12 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d9ac5e6-2a18-3de4-a582-d6b8532bc249 | -5.06356 | -46.07388 | 2024-10-12 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c216d8f5-11e9-3aea-8821-75ac579a1c9f | -5.06271 | -46.07873 | 2024-10-12 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8d035795-e602-3a18-af22-cc5781f39929 | -5.05745 | -46.07249 | 2024-10-12 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf18e5c4-af80-3e97-8b9f-9e4c54ba713c | -3.21769 | -46.78401 | 2024-10-12 03:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db5f6289-38c5-39c1-8130-de3cfbee06d9 | -3.21107 | -46.78289 | 2024-10-12 03:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1e25585e-1835-3520-aeb7-7a44e57c0427 | -3.21009 | -46.78853 | 2024-10-12 03:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6aba612d-ca06-3912-bc15-103fb1e53781 | -2.74181 | -46.78313 | 2024-10-12 03:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45a1ab01-4352-35d0-bcf3-62daa259de26 | -4.91412 | -47.65035 | 2024-10-12 03:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b97a3779-2737-382c-bcd0-dc483fdc55e5 | -4.91283 | -47.64956 | 2024-10-12 03:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae465b93-7c2c-3675-a884-632fd38e199f | -4.91179 | -47.65543 | 2024-10-12 03:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 70c7fcbc-5e17-394b-a78f-49022ffc1b3c | -4.58503 | -47.09823 | 2024-10-12 03:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| fad531ad-f8f7-366d-b548-36240985be2c | -4.58406 | -47.10379 | 2024-10-12 03:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9ac8f26d-25ab-3dcc-9ccd-f65b44592380 | -4.58255 | -47.09886 | 2024-10-12 03:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| c06019b6-e538-38a5-810c-fd9b8c680424 | -4.5785 | -47.09659 | 2024-10-12 03:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1553a271-b5aa-309c-9918-baa731e88375 | -5.65057 | -47.9219 | 2024-10-12 03:40:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b7c0dd2-2532-3430-aeaa-5c35d5b54dc4 | -5.6494 | -47.92827 | 2024-10-12 03:40:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1576fe4a-3d5e-35ac-927f-31ef60f56e9e | -5.08113 | -47.18351 | 2024-10-12 03:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f16347a-0eb7-3d2d-adb3-1f4d2e34185e | -5.08992 | -47.92847 | 2024-10-12 03:40:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a73293f5-b6bb-3937-a053-215e953efcf7 | -5.08878 | -47.93491 | 2024-10-12 03:40:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5727b89-48a8-3222-a35e-ebedaeac97dc | -4.11354 | -48.24832 | 2024-10-12 03:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bad272a1-de04-39f4-a389-edadd2052abe | -4.11229 | -48.25536 | 2024-10-12 03:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a850ac32-fbcd-3d7c-a7d5-d13dc9ef7d1e | -6.42215 | -48.27012 | 2024-10-12 03:42:00 | NPP-375D | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 302beb5b-374b-397f-9ec0-30db1bf549b4 | -6.42102 | -48.27226 | 2024-10-12 03:42:00 | NPP-375D | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 2677217b-a576-324c-bb8c-c939fcf71193 | -6.42099 | -48.27654 | 2024-10-12 03:42:00 | NPP-375D | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4d3b9a1b-c30d-3f3a-b347-296d9d28962f | -6.4153 | -48.2687 | 2024-10-12 03:42:00 | NPP-375D | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8adbe83-9098-341c-8e7b-174ae6aebc76 | -6.41414 | -48.27509 | 2024-10-12 03:42:00 | NPP-375D | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c96c8aaa-a4fc-3c0f-91f5-d48faa7b8de7 | -5.733 | -48.46654 | 2024-10-12 03:42:00 | NPP-375D | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bceed6bc-6a52-3bb0-b9af-ed13ce931026 | -5.73172 | -48.47338 | 2024-10-12 03:42:00 | NPP-375D | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f6ce668-75c4-37a8-9d4e-18a11575c303 | -5.72905 | -48.46681 | 2024-10-12 03:42:00 | NPP-375D | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7487e3e-5ffe-369a-af61-f9c98cdbef11 | -5.7278 | -48.47372 | 2024-10-12 03:42:00 | NPP-375D | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a40432da-8ee9-3103-9488-6c453edaf5ce | -9.83865 | -49.56425 | 2024-10-12 03:42:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65c3e9d6-db3c-3e40-a119-cf61b75dcf06 | -9.83727 | -49.57111 | 2024-10-12 03:42:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c84b8e8-0446-339a-b760-c35f66e4a2fb | -9.83028 | -49.56961 | 2024-10-12 03:42:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c1ba0c2-3348-31f2-8ce8-74c8bb80f3f4 | -10.53585 | -49.10424 | 2024-10-12 03:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 81428feb-1a6a-37a1-83b6-2eb603ca950d | -10.53456 | -49.11058 | 2024-10-12 03:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 201165dc-410e-3640-9740-d5ce34288222 | -10.52784 | -49.10904 | 2024-10-12 03:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2701609f-a951-339b-aa8f-ad227cec550c | -9.83919 | -39.59902 | 2024-10-12 03:42:00 | NPP-375D | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4f455970-c077-33a2-9ba3-394b63d201cf | -9.29917 | -40.55454 | 2024-10-12 03:42:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a6d5745b-6a1b-390b-a5eb-4cace8779d8f | -7.21304 | -44.14109 | 2024-10-12 03:42:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 147cef1b-41d1-3f8b-995c-ef6e3381a52c | -6.63912 | -43.86052 | 2024-10-12 03:42:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 827901b8-a30f-32aa-9464-4c0fdfe98b03 | -6.63391 | -43.85963 | 2024-10-12 03:42:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d395e08c-5640-33a9-b380-746da1dd85c9 | -6.63337 | -43.8627 | 2024-10-12 03:42:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b06f6418-aa45-3365-b7e7-dbf0fbc3329c | -8.82317 | -45.37737 | 2024-10-12 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f2b3e71-e66c-316c-847f-bdafdc7ebcc8 | -8.13456 | -44.46331 | 2024-10-12 03:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 22513179-8e28-3fea-bc2f-91008868f605 | -8.13399 | -44.46652 | 2024-10-12 03:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9eef18f0-c9a2-303c-896b-455fef8d72f0 | -8.12986 | -44.45911 | 2024-10-12 03:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0dcad25-c45d-3961-aec1-4b685253e7d9 | -11.46011 | -43.92747 | 2024-10-12 03:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 86832481-39d2-37c0-988e-d55a41e9b5d5 | -11.4553 | -43.92657 | 2024-10-12 03:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b0a20bb2-2484-3bf7-a5d4-bb7683dd8f79 | -9.57548 | -44.3882 | 2024-10-12 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README37.md)
