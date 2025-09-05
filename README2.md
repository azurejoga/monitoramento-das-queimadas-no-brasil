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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 116c0644-186f-3b1c-82da-fb2af72f0dbe | -5.5894 | -45.0051 | 2025-09-05 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 5a8031ba-45bd-3520-8156-56a1a2f235aa | -23.605 | -52.8732 | 2025-09-05 00:20:00 | GOES-19 | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 107.5 |
| 5d59bf46-b8e3-3313-8368-d2cd41cb072b | -5.6077 | -45.0492 | 2025-09-05 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 6a0886ee-6993-393b-90af-077a81af986d | -13.1079 | -57.1109 | 2025-09-05 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 160.6 |
| fd2b2e20-87b1-3399-b9e6-d25965cc159d | -22.72316 | -43.76588 | 2025-09-05 00:26:00 | TERRA_M-M | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 2572711e-2a99-3d6d-aad1-7f86c6929ac4 | -23.03855 | -47.82814 | 2025-09-05 00:26:00 | TERRA_M-M | LARANJAL PAULISTA | SÃO PAULO | Brasil | 3526407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 6ac58e40-255f-3568-ab02-a7dff653d4d3 | -21.49262 | -46.1971 | 2025-09-05 00:26:00 | TERRA_M-M | DIVISA NOVA | MINAS GERAIS | Brasil | 3122405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| a64de5d3-69ec-30eb-bcf5-29a587bcef30 | -23.60011 | -52.8561 | 2025-09-05 00:26:00 | TERRA_M-M | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 99.3 |
| bb36bde5-312b-3611-bdcf-667caaf352cb | -22.66443 | -46.82243 | 2025-09-05 00:26:00 | TERRA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 300381ee-214f-35c2-ad46-1fca056f785e | -23.29733 | -46.1535 | 2025-09-05 00:26:00 | TERRA_M-M | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 018a9433-f9de-3622-8c2c-cbb664d704f2 | -22.62811 | -46.73599 | 2025-09-05 00:26:00 | TERRA_M-M | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 2aec7192-06b8-3918-913a-cd3e3217f916 | -23.22544 | -45.32592 | 2025-09-05 00:26:00 | TERRA_M-M | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 3788703e-a532-3cc0-8cdf-3e1f3e8a9ee5 | -22.2819 | -47.63481 | 2025-09-05 00:26:00 | TERRA_M-M | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 2aeb1613-d376-3cb8-82f8-9f995d593d23 | -23.59774 | -52.86184 | 2025-09-05 00:26:00 | TERRA_M-M | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 156.3 |
| 3bb16b1e-c8d9-30eb-adfe-d95ad97987c1 | -20.52539 | -46.11479 | 2025-09-05 00:26:00 | TERRA_M-M | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| db93eb77-72fc-38a1-bab5-a463c1085f9f | -23.60254 | -52.88465 | 2025-09-05 00:26:00 | TERRA_M-M | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 183.5 |
| 91f277c3-517c-3e45-b094-21fdae73ef37 | -22.26254 | -47.6377 | 2025-09-05 00:26:00 | TERRA_M-M | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a298bf7e-8fe8-35b5-89df-1c6b8cb99f24 | -20.52411 | -46.1052 | 2025-09-05 00:26:00 | TERRA_M-M | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 07b6b99a-5532-3f75-8460-bc3491fb036b | -22.2738 | -47.14111 | 2025-09-05 00:26:00 | TERRA_M-M | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fb22b47d-8ca9-3e7b-81b2-c1fc5631e843 | -22.85541 | -43.72643 | 2025-09-05 00:26:00 | TERRA_M-M | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| e3029386-71ac-367a-90bd-ec3b35bffdca | -21.37066 | -46.95485 | 2025-09-05 00:26:00 | TERRA_M-M | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 41f89321-3ee7-3ffa-8ff4-2df69f23894a | -21.49134 | -46.18727 | 2025-09-05 00:26:00 | TERRA_M-M | DIVISA NOVA | MINAS GERAIS | Brasil | 3122405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 93028173-0979-348b-b921-b2e5dca09764 | -22.27244 | -47.13015 | 2025-09-05 00:26:00 | TERRA_M-M | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bbd84c89-9516-3883-aa5e-b462ef18d535 | -23.60033 | -52.89001 | 2025-09-05 00:26:00 | TERRA_M-M | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 98.7 |
| 581f9204-c826-3af0-b37b-b783e194f704 | -14.28618 | -45.22845 | 2025-09-05 00:28:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 62d0438b-fddc-32bf-afdc-e6abe12f0c3a | -13.47308 | -46.83991 | 2025-09-05 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9d87a147-4439-377a-be24-3a0aafbab4be | -13.22006 | -44.55033 | 2025-09-05 00:28:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| d667f088-e2e2-3bb7-9f5b-8371c5095239 | -13.58094 | -48.11714 | 2025-09-05 00:28:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 38f608e5-abb9-3487-8e73-fe3a55357171 | -18.8676 | -46.36993 | 2025-09-05 00:28:00 | TERRA_M-M | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2fbf3dfc-d22e-3131-bf03-ad6121b6985b | -15.85628 | -52.29288 | 2025-09-05 00:28:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 773f3a0b-90b5-3345-b1e6-e3831d325816 | -14.56065 | -48.08695 | 2025-09-05 00:28:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4e1d66f6-650e-3b08-ba01-a2d4b6ae322e | -17.53706 | -46.60387 | 2025-09-05 00:28:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 91d9134f-4338-3a41-8b6a-a519a5238dde | -16.903 | -45.74707 | 2025-09-05 00:28:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 20484df2-9175-3f5a-a201-dff1df9e1c13 | -13.65658 | -47.92583 | 2025-09-05 00:28:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7aa2b02a-d386-3a1f-ab0d-254c8fcf66da | -19.80557 | -45.68799 | 2025-09-05 00:28:00 | TERRA_M-M | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6e1c8fcc-76a7-3161-806a-0e782379bc9a | -13.87531 | -47.97906 | 2025-09-05 00:28:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 749c0f22-c723-3ec1-9ac7-30bb0efffcb0 | -13.74125 | -46.92639 | 2025-09-05 00:28:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c18bfd4b-862d-3ce8-a7f8-d94880dd4ae0 | -13.87658 | -47.98855 | 2025-09-05 00:28:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 83a21e6e-9d51-3583-9469-746e7f998406 | -17.4923 | -43.33955 | 2025-09-05 00:28:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 21630990-06ff-3d3d-a969-db00d4d2a8cc | -16.30581 | -45.68812 | 2025-09-05 00:28:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5d0ec340-b7b3-378d-8d5e-47242d3abcf5 | -18.23949 | -42.66957 | 2025-09-05 00:28:00 | TERRA_M-M | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| f8f2ddf2-031b-3444-9970-c7695b672cf1 | -16.3071 | -45.6973 | 2025-09-05 00:28:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 71aaea50-d4da-37e2-ac07-c1d9916dd04e | -15.85858 | -52.31318 | 2025-09-05 00:28:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9bac2665-588b-3d19-8844-828b29d1d0de | -14.56974 | -48.08537 | 2025-09-05 00:28:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ceb43052-558b-30e0-93ee-fb3ace093d27 | -18.956 | -44.68656 | 2025-09-05 00:28:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e24ad5f7-5cc5-3852-adc9-136f64293baf | -15.20208 | -52.37484 | 2025-09-05 00:28:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5e36791d-d429-3690-99de-9e53eeb66aa1 | -13.38078 | -45.73133 | 2025-09-05 00:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3b00e4f6-7388-3cbb-8382-edc338943f65 | -15.19322 | -48.00397 | 2025-09-05 00:28:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 45c8c146-dee9-38a8-8bc8-4639ce6f2fea | -13.73991 | -44.71008 | 2025-09-05 00:28:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 54c5221c-8bf1-3a10-b8a9-76f5ca94d4ee | -15.75298 | -53.63915 | 2025-09-05 00:28:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| cb313730-7573-37e5-b85a-500d4615ee6e | -15.5501 | -48.41404 | 2025-09-05 00:28:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 36066390-268f-3b29-8af6-a92b4630e2cc | -17.53833 | -46.61324 | 2025-09-05 00:28:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ef238e13-2ada-361d-98fc-53a9b2e870a4 | -16.50182 | -43.73009 | 2025-09-05 00:28:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 6badc5b8-2368-32c0-b3bb-4ac4621f80a7 | -17.52942 | -46.61457 | 2025-09-05 00:28:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 080673ae-15f4-303c-9306-6564c558261f | -15.22877 | -52.39009 | 2025-09-05 00:28:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 314cc072-2e73-3df8-88be-abc7acc5839a | -14.58806 | -48.013 | 2025-09-05 00:28:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fe59162c-53ac-32a3-8902-c0e68d45033d | -13.87134 | -48.01823 | 2025-09-05 00:28:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dee706b5-5b0a-3ed7-8c87-d38e4ae94c22 | -14.28481 | -45.21898 | 2025-09-05 00:28:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| f4fca64f-21a6-3175-a259-297ebd2e2183 | -15.55145 | -48.42451 | 2025-09-05 00:28:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a4947289-a594-3114-8557-024f3dffe7b2 | -19.30192 | -42.11982 | 2025-09-05 00:28:00 | TERRA_M-M | SOBRÁLIA | MINAS GERAIS | Brasil | 3167707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 1df6a4f8-6145-3bbc-90c7-173a0219b3ab | -17.62379 | -46.70002 | 2025-09-05 00:28:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0a10027a-94f1-3654-b55c-a037ae5605d5 | -17.62505 | -46.70944 | 2025-09-05 00:28:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8f3b0e73-c82d-3845-90dc-2e7eed93c25b | -19.1266 | -46.44777 | 2025-09-05 00:28:00 | TERRA_M-M | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a9c2e5fe-68dc-3ad2-9ad8-9632503ec495 | -16.60154 | -50.83528 | 2025-09-05 00:28:00 | TERRA_M-M | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3afd2968-0fce-35d2-907a-3c85d07b30e0 | -15.54079 | -48.41554 | 2025-09-05 00:28:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4d65bf26-66bc-3634-98c8-9b4d3bdf4c3d | -16.49242 | -43.73154 | 2025-09-05 00:28:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 7bac48a3-b75b-31a2-a2a8-a5c1281e0f2e | -15.71625 | -53.62625 | 2025-09-05 00:28:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 7bcef32f-2532-34b0-9434-aeef9a0d3189 | -18.56877 | -43.61521 | 2025-09-05 00:28:00 | TERRA_M-M | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 029fb79b-d5fa-3663-90e0-ecb90d15af05 | -13.22154 | -44.56048 | 2025-09-05 00:28:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| b6dad771-a8ad-31aa-9c9a-e9bbbb9fcaf4 | -18.86886 | -46.37939 | 2025-09-05 00:28:00 | TERRA_M-M | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8bba0f8c-a5e2-3fda-a4ef-75e36560dec5 | -14.27717 | -45.22985 | 2025-09-05 00:28:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c70feed2-331c-38f9-80c6-77d6fdf7ffa5 | -13.73845 | -44.70016 | 2025-09-05 00:28:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d2e5bfb1-8de6-3852-8776-946ca8c3296b | -18.54071 | -48.26035 | 2025-09-05 00:28:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 18.0 |
| f6db8837-1622-3bf0-bbe3-24975b356689 | -15.54746 | -48.39349 | 2025-09-05 00:28:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9251f312-955b-338a-8fda-83aacd2a31f8 | -15.71381 | -53.60337 | 2025-09-05 00:28:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 630a6a65-86dd-397b-8828-0e997fde9e1a | -14.2758 | -45.22039 | 2025-09-05 00:28:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b20d5570-1e07-3613-b338-cd5b7900b435 | -13.75888 | -49.1094 | 2025-09-05 00:28:00 | TERRA_M-M | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| db0ec91c-53a7-3f22-8150-8a1888fe6c58 | -5.6081 | -45.0038 | 2025-09-05 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| c70f1842-86fe-34e8-9d2c-d96678428da2 | -14.2892 | -45.2134 | 2025-09-05 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 5e5580f8-b18c-35e8-9111-b9fdd3015d39 | -5.5892 | -45.0278 | 2025-09-05 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 704cf11a-7f2d-3546-a255-ac631e1e52f3 | -9.7034 | -51.0591 | 2025-09-05 00:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 43296258-5c52-39eb-a672-dd59199dc06c | -5.5608 | -46.1988 | 2025-09-05 00:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 11609084-122f-359b-80bb-e72a05450edd | -13.1079 | -57.1109 | 2025-09-05 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 991c4efd-9ca3-341d-8ff1-79317baabef3 | -9.0765 | -46.9891 | 2025-09-05 00:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 0062faad-7ab3-3969-bd3f-cdfd7c0d5404 | -8.0799 | -45.339 | 2025-09-05 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 61.7 |
| bc722cd7-c991-3f4a-afe5-dfab893141ed | -5.6079 | -45.0265 | 2025-09-05 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 218.4 |
| 1e4a32b5-a783-330a-81ea-406e0fec4bc0 | -7.8921 | -45.312 | 2025-09-05 00:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| d24a0f83-94b0-3cee-b55a-3d899c7411c2 | -5.5101 | -60.1183 | 2025-09-05 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 97cbd93b-3a4c-3851-beae-552f26d13531 | -8.0988 | -45.3371 | 2025-09-05 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| de533b44-d873-333f-8d2a-ef9486a5c811 | -5.4917 | -60.138 | 2025-09-05 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| d755aac7-3575-385d-8eaf-1b59f99a4fe6 | -5.6266 | -45.0252 | 2025-09-05 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 9bf1e299-ca3e-3dda-b64b-a71210404dec | -5.4918 | -60.1189 | 2025-09-05 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 0b6cd28b-fbce-3b1c-a58c-1b89d35cf54f | -9.2102 | -57.0918 | 2025-09-05 00:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| b56be4bb-89c7-32c4-b9f5-e8bdd559ea31 | -6.6044 | -44.5624 | 2025-09-05 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 14ef2ac2-fb02-3136-8596-5c3a62462ed9 | -5.7413 | -49.2831 | 2025-09-05 00:30:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 5216c273-8bd1-3d4a-abfd-7bb3fceb2ff2 | -13.0889 | -57.1126 | 2025-09-05 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 293862cd-8f52-3c09-b616-4e736459bf28 | -9.0762 | -47.0113 | 2025-09-05 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| caf975e7-60cf-3762-9e23-046625bbd182 | -5.0266 | -45.3362 | 2025-09-05 00:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| d91f031e-78d3-3251-897b-de8e437d5370 | -11.6409 | -54.5315 | 2025-09-05 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 06157d02-7776-3cf3-bb18-fc98a5ab621f | -9.2477 | -57.0697 | 2025-09-05 00:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |


[Clique aqui para ver as próximas entradas](README3.md)
