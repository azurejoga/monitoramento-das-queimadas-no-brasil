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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65264b61-3efc-3e6c-b95a-8991c669bfab | -7.85892 | -47.00301 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5d7d4cba-11cf-36ac-8e82-f9b0b0638bac | -8.77537 | -46.69645 | 2025-08-22 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0706135d-0cfe-3ef2-936b-302ffcf21df9 | -12.96263 | -46.25777 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aea610dd-d53b-3e3d-9409-5f73e20af995 | -14.887 | -47.95794 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 945533be-d342-3127-b35c-9f59982b0326 | -13.50247 | -47.0629 | 2025-08-22 03:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f488f021-10a1-365d-90b1-793fcd5d3277 | -14.46983 | -48.36177 | 2025-08-22 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec629a4b-6be4-3b14-9635-4e8e9ff99644 | -13.37071 | -47.50121 | 2025-08-22 03:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 519462aa-a849-3d55-ba44-9dc57a487505 | -12.00099 | -44.67438 | 2025-08-22 03:57:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98cfaf4c-a499-3af5-92bb-ac199f00711c | -14.86868 | -47.94997 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ae31564f-c669-37a4-9de3-a22feff13086 | -10.44388 | -48.36138 | 2025-08-22 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b312544-f297-30ec-9f47-12e5e8dfd94e | -10.28139 | -46.7544 | 2025-08-22 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f050d7d-ce8b-3b2b-aaa0-5df49e18cc28 | -12.96527 | -46.26095 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6cc4c47-674f-3880-9846-6c90c6e6618d | -8.77638 | -46.69093 | 2025-08-22 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3698f44-bcf0-3e61-98ec-9eb3b6700fec | -12.98855 | -45.23678 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 96c732d8-4173-3e37-b836-558d5032df1b | -13.02209 | -45.19208 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50ae44bf-2a10-30d4-8a84-36602ac5dee8 | -13.00645 | -45.23225 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a76714df-8459-3e8b-ab34-3f88cc824692 | -7.86914 | -46.99163 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8a1f5b1-023e-37d0-bc78-6246886e3b98 | -15.57695 | -43.41287 | 2025-08-22 03:57:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a364b94f-cd78-338c-bd4b-72475174eae3 | -14.76964 | -45.41151 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f1c3c1d9-8518-3e13-94fb-02d824687fd7 | -12.9587 | -46.2797 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2155bec7-83c3-33b0-997c-589b05ec0eac | -12.992 | -45.24136 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b5e7690e-a881-32a4-b514-e6fe3603c067 | -12.49973 | -53.81306 | 2025-08-22 03:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 08540592-6d64-3126-846c-86ffcef34b2c | -10.18209 | -47.56872 | 2025-08-22 03:57:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf2784ce-44a2-3549-b2cf-851466c46423 | -14.76896 | -45.41522 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ae2376e-e0b9-3681-9b74-f1b703c15c36 | -13.03089 | -46.32811 | 2025-08-22 03:57:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1acd7f94-4c0e-3410-a9fe-b44b48858ca6 | -13.02966 | -45.19741 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 722002fe-0c38-3eca-aa75-af0f1e8e424f | -14.7534 | -45.40841 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b820155a-8210-3811-98cc-43c9a776b47c | -11.3076 | -44.94706 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb8e49df-1e97-3a01-bcb7-05909cebc2f9 | -11.31042 | -44.95552 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a7820aa-05aa-3ef0-a4f7-206f51c3fc7c | -13.02754 | -45.18531 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53a8e75b-ea1f-3a62-80e3-961d224bf5e4 | -12.93078 | -46.18121 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6eadd6f4-9604-3cf2-b1de-98172f02a81b | -13.32609 | -54.3999 | 2025-08-22 03:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4877de5d-19a1-3012-b10a-4baca3083fc2 | -12.93507 | -46.18269 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 457b6fdb-870b-3187-b9d4-2b90bf5f129f | -13.02954 | -45.17396 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46883a69-a80a-3110-ae6d-1067500e09aa | -12.57146 | -41.27864 | 2025-08-22 03:57:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f71fd225-c574-34a1-95b1-b275ca01ed66 | -10.44983 | -48.35906 | 2025-08-22 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6905dbe9-7043-3904-94ee-af810824cfb7 | -12.92644 | -46.18003 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9a251b7b-bb7c-3959-8728-5745f44ed24b | -14.88376 | -48.0536 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a147b9a5-ace4-32e5-ac37-a0630a3b245c | -14.88322 | -47.95174 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9dbc7bff-6aa5-3ce2-9422-2868cb1f6aeb | -10.8552 | -45.20797 | 2025-08-22 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efe59b7f-7236-3518-ab71-8e8541d794f4 | -11.3111 | -44.95167 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36a942d0-c3d7-3488-8a3e-b79fb9eaad23 | -12.95245 | -46.28046 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3fb37763-bafd-346d-a36f-39c9a95e7396 | -13.03245 | -45.20579 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc85f3ff-6fb6-3d4a-8c96-8b9ff443a5d5 | -13.6457 | -45.70147 | 2025-08-22 03:57:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53f1c044-b8f3-3fc8-8ff4-ccee74095ad5 | -14.76422 | -45.39518 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7b947bb-03c2-3803-a8b4-e09fea7f91dd | -7.86406 | -46.99069 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4792d580-ea2c-3ca8-aa2b-d8c3bccc8679 | -15.44683 | -39.29939 | 2025-08-22 03:57:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 53078f69-31cc-392e-8956-f19977a33a3b | -10.26599 | -46.76244 | 2025-08-22 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9cb41b9c-60cc-38bd-b494-4b8119c1ed3b | -10.72962 | -48.2494 | 2025-08-22 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8db92f21-0a6a-3a01-96ba-ae590e2f72a3 | -13.46648 | -47.05051 | 2025-08-22 03:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3511a37b-b51d-36c3-8fd3-946b34146b6b | -12.29272 | -38.937 | 2025-08-22 03:57:00 | NPP-375D | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c7285a37-da92-3469-ae91-15e81ac28316 | -13.64497 | -45.70548 | 2025-08-22 03:57:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da4a5111-73d0-30a7-9988-8f62d05de2a1 | -13.03549 | -45.19753 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efcc5234-2340-3181-a2c9-f1de755e0c8b | -13.02131 | -45.17237 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e417f6e1-a291-3940-87df-f946f5effd2c | -12.93003 | -46.18531 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5e28a44d-7721-3e4f-9b02-62bc5ee84ad2 | -10.27082 | -46.76313 | 2025-08-22 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e1f008c-f2bf-3862-ae38-62dc282bd860 | -11.31178 | -44.94783 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0454c206-dc46-3e9f-a2b7-4e3295da1c35 | -13.03099 | -45.18988 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 199a132b-5bf6-35e7-b85c-d82332b50d0f | -7.86462 | -46.98763 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0228a7d-e791-3dd1-9b2a-1b9f5b45b6e4 | -13.50062 | -47.07275 | 2025-08-22 03:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1ba2e2f-7384-32cb-9921-e3631d03fb45 | -12.9584 | -46.27321 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45d2b037-3344-32b9-8d6e-ac24317944d6 | -12.09659 | -43.34399 | 2025-08-22 03:57:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd3eb1f7-3e3c-31ff-bb02-abdde23e3fd6 | -13.02064 | -45.17616 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29326255-6e97-316f-9a1a-5d1c32f14ef3 | -12.95727 | -46.25474 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 223c7704-44a0-3d77-845e-f7a0be59bdf1 | -7.86126 | -47.00608 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 161604ec-f0b7-3c22-bcf3-4cb439e56644 | -13.48683 | -47.04423 | 2025-08-22 03:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb24f5cd-bc63-3d40-a874-a46ef3fd5be2 | -12.99676 | -45.21469 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86c64f4e-0917-31c2-9fa0-999ea3e2b120 | -14.75272 | -45.41211 | 2025-08-22 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8c34763-404f-34a5-bc77-612c975aa848 | -14.49675 | -48.83613 | 2025-08-22 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 842d74cb-3f84-3c3d-b280-c018b8b6fb09 | -13.02478 | -46.33649 | 2025-08-22 03:57:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c6792d68-d35b-39d7-803a-e47ded659943 | -13.64424 | -45.70949 | 2025-08-22 03:57:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51618eb5-4a07-3afc-81fe-140559d4f138 | -14.31897 | -52.01748 | 2025-08-22 03:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7416ef1-bba8-3bc2-b720-05412df16cae | -8.50117 | -44.73831 | 2025-08-22 03:57:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9fd4346d-bd14-30e4-a4f4-ada357840189 | -10.4492 | -48.36242 | 2025-08-22 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc245d8f-409d-32d8-b856-cbc44de1cf81 | -13.50339 | -47.05799 | 2025-08-22 03:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6aaee382-a0a3-3779-806c-febd6be5fa18 | -10.73276 | -48.23248 | 2025-08-22 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e01c0317-5251-3d1b-abd4-92ab6e6113ab | -11.30626 | -44.95468 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 128ff1a8-af4d-39cf-ba21-179de54b3051 | -13.02766 | -45.2088 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02c357c2-c449-38c4-87e1-fbd455d09f14 | -13.64846 | -45.71025 | 2025-08-22 03:57:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3f58f5f-fad8-39ab-a230-84905b4c2ae0 | -13.01652 | -45.17539 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88c3bf44-1d8a-35c9-80bc-093c64b95b06 | -12.98578 | -45.22837 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71ce7600-9775-3d3f-a870-2c730679f63b | -13.02543 | -45.17316 | 2025-08-22 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad076fec-7844-3581-a878-f77c6d85efed | -12.00975 | -44.6722 | 2025-08-22 03:57:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 30226e7c-847c-3aca-9d8b-92ccbe09759c | -11.12692 | -44.71913 | 2025-08-22 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 28fc6c4b-e7f4-3836-a786-1eeff5becd73 | -12.954 | -46.27219 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3369d50-f516-3ec7-8595-9aeebb584917 | -11.79638 | -48.79058 | 2025-08-22 03:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| da5acba1-7ead-35f5-a9f9-38d51450a0bc | -14.88055 | -47.93974 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f40889a6-b215-3eda-b796-fef82025bb72 | -14.53074 | -39.73942 | 2025-08-22 03:57:00 | NPP-375D | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5cf2af7e-3db0-39d7-a0a8-7764fc273e55 | -15.44738 | -39.29572 | 2025-08-22 03:57:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1342eb86-4f00-3b2b-82bf-f6ae1acd05fc | -14.88429 | -47.94614 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fffef6bc-4c21-3e29-a60a-caec71ec37be | -10.86021 | -45.20458 | 2025-08-22 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f42a3b34-4543-3239-98a5-960b03e5d025 | -14.517 | -47.85702 | 2025-08-22 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87822363-28ff-375d-8599-d036eaa6a895 | -11.435 | -47.31978 | 2025-08-22 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de108396-d23e-3ebf-96f9-fc47e9d8aee1 | -13.45997 | -47.05954 | 2025-08-22 03:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f51c9f1a-f480-3f0c-b5b6-83f7cf645b32 | -11.99694 | -44.67365 | 2025-08-22 03:57:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90d2ae8f-ee97-3ebb-924c-cd33622e43b6 | -14.8746 | -47.94495 | 2025-08-22 03:57:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82a2bfa6-47df-3822-b737-509b9c9c24d6 | -8.67834 | -47.98306 | 2025-08-22 03:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1ba8a6b-1a17-3460-8cfe-70736f06f1b3 | -7.85954 | -46.98668 | 2025-08-22 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6cd6ac20-92e8-326d-a92a-94325031f775 | -12.96184 | -46.26219 | 2025-08-22 03:57:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e934b215-dc1a-3af5-bb11-a954e359bac8 | -10.73435 | -48.25324 | 2025-08-22 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README19.md)
