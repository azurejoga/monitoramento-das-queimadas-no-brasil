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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 919b9584-8875-368b-819f-d94e486d9c0e | -1.08377 | -54.11154 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 73251823-657a-31c0-8cd3-eeaf077dae94 | -3.5948 | -54.59386 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 16bd45ea-5056-3cc5-9cde-21d1b5cc1cdf | -3.54354 | -54.69189 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc017b8f-d5c4-30c8-9440-b0661f559912 | -6.50083 | -44.36317 | 2026-10-10 04:44:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1a5f56b9-86af-322f-ae90-a3e4bdddda5e | -1.27609 | -55.75068 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddc5cf57-9531-3ee5-bd96-7cf87c1ac39f | -3.80609 | -49.93316 | 2026-10-10 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 48ae10bc-b96d-3afd-8310-9a0cd3615a9e | -2.89131 | -54.06696 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 81252c6d-9941-393b-848a-92c3ac217c43 | -3.54115 | -54.74408 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b8632659-2b3f-3d0e-a3d7-e8f2179ec6f2 | -3.43237 | -54.54269 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 39cd5681-3064-3f32-86e3-79fbab8adb6c | -3.35128 | -50.41132 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c41964f-907e-3994-9c68-1b32c0d0cc69 | -6.06862 | -44.65945 | 2026-10-10 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 433c59cc-be4d-3e7f-8757-ed482f75594a | -1.79579 | -47.84987 | 2026-10-10 04:44:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08c4b536-b28e-3443-ab97-939f42e3ebbd | -3.12597 | -54.1802 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 3fd66baf-4730-349b-8d16-e93764bfe98a | -3.31274 | -54.02133 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ad7ef12-6bf5-3bb2-9587-dc15100d0897 | -5.08588 | -46.21404 | 2026-10-10 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9853332-08e3-356d-b0b3-cacd9d4cf7a0 | -5.71214 | -53.47775 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03d930d7-f16b-3ec7-a8ab-664f348e67ac | -5.58707 | -47.28482 | 2026-10-10 04:44:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca742369-f8ad-3ff8-82ba-6e900c6559f4 | -4.50281 | -47.14578 | 2026-10-10 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8f1a41d-d737-3d75-9a89-5325a3c6121d | -3.20592 | -50.54905 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbbd3f69-d127-3174-b654-a8023ec22288 | -4.10011 | -54.01381 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d1576089-4920-3804-b871-668db284b1b3 | -4.59554 | -55.7208 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2431755e-4df4-385c-ae3f-e20ac37b03d7 | -2.5245 | -46.8017 | 2026-10-10 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b502a53-2e9d-382a-9e0e-43c2059052b7 | -3.19847 | -53.85942 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7f2bffa6-329d-3050-ab4c-bc4b4630a889 | -4.12785 | -46.86642 | 2026-10-10 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 22b0c897-0bef-3c47-a66b-c6b244854ed7 | -3.27207 | -50.39624 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 048a5cb4-6bf4-3101-aa9d-34d4277c8841 | -1.76524 | -55.69902 | 2026-10-10 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c3b2e56-b325-31f2-aef1-f54cc2c4d140 | -3.251 | -50.41031 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5eae0832-fe5d-373b-b68c-0ae207d35d2c | -2.93186 | -54.05377 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ad9028f-c52a-38df-9101-6662ab74ca56 | -7.23962 | -44.17366 | 2026-10-10 04:44:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb0ef14d-d2ef-3c60-ac5a-0a55ecd873c0 | -6.51838 | -43.39209 | 2026-10-10 04:44:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a912cd2d-2bd4-30f2-8c3f-196c1a498817 | -1.64877 | -55.20205 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b652be3-7eb2-3d82-accc-8b1f2c1bfb9d | -1.96315 | -54.38657 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 808de401-5212-3379-98c4-b11d8094fcd3 | -2.61176 | -59.98675 | 2026-10-10 04:44:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c57b4036-dc10-3800-8c49-bcd3f498bd8c | -0.9717 | -52.45771 | 2026-10-10 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da573d53-6695-3ce0-9051-db0cbb6c0658 | -4.45335 | -47.92331 | 2026-10-10 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3235b10e-c8ce-3b74-9749-074aa0c3bfd0 | 1.05824 | -50.03469 | 2026-10-10 04:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7796952-6e56-31dd-a6af-0602d578be50 | -3.10617 | -50.31004 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bb4a742-0a36-3d28-993c-a6cc383b2b7e | -5.79608 | -53.79916 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e906a07-308b-33b0-9b0d-be5e4fcea61f | -1.21161 | -55.65627 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ade75a1-3907-3501-a115-54c46741a0f5 | -3.1766 | -50.58907 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 051a4f2a-eb14-3db6-8b72-f9b1bc36c21b | -5.8806 | -43.41039 | 2026-10-10 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| facb3d2c-7d14-31c7-8943-f7e32562004f | -3.03765 | -50.34458 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e6b6c2ca-75fd-3eeb-b4ba-63cfc8e537a7 | -5.59317 | -47.28934 | 2026-10-10 04:44:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e48e1fc-5da0-365f-aa4b-261aedb8ef48 | -3.46899 | -50.07825 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ff02645-a77a-3859-97fd-8a751498575a | -3.87402 | -52.25787 | 2026-10-10 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1ad96e1c-52d3-3165-a7de-f87b27995f82 | 0.99898 | -51.10047 | 2026-10-10 04:44:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a9ed5377-46d6-3e33-9f22-3b9c59553d2d | -5.56059 | -43.96503 | 2026-10-10 04:44:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3823b531-76e6-3813-b8d9-51c95e40fd59 | -3.09028 | -54.30616 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7ef39db-eee7-3a3e-80cf-932cf286b31f | -3.10732 | -53.7895 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 80f6978a-2a5e-31d6-b72f-19448340847d | -3.27356 | -54.70131 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a50d243d-de8b-3c92-8908-4c22a6dcfc9a | -2.45709 | -47.58299 | 2026-10-10 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1dcc333a-d68f-35dc-91a8-014e1347e60f | -1.02183 | -52.43093 | 2026-10-10 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 32481b67-aa29-38c7-95f8-9a4ea3404382 | -3.54924 | -54.68757 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bcff91f3-6da8-3105-9f05-396b5c10ef86 | -6.43766 | -43.50799 | 2026-10-10 04:44:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db47d21e-8158-3c66-9e26-5503e5129fe7 | -3.73616 | -58.49951 | 2026-10-10 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 4a5aad60-d73a-37bf-af61-68d8feb435a1 | -3.31504 | -54.03626 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 25fb2cbe-e6e3-3bb8-af4e-bc3578a20245 | -4.29437 | -48.60402 | 2026-10-10 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41059a08-18a7-38fa-b60f-1c18fca1fa4e | -4.40344 | -43.12086 | 2026-10-10 04:44:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ddc5227a-7523-3498-bff6-885077617b5f | -3.4742 | -50.09161 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 90dae774-a025-3221-8e5a-49f439238be8 | -3.3127 | -54.67516 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fb64a321-a698-30e6-ad47-8608ff7435e4 | -2.38949 | -57.90112 | 2026-10-10 04:44:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91414ebb-a811-3af7-bfdb-c16e61d8f47a | -2.23803 | -51.92845 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2060ffc4-cad4-3ff1-a387-d7f41022a1cd | -2.99577 | -53.89771 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f4227c0-5504-35c3-8d2a-f10f38936b84 | -5.88131 | -43.40572 | 2026-10-10 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b6285c7-1397-3fe3-ad00-248d6fdd1791 | -3.11826 | -54.16878 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| daaba2d2-1f57-3a45-a005-a9f5c4e75150 | -2.85964 | -51.2763 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e0fb0e2-f405-31fd-8255-ecb6aa201f7d | -3.46823 | -50.59291 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 369ce853-0008-337a-b21e-f40a82c9c2e6 | -3.16556 | -50.45547 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ee2267d-cd58-397d-82a9-e459a438ad5f | -4.3996 | -43.12027 | 2026-10-10 04:44:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3758359-b092-323b-a7d2-9b8936cb2141 | -3.58821 | -54.72088 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43e11666-93f1-3532-b2f1-329f36bcc7e8 | -4.2265 | -46.9281 | 2026-10-10 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 518e09ff-f580-32de-a87b-d9b03065c243 | -1.21643 | -55.66039 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1a6c9885-cd59-33b4-ad5c-5f0d7a52e6ce | -4.17435 | -48.74432 | 2026-10-10 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19be071e-6cc4-3a67-9873-922e6c49bc4d | -3.18244 | -50.57658 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9e49b7b-2512-36e4-828d-ce17fc22c643 | -3.90825 | -59.59093 | 2026-10-10 04:44:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae9237ea-c150-3c6c-991a-936ad4eeb24b | -3.13396 | -54.36524 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a7f8de7-54e4-372b-a43c-e64d89572b4d | -6.43209 | -43.50903 | 2026-10-10 04:44:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c5314a6c-3eba-35dd-b516-94b117192ea9 | -4.28429 | -48.5804 | 2026-10-10 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07bf7b57-ae10-3808-8039-3dc85dd79548 | -3.18031 | -50.58967 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1888c22-5cb6-3592-87d8-451ad6fe260b | -2.43744 | -55.98542 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5bf43022-0d75-36bd-9417-661fca7618b1 | -4.40836 | -49.78244 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4b15bdfb-98ab-388c-9046-32167e5f9e38 | -4.16564 | -54.54366 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f3af768-4c8e-3029-a3d4-7f0eda6b0ef7 | -3.12371 | -54.16494 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f54a4479-39db-3a88-9a96-ecec6a66ff2a | -3.74158 | -58.49801 | 2026-10-10 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 2a32c7d2-f1d6-3233-bb77-d81632d31ac4 | -3.59786 | -54.6049 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 45ee77be-3723-3b72-94ae-95129ed985a3 | -1.96144 | -54.39716 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7cd54848-c9c0-3b77-96a8-0e4504becf24 | -5.95875 | -48.91874 | 2026-10-10 04:44:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0fafb0e6-5bb4-3054-9c0f-dd073edb986a | -3.21772 | -50.54648 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1569d56e-58dd-3014-8ff5-a0c7b6b3d4fa | -5.79535 | -53.80347 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27aa7a66-f3b8-351a-9e45-4addae8e3026 | -4.45391 | -47.91982 | 2026-10-10 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e67bce60-8ecf-37ef-af34-645302269386 | -5.35922 | -48.56417 | 2026-10-10 04:44:00 | NPP-375D | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4fa3fd2c-7cec-3279-8523-8a18fe55eb15 | -3.18816 | -49.2519 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2afd7df-98d0-3d5e-89e6-8e99848c479c | -4.41089 | -49.76685 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 247338da-ea99-3749-9220-4932e288ef03 | -2.47314 | -56.08354 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06a58395-8619-39c4-a3bc-a7d04cfe22b4 | -5.95537 | -48.9182 | 2026-10-10 04:44:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9dadac07-58e8-32cc-8b04-29de74f24ad3 | -4.72535 | -55.65308 | 2026-10-10 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f02db931-a0cb-33ed-b377-0222a146c795 | -5.78664 | -53.80181 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fdc11b0-beaf-34e3-98fa-89a21a6b2096 | -3.17289 | -50.58847 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8410970-49fe-3d46-ba2e-7866bdc6f5a7 | -2.56692 | -57.41663 | 2026-10-10 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 57fddb6c-c4ff-3422-9091-24d6d830e21d | -3.22749 | -49.43142 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |


[Clique aqui para ver as próximas entradas](README60.md)
