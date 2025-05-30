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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efc6e927-7f32-3a28-bb8b-ee6db72345c6 | -7.32259 | -43.49297 | 2025-05-30 12:21:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9d231416-aee9-378a-ac25-4d572ded6c63 | -6.3499 | -43.38233 | 2025-05-30 12:21:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 129.5 |
| e2ec523f-2248-3193-81d2-fe9995b0c1c0 | -5.78457 | -43.61396 | 2025-05-30 12:21:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| de134ecb-2622-3b41-b13a-9116e757e60c | -6.19385 | -43.10677 | 2025-05-30 12:21:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| cb7e27cb-277e-3a96-9ffd-344f9e8e650c | -5.7717 | -45.90206 | 2025-05-30 12:21:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cc4760ea-ff79-3fe8-af8b-c92f45865794 | -6.34851 | -43.39248 | 2025-05-30 12:21:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1335d042-dcbb-3c35-867f-ea735508db6d | -6.32322 | -44.17204 | 2025-05-30 12:21:00 | TERRA_M-T | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 35d5027f-3474-393d-9998-8fb58d76f368 | -7.58624 | -45.85837 | 2025-05-30 12:21:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3dc33c28-27ac-3816-97ae-212ca6d6f8f5 | -6.05658 | -44.0432 | 2025-05-30 12:21:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7c530e48-0d27-36c3-9b37-6154de2f6630 | -6.97264 | -42.78688 | 2025-05-30 12:21:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 542d7e83-9812-3e28-9f18-eba79916aee7 | -13.72054 | -45.25481 | 2025-05-30 12:23:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 9488a0b0-5f7e-3380-a100-fad0b4b3f940 | -10.61554 | -44.76046 | 2025-05-30 12:23:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 51.1 |
| ff387af8-946e-3d22-b088-3c161438b508 | -14.58925 | -47.53894 | 2025-05-30 12:23:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e1f96119-18bf-317f-b3ba-62318d608f02 | -12.0148 | -49.5182 | 2025-05-30 12:23:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e78a8ccb-6dca-32a6-83ac-603e4a5deadd | -12.17455 | -44.33597 | 2025-05-30 12:23:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5afc0cf9-8885-3c07-bb7e-1f4557cbdfe8 | -10.46234 | -47.9531 | 2025-05-30 12:23:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 21d82591-3f3e-33ca-a277-ff8ef5afe7e1 | -10.60496 | -44.76896 | 2025-05-30 12:23:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ae92466f-183a-3fcf-8116-d51d1382b417 | -14.8533 | -46.85455 | 2025-05-30 12:23:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a9a1bdea-f944-3c4e-8b45-594308c05c78 | -13.09025 | -45.29646 | 2025-05-30 12:23:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 47.4 |
| f32a0f21-8a3a-3305-a3ce-8118979eb3e3 | -12.24847 | -43.32118 | 2025-05-30 12:23:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9bbb0123-bfb1-3909-8569-71e83eaaeaf8 | -14.93234 | -46.94726 | 2025-05-30 12:23:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d434ca31-cc1e-3bb7-aa79-30b4b702bff0 | -12.1731 | -44.34664 | 2025-05-30 12:23:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 80ac1900-ca00-3cb1-8eaf-0605458596e2 | -9.26862 | -47.91814 | 2025-05-30 12:23:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6a2b2126-f31d-356c-95e9-d7d4b880d690 | -13.68071 | -48.6442 | 2025-05-30 12:23:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b1eaee05-da82-36a7-89e8-958189b0a753 | -13.71491 | -45.24762 | 2025-05-30 12:23:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| ccc3a365-e72d-303f-8565-96be23622e82 | -13.10003 | -52.0407 | 2025-05-30 12:23:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 1bb9d6bd-4a94-33d3-8e8c-d7662695be0e | -10.4976 | -42.50352 | 2025-05-30 12:23:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 29.1 |
| f052b05f-f45f-35e0-8d83-61bc96762040 | -14.83966 | -48.10437 | 2025-05-30 12:23:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 126779cc-6c05-3511-9b97-22ad409e662a | -10.73592 | -49.28089 | 2025-05-30 12:23:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 464890a1-ab6b-3a5b-ab14-8dacb62d35c9 | -9.04062 | -48.5113 | 2025-05-30 12:23:00 | TERRA_M-T | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7443d2eb-9bd6-338e-ba6f-309691540e4a | -10.73842 | -49.28793 | 2025-05-30 12:23:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 6755c404-64dc-3e36-a735-967290f13e5f | -10.46373 | -47.94371 | 2025-05-30 12:23:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| cb8076d4-df28-38e4-a88c-4e1bdca24a27 | -13.71631 | -45.23751 | 2025-05-30 12:23:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 299ec924-d722-31dc-ad76-715a15c84fe0 | -9.84289 | -44.68374 | 2025-05-30 12:23:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0b709c6e-38cf-330c-9f9c-ebe6cd80045a | -11.78448 | -49.7482 | 2025-05-30 12:23:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0ec677f9-db9e-35f3-b8f5-586328f1d77f | -10.22773 | -47.4175 | 2025-05-30 12:23:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c287cfba-0338-341c-b815-d78a039b70f5 | -10.22639 | -47.42662 | 2025-05-30 12:23:00 | TERRA_M-T | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 90fa7c26-1019-360d-9ed9-e567ef56889a | -13.09948 | -45.29774 | 2025-05-30 12:23:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 4e8ee42e-8f1b-314c-bc2a-e17f6e611365 | -14.66966 | -45.38678 | 2025-05-30 12:23:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f6e5ccb8-24d4-360f-aa2c-1d8e60dddf61 | -13.63825 | -47.42808 | 2025-05-30 12:23:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| dd5393e4-7b7a-38be-8ddb-5c60e79fda89 | -10.49124 | -42.51009 | 2025-05-30 12:23:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 0788d9c0-baf4-3039-86a4-b4b8e29bf926 | -10.61419 | -44.77023 | 2025-05-30 12:23:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 9ee0f5c8-6930-3747-97bd-12f96045d243 | -10.41491 | -46.57828 | 2025-05-30 12:23:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9b4f8143-a2e2-3724-bf32-3d419224417c | -13.10082 | -45.28787 | 2025-05-30 12:23:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 304.5 |
| 06c83991-7b0e-3422-953e-97a0ebca7c96 | -13.09159 | -45.28659 | 2025-05-30 12:23:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 246.8 |
| 9adac876-5f25-3cbd-bc2b-0e8904a92489 | -9.04216 | -48.50112 | 2025-05-30 12:23:00 | TERRA_M-T | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 0d38edd6-9edd-319b-b4fd-0e03af66ad77 | -9.27002 | -47.90857 | 2025-05-30 12:23:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 0ce26b3f-8a6e-30a1-a5b3-451f7d536229 | -16.0474 | -43.806 | 2025-05-30 12:23:00 | TERRA_M-T | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 487120c4-d2c2-3955-9ffa-76a52dbb2730 | -10.49299 | -42.49698 | 2025-05-30 12:23:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| fdfd40b9-9d30-3c5c-be2c-e5496e8ad7c0 | -9.6782 | -49.70723 | 2025-05-30 12:23:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4ab1baeb-48f8-3e73-bf95-5e3e01eca7fe | -10.74009 | -49.2772 | 2025-05-30 12:23:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d73f0d8f-af3b-37a1-a4fb-bbeb4e573756 | -13.72189 | -45.24475 | 2025-05-30 12:23:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| b7bdfc47-9bc3-3e04-b098-d0f04c245e82 | -17.28045 | -47.01519 | 2025-05-30 12:25:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 1b2758f9-07f2-3e29-a272-21e83b9e27dd | -16.76228 | -44.1212 | 2025-05-30 12:25:00 | TERRA_M-T | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| aedda1e7-ee78-3d4b-80f0-b4f08dd8910e | -15.98248 | -47.01572 | 2025-05-30 12:25:00 | TERRA_M-T | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 18.9 |
| adb9edab-9ce0-3993-a9f2-5bdf380b2b80 | -15.98378 | -47.00644 | 2025-05-30 12:25:00 | TERRA_M-T | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f887872d-8ecc-3f09-8a20-97f82b83e746 | -19.77193 | -48.92947 | 2025-05-30 12:27:00 | TERRA_M-T | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 726d8722-09b8-34b0-9fa2-b78072f10905 | -19.99007 | -47.17724 | 2025-05-30 12:27:00 | TERRA_M-T | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8f502a83-96aa-375b-afd5-f6148d2773b0 | -24.42583 | -47.88595 | 2025-05-30 12:27:00 | TERRA_M-T | SETE BARRAS | SÃO PAULO | Brasil | 3551801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 80a25737-a885-3148-a9c2-c8565d1aedb2 | -6.3536 | -43.3816 | 2025-05-30 12:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| bee3dff6-704d-347f-a7c2-5aeca0469126 | -13.0874 | -45.2791 | 2025-05-30 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 234.0 |
| 942c93c9-d341-3387-be9c-cad2e0ff8e88 | -6.3348 | -43.3832 | 2025-05-30 12:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 205.4 |
| 00b2c6d4-f4c0-3445-bb6d-e1d7706367b3 | -13.087 | -45.3023 | 2025-05-30 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 09ee62f6-7dd1-37f8-b2cd-24721363e627 | -13.1068 | -45.276 | 2025-05-30 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 261.6 |
| c457a9b7-5852-3601-8e41-9212e3bef52b | -6.9804 | -42.7854 | 2025-05-30 12:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 212.0 |
| 071ca83c-c3bf-37a0-9e57-8a2165bf9543 | -7.983 | -50.699 | 2025-05-30 12:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 145e6795-6f86-32a2-9cb2-cd19d0fc69aa | -7.983 | -50.699 | 2025-05-30 12:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 24ff4e98-7033-3178-a001-00a4c090e693 | -6.9804 | -42.7854 | 2025-05-30 12:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 187.9 |
| 566805a7-ce5a-368b-a698-92003b1675df | -6.3348 | -43.3832 | 2025-05-30 12:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 2a6b523d-f0cc-3814-8a79-6afc9a44a81a | -6.3536 | -43.3816 | 2025-05-30 12:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 84bb3147-3069-3042-9d06-4a072022ccb2 | -6.3536 | -43.3816 | 2025-05-30 12:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| a712b595-3b5d-3ebd-a742-d4db004d1b51 | -13.0874 | -45.2791 | 2025-05-30 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 198.0 |
| 413b85f2-d11e-3c47-ad1b-1eb120b84e56 | -13.087 | -45.3023 | 2025-05-30 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 1729a9bf-2a46-3f9d-b41d-5a1eadf1f27b | -13.1068 | -45.276 | 2025-05-30 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 273.0 |
| 72413d6f-716d-324b-98f6-cf96749ec69e | -11.6878 | -46.2231 | 2025-05-30 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 196.5 |
| 4d8693c1-8088-3178-bca3-d9a60ade2ec2 | -6.9804 | -42.7854 | 2025-05-30 12:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 280.7 |
| 1a2f7f37-50a5-3e82-812f-65c60b454705 | -7.983 | -50.699 | 2025-05-30 12:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 2d2eebaf-a3fa-348a-b3c3-f41baaad6e2a | -13.0874 | -45.2791 | 2025-05-30 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 183.6 |
| 29f14051-0566-3fe7-807f-e9012105548f | -11.6878 | -46.2231 | 2025-05-30 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 185.1 |
| 8bca1b55-ede0-36d4-9c30-e0bba5df94cd | -13.1068 | -45.276 | 2025-05-30 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 354.4 |
| 43f9a884-7cd6-3452-b775-7a5a9272591b | -6.9804 | -42.7854 | 2025-05-30 13:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 329.1 |
| a6a1a260-2fda-3954-9236-071836e237fe | -13.087 | -45.3023 | 2025-05-30 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| b4bd3d1c-2b7d-31c5-a89a-d83990b2808a | -6.3348 | -43.3832 | 2025-05-30 13:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 807539f1-84e2-319f-8351-54a42180dd4d | -7.983 | -50.699 | 2025-05-30 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 0a188ec1-29c3-3052-86c9-f463f5d56a3d | -6.3348 | -43.3832 | 2025-05-30 13:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 144.5 |
| f291bc46-1d85-3ef2-958b-be4d05592aec | -13.087 | -45.3023 | 2025-05-30 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 878ac0df-cdbd-3c7c-a07f-35b5a536aca2 | -13.1068 | -45.276 | 2025-05-30 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 334.9 |
| d88fa43f-f30c-3091-8b1c-ab1862c378d5 | -13.0874 | -45.2791 | 2025-05-30 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 169.5 |
| 66d05a8c-b492-3d18-a841-3b715b16528e | -6.9804 | -42.7854 | 2025-05-30 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 323.7 |
| d740273a-1ea1-355f-9daa-56cd547532b0 | -11.6878 | -46.2231 | 2025-05-30 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 250.1 |
| 6da106ca-218e-3ed0-b33f-f2056d502aaf | -11.8963 | -47.4537 | 2025-05-30 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 38259a9c-209d-31f6-b582-55381b874666 | -13.0874 | -45.2791 | 2025-05-30 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 4106bbd3-6b00-3032-8781-6730a3ae23c9 | -6.9804 | -42.7854 | 2025-05-30 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 323.9 |
| 91a88c52-827b-30a9-b294-440a1ae0fac0 | -13.087 | -45.3023 | 2025-05-30 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 21d568cc-a06d-353c-8e5f-b6d2345fc166 | -11.6878 | -46.2231 | 2025-05-30 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 169.2 |
| e6aba834-2ef9-3d77-b976-2ade955a6525 | -13.1068 | -45.276 | 2025-05-30 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 382.8 |
| 1bacb2f7-2bf7-3875-b698-51d10dd7227e | -11.6878 | -46.2231 | 2025-05-30 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| f913ad8c-49c8-365b-beb9-8d2c58228b08 | -13.1068 | -45.276 | 2025-05-30 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 355.6 |
| d8cf3096-a0f2-3351-91f2-4e6aa2139088 | -6.9804 | -42.7854 | 2025-05-30 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 227.0 |
| e3f47ec5-ed18-3638-80bf-5cad7a3df3c2 | -13.0874 | -45.2791 | 2025-05-30 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 168.0 |


[Clique aqui para ver as próximas entradas](README15.md)
