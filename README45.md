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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14a75113-cb88-3a79-a95e-5acd84aba5d7 | -15.83541 | -48.96496 | 2025-09-10 04:17:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e910a780-f4b1-3b6c-8165-b8079c70d86f | -21.43279 | -48.90975 | 2025-09-10 04:17:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25431d78-92c4-36ac-bbb0-db57399b01a4 | -17.24318 | -46.07648 | 2025-09-10 04:17:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd2d3238-6869-35cd-a24a-e3786d1d881e | -10.19145 | -49.58666 | 2025-09-10 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b2bb9339-8611-344b-97ff-870975250ecf | -11.15851 | -45.28297 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd12004d-4a58-3ada-977e-1e9c9d65e711 | -11.94038 | -51.08052 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2a67956-16d2-381c-aec4-f9ca0d597cd7 | -11.44763 | -43.6118 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5df804e2-810d-3459-afd6-6746bedfe08d | -22.0471 | -45.57616 | 2025-09-10 04:17:00 | NOAA-21 | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 93ca624f-d9cd-3ae8-95aa-6cb5a47ff8b2 | -17.2393 | -46.07954 | 2025-09-10 04:17:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 45a13f31-4748-3076-9cad-99e33522e966 | -12.9257 | -54.7785 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7f536e67-d01d-32cb-86fd-9f0163057ad0 | -11.11306 | -48.45853 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 324ba4fc-0084-3307-9e4d-abeaf09d873a | -13.19477 | -45.27638 | 2025-09-10 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0e8be6be-8126-3fab-a4a7-86eb00d1717c | -10.9511 | -46.79987 | 2025-09-10 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b34648e-9050-3ef3-ba6f-534383f33d9d | -10.52127 | -49.78913 | 2025-09-10 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3395519-f678-34b0-8c51-1c3f6d88e01f | -10.19456 | -46.67437 | 2025-09-10 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdf9b689-e9ed-3801-807b-55f809b884d8 | -10.73336 | -48.28958 | 2025-09-10 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bdde3fd5-c705-3256-9aed-e1279e74ec1f | -12.1825 | -53.86396 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6548313b-e181-3128-9452-0566389cdbca | -15.90541 | -50.18639 | 2025-09-10 04:17:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7d1c17be-e485-30ee-bf9c-fe34d952c482 | -13.65157 | -46.97086 | 2025-09-10 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6f119ce-06e5-3a71-aa39-1d10c6060aca | -15.69401 | -49.89956 | 2025-09-10 04:17:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d1ba7dcb-4a13-3836-be64-a90473789cce | -20.93123 | -45.7968 | 2025-09-10 04:17:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 028027c3-c680-30e0-86cb-25a14bf0c9bd | -21.25571 | -45.49345 | 2025-09-10 04:17:00 | NOAA-21 | SANTANA DA VARGEM | MINAS GERAIS | Brasil | 3158300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e6b1ac9a-7d2d-3f76-9a76-88d8c2df7754 | -11.44587 | -43.6009 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df5c41d6-6846-3f35-82f1-8a4d44473d43 | -10.60085 | -43.30455 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c583ba4f-ffc1-355a-bda3-f8f224cafebc | -15.8414 | -41.84652 | 2025-09-10 04:17:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf1e88ba-f3cd-3089-b0b6-5255978d0c4c | -10.14567 | -46.18632 | 2025-09-10 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8512ec69-7913-353a-b853-5728a9d91dd8 | -15.13616 | -52.39622 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ec3c2171-95c8-3653-afbe-497e2d0872b6 | -12.54687 | -49.10309 | 2025-09-10 04:17:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 844e8e87-f6eb-3210-a5b5-dab9ccaf6841 | -23.97444 | -46.47083 | 2025-09-10 04:17:00 | NOAA-21 | SÃO VICENTE | SÃO PAULO | Brasil | 3551009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8029babf-a3c3-37ef-a4e4-6a3e15924f12 | -15.22537 | -44.03917 | 2025-09-10 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 236ccd32-1820-35f5-9cfa-8051ae7b0472 | -23.29686 | -45.47857 | 2025-09-10 04:17:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 93747abc-0c16-317f-a703-e6a199030114 | -16.47395 | -50.66954 | 2025-09-10 04:17:00 | NOAA-21 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac0426f7-dbbf-3853-8cc2-0eabdface994 | -13.64349 | -46.9771 | 2025-09-10 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68cfc001-2954-3a13-8940-5a3f838ac17c | -14.53572 | -42.47728 | 2025-09-10 04:17:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4064c085-9388-36bb-8d5d-fc4ff01ef958 | -22.21958 | -45.87795 | 2025-09-10 04:17:00 | NOAA-21 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e9a1b374-f140-3aef-b728-313f07754cf1 | -9.73722 | -49.11517 | 2025-09-10 04:17:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85d2157b-6155-3bd6-ab26-b184446c56ff | -15.16562 | -47.95267 | 2025-09-10 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37577b04-34b7-3d99-b784-b418986a10e0 | -11.99324 | -47.19488 | 2025-09-10 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa18cf8a-ae66-36ad-8901-d151d0c953b2 | -20.53193 | -47.66498 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e34240a8-f947-34ab-8c49-539e8bf5a4a0 | -13.18985 | -47.25243 | 2025-09-10 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc3f5576-c399-32e5-8624-2fa2ca04644c | -16.5726 | -49.73617 | 2025-09-10 04:17:00 | NOAA-21 | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64ea26f9-2e61-36fc-9d8a-5117e7bb96b2 | -10.39107 | -48.82813 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4cea9aa8-7236-3679-9bfb-9f9bba444309 | -10.56125 | -51.49865 | 2025-09-10 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7d8d4d20-bea2-325e-824f-c02ca837a057 | -11.83247 | -46.74421 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c853896c-bb8a-3d00-872e-56cccf98f00a | -15.81348 | -52.27204 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4046023-812d-38bb-a4d4-399820f95af8 | -23.30083 | -45.47513 | 2025-09-10 04:17:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 736b2232-587b-3820-a032-e1cc6da80a30 | -13.29744 | -51.71882 | 2025-09-10 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 729d4f32-52d6-35db-b715-e28d1036c1b3 | -13.18158 | -47.25912 | 2025-09-10 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ad9e62e9-a277-3427-979e-6e82d9382cb6 | -12.01977 | -45.85563 | 2025-09-10 04:17:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9f2d3c63-327b-308d-bbda-4592cbac3cae | -17.90572 | -43.40483 | 2025-09-10 04:17:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4aedc84-5532-3acd-bfa2-9c64dd5e081f | -12.41441 | -47.50057 | 2025-09-10 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c850670a-7092-3b39-b86b-372fba5900d2 | -12.55003 | -45.28606 | 2025-09-10 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 235fb0be-d5c1-326b-9fef-b0520a515825 | -13.96875 | -48.22252 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5fc38ec7-dd7f-30f1-8b0b-9853c1d036a1 | -13.02071 | -48.03552 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b85c1acb-7216-3c15-b25b-d5ba5411b72a | -14.39008 | -47.33232 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff2dbfe5-b1d6-3b0d-b02b-eb7d396d476d | -23.35611 | -47.20355 | 2025-09-10 04:17:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fd4f7a9c-7a48-3653-ae9c-47bfe3254801 | -13.89907 | -47.98141 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fc690c8-9577-3333-ac54-ee194f68ae5b | -23.4979 | -47.20977 | 2025-09-10 04:17:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 474aa9fd-521d-3f14-aed1-a6f3ca5c2ebd | -13.97627 | -48.23135 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0e865e7b-1a8e-3729-a4ce-2d49ecbab340 | -20.96487 | -43.99625 | 2025-09-10 04:17:00 | NOAA-21 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e8a53427-a0f6-3119-a091-21e31bf087e8 | -11.48637 | -48.5512 | 2025-09-10 04:17:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 856f1f78-4685-3d0e-9870-b57f91d7bb82 | -10.56264 | -51.50029 | 2025-09-10 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2bbe2fef-89e4-393c-a3cb-d3f7819f62e8 | -11.43978 | -43.59631 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc17fbd1-b926-3e31-a9c2-cc5d156c131a | -16.30664 | -45.69358 | 2025-09-10 04:17:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ad25999-211b-3cfc-90e4-95c915e2ec29 | -17.25252 | -46.0818 | 2025-09-10 04:17:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ca4296e-4fdf-3e53-be76-6f04512c4a41 | -15.91401 | -50.18479 | 2025-09-10 04:17:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 56b0cc93-1e7c-338a-9bac-862133a98c75 | -20.37319 | -46.63826 | 2025-09-10 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 604f380c-f154-3c55-9edc-c1481ab500b8 | -13.96369 | -48.23063 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6d70a78-915b-3a0f-9d9c-595e5085a2df | -10.88493 | -47.26022 | 2025-09-10 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d2cb702-ab7b-30a9-9069-0e4ef7c2e3a5 | -22.73146 | -47.26046 | 2025-09-10 04:17:00 | NOAA-21 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 906cb6fd-d13d-3f9f-8b5c-1415569cd59a | -13.97909 | -48.23649 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 599c6766-dfbd-3843-874e-e4ce4a3e51b5 | -15.84655 | -52.26802 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8f2ef531-10a1-38b5-aeab-1cad45388ed6 | -16.28738 | -45.68667 | 2025-09-10 04:17:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da607f04-1008-3c8a-bc8b-e0c5e2468fea | -12.20231 | -53.86851 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c4ad2fc2-1f09-3c61-a6c3-2c47f63db08e | -13.01996 | -48.03983 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbfba89a-73b9-3843-aea6-343d3293ba3b | -12.87081 | -47.96233 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 060c5012-ad9d-3748-9656-54d9fd36ba4d | -11.5406 | -47.31549 | 2025-09-10 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e294b241-a4ea-3d9a-8dac-6b057559263a | -11.4626 | -43.62503 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| abb359df-2fe5-3e68-a071-306ad053c837 | -15.2526 | -53.78891 | 2025-09-10 04:17:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24dd5171-7c84-31fe-a9c7-9ff242745249 | -14.33656 | -47.29655 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f4cd60ce-af39-3726-a876-83fd46bab27f | -15.28348 | -53.78947 | 2025-09-10 04:17:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b25e9401-00b3-3352-bb80-7881a57fd973 | -13.00419 | -48.03804 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 705832d3-d51b-390f-894b-9d0bbe34b771 | -13.34539 | -51.69751 | 2025-09-10 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 597d436f-c02e-3a4b-aa42-9f0b53abb6bc | -15.21868 | -44.0381 | 2025-09-10 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b4add5a-b1de-36f8-a11c-19c25506638f | -14.8589 | -49.53108 | 2025-09-10 04:17:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 308879d0-9fba-3bbb-9ddd-f5d0b193b958 | -11.6698 | -46.90545 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b55be919-6d66-3c83-a08f-3bad666d5134 | -10.72801 | -48.2982 | 2025-09-10 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 45b753f4-dd6f-31b8-b0af-a7e8205b8bc6 | -11.46098 | -43.63563 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 893bdb93-1d0a-3592-b70b-bb4b83cc48f1 | -13.90412 | -47.97919 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d202bed-7d60-389b-8490-25aed1823a51 | -21.49736 | -47.0171 | 2025-09-10 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e5b44db-8c1a-30c7-80e7-ef947a0c20e6 | -22.03047 | -42.89829 | 2025-09-10 04:17:00 | NOAA-21 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 006451ca-2573-31a0-9e6e-e5804185c7cb | -11.33386 | -46.52781 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2f9de0d5-5f5e-377a-bf21-7d5ecc806585 | -13.30194 | -51.71967 | 2025-09-10 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e4810588-9e00-31a5-b7a2-2aa55edf178e | -11.11809 | -48.36209 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 12f71b50-3143-3aa5-8435-f5b2a8cb6a94 | -17.18434 | -50.15358 | 2025-09-10 04:17:00 | NOAA-21 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c194516d-2521-3579-a0a8-fd2cd2388389 | -16.73234 | -48.55444 | 2025-09-10 04:17:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4a98328-3a17-33c4-8e66-5d8ce5c30141 | -21.5797 | -44.01097 | 2025-09-10 04:17:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| a5ce1cf8-ef1d-3e7c-a910-61de286e73a7 | -17.66606 | -44.13955 | 2025-09-10 04:17:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8968b02-72da-3595-bc4c-5fb1c57ac2b8 | -20.3798 | -46.6394 | 2025-09-10 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58b0868e-c94f-3e7c-87c4-58653c5958eb | -20.16267 | -47.6987 | 2025-09-10 04:17:00 | NOAA-21 | BURITIZAL | SÃO PAULO | Brasil | 3508207 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README46.md)
