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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c16ef63-f2e3-3bd8-9607-2600f1048897 | -16.40793 | -44.04617 | 2025-09-11 03:57:00 | NOAA-21 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0a4c266-3486-3888-b247-30bcdff0fb5b | -14.40733 | -47.32365 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9c3c6bad-b6f5-3af4-86b7-2d37808d1133 | -19.99904 | -47.62524 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 164714b3-49f0-3943-b1f0-fd8955675158 | -17.59694 | -44.75991 | 2025-09-11 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7784ab36-8d6d-35d2-b86f-7145f7777db7 | -19.9595 | -46.88078 | 2025-09-11 03:57:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e2f91fb-277d-3663-84b4-e672b66ec7a0 | -14.85201 | -46.78793 | 2025-09-11 03:57:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a011ad1-c182-35eb-9c9a-8038dcce38d3 | -15.12827 | -52.41416 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 589a4358-0920-3823-9c83-ba352903f5b1 | -14.91737 | -47.3121 | 2025-09-11 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45b0f36c-9caf-3785-b368-2cd3b8304f07 | -20.38918 | -46.24184 | 2025-09-11 03:57:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57a8797f-74e0-3f5f-a3d5-8f5330348869 | -16.56919 | -49.73638 | 2025-09-11 03:57:00 | NOAA-21 | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 421c771b-71b5-3676-b6be-564af5bea850 | -17.79682 | -44.41001 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffcc5782-881b-3af2-be15-7f3233fc27c4 | -13.0167 | -48.72437 | 2025-09-11 03:57:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b07f018c-a759-3283-aa16-7c2b7a72b2d3 | -15.80797 | -52.27776 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 29e5391d-7494-395c-a174-d766152a101d | -16.43264 | -45.68902 | 2025-09-11 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4b93275-d611-3122-87b4-284b88f89126 | -14.40434 | -47.31463 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6bf051a-3eaf-3c99-bd21-23b50cbd63a8 | -18.35057 | -49.32644 | 2025-09-11 03:57:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 302b4266-4dbe-3784-9f40-649536646aa4 | -20.17453 | -42.21876 | 2025-09-11 03:57:00 | NOAA-21 | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c9d8206f-6dd5-3099-a700-0875b02fb23f | -19.8756 | -41.41574 | 2025-09-11 03:57:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4cc60023-524c-359e-9154-04f84da3e17e | -17.56625 | -44.54684 | 2025-09-11 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9815bb6-189f-3ac7-902b-ff80b7aab79d | -16.88625 | -45.75177 | 2025-09-11 03:57:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df6fb4fd-a13a-3571-962a-60c1de380254 | -14.28183 | -49.3974 | 2025-09-11 03:57:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bda22336-9546-3a6e-b4e5-ac14cbd9d1bd | -20.51712 | -47.62943 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 054833ba-f76c-333f-b096-3cc286fea745 | -18.73173 | -40.69838 | 2025-09-11 03:57:00 | NOAA-21 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5aa2e5a1-a835-3eed-ad22-8a58ccc61c39 | -15.22163 | -44.05292 | 2025-09-11 03:57:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 141ac8a4-3f8b-3ee6-b029-acd6bb605f68 | -14.30618 | -45.04153 | 2025-09-11 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64d4305e-f7ea-388e-978e-9f09700ac566 | -18.06721 | -39.74175 | 2025-09-11 03:57:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5fae2771-6408-3942-95e8-54b3b60584d1 | -16.63101 | -49.76063 | 2025-09-11 03:57:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44eed990-3081-313e-8b79-7f4bffafbb77 | -17.93915 | -44.48392 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 71369ebd-03c3-3678-8104-5bc166868ea4 | -19.99063 | -47.62401 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| c495fece-e9bd-36fb-8689-3eaa579657d7 | -15.66946 | -47.0339 | 2025-09-11 03:57:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 550ee0c1-d4f6-3d58-a767-0bc847eeed2b | -20.07407 | -47.52549 | 2025-09-11 03:57:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf4af1b3-33cb-374c-b3bc-06b78451b8ca | -17.57788 | -47.49426 | 2025-09-11 03:57:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f2e91b8-7faa-3733-9b26-52ea6e0f7edb | -14.39605 | -47.30901 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 614b3790-239a-3ce5-9509-0ed7d17a3f49 | -19.55259 | -46.94791 | 2025-09-11 03:57:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 69be8eb2-cae7-3fe4-9832-e6b3045fa3a7 | -17.84541 | -46.74806 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 857aa0b4-56d6-36a0-85cf-4417bc765d14 | -12.84697 | -47.96462 | 2025-09-11 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5a141391-e81b-37a4-bd9e-a47a46f91941 | -20.92752 | -45.78982 | 2025-09-11 03:57:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3220250c-dec7-31a9-881d-58b4dee64c8d | -19.14041 | -43.05433 | 2025-09-11 03:57:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d277a45e-26fd-3588-b4b1-f3dc57ac7e79 | -18.01246 | -47.13199 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6207fec1-7b5f-3c6c-87f9-addfcfad6c7b | -20.16129 | -41.03912 | 2025-09-11 03:57:00 | NOAA-21 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 6f95d2eb-559a-3e0e-b8ec-bf82c01039a5 | -14.28026 | -49.39964 | 2025-09-11 03:57:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 473def47-6cea-3757-9874-331cf492ea90 | -18.35432 | -49.33252 | 2025-09-11 03:57:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4727066-f81d-3d32-873f-7cf5d90a6716 | -15.23044 | -44.04541 | 2025-09-11 03:57:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c4d5cdd-9e69-3fe9-8fd4-87abbbd91e64 | -16.26527 | -46.78545 | 2025-09-11 03:57:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e812bcd-a41f-3460-a09b-d21f9edf5bbc | -16.61532 | -49.78568 | 2025-09-11 03:57:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 901a8694-1dab-344f-86fa-660ef08822e8 | -19.66166 | -44.89906 | 2025-09-11 03:57:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e959fc1e-fe08-32db-af09-12b53ce981c0 | -15.10922 | -50.14497 | 2025-09-11 03:57:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ad19bd8f-5417-3258-8171-5feea9d1de8a | -17.76825 | -44.38244 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33e9a582-bee2-3669-b91c-5e575ef2935e | -18.57015 | -47.41585 | 2025-09-11 03:57:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4230df52-7e44-3da2-8058-cd3f524aa9a0 | -18.60703 | -43.96988 | 2025-09-11 03:57:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c4cb0c2-24c0-3056-b521-92a05c7d360b | -16.61072 | -49.78222 | 2025-09-11 03:57:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6434bbac-bea7-3cf5-8c7d-93e79dd149fa | -17.24772 | -46.75974 | 2025-09-11 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5be3752-4d23-3663-a11f-340d069d33eb | -20.24264 | -43.57975 | 2025-09-11 03:57:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 372e5a42-a141-3b61-af28-0efab74cabc2 | -14.78066 | -48.2278 | 2025-09-11 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c75f8d6b-f416-3e67-b1f5-a69a1633b146 | -19.72587 | -43.91265 | 2025-09-11 03:57:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9cc8948d-84d8-34ec-9bfc-c6e80af6eec4 | -19.46996 | -46.13015 | 2025-09-11 03:57:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69023df4-16ed-3399-a4b3-e096fd4ea46a | -19.4604 | -43.71342 | 2025-09-11 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46962ea1-9f40-328a-8b7a-70ffe7d0497d | -20.17512 | -42.21507 | 2025-09-11 03:57:00 | NOAA-21 | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 69e3615a-db7e-3000-b000-898a732ad9a5 | -15.98446 | -42.98033 | 2025-09-11 03:57:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e56cafdd-5519-34b9-af98-83f057a9d936 | -18.06007 | -50.73096 | 2025-09-11 03:57:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 60609e74-85f7-384f-bcd7-e67a593710ce | -20.46909 | -42.8428 | 2025-09-11 03:57:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d0f96817-0505-38ed-8826-c179ea67f844 | -13.78932 | -46.2844 | 2025-09-11 03:57:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| eecfc453-65e0-3c6a-b27c-89aaf728d79c | -16.2915 | -45.6863 | 2025-09-11 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a83750bc-f95a-33f8-ac79-c28c19cc35e2 | -16.60877 | -49.7767 | 2025-09-11 03:57:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 893843ec-555f-3a23-b63b-587546f48c25 | -13.85494 | -43.82276 | 2025-09-11 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fc99c332-1e26-37ff-b765-b21295aabccb | -18.60774 | -43.96575 | 2025-09-11 03:57:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6f0f0714-baf1-3814-87ad-d531ce5179b9 | -20.36817 | -46.66266 | 2025-09-11 03:57:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 80310418-1fcd-3703-a0de-b562059ce8e8 | -19.64769 | -45.04281 | 2025-09-11 03:57:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a306672a-b881-3f97-942b-d64766dea64b | -15.81915 | -48.94427 | 2025-09-11 03:57:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f19115de-406c-35ea-aea8-223ee7eed950 | -16.69524 | -44.34179 | 2025-09-11 03:57:00 | NOAA-21 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21ac5cae-2cce-3831-9108-4b6f75581a56 | -19.9132 | -42.25601 | 2025-09-11 03:57:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7eaa5867-a69a-31de-9d86-dee2102cbe93 | -15.20492 | -44.04079 | 2025-09-11 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ae23f80-2784-3d4d-8cea-4a6fe46d263d | -17.56106 | -44.5552 | 2025-09-11 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3b640056-5a44-3bc8-8e2c-c183db2111f3 | -18.60156 | -43.95981 | 2025-09-11 03:57:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1c4358c-d64b-3e6b-b67f-0a6c1c514097 | -14.28618 | -54.7496 | 2025-09-11 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3a6fb074-52c1-373a-ac03-6264e957d238 | -15.54793 | -54.76276 | 2025-09-11 03:57:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3a7dad38-65ec-36c7-b013-d362a715034a | -15.56014 | -54.74805 | 2025-09-11 03:57:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| af73197e-fb71-3ad5-a6d9-bc15ad2876b4 | -17.64482 | -44.74562 | 2025-09-11 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc41b51e-d99b-3755-bc64-ae1717ed398d | -15.11901 | -52.39738 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2d818f8-dfe2-3429-a85a-d67553874048 | -17.47712 | -45.10408 | 2025-09-11 03:57:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6240e373-25f5-3854-99bb-95cbbc7039f1 | -20.00728 | -47.62737 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00e48378-dc69-3dd1-8661-43a5aded8575 | -18.15864 | -48.09581 | 2025-09-11 03:57:00 | NOAA-21 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c68f024-1cd4-36b2-acc3-1d55a168fb87 | -13.32463 | -46.37447 | 2025-09-11 03:57:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 745d6f4d-6af1-3480-8a49-a0157488e24c | -15.20051 | -44.04455 | 2025-09-11 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| adc094b3-9be6-3a7a-9c66-a8edfe7fa296 | -15.12705 | -52.41987 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8ae0cdcb-c847-3a52-a308-0b1056c0f94c | -15.95853 | -50.22357 | 2025-09-11 03:57:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fbc04107-24fe-3fa9-9797-12dcea54c62f | -16.62175 | -49.78014 | 2025-09-11 03:57:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a41150b7-6ea7-3156-9a4b-54d44942e381 | -16.32625 | -43.75858 | 2025-09-11 03:57:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41439413-b82a-3c6d-8ad8-3e410cbab2a3 | -17.15784 | -44.45005 | 2025-09-11 03:57:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 044d4a10-b951-3395-af64-2e94cef6ae35 | -15.55807 | -54.75039 | 2025-09-11 03:57:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f7a8e0f0-141a-3a9e-b44e-c132045dc4c0 | -19.95555 | -46.87986 | 2025-09-11 03:57:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6c5b1d9-97bd-32c8-b731-42c6256e304c | -12.84216 | -47.96352 | 2025-09-11 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ac12c5a0-a734-3185-a914-b9170c6fccba | -14.30738 | -54.75478 | 2025-09-11 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32d0a1e9-baea-397f-90d5-7655df1df4e0 | -14.30633 | -44.99474 | 2025-09-11 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 193974b3-c6b2-3282-a35d-3a435abb9f1e | -19.98494 | -47.63104 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 913d1acc-f37b-37a9-8c02-ac71a00a9e7d | -20.16814 | -44.62329 | 2025-09-11 03:57:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f002896-b806-3473-ad27-2dfd47149061 | -18.48477 | -41.19691 | 2025-09-11 03:57:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5d006818-b191-3660-a919-f44f977dbaed | -15.80593 | -42.57133 | 2025-09-11 03:57:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ce61ba69-8c02-3630-88af-c3b482337914 | -20.7077 | -46.05618 | 2025-09-11 03:57:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48dbb255-8423-368d-9da9-aa8c7d0405dc | -14.35903 | -47.29964 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README34.md)
