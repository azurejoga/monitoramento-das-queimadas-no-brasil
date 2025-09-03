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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aaa0e81c-8620-3db0-8960-09b6145c49bd | -10.89472 | -45.79253 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ff4b67f-b73d-3a69-8347-926b15629dc9 | -12.95922 | -48.07349 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 02c5507e-870a-365e-8d90-0f8c335ebdb2 | -10.91265 | -50.8329 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6858397-230f-3c1d-bfdd-88b18dc35cac | -10.48684 | -50.34269 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83ad8530-f83f-3378-a3cf-52ec33038a7c | -14.56429 | -49.1496 | 2025-09-03 03:55:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43d00a45-097e-3056-bc4a-61cb613d6f5a | -10.73158 | -44.80669 | 2025-09-03 03:55:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f3a59f2-5e70-33db-9f85-92dcb3b09805 | -11.8909 | -46.66704 | 2025-09-03 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94959e0b-554b-3f12-a7e5-93d05612ecfa | -11.08107 | -45.12303 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f9f368c-83c1-3596-af0a-9d2ad9564ba5 | -11.38972 | -43.63164 | 2025-09-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62cfab8d-bf7f-348b-8a32-c1b33dd3e178 | -19.13879 | -47.70314 | 2025-09-03 03:57:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22d8e097-f555-3c82-bb4b-934aedc94dce | -22.1696 | -48.83363 | 2025-09-03 03:57:00 | NOAA-20 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d4ad99dc-76a7-3d72-bc2d-dbafcd98cc54 | -15.73448 | -53.69025 | 2025-09-03 03:57:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| af549570-26dd-3aff-961f-7bf29e1ef943 | -21.3022 | -48.55107 | 2025-09-03 03:57:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bebdcadf-31a0-3018-862c-05e299049124 | -22.86791 | -47.39339 | 2025-09-03 03:57:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b8b95527-d553-3d7a-ae62-1fdeaea91b48 | -15.74377 | -53.69221 | 2025-09-03 03:57:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4a75bfc3-b92d-34b6-8302-5b37df908bd4 | -17.53385 | -47.57644 | 2025-09-03 03:57:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf9cf208-4c0e-3ed6-8a0c-5b2214932339 | -18.02975 | -51.59137 | 2025-09-03 03:57:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fa909ef-43f1-302d-9010-8893c809ee4e | -15.71978 | -53.64396 | 2025-09-03 03:57:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ae7a0c2-e9c3-302f-b535-9f1eb0c35a64 | -15.74102 | -53.69192 | 2025-09-03 03:57:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 246709c7-a520-39a5-8106-24275f19157e | -17.94474 | -47.23535 | 2025-09-03 03:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac48f3f8-5bc6-3f35-b8a3-041f5722dcd1 | -18.13798 | -51.75593 | 2025-09-03 03:57:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 74c0b61d-1dcb-30e4-a51b-ba3a2dfc15f8 | -15.74227 | -53.66735 | 2025-09-03 03:57:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b61e6a8f-a4cf-3c23-9886-3dc33bf776c2 | -15.73971 | -53.69777 | 2025-09-03 03:57:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| edc9e391-c09e-3927-a878-1625ce68c497 | -17.91983 | -47.21088 | 2025-09-03 03:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a8955cf-2ea6-334d-8eac-ee2d73ce2ea9 | -17.94209 | -47.22619 | 2025-09-03 03:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 75709f3b-76f8-3818-9a25-8f12df95563b | -23.9252 | -48.8609 | 2025-09-03 03:57:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98f64130-ed95-3ed5-b532-357765d7e5d0 | -15.5829 | -54.32951 | 2025-09-03 03:57:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65ea62e2-32ca-3f4f-bb88-0789aa03385e | -17.18967 | -46.05841 | 2025-09-03 03:57:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cf1a1aa-525d-3c1c-8388-4f7c3ad72235 | -18.92725 | -47.57568 | 2025-09-03 03:57:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ac94034-70e4-3843-82de-7331e826be29 | -18.03058 | -51.58751 | 2025-09-03 03:57:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebf781bf-2820-3670-940c-c34b36c062d5 | -22.18441 | -48.82747 | 2025-09-03 03:57:00 | NOAA-20 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.2 |
| ad08020f-3bcc-338b-b132-10611bf79916 | -19.42564 | -45.56631 | 2025-09-03 03:57:00 | NOAA-20 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0be1ce4f-de63-3a48-8805-10b0f989718d | -22.17575 | -48.82547 | 2025-09-03 03:57:00 | NOAA-20 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 74073ecf-0c47-3730-86c5-e50adb66ac35 | -16.63771 | -49.28605 | 2025-09-03 03:57:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aebb1f25-99f9-3ca4-a7ee-d25933c57dd4 | -18.06566 | -45.99346 | 2025-09-03 03:57:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1071a80f-34c4-3507-883c-b3e6fd0c91d6 | -17.24747 | -44.86008 | 2025-09-03 03:57:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0745727-0321-30f2-a349-31ec4bd138d6 | -15.74887 | -53.68776 | 2025-09-03 03:57:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4efb2b38-a1e0-3aa3-ac6b-1f947f5ff97d | -22.70837 | -47.03803 | 2025-09-03 03:57:00 | NOAA-20 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27b7183e-ce4a-373b-9247-b9faad500056 | -22.17919 | -48.83099 | 2025-09-03 03:57:00 | NOAA-20 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.7 |
| 82d752de-4aba-3ffc-9b82-dc790a1edad4 | -20.59877 | -45.11184 | 2025-09-03 03:57:00 | NOAA-20 | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| becded77-c027-3927-9b2a-080b87fbfeab | -20.75916 | -45.20525 | 2025-09-03 03:57:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d6e15592-2211-3508-ae34-b91ea8ff605d | -15.73563 | -53.66615 | 2025-09-03 03:57:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc8cd201-dbf0-3bd8-9001-2e88a940061e | -20.74653 | -47.13311 | 2025-09-03 03:57:00 | NOAA-20 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dcbd49f-92fc-3982-9361-2ce4a6f2072c | -20.40694 | -45.69675 | 2025-09-03 03:57:00 | NOAA-20 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9874de8e-47d8-35d5-b827-3819ca5b7f58 | -22.18008 | -48.82646 | 2025-09-03 03:57:00 | NOAA-20 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 4cac68b3-5c79-314a-b209-69d255f49e8d | -20.69715 | -46.33014 | 2025-09-03 03:57:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4673f9d6-f992-3594-b607-4d7bd966e5e0 | -20.88758 | -50.09693 | 2025-09-03 03:57:00 | NOAA-20 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 94038a1c-3a7f-34c4-b2c3-009e14b01f27 | -19.13964 | -47.69861 | 2025-09-03 03:57:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 659b31cd-c402-3a3c-abb8-cc9acfec9ab8 | -17.92482 | -47.20773 | 2025-09-03 03:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d5bb27a-1aaf-3b45-98b6-1a1983e5704b | -15.57629 | -54.32692 | 2025-09-03 03:57:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 017d5f1f-e178-332d-9656-67b7b58f5e23 | -16.63653 | -49.29182 | 2025-09-03 03:57:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 247706ad-0d38-30c0-a112-137783179a2d | -20.4032 | -45.69607 | 2025-09-03 03:57:00 | NOAA-20 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d482d593-ac24-38c6-a3b7-367bd0ad7340 | -20.19137 | -45.70351 | 2025-09-03 03:57:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a3dcdd1-f2f2-3d2c-9c29-5a0fd3b40300 | -23.35095 | -47.72408 | 2025-09-03 03:57:00 | NOAA-20 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3990f699-45cc-3042-b89c-75bb3e388bcd | -17.92477 | -47.17898 | 2025-09-03 03:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1711970-6c79-33cb-ad7a-c8202c1deb99 | -20.19049 | -45.70832 | 2025-09-03 03:57:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8ff506a-327c-3497-998f-fa63aedae41d | -19.74553 | -43.29647 | 2025-09-03 03:57:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a1b4644f-6a6b-3992-9a4b-2d7225d07061 | -15.73599 | -53.69618 | 2025-09-03 03:57:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c730514-9cd6-38ec-88ef-3aa5a2b78e48 | -17.53327 | -47.57951 | 2025-09-03 03:57:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d60ec3f3-04db-338e-bf45-13a4b695e402 | -16.53 | -49.4085 | 2025-09-03 03:57:00 | NOAA-20 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 962b29e0-d35f-3723-8687-5029972c694f | -16.30572 | -52.96745 | 2025-09-03 03:57:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e06db66-4a8a-3161-bbfc-24ac0c3d7494 | -22.00566 | -45.06202 | 2025-09-03 03:57:00 | NOAA-20 | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 54e5cb25-f27a-3567-b4bf-51b3613b59b3 | -22.49078 | -43.72414 | 2025-09-03 03:57:00 | NOAA-20 | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b8ac3939-dd42-34e6-a09e-6f7dc1944ee0 | -18.13882 | -51.75204 | 2025-09-03 03:57:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ccb2fa4f-5a62-3bb7-b71d-40db0c96e5c4 | -21.30131 | -48.55555 | 2025-09-03 03:57:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 852c9d11-b99b-397c-b26b-388da054e4b1 | -22.75633 | -47.27608 | 2025-09-03 03:57:00 | NOAA-20 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 9c58b9ba-9ef4-30d9-b3ab-aad58bed4e78 | -19.74827 | -43.30101 | 2025-09-03 03:57:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 8ee9244d-cc1e-3c95-9bbf-9aeddf584002 | -18.02722 | -51.58691 | 2025-09-03 03:57:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f0507fa-3488-383d-a01e-14b0944da8d0 | -18.50659 | -49.65462 | 2025-09-03 03:57:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| f25b2e1c-f8a1-34f8-9279-c11447cfa745 | -22.17394 | -48.83461 | 2025-09-03 03:57:00 | NOAA-20 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.7 |
| fa69da04-e240-3a7b-9f69-e68f16e29587 | -17.19369 | -46.05912 | 2025-09-03 03:57:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4135ac32-d44d-3640-92b5-56797fe14e37 | -23.39209 | -45.96122 | 2025-09-03 03:57:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 23e23617-f81e-3d54-8368-c990585a8f31 | -23.93025 | -48.85755 | 2025-09-03 03:57:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec89fc1c-fb68-3753-a6d4-95b08c16f5c9 | -19.14453 | -47.60243 | 2025-09-03 03:57:00 | NOAA-20 | PEDRINÓPOLIS | MINAS GERAIS | Brasil | 3149200 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b831dc83-02d4-3182-a811-e99444d095a7 | -16.84764 | -52.11394 | 2025-09-03 03:57:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5172e717-3523-3c16-968c-a2c4fd5ed421 | -20.69332 | -46.32928 | 2025-09-03 03:57:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c29c9bb-bb8c-30f6-abd8-414468c58cc0 | -15.58278 | -54.32931 | 2025-09-03 03:57:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29a35828-8cfc-37c6-8c81-4d8523bae3c3 | -17.53909 | -46.61422 | 2025-09-03 03:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 623e6747-8775-3cbc-aad9-f8f38fff0641 | -16.29063 | -52.96056 | 2025-09-03 03:57:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| af952788-dedf-3072-9eee-75b10f3afe06 | -16.85812 | -49.60638 | 2025-09-03 03:57:00 | NOAA-20 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0628402-02e7-3ca4-8c1f-eb5055b229b4 | -17.94397 | -47.23936 | 2025-09-03 03:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd98f19e-4d82-3079-837b-1e9b24d39409 | -22.68581 | -46.88164 | 2025-09-03 03:57:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a2e035c4-5709-30c5-9f4b-8c8654c8cccc | -19.38142 | -49.06896 | 2025-09-03 03:57:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96b4da32-708b-3d74-a9eb-6de2bb48409e | -20.89239 | -50.09806 | 2025-09-03 03:57:00 | NOAA-20 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| cd3d8b2f-e021-32c9-ab98-d673ae7a3b9c | -22.00646 | -45.0574 | 2025-09-03 03:57:00 | NOAA-20 | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a7931494-9ce1-3bd3-8454-4ef6d2be404b | -18.65828 | -49.09612 | 2025-09-03 03:57:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fb14171-e6e9-35fa-aaf5-0f2d98891d69 | -22.17403 | -46.61496 | 2025-09-03 03:57:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 330d52a8-2c23-34dd-9738-114b7a999d33 | -18.14052 | -51.74419 | 2025-09-03 03:57:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6979a5a6-1694-3d99-ad17-0edfe59f9318 | -23.53562 | -46.86948 | 2025-09-03 03:57:00 | NOAA-20 | BARUERI | SÃO PAULO | Brasil | 3505708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 80bda0a3-b3d4-36ec-94f8-7adc5bf24a41 | -23.39126 | -45.96574 | 2025-09-03 03:57:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 993c7f2b-9899-328d-abb6-20c70f73aa59 | -16.29315 | -52.96489 | 2025-09-03 03:57:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0d507a1-0496-3f46-9f96-b73e650b977c | -20.7067 | -46.2994 | 2025-09-03 03:57:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 354a3c0d-730b-302f-aaf2-37924b6d307f | -19.75232 | -43.2978 | 2025-09-03 03:57:00 | NOAA-20 | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 5c540d5e-aada-3654-9ea3-53daa4902ff5 | -19.13686 | -47.70088 | 2025-09-03 03:57:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5fd1481-55f9-3962-858f-354955aea7fc | -18.12076 | -44.98755 | 2025-09-03 03:57:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6cae05f-3ea9-3ec8-a12b-392e87876a9d | -21.08652 | -45.45576 | 2025-09-03 03:57:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d07bf726-7ee9-3b79-9407-654c50c8f811 | -19.74488 | -43.30035 | 2025-09-03 03:57:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b79a141d-2b3b-3d7c-907a-9e86dfe3cd00 | -17.36408 | -49.17821 | 2025-09-03 03:57:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e1499851-50f9-3927-9dd2-09393b11e63f | -23.92911 | -48.85994 | 2025-09-03 03:57:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23696f1a-6a2a-3b93-8fa4-705ec5a3c7c2 | -17.91835 | -47.21216 | 2025-09-03 03:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README46.md)
