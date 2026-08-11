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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30705701-0201-39b6-a739-81a42383aa2b | -18.0419 | -51.3097 | 2026-08-11 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 156.7 |
| dd578165-e627-3fb6-a484-a9859a6d4504 | -21.4829 | -48.6074 | 2026-08-11 00:00:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 99.1 |
| eb1191cd-f7c7-39b3-a4d2-14009ed1833e | -4.2182 | -46.4538 | 2026-08-11 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 662d0039-b2a9-39df-8499-aba1d7a77b1c | -11.4681 | -44.5558 | 2026-08-11 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 2b214753-6c70-31cb-adc6-39d2dace81dd | -4.2821 | -48.1791 | 2026-08-11 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 46aa99d7-512e-3f00-8208-0dae7adaf8fe | -4.4507 | -47.9112 | 2026-08-11 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 3e2e7b1f-adde-3c2d-a928-8e0ef57369d8 | -4.2634 | -48.2016 | 2026-08-11 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 1443dfd2-02e9-3d36-8b3b-31232bde370b | -4.1996 | -46.4548 | 2026-08-11 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 75ea497f-9c3f-31ba-9e70-2da4c67095ee | -14.4539 | -45.6948 | 2026-08-11 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| fa11cb2e-95c0-302f-a435-fc39da16c7ca | -14.4739 | -45.6682 | 2026-08-11 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 0f5aa9fd-1aa7-3fda-9016-0204433b3e2e | -6.5185 | -45.6592 | 2026-08-11 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| aa79a249-fbac-3c67-b592-637b40626bde | -4.1997 | -46.4326 | 2026-08-11 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 62.5 |
| c1cec877-596c-366c-8112-58b92b223e61 | -2.9623 | -49.2587 | 2026-08-11 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| fa52fc37-bfdc-3295-8717-fe69deccec33 | -14.4734 | -45.6914 | 2026-08-11 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 7c8a5392-445c-3d9c-aca0-78e0320dfbe9 | -18.0619 | -51.3063 | 2026-08-11 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 570.7 |
| 687dc882-a9a5-3ee4-a745-99fb4ea92d13 | -11.4677 | -44.5791 | 2026-08-11 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| e772e8c9-98c0-3f29-a3aa-af243a0a632c | -4.2183 | -46.4317 | 2026-08-11 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 6aa61fa3-2b59-3d72-85fb-a0824de58698 | -21.4622 | -48.6122 | 2026-08-11 00:00:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 120.2 |
| e45f7a5b-b65c-3366-b09e-f0c1326eb62e | -18.0614 | -51.3283 | 2026-08-11 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 190.0 |
| 48a1006b-29ef-3c9d-b580-781c1c7f6797 | -4.3958 | -50.9749 | 2026-08-11 00:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 1fb7f79c-8d4f-3937-850b-a61abfd96886 | -14.4544 | -45.6716 | 2026-08-11 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 4b91883f-3d32-31b3-bd24-352f6b218152 | -18.0623 | -51.2843 | 2026-08-11 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 102.9 |
| cd380a6e-891b-3a5a-ae92-230a9298afad | -4.2635 | -48.1799 | 2026-08-11 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 5d343596-8d58-37e7-93bd-df900b030846 | -4.282 | -48.2007 | 2026-08-11 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| d329dd85-d131-3a52-b516-f3c3952c5357 | -14.4544 | -45.6716 | 2026-08-11 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| ae417f1f-75d6-327d-92d0-77a8bc32a6cd | -4.2183 | -46.4317 | 2026-08-11 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 74.6 |
| e9ef0896-f612-31b3-8e69-1bf2587f9340 | -21.4829 | -48.6074 | 2026-08-11 00:10:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 6a830a7c-f387-38d0-b288-5a364437d261 | -4.4507 | -47.9112 | 2026-08-11 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| f64a059f-8c21-3dbd-b554-7dfd46ff645d | -14.4734 | -45.6914 | 2026-08-11 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 6b7e32d7-d3e5-35e2-b10a-e774422e2f92 | -21.4622 | -48.6122 | 2026-08-11 00:10:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 164.1 |
| d4e3c6ab-868e-3b8e-adb2-12324ad986b1 | -2.9623 | -49.2587 | 2026-08-11 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| cf410505-e766-3f08-8628-c8422e18d7c7 | -11.4681 | -44.5558 | 2026-08-11 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 7ed12083-d0bb-3524-9767-b6dcb553173e | -22.2896 | -42.8358 | 2026-08-11 00:10:00 | GOES-19 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 58.3 |
| 9262db60-b3bf-3106-b39b-5a7729c4ce4e | -11.4677 | -44.5791 | 2026-08-11 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| e9dd53a5-03d5-3672-bb20-fb7f89a477b3 | -14.4539 | -45.6948 | 2026-08-11 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 83952c23-1e4d-306f-9de2-b94122f23b5d | -4.2821 | -48.1791 | 2026-08-11 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 25d3f145-5301-3339-a5ac-d034b40961cd | -4.2635 | -48.1799 | 2026-08-11 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 0977f086-dcb3-3562-8b03-5da173509810 | -14.4739 | -45.6682 | 2026-08-11 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| fc19e651-1219-3af3-8a66-14829d87bbea | -4.4693 | -47.9103 | 2026-08-11 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| c1922fbd-3d47-30f9-a85f-ee4d92562d42 | -4.2634 | -48.2016 | 2026-08-11 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 9ef1143a-bdf0-3de5-a5e2-ccb02ff121d3 | -4.2182 | -46.4538 | 2026-08-11 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 9b8ebee1-4ab5-34b6-aa9e-5817428ce2fc | -12.47 | -45.28 | 2026-08-11 00:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8afbc9a5-0590-3ebf-8d4b-722acd9361f6 | -12.47 | -45.33 | 2026-08-11 00:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1934c8cc-08e8-3e14-9215-511aa7e336a3 | -6.5185 | -45.6592 | 2026-08-11 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 4f2583ad-258a-307e-a6ed-3277d947ff9b | -12.4511 | -45.3338 | 2026-08-11 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| cdb38a76-6803-3447-8b4f-7aea729f7b4c | -21.4622 | -48.6122 | 2026-08-11 00:20:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 7b7498ed-4a11-35ef-8633-07b4b8b8ac2e | -4.2635 | -48.1799 | 2026-08-11 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| bf278991-5726-3ba9-acd2-4ea9d944ce8a | -6.5183 | -45.6817 | 2026-08-11 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 0993cbaf-f959-3734-be57-dae8ac8f5cb7 | -12.49 | -45.3047 | 2026-08-11 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 7b409e13-cd3c-3138-8ebe-7d82f122012f | -21.2024 | -49.0882 | 2026-08-11 00:20:00 | GOES-19 | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.3 |
| c3f17c11-a575-3986-b85c-20ec8a44aebe | -21.203 | -49.065 | 2026-08-11 00:20:00 | GOES-19 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.7 |
| c5191c98-56ca-3111-adf1-5a84a2bb9331 | -12.4708 | -45.3077 | 2026-08-11 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 279.2 |
| 2548469a-16e6-35da-b962-58da6a188352 | -18.0419 | -51.3097 | 2026-08-11 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 59c7c758-f209-3e93-b399-ac7ae8857ec3 | -18.0614 | -51.3283 | 2026-08-11 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 23eb9c55-2b05-3618-aa81-638709236b90 | -14.4544 | -45.6716 | 2026-08-11 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 7fc39387-2f30-3f69-8d1f-8cdcdc57a466 | -12.4515 | -45.3107 | 2026-08-11 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 3f918dd9-4890-300d-be51-3cc182800afc | -4.4507 | -47.9112 | 2026-08-11 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 1a334b94-7774-3473-93a5-43a312eeda04 | -4.2183 | -46.4317 | 2026-08-11 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| cd785ae6-e4af-3761-8988-a92e6f449e17 | -4.2182 | -46.4538 | 2026-08-11 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 1e736557-07d3-3c71-bced-8db76545b59b | -12.4703 | -45.3308 | 2026-08-11 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 235.0 |
| aae0dcb3-bd00-3371-a48b-05529b427f14 | -14.4739 | -45.6682 | 2026-08-11 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| c234ae78-9548-3ad1-8aea-b21aa33aff08 | -21.4829 | -48.6074 | 2026-08-11 00:20:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 3699839b-91e1-319b-bf56-ef2364730f14 | -14.4734 | -45.6914 | 2026-08-11 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| ce5bb7b9-cc38-39f8-a91a-56af6221ad36 | -18.0619 | -51.3063 | 2026-08-11 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 375.0 |
| 5b5ff83e-edb5-31b2-a341-a1b860c38ab9 | -11.4677 | -44.5791 | 2026-08-11 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| ccbfc66c-38ca-36f2-a68b-d3ce63c719ba | -14.4539 | -45.6948 | 2026-08-11 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 0fa028e3-f880-3dcb-9c6e-4a3cd7fc7253 | -12.4896 | -45.3278 | 2026-08-11 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| acdef11b-8484-353c-9831-32a0e889ef63 | -11.4681 | -44.5558 | 2026-08-11 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 3973c443-ff16-384b-8ad7-b77f9d6ac95b | -4.2634 | -48.2016 | 2026-08-11 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 0cedbfd8-27cb-3789-ade4-24f4a6fefe23 | -2.9623 | -49.2587 | 2026-08-11 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 4477c224-beef-3619-b72e-17ca0e77a086 | -14.4734 | -45.6914 | 2026-08-11 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| c99d17dc-6d72-3e02-841f-db41165ce2b9 | -12.4708 | -45.3077 | 2026-08-11 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 209.0 |
| 1ba2e490-6428-38e3-a4aa-be1cb32c42ac | -12.49 | -45.3047 | 2026-08-11 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 478585d3-ccb7-399d-b039-79cd2cde46f3 | -9.4383 | -40.3668 | 2026-08-11 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 65.1 |
| b508ec61-bbde-397d-87e0-b8d212285630 | -12.4896 | -45.3278 | 2026-08-11 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 97899f1c-074d-35ce-81dc-c0fe285769b9 | -2.9623 | -49.2587 | 2026-08-11 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| bd3aaeeb-9573-3a19-a73b-df24141f2fd1 | -14.4544 | -45.6716 | 2026-08-11 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 07d6e398-3024-3a58-8815-a22e36a37caf | -11.4681 | -44.5558 | 2026-08-11 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| fae04e03-334a-3cdd-a563-1b63a0ad06b3 | -21.4622 | -48.6122 | 2026-08-11 00:30:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 104.3 |
| f27038b5-ba71-32a2-a6fc-41421cc5d64b | -11.4677 | -44.5791 | 2026-08-11 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| c735244c-2977-3764-b005-0452f17a1977 | -4.2635 | -48.1799 | 2026-08-11 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 9f2ddbec-6f1b-3c05-a42f-450bc31e9d37 | -18.0419 | -51.3097 | 2026-08-11 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 5947e0a9-9bd0-32a9-89cc-60d568578e77 | -18.0619 | -51.3063 | 2026-08-11 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 183.5 |
| cffcf1b8-7752-33c4-b7e6-1f9074df8577 | -4.2634 | -48.2016 | 2026-08-11 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 65a82099-d832-3ea0-a5c0-ef7b2be3d003 | -12.4511 | -45.3338 | 2026-08-11 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 8af7ee63-7668-3999-833c-07d5f25b06d7 | -9.4379 | -40.3917 | 2026-08-11 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.0 |
| 87a211b6-d8f5-341c-b27f-cf846735fbd8 | -12.4515 | -45.3107 | 2026-08-11 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 8214e633-0589-3423-a466-80c34d4b0627 | -8.9415 | -60.5174 | 2026-08-11 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 4869c6a8-8b44-3e81-8f60-d7095e938bee | -14.4539 | -45.6948 | 2026-08-11 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| a38a26a4-e1b4-350d-9784-63e7392153f9 | -12.4703 | -45.3308 | 2026-08-11 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 266.3 |
| 20c8df6b-6877-3619-9209-db7aef826b41 | -12.4506 | -45.3569 | 2026-08-11 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 0b9f6717-8a23-3591-af20-7794e16bf08c | -12.4708 | -45.3077 | 2026-08-11 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 0a177f7f-bcaf-33df-9d4d-4377354a37d0 | -18.0419 | -51.3097 | 2026-08-11 00:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 7ca8649d-7217-373d-9ca8-f0a313c33518 | -12.49 | -45.3047 | 2026-08-11 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| dd563676-d311-3703-95fd-a175b8daeefa | -11.4677 | -44.5791 | 2026-08-11 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 6255cf2f-c4ec-33a0-8332-c510b7ab219d | -21.4622 | -48.6122 | 2026-08-11 00:40:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 104.4 |
| cb08f209-d8b5-3d72-80d4-3eb95ad6d1b1 | -14.4739 | -45.6682 | 2026-08-11 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 1a4e6ef3-0eaa-32ae-ba1e-30c5e6ecc864 | -14.4544 | -45.6716 | 2026-08-11 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 46726d42-caf7-33b2-8db2-bbd059efbd4c | -8.9602 | -60.4973 | 2026-08-11 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 6955e407-7e81-33fb-bcf3-874f1858b404 | -4.2635 | -48.1799 | 2026-08-11 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |


[Clique aqui para ver as próximas entradas](README2.md)
