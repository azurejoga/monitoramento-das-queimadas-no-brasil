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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c6847b0-7650-33c5-902c-35fb9730a9b0 | -11.78178 | -43.75306 | 2025-09-27 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8da49c2b-0bad-3360-9eaa-a07dd99b1a8c | -12.44503 | -43.54433 | 2025-09-27 00:11:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d8af66b8-3ef1-33f3-b21c-880eb6c994a6 | -10.92972 | -48.82465 | 2025-09-27 00:11:00 | TERRA_M-M | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 70cde936-755b-375e-8d26-8f6f8186cc35 | -12.96876 | -46.25518 | 2025-09-27 00:11:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3aabe09b-3784-3266-a11b-410bc68ad181 | -14.87292 | -45.58896 | 2025-09-27 00:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| bec2d60b-079b-3d7b-80b9-9c7d023237ec | -8.82915 | -45.97511 | 2025-09-27 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 52f5f0c7-a4d9-303d-a943-fa47af4dd221 | -15.53953 | -44.33294 | 2025-09-27 00:11:00 | TERRA_M-M | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 163867f1-a9d9-38ab-8943-cd5c0a18a359 | -10.25244 | -50.47451 | 2025-09-27 00:11:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 0678bf72-876c-3016-a475-083ca8cfda81 | -11.97094 | -46.59155 | 2025-09-27 00:11:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7db71c10-dd29-370c-bb5c-23ee7b56aaca | -14.9574 | -47.51729 | 2025-09-27 00:11:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 5dd355d0-9cf3-3541-9993-0c04861ebaa8 | -9.09792 | -48.904 | 2025-09-27 00:11:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 429a7ecc-8f04-34a9-8eba-df2f480ee995 | -8.9134 | -46.10048 | 2025-09-27 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7d847107-48be-3fc8-a3e4-7e6d6b3a0a9b | -12.97032 | -46.26731 | 2025-09-27 00:11:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4be3e06c-fbf1-3da2-a090-aed024ac4354 | -11.4303 | -44.96952 | 2025-09-27 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c03f73b3-f4a6-37e2-a3c2-59d545090d09 | -13.60712 | -47.30957 | 2025-09-27 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 7b7a6110-f65b-36e1-accd-5c15372ea504 | -12.30502 | -44.35707 | 2025-09-27 00:11:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 80983bed-f01e-3f97-8c9b-82efcc3589f3 | -11.23892 | -45.5645 | 2025-09-27 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4aec3110-f592-3991-a62b-bd0179650e00 | -15.04157 | -47.15484 | 2025-09-27 00:11:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 611bc872-1aa1-3d35-b2a3-ab64f625a5d7 | -8.37091 | -41.40604 | 2025-09-27 00:11:00 | TERRA_M-M | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 81e654e6-a0f9-3e0b-98ba-2fa3306f75a1 | -13.63122 | -48.07823 | 2025-09-27 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| dfc810a2-3438-315a-9782-d43340e63d06 | -9.96636 | -43.60778 | 2025-09-27 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| ba5c840a-ed9a-3a1c-9377-55e48ab4bbdb | -10.24226 | -43.94791 | 2025-09-27 00:11:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 20208212-2a37-315f-a479-54392e2dc8d7 | -12.26612 | -44.06535 | 2025-09-27 00:11:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 278.3 |
| a98d8345-51fb-3062-81b2-825eba33c3f3 | -8.67294 | -43.99272 | 2025-09-27 00:11:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a41c80b9-ad26-3d81-af12-234abbc675cc | -15.42155 | -48.22603 | 2025-09-27 00:11:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 651c0403-c918-37e1-8166-6e33d9711fb4 | -12.05704 | -48.77262 | 2025-09-27 00:11:00 | TERRA_M-M | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 332baf38-41cf-3003-92cb-b75baf9819fc | -8.83794 | -46.22309 | 2025-09-27 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| eda3f246-4d54-3a21-ba38-23f80833eab4 | -9.89422 | -49.1338 | 2025-09-27 00:11:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 842c5e5f-cc55-3030-8a7e-2f660791f54d | -14.05942 | -48.82915 | 2025-09-27 00:11:00 | TERRA_M-M | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 86cebada-d0bd-3364-927f-beb4ea7d7f95 | -12.62084 | -48.13973 | 2025-09-27 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| f1d4191f-3a19-33a2-84e9-da2b7ebd70c6 | -14.63732 | -48.29646 | 2025-09-27 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 6ebec923-7f38-3e3d-929a-5596cacd815c | -8.83261 | -46.25607 | 2025-09-27 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8149f577-320e-3822-a59b-4cccb3da2515 | -15.03979 | -47.13971 | 2025-09-27 00:11:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 235.1 |
| 42ccea23-5ab1-34d7-aae4-fd46aaef03ed | -12.26487 | -44.05603 | 2025-09-27 00:11:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 411d3610-dcd4-3199-87f5-0643ff54fba8 | -9.3068 | -49.01769 | 2025-09-27 00:11:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a8098964-8ec4-3ab9-9238-67827eb867a3 | -15.42509 | -48.21851 | 2025-09-27 00:11:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 8fd883e0-aee0-393b-b7e1-6c9c95abee0e | -15.58546 | -42.40646 | 2025-09-27 00:11:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 4cef917f-dbfa-371d-9abc-dbc78f6de983 | -13.17338 | -47.41338 | 2025-09-27 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f08e2070-c4df-36f5-be13-44e4ccad5d07 | -10.18856 | -49.5064 | 2025-09-27 00:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ea30ca1d-3d38-39b8-9ce5-1921e16095eb | -15.04068 | -46.95697 | 2025-09-27 00:11:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 15cc68c2-42f8-3a1e-a12f-b0363bac0373 | -15.26703 | -46.46493 | 2025-09-27 00:11:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 74e10a73-41de-3f26-909e-f59ecc34b8fd | -8.83405 | -46.2668 | 2025-09-27 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 33b1bc25-a572-3835-8fc5-61e1a462e0dc | -15.01862 | -46.95976 | 2025-09-27 00:11:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 36de4424-a57b-35fc-a5c6-b9d2e2115301 | -8.82834 | -46.22423 | 2025-09-27 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e862bca6-c24c-3a63-ac0a-df243ad63617 | -11.69265 | -44.4573 | 2025-09-27 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3c19917c-530d-33ee-85e7-effdf25581ac | -10.87859 | -49.39739 | 2025-09-27 00:11:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 258cf70d-fb8c-3b70-903a-07761a8be8cb | -12.0307 | -47.06533 | 2025-09-27 00:11:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6f106c0f-59ad-3029-93a4-c7f116795fbf | -14.90121 | -50.29472 | 2025-09-27 00:11:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 5df547d5-c0da-37d6-b388-cc94bb2b1d49 | -15.5779 | -42.41689 | 2025-09-27 00:11:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 30.4 |
| bf94962a-745d-30cd-93bf-7c06a27c8cbc | -11.77414 | -43.76343 | 2025-09-27 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 30.7 |
| c49dd883-488c-3d52-a7e0-f5e324d3fa54 | -8.36942 | -41.39586 | 2025-09-27 00:11:00 | TERRA_M-M | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 32a192b9-39e3-317f-853a-0f47725089bd | -14.88974 | -50.28922 | 2025-09-27 00:11:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 9c0bf13e-83d6-366b-b70b-4f6625b9a59b | -11.24706 | -45.55275 | 2025-09-27 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 480a90ee-574c-358f-b338-05f7ba22ac97 | -11.49382 | -43.53662 | 2025-09-27 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1f4d18c7-8b6c-381a-9115-4d3f197e914b | -10.4742 | -46.53492 | 2025-09-27 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4026b21e-fda3-362f-9a4e-1987fd49f8d6 | -9.08117 | -48.02531 | 2025-09-27 00:11:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 0853bef5-a220-3af1-9fb5-1e7e33ce075a | -12.22987 | -47.19174 | 2025-09-27 00:11:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6765b33b-a36a-33e2-b441-faca1695c565 | -14.46741 | -46.85027 | 2025-09-27 00:11:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ff5d83f4-1877-3e9b-9b63-805caa3c508c | -10.98225 | -50.72201 | 2025-09-27 00:11:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 07332b9e-9676-313d-a7e3-d347eb268eee | -15.53152 | -44.34449 | 2025-09-27 00:11:00 | TERRA_M-M | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 17.4 |
| be25d270-47d8-32b2-8e15-eb5b10f51006 | -15.26488 | -51.45386 | 2025-09-27 00:11:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 861c2c62-a71c-3d68-97d0-930ff86b9208 | -11.43713 | -43.51728 | 2025-09-27 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| fe955e16-3cb8-3713-bec3-fea115d2c453 | -15.1268 | -49.54242 | 2025-09-27 00:11:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 756fbf1e-d5fe-3a37-b195-be1d4be32a48 | -13.18629 | -47.42666 | 2025-09-27 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 67ed1173-0587-3144-80cc-7c1bb665ed0e | -15.55613 | -47.92196 | 2025-09-27 00:11:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 53a91041-555c-3bab-ad40-e729d97fbedb | -12.04132 | -47.064 | 2025-09-27 00:11:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 44120b61-23cf-3d76-889b-07a2ab271524 | -10.29742 | -48.79057 | 2025-09-27 00:11:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| d51f1f00-c4ce-3df3-aec7-b7e4209d3996 | -11.37752 | -44.99648 | 2025-09-27 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2ba819a4-16da-3220-a262-db3d14d3f66b | -15.75178 | -43.84531 | 2025-09-27 00:11:00 | TERRA_M-M | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 2e8105ab-0ab9-3b44-8fd3-cbb1b5010217 | -11.38271 | -45.03594 | 2025-09-27 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2c22229c-60bf-3d24-9c8b-0836daba32f9 | -10.94491 | -44.30645 | 2025-09-27 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 345e5200-b895-37c4-bd1e-01b0e36c1945 | -12.54867 | -45.84828 | 2025-09-27 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 490ebb0d-a994-33ff-9b24-ad226bc7633d | -8.81036 | -40.99101 | 2025-09-27 00:11:00 | TERRA_M-M | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 838beb78-aad9-324b-b2d3-687d1b73a5f7 | -15.5302 | -44.33424 | 2025-09-27 00:11:00 | TERRA_M-M | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 0f306f45-f90f-3ea7-aba6-ea0ea2636538 | -10.24169 | -50.27184 | 2025-09-27 00:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| bcec9072-e94e-3023-9e67-4031ae139e17 | -10.1869 | -49.5121 | 2025-09-27 00:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 520fbb63-2554-3033-9229-18e727e877a5 | -12.25716 | -44.06667 | 2025-09-27 00:11:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| c82440ce-a54e-33f0-b109-f71dc44d42c8 | -14.95557 | -47.50116 | 2025-09-27 00:11:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 703563fd-484f-3c1d-9199-915a97cd0f1e | -9.76036 | -46.14017 | 2025-09-27 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 469a6c61-7800-3bdd-a34e-a2f0cb142732 | -8.8119 | -41.0016 | 2025-09-27 00:11:00 | TERRA_M-M | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b19d0ac6-3d6a-3f58-a6bc-9e9b433fbd0e | -10.81281 | -45.38197 | 2025-09-27 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 522b4f21-73c1-394e-93ac-42dfc6c51156 | -9.0772 | -48.01727 | 2025-09-27 00:11:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 62fd256b-1422-3c7b-b6d5-82687a061fc6 | -9.69977 | -48.94276 | 2025-09-27 00:11:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 4a0dfa50-9444-3dee-b1d7-468234b733a6 | -9.03567 | -45.51914 | 2025-09-27 00:11:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 342fdaea-1ea3-34d6-bd0a-201d8164f6c0 | -10.1702 | -49.38035 | 2025-09-27 00:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 98959533-8c70-32d7-af14-bc57c72bf32a | -15.57665 | -42.40778 | 2025-09-27 00:11:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 8bfd925c-e102-3e5c-baba-ae368379dff9 | -10.17173 | -36.38099 | 2025-09-27 00:11:00 | TERRA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 27.0 |
| f5ac04c0-4062-31c3-8fe9-7e589d1ca47b | -12.07581 | -45.05046 | 2025-09-27 00:11:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ef6c1937-e1fd-3fd8-bae1-a3748d12a10f | -11.24841 | -45.5632 | 2025-09-27 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 76807744-a5e3-335a-ab5e-f7b195b7d1d8 | -8.75141 | -44.23592 | 2025-09-27 00:11:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2abec54a-abf0-3e08-87f1-c4de4c1fc55c | -12.2584 | -44.076 | 2025-09-27 00:11:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e9cdbbd0-09c1-3ca9-a6cd-2f311ae4753a | -10.17116 | -36.39795 | 2025-09-27 00:11:00 | TERRA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| 35f6c2cf-1972-39b3-b4b8-242ec7a08ef5 | -15.56144 | -47.91462 | 2025-09-27 00:11:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 65843f4f-457b-38b3-9e58-07a49554e6e3 | -11.4316 | -44.97925 | 2025-09-27 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 6c650106-6039-30fc-b8a7-c8367d4ccfb3 | -11.38158 | -44.95611 | 2025-09-27 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2a768300-a140-382a-b881-3dd3fe173b80 | -11.43174 | -44.92362 | 2025-09-27 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 7bd25e4a-f6e8-3c11-a877-c45ac87ba25a | -10.12499 | -45.33611 | 2025-09-27 00:11:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1749c1f9-7873-31d4-ae71-e6239fe4ce74 | -11.42629 | -45.00979 | 2025-09-27 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b5a375fa-7a4f-3c52-848e-420809ebd287 | -11.69536 | -44.40879 | 2025-09-27 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 67cea852-7468-3c11-bc35-d4a0a344330b | -8.83653 | -46.21263 | 2025-09-27 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |


[Clique aqui para ver as próximas entradas](README3.md)
