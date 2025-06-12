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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae23eae4-7774-3c68-993c-86939d055628 | -12.09108 | -57.37285 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 32a2675b-c98f-3831-b6b0-574cbefbd8db | -10.95059 | -55.32183 | 2025-06-12 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03fb297f-c6c0-3816-89ec-86a7b943a8ec | -11.97099 | -49.57359 | 2025-06-12 04:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee011723-feb2-3395-999f-36bf1f912d40 | -12.13521 | -54.66523 | 2025-06-12 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94fb7691-2cc7-3eb5-b4f1-19160044a670 | -12.46742 | -58.47128 | 2025-06-12 04:29:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 995c2f53-0f1d-311c-8b55-c401947e9b9b | -12.23394 | -44.16234 | 2025-06-12 04:29:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 554ff546-c8b3-37b1-8931-2a51bd3803c9 | -13.29358 | -57.07604 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0c2165c-3bb6-3984-8efa-fa8350a2c2d6 | -12.82748 | -47.37818 | 2025-06-12 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a75c7b9-48ff-311f-84d8-c887ffecb8a4 | -14.65753 | -48.06957 | 2025-06-12 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff397f51-d55c-3f54-855b-f6e0f0d5fbbd | -14.8266 | -54.65678 | 2025-06-12 04:29:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5cc259bc-700c-3c55-b089-849115cee102 | -14.03051 | -55.12333 | 2025-06-12 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0dbafbfa-a8da-3247-81f9-a83be74a174f | -13.71706 | -58.67712 | 2025-06-12 04:29:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f00dc96f-d62f-3eea-aa61-d21536ef0994 | -12.62945 | -54.06597 | 2025-06-12 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0f7b358-bfcf-3796-9fba-0e03640b7ab7 | -13.88938 | -54.64659 | 2025-06-12 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5278fe2b-b807-33f0-97c5-cc396bff8c6c | -13.56695 | -44.27171 | 2025-06-12 04:29:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e14639e1-2b60-3966-9f42-40ca5d16ee7f | -12.38255 | -45.77216 | 2025-06-12 04:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d334555-03c9-3de6-af52-57c88a30abcb | -15.37383 | -47.87418 | 2025-06-12 04:29:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88b5963d-1f1e-3e87-bb12-894a36416218 | -13.28709 | -57.08144 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a0ec5d9-22a6-3abe-84da-47e30f764f3f | -13.28899 | -57.0715 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e551fbd4-cc7c-3884-a274-171bef7cdccc | -11.0665 | -55.04483 | 2025-06-12 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55f241fb-16b6-3dee-b59c-2b6913764718 | -12.8236 | -47.38119 | 2025-06-12 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63dd4ee8-afc4-31a7-88c7-f344f24e091f | -11.56727 | -51.3022 | 2025-06-12 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed011166-981e-300d-9d62-df9dcaf21081 | -12.17517 | -54.23509 | 2025-06-12 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 196bc34e-1310-32c4-a324-1a9a2a7ef6f6 | -10.94957 | -55.32731 | 2025-06-12 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7ded7ee-edad-3077-b7e4-7ba44b8c0fb5 | -12.21238 | -49.6371 | 2025-06-12 04:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56ed9145-6e6b-3c68-b5c7-b4fd2eb6fd2f | -13.71723 | -58.67957 | 2025-06-12 04:29:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26868540-6518-3ae1-9fec-95f1bbb890dc | -14.16997 | -45.4882 | 2025-06-12 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e5bdbe2-1e92-30e5-9ab9-760cef99032e | -13.65238 | -53.94252 | 2025-06-12 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1de0ae58-d9dc-3f40-b671-f37eaf3f346e | -11.83875 | -43.79743 | 2025-06-12 04:29:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56a7d5c3-32f2-389a-8749-8b31db4ae768 | -13.89832 | -48.73893 | 2025-06-12 04:29:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3891e043-1472-341c-b5a0-4f50a979c10a | -11.77032 | -54.36971 | 2025-06-12 04:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78c5e1bb-0b1f-38b6-902d-1851e8373528 | -11.00904 | -49.57812 | 2025-06-12 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8f9f791-80fd-3a84-a674-6f264bbe1bce | -15.37938 | -47.88246 | 2025-06-12 04:29:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46d3f342-24a8-3522-bf4f-da3ea0cf3b0f | -13.89662 | -54.65702 | 2025-06-12 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ef4bfccd-0b66-3f79-973b-f4e99b9bc32f | -11.83808 | -43.80196 | 2025-06-12 04:29:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16616c8f-2e66-31d8-b53c-71e314a47be1 | -10.36611 | -57.23408 | 2025-06-12 04:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ee87021-f31c-3824-9198-beabdb6c3e3b | -10.36753 | -57.50129 | 2025-06-12 04:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fb77352-ef01-32d4-b31c-936154077c3b | -13.89549 | -54.63848 | 2025-06-12 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 54f1befb-7760-312e-ac1a-463c4b5a0fcf | -13.9711 | -54.42647 | 2025-06-12 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e35aaf2-8607-303c-acd6-80cc20a4dfc5 | -14.17349 | -45.48875 | 2025-06-12 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b84f6b3b-6349-3c04-a1d8-6f5f33d3202d | -13.52978 | -47.85958 | 2025-06-12 04:29:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65eaef81-b973-3434-b8bd-4b52c8a9ddae | -13.29296 | -57.07407 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ef157de8-16d1-38f4-8d59-5862114234ac | -10.36537 | -57.23789 | 2025-06-12 04:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 580b04a3-9f17-3a02-8268-94fe3a2c9c51 | -14.17702 | -45.48929 | 2025-06-12 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a9fa0d7-8b7c-3bde-84c7-cc5699e5faf6 | -14.18115 | -45.48581 | 2025-06-12 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18b1cef2-a809-3c13-bbaf-cb49347bd558 | -13.28773 | -57.0781 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57c34717-002f-3aae-9be1-ea27058baeb9 | -14.17995 | -45.49387 | 2025-06-12 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a3974d9-f897-3db2-906d-7e5cdbb17fe3 | -13.90777 | -48.73667 | 2025-06-12 04:29:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cebe1c63-7fca-335f-8453-49b5a3d76eca | -12.09039 | -57.3764 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a928c77-34d3-365f-a8d1-6fc8f9a68cd8 | -13.28961 | -57.06826 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 275f0804-1681-36b7-9083-7694b3faf412 | -12.82124 | -47.38091 | 2025-06-12 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c3ed62b-518b-36fb-b05b-d0fc8868cc66 | -12.08493 | -57.37522 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72348ed4-1843-3c68-83cd-7c7b543863b9 | -10.8839 | -54.75029 | 2025-06-12 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 34f80433-6d18-3e76-8c14-35df1864467c | -12.20894 | -49.63651 | 2025-06-12 04:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00cdb863-159d-3d6b-b862-268f4f612e21 | -13.64812 | -53.94175 | 2025-06-12 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d742a495-08be-36b1-8399-0c0707266082 | -14.03697 | -55.13927 | 2025-06-12 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c43739d-d55d-3baa-9866-906a1e19036e | -13.52922 | -47.86312 | 2025-06-12 04:29:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd6cd2c5-20d3-3742-b04c-225e4f514bb2 | -11.8149 | -46.56676 | 2025-06-12 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 656020f4-e5fd-3207-8c11-d48ea6a52a43 | -12.21301 | -49.63329 | 2025-06-12 04:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1a6b590-bc4f-3f00-81e8-e1492f8434e6 | -15.38605 | -47.88354 | 2025-06-12 04:29:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10430e75-247e-31ed-bbbb-078349dca474 | -11.58072 | -47.44147 | 2025-06-12 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 03abcafd-b049-3bda-b1f4-d65c7c1867a9 | -11.84248 | -43.798 | 2025-06-12 04:29:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd401d61-330d-30f1-b44b-ae824811e19f | -14.0333 | -55.13362 | 2025-06-12 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d167cc7-d3ab-3604-9d16-ce78007db164 | -12.13943 | -54.66278 | 2025-06-12 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49eca36b-57f5-36e0-b292-7554f94b49d6 | -15.92931 | -42.9079 | 2025-06-12 04:29:00 | NPP-375D | SERRANÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3166956 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af0af4fc-fdcd-38c1-801e-d231a600a65e | -13.29489 | -57.09184 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c6b0d9c8-f388-3800-8fd1-63fa36143b18 | -13.49491 | -53.49113 | 2025-06-12 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eaf60d90-0dcb-3d59-9ad7-92f78e64364e | -12.39784 | -46.42799 | 2025-06-12 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d695951c-f1cb-32b5-b8da-8063464b6407 | -10.99139 | -50.75662 | 2025-06-12 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce329b44-509f-3ead-859a-57aa1778bc63 | -14.02963 | -55.12801 | 2025-06-12 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd714037-9b77-3c65-b068-9a9050f3a1d1 | -10.87242 | -54.32233 | 2025-06-12 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a64f3c9-66fb-3751-b43c-3a23e386fa26 | -13.29622 | -57.08517 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2f0d8097-5e91-3f1e-a64b-be88828d1d58 | -13.89299 | -54.65183 | 2025-06-12 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 45d17083-8654-3ed9-8f4a-2317832c2144 | -14.65421 | -48.069 | 2025-06-12 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ca06f34-c58e-3518-a02a-01c1577f584d | -11.37241 | -55.11584 | 2025-06-12 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1808def-07c6-3ca9-9e9f-380123e7c5ef | -13.33015 | -40.30918 | 2025-06-12 04:29:00 | NPP-375D | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a8cd30c0-26f9-3c22-bd20-b381269e52ad | -12.05159 | -48.07886 | 2025-06-12 04:29:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f47a09e1-47ce-3278-8396-6b3d43e28ccc | -17.10658 | -50.07468 | 2025-06-12 04:29:00 | NPP-375D | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2f001375-76c6-3847-9e90-51efdbcdad73 | -15.0793 | -48.94339 | 2025-06-12 04:29:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd129ca5-c48f-347c-83fa-119febce6b26 | -16.6818 | -43.88565 | 2025-06-12 04:29:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d4163fa-ec61-37f9-9bc5-aba5c04cb139 | -14.84512 | -48.31286 | 2025-06-12 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce79c60a-c1a5-327d-84fb-deda49fae9d5 | -12.83081 | -47.37872 | 2025-06-12 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cc8ba11-d21e-3da8-a339-2a66b7e0d67d | -12.13605 | -54.66055 | 2025-06-12 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3a1732c-a852-34ff-9dbc-93dc5315300a | -12.70923 | -58.03641 | 2025-06-12 04:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4b47e863-8786-32ee-8f03-414d806ca824 | -16.68002 | -43.88398 | 2025-06-12 04:29:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28cdd07e-dadf-3e6f-a235-6bb2a379bfc4 | -13.89826 | -54.64818 | 2025-06-12 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7c048a35-f291-31ef-a08b-bdf39ad351f0 | -13.89382 | -54.64739 | 2025-06-12 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 935bd262-1510-352a-8925-64d2ccf7cca4 | -11.13656 | -53.94814 | 2025-06-12 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8dbbacc8-98d1-3b03-a9e0-00b107ad77c5 | -12.43416 | -54.87589 | 2025-06-12 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38a72c8c-1e0b-39bc-9bc5-cf9e59fb312c | -11.13611 | -53.92504 | 2025-06-12 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1ccd2b4-1b0f-34ff-bca3-d888913ced8b | -15.37271 | -47.88137 | 2025-06-12 04:29:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96cd3e79-eacc-37f7-8977-f16049accb83 | -13.89909 | -54.64376 | 2025-06-12 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4e8b3c4b-5e24-3af1-b887-6f647cfc3e6c | -14.18821 | -45.4869 | 2025-06-12 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f0fca1c-222d-32f0-b8c9-d5911986e489 | -13.66087 | -53.94415 | 2025-06-12 04:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ceb0f298-1a63-3b1a-902b-c4f78acff4e7 | -11.3859 | -56.55554 | 2025-06-12 04:29:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98802794-29d8-3254-a509-e1d1150d71d5 | -13.29556 | -57.08849 | 2025-06-12 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f1cb527d-c8b1-327c-8f0e-c4e201d398c5 | -13.89465 | -54.64293 | 2025-06-12 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5422c2e9-b5c3-372f-b632-55d407d18ea7 | -12.43506 | -54.87109 | 2025-06-12 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f9a464d-9d93-3c97-b8fe-56f5f5ed3bf3 | -11.84182 | -43.80253 | 2025-06-12 04:29:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 733e7780-feb9-3fc6-b1be-5a0ddddd32a0 | -15.38549 | -47.88713 | 2025-06-12 04:29:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README14.md)
