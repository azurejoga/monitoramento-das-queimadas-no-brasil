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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76d272e3-d92c-3985-b283-c3003b525abc | -12.70767 | -46.30838 | 2025-10-29 04:25:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 08f2b202-75db-3244-af4b-d7423f51e01d | -15.11266 | -43.26519 | 2025-10-29 04:25:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d3875bd5-a8c7-3c1f-b6b5-4ff57913a8ee | -13.55056 | -47.32218 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f20708a-1756-32a6-b705-5915bab9bb05 | -12.76657 | -46.65995 | 2025-10-29 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 12f464c6-555b-38cd-a322-d5649b21f841 | -17.53809 | -44.61794 | 2025-10-29 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a680b66-bce7-363a-92e0-da17652c22bd | -13.63854 | -47.04572 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5655aedc-4e0c-3236-86d9-b7f0b44418ec | -15.18216 | -47.23722 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ed4f367f-2a2b-316b-b599-31799622e58c | -13.91208 | -48.46761 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1a520c5-2d9b-33eb-a61c-0854301c43cd | -11.07808 | -48.3278 | 2025-10-29 04:25:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 58576425-65f9-3fd0-8b84-855c15602622 | -14.2715 | -47.32015 | 2025-10-29 04:25:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 80a701b9-3c88-366b-808c-1912d215aebf | -15.1645 | -47.2194 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f768b3a4-a63a-3c15-ad75-ea01e00317a0 | -12.1848 | -46.72064 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80ad0c97-988b-3cc4-b655-e498f4dc99b9 | -15.45792 | -47.69047 | 2025-10-29 04:25:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09ed5959-56fa-3843-932b-fdae23c7aac7 | -14.60332 | -48.42712 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| beb04a7e-cff6-39fb-9bf7-b4cd3151bd15 | -13.39566 | -47.50396 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe38c05e-0921-38f7-a3f8-3fe5b0302dd8 | -14.98539 | -47.86884 | 2025-10-29 04:25:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 26d342fb-f616-35f9-9a8c-171b1c959917 | -13.62554 | -46.46955 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d0da650a-f5f0-3578-9928-50f29adfa47f | -13.57982 | -49.60114 | 2025-10-29 04:25:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 774d9e6c-f95a-3100-962a-b93db8884c9f | -13.78811 | -43.25521 | 2025-10-29 04:25:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f0b890fa-a36b-3a59-9fc3-999a43f1ce3c | -18.92567 | -45.03624 | 2025-10-29 04:25:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 22c5b4b2-be96-3cf8-b908-a00c2a610d5b | -15.1684 | -47.21637 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34b27707-2ddb-3457-beb2-86b69bbe8bf0 | -12.18871 | -46.71764 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ea7774ae-cce1-3212-9abd-79fd167cbcb7 | -15.20891 | -47.21959 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cdc1686-894d-3e74-8d9d-246dac827696 | -14.61757 | -48.42596 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d6508cf9-9afa-3ac2-8f6f-a5e4b2881f49 | -14.59548 | -48.41486 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3eec7893-e872-3d21-a2a9-cc3013c3972f | -13.64041 | -46.50479 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76ed1824-2eb9-34e0-b7d0-0d545df211b4 | -11.02177 | -47.84348 | 2025-10-29 04:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 723d47c8-fa70-3090-a14f-6fe6c3b65c7b | -11.78731 | -44.16181 | 2025-10-29 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c030a653-cd74-366e-8882-5b5e6d8a6475 | -12.10003 | -47.17052 | 2025-10-29 04:25:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8177d99e-00b4-3682-9d34-18f637991719 | -14.66397 | -50.18777 | 2025-10-29 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6fb80c54-91f3-3d2f-8367-affd8edaf089 | -13.2344 | -47.99652 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 344c42fb-ff38-36a3-aa17-6ae00a4ed360 | -13.26672 | -47.73506 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31f5f5f1-68b2-3e07-be45-acf1a34da88a | -13.24777 | -47.05785 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7aca928-787d-3045-9b33-7176a14c0008 | -14.8884 | -46.76199 | 2025-10-29 04:25:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5822072b-e748-39dc-a257-2117c8af805c | -13.24961 | -48.01055 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdd02633-3697-353b-9c10-529339421b42 | -12.07997 | -47.99885 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| efc660e5-5bc3-3a4e-99ef-f5b4907028cb | -12.10804 | -44.59763 | 2025-10-29 04:25:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93b7d5a0-8e61-3fb0-80b8-bb25af5c2a5c | -11.28974 | -47.55558 | 2025-10-29 04:25:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94cb151b-8a68-324c-bee3-b2cbffc1be2d | -10.90312 | -49.4744 | 2025-10-29 04:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd69ae55-4958-390a-9dfa-09570b737a07 | -13.87737 | -48.48472 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81594ad2-1099-3d94-b9e9-d56d9335261a | -12.68822 | -48.44267 | 2025-10-29 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cabe42a-b590-3ea0-a831-cc1a6a6c1fa5 | -12.32315 | -46.9161 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 133aea85-44e2-3807-a1e1-8bd31bd9ace1 | -13.81768 | -41.69263 | 2025-10-29 04:25:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 346d342d-668f-3fd6-819e-cfe59d2c4f9f | -11.97394 | -44.03105 | 2025-10-29 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a421fb99-16a4-32b6-811d-3a20d203a55e | -11.97655 | -49.94002 | 2025-10-29 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91308758-99e8-34c8-b1dd-45923ea8648c | -13.2462 | -48.00997 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 226d665c-07a4-395b-b5b7-730397a0fdbd | -18.20333 | -44.33243 | 2025-10-29 04:25:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc9bec19-1cfc-3467-9696-a1470dd4846d | -13.22552 | -47.73188 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07e74e9e-ac43-3b4a-a290-f237e7325981 | -12.292 | -47.00285 | 2025-10-29 04:25:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 840152a3-34d3-3552-a098-44e64a3b977d | -17.20527 | -47.00417 | 2025-10-29 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c802edf8-1bd6-3926-a94f-95c2e49e60d2 | -13.24026 | -47.72676 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55341c18-bd3c-3084-ba4e-03f70978f5a7 | -12.70711 | -46.31192 | 2025-10-29 04:25:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 221bf11f-7b9a-319c-ab80-7144be5b6b22 | -13.64477 | -47.02835 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c64ba92a-0df5-3025-895a-f63f604a2441 | -13.94427 | -48.47753 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0678aed-490f-3cdd-ab8b-fc92d8822b3a | -13.55728 | -47.15284 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 302becf8-8caa-34c9-afb0-fe9981c70350 | -15.10729 | -47.93552 | 2025-10-29 04:25:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7b7b10b-a7d4-32be-8937-686a57f25981 | -10.85559 | -50.12724 | 2025-10-29 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2459087d-3f39-3069-b599-4dbf644ff0b6 | -12.07691 | -46.3829 | 2025-10-29 04:25:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6c6724d-044d-35c6-a8f9-c1294f42a813 | -13.55786 | -47.14923 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0382857-8d62-3c19-bb16-5d151e2e3267 | -11.33713 | -46.07402 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25ea9f91-2878-31be-ac8f-409bb80e3222 | -13.37103 | -47.42205 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fbb488d-3cce-375a-9302-2e66a51358d8 | -13.55543 | -49.56964 | 2025-10-29 04:25:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a4b07363-a60e-3f33-89af-b1372f75d374 | -11.35882 | -47.02274 | 2025-10-29 04:25:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4cbc86c-0f72-351b-8a62-c8a46c32d453 | -13.86291 | -48.4865 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd7d2fe3-b006-3bf2-9b44-e59647797ea8 | -13.86229 | -48.49021 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47232782-4a09-349b-8f85-fbb3fe0728ee | -13.35447 | -47.38636 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbede581-d1cd-36a9-bddb-9d2d3b80c24b | -13.24722 | -44.1104 | 2025-10-29 04:25:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69c07ee1-abd0-3d19-8dc0-8fed0a19b4f3 | -13.64205 | -46.51599 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07dfee6f-e15b-399c-b779-f9cb2f2adb69 | -14.60386 | -48.42803 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37a3d0ab-c1bc-36f4-a0a5-a05e6fe68166 | -13.64201 | -47.02421 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38a486be-bfdc-388c-af06-dcafa07d631e | -11.40056 | -47.75499 | 2025-10-29 04:25:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 930e7d1a-731a-31c3-8ab2-7956cb1799f5 | -12.01 | -46.77992 | 2025-10-29 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 028bb9ce-8903-3f76-96d0-718c86887764 | -13.91956 | -48.46521 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c580f0a9-841e-344f-a712-e3bf53d684c6 | -14.65335 | -48.40097 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8d53b2cf-80c4-3755-ba5b-a08a5edc4445 | -13.03576 | -46.73689 | 2025-10-29 04:25:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7daa744-db34-3522-b0b1-c815ae03ec0d | -12.70491 | -46.3043 | 2025-10-29 04:25:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ef5ce416-3d1a-3b50-aa3c-8c940d4870f0 | -17.53102 | -44.61682 | 2025-10-29 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ce47817-5fa5-389d-86d8-d675986df9f3 | -14.31456 | -46.52133 | 2025-10-29 04:25:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47674af1-07fc-34d1-a852-c7a55f53b8e9 | -14.60819 | -48.40166 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95756fed-b95a-3921-aceb-e6a325701adf | -12.19538 | -46.71875 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| dbf1f3a4-bd66-3074-bc57-681907509c42 | -12.68949 | -48.43503 | 2025-10-29 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3d068e0-7143-3177-9fd3-d7d10b397902 | -11.7343 | -49.33445 | 2025-10-29 04:25:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8eb95ce-be64-3e0e-b9a7-3d8221c6b896 | -15.18158 | -47.24082 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33934daf-e6b9-3952-8575-19840ebc29dc | -11.93458 | -51.33817 | 2025-10-29 04:25:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5526ed4-7610-3164-b2bf-782394d479b5 | -16.67613 | -41.35652 | 2025-10-29 04:25:00 | NPP-375D | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 162e82f4-6c59-37b3-9408-678407943a45 | -13.63985 | -46.50834 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e82936c8-1471-3135-b458-2a80759ce964 | -10.97835 | -50.25219 | 2025-10-29 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03acfc24-b14b-34d5-937e-f0301917d11d | -13.23659 | -47.06341 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c009453e-2f19-3912-b46b-9d0757a57232 | -17.13408 | -45.37746 | 2025-10-29 04:25:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d32e6df4-f937-3d12-8ccb-d889249c133c | -13.22154 | -47.73492 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 902bfa59-c19b-3699-aab2-640c5ffa28f8 | -11.40792 | -51.38697 | 2025-10-29 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e5f3b64c-bee5-37d3-bf5d-3577a9a1b85a | -13.63822 | -46.49714 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26b860d3-61e5-3282-8c04-14b8997a66dc | -10.86455 | -50.09878 | 2025-10-29 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a597b55d-0ecb-3344-8469-e23c7460c337 | -13.69437 | -47.68561 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65dad658-f34f-386f-b187-e58cfa349677 | -13.85668 | -48.08139 | 2025-10-29 04:25:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d7fcfa6-1950-3c9e-937e-c83eae666010 | -13.32949 | -43.18503 | 2025-10-29 04:25:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 63fb4b5f-504f-3388-bb94-7108a18958bb | -13.17942 | -46.45103 | 2025-10-29 04:25:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db4ab7f2-920d-3f0d-9bfd-187ee75f78d6 | -13.64537 | -46.51654 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bc87918-4ac6-39dd-89e1-60c1bab4556e | -13.25043 | -47.72835 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9771c72b-c11f-390e-92b4-964201ef617a | -14.61821 | -48.42219 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README52.md)
