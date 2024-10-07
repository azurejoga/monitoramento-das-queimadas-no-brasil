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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 489cb9a1-c1a3-3ef5-8b89-f10dbbe88fdf | -21.39402 | -57.24732 | 2024-10-07 04:04:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 67dc279e-975e-304e-8ef1-2fd0723ea9dc | -17.72536 | -57.08734 | 2024-10-07 04:04:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 06aa94f6-fab0-334c-8185-4cd02aa37fd7 | -17.72209 | -57.0853 | 2024-10-07 04:04:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ca49b34f-b80f-30b7-8898-b7f8818c0210 | -17.71837 | -57.08544 | 2024-10-07 04:04:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| d5ce4119-ddc4-3b9a-b105-c78114281a26 | -17.71667 | -57.09268 | 2024-10-07 04:04:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c41e43e8-b6cd-30f7-beab-657b084dead7 | -17.71509 | -57.08341 | 2024-10-07 04:04:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| d15b2394-2148-34c1-8f4c-d8a7bd5c46ea | -18.70448 | -57.26546 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 84fc2b45-18ba-389d-9c74-f7e00c301178 | -18.72713 | -57.29438 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 22777026-5ed6-33ac-903c-83b931c815c8 | -18.72542 | -57.30153 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 44d73da8-96e2-3ab1-8ebc-556d265fc28e | -18.72453 | -57.29301 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5bbbed0a-bdd9-3575-a9aa-0b577e62b2d6 | -18.72371 | -57.30864 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 2198924a-ddef-3a88-b78f-8e79c96996c1 | -18.72278 | -57.30013 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.2 |
| f85c12c4-7d70-36f8-b2b4-662822565c4d | -18.72102 | -57.30724 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.2 |
| bbbee34e-8fe7-3dea-bfa2-9504dccdac7e | -18.7202 | -57.29242 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| bb9c9992-81cd-3d7d-975d-8d5668c09e33 | -18.71928 | -57.31433 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 7285be67-4601-3baf-89ad-f022808e155f | -18.71848 | -57.29957 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 08639989-8206-3190-90a7-321906b5d626 | -18.71677 | -57.30672 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.7 |
| d544457f-9f15-3295-835d-013c9175d415 | -18.71506 | -57.31385 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 206a7dd7-f691-383a-8293-775a2ea6bea1 | -18.71325 | -57.29052 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c58b2cec-ce2d-3050-a539-7f1931847fb1 | -18.71153 | -57.29768 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2bc2d1ad-7e1b-3bdc-8a17-d699084391f2 | -18.70278 | -57.27254 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ee9a61ef-eb0b-3582-99b4-07f231598262 | -18.69754 | -57.26358 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d4610180-7c43-30bd-8c2e-19603a000f73 | -18.69584 | -57.27065 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4d1278bc-d0eb-3b61-84bc-40d167fd66c9 | -18.69061 | -57.26165 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 19cf3bbc-b68f-3a56-8f2f-48745ce1ab27 | -18.6708 | -57.26265 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 2812277d-3bb4-398f-883f-74e1c142e16b | -18.6698 | -57.25596 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 28f21860-8ea4-3cb3-b599-23e53bf0e545 | -18.66808 | -57.26305 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1c5adfe9-08c1-369b-8391-dfbbfdaff0cc | -18.66387 | -57.2607 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| bdb8a38e-cc8f-3ccf-b544-864312980003 | -18.65862 | -57.25168 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 439a9537-f00b-3891-9259-1ff119eae381 | -18.65693 | -57.25879 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fc179420-2ea7-344b-a903-f740feceed0e | -18.65592 | -57.25219 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9b341987-e529-3cf7-9671-753446dadf8b | -18.65167 | -57.24979 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f6d34fe1-1147-3703-83a4-a8ad84111808 | -18.64999 | -57.25686 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4e3ad81c-c098-34b2-b5f0-012e9109366d | -18.64898 | -57.25032 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 78efe199-c1d7-32f1-af37-e2b6602c7472 | -18.64726 | -57.25737 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 3073129a-4ca4-3a6d-8233-4dd5b00bfeef | -18.64552 | -57.26447 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 01bc8022-3d8f-377b-bcc3-32e7d66bb1b6 | -18.64305 | -57.25495 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.8 |
| e46a2d5f-ddaf-3246-bc31-5e464a3bd423 | -18.64137 | -57.26204 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| ac81feeb-56fe-30b0-b562-71bcc7c7fa3f | -18.64032 | -57.25549 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| d5c20dce-999d-305b-85f4-55fe5fbe6c24 | -18.63859 | -57.26255 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 8c164d69-7d45-349f-965b-9fc1b503fecc | -18.63442 | -57.26013 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 9cd45623-2108-3d75-94ec-038524f1a2e2 | -18.63273 | -57.26721 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| d770ae01-ae0a-391c-9a17-d187fa1e1897 | -18.63164 | -57.26068 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8d2b2a6e-9e84-3d5c-a1e4-ae085ddfb1e1 | -18.63104 | -57.27432 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 12d56691-f3f5-3f56-a23a-e0f39d1a0b37 | -18.62991 | -57.26774 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 04e7e149-286c-3c32-920f-210605a06706 | -18.62817 | -57.27483 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 4c9e499d-8624-336b-9567-5c5c0b721e98 | -18.62579 | -57.2653 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| cdb7532c-e492-3653-9593-d03aa1444b71 | -18.62409 | -57.2724 | 2024-10-07 04:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| dcdb5a5e-10a5-3f7a-be9e-8dee9550c9ee | -20.87156 | -46.92749 | 2024-10-07 04:04:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 58248132-f7ba-37a8-ae02-fead4572632e | -20.65953 | -47.08491 | 2024-10-07 04:04:00 | NOAA-20 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22e8350e-5d91-3f50-859d-28ea0e998145 | -20.5149 | -48.12591 | 2024-10-07 04:04:00 | NOAA-20 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 30.4 |
| b81f2a0a-f56d-33fb-b9f3-5827fe00a5b0 | -20.51098 | -48.12513 | 2024-10-07 04:04:00 | NOAA-20 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 020c4c14-0fbb-3cbe-971f-8b3a82c33d81 | -20.50998 | -48.13041 | 2024-10-07 04:04:00 | NOAA-20 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 30.4 |
| ad71767e-8407-3367-a617-78b15ebaab9b | -20.509 | -48.13563 | 2024-10-07 04:04:00 | NOAA-20 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c04c2d58-7915-3aa3-92b3-1211e6afe2b0 | -20.50606 | -48.12965 | 2024-10-07 04:04:00 | NOAA-20 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 96491881-6cab-3bfa-84c9-91d468e75d55 | -20.50507 | -48.1349 | 2024-10-07 04:04:00 | NOAA-20 | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 6ded36eb-0dea-3f5c-8b98-2a5d7c454712 | -20.43649 | -47.71771 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 772f434b-8f29-3e2c-b238-aa9dee7333a1 | -19.81038 | -48.02638 | 2024-10-07 04:04:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 757b7e5c-0c71-3701-b3f8-5af4d50b8068 | -19.80645 | -48.02552 | 2024-10-07 04:04:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1316008-01ee-3226-991f-a4c142ac3948 | -19.80545 | -48.03089 | 2024-10-07 04:04:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37bfc9b3-5ab9-3c7d-b6e1-116ba2b3d8b5 | -20.44123 | -47.71349 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 87f25fc6-1c51-39f3-a343-be130b3ba0b3 | -20.43265 | -47.71699 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c35c5967-37ca-3d63-aaad-adc4384daeb7 | -20.03732 | -47.76143 | 2024-10-07 04:04:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0c92e9f-a5f4-3687-811d-c9e9791fd56e | -20.47422 | -47.66257 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 088851b7-e61a-33ea-8e14-fd7918df2908 | -20.4733 | -47.66769 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a2f15705-4452-374e-bc98-7a638cc2565f | -20.47239 | -47.6728 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a6118403-1170-31c4-88d3-a92fb4689377 | -20.47214 | -47.66463 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2507f647-4d12-390c-b548-d018451851f3 | -20.47119 | -47.66971 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3ed463ca-b6fd-38fa-bf25-8af8af8500f8 | -20.4704 | -47.6618 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 31af817c-ecc0-355d-9edf-4e4d339616b0 | -20.47024 | -47.6748 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 86ab6f65-627b-3499-ab38-22ff98a5e708 | -20.46949 | -47.66687 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7045539f-011e-340f-8c07-6eb9da80b12f | -20.46858 | -47.67195 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 5eb0ae23-e156-35ca-881d-49370d39788e | -20.46834 | -47.66378 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1d5a4f09-fa2d-391b-a220-d7525b961534 | -20.46766 | -47.67706 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 7eac1a6b-ee40-3d1d-ae86-16f6a2767e13 | -20.46752 | -47.65586 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 925cbcbd-c0db-3774-b2d8-a38945db0d94 | -20.46739 | -47.66883 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 87bdba65-ed77-372f-aff1-a47075ce4f27 | -20.4666 | -47.66091 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4457e5f4-67c6-3b67-b420-e30fa0b7dfef | -21.91125 | -42.26192 | 2024-10-07 04:04:00 | NOAA-20 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 048d2dfe-9346-3e30-b206-7765c83a2b6c | -21.71187 | -42.29422 | 2024-10-07 04:04:00 | NOAA-20 | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 22e55899-c5b9-370a-abd1-abc7f7ef02e8 | -21.70908 | -42.28986 | 2024-10-07 04:04:00 | NOAA-20 | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 04d56c82-b137-3aa2-a196-5ab9444fe5d9 | -21.70851 | -42.29369 | 2024-10-07 04:04:00 | NOAA-20 | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6fc5d33e-6ac1-3307-a9aa-0cfb00bdda14 | -21.70795 | -42.2975 | 2024-10-07 04:04:00 | NOAA-20 | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f530373c-9128-3c56-8214-428434994dea | -21.70572 | -42.28933 | 2024-10-07 04:04:00 | NOAA-20 | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f88d1afa-bc22-3492-9f02-345c181179bc | -21.70516 | -42.29316 | 2024-10-07 04:04:00 | NOAA-20 | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e8aca824-7043-3361-9bf7-60f62dd121fb | -21.70459 | -42.29696 | 2024-10-07 04:04:00 | NOAA-20 | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3a1a774c-b4bf-3f06-b386-cbdb11605a2c | -21.70181 | -42.29257 | 2024-10-07 04:04:00 | NOAA-20 | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c93975e0-c5a0-3ab3-8279-85571f2ffbc5 | -21.54281 | -42.20407 | 2024-10-07 04:04:00 | NOAA-20 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5259448d-6de5-38df-99d3-bb26c3b4e010 | -21.53946 | -42.20348 | 2024-10-07 04:04:00 | NOAA-20 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 415ba056-b5db-38ab-ab97-681fa59736f6 | -21.53611 | -42.20289 | 2024-10-07 04:04:00 | NOAA-20 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a0759ea3-f581-38f7-a269-84a996fde60f | -20.92975 | -42.60273 | 2024-10-07 04:04:00 | NOAA-20 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0186b056-8d64-3d7f-b05e-77c88e0ce85d | -20.87315 | -43.27484 | 2024-10-07 04:04:00 | NOAA-20 | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0c762923-3978-361b-b2c4-655c3ce02150 | -20.8671 | -43.26998 | 2024-10-07 04:04:00 | NOAA-20 | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 483f50f9-2844-3b98-a86a-a87673ebfe8b | -20.86379 | -43.26939 | 2024-10-07 04:04:00 | NOAA-20 | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 355d7660-afb2-32e1-99f7-e87728a06f2c | -20.69234 | -43.30004 | 2024-10-07 04:04:00 | NOAA-20 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0c421eb4-687b-3c66-853a-2317e2079cb3 | -20.6794 | -42.92805 | 2024-10-07 04:04:00 | NOAA-20 | VIÇOSA | MINAS GERAIS | Brasil | 3171303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6bd324c3-101b-39a7-8cab-8eafd1edd216 | -20.64138 | -42.91004 | 2024-10-07 04:04:00 | NOAA-20 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 29ec691e-a035-3730-907a-d42d0fb36dab | -20.64081 | -42.91372 | 2024-10-07 04:04:00 | NOAA-20 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ff5b8729-b9e9-3d5e-81f6-22e15dc5a2ef | -20.63807 | -42.90946 | 2024-10-07 04:04:00 | NOAA-20 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| dbd05974-1c2e-3281-aa06-07727cc89d26 | -20.63693 | -42.91682 | 2024-10-07 04:04:00 | NOAA-20 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a38e93af-4c4b-3465-b0ab-cf7e6d04b9b5 | -20.49496 | -42.29752 | 2024-10-07 04:04:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |


[Clique aqui para ver as próximas entradas](README73.md)
