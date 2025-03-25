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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 081f1dd4-16f7-325c-aca0-bed154329041 | -8.11492 | -43.1284 | 2025-03-25 04:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| da5c1abb-59f5-382b-8134-36d6b53a1c33 | -10.58121 | -45.14063 | 2025-03-25 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5182a976-22b1-370a-9ba4-7b235019173c | -9.31959 | -40.44208 | 2025-03-25 04:08:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d2fe4647-430e-3bb0-bb38-081eb9b41b23 | -7.22751 | -44.77018 | 2025-03-25 04:08:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 26996415-55e0-394a-a0b0-55accced0d31 | -8.67441 | -36.24015 | 2025-03-25 04:08:00 | NPP-375D | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0dd1e447-865f-30c8-9386-e1cc3dc1fec7 | -8.10817 | -43.12731 | 2025-03-25 04:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c568794a-531c-3991-b2cf-dee84cd72ec5 | -7.03972 | -44.36891 | 2025-03-25 04:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f01b793-6837-34b8-a401-c2d4d6135ad3 | -5.63242 | -44.31882 | 2025-03-25 04:08:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37e61f99-5354-334a-bb26-fbe425b01a85 | -11.9032 | -41.61251 | 2025-03-25 04:08:00 | NPP-375D | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d0d24445-4c91-3873-9642-e0927f10604f | -7.04262 | -44.37356 | 2025-03-25 04:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28a6c7db-2647-3b93-ae8d-1db1b12fce01 | -8.11155 | -43.12785 | 2025-03-25 04:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d29a2a32-3325-38d9-af82-cfea9dd4154d | -6.82673 | -44.39099 | 2025-03-25 04:08:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd7b2bbc-ad4f-3c63-9fcd-ead632de89e1 | 4.6634 | -60.9225 | 2025-03-25 04:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 47.7 |
| f497046c-b60b-3227-9efd-79e8ae44c9a7 | -18.04016 | -39.92688 | 2025-03-25 04:10:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fd19b72c-eb2d-3fe1-9c3c-3f0f43303c6a | -15.51204 | -42.60219 | 2025-03-25 04:10:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7eea69e1-9ba5-31ac-85ce-1a230a67ede5 | -16.67981 | -43.8835 | 2025-03-25 04:10:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cf3434f-fcb8-3cf8-b190-fc2ff53ed639 | -17.55833 | -40.63595 | 2025-03-25 04:10:00 | NPP-375D | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 195183d3-f4b9-33bc-ae40-41a118e6e3fc | -17.85748 | -39.85358 | 2025-03-25 04:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 27.4 |
| 8f1572cc-f99d-3ec2-baad-5a0b96047cb1 | -17.86761 | -39.86494 | 2025-03-25 04:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 76.0 |
| 2fa62d3a-b7f7-37b9-b97f-9d126d270c89 | -16.08968 | -42.28408 | 2025-03-25 04:10:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 33fffe5b-8794-3286-bdae-5bfa41b36e93 | -17.55771 | -40.6404 | 2025-03-25 04:10:00 | NPP-375D | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 083689aa-6194-3cbb-af2a-4e4576476925 | -17.85999 | -39.86384 | 2025-03-25 04:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.6 |
| 059c36f8-665a-3b3e-a65b-51fee1930ae5 | -17.8651 | -39.85471 | 2025-03-25 04:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 8ea26363-3c13-3cc3-acee-c0289b36b8d6 | -17.85367 | -39.85299 | 2025-03-25 04:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 27.4 |
| 7fb10624-1c7a-34be-a59d-fff52f802068 | -15.51148 | -42.60583 | 2025-03-25 04:10:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bc750365-09c1-34c9-ba41-db15cf4466e7 | -16.09362 | -42.28088 | 2025-03-25 04:10:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 4c36b4be-3680-37f6-8817-2a38bf726410 | -17.55469 | -40.63541 | 2025-03-25 04:10:00 | NPP-375D | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c29bf882-7e36-32f0-a3a4-04f899b7216e | -16.0945 | -42.28014 | 2025-03-25 04:10:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5d7576d8-fdc2-3bb8-baf3-51f3e6dd8769 | -16.09025 | -42.28034 | 2025-03-25 04:10:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 4f79dde4-d54c-3262-9adf-4a70c903bfe1 | -15.51259 | -42.59855 | 2025-03-25 04:10:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ef3ad60-6817-3ee0-b27f-a74b4ac7bdea | -19.83752 | -40.86826 | 2025-03-25 04:10:00 | NPP-375D | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c147f835-83c9-3f09-9815-0c960d94bbfb | -16.03823 | -43.72467 | 2025-03-25 04:10:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0db5b50-f484-34b7-a76c-10ec1b857baf | -17.85182 | -39.84585 | 2025-03-25 04:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| af947baf-cdbd-3ecc-8408-47c0182c0dce | -17.85619 | -39.86326 | 2025-03-25 04:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 77cad74c-4aa1-3204-bdb7-c86014d83e6f | -17.85114 | -39.85071 | 2025-03-25 04:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 6f5bda3b-7eb4-3698-92b4-f5426b7a0142 | -19.71799 | -40.35252 | 2025-03-25 04:10:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ba0ebb59-8b55-3350-ac52-0eaeee6a4af9 | -17.86891 | -39.85523 | 2025-03-25 04:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 22.9 |
| 32dee064-bc15-300b-91e0-d8fe99ce25a5 | -17.85432 | -39.84812 | 2025-03-25 04:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| abe1b643-adc9-3f9d-82d9-c5e5c210ca2f | -16.09305 | -42.28461 | 2025-03-25 04:10:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 5a25f250-59cd-36cf-b771-f0badde03b5f | -16.03767 | -43.72825 | 2025-03-25 04:10:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 334c57dc-4c98-37c8-87d9-9ccf1029cceb | -20.90167 | -43.81818 | 2025-03-25 04:10:00 | NPP-375D | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e4a6c6af-137b-358c-aefc-240077efe0cd | -17.85051 | -39.84753 | 2025-03-25 04:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 4095e88f-c6ed-3359-ae45-f19cc3350141 | -17.85238 | -39.86269 | 2025-03-25 04:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 22eea638-ecc9-34d3-a8de-54502272d721 | -17.85813 | -39.8487 | 2025-03-25 04:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| d99c2ceb-68ea-31a2-8fa2-2c41b2831f1a | -16.83043 | -42.87329 | 2025-03-25 04:10:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e6aad0e-f366-339d-8ef7-70bc41e801f5 | -17.86128 | -39.85416 | 2025-03-25 04:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| b7da3c0d-76a2-33c2-ad0b-5f59a2c31576 | -17.84987 | -39.85239 | 2025-03-25 04:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e29cacda-57b1-384b-881e-fdee363925c8 | -16.09394 | -42.28387 | 2025-03-25 04:10:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 55a7cabe-dba6-34a0-a2c4-cbf8fd232a20 | -15.50814 | -42.60527 | 2025-03-25 04:10:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| acaf72fa-13c1-3f18-9d40-55c812a1e202 | -17.85683 | -39.85843 | 2025-03-25 04:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 27.4 |
| e640a1a4-371d-3dde-b3df-041760b34a9a | -17.85303 | -39.85785 | 2025-03-25 04:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 27.4 |
| cd7eaaea-f3bd-3776-8507-19ae7e861968 | -17.86826 | -39.86009 | 2025-03-25 04:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 22.9 |
| 33205e7c-8cf7-31a3-8fb6-b3765596e8dd | -17.8638 | -39.86441 | 2025-03-25 04:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.6 |
| c58672d7-41ab-3912-9147-a9f70e5dc3f5 | -17.86444 | -39.85956 | 2025-03-25 04:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 28b1e71d-bf55-35f8-9efe-21b615d365bc | -15.50869 | -42.60163 | 2025-03-25 04:10:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb0d133e-0d66-3732-9940-85f97f4e80ea | -17.05466 | -39.22085 | 2025-03-25 04:10:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 77532c38-8eec-335b-bea0-8a0b34166d0b | -22.19554 | -57.0845 | 2025-03-25 04:12:00 | NPP-375D | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 595447ac-4c37-370b-a286-68be02f2e312 | -21.19545 | -44.93619 | 2025-03-25 04:12:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5280f981-d212-3c3a-87aa-a5de200c0ede | -23.59384 | -47.44017 | 2025-03-25 04:12:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ae0ef14d-0fa8-3f7b-a058-dd810a59487a | -22.89684 | -53.50924 | 2025-03-25 04:12:00 | NPP-375D | QUERÊNCIA DO NORTE | PARANÁ | Brasil | 4121000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a49d7a6f-bd0b-39ac-9bf3-c8b7e7171e4c | -22.90203 | -43.75334 | 2025-03-25 04:12:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| af1ad628-7195-3ba2-8ade-777fed880a7c | -25.34751 | -51.47407 | 2025-03-25 04:12:00 | NPP-375D | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 88f43f6a-657c-3947-9d32-a2fcdf0753de | -22.89239 | -53.51116 | 2025-03-25 04:12:00 | NPP-375D | QUERÊNCIA DO NORTE | PARANÁ | Brasil | 4121000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 92830056-c038-3f55-8baa-fef7cf20df2e | -22.89717 | -53.51221 | 2025-03-25 04:12:00 | NPP-375D | QUERÊNCIA DO NORTE | PARANÁ | Brasil | 4121000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 01e21f00-8227-33bc-869a-e5477a4a558a | -23.98536 | -48.91721 | 2025-03-25 04:12:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2910a5af-937b-3604-a202-ae92874b46a5 | -25.33173 | -52.58577 | 2025-03-25 04:12:00 | NPP-375D | NOVA LARANJEIRAS | PARANÁ | Brasil | 4117057 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4a370448-4b5f-3c9c-8384-9b4591bfeaf5 | -22.89206 | -53.50818 | 2025-03-25 04:12:00 | NPP-375D | QUERÊNCIA DO NORTE | PARANÁ | Brasil | 4121000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c74210b7-fcc1-3679-b43d-afbd355e4fb5 | -20.78307 | -49.84838 | 2025-03-25 04:12:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 82d0a0b7-5459-3e6f-be9c-78ecf4ca1c92 | -23.33822 | -46.77317 | 2025-03-25 04:12:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| aa56e69d-fcb7-39ed-9339-24d2c7616759 | -23.52149 | -46.97591 | 2025-03-25 04:12:00 | NPP-375D | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 71e5c699-2480-352b-adf5-000079478305 | -22.91975 | -45.41304 | 2025-03-25 04:12:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f287b8df-6df5-3eee-905e-dc07ef2dc409 | -27.14159 | -52.0974 | 2025-03-25 04:14:00 | NPP-375D | IPUMIRIM | SANTA CATARINA | Brasil | 4207700 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 85511c22-6f5c-3959-b97c-4206ee95f1cb | -27.13757 | -52.09638 | 2025-03-25 04:14:00 | NPP-375D | IPUMIRIM | SANTA CATARINA | Brasil | 4207700 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e8811284-6556-34ed-85d7-12c7d960e792 | -26.46859 | -53.35831 | 2025-03-25 04:14:00 | NPP-375D | PALMA SOLA | SANTA CATARINA | Brasil | 4212007 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 49478b7b-8a4b-3af4-bf72-f7bd1f5077e1 | -1.70601 | -46.78427 | 2025-03-25 04:27:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 084f9eb9-d67c-34a1-86df-7e1b1c76272d | -1.23723 | -50.65456 | 2025-03-25 04:27:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f044eef9-cf5c-34c6-9b42-f291c0abbed6 | -1.94558 | -47.91594 | 2025-03-25 04:27:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f9607d09-072e-3fa3-b819-5a80ee054b59 | -5.63206 | -44.32015 | 2025-03-25 04:29:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3adf01cb-949c-370e-b7f2-72940ceec77c | -8.11376 | -43.12723 | 2025-03-25 04:29:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6c834db4-1b55-3f70-9485-78b9fa449884 | -7.22697 | -44.7705 | 2025-03-25 04:29:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed491fd4-86d2-3736-83f7-4fbfced15ee8 | -5.99608 | -44.61137 | 2025-03-25 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c2c740f-2902-3825-8ca1-d7c539b0d129 | -8.10975 | -43.12664 | 2025-03-25 04:29:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9d18e3e0-b751-3eec-8e3a-112a00c201b8 | -8.10574 | -43.12601 | 2025-03-25 04:29:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c3d2861e-54c0-3c93-ac4b-c4d8503e6744 | -2.65816 | -48.79867 | 2025-03-25 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7fcfbd82-29e8-3fab-89b9-83f9deac7a6f | -4.81635 | -42.98851 | 2025-03-25 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2c94aa3b-0c5e-37df-9dbc-3c2020661e4b | -4.81427 | -42.98537 | 2025-03-25 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 213bbb4f-b1e1-3c42-a8ce-d5210869ada3 | -7.04029 | -44.37333 | 2025-03-25 04:29:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af7192ee-529d-332d-bad9-86e7c5bbb4ad | -3.78396 | -41.60262 | 2025-03-25 04:29:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3fad9d82-8d78-3b7c-884f-15a67bf8cbca | -7.04095 | -44.36897 | 2025-03-25 04:29:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e77d13c9-587c-3b57-af60-3625d95f4bb3 | -8.10121 | -43.12894 | 2025-03-25 04:29:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7248762e-d4ba-358f-aca6-dc9e3d0225e7 | -8.10522 | -43.12955 | 2025-03-25 04:29:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c415d1ad-f79f-3f2a-882d-65feeaeaf80f | -6.20849 | -48.05543 | 2025-03-25 04:29:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6258c0c-e09d-37c9-be95-abbe7e0aa5a3 | -4.01361 | -41.79324 | 2025-03-25 04:29:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b44089a1-61eb-30be-9599-8a77020716b6 | -5.41919 | -45.26135 | 2025-03-25 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3bc9e0e-35bc-324e-a1ad-453ea3e8292e | -5.97336 | -39.67164 | 2025-03-25 04:29:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8d603790-5926-3f19-8674-9ca02da2ec3b | -3.42243 | -43.16598 | 2025-03-25 04:29:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 472f4c51-5d0b-32b5-9e24-70faaf91c19f | -3.78452 | -41.59889 | 2025-03-25 04:29:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 90247e0a-1c1e-3cec-9d1c-27e3e4c5bde9 | -16.03476 | -43.72793 | 2025-03-25 04:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 28f81905-280d-30b5-82d6-0ebf34d6af80 | -16.03739 | -43.72506 | 2025-03-25 04:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f2976e9-57dc-33a1-8dd3-237f19279954 | -16.09176 | -42.27765 | 2025-03-25 04:32:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |


[Clique aqui para ver as próximas entradas](README5.md)
