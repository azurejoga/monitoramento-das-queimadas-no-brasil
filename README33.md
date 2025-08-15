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
| f2044e2b-6c15-33c2-ade5-a8f881eb223a | -11.80859 | -44.26363 | 2025-08-15 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de83b208-7e8f-349c-95f9-6d5466a246fd | -13.38256 | -44.30966 | 2025-08-15 04:29:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0464f7f-6a36-33fc-b666-ab3f3ae84a2d | -13.12997 | -57.16505 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f228b30e-3981-3a7d-8e04-a11ba3762cd7 | -15.88825 | -50.17733 | 2025-08-15 04:29:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 66b3fee7-1a2d-370f-88b7-485fddd61269 | -9.21662 | -59.66127 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f510cf8-1a6d-32c7-a821-54601cbb2b1b | -9.49792 | -60.54352 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 140f1e34-9927-3a4e-a9c9-8d9d79904772 | -12.76133 | -44.41487 | 2025-08-15 04:29:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 82584eb6-2867-3f86-8020-c61871e278dc | -9.17514 | -59.69551 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ab546a82-4ee5-39cf-8e18-3328669154ed | -9.16293 | -59.68689 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad53f988-d4fe-3557-8844-44aa0d72252e | -12.58249 | -46.95789 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 14025354-cc46-35f7-89c0-667245a59732 | -9.15937 | -59.69155 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd29315f-4caa-3642-b296-b4a76e63f913 | -9.50027 | -60.51828 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9be12df5-df57-36d4-9681-fcea11147d0e | -9.20452 | -59.65219 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6e2ddb32-ba44-3ae4-be80-b9db6f833b43 | -12.50091 | -47.02111 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6555c8a3-0b1c-311a-a3d4-541c3d758ac1 | -10.96592 | -49.57056 | 2025-08-15 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 384392b3-6de8-3654-a27b-73181f920130 | -9.39146 | -60.54199 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a5c2b677-8708-3091-b968-b96737cc79b9 | -13.32302 | -45.22771 | 2025-08-15 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f8ea77a-3370-3278-96a3-0237b3e4182f | -13.48107 | -56.66401 | 2025-08-15 04:29:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c1c7a259-91ea-3fce-8a50-a6c16a3dc9ae | -9.50323 | -60.51668 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6287de6d-d009-351c-935b-78c965fb0b1b | -12.42582 | -48.70095 | 2025-08-15 04:29:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad336ecd-2e12-362b-845b-7221f3fe018c | -11.94481 | -58.76477 | 2025-08-15 04:29:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e0db265-f65c-36af-9620-0a45a63b1c16 | -11.35571 | -55.4162 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 44051a91-285f-3cc6-ad6a-e8c41e2a9901 | -9.93663 | -60.47911 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7dff94ef-7c13-3268-8eee-351c4b2a152c | -9.16722 | -59.68686 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 71c79308-972d-3a9e-94b2-2fce88be6131 | -9.50173 | -60.5467 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6473c6c3-bb8f-3cc9-bfb6-e21086acaa69 | -12.58471 | -46.94368 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f05332aa-0249-37bf-90cd-e5b358ac859d | -13.88604 | -45.55916 | 2025-08-15 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad579828-87bb-3789-bf6e-844cc97dae2a | -9.17436 | -59.66433 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8cd2a963-0609-3261-89d2-752f3a6518fa | -9.15178 | -59.65879 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35afabb7-8790-3932-b470-aa5b46183878 | -11.91876 | -43.44257 | 2025-08-15 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ba29a86-4067-3663-9f91-89d8f51762dc | -13.32712 | -45.22427 | 2025-08-15 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bdadc7e9-22b7-361f-9902-ac71daa9a6a9 | -12.67971 | -44.95515 | 2025-08-15 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7119a111-0be0-3222-b763-078c87956c61 | -13.46641 | -43.75407 | 2025-08-15 04:29:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2e88430f-d8f0-373c-aade-be0a91f2610d | -9.49753 | -60.53166 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6e915071-8464-3dac-be74-3a7b57cc7b80 | -15.39544 | -55.7781 | 2025-08-15 04:29:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6cb3d3e3-d565-393d-a741-8f31888674b3 | -10.00958 | -58.43096 | 2025-08-15 04:29:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1533ee48-16a2-3836-93cf-f8b5c0537d55 | -15.39149 | -46.59015 | 2025-08-15 04:29:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e6e1611-4beb-37d6-93fb-8351d2837efe | -13.04678 | -56.8406 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d9ac2d5c-a5af-3058-950d-c74299d86804 | -13.11858 | -57.16632 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82a1a8aa-45a2-39fe-8b41-5b7b29ef250c | -9.18537 | -59.67893 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a120b8a-c0f2-3faa-bb4f-f2abea685102 | -13.58075 | -46.96668 | 2025-08-15 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 836c744f-3dac-301d-9681-680acca8311d | -15.85273 | -48.12199 | 2025-08-15 04:29:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b1d9faba-ce05-3075-ae3f-e67f535a2349 | -12.68265 | -44.95969 | 2025-08-15 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bc40ead-0f55-3ed1-acb8-9a2ebc7132f5 | -15.93141 | -48.15676 | 2025-08-15 04:29:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4e571063-0c93-3cf7-a28a-57711b77abf4 | -9.15381 | -59.68433 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ca65405d-e4a5-3038-8de9-c3db554fd8b2 | -11.35215 | -55.41037 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b5ad3f5-a7c0-35f4-9451-8bb8d0e2ed30 | -14.02553 | -52.03923 | 2025-08-15 04:29:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43808b63-060d-33d5-a67b-0cda2d4ae99a | -9.16054 | -59.68548 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f8a1c82-5560-33e0-a52f-f19c06cea89d | -13.32419 | -45.21975 | 2025-08-15 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6286c4b2-0f61-30c8-b2c5-4a04b8967d3f | -13.116 | -57.15109 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8802cd4-72f1-34f1-b346-7e7e5b031458 | -9.15266 | -59.69031 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4cbb9c59-9979-3749-abbf-7ddaa480afba | -9.51005 | -60.5416 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5eb57fe1-0ac2-3ec9-9c98-e89b02e4e26e | -11.9387 | -58.76386 | 2025-08-15 04:29:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 81f6ad31-7be6-38b4-8075-98f2e602fc95 | -9.39477 | -60.5497 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9bd58004-9a8b-37d8-8e40-bda75009233d | -11.92325 | -43.43827 | 2025-08-15 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ea2d0af-2d1d-37a0-8004-919d8ce0c6d4 | -13.87067 | -43.49397 | 2025-08-15 04:29:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5031cf53-0ba8-33a3-a7c5-f75ec3277dd3 | -9.50618 | -60.53848 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ff509171-d920-3ef4-9a37-a51a86f677c4 | -11.35493 | -55.42262 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 357eef04-0fb8-3ae6-ac82-ce335f4ab863 | -14.06899 | -46.32177 | 2025-08-15 04:29:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ef4be53-6fcb-3cb7-9f8b-c68e80bc6aa9 | -10.35625 | -50.80726 | 2025-08-15 04:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b33b0f33-bcb1-3b29-b315-ee8b6ee7dac2 | -12.78917 | -45.95779 | 2025-08-15 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d523789-b431-3203-a25e-b486cef9f428 | -12.49758 | -47.02057 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c8d9839-d727-3225-aedf-27c4ca5e1e27 | -13.1262 | -46.85057 | 2025-08-15 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f23f865-da04-303d-b5a8-28d872f9c1d9 | -11.35 | -55.42168 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 97521f74-109d-3664-bb4c-e6b9fdd6ef90 | -9.93388 | -60.48455 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3b76f3b-6d14-3dc1-8558-3d58e6acdb77 | -11.54628 | -47.2657 | 2025-08-15 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e70145e5-db95-3c4f-9dbc-d8c9ae1dd545 | -10.35998 | -50.80791 | 2025-08-15 04:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 579917fd-cd08-3ddb-8986-2baf8ea9168c | -14.9045 | -45.18734 | 2025-08-15 04:29:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb7adebc-95c0-3f05-8d64-d196d925c26b | -14.24226 | -44.58426 | 2025-08-15 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 46d33b4f-fc82-3043-b903-d6821d004da8 | -12.68324 | -44.95569 | 2025-08-15 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09e8d2ea-d0d9-3bc6-b8e7-509eb530b2b5 | -9.17314 | -59.67046 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1647065a-4461-3adf-a1f7-26a52582c1d9 | -12.5836 | -46.95079 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5f36d7f7-d22e-3d4b-bf80-ee2dd8a8ae83 | -9.39014 | -60.54866 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 27a22abb-35c9-32b9-bc1e-e3a4e2c207d0 | -13.27921 | -50.83103 | 2025-08-15 04:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5efbf90-ca34-3f4d-a55e-d793b1e0557d | -9.1562 | -59.68574 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 318a0894-2530-32be-8b4d-40a7edbf2b62 | -12.77383 | -45.94397 | 2025-08-15 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc960bd6-3436-30bf-a8f1-46fe464ebef5 | -14.23797 | -44.58807 | 2025-08-15 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5744f078-6179-3028-a7c5-cbd47a1837c0 | -13.33062 | -45.22482 | 2025-08-15 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5646fe50-6014-3330-9afb-216418b022bb | -15.89572 | -50.17478 | 2025-08-15 04:29:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 316baefa-ec26-3f02-ac8d-e1f80cb87e49 | -14.06504 | -46.30196 | 2025-08-15 04:29:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af40282e-b2bd-38a0-aec8-666ae0cdd02b | -13.31951 | -45.22717 | 2025-08-15 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6ba0d42b-d5f9-3f47-b520-4812422c2775 | -11.36063 | -55.41726 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c9b9d091-01b6-346f-be48-b4cfa03cc6b6 | -13.316 | -45.22663 | 2025-08-15 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2da125a7-69cb-3e2d-9717-d1553ae5afa3 | -16.37645 | -50.90114 | 2025-08-15 04:29:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a380227-2dc3-36b8-b13e-51ecf0f9fce7 | -13.11322 | -57.1652 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ef3e85f-2af2-3876-9c8b-68578be797af | -15.39546 | -46.58693 | 2025-08-15 04:29:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e26e93be-cd2d-35ed-9a35-90b1201f4e52 | -9.17197 | -59.67641 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f7e7f799-2c52-3c6d-9f42-ec321f2c019c | -9.18894 | -59.66082 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 548f948b-ab9c-3e85-924d-aa2708c497a8 | -9.16168 | -59.67952 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 619a98af-8fa7-353e-bf04-64d3ed770ac1 | -12.15227 | -43.2111 | 2025-08-15 04:29:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 102b98c5-b3b6-333c-8eb4-6188f6f882dd | -13.12204 | -57.14869 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 449d56a3-5c43-3a74-afce-477aa8b1f76d | -14.73854 | -46.29706 | 2025-08-15 04:29:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa6870ba-1e0f-38f3-9fb8-a23228d2e9aa | -9.15383 | -59.69766 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f7c5c684-77a6-394e-8559-3612db221b2d | -13.10925 | -57.15708 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5de3e8a4-1fc6-30c1-8b1f-5fa27353d2aa | -9.17631 | -59.6896 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 03ee3f16-7050-3770-9f63-42a8ab5b0b2c | -11.31434 | -55.20076 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5976a02a-4102-33a4-8abe-6708342d79fa | -9.14945 | -59.67084 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60426734-805e-380f-8f34-953ba749377d | -14.79197 | -42.72638 | 2025-08-15 04:29:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a6248420-f3fc-3bde-96eb-684b49b68ca6 | -9.50192 | -60.5233 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 65eaa224-7acb-3b30-85c3-778be8ef34de | -11.80923 | -44.26637 | 2025-08-15 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README34.md)
