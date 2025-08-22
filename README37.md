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
| 30dae9ec-cb42-30ac-b5bb-08539c0a97e8 | -13.03017 | -46.33256 | 2025-08-22 04:21:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 40.9 |
| ca7d3391-c7e2-3654-8bd0-cda723ad8fca | -12.92048 | -46.16612 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b211e7d-6c6c-37b3-a121-41a33956c39e | -18.1803 | -48.03741 | 2025-08-22 04:21:00 | NOAA-20 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5550a5da-3cb2-3e47-aeed-20addb2abf63 | -19.65042 | -45.97572 | 2025-08-22 04:21:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1182b9e-c762-3df0-8429-74b9b24b115d | -12.49254 | -53.80449 | 2025-08-22 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f034ac1d-b592-33ea-a8da-fab80c1bb6f8 | -14.46619 | -48.35736 | 2025-08-22 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b4ba3c4-1dff-3af4-bf9d-79be3ae3d51f | -12.96076 | -46.25609 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26bd217d-ae31-3256-bfba-739c9a7e1c70 | -15.13848 | -48.10501 | 2025-08-22 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6735600c-ac83-3e5f-85a4-6fcee2d5c17a | -18.26535 | -45.55499 | 2025-08-22 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afbe27d5-c3c5-388b-8206-aeb939fb05f9 | -12.97576 | -56.89005 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62b7464a-a415-37b7-94ab-009b4dc11428 | -14.62938 | -54.84339 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ebb68526-6f88-32ec-a97d-1a925d41abd5 | -14.32181 | -52.01055 | 2025-08-22 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2c6a6bb-a994-3132-9252-34d5bf92ce2d | -14.74005 | -56.04246 | 2025-08-22 04:21:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5af05cef-f268-3f19-b5e8-b1edc8fcde93 | -16.78035 | -47.65548 | 2025-08-22 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f0b1220-3705-3529-b006-5e391873de7e | -13.02633 | -45.19939 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| efc19b47-7048-3864-8b90-455229aeadea | -12.92875 | -46.17831 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 457e6012-9da9-3b95-a5f8-88c6c2ace6d2 | -17.60442 | -46.09243 | 2025-08-22 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4384cb52-d1b1-38f0-9cde-b2d5256e1e86 | -18.95206 | -50.02661 | 2025-08-22 04:21:00 | NOAA-20 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 99efa353-d214-3af2-aa3e-c386a85aeec7 | -18.28245 | -45.53385 | 2025-08-22 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19ac0cc5-2bda-33da-b0a7-542879a80fa4 | -14.76151 | -45.22755 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e6dfaa39-b4ff-3911-a806-3a0aa2d1e9bc | -12.42668 | -48.70379 | 2025-08-22 04:21:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f94494e-4e44-3e68-95e4-3074adebe46b | -15.56675 | -50.33467 | 2025-08-22 04:21:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85d5662c-225a-30cf-9bb7-1012e035c57f | -13.02799 | -45.18856 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6dc4ad0b-23f2-3414-9989-bf463dd5e156 | -14.25583 | -53.33704 | 2025-08-22 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc2e9fe3-e94d-3712-a9a2-fd636135475c | -13.5026 | -47.05698 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26fcd3cd-f064-32e8-9250-63ed5ed66dcb | -16.61076 | -43.36264 | 2025-08-22 04:21:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34be4321-1ef7-3d3e-8fde-cd6678dedf7e | -20.24522 | -46.69816 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abf6722b-812b-32c9-878b-be1539495d70 | -20.07921 | -46.12555 | 2025-08-22 04:21:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6f5e76fa-e15a-37ce-8e33-fb22cbedccb2 | -13.65083 | -45.70672 | 2025-08-22 04:21:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3a4920bb-d8c7-33c5-ac1c-f40564748591 | -15.54731 | -43.98811 | 2025-08-22 04:21:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a261959-353f-3300-80a3-e9b350b2207b | -16.48444 | -45.09258 | 2025-08-22 04:21:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 441e5fdf-30b8-3a54-81b4-be2524f1ebbd | -13.13951 | -57.12301 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f35698f1-f1c0-33b6-9827-0f2cf418fc44 | -20.23469 | -46.60767 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4f04433f-47dd-3ce2-bc71-2e63ea2fed34 | -18.93855 | -41.49287 | 2025-08-22 04:21:00 | NOAA-20 | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0eee15f7-aeb3-3144-bfc2-ee99e39e1ae8 | -14.87764 | -48.05261 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 03e29d5b-999d-3fdd-9e23-c04914e56072 | -20.45671 | -41.68068 | 2025-08-22 04:21:00 | NOAA-20 | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3ec7ef93-bc3d-37f9-9c4c-9cb958d42376 | -14.75546 | -45.40418 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5c2c32e-b5e2-3ed7-9995-57152650b269 | -13.143 | -46.90595 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7895468a-c45f-32fc-8949-0e83a4ae6bfa | -14.79119 | -59.65664 | 2025-08-22 04:21:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 93394edd-44d2-31ad-9eb3-a882e911a43d | -14.87552 | -47.93897 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ca081c57-5225-3771-bbbd-571f49339359 | -13.39347 | -46.22526 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5759432c-0f36-3316-8084-793c85963b20 | -12.95523 | -46.26965 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1ad1c10d-8fb7-30b4-8f3f-cf2b5b13c5c6 | -15.08275 | -47.09767 | 2025-08-22 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae9928c8-c610-3337-8d0b-f83f805513c5 | -13.01914 | -46.33798 | 2025-08-22 04:21:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9a56698-7172-377a-be09-f0e505831c25 | -13.48439 | -47.04291 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b8d507a-2c57-3d9e-985e-bf341091caec | -17.66727 | -54.05423 | 2025-08-22 04:21:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6534db1-1d5d-3dce-a9c1-7486b34d6c7c | -16.93468 | -44.14779 | 2025-08-22 04:21:00 | NOAA-20 | CLARO DOS POÇÕES | MINAS GERAIS | Brasil | 3116506 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 35490f1e-cc65-3f58-9ee2-09aee23812a5 | -12.98137 | -56.89541 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b244f99-e2aa-3a6c-be8b-efca7f1f5ed9 | -17.83218 | -44.4245 | 2025-08-22 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9247816-8a97-3103-aedd-b7a9958d2427 | -14.65757 | -56.5958 | 2025-08-22 04:21:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cc0aa6f-9b91-3dfb-900a-91ad7f29d988 | -12.98221 | -56.89133 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7e57200-b292-3aa0-a15d-104534dfae8f | -13.35859 | -46.25196 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 257dda19-3bc0-3b3e-889b-3f8b9ff53277 | -15.5481 | -51.71247 | 2025-08-22 04:21:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d2b7bfe-7172-3f10-bc8d-aa2940a531fc | -14.56508 | -51.96114 | 2025-08-22 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90a06c57-288c-3a14-8ff9-ef7958f71667 | -18.26019 | -45.54224 | 2025-08-22 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92e21f47-2231-35e8-bd99-c84c6fd3a1bf | -20.27131 | -46.57079 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03520091-acbd-36f4-8c94-a54b4852c06d | -12.95798 | -46.27373 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7fbb616f-3027-374e-bd83-576c4b954948 | -15.2437 | -49.68326 | 2025-08-22 04:21:00 | NOAA-20 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88968ac8-3b98-3654-946d-1e99077479d7 | -12.95414 | -46.255 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a7d84d5c-e1af-30bc-9c38-efbe668d0c7b | -20.23863 | -46.60444 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f3196d70-71b0-321e-bd62-6c9ba8c77104 | -14.75602 | -45.40052 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b22b332-e763-3173-be13-c53d170f5428 | -16.74988 | -49.31579 | 2025-08-22 04:21:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 758d2f1d-a897-3224-a722-eb68f5e40ecb | -12.98053 | -56.89956 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88e7eee9-95e2-3925-8b93-0719446df2b9 | -14.91227 | -49.45624 | 2025-08-22 04:21:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8667e6a2-55f3-307e-9d8a-3b2bc9b1e136 | -12.92655 | -46.17072 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 00f3b261-52bd-3a8d-ab9d-606078bfb47c | -12.95027 | -46.25798 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 713ae109-393e-35f9-9a43-a8375563a096 | -13.35748 | -46.25903 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49b92fec-dabb-3ac7-9d16-0da8cf747a10 | -13.50202 | -47.06054 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2fe0015-cab1-3f94-bec0-f39fc387f4fe | -13.02405 | -45.16945 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85238ee8-6aab-3e66-917a-08cf9f4f9f51 | -15.73332 | -49.45046 | 2025-08-22 04:21:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 189d4cfe-69a7-3e78-8d00-6cbcec1685c1 | -17.92039 | -44.48721 | 2025-08-22 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc66024a-6032-391d-9ad3-9581b0cb84b5 | -15.89617 | -43.45858 | 2025-08-22 04:21:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 71669e59-0cd1-3416-a5e0-03d001492a67 | -20.24972 | -46.69118 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1efe722-daec-3fc0-94ab-d6c9f91ecbd2 | -13.03019 | -45.17412 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f069863d-6f5e-3535-b1c6-8aaa6bccb63e | -13.02578 | -45.20299 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dedac98b-3765-3178-90b3-ecfa6a1ca8ea | -13.02686 | -46.33202 | 2025-08-22 04:21:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 525791ac-4667-37cc-8605-75acc60d03aa | -13.19915 | -46.89331 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 943e8ee9-dec5-36b3-8f43-36616f635f0a | -15.5866 | -50.3068 | 2025-08-22 04:21:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6abf6e51-4d68-3ede-861f-741665603bc2 | -13.02354 | -45.19524 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65a60d8e-e92a-3713-b5f9-08b373eee05b | -20.74353 | -43.48379 | 2025-08-22 04:21:00 | NOAA-20 | LAMIM | MINAS GERAIS | Brasil | 3137908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 35a3addd-09c5-3c83-87b6-f53eef2efdf1 | -11.31834 | -55.22427 | 2025-08-22 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e19a7faf-6810-3d60-af71-6133e1ce7922 | -12.49741 | -53.80788 | 2025-08-22 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bffe2a02-9efa-3685-8ed4-34a54565a90f | -13.15903 | -46.91236 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b560b12-5df3-342b-ac20-1fbf63f7df97 | -13.39678 | -46.22581 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3f8820c-2250-3f06-8d71-8228d4d7f54f | -14.5912 | -47.28267 | 2025-08-22 04:21:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9ebfeb6-41d9-36eb-83bb-76f7607cb874 | -19.67431 | -48.99283 | 2025-08-22 04:21:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 888b106e-e9a2-3284-bb48-a766b32ad80f | -13.01681 | -45.17199 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 076d512c-4637-3bd8-a381-d4a0d272d309 | -15.63401 | -45.14741 | 2025-08-22 04:21:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| a7f0d660-1989-3ff3-be4a-7f3f8ff5ab46 | -20.27076 | -46.57448 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a00ce1f2-103b-3a5a-87bf-403160457e99 | -13.02185 | -45.18389 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0633eae-3bc9-3a57-beeb-6ef5e7b5db01 | -13.16197 | -46.91269 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c2e49b3-3c0d-3fbe-aa63-68539457057b | -13.4987 | -47.05998 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97427fa7-9a9f-38bc-918d-ac5d12989317 | -13.03413 | -45.19323 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6f57e06-8c50-3a60-a53e-a8152c45996b | -12.99042 | -56.88043 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1be9ced7-fc26-356e-8f59-0c9dc9256b61 | -13.64473 | -45.70206 | 2025-08-22 04:21:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52037c09-3e4c-3775-8010-b82677519793 | -12.431 | -48.70348 | 2025-08-22 04:21:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccea56c7-1c4d-31f7-b16f-21f670e45006 | -20.3559 | -46.56913 | 2025-08-22 04:21:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 53c65acf-a95e-3ba1-a992-6ce228d7f7f6 | -14.65204 | -56.59502 | 2025-08-22 04:21:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99206748-c553-3e75-af89-f05245885ac1 | -11.89486 | -55.89861 | 2025-08-22 04:21:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe71a5d2-4e3d-3e99-b156-a6a5c44f6e1a | -13.02025 | -46.33093 | 2025-08-22 04:21:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README38.md)
