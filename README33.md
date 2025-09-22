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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d80b52f-6e03-393b-95cb-1804e2a5b0be | -20.54239 | -56.15316 | 2025-09-22 04:42:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 17e847d7-0b1d-37d2-83ab-26e7c714f825 | -19.24985 | -46.54837 | 2025-09-22 04:42:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e657ac4-3ece-36e6-afbd-b371c3c97681 | -20.4336 | -43.67599 | 2025-09-22 04:42:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c3d5839a-adf1-33b3-9309-024b8b7a707a | -21.84431 | -53.96121 | 2025-09-22 04:42:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 4534536e-a244-37b0-ae8d-6197634fbc6c | -18.8789 | -43.24955 | 2025-09-22 04:42:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 428dfd21-292e-3770-b0c2-cefac4e3c0d7 | -22.94774 | -46.07919 | 2025-09-22 04:42:00 | NOAA-20 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6de9ed4b-6a38-36c9-a821-e8ec0a88a62f | -19.81781 | -46.39569 | 2025-09-22 04:42:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5af39963-ce29-3fa3-b512-4b4dbd256d6d | -19.98046 | -46.85836 | 2025-09-22 04:42:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76318fb2-2717-362d-9e28-596d1994e639 | -19.8474 | -57.3053 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c38711f8-4c8e-3b59-a84d-045d2daad274 | -20.12924 | -42.49368 | 2025-09-22 04:42:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 73fd7c82-29b7-3f74-935f-9c431d21e2e0 | -20.26979 | -55.49604 | 2025-09-22 04:42:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a040b199-6d69-3978-9b99-43290e1881b6 | -20.66575 | -54.48834 | 2025-09-22 04:42:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0aa79938-e8d7-34ed-bf21-01bd2e58581d | -19.84929 | -57.29494 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c28aa30b-59df-3e82-b840-7b146fbe37b6 | -19.63045 | -57.73642 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9017a857-8894-3be9-a2ef-17edeab8d550 | -21.84825 | -53.95807 | 2025-09-22 04:42:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 729f78fd-a2c7-3245-827c-f0973047fa9c | -20.54317 | -56.14874 | 2025-09-22 04:42:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27e4718c-4c6d-3245-9787-9c989d3fa23d | -19.85223 | -57.30093 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 82db61ae-803c-3b18-8b7b-f80bd9c361af | -19.30849 | -43.75689 | 2025-09-22 04:42:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7737adb0-5008-3a3d-a3d4-d1a8f90af8d1 | -20.6681 | -42.29033 | 2025-09-22 04:42:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d15faca5-69af-36c8-9d0c-60c506b370e2 | -20.86164 | -42.24187 | 2025-09-22 04:42:00 | NOAA-20 | VIEIRAS | MINAS GERAIS | Brasil | 3171402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f9ddf305-9730-306d-b387-2f93ecc73ee2 | -20.19131 | -44.62283 | 2025-09-22 04:42:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 98891897-9a46-31c8-89df-3d71ebe2ebbd | -20.67607 | -54.57375 | 2025-09-22 04:42:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 526be296-0c3f-31f7-9db2-c0feec93137a | -22.30048 | -46.69003 | 2025-09-22 04:42:00 | NOAA-20 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3ced0f1c-c4bd-3dad-9771-6bc094a5c5a4 | -19.85429 | -57.29205 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 2667682c-589c-3bb2-a97b-4f368e045e4c | -20.66975 | -54.56944 | 2025-09-22 04:42:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2a68e50e-4374-3d29-ab86-e75a3464e6f1 | -19.64174 | -57.74262 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| c664b158-b1f4-32b8-8c09-1a98b5900bc8 | -19.57443 | -41.65223 | 2025-09-22 04:42:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 631e49aa-0ecd-39fe-8290-0390bedde6db | -19.27423 | -43.74306 | 2025-09-22 04:42:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| adafa3a0-d800-3a36-a99a-df0e60d2e3fa | -20.57042 | -54.53428 | 2025-09-22 04:42:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2e8b3931-7136-33e6-ab8b-51e70873ed54 | -19.85411 | -57.29058 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 3554cc1b-50a4-313b-bfd6-ae40eea1d332 | -19.64048 | -57.72708 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cf0b9c37-f1f1-329e-9467-d9e8db44fe75 | -18.40888 | -46.86636 | 2025-09-22 04:42:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec893349-3aef-377d-827e-94ebc522d712 | -21.8328 | -53.9474 | 2025-09-22 04:42:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c2b62eaa-eec5-38ae-b287-a760fec19093 | -20.26107 | -44.42406 | 2025-09-22 04:42:00 | NOAA-20 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d8720316-3832-335c-8f3f-1f8bc53ad032 | -20.6102 | -46.07434 | 2025-09-22 04:42:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 465d3a7f-d342-389a-84a6-5a85cd91e82b | -19.97631 | -46.85785 | 2025-09-22 04:42:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97264780-a0d4-3754-a257-78571342d355 | -19.64574 | -57.74347 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| c9dd410c-2298-3e5f-8c20-5878c5beebbc | -21.14167 | -46.33728 | 2025-09-22 04:42:00 | NOAA-20 | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2cacedb7-182c-33de-a88a-9bc885e12053 | -20.19187 | -44.61788 | 2025-09-22 04:42:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fc921713-4133-3624-a29c-24f3ca3cfaa4 | -19.85611 | -57.30174 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 46a1da36-6ffb-30a6-96bf-ba4f017ba424 | -22.3048 | -46.69067 | 2025-09-22 04:42:00 | NOAA-20 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5d55c7a1-3c1d-38e7-ae5d-44a481c7704a | -19.8093 | -46.39444 | 2025-09-22 04:42:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f42459e7-b891-3283-8c74-c449c53f3a0c | -19.63775 | -57.74178 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 36122ac7-9569-35ab-a3fa-d5c1a2df48a9 | -20.26201 | -55.49884 | 2025-09-22 04:42:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 503d3550-eee0-3bb9-ad79-bccaeb2e8df7 | -22.30326 | -46.70361 | 2025-09-22 04:42:00 | NOAA-20 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0bd636c3-66ec-3425-9d26-b1f8f1e34bd5 | -18.40673 | -46.85104 | 2025-09-22 04:42:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b18e02d7-3931-35cf-8d93-64972f8a3dbd | -21.17182 | -54.63285 | 2025-09-22 04:42:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ef87c11-6b89-39fb-9723-15791cbda191 | -19.84247 | -57.28814 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 718cac14-a425-34ea-a06e-cd2e268b7d65 | -20.12889 | -42.49272 | 2025-09-22 04:42:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| db0116dd-fd69-347d-aa92-bc6e17c3b53a | -20.25619 | -44.42343 | 2025-09-22 04:42:00 | NOAA-20 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 13bb0a41-eafa-3cfd-912c-018e7bfe7f05 | -20.12543 | -42.47648 | 2025-09-22 04:42:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5dcf61ff-4a11-35b3-9b3f-46307b51f6d3 | -19.13952 | -42.66541 | 2025-09-22 04:42:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 09e53e44-ddaf-3b32-beae-9153c090fcfe | -21.64632 | -47.48783 | 2025-09-22 04:42:00 | NOAA-20 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3121d69-6b99-3ab6-b296-b1af59b31dd3 | -20.42542 | -55.07723 | 2025-09-22 04:42:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c5814b4-17a3-3387-beca-dba5815809a7 | -19.13991 | -42.66174 | 2025-09-22 04:42:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b6fc2864-fcca-395b-a1af-93fbbb550257 | -19.85517 | -57.30693 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 8a346c5e-4b7c-370c-bc0b-3271d9083ce4 | -20.86728 | -42.24274 | 2025-09-22 04:42:00 | NOAA-20 | VIEIRAS | MINAS GERAIS | Brasil | 3171402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b0f5f0c6-f91a-3756-85f1-39a57f49c274 | -19.8601 | -57.304 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 12226dcf-0b5b-3164-8508-645d19d7695e | -20.1296 | -42.49022 | 2025-09-22 04:42:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6c5cefaf-e266-3f9f-8b47-9d14d23898da | -19.84541 | -57.29413 | 2025-09-22 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 4aed5a7a-8a39-3233-8f9f-53eeb9cb72d8 | -19.83876 | -42.20979 | 2025-09-22 04:42:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7b498caf-46d4-3bdd-94a3-8ab4275ce3bc | -20.55324 | -56.1553 | 2025-09-22 04:42:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2186266-3c7f-34de-b632-6f000d4307e6 | -20.26554 | -55.49954 | 2025-09-22 04:42:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 9c0d89ff-449c-32a1-a20d-aef47dd1c6e2 | -20.6146 | -46.07494 | 2025-09-22 04:42:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f7bcdba-e222-31a8-8695-af45c5076661 | -21.8343 | -53.95933 | 2025-09-22 04:42:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f9195685-661a-3039-8526-6dfa1a8cc9f0 | -21.01747 | -45.80218 | 2025-09-22 04:42:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e20640bc-6592-306b-91e7-4c7a4f1224b5 | 4.18742 | -60.08116 | 2025-09-22 05:25:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b0a526e-4b98-3058-9993-92af6edc73b4 | 4.33242 | -60.76927 | 2025-09-22 05:25:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9fa4a6f-c609-3679-bc41-3919b65d6e38 | 4.33351 | -60.77633 | 2025-09-22 05:25:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69880fc4-d493-3e27-8655-9a3211da96d0 | 4.23329 | -60.10899 | 2025-09-22 05:25:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c2ffe48-90b0-330f-9408-046a1853e55d | 4.31089 | -60.49903 | 2025-09-22 05:25:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d73d10dd-17de-3784-8bd7-45de2ff18eba | 4.18796 | -60.08459 | 2025-09-22 05:25:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4929e38c-84fa-338d-91d8-f37ae7db9bce | 4.33481 | -60.71883 | 2025-09-22 05:25:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40a4aae4-c7c5-370b-97fa-66111822b942 | 4.23383 | -60.11241 | 2025-09-22 05:25:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7525ed6e-4cb9-30fe-a256-4f42392e3e73 | 4.32965 | -60.7733 | 2025-09-22 05:25:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d16450c6-9571-3d4b-b580-2872d6b6343b | 4.33535 | -60.72229 | 2025-09-22 05:25:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 392be797-3771-351b-9c9b-68d6fb234832 | 3.99116 | -59.65209 | 2025-09-22 05:25:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72e79bf5-3c03-3ee5-b74d-d92b390a448e | -3.48511 | -52.81199 | 2025-09-22 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d6aecec-9aed-3e1a-9523-13dacf36b248 | 1.83033 | -60.87278 | 2025-09-22 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d9e7c7f-f21a-36c1-b4bc-df5378686581 | -4.44376 | -55.39318 | 2025-09-22 05:27:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95eec360-affc-32dc-9feb-fb02f9ef8538 | -3.18935 | -58.98226 | 2025-09-22 05:27:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f86e640-8ad2-3b4a-a4f2-ca27f07fd171 | -4.58051 | -56.1855 | 2025-09-22 05:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00a0fce1-5ae4-358a-950c-58682219721f | -3.48558 | -52.80879 | 2025-09-22 05:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 559a4c47-d673-3687-9dec-87f115045618 | -3.59415 | -58.58529 | 2025-09-22 05:27:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7cdf377e-fbe6-3314-a14a-ec7cc72cdb58 | -4.57575 | -56.18878 | 2025-09-22 05:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c47369a9-0b40-31d5-b5bd-d0df2a9c323c | -5.39184 | -48.63488 | 2025-09-22 05:27:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 960cb552-8ca7-3c96-b23b-11aeb8fb5d09 | -3.76101 | -54.81333 | 2025-09-22 05:27:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba000c7f-01ce-3ded-94fe-2c02b2be9423 | -0.94935 | -47.35511 | 2025-09-22 05:27:00 | NOAA-21 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4a7ffc26-1be0-3599-8c14-e05061d32795 | -3.95314 | -53.39205 | 2025-09-22 05:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbae5495-9a7e-37cf-87e3-139811475174 | -3.59772 | -58.58583 | 2025-09-22 05:27:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bca2f406-a623-3574-b646-a05bf4ef32e7 | -3.06892 | -57.97758 | 2025-09-22 05:27:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d207bb7d-3df0-31f2-90e0-54d96c51c700 | -0.95242 | -47.35415 | 2025-09-22 05:27:00 | NOAA-21 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 93c5615e-c417-3064-837a-8c552a9e2c2a | -3.84531 | -55.60007 | 2025-09-22 05:27:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 91433f6e-14e1-3597-8e5d-37bc49f755ce | -3.65125 | -58.16196 | 2025-09-22 05:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9049c6b-13fb-3b88-97d7-195144e93eff | -3.39743 | -60.39138 | 2025-09-22 05:27:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d64d660-535a-3bbc-952c-11b9f98e1a76 | -3.95357 | -53.38911 | 2025-09-22 05:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d9f4723-d58b-3f23-a972-870aa299d578 | -4.07931 | -55.797 | 2025-09-22 05:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f23c2b78-2999-3bca-af59-2d67d6261ff7 | -3.89382 | -52.1799 | 2025-09-22 05:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b4fee23-71f5-3eec-8b0d-2eb3418b7d98 | 0.57335 | -60.17231 | 2025-09-22 05:27:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4b67ce9-62b0-3227-b5c1-575a46a037be | -4.47481 | -55.09721 | 2025-09-22 05:27:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README34.md)
