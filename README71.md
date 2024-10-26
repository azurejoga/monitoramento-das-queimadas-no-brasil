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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e3a5108-2b34-3f31-b0be-1a8407fa694e | -1.69841 | -52.15441 | 2024-10-26 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61c5e4ed-24de-3e76-8be6-459826e9faad | -1.58626 | -52.37933 | 2024-10-26 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3107bc73-f4dc-362e-933b-9f074084c72e | -1.56113 | -52.02669 | 2024-10-26 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6e19f70-e0b3-3f32-aca6-8aeb2d122013 | -1.56055 | -52.03043 | 2024-10-26 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8745ef67-5a46-3de6-8ca1-0c03d5d63d4e | -1.55763 | -52.04914 | 2024-10-26 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14c54dde-04b3-37fe-a20e-972d16e9b91e | -1.55588 | -52.06037 | 2024-10-26 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ab974df0-c26e-3f92-9531-ce026ca97014 | -1.54465 | -52.15494 | 2024-10-26 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ac9e8ce5-3385-3571-92a4-0ff3f1dadfee | -1.54177 | -51.99305 | 2024-10-26 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88797a6e-0643-33ca-a534-3cd0720707ee | -1.53834 | -51.99252 | 2024-10-26 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a83367b-784d-3317-8414-e646d8b822e0 | -1.41569 | -52.10449 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58cf3c70-daf5-3adb-82cd-3372e6abbf1f | -1.41284 | -52.10018 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a6cd800-b931-3324-8581-f3152fe8c315 | -1.26828 | -52.95006 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a23562af-87c3-33af-bb70-9eea45a37aa3 | -1.26534 | -52.94541 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f2160e0-9900-34cb-a4c5-5499dfaa1295 | -0.87739 | -52.93165 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a05e2656-3c3f-3aa3-bdbe-fb23fed6d47f | -2.03965 | -52.69746 | 2024-10-26 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e53d5923-9177-3339-bbf2-d3e19cea86b2 | -1.65268 | -53.24314 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37f617af-08da-3c4f-8d28-e075061e4cbd | -1.64905 | -53.24256 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 055264bf-ccc8-3150-a88f-76ac892dc68c | -1.64839 | -53.24675 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61d05e86-9e8a-3827-be4b-50b8d5b205ce | -1.60062 | -53.31261 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95e1a35f-674d-3cd2-b7a8-b4f46f60ac30 | -1.59766 | -53.30776 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1426be17-f970-3879-af89-7a5eb781219f | -1.59698 | -53.31201 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fe186c85-7f33-329a-85f2-12b07eed90d2 | -1.59402 | -53.30719 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cf06abf-c252-3185-aff0-d1b80cd2c757 | -1.59038 | -53.3066 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 141524f7-2c9c-33d9-b5a9-c46fef9ea18d | -1.5897 | -53.31086 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ae8f34bb-2553-393d-a343-2e6fc1b07174 | -1.5782 | -53.31021 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9703eb9d-4722-3d61-b6fb-6148f8af2aa6 | -1.57809 | -53.31338 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a771d3b4-194a-31a8-a7fc-0da1a15480fc | -1.57754 | -53.31448 | 2024-10-26 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e0a515f-95a0-3237-8925-f1b420e9d08e | -3.10771 | -53.1329 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ceeb1e9c-37a7-34f5-b605-6dcc9af59f9b | -3.10604 | -53.12046 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c159797-a4e9-3f98-88ca-b169d924fdd8 | -3.0804 | -53.23621 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a75fcc5-8f2b-354b-880a-6b33fbd5ab38 | -3.0762 | -53.23967 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae7aab2a-4e6e-3dd4-86c4-d0c77596900f | -3.07263 | -53.23913 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 566a8243-9707-3414-8f6b-1455063f44d7 | -3.07134 | -53.24718 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 090f8eec-c6a5-3a1b-b131-45ab8184a2b0 | -3.0322 | -52.34653 | 2024-10-26 04:42:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 300f273e-2e39-3020-bb6e-11ad96a8df02 | -2.89506 | -53.326 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| afa1fd7e-664c-32b3-83f1-2f5995cca054 | -2.89439 | -53.33014 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3b9a069-a906-3bc9-ad20-ced45088fb16 | -2.89148 | -53.32538 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bec6741f-a28f-3d1d-8c43-a4450ec2dbd9 | -2.8908 | -53.32955 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b73cce8c-8b89-32f5-98de-653f3faf8cdd | -2.88635 | -53.31165 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8df0998-2cdc-3eed-b749-928917b7f5cf | -2.88567 | -53.31578 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 75cd325f-b1f0-3a7b-b38d-f5c30c4cf93a | -2.88517 | -53.32956 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a398de91-013b-38a0-bcf3-4d46f1d71a34 | -2.885 | -53.31993 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d4b13e4-157e-3179-91fd-26c410e4f253 | -2.88432 | -53.32411 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1484912-8dcf-3626-a2f7-b49427853fce | -2.8842 | -53.31226 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b086b801-95d0-3b1b-a95b-2b68d2fbd817 | -2.88364 | -53.3283 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a4a4a17-688a-31c8-8c35-37feae0393f8 | -2.88355 | -53.31639 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7b78a4ac-b831-3298-8ec1-4c452e1ba6a2 | -2.88296 | -53.33247 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53724f39-d4d0-3f02-b641-576a48e4ce0e | -2.8829 | -53.32053 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b2c84f3c-3e9f-33cd-9898-bd58fac55186 | -2.88276 | -53.31108 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f388aaff-e312-34a3-8dff-90dba276a18f | -2.88225 | -53.32473 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a0da4361-6559-3214-96ad-2805f6d0425e | -2.88209 | -53.31519 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e5c16ef-17a6-39e8-b307-dd6b74be2784 | -2.88159 | -53.32893 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7eca3cf-69c8-3017-ba0a-0c6390f95525 | -2.88142 | -53.31932 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95d63414-520b-3a98-9b86-6d44c24baafc | -2.88074 | -53.32347 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b054b27e-8fbd-3c81-8fb4-e469bb65f960 | -2.88061 | -53.31169 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 269c8c55-822e-358c-b75a-d44efcc7256f | -2.88006 | -53.32766 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76265bd4-31e7-3cc3-98d1-df5df8d59ac5 | -2.87997 | -53.3158 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5b0dcf4a-c487-3a8e-905a-9d6c755722c3 | -2.87932 | -53.31992 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8529ef1b-666a-36c5-bae1-aebb72ff354c | -2.87767 | -53.30702 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1be6a24e-ee2f-37f8-a90a-d4b1cf200a93 | -2.87702 | -53.31112 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bbec974b-1718-3a59-81bc-d8eb22fcac0d | -2.87638 | -53.31524 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 30d64501-abbf-39ee-a59d-46264f463ed0 | -2.87573 | -53.31937 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 774130a6-da4f-31d7-a46e-12dd7b6690d1 | -2.87343 | -53.31055 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82d07df7-d551-3496-b98b-09ba2c3d8e41 | -2.73862 | -53.1985 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14c72a5d-0b3a-3837-ac47-a2048af312c8 | -2.73796 | -53.2026 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c9e4665-f046-3269-873c-d7c16e2bd92c | -2.73438 | -53.20208 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 816c7e8d-51fd-30a5-8f1e-80b7f02763e4 | -2.68814 | -52.06179 | 2024-10-26 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c048d0e-83eb-370a-b354-ab37b91e3bb1 | -2.68755 | -52.06548 | 2024-10-26 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07f0b752-c6d6-341d-95bf-250c0c1d50cb | -2.68472 | -52.06129 | 2024-10-26 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94dbf4ca-40d7-3965-8d19-b4849d43f1a2 | -2.68414 | -52.06495 | 2024-10-26 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2730c49-396d-3037-8176-caddb0676c77 | -2.62284 | -52.4494 | 2024-10-26 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65eb3804-41bd-3640-9f0a-764355fb83fd | -2.62223 | -52.45318 | 2024-10-26 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ce756ac-7bf0-3c46-ae2e-ef32d2f55256 | -2.61998 | -52.44507 | 2024-10-26 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67c66dcd-bf50-37fb-b05b-eb0cc3951760 | -2.61938 | -52.44885 | 2024-10-26 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 80498731-0c42-36bc-8467-9786dbe1c16b | -2.61652 | -52.44453 | 2024-10-26 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 710d2176-d6b5-3cea-a936-27387b650899 | -2.99966 | -53.44208 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c8968d8-c1d9-3688-a311-8e849bbaacca | -2.97785 | -53.26774 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac5802e9-916b-3047-9704-05bc6d92fd34 | -2.97428 | -53.26714 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2b47b7be-a08e-3968-9aca-9c4582d1743a | -2.97071 | -53.26654 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1be8f594-aef1-3fd0-8c9b-4f98dedf1617 | -2.97006 | -53.27066 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5d002f5a-3a14-3414-85c2-8b59443d941d | -2.96714 | -53.26594 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c9f8d84-57f4-3074-b11b-bee0a15c736d | -2.96649 | -53.27007 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 627794a4-d6ad-3347-9bff-4b3a76811a1d | -2.95505 | -52.56633 | 2024-10-26 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73d20655-65fd-35e6-8602-e3c91cfc8a73 | -2.95445 | -52.57013 | 2024-10-26 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c5ef9788-56f1-3870-992b-39bf36c50039 | -2.95384 | -52.57394 | 2024-10-26 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f4be08d4-aedf-3f1f-ac2f-69ec06066051 | -2.95158 | -52.56579 | 2024-10-26 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79a4f628-3089-3796-8721-02174a53bef6 | -2.95098 | -52.56958 | 2024-10-26 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7b1b15a7-d917-31f7-b46c-4dc8a49bbaf2 | -2.95037 | -52.57339 | 2024-10-26 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 94ca92d3-afdd-327b-8f27-52dde26f0d50 | -2.94872 | -52.56148 | 2024-10-26 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d3fc23c8-f435-3cce-af1f-1320fe1b6f82 | -2.94812 | -52.56527 | 2024-10-26 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 387ff4b2-c01e-352d-9680-ac3bc0c93468 | -2.94751 | -52.56905 | 2024-10-26 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 416d0ce5-bb07-3e6a-91e6-278db83ae936 | -2.94691 | -52.57285 | 2024-10-26 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 1dc41ec1-5185-3f3f-bbbd-290a9ef59511 | -2.94525 | -52.56096 | 2024-10-26 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 69cfa046-0e39-3c44-8744-f4f07a90d3b4 | -2.94465 | -52.56473 | 2024-10-26 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 617fb36d-c5ea-3a12-8373-e6c47df3b8e2 | -2.94404 | -52.56851 | 2024-10-26 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| ccefbe07-0e0c-3820-b36e-b98ac7477e6d | -2.94344 | -52.57231 | 2024-10-26 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| b0f720db-b570-346d-8428-ec059b118264 | -2.94339 | -52.98231 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b5033e8-f430-3503-8b71-66bb8c6f025c | -2.94276 | -52.9862 | 2024-10-26 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 067cbcd2-ef13-3fb9-9c62-5f1fb4908e21 | -2.94118 | -52.56421 | 2024-10-26 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ca3f7cf-c0bd-336a-8d1b-df730ec96b17 | -2.94058 | -52.56798 | 2024-10-26 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README72.md)
