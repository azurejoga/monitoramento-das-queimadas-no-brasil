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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd82d0b2-3a6c-3ce5-94ba-1819f5b3ab40 | -16.2585 | -53.67891 | 2025-06-28 04:32:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88725278-fc47-3033-a1c0-4d9095fc8585 | -18.33808 | -55.90368 | 2025-06-28 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.1 |
| 7f85c1e0-3bc2-3371-b040-fcff8b7b51d9 | -18.33276 | -55.9073 | 2025-06-28 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.1 |
| 330eb6c4-d6ef-3e65-95c7-d527a791b78f | -17.68861 | -54.00916 | 2025-06-28 04:32:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8dffaea9-d48f-360f-a8c8-a114500b39fd | -20.7619 | -46.76741 | 2025-06-28 04:32:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f4ff0bbe-e7c8-3fcb-8301-6798e6960ceb | -20.85195 | -45.52973 | 2025-06-28 04:32:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bce7e6b-9991-3f2e-b068-92184c48021e | -16.25385 | -53.68166 | 2025-06-28 04:32:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cfcbdd96-c63f-3b96-9b23-2258ad8185b3 | -21.10831 | -45.71042 | 2025-06-28 04:32:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0c103d4b-dced-3807-b657-619a788f577e | -21.94032 | -48.5214 | 2025-06-28 04:32:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c76b0b6-712b-3a3b-b7ae-37606d622b7a | -16.25321 | -53.68518 | 2025-06-28 04:32:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72cc5bf8-0417-36e8-a29b-24105bf01c39 | -16.07969 | -53.74517 | 2025-06-28 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bca329de-3fd9-30cf-9de0-2c39869acf37 | -21.60775 | -57.56482 | 2025-06-28 04:32:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86ba06a2-c131-3b5d-897c-356521927e65 | -20.3085 | -50.36662 | 2025-06-28 04:32:00 | NPP-375D | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 3b85a181-d465-3dda-aeb8-9509eb31a1c9 | -21.20227 | -48.51545 | 2025-06-28 04:32:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19d24bf2-d5c1-37f0-bfbe-2190d2acae92 | -18.59408 | -46.55159 | 2025-06-28 04:32:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a8f671a-25e3-3ed8-9c51-532216017150 | -17.66795 | -46.84289 | 2025-06-28 04:32:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a300189-d87d-3cc1-8a39-e12592add257 | -16.25449 | -53.67813 | 2025-06-28 04:32:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee567343-1598-3f86-9d33-dd7d91768da8 | -19.16132 | -49.13469 | 2025-06-28 04:32:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97ba042a-89c0-35db-a933-b4d4bb25f8ea | -19.02042 | -57.6246 | 2025-06-28 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6e2a12f7-2767-3ace-a63b-3ca08b0515e5 | -17.75312 | -52.43121 | 2025-06-28 04:32:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe34fc06-6fc4-360c-9633-c4b7996650e8 | -21.20565 | -48.51601 | 2025-06-28 04:32:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e186fc17-0fe4-3d55-a516-df4069ec7860 | -21.10767 | -45.71522 | 2025-06-28 04:32:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 6fb71d5d-e4a4-304c-9a29-2dc35d12db97 | -19.55102 | -46.43422 | 2025-06-28 04:32:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85f3aec3-22b1-300b-a57e-94c9d21de6e0 | -20.76545 | -46.76802 | 2025-06-28 04:32:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 99899dd5-ec07-3597-a1ab-ff6095df72a8 | -16.07902 | -53.7488 | 2025-06-28 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b691c958-3bad-3330-bd7e-dd1614335649 | -20.85573 | -45.53035 | 2025-06-28 04:32:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d38479dd-1099-32b0-8e9f-ab2f5e7ee7b3 | -20.41743 | -43.55303 | 2025-06-28 04:32:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 96c55346-4f0c-3200-96ee-d410c715e683 | -17.15366 | -54.01196 | 2025-06-28 04:32:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96298cf3-8e3b-3d03-bcc4-b57780e00de8 | -20.3079 | -50.37035 | 2025-06-28 04:32:00 | NPP-375D | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| bb28584f-0f75-3c68-abdc-00e8e70f2cfd | -18.0902 | -54.27601 | 2025-06-28 04:32:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43633909-3460-3854-b250-5b4225b911d9 | -20.31144 | -45.58446 | 2025-06-28 04:32:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4afe0904-4209-37e6-b079-5d47092f0d85 | -9.7228 | -56.183 | 2025-06-28 04:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 775b6422-6dc8-32e9-9ce2-d5556a228c97 | -4.5429 | -48.0151 | 2025-06-28 04:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| e2f52276-db25-3455-9d48-7e04214417b1 | -9.7041 | -56.1843 | 2025-06-28 04:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| d4010d6c-b1d0-3756-b713-311271e4e9d6 | -11.0455 | -55.3773 | 2025-06-28 04:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 0bd99d7e-b3ff-3b32-a818-f5f0c116a201 | -11.2664 | -52.7527 | 2025-06-28 04:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| b521b81f-752e-3baf-8dcc-541a2098df0d | 2.75098 | -60.36874 | 2025-06-28 04:46:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57fbab8d-a891-364f-8374-2b37d5101b98 | -6.90875 | -43.97634 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e89295c8-b4e7-3cd1-809f-7f2968e0dc5e | -6.60593 | -55.30616 | 2025-06-28 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 92f5e162-f501-34af-a9ba-e5b4bd19677a | -6.90601 | -43.99561 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| abae162b-c0e9-3d01-93bf-bb0c88a899f4 | -7.22014 | -43.08394 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| a0a05c5c-776b-36a3-9b50-21042fbf449e | -8.7366 | -47.85183 | 2025-06-28 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a175563-8b63-36c8-a93f-b493bc0e8cb6 | -7.21963 | -43.0877 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4f6aa5bf-d5d2-3dcf-bc92-30b554f0faf2 | -6.89877 | -43.97169 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f82f2e38-3371-3e5f-98e3-b8e543256450 | -7.20243 | -43.08907 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 29f7b89b-e6db-3ea6-8328-06c3c8623659 | -8.74073 | -47.85231 | 2025-06-28 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 526ce773-82ce-3cdc-9f8f-2b668903ffad | -6.89785 | -43.97818 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2071546c-5a3a-3a12-a8c1-b040626ad0d0 | -6.90399 | -43.97239 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7b9a9782-d5a6-3964-9917-1ed7622b3906 | -6.95603 | -42.91124 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b44ceaaf-f722-3a8e-9c88-562d590fca6d | -5.47191 | -48.69159 | 2025-06-28 04:49:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90483d9c-3173-3a4d-92b6-a2973e1a4a79 | -6.9459 | -42.8757 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 32265992-6246-3c18-a6ab-cf9cb0ca58d5 | -7.21562 | -43.0756 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 0a7f5ff5-9206-3f34-96f4-cb2e9b34c060 | -4.18642 | -48.13959 | 2025-06-28 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a948e343-00e5-385d-8920-58f6c017749a | -8.11871 | -49.99842 | 2025-06-28 04:49:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b83cd1bf-9c30-3db0-8304-9aee5562f4eb | -8.30948 | -46.30659 | 2025-06-28 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91e50560-9b3b-3493-b5f2-6039d4791e42 | -6.95043 | -42.8843 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 28671d43-230f-393c-a7a3-3a45f37e4493 | -7.38824 | -44.54929 | 2025-06-28 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 60d2dec9-0a29-373a-af32-60d189e42b0c | -5.46631 | -43.077 | 2025-06-28 04:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f0d53d2-340f-337f-a4a4-6fe6838ac96f | -7.20953 | -43.07859 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d0ce3bdd-187a-3024-8957-c23225df918c | -2.49778 | -54.13181 | 2025-06-28 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0cbc8845-4fad-3c3b-b9dc-5860ac7b1590 | -7.2252 | -43.08845 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4868ccf5-6fef-3115-8c0d-9eb5e0451ad2 | -5.45343 | -43.07864 | 2025-06-28 04:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ccc2cd6f-7cf1-303e-bef0-548ff75a9982 | -6.90738 | -43.98599 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ef4a0c85-6c81-3c9d-9805-d574f40b25e0 | -6.89739 | -43.98142 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 093162e0-ea3a-3dd0-97c4-6ee531539f42 | -6.68824 | -43.06913 | 2025-06-28 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f58aa69-8fcd-36f1-93ca-8d4c4b88f74b | -7.15197 | -43.3765 | 2025-06-28 04:49:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 41415bc4-8c36-3ac9-84b1-4dc5687a8fc7 | -7.0838 | -49.59621 | 2025-06-28 04:49:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ad9e726-508e-3bbf-82d8-c38df47d1f3b | -6.9146 | -43.97837 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e96d5f5-10ab-39eb-8a65-754e16807204 | -6.68774 | -43.07269 | 2025-06-28 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0541b5e1-ee85-39ec-9829-758bf1b83842 | -7.10634 | -52.5881 | 2025-06-28 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09c92d4b-5d6f-3573-9a2d-8228c05247f4 | -6.95795 | -42.91235 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9fad8d29-df20-3a07-aed3-4e9af6dd608c | -7.15149 | -43.38007 | 2025-06-28 04:49:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cdcb02a0-ed42-3589-bfaa-a2e2d6e1ebb8 | -7.10304 | -52.58758 | 2025-06-28 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c10e8282-04ef-3bb7-8d24-1004ad46f994 | -5.69237 | -50.05107 | 2025-06-28 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f8448267-8d3b-317a-ac45-368d545b3520 | -6.44594 | -44.57104 | 2025-06-28 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00910a43-4855-39fb-b02c-538081ae4aa1 | -2.44046 | -47.4829 | 2025-06-28 04:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3e8c258-ed38-3b27-bddc-8ef711364365 | -6.9083 | -43.97955 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 39b7dc92-28fb-3d1c-ae59-7c2a8cc20448 | -4.54432 | -48.02344 | 2025-06-28 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| ded11180-fb0f-3239-8665-ed073a09e91f | -6.9017 | -43.98853 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1b92ebb8-3fe3-34dd-9555-10b99f1bb093 | -7.2085 | -43.08611 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dcaf1fa8-1a1f-3dbd-98f4-fd47fa9a40a6 | -6.91306 | -43.98348 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 058214cc-460e-35a2-8618-929b542c549b | -7.21057 | -43.07101 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 4d94d342-6cc1-3f6a-bb97-430219269d51 | -4.5412 | -48.01812 | 2025-06-28 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 6fa05475-2643-325e-a2dd-955ff916cdda | -6.9126 | -43.98669 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2556252f-e0d3-3b22-a7d8-5302a9c9e147 | -6.95094 | -42.90651 | 2025-06-28 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 44c842fe-4658-3b59-a5ff-ee4c7a639974 | -6.71501 | -44.40243 | 2025-06-28 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 849d76fe-a19b-3188-baf1-8025653b6344 | -8.03911 | -47.64314 | 2025-06-28 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0546611-4cfd-3095-8e44-dbd852a2d909 | -8.85419 | -47.95359 | 2025-06-28 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d7d438e-0b2f-3254-a8ba-6471b3d61f2e | -6.90216 | -43.98531 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8e9dcc7a-8824-3861-8d53-b727f0fdf753 | -6.54951 | -54.98001 | 2025-06-28 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3a765c4-b36c-391c-903d-8afe9dd623ff | -6.91286 | -43.99125 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fab99c0-e479-359b-acb7-72698cc152a2 | -7.54501 | -45.82471 | 2025-06-28 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bfd9ec89-a8c1-35fb-b1bd-77e6e97bec2e | -5.44188 | -46.55822 | 2025-06-28 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca52c72f-0221-3b52-afb1-16939652d15c | -6.22765 | -44.52501 | 2025-06-28 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6bfab9b4-b08a-35d8-a7be-325f85b33f35 | -6.71458 | -44.40553 | 2025-06-28 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 663568fe-6120-3642-9ea0-ed9bbd89a963 | -5.45548 | -43.07517 | 2025-06-28 04:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d96acd6a-9645-30af-bce1-a5c76e982e21 | -4.12502 | -43.06841 | 2025-06-28 04:49:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3aa44404-6ca1-3e83-b04d-6560eee0b2e5 | -3.31418 | -48.71567 | 2025-06-28 04:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6a68311-9e59-3aef-9fe8-adcc78c09a93 | -6.89831 | -43.97493 | 2025-06-28 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bdea264-64f5-3da9-bd88-4903ea8da256 | -8.03857 | -47.64688 | 2025-06-28 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README21.md)
