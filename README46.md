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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24b72d8d-5610-33bb-bb9f-a0671e9481bc | -10.64668 | -48.52483 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4db60a11-2498-37fe-88e0-243f03c4f208 | -14.59462 | -48.22142 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 39431d50-32a3-3305-a209-ff85580e7c8d | -16.86436 | -44.27186 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 84515130-cc04-3c39-9bab-d61b7fa95c1d | -11.35623 | -44.9785 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acfbffba-1a7f-3a45-99d5-cfbea66a2f76 | -12.17605 | -51.41726 | 2025-10-01 04:21:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 813c5968-d2fb-3cfa-a61c-44828bf02479 | -13.3685 | -47.29317 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d689aad-11df-360e-85fc-8c0137177028 | -13.13735 | -47.41717 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eb9f8392-4e7c-33d7-b4f2-5f3d37036806 | -14.98611 | -50.76166 | 2025-10-01 04:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 612180ac-a229-3696-b3de-897eea112655 | -10.04259 | -52.09312 | 2025-10-01 04:21:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e33e131e-73e8-37d7-867b-6a7f1379fdf3 | -14.08556 | -44.08994 | 2025-10-01 04:21:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 706566cc-d450-3e64-9da5-b94b6ed7a9bf | -9.78035 | -47.75692 | 2025-10-01 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b9245aa6-0cd4-3400-9032-8b5285440799 | -10.85068 | -45.41302 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cf008012-307d-3588-a19b-83ee76782e55 | -14.20708 | -44.93231 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 557ba7df-157d-3c11-8edd-0289c2a5be1c | -14.18289 | -46.1201 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 23ef7128-6599-3fe2-9092-abe9fdc15ebe | -11.94677 | -43.91809 | 2025-10-01 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 48c53285-8766-30e1-8213-6f2553d958a4 | -14.35753 | -47.13287 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bfa9dc0a-c4dc-3835-a193-987142d01b5e | -14.72751 | -48.26642 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aab2748a-c45c-3e32-9703-c92bd3892cfe | -12.24316 | -47.80833 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f13133fe-e890-311b-b7b8-78db50c2d565 | -12.8551 | -46.9481 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| adb9dc6e-29eb-3f73-aca5-da7407e33ac9 | -14.96771 | -46.87032 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c7c6ac4-2775-365e-8295-b7f7e04d88a1 | -15.78077 | -43.70552 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23886469-14f1-3eef-8ffe-d0e077c6bd6f | -10.73841 | -45.37009 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b88d00c2-cf34-3887-b518-6b2f4286d6c2 | -15.17367 | -49.08164 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 03d872a2-4a8d-38d7-a313-e99af8727da8 | -14.76764 | -48.09475 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35595c83-41fa-322d-b9a6-21cbc0e3d246 | -13.8125 | -47.8809 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67e3a571-7003-3942-89e1-3f482280c8a9 | -16.03173 | -50.89157 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b75b32b4-7436-3c68-b9f3-c5a4ab0c2033 | -14.7072 | -48.2209 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8e1b0bc3-9fad-3176-b219-734c3f64341f | -13.7528 | -43.66211 | 2025-10-01 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76498785-c41b-34dd-af88-c275ab74c442 | -14.58927 | -48.29683 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2c901533-5a94-308f-957d-73fd4b74352e | -15.24994 | -49.70537 | 2025-10-01 04:21:00 | NOAA-21 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b72c69bb-4a91-35eb-acbb-7d409a864560 | -12.22773 | -43.74879 | 2025-10-01 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf5cf424-1b53-3bb8-8460-e88439199d69 | -14.94602 | -45.55164 | 2025-10-01 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 643fee3d-1361-3afc-93c9-f271ab4e100a | -10.18873 | -52.56371 | 2025-10-01 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76f0d171-8e19-3470-88c7-42eb132d6e53 | -15.39289 | -47.06501 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14cb0e29-fccc-3ac3-b874-15660a0e3980 | -18.33723 | -41.80338 | 2025-10-01 04:21:00 | NOAA-21 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b26df66f-a59c-3f56-ab0e-8e06e4303f2e | -14.69994 | -48.26546 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f52cbccd-9f68-3896-abf2-238cdadfa018 | -13.33408 | -47.84505 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1ab0b145-f5a1-3ef6-bca2-35649ea66db0 | -12.35716 | -43.21115 | 2025-10-01 04:21:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0493df22-6118-3497-a143-0561753cdd7e | -11.19995 | -47.75829 | 2025-10-01 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7f53261c-49c5-3c39-b2d7-240eb91c0ad4 | -13.22747 | -47.32478 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b3dbedb-01d9-3063-85da-4b849a968725 | -12.95976 | -46.41861 | 2025-10-01 04:21:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6de01235-26bc-3a54-9082-2c09d44b1708 | -10.82378 | -46.643 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 242cab51-035b-3a71-b3fe-6fdc00a61ee2 | -12.87953 | -46.90112 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d705644a-77f7-392e-91fd-26b2b00c7b1f | -14.35374 | -45.9399 | 2025-10-01 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61ff1477-e2d5-3f57-ba7e-fd25d3a7ffdf | -15.36038 | -47.07785 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f09af8f-c513-3954-80c5-d8086a317884 | -16.36224 | -49.96406 | 2025-10-01 04:21:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc2acc61-e3e3-3b90-8806-f1ee0bed7e37 | -11.86707 | -48.02339 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb9b9769-612c-32f8-9f66-e8651087f668 | -12.95294 | -46.41416 | 2025-10-01 04:21:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb5458bb-0ac6-35bb-8e9f-4d832456920e | -10.94599 | -44.32593 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbc2bfff-cef0-3704-848d-e06a61bf0856 | -13.0793 | -47.08031 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ab47fb3-a88e-3ae1-8db8-181da24cf4bb | -16.17191 | -46.51814 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d5c96a5-24a9-39b1-984a-f3ea2ac1fa49 | -13.4992 | -43.8159 | 2025-10-01 04:21:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bc877b58-2bc2-358b-bd61-74915e9000ed | -13.33425 | -48.14349 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 380a1132-b225-30c8-82ed-f1f80997802b | -12.04367 | -47.90933 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d223176-6756-33cb-a8b5-928477bb777a | -14.44957 | -46.35255 | 2025-10-01 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 256e8198-5267-3a94-a322-a8ba09b6a962 | -12.95571 | -46.37497 | 2025-10-01 04:21:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d07662de-6906-302b-82e8-2b991f62afa6 | -14.37503 | -47.13189 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fea51ec0-e58f-3515-8572-22d6f7dcc1c8 | -17.39045 | -47.14718 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 41a27405-f0fb-3899-8975-9ad13e6bd7a5 | -11.60707 | -45.05019 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 171c7a8e-10a3-36d2-828a-81b0511b2708 | -15.93923 | -46.2404 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cbf7718-5c8d-3918-a655-3d288ca9a2f9 | -9.32261 | -50.62793 | 2025-10-01 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f569574-eb88-3401-b9aa-e08171cac036 | -11.46669 | -45.07906 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9177f940-b8af-33bb-aff1-0b5d7e483e83 | -12.82883 | -47.02779 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5bc7d71d-8e9f-38e7-8255-eb5a8c9e6251 | -14.79352 | -45.798 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b37b0ceb-bdf4-3726-8de7-000bf30f4cf0 | -13.20963 | -47.32946 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9f445fe-05fa-3937-8c09-ddbbbb8f6656 | -11.8503 | -44.99396 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| fdecb897-22e5-39ba-8534-1cae91f3de1b | -13.76041 | -48.40026 | 2025-10-01 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29ac093c-e443-33cf-9486-54747425bd84 | -16.05506 | -51.0205 | 2025-10-01 04:21:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 34d912f1-9add-3e8d-b65e-60ab89855300 | -14.6794 | -45.29295 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc9c55e0-e01f-341f-956a-bf52187c3c9c | -9.92432 | -46.83974 | 2025-10-01 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ec3e07f-1268-3727-980a-cb6d7efceeb0 | -11.82308 | -44.97137 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0eeb0219-a223-3e8a-b02f-c04ff995e7ba | -15.15672 | -48.00984 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2475639b-b8cd-36ac-9b3d-58ad93fdfeef | -12.3912 | -44.6981 | 2025-10-01 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9673063b-441a-3c9d-aaa7-74cabda7e905 | -14.18453 | -46.10951 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01ac0c83-9d34-3503-982d-66808dc634f5 | -13.387 | -48.0829 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8ca5a38-8b03-32d8-9d66-9af648d79a44 | -14.03975 | -47.96427 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 294e9169-0765-34a9-bb69-88fe6911ed88 | -13.36907 | -47.28962 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f94a448a-84e7-3d0b-83d4-44451bc988d6 | -14.72473 | -48.15554 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22e81df4-e245-3b08-bd5c-3a87a68eea01 | -11.6331 | -47.49586 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 51d94d40-60e1-3963-9613-ec18c3b08976 | -14.18674 | -46.11712 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 42e44bed-e42c-3108-81dd-455755f691ca | -16.02702 | -50.88698 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e8fde32f-3f77-3682-920a-ad48dd592e0b | -12.18244 | -45.04573 | 2025-10-01 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1288eeab-b44e-3e77-a9db-da8eddca9be3 | -10.21276 | -48.20496 | 2025-10-01 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 21efc04b-76f5-36c6-9b42-96819583c53f | -11.47338 | -45.10188 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2097cf05-9d88-3a72-b7c8-defac764775b | -15.29584 | -56.78408 | 2025-10-01 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82c72ca1-f7a0-3a51-abac-d8a9f81d47b4 | -13.56083 | -47.26266 | 2025-10-01 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fdfdf0b-3333-3df4-a5c7-c562fbe16164 | -16.68065 | -52.53567 | 2025-10-01 04:21:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0a299d9-e0c3-3dd8-a4d3-c1f08b134c87 | -14.052 | -47.97384 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e8cec8b8-19be-3072-9965-2e601ee5ea4e | -10.20586 | -48.20329 | 2025-10-01 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c2c1f7d4-ecc4-3944-8700-7c735d4da9a5 | -15.91877 | -46.21901 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 308c1578-1c91-36ea-a577-e85f534bb187 | -11.82187 | -44.93466 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d35ab53d-f6f6-3fc1-8657-62147fd0b833 | -13.37436 | -47.32021 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a8700c5-5560-39b3-8407-4b3ad4cb1a14 | -11.45823 | -45.02325 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80cea795-1eb5-3471-be38-aaf459a08937 | -14.98072 | -50.77031 | 2025-10-01 04:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae2c6fe7-f456-34aa-9f94-63bcb31ae026 | -13.63204 | -47.64779 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 140d60de-e5d1-3ced-8090-e16c56af572a | -16.17135 | -46.52172 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38846607-7a4c-3bd8-8877-d2162d926d3c | -10.06974 | -50.28056 | 2025-10-01 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 16f876d1-fb13-35ad-8943-880d99c415d2 | -15.25908 | -48.05024 | 2025-10-01 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d116848-0d98-38fb-847a-b99264e16ab9 | -13.98281 | -44.90945 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 458eed8a-9615-33b1-9660-4df567d12a93 | -11.83415 | -44.96586 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README47.md)
