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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 762ab25f-5352-39b6-8376-c7b9287da9ed | -15.28883 | -56.78549 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98b23641-e9f3-3127-b82c-176af1bc9a80 | -16.73645 | -52.40116 | 2025-10-01 04:53:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e72dfe0-3dbf-35ac-9aee-bf238fd8a743 | -20.83734 | -43.02253 | 2025-10-01 04:53:00 | NPP-375D | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0627b1f6-2e3b-3a40-bd3d-ad13abbe24ee | -17.3934 | -47.1634 | 2025-10-01 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8216544d-e25f-3b4d-9634-0cb422920a8d | -21.04354 | -45.68172 | 2025-10-01 04:53:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 819706c2-c336-33f0-a158-10050de1307d | -17.85787 | -46.15705 | 2025-10-01 04:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 442a20cf-6e61-3245-887b-55a403a87274 | -20.22004 | -43.44281 | 2025-10-01 04:53:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ed848768-b393-3eba-b01e-079d9ca54c2d | -20.47959 | -43.94582 | 2025-10-01 04:53:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| caa59c15-dadf-362e-a897-04b452030085 | -20.63581 | -46.21549 | 2025-10-01 04:53:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e7be4d81-0700-37da-b17c-38ae7e992d53 | -20.02987 | -44.54564 | 2025-10-01 04:53:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a6c477ab-265c-3fb1-84d6-cc6397093110 | -21.04419 | -45.67572 | 2025-10-01 04:53:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af374472-d8dd-3c57-8cab-ad0a3b226239 | -17.40152 | -47.17007 | 2025-10-01 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1d896c47-7860-370b-baa6-5f056c39f73d | -18.23763 | -53.30419 | 2025-10-01 04:53:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 637ef042-42f8-3030-919b-02335e82b2ef | -18.7084 | -43.17328 | 2025-10-01 04:53:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9edc8a6d-11fa-3ade-a4a7-ea2d6944555a | -20.62665 | -46.20856 | 2025-10-01 04:53:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8bdfa5e6-8692-36ff-82cd-f2274b8556f0 | -22.10332 | -47.80033 | 2025-10-01 04:53:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6691420e-ecd5-3585-9e84-8694959808af | -16.76704 | -51.34374 | 2025-10-01 04:53:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4322ef98-81e5-3f8b-9717-21ebf08c39bd | -22.78937 | -47.22219 | 2025-10-01 04:53:00 | NPP-375D | NOVA ODESSA | SÃO PAULO | Brasil | 3533403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 5686ec74-e2d3-35d8-90a2-566969cfe445 | -23.061 | -47.03116 | 2025-10-01 04:53:00 | NPP-375D | VINHEDO | SÃO PAULO | Brasil | 3556701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 6ede5be6-409f-3d73-9225-c708c691eaa8 | -20.49429 | -43.94083 | 2025-10-01 04:53:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 831845b5-3c17-31ee-8141-2258180040cf | -20.11982 | -46.34146 | 2025-10-01 04:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 275f36cc-010d-3880-879a-1a5aa674b8c7 | -23.41751 | -49.4611 | 2025-10-01 04:53:00 | NPP-375D | FARTURA | SÃO PAULO | Brasil | 3515400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b805e3c2-b458-3d0a-98fd-37bd6efc22be | -22.11519 | -44.68959 | 2025-10-01 04:53:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f3e9855a-c473-3561-a12c-2d61d0610eb1 | -16.24945 | -50.93054 | 2025-10-01 04:53:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 492ebf8b-ed64-3b1d-aa63-3959e8b067b8 | -18.16373 | -46.11005 | 2025-10-01 04:53:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b5296365-c878-3f42-b954-35d4234844b7 | -15.25749 | -56.77993 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33f89b9f-a80e-3dc4-9b50-862fbf982f51 | -22.10379 | -45.31322 | 2025-10-01 04:53:00 | NPP-375D | OLÍMPIO NORONHA | MINAS GERAIS | Brasil | 3145505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e9bae1a1-6a46-3baf-accc-4df8f44cf5f7 | -19.93424 | -43.9026 | 2025-10-01 04:53:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 00a30304-c2bf-31b6-85a1-760ea15f5970 | -16.25938 | -50.93616 | 2025-10-01 04:53:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5801696b-4f37-33cc-b73a-1c6d5fb5d7e9 | -22.09833 | -47.80419 | 2025-10-01 04:53:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ac7df3b8-0477-3af3-abee-0b3cbe65d140 | -17.96611 | -45.03976 | 2025-10-01 04:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bef5a88d-f145-31cf-ba39-c8710455aaea | -18.96924 | -47.87379 | 2025-10-01 04:53:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d9366857-40b0-3ac1-9cad-e7bf584f9bbb | -22.2736 | -46.72679 | 2025-10-01 04:53:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ce0d291e-ac58-38c5-a38a-9c9e506fcbfd | -18.42053 | -53.21798 | 2025-10-01 04:53:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15bb9493-5f65-30a0-8860-2253b91bf284 | -15.28352 | -56.79392 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ab6a4b1-702d-34f2-9447-563929a1ca5a | -17.96874 | -45.01609 | 2025-10-01 04:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23cad36c-483e-3fad-9040-63acadfe70bd | -18.48257 | -44.01876 | 2025-10-01 04:53:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 138e304c-e044-3ecb-bfee-692cf648dcf4 | -22.62842 | -49.05405 | 2025-10-01 04:53:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9296a1fc-0b1e-3b83-b45d-1c5b4a52a921 | -15.861 | -59.3143 | 2025-10-01 04:53:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83b6cd5a-bb9f-3ca3-96d5-2f45a5536e73 | -20.62301 | -46.19651 | 2025-10-01 04:53:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d71a6466-6890-3d35-aad9-22517db021c8 | -17.49391 | -43.47969 | 2025-10-01 04:53:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45869926-1ec8-3dde-a375-67db670f8134 | -20.5868 | -45.88408 | 2025-10-01 04:53:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 05da75db-bf40-3bc9-b872-bed9b84e1122 | -18.40993 | -53.21997 | 2025-10-01 04:53:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 018756e9-99e6-3dc8-b909-2ab601e910d2 | -22.78994 | -47.22337 | 2025-10-01 04:53:00 | NPP-375D | NOVA ODESSA | SÃO PAULO | Brasil | 3533403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| d8dcb495-694e-336e-8507-f6af6c20b251 | -17.38734 | -47.13981 | 2025-10-01 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 00c33a1b-dfd5-3d39-9c69-456a449b263f | -23.17103 | -45.73711 | 2025-10-01 04:53:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4ec5a9c0-d229-3b39-be8f-5faf22b5cd25 | -15.99055 | -59.51976 | 2025-10-01 04:53:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dae2833c-e98e-310d-b9ee-42d73f83e39c | -16.66552 | -49.1302 | 2025-10-01 04:53:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47c69b5b-dd5c-32e3-9488-76e60e9362c0 | -19.46159 | -44.28515 | 2025-10-01 04:53:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5292d46d-ec96-3d00-8aed-63e31b2f3145 | -16.41236 | -53.54201 | 2025-10-01 04:53:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 46911d58-e8f2-3bac-9e71-473ce7645ec8 | -22.92982 | -45.50876 | 2025-10-01 04:53:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 8df10d00-559d-3006-827f-008668ef0b27 | -22.24178 | -43.40617 | 2025-10-01 04:53:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 4dc33a4e-f31d-3b75-8f7a-67c47026aee0 | -20.22868 | -43.88845 | 2025-10-01 04:53:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b964aaa2-ea42-311b-bf69-f7958b93c36d | -22.29123 | -47.73208 | 2025-10-01 04:53:00 | NPP-375D | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e7b1621-13d4-37a3-8bb4-3eec63456cdb | -21.04105 | -45.67781 | 2025-10-01 04:53:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c210e98b-78d4-32ee-9526-519b302fb90b | -18.49138 | -44.04107 | 2025-10-01 04:53:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65b10201-3df9-3e7c-8465-a834b10c5754 | -18.80948 | -47.5512 | 2025-10-01 04:53:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42bf9a8d-06b3-3d19-b4b4-51c3e929fe69 | -23.18162 | -45.47718 | 2025-10-01 04:53:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 18a45ac7-c60f-3abd-a266-275bf4d15246 | -18.4211 | -53.21431 | 2025-10-01 04:53:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07017dcb-0a89-3a7b-a514-a634430ebade | -22.6503 | -46.76193 | 2025-10-01 04:53:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d60a30b5-1cd4-307f-a2fc-4140ad7097f3 | -18.16434 | -46.1048 | 2025-10-01 04:53:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b3afba55-b330-37d8-b96b-29bb1528123d | -21.04387 | -45.67871 | 2025-10-01 04:53:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28975a3d-1cb2-369d-87b0-06dcdeb38e9d | -23.68469 | -46.86969 | 2025-10-01 04:53:00 | NPP-375D | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d5524de5-568b-3b24-999f-a479160f5a7a | -18.2404 | -53.30838 | 2025-10-01 04:53:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 577b2bef-538e-3331-8420-bb92743c6d14 | -22.77683 | -47.60911 | 2025-10-01 04:53:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 157cc7d9-6f66-3e7f-9c97-cd83e3261a68 | -22.10913 | -44.69282 | 2025-10-01 04:53:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 29fb8ca2-e018-37a2-a528-790e27928f8f | -23.16369 | -48.08355 | 2025-10-01 04:53:00 | NPP-375D | PORANGABA | SÃO PAULO | Brasil | 3540507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| eca8fedc-d325-35e9-b0ed-bb34b76b4d43 | -20.61012 | -46.22357 | 2025-10-01 04:53:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8be898b1-29ae-3cd0-b7de-aab310a0b972 | -18.96467 | -43.70885 | 2025-10-01 04:53:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e5286a6-6312-3372-8d6b-2aa98ce84a09 | -16.25179 | -50.93905 | 2025-10-01 04:53:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bac0b247-c8b3-3d37-9a23-78c3aac6cfde | -20.23504 | -43.88203 | 2025-10-01 04:53:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9be21063-29ad-3442-8400-1030ee925199 | -15.30721 | -56.78955 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12420b2c-4c55-3eda-8e37-eb21ccc8ae21 | -20.02476 | -44.54192 | 2025-10-01 04:53:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 68ce638c-6bc0-3f4a-9506-c5f0c46bb449 | -22.10913 | -44.69493 | 2025-10-01 04:53:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 89def063-cb02-314e-ac76-bc6a2d42b58a | -22.65201 | -46.74554 | 2025-10-01 04:53:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6ab9ced9-1792-3d66-9f13-906aa47f2768 | -23.16626 | -45.73391 | 2025-10-01 04:53:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| deb73fa9-b1c1-3a78-adba-a42e809f3d5e | -22.57765 | -46.77315 | 2025-10-01 04:53:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.6 |
| 82d26493-7b6d-3b24-a4e0-885a3d99e49b | -22.92948 | -45.5122 | 2025-10-01 04:53:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 3350ccb1-52e3-3e9f-af0b-10793155a102 | -15.84459 | -59.5967 | 2025-10-01 04:53:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3bb8301b-b192-3efc-9e72-d0d5a0f53c22 | -17.67967 | -47.26146 | 2025-10-01 04:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66e40eec-63db-3db0-a892-90e0018d5054 | -20.64076 | -46.21555 | 2025-10-01 04:53:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7602f231-e8f4-3233-99c6-3504d4961733 | -22.36973 | -48.6496 | 2025-10-01 04:53:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 97e581c2-4b6a-3a6f-bddd-27908c218ab0 | -22.64351 | -46.7545 | 2025-10-01 04:53:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3f9fdb78-936b-3a62-8554-e16486ca9dd7 | -22.40889 | -43.17106 | 2025-10-01 04:53:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ae7e2aed-2af9-39f9-aad5-ba3997ac149c | -18.44825 | -48.03123 | 2025-10-01 04:53:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ae1121d4-acf3-3e7e-aac2-7e7b07bf70d6 | -23.24706 | -46.78874 | 2025-10-01 04:53:00 | NPP-375D | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a293311a-6a94-3808-9712-d2267930a03f | -18.70545 | -49.16842 | 2025-10-01 04:53:00 | NPP-375D | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25118e5c-6366-3542-8f2f-ccce98be9684 | -21.88228 | -48.1452 | 2025-10-01 04:53:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcabfdb7-d7ef-3843-808d-2d963d8f6dc0 | -20.48561 | -43.94282 | 2025-10-01 04:53:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 55582648-2308-3b0d-b96e-b3d7443853bb | -15.27859 | -56.77858 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d18c560-1e9d-3791-9243-9c1e2109c73e | -18.80458 | -47.55478 | 2025-10-01 04:53:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b97eff9-a7ad-351d-afd3-a4da752fa13d | -21.04644 | -45.67555 | 2025-10-01 04:53:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1942d1d7-c625-3832-b6f4-dfcf0ad13ca1 | -19.86805 | -43.82076 | 2025-10-01 04:53:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 81bbeb1c-9ac4-3b7c-9f97-b2cc48473ef5 | -17.39061 | -47.14974 | 2025-10-01 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 47613f83-e5e9-3db0-bf6e-9e8cf2c6f771 | -18.60431 | -43.27365 | 2025-10-01 04:53:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cab62fb2-333e-3472-8a65-0bce42d35857 | -17.38956 | -47.15823 | 2025-10-01 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 673eda27-7240-36c9-be5f-0cd8cb0d79f8 | -15.33803 | -56.63491 | 2025-10-01 04:53:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 59794f79-6226-394a-8f6e-d01efa5c7412 | -20.13019 | -46.33643 | 2025-10-01 04:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| df8e3fa7-7d62-3b5a-9fa8-330adf7664e2 | -22.62424 | -49.05339 | 2025-10-01 04:53:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 61f462d0-75a4-3f47-9d27-1f7f7f082a62 | -17.49429 | -43.47606 | 2025-10-01 04:53:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README115.md)
