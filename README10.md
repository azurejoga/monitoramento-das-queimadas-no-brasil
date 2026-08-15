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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f1fafd4-f273-3d61-bc4f-277ee0e3e39b | -14.4367 | -51.85722 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fcb532a-f260-36ad-865a-b94e95e22af1 | -14.44639 | -51.91431 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f7937a90-a97d-3653-8bce-10bbf977c5dd | -18.58315 | -41.28384 | 2026-08-15 03:55:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 2b6da2ae-77ff-3b73-acce-37e746950c1b | -15.65018 | -48.20977 | 2026-08-15 03:55:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c8084bab-dc03-3f67-bcdf-738f71904bb4 | -18.17384 | -43.99116 | 2026-08-15 03:55:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14904a76-aeca-3414-9336-999b1c4271f2 | -12.73481 | -48.43086 | 2026-08-15 03:55:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f151eb3c-22b4-3c1c-8a60-3f140006675f | -14.44522 | -45.69566 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33703be6-993a-30b0-a272-901485d6968c | -11.48336 | -44.567 | 2026-08-15 03:55:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f1ccf02-7e6e-3a95-9c57-db4b5d64503f | -14.46807 | -45.67797 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 089ca36d-2a9d-3551-b493-40d0ee71db18 | -14.43864 | -45.69494 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d31a21d-a49e-34d3-bcad-719beaee2b76 | -14.42824 | -51.92732 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 18424c33-cf66-3973-9d2c-62028716e732 | -13.6876 | -46.26539 | 2026-08-15 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd9fca52-1641-3e62-8f6d-b8881ea91a09 | -14.91296 | -46.64288 | 2026-08-15 03:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b07651c-f028-3e1e-a992-8833c40a0194 | -12.08575 | -43.1782 | 2026-08-15 03:55:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b3cc86ea-684b-37c9-9867-63af8098d409 | -11.39587 | -46.31978 | 2026-08-15 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a08a426-1aed-3399-8473-385409c84897 | -14.46189 | -45.68287 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 05033fc6-8f76-3676-a01a-55e249a59fa4 | -11.40872 | -46.34673 | 2026-08-15 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 78b850aa-2168-3f39-8f91-96d1ffaaf6a3 | -14.94053 | -46.61546 | 2026-08-15 03:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c74bc08-df75-3452-a296-488c9b553cf5 | -17.9054 | -44.44611 | 2026-08-15 03:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 800c08db-5f5a-32e2-83f5-23856f48dca2 | -10.71436 | -50.55501 | 2026-08-15 03:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2b1d0d0a-27d0-3d20-9296-5a8429c2d9f0 | -14.57854 | -46.77483 | 2026-08-15 03:55:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac55d8b4-e4b1-33b5-b1d9-c8712c8c2d22 | -12.72935 | -48.42632 | 2026-08-15 03:55:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07279942-693c-3da9-bb49-30c41ce4a09f | -11.07279 | -47.22761 | 2026-08-15 03:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6f90923-56fb-389d-bfa8-5ff5ea571eb9 | -12.01662 | -46.4272 | 2026-08-15 03:55:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14372ed5-279f-30ce-9391-6e66f3045f93 | -14.46307 | -45.67695 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7aa0a90f-cbf0-3ceb-b753-34a151a7f78b | -15.92186 | -43.52369 | 2026-08-15 03:55:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eaa28279-920e-3838-9d39-0231448668cb | -10.41108 | -47.98161 | 2026-08-15 03:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 62118667-b916-3d8e-992c-ed8471f628ce | -16.8007 | -42.48737 | 2026-08-15 03:55:00 | NPP-375D | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8685e8a-5b4e-30e3-8076-f321f5a94e64 | -12.72223 | -48.42975 | 2026-08-15 03:55:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 54d210f6-def1-3d50-b5df-ab49209947b9 | -14.42304 | -51.91659 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e908358f-f868-352a-b310-241fe9e3f24b | -12.13596 | -47.17088 | 2026-08-15 03:55:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04d73eef-6279-3a94-8be5-acbac3537f79 | -11.41508 | -46.33871 | 2026-08-15 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b82dcfa5-043b-3e86-8d4c-3465cae04e89 | -14.43197 | -51.91071 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| f8aef335-4cdc-3494-93da-e71f6da00edf | -14.75542 | -48.24684 | 2026-08-15 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ba298be-aab3-379d-a14d-4c0c69ff03e8 | -14.44366 | -45.69596 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3daddaf4-23bb-3e18-86b1-6520329fcd78 | -14.44808 | -51.90672 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7ad3cfb8-0582-3c57-b306-5552abdf5671 | -14.43918 | -51.91252 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 581ddbd1-c782-3414-98af-2de79063b7cb | -14.96487 | -46.63106 | 2026-08-15 03:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7f54141-30e8-3256-9ade-1683c5b6b3cc | -14.44087 | -51.90488 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 50f819b2-87ba-32c8-9049-db180163b0fb | -10.41211 | -47.97655 | 2026-08-15 03:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 18ce6865-ea41-384e-a6e9-66a7b41c6c1b | -14.44925 | -45.69404 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cb14d9f-2231-3fe8-b9c8-ed8d02c43ea2 | -11.43138 | -43.92107 | 2026-08-15 03:55:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9082eab-0334-38c0-9033-bb229d57b0b6 | -16.71144 | -46.40231 | 2026-08-15 03:55:00 | NPP-375D | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f7b8050-44a6-3961-80f4-e4fb7c77b473 | -14.92412 | -46.64222 | 2026-08-15 03:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9d669fa-a54f-394c-b27b-deebf7bd3247 | -11.39015 | -46.31975 | 2026-08-15 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 142b8a4f-996d-37d8-9cff-07742874fdc9 | -11.41103 | -46.3345 | 2026-08-15 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a795164-affe-393f-a124-8bdd30eb2345 | -14.43661 | -51.85577 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e641f4a-feae-31d4-8b57-d52535391721 | -10.72152 | -50.55659 | 2026-08-15 03:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| dc95a20a-c5a3-3752-940e-f7cc89f8dd08 | -14.43462 | -45.69659 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01c1d946-637d-3efa-a268-b066e4b15f5e | -15.10663 | -48.69799 | 2026-08-15 03:55:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14e3bdea-511e-32a8-8bc6-154942cb805e | -12.38126 | -46.41867 | 2026-08-15 03:55:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51e07d1b-64dc-3365-964a-e0eca8f68a11 | -18.58031 | -41.2789 | 2026-08-15 03:55:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 2891b065-24fd-318d-8174-fd060eab5d35 | -14.75849 | -40.85789 | 2026-08-15 03:55:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4382788b-613c-3b9f-9222-eee0a69fdc7b | -13.53718 | -46.25631 | 2026-08-15 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38ac47a5-adfc-3d9c-8225-63cee491c200 | -14.22177 | -45.4111 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 313fc12c-727f-3694-8ff5-ecc7d194b906 | -15.12313 | -48.70246 | 2026-08-15 03:55:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a30e018a-1262-3692-8e25-ff9f04ef101e | -15.65134 | -48.20606 | 2026-08-15 03:55:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8de84b85-3c12-3200-9b16-78a127d65b98 | -12.01616 | -46.42736 | 2026-08-15 03:55:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04dd98f1-a94e-3d9a-a698-c42dc1961fc3 | -14.43748 | -51.92014 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 5be95fd0-904a-3bb2-8384-40cd8dd65331 | -16.83443 | -42.25992 | 2026-08-15 03:55:00 | NPP-375D | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d7447495-f571-3428-9727-cb9ea92c9371 | -15.03659 | -47.03693 | 2026-08-15 03:55:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08f12c64-dbca-3284-b38b-884d33ed6132 | -14.43805 | -45.69792 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da94972c-0a02-339b-a65c-5dca68456368 | -11.36076 | -46.26822 | 2026-08-15 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d3d9aac-e5df-38ac-92ec-2775bc940e48 | -11.07194 | -47.23195 | 2026-08-15 03:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62d98d78-29ba-3f3f-a062-8d9727c9b996 | -11.72569 | -47.00833 | 2026-08-15 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3080e657-7c6d-3983-a3e9-733341dd2793 | -11.40534 | -46.3343 | 2026-08-15 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8faa463d-009a-3de8-952f-2570ef4b350c | -14.93459 | -46.61767 | 2026-08-15 03:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cffdb27a-21e8-3f28-aaf6-f5fca04a3459 | -11.40055 | -46.32933 | 2026-08-15 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 85a3840a-938e-3015-b740-a391ccbb2d27 | -14.91375 | -46.63904 | 2026-08-15 03:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98b8f59e-c822-38b6-a9f0-fca3f6493067 | -14.96058 | -46.62506 | 2026-08-15 03:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c76208f-cf91-351d-9c6a-7ab6e6d5206e | -12.14254 | -47.16788 | 2026-08-15 03:55:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fb740d1-95f2-3e6c-9e9f-90fc69e5e287 | -18.45012 | -43.43556 | 2026-08-15 03:55:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 24acebc5-8e8c-3ad5-8f58-b6ec680bbbd4 | -14.91896 | -46.64046 | 2026-08-15 03:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22983510-7d5f-301a-a512-a0a15822dac4 | -11.41351 | -46.3467 | 2026-08-15 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 44254928-58a7-3c38-85a2-40de492a5f4d | -13.53867 | -46.2487 | 2026-08-15 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 545cce5d-79fa-3cff-a982-2023c437b017 | -14.9597 | -46.62943 | 2026-08-15 03:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8870b508-6798-303a-bded-c854015f7d3b | -14.6235 | -40.85815 | 2026-08-15 03:55:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 57169a23-9977-3c40-af64-ec54eda7ba8d | -15.06102 | -48.67084 | 2026-08-15 03:55:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c9d3bd0-704f-3b92-93e0-154e90263685 | -12.38065 | -46.42173 | 2026-08-15 03:55:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b290f7d-c721-3663-9509-d68d10a4dbfc | -17.90456 | -44.4505 | 2026-08-15 03:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9af7fe77-6aac-3a69-ace8-8541947375c5 | -14.40223 | -48.95951 | 2026-08-15 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6ede188c-b59e-36f4-bebb-00729f05899d | -13.47622 | -44.03748 | 2026-08-15 03:55:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d6a5f44-c4e2-3693-921f-67da9097420d | -14.91929 | -42.04335 | 2026-08-15 03:55:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1ab0dfc8-0f00-3bf3-8ad6-26d1f229a84e | -14.44992 | -51.9326 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9ec175dc-8bce-33a9-8fcd-02428de45792 | -14.44483 | -45.69005 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6f5c800-b268-39ca-ab11-bac894d7557b | -16.11047 | -49.86225 | 2026-08-15 03:55:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ba32e2d4-a773-377d-a528-0e8fe95b4ce9 | -18.57958 | -41.28306 | 2026-08-15 03:55:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 43be3d2b-af35-3240-bec8-f935942cb8c3 | -14.44444 | -51.92317 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c6702f29-bc50-3306-add0-c548545fa637 | -13.68303 | -46.26066 | 2026-08-15 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c42fcb13-8fff-3e5f-9738-d499455072d8 | -11.40454 | -46.334 | 2026-08-15 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7f17c152-9906-35c0-9f19-dba5343e86b0 | -10.52492 | -44.85206 | 2026-08-15 03:55:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd394dff-76b6-3ef2-a47e-82da5b80652d | -14.45306 | -45.67488 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c48e5b76-bc05-32b4-9f70-645ee033d2c7 | -12.14172 | -47.17199 | 2026-08-15 03:55:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33e1a5b9-246f-3628-a851-3c6801ad9c23 | -11.40941 | -46.33839 | 2026-08-15 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0ded21e0-0bf4-303c-acc7-76e12d171b73 | -16.11566 | -49.86864 | 2026-08-15 03:55:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 463e681a-1b94-30d6-834b-8a5a0d9c812c | -14.91661 | -46.625 | 2026-08-15 03:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6af95385-6a77-357e-8ab3-e4b430703b63 | -15.06199 | -48.66627 | 2026-08-15 03:55:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b71b4153-a1e4-311a-81a8-c9c71459863c | -12.72854 | -48.4302 | 2026-08-15 03:55:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5fdaac10-9cda-3a6f-9e85-2769dd2c93f6 | -14.43303 | -45.69691 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fd3c10e-18f8-343a-aaf9-3e2ffbccbbef | -18.58389 | -41.27965 | 2026-08-15 03:55:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |


[Clique aqui para ver as próximas entradas](README11.md)
