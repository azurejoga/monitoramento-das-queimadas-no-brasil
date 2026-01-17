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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3eeb9cf-31e5-33af-9469-8c817b1fcc7e | -13.95273 | -48.50672 | 2026-01-17 04:27:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7177c5c0-6618-3452-8fa1-ae127ebecfa4 | -11.28925 | -48.73288 | 2026-01-17 04:27:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ae0dccb-8d87-3558-96e9-5307116ed4a9 | -14.75315 | -45.91663 | 2026-01-17 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6108760d-2119-32dc-8592-b0360d7953f6 | -12.65416 | -46.75906 | 2026-01-17 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4e2d178c-e54e-327d-97ce-e64786544a94 | -12.91816 | -49.48418 | 2026-01-17 04:27:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3dc9e99a-65e9-3d71-bc53-2719975a9e8d | -14.7738 | -45.93856 | 2026-01-17 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4dbaa05f-ae53-3f70-9454-aa96a8f82d6b | -12.65806 | -46.75606 | 2026-01-17 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ff0a2410-c89d-366e-9143-666299a4cc6a | -12.22235 | -49.64067 | 2026-01-17 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e04f4211-0897-3569-afdd-acc2b7150c0f | -17.27928 | -42.64849 | 2026-01-17 04:27:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e81ef638-8feb-3d0b-a6a7-498779be3c00 | -15.01625 | -48.67088 | 2026-01-17 04:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 31c3b5c4-e15d-3b66-b498-e069f47122c9 | -13.74485 | -43.66229 | 2026-01-17 04:27:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd5d1a3d-745f-3be5-b320-4c2e572aaf37 | -16.31939 | -57.56256 | 2026-01-17 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| e4d8768e-ba5d-3085-a1bc-a53d7419b3b3 | -15.0534 | -46.85217 | 2026-01-17 04:27:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16c148e0-c434-3d27-9f07-2c5d91c6ee75 | -12.65083 | -46.75851 | 2026-01-17 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fe4b447-9867-3af4-920e-5c046b177cfe | -16.58537 | -57.80957 | 2026-01-17 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ef838797-4336-3ec9-91ee-93e69b6e196e | -16.31166 | -57.56257 | 2026-01-17 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 4ab7a0f1-3c07-3b88-962a-b69e0db74f57 | -16.31851 | -57.5667 | 2026-01-17 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1008050e-e009-3aba-87a7-dffb611091c7 | -18.68569 | -41.87091 | 2026-01-17 04:27:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 47fc43d8-48b4-3458-8475-feccd135edb3 | -14.71832 | -53.97115 | 2026-01-17 04:27:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ca3e0931-9fc5-32cc-a828-50a5489f3f87 | -12.35154 | -52.48015 | 2026-01-17 04:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df9fb99f-ed51-35fe-87b7-e5c08f253468 | -14.71463 | -53.96535 | 2026-01-17 04:27:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ae9e9db9-0f7e-3133-a80e-34a361179d0f | -12.65693 | -46.76317 | 2026-01-17 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 45426bcb-3303-347f-a40f-bb336ad481b6 | -15.25795 | -42.98491 | 2026-01-17 04:27:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2706ed2e-7ea6-3555-b38a-5d6235843b48 | -14.77659 | -45.94273 | 2026-01-17 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f516aa56-7d61-3812-9775-1226dda93815 | -14.48349 | -44.33246 | 2026-01-17 04:27:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef5f3790-0923-395f-8dcd-8695a7925048 | -13.69798 | -45.47406 | 2026-01-17 04:27:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f537c935-a2ea-3b42-b781-386b6ca7817e | -16.58628 | -57.80535 | 2026-01-17 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4afd281f-c07a-3902-a209-e703664e6166 | -12.08578 | -43.76528 | 2026-01-17 04:27:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f89e521b-3c77-354d-84af-67cc24fb63b3 | -14.78329 | -45.94382 | 2026-01-17 04:27:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3ef38809-7cd4-3a72-8a78-ab2536d9fa47 | -16.59048 | -57.80746 | 2026-01-17 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 913c8a4d-9c9a-3298-8352-5aafbdc13c93 | -16.32291 | -57.5651 | 2026-01-17 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ec192260-cf1d-3e78-b542-af9e30bf7a7d | -17.60957 | -46.65545 | 2026-01-17 04:27:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e91c3c4d-6e0c-3748-a58c-6464042c85ff | -11.80488 | -45.36128 | 2026-01-17 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4706b3a-2c95-3591-89df-79b6766582e1 | -14.77101 | -45.93439 | 2026-01-17 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1130ec6a-1e3d-3561-a6fe-a56ef34c9ac0 | -13.28389 | -53.96336 | 2026-01-17 04:27:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5e7ca2f-ac4a-3727-8a9d-68c62b237aa6 | -11.80099 | -45.3643 | 2026-01-17 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1c186d4-5a0a-3439-956f-82577f0fcfcc | -12.65636 | -46.76672 | 2026-01-17 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b2c7c4e-1eb5-3993-9373-69b13d53e81d | -17.61014 | -46.65178 | 2026-01-17 04:27:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 92dd922e-1ca8-3386-8fea-5a356897b4c7 | -14.74925 | -45.91971 | 2026-01-17 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1d3e8c1-7125-3ec1-a18e-bcf5a285ad22 | -13.70134 | -45.47461 | 2026-01-17 04:27:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dce3d671-5ecb-3a8b-b4cb-0236e4f85390 | -13.55388 | -53.25166 | 2026-01-17 04:27:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b328411d-8c80-3f4b-aa3c-2ba8831e8372 | -14.76543 | -45.92607 | 2026-01-17 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| deddf7b5-2282-3934-a59a-d66f756b180a | -16.58395 | -57.81028 | 2026-01-17 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7c9e5c9e-eea4-3677-b78b-b36095248020 | -15.44272 | -56.33048 | 2026-01-17 04:27:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2baaf34c-f075-311f-adcd-123582bc378c | -11.81378 | -45.34808 | 2026-01-17 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 975108bc-5900-398c-94c1-2963a00fd934 | -13.50144 | -46.70578 | 2026-01-17 04:27:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8aa6994b-d909-3a8e-a4e4-b265aa2e736f | -14.71556 | -53.96047 | 2026-01-17 04:27:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1fe9e73-24c9-3167-a311-9eb0a44c26f6 | -17.60901 | -46.65911 | 2026-01-17 04:27:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b594e1c-c29d-3f60-8b11-ab32af124cd7 | -12.33413 | -52.47683 | 2026-01-17 04:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f88645f-ce13-3129-b560-774b06b065a2 | -13.502 | -46.70223 | 2026-01-17 04:27:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 704bbb8f-d46e-3972-8b12-f1b368cb80ff | -15.89188 | -43.4547 | 2026-01-17 04:27:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4bbe772d-e02e-314b-9f50-e13b0c09b32b | -16.58483 | -57.80603 | 2026-01-17 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 063ab359-26b8-32e2-b87c-4a17f120c224 | -13.94178 | -48.50875 | 2026-01-17 04:27:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88934a30-87c0-3579-b48f-cdb8b38c9ce0 | -14.76878 | -45.92661 | 2026-01-17 04:27:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91604ca4-9211-3a8a-8b3d-f3510f9a5d6f | -11.53245 | -47.69306 | 2026-01-17 04:27:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2db5819d-2f62-3b30-83fa-25cce63203fc | -12.08228 | -43.76471 | 2026-01-17 04:27:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e48a6575-e335-3b4b-b290-34fa726c0ca7 | -12.49693 | -46.34437 | 2026-01-17 04:27:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc9d64a4-3a3a-36f0-98d8-004d25552b6b | -14.77715 | -45.93911 | 2026-01-17 04:27:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d55f382-a566-36c8-abc8-38b3e291a8db | -15.25864 | -42.98011 | 2026-01-17 04:27:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 034e2439-3957-3d0c-afa0-43f8d9a640c0 | -11.40969 | -49.17003 | 2026-01-17 04:27:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1e09109-2a93-3e4e-b7c3-908da86c1f8b | -14.76264 | -45.92189 | 2026-01-17 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61f20292-b496-3f80-b2fd-d3a49c0764b4 | -11.80991 | -45.37304 | 2026-01-17 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51a12f58-cbe1-330f-bb6c-3488e5f37f38 | -12.97705 | -48.83587 | 2026-01-17 04:27:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 90fafdc8-d0ca-38fe-8841-e971dd8f7326 | -11.53183 | -47.69679 | 2026-01-17 04:27:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 597347c0-01f7-32b9-81c9-812324b946ed | -12.65473 | -46.75551 | 2026-01-17 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 78e75fac-1aba-3612-a7e6-503e6b880749 | -12.66225 | -46.76366 | 2026-01-17 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1584af41-e57d-3ffd-82ec-607b1cd7718d | -16.31728 | -57.56384 | 2026-01-17 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 8a95a80b-bd10-3f2c-8b95-9f2853e3cb1d | -11.81825 | -45.36343 | 2026-01-17 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71c2fe70-30ed-3d5f-860c-9c22a43716e9 | -12.65026 | -46.76206 | 2026-01-17 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6298146c-de60-33b6-9360-beba534a1321 | -14.77938 | -45.94689 | 2026-01-17 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0e576cdc-f853-3b01-8a36-54dd89117623 | -14.78273 | -45.94743 | 2026-01-17 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3ca6b33d-4ab4-3290-8ced-2812a6f63ba8 | -15.43744 | -56.32927 | 2026-01-17 04:27:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2456f7e5-032c-32f7-be68-e6c92c97927b | -13.54938 | -53.25087 | 2026-01-17 04:27:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c3239177-7587-3e64-bf0f-018ae067c448 | -12.65834 | -46.76666 | 2026-01-17 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 947b83a8-8c59-3574-b6fc-0fee5a44476e | -15.63442 | -48.54621 | 2026-01-17 04:27:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4973d136-6faf-31c5-bb39-110fa843138c | -14.76822 | -45.93023 | 2026-01-17 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fd14405-fb2f-3aaf-8972-16b542fa9634 | -14.71925 | -53.96622 | 2026-01-17 04:27:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8c9b2c15-211e-324d-be6d-56f206e6b100 | -11.93665 | -44.61528 | 2026-01-17 04:27:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10d929b1-ed6f-35c9-9300-1415f0a1b318 | -12.50026 | -46.34491 | 2026-01-17 04:27:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78680a05-83ba-30ec-9a35-bc119297b90a | -15.02031 | -48.66766 | 2026-01-17 04:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 911ba44a-645c-35cf-9054-c4f9b2c07c15 | -17.27535 | -42.64783 | 2026-01-17 04:27:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f4a806e-77c3-3b94-9a0c-04d0dccdda00 | -11.88427 | -45.70118 | 2026-01-17 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4cbacafd-1d4f-3b5f-af91-54c13ad4b76a | -14.78608 | -45.94798 | 2026-01-17 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8f6a3d5e-1817-342e-8802-1445aac32d4d | -13.95147 | -48.51432 | 2026-01-17 04:27:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f38eff7-87b3-3a4b-94f3-485915ea7d72 | -11.80154 | -45.36074 | 2026-01-17 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6eb3d31b-d414-325a-b246-12a85f040cd6 | -16.31378 | -57.56128 | 2026-01-17 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 4abcdd43-51ef-3ee4-b1ab-46ef5eed19b2 | -12.6575 | -46.75962 | 2026-01-17 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6f06816c-5450-38c8-88b5-496b5caa2dba | -15.01968 | -48.67145 | 2026-01-17 04:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e52f92fc-6552-3d23-8846-d9a26093f8ed | -14.75092 | -45.90885 | 2026-01-17 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c4e7fb6c-b849-32d6-b907-7e74493f561b | -12.22828 | -49.62819 | 2026-01-17 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5dbbad4a-910b-3851-84dd-b076eabb2f50 | -14.75036 | -45.91246 | 2026-01-17 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5416a5b-d105-3991-9026-07b65003d165 | -12.84946 | -49.86429 | 2026-01-17 04:27:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebaa05ca-7c0f-32ca-bd70-762c87ba5a0b | -11.59539 | -46.77094 | 2026-01-17 04:27:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79c5f67e-a9bb-3106-911c-e8f73cd834b5 | -11.7971 | -45.36733 | 2026-01-17 04:27:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be4405dd-1745-38d7-8c3f-dac09545d1f4 | -14.77994 | -45.94328 | 2026-01-17 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e6663ce3-cc31-352b-9662-cea2a4a0a59c | -13.94803 | -48.51372 | 2026-01-17 04:27:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 335252e0-09d0-3d65-9ef9-da194e589b16 | -11.2857 | -48.73227 | 2026-01-17 04:27:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68da96cb-3d74-355b-aba3-da4a7358b6f2 | -13.27916 | -53.96246 | 2026-01-17 04:27:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b8ec632-53d9-3599-8613-9bacb293306e | -15.98786 | -46.58694 | 2026-01-17 04:27:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7aab6d94-b551-3e43-8bbe-085776b6d113 | -15.43676 | -56.33262 | 2026-01-17 04:27:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README7.md)
