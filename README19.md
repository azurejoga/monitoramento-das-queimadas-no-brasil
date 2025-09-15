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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5470d5fe-9bb2-3f97-8130-be3da53f8205 | -5.78199 | -43.74216 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 849d07ad-8f10-38dc-ac46-70445a731452 | -7.85966 | -46.1194 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cd300256-da69-38e5-8145-7c5c57d036a1 | -7.36746 | -44.35386 | 2025-09-15 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d6620ba4-7ed4-33f3-b018-26ae49736485 | -8.97439 | -46.21573 | 2025-09-15 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 56b61a66-41e4-3e33-8850-cc8cd835aee5 | -8.64696 | -46.36894 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d934694-1b4d-3441-af08-95e998c7a03d | -8.59672 | -46.3647 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee5fe88c-cf28-3382-b535-c511d9ffb1e0 | -8.63367 | -45.72414 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4018840-84ef-376a-b178-3aa8fb9f4eac | -7.39207 | -49.99387 | 2025-09-15 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d75faee-590b-36f0-a314-60a86ea27a01 | -7.69923 | -44.66952 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c4035d0-90c1-37ec-8e45-464978c1b324 | -8.42785 | -45.7337 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a68723b6-da03-3eab-a0e0-8738ebf36c9f | -4.11346 | -51.09326 | 2025-09-15 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c163d14-9080-3c7c-8ffa-3af293e51323 | -7.88848 | -43.57005 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 28.0 |
| d39bbbd8-f63d-31f0-b349-a673435e7544 | -7.87278 | -43.58249 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 889ec498-a611-3e6b-bdec-0713dc324bc3 | -8.9634 | -45.79128 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 267eff91-1484-3a86-9cc4-1d4db2cd061f | -9.08832 | -44.81452 | 2025-09-15 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca8bd699-3ca2-3ec7-8a5a-e7c2c84d4b2a | -8.76597 | -46.07029 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| eb237076-6391-39cb-98f5-81de2b7665de | -8.91727 | -45.49937 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d29f0fd8-51b9-3250-8e5c-889a3c5774cf | -6.31408 | -43.57887 | 2025-09-15 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a709db8b-d8ea-3c79-9171-b35be39a5e3d | -6.63587 | -44.74942 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea08c9d6-0ec8-3c79-af40-20b035ddbcbd | -7.84415 | -46.10965 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24de7e10-b658-3a1f-b5de-216112568d45 | -9.02251 | -47.02283 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ea31387-2e35-3978-b56d-89e5fa6d1f77 | -6.08137 | -43.15054 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2b46fa33-bc27-37f5-b84e-d338800d4d61 | -7.02257 | -44.53794 | 2025-09-15 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7665cf23-112c-3cae-b10a-f4b2378b190e | -8.20666 | -45.58037 | 2025-09-15 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 172a1e3e-c0e1-39a8-98cb-c23e9dffb387 | -5.60169 | -42.89939 | 2025-09-15 04:19:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 41d10458-d95c-3e12-9c82-cbf75fb040ed | -6.13359 | -43.38309 | 2025-09-15 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e737151a-8633-347d-99b5-7518a5540c64 | -6.18049 | -41.18517 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7217aa04-2a4a-3309-8826-2e8bdd8710ff | -5.73506 | -43.19017 | 2025-09-15 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5287ced6-d973-3fef-99e9-8569dc6f353c | -8.98653 | -45.81639 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9f970c8-3fea-3302-87db-c1ac72a753ca | -8.93858 | -45.79451 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a41f6ff-acb2-30fb-bf8e-bc36bc5eff10 | -9.24218 | -45.6617 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ee80fcb-5884-3d54-bedd-53d8a1b14a3b | -8.65086 | -46.36592 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af4fcb53-b02e-3c00-9abc-f6b034b5902e | -8.7737 | -46.06437 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a96c5ef2-7aa3-3b10-ae99-e6df9b23be6a | -8.9777 | -45.76504 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bde38116-4196-32c1-8a59-1a69e651318b | -7.88965 | -43.5851 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 7fe69b63-8251-3d11-8439-c01e06ade1c5 | -7.79333 | -46.15179 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c0d9b1d-5e54-3b92-a154-d602c628eada | -8.90187 | -45.48982 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac6e2ae7-c790-3df9-9b84-f54b2b1d0428 | -7.40805 | -42.08692 | 2025-09-15 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7e0e45e2-f2e3-3094-add5-4aa0d2d6af6e | -7.692 | -48.86639 | 2025-09-15 04:19:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c10a0abf-8adf-3545-945c-f9c58505b27e | -7.68904 | -48.8613 | 2025-09-15 04:19:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ebb9f07d-5ebf-3af0-b63d-0b8b1513a75a | -4.34644 | -46.47353 | 2025-09-15 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd978e3b-bbe5-3f6c-99b6-431d17102b78 | -7.39666 | -49.99104 | 2025-09-15 04:19:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05d3973a-db96-3e80-9672-e043ce28f14f | -6.93928 | -44.79043 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfb0148e-15c2-3543-ba4a-00d60f16930b | -8.14521 | -43.67532 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f04ed4f-4df7-3328-876b-27865637a200 | -7.88455 | -43.57317 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 9f8a7e77-8e94-35eb-992b-e9c2e1a7e1e7 | -6.40902 | -42.61649 | 2025-09-15 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 766318df-7b1c-3815-a98b-1f7930be45c3 | -8.2131 | -45.58568 | 2025-09-15 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc5e67fe-0bca-3f8e-a4e0-0b118125b157 | -7.85024 | -46.11424 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab3fea05-69f9-3a79-888e-65bf97b2114e | -9.00604 | -47.03897 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f244ca14-66f8-360c-b799-27bc831e4b17 | -6.40671 | -46.94482 | 2025-09-15 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f39c792f-5e47-3e3e-8535-f608d1c288c4 | -6.97032 | -44.5476 | 2025-09-15 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e508aefa-ec03-3810-a96a-248e41b04d21 | -7.36961 | -44.33997 | 2025-09-15 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdacbf64-9759-3e2f-8381-c12865a03a60 | -5.75669 | -43.90637 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 501ff43b-0bf9-35f8-a416-96ba4a71f37f | -7.86002 | -43.58769 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ff14416-810a-3d98-9f69-fb57a090508b | -8.4225 | -44.96561 | 2025-09-15 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf481524-d152-313d-b1b5-e128523e6f43 | -6.11285 | -44.50461 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 15f8e624-6f4d-38a7-a111-b004388c88f1 | -2.57729 | -48.39652 | 2025-09-15 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d79d819-36c5-3409-95b2-7b08bfa39d19 | -6.64301 | -44.747 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1af239c7-6aac-30e4-be06-7ab146c2fecc | -8.14858 | -43.67586 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5986ac6d-1ddd-38f2-bb4b-2adc322b9802 | -3.39168 | -50.14994 | 2025-09-15 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06b78e9d-45f7-3270-a84a-0350d6f8ba27 | -6.42788 | -44.42292 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6264597-27b6-3514-865d-c862a001dc28 | -4.17685 | -48.56571 | 2025-09-15 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7a3521f6-be5a-3828-9d61-39407bc79410 | -7.97838 | -45.64725 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8d2e7df-bdd6-33d5-be9e-4290a53d5073 | -8.91673 | -45.50283 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c46926f4-68f1-3856-bee1-7a194d91394d | -7.86733 | -43.58512 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e78540e1-1657-3ca0-8d11-5f99d4f46b36 | -7.89131 | -43.57421 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4c9c72d4-684a-3af4-8bff-f3bef1f2062a | -5.79884 | -50.08895 | 2025-09-15 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fb426ab-471a-3c2e-8d79-53db7717f965 | -8.98102 | -45.80838 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 37ee98d5-1ba6-3540-bcb0-172a369e42e8 | -8.7781 | -46.01497 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 574dbee9-0ebc-35d1-93db-128d47464e39 | -7.29746 | -43.948 | 2025-09-15 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ed535fa-af00-3348-9645-c87dca70ba37 | -5.94922 | -42.80524 | 2025-09-15 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1a38ef0e-4652-30b7-a9ed-e33ff713aaf5 | -8.91836 | -45.49244 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34b242d1-9a90-3023-9051-fa3e8ef951c5 | -6.5289 | -51.19064 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e5d5157f-89e6-3b7c-b7cd-6e3cfc5d6d55 | -2.94614 | -49.3453 | 2025-09-15 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ddf77d5-a9bc-35d2-b771-7f5725b4c8f7 | -6.06608 | -44.82545 | 2025-09-15 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e704939-5b97-3cef-a0b4-e357e5d6e726 | -6.89828 | -45.63524 | 2025-09-15 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cc4d769-97af-3756-b41c-427e3c7bc94b | -9.2334 | -45.67455 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cddce86-2824-3123-9486-3cad4b5f63a9 | -8.63986 | -46.99501 | 2025-09-15 04:19:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78a0f4b7-ec74-316a-a130-e2a5ffefb068 | -5.2069 | -45.18049 | 2025-09-15 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 408f4c85-dd9e-3297-a168-fbbaa6316635 | -7.84748 | -46.11018 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05bde5c0-ddcb-3fef-98ad-172515c6d99c | -5.72439 | -44.09341 | 2025-09-15 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5473f4e3-0441-3cd5-8999-ff217df9e152 | -5.69662 | -49.19667 | 2025-09-15 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c483a66a-1234-34a3-a238-38087fcbfaab | -7.1605 | -44.35034 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d6ccf28-ed8c-3bc1-9aef-d13513af9160 | -5.94978 | -42.80155 | 2025-09-15 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f0569be1-e3c4-3085-9fb0-74de47b40f38 | -8.83731 | -43.01567 | 2025-09-15 04:19:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9ea121b2-efea-3397-b657-44d111ae6565 | -5.77059 | -43.92634 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b66dff7-97a6-392b-8c2f-e6dda060ba3c | -8.96719 | -46.21821 | 2025-09-15 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8e755d0-3269-32b2-8500-be3e464d8e4d | -6.05988 | -43.57209 | 2025-09-15 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52d22b67-b30f-338c-bc32-5106df9bb0cb | -7.78944 | -46.15477 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b09ea13-164d-33ea-8b6e-246144c98da2 | -6.29901 | -44.1155 | 2025-09-15 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a47b82ea-3ce5-3c45-b9b7-0792bc88bd87 | -7.5225 | -44.67028 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3639560f-e6a1-3237-9f14-e438145fac8f | -5.6477 | -42.59631 | 2025-09-15 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ab3f169f-f988-3b28-92ce-e60ba76c48d9 | -5.93744 | -44.86483 | 2025-09-15 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a3cbb7c-7054-3d89-8ee7-33265e709d32 | -9.22428 | -44.50799 | 2025-09-15 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3bea870-8ca4-3a91-b6a4-3ef6b7034bb8 | -7.47837 | -44.97513 | 2025-09-15 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 81159231-ba40-3678-bc2e-64b26fa36aae | -6.05844 | -44.54507 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 202b8fc7-0b1d-33b7-ad9e-a0b4fdb02f91 | -8.78033 | -46.06544 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86410748-0687-3022-bc7e-89489877101c | -6.66581 | -45.55481 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff8c387a-d0f5-31d4-bcc0-f4f9d50931f1 | -4.10401 | -47.31754 | 2025-09-15 04:19:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce877ea2-4f81-3523-ad13-19f0a1e896f5 | -3.27736 | -43.5298 | 2025-09-15 04:19:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README20.md)
