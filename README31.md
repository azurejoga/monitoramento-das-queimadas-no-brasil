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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b4ae7fa-3ec1-3ed7-ab69-b4f8abf2a769 | -17.77071 | -46.13429 | 2025-09-11 03:57:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4aa793e5-0c36-33bd-bdb8-d1ba85d8fabc | -15.67382 | -47.03456 | 2025-09-11 03:57:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07c17dfe-4b53-31f6-bcfa-d6456f54ae49 | -13.64884 | -45.70301 | 2025-09-11 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0770bf0b-70e9-3a7f-ae8a-af4c5b51d897 | -20.24057 | -43.57111 | 2025-09-11 03:57:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 034170be-120b-348f-a497-afbdc410c1a8 | -15.87447 | -54.94304 | 2025-09-11 03:57:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 28.4 |
| ea903545-35be-30da-a226-79f1bab61f4f | -18.28384 | -39.69844 | 2025-09-11 03:57:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 93899d1f-c6c2-3942-b9b9-9bad3cdd9ae4 | -14.78448 | -48.23358 | 2025-09-11 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dbf3a584-7533-31c0-91f0-b70c5cda07e8 | -12.84576 | -47.97095 | 2025-09-11 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| da483d70-c71d-3f3b-85a8-faf3cf5ac4db | -20.00243 | -47.63009 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28b0caf3-bc40-34f4-9c77-9e5abcf7f83b | -20.23917 | -42.74751 | 2025-09-11 03:57:00 | NOAA-21 | PIEDADE DE PONTE NOVA | MINAS GERAIS | Brasil | 3150208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 951acb7a-6375-3744-a637-fe2c273e24af | -20.07816 | -47.52655 | 2025-09-11 03:57:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a3e6370-5f68-394c-8856-3e00acc83bdd | -17.68699 | -44.20107 | 2025-09-11 03:57:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 321d0d22-c233-3d4f-8708-3e30a634763e | -19.55191 | -46.94708 | 2025-09-11 03:57:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| beb6166d-8b9f-38d3-a399-3fc30404cc8c | -20.46787 | -42.85034 | 2025-09-11 03:57:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0673fb6b-956d-3ee7-bf20-1af3b9fbc202 | -19.91118 | -44.3438 | 2025-09-11 03:57:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dfebb985-df39-35d1-badd-7773bc6029cc | -14.40057 | -47.30984 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6b473fee-7487-31e2-b980-023ef27d7ba4 | -15.80934 | -42.57191 | 2025-09-11 03:57:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1487485e-e69a-3950-8587-617ffaade53c | -20.46453 | -42.84975 | 2025-09-11 03:57:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| bb47e4c3-a7a7-3a06-be0f-c09bf3b91218 | -19.66522 | -44.89996 | 2025-09-11 03:57:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 38890ab6-d57e-39d1-9291-1d7daf583647 | -16.61758 | -49.41606 | 2025-09-11 03:57:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a04a12bb-a637-3449-b488-db791efa70d9 | -17.55613 | -44.54039 | 2025-09-11 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c6ab5a7-09c5-35fc-bc48-2feabd293dc0 | -17.84484 | -44.21605 | 2025-09-11 03:57:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f078aab4-9440-34a2-a0c8-3da664c07942 | -19.48251 | -44.31752 | 2025-09-11 03:57:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40c8dccb-4ef0-33bc-a4a7-73c815c65d22 | -15.24804 | -44.03044 | 2025-09-11 03:57:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d8b6c8be-0f25-3eb7-9c01-4abd38156882 | -14.30192 | -45.01987 | 2025-09-11 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47c90f25-7f4d-389a-bae6-4cf2f3f4b7ea | -17.99959 | -47.10861 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0829a4dd-42bc-3631-8731-11f5e892cca8 | -18.40821 | -43.48389 | 2025-09-11 03:57:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69ec164a-d91f-3d6e-a3d5-82756d55ffd1 | -14.71278 | -45.34072 | 2025-09-11 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d78a0ffc-a865-3595-9331-9caabb510c1c | -19.23811 | -48.00411 | 2025-09-11 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 9d33fc2f-6e6e-34ec-b2d5-d7c4c64bfdcf | -14.36815 | -47.30832 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5f5351a0-2396-35a6-b561-c2d76333be58 | -20.16888 | -44.619 | 2025-09-11 03:57:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f101738b-e16d-3890-ba68-e4c409588d77 | -18.76403 | -48.19317 | 2025-09-11 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c8eb148-882e-3a92-8a00-862648bb65ec | -15.75192 | -49.959 | 2025-09-11 03:57:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75b74611-871c-37f5-ae1c-4fefa188b065 | -20.70015 | -46.07789 | 2025-09-11 03:57:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2e4a8017-f25a-3618-b543-b34e979a7938 | -15.67535 | -47.02629 | 2025-09-11 03:57:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d5b98f57-021b-3222-8051-fb23de63af13 | -18.00929 | -44.04062 | 2025-09-11 03:57:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 754b5761-2d6b-3fa2-a6a5-03a0e8b0e585 | -18.71491 | -47.17981 | 2025-09-11 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7c95eea-d54d-3c85-abed-0554a6973563 | -17.50187 | -43.75658 | 2025-09-11 03:57:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abd53413-6b97-3d24-b3ff-c6a95c41fb33 | -20.07723 | -44.74667 | 2025-09-11 03:57:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6dadaf47-e295-35e2-ad92-092eb3cab6d8 | -18.56071 | -46.56479 | 2025-09-11 03:57:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9445fdf2-5014-3548-a0f2-8f0589de2a78 | -13.66059 | -45.73272 | 2025-09-11 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6ade55e-1c5b-3231-b4c2-9e5097d9fc7e | -19.90989 | -42.25543 | 2025-09-11 03:57:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1bd5c43b-56c5-3f16-8351-e7e18701a0b0 | -15.24729 | -44.03483 | 2025-09-11 03:57:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c0ec0dd0-74a5-3630-9608-e2362343c1d5 | -13.65505 | -45.71592 | 2025-09-11 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a23b136-a132-39fe-9fd0-dfeedc63abd4 | -18.01101 | -47.13965 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56ca5404-fafd-3e5e-a894-183749d075ba | -15.19686 | -44.0439 | 2025-09-11 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 902ae6c4-6244-3dcb-9872-b9314fdd8032 | -16.28853 | -45.68394 | 2025-09-11 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| baa94902-fe29-37ec-a856-b8b309605df0 | -19.95483 | -46.88372 | 2025-09-11 03:57:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 100162bb-2dff-363b-901b-96dcec09113c | -13.58387 | -47.70245 | 2025-09-11 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| df25e4ca-c788-335c-8768-9f1f1b23c2c7 | -18.01172 | -47.13591 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04d9ef2a-2308-36e5-b77f-3a94d3f06d38 | -13.9584 | -42.49417 | 2025-09-11 03:57:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fce2c2dc-5215-3e63-822f-3759bea8762a | -19.79302 | -47.16481 | 2025-09-11 03:57:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c8c3262-c263-389d-a33d-0427f249ef4d | -18.60286 | -43.97324 | 2025-09-11 03:57:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 905ecd13-6f42-39dd-981d-2db1107f894e | -19.02573 | -46.26271 | 2025-09-11 03:57:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64d420e4-8004-315e-9332-05c502518dbe | -19.9262 | -46.1671 | 2025-09-11 03:57:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0434e545-4999-3063-843e-6a62f50508a7 | -18.01146 | -44.45221 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 87a85726-da4c-364c-b044-02ef564f8f8a | -15.14199 | -48.61216 | 2025-09-11 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6c8982bf-aa9e-3bba-8384-2fc1dda72191 | -19.98153 | -47.62629 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 37e65efb-d57f-34c6-babb-74595817618f | -15.13756 | -52.4309 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9727364f-1c59-317e-933a-39a6406df8c4 | -19.55332 | -46.94409 | 2025-09-11 03:57:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 328196c2-5604-3b3d-9e0c-e418d05829f3 | -15.22406 | -44.01702 | 2025-09-11 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67f24953-9111-3252-b44c-9eab1b4ee970 | -18.34333 | -44.36194 | 2025-09-11 03:57:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 167ca191-3ee7-31ab-8f7f-90cbceaeee5e | -18.59121 | -43.8736 | 2025-09-11 03:57:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b3daa84-706e-36ba-baea-c119232f3ecb | -19.01893 | -46.25591 | 2025-09-11 03:57:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 094803d7-398a-3fc5-ab52-5cdaadf9dc8e | -12.97397 | -46.73195 | 2025-09-11 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0804d8e6-c293-34f9-bea5-212490937256 | -20.12623 | -47.69022 | 2025-09-11 03:57:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f922427-e347-344a-866d-e452e1df64dc | -15.47798 | -49.36086 | 2025-09-11 03:57:00 | NOAA-21 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 124fd13f-4ff4-3a18-9293-8e8289d10928 | -20.70141 | -46.06963 | 2025-09-11 03:57:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| eef901a0-861c-39a3-82f3-97ab12a847ff | -14.3813 | -47.33771 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fee55a47-fea7-38c3-82f6-0aec2a799baf | -20.70227 | -46.06483 | 2025-09-11 03:57:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdfcd881-4b35-3d62-8ea5-7eaef6bd6da3 | -14.77972 | -48.23269 | 2025-09-11 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c52c4bd0-725f-32ce-bd1f-266e0d3aea64 | -15.70344 | -43.85233 | 2025-09-11 03:57:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 96687d7b-bf64-3cc3-96ea-cdebabb03ee1 | -20.17241 | -44.61966 | 2025-09-11 03:57:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0c8a31c8-2521-3b4d-aecf-0274c4ff8c50 | -17.33321 | -46.67991 | 2025-09-11 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 215138b1-7f84-3a7e-894b-254afc3f873a | -18.89278 | -43.78276 | 2025-09-11 03:57:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfd91826-41e2-3574-ab55-d4286cd7caad | -18.7108 | -47.17881 | 2025-09-11 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| acb7c935-7d83-33d5-ace9-d163836af621 | -15.2268 | -44.04475 | 2025-09-11 03:57:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe102ff5-a965-398e-a3bb-b1f80a221ed8 | -17.78244 | -44.40742 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3893140-e809-3b14-96b1-52320fba700f | -15.25243 | -44.02669 | 2025-09-11 03:57:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f6c42e0-729f-3182-a6a3-4612a6df3e33 | -20.07445 | -44.74161 | 2025-09-11 03:57:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7192a06-44ab-3a5a-8898-656724bc4ad2 | -20.1311 | -47.68745 | 2025-09-11 03:57:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3963ff19-d614-30d9-9a75-57cd3fba80c1 | -15.80345 | -52.24012 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ac6bfd94-2ec3-349f-b3b6-0391a3dcb6ff | -19.18979 | -48.79348 | 2025-09-11 03:57:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3afa5f9-d381-3172-921f-7f2deed6650e | -19.33733 | -41.31244 | 2025-09-11 03:57:00 | NOAA-21 | RESPLENDOR | MINAS GERAIS | Brasil | 3154309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d5da1097-b9c8-3ef4-b94a-da8f95101178 | -18.62551 | -44.26357 | 2025-09-11 03:57:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b1e908e-0d38-3c74-95ee-53fb79978c79 | -16.63449 | -49.76959 | 2025-09-11 03:57:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29734565-8e70-363a-93a5-804f2ddccfae | -20.51637 | -47.63345 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b861cef5-ec2a-323f-946a-f4bd0eb9cd85 | -16.42968 | -45.683 | 2025-09-11 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a5b1da2-1f50-334a-a705-0ad76dd3f663 | -16.28757 | -45.68556 | 2025-09-11 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9ce3705b-503f-3ac9-a2de-c0d4ff1789ca | -15.56575 | -54.75569 | 2025-09-11 03:57:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 1c8e1926-c719-3d29-9aaf-7fd2e661b56b | -13.64722 | -44.26211 | 2025-09-11 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1de18936-2407-36f0-8b4e-0ac844ad0723 | -15.816 | -48.96017 | 2025-09-11 03:57:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 554cdf3d-a819-3118-9e91-e404bda77660 | -16.42871 | -45.68829 | 2025-09-11 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35a1f9d6-4478-390a-a61e-274d51f93490 | -14.47327 | -46.35535 | 2025-09-11 03:57:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61da4c93-28ab-31e8-b5a3-38ea7fe4bb13 | -20.36763 | -46.66607 | 2025-09-11 03:57:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cd8d91f-3c0b-34a3-b877-85f32d0af66d | -17.56184 | -44.55067 | 2025-09-11 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 43d8d62a-8827-3ee7-ae97-0996533aadf3 | -15.13225 | -52.42566 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 75b4f21d-5298-3366-aa21-74bb852d63b8 | -12.98566 | -46.74348 | 2025-09-11 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9ce4463-b5e9-33d8-9633-9a3877fd5a9a | -19.18809 | -48.79979 | 2025-09-11 03:57:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 365010ab-fd9d-3c4f-b8d2-e2fdba1603d6 | -14.12859 | -45.38431 | 2025-09-11 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README32.md)
