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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3575a54a-41dc-34c8-a616-20dd09838b53 | -21.2563 | -50.8746 | 2026-04-26 00:10:00 | GOES-19 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.4 |
| c98e8ef3-4673-31d1-8123-9725a4467a28 | -21.49839 | -51.77198 | 2026-04-26 00:33:00 | TERRA_M-M | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 5c79e899-fc72-300f-89bd-f81d406492d6 | -23.60518 | -52.90087 | 2026-04-26 00:33:00 | TERRA_M-M | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| ac5f1cb9-e6d7-37bd-9293-50bd26533444 | -23.54675 | -48.0102 | 2026-04-26 00:33:00 | TERRA_M-M | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5cb5c9f5-d8a1-3cfc-8f33-a5479b5f3827 | -20.18005 | -46.92102 | 2026-04-26 00:33:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 36cb39a0-b73e-3c54-9a68-82e5d4dac8ba | -21.18302 | -56.50299 | 2026-04-26 00:35:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2f37cfae-cadf-3949-a226-1a911c37f41c | -21.17188 | -56.50424 | 2026-04-26 00:35:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 079b0906-33a8-31e1-bb6c-289fcf5e7a69 | -18.28709 | -54.13494 | 2026-04-26 00:35:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6600ffa8-52b4-39b6-ba37-33623e6ed5bb | -18.50539 | -55.50562 | 2026-04-26 00:35:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 4e969dd1-3400-3263-88c1-45fb06a201fb | -18.22836 | -54.59762 | 2026-04-26 00:35:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a0c37e20-522e-3165-97b8-dab5e93635ff | -13.38898 | -45.32693 | 2026-04-26 00:35:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| b1373bc3-97e5-3ee0-a7d7-3936d6e24dd3 | -21.4963 | -51.762798 | 2026-04-26 01:01:00 | METOP-C | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8ab91e97-0ed1-3966-88b4-a19c988fb238 | -21.1737 | -48.894402 | 2026-04-26 01:01:00 | METOP-C | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1ec971d1-efdc-30b4-9d84-85539c5cf909 | -21.4979 | -51.770199 | 2026-04-26 01:01:00 | METOP-C | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 24b582bc-b2ae-39e7-b818-e120a2650374 | -20.0516 | -47.9403 | 2026-04-26 03:00:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 35727491-2c7a-34c6-9d31-d8720008c982 | -20.0523 | -47.917 | 2026-04-26 03:00:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 033111eb-d0ef-3291-b322-92e06950688e | -18.75638 | -40.2704 | 2026-04-26 03:02:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 69b70e51-923a-353a-8637-5a4660f38686 | -8.79267 | -37.31319 | 2026-04-26 03:32:00 | NPP-375D | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a5be2dee-d7a6-376b-9b2e-126585bc7daf | -11.07419 | -45.27532 | 2026-04-26 03:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0b3ced6-0e53-3969-a52c-c065b3fcc25d | -8.78836 | -37.31213 | 2026-04-26 03:32:00 | NPP-375D | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 34a6933a-ca8a-355d-a0e6-c01721d86812 | -11.08117 | -45.27652 | 2026-04-26 03:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5a7b2fd-296c-3196-aa59-8b969f2f831d | -11.07556 | -45.26871 | 2026-04-26 03:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b97ec23-b217-3149-81d0-1e266a79f654 | -15.82319 | -43.77963 | 2026-04-26 03:34:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ed30c01a-3f23-3c1d-8d8b-287a7128e09e | -18.75643 | -40.27068 | 2026-04-26 03:34:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 414f51a7-57bb-3338-972c-a79b167278c5 | -14.79548 | -42.8083 | 2026-04-26 03:34:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f8c7f847-1f77-3828-8e73-fd6cd9d5c7d3 | -14.78893 | -42.81163 | 2026-04-26 03:34:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6fcf2a57-a9f9-36dd-8543-bb993f1601f7 | -14.79466 | -42.81231 | 2026-04-26 03:34:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bf3ec88f-fdd5-34ab-b5fa-8767052e7441 | -19.47731 | -40.66104 | 2026-04-26 03:34:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2d06a4a1-5cea-3417-9759-c373a5cbba10 | -13.38915 | -45.32807 | 2026-04-26 03:34:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb3062f1-9e1b-3ddd-8f05-3c6e34c963a8 | -13.39452 | -45.33564 | 2026-04-26 03:34:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05963404-f821-3b4f-9968-7a0343c3b053 | -15.82229 | -43.78395 | 2026-04-26 03:34:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 16f5e13b-4103-32c6-a266-6e293537a4fa | -18.75198 | -40.26979 | 2026-04-26 03:34:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ffddb7b8-74ad-30ff-89f3-400ec2c80d0a | -20.19217 | -46.87461 | 2026-04-26 03:36:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 90982efb-0e62-3ed5-a4dd-ab625d44e4d9 | -20.18214 | -46.91694 | 2026-04-26 03:36:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2895aacd-7184-3b46-ba34-eccb3211c528 | -20.4578 | -45.5718 | 2026-04-26 03:36:00 | NPP-375D | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f7db204-5b17-330a-8c77-067c62990619 | -20.46383 | -45.57291 | 2026-04-26 03:36:00 | NPP-375D | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 226f048c-7f57-3f1f-8989-26183a59a1a5 | -20.19338 | -46.86951 | 2026-04-26 03:36:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 186e0d2b-08a8-354d-8243-5493764479d3 | -20.176 | -46.91403 | 2026-04-26 03:36:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1846a5b9-68b5-3c10-bbab-775798c94470 | -20.18103 | -46.92159 | 2026-04-26 03:36:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 56c9e285-fb40-31db-98a9-b430407f37bf | -12.07709 | -44.01772 | 2026-04-26 03:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12991b37-59e7-3ca6-b550-423cd9f476c3 | -11.07707 | -45.27219 | 2026-04-26 03:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 30ea0ca5-a792-3e9b-a998-107c1ef49551 | -13.65343 | -43.73608 | 2026-04-26 03:51:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e4918c7e-529e-351c-8a07-90371a5bb399 | -11.078 | -45.2671 | 2026-04-26 03:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 91b9057b-e6a2-32d8-a943-8bc264c7b36d | -9.08002 | -37.64864 | 2026-04-26 03:51:00 | NOAA-20 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0347d8b3-ce43-3b8f-853e-cdc4f9c9eedc | -8.79031 | -37.31292 | 2026-04-26 03:51:00 | NOAA-20 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7c0ae6f4-6802-3959-a04f-7ecd39a01e8e | -11.07329 | -45.26632 | 2026-04-26 03:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04632b00-008f-3a4f-9293-85d106e4dbcd | -14.79184 | -42.81063 | 2026-04-26 03:51:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d6152a60-96e2-380e-9cbc-8a34e8977b5e | -11.55493 | -48.26442 | 2026-04-26 03:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5f931545-eeb4-3147-aca1-b3bf740943ba | -8.79086 | -37.30944 | 2026-04-26 03:51:00 | NOAA-20 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e3b8c87d-54b7-3c03-81c1-b476c0c4be4b | -13.88284 | -43.78717 | 2026-04-26 03:51:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 361127a5-0978-3671-be3e-36e3d391a606 | -13.88349 | -43.78349 | 2026-04-26 03:51:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7288481b-c924-3fa2-83c4-f89100d19dd6 | -20.18675 | -46.93799 | 2026-04-26 03:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca6b846f-96af-35c5-931c-e38d32be3a61 | -20.18168 | -46.91723 | 2026-04-26 03:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 37e5a5dd-bf21-3540-b498-6770798bf3c7 | -20.18244 | -46.93642 | 2026-04-26 03:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7be39592-d659-361d-9cd3-359ac8a4d782 | -15.55345 | -42.63841 | 2026-04-26 03:53:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9fb19eb6-e76f-38d9-8962-9f4daa490ad6 | -20.45948 | -45.56903 | 2026-04-26 03:53:00 | NOAA-20 | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6081d5b2-dd8d-36cd-b172-ce7d33628723 | -20.19115 | -46.87006 | 2026-04-26 03:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4b5258a0-0b21-392f-b0bd-3b8b998d0c5d | -15.82199 | -43.77934 | 2026-04-26 03:53:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 50951925-41e4-3380-a5c3-bc6d2ea8d76d | -20.17735 | -46.91582 | 2026-04-26 03:53:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1aa0da9e-cc0b-3f44-865f-fcadafc27f87 | -20.18513 | -46.92306 | 2026-04-26 03:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24c47adf-9480-3cb7-8625-69110563f5fc | -20.46283 | -45.57353 | 2026-04-26 03:53:00 | NOAA-20 | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35f17fa5-4398-320b-8c68-e75189678f14 | -20.17819 | -46.91162 | 2026-04-26 03:53:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8371f65b-52db-3869-93f7-a59a0ad7c76a | -21.12245 | -42.20212 | 2026-04-26 03:53:00 | NOAA-20 | EUGENÓPOLIS | MINAS GERAIS | Brasil | 3124906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 916bbae0-6332-3b25-a1f3-51867157b134 | -15.82592 | -43.78013 | 2026-04-26 03:53:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4fa133cb-a4e4-3537-8fa6-058f311c04ea | -20.05014 | -47.92584 | 2026-04-26 03:53:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 939abcdc-73ea-3b6c-a984-f89ecbd89a52 | -18.75453 | -40.26788 | 2026-04-26 03:53:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a6c2bc5c-0848-34da-b95c-90ea8694bc4f | -19.47618 | -40.65927 | 2026-04-26 03:53:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 2cffc382-98b2-3dad-9746-a18a4f5a2909 | -15.82106 | -43.78454 | 2026-04-26 03:53:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c16ee202-2d77-3ed0-a33d-96cf5deae16e | -20.50761 | -40.37609 | 2026-04-26 03:53:00 | NOAA-20 | VILA VELHA | ESPÍRITO SANTO | Brasil | 3205200 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 96a93325-b9f7-336c-b5e2-82d3c5e8b37a | -21.42168 | -43.87861 | 2026-04-26 03:55:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7a273619-4f75-31eb-8d93-503c5da9618d | -22.77142 | -42.91218 | 2026-04-26 03:55:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| de749a24-8cc3-30d4-94d6-ea4bcc6b039c | -21.49559 | -51.77446 | 2026-04-26 03:55:00 | NOAA-20 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5bd505aa-b45f-37fb-adf2-9cb5a7881367 | -21.50137 | -51.77599 | 2026-04-26 03:55:00 | NOAA-20 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1501dc9b-0454-3cc9-96c2-a3f27b93d99d | -21.49082 | -51.76851 | 2026-04-26 03:55:00 | NOAA-20 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f6321eaf-ac57-3393-89f6-41d6e6936746 | -21.50235 | -51.77172 | 2026-04-26 03:55:00 | NOAA-20 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f38226f8-f1cf-3825-b609-52bde43ddad1 | -22.46685 | -42.35383 | 2026-04-26 03:55:00 | NOAA-20 | SILVA JARDIM | RIO DE JANEIRO | Brasil | 3305604 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 33d1f6da-5a1e-3f26-9e73-b5166cc5734c | -21.42531 | -43.87937 | 2026-04-26 03:55:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 434f7015-3fba-3595-b048-88c25d39d1a0 | -21.49657 | -51.77016 | 2026-04-26 03:55:00 | NOAA-20 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3f590fa0-c435-3df7-b5ef-508ec02ec9df | -21.90391 | -42.3579 | 2026-04-26 03:55:00 | NOAA-20 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d21b4d99-f698-364c-a0cc-e6c7a0f250b2 | -11.08005 | -45.27486 | 2026-04-26 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 309e3dd5-8169-3e48-897e-90d7c05ff73c | -11.077 | -45.26703 | 2026-04-26 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8a7d88f-e2d7-3975-b988-ecd35b111685 | -11.07651 | -45.27061 | 2026-04-26 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45290096-0a78-3d61-90bd-ea4a641a94fd | -11.08054 | -45.27127 | 2026-04-26 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0a006092-3467-3af8-a997-5508b08d67ff | -17.02154 | -49.23605 | 2026-04-26 04:42:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ccce6e37-6ec9-34cd-916f-1117f65e6819 | -13.88457 | -43.78559 | 2026-04-26 04:42:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96e858f2-8321-3c07-a37d-4d782d657381 | -14.7935 | -42.81062 | 2026-04-26 04:42:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 73294324-dcf5-3470-9244-113db848a226 | -14.20403 | -57.43045 | 2026-04-26 04:42:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f994531c-0406-3aa9-8f45-88e58df9322c | -15.23336 | -54.60691 | 2026-04-26 04:42:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4ea7892-509f-3eb3-bcfd-d16f64418224 | -15.55698 | -42.63961 | 2026-04-26 04:42:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 266cc361-9d59-3737-9740-4c35ea91b9be | -14.20479 | -57.42626 | 2026-04-26 04:42:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a02ff037-32ef-3646-8c3f-f6f1d3f7cde3 | -12.01762 | -49.27513 | 2026-04-26 04:42:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc709a22-57c7-390f-bc71-d4b47fed06ed | -11.55825 | -48.26687 | 2026-04-26 04:42:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0ce826dc-6039-3c8b-b3f2-c300ca340e09 | -16.45997 | -53.43464 | 2026-04-26 04:42:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7434d7a9-938e-33b9-af3b-0caf47577c88 | -11.55536 | -48.26248 | 2026-04-26 04:42:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6eef846-d927-34b9-8610-83e0c2ef63d8 | -13.49436 | -46.25529 | 2026-04-26 04:42:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7036cbb-e9a8-3a9d-8ae7-4667eb364411 | -16.86341 | -49.72863 | 2026-04-26 04:42:00 | NOAA-21 | CAMPESTRE DE GOIÁS | GOIÁS | Brasil | 5204607 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5806cba5-a29c-3c64-b12f-cc89332f6fbb | -14.87395 | -46.61354 | 2026-04-26 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9c0b9cd-ec61-374e-97ae-42c984203ef7 | -11.29736 | -54.02177 | 2026-04-26 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4fca3f3-d48e-34a3-8311-4797ed6584a8 | -11.55882 | -48.26301 | 2026-04-26 04:42:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 64e7e298-2c3d-3868-b03a-d0c144a57b61 | -13.49687 | -46.26599 | 2026-04-26 04:42:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README2.md)
