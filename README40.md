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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e90a6f66-1dde-3091-b3ba-4a9e8b62cb92 | -14.88282 | -45.54761 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6356502e-0c16-311b-bdbf-d35279b9f0ec | -13.76039 | -47.87058 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efe4205f-ab82-339e-a87c-82503b8d1a16 | -15.24936 | -46.44762 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0f17eb6-b5e3-32df-afd3-f0c054d4052f | -18.25344 | -47.0112 | 2025-09-27 04:25:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0dee6be-0e57-371f-a817-d6bf8ffaed6b | -15.035 | -46.94854 | 2025-09-27 04:25:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a1a72597-9251-3aba-8a80-b4e7e9fed04b | -13.67152 | -47.6885 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71b0c08e-ada7-3be2-9d10-66471c1da61f | -15.56316 | -47.91671 | 2025-09-27 04:25:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 42c0f4f1-d47b-3d4f-ba02-ddf871689ef7 | -14.96987 | -46.76157 | 2025-09-27 04:25:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f19c9064-2057-3898-922e-44a9386007ba | -14.02117 | -56.10748 | 2025-09-27 04:25:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a587a79-cf74-38bd-92bc-33c4896d4117 | -20.16989 | -46.20473 | 2025-09-27 04:25:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 237ee30e-e859-372d-af47-5cfd6d238dd1 | -15.2028 | -48.47103 | 2025-09-27 04:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 11bd72ed-f484-36ba-8dbf-568b57c0fb84 | -13.76322 | -47.87458 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a68e49ca-eb36-3124-8bb8-bc44dcfe6d48 | -21.11214 | -42.92303 | 2025-09-27 04:25:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0ccf4252-1feb-3040-aeec-5201a2e97f30 | -13.60188 | -47.29924 | 2025-09-27 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87c3e1e6-5d30-3819-9876-77d6f4a76518 | -17.75896 | -47.42806 | 2025-09-27 04:25:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3205a3b3-2a47-3df1-83a6-d95ff06b40f8 | -15.03329 | -46.95928 | 2025-09-27 04:25:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c64b1a2b-e8f3-3a1f-9e9a-0e0158282798 | -15.90373 | -57.50113 | 2025-09-27 04:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8cbd9178-86bf-3c27-8fcb-e68b2fbb98f5 | -14.94882 | -47.50653 | 2025-09-27 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bb294439-1a51-3c26-a71c-83de330da4f8 | -15.01114 | -54.9975 | 2025-09-27 04:25:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c4a90a2-9cd3-379c-a3e5-2dc8f50e58e5 | -15.89931 | -57.49929 | 2025-09-27 04:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08c856f3-df75-3a17-ae02-b69c267c3f35 | -21.2849 | -45.80941 | 2025-09-27 04:25:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 98113c71-7ad8-31d4-839b-1911f2b4ea8b | -13.61356 | -47.31218 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c53486fb-2a09-3f67-8ffd-d0a866ce700f | -17.3685 | -48.17736 | 2025-09-27 04:25:00 | NPP-375D | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ef3a333-31db-37f7-9b0d-f0e037aa17e8 | -18.18281 | -53.32363 | 2025-09-27 04:25:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06f8a5d9-07c5-3e56-bc8a-e894f6fcb77e | -15.42716 | -48.21246 | 2025-09-27 04:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37783bc1-f372-3a14-81fb-ea5d1ab47784 | -13.76662 | -47.87502 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b5f5af77-2c4e-3a07-af20-e94986843b56 | -19.63692 | -45.57325 | 2025-09-27 04:25:00 | NPP-375D | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e50ecf58-b773-3caa-aa7d-b3da000d9ac1 | -13.61297 | -47.31583 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c418dc83-c0af-3de4-aeef-a61420b683bc | -14.95276 | -47.5035 | 2025-09-27 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1722650f-86fa-3bc8-9ac0-b84a6b49ce15 | -15.59718 | -46.45329 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 826dc772-e969-3b7b-8832-faf06fc8ff85 | -13.51419 | -47.40777 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ffa870d-7316-32ee-8f32-5cfbd8b43516 | -15.02938 | -46.96232 | 2025-09-27 04:25:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19df5d52-b15e-3567-87cf-a0e3b19dd0fb | -14.88114 | -45.53606 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ad7f902-4cca-3d23-8552-2f955a4572b9 | -15.20344 | -48.46722 | 2025-09-27 04:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c1bcfa18-4dfe-3b67-b4cd-248a66663ff6 | -15.44636 | -43.64699 | 2025-09-27 04:25:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 00572c02-4a79-379d-a1a4-057fd0cfef81 | -16.12515 | -47.39323 | 2025-09-27 04:25:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01841639-2dd1-3cba-a0ad-f76f8ffdcae9 | -19.7885 | -46.14396 | 2025-09-27 04:25:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf9b8081-b3eb-3fd5-9b40-5e9b0e0242fb | -16.91022 | -45.94781 | 2025-09-27 04:25:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9692c5be-2fa8-3800-baa2-24e6deb942ce | -15.75597 | -48.50722 | 2025-09-27 04:25:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 832ace02-953e-3d42-a4d3-b24e871a603b | -13.67935 | -50.63378 | 2025-09-27 04:25:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb2409e6-f81d-31b2-b198-024f8d8a67ff | -14.84861 | -45.6132 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e07f74a-05cb-39b4-9442-c4136c9ef695 | -15.20084 | -50.10061 | 2025-09-27 04:25:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3309bfcc-1215-3b3f-a6c6-0907cf7e28ad | -20.35507 | -48.7886 | 2025-09-27 04:25:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6d28df7-3612-38c2-a923-5c8481721e7d | -16.91359 | -45.94836 | 2025-09-27 04:25:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38b51884-1258-325d-bb19-002822a3b9da | -13.80904 | -47.91696 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3418699e-abc6-333c-a113-6f45774fd69d | -15.28214 | -46.43468 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13b12d3b-c97e-38a7-b7d6-51c96831598e | -14.85476 | -45.57309 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e45de1e2-cd57-32bd-96e0-708a76bbe58b | -14.01979 | -56.10737 | 2025-09-27 04:25:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b74aaa56-25e2-3a03-b19b-c7dff09e2eeb | -15.66237 | -50.11143 | 2025-09-27 04:25:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac5737a7-7e59-394c-9fcc-6e138b7dd38b | -15.42437 | -48.20825 | 2025-09-27 04:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c41550f1-480b-3606-b404-99a74373520e | -14.42671 | -44.88071 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 786ee5bf-b2ac-3c5f-8079-bdae35326d59 | -13.61863 | -47.3022 | 2025-09-27 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ba6ed8d3-7ecd-3f91-87e3-06a93da8629d | -14.63522 | -48.29025 | 2025-09-27 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d5d217f2-a7f5-37da-9009-bcef8723996c | -14.6318 | -48.28972 | 2025-09-27 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26c54388-b135-322e-aec5-d86890815ff4 | -15.19725 | -48.46221 | 2025-09-27 04:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 16d406ad-fd79-3905-a855-bfb43318a0b4 | -15.56775 | -51.71386 | 2025-09-27 04:25:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d79ca55-1f6c-3411-a44e-19613b7039be | -15.11184 | -46.46197 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a409e17a-0627-3f0a-9b12-ef69e22c1414 | -14.43297 | -44.88552 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73a6cd66-c4b6-351d-8fb8-57c3cdf6aa23 | -15.42594 | -48.21996 | 2025-09-27 04:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 634d55e8-65bc-39c6-8361-71e34468768f | -18.41792 | -48.55437 | 2025-09-27 04:25:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9483e7db-e536-3635-96f2-260f745518f9 | -19.05313 | -48.13332 | 2025-09-27 04:25:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d5638836-f8ee-3f07-a1f3-991a89b0ae2b | -15.8849 | -59.32968 | 2025-09-27 04:25:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea32d37c-430a-3635-82bc-1cbe33e17448 | -14.9732 | -46.76212 | 2025-09-27 04:25:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36bcd70f-fad7-319d-a65e-c78f90023a04 | -16.18332 | -43.63641 | 2025-09-27 04:25:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14d21738-57c6-3a94-98be-cbb83df34c70 | -15.42193 | -48.22318 | 2025-09-27 04:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc5abba3-1100-3fbe-a922-9fd2ad9f2b1a | -14.4633 | -46.84669 | 2025-09-27 04:25:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11967506-6993-3903-af9a-9e66d6488ec9 | -14.82956 | -45.6251 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 18308b86-be26-38be-a948-476c5353f4b2 | -13.3797 | -47.82873 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4cbca359-6ad4-32d5-b0c6-17e5b968ae2b | -14.45997 | -46.84613 | 2025-09-27 04:25:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbd9c66c-7960-3752-ac98-cafff05b4978 | -15.14465 | -46.42702 | 2025-09-27 04:25:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddd7a2a4-de57-3b3c-806e-9a0d535c186d | -15.53312 | -44.33854 | 2025-09-27 04:25:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9865e117-a055-3bf6-9472-7c982a283c2e | -14.63117 | -48.29354 | 2025-09-27 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd15fdce-1ca3-3b46-8922-32d8e68f8ce1 | -14.05289 | -47.03883 | 2025-09-27 04:25:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cffa8628-30c4-3550-a6bd-5b839e31e535 | -18.293 | -57.09108 | 2025-09-27 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0e7378ed-9d87-39ac-9512-55277c75594d | -21.11262 | -42.91923 | 2025-09-27 04:25:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a7681786-0100-31f4-90c2-36506e118be3 | -13.6029 | -47.31426 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91976af4-67d8-3af6-a358-93c9076ac154 | -15.42254 | -48.21941 | 2025-09-27 04:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 008989d7-46b0-3936-8e21-dbffb606beec | -13.50573 | -47.41732 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fe66e86-5a84-364e-a0ee-a4bea8534dd2 | -15.74804 | -43.84973 | 2025-09-27 04:25:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8c975d34-fc9f-38bf-9bd5-e0b387a1bcf9 | -15.89314 | -46.19408 | 2025-09-27 04:25:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a5d42e54-2a28-3170-b7b9-45c4a2289315 | -21.19044 | -45.5885 | 2025-09-27 04:25:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 60b84437-b95e-30f6-97e9-826e23ed1558 | -13.37631 | -47.82811 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c901e020-8d15-3fad-ae37-1138649b029c | -13.75088 | -48.37548 | 2025-09-27 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7298dd8f-4777-3af6-85c4-b36b4287a914 | -15.55367 | -47.91135 | 2025-09-27 04:25:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e311ccd9-e9e1-3b0b-957b-30abeec0fc13 | -14.63054 | -48.29734 | 2025-09-27 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2cc537ce-9bad-311f-884a-bf21dd114abc | -15.87842 | -59.3289 | 2025-09-27 04:25:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb3a451a-d108-3d42-9c4f-41f4427975ba | -14.58967 | -48.24778 | 2025-09-27 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 049cfaca-0511-3436-a9da-91d3a2f1b9d4 | -13.70743 | -47.89599 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| beafc476-657c-36ce-9b47-2cbfbeb99db2 | -21.5611 | -41.33585 | 2025-09-27 04:25:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a5b2ce35-8b7d-3299-91a6-3364153090dd | -13.63926 | -48.07563 | 2025-09-27 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c715b748-3d97-31c2-9a8c-aad46e5e0abe | -15.27824 | -46.43773 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55db8880-cd71-35c4-98ac-22dccb21129e | -15.25268 | -46.44819 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21081935-4177-3362-9080-73fc9c9e54bd | -15.03271 | -46.96288 | 2025-09-27 04:25:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 464eee0d-27db-3b6e-9ff4-7c76eebad2c2 | -14.8933 | -46.95118 | 2025-09-27 04:25:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 794628eb-478c-3a8e-8d81-bbbc14668eeb | -14.05623 | -47.03938 | 2025-09-27 04:25:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80cc6029-3494-3ea0-9b06-a018499ee587 | -16.71348 | -51.48088 | 2025-09-27 04:25:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba1a9440-8e1c-3e15-b887-e3d4efd6b6f6 | -15.27713 | -46.44489 | 2025-09-27 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 535f3f08-97a7-34c9-98c9-612157492c52 | -14.82844 | -45.6324 | 2025-09-27 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e599b9f8-edd4-3a4c-bc66-0970fa1bb6dd | -14.78015 | -60.18541 | 2025-09-27 04:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b53d0318-eb80-310e-a1fa-b8b17ded80ca | -15.15949 | -47.88299 | 2025-09-27 04:25:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README41.md)
