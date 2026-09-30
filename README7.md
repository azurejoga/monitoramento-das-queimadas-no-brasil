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
| 111b75ce-75cc-3c34-9001-7bbaaf25430c | -12.2327 | -50.2566 | 2026-09-30 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| a7560147-f87c-35e6-8060-d5b6cfc0fd8a | -2.9739 | -51.0455 | 2026-09-30 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 132.9 |
| 006e43ad-22b0-3d2a-b178-e95784b8b12b | -11.8491 | -50.4311 | 2026-09-30 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 957ba7ac-b5d0-3d25-9c32-74ac649599e7 | -11.8297 | -50.4548 | 2026-09-30 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| c8ad7e8f-4fd2-3399-9261-107a3a5fe1b8 | -5.1806 | -55.9925 | 2026-09-30 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 293d5eaa-3a36-39c2-91de-95666e0e40f5 | -7.8483 | -45.8363 | 2026-09-30 02:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 42858153-05d5-3f38-9aa2-0c791419cb80 | -8.2865 | -50.2731 | 2026-09-30 02:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 1e94ab59-c481-341a-b930-3cb6b6db599c | -7.4223 | -64.3464 | 2026-09-30 02:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| e6c6e8d2-1823-3eb6-921d-b1fead424b31 | -3.3801 | -50.95 | 2026-09-30 02:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| c35afe31-e89f-360c-9bdc-f9f7e8d8044d | -11.8488 | -50.4526 | 2026-09-30 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| c7315572-0245-34f6-86f1-3dedaf41bbeb | -2.974 | -51.0247 | 2026-09-30 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| a29d4740-9b96-3a12-b912-90d2bfece018 | -7.8297 | -45.8156 | 2026-09-30 02:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 194.8 |
| 6109ebc5-6c3d-3e6d-9a9e-77fb16599248 | -3.2129 | -46.9383 | 2026-09-30 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 3966cfbb-9a7e-3193-a424-da883f858915 | -12.3085 | -47.9539 | 2026-09-30 02:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |
| ab5ec016-cc1c-3bfc-937d-310334e3309c | -11.83 | -50.4333 | 2026-09-30 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 0a0d720d-6ed9-333e-8718-90dc7fb66c5d | -2.9082 | -54.0907 | 2026-09-30 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| b0479a60-7747-3814-959d-b11420d6f0b9 | -3.2313 | -46.9596 | 2026-09-30 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 75a1cd5b-51ea-3e35-bf59-1d2bd43701fc | -7.8486 | -45.8138 | 2026-09-30 02:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 133.9 |
| fd227c1c-67fb-3448-8fef-c95af482849f | -6.895 | -43.7066 | 2026-09-30 02:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| b8f4215d-371e-3344-8324-809d2771e38d | -7.8295 | -45.8381 | 2026-09-30 02:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 74cfbb37-8056-3f9a-a350-be0725578df9 | -11.83 | -50.4333 | 2026-09-30 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 153.5 |
| ade3c445-e713-3af3-9fed-944d1cdd1da1 | -11.8297 | -50.4548 | 2026-09-30 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.1 |
| f8168805-5085-3bb0-aeb3-b64a04db1692 | -8.2865 | -50.2731 | 2026-09-30 02:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 92b824dc-0659-381c-9f08-d571bfe4c70b | -2.9924 | -51.045 | 2026-09-30 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 11b0df85-274d-34ab-9874-a15a4d8128f9 | -11.8491 | -50.4311 | 2026-09-30 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 12a72f3a-7ca7-32dc-b6f7-d9eb402e8ad2 | -5.7561 | -45.1747 | 2026-09-30 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| e4649c35-014f-3616-a816-1d123f8d6323 | -11.7182 | -43.4386 | 2026-09-30 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| bfc59597-7437-3a31-af39-fae7f6473d0e | -12.2515 | -50.2758 | 2026-09-30 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 8727a90e-03df-37c8-aa11-5c11f273f6ae | -3.3801 | -50.95 | 2026-09-30 02:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| efe89bf9-766b-3c30-9baf-f93847818f53 | -2.9925 | -51.0242 | 2026-09-30 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 854d0455-dbf2-347f-b7ba-ffeec9fde2e0 | -12.3085 | -47.9539 | 2026-09-30 02:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 1b0afe1c-0772-3aa7-ba51-efbaa0b87c26 | -11.811 | -50.4356 | 2026-09-30 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| bd19c7ae-8fd7-347e-85a6-1a1225355df5 | -2.9739 | -51.0455 | 2026-09-30 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 76fcaf74-34b8-3df6-93cb-703359efa9d8 | -7.8486 | -45.8138 | 2026-09-30 02:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 136.9 |
| aec8c783-63b9-3eb5-8261-9b535a2d3bbe | -7.8297 | -45.8156 | 2026-09-30 02:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 203.0 |
| a92cd5c3-b98c-391e-9c2a-3b5e27a8974a | -2.9082 | -54.0907 | 2026-09-30 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| ab768db9-e52c-3678-bf2b-a80fa13c9e9d | -2.974 | -51.0247 | 2026-09-30 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 5b0fefe6-0d7e-3650-bbbd-c9d630143f4b | -7.8109 | -45.8173 | 2026-09-30 02:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 0bbbd298-0fab-3696-977d-d1c018a98dd1 | -12.2709 | -50.2519 | 2026-09-30 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| a404a03a-abbf-3bba-83cb-1890af70a708 | -12.2518 | -50.2543 | 2026-09-30 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 05534c24-7d57-362d-ab34-de67a5bdf90a | -6.895 | -43.7066 | 2026-09-30 02:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| c7679d9c-37fd-38df-b582-3d4a3af27b1d | -11.8107 | -50.457 | 2026-09-30 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| d77e9926-0a1d-3348-97a0-5da6d5bd93e8 | -7.8483 | -45.8363 | 2026-09-30 02:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 8397af03-94c1-3d1d-9ade-91c7910429de | -3.2314 | -46.9376 | 2026-09-30 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 691ef9fc-2b73-3a1c-bbc5-033396055057 | -6.9138 | -43.7049 | 2026-09-30 02:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 2533e2bd-71d4-3267-b01a-437eab0a262d | -11.8488 | -50.4526 | 2026-09-30 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 4c52cc30-f6e7-3c62-b32a-39cb8383c0fa | -12.2327 | -50.2566 | 2026-09-30 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| c4ccff3e-88e1-3f7a-8902-56710e476ae9 | -3.2129 | -46.9383 | 2026-09-30 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| c6a7dbcb-e446-326d-a6a3-b6f4069eb320 | -7.84 | -45.84 | 2026-09-30 02:15:00 | MSG-03 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 40cdbce3-2285-342f-95df-870576a9c583 | -2.9739 | -51.0455 | 2026-09-30 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 129.5 |
| c340acfc-a9e5-31d4-ac9f-a36613d3815d | -2.974 | -51.0247 | 2026-09-30 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| c345c682-8017-39d5-aa6e-40d687ff73c7 | -11.8297 | -50.4548 | 2026-09-30 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 40d12870-6709-34c2-8440-44c003577480 | -7.8297 | -45.8156 | 2026-09-30 02:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 180.5 |
| abe279a8-c213-3fe4-8d9e-3c016a845f3b | -11.8107 | -50.457 | 2026-09-30 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 0b8cdee3-5b07-3095-b96b-964735a8e62f | -3.2314 | -46.9376 | 2026-09-30 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 586df4b2-e48d-34f2-b83c-f62f8997ff25 | -2.9082 | -54.0907 | 2026-09-30 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| a048f7dc-b308-3978-a6f1-4e21f605c9bc | -12.2518 | -50.2543 | 2026-09-30 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 241eab10-b410-3144-af87-a44d71c8f694 | -12.3085 | -47.9539 | 2026-09-30 02:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 14e8fddf-a383-396d-9396-73728091e676 | -6.895 | -43.7066 | 2026-09-30 02:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| cc6c44ae-8548-3cfb-9884-ff472eb15436 | -3.3801 | -50.95 | 2026-09-30 02:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 491c80dd-afd4-35a2-aa95-0be1c9f81b3c | -2.9925 | -51.0242 | 2026-09-30 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 1eb8d5a7-b25f-39d0-9444-b4b3f3d32078 | -7.8295 | -45.8381 | 2026-09-30 02:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 052f97d8-3b77-3ade-9266-c6f8ca6da479 | -3.1061 | -50.2686 | 2026-09-30 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 653e1f75-089f-3d6e-9073-993b30ecb368 | -11.7182 | -43.4386 | 2026-09-30 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 4c4e4991-560c-3f21-bf19-b23df5263f12 | -3.106 | -50.2896 | 2026-09-30 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| a3efc0bd-30e3-3bd3-a51b-65d68776059e | -7.8109 | -45.8173 | 2026-09-30 02:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| c15b36a5-4f9a-303e-8ab0-63997a92cfd7 | -11.811 | -50.4356 | 2026-09-30 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 5e7a2dda-8f3c-3b8a-8eb0-9ea026b4f08c | -11.83 | -50.4333 | 2026-09-30 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 1e08596b-cd07-35bc-a215-3c3a6ecfa8f3 | -8.2865 | -50.2731 | 2026-09-30 02:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 7e7b3877-d5e0-350e-a59f-95bf10ee41f4 | -7.8486 | -45.8138 | 2026-09-30 02:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 63de8605-049d-3075-8161-6b84fe184394 | -2.9924 | -51.045 | 2026-09-30 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| c6da573f-1524-32cc-8157-f606f95f8e8f | -7.8483 | -45.8363 | 2026-09-30 02:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 0d4bd76c-b643-373d-b622-502372b6b01b | -3.2313 | -46.9596 | 2026-09-30 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| c70fe68f-6535-34b1-830c-dd1f36028e62 | -7.8295 | -45.8381 | 2026-09-30 02:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 7dcf0178-b2f3-3d54-aace-76c239375ced | -7.8486 | -45.8138 | 2026-09-30 02:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 8f19246d-9681-3c5b-82f0-80bd641c1f66 | -12.3085 | -47.9539 | 2026-09-30 02:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 12da70df-feae-360d-a12f-69b079fdb2bf | -2.9739 | -51.0455 | 2026-09-30 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 142.8 |
| 1b18a945-ea94-3a72-b899-b9a8d6cae284 | -7.8297 | -45.8156 | 2026-09-30 02:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 172.8 |
| d2b46f9f-decf-3db4-a285-3f649c00e4a5 | -3.2314 | -46.9376 | 2026-09-30 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| f459aaf6-606e-325f-ba8e-57410db614e2 | -2.9082 | -54.1108 | 2026-09-30 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 065792da-00c5-36c2-b0a4-fd2d70e5c378 | -7.8483 | -45.8363 | 2026-09-30 02:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 170112cd-016b-3240-ad71-13441d324fdd | -2.9924 | -51.045 | 2026-09-30 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 29ac550c-49f4-328a-9b27-d2eb23c29f30 | -12.2518 | -50.2543 | 2026-09-30 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 1564f3c3-cbfc-3a21-9b74-4502fc9aec87 | -6.895 | -43.7066 | 2026-09-30 02:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 6f592418-64f7-3fa2-90c6-42d01fdaab55 | -8.2865 | -50.2731 | 2026-09-30 02:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 77648256-7cd1-36e8-9ac7-2a4108e89a51 | -2.9082 | -54.0907 | 2026-09-30 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 91b740bb-3f7b-318c-80a8-0f435c26de3c | -20.5138 | -49.6289 | 2026-09-30 02:40:00 | GOES-19 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 37190e3c-e12b-305a-9f2f-f4fc2a415e76 | -8.2678 | -50.2746 | 2026-09-30 02:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 15aca8a2-7d62-35a7-a3a5-385ac533616a | -5.7561 | -45.1747 | 2026-09-30 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 63ec8fc0-a29b-3179-b10d-466f4a834ca2 | -7.8109 | -45.8173 | 2026-09-30 02:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 56a462f4-645b-367b-aa24-e68c64e89f82 | -2.974 | -51.0247 | 2026-09-30 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| a9a05e4c-22dc-3031-92cc-0ff4a39e9049 | -3.2314 | -46.9376 | 2026-09-30 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| d338af35-47a6-3076-9818-04aebfd27754 | -2.974 | -51.0247 | 2026-09-30 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| db1708e1-2a20-381d-999b-3a9f182d1361 | -11.1204 | -45.9147 | 2026-09-30 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.2 |
| d29a5c41-1bf6-3860-9037-9b828a5d18b9 | -12.3085 | -47.9539 | 2026-09-30 02:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 177c5f3a-cb97-3f19-8ab2-684bb009742b | -7.8483 | -45.8363 | 2026-09-30 02:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 397ec045-3af4-3825-8376-f5c2055131e2 | -3.2129 | -46.9383 | 2026-09-30 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 39fbaeef-4556-3af7-baa5-b39968ba83a7 | -7.8109 | -45.8173 | 2026-09-30 02:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| fd2b6acd-3e2d-32e2-89a7-6e7dcbc96a85 | -2.8899 | -54.0912 | 2026-09-30 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 7b777e8d-d40d-3a3b-8b87-bfc88c8b943b | -7.8486 | -45.8138 | 2026-09-30 02:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |


[Clique aqui para ver as próximas entradas](README8.md)
