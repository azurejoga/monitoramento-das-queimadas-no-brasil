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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1e0c44d-7104-39af-92a7-95efea4de407 | -14.10651 | -53.70854 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 174109c4-7a6e-3eb4-ac30-6ffda154a71f | -20.01765 | -43.89426 | 2026-08-15 04:17:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 8edb8bcc-d219-3fd7-9698-8ef4dfe260b4 | -14.91199 | -46.64161 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f3d745a-4e7b-3d49-a926-82dec974ab0f | -17.89612 | -44.44113 | 2026-08-15 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 958002a0-4c4c-3689-b1c7-1e0bf8f61f92 | -13.91716 | -53.95277 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43e676a3-613c-3962-aa7f-5fa41b811eec | -14.48734 | -52.08661 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| baf627bb-9014-3574-8508-da30b4ae26cf | -18.45627 | -43.43616 | 2026-08-15 04:17:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a5d64235-6e81-3be7-9563-4d20bb8b80c4 | -20.28823 | -41.62424 | 2026-08-15 04:17:00 | NOAA-20 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 753c3473-b6d0-373b-a361-a0bdabd87cec | -18.58179 | -41.27681 | 2026-08-15 04:17:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d0f19974-15a0-3ae1-8237-9e0854c28802 | -16.11348 | -49.86518 | 2026-08-15 04:17:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 08f4c05b-fbe4-3c0d-aafb-0656e1c35722 | -14.44388 | -51.91185 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5eeb7643-0cd3-3b67-9f14-374549d6e842 | -19.93785 | -42.13348 | 2026-08-15 04:17:00 | NOAA-20 | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| d17942f7-6211-30b9-8f9e-9611c9f03cc4 | -14.40205 | -48.95791 | 2026-08-15 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4c1c8080-d7e8-3b22-a0ee-e76870c992b0 | -16.83484 | -42.2626 | 2026-08-15 04:17:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 27ee83f0-23ac-3256-adfc-4db9bbe2e6b4 | -16.10465 | -49.8641 | 2026-08-15 04:17:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 170106b2-eaf0-32c3-801a-51add95f5c77 | -15.64846 | -48.20379 | 2026-08-15 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc602ae5-1970-3212-843e-cf6dddcee209 | -18.57612 | -48.33967 | 2026-08-15 04:17:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 754fcf92-7b30-336a-9014-bd0695e1bbd1 | -14.93901 | -46.63354 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e64b6236-798f-3341-9030-39792f9213f6 | -18.58541 | -41.2773 | 2026-08-15 04:17:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 5570834e-541f-30cc-8222-b9f8d18d1364 | -14.12845 | -53.6862 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 45f8e50a-2c6c-3453-a62d-ffbc219fdd47 | -14.94965 | -46.63027 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8e18b8a-7447-38a0-ac5b-e02cc7d07b04 | -14.42141 | -51.91728 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e40fa9ba-d5f7-30c6-b782-2a6a6bf6dc1c | -14.44655 | -51.92442 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bff87fa4-4e46-34ae-99bd-428430041cfa | -14.40138 | -48.96162 | 2026-08-15 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 986c95ce-f11c-321b-9a4a-4fbaa5d6554e | -14.91628 | -46.63796 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bc29c4b3-ce42-397e-829f-69eb5520387a | -14.96449 | -46.62916 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c997def-fc84-3f8c-9bc2-aad519b9e757 | -16.90197 | -54.16506 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee1bb1fc-de2d-31ac-badb-059332d07cc1 | -19.25465 | -44.37421 | 2026-08-15 04:17:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94b0b1c1-1444-3f8b-9581-cfca7e4603d8 | -16.88807 | -54.14965 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5fbe202f-a500-3c6d-851f-30bda4248a38 | -20.80359 | -44.73826 | 2026-08-15 04:17:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d3162126-d55a-31f2-b256-87c31371b36b | -14.91702 | -46.6336 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12f0b9fb-3fa7-3c6c-9d0b-1320a798bced | -13.24355 | -54.19487 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 61d9b6ae-251b-3ce8-8180-dd856b21fa5d | -13.91636 | -53.95679 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75122914-b0e3-3c9b-a120-a7372f73e16c | -16.10538 | -49.8601 | 2026-08-15 04:17:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8627e7dc-794c-33c4-9efd-bf85d5f679ac | -14.92692 | -46.61842 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d371e6a6-1963-3e92-b70c-2c5496597d26 | -14.43059 | -51.84937 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0904536-7922-3257-8e4e-96d276bf5931 | -15.61547 | -41.55267 | 2026-08-15 04:17:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 538a7df5-027f-358a-b11b-7d3d1f4b6769 | -18.45292 | -43.43562 | 2026-08-15 04:17:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c61a98e4-061f-3b08-a200-56d98e0dc7f8 | -15.10657 | -48.69281 | 2026-08-15 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fcd4ed7-87e9-3ceb-b214-db9eb8007827 | -14.7171 | -52.88625 | 2026-08-15 04:17:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1d0f960-c40c-3099-8cf9-7bd5646c22b6 | -13.41673 | -57.05448 | 2026-08-15 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9632ee57-d844-39c4-b856-27ec1189cf67 | -16.24985 | -53.70293 | 2026-08-15 04:17:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc691466-67c3-3620-a2d6-db2a21f53463 | -13.75757 | -53.43277 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92d6b8e3-5ba6-3cfb-8046-53b8aeed3c6a | -14.49142 | -52.03786 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a80ee24-f718-3709-b113-d1b954dc2a24 | -14.57797 | -46.77284 | 2026-08-15 04:17:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 064ef143-d04f-365c-a634-9a7bf0927805 | -13.2611 | -54.19834 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfc097e1-4113-36ed-9ea6-572c8bfa4431 | -14.43705 | -51.94656 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a41b2c04-da76-3e03-ae96-e4349940c221 | -16.11305 | -49.86568 | 2026-08-15 04:17:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 749f942a-7f95-32c1-9906-a595bd8c908e | -13.75284 | -53.42772 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fdb59ef1-eb1e-3e06-b418-e9b83e0c6508 | -16.90118 | -54.16892 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcc64423-7463-37be-9920-72f7a2f17f52 | -20.01709 | -43.89798 | 2026-08-15 04:17:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 630fb38c-4fa8-35ce-a4de-9b94c5ac45df | -13.47028 | -51.81071 | 2026-08-15 04:17:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62884447-32b6-305f-a2fa-e21d9fda3f93 | -14.21634 | -45.41094 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89f1ed40-b8ae-343d-a528-a44bc51c5cb9 | -14.91774 | -46.62931 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 902a6556-39cc-3644-8be0-9d5ed16e5173 | -14.60713 | -46.74088 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad494eaf-b942-3211-870b-248637fc3d80 | -16.10885 | -49.86489 | 2026-08-15 04:17:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 26f9ea5b-047a-3903-8cb4-4e1744c43164 | -14.45148 | -51.92546 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf2727f6-380a-3bc3-a8cb-cbef7eb7ed13 | -14.96096 | -46.6284 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb6eac02-1b75-3bec-8248-76b0057b68ca | -13.81479 | -53.78896 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 580576c4-2096-3e60-aa36-d8588f2e925a | -18.55225 | -45.45224 | 2026-08-15 04:17:00 | NOAA-20 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c9792e50-10ef-3272-9860-9113a29b67a0 | -14.21975 | -45.41154 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f05ce4c-8901-31fc-aa21-1584a2691c8c | -16.1723 | -46.8055 | 2026-08-15 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53383d52-a8c8-36fe-bb64-381083078eca | -14.44541 | -51.93022 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0cfa895-1f55-391d-a659-8f9a94a0d66e | -14.07891 | -53.62347 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 500ff728-d1d5-36f9-ad06-7b97a8de8351 | -20.45815 | -46.47468 | 2026-08-15 04:17:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1a2224c-f127-32ef-8638-3b565f9d753c | -14.46278 | -46.76614 | 2026-08-15 04:17:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc7c238b-aae9-38e7-99b0-90ae81289e30 | -14.95033 | -46.63158 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd7ddf79-3fd1-3398-86af-55e8de60b26d | -14.49377 | -52.02612 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 103d86ca-33f1-3afb-aee0-2b93ada9c32a | -17.90273 | -44.44228 | 2026-08-15 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4991e12-0903-3304-ae84-e4e64e5284ec | -13.42361 | -57.05593 | 2026-08-15 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 535f9b14-78bd-38d1-be42-e34417e84d20 | -14.22998 | -45.41333 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 659d2072-8632-3071-a577-fff2b99c82e2 | -16.90291 | -54.16234 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16311b21-c204-3c23-8328-51f07e3c5934 | -17.90216 | -44.44588 | 2026-08-15 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5622dd10-077a-3ce2-9a3a-00305271f17b | -14.45634 | -45.6795 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 112007ea-e54d-3bb3-9ea5-0d4491f223c5 | -14.9142 | -46.62862 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a746dea-0430-3877-b8e6-d7358b3d0e8b | -19.50844 | -44.24855 | 2026-08-15 04:17:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7330bd5-7f4d-36c6-bd1a-a30d6ed3f3e4 | -14.92267 | -46.62192 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 00090f43-bd10-34a8-ad59-02fb34378063 | -14.59665 | -46.74999 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46c2d96d-9536-3589-84a7-3f7ef172fa28 | -15.29168 | -53.18659 | 2026-08-15 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f11d739-6bea-3605-b847-1d9fd1953311 | -14.09412 | -53.62719 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9770f44b-5da8-3ccc-8c60-9760ba0697c5 | -14.60239 | -46.73794 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 361cbffa-0928-30ca-a662-48273626a308 | -13.81811 | -53.78799 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bd76dcf-8b7a-3f84-b35f-d91d402342ae | -16.25518 | -53.70421 | 2026-08-15 04:17:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61d17c8d-cd98-3d07-b5dd-0ed16c44f9a3 | -13.75206 | -53.43159 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ee713ac-9f2b-3445-9f52-e48784d313a8 | -16.89187 | -54.15883 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 975dd0d4-829d-3d68-8372-dc7b57a9a46a | -14.22316 | -45.41214 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17ebbae3-16e8-3c46-82c1-72dc4956c998 | -13.47082 | -51.80794 | 2026-08-15 04:17:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31707d9a-a955-388f-a044-72aebcda4ef7 | -16.90207 | -54.16628 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b8cabff-ab1a-3bc6-b932-f4de2c72e671 | -14.07754 | -53.62343 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 20dfedcc-27c2-3175-9842-820909dab430 | -14.45761 | -45.67179 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1deaa4dc-8748-35a9-9ede-81ef1d6f3f16 | -15.12428 | -48.6978 | 2026-08-15 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6dfb0688-6ca2-3766-a71d-343e93af75ca | -14.08859 | -53.62591 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 738efdbe-ec01-3b11-b390-292dcb8cefd9 | -13.23364 | -54.1839 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e793825-797c-31a0-acbc-9a0ae3ddd817 | -14.72956 | -52.6885 | 2026-08-15 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 78423616-e4d8-330f-b7d7-7c637963b231 | -14.95108 | -46.62711 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b801f6e4-2dde-3230-8bf6-1fe65092c812 | -14.96022 | -46.63267 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d8d5693c-3931-3620-8329-dd8c775a53cc | -17.69033 | -44.21748 | 2026-08-15 04:17:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6db04feb-d482-34a0-888a-0245eee87c36 | -16.19527 | -45.26953 | 2026-08-15 04:17:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84d35702-1d09-3a40-98f9-d00986cb4fc9 | -20.45586 | -42.01737 | 2026-08-15 04:17:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 70f13b96-50d1-30de-97d0-6aa55450eb06 | -15.12664 | -42.12777 | 2026-08-15 04:17:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |


[Clique aqui para ver as próximas entradas](README18.md)
