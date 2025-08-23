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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd1f0f5d-fa7f-361e-80c7-143bb7f0f906 | -9.51656 | -58.34857 | 2025-08-23 05:21:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57886e74-3b32-31b1-8f8f-7d43ec6a75b2 | -14.27221 | -58.53204 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 34b5e8d6-ec6f-3495-9d9c-d1a8442f27f7 | -9.51766 | -60.50893 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e624b9e-8913-3506-8c04-ccf729f65f30 | -10.7516 | -48.25282 | 2025-08-23 05:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6b43d17-c0d9-3d61-9230-5394694eb574 | -9.19671 | -59.46154 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0abc94ed-425e-3bcd-92a6-151952081fa5 | -7.44304 | -63.3051 | 2025-08-23 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3fb1aad-f8a3-3f2a-aa1a-d4c689064f91 | -9.20003 | -59.46206 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9fe225c-4098-3006-a449-630655701f06 | -14.28541 | -58.52568 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80f7318c-4102-34e8-b846-d42fa859b747 | -9.44237 | -47.64872 | 2025-08-23 05:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d17830a3-eb87-35b7-8bf5-ce4222f960db | -11.61947 | -50.42327 | 2025-08-23 05:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca0b606c-1274-3747-88ed-93308620474b | -9.96221 | -60.18119 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| b8719749-21f8-3bd6-9177-e52cf157a7aa | -9.95607 | -60.19825 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 4cac4800-dce3-33ee-8061-b6a78395adc5 | -8.87524 | -62.42427 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75d9e1fd-7641-3a61-931c-cea7162005fc | -9.19615 | -59.46503 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bff80ea4-2ae3-3ae4-8f73-686185556769 | -11.93954 | -58.76412 | 2025-08-23 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 384453f6-f18c-39e3-8643-972ce9982f4e | -9.03036 | -59.0126 | 2025-08-23 05:21:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d1464bb-e095-3c25-9fa7-aaa311ef1c35 | -14.29375 | -60.38908 | 2025-08-23 05:21:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be021cf4-024e-344d-bd06-ef2fd3661904 | -13.39353 | -46.34592 | 2025-08-23 05:21:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 50c4b5e1-30da-3d54-8ee3-55840a471ea4 | -9.46062 | -60.37194 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f186d9a-88c2-3f7e-8842-15bc563459e5 | -9.20342 | -59.61304 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ffe455b2-a8fb-32a7-83c4-6f8823a58ef7 | -9.19291 | -59.6364 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ed8db57-9c5d-377a-bc1e-f61017d7ba93 | -9.22939 | -59.74616 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53d3bd25-f3cc-389e-914b-fbb10dbfdeb3 | -14.96891 | -48.67353 | 2025-08-23 05:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ab1ec2d-1d90-3af2-98d0-676a92aaaf86 | -7.54869 | -63.85074 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d73a467-a775-3252-b45c-a2da6e0e6468 | -12.70775 | -48.106 | 2025-08-23 05:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ab5cbcf6-74bc-3594-bf56-2f16654554c1 | -9.9533 | -60.19419 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 7d6bc2fd-6b10-3ed7-a04e-53c4cb1ad5b4 | -14.28833 | -58.55387 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b03a74f3-aacb-3e8a-8bb5-3545036fcb4e | -9.18958 | -59.63586 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 985c558a-5817-37eb-8779-892b7e6eb6fb | -9.51709 | -60.5125 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a0834e3-f412-358a-8c7c-07218be46acc | -11.93899 | -58.76775 | 2025-08-23 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58b342f0-069d-3743-9f12-1eae1b255b0e | -7.30249 | -59.62777 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38a43b30-855b-3908-bac8-65a72a79d367 | -6.83094 | -59.88782 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 56235df1-fe73-3c35-a31c-2ac99f3040f7 | -9.95442 | -60.18715 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 557695b4-ba44-3197-a821-88127ebb905d | -9.19338 | -59.461 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b209446-d9b0-3d3a-acc0-f2bea6f5b20e | -14.37459 | -52.05852 | 2025-08-23 05:21:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b8939e4-c391-389b-932a-5eb66791ac5e | -9.20898 | -60.82408 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e995c49-a0c6-38b7-a954-a0b0275e25c4 | -9.23723 | -60.47836 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 253efd4c-71f0-306b-b685-0c254bf79ab0 | -14.6727 | -54.92828 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| aac0eb0e-4355-387c-9b6e-9a5394945f2a | -8.36945 | -54.986 | 2025-08-23 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27f10b46-c2f9-308e-bb62-7996c68bbd6b | -14.73644 | -56.02559 | 2025-08-23 05:21:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1e28c8e-24b3-3246-a3de-3d58f8215cd7 | -9.52765 | -60.53252 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d3a5b55-1b56-3c1f-b445-74f27f8d37c7 | -13.02759 | -56.81751 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bdb4394e-c00b-35c1-94a9-8aa64106d85c | -9.95498 | -60.18363 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| f3603b4e-a8e3-3ba5-8781-a1d625e6e79d | -8.9006 | -62.43201 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 586e857d-8f7b-38dd-a55c-f24f13074bf8 | -8.88156 | -62.40832 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7bb4398-3fa1-3962-8b0a-0db4dd49784f | -9.88489 | -60.28844 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a08e2a6c-3b1c-3982-b7c2-2a99f77cbb00 | -9.20778 | -59.45614 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 944ebf46-a2aa-3b97-a851-ed30c76f3732 | -7.78353 | -61.57278 | 2025-08-23 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17889f27-967c-3667-a509-923ae1663c13 | -9.51815 | -60.52732 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba17688c-0152-3534-939d-26a2f3c8a6ad | -9.52208 | -60.52429 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a34b8f7f-9701-313b-b946-56ffafa51437 | -12.5005 | -53.82417 | 2025-08-23 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fea97cc-256b-3cb8-9c90-129720e45c40 | -9.23049 | -59.76069 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 793d2ea6-cfe9-3713-a3b8-edf99f1a1eac | -9.25323 | -59.61737 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c2827ae-b15e-3aaa-aaf7-209d8f029dd8 | -8.89324 | -62.42731 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb30f9eb-8ec4-339a-9918-6fd1dd2ee503 | -12.79101 | -48.72303 | 2025-08-23 05:21:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 411cc0ca-40e2-30e6-91cb-c0aceb238f10 | -9.07224 | -60.41476 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d4b79993-d97a-3c09-bbe4-1120d700a228 | -9.20833 | -59.45264 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 493d99f2-f999-31c2-bca2-5a5852215d26 | -7.81293 | -61.328 | 2025-08-23 05:21:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63996b65-2b09-380e-9cde-00c25612751c | -13.16762 | -46.91943 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e5e62f30-8bd4-3f77-ad89-de4e36c0f453 | -13.02563 | -56.83083 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b37f0dda-3f45-3d2d-87f9-6cd780be5d2d | -8.85116 | -49.86793 | 2025-08-23 05:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88422fea-a0ca-34f5-9b18-edcb7f418de1 | -9.20779 | -59.47763 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f38b550-b78d-33fe-a6e6-a0fce2d7b06e | -15.03573 | -49.60135 | 2025-08-23 05:21:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6f93ea5b-cb61-3a60-ad5f-deaa7b8f1568 | -6.94225 | -59.55581 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 811b4f86-d003-3419-bcf2-5e8a271988f9 | -9.2039 | -59.45911 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fd65f99-8acc-3343-a679-fa4767d5b505 | -13.3772 | -46.21821 | 2025-08-23 05:21:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5150441f-24f7-333f-add7-e5fb0e181f57 | -7.03461 | -59.91355 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79b262e0-b45f-308c-8073-18ec4a94d59c | -14.28488 | -58.55334 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 057e6824-ff75-32c0-8a5d-eea21a88ccce | -8.89908 | -62.43683 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 56d35831-3bce-37d3-9fe1-fec2f08b5ee1 | -10.46644 | -59.1319 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63d7d316-9edd-34f4-b732-662b92b14e23 | -13.02664 | -56.86467 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf691381-daba-3f9a-a264-a8b4d1672c6e | -8.61358 | -62.60773 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05bd4f64-c646-3067-aa34-a181ea1cb4c6 | -8.88468 | -62.43439 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7c3e5a9-6709-39e3-81e7-e1a0ec8c09fe | -11.3097 | -55.13969 | 2025-08-23 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51debef4-71f1-3d87-b406-c893b166ba5b | -14.30964 | -58.55322 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5dd444a-f94e-3d1e-be9e-cff491d30483 | -9.84583 | -56.07531 | 2025-08-23 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90e29aa6-8364-364a-9263-c934c3ea6fc4 | -9.19567 | -59.61897 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb363a3d-364d-3654-abfb-d3bc480fd900 | -9.82192 | -64.26739 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| acfa421c-9657-3dba-abb2-e62a1560dfd3 | -9.52144 | -60.54982 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 680ea73d-3cb1-3d14-9ee4-b9d03b23416a | -12.79315 | -48.72477 | 2025-08-23 05:21:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 523368a6-585a-37a3-9efa-8b1a4ae1cc3f | -7.10662 | -59.77656 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 034a1c5f-b8e8-36d0-9cb7-0769bbcd0db3 | -10.10758 | -57.7664 | 2025-08-23 05:21:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d800b80-31dc-3392-a242-d7ca324a640c | -12.77561 | -48.71297 | 2025-08-23 05:21:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 728d913a-6a91-367b-9462-0fc0ff3cbf77 | -9.52322 | -60.51715 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86a01697-be3c-307d-bfdd-0276f718d071 | -9.02703 | -59.01206 | 2025-08-23 05:21:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 309b2a53-0c30-35af-80f0-cfcbf8d810fd | -10.40733 | -57.68053 | 2025-08-23 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a0083bd-b2d3-3c99-8970-5bf41b29cdc5 | -12.78016 | -48.70702 | 2025-08-23 05:21:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d9ddbe8a-e1dc-318c-a7be-0d2bffb19f3e | -9.25543 | -59.77545 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 182e8a56-ce05-3cfc-aed7-bb62367833ab | -8.85208 | -49.86081 | 2025-08-23 05:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22404d7d-cd78-3bf4-994b-a4ecf43bb72e | -9.15006 | -59.50436 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0f3878c0-f1a9-3587-ac08-829d0598ea0f | -9.16741 | -59.60369 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea38f8e1-c99b-32f5-adf2-713e44d7c9ce | -9.20952 | -59.61761 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da3e7ee1-5df3-3417-95be-19e0d117f645 | -9.18347 | -59.58835 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01ff653f-8d60-3182-89b2-58166dc8debb | -14.75802 | -55.9867 | 2025-08-23 05:21:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34ec6c9e-0fbc-3229-9d28-b74a0757f3f6 | -12.5105 | -53.81656 | 2025-08-23 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70005e3e-5382-3e64-9afe-e47ea75ef34a | -9.16187 | -59.59563 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfea801d-b926-341e-84c0-cf860608b240 | -14.66505 | -56.58713 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6c1ca3e8-a723-32b9-a011-9f226de2c32f | -9.16076 | -59.60262 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 333baacb-f979-3a3d-b8a4-9bf9f738115f | -14.76197 | -55.98727 | 2025-08-23 05:21:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3e42de1-a45b-3fef-93d8-aad675f68256 | -9.95 | -60.17199 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README65.md)
