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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75a736a2-046b-3a4f-9512-20cc3df92900 | -13.41949 | -57.03094 | 2026-08-07 04:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8dd81ca5-6de2-3511-8946-be3475199213 | -13.42225 | -57.04179 | 2026-08-07 04:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f5600fc8-7ae8-3b4b-be7b-158bd68ab188 | -11.14567 | -44.47935 | 2026-08-07 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 0d892b4a-2d3c-34f7-a315-e9cd730aebcc | -11.45653 | -44.56063 | 2026-08-07 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 823ec028-a5c8-342c-b87d-c18ae0f90cdb | -9.08572 | -59.48512 | 2026-08-07 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fd4445d-2db5-3e2c-84b1-9168b6c6b8e5 | -14.41527 | -53.05762 | 2026-08-07 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d024c01-5ef5-3dd2-aeb6-b48123cc9688 | -16.89134 | -51.07362 | 2026-08-07 04:46:00 | NPP-375D | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1d0dc40-4953-3a6c-ab4a-425a030ff564 | -12.5512 | -46.95746 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 620c450e-2ccf-3fd7-b594-a4e2dafbee4c | -15.0756 | -53.58791 | 2026-08-07 04:46:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 43.0 |
| feb6b6d0-b0ce-3ff5-8ad0-8121a0169d98 | -11.41168 | -41.79784 | 2026-08-07 04:46:00 | NPP-375D | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8ccf16dc-373a-310f-a806-0de61efe64d3 | -16.52938 | -49.42288 | 2026-08-07 04:46:00 | NPP-375D | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62ce0abe-4460-3d9e-bd7f-63dcf7a9199d | -12.62972 | -46.88864 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1d9a576-f66d-3bb3-a668-a6175353fe0e | -11.15137 | -54.90759 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3d11ef8-316c-3cfb-90f2-bf2d51759938 | -11.13381 | -54.90827 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b77f69b-7536-3e42-a797-cb469867c70b | -11.99964 | -45.13537 | 2026-08-07 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f69b799-1eaf-3685-9abf-c43870011e6a | -15.09026 | -52.76835 | 2026-08-07 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 522ee4b4-eb8d-3a23-bb24-02311bfaa328 | -11.45973 | -44.56625 | 2026-08-07 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 40052d7a-7d04-394a-969c-92ca7440c20c | -11.15984 | -54.86014 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43e6e22e-38ef-3e08-ba5c-636ec31f3251 | -14.2733 | -45.29397 | 2026-08-07 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d9f48d18-fd58-3763-89d7-9a6cccf3dc0b | -15.86992 | -43.59803 | 2026-08-07 04:46:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ecb5ad52-ef01-3c85-9aa2-4fdf3a69fffa | -12.49539 | -50.36952 | 2026-08-07 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff12cc15-2515-3e7b-82c3-3f7cf670908f | -15.10863 | -53.59411 | 2026-08-07 04:46:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b11fff1e-4748-3b86-83ed-8098be19db19 | -11.47077 | -44.57303 | 2026-08-07 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de7ffc2e-7879-3bb7-884d-54263caab944 | -14.35123 | -54.91528 | 2026-08-07 04:46:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 174e36e3-d314-3805-b93e-76d65f5bcfe8 | -17.52974 | -45.35672 | 2026-08-07 04:46:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab44deff-32ac-3a1b-86c4-07b18c61e182 | -11.17668 | -54.86308 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cd7ce52-3914-32dd-81d4-f65ea6d6368f | -13.82392 | -53.71946 | 2026-08-07 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7598091c-5ee3-3cec-b37f-ff669f5c6e2d | -13.42976 | -57.02792 | 2026-08-07 04:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c367fbde-3d4b-3d33-a971-583687de925c | -12.59167 | -46.90253 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15eec57d-2e2d-3360-8433-02b94c2f537c | -15.07483 | -53.59235 | 2026-08-07 04:46:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 90130634-dadd-30fc-ba90-24ba3435318e | -9.09245 | -59.48201 | 2026-08-07 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b04351ab-6483-3c07-8823-b74b710b4aa9 | -12.49204 | -50.36895 | 2026-08-07 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 112038d6-3444-3a73-b80d-fb9bccf959f9 | -14.33606 | -54.93076 | 2026-08-07 04:46:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63b98a9e-34a1-3e4c-8a18-cdc8acfbba7b | -18.14796 | -47.98514 | 2026-08-07 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8c5b22d-d7f0-36a5-bc6a-cdf3ea3504ac | -12.14078 | -48.26613 | 2026-08-07 04:46:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb08c039-99f1-3779-a9c2-bb3eb44d705c | -17.1307 | -47.56292 | 2026-08-07 04:46:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9304f80a-8035-3207-b222-78f791ee7a72 | -12.62504 | -46.89583 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e14fb9ea-d36d-3b66-87ac-4427f0049b7e | -11.12681 | -54.89874 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 035d1946-6140-3757-8a4d-7c9980399260 | -11.3196 | -45.20741 | 2026-08-07 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0472fa7e-f0cf-3609-80d3-07f707650a4a | -12.56053 | -46.94291 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e5f24a93-970f-308f-9f35-67621d54405c | -10.63516 | -47.48624 | 2026-08-07 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2d3b29a-2159-360b-9968-1d037c66df95 | -13.54202 | -43.69793 | 2026-08-07 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efee597d-1ef9-3acc-8fef-81c5ceb61bba | -11.08209 | -47.79794 | 2026-08-07 04:46:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f51e9cf2-67b4-3342-a6f8-34574f2dc6e8 | -16.68455 | -51.3712 | 2026-08-07 04:46:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3c18ffb-9cfa-3265-94f8-1debcc5c0212 | -14.26869 | -45.29842 | 2026-08-07 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a065ef49-b23b-3ad0-b191-d3785573ac11 | -13.93404 | -47.3633 | 2026-08-07 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fd85c41-762e-3a06-b778-ace1d1338bb8 | -14.41973 | -45.66585 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7dc41f6a-0360-3268-9836-ee05ae8b2864 | -15.92654 | -43.98593 | 2026-08-07 04:46:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15375520-4c0d-3a04-a9a5-3877130d49a9 | -16.18063 | -50.35717 | 2026-08-07 04:46:00 | NPP-375D | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd9c7974-479a-34d8-8d13-d480e61f43f3 | -12.00415 | -45.13116 | 2026-08-07 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fae67ab-aa39-30f2-96ef-309c9e3d8819 | -11.15278 | -44.48562 | 2026-08-07 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f14f1285-6ce1-3795-a444-c579f31a3027 | -11.62995 | -59.0154 | 2026-08-07 04:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b82272a-9728-3de3-8562-9f88cd909d70 | -11.1261 | -54.90269 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbe42969-96f9-3a80-b88d-dacfb06c021f | -11.17944 | -54.84752 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff2abca1-286a-317a-860b-cf7f7b8d42c3 | -13.00617 | -42.66914 | 2026-08-07 04:46:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6bd4b7ce-5d8c-3c27-b10d-999b459eb3cb | -12.60558 | -46.95358 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ec14b17a-e29b-32b2-823e-c2fc5a57ee98 | -12.57822 | -46.8963 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 624a61f9-dfef-3b6c-b9e5-534c2c5c1256 | -13.8285 | -53.71551 | 2026-08-07 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e162506-6380-3427-96d2-bf6401246c7c | -11.43623 | -42.50051 | 2026-08-07 04:46:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a67cd2c8-40fc-3bba-97d6-bd9c328cbf79 | -15.10496 | -53.59344 | 2026-08-07 04:46:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3917fdcc-e176-307c-a612-bffd5bfe9842 | -11.13386 | -54.88381 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5cb1a95-08cb-3cc9-8cd4-5830bd3bf8c7 | -13.93694 | -47.36776 | 2026-08-07 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34ac9633-3333-37e9-a414-9327896391ec | -13.68852 | -51.97403 | 2026-08-07 04:46:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d8cce9f-5aa9-3deb-8e49-c75932ba25c4 | -13.83226 | -53.71621 | 2026-08-07 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e427655b-6611-33ed-a314-787d0c196daf | -13.9613 | -47.37189 | 2026-08-07 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59182df7-9099-39e5-9ff7-7f2080fbff51 | -11.18714 | -54.85302 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dabf273c-5358-369a-bd25-ab538f568c1e | -14.26888 | -45.29562 | 2026-08-07 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f5b0d786-f54b-3b27-a57b-9beb63e2c39a | -12.86269 | -52.82079 | 2026-08-07 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 432829df-1a5b-3099-a3fd-8f3e7b9619f1 | -11.18364 | -54.84832 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6944ed7f-00fd-3d5e-b76b-98c8b1881fac | -11.13802 | -54.9091 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79f29e95-ed8f-3903-97fa-2a00dc85bff9 | -15.89971 | -48.01037 | 2026-08-07 04:46:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2aa698db-00f9-3070-8c10-a4583ae456e5 | -12.00981 | -49.27848 | 2026-08-07 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f6f6d4f-44d2-3c1a-ae76-2b6f6d9f9501 | -14.34251 | -53.34793 | 2026-08-07 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79fad18d-33c0-34e9-9ff7-221412da7005 | -11.13236 | -54.91631 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5bf6bc6-26a9-322b-949d-81498b328e88 | -9.08921 | -59.48424 | 2026-08-07 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6cb9cb4d-5455-3ff0-b24d-b9ca84b5a4ed | -17.4347 | -43.65016 | 2026-08-07 04:46:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11723d27-ef96-3229-bb7a-4903eab5e26c | -12.55234 | -46.94977 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2f85dbb-83a7-369f-9b26-f1c31c55f387 | -14.2682 | -45.30064 | 2026-08-07 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f2f39fb-e0e2-3248-ac46-e63e3adbeadc | -12.57397 | -46.97309 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8d45f2d-8b2a-3950-9503-af5cac436f57 | -11.13453 | -54.90428 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8017e7e-6196-317d-b848-696e07111ba8 | -15.58852 | -43.73611 | 2026-08-07 04:46:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cbee65fe-6eae-3a56-a5d1-d266269de6b6 | -15.0785 | -53.59304 | 2026-08-07 04:46:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 30.5 |
| e4b0472d-ba30-3866-9dda-5eb2311b97c2 | -12.87068 | -52.81781 | 2026-08-07 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b71bce2-f165-3816-8165-c050c0eb51d0 | -11.45971 | -44.56358 | 2026-08-07 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5ecf3f02-c97a-3cac-90b2-edc6420d463e | -13.93867 | -47.35616 | 2026-08-07 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb55a1d5-0ead-3ec6-b4e6-90ddfcf99409 | -14.34785 | -54.91096 | 2026-08-07 04:46:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d999892c-f369-3ab1-a923-f425b253015f | -17.45963 | -47.15416 | 2026-08-07 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77d7deb8-1dc3-37f3-bab7-118a650d41eb | -13.00574 | -42.66725 | 2026-08-07 04:46:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 505d0cf3-0b51-32a9-b840-74463603814f | -13.93462 | -47.35944 | 2026-08-07 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2976b410-ae4d-3aa8-b23d-2b1b6cff9624 | -17.85497 | -49.611 | 2026-08-07 04:46:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d5c5907-ed9f-3045-9bb5-ed93c72a0c55 | -14.26499 | -45.29504 | 2026-08-07 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 190c7036-3ce1-3faa-af5a-374c1c10e65c | -12.14983 | -48.45146 | 2026-08-07 04:46:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 634af7d3-f0d6-30a3-956c-85e5c1ca53af | -16.52994 | -49.41923 | 2026-08-07 04:46:00 | NPP-375D | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 374971fe-0477-3ab6-883e-6bfd19d4f6ae | -12.56176 | -46.93464 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fd22288b-6a46-380c-9ac7-ccd509f58ba9 | -9.09164 | -59.48625 | 2026-08-07 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 785bff1e-cac1-350f-92cd-3a5894c2fce4 | -11.15614 | -44.48264 | 2026-08-07 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3cf981e1-774f-3715-acf9-02204056d3cc | -13.83683 | -53.71227 | 2026-08-07 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e98f771b-9fd7-3d97-9f3c-cf6ec74c3885 | -11.18295 | -54.8522 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08d8020f-f59d-31c4-afb5-4f22c9942775 | -15.08294 | -53.58929 | 2026-08-07 04:46:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 1a35c145-7cf1-3882-8ef8-3692a5dbe9ec | -14.98948 | -47.8694 | 2026-08-07 04:46:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README17.md)
