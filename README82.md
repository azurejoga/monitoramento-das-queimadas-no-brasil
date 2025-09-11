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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90ed14af-36d9-369a-bc92-2af9a0507075 | -17.37966 | -52.93266 | 2025-09-11 04:25:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 332299f1-e9fe-30d0-a745-5cd98b78360a | -15.54881 | -54.74901 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6e942f4-ce75-3d3b-9b7d-a019cfadaadb | -21.00101 | -47.71653 | 2025-09-11 04:25:00 | NPP-375D | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aecda47e-08f0-3532-a54a-19d12a56c61a | -20.16163 | -41.03914 | 2025-09-11 04:25:00 | NPP-375D | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 04653438-29bf-3fe0-87b2-395ee210258b | -15.11895 | -52.39721 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54f83ceb-9456-3d9a-a08a-15d72fa395b5 | -15.1591 | -52.41386 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f19f00ea-f879-3de4-a81d-ac0e38b120cc | -20.15531 | -43.667 | 2025-09-11 04:25:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cc9b8a81-23de-30ec-9f1e-94c7f3102196 | -17.4669 | -45.10007 | 2025-09-11 04:25:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 860ca06a-f7a2-375f-98e5-b330bd9d142f | -14.50172 | -53.93965 | 2025-09-11 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8adfffd9-8c4a-33e3-a920-20c85adaff4b | -15.11667 | -50.08334 | 2025-09-11 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 26a2a2aa-4cf2-3d74-a7e2-e38bf0158d82 | -16.42901 | -45.68513 | 2025-09-11 04:25:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb2a3e50-3b36-398a-bd7f-9075180f9c88 | -17.33396 | -46.69598 | 2025-09-11 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f596d402-094e-3c47-ba9e-1c9dbe4e05fb | -16.29624 | -50.05153 | 2025-09-11 04:25:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f4f355d5-b297-3f43-a342-8cf748ece417 | -19.99667 | -47.60903 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09bcc891-7dfc-34f1-a67c-f3cf91f6ddb3 | -20.0789 | -46.66225 | 2025-09-11 04:25:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f71358e-2cca-34f7-a871-d8bb01c33a7f | -15.79499 | -52.26471 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5861836-5e96-3378-9ae0-687e7ef059d4 | -14.90776 | -55.87747 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 270c93ab-7611-3fbf-aba9-cb6538874e09 | -15.80338 | -52.24249 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 53c9ae19-ba2c-3b40-a1f7-ad638cf7e356 | -17.26702 | -46.08466 | 2025-09-11 04:25:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d86788b9-2126-3643-ba79-554f283a15ab | -19.80312 | -47.16367 | 2025-09-11 04:25:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df28a590-597f-3e75-981f-acc0f4b510bc | -15.11844 | -52.3997 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5afcdbbd-835c-3056-973b-0832d6e8cb94 | -19.33768 | -41.31231 | 2025-09-11 04:25:00 | NPP-375D | RESPLENDOR | MINAS GERAIS | Brasil | 3154309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 41743a25-63bc-394a-9e13-2c3d36e40878 | -18.50259 | -47.3059 | 2025-09-11 04:25:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b4bb985-e672-3f73-8749-0146a43ec170 | -15.14315 | -52.45321 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34ea0832-c6c5-32f5-9760-ddfd3a044995 | -20.91565 | -49.46585 | 2025-09-11 04:25:00 | NPP-375D | BADY BASSITT | SÃO PAULO | Brasil | 3504602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 3c0edf38-6be5-33af-9cab-7525b3b87d2d | -17.199 | -50.1551 | 2025-09-11 04:25:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca5e9850-18c6-313a-9527-69e1500e84c0 | -22.83839 | -47.47264 | 2025-09-11 04:25:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| eb63e230-80cd-3148-8ccf-37cbe3a21210 | -18.00965 | -44.45483 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b900776-c611-3aea-a192-443adf472356 | -18.01107 | -47.14104 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3e09f60-61a3-3ef2-9e09-12a8088dd5c8 | -15.13151 | -52.42249 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 929ee2bc-6ab0-343d-bf23-e4f11329cebf | -20.12981 | -47.6884 | 2025-09-11 04:25:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdb1d927-384a-3917-978f-5a1faad841f6 | -20.07267 | -47.53905 | 2025-09-11 04:25:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d58a219f-1e25-32a5-afc9-fa2fea7cc156 | -15.55951 | -54.7455 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b10ee12-5042-3528-9ab3-040532b88ef5 | -16.17496 | -48.68888 | 2025-09-11 04:25:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2aa9c428-715e-3574-9c28-e6f4031cf185 | -16.06693 | -49.97283 | 2025-09-11 04:25:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e61578b7-0084-3fdc-b509-3a83bb9eec3f | -19.35628 | -41.3049 | 2025-09-11 04:25:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 79bb0cca-6d35-3933-9003-a6a0a1f60f8c | -18.01022 | -48.00077 | 2025-09-11 04:25:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 434ea28a-118e-3802-a920-fdc8ea98a515 | -19.10612 | -43.22089 | 2025-09-11 04:25:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 42b34ca7-5aa7-3939-b380-47997e2abf2b | -17.07303 | -43.1918 | 2025-09-11 04:25:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cde66867-81ba-30d7-aa90-415c96d1a999 | -17.07228 | -49.6727 | 2025-09-11 04:25:00 | NPP-375D | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84a62795-c325-3b0f-96e2-4bb424392e3c | -18.82357 | -46.87512 | 2025-09-11 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5339e931-3ac7-36f3-9ede-ed40ceb307e9 | -14.91331 | -55.93153 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2a0a7ea-8072-315a-a130-997aafbbe598 | -20.07382 | -47.53168 | 2025-09-11 04:25:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f67ab359-5dbf-39cf-9796-560e9cac8a0f | -18.50203 | -47.41806 | 2025-09-11 04:25:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10696bbf-b8f8-3392-a8eb-b28ec7e2292c | -15.55367 | -54.74978 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 955f9075-66ef-3dee-bffc-fd5a6984190b | -15.12375 | -52.4186 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69b9c834-4ae1-3906-81ba-76aab19f4a49 | -16.60541 | -49.78107 | 2025-09-11 04:25:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac1ebe12-310b-3af0-8872-ff08257c57c7 | -15.55057 | -54.76605 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2dbaa227-d118-3f5b-94ac-6d97c4bd7b22 | -20.16121 | -41.04273 | 2025-09-11 04:25:00 | NPP-375D | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 543cf9db-4b54-3b00-bf01-05ca86ecc8bc | -20.54185 | -47.62244 | 2025-09-11 04:25:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74f8035d-be09-3312-86fb-3eb86652d7b5 | -15.15144 | -52.40847 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a739484f-9b66-3de4-9bf8-f87b0aad2935 | -19.46917 | -46.13197 | 2025-09-11 04:25:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b925401-d5ea-3081-9143-b3e335957815 | -17.73614 | -44.45343 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33cee496-df44-3b3a-8aa6-b47b215da49e | -19.24184 | -48.00322 | 2025-09-11 04:25:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7a5da5c0-b630-3184-bade-afcc44b2c933 | -17.27039 | -46.0852 | 2025-09-11 04:25:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f21c11c2-5f65-339b-9ffd-3687a1e6eecb | -15.13775 | -48.61399 | 2025-09-11 04:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be0b822c-422c-342d-b83b-c217063874ce | -20.53461 | -47.62496 | 2025-09-11 04:25:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5fbf2947-e77b-373e-9775-799fa399c5a7 | -16.57003 | -49.73241 | 2025-09-11 04:25:00 | NPP-375D | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cec78f9-147c-3a57-8c88-455c60193b66 | -17.46978 | -45.10455 | 2025-09-11 04:25:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e5abb98-8abd-3c1f-9b31-d5a1b8e77102 | -17.31042 | -49.31605 | 2025-09-11 04:25:00 | NPP-375D | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38791bfd-60d5-3788-b2ec-27ff591b8004 | -22.56222 | -46.043 | 2025-09-11 04:25:00 | NPP-375D | CAMBUÍ | MINAS GERAIS | Brasil | 3110608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 43bc7cb4-4ddc-3588-9da0-143da054ab86 | -15.13278 | -52.43891 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b9aa4258-aa73-36e9-8aec-25dc8ea9dee6 | -18.89288 | -43.78303 | 2025-09-11 04:25:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ca7c40c-2a7c-32ee-b4d4-174242a869b4 | -15.68079 | -49.43722 | 2025-09-11 04:25:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ff45d02-dc8f-3518-9936-40d67f567530 | -19.79253 | -47.16561 | 2025-09-11 04:25:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb04de47-1f3e-3249-8dfa-b5151560bca5 | -22.14424 | -48.63564 | 2025-09-11 04:25:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 39d7e2ea-00ce-361c-b757-89a0e6be15e3 | -15.8711 | -54.92956 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0d8f9a3b-3e69-3a61-9a2d-6172855c9de0 | -19.36956 | -43.26818 | 2025-09-11 04:25:00 | NPP-375D | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3f729df5-e25c-3512-a500-0d054aef1525 | -17.84262 | -46.74632 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5b42ef8-acc8-31cd-b0e2-827ce17fea44 | -17.51262 | -43.74221 | 2025-09-11 04:25:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28e41436-5795-3fbb-9a1c-047de7ed92eb | -22.82597 | -46.4311 | 2025-09-11 04:25:00 | NPP-375D | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 15a737f2-890d-30fe-8c2d-c36829ecddfc | -17.33951 | -46.70438 | 2025-09-11 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 358567ad-588e-3950-bc73-734e5c1d35f7 | -20.52012 | -47.63005 | 2025-09-11 04:25:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3725ef2d-745b-36e1-b5b6-ed3bc5d41440 | -15.67647 | -47.02377 | 2025-09-11 04:25:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4057e2e4-bafa-335d-af28-cd976793eae5 | -19.4194 | -43.13313 | 2025-09-11 04:25:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d3c9f6bc-7c26-36fd-a062-cc146b6b191d | -19.01218 | -46.25385 | 2025-09-11 04:25:00 | NPP-375D | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 14e4d35a-f14e-30ca-aa4f-ab058f7aed3b | -20.03896 | -42.73332 | 2025-09-11 04:25:00 | NPP-375D | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| dbc3aeec-06ea-39e9-bc9b-80ca345daf38 | -14.27996 | -54.76126 | 2025-09-11 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ba98c623-8b7f-3225-8c93-20d8968d4e9d | -18.0144 | -47.14161 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b28825a-e09d-3127-9275-4352d669ba34 | -15.10227 | -50.06382 | 2025-09-11 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2efcf567-7442-37c2-acb1-f6e1c5a2b82c | -15.08402 | -50.06044 | 2025-09-11 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 608b7ac2-c4d0-381d-a3ec-3ea4e78cc544 | -16.88877 | -45.82607 | 2025-09-11 04:25:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f42fbe84-e305-31cb-b485-52a8cf400fae | -21.9793 | -46.85729 | 2025-09-11 04:25:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 007b2cd3-b6fb-3e18-803e-773ec35d2d20 | -20.35859 | -42.19475 | 2025-09-11 04:25:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 637ae010-bbe7-3645-adfb-77450aacafb4 | -19.17207 | -48.78623 | 2025-09-11 04:25:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| d899ed9b-6e70-3311-a085-f3a732c79b3c | -15.11915 | -52.39592 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f63b4c1-8084-36fb-972a-cdec0f462767 | -16.71354 | -49.3791 | 2025-09-11 04:25:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4d5502be-ea47-3d48-9248-157578771e9a | -15.52011 | -48.37832 | 2025-09-11 04:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08ec5725-4cbe-3e18-9bda-29b40adf1bc3 | -16.29984 | -50.05219 | 2025-09-11 04:25:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 092306fc-0227-346a-a4dd-062cd50ee7a3 | -17.38039 | -52.9287 | 2025-09-11 04:25:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98df5dd3-5ae5-32f6-a8f3-69ce44b3793b | -16.05686 | -49.96676 | 2025-09-11 04:25:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76d5afae-2e12-35e6-92f6-ec7dd3ad7b9a | -24.20104 | -51.76196 | 2025-09-11 04:27:00 | NPP-375D | JARDIM ALEGRE | PARANÁ | Brasil | 4112504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| fd339d46-adbf-3b97-a3b8-e244e5844750 | -24.47508 | -50.80923 | 2025-09-11 04:27:00 | NPP-375D | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d14d6a89-b7d9-3768-b77a-f2d6a1b72f1d | -22.66824 | -53.12811 | 2025-09-11 04:27:00 | NPP-375D | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f6e07aef-964b-37ed-931f-df3c50d63bcc | -23.4177 | -46.14062 | 2025-09-11 04:27:00 | NPP-375D | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8406496f-f815-31fb-8a60-14e43ffdea65 | -22.59878 | -51.88464 | 2025-09-11 04:27:00 | NPP-375D | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 815cd340-bb66-340b-8cd3-4ec32508a503 | -22.92776 | -48.38564 | 2025-09-11 04:27:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 17.4 |
| eeac76b8-90ec-3771-bd42-ae2d0b24d8e7 | -22.92836 | -48.38187 | 2025-09-11 04:27:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 34512921-dba0-3238-9be8-0080c9706b77 | -23.97358 | -46.47151 | 2025-09-11 04:27:00 | NPP-375D | SÃO VICENTE | SÃO PAULO | Brasil | 3551009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b68b9b04-191a-3bd3-a756-8ec76cd7799f | -23.34455 | -47.2087 | 2025-09-11 04:27:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |


[Clique aqui para ver as próximas entradas](README83.md)
