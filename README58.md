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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2ddf324-6618-315c-9d72-bfb4bec48e05 | -4.85924 | -45.8536 | 2024-10-05 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e5566cb-a0ab-3557-9a92-5c720ac59deb | -4.84665 | -46.52228 | 2024-10-05 04:12:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f2558df7-cada-3c2d-8dce-3a0ba77359de | -4.81771 | -44.35438 | 2024-10-05 04:12:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa2f7a7f-45e8-33b6-bb06-dc4ececda3ef | -4.79632 | -50.80943 | 2024-10-05 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 023245f7-8239-35a0-a9e5-eae1886ee2db | -4.79534 | -50.81521 | 2024-10-05 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a2d7711-86bd-3168-8a1a-c1dd9720ab42 | -4.79131 | -50.80862 | 2024-10-05 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9d4f57f-06e6-3e9a-bfe4-ddca14a19281 | -4.7893 | -45.26096 | 2024-10-05 04:12:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f09cd5e-c884-35e9-8732-30f7ba04ecb2 | -4.7863 | -50.80778 | 2024-10-05 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 231b55cb-cd4f-3528-8bbb-e6ee462d104e | -4.78129 | -50.80693 | 2024-10-05 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 911a2a22-fbce-3f64-b559-4ef95fc6ea86 | -4.78031 | -50.81263 | 2024-10-05 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d20a787-fe20-315e-89c4-a282236715ea | -4.76908 | -46.6713 | 2024-10-05 04:12:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a211bf45-5c87-3824-a017-a8c76095e336 | -4.76834 | -46.6759 | 2024-10-05 04:12:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 871a9a2a-2cc7-30a3-810d-12494a2d5885 | -4.76526 | -46.67077 | 2024-10-05 04:12:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d275b8f-6bf5-3aca-9c8b-ea4ad7f72ec0 | -4.76452 | -46.67537 | 2024-10-05 04:12:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa6e9d72-66a3-3424-91d3-a9dfa573b436 | -4.69185 | -45.8734 | 2024-10-05 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1de15f2f-e17e-3d7f-b84b-d4e62eb496d4 | -4.69118 | -45.87757 | 2024-10-05 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e949087f-84a8-30ea-88d4-52cbe6e3b77a | -4.68821 | -45.87276 | 2024-10-05 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dc64019b-faf5-358d-8927-63a9a6c7d8ed | -4.68754 | -45.87697 | 2024-10-05 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 26473716-4db5-389a-9f43-98ab1284bac3 | -4.68322 | -45.88059 | 2024-10-05 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6707a0b0-76b7-3e8e-85c6-89ca8b2e1740 | -4.68024 | -45.87585 | 2024-10-05 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a029c1a-2f1e-3930-bf2c-b887a4e86834 | -4.67958 | -45.88 | 2024-10-05 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e292cf4-6b9e-3e7b-a5a3-fbfcc036f236 | -4.67658 | -45.87534 | 2024-10-05 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 793bffa3-8265-3f7c-89e4-060a93070d2e | -4.67292 | -45.87484 | 2024-10-05 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73aa70bf-d278-3add-870f-f55a6677b8c3 | -4.66122 | -49.52833 | 2024-10-05 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a8e348c0-7c1c-345b-b4c5-ad6249356d7e | -4.66042 | -49.53306 | 2024-10-05 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 220ea80d-3af6-30f5-a995-96f9483de201 | -4.65503 | -49.53696 | 2024-10-05 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 305a8c8f-7a6f-3b67-b9ef-379a00df6b49 | -4.65421 | -49.54174 | 2024-10-05 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9aaf8c4b-8ef8-3e79-9d71-6e67fc0828ab | -4.59704 | -45.6027 | 2024-10-05 04:12:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a84f84e2-efd3-3e33-a3c3-8039dbdb5dfa | -4.59638 | -45.60678 | 2024-10-05 04:12:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42336365-3a9f-3346-b073-7d2c264308c0 | -4.5746 | -48.01511 | 2024-10-05 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11009c03-5355-3c0e-8d19-f1be774d15a7 | -4.55295 | -46.40597 | 2024-10-05 04:12:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43d50853-b25a-3d61-a9d0-ee8b6598fad9 | -4.4997 | -45.90475 | 2024-10-05 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 066bf1cc-3c7a-3645-88f7-04a5daabd858 | -4.4855 | -48.10939 | 2024-10-05 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c3791a3b-71c5-3200-aee9-b8ef85f8d5a7 | -4.48131 | -48.10872 | 2024-10-05 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e132ecb4-08ba-322c-ad4c-d56540a78ff1 | -4.41635 | -45.38006 | 2024-10-05 04:12:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 604f3d95-e5cf-34d8-b866-96e86f53360c | -4.41343 | -45.37544 | 2024-10-05 04:12:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5aedc79e-bfd2-3976-b064-33bf145b6292 | -4.38742 | -48.7005 | 2024-10-05 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0f5bdefe-e0d1-326c-9650-0664e237d6db | -4.37942 | -48.69474 | 2024-10-05 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8804937d-47ec-33c8-963d-ce34d573a451 | -4.3643 | -45.63524 | 2024-10-05 04:12:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9b42499-6094-35d2-bed3-1396d716cb37 | -4.32657 | -46.7099 | 2024-10-05 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f4e7b77-2259-3d99-8fc4-dfbe2ea70e5b | -4.32581 | -46.7146 | 2024-10-05 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc05823c-3997-3b96-983f-5a41d3eee8cd | -4.32199 | -46.71389 | 2024-10-05 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0733e549-327f-3d95-bbbf-9c5c313066df | -4.31511 | -47.70541 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2a23045-57bf-3278-892a-22140b0254c6 | -4.31105 | -47.70464 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 208afb41-ab1d-3147-a739-050510c268ce | -4.28452 | -48.07023 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd1836ad-5359-35e2-a5b3-1988f273e0ee | -4.28034 | -48.06951 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de0c0d7f-68fb-3580-88d2-d9f3660a9934 | -4.27741 | -48.06118 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38e28376-e69a-3d00-a31e-6486125797f4 | -4.27678 | -48.06499 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b8b95b6-5f41-3c3c-ad2f-9e1d0e2e8316 | -4.24139 | -47.57248 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9404dca9-f940-32be-86c0-c70225ad7348 | -4.1667 | -46.83288 | 2024-10-05 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e21720f8-1b29-36b1-b9db-0765fd49b7a0 | -4.16282 | -46.83225 | 2024-10-05 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 089a8408-cc13-394a-a0a4-fe2b196d0423 | -4.15974 | -46.82674 | 2024-10-05 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a2236fd9-1bae-379c-9c68-d5e07c4c3d8a | -4.15587 | -46.82612 | 2024-10-05 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffbff583-f23b-34e4-a78e-7ba78ca99f88 | -4.09605 | -48.27623 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2c0adae-5959-3b84-84f1-20fe87ad2837 | -4.09541 | -48.28025 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b5e7eb0-1ca8-3bca-bc84-41a904371517 | -4.09442 | -48.27564 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 976f685f-277c-34d0-8e43-324115a7d1b0 | -4.09374 | -48.27966 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 604e7659-5671-3109-a21d-79c6bc60dac1 | -4.09115 | -48.2795 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f99d1a8e-931c-306e-9163-7bfd25986df9 | -4.08369 | -47.95258 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a1d57162-7c98-3b62-8b27-71acd2f317d7 | -4.08307 | -47.95633 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9888b740-8667-3717-9b24-4a4698828edc | -4.08015 | -47.94807 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 793c8265-0660-32c7-ba8c-31809a70ffe8 | -4.07952 | -47.95189 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 78707975-4fcb-372c-8d1e-fad67597d162 | -4.0789 | -47.95564 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 26aa24b6-1f15-3bab-aa5d-de06040494b5 | -4.0766 | -47.94366 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bf6dc7e5-e890-3bb4-a611-2d00b10340e1 | -4.07598 | -47.94741 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3b113f47-1068-3846-9179-8d765e79dbb5 | -4.07535 | -47.95121 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 18b6f458-a8fa-32ee-8cfa-30dd5e3af2a0 | -4.07181 | -47.94676 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f02c85b0-3a93-3f70-beb6-d6db66cb5789 | -4.07118 | -47.95055 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5905955f-0e02-304d-9164-e0128bb2d1d6 | -4.06763 | -47.94612 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b340cbb0-9d05-31b7-93f1-d53e3bcae52d | -4.06701 | -47.94989 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 664c0e3f-f2cd-34c1-abd0-261c83c55bb1 | -4.06638 | -47.95367 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44794f1e-f0aa-3dc3-a3af-80ae098638e1 | -4.05698 | -51.11425 | 2024-10-05 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c08562fa-f638-3dca-b37b-70bc21f11369 | -4.05254 | -51.11176 | 2024-10-05 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74a202cb-5c33-3b74-aa9e-044ad75b6bb0 | -4.05205 | -51.11462 | 2024-10-05 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6001e29-2bd0-308a-806d-8800efb1929f | -4.05203 | -44.31849 | 2024-10-05 04:12:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b346734-5b73-3336-9dde-27f3afd98277 | -4.05184 | -51.11317 | 2024-10-05 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c7301d0-152b-343c-be6c-8a42c5d00476 | -4.04493 | -51.09053 | 2024-10-05 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce87f9f1-2650-30e1-9a58-a61e43934e5b | -4.0444 | -51.09373 | 2024-10-05 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e50a4e1-bebd-300c-8dd3-aabc90a09028 | -4.02114 | -50.45771 | 2024-10-05 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ee89f4bf-6d79-3c6e-a29f-3166be8bd404 | -3.98137 | -50.54305 | 2024-10-05 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db3e1e69-558d-37cd-939d-1bac99710d88 | -3.98042 | -50.5487 | 2024-10-05 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7aadfb87-e70a-32ee-930d-f87ca07c9cd1 | -3.92925 | -50.66872 | 2024-10-05 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 774b6b66-36de-364f-8755-f6ac9a447da3 | -3.92239 | -46.43754 | 2024-10-05 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3352a9df-4221-374e-b4c0-bfd827b54c1a | -3.90719 | -46.43518 | 2024-10-05 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a74d705d-cd6a-38c8-9970-86872c5a02da | -3.9057 | -46.44436 | 2024-10-05 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97484a34-679d-32c8-a88e-b30ebccafff1 | -3.90189 | -46.4438 | 2024-10-05 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42a4d25f-b84d-3934-a06c-9e0ac1568cda | -3.90154 | -48.34822 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6434134-9cdc-37fe-930e-54d5e4d14f4a | -3.90086 | -48.35236 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d876492-3d47-398b-845c-da08512c3faf | -3.89657 | -48.35162 | 2024-10-05 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7cc900bb-3797-38fd-9ae8-65e6b462939a | -3.86858 | -54.23061 | 2024-10-05 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6413157d-2c6c-31e8-8031-d2c665d415a2 | -3.86768 | -54.23576 | 2024-10-05 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2269286a-1e21-34da-8193-517084911bef | -3.85472 | -51.93314 | 2024-10-05 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16a17619-46c2-33e1-ae19-726be422c8a5 | -3.85411 | -51.93675 | 2024-10-05 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3879bcac-b977-3448-8efe-1e8f8dd1f698 | -3.84645 | -52.35851 | 2024-10-05 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e09fae2-18e0-324b-b4c2-2f26a4315533 | -3.84341 | -52.35436 | 2024-10-05 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c029f88b-f258-33ac-9d4e-c3480c5aa6fd | -3.84277 | -52.35808 | 2024-10-05 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 10ae5eae-9500-38e2-a9a1-f3df4fb3e348 | -3.84143 | -52.35376 | 2024-10-05 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1ae3fbf1-becf-3ae1-851a-129d70627b16 | -3.84081 | -52.35751 | 2024-10-05 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4dbb6297-fd03-3d4a-828a-89ac55ef5497 | -3.82349 | -47.486 | 2024-10-05 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 195db5bf-ce43-37fb-a7a8-0ebfe8983f7c | -3.82291 | -47.48952 | 2024-10-05 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README59.md)
