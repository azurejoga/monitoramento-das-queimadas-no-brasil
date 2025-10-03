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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee78fb41-643a-3160-a0b6-2bcda3f06160 | -12.62383 | -46.99245 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b610fa8b-5bf9-374f-be5d-3450bdd48147 | -9.92166 | -43.73495 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 50c38876-f644-3785-a4d1-d70e4c5eadde | -13.76816 | -47.57281 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a8afd801-1820-314b-860c-15ec7413d4f0 | -11.47099 | -45.02638 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12530c0b-fc5d-37b5-b40d-921a7fa65017 | -13.76698 | -48.05135 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93ebac8e-afe6-38ac-b39e-f4ac59e455a3 | -9.38154 | -45.85148 | 2025-10-03 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9a7b184-2395-3ca6-9fc0-a90de3f1dd83 | -11.07694 | -47.70818 | 2025-10-03 04:12:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc3d1e34-c29e-3316-8dd9-5c0016413216 | -13.33112 | -47.59172 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c30844f2-f01e-3ce3-b4d4-94438ad5442d | -13.33319 | -48.11981 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b5e914b-5349-33c1-a526-01d9ca3f778b | -13.79799 | -47.58358 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 497cabdb-76fd-36db-bc61-5a09951f2c32 | -11.14345 | -43.39927 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 86dbc853-d630-3221-a499-53c9a92d2c19 | -12.62876 | -46.96357 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 396134f6-2d9b-395b-b5fa-5472e33d98ae | -13.97203 | -48.12666 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 546a0881-9441-3ca6-b1db-e1b54a4b160a | -13.75836 | -48.07639 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3878f8f0-51eb-31c4-850f-d5da04abd1fb | -9.94844 | -43.747 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2aa0ff5c-5383-3320-a594-645954230b87 | -11.67927 | -44.27726 | 2025-10-03 04:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f57f76f2-94f3-3c61-ae1a-c126caddc5d6 | -12.90887 | -46.91132 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ab9d9dec-42f6-3af1-aa6b-9143a885b6a3 | -13.19877 | -47.33661 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 029133db-e37f-37ef-9835-df0995f208d8 | -13.1975 | -47.89498 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1588f4ca-9c85-3ee4-95a2-a364853705b8 | -11.29127 | -47.84028 | 2025-10-03 04:12:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4d59e449-6dda-3884-9de8-fdda7a5d3b9c | -13.32119 | -47.58022 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 706649c1-bd3f-3b06-a367-c5d6786abdf9 | -11.90657 | -46.27034 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a739f280-b97a-330d-8303-cd0108fdb774 | -8.91037 | -45.03728 | 2025-10-03 04:12:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a58b58f-d330-3b73-ba4d-af8b204ea43b | -14.20432 | -46.08784 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb3bd226-aa57-3cb1-8f28-8f13c7efb59a | -13.23791 | -47.30599 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f671a5b-f652-32d0-8ba2-7029104b94e9 | -13.38144 | -47.28445 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d3c0974d-b807-393e-818f-9b4f1997e3cb | -11.08946 | -47.87014 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| df6e4b6e-e605-345a-adb0-65053384e7eb | -13.7677 | -47.53075 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 850039d5-8dcd-3b21-8945-2a5149954c17 | -12.75354 | -50.5535 | 2025-10-03 04:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53564f7e-2404-335f-ae9b-6cc875668085 | -9.95379 | -43.71425 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f20ae61-29fa-3add-8f6c-a0a015fcf906 | -10.895 | -46.71806 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f8370e0c-9ac7-317c-9123-e60c384486d7 | -9.3835 | -45.84983 | 2025-10-03 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96ee8aab-8e06-3c04-a638-9041b2e86d97 | -11.20757 | -54.09106 | 2025-10-03 04:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b6d74f6-9b44-3f53-825e-2f1a1f8a6302 | -11.35157 | -44.93623 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56e0d448-b031-3d52-a551-a4a8a46c00f4 | -9.94607 | -43.76153 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8f8597d5-d0fe-3ce6-ae4c-e82f7b360580 | -14.21555 | -46.08614 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79f5ccc2-0c22-39a2-bccb-59f3c4a46978 | -13.2124 | -47.34898 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff20aff4-f40e-3600-b6f7-3f78106349dc | -13.6613 | -47.30421 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc5fae4f-5a51-3465-a5e6-4ee1b57245cc | -13.12743 | -47.88499 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79bd756a-70d9-33d5-a6f9-3855bcb55787 | -12.81226 | -46.86439 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4e7befd4-ffaa-3825-abf5-ff35e4b99004 | -8.83209 | -46.77766 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1afd4c29-5eec-3ad5-9b3b-69088d7e8a50 | -11.62242 | -47.99008 | 2025-10-03 04:12:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ff1faf2-a3d2-383a-9a8c-2ac8d6fc4f83 | -14.6035 | -46.711 | 2025-10-03 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e76395c-46bd-3600-8d1a-8736f3638bfc | -9.92196 | -43.77621 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8b759d41-b28d-3ac6-8284-679639a9abfb | -13.19619 | -47.81045 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01197301-a7af-3e49-883a-a7cd1850e7fa | -11.12341 | -43.39584 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6c9d50c8-4724-3cde-8b78-e0e7e840dad3 | -8.45682 | -47.65989 | 2025-10-03 04:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eee8bece-4021-3afd-8b2d-8c2ff590f874 | -13.76123 | -48.06055 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 185573e0-8657-3ebf-afde-3377e04242ff | -14.22949 | -46.10414 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ac37aaf-5240-32e7-8c1e-b31c40810b21 | -13.17589 | -47.87889 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 915fb6f5-79ea-3f5e-bead-a121fe953bac | -13.0483 | -47.02133 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd28acab-9a2d-3561-b485-36aae2d2876d | -12.80152 | -47.0155 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e2802ce6-03fe-30b8-8f49-bb2e9124cb2c | -11.8482 | -44.96915 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d1a57f0c-b09b-30ce-ab5c-787e87dc8135 | -13.97331 | -44.86374 | 2025-10-03 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 596a522a-6ede-3392-b527-e06fbb9ba2d0 | -14.79464 | -42.82658 | 2025-10-03 04:12:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b56a21f2-39c7-32c0-8dde-8b628ff59ade | -14.23019 | -46.10003 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b470add7-9ab4-3b19-a704-cf201daf0c3c | -10.63587 | -49.15208 | 2025-10-03 04:12:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 58dfa553-83e7-3c44-a9bf-0e5afcf620fd | -11.63708 | -45.06554 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb0cea6b-b5b6-33bd-8b49-4e4847da41fa | -8.79822 | -46.66893 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f055b00-8660-3c15-bacc-d2de62fa7cb3 | -13.68202 | -48.63404 | 2025-10-03 04:12:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 510ecc91-e3e9-301c-baf9-d7abf8dfaaa1 | -12.38107 | -46.53388 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f2f3718-56e8-384c-8818-ae179237fa93 | -10.10867 | -50.27295 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 5d0ce668-ebf0-30b4-a9c2-d5f03cdbe00e | -9.95265 | -48.77615 | 2025-10-03 04:12:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40862a18-defe-3905-b512-7ab3449eb97b | -12.9104 | -46.36155 | 2025-10-03 04:12:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52def097-05d1-3df6-a242-6ddefc442b64 | -10.22828 | -43.02514 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 51800357-d8eb-3762-a2ed-29cb6d41c395 | -13.3419 | -48.09437 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72ec6bff-648a-3024-acc4-1ed3397cd09f | -14.20498 | -46.08393 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8346767-b416-3ce7-bd4c-6cd45276013c | -10.91543 | -47.04247 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 569df1df-c8e9-38cb-be67-6cfe47dd71d4 | -10.90679 | -47.04382 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 337d048e-6f16-3df1-a6dc-0f8eda07c85f | -11.08659 | -47.87021 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f3bc67b1-cded-3e9b-8061-1127aa8bd11c | -12.80853 | -46.86368 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a830700-b493-324c-bf92-5588786eb342 | -8.79898 | -46.67126 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03154bf6-b24e-3b03-b5f4-b13c8aa9bf50 | -13.38525 | -47.28512 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 24cf7c7d-80aa-375d-9089-359f84ebbd3a | -10.86188 | -45.41161 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1067e8f1-ab63-35e9-bdd4-1a9e15994e5a | -13.12587 | -47.84723 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4047e339-ed83-3255-8acb-e51c7e1d084a | -10.34508 | -43.75483 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a156937d-f60e-377e-a1b2-887be67f622f | -12.02561 | -47.90076 | 2025-10-03 04:12:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7e62803e-0166-3ed7-b0de-51bdf5d41b0b | -12.65024 | -46.99751 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 216a3a49-4626-3a91-b84a-ed3baa03792e | -14.00878 | -44.92303 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2933bf2c-e3bd-3b70-a6c4-720419500287 | -13.28508 | -46.994 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08c03272-7278-31ac-8147-f56aba161e50 | -11.86704 | -44.98447 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04329547-78bb-3da9-9d6f-392337f731ff | -14.29357 | -45.91942 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 768c4adc-df99-32a4-9ece-ff9b4839fad2 | -11.87203 | -44.99749 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd6afd96-4410-3fc8-8978-172fa7201853 | -11.82031 | -44.90151 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08f6c2a3-4234-3d4c-b174-630cc492c3b9 | -11.53768 | -49.82423 | 2025-10-03 04:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5d876bea-054a-3229-8bfd-9abd4d61effb | -11.4772 | -44.96796 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60278778-a7d5-3cc0-953e-beeba8957939 | -14.3304 | -45.87225 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1ae23fd-c067-3bf6-b525-37d563d20355 | -11.59941 | -42.87093 | 2025-10-03 04:12:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 272950ce-c53d-3ae9-97c3-b3b26cb94ff8 | -13.23231 | -47.35956 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2d1a52e7-9501-3bce-bce9-3212f2fd1022 | -11.09419 | -47.86718 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6ac288ee-f342-3c11-8d4a-a4aaacde190c | -13.33999 | -48.10496 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcdaa6c7-a78b-37c1-8cda-da1a4d9239ca | -9.87693 | -47.81182 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 367ac514-7359-39f2-b59f-9afb1fb58476 | -14.59839 | -46.71896 | 2025-10-03 04:12:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 019687e5-44bc-3e67-885c-edb33e373989 | -13.13544 | -47.88581 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2fcb94e7-aa11-3320-b6c5-6c4b9a0fa702 | -12.94246 | -46.3715 | 2025-10-03 04:12:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26f02cf8-5980-355b-b12c-b288f1f4ff09 | -13.30778 | -47.8143 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a09c9592-0cdb-3b28-b0f6-8d22ff9ecff5 | -12.92645 | -46.37739 | 2025-10-03 04:12:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c7f24501-443f-3022-8f5d-645137f557dc | -9.13027 | -45.92733 | 2025-10-03 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9357667-fbda-3597-83da-8bb3123eda0d | -9.91269 | -43.72598 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3ee27b40-8e95-33cd-b74d-01e97f63fabd | -11.15139 | -47.18496 | 2025-10-03 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README60.md)
