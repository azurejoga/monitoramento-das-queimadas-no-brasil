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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1c40fc9-bfb2-3a85-afc2-4309945d4ae5 | -20.40159 | -45.39986 | 2025-08-15 04:32:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cd1d2d83-45d9-3650-bda8-2592541e63da | -20.56864 | -47.09875 | 2025-08-15 04:32:00 | NPP-375D | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ac31995-3045-3110-afa8-2e9fe4a38e90 | -18.51604 | -46.27914 | 2025-08-15 04:32:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f09f53d-55b1-3a07-94bf-a70b37172c00 | -22.95892 | -48.82075 | 2025-08-15 04:32:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 869838e2-4dcf-3cbb-b0d3-fbf2e4e9182e | -20.40096 | -45.40455 | 2025-08-15 04:32:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 83a01756-8ea9-3d6f-a9bd-e26f5b71a9b9 | -20.00831 | -42.20155 | 2025-08-15 04:32:00 | NPP-375D | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 404aceb5-564d-3416-92c2-9b45e5fc8171 | -22.98557 | -49.17856 | 2025-08-15 04:32:00 | NPP-375D | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c951ad5-5a88-359a-a469-0c65ecfeba2c | -18.94626 | -48.18075 | 2025-08-15 04:32:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 833b11a0-228f-3860-8e44-7855c2c72852 | -19.47372 | -43.61666 | 2025-08-15 04:32:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f377e653-6e27-373d-8c99-b3cb8d44db5c | -20.51289 | -47.41407 | 2025-08-15 04:32:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44630b05-95fe-3165-b228-eebe9f78af56 | -21.19199 | -45.68789 | 2025-08-15 04:32:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2f30cbe-f5c4-3805-92c4-c4eaad717d8f | -22.83545 | -46.42628 | 2025-08-15 04:32:00 | NPP-375D | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ad4f7cec-c0e7-30a0-b7cc-2f6bcce076dd | -17.56592 | -52.53007 | 2025-08-15 04:32:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f23f3a7c-3342-3a95-9b67-f9198d3f848e | -23.20411 | -46.74517 | 2025-08-15 04:32:00 | NPP-375D | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d76a79e4-6299-307d-8c31-97bfa1e7bfdd | -19.6969 | -51.1654 | 2025-08-15 04:32:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d77fade-fd80-3880-a73d-30e9080186f6 | -22.71572 | -47.32881 | 2025-08-15 04:32:00 | NPP-375D | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4da9b3af-6f82-3fd9-8baa-e9d34bd6e9b9 | -15.9656 | -59.51424 | 2025-08-15 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e18d5ee0-f893-3d2e-a06c-5fef9d845b34 | -20.59809 | -51.60993 | 2025-08-15 04:32:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6613f6a9-1893-3084-bbb4-741455052db2 | -18.50941 | -50.65006 | 2025-08-15 04:32:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 447e5ba0-2c83-32f8-9761-18fd316b482e | -18.53375 | -45.44933 | 2025-08-15 04:32:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29bb7030-275b-3ec8-a53d-50a25c44ce34 | -22.39736 | -45.47977 | 2025-08-15 04:32:00 | NPP-375D | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5275f9f2-0e63-3550-a8bc-97d81a9805ea | -21.1703 | -50.24831 | 2025-08-15 04:32:00 | NPP-375D | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 64566d30-bbbf-34af-afc4-3883070d0c9f | -16.48001 | -51.98326 | 2025-08-15 04:32:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c4748a0-c9a6-3da5-9ae8-101e2f5c009f | -22.04864 | -48.33798 | 2025-08-15 04:32:00 | NPP-375D | TRABIJU | SÃO PAULO | Brasil | 3554755 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6994e004-b6d6-3d56-aa7c-57b5bf8d9be6 | -15.9706 | -59.51965 | 2025-08-15 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aeed156f-4923-39f7-8e3a-f79f6c2e5b6c | -18.94569 | -48.18445 | 2025-08-15 04:32:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0f0b5fcb-cf35-3f01-8ff7-4f834adbf994 | -23.40583 | -47.11459 | 2025-08-15 04:32:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cdcb552f-632e-37ce-9cd6-83ff0651a6b2 | -18.63666 | -49.08647 | 2025-08-15 04:32:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f13cd320-d7b0-31fb-9c5c-4534ea058d11 | -18.00818 | -49.39758 | 2025-08-15 04:32:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0bf3ea7b-24c1-3e90-a5f0-85105e0bd2e7 | -19.90625 | -47.47246 | 2025-08-15 04:32:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8b390fb-6fb0-3e5c-9360-dba69417b9aa | -21.99484 | -44.88112 | 2025-08-15 04:32:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 252794ff-c9f2-3a21-be91-9f2ca37a858d | -22.77816 | -46.74225 | 2025-08-15 04:32:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 60d058be-3c41-38d6-8e8f-ad8abf665d8a | -23.10518 | -52.09613 | 2025-08-15 04:32:00 | NPP-375D | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e8cfb7b1-96dc-319a-a765-913220aa9ba7 | -16.38631 | -50.91021 | 2025-08-15 04:32:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9600bb50-efdb-38f5-b0ca-6252419baf78 | -22.68476 | -50.47432 | 2025-08-15 04:32:00 | NPP-375D | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3547f502-8ad3-3518-9988-df83a72b13fc | -20.85397 | -46.38099 | 2025-08-15 04:32:00 | NPP-375D | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6704dc3-c708-3146-83b8-d90b2d433faf | -16.31816 | -52.92215 | 2025-08-15 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10d38c98-18cf-38a2-80be-a0276a58300c | -16.42401 | -51.0913 | 2025-08-15 04:32:00 | NPP-375D | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6e0f10d7-20b2-3c32-ab9b-f4f2fb80c640 | -21.19144 | -45.69 | 2025-08-15 04:32:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edf66a38-082f-34de-8c0d-18ae12d525e4 | -17.05817 | -51.7984 | 2025-08-15 04:32:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17a435a9-9bcf-38bd-929b-4d017cb71a0b | -23.4094 | -47.11524 | 2025-08-15 04:32:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| add8b038-d43b-30ba-97b8-ad31141d55f4 | -17.55806 | -49.41766 | 2025-08-15 04:32:00 | NPP-375D | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8ecbcc0d-c605-3cba-b559-1ab27bb75106 | -17.49499 | -47.84118 | 2025-08-15 04:32:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e5a1637-4d5e-36ab-a77e-d8263b5792a2 | -16.30561 | -52.92533 | 2025-08-15 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| d5fd458f-32d4-3389-a515-422deb0ac742 | -17.64683 | -44.48926 | 2025-08-15 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39b31cac-3128-341a-abbf-14cf0251ca89 | -16.47631 | -51.9828 | 2025-08-15 04:32:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a719373-893e-3586-a5f1-27c8806701a2 | -23.34346 | -46.89425 | 2025-08-15 04:32:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0141d1d0-c9ea-3280-866f-2923dfe96374 | -16.3898 | -50.91083 | 2025-08-15 04:32:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3401154b-7a44-38ab-857c-383a4898d60f | -21.8438 | -46.68521 | 2025-08-15 04:32:00 | NPP-375D | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d3910df2-8be6-3235-b97e-aeaeac369ace | -18.69903 | -48.18133 | 2025-08-15 04:32:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 06cceb63-84ca-3e49-b4f5-62f5fc578c9d | -22.39802 | -45.47482 | 2025-08-15 04:32:00 | NPP-375D | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d2a06853-609a-3deb-bc18-9e466dbbf3cd | -16.38557 | -50.91115 | 2025-08-15 04:32:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11bd1c84-f954-3af2-a3bf-efc82ee4ed5e | -19.7841 | -43.73337 | 2025-08-15 04:32:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1882c7e-d033-364d-a00a-af01f4ac8209 | -16.47552 | -51.98729 | 2025-08-15 04:32:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 359f81eb-0860-3984-a7b6-92714e27e1f3 | -18.00876 | -49.39391 | 2025-08-15 04:32:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1dce6a62-d089-3b6f-99ac-04d60fd7de63 | -17.05534 | -51.79332 | 2025-08-15 04:32:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78a9206f-68c3-3917-b10b-fadd44e81bc8 | -17.49556 | -47.83749 | 2025-08-15 04:32:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4ba3705-555f-3b58-8300-b256d37d5521 | -16.4726 | -51.98238 | 2025-08-15 04:32:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48e2cdd8-3f48-3a08-a65f-5a3daa1a0096 | -19.67195 | -44.60099 | 2025-08-15 04:32:00 | NPP-375D | SÃO JOSÉ DA VARGINHA | MINAS GERAIS | Brasil | 3163102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8974b89c-15ca-331c-85a7-45de4c8b9465 | -18.96976 | -49.49997 | 2025-08-15 04:32:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e5c1628-ef9d-3742-abe1-1861a268a4cf | -23.1797 | -46.60019 | 2025-08-15 04:32:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4a601f3f-2619-3be8-807b-91f59548d931 | -22.39955 | -45.47645 | 2025-08-15 04:32:00 | NPP-375D | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 67366352-a489-3b41-99a2-cd058fc6f6dc | -15.385 | -59.82522 | 2025-08-15 04:32:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a98451a8-c932-3f38-85ec-a120d9ad4de4 | -16.39401 | -50.90731 | 2025-08-15 04:32:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88140199-434b-398e-9fe7-df94b2b6132f | -23.63889 | -51.6263 | 2025-08-15 04:32:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| bcf3afd4-c3eb-368b-a8f6-23b1237013a0 | -18.94291 | -48.18019 | 2025-08-15 04:32:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee105ea0-032b-37fe-bd25-92b7a3fa2d04 | -16.90682 | -52.55262 | 2025-08-15 04:32:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16367a3c-5812-3051-ac42-bbe131a7c4c3 | -17.55472 | -49.41708 | 2025-08-15 04:32:00 | NPP-375D | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 13c0bc18-62d8-3f7f-b9fd-e5dcc9026d08 | -20.59519 | -47.85492 | 2025-08-15 04:32:00 | NPP-375D | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efe5ac5f-df31-3fa1-a0dd-62170e408565 | -24.1702 | -50.35242 | 2025-08-15 04:32:00 | NPP-375D | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ec590a5f-f42c-3087-b37b-60f240c7e7aa | -20.3249 | -45.2288 | 2025-08-15 04:32:00 | NPP-375D | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 3b9266a2-f1dc-37fd-b66d-19ce893773b9 | -17.05892 | -51.79408 | 2025-08-15 04:32:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8044e679-50b9-311a-af3a-75acf46c91fc | -18.87191 | -51.99903 | 2025-08-15 04:32:00 | NPP-375D | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94f9c8dd-a2f8-3750-8d20-d35ba6ff7cc0 | -20.39783 | -45.3993 | 2025-08-15 04:32:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4c92686b-58e0-347d-8bc6-3a76ebc275a3 | -16.38839 | -50.91586 | 2025-08-15 04:32:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 121a1f0b-d0f6-3b31-9187-d1317b4d9632 | -20.97855 | -47.42093 | 2025-08-15 04:32:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bab4a85b-167b-35eb-933d-31021ca6b027 | -18.69569 | -48.18077 | 2025-08-15 04:32:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 8920a406-cbe5-377e-8ae8-1280b619fce0 | -23.98046 | -51.27596 | 2025-08-15 04:32:00 | NPP-375D | FAXINAL | PARANÁ | Brasil | 4107603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b79a0996-8a20-3731-835e-e756bcea6c4e | -19.46914 | -47.16136 | 2025-08-15 04:32:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d39bff2-2a22-3fae-a922-5a883d8b645f | -19.5489 | -44.83949 | 2025-08-15 04:32:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a700cad-217e-3e49-8b65-0d0a0e22fa77 | -16.47923 | -51.98769 | 2025-08-15 04:32:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25484259-4809-3af0-a271-21a6621943b9 | -21.1921 | -45.68522 | 2025-08-15 04:32:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 515f75ca-1d8b-3878-83d3-ecac07ae6551 | -18.73645 | -46.90945 | 2025-08-15 04:32:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b50a2715-7008-317a-ab0d-f81495715931 | -19.64308 | -46.09636 | 2025-08-15 04:32:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e4a6b9c-976a-3fdf-b7fa-974d40e01c23 | -21.63302 | -46.99011 | 2025-08-15 04:32:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ec0678f-4e10-3a41-831b-3a4e05fc2251 | -17.49221 | -47.83694 | 2025-08-15 04:32:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83be4575-28d5-302d-9dca-fc5b9224f002 | -19.11711 | -44.46976 | 2025-08-15 04:32:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd911035-39d8-308a-93d1-5ad8bed278e3 | -16.3891 | -50.91493 | 2025-08-15 04:32:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b121cbcf-ead3-35c4-bedc-347f40e1bfae | -18.96917 | -49.50362 | 2025-08-15 04:32:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52d1a328-7b77-3ae7-9c05-b0b952f24c3a | -19.64057 | -46.93106 | 2025-08-15 04:32:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7f812c0-d20f-3d3b-b953-656bc3a9f246 | -20.97913 | -47.41692 | 2025-08-15 04:32:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f8feacb-f63d-32cb-a473-b605f915ec0b | -20.00842 | -42.20328 | 2025-08-15 04:32:00 | NPP-375D | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f4feb390-397f-3faf-93eb-595efbdef281 | -22.57164 | -47.02559 | 2025-08-15 04:32:00 | NPP-375D | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d0d69ce-c616-3056-a640-6652d3bcaaf5 | -16.30175 | -52.92461 | 2025-08-15 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 94370089-cc81-334d-8591-5c70ada02ecb | -16.29786 | -51.74014 | 2025-08-15 04:32:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dbeac6c3-b19e-3c69-9630-a6e17930130e | -17.50026 | -48.00714 | 2025-08-15 04:32:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd8a050f-955b-325d-a78b-5a8ba48fbd3d | -17.65532 | -46.68309 | 2025-08-15 04:32:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a41a18b3-7f0f-306a-ad21-3d69f045480b | -23.4093 | -51.84944 | 2025-08-15 04:32:00 | NPP-375D | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5d4808b0-fc95-352c-8cba-7aedc5411f40 | -17.64559 | -44.49841 | 2025-08-15 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6d7eb6ce-0a51-30fe-a856-8ce8b9ede0e1 | -16.69226 | -49.37001 | 2025-08-15 04:32:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README39.md)
