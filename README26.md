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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a9c392a-a157-3021-9c93-f3aa97ca133b | -11.12661 | -54.91019 | 2026-08-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 43223504-e735-321a-9953-1ff986896075 | -11.63538 | -59.01484 | 2026-08-07 05:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32a7e3cd-c7ae-3309-85a1-fad26472c4b7 | -14.35175 | -54.9152 | 2026-08-07 05:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 77b081e1-c278-3d53-a700-85dd708002c5 | -14.34336 | -54.92845 | 2026-08-07 05:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e085b61a-a012-3ce4-b6b3-941ee884f8bf | -14.35244 | -54.90806 | 2026-08-07 05:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 83ee3d81-8463-36c6-8d66-bb1334836a38 | -3.06965 | -39.64399 | 2026-08-07 06:20:00 | AQUA_M-M | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 86cbeb11-d37b-39d7-b460-df914f8f58d3 | -3.07575 | -39.6413 | 2026-08-07 06:20:00 | AQUA_M-M | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 146e463e-45cf-34e8-aac0-2b90f152a86c | -7.07683 | -42.26413 | 2026-08-07 06:22:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 65d1357d-a440-3f44-b7c0-9234b9fa030d | -4.45503 | -47.91808 | 2026-08-07 06:22:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 497f8ebd-64f8-36ab-b6aa-f83f3be09237 | -8.74278 | -39.12804 | 2026-08-07 06:22:00 | AQUA_M-M | ABARÉ | BAHIA | Brasil | 2900207 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 05c49994-d0dc-3aa0-bb10-8c71b5da7812 | -4.27052 | -48.19051 | 2026-08-07 06:22:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| e7c87345-b1d0-3970-824f-18c7fe615e47 | -6.8606 | -46.00597 | 2026-08-07 06:22:00 | AQUA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7799931e-cf5c-3fc8-8fac-c5f94bc41ce1 | 1.93983 | -60.84656 | 2026-08-07 06:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f04e01b-1f0b-378d-9c77-e1d1969f0848 | 2.52017 | -60.64824 | 2026-08-07 06:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05559fd9-c72e-3327-b746-ddc62e0d7c15 | 2.52089 | -60.65259 | 2026-08-07 06:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3e836f8-0bd4-3dc6-8f37-990e04d5b3c1 | 1.94305 | -60.84767 | 2026-08-07 06:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6ba4882-af85-3201-a852-736a349e9d00 | 2.51945 | -60.64389 | 2026-08-07 06:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82b09c11-c9d4-31b5-9a94-2f6e5e658f27 | 1.93713 | -60.84861 | 2026-08-07 06:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5e79f04-978e-33fd-a15b-ba5ee0c84ef9 | -12.5594 | -46.93985 | 2026-08-07 06:25:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7412efff-6248-35fb-92b6-7870647a79fa | -12.57602 | -46.89815 | 2026-08-07 06:25:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5e8296bc-96a9-3c0a-a968-6571772ad50b | -14.42823 | -45.66206 | 2026-08-07 06:25:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2e41a84b-d7b5-3b18-a5c9-1cceafdd214c | -11.1526 | -44.48044 | 2026-08-07 06:25:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c0224648-19ee-3225-a2d0-8ff3da25575e | -19.71023 | -48.13171 | 2026-08-07 06:25:00 | AQUA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 45f9465b-544b-31e0-94f7-6ff6f448216b | -11.14378 | -44.47908 | 2026-08-07 06:25:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 26da1934-7496-302b-b1d0-9ae3debf01cd | -13.93264 | -47.35855 | 2026-08-07 06:25:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 96e56062-2b92-3e4c-a1eb-8a9bb0b85aad | -12.63114 | -46.88955 | 2026-08-07 06:25:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 228948b2-39e0-30f9-afb5-aef27e941d09 | -14.41786 | -45.66994 | 2026-08-07 06:25:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fac11861-a53f-3dfc-aa46-b5fce9278454 | -11.14517 | -44.47008 | 2026-08-07 06:25:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 809f1e85-9e61-3483-9e13-e5bb38a6cabc | -14.42678 | -45.67139 | 2026-08-07 06:25:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a79af3ba-121d-30e5-8ad5-abf630954ee9 | -14.27332 | -45.29304 | 2026-08-07 06:25:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5fcf926d-6a14-3c33-b4c4-f263a27c3f85 | -10.0734 | -67.79009 | 2026-08-07 06:25:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f145eed-8472-3e22-934f-8517e6d01623 | -22.93259 | -46.17058 | 2026-08-07 06:27:00 | AQUA_M-M | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 485b52ef-3813-391f-a6b3-ff6e757eba74 | -22.93118 | -46.18005 | 2026-08-07 06:27:00 | AQUA_M-M | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 9a24811e-da7f-3bf3-b11d-6d50fa891d2d | -7.75587 | -73.06255 | 2026-08-07 06:44:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d05c35b5-273c-35f3-8f1c-818f8ae47801 | -15.0781 | -53.5947 | 2026-08-07 07:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 47.1 |
| e523313d-fccc-3210-91d1-ae45f62973f8 | -15.0975 | -53.5922 | 2026-08-07 08:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| bffabfcd-e7f9-3eae-b35c-0f0a410b60e5 | -15.0781 | -53.5947 | 2026-08-07 08:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 594cd023-a291-3035-916f-d5d9efdf7616 | -15.0785 | -53.5737 | 2026-08-07 08:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 15710775-0dd3-386b-be0e-3e36c06c3dc9 | -15.0975 | -53.5922 | 2026-08-07 08:50:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 44.3 |
| cce0f1c9-729c-3add-b3e7-72c0cd0a04e0 | -15.0781 | -53.5947 | 2026-08-07 08:50:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 28aca27a-7146-35e3-8227-8254fb7a70d5 | -15.0785 | -53.5737 | 2026-08-07 08:50:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 0c7304ac-5558-3021-884d-b9cc7cba70c0 | -15.0781 | -53.5947 | 2026-08-07 09:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 15ff3948-9966-3b1a-a2e3-df7af6971b24 | -15.0975 | -53.5922 | 2026-08-07 09:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 1c0d430d-56e9-337d-9731-0f6c99c97447 | -15.0785 | -53.5737 | 2026-08-07 09:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 6b086151-706f-397a-8f5a-e5a0a1fcebac | -14.27929 | -45.30885 | 2026-08-07 11:19:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f07462e7-f71a-3de9-bfdc-9643b3715973 | -13.39178 | -43.56705 | 2026-08-07 11:19:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 41b2b2e4-13d9-3bde-bdab-c0e82f741dc5 | -6.98259 | -42.8947 | 2026-08-07 11:19:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 8abf4f26-350f-38f9-ad64-31832f762ee3 | -6.4789 | -42.22384 | 2026-08-07 11:19:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 027038fc-4d95-3432-a720-dc9c772a709c | -16.46802 | -43.43902 | 2026-08-07 11:19:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eb0ffbec-a808-36fc-9ed1-31196f961076 | -6.99261 | -42.89626 | 2026-08-07 11:19:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 6bcd65b4-9837-3119-a21e-547f2539ff03 | -9.56067 | -37.18093 | 2026-08-07 11:19:00 | TERRA_M-M | OLHO D'ÁGUA DAS FLORES | ALAGOAS | Brasil | 2705705 | 27 | 33 | nan | nan | nan | Caatinga | 6.5 |
| e752283f-208b-37c1-b398-d4adfdaaf79b | -14.27718 | -45.32226 | 2026-08-07 11:19:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| e8712184-682c-301e-b04e-2fa1f2382dbc | -13.39013 | -43.57776 | 2026-08-07 11:19:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a9bffe29-c151-36ea-8d6e-89ec6ffe1231 | -11.93311 | -42.04238 | 2026-08-07 11:19:00 | TERRA_M-M | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 043e1489-82cf-3266-a402-22515030c870 | -12.55574 | -46.94078 | 2026-08-07 11:19:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| c609e1a2-dec5-372a-ba16-527a1c79647e | -8.21465 | -42.2124 | 2026-08-07 11:19:00 | TERRA_M-M | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 15d00ef7-9a92-390b-b1e4-fe13f49fd707 | -14.44192 | -45.67907 | 2026-08-07 11:19:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 624ecb06-0d13-3704-9cef-5668db2cbefb | -13.28027 | -43.56492 | 2026-08-07 11:19:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 21bd1acd-19e6-3e3e-859e-0a383621ac4f | -16.46956 | -43.4289 | 2026-08-07 11:19:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ad99917a-343f-3ac8-a2e8-f58eb12fc88b | -15.66007 | -46.82808 | 2026-08-07 11:19:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 52671f45-c1e1-3f94-be21-bee8af584877 | -11.02259 | -43.49492 | 2026-08-07 11:19:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| cb2f26c2-bfb7-319c-977c-62bd1c287c45 | -10.56586 | -42.36717 | 2026-08-07 11:19:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 2cb2f52e-f8e8-3efa-a5bc-4b222d6a597c | -12.5607 | -46.9291 | 2026-08-07 11:19:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 86475104-dbd9-39b7-9e1d-127c5ceeb5b0 | -15.07549 | -45.45806 | 2026-08-07 11:19:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 69ff0b4d-01a0-3088-8a4e-09ceee50ea84 | -10.55658 | -42.36579 | 2026-08-07 11:19:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 747ad9f6-1ffa-3d94-9b21-a48fc8eaa1f0 | -8.81168 | -39.71104 | 2026-08-07 11:19:00 | TERRA_M-M | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| d92e3b31-511e-3314-b878-c758025fe178 | -12.55777 | -46.94647 | 2026-08-07 11:19:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 95c23176-5f5d-3080-8a5e-ad6f38b5afbb | -7.07595 | -42.26215 | 2026-08-07 11:19:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 0b3353fe-6c56-388b-8e63-638efba0f958 | -13.2786 | -43.57566 | 2026-08-07 11:19:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 6c31182a-4353-3aeb-9fb3-94370ed5fc9c | -8.90531 | -41.23475 | 2026-08-07 11:19:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 239b6561-15e1-3cc2-a5f9-d5ba085ba811 | -14.2687 | -45.30709 | 2026-08-07 11:19:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| c19abd43-4bb8-33e8-b7cb-3f8f2be52f03 | -15.07763 | -45.44462 | 2026-08-07 11:19:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 552d5218-e6a2-3d63-b4db-7c144267ce92 | -8.12932 | -42.97089 | 2026-08-07 11:19:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| c0679039-4608-373f-b15d-dbae83203cbb | -6.47729 | -42.23455 | 2026-08-07 11:19:00 | TERRA_M-M | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| f65cd3d9-77a1-3451-a8d7-1cb68769a568 | -9.48794 | -40.53326 | 2026-08-07 11:19:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a7886782-c6c6-3dc1-8d10-0316c3dc5a48 | -14.26657 | -45.32056 | 2026-08-07 11:19:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| d7a3f3e5-82d4-35b6-86c5-d195c5dea91b | -9.31062 | -40.28051 | 2026-08-07 11:19:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| db8f1b1b-0d3b-31c4-a52a-118c399a51a4 | -14.43962 | -45.69318 | 2026-08-07 11:19:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 0612ccd4-aa70-3bdc-a0b1-b0ae11e020fa | -9.41249 | -40.41646 | 2026-08-07 11:19:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a338606e-2852-3093-b687-d20ed2d0d211 | -21.34413 | -42.78477 | 2026-08-07 11:21:00 | TERRA_M-M | DONA EUSÉBIA | MINAS GERAIS | Brasil | 3122900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 387fca2f-686b-350e-93aa-83251efb972f | -17.84608 | -42.86599 | 2026-08-07 11:21:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8bf6b86e-4cf0-32a0-b6fa-2f3c77ac0484 | -19.32818 | -40.58102 | 2026-08-07 11:21:00 | TERRA_M-M | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| f5da8647-b3b9-3346-83a9-125c71c36f8b | -20.99256 | -45.56192 | 2026-08-07 11:21:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 31.9 |
| bea254a7-7a1c-38c1-a8f5-b09ad308ec2f | -22.93708 | -46.17508 | 2026-08-07 11:21:00 | TERRA_M-M | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 01d7a35e-918b-3158-a3e1-abf5c5f056ea | -20.9907 | -45.57333 | 2026-08-07 11:21:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0436c286-e6ee-30ba-9b35-1bde60bf9128 | -17.98169 | -44.28011 | 2026-08-07 11:21:00 | TERRA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 858b9da7-bde1-3339-aacb-401d497640c4 | -17.58537 | -46.49484 | 2026-08-07 11:21:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 97c362fa-d30d-3399-a70a-9c6f563875d6 | -22.93525 | -46.12542 | 2026-08-07 11:21:00 | TERRA_M-M | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| a91fafe2-6e97-3027-909b-9bac747b0808 | -19.16222 | -40.65603 | 2026-08-07 11:21:00 | TERRA_M-M | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| e7ab5e59-015d-374b-b0c7-dd3cbc617203 | -18.3129 | -46.65007 | 2026-08-07 11:21:00 | TERRA_M-M | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fb2338d3-16ee-30f9-b149-32b495be636f | -20.98906 | -45.56648 | 2026-08-07 11:21:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 33.7 |
| b62f4f2f-e82f-3553-b4d8-284eb0d1d5ee | -20.99084 | -45.55514 | 2026-08-07 11:21:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c7ab56df-c5f5-3de0-ac60-1af6f20e5fdd | -17.59626 | -46.4968 | 2026-08-07 11:21:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 48a02043-6191-310b-8062-9584c1251bae | -19.01428 | -40.73252 | 2026-08-07 11:21:00 | TERRA_M-M | ÁGUIA BRANCA | ESPÍRITO SANTO | Brasil | 3200136 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 25554c75-d589-3c55-9350-5a0036f6426b | -17.59247 | -41.29984 | 2026-08-07 11:21:00 | TERRA_M-M | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| f75b6962-71a2-3542-a81d-30be8db2833a | -19.336 | -40.59234 | 2026-08-07 11:21:00 | TERRA_M-M | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 95ade4a0-8b74-37e0-989e-01334326b7c0 | -20.07872 | -43.11822 | 2026-08-07 11:21:00 | TERRA_M-M | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| e9e7f0c8-e282-37bf-aad1-7bf13a04a6e9 | -14.2677 | -45.3103 | 2026-08-07 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 6671e876-6e24-3991-8728-66c884c820d2 | -12.4789 | -50.377 | 2026-08-07 12:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 94136a7a-b6c0-3fe5-b816-e6772e86c5b1 | -12.4789 | -50.377 | 2026-08-07 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |


[Clique aqui para ver as próximas entradas](README27.md)
