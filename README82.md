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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6c8d3e2-3001-3266-b82d-dc51f86f7602 | -9.18756 | -59.61435 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 77656463-41b1-36e2-bf8a-4f978a95106f | -9.20073 | -60.79831 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46f2db6f-2b7b-3334-8c58-94379c6b0074 | -8.21232 | -69.86214 | 2025-08-24 05:25:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3d55b64-2981-3e8e-acbe-f91634de2959 | -8.13727 | -62.87165 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15ad548b-9de9-31bc-9aba-89e0ef8f8a7c | -23.10723 | -49.97598 | 2025-08-24 05:25:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 95980a6f-5aa2-338e-ad3e-fa8e09741f7e | -11.18663 | -55.02609 | 2025-08-24 05:25:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a76c8282-810f-3fed-a75b-268a1389d402 | -9.19031 | -59.46008 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9164920d-675d-3b2e-9fcb-020b6272b189 | -8.67697 | -62.87471 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f0ab21a-c696-3d7a-8b46-adeffa0d94ab | -9.00377 | -65.71326 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1879d7d2-9cbe-3a0d-ab09-6edc21102a23 | -9.16192 | -59.46326 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2dac8f4b-2923-35cf-a89f-f3be178f66ff | -9.25796 | -59.63604 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9ebee65-5d87-3e28-89c9-19a5b720edb5 | -9.0034 | -65.7107 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f88d6766-4dd0-30ce-a1eb-431b00c24411 | -9.17798 | -59.65409 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3022e717-d533-3b5a-96bc-61b069dde3e2 | -8.60856 | -62.64541 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58d6140e-d39f-3171-bfde-baad6e79afd5 | -9.52417 | -60.55109 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20e980af-6f44-351a-8885-8cc3e389c318 | -8.90447 | -62.44816 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e83ca72-e823-3b2f-a2a8-09f2de8e1586 | -8.91176 | -62.44567 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b7ed522-3713-3205-bb40-471e96585587 | -9.64049 | -63.33527 | 2025-08-24 05:25:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b938f9f-604d-32b4-8378-da226a45db3e | -9.16084 | -59.49337 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 883fdb93-1d11-3205-bbfe-518273499cbe | -9.50914 | -60.51992 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49fe7fe4-9624-3a0b-a4b7-884ce14d5b87 | -9.00245 | -65.69775 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 377d1d3f-97f3-37a6-a80b-d851708ec586 | -15.316 | -56.15411 | 2025-08-24 05:25:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f04b584-b02f-3eaa-8924-496fb98fe017 | -9.19547 | -59.65314 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 596de7bc-6b17-36ee-aa03-96df1b897749 | -11.53337 | -51.84748 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 46246103-e9d8-3cb1-a87f-74850d44b413 | -9.93152 | -60.48816 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5b55df9-43a5-3b94-8ad9-1c5edf9473e9 | -11.52262 | -50.49609 | 2025-08-24 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 456e05ac-45ee-3375-95cc-7ad9efcebdd0 | -8.8858 | -62.40142 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c71e9406-2ee3-34de-86d2-7054c29e6fbf | -9.16143 | -59.51238 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9abce4ad-3c49-3ee9-b15a-330345a6284d | -11.53245 | -51.85497 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 66f29a00-43f7-300d-9555-d1d7098a12bd | -9.85841 | -65.26048 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5efb197-0cbe-3290-bdd3-49dcb4261446 | -9.94385 | -60.16447 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50860acf-ab5f-396b-b068-e561904023da | -9.02489 | -65.7067 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7f304b3c-ae57-3512-bc19-0a2da38bf126 | -9.00549 | -65.70329 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 26883314-8786-30bf-a192-0a626c086748 | -8.60576 | -62.64123 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35428e6f-402c-3658-aa17-46a3b390c1dc | -9.04954 | -65.72621 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5953e71-6ad0-3984-b63b-2b16182abac3 | -11.52424 | -50.48199 | 2025-08-24 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 662aa01e-9952-317e-b913-dd7ed0b09582 | -9.00463 | -65.70827 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f9ed55a3-57bf-322a-b483-6b09519ae670 | -9.18416 | -59.59127 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffde1993-8053-30be-ab4b-777ca2d4b565 | -9.1602 | -59.45161 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1749a779-f682-3172-8da6-5bd4cee703da | -9.13868 | -60.73869 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c055f4b-7b8f-39fc-9044-8cb59188f8b2 | -9.10158 | -61.42877 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2caa7ef9-4f3a-35fa-863b-8ad85411b2f6 | -9.18982 | -59.62221 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c817ef6d-de26-3157-9cc3-836f58dc8c80 | -11.54786 | -51.91358 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9fa4214-af5f-3c49-8e0b-9ae1c59f2c9f | -9.17534 | -60.80861 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14c28d58-d359-3970-8728-60ac3c2bf137 | -15.29665 | -56.16477 | 2025-08-24 05:25:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 234ad7fc-8000-3fab-a850-0f5b91caecc6 | -9.2522 | -60.92454 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 248d3011-6808-31b4-9939-cebe3c017777 | -9.19315 | -59.4643 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b8d1f7e-c395-3288-a20b-f8b04edeab3d | -9.16705 | -59.47542 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fde24e12-6d17-3789-9e68-582622ada3d1 | -8.90633 | -62.41533 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8599fab4-a4a7-376e-b6c9-971550932cf2 | -7.93778 | -63.06264 | 2025-08-24 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df3b6860-0a79-3cee-9964-39ef3d281291 | -9.17741 | -59.65778 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 842b36f1-23d1-3f67-b37f-708afcc3bfc3 | -10.34696 | -58.59811 | 2025-08-24 05:25:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a042c22c-6322-3ceb-97ff-6965c194ade8 | -8.96231 | -60.49885 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e464beb5-efc2-3f7d-a6fe-d74e03a8eaa8 | -9.20849 | -59.47801 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ebfd1df0-7e53-3a3e-9b9a-c2cf95f58f89 | -10.34635 | -58.60218 | 2025-08-24 05:25:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d4cdedf-8080-3aaa-8628-7fa7495e4b2d | -7.73063 | -67.06528 | 2025-08-24 05:25:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be83a670-7a3c-3e21-9623-6fc58c2a4939 | -8.89395 | -62.42803 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68ce1544-12c2-3952-89ed-76523ced8426 | -9.51643 | -60.55709 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c6e8fb1-7dfd-330f-9904-cfe5f4310ad0 | -8.70418 | -62.87919 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36ce07cd-f55c-30b3-b7bf-8de7bbe66ffd | -9.19321 | -59.62274 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f060b8a-591d-3e99-96e5-f15070096506 | -9.00505 | -65.70074 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b150a9a7-0fee-33c0-ae9c-ccf10a908783 | -9.15339 | -59.45055 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1fe32ae7-f3df-36f6-92e9-03f9e903324b | -9.01578 | -65.68997 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 761d788c-ffd0-3161-a140-4d5b579ce3df | -9.0218 | -65.38626 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb1181b6-a411-352b-83ef-a4b90dd636e0 | -8.89672 | -62.43216 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0934a5f-e037-330b-81db-fb3a1e4b931d | -9.37357 | -63.44765 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07ad700b-42c7-3ca4-9155-f1859748d70d | -9.16252 | -59.48229 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 75c2864e-3211-34fe-8602-0cd845803d7c | -11.73499 | -51.70372 | 2025-08-24 05:25:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b9678b0-dab3-3b0b-a51f-432c569e2baf | -9.21243 | -59.6107 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac15642a-4d6a-3507-9077-4b823d9b26f8 | -15.29281 | -56.15979 | 2025-08-24 05:25:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9dc975c2-6a3b-3840-a940-57d4135d5a09 | -9.20069 | -60.77681 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db14aabe-201a-3a90-b686-105e227d98c0 | -9.2292 | -61.02805 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61ca6d18-7c22-3eb2-86b4-83ef08cdbdce | -10.4798 | -61.32468 | 2025-08-24 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c55463c-d648-31a0-a941-e0d0c87f0988 | -9.50636 | -60.51587 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e964d089-46b1-3dc1-862b-7f7b1b2074cc | -8.89556 | -62.43934 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42ec5b65-382d-3e1c-bc46-2eb9bac7f1ac | -9.23238 | -60.92139 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7f73be8-ede3-3ac2-8460-3e1617030fd8 | -9.23564 | -60.92191 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ebbd0349-d154-35e4-9c66-a87af90dc1c9 | -9.02724 | -59.01255 | 2025-08-24 05:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e0e4608-bb26-3bf4-93c4-bf61e2ca28f4 | -9.16087 | -59.51606 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d36f6d3-6ba9-37ca-8efa-4dd59ce998a4 | -9.51024 | -60.51287 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad42709a-bd97-3eab-b69b-a98a0e0bcf2b | -7.97158 | -63.07207 | 2025-08-24 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9005461-1dcb-33e2-9adf-74bea21e8c52 | -8.61057 | -62.58977 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| da64a2a8-6867-324c-a635-e4ee7230b15b | -7.97035 | -63.07963 | 2025-08-24 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0654859-7c5d-3bfa-9374-00fa562660b3 | -9.18974 | -59.46378 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c1d442b-50d0-3d77-89f8-990c88600e4e | -9.19738 | -60.77627 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03c5912f-7fce-3ab8-8263-3305c289a124 | -9.15119 | -59.48808 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8fe8b39e-404e-3ffd-b0cc-c87030cef78e | -8.13787 | -62.86793 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8737a76b-fad6-34b0-8ab6-b05889261d19 | -11.17766 | -55.02481 | 2025-08-24 05:25:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 31147a74-2719-3afb-8fb6-799053339deb | -8.60882 | -62.60067 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d2cffac-0be7-3430-bebc-bcb47d9852c4 | -8.86395 | -62.40889 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 321e05a0-9b18-3a8b-af19-e82daa516706 | -9.16663 | -59.59229 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb2709c7-6e6d-374f-8d17-2948998d8fe3 | -8.92022 | -62.43597 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40d85f61-5928-3302-90a6-a24547b9bd72 | -9.00665 | -63.63428 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0ba1c0c2-1e71-38de-8d95-7ef28e5443c2 | -8.89337 | -62.43162 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19083269-41ea-3683-8b9b-dc50bd7d854f | -9.94321 | -60.50089 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11a43435-13a3-3928-8875-e40507271fe5 | -9.17202 | -60.80809 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac6e7c6c-0ae9-329c-913d-f72e6e810386 | -8.13846 | -62.86422 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6112c3e-70a8-3ad9-8824-49c08a9dd6a8 | -11.31148 | -47.85082 | 2025-08-24 05:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 23a5d5b3-d63e-3e59-b521-dbfd1c120d1e | -11.31073 | -47.85769 | 2025-08-24 05:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 185f1321-5b0b-3c07-babc-17445a3c5c62 | -7.94589 | -63.05621 | 2025-08-24 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README83.md)
