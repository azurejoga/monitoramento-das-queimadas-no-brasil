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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5131b6e-5b4a-35ea-a1bc-6c5983ca2f58 | -11.84284 | -43.78688 | 2025-12-25 04:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 831556fd-e3dd-30eb-a7e5-f9906d58bf67 | -11.7575 | -43.32108 | 2025-12-25 04:57:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4028819f-49ec-320b-9243-acfa9d14f96b | -11.7537 | -43.31421 | 2025-12-25 04:57:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ecf4234-ca07-307e-932d-0981ada9725c | -11.75799 | -43.3277 | 2025-12-25 04:57:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 648d6f9c-025e-39b4-9420-eb95875b757c | -11.74676 | -43.32195 | 2025-12-25 04:57:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 935b3828-de2b-3118-8637-cb17885cbcb0 | -11.75211 | -43.32696 | 2025-12-25 04:57:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f395f394-d28e-3d1c-8af4-eb488d57980b | -12.51353 | -48.37736 | 2025-12-25 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f9ca3215-90fb-33c9-9975-005511a5836a | -11.84189 | -43.79478 | 2025-12-25 04:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0ffad4f-bc73-3a90-9797-ca97ad05653e | -12.90746 | -52.52475 | 2025-12-25 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49857d2d-8c01-3af3-b8fc-dd99cd350de8 | -8.27704 | -55.10922 | 2025-12-25 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 050aea8d-2e53-3230-b6ef-a8a830344dc1 | -15.51663 | -51.85819 | 2025-12-25 04:57:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e71485a-c374-3ea9-b9dc-62fb0711503b | -12.89835 | -52.51565 | 2025-12-25 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49a59862-77c9-39d7-933f-1a21e2565c82 | -12.90803 | -52.521 | 2025-12-25 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43981b23-cf97-355c-b6c1-3f51439ad534 | -11.84759 | -43.79558 | 2025-12-25 04:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68bb4d0f-3770-31df-941e-57a7839b9a3f | -12.51831 | -48.3739 | 2025-12-25 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28add66c-a67d-3388-9165-66b507d9b562 | -11.75261 | -43.3118 | 2025-12-25 04:57:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da9743f3-3e69-337d-9cce-d468de6d3f35 | -11.75852 | -43.32344 | 2025-12-25 04:57:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 472b3e44-f4d8-35ed-b3ad-bff752ddb84e | -11.75162 | -43.32032 | 2025-12-25 04:57:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ca7d48a4-ae13-338a-bd77-f7a1823ba3c2 | -11.75317 | -43.31845 | 2025-12-25 04:57:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27f03702-b50e-3667-a206-7a55e0724bab | -12.51338 | -46.29182 | 2025-12-25 04:57:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33cba5b8-c00c-3238-b2da-614265525f9b | -12.51408 | -48.37331 | 2025-12-25 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 588d525f-8d38-39a9-90cc-c8bc98d55f36 | -19.2097 | -53.43399 | 2025-12-25 04:59:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23d7bc07-8d6d-3a6b-993a-ed227baf9971 | -17.79615 | -46.98907 | 2025-12-25 04:59:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0035903b-df98-308c-b01f-8d0f20148eda | -19.53349 | -43.61205 | 2025-12-25 04:59:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae36af4f-f271-3b0a-be96-97b59d61cc38 | -15.96433 | -57.24098 | 2025-12-25 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bbdcaf65-d273-3a98-a377-bc726cac5ca4 | -19.21167 | -53.43554 | 2025-12-25 04:59:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef126663-dcad-3eba-8626-152f974a4a5f | -17.01482 | -47.25441 | 2025-12-25 04:59:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3e303e5-69be-38b4-bb01-1773fa3b3f29 | -18.59171 | -46.55099 | 2025-12-25 04:59:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85ccab87-f119-360a-9f4a-ff4c2c829dc9 | -19.53395 | -43.60681 | 2025-12-25 04:59:00 | NPP-375D | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3569bda1-e848-3fe7-80d4-50f8207fdf57 | -15.96085 | -57.24043 | 2025-12-25 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 387f6e71-5967-36fd-9142-fd2647aedf48 | -17.01819 | -47.25142 | 2025-12-25 04:59:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8936f45-43ad-38a7-b287-e3bf5e0b9f71 | -17.01548 | -47.24899 | 2025-12-25 04:59:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5081401b-7450-309a-af8d-22172a889bad | -18.59693 | -46.55143 | 2025-12-25 04:59:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04acf993-c5e7-3eb3-b154-7def5e4102bd | -19.21317 | -53.43454 | 2025-12-25 04:59:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0bebf47-4a5a-3724-8fe0-a78ee540d193 | -17.01756 | -47.25694 | 2025-12-25 04:59:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d746c40-1211-39db-b3e2-6a314cf83dc3 | -18.59601 | -46.55187 | 2025-12-25 04:59:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98a4dcbe-a99a-31a1-af7c-fc0a30975de4 | -15.96714 | -57.24558 | 2025-12-25 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5af35804-bb37-3bad-8a74-e59f26203176 | -25.51435 | -49.46171 | 2025-12-25 05:01:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1c4d8202-181b-3800-8e6a-dda410d7b6bc | -25.25848 | -49.67055 | 2025-12-25 05:01:00 | NPP-375D | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 59a1f26b-d01e-3a7a-95d0-1a3848d823b0 | -25.51381 | -49.46704 | 2025-12-25 05:01:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 4ee7b5a9-95e3-3c43-b1e5-a08cd9c48237 | -25.5185 | -49.46773 | 2025-12-25 05:01:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4b064b9a-49a9-3e35-b041-6a007a41aaa4 | -21.75894 | -53.14711 | 2025-12-25 05:01:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c436c24f-21fa-33b0-94e0-8f124f0e391b | -25.25714 | -49.67153 | 2025-12-25 05:01:00 | NPP-375D | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2331ded4-40ef-3796-827b-d273e412661f | 2.87334 | -60.26308 | 2025-12-25 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b879b74-b4a3-3fee-89c9-25894627dc3e | 2.87696 | -60.26252 | 2025-12-25 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b804ae5b-fe77-398f-8e57-e4a17237b671 | -8.27471 | -55.11095 | 2025-12-25 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f5f6ca7-09f9-38cd-bd14-5c7dcef8127f | -12.90762 | -52.52433 | 2025-12-25 05:20:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7d2b1e8-64b5-3807-98b7-fae4976a9eb1 | -15.96364 | -57.24044 | 2025-12-25 05:20:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2ef81cc-05e3-3224-92b3-7e342db11664 | -12.90269 | -52.5237 | 2025-12-25 05:20:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25c020c0-e767-3433-8ee7-6f9f5da9ea70 | -15.51943 | -51.85771 | 2025-12-25 05:20:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4b44e4c-d91d-349c-91f6-916e8b1b7a53 | -12.89848 | -52.51744 | 2025-12-25 05:20:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7be8cdcf-b21c-3dea-9bbd-019224e4ee4b | -15.96339 | -57.24292 | 2025-12-25 05:20:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e4b4a1a-77ff-3446-962a-9b095637c3e6 | -15.51904 | -51.86115 | 2025-12-25 05:20:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8929d1a2-4864-33cd-99c4-4163defb524c | -15.96715 | -57.24365 | 2025-12-25 05:20:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 246691f7-42e7-3b09-88e7-5707867e86fc | -15.96675 | -57.24569 | 2025-12-25 05:20:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91beaa57-2e5c-32d7-97aa-cdcf5ddaa062 | -12.51183 | -48.37818 | 2025-12-25 05:20:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f2fc00ff-c83e-31ca-b150-e970496ae706 | -15.5137 | -51.86047 | 2025-12-25 05:20:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ec2c306-41b6-3051-af2f-6fbd7414d91d | -12.90342 | -52.51807 | 2025-12-25 05:20:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15e0579a-0767-3783-b334-3775bd42eeb5 | -19.21024 | -53.43716 | 2025-12-25 05:22:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de71dc0a-bfbb-3137-82c8-bf31710622fc | -3.72245 | -38.55133 | 2025-12-25 05:44:00 | AQUA_M-M | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 7a629047-c43a-3ef6-b21f-9b4b43fc6e40 | -3.72384 | -38.54191 | 2025-12-25 05:44:00 | AQUA_M-M | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 25.4 |
| fd4d08b8-ec7a-338a-b67e-2f987da8315d | -11.75623 | -43.32034 | 2025-12-25 05:46:00 | AQUA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 427ef07b-e9fc-3a9d-8548-2d10d5e61a45 | -11.74725 | -43.31892 | 2025-12-25 05:46:00 | AQUA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 4cf9843d-9858-3331-85ae-89be36736c26 | 4.04907 | -59.73893 | 2025-12-25 06:03:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 049c9965-342c-39f2-b543-e2cfcc19c1e3 | 4.04966 | -59.7425 | 2025-12-25 06:03:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e27da624-44f9-31e9-9ff9-06c533c66a41 | -5.39567 | -37.66776 | 2025-12-25 11:55:00 | TERRA_M-M | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 26.4 |
| 3cb0e2df-b95d-3248-b343-2a741116ffc0 | -3.49723 | -39.89759 | 2025-12-25 11:55:00 | TERRA_M-M | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 20.8 |
| b5a7861c-fbf6-3320-906f-3ea90aa555bf | -5.40771 | -37.66921 | 2025-12-25 11:55:00 | TERRA_M-M | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 34.5 |
| 7b0efaa6-2962-32be-ab76-c925369c45ab | -11.84308 | -43.79393 | 2025-12-25 11:57:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 60971f64-e7b1-33dc-a13a-f7b1f12217b7 | -11.7526 | -43.3224 | 2025-12-25 11:57:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 330475f6-33ed-3852-b30a-a920477b4a5b | -10.98216 | -44.72224 | 2025-12-25 11:57:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c25ec34f-0b9f-3b9e-85e9-3afc8f17286a | -9.36625 | -40.68958 | 2025-12-25 11:57:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 13.6 |
| e4203e2b-3a28-308d-bfcf-825c12272421 | -13.61895 | -43.00834 | 2025-12-25 11:57:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 730fdebe-6b84-3985-a0b7-80eba9c3013e | -10.64511 | -42.67126 | 2025-12-25 11:57:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 410d9ef3-fcd9-3d6c-a96a-814a52c7c428 | -10.63674 | -42.67397 | 2025-12-25 11:57:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 3c74747a-df23-3248-82c5-659543d947d2 | -10.0405 | -41.37495 | 2025-12-25 11:57:00 | TERRA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 275d97fd-7385-3ada-ac20-07fbd33739ae | -10.03901 | -41.38599 | 2025-12-25 11:57:00 | TERRA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 456d823b-b20e-3c9c-b9a2-4bed046eeb95 | -7.01801 | -39.85541 | 2025-12-25 11:57:00 | TERRA_M-M | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 3dea79b5-6f4e-35b0-936e-f9cb0f145fbf | -7.01968 | -39.84302 | 2025-12-25 11:57:00 | TERRA_M-M | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 61.8 |
| 7936ec59-57cd-3c28-bf3c-6b379e8a6e70 | -12.10538 | -43.50172 | 2025-12-25 11:57:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b0da2458-074d-3e2b-b3ee-0137db4f5a71 | -11.76164 | -43.32366 | 2025-12-25 11:57:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5abae8b1-b6d5-311d-8ec8-f98ca48f845d | -20.3638 | -43.41623 | 2025-12-25 11:59:00 | TERRA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 022950f5-56a2-3867-9ea3-20476d8ffc8d | -22.22536 | -42.51675 | 2025-12-25 11:59:00 | TERRA_M-M | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 61637824-9e66-3377-9a83-288a70400f56 | -20.39546 | -43.41568 | 2025-12-25 11:59:00 | TERRA_M-M | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| d5c18aae-c7e0-3677-a115-9f7c07751ddc | -22.23973 | -42.52454 | 2025-12-25 11:59:00 | TERRA_M-M | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| bbba3f8d-e83e-3e5f-8e14-8666cf032bae | -19.88649 | -43.66384 | 2025-12-25 11:59:00 | TERRA_M-M | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 766cc08e-8b56-3097-a794-000c7fc9fa28 | -15.50104 | -43.23242 | 2025-12-25 11:59:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 8.1 |
| cf0bd3fc-fc74-3dd9-a454-74fbc13b5c30 | -20.05892 | -43.9818 | 2025-12-25 11:59:00 | TERRA_M-M | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| be29628e-b589-367c-aab4-6c80d4bec997 | -19.53561 | -43.61491 | 2025-12-25 11:59:00 | TERRA_M-M | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c18e26a8-f34a-39ae-a444-b88056d1bd5f | -22.29332 | -42.53147 | 2025-12-25 11:59:00 | TERRA_M-M | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| d06078b3-2035-3e71-9267-2aeee70cef13 | -20.73154 | -42.03436 | 2025-12-25 11:59:00 | TERRA_M-M | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 7218c8f7-5420-37f9-ab39-7b5bf7239703 | -21.70588 | -43.43736 | 2025-12-25 11:59:00 | TERRA_M-M | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 31bac5da-7bde-3b50-bd53-d5c4372a9364 | -19.53704 | -43.60354 | 2025-12-25 11:59:00 | TERRA_M-M | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6832f2e6-b522-3cbe-ae26-f4d4b3184c65 | -21.70739 | -43.42507 | 2025-12-25 11:59:00 | TERRA_M-M | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| e5e8afc3-3bd6-30c0-a6db-23558f691c9f | -19.84386 | -43.17745 | 2025-12-25 11:59:00 | TERRA_M-M | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 59debb61-0071-303a-8c6f-876f57b455d9 | -19.60054 | -44.12349 | 2025-12-25 11:59:00 | TERRA_M-M | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0f5325c4-26ad-3384-b5d2-cd58b27fd3fe | -22.46262 | -42.64663 | 2025-12-25 11:59:00 | TERRA_M-M | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| e545f41d-20b4-3d48-8f02-a59fa9353dd2 | -23.68719 | -48.02426 | 2025-12-25 11:59:00 | TERRA_M-M | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| caa67abf-93ca-3821-bf30-e355b39459f2 | -19.60991 | -44.12482 | 2025-12-25 11:59:00 | TERRA_M-M | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e327ab0b-3a54-3722-bb24-454ff1209172 | -20.89016 | -42.34066 | 2025-12-25 11:59:00 | TERRA_M-M | MIRADOURO | MINAS GERAIS | Brasil | 3142106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |


[Clique aqui para ver as próximas entradas](README4.md)
