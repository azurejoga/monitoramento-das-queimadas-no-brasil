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
| 9d0389c7-0f84-39ce-8e76-fb45c1c9a189 | -3.1977 | -51.026501 | 2026-09-27 01:15:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 155bed6e-f99a-3a68-a35e-c7e0316f02a3 | -4.5011 | -54.9505 | 2026-09-27 01:15:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e0f8d35-8a88-3d1b-a166-95f651b24821 | -12.0475 | -51.419899 | 2026-09-27 01:15:00 | METOP-C | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e8e711c7-81f6-3e3d-b948-93fc7854b8ca | -6.0919 | -57.617699 | 2026-09-27 01:15:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63968c1c-5c5a-3e63-b68f-8e4fd2f64cd8 | -11.0181 | -54.040501 | 2026-09-27 01:15:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27d78fc5-0ae9-3cef-80ce-1de312eb7058 | -3.0052 | -54.200699 | 2026-09-27 01:15:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6755dfc7-3af5-30e7-86d3-1436cb67c9b7 | -12.0441 | -50.617401 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 444887da-cb3e-36b8-9a4a-89ac2fee8be8 | -9.6161 | -55.103298 | 2026-09-27 01:15:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ed92fe6-9d10-31af-9c8b-7f1ba6b91866 | -2.7891 | -57.700901 | 2026-09-27 01:15:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d35486ad-b0b0-318c-be74-918ae50251a5 | -2.0596 | -56.865601 | 2026-09-27 01:15:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ace71a7-7cef-3b30-a007-66eaf7494ede | -12.3013 | -50.323898 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 09553ac0-df6c-3ac2-a9ed-9f1b4a63de57 | -6.0935 | -57.6245 | 2026-09-27 01:15:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 821d4f04-f925-3a89-a06c-946a7b17fec5 | -4.5089 | -54.939602 | 2026-09-27 01:15:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ebf7aa1-98ba-3fb5-8e42-185a45105b7c | -1.0563 | -53.568802 | 2026-09-27 01:15:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ec063e5-c137-3452-93ce-344a09ad14c6 | -12.2915 | -50.3671 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 44ca4452-8f25-31e9-95b0-06f7c67e47fa | -2.9475 | -57.716702 | 2026-09-27 01:15:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89b3deb7-661e-3cf0-99aa-ee5ca20a4dd3 | 2.6474 | -60.165401 | 2026-09-27 01:15:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b59fee19-6929-3509-8d83-98626ab1837f | -10.8173 | -60.709301 | 2026-09-27 01:15:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7822a8db-dfa5-3328-aeff-5e6186aeb231 | -12.6619 | -47.322701 | 2026-09-27 01:15:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a72f0c3-a727-3da6-af47-60f4f5d10181 | -5.1718 | -56.007599 | 2026-09-27 01:15:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc4e3c96-cc27-3090-93aa-501695949529 | -3.0753 | -58.405399 | 2026-09-27 01:15:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ba85b03-1cf7-310f-a667-dd1a80d26935 | -6.0967 | -57.638302 | 2026-09-27 01:15:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00e517be-1f78-3f33-8a49-dc1e77d5768c | -2.6683 | -56.466 | 2026-09-27 01:15:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba95067d-7e65-31da-816c-7b0affd70cbc | -1.7461 | -55.249001 | 2026-09-27 01:15:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cef1c1c2-c4e9-319a-9da0-4654c1ef8fcf | -14.1124 | -46.331501 | 2026-09-27 01:15:00 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 443eeeec-904f-3467-a86d-3f3d7e6625f0 | -11.779 | -51.005402 | 2026-09-27 01:15:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 62b19d49-cf2e-3c61-9b4b-086b38cbcd4a | -1.6822 | -55.9048 | 2026-09-27 01:15:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecf97e19-bce7-335c-a17c-e34e8c9faaa5 | -3.0728 | -54.4007 | 2026-09-27 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9389829f-7cab-3600-9ee6-12417612e444 | 1.6605 | -55.967899 | 2026-09-27 01:15:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff055997-4289-3f20-a71d-1d11427eba42 | -3.4964 | -53.270401 | 2026-09-27 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fa8d3b0-fe86-3a64-8268-57788d01ed06 | -11.9508 | -50.5755 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 90057b00-75b3-31b0-84db-d9a4f6279ffe | -13.3426 | -51.342098 | 2026-09-27 01:15:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 54aaa6f9-b36e-3bca-98ee-13d358e0a502 | -6.0642 | -57.8116 | 2026-09-27 01:15:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cd217fa-8356-3ae9-b2f7-7427d09a1a59 | -2.6549 | -56.4529 | 2026-09-27 01:15:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b499330-8d64-3aea-9434-53cc1dbb0528 | -3.2299 | -54.324001 | 2026-09-27 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d399648-b604-3f0d-a1d4-4d6cb9db55c1 | -2.6548 | -56.5411 | 2026-09-27 01:15:00 | METOP-C | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 21e43cf8-f45f-3c22-9e5f-5a09ff1e6137 | -12.2949 | -50.298302 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2f7c61cb-493c-3d2b-8799-7d3506558dc7 | -10.8113 | -60.729099 | 2026-09-27 01:15:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6473164c-a2da-3b65-85b2-f3593f39bb38 | -2.6665 | -56.458401 | 2026-09-27 01:15:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d4f3db3-422d-39c9-b14e-56a0ea908c01 | -1.6065 | -54.826099 | 2026-09-27 01:15:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d0cea81-68a4-3353-9711-da694743a58d | -12.8934 | -61.725399 | 2026-09-27 01:15:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a5018584-693d-3405-9696-dbc7b06423da | -6.0853 | -57.633598 | 2026-09-27 01:15:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d84499a3-22d1-3fdf-af92-f8a081a55fe2 | -11.0422 | -51.328201 | 2026-09-27 01:15:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a2811ba5-4234-365b-af25-572e340a246e | -3.0075 | -54.210499 | 2026-09-27 01:15:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ecda993-e510-330d-a73a-48e83b71ad1f | -1.1237 | -57.278702 | 2026-09-27 01:15:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae865f27-668e-3568-9b44-6d3253bf7fd4 | -11.0201 | -54.048698 | 2026-09-27 01:15:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5381c1d7-885e-3748-b897-93eb9bdfefdd | 2.6344 | -60.1768 | 2026-09-27 01:15:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b73b9deb-7b84-3d32-ab54-c9370581af16 | -6.1362 | -53.061298 | 2026-09-27 01:15:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bccaddea-79b0-38f7-80de-aa1064221a86 | -4.2622 | -51.0541 | 2026-09-27 01:15:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68191d50-4abe-32c3-a983-30bb3ed71da0 | -14.415 | -52.807201 | 2026-09-27 01:15:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3c90ae3b-a411-3af4-928f-c17803ce8f12 | -7.498 | -55.0112 | 2026-09-27 01:15:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4426d161-3cac-3226-845f-57b8a96b9e48 | -10.8192 | -60.718102 | 2026-09-27 01:15:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cbdbdd4d-3d94-3aee-ad2c-01fa471fb928 | -3.703 | -51.377102 | 2026-09-27 01:15:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d575a2b7-12df-3b0a-87e7-c83d95692115 | -12.0448 | -51.408901 | 2026-09-27 01:15:00 | METOP-C | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 103fee12-ec6c-3365-a2ae-0f3994f0aca3 | -4.5364 | -54.969398 | 2026-09-27 01:15:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 363417d3-4868-3b70-b457-66d5c5cd7215 | -10.2471 | -59.133701 | 2026-09-27 01:15:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b3264334-9eb9-3e83-be08-94c4478a7cc8 | -6.0869 | -57.640499 | 2026-09-27 01:15:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45adaaf4-81b0-3596-963c-6ed416d17eb1 | -6.7246 | -52.976799 | 2026-09-27 01:15:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc3f4c52-6f1e-3360-8bcf-df055006cbc0 | -11.782 | -51.0172 | 2026-09-27 01:15:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e2f9e446-6a4d-3626-b0a1-def230ef9814 | -17.046301 | -56.569698 | 2026-09-27 01:15:00 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6e16b297-656d-3426-89d5-a593be2bd798 | -12.6716 | -47.320099 | 2026-09-27 01:15:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 195b53c3-a182-3337-a1b0-6345b40521ef | -11.2746 | -54.425201 | 2026-09-27 01:15:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6394f0f6-d752-3038-aa32-2084e2cef27d | -2.0006 | -47.0033 | 2026-09-27 01:15:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae3b587f-8006-32df-ab06-07d16a2be987 | -10.4172 | -53.8172 | 2026-09-27 01:15:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ef776cea-f578-357c-9286-3ced93970801 | -8.0284 | -54.8955 | 2026-09-27 01:15:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34a36193-f66e-362e-a69a-66dbbd56dd3b | -3.9622 | -59.3489 | 2026-09-27 01:15:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0f7391df-2ca7-39a8-94d3-fac2f6a31bc9 | -1.6186 | -54.922401 | 2026-09-27 01:15:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 259c837c-0f6a-333e-8649-377bad757e20 | -11.2765 | -54.432999 | 2026-09-27 01:15:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2262b1e5-bf23-31a7-bd34-ea78c7beeec6 | -12.2884 | -50.313599 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a2fe4629-57bf-3935-a362-d2bd9150bb4f | -3.9767 | -50.723 | 2026-09-27 01:15:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ec4204b-7277-3042-b317-a946a6da94fd | -11.0394 | -51.3167 | 2026-09-27 01:15:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f9432688-13d8-3319-a403-0154aa2c761e | -12.0344 | -50.6199 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5eee7b5a-1210-3c09-91e3-1495f5067845 | -12.2947 | -50.379799 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aca3b3fe-b67d-3f28-a5fd-edd1417ea411 | -6.0837 | -57.626701 | 2026-09-27 01:15:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9ac56f2-ee7d-30e2-820c-eb10ba9188ab | -11.0546 | -54.194 | 2026-09-27 01:15:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80e7712b-551d-3646-b1db-caf5a41ad5f2 | 2.6458 | -60.172199 | 2026-09-27 01:15:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 742f0ac0-e4a9-3666-80fd-84e4af6c8a3d | -3.7201 | -54.655399 | 2026-09-27 01:15:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 538d47ff-fa00-3670-8d93-62a40262f2cf | -12.2981 | -50.3111 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3bb412ab-c57a-3b64-a0a0-82d5a569daac | -10.2552 | -59.124001 | 2026-09-27 01:15:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95e0f818-c8aa-3ba9-bc78-5f7d51253e1d | -12.6759 | -47.297401 | 2026-09-27 01:15:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e174d252-9004-36a1-9e38-bfaa7f22b767 | -11.9445 | -50.550499 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f8b5c9a0-799e-3647-bb08-bb9e38cdd16f | -20.837099 | -57.714199 | 2026-09-27 01:15:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ada7a043-b6fe-33bf-916c-fd98665a24b1 | -11.2801 | -54.448601 | 2026-09-27 01:15:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7959803f-57c2-3b3f-909f-6029178a6b92 | -4.5404 | -54.9865 | 2026-09-27 01:15:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 022d61aa-d8bf-3cd5-9b01-a3282a741d14 | -11.9573 | -50.560501 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6db804e2-7ddf-3d3d-8a34-f730a7e0294e | -11.9951 | -57.602299 | 2026-09-27 01:15:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d35d843-3fde-31b0-b259-20bd1ffb3b32 | -10.2454 | -59.126202 | 2026-09-27 01:15:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5cc8a125-f797-3977-91c1-9411bca3d328 | -11.9414 | -50.537998 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c93b4628-6e64-345e-a910-6dd16a3b0c44 | 2.89 | -60.276901 | 2026-09-27 01:15:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5286ea5a-1e3d-3dff-b654-4fc5da17206b | -1.6163 | -54.823799 | 2026-09-27 01:15:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fb51221-fb81-39c8-b31b-53bac9e9ab98 | -3.0769 | -58.4123 | 2026-09-27 01:15:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f2f8ab1-956b-3ee8-8cb0-6f2f272e7320 | -3.9728 | -50.706799 | 2026-09-27 01:15:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f10f699a-8b2e-3ad0-9a9f-f27326b315bc | -10.8132 | -60.737999 | 2026-09-27 01:15:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| efe926c0-bc6e-33ec-afd8-1872f2353271 | -5.1602 | -56.0023 | 2026-09-27 01:15:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df474c12-764d-3f94-bf39-489f39d4c51c | -3.2016 | -51.0424 | 2026-09-27 01:15:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9108d7f0-17c6-3f32-88a4-5bed052b0aae | -6.0838 | -57.807201 | 2026-09-27 01:15:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b00ea8e-00ad-3f35-ab07-9ef9c8f575d8 | -7.6855 | -54.755402 | 2026-09-27 01:15:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69486da4-d7d3-34ac-973e-7086dbcd70d2 | -6.0854 | -57.814098 | 2026-09-27 01:15:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a244cd53-fb92-3a25-9338-1696844f21ee | -12.041 | -50.605 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aad04818-84eb-347b-901a-8f9b7cea9c9b | -8.9038 | -61.481602 | 2026-09-27 01:15:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
