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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ac00b40-3af4-3167-bbf7-9a7a2741ffb4 | -9.80341 | -47.76123 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3fee80fb-cc22-3291-965f-6f8ba6d2dad1 | -9.81338 | -46.82329 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7585fbb-dfd0-3526-846f-e41537ad406f | -11.34464 | -46.48684 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 287182fb-4266-3ef4-af8c-961acfb8f96d | -12.52749 | -45.34999 | 2025-09-11 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46458229-3503-3bd4-a690-2502100fcb78 | -12.10267 | -51.01608 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d07d1b10-9637-3b39-b872-254ecf520215 | -11.35238 | -46.50272 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0148fce-e799-3579-88ff-832254aff570 | -14.06002 | -42.16805 | 2025-09-11 04:23:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c3cfff90-b10b-3f8a-b216-59f199e1590b | -12.8438 | -52.95941 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 14f06ce8-9317-3a5d-94e0-328016745024 | -10.5406 | -49.88899 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 376d34ab-97d9-3418-a0b2-4c8827d8beb0 | -14.56627 | -48.768 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4554e518-5b88-3f7b-a023-eea56e5e237e | -9.98757 | -51.70044 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac4c06e6-38f4-33d0-8f55-4fd49cf6f8c6 | -13.29139 | -43.76354 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb984769-3b02-3751-b8e6-9b55be3b25b1 | -12.04969 | -47.55124 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7e51f2a-bc7e-370d-81bf-6f9b22c4c14e | -9.06801 | -47.0461 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b14e136d-426e-3047-bb7c-0d167a1c7f33 | -13.78769 | -46.28265 | 2025-09-11 04:23:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fe95db1a-d048-30d4-b29c-8ee1102576b6 | -14.41689 | -47.32583 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 98506269-4a1f-3986-85ca-628dd0addf5c | -12.017 | -47.58007 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1e01d1c-8c37-378b-a0a8-611258e93990 | -10.54142 | -49.88417 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba0e371c-777b-335d-87ac-9643d081c9bc | -14.39799 | -47.31517 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| af76e0ca-87fb-3f55-b917-89ebecf172b3 | -12.03941 | -47.61452 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97f9a6f3-414f-3c69-92c5-2ec9505b732e | -13.954 | -48.21018 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80c3784c-8c8a-3977-9542-19903636022b | -12.14145 | -44.85892 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3f4fa982-6e70-320b-8b78-1df6c7ff1c83 | -10.77911 | -46.00288 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d8a2d175-0bc9-3975-9175-9ccc7576cc27 | -11.36111 | -46.56598 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c603668-8f4f-3f68-b5e6-7210421ee91f | -12.036 | -47.61395 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b432bb6-2f1d-3ec2-94f4-0527d4eaae23 | -15.22341 | -44.01923 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2982118e-8821-3025-8a92-9645b6ad3a34 | -14.85106 | -46.79077 | 2025-09-11 04:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9046863b-4130-3b1b-b9df-91b9f82dce56 | -11.36628 | -46.53392 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 104aff96-6b6e-327b-9ed7-0b759dc05961 | -11.34186 | -46.48276 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4849628b-d06f-3485-97a4-536406da5e90 | -12.16413 | -48.48298 | 2025-09-11 04:23:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a8435ee-18ca-3f5b-a419-cc21a04dbad1 | -9.59001 | -48.07188 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcbf245f-eb35-35de-9394-3f438180a2f9 | -10.13835 | -47.89553 | 2025-09-11 04:23:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e84a2a0-2d14-3f3d-a7ba-fa35c00305c5 | -9.70069 | -43.54162 | 2025-09-11 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 168c63f3-0e1e-3fb3-a768-153490e0a6d9 | -11.16988 | -45.27932 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28ba520a-d706-3d4c-beac-f1a2a55e7f1f | -12.1008 | -51.02679 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 026eda85-d902-3bd0-85a3-2d8bb7d70a37 | -9.02592 | -49.52611 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b959fba7-7962-34c0-a791-244cafad2f76 | -14.30038 | -45.04006 | 2025-09-11 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 402ed4e4-f300-387b-8f2e-40ffcf4f5bad | -12.5658 | -44.64093 | 2025-09-11 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7dfc34db-e073-3492-a446-7f648d3e8c3c | -11.47686 | -43.62306 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f22aeb34-9cce-358d-a52e-b187b4ddeb89 | -11.14818 | -45.24324 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3389a33-fb47-3fa7-86f5-4d341fa56964 | -13.13533 | -54.91672 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d9feb38-958c-3464-9c43-0bf55d92c523 | -12.00556 | -47.58577 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51abd8b2-88a7-30f3-a737-d2f4e169db45 | -9.3827 | -46.76458 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 433db105-f8a8-3c41-8db2-787bf6ba8cac | -14.22407 | -43.0886 | 2025-09-11 04:23:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 81a474b9-df4d-3502-95bd-6b51b87f0edd | -11.359 | -46.5257 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62ab3829-c890-3f04-a8aa-31403095d7d7 | -11.11007 | -51.99929 | 2025-09-11 04:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 48036508-5b4d-3b79-aaa3-7be55fd9d68e | -9.8925 | -51.88241 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 827f16e3-2122-3095-93b0-3e59956e0546 | -14.9205 | -47.32493 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 84473819-ec47-34a2-baf3-b8c0647d4d1c | -11.4837 | -49.25937 | 2025-09-11 04:23:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb19abaf-bc57-3ce1-8ba5-93375c8a5405 | -14.3583 | -41.85912 | 2025-09-11 04:23:00 | NPP-375D | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8283a68e-be56-3ed6-ad66-88f4fa24d0de | -10.7306 | -46.13599 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8afd1f8b-b8e8-31c6-9691-10fab751feb6 | -11.09359 | -48.44888 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb539c18-e17e-38ce-9d61-6e9482568b86 | -13.84133 | -44.46038 | 2025-09-11 04:23:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ffcaa45-2594-33b8-94df-9a523a7303a4 | -12.93351 | -54.79863 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07e7afa2-f51a-3cf1-88f7-59d4e784b45f | -11.48791 | -43.67897 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 86ced4d8-5038-34c3-b3a6-344a4ad9ed71 | -9.52061 | -54.64348 | 2025-09-11 04:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65662841-b127-33f2-bd06-fac063af77eb | -12.58507 | -44.78661 | 2025-09-11 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c63bdb55-dbcd-3511-a2a1-de2bac7a47f7 | -8.89348 | -51.05824 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5635626c-fd8b-3cd6-a9b9-d78977392d4b | -11.14909 | -52.03313 | 2025-09-11 04:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6dcab0a1-61f3-36f5-b344-3ef989b90cfe | -12.93477 | -54.80796 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8a6af7d-efc5-38e0-af4b-6f3ffc577895 | -9.1348 | -46.19381 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5547481-48f9-3828-8376-a07012688180 | -11.94839 | -46.64441 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32362805-f7fa-3e39-84c0-e883a9aa8ba9 | -9.6744 | -47.53111 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d44f7d35-7f2e-37f6-91b5-6dc6beb4f4ef | -11.71919 | -48.24857 | 2025-09-11 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 422cec5a-2674-3962-a61b-6d1edba08386 | -14.38664 | -47.34284 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40ad8dd7-323f-3c7e-b967-b3880ee52103 | -11.71334 | -46.50324 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9b64211-b578-350f-98ff-15a4fd01297f | -8.08574 | -54.74829 | 2025-09-11 04:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81cf5951-1f75-3b6a-aec6-1ac44162cbe9 | -11.19949 | -48.39933 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6053e251-4e34-3ff3-aeef-67ed4fdcfb77 | -9.0646 | -47.04545 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3fcd67d3-1f87-3451-b72f-9f4ae0d8c0f0 | -8.08151 | -54.74011 | 2025-09-11 04:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e6aa21b-85b9-38ee-8ed0-a6a749b05606 | -9.13146 | -46.19323 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2bf1db04-4159-37e6-ac3a-04a57f323af8 | -12.97464 | -48.02364 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be70a156-77c3-38b1-b282-8183acc0c199 | -11.6565 | -48.32288 | 2025-09-11 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63cd84e8-8c11-35f3-a21f-42d91ee3c665 | -11.65487 | -46.90838 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 680c3409-c592-3257-a843-1cf410189ea7 | -9.7127 | -43.53197 | 2025-09-11 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65d545af-b266-311a-b111-2105e8e4c94f | -10.54 | -51.50971 | 2025-09-11 04:23:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc33b0f6-788a-3584-bbb2-123ad0786f4b | -14.14038 | -45.40232 | 2025-09-11 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e80d2dcc-5584-3ee6-89a7-f9a8be43f169 | -14.41239 | -47.33241 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14a6e077-2c0b-3813-9e79-e8728506e181 | -9.03337 | -49.77082 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b778950b-aa10-3218-9db8-2f9a36eb4337 | -11.35959 | -46.53287 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8de33bee-b729-35f4-9f4e-b56a59853bdb | -11.38778 | -43.52322 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f1202c9-2643-3688-b412-1b5c7c1ade8c | -13.29669 | -43.75216 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16789c93-fa38-30c6-a9af-650a64886219 | -14.34166 | -45.06547 | 2025-09-11 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79e307d2-3621-30b0-b2a0-832b7b8b1e59 | -11.47928 | -49.26314 | 2025-09-11 04:23:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74b465c0-a877-3a4d-a6b4-ae0d0da8fc3b | -11.77348 | -46.49133 | 2025-09-11 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1188685-19c2-3298-84cd-a2fe075060e2 | -10.54292 | -51.51798 | 2025-09-11 04:23:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d106255-1cbb-3b3a-97c6-853e53675396 | -12.00216 | -47.58521 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42ab49f0-748b-3ea9-bd9b-6f4bc2112d26 | -9.09324 | -46.9554 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24cb0cb7-d5ed-3d48-8a42-b6ad3f429792 | -11.65881 | -46.90533 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f86335f-48ca-32ab-a6c3-f7b488f760d3 | -15.22813 | -44.0366 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bbfeed1c-ba72-3aad-95de-c85cbf5eb4fb | -9.12084 | -46.1951 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36ff2b13-b6fa-3249-a86c-25a59419ac2d | -11.47452 | -43.63846 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d4403ce3-9809-37dc-8f32-333addf66f81 | -14.44254 | -48.4257 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebd189d7-cec1-337b-99e9-4501fc7712e0 | -13.65655 | -45.71684 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38c4794d-9484-35fb-9ffb-3754c3f302ad | -12.97586 | -46.73259 | 2025-09-11 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 94d1811a-45da-3932-8457-b99b73c67c4f | -14.41632 | -47.32939 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ffce312-7f8b-35ca-974a-72e69be7c089 | -11.08418 | -51.34617 | 2025-09-11 04:23:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1af911fc-de63-3601-bf1a-4f1fd1088f65 | -9.67986 | -47.52775 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9956f21c-f18c-3aaf-bebd-e0f83dc0a413 | -11.16269 | -45.30348 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18ccac14-7c76-3ba9-b9f9-fb3b89ce0a6a | -9.67625 | -47.51969 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README64.md)
