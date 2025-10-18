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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5ae66b6-b8a6-3ffe-b9f8-9a42f62155d8 | -14.90768 | -46.76725 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e04775b-13d0-3dc6-8f91-5958da30d802 | -13.41023 | -48.59281 | 2025-10-18 04:32:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1c7eba4-df12-3140-afc2-97e340e5e4fb | -13.66545 | -43.37447 | 2025-10-18 04:32:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1ebfcfac-47de-3514-85dc-fb4afaaea6ef | -11.36619 | -45.26218 | 2025-10-18 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27467059-cc7a-3c3b-be3a-f4c735e92849 | -13.41318 | -47.97682 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9edd7541-edf2-3a65-9c20-e8b8a245b501 | -12.30449 | -47.26628 | 2025-10-18 04:32:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4115caad-ea4a-3053-968b-59ee5c2e797c | -13.43377 | -47.93291 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e2af4e5-e468-3de9-9762-9a2006ba4787 | -15.78532 | -41.32949 | 2025-10-18 04:32:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 31f63c38-b725-3a4c-88d3-d0665f8684e5 | -13.84261 | -42.38425 | 2025-10-18 04:32:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 49350d17-f9cb-31a1-8ab8-ec68336abcf8 | -13.8653 | -45.46108 | 2025-10-18 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb1adb41-f4e7-33f6-951b-9baac880c4df | -13.04318 | -46.9562 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cad66ec3-14ab-319a-89af-73498680eec8 | -11.95723 | -45.34938 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f94012b3-1bb5-3b10-870c-f502791f3253 | -11.37008 | -44.27 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07a824bd-f789-3f88-9070-7a695c5d7907 | -14.14834 | -44.2439 | 2025-10-18 04:32:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6ac9b92-1c34-32fb-9a09-df709cc87de4 | -12.04553 | -54.24332 | 2025-10-18 04:32:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0b59ade-f078-3d35-a20d-bd7003e50435 | -11.36207 | -45.25866 | 2025-10-18 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 558bd621-dd2a-35cc-8812-753e4dfe7548 | -10.92132 | -47.97207 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b1b3876-2a0e-372a-9d8c-979a7233dc88 | -13.40863 | -48.58145 | 2025-10-18 04:32:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c216896-ad0a-3f7f-bedd-ed2f464e0fb0 | -18.52382 | -43.99656 | 2025-10-18 04:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89be6964-5f66-3666-a277-799ef7a8266a | -14.90882 | -46.7598 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f9b6d73-df37-3ac6-a331-f72920dfaad6 | -11.85523 | -45.44903 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf2ef1bf-ed93-3341-849e-2a2f19183619 | -17.96306 | -46.74507 | 2025-10-18 04:32:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08046ccf-a8dd-3efa-b501-a7601d6f79bb | -13.40529 | -48.58091 | 2025-10-18 04:32:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8eb4f822-e5f4-3f6e-b80f-8e8004d42603 | -10.92597 | -47.55691 | 2025-10-18 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5ee7520-e9b5-3ad1-bbd4-519017ff0e6a | -13.61571 | -43.96338 | 2025-10-18 04:32:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3d9c1cd-f92c-3c76-838b-88bb0fd23637 | -14.91054 | -46.72564 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8577611f-962d-37e9-977f-7d0346a7d0bb | -15.04721 | -46.60502 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e64883d-8542-30fa-aafa-069a4aaafa77 | -12.16807 | -45.09447 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba622efd-e135-3c0a-b7ef-2f7a8ab7378d | -10.92075 | -47.97557 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 280e6b4e-5732-35ce-b781-afe1e88654e9 | -13.45667 | -47.97981 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cf43ebe-683e-3fbd-bba4-c1e271e0fda4 | -17.49318 | -43.46242 | 2025-10-18 04:32:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ee471d60-001f-37f5-8dc4-b7dac9a6e0ed | -11.60653 | -44.07768 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b9f010e8-691c-370b-92c7-133c6e4aa7af | -13.11636 | -48.09879 | 2025-10-18 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c3aebf0-8f81-35d8-9202-d268265fb709 | -11.9433 | -44.24333 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a5ed98d8-59ed-3609-accd-cdfa2868c437 | -13.62773 | -43.96041 | 2025-10-18 04:32:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c51479bd-a665-3d92-aeb1-2671627f37ed | -13.52039 | -48.00853 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eae8773c-3a6e-37c9-a3ec-df9e3cdbb19b | -15.79893 | -43.57122 | 2025-10-18 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1ab611f4-762c-332a-9211-9a918d4e703d | -14.13004 | -44.71338 | 2025-10-18 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3371ae45-fcc5-3be2-86b5-ad7384221d1a | -12.98485 | -48.45971 | 2025-10-18 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a3c0b46-e6ba-3523-a8c0-2a90ca2c5467 | -16.5324 | -43.67654 | 2025-10-18 04:32:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7cd4342-4b3c-358c-9136-1b63716be134 | -14.52036 | -47.78662 | 2025-10-18 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09c62c32-5034-32d1-8c3b-1e6a79cd1b02 | -13.48689 | -48.11225 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e879ed51-e9f7-3adc-b09f-8609606c6bd6 | -12.43172 | -47.7906 | 2025-10-18 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 555f10de-353b-3f2a-81ba-1602e4a67677 | -13.03815 | -46.94435 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8bb61518-31dd-3899-bbde-0a77e38c90f1 | -11.20365 | -47.82972 | 2025-10-18 04:32:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 25939d30-1f70-3147-ba6e-ed84db87a1a8 | -11.34852 | -44.21459 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d026810-0552-3265-a3aa-c9fb6e651193 | -12.87249 | -44.82832 | 2025-10-18 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 14f6b05e-e488-38e2-ada9-4122a026be38 | -11.38949 | -44.26425 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4c1e165-fa6a-349f-8ed6-6b0f223022ba | -10.91629 | -47.98207 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94fd40f7-c1b0-3893-8f11-42a846f35067 | -13.76595 | -48.22432 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2b0f295f-3ba3-38c7-9c40-07b0f8e3c4c2 | -13.44845 | -47.92382 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7bb03a36-15ae-3b6d-b01a-b996a550f18d | -15.78993 | -43.6519 | 2025-10-18 04:32:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3fdb73b-2f1d-30f2-a700-9db274c89eb4 | -18.40306 | -41.839 | 2025-10-18 04:32:00 | NPP-375D | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c88d1396-8b0d-3759-9974-14b2f9919097 | -13.42318 | -48.0835 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b43db808-5b65-3b9b-a221-2b9ad0581181 | -15.0528 | -46.60583 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 431aece3-c821-3c1c-848c-42580faea66d | -16.04398 | -43.50694 | 2025-10-18 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70c18ee2-bfe4-311c-874f-02b6b6130986 | -11.00407 | -47.89455 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 180c3110-9af7-3a78-abd4-5f4f6fa270a8 | -15.18497 | -47.08892 | 2025-10-18 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d631dae-8b9e-3f9a-a01c-028478d6affb | -11.60893 | -44.08695 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5cc34860-4c64-300d-b110-f76a72f3b687 | -12.9429 | -47.95716 | 2025-10-18 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| acfa8988-61b2-33cc-b82b-1063fc185693 | -14.90219 | -52.4007 | 2025-10-18 04:32:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7fc1f01-6a99-3ad7-8fa2-ad3c50fb3405 | -13.86883 | -45.46164 | 2025-10-18 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a68fd9b-0653-3b42-a7fe-e6bebd328c7a | -13.83457 | -42.63391 | 2025-10-18 04:32:00 | NPP-375D | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8c06df29-38c7-3add-ab80-98474d40b722 | -13.44067 | -47.92982 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ebd99c13-aa8e-3f8f-9c46-a8d020510666 | -18.39952 | -41.82904 | 2025-10-18 04:32:00 | NPP-375D | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dc5292b2-0384-3945-afd5-9d90eb13bdad | -15.09121 | -44.00441 | 2025-10-18 04:32:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d9a14c9-8cf2-3dbb-bd0c-845d9f3e3ac2 | -13.43172 | -47.98659 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0db988dd-ad2d-3469-aeb6-b933155f076c | -15.50854 | -50.38312 | 2025-10-18 04:32:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 411bb64b-33d3-3e28-b918-0ad49bfe188d | -16.64641 | -52.52697 | 2025-10-18 04:32:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7f50f91-67d2-31a7-81a2-544eb560b31d | -13.11693 | -48.09524 | 2025-10-18 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba128413-03e3-37a2-b1ca-705cfa4608a5 | -13.62838 | -43.95576 | 2025-10-18 04:32:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c08487b-eb48-3f30-9a78-8898690917e8 | -10.75523 | -47.88327 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7392126c-0b7f-3196-a01b-97b14010eecb | -11.50969 | -44.05645 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf1c8bb4-a17d-3811-b8a1-49c1b0beeffb | -13.27249 | -48.55933 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6e192db-9928-37c1-85a8-88caf91358d1 | -11.36966 | -45.26278 | 2025-10-18 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 050f0f8f-6eb7-3ab6-ad97-8bdb9dfe46f7 | -11.35982 | -45.25722 | 2025-10-18 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5bc7fc6-7aff-30d3-8143-b90fd3bb2754 | -12.66192 | -54.77337 | 2025-10-18 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c33885e-d73c-31d6-b7ed-de924edf122f | -12.98819 | -48.46027 | 2025-10-18 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4d4f784-989e-379d-94ce-c5635863c421 | -11.61692 | -44.08369 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b2656534-d65b-3b2d-a4c2-2c9c5735e613 | -15.03866 | -46.61526 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e5442ea-588b-3246-a27d-628686e846e7 | -18.39843 | -41.83837 | 2025-10-18 04:32:00 | NPP-375D | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3869d3cb-8d88-37fd-90b4-ab249a24c50b | -13.41871 | -47.98502 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2dd967c5-d382-32b6-98ac-04d51c025bb9 | -16.08121 | -42.55692 | 2025-10-18 04:32:00 | NPP-375D | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83dbb7d1-5521-3228-acea-f497cc336ae2 | -12.60638 | -52.80978 | 2025-10-18 04:32:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56ade7f9-54ef-3f10-b2df-826ad2d2d778 | -15.7939 | -43.65248 | 2025-10-18 04:32:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67507fb0-4542-3eb9-821f-fffa8df9c8e9 | -15.1844 | -47.0926 | 2025-10-18 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f59ea3f-68c8-3325-b817-3058ff41feb7 | -15.45244 | -45.93683 | 2025-10-18 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c88a1a6d-3ccb-3f0a-b8c1-94d82e2d085d | -12.94351 | -49.0002 | 2025-10-18 04:32:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 943916f6-1231-3d95-b7af-ec5e179431f8 | -12.30505 | -47.26273 | 2025-10-18 04:32:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4439b20-60e1-3552-9edc-67f4763e1975 | -12.99152 | -48.46082 | 2025-10-18 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2423a990-5f9d-318f-97ee-ecc455c67190 | -15.60182 | -42.6577 | 2025-10-18 04:32:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7fdf5c3e-70a8-30cb-aaa6-eacfb9ff4e7c | -11.59069 | -44.05749 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6e6b927c-da35-3578-9eaa-874249fd4d15 | -13.76815 | -48.23195 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 873be156-1240-3403-8473-44eeb6de5bd0 | -12.16454 | -45.09395 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2abf65d1-41cc-37ab-8c73-019836b1c9e9 | -11.63926 | -47.85665 | 2025-10-18 04:32:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf63226a-b562-3a5b-ac64-537fae5a8839 | -12.4949 | -45.50382 | 2025-10-18 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41d831b2-19cf-3070-a26c-4df0492cbadd | -11.59982 | -44.07223 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13ddc9bc-3711-34f4-8b46-cc3781548e26 | -14.4892 | -44.61016 | 2025-10-18 04:32:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 677f575f-d1a7-3632-8364-fccc812aef7b | -11.94331 | -44.23682 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 051b344d-2f76-3a59-bb0b-f66f9890606b | -13.46016 | -43.76067 | 2025-10-18 04:32:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README65.md)
