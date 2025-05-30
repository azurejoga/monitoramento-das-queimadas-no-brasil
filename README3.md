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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ad21a63-f0f9-35ad-9e9c-efa91acb80b9 | -7.53324 | -43.32417 | 2025-05-30 03:32:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36e1f0e2-89e4-3d24-be3d-e1b0e45b7816 | -5.78176 | -43.61133 | 2025-05-30 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58f6e577-84c2-38bb-89cf-5976cbabda00 | -5.78086 | -43.61626 | 2025-05-30 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d4a4ad7-801f-369b-a479-51836673590c | -9.40289 | -40.36269 | 2025-05-30 03:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3454a3bb-73c1-3431-b702-16d9e4f52d6f | -7.58742 | -45.95135 | 2025-05-30 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16c8fd03-011b-3fab-b0ac-cc090f77605d | -11.69217 | -46.21714 | 2025-05-30 03:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88dbe3aa-f642-3050-a738-179fc49f8885 | -8.54385 | -46.42659 | 2025-05-30 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f680517-a2d0-3098-8c1e-5e858b533cb4 | -7.23705 | -43.0911 | 2025-05-30 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f5765911-cef3-3515-8f69-78590d0e74e8 | -11.6934 | -46.21123 | 2025-05-30 03:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 160c7992-058f-31e8-ac7a-9e436080e44a | -7.18792 | -43.10828 | 2025-05-30 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f297ad03-5f29-3e43-a689-0a0062928237 | -7.52728 | -43.32286 | 2025-05-30 03:32:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb3c913d-f2f3-3baa-9d42-4f69df79f3d2 | -7.53408 | -43.31974 | 2025-05-30 03:32:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e56f48f-2e8a-30f9-ae63-ec7007d631dc | -7.18119 | -43.11137 | 2025-05-30 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e49298fb-6486-3b5c-a3f2-11c459b71aad | -7.18871 | -43.10401 | 2025-05-30 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a7baef7b-a3cc-350c-864d-1a10f95fa58e | -7.27551 | -44.22868 | 2025-05-30 03:32:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f986bd4-7775-3e97-9286-285a89266609 | -6.24055 | -43.3776 | 2025-05-30 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| defa363e-0cb8-30f4-b670-ae572aa22f3e | -6.82733 | -44.65189 | 2025-05-30 03:32:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3872b9ed-4f99-35b3-a866-fa6362cdc9e7 | -7.61335 | -45.7366 | 2025-05-30 03:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4031e213-2a4c-372e-bb5e-ee8c6ed60827 | -7.58371 | -45.95754 | 2025-05-30 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73c16c1a-f4c1-3f63-b131-f868c08b4bf4 | -9.40194 | -40.36795 | 2025-05-30 03:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| a37736bf-2dee-31e7-a1a8-93bd6b6b7e30 | -7.53819 | -43.32443 | 2025-05-30 03:32:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1032f30-3f2e-399b-afe3-af802f91b280 | -7.6123 | -45.73659 | 2025-05-30 03:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1e77425e-2fd0-3771-9e4f-f7af0f29e90b | -8.90574 | -44.78249 | 2025-05-30 03:32:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e9c547f-ea30-3a2e-bcba-4d913ff94bf8 | -7.57974 | -45.8664 | 2025-05-30 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 64ec6afa-c9bf-309c-b48c-0d3e39b459b1 | -7.23871 | -43.09973 | 2025-05-30 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 8357606b-5a34-302e-b9c2-3187fcf42077 | -7.53222 | -43.32309 | 2025-05-30 03:32:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 93dcfa9b-8270-37e6-a5a2-abbb9cfd6a6e | -8.9068 | -44.77697 | 2025-05-30 03:32:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c3063df-6253-393b-8efa-0f0cca4ff95c | -6.24544 | -43.37757 | 2025-05-30 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3067a041-f9e2-31aa-8eae-615c1118cb2e | -7.23625 | -43.09537 | 2025-05-30 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f6bdb87c-b835-371c-aead-bebb68994933 | -8.00477 | -45.68944 | 2025-05-30 03:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f542786e-0192-3da5-a22d-dac66929c142 | -11.79052 | -44.28394 | 2025-05-30 03:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6ae8d1d-eb38-3277-a9dc-6b4c6228f4f8 | -11.69625 | -46.21851 | 2025-05-30 03:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99fca11e-fe49-38ed-8917-5e1a9b4d8a1e | -8.54803 | -46.42362 | 2025-05-30 03:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8fbb4a7-2106-3154-9f65-a072c6fb61d8 | -6.2463 | -43.37292 | 2025-05-30 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a175701-f09c-3853-b15b-a3d430b5fac4 | -12.25733 | -44.60294 | 2025-05-30 03:32:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afc3b0c2-759b-30c6-95d7-844e00940d32 | -7.24219 | -43.09649 | 2025-05-30 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 0dd345f0-41e2-34f1-905b-86700e0bc5b4 | -7.99771 | -45.68912 | 2025-05-30 03:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f26fcdde-99e7-3b80-98db-4e48958d40fd | -16.51446 | -43.06854 | 2025-05-30 03:34:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62d6d42e-01f9-38d7-8c58-b46143a746d6 | -18.38054 | -44.51402 | 2025-05-30 03:34:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b3883e8-53d5-3422-9aed-19a7b79020c1 | -18.38301 | -44.51599 | 2025-05-30 03:34:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f69606e2-205e-3a32-b5fd-bc873656fc03 | -16.52009 | -43.06669 | 2025-05-30 03:34:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| beb68d93-0cd7-38e2-9486-a21c57db75e2 | -16.51947 | -43.06971 | 2025-05-30 03:34:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a864b8a2-f8b7-32b5-9ad4-3123a2edf76c | -13.53104 | -43.68172 | 2025-05-30 03:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 65f4ed0a-abe9-36d8-8023-70994025ce9c | -13.53178 | -43.67801 | 2025-05-30 03:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| e281abd6-0785-39de-83f3-e44d2b2148de | -16.02634 | -43.68256 | 2025-05-30 03:34:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44b9b16c-0616-3920-bd45-64123e669293 | -16.52174 | -43.06621 | 2025-05-30 03:34:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 64f9be03-33d6-329c-a200-b0cc1a332d88 | -18.37978 | -44.51759 | 2025-05-30 03:34:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ae55213-1770-3ced-b234-4a3c65e974df | -14.84061 | -48.10345 | 2025-05-30 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0eb7a168-9fb5-3495-a131-286b65ac839d | -14.85084 | -48.09066 | 2025-05-30 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b57b4ce4-8d0a-3069-a44d-404b3a8d893d | -14.84921 | -48.09789 | 2025-05-30 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5907333e-9bbf-317d-bcd3-ad506bd97cc9 | -14.85753 | -48.09354 | 2025-05-30 03:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f2a86012-4d92-3709-9715-48df3fed4605 | -16.51613 | -43.06809 | 2025-05-30 03:34:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9d488ef6-8b4b-3a3c-957c-2438153440ef | -14.84767 | -48.10477 | 2025-05-30 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d5d788b3-4dca-3944-aa25-450b27f2eaaa | -13.53656 | -43.68288 | 2025-05-30 03:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 55305f8b-95b6-3a90-9114-b65eeee5b0ef | -13.63299 | -47.42662 | 2025-05-30 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db5e85ee-e140-3eba-91aa-a316e226d09a | -13.5373 | -43.67917 | 2025-05-30 03:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 878318d4-67c2-32f8-b969-4245c902bbc6 | -14.86238 | -48.10475 | 2025-05-30 03:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d15ffc2d-b69d-3fca-8cdb-1311b977a9e6 | -16.37696 | -43.04029 | 2025-05-30 03:34:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0f4b28e-8b57-3a39-ad5d-9ff15e9fe05f | -15.24714 | -47.46619 | 2025-05-30 03:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 542f9179-bbef-3299-ad48-48fdf6b4ce86 | -15.24863 | -47.46614 | 2025-05-30 03:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 97f7514a-5645-32fc-b3de-832923776973 | -18.3777 | -44.51477 | 2025-05-30 03:34:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6dcf3bf-25d4-31dc-a3ce-f3a48b2d66aa | -15.90886 | -43.45801 | 2025-05-30 03:34:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 411f078b-bda0-36ad-86ad-263818c163b1 | -13.63175 | -47.43233 | 2025-05-30 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 32db37b7-3bc4-39fd-be5e-41d1dbf7a5d4 | -16.51507 | -43.06557 | 2025-05-30 03:34:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74aba091-3b94-33fa-a418-1f4d452c092e | -16.04382 | -43.80018 | 2025-05-30 03:34:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d39fd81a-7f75-34c4-b6ff-402e864a4d96 | -14.84602 | -48.1121 | 2025-05-30 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 77851fb6-b9dc-35ee-a721-79919e1af17a | -13.53804 | -43.67547 | 2025-05-30 03:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 0c4aa7bc-cd81-3116-a309-79def1acb380 | -16.52071 | -43.06362 | 2025-05-30 03:34:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5b46e5f-ea8e-384b-9935-c15f83ec403d | -13.63085 | -47.43262 | 2025-05-30 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84a509a9-e4cb-37a8-b0ec-8cdb99c10c61 | -15.24192 | -47.46464 | 2025-05-30 03:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d2d4ba7-6e26-3cd5-a115-42659d0d82f9 | -13.63211 | -47.42696 | 2025-05-30 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de29f792-e800-3112-bc25-e747fcd618e4 | -16.03165 | -43.68356 | 2025-05-30 03:34:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf158884-8f0c-3168-bb38-de851e664b00 | -14.83889 | -48.11113 | 2025-05-30 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 91834806-2ada-3889-9d3c-24dd809a1fac | -16.51672 | -43.06508 | 2025-05-30 03:34:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0e45fd66-37c0-3530-a2a5-be9147ef5752 | -16.04313 | -43.80354 | 2025-05-30 03:34:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4e1946a-a655-393f-bc2f-d9617c863e77 | -23.28059 | -50.89528 | 2025-05-30 03:36:00 | NPP-375D | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 64a03122-010e-34c6-9305-22da62eadc6e | -23.28745 | -50.89734 | 2025-05-30 03:36:00 | NPP-375D | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 8e727be6-9a80-3a55-bcb2-d3de2a2ea56c | -23.28265 | -50.89807 | 2025-05-30 03:36:00 | NPP-375D | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| f41717dc-be24-309f-aa43-1eea46fc5d71 | -22.22919 | -50.86672 | 2025-05-30 03:36:00 | NPP-375D | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 87def840-61fa-3634-915d-d7c81e741c1b | -13.5261 | -43.6797 | 2025-05-30 03:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| b4db7fe8-26a6-39ea-8f75-9d4f3c0c02f5 | -13.5456 | -43.6762 | 2025-05-30 03:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 0b6eea07-a9be-3a2f-a2cc-fa2cf1aeb245 | -13.5456 | -43.6762 | 2025-05-30 03:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| bb694e42-96f9-3c6a-a2c1-6669f62ce6b1 | -13.5261 | -43.6797 | 2025-05-30 03:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| d5d92178-ffba-3157-affa-bd084d1c9da8 | -5.50602 | -35.59545 | 2025-05-30 03:51:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fbc289ae-d78c-3b47-96d0-234f5f55cf74 | -6.33332 | -43.38329 | 2025-05-30 03:51:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10a69726-91b7-3b43-a47a-f1a43375cd90 | -3.96153 | -41.48238 | 2025-05-30 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1b92f202-ff1b-3569-abb7-dbc8da8510a6 | -6.55246 | -41.3469 | 2025-05-30 03:51:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5d94ea9f-1a5e-36d7-b32c-8e13802f295c | -4.67142 | -39.02078 | 2025-05-30 03:51:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 113ea241-ef89-3e69-9e18-f4250efaff86 | -5.59126 | -43.57495 | 2025-05-30 03:51:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32719422-1052-39d9-b7b4-0614d311777c | -6.26973 | -44.20385 | 2025-05-30 03:51:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34ec52b3-c954-3ae1-89fb-6b35f2cab891 | -6.24233 | -43.37856 | 2025-05-30 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4850516a-0af0-3640-9272-b57cd1d91cb5 | -5.07121 | -37.71549 | 2025-05-30 03:51:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 88983b73-438d-333b-be47-a221264d6f7f | -6.33736 | -43.38394 | 2025-05-30 03:51:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 12f64527-960c-381f-801a-7d615e05ff44 | -4.25042 | -47.58543 | 2025-05-30 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59f33be1-ca8e-35ed-bd17-b0428ae984da | -5.76298 | -38.90589 | 2025-05-30 03:51:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 98506c5d-3f68-358a-8bcd-e92b2405c020 | -6.24291 | -43.37503 | 2025-05-30 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 35bde143-7b60-31cb-b939-8500528126fe | -4.97979 | -38.59613 | 2025-05-30 03:51:00 | NOAA-20 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0e580c25-20d0-3c17-a701-3cfcf17e3618 | -4.81694 | -44.35472 | 2025-05-30 03:51:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3525bbe9-d4a2-302a-9897-c4d65e583f25 | -5.76564 | -43.48579 | 2025-05-30 03:51:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7997f78-a1b4-3080-8441-35e4fbbee19d | -3.28477 | -43.49414 | 2025-05-30 03:51:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README4.md)
