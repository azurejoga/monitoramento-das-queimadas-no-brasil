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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a258e349-8c56-3cb2-913f-bf1ecc343392 | -10.66085 | -46.60325 | 2026-07-23 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6dfc5045-9a40-3dc4-8129-ff1cf10b9845 | -7.88783 | -46.9048 | 2026-07-23 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 854ca3a8-ceeb-3a49-8157-69a4128c3550 | -9.46293 | -45.64494 | 2026-07-23 04:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25c1ffd0-04b5-399a-9a50-90d066f33093 | -11.95003 | -50.37408 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 71d54dfa-b974-3ed3-80e8-f7b338dc89a4 | -11.96406 | -50.36853 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f8cc7145-e74b-3dfe-a9ce-6608e6202521 | -11.68733 | -50.36353 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3961c9de-fa89-34ed-bff7-e70077a3af45 | -11.99699 | -50.32903 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff402536-d73e-384f-b214-5abf3abb879c | -9.10663 | -49.65585 | 2026-07-23 04:25:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e4ffdcc-b48b-3478-9dbf-75356b9acc9c | -10.65942 | -46.60392 | 2026-07-23 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| effac0de-8799-36fb-b522-4ee62b578ee8 | -11.4012 | -47.48232 | 2026-07-23 04:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa74bca4-8bf5-3c7b-8619-2f2c1b64a2ab | -12.32163 | -46.73767 | 2026-07-23 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95016753-f4e8-3043-86e7-b0c780a5a2cb | -11.91013 | -43.84506 | 2026-07-23 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7849d8ff-c15c-3728-ac10-022b3d2ca9f9 | -11.67607 | -50.35319 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dacb47bf-c014-30f9-bf8c-a6591d551b40 | -10.15433 | -48.31366 | 2026-07-23 04:25:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e32a9edb-0018-3004-9eb2-c35df5de9559 | -11.59633 | -48.02953 | 2026-07-23 04:25:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 137efe4f-8d31-333d-95b6-4059717195d6 | -12.24981 | -43.5722 | 2026-07-23 04:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 655d99f6-0875-3c06-a719-9cb7ed45306d | -11.67041 | -50.36036 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee6e6521-0629-3a9d-afb9-8dd0a385424a | -11.57971 | -48.40027 | 2026-07-23 04:25:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b87ef4fe-7c18-34c2-a84f-7ae14811c46b | -13.7804 | -43.18344 | 2026-07-23 04:25:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8a5d6bfc-491a-31d5-aa68-f92b20820000 | -11.67248 | -50.37313 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3a914174-8dbe-3b7e-80d7-06a1317f5fed | -11.66545 | -50.36357 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6db75614-6b46-35df-b9cd-8c649dd1d633 | -11.67464 | -50.36116 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 977c7328-3f11-36d0-9b69-ced08dbcacbb | -11.77666 | -47.10095 | 2026-07-23 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9deaa631-28e0-3aff-8f2b-268ba01c87b3 | -12.39801 | -50.38874 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9fe6526d-e5d0-3972-a917-b025f6051613 | -7.73217 | -47.24855 | 2026-07-23 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6259cdb4-45a5-3225-a051-f13cde7a2982 | -12.66382 | -48.21481 | 2026-07-23 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fb3e124-5138-3309-bd72-4b9534cfc9af | -11.57596 | -48.3996 | 2026-07-23 04:25:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 209881a0-fad6-3aed-8a77-de7e803d1c2f | -13.4381 | -43.84857 | 2026-07-23 04:25:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df1fdba8-1d98-3335-a88c-139b3db93752 | -11.3912 | -47.47599 | 2026-07-23 04:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 26ea9493-bbd6-3c0f-a62a-d0a02869924b | -8.83667 | -48.33802 | 2026-07-23 04:25:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c90ffcef-3359-3ea7-9417-a5d1568729bb | -11.96038 | -50.3629 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6fa8b2a4-12da-388b-af7e-68dfbaf21c01 | -11.56765 | -48.40287 | 2026-07-23 04:25:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b5695c8-3cb8-3cfb-a02e-b86b974a333f | -11.67392 | -50.36515 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e78c241e-ff47-3040-aac8-d6713cab044e | -11.58051 | -48.39567 | 2026-07-23 04:25:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 218e72b5-632d-3f1b-ae4d-78ff860da1e4 | -11.88899 | -43.82708 | 2026-07-23 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4777db10-e23d-3aa8-bcdb-4142b0dbe6c8 | -11.96476 | -50.36457 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1bc317e6-074b-384d-826d-54e4a8e9ba05 | -11.67536 | -50.35717 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e58364e1-7378-3427-8eaa-6214ca1700c7 | -10.66006 | -46.60001 | 2026-07-23 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05392287-c709-34c2-8112-669609c92d55 | -11.8051 | -50.38528 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9152f183-d3ee-30fb-a95d-3c51f2e51ab2 | -11.5714 | -48.40354 | 2026-07-23 04:25:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bd60d013-86f7-3876-aecb-f10bfb806bde | -13.36946 | -54.30663 | 2026-07-23 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4ef155e-2243-3a5d-a8e0-c5a907d1053d | -11.79354 | -47.108 | 2026-07-23 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1d1cb1f5-c6d0-3c84-97b7-f1f160a30e9d | -11.79422 | -47.104 | 2026-07-23 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| de8c935f-21cb-343c-911d-3ab5b7a52cf4 | -11.69085 | -50.36831 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4193044d-9b21-3eef-a8fc-be2cafc08f95 | -11.66762 | -50.35161 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| f6a6e054-d64d-39e8-82d8-344857e87b26 | -11.77828 | -50.38852 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0367c12d-b9ad-3d33-9df7-c217a5a820fc | -12.76268 | -47.12978 | 2026-07-23 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64bc025b-7999-33f5-98a4-eeaa0250b080 | -11.68102 | -50.34999 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49820f76-5bb7-35fa-a23e-0f76a2d91fcd | -11.67185 | -50.3524 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7628c1a8-5002-3fd3-ba5f-5bf839d2e607 | -11.95187 | -40.60237 | 2026-07-23 04:25:00 | NPP-375D | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7001dcc0-5995-39fa-8e57-00487202b8c0 | -11.96808 | -50.36842 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a0e42779-6f5b-3c98-bd32-4b735f90ee02 | -11.79489 | -47.10002 | 2026-07-23 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a252eb79-fda0-3c58-ad56-264cb8e1d680 | -7.73305 | -44.55919 | 2026-07-23 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4fba1f56-c293-33a0-826c-510884691199 | -8.83749 | -48.3331 | 2026-07-23 04:25:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b183d71-a896-38ee-8394-1735ad42dcda | -12.14268 | -48.26087 | 2026-07-23 04:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76aa7212-c7c4-3e94-b31c-eb3c26ef4c4b | -9.558 | -40.33625 | 2026-07-23 04:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 513e5966-75f5-351c-889b-d217ba85b2dd | -11.66969 | -50.36436 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2ea3046-dcf8-3cfc-ab13-a28fbdcb6f34 | -10.15174 | -48.31492 | 2026-07-23 04:25:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de9ae26a-988b-3f03-b5df-43bcb0bf5f95 | -11.93316 | -50.37092 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a60ab006-2aa8-38fe-bcd7-1cdadbc89fe8 | -11.97229 | -50.3692 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3e9b02f7-af68-3cd5-b8e0-48881cb0188d | -11.78368 | -47.10217 | 2026-07-23 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb3a2c49-2f79-3956-ac1f-b26725e7e721 | -10.66151 | -46.59935 | 2026-07-23 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28c4fa40-623a-3492-8ae2-e14f1dca1e59 | -13.32479 | -54.30831 | 2026-07-23 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d58ae704-81e7-3fd9-b139-c0bef238db1b | -13.9931 | -49.5918 | 2026-07-23 04:25:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92c58305-6127-3ce3-a920-c459422ed96a | -11.69579 | -50.36511 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3277d0f3-5d03-390f-949d-a947bca6b5eb | -11.96055 | -50.36378 | 2026-07-23 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b754503b-bc65-3b25-85c3-f7e1b757e9f4 | -20.23549 | -42.82592 | 2026-07-23 04:27:00 | NPP-375D | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| c70512c1-4ef9-367d-ae97-83736665c5e4 | -19.86088 | -48.19984 | 2026-07-23 04:27:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77918217-155c-30f6-945a-f59843745ef5 | -17.7345 | -52.74731 | 2026-07-23 04:27:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a54f9c2-2ca5-375a-9027-02359f92ed0d | -21.07093 | -45.94216 | 2026-07-23 04:27:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bf17241e-50bb-327f-a5d6-4e9761625c77 | -21.21326 | -48.99141 | 2026-07-23 04:27:00 | NPP-375D | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d0a64b62-85df-36f1-b2dd-ca5d59ec7b04 | -21.36791 | -43.76392 | 2026-07-23 04:27:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 426e2dc3-8bf4-326c-846a-f501d3f9c662 | -20.58136 | -46.91526 | 2026-07-23 04:27:00 | NPP-375D | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b13051bb-206b-38a9-8cc9-db1a76d4a70c | -19.7094 | -48.08089 | 2026-07-23 04:27:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5576f2ea-c14d-3fd9-a3c1-3e2eacc700ed | -14.38271 | -58.34178 | 2026-07-23 04:27:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c9c01da-a2cf-31a8-9e73-c9864184135e | -19.82031 | -43.83142 | 2026-07-23 04:27:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| afc17e66-532f-3ec1-9124-9187d43f0dad | -17.58285 | -47.51301 | 2026-07-23 04:27:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36486ace-d12a-3d02-83ed-cddabbaa2eb3 | -18.80403 | -42.90367 | 2026-07-23 04:27:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2f26b984-ddc7-3ed2-b949-a215d4ca321c | -20.42943 | -46.48702 | 2026-07-23 04:27:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b77f75e-671d-3be6-b4c1-cada48b9aa33 | -19.16715 | -46.59163 | 2026-07-23 04:27:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 505b0865-ff99-3d08-a69a-fdfd069d42ac | -12.88371 | -58.29015 | 2026-07-23 04:27:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b7c9cb47-34f6-3d1d-8d63-1d30ce522094 | -20.80638 | -40.67335 | 2026-07-23 04:27:00 | NPP-375D | ANCHIETA | ESPÍRITO SANTO | Brasil | 3200409 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4622cb05-10a7-3713-9793-a97832fe9995 | -21.58102 | -44.76231 | 2026-07-23 04:27:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cd4eed9f-7547-3bff-acb7-03e786813e8b | -12.88377 | -58.29132 | 2026-07-23 04:27:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c3dcf23-8e42-36b5-a58d-38f935e1b16d | -16.85529 | -49.55879 | 2026-07-23 04:27:00 | NPP-375D | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae2fde55-7b20-36bf-9489-232c1fb6b3d8 | -20.58329 | -46.91878 | 2026-07-23 04:27:00 | NPP-375D | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f413e824-e3e9-3b91-bbd4-2d9ff954ee00 | -16.74327 | -47.6374 | 2026-07-23 04:27:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 387d572b-9e2e-3d0d-9f70-e9bcd7d62949 | -20.44768 | -46.47468 | 2026-07-23 04:27:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7c6ca5c-18de-3737-a316-1a24537df27b | -17.56717 | -47.50234 | 2026-07-23 04:27:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 722798f7-9f94-33ef-96e7-42e0c9fda1d0 | -20.44827 | -46.47101 | 2026-07-23 04:27:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7c6e6b7d-31b6-3863-9671-765343810cd0 | -16.08845 | -45.13751 | 2026-07-23 04:27:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 726dc59f-eb1b-306e-a4ae-fac625576d64 | -20.09509 | -44.26383 | 2026-07-23 04:27:00 | NPP-375D | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cbc9c394-2a04-325e-ad6b-19415e488e42 | -21.0715 | -45.93842 | 2026-07-23 04:27:00 | NPP-375D | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2366286a-4cd2-38ff-9c47-48b55df82daf | -16.85447 | -49.56343 | 2026-07-23 04:27:00 | NPP-375D | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04b5021d-bc37-3e79-8873-67ae7c1642f1 | -20.15924 | -43.92157 | 2026-07-23 04:27:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9e449a6f-1dcb-3d6b-a9c7-b1b59292ae24 | -14.31297 | -52.09313 | 2026-07-23 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94834af0-08f2-39e2-a429-be206b8760f8 | -19.86153 | -48.196 | 2026-07-23 04:27:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 949eb712-7da1-3ab3-ae69-a75f20136cab | -21.89518 | -41.17669 | 2026-07-23 04:27:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 338ad0fd-cfe6-3b0b-9036-78404019d202 | -19.55635 | -46.95025 | 2026-07-23 04:27:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3323a2c2-7361-3e50-98d8-b9227b0b2f14 | -20.16626 | -43.92266 | 2026-07-23 04:27:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |


[Clique aqui para ver as próximas entradas](README13.md)
