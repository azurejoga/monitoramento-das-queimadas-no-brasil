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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1eb2eae-0746-3bda-8326-72436be28cb6 | 2.00105 | -55.66951 | 2025-12-11 06:33:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7339673a-d9e8-3340-accb-68fa38960832 | -2.28853 | -45.57193 | 2025-12-11 06:35:00 | AQUA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 48249a41-cf6b-3dd1-95c3-c017edd71c3f | -2.20937 | -51.89169 | 2025-12-11 06:35:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 56ea6641-ea08-3dc1-9b8a-91f4b4b5bf44 | -3.22948 | -47.47643 | 2025-12-11 06:35:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 61612566-0698-3024-a6eb-947b1341f3a5 | -1.8017 | -54.05598 | 2025-12-11 06:35:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a67c41db-32ec-36bc-aee9-94bd7913b088 | -1.30306 | -53.48343 | 2025-12-11 06:35:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0ca3bfb1-1420-355b-8a3f-384ff66b90ae | -2.68954 | -51.64515 | 2025-12-11 06:35:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 37e0ed89-904e-3d9a-a81a-a4e19e74041b | -1.58721 | -53.75494 | 2025-12-11 06:35:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 80f7ce2a-b0b5-34b9-a93e-b709fcfad99e | -2.28786 | -45.6035 | 2025-12-11 06:35:00 | AQUA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 46.6 |
| b59bfc2e-4d9f-3bc1-abf9-690f3c509d5e | -2.28472 | -45.59796 | 2025-12-11 06:35:00 | AQUA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 74975002-3067-3c1d-9282-e0928a0e6680 | -2.08367 | -52.04704 | 2025-12-11 06:35:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9dff709b-e27b-340b-a496-2d0495086ce3 | -3.23282 | -47.46432 | 2025-12-11 06:35:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 0e564629-bd82-3248-8d76-b4e58e630684 | -2.65282 | -51.63982 | 2025-12-11 06:35:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f76193a3-0a51-3b34-9c6f-01e350c54f10 | -3.2323 | -47.45734 | 2025-12-11 06:35:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| ba2cd51f-6522-3992-aa66-b613f554b6ec | -2.29148 | -45.57745 | 2025-12-11 06:35:00 | AQUA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 42d8a8a7-c729-3624-82fd-8bb98e266419 | -2.01948 | -52.04704 | 2025-12-11 06:35:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 80cd5d53-d221-3a92-80f9-d9a1252381ba | -2.93717 | -53.01665 | 2025-12-11 06:37:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9d102c0b-2d00-3ee1-b39a-ee6c34e70e1c | -3.75343 | -45.45932 | 2025-12-11 06:37:00 | AQUA_M-M | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 638b94d2-0a07-394f-b1c1-13fb8ca98fbe | -3.74946 | -45.48747 | 2025-12-11 06:37:00 | AQUA_M-M | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 764.6 |
| 54509935-c55e-34d7-84c3-f2f4361d2b11 | -3.74549 | -45.51555 | 2025-12-11 06:37:00 | AQUA_M-M | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 525b3cf6-2f16-36a8-a8d2-a17cd25aed19 | -2.93585 | -53.02544 | 2025-12-11 06:37:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e533b6a9-bb4c-34a7-9214-e4dbe04e97f1 | -3.7588 | -45.5168 | 2025-12-11 06:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 494d074a-5999-3141-9d70-1b2607025c4c | -3.7402 | -45.5177 | 2025-12-11 06:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 107.2 |
| d0e90ab9-5aea-311c-b87b-1aeacc2061df | -3.759 | -45.4719 | 2025-12-11 06:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 98.7 |
| d14c04a8-449f-30c0-afa8-a25a7e1d4202 | -3.7589 | -45.4944 | 2025-12-11 06:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 301.6 |
| c4a4a44a-4608-369e-8bfa-bf0107954780 | -3.7403 | -45.4952 | 2025-12-11 06:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 359.9 |
| bd3620ca-eab8-300d-91b2-5d320d18ac42 | -2.2906 | -45.5933 | 2025-12-11 06:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 3afb4f24-e28c-3923-ad9a-5bd03f9faed3 | -3.7404 | -45.4728 | 2025-12-11 06:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 5db78ed6-6376-35cc-8067-58509d02bff4 | -2.2906 | -45.5933 | 2025-12-11 06:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 24a0ca6d-7220-3e71-8dd8-a51a391410e9 | -3.7404 | -45.4728 | 2025-12-11 06:50:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 40a11879-26b2-3b3e-95a7-6cf06c34a028 | -3.7588 | -45.5168 | 2025-12-11 06:50:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 26dadbae-46aa-33ff-b3c0-4a55cf5462de | -3.7403 | -45.4952 | 2025-12-11 06:50:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 347.3 |
| 961de249-8d47-3e81-92b7-0da76182b85f | -3.7402 | -45.5177 | 2025-12-11 06:50:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 97.0 |
| eb1bbf75-7069-312b-af8b-a8dda020a010 | -3.759 | -45.4719 | 2025-12-11 06:50:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 20098f98-8dcd-3cc5-97c7-fa99eaa97bbf | -3.7589 | -45.4944 | 2025-12-11 06:50:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 317.5 |
| 05ce66e6-720f-3abd-bb9e-cb090b578a0a | -3.7402 | -45.5177 | 2025-12-11 07:00:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 154.8 |
| e0e4cb74-f74f-3f60-8375-8b2ce87c81ea | -3.7403 | -45.4952 | 2025-12-11 07:00:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 377.1 |
| 3093164d-3c01-3777-b1ad-34ad92349d86 | -3.7404 | -45.4728 | 2025-12-11 07:00:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 1641bfd9-194c-31f6-bfdd-7a74d1de0f25 | -3.759 | -45.4719 | 2025-12-11 07:00:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 6ee84390-68fd-311b-ba01-36337e332b15 | -2.2906 | -45.5933 | 2025-12-11 07:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 26fe2fc5-d95f-3076-bc5e-7afaca59dc06 | -3.7588 | -45.5168 | 2025-12-11 07:00:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 123.1 |
| c92e91fd-d7df-31a3-97f5-223c1f74c0e6 | -3.7589 | -45.4944 | 2025-12-11 07:00:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 316.0 |
| df01aae9-dec6-3e72-92be-4a878d13d5d9 | -3.7402 | -45.5177 | 2025-12-11 07:10:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 6652590d-bf80-312f-804b-61cc8c02ae5a | -3.7589 | -45.4944 | 2025-12-11 07:10:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 313.2 |
| 679bb70b-d242-3f01-a812-3807896863b9 | -3.7588 | -45.5168 | 2025-12-11 07:10:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 112.9 |
| ece1a369-495b-30d7-886d-2b01ce7d8328 | -3.7404 | -45.4728 | 2025-12-11 07:10:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 94.3 |
| ea37dd52-0977-3b99-852a-ae42f1bab356 | -3.759 | -45.4719 | 2025-12-11 07:10:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 705009f1-b999-3404-a490-54f060ab19b8 | -2.2906 | -45.5933 | 2025-12-11 07:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 61f5df1a-6d03-30e4-ab9c-e198910734e6 | -3.7403 | -45.4952 | 2025-12-11 07:10:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 356.3 |
| 7e81edbc-0ac3-3403-8764-c495c5bfb6b5 | -3.7403 | -45.4952 | 2025-12-11 07:20:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 355.6 |
| f6b55d6f-b1d4-37db-92ed-e65bde196a0c | -3.759 | -45.4719 | 2025-12-11 07:20:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 126.8 |
| f6f6efdb-f0eb-34fb-aa41-8695f27121b5 | -3.7404 | -45.4728 | 2025-12-11 07:20:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 3d4d0345-4051-3403-ab37-a654f287cda8 | -3.7402 | -45.5177 | 2025-12-11 07:20:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 8b88c965-66c9-3222-a2e6-035135dfdf38 | -3.7589 | -45.4944 | 2025-12-11 07:20:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 646.8 |
| 21fee6d3-2a2e-3adb-a49e-4a61079c5618 | -2.2906 | -45.5933 | 2025-12-11 07:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 51.9 |
| a5c8c7d9-2ae9-31f6-ba21-210d08fa7ff0 | -3.7588 | -45.5168 | 2025-12-11 07:20:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 148.9 |
| 14c0544a-6f90-302b-ab5a-fe7413e7ae56 | -3.7402 | -45.5177 | 2025-12-11 07:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 116.7 |
| e929ca2a-ff30-34e1-b9c2-def6e778ee88 | -3.759 | -45.4719 | 2025-12-11 07:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 5c0229ed-999a-3ebd-8f4e-df5ed7b62522 | -3.7588 | -45.5168 | 2025-12-11 07:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 60cd3179-20e7-3bf7-b830-903c6060f397 | -3.7404 | -45.4728 | 2025-12-11 07:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 98.6 |
| dbc751de-c9e8-349f-8e79-5be851626f87 | -3.7403 | -45.4952 | 2025-12-11 07:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 370.4 |
| a6502fef-fc87-3a05-8315-f7d55ed51d80 | -3.7589 | -45.4944 | 2025-12-11 07:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 491.2 |
| 7b220a6a-d652-38c7-82f8-22a764a45bb8 | -3.7588 | -45.5168 | 2025-12-11 07:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 76.2 |
| a843195d-9294-3613-94d0-d851917fbcc1 | -3.7404 | -45.4728 | 2025-12-11 07:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 151.0 |
| cde3f44e-f873-3ac8-8bab-a80a918fa1c0 | -3.759 | -45.4719 | 2025-12-11 07:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 3121481c-48e0-3769-9ea5-69cce2a9c449 | -3.7403 | -45.4952 | 2025-12-11 07:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 383.1 |
| 37089b16-9410-3936-903e-eba3f8f533d7 | -3.7402 | -45.5177 | 2025-12-11 07:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 67dccf6c-9515-311c-b0a0-ca07f30bfeb2 | -3.7589 | -45.4944 | 2025-12-11 07:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 284.2 |
| e5595926-7fbf-3e5f-b67d-40d139b5f979 | -3.7589 | -45.4944 | 2025-12-11 07:50:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 362.7 |
| 72c36670-6675-3b45-af97-e4359ea33c1f | -3.759 | -45.4719 | 2025-12-11 07:50:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 3e5316e0-e0ae-3702-bdd8-c2e65b3bb7f2 | -3.7588 | -45.5168 | 2025-12-11 07:50:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 7a207315-82bd-3dd1-8632-35a8060deea9 | -3.7403 | -45.4952 | 2025-12-11 07:50:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 447.1 |
| 536f5451-31e7-3c45-8ea6-206130839ccb | -2.2906 | -45.5933 | 2025-12-11 07:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 39.5 |
| b975ab9d-9b72-32a9-9372-876d4340cd9b | -3.7404 | -45.4728 | 2025-12-11 07:50:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 164.0 |
| 7115b6a0-fbbd-38b5-9c87-0c7546e7b103 | -3.7402 | -45.5177 | 2025-12-11 07:50:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 97.4 |
| d66bbffd-1613-3a00-bdab-df7c96c17be4 | -2.2906 | -45.5933 | 2025-12-11 08:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 44.0 |
| cbfc0df5-7a7d-3e42-adc1-ec45b3c1b65e | -2.2906 | -45.5933 | 2025-12-11 08:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 37.3 |
| b3c958af-a9a1-3660-a24a-cd2b03e3d038 | -3.7403 | -45.4952 | 2025-12-11 08:50:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 138.2 |
| 37528a80-b4a0-3390-9c6c-cfe46f4036d1 | -3.7589 | -45.4944 | 2025-12-11 08:50:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 0fa6579c-429d-36d6-90fe-8f63096e76f0 | -3.7589 | -45.4944 | 2025-12-11 09:10:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 0df6702c-296a-3d88-88ea-f3558b7edf25 | -3.7403 | -45.4952 | 2025-12-11 09:20:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 101.6 |
| c40c0b20-602f-3b2e-a7ea-1d2fd2039529 | -3.7589 | -45.4944 | 2025-12-11 09:20:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 7f463c0b-d3c5-362b-a080-858c1f304494 | -3.7589 | -45.4944 | 2025-12-11 09:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 150.5 |
| c1197b40-eb9c-36ef-9f21-990ca1ba6666 | -3.7589 | -45.4944 | 2025-12-11 09:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 7ffdda09-d1a9-3e09-846b-4c169522418f | -7.92534 | -37.63269 | 2025-12-11 11:00:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 45.9 |
| eab0dde9-ebb8-358f-b737-15978152fb5c | -7.92077 | -37.63874 | 2025-12-11 11:00:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 189c53cf-555e-373e-aa02-96437e8ec448 | -4.3897 | -43.0562 | 2025-12-11 12:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| e95e6891-cad0-3492-80eb-32581104fa69 | -4.3897 | -43.0562 | 2025-12-11 12:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| a986f586-139d-31d3-9963-aa3bd5302986 | -4.3897 | -43.0562 | 2025-12-11 12:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| b04a19af-d547-304c-a167-67f65b559b96 | -1.31239 | -53.48317 | 2025-12-11 12:33:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ff8df650-2fce-3c34-9568-a50ba7485e2f | -2.0897 | -52.11434 | 2025-12-11 12:33:00 | TERRA_M-T | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a8a41e52-82e2-37a0-8c2b-21e4aecd7d54 | -0.73467 | -49.45766 | 2025-12-11 12:33:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 966417e1-b9b9-36e8-b0d3-196bdbe0b7cc | -2.03997 | -47.42647 | 2025-12-11 12:33:00 | TERRA_M-T | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 8596078e-70cc-32f4-89f7-82cfa8b5c373 | -1.43022 | -45.66254 | 2025-12-11 12:33:00 | TERRA_M-T | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 9e55749c-53d7-3b7e-a609-ae33e9bdb9fc | -1.59568 | -53.75656 | 2025-12-11 12:33:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fdc3106d-bdb0-3f3f-bd4d-e4b367014732 | -1.11677 | -53.68992 | 2025-12-11 12:33:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f650b410-a75e-32d2-8623-35b60a7f2894 | -1.06446 | -48.13894 | 2025-12-11 12:33:00 | TERRA_M-T | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f25bf7a1-bd11-3474-9828-0a585bd6a1c7 | -0.72659 | -49.44597 | 2025-12-11 12:33:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 31539621-a3c7-3879-80ec-4c315d0c0aa9 | -1.95031 | -49.91988 | 2025-12-11 12:33:00 | TERRA_M-T | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f35d5096-e022-3840-aa3c-cfff37ecbe8f | -0.73613 | -49.44729 | 2025-12-11 12:33:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |


[Clique aqui para ver as próximas entradas](README19.md)
