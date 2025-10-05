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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4360a468-e5c2-3b5f-891e-1a3e070acbbd | -5.8388 | -44.461 | 2025-10-05 03:32:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 13cc74cf-29c0-3eb1-acd6-8b704ab6a068 | -5.77518 | -42.94829 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 22.0 |
| fb4b9a8a-1c16-3954-9d10-f26f2a0d6e47 | -5.83993 | -44.45467 | 2025-10-05 03:32:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| c31f46c6-af24-3aae-be24-d38f77119c09 | -5.77908 | -42.93274 | 2025-10-05 03:32:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| 1e4deb9b-53ef-3c2c-87c3-46c907edd9c2 | -5.91208 | -42.53841 | 2025-10-05 03:32:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a278687a-bd9d-322b-89d7-723363cd8acf | -6.13868 | -44.64209 | 2025-10-05 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5da48b4e-5fe6-35b1-b8b7-43dc566416a9 | -6.40849 | -43.06876 | 2025-10-05 03:32:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 7f11165c-c300-3621-9267-ff18afd33306 | -5.9271 | -43.33043 | 2025-10-05 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bc54f3d2-b4bb-3323-9eda-f3dde11813b3 | -11.83286 | -45.04949 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edf0f130-8e9c-3867-9184-92ed67cf9958 | -13.35837 | -48.06138 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2eb770e1-8b70-31e1-b2f9-2462d937dc73 | -12.45612 | -44.74109 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2645a9e4-adfd-30c0-8164-a86b3447ac5c | -11.52931 | -47.68172 | 2025-10-05 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7d568c3-255a-372d-b5ac-da4682dc7120 | -11.53039 | -47.24195 | 2025-10-05 03:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c848ed0-db36-3fa0-927c-c7bf1c0e6293 | -11.80574 | -46.84528 | 2025-10-05 03:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88cda4a9-3148-3d8c-b5f8-52a8b5d099fa | -11.81975 | -45.07061 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fae068fe-dd73-361d-945d-5d82fb96c7dd | -11.82169 | -45.06116 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82f5fd97-6f9f-3422-a024-a8b457bd9360 | -8.78835 | -40.56655 | 2025-10-05 03:34:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 65339caa-14d9-39f4-8953-dfca2475e0a3 | -13.2892 | -47.18068 | 2025-10-05 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04879bd1-e472-33af-b174-c84b176d5c73 | -10.94532 | -47.06773 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 980cf488-1980-33bd-86c1-998c9a3f86e9 | -13.58917 | -48.1674 | 2025-10-05 03:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fbc51fae-91da-3b1b-b219-61c5af35cc0e | -11.62265 | -45.02828 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1411f449-b549-303f-9107-215c0ae0da4f | -7.47459 | -43.03241 | 2025-10-05 03:34:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 87309703-6601-3be2-8d4a-921313efdeff | -11.66895 | -43.90107 | 2025-10-05 03:34:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0b04ab26-5971-3f65-a4d5-686ea9d009b0 | -8.56157 | -46.36736 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90393fcf-c5d2-3252-b0f3-807da758672e | -10.94875 | -47.06874 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| c2c33fbd-c0d6-3f5a-b308-e2d0804865e4 | -7.72636 | -42.38717 | 2025-10-05 03:34:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fde532df-b084-308b-8b17-bbda76ccc73a | -12.39993 | -44.83103 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21a34737-81e3-38a2-91f7-1945afc47a11 | -8.78958 | -40.56833 | 2025-10-05 03:34:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3f0a3d59-3d48-3427-a7a2-357a86d03b94 | -11.75999 | -44.74732 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3897d204-0060-3f2d-9210-502d6d96c0ec | -13.31952 | -47.17297 | 2025-10-05 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 11bf1770-a2aa-33d6-8b28-f5db0085b470 | -13.25855 | -47.82297 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0743cf1c-06ac-37d1-9bce-d3f7955c8a60 | -9.24975 | -46.78519 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b1573fc2-052c-356a-a375-079a2ba068a9 | -8.55332 | -46.27746 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 10f9f378-51f0-39bb-a84f-ba6fdc440579 | -7.71881 | -46.27422 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dbc00cfa-4648-30e2-9c3c-65ccebd1bd93 | -10.39919 | -45.3977 | 2025-10-05 03:34:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b742a05e-6f66-313c-9998-45661237611f | -10.6233 | -43.31823 | 2025-10-05 03:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 403be169-4d45-32b9-9aac-d2f8363a01c8 | -11.87256 | -44.96991 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d2ceea78-2536-38fa-a195-ebab7c2b3d9c | -11.69199 | -47.48715 | 2025-10-05 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee092843-7bc6-30bb-95f8-81edf46931a3 | -11.70317 | -47.50486 | 2025-10-05 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eca14a99-6d2e-3c01-81f4-1ed03cd806fd | -7.47204 | -42.63236 | 2025-10-05 03:34:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 02fcf8c2-0210-332c-883a-ba68aac15004 | -11.57922 | -46.76908 | 2025-10-05 03:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7c10127-e1a1-3899-9ecc-7aac612d4674 | -11.81979 | -45.05025 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c2f47dc-89f2-3be0-a194-31e90d3555e6 | -13.4783 | -47.23036 | 2025-10-05 03:34:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad68b118-c0a2-3a68-9dec-e9c7da182a30 | -10.95156 | -47.05515 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 363155ef-6295-3043-a309-6d97e4051e74 | -8.54538 | -46.31805 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 62ebecbf-b695-3f85-932a-11474b59096c | -8.58451 | -46.30495 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 137bda1e-2601-345c-b700-6a278e848c13 | -8.57683 | -46.32786 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 92ac852f-2f47-3504-9205-285609b454f5 | -13.11994 | -43.84715 | 2025-10-05 03:34:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 12e0e21a-4b88-33e9-be6b-d0ca0a6791f3 | -13.52258 | -47.29108 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ecf10a8-8732-3e87-9220-2bf22d494a21 | -7.74946 | -42.51604 | 2025-10-05 03:34:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 02a62862-7ba5-3a08-8816-797de21b315c | -7.71806 | -42.5587 | 2025-10-05 03:34:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6bf168b4-22a1-3be6-a658-9c587365cc77 | -9.28071 | -46.00803 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b68b5c1-b5ef-38fd-90a3-7141c4cfb579 | -7.68923 | -42.58372 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 41b84be1-de5b-31e6-aa3d-0611d1948ec2 | -13.28853 | -47.58214 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b122c934-4b7f-3eb7-86a4-95ecf948b78d | -9.19939 | -46.92687 | 2025-10-05 03:34:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 011dcbe1-c97b-330a-968e-d41250b03cef | -9.36542 | -43.02823 | 2025-10-05 03:34:00 | NPP-375D | VÁRZEA BRANCA | PIAUÍ | Brasil | 2211357 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8ea1c3b7-0d2d-366b-b8c9-fefbfdddd419 | -12.60689 | -48.12111 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 166a2a87-54d5-3603-9b93-6851ef4bf6fe | -11.48522 | -45.0347 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c56ed1c1-72f1-3ce8-8d49-445c0afe45ba | -13.00126 | -43.99786 | 2025-10-05 03:34:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c3f04e4-e4fc-3f78-a413-0bc3309d490f | -7.69421 | -42.58892 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aeccf22a-5779-3deb-ba99-f2d9d8f4c3cb | -10.8654 | -45.40833 | 2025-10-05 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dba96410-c672-3b22-8cab-cedc9d9d358d | -13.48263 | -47.2756 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ce1a50f0-9d39-3269-9204-d048334eb0cf | -11.89504 | -44.98589 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6da3a8bf-f115-36bc-8aae-839af6dfd309 | -11.52361 | -47.67299 | 2025-10-05 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bc4e1acf-7942-3e31-89af-cee7b716ed5b | -11.87859 | -44.97187 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7fe7e9fd-fb90-36af-8eb7-0d70723344b3 | -12.10392 | -43.44848 | 2025-10-05 03:34:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4737b777-a514-3f82-ae46-d0a8e76ed7d8 | -11.85306 | -44.94706 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3dca588-ef35-34cd-8b04-74819efbfee7 | -14.2709 | -45.87197 | 2025-10-05 03:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d6ddb59-2292-3a8a-9e1f-84488ba2865b | -11.0094 | -45.58909 | 2025-10-05 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a292ddc-b963-389f-b298-53959515902a | -12.90251 | -47.32075 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 004c60d7-a58a-312d-8604-92ef7a9bc7fe | -13.3196 | -47.17245 | 2025-10-05 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ca7908d-b58d-3850-a579-4f5eca8dae04 | -7.46679 | -43.05413 | 2025-10-05 03:34:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e6ceb65b-c886-33e1-9b8b-91b9206bd983 | -13.28244 | -47.17884 | 2025-10-05 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0f208506-9875-3415-864a-bd6278e1e6e0 | -13.48444 | -47.26809 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| edf2531b-d116-351d-9616-21504be25974 | -10.94963 | -47.04755 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0363632d-8748-3e0f-a829-83d8e703d80d | -12.82398 | -46.85209 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ab8f24ce-abf5-3f82-aca9-4fab9fac53d1 | -8.57259 | -46.36651 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69c7acec-fc63-3923-9b68-5384f740139e | -7.72783 | -46.31914 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 824283aa-b2ff-343a-963e-65550aae8d4e | -13.29574 | -47.82244 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5aeba521-8815-3909-bd62-7f074a814f54 | -13.3507 | -47.58446 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d39b045e-ba20-31b0-add8-66fa735af94e | -12.82331 | -46.85793 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7e7f57a-662a-3044-93f6-627eb53879a8 | -9.56992 | -46.12611 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 070726b0-4c6a-34d5-89f3-8187b1bdf9ef | -12.45984 | -45.50488 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a26e44e-d332-3644-a19e-54bfd7a8ca1a | -9.25172 | -46.78392 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 69b87a0c-a249-3e26-8634-97f297cc3dba | -13.24456 | -47.81906 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aecee26c-8674-3b49-bcf7-5e7adcb4ecfe | -12.92574 | -47.30447 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 94b9631a-96f8-356e-a87a-b23da3ed2643 | -13.0296 | -42.4545 | 2025-10-05 03:34:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 65691b57-14d8-3133-bbfd-c12cb97c6de1 | -7.43626 | -46.52466 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 407ea802-9815-3821-a93b-c9579c52d20e | -13.30055 | -47.8126 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1a2aea4f-c8d7-3346-84a0-2bc101574e4d | -11.93304 | -46.43963 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be6da511-3326-3b1d-9b41-45ba2391f105 | -7.79933 | -42.56568 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c5a4b452-b264-332a-a969-74b706b44add | -12.39385 | -44.82987 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 315536e7-1b3e-3aff-881d-02b30c732703 | -13.08254 | -47.9002 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 31c38025-2f5c-35f5-bb8c-54bff30cc75a | -13.24761 | -47.81706 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49ca8905-60fc-3388-b6dd-5fd3dbb61cf8 | -11.81236 | -45.08764 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cb920fb-fe28-3fd9-8dac-7e9fdcd17333 | -13.30881 | -48.12388 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e0d6a9d5-7fad-32bb-afda-b70b44e21af3 | -11.8795 | -44.96737 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c2770ab-91ce-3d19-b7e3-4c9e23264a2d | -8.57618 | -46.3102 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0de9fb72-0bd6-335a-b621-e5eb5c1b6fee | -8.56019 | -46.3742 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| faca795a-722d-3f2c-9c83-f236aecf9717 | -8.58669 | -46.31519 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |


[Clique aqui para ver as próximas entradas](README26.md)
