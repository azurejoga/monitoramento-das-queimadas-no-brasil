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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a92e0ec-a18f-325f-a334-1485874220fc | -18.8711 | -43.58632 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f899c73b-d33a-34e4-bf90-32c2f2a3a70c | -18.87052 | -43.59029 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 851a715d-731a-3964-add5-9c66da8e5254 | -18.86766 | -43.60999 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| a245b245-68c7-3c4c-96bf-d3a11e7de29d | -18.86471 | -43.60577 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| c017e916-ecf1-3376-b4e3-e3c0fca66011 | -18.86415 | -43.60962 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| efbaaf86-2db8-35e9-845e-4e7b7583fb96 | -18.86061 | -43.585 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 97b55bb9-4f74-327c-9320-e227bec1808d | -18.84617 | -43.58641 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dc48bab2-8e10-32e4-8856-23f0c947f89a | -18.84557 | -43.59061 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6cfe1d72-7c9e-395c-819b-ba56df9d6b15 | -18.65068 | -43.14395 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c3ade01f-b0f0-33c7-b4f1-a137536937ef | -18.64829 | -43.13523 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 528b6384-9be5-3038-9437-fc538982e7b4 | -18.64791 | -43.14071 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 43d97dfa-5398-34ca-b40c-5318d166d06b | -18.64715 | -43.14339 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| f201577f-1142-319b-9919-9a123f8a2dec | -18.6461 | -43.15314 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 854c128d-fc95-3ac5-99b4-0c64bdcb2347 | -18.64598 | -43.15173 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9babc6a2-de7f-39c1-9675-09cfda08d8e3 | -18.64475 | -43.13468 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 36d1f9a2-5d0e-3bfb-a39d-7784bfcaa690 | -18.64437 | -43.14017 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| e1355c08-792a-3480-8783-1dc9dfd5905e | -18.64418 | -43.1388 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 9040a791-e7fc-34c3-a220-3c05fc21c6cf | -18.64378 | -43.14424 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 178ad657-d7eb-36b8-9720-a26000b31cd4 | -18.64318 | -43.14839 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| df4eae0f-6c3c-3cf1-b9db-a6a7d4988b86 | -18.64302 | -43.14698 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1368c4da-b11a-3c43-845d-f72b79a4b142 | -18.64244 | -43.15117 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 90b2425b-5b96-313f-a811-b6ff9e48fa60 | -18.64082 | -43.13971 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| fa672f7b-85e8-31c1-9114-5d5f4a776ccb | -18.63727 | -43.13922 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 2405f8ba-afeb-3c47-9441-a0290f620b54 | -18.6361 | -43.14733 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c0fcbcdf-39b7-3343-a7b3-f620814ffb1a | -18.63538 | -43.20211 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 6e4024e9-9aac-3c2f-a530-ef6519419475 | -18.6349 | -43.20483 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1a021b9b-fde9-31ce-8bb6-8a6807b45911 | -18.63316 | -43.1427 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 96106be1-860b-3878-b184-249734f3a934 | -18.53135 | -42.26661 | 2024-10-05 04:17:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 01dd4b9f-b7cb-30a3-9e14-9ff2aaab98eb | -18.46877 | -42.42041 | 2024-10-05 04:17:00 | NPP-375D | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3b7860a6-939f-3fbd-9586-9f356db5232b | -18.25124 | -42.94667 | 2024-10-05 04:17:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f710362c-8074-384a-a6be-d13ba1913d31 | -17.87613 | -42.68092 | 2024-10-05 04:17:00 | NPP-375D | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 27f20091-1299-3d29-a676-ceacd1160e00 | -21.44691 | -46.55615 | 2024-10-05 04:17:00 | NPP-375D | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ebfd8a51-0f3d-36dd-8a22-3b88fc93ed05 | -21.4463 | -46.5598 | 2024-10-05 04:17:00 | NPP-375D | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0182b1de-3cf7-3456-81c9-c6897320769b | -21.44358 | -46.55556 | 2024-10-05 04:17:00 | NPP-375D | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8a0d9cd3-eaee-32a4-807e-733704e643b8 | -21.443 | -46.55927 | 2024-10-05 04:17:00 | NPP-375D | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 92c8247f-fa03-3146-bae7-a2c16821f20a | -20.51549 | -44.89877 | 2024-10-05 04:17:00 | NPP-375D | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0843e40d-61b6-3947-90e9-090307d835d5 | -20.51211 | -44.89819 | 2024-10-05 04:17:00 | NPP-375D | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 542a1da4-434b-3fb5-8265-6408ad848b69 | -20.48144 | -42.36196 | 2024-10-05 04:17:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d4c739e3-8214-3e82-8cf6-4b5c8a5f983b | -19.95715 | -44.32023 | 2024-10-05 04:17:00 | NPP-375D | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b07e088c-5af3-3daf-8308-bf316d08700a | -19.31334 | -42.56462 | 2024-10-05 04:17:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 178a485e-004e-3662-8f76-112d9709cd59 | -19.31127 | -42.5797 | 2024-10-05 04:17:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b9027182-72c0-3c74-ba27-3134ca66232a | -19.30902 | -42.56892 | 2024-10-05 04:17:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 75c58b24-dafa-372d-b37e-d1cf871e34b8 | -19.30472 | -42.57302 | 2024-10-05 04:17:00 | NPP-375D | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 5a763b75-f682-39d9-b0dd-a6bbb4f98cfa | -19.26034 | -42.86713 | 2024-10-05 04:17:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 373b5253-6347-3c7b-9e4d-55bc7694552c | -19.02312 | -43.17759 | 2024-10-05 04:17:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7a5e7742-8627-3387-b26d-fdc8041c326c | -19.02075 | -43.16884 | 2024-10-05 04:17:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6333e6dd-d8b1-395a-ac2c-f8e19924f278 | -19.01957 | -43.1771 | 2024-10-05 04:17:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ef08971b-957b-3076-aeb4-6feb5cd7bc4c | -19.01781 | -43.16402 | 2024-10-05 04:17:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2bca84cf-3676-3cb1-9e0b-4e46f9e8e520 | -19.01721 | -43.16823 | 2024-10-05 04:17:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 89a94391-1ec8-313c-9dd5-1d5c23d72981 | -19.01603 | -43.17658 | 2024-10-05 04:17:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fa06a716-54f9-3d0c-820e-80a7a4a45a5b | -19.01368 | -43.16759 | 2024-10-05 04:17:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 07439e9f-9273-306d-812f-19b4393fd6ba | -19.01075 | -43.16268 | 2024-10-05 04:17:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f06f9ce7-c5a8-3acb-9d34-5b44a3744b4f | -19.01015 | -43.16692 | 2024-10-05 04:17:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d3cfb0e8-d7ad-3a7a-8122-e2717f05a9cb | -18.87581 | -43.60293 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| d0cd3604-b9a5-334e-9f20-2c210699a04b | -18.87231 | -43.60249 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 09f791ae-4c70-326a-8d29-231c7993f760 | -18.86823 | -43.60608 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| fec13a2f-4d01-3234-811c-124fc4355e98 | -18.8676 | -43.58595 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e7d494bb-af36-3818-921d-a3132572c497 | -18.86709 | -43.61391 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 749a6ff3-53e9-3878-b202-5f70599e81d4 | -18.86528 | -43.60187 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a5aaf1e6-117b-339c-a324-7ea462d5d5eb | -18.86409 | -43.58555 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1eaa9c17-b036-3374-9ca6-b4b11dc9a2e4 | -18.86359 | -43.61349 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b3cf7dc1-ce12-3b16-8373-77e759f078e5 | -18.86177 | -43.60154 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8d48a779-e545-3825-8672-2b484774c40c | -18.84963 | -43.58712 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cdecca39-40d3-3280-bded-800abf3552fa | -18.84379 | -43.60287 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8c83bfca-14a6-3fcc-b06c-48cd84120630 | -18.84209 | -43.59001 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7693578e-71ac-3e92-9766-d314b9f715ad | -18.84031 | -43.60236 | 2024-10-05 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fe72720d-5cd9-3874-9747-85f5fb65b6ee | -18.6501 | -43.14808 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7efbdd14-0f04-3e09-894a-f6bd6d09cf5c | -18.64732 | -43.14476 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 8a154e96-f4fb-3130-8862-74b569dc2a42 | -18.64672 | -43.14893 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 680e2ba2-2f84-3e60-823b-e525d119c595 | -18.64656 | -43.14751 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 78e185c1-9154-3441-8fd1-b896edda682f | -18.64556 | -43.13195 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5af17926-fe74-3321-b421-a560f20f3427 | -18.64496 | -43.13608 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ffbc73c6-5507-3de4-9dc6-d56400241ac0 | -18.6436 | -43.14287 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 06d63416-01a7-3604-a00c-bf37390ef8cd | -18.64257 | -43.15257 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 86ec7627-f30e-3165-bd19-7081b1fd44e6 | -18.64141 | -43.13562 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3546f118-098f-39ef-8385-d733db93227a | -18.64024 | -43.14376 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 4336bb6e-4293-3f6f-bd21-67ae5675166d | -18.63964 | -43.14785 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d5b719b5-f390-3542-8049-3d21e1ba86df | -18.63904 | -43.152 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1286be49-279b-3c94-83df-1d5669ce60ce | -18.63669 | -43.14326 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 408bc8ea-d637-3058-8b3d-9f51d708e62b | -18.63551 | -43.15145 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b95d68c3-aec2-3822-a996-6783f33940fa | -18.63546 | -43.20084 | 2024-10-05 04:17:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e8020cc8-86aa-3329-a45c-4af5cfc36094 | -18.56618 | -41.23191 | 2024-10-05 04:17:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4f432cb2-d1aa-3e3b-8b9c-247cd49c2d4f | -18.55847 | -42.23417 | 2024-10-05 04:17:00 | NPP-375D | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 17c528c1-db7c-3871-b512-f5c79ada759a | -18.55746 | -42.23136 | 2024-10-05 04:17:00 | NPP-375D | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 056157f7-2258-389c-9030-cdf43ed89521 | -18.55684 | -42.23603 | 2024-10-05 04:17:00 | NPP-375D | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 3fc97f57-c1fa-320b-95a4-5b798699c851 | -18.55478 | -42.23363 | 2024-10-05 04:17:00 | NPP-375D | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 19c07b63-3e62-397f-a4d3-d85ceea68677 | -18.55413 | -42.23826 | 2024-10-05 04:17:00 | NPP-375D | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| a1cfaf47-9283-3fac-a959-61342fd87784 | -18.55314 | -42.23551 | 2024-10-05 04:17:00 | NPP-375D | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 4b65482e-6d4b-33b0-b496-04255a6c65ca | -18.55252 | -42.24012 | 2024-10-05 04:17:00 | NPP-375D | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| a00a2d2d-6399-3fa3-91fa-0a97bc86262c | -18.55044 | -42.23777 | 2024-10-05 04:17:00 | NPP-375D | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 49f9c5fe-8bf4-35d5-a481-a814e8b5f823 | -18.53197 | -42.26221 | 2024-10-05 04:17:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6a72495b-e07c-373a-b9b5-b8bc6d7bf64d | -18.52529 | -42.25618 | 2024-10-05 04:17:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| af7d144c-f3ae-3b09-938d-1ee81108c32b | -18.52163 | -42.25549 | 2024-10-05 04:17:00 | NPP-375D | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e952a7b5-401f-306d-8ee0-66988779ec37 | -18.4966 | -42.19139 | 2024-10-05 04:17:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 15ffdea0-4bfb-337f-96d4-d6e7c2138a1e | -18.47854 | -40.93239 | 2024-10-05 04:17:00 | NPP-375D | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| a49f4c1e-99b3-3e6b-b0d4-045cab7242f3 | -18.46513 | -42.41979 | 2024-10-05 04:17:00 | NPP-375D | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bb95f829-8fc0-3dbe-89b7-d054463b02a3 | -18.4313 | -42.21467 | 2024-10-05 04:17:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6737e479-4315-3d27-a9ff-1d37a7070a55 | -18.43066 | -42.21928 | 2024-10-05 04:17:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1933a911-b35f-36a8-96ff-72412cb1e7f8 | -18.42762 | -42.21409 | 2024-10-05 04:17:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c9e44c5f-17cb-38de-b0af-43de93e54ea8 | -18.41781 | -42.20341 | 2024-10-05 04:17:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |


[Clique aqui para ver as próximas entradas](README81.md)
