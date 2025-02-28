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
| c9158649-fa6a-3ab1-9da2-17b664b6e342 | -19.2739 | -47.32845 | 2025-02-28 04:55:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0134ee76-0485-3459-baca-fa78cbe4cb51 | -19.37779 | -46.04393 | 2025-02-28 04:55:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2ac9a56-d6db-3c2e-9d13-97a49ccb0240 | -23.2051 | -50.81091 | 2025-02-28 04:55:00 | NOAA-21 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f6369154-b675-3b49-87a4-fb3bd0aa7110 | -21.04995 | -47.78145 | 2025-02-28 04:55:00 | NOAA-21 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a8830f8-ab21-3535-a157-c69ac878e879 | -21.61686 | -48.46555 | 2025-02-28 04:55:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 866287de-0596-3674-9c52-2c8ddc72485b | -21.16394 | -48.56476 | 2025-02-28 04:55:00 | NOAA-21 | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5eb3799f-02b5-3457-9439-bfc8619affb4 | -21.61629 | -48.47076 | 2025-02-28 04:55:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4eb61757-b762-3af7-93de-738f20c39e08 | -22.54111 | -48.81435 | 2025-02-28 04:55:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 773b6a51-033d-34ec-b3b4-e85268701efb | -14.86371 | -46.8214 | 2025-02-28 04:55:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 436bdf80-ff50-3c03-ba66-558732339fb3 | -21.61509 | -48.46269 | 2025-02-28 05:08:00 | AQUA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 6113c403-5e75-34a4-bce6-e1db4aca55b7 | 2.79003 | -60.79519 | 2025-02-28 05:14:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bff4ebd1-b6bd-3d54-beef-6ad63b5b2b7d | 2.80675 | -60.82722 | 2025-02-28 05:14:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1aa85e5e-46cb-379b-8579-5b5c9159613b | 2.81087 | -60.80338 | 2025-02-28 05:14:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcc9b8c9-dc71-3b79-be90-df2434ec9a34 | 3.21137 | -60.34651 | 2025-02-28 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a24477eb-76fd-3d28-a79f-5f78b4094e44 | 3.21082 | -60.24511 | 2025-02-28 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0b29dca-be52-3db5-84a8-7d25c8db2451 | 2.81883 | -60.11961 | 2025-02-28 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f2b005d2-539f-32eb-af31-eb9a61196cc7 | 3.78665 | -60.04025 | 2025-02-28 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb58ce7c-5ef8-3dc4-9b1d-105f34d9a546 | 3.20938 | -60.33352 | 2025-02-28 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da2ecdf2-ae13-3b68-8608-c9d174a57442 | 3.21016 | -60.2408 | 2025-02-28 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef9f2858-8271-3125-a00a-aa0581abd44b | 3.84395 | -60.5257 | 2025-02-28 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb5a51cf-ac71-316e-9369-5d71e2f2bbd9 | 2.80701 | -60.82967 | 2025-02-28 05:14:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55d485b6-70ee-37e8-b1fc-f2169439eeb3 | 3.21383 | -60.24023 | 2025-02-28 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32ba54ef-14f7-3ef0-b10c-d4ff535b2367 | 0.74591 | -59.78527 | 2025-02-28 05:16:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe5af678-b8a5-346c-a589-b9028e7a787c | 2.10993 | -61.82123 | 2025-02-28 05:16:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0df4d967-29c5-3426-b67d-9d36f49a17c6 | 2.25502 | -60.28292 | 2025-02-28 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48d6081f-2b70-3060-9588-f00f9cdc2bad | 0.82895 | -59.94721 | 2025-02-28 05:16:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2e733d2-7629-3c4e-9ca4-239e8699957c | 2.29668 | -61.04904 | 2025-02-28 05:16:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17400f2f-4b22-3f14-8a78-60fdb10564ad | 2.51024 | -60.98355 | 2025-02-28 05:16:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0a15ba92-8b40-36f1-b292-458f3774a903 | 2.43975 | -60.65176 | 2025-02-28 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fc185e2-d7d6-3b38-9f45-32e3189c57a5 | -1.56324 | -54.36588 | 2025-02-28 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb8a2817-3b80-3d65-91a9-a18151550e48 | 1.53783 | -60.24562 | 2025-02-28 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a8a3986-9645-3b04-8227-9de61d3c58d1 | 1.31225 | -60.06731 | 2025-02-28 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fcbe6bc-65e8-330d-bf44-bd937099aee0 | 1.14106 | -60.4292 | 2025-02-28 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 195480a5-c113-3a9e-961b-2db274104ba5 | 0.83247 | -59.94667 | 2025-02-28 05:16:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0423b79b-a2be-3d26-af6f-0585d9b56c95 | 0.73485 | -60.47849 | 2025-02-28 05:16:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdff0929-0511-3b76-8262-bd28b706ac49 | 0.81182 | -59.76818 | 2025-02-28 05:16:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8e079bf-150a-3151-b9d3-342e5dfb3c82 | 2.10916 | -61.81614 | 2025-02-28 05:16:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d27a4d5-a097-344d-8e52-9ac61f6f81aa | -1.56393 | -54.36155 | 2025-02-28 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7672c21-c63a-3733-a97c-abf37ef81df3 | -3.02217 | -54.59033 | 2025-02-28 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9251527d-1c3d-372f-9150-e5794e9d096c | -3.1175 | -59.92916 | 2025-02-28 05:16:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9f14709-abd9-362c-a7d4-49c3002242f9 | -1.56583 | -54.35973 | 2025-02-28 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8f264de-aca8-3699-af57-685817b7d197 | 2.51073 | -60.98093 | 2025-02-28 05:16:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5bf90629-13de-326a-ba82-9f1c8890e1cd | 1.28291 | -60.10354 | 2025-02-28 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2947add-06d5-320e-be71-17be12724ea8 | -1.56516 | -54.36411 | 2025-02-28 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa2eb8ad-d628-3170-979c-e953c769babd | 0.8324 | -59.94787 | 2025-02-28 05:16:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7468b146-eed3-33cd-bd42-1702d568d589 | 1.08613 | -60.65111 | 2025-02-28 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8f7ecb9-60dd-3b1e-a408-137252b17357 | 2.29799 | -61.05104 | 2025-02-28 05:16:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bcf2cef1-e86d-343d-91ac-15fb7fd165ee | 1.19712 | -60.06763 | 2025-02-28 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 862d9430-0be0-3c7d-8f47-d758585238aa | 1.2749 | -60.07603 | 2025-02-28 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 236c5b93-79be-3ad3-a5b6-458ae6d5e86e | 2.29739 | -61.05378 | 2025-02-28 05:16:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 796cc01d-91b5-3289-8dc0-0a967ef5aa1a | 1.31287 | -60.07132 | 2025-02-28 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3b2e75f-1e7b-3453-ab4b-104ff2ed8517 | -21.6166 | -48.46498 | 2025-02-28 05:22:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8e412e14-c5d9-334c-a961-50d3f57ac744 | -21.61411 | -48.46284 | 2025-02-28 05:22:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 41cf8c79-5c95-3747-b948-cc8088e2c475 | 3.21142 | -60.24262 | 2025-02-28 05:37:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa043afb-7785-32a9-88cf-847ba4ac2c9f | 3.21146 | -60.3329 | 2025-02-28 05:37:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b68479c7-88af-3dcd-ba20-4056bdda4dbd | 1.20108 | -60.06979 | 2025-02-28 05:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5abe3074-0d59-3f57-b791-b10ae88d955a | 2.10939 | -61.82293 | 2025-02-28 05:37:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 216acbab-41ef-3ca1-8560-865d11c677fd | -1.56466 | -54.36244 | 2025-02-28 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c185576-4e00-3c1d-8e82-10ddf818f7b6 | 4.35458 | -60.69671 | 2025-02-28 05:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ff50fbf-eb59-3cbc-b514-814e43c76135 | 2.77668 | -60.72008 | 2025-02-28 05:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4538436a-b967-326c-8584-90de0e1ba5d2 | 1.31299 | -60.06729 | 2025-02-28 05:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd8f485a-f7b7-385d-84f6-3d1d8716b589 | 2.81109 | -60.80185 | 2025-02-28 05:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5b05cf5-d901-3cd6-a2db-0c23e7636220 | 2.79246 | -60.79689 | 2025-02-28 05:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46db0499-5318-3744-9547-c71949569f8e | 2.10601 | -61.82344 | 2025-02-28 05:37:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a206bcb4-3dd6-3260-955b-69664c66befe | 3.00832 | -61.14091 | 2025-02-28 05:37:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f5c41603-251d-3830-8c9c-ae45b939dbe4 | 2.29658 | -61.0519 | 2025-02-28 05:37:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6752d270-bb73-364a-891a-4c987ac1d0e4 | 2.8117 | -60.8057 | 2025-02-28 05:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56db3ac5-90f5-3bae-89c9-a251cc18b89a | 2.80491 | -60.83039 | 2025-02-28 05:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27e20120-ecf0-3fce-ab29-aa26015fdafb | 2.11276 | -61.82241 | 2025-02-28 05:37:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b337d145-9fbb-3397-9d54-73a7d4fa3385 | 1.28498 | -60.10075 | 2025-02-28 05:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f023f6ca-7e80-3490-b6b9-6c4f4bfbf399 | 3.21206 | -60.24662 | 2025-02-28 05:37:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc2bb422-ad85-331e-b3b7-32ad18ac15f2 | 1.66999 | -60.6633 | 2025-02-28 05:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4652f38-7482-3e0e-9b60-8dd158a7b9d2 | 0.73454 | -60.4785 | 2025-02-28 05:37:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ce817f4-8a4b-31ff-b84c-56660015cd93 | 2.37493 | -61.26082 | 2025-02-28 05:37:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a99c2fa8-7c2d-3f48-8138-5672e5413531 | 2.81004 | -60.81778 | 2025-02-28 05:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2718dbb6-3005-3aab-a4c7-7b11b9a8abbd | 2.50986 | -60.98088 | 2025-02-28 05:37:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c09ef55-c7e6-3a7a-b440-5e20f2e34bb7 | 2.10882 | -61.81932 | 2025-02-28 05:37:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| febf8928-6562-3863-b308-f62556bd7edc | 2.30005 | -61.05135 | 2025-02-28 05:37:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfa206e3-63da-3d37-b04d-e19d3709b87a | 3.21433 | -60.23805 | 2025-02-28 05:37:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ffaf3be5-aa92-3658-866d-e13dcc58dbea | 1.27726 | -60.07554 | 2025-02-28 05:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 012069f1-0975-358e-a56c-0fbb17306587 | 2.10825 | -61.81573 | 2025-02-28 05:37:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d69c537f-ad2d-3ddd-b210-f43e0f1ad558 | 1.19769 | -60.06899 | 2025-02-28 05:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6a9e602-688c-3761-9726-3cfad51bc5c6 | 3.20729 | -60.37434 | 2025-02-28 05:37:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fc432d2-74a8-39ba-bb26-4427f052eef8 | 1.08874 | -60.65376 | 2025-02-28 05:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1eef99c1-3a62-3f85-a7c4-5833ea271c8d | 1.31369 | -60.07158 | 2025-02-28 05:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8e4781c-753c-3a0e-8df5-5b862b2d864c | 2.10995 | -61.82654 | 2025-02-28 05:37:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f60a5355-888a-3401-b453-32df1ffe10c5 | 2.10544 | -61.81984 | 2025-02-28 05:37:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b7fd6ec-d6f0-3f09-a117-cc35cb435d74 | -1.56411 | -54.3661 | 2025-02-28 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60a4054b-52f7-3a0e-ae28-49e578e5bb74 | 3.20851 | -60.24717 | 2025-02-28 05:37:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76e54de3-210f-3f49-b737-7d24c823c354 | 1.28199 | -60.10563 | 2025-02-28 05:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ae29139-bb5f-38b0-b83f-0d35c943a385 | 0.83101 | -59.94999 | 2025-02-28 05:37:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 048a91c8-913d-3cf6-8ef5-973ba647d50f | 2.25437 | -60.2845 | 2025-02-28 05:37:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f2f2823-5b31-3a53-87dd-ab2c928ea16b | 2.11633 | -61.81717 | 2025-02-28 06:39:00 | AQUA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |


