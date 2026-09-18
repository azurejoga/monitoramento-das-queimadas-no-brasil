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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf465216-1123-3408-b4ea-1c52973bcec2 | -4.88476 | -56.06692 | 2026-09-18 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 923b154f-f33f-37ef-9f79-2d5cfb868389 | -3.10582 | -48.69096 | 2026-09-18 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24333ce4-e5a4-3d20-add8-ae99a202af82 | -6.12164 | -44.03291 | 2026-09-18 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3e28b04b-6ee0-3386-b6f8-26291f086dc2 | -6.91065 | -41.71762 | 2026-09-18 04:19:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8c1b4754-ec2b-30bf-819f-789f430b3099 | -3.70524 | -54.1806 | 2026-09-18 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c50c5d78-7068-3367-b3e9-51f9982b24cc | -7.20524 | -44.10416 | 2026-09-18 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c55f51ca-ed32-3665-a941-be1207bc86fb | -2.48387 | -49.40649 | 2026-09-18 04:19:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f84d9434-09d8-375b-a6ce-2107d45885c6 | -4.43376 | -55.07905 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 64cc362e-99bd-3380-ab5e-a6d9d3d47e5d | -4.56298 | -42.95977 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae946662-39a4-39ce-bdb1-1e72c15f3d08 | -5.73452 | -43.27822 | 2026-09-18 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bada6fd-1896-383d-b422-69ce7510c97a | -4.43192 | -55.5258 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3f9fd04d-1f7d-3fcf-abc8-ace529c9fd37 | -5.62224 | -40.8628 | 2026-09-18 04:19:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3dbdbf42-26be-3a2f-b945-61b9f9cd1a0d | -2.58713 | -48.44093 | 2026-09-18 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2384f9a-4912-35ab-9536-98bab3c1b861 | -7.34575 | -44.62677 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e425dfa-fb8d-3423-99d3-5f685f22a225 | -6.6708 | -50.92611 | 2026-09-18 04:19:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e574691-9a66-3592-92a0-15fac21359b3 | -7.20369 | -47.88158 | 2026-09-18 04:19:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77da30d3-4d2f-3b6d-8936-efce7d8326c8 | -6.27042 | -51.75179 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 633f3ebf-7bfa-3cbb-9d34-4cd986981bad | -5.63791 | -44.8028 | 2026-09-18 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a74b74b-d4a3-3553-915e-e673b03d1f0c | -4.5163 | -56.08739 | 2026-09-18 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1ed68d31-b14b-393c-8829-56bf4bb2c31d | -5.42759 | -43.44299 | 2026-09-18 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 95019a7d-1168-3600-bf10-95ea7185b7d8 | -4.57419 | -42.95414 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| ea21d2a6-5c02-3ea6-8637-99c8abcb0534 | -7.1986 | -41.81313 | 2026-09-18 04:19:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 68b6e671-ba0b-3095-be28-450d034302de | -3.35758 | -50.45878 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e07cd0a9-470b-3fcf-a528-a64374c24ddc | -7.18826 | -44.54484 | 2026-09-18 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc5d97b6-fe5b-34ed-befb-257bab6ec87b | -7.08339 | -41.75833 | 2026-09-18 04:19:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9eb84375-01c6-3e22-839a-8d0c6ffc520e | -4.57812 | -42.95105 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d1f6fef4-2089-3437-bfab-7eb7b5eb869e | -3.3581 | -50.45157 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cee34acb-8a3e-3c5a-a946-ef614e993bfa | -7.34691 | -44.64119 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c9b7c5e-6e7f-3bb3-a7c8-4f9931462330 | -6.45834 | -46.0134 | 2026-09-18 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7701f3d-cc41-3f1c-a913-c2a40a54aca4 | -7.09909 | -41.8365 | 2026-09-18 04:19:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ec9911c0-27b6-3d77-aac5-de4fe250bbfd | -7.93462 | -44.84002 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5c5c058-5770-388d-ba85-c869e5a44550 | -7.29587 | -38.95955 | 2026-09-18 04:19:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 09c96e92-bd24-3dde-9d10-6b4f478b976f | -7.35129 | -44.63478 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 070e7e6f-bdf4-380e-937a-7942639499ba | -3.3728 | -50.44825 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 66ffe768-87b7-39e3-ae4b-11724c607578 | -7.06647 | -42.13413 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 31bf1846-b8c8-3f24-ad15-d24a85b3449c | -3.06588 | -49.52088 | 2026-09-18 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e21fb30-bb52-3c8a-8f17-98fdd235084f | -5.83578 | -52.0316 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 035f90ae-8f39-3839-ae44-e547f6c611dd | -7.66296 | -45.83823 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b640e246-5a85-3c00-9d9f-80bc45b8b755 | -2.8183 | -50.46776 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| c0052ba5-b223-3b05-bd76-bb1352c22e87 | -7.80228 | -44.90443 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4bc2a7b-35af-3e10-893e-3163bdf805a3 | -7.62154 | -44.79762 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0efd1c9b-3944-3883-8f3e-295c6faa5817 | -6.11832 | -44.03242 | 2026-09-18 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c591eae2-9d10-3586-a1f1-70cb4bdcf2bc | -7.62039 | -46.17348 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 0565a912-21d3-30ea-806f-d003b8c98528 | -6.49013 | -44.24374 | 2026-09-18 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 111e153f-3fc9-3256-9d38-b8bd1dce0ca2 | -7.33529 | -44.6287 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8b53e7d0-b2b8-3f4a-a166-d56a4bd8c077 | -6.3044 | -45.69358 | 2026-09-18 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d31146d-9ea1-31a6-ab77-281143d13792 | -3.04596 | -51.37484 | 2026-09-18 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| ef78a3c4-3624-3c32-8597-a86453e9d680 | -3.67298 | -40.57291 | 2026-09-18 04:19:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d1d7cb44-419c-3dc9-9d68-5372dc984073 | -2.49094 | -49.41526 | 2026-09-18 04:19:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb43cf66-3cc6-35fd-8738-63e4205d738a | -1.87683 | -48.73343 | 2026-09-18 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8543e1ce-bb6b-31c3-8955-bd41070facb4 | -7.67106 | -46.10928 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b523df63-b863-3849-802a-3635ca95d3bd | -7.5207 | -44.92379 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03cc8b8d-73a5-345e-8ebb-352f689fa354 | -7.27295 | -46.79571 | 2026-09-18 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb28769b-c595-3704-88dc-8700f6348a14 | -7.80206 | -44.84052 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96775f1c-21fb-3292-b0de-98b956d0347d | -3.26494 | -54.27076 | 2026-09-18 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7685e78d-4cb0-3219-9c80-7d592365b953 | -7.01797 | -44.65698 | 2026-09-18 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36e0434b-61b8-3c16-95ca-28cc972054d6 | -5.97934 | -53.5826 | 2026-09-18 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 384c47fc-fcfc-3768-af7a-1af8a1231af3 | -7.05228 | -42.06241 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8b0c7966-a13d-3998-8466-b667e56013fc | -6.02959 | -51.80904 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92868e84-da49-3051-961a-c7cde19bc8bb | -6.93188 | -41.69921 | 2026-09-18 04:19:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f70268d2-0878-3bf3-b2aa-4764f42ab415 | -4.54308 | -54.93261 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a540211c-928f-3124-be53-c9d5e1eb25e1 | -6.47392 | -44.19497 | 2026-09-18 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a72f20fb-30ae-3902-b880-04ecf2e8fcda | -7.8155 | -44.9065 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 781484bc-4e46-3055-a113-19843f628374 | -3.63222 | -44.57492 | 2026-09-18 04:19:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 279df038-0b2a-3a2d-9505-8c5159f4fe54 | -6.93244 | -41.7205 | 2026-09-18 04:19:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e0b01a09-5945-3f6a-aa61-8aa5a49cb8c7 | -3.2126 | -53.94751 | 2026-09-18 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b43886a-4ad9-30f1-90be-b2bdda99229b | -2.61605 | -54.7572 | 2026-09-18 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57e32ef9-7ea1-307d-88d3-263e5a42704f | -5.65715 | -43.38755 | 2026-09-18 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b6841851-b7e8-363c-9885-4e9af8ac7be4 | -6.35641 | -43.3654 | 2026-09-18 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c1d0bfd8-93c1-3951-afbe-ce9bd65e96df | -5.62161 | -40.86712 | 2026-09-18 04:19:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 594445d4-7949-33eb-b5b1-bad1580814d5 | -7.63486 | -46.165 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e570656-1562-37ae-b754-8c902e73a3cb | -5.50174 | -45.51954 | 2026-09-18 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b13a6c5-42cf-308c-b033-6fa90ec0b271 | -2.83061 | -48.65024 | 2026-09-18 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1d24ce48-9e7b-3265-9dfe-23b1d06deedb | -6.66535 | -43.63646 | 2026-09-18 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48a3e4ab-bdcc-35f1-8d97-06999c927402 | -2.90872 | -54.17777 | 2026-09-18 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 322821da-44de-3515-8a0d-5e907745a5f9 | -3.21758 | -53.95185 | 2026-09-18 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 230fb80f-6eff-3697-b5e2-d6aa408bb029 | -6.73745 | -44.09588 | 2026-09-18 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50c99d83-7d1d-3b2a-9305-05bef364a9fb | -5.89089 | -52.08947 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2d887b1-c7ef-3a9c-b3be-7d316992ef9e | -6.22785 | -45.44588 | 2026-09-18 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 153528e9-98b8-3e86-8455-133e614faf47 | -4.83166 | -42.16337 | 2026-09-18 04:19:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 56d6bc0a-5b01-3253-afc7-db3fa2a5bebd | -7.80806 | -44.82368 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c09a2de6-4da8-3eac-aa23-317bc180956e | -6.9173 | -41.72277 | 2026-09-18 04:19:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 781ae5eb-ee84-39f7-87b6-463ce9a7f17e | -7.39596 | -44.4994 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ebb8839-f9ec-3127-ac88-625ba99806f6 | -4.42746 | -55.51589 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a96dbd3b-b525-3a30-9726-9493eb251510 | -7.65688 | -45.83368 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6de71853-90f7-39ec-805f-89dd486ff8e4 | -6.95354 | -43.1042 | 2026-09-18 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3604e8fe-115a-30e0-a992-4b0cbf1d2a2a | -2.96421 | -50.32297 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f16f8765-afa1-3b9d-9ac2-4fbf84261caf | -6.43767 | -44.95428 | 2026-09-18 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7d7398cb-af45-33c8-9be4-e73ccf1febf9 | -5.58362 | -48.10703 | 2026-09-18 04:19:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5db4f1e-348a-3c9b-8142-0f8927add891 | -2.9525 | -50.31253 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4ce05121-2c6c-3fce-ba2c-a644899576e5 | -2.32983 | -47.20225 | 2026-09-18 04:19:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ebd15963-ade1-364b-9a6e-52a5035a6042 | -6.91551 | -41.70975 | 2026-09-18 04:19:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1e592483-e284-39bc-86f0-ce32de90b539 | -7.03498 | -42.08043 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| aac2a956-88b1-3ca4-a8b6-1d0086dcc05c | -2.96781 | -52.13405 | 2026-09-18 04:19:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| aa9e8aa9-1b06-32d2-9b72-db69138c7203 | -7.37113 | -46.79721 | 2026-09-18 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30259aeb-cad3-3e8f-9141-d1ea9daf3024 | -7.06588 | -42.13815 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 46c1af53-6d62-3639-9887-3af6a12f5f9e | -7.63311 | -45.83355 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| def4eb8f-5975-3eb3-926e-59787beb374c | -5.86389 | -52.03621 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8ed7be3-965e-39ed-b52c-f23152838b5d | -7.39981 | -44.49644 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6d7cf7b-7733-3f4e-ba03-158feec66dc7 | -6.46581 | -48.00686 | 2026-09-18 04:19:00 | NOAA-21 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README33.md)
