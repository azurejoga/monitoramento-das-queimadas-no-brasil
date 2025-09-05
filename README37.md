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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c57cc53-4886-3122-a011-f59d7a82699f | -15.22703 | -52.38089 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38cd7e5e-cc10-3d95-9915-757ec4e69efc | -12.96446 | -54.80242 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 619efa94-6243-3b57-a3a7-67d0504ed17a | -15.36638 | -46.40721 | 2025-09-05 04:38:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e9c523a-fa61-3c44-8a54-0956fcb77e7f | -15.32032 | -52.74634 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eed43c2a-5606-3c1d-b622-6aa5c7113942 | -15.61376 | -52.89117 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 272a0071-1a01-3ede-b013-e3fc102ba0b1 | -15.22421 | -52.37626 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc986f20-a61f-3ac8-8533-ce257acb8507 | -15.61088 | -52.90799 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19614b56-8d5e-3a79-bd16-492728b94edf | -17.06409 | -46.47522 | 2025-09-05 04:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 654f943c-a550-3aa7-b739-e3b084daec0f | -20.23867 | -51.30398 | 2025-09-05 04:38:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| f44edf1c-7498-37ea-8d18-6a7d4a72abe8 | -15.71199 | -53.60014 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a4b2a70-51e0-35a8-9cfa-845934106eb2 | -18.95108 | -44.68201 | 2025-09-05 04:38:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6259e846-b9f9-3920-bfc7-c5c60a4af627 | -15.76207 | -53.64888 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee583c8e-280a-3cd6-a10a-4dc05253573c | -12.97956 | -54.78969 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa33bcba-c3cf-39dc-816c-662e514472ab | -15.85167 | -52.29536 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0049d6db-ee41-3ae4-bbfe-cc62d315757c | -16.3053 | -45.69199 | 2025-09-05 04:38:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e6893466-907c-3a01-a201-c4c94162cecb | -15.74371 | -53.6152 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f33ae2b-85fe-3abb-80bb-a6c9767e51d5 | -15.6116 | -52.90378 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 683049cd-15f0-39d0-9a51-3a66817affbf | -12.98713 | -54.79506 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c820dd55-1cdd-3f9e-bff1-2a2c6a340c40 | -14.28104 | -45.21866 | 2025-09-05 04:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 52fb28fa-47d3-3f4f-aa95-95afcb449675 | -15.8586 | -52.29678 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a3b6dfa-6b3d-3436-a378-58ba6caf40a7 | -19.40804 | -44.32489 | 2025-09-05 04:38:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 740fdb34-f034-3945-bcae-478c09d924e6 | -13.98898 | -49.54966 | 2025-09-05 04:38:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc925b37-ef25-34f2-86fd-702c9f2b204a | -13.26396 | -51.85078 | 2025-09-05 04:38:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a55f1193-05da-3161-ae11-8ba65daa8844 | -15.56966 | -46.4918 | 2025-09-05 04:38:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2929ece0-b47e-3bc6-855a-c35f69aea2b7 | -12.96511 | -54.77526 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91266fc6-b191-3d98-97c0-3d75b8a47494 | -15.06489 | -50.05647 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8dc0ffb-ae19-37c6-81fc-6a6204438950 | -14.98938 | -50.08849 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ceed9291-1a4a-392f-a75a-1fdd705ee794 | -15.73176 | -48.15163 | 2025-09-05 04:38:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8023dee2-bd46-3e86-b425-cba1a6e6bc5f | -14.43595 | -52.97916 | 2025-09-05 04:38:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| b3e05fe3-962a-34f1-a67f-13c3a3bf4162 | -14.98662 | -50.08434 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fb90774-ae2f-3bb9-b28c-81ec7983789d | -17.86392 | -40.1303 | 2025-09-05 04:38:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 08a7694c-6f59-3c9f-add9-687ec4d3b495 | -15.73998 | -53.61469 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82623133-047a-37c7-a36a-560bb2b46072 | -15.0704 | -50.06477 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b5519ce-e451-34cb-9494-501040127f3f | -15.54263 | -48.38826 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44df6d8c-92a9-3542-9db5-b3547ae03352 | -14.5669 | -48.08792 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f96d0575-0485-3b73-8876-070775394f8e | -15.54435 | -48.39998 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 347588dd-d233-3bd0-a90d-7fc27273add5 | -15.15022 | -53.51416 | 2025-09-05 04:38:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f290de48-f164-3248-bbd0-4467b8e1a514 | -18.46216 | -53.03741 | 2025-09-05 04:38:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 79194a36-c6a2-3370-a80d-be91af583fe0 | -15.04366 | -50.08242 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a19deda1-45b2-36c0-b416-8b05c0ec55d4 | -12.96923 | -54.77605 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36353c53-6657-35a8-9e6a-bed7973be2d8 | -15.02563 | -48.11972 | 2025-09-05 04:38:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dff01025-29ff-3135-9575-16d7e8f1437c | -16.49454 | -43.73465 | 2025-09-05 04:38:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95d23f0f-ef57-3b7e-a4e9-31ac51e5dac6 | -16.55829 | -55.12841 | 2025-09-05 04:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 06d7cda2-0fe4-36c1-95f5-0d6cf3ddbceb | -12.99064 | -54.82314 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 256e035b-472b-3871-83b7-2da7cae32325 | -20.23926 | -51.30029 | 2025-09-05 04:38:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| aa922b5d-b04a-373b-87b3-0f2b8c84983b | -12.89051 | -56.95233 | 2025-09-05 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 898af397-30dc-3ff3-8772-5237bfa3952d | -16.30144 | -45.69141 | 2025-09-05 04:38:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9f236b2a-7cb6-3942-9ba1-46a3da272787 | -13.88379 | -47.99741 | 2025-09-05 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04b2b19e-561d-34ff-bbb0-5c6eeb1f8c46 | -15.72075 | -53.61562 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82ffe0d3-040f-33f7-8eaf-67cfc3e2ad18 | -12.97546 | -54.81247 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a5dfde2b-ca6d-37b1-a084-5dbdc8507d6c | -14.58795 | -52.18427 | 2025-09-05 04:38:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 003c27da-7e01-3339-92b1-5edc5d6ce312 | -12.9934 | -54.83161 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 133f8a0e-1e0f-3b07-8e00-3ca37b6cc638 | -17.48899 | -43.33891 | 2025-09-05 04:38:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6048a52d-6ea6-33ca-9d8a-31314982b838 | -16.31402 | -52.95392 | 2025-09-05 04:38:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9467d01a-02c2-3af1-9742-e19a19b45f17 | -17.85824 | -40.12962 | 2025-09-05 04:38:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3ca48926-88da-322e-84b7-6cd800f4ee89 | -16.90588 | -45.75246 | 2025-09-05 04:38:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf562af0-68db-3e2b-9327-9cb6cb25e725 | -14.55617 | -48.08975 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d88e5e2-cb58-3133-ac7e-d4a41bf5de30 | -12.97615 | -54.80864 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 64c5cd84-11b7-353c-b377-f698548b34d0 | -15.74448 | -53.61071 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4092e7ba-9d46-3042-a92f-a89dac5e3d0c | -14.58272 | -48.02959 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f1b8430-180d-325c-aaa6-ea4edaf38169 | -15.35972 | -46.40139 | 2025-09-05 04:38:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 266d0c5f-b7cb-3162-a455-ca9317b2ac62 | -15.75729 | -53.67587 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a56ef6d1-605a-3130-9cb0-938c5150243e | -17.58611 | -52.5586 | 2025-09-05 04:38:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41a84381-fc0c-3a06-90c0-57b5ff0e1cef | -12.99681 | -54.81253 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8215108c-948b-32c8-966d-61a3b006ba1c | -16.55921 | -55.13002 | 2025-09-05 04:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2c311970-7137-3fee-a97a-892711fff6d0 | -15.99152 | -55.95491 | 2025-09-05 04:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 1476e441-dd09-3bd3-9a76-7bb8b54700a1 | -16.49507 | -43.73037 | 2025-09-05 04:38:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d54ad868-4ad8-3b90-9352-447fca343ba1 | -14.98443 | -50.07659 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f09f95f-1ef7-33ae-8695-1f7e4e1a9334 | -21.28025 | -43.88201 | 2025-09-05 04:38:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 55da9b5b-2308-39c4-8a8a-c13489c98a5c | -14.9811 | -50.07602 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81f9084a-83b2-3293-ad13-469a59d44ff0 | -14.54932 | -48.04282 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71fc03c3-3030-37ff-904f-0a9a00b23c6a | -15.14159 | -52.3298 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ace88c26-c7d5-3fb7-9748-0a53dcc775c7 | -19.40749 | -44.32929 | 2025-09-05 04:38:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04fc3db6-fe5b-3eb3-9e70-f3169b0725ec | -15.54662 | -48.40802 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e730f2e5-52b4-33c0-8f02-bf0ac3fad4b4 | -15.14383 | -52.38057 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 56b7d54b-ca7d-3f8c-86c5-863329d4b546 | -15.7536 | -53.67511 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f7d4df4-cd09-3d60-8d0e-996a3b4a0972 | -15.72039 | -46.22664 | 2025-09-05 04:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d293cc0f-eb61-3a10-8a6f-84ac92e8b979 | -15.14314 | -52.38464 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 442f9712-deb1-367f-b603-9e8eb82a1458 | -15.5483 | -48.39682 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efdee46d-4c44-3d15-ab5f-a588be5ba075 | -15.85581 | -52.29202 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afb3397f-215f-3223-b41c-dcaba65b9761 | -14.5417 | -53.14282 | 2025-09-05 04:38:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3454ba60-0c10-3176-8dd7-b86988b9bf55 | -12.96652 | -54.79103 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 01afbf95-2641-3489-8f17-164082efbb8c | -12.96376 | -54.78272 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ffb65f40-ef97-36ab-9561-befce159793e | -16.55923 | -55.12317 | 2025-09-05 04:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4f4eb018-3e9d-302a-af89-3d0539010645 | -13.50655 | -50.81069 | 2025-09-05 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c03db73-9e93-3fc3-bb52-11496968b6e1 | -14.564 | -54.53189 | 2025-09-05 04:38:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a99f625d-bcc3-3f30-ab89-877023264f06 | -14.28423 | -45.22416 | 2025-09-05 04:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7cfcea74-7bf3-3d7c-928b-ffaf7bbf0c2b | -14.28193 | -51.87609 | 2025-09-05 04:38:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d3d4e63-1038-3ddd-88f6-8386b7a456f9 | -12.99269 | -54.81171 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bbd01226-736c-3e0e-9add-f4349b4b8b1a | -15.54323 | -48.40742 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62806eab-769a-3961-983f-84f033515cfa | -18.40485 | -50.79064 | 2025-09-05 04:38:00 | NPP-375D | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e466273b-6e08-3915-97f5-6b74d58d13c0 | -15.62879 | -52.88943 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2f24ff2f-8e0c-3f5a-9dce-86ce04fd4b8b | -13.88039 | -47.99686 | 2025-09-05 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 570830d1-0e13-3dcc-8f42-edfce02b1d4e | -12.97684 | -54.80482 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b0149d5a-0a01-3e4a-bc8f-a9ee12a4be8d | -13.27313 | -51.8606 | 2025-09-05 04:38:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5c59bbf-cf9e-38c2-a3df-8331da46eec7 | -15.04453 | -50.04255 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0803984-d768-3800-8ad2-d01bb8838d48 | -15.98693 | -55.97921 | 2025-09-05 04:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 259cce5d-787c-3556-9499-c46a4511260e | -15.136 | -52.34139 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 949cf5d8-9bd3-3504-bfc0-feafb231608b | -14.57086 | -48.08479 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f5cbb42d-35ec-3374-9279-5952c3bfb984 | -14.49176 | -53.06807 | 2025-09-05 04:38:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README38.md)
