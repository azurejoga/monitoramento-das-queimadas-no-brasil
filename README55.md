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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd66d6ba-860d-33fc-8336-085990f5413b | -22.65602 | -53.10225 | 2025-09-12 04:08:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 67ac825d-5914-3bd4-a49c-728fc07d060b | -21.19841 | -47.52726 | 2025-09-12 04:08:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 17.2 |
| c370dd17-f489-3be5-b229-720945ddddad | -20.27015 | -42.12814 | 2025-09-12 04:08:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 21aa27fd-91b3-30e6-8385-f7e0b34326f3 | -19.16661 | -47.96205 | 2025-09-12 04:08:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbe9a32c-fc18-37ac-8eef-6033075365ff | -19.95381 | -49.26813 | 2025-09-12 04:08:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3680a037-5239-3a2a-a935-3d5018c30b0c | -23.37661 | -47.23306 | 2025-09-12 04:08:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f90a7bb0-28d4-3496-8011-ae6921cd1781 | -24.80337 | -50.23135 | 2025-09-12 04:08:00 | NPP-375D | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 04c2f49f-f77d-31db-a85f-17d61048bf29 | -21.76371 | -47.28157 | 2025-09-12 04:08:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a5d761a2-abab-35a2-98dc-c86ec48bc3d4 | -21.18624 | -47.52973 | 2025-09-12 04:08:00 | NPP-375D | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 008aa348-3f63-385f-9039-6632c6317ec5 | -17.36849 | -52.91915 | 2025-09-12 04:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| add7e7bb-fc81-3660-b2d0-d33d9acb2e53 | -20.70915 | -46.0567 | 2025-09-12 04:08:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9e3ac91-7b9e-360e-86d6-2260fb1ef353 | -22.81882 | -46.42812 | 2025-09-12 04:08:00 | NPP-375D | PEDRA BELA | SÃO PAULO | Brasil | 3536802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a0b039fe-47a9-31f8-9da4-8d7eec7a8bae | -22.68696 | -45.52472 | 2025-09-12 04:08:00 | NPP-375D | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c1f06df7-db81-3ef4-9ddf-e6f9b03bc066 | -20.26402 | -42.12308 | 2025-09-12 04:08:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 4be16e40-8327-39b1-bac7-365e2eeeb9c0 | -23.49188 | -47.25988 | 2025-09-12 04:08:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 82794065-35ee-3329-b183-360334fc1727 | -19.60735 | -43.57741 | 2025-09-12 04:08:00 | NPP-375D | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76dccdd1-cfcc-3bea-a7fe-a1ec68d23da6 | -18.59347 | -47.18612 | 2025-09-12 04:08:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 91794337-4172-3f5c-b4dc-82f33add2f42 | -22.62615 | -53.091 | 2025-09-12 04:08:00 | NPP-375D | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 16f87a14-0b35-3aea-bad5-a9d293de4e7b | -23.39552 | -46.70848 | 2025-09-12 04:08:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f076701d-8f23-3169-a6e1-32aed7b4632c | -20.70197 | -46.0769 | 2025-09-12 04:08:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8b18bef-e937-347f-9a66-a49a9dbc040d | -18.75182 | -47.62487 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3602bcb-82c8-392c-9d41-20bc47d386ca | -20.57117 | -43.74699 | 2025-09-12 04:08:00 | NPP-375D | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0f33cc89-f6cf-3b48-b683-82d0d4b5e8e7 | -18.68113 | -47.67691 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 92a09d12-5d78-39ee-b183-7fa51fa1eea3 | -19.87467 | -42.48152 | 2025-09-12 04:08:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f67e5cf1-3c90-3e4a-8293-e0dc09633d0c | -23.11164 | -47.49241 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ad9e7188-76fa-396c-9adf-685e13578f8e | -23.21948 | -49.42747 | 2025-09-12 04:08:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 928577a8-0a6b-3383-a632-00f56902b8e1 | -20.15546 | -43.68105 | 2025-09-12 04:08:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bd9218b1-860d-397e-b757-bc31a94b49db | -21.97346 | -47.55545 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecd47649-d9f8-3eab-a303-4684f1e79f4f | -21.32253 | -45.00661 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a4da6ff9-493a-3df1-9ad1-9780a52a7492 | -21.95596 | -47.56656 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 451d75f1-e3eb-31ad-87fd-4326b378eb36 | -21.33307 | -43.50804 | 2025-09-12 04:08:00 | NPP-375D | OLIVEIRA FORTES | MINAS GERAIS | Brasil | 3145703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d9ffa7db-c977-3f6d-a9c2-e27b6032c2f9 | -23.10097 | -46.67533 | 2025-09-12 04:08:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 3c2a2a49-80f0-380b-b1e7-50054fe107ad | -20.20861 | -44.55502 | 2025-09-12 04:08:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| d9782788-5bd6-3e4b-b278-5e7529453922 | -20.66096 | -43.13954 | 2025-09-12 04:08:00 | NPP-375D | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1a994659-8913-32f4-bb71-f80baf5c0c34 | -22.60421 | -47.27995 | 2025-09-12 04:08:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08263175-1c2c-3228-94da-d181ae0c6653 | -19.63534 | -41.57924 | 2025-09-12 04:08:00 | NPP-375D | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 68716ec9-20e5-3e9d-93f3-d833fbfcd4e8 | -18.77429 | -48.54731 | 2025-09-12 04:08:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6f6e273-f213-3583-991d-f7eaf9876272 | -21.9511 | -47.55083 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dc3673b3-0a0f-3664-8a5f-bdae4fc972f5 | -21.94101 | -47.56368 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c2f56771-19ce-3509-beaa-390924b3cce6 | -19.19941 | -48.00813 | 2025-09-12 04:08:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83a286e1-3dcd-3b42-959a-e1335727060d | -22.74651 | -47.61294 | 2025-09-12 04:08:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a0297f83-89f6-3c81-a208-f2ad6e68ccc3 | -20.56933 | -44.36248 | 2025-09-12 04:08:00 | NPP-375D | PIRACEMA | MINAS GERAIS | Brasil | 3150604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9b79648a-2e8b-3e33-b59e-59b602e9579b | -19.78719 | -48.28388 | 2025-09-12 04:08:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20cb7e75-d87c-3866-be47-ef94f4e6cc74 | -22.50344 | -44.90711 | 2025-09-12 04:08:00 | NPP-375D | LAVRINHAS | SÃO PAULO | Brasil | 3526605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fa2fccae-dfa0-30d8-a4d7-16b8c809c750 | -23.28472 | -46.47477 | 2025-09-12 04:08:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 13ff927e-8714-36c3-aa06-37f2f251e993 | -19.97175 | -47.592 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eeddddd7-9038-3904-bc03-2b9a8b5115b9 | -19.74783 | -46.09232 | 2025-09-12 04:08:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b542a46-c9a7-3701-b298-9cbf0fe6a3ab | -17.38194 | -52.93864 | 2025-09-12 04:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 447d1dc1-4b1f-363b-a930-d3e32547bdc9 | -19.99514 | -47.63841 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14fd0a5f-7147-313f-9984-0a8b1eecf85b | -21.84515 | -46.51129 | 2025-09-12 04:08:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d336772a-38f3-34c8-a762-cf324f5aa629 | -22.62105 | -53.08967 | 2025-09-12 04:08:00 | NPP-375D | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 7987423d-22e7-3ddb-b562-f840e9d12e3c | -21.3718 | -45.16861 | 2025-09-12 04:08:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a7bf4337-21d1-3d29-9685-4dee1bff2912 | -19.18644 | -48.01114 | 2025-09-12 04:08:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d68baa42-a575-3b13-9d39-aa0d1fc6b075 | -19.63816 | -41.58362 | 2025-09-12 04:08:00 | NPP-375D | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bb31c198-d8d5-3025-b586-394580eb27fe | -19.19542 | -48.00731 | 2025-09-12 04:08:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19166461-c8fd-3c44-a016-0a9cda0ebef3 | -18.77161 | -48.5386 | 2025-09-12 04:08:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7193297-19f5-34aa-bf01-11d2957af163 | -20.35044 | -49.95613 | 2025-09-12 04:08:00 | NPP-375D | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4adcd9ff-f3a8-30f5-9874-9db10189b809 | -18.67918 | -47.66533 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79c384ac-0c63-3747-84bd-c32916ab35d8 | -20.01532 | -47.63738 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0fa8cdb1-343d-34b2-b5d8-cd80d145cc30 | -22.65689 | -53.10223 | 2025-09-12 04:08:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ee62048d-e3b8-329d-aca8-0fcad8d1b973 | -23.35292 | -47.15584 | 2025-09-12 04:08:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fc93512e-db8d-39ea-b2d6-8fef3c2f599f | -19.64155 | -41.58419 | 2025-09-12 04:08:00 | NPP-375D | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1112dce2-196a-36b7-8353-7b3145a0189d | -23.13491 | -46.75326 | 2025-09-12 04:08:00 | NPP-375D | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a058825f-8513-36ae-b172-ae70d514a79f | -20.56844 | -43.74267 | 2025-09-12 04:08:00 | NPP-375D | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1d361040-3d22-3b29-823a-39254c5c1b0c | -22.61432 | -47.28688 | 2025-09-12 04:08:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8311fe5d-2d81-3562-b218-86751a4b2817 | -18.32332 | -49.33176 | 2025-09-12 04:08:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd1ffb3f-3075-3b04-94d1-0e9f2dab964e | -18.31476 | -52.0775 | 2025-09-12 04:08:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 512f3fd6-2b12-3e74-8607-12d5d6c8f9bd | -21.94937 | -47.5603 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 624c4188-ee3b-3f88-ac36-a0f58c8195f8 | -19.63196 | -41.57865 | 2025-09-12 04:08:00 | NPP-375D | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 34735615-aa39-3eeb-b6c7-bebef159282d | -22.70076 | -48.68946 | 2025-09-12 04:08:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 478fdb51-06b7-3a4d-b328-26cd1a8afd52 | -21.31991 | -45.02224 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 83948de4-4972-3647-9ce9-698382bcdeeb | -20.5651 | -43.74206 | 2025-09-12 04:08:00 | NPP-375D | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1ed24c67-cea2-340a-ae8a-05c7a1e42218 | -20.3542 | -48.40371 | 2025-09-12 04:08:00 | NPP-375D | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d47b03ef-fec2-3d64-805d-ba784ac84ff3 | -18.4488 | -47.18601 | 2025-09-12 04:08:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd75ccb1-edf2-33ff-8996-e520435f1fe1 | -21.3364 | -43.50865 | 2025-09-12 04:08:00 | NPP-375D | OLIVEIRA FORTES | MINAS GERAIS | Brasil | 3145703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f7eaf98b-9a06-35ba-b8bb-0f025d55e3f9 | -19.23997 | -48.04047 | 2025-09-12 04:08:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 5ee9c18d-6802-3d84-b974-218e8faae62e | -20.69767 | -46.08059 | 2025-09-12 04:08:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f46ec72c-1007-30d9-bf86-3f69f1b83119 | -19.241 | -48.03502 | 2025-09-12 04:08:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ee2e5701-739f-3335-97c2-d6d0b250e34e | -23.11077 | -47.49708 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b62bb4d4-7e34-36eb-a91c-c8b12642ab06 | -23.34862 | -47.20089 | 2025-09-12 04:08:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| dcfae19f-8c62-351a-9061-a4903c897cbc | -22.61396 | -47.28458 | 2025-09-12 04:08:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab9f67fd-523f-378e-84e5-8c6a499919de | -22.70365 | -48.69569 | 2025-09-12 04:08:00 | NPP-375D | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 40b5283e-a105-3e7d-8186-3f55bac9e97d | -17.37226 | -52.91597 | 2025-09-12 04:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eba4ee54-4362-3fe0-a4a5-171f0b6ec5cb | -22.19086 | -49.59016 | 2025-09-12 04:08:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 856f8c79-1f81-38d8-b6cb-09be787f93ea | -22.82159 | -46.43302 | 2025-09-12 04:08:00 | NPP-375D | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 9c91e975-c4fc-3695-bea7-e9841290a994 | -19.74046 | -45.94455 | 2025-09-12 04:08:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b818634-3bae-3dd5-8293-1b93d971e7da | -22.83647 | -47.46474 | 2025-09-12 04:08:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 20d79fc5-d0b3-3061-97cd-8d82b1f0890d | -19.97864 | -47.61953 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e418bbea-b6b3-3299-a94f-86c2a707f9b9 | -19.65929 | -44.90937 | 2025-09-12 04:08:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 53458446-cd41-3cc9-a0fd-8970f0d2c6fc | -23.1271 | -47.49086 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0afb4b5b-7154-37c5-b79d-4939a2b12620 | -18.32258 | -52.08522 | 2025-09-12 04:08:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b5cd036c-08f5-31eb-8bd0-1beefb69d84d | -19.65996 | -44.90543 | 2025-09-12 04:08:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 56cfbc1d-4f75-3b12-bcbb-12b87b3a7c55 | -23.12088 | -47.50408 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 547fd9aa-0ad4-34f2-bb05-f5a30727a91c | -23.1896 | -49.64532 | 2025-09-12 04:08:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7db4b17b-575e-3e97-a2de-c5b18b55b949 | -20.65545 | -46.53215 | 2025-09-12 04:08:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6888147f-2376-30e1-9f9b-0c7386223ba3 | -23.11925 | -47.50154 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| c130d48a-317f-3954-b669-fea09e99ecd8 | -20.81465 | -42.82806 | 2025-09-12 04:08:00 | NPP-375D | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6ca8464b-7a6d-3d95-b435-e1c879bcb92d | -20.35848 | -49.95565 | 2025-09-12 04:08:00 | NPP-375D | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3052f143-e656-328f-8b34-adc78f81472d | -18.53526 | -48.41268 | 2025-09-12 04:08:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b1cbad25-d385-3a71-8de3-938cacfb769f | -21.70935 | -46.2545 | 2025-09-12 04:08:00 | NPP-375D | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README56.md)
