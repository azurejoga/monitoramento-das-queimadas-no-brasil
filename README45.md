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
| dbb174d9-5a20-3bce-879f-54126a3ab0b7 | -11.1642 | -54.8923 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c61c3c9-b9c4-3ec2-9259-80acdeb636ee | -5.70674 | -44.21442 | 2025-10-08 04:17:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 467b1b9d-ac1e-3c5a-93dd-f3e2d3f8952b | -7.67588 | -42.57732 | 2025-10-08 04:17:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fc442db6-42ca-3a8e-be41-b7ddcf53a3ae | -11.80431 | -45.04354 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6f7762c-dfc9-3aa5-940f-468812c3ca63 | -7.28043 | -41.98277 | 2025-10-08 04:17:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 7bd37af3-737b-3f97-a559-2c36b176d05b | -12.02874 | -45.20798 | 2025-10-08 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5086631f-adec-39e9-ae85-9c8bd333978b | -3.46212 | -44.27171 | 2025-10-08 04:17:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec29aa84-27fa-3139-b4de-628ee048c213 | -9.54263 | -47.76538 | 2025-10-08 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6b2592f-299f-3528-9107-279b11278b73 | -12.71825 | -44.375 | 2025-10-08 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4e9e364-c5f9-348e-8f06-6605471833ee | -11.37693 | -54.34889 | 2025-10-08 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55aed804-abc0-3ac4-ac5e-26f7a9067a3a | -4.20565 | -44.66912 | 2025-10-08 04:17:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7cd865e-d3fa-3171-997d-ae6d5ba322d2 | -4.94824 | -45.59207 | 2025-10-08 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 057cb92d-9f38-3e75-b205-08f6e95b95dc | -5.42155 | -43.18763 | 2025-10-08 04:17:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e1380f9-6e8c-3311-89bb-6d9e362b78a9 | -5.59369 | -45.84266 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84555983-81e5-37f6-9eba-163b3674bb9a | -11.34024 | -56.20867 | 2025-10-08 04:17:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62c81143-2f34-3dab-8f3d-8308206bb932 | -11.78441 | -45.14626 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5bfa0f51-6a29-3dbd-beb3-0672f91a9386 | -6.99956 | -42.89183 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8a8c4604-7f4e-3393-afcc-38a255f475c0 | -11.14188 | -54.88997 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7a05eeb-06fc-3695-9081-1d4c64448e92 | -11.15168 | -54.87054 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb8e430f-a0d3-39a8-8bce-6e3f2f604003 | -12.23718 | -43.78136 | 2025-10-08 04:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 024d217f-d9fb-33f6-a52b-188697309430 | -3.82277 | -44.00321 | 2025-10-08 04:17:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c72fd587-48c2-33f0-9cc5-6756d73138eb | -11.34131 | -56.20346 | 2025-10-08 04:17:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c99d9260-cff7-39d2-88fe-c216fe68dd13 | -3.1122 | -47.79884 | 2025-10-08 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e5c9bd91-b42c-3893-872c-7b527754631f | -3.82912 | -50.97042 | 2025-10-08 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ea941a93-ff2e-3f22-888f-6d7f628b6da8 | -12.37567 | -50.30384 | 2025-10-08 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c580372-5b7c-36de-ba6d-0653c6cb6b00 | -12.93365 | -46.86204 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b2ef6024-87a5-3573-acfb-6f6976292f1c | -11.1709 | -54.89603 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a26d90ac-a036-3d72-85ce-c5944d69dc55 | -6.32009 | -41.60712 | 2025-10-08 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5794d20d-85a0-37e5-b419-b335a9017dbc | -11.73615 | -50.93811 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 754b83fa-0a20-3ad7-9755-9aea4107f156 | -11.30097 | -48.26979 | 2025-10-08 04:17:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcf3aecc-c063-3bca-aa5b-d859a248e125 | -11.17074 | -54.86546 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 904b1b88-f4b3-38b4-a0b8-e417f8f8043f | -5.31162 | -44.99818 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b10b8616-0830-3994-92cd-dc0f1d044092 | -14.00416 | -43.081 | 2025-10-08 04:17:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 98d78e86-ab56-30a8-8178-dcf17dc54102 | -5.73781 | -45.26348 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0666914-a117-364e-854f-6da9fa31d368 | -5.77194 | -45.74107 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72d2e139-d555-357e-a790-4c27f3d3ec4c | -11.90587 | -46.74892 | 2025-10-08 04:17:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e1cebee-6ad4-3c23-a59d-9bc5c1ceb2d4 | -9.7863 | -47.72079 | 2025-10-08 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 157f3ded-e6b8-3f70-9b2d-8602ee4fe6b4 | -5.68436 | -46.38117 | 2025-10-08 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a3236df-c625-3376-8ab0-314acb7cb612 | -6.00412 | -43.75417 | 2025-10-08 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9dd1e22-3591-394a-930b-8702578fb890 | -11.15988 | -54.85927 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04c31d82-661b-3c1a-8085-4b2edf4b2a1f | -11.68371 | -50.96183 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4136d44f-bcc5-3050-97d7-453a6127dee0 | -3.11778 | -48.78495 | 2025-10-08 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45181e4e-e247-3ffc-8ec8-0c39ec48e461 | -11.95929 | -51.46636 | 2025-10-08 04:17:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25d83a67-e445-3ae8-8e4f-c9bc350a2bc9 | -12.3682 | -46.49199 | 2025-10-08 04:17:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88dce2b0-9096-3708-8852-b701df4cfb45 | -11.15055 | -47.74635 | 2025-10-08 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4fe9af4f-0bf0-3865-b5d5-670f7e78a56c | -11.78982 | -45.04841 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a40e86a6-ff60-3283-8b42-c702e725e3c3 | -11.16255 | -54.87672 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 33eef66c-7977-3c69-96ae-62838053616c | -5.02534 | -43.66064 | 2025-10-08 04:17:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df5d7d3a-f9ca-387f-9754-eb92550f7811 | -5.13953 | -44.96463 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 901c8c0c-0110-3ddc-91a0-6bc7eb2a789f | -5.16504 | -46.22444 | 2025-10-08 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 732a4c33-4d89-3443-8c60-c5edfd2398a9 | -11.18081 | -54.86951 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75528836-e2ca-389f-b2e6-26ed22d8fcb2 | -7.47624 | -43.07058 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 10a542c7-2448-3062-9643-0d37502aab16 | -4.37551 | -45.78445 | 2025-10-08 04:17:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25745fb6-e7bf-31f3-81c5-018e62be6fbf | -4.69099 | -46.4726 | 2025-10-08 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 374e1137-5b11-38e1-9db3-bfcd2a956d6f | -6.99897 | -42.87386 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 6d6be850-218d-371f-8fe4-af9e9b35ca39 | -5.16434 | -46.22868 | 2025-10-08 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5a45e88-1ae5-3d53-b633-b989bb6f2370 | -13.42591 | -43.49421 | 2025-10-08 04:17:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1bfecee-ab57-3228-8451-1fd638f7a05f | -6.28174 | -45.31959 | 2025-10-08 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09ebfe8c-396e-3d81-a35e-c51e1605f654 | -7.44918 | -43.13416 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 30644edd-e411-313c-90cc-7cdc8764bf6e | -10.42976 | -45.38124 | 2025-10-08 04:17:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fc8ccef-d9c8-3480-a224-5fac58efa78e | -12.78126 | -50.50407 | 2025-10-08 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7522062-04b6-38ae-9bd3-7eb6b6a48fb1 | -10.46917 | -49.38941 | 2025-10-08 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00118f5e-b4eb-333e-931b-96ea3de76993 | -7.52787 | -42.72028 | 2025-10-08 04:17:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c5a57e03-8d2d-3e38-8690-ab3f0880631d | -3.11234 | -48.78228 | 2025-10-08 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57240c99-c673-3e58-be2c-9f61ba58b1bc | -4.68976 | -45.84885 | 2025-10-08 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3182c3c7-2c06-3b1b-89c2-690f429fc805 | -1.40752 | -46.70211 | 2025-10-08 04:17:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d44bac77-c6b7-3b1e-b4a7-26c523cdb87d | -3.08491 | -50.58251 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 626c1ecd-2d85-3fe0-9c40-347b74a4fb9c | 0.93056 | -51.12418 | 2025-10-08 04:17:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b533470-8507-3820-9b87-99760ef8df09 | -9.79445 | -47.74074 | 2025-10-08 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0ae16695-87c7-30f8-bc50-14df05bb695f | -4.05372 | -47.50037 | 2025-10-08 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 233b84a5-e89f-38c5-b9b5-702e2bd6efaf | -11.44849 | -50.2098 | 2025-10-08 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54eb141e-e9bf-398a-a174-db6b31b220b6 | -3.44776 | -45.59255 | 2025-10-08 04:17:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e94153c6-cc51-3083-8a77-c927d3d8497d | -11.11206 | -54.04466 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7efe66d7-2ee8-366e-af6a-968fc2535a93 | -9.45334 | -56.65559 | 2025-10-08 04:17:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f815fd7-0e80-3d3a-99a4-3d6af9c909a9 | -11.99798 | -47.19056 | 2025-10-08 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad03c6f8-fc9c-3b0b-a704-2ee1b84a74b7 | -7.72399 | -42.41013 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c1c08a9c-fa57-3e0d-b84e-e6f35a4ec0bf | -3.13611 | -40.99198 | 2025-10-08 04:17:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4d536b14-8299-3406-81eb-1e05e993388b | -6.7823 | -44.97219 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 313b5a80-9178-3576-99e0-bfa932ba9977 | -10.23337 | -52.69554 | 2025-10-08 04:17:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1291a412-988b-3ef5-8331-74880ef9a71e | -13.82115 | -41.29135 | 2025-10-08 04:17:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ea8987fc-90f0-30b1-987d-23909e6b5671 | -11.73534 | -50.94255 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a8f6bed4-4e1e-3908-9270-b406c22cf28d | -7.44475 | -43.14059 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2924a15c-dcaa-3250-89e9-757474e6a10b | -12.23836 | -47.87411 | 2025-10-08 04:17:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 500b8f5d-579c-3f10-b53a-baed5cab35d5 | -10.75036 | -47.87343 | 2025-10-08 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46c0c19a-d0a5-30ee-9ee5-483978d5a760 | -12.24201 | -47.87484 | 2025-10-08 04:17:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b984f2e-eba2-3235-9e4e-abcb1ba1ed59 | -5.74669 | -46.04965 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a30a4439-86c1-3377-945f-f96692a9a442 | -4.85318 | -45.66766 | 2025-10-08 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b1e4f48-4a84-37f0-aa79-8075ffff2b93 | -5.31858 | -43.08909 | 2025-10-08 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7feb585d-1d8b-3e23-a89e-b8a8ecba8d61 | -7.67198 | -42.58032 | 2025-10-08 04:17:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9cd16e84-832a-312e-b495-a44079de0e9a | -5.36213 | -44.44463 | 2025-10-08 04:17:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d6e0e4de-e66d-3a9e-ac9b-d90a1d9ce0b5 | -7.73921 | -42.75298 | 2025-10-08 04:17:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 72730717-c0f5-344d-8891-a2df03163129 | -12.933 | -46.86592 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ee6a0d1d-e431-3f22-a160-8ca308302c4d | -11.37881 | -54.35665 | 2025-10-08 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb61cbf4-fc1e-3bce-8eef-f2c08f25622f | -6.25705 | -45.04501 | 2025-10-08 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7fc78551-8466-347b-b049-b49c7876637a | -12.25427 | -47.86322 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ff875062-8f25-356b-af21-95adafb0574b | -5.25614 | -44.14407 | 2025-10-08 04:17:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61b12e8c-72d8-326a-8ccf-037d508b4f33 | -13.28905 | -47.15846 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb736b2b-f485-36ba-8307-ae4fdb6309fd | -5.13606 | -44.9641 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a8fc007c-3db2-3653-918b-b9c929b52e3a | -7.47854 | -43.12095 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6e517fc5-066e-3cb2-892d-ec940dbb4712 | -2.89261 | -50.73063 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README46.md)
