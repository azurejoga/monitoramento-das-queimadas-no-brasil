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
| ca065994-def2-3fbd-bdab-bdab3b4b1a6d | -18.64043 | -55.73331 | 2025-07-08 04:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b36aa02a-28f2-3aaa-9650-5973d711ad3a | -17.65417 | -46.831 | 2025-07-08 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f99dbb0-ca41-3b0e-a3f0-1a21fa157e28 | -20.77379 | -49.86236 | 2025-07-08 04:44:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7a855432-129f-352f-bb55-a9da9201724c | -15.69399 | -53.32563 | 2025-07-08 04:44:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19b21f66-e72c-3a19-a662-c932720bee6c | -18.73427 | -49.10402 | 2025-07-08 04:44:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d74e5fea-62b8-3724-8fd6-b083d7c88078 | -15.96282 | -52.21016 | 2025-07-08 04:44:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 248c77c5-d920-3cee-8664-28c78f3a14fd | -21.3044 | -48.56377 | 2025-07-08 04:44:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4f1b1cf-c033-34e9-8be0-664815621cd4 | -19.08982 | -56.0483 | 2025-07-08 04:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 899bd798-022a-3eea-8972-0931eab19847 | -20.62523 | -54.83837 | 2025-07-08 04:44:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 487ec163-06bd-347e-a64b-06a86691b653 | -19.00532 | -48.05881 | 2025-07-08 04:44:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1baa6f6-d968-30a6-9bd8-8d02cde82461 | -20.72337 | -56.65354 | 2025-07-08 04:44:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 412ea669-be77-31f2-a2c5-e0237d13c5b2 | -15.07665 | -48.94432 | 2025-07-08 04:44:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19ef4b0b-cb7f-3181-988d-ba885a7cee26 | -17.91772 | -45.55733 | 2025-07-08 04:44:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 408f25c9-1a27-3109-94e3-902e299b717c | -17.67532 | -52.90601 | 2025-07-08 04:44:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fbd7f7a-833c-374a-ad49-11c6d1494895 | -18.51971 | -47.15271 | 2025-07-08 04:44:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06554922-9bc9-38a8-b2f8-d746930a9cc0 | -17.05923 | -48.65837 | 2025-07-08 04:44:00 | NPP-375D | SÃO MIGUEL DO PASSA QUATRO | GOIÁS | Brasil | 5220264 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b187f0c4-50b3-342a-9cd8-2af03efcefb6 | -21.19003 | -48.93918 | 2025-07-08 04:44:00 | NPP-375D | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8be66254-766b-3f41-a2b6-587559b0980b | -15.56886 | -47.85691 | 2025-07-08 04:44:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c46d60e-cf38-33f4-9ca7-8b74f9b43496 | -20.87649 | -43.91321 | 2025-07-08 04:44:00 | NPP-375D | CASA GRANDE | MINAS GERAIS | Brasil | 3114907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 356fd10b-86ec-36c1-ba25-a3acf9343da5 | -20.62179 | -54.8377 | 2025-07-08 04:44:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 055cc1e3-e671-312f-aef0-1a2089d3eaa4 | -19.08615 | -56.04757 | 2025-07-08 04:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| dc4d921e-cedc-3b7c-a6bc-71fbf91f45d1 | -16.06756 | -53.75225 | 2025-07-08 04:44:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c64feeca-652f-3985-b15b-76f775ac9676 | -20.77319 | -49.86662 | 2025-07-08 04:44:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 072c9d14-af01-3c52-8ffa-c5051b3f9820 | -16.06494 | -51.56702 | 2025-07-08 04:44:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 902e4dc7-cdfa-336e-b572-efd904537dd2 | -17.7755 | -42.80793 | 2025-07-08 04:44:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51a0df1e-383a-3de4-b873-a08b835b6517 | -20.72708 | -56.65421 | 2025-07-08 04:44:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84500cce-104f-3d39-a33f-532a928a5c25 | -16.05169 | -43.79956 | 2025-07-08 04:44:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ae11a21-7b49-3a57-9b6c-c12a4c4d9f5a | -18.6412 | -55.72887 | 2025-07-08 04:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 00bb9bbc-bc1e-3c34-be8e-8c9e26facc1a | -14.84066 | -48.24314 | 2025-07-08 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e642331-bc98-3782-a9ce-6a174ffc5f5f | -15.25057 | -51.53808 | 2025-07-08 04:44:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 054dd39a-78c0-3124-ab4e-a23cbc72fa0a | -18.73488 | -49.09968 | 2025-07-08 04:44:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ce407220-390f-3df1-82e5-d62d809687bc | -16.58223 | -43.64838 | 2025-07-08 04:44:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e6664d6-7620-32e4-b8c7-b28816b82964 | -14.84186 | -48.23479 | 2025-07-08 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2fe3783-3b5d-3d6a-9a49-2c2e994be836 | -15.25113 | -51.5345 | 2025-07-08 04:44:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d7850fb-6900-39c3-b1b0-664dae9aa1e3 | -21.72558 | -46.37582 | 2025-07-08 04:44:00 | NPP-375D | BANDEIRA DO SUL | MINAS GERAIS | Brasil | 3105301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 18c285a6-97b4-3f9b-ba20-bc224f098158 | -20.77915 | -49.61528 | 2025-07-08 04:44:00 | NPP-375D | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bfff9f15-c92d-39d2-80c4-f5cfc8f2ef1d | -18.64198 | -55.72445 | 2025-07-08 04:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8c362f2e-e863-3a35-8a38-fe86d8f6e320 | -20.45995 | -44.74559 | 2025-07-08 04:44:00 | NPP-375D | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fe92c9cb-7d2e-3004-8a83-9a584b5a464e | -20.87825 | -43.91307 | 2025-07-08 04:44:00 | NPP-375D | CASA GRANDE | MINAS GERAIS | Brasil | 3114907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| df57e505-4ffa-3b64-ab41-44e1198c8b66 | -16.07193 | -46.12856 | 2025-07-08 04:44:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9097fbe0-e4fa-3b80-af08-857d6e29115d | -18.64407 | -55.73402 | 2025-07-08 04:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e3601b42-4094-305f-bff4-fbc38ed4ade5 | -23.59464 | -47.44078 | 2025-07-08 04:46:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3ed833ab-6f85-3f4b-9966-ef14ddef0645 | -23.55673 | -54.80146 | 2025-07-08 04:46:00 | NPP-375D | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1c5db9dc-e5ed-3e3d-aa74-f79417de4a3a | -23.55737 | -54.79758 | 2025-07-08 04:46:00 | NPP-375D | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3d381c9d-47e3-3139-8bf2-f105db17710e | -22.54004 | -48.81278 | 2025-07-08 04:46:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0644b2f8-c140-3b21-a2a3-03052c98b7da | -27.4517 | -48.42675 | 2025-07-08 04:46:00 | NPP-375D | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9b36cd93-a85d-3e55-8de2-d68cf1e708a6 | -23.75756 | -45.72896 | 2025-07-08 04:46:00 | NPP-375D | SÃO SEBASTIÃO | SÃO PAULO | Brasil | 3550704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9d84a30d-2b29-32ff-bf79-83eb46c2d43c | -24.74264 | -53.80952 | 2025-07-08 04:46:00 | NPP-375D | TOLEDO | PARANÁ | Brasil | 4127700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e58b71b4-7de9-3333-9548-3c8c9d97029c | -22.20286 | -56.32152 | 2025-07-08 04:46:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57e9a571-ec21-3ecb-95c8-ce6aac5c6407 | -11.4205 | -45.095 | 2025-07-08 04:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 25aac689-d06e-35c6-a107-cd5417d941c3 | -11.4397 | -45.0923 | 2025-07-08 04:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| c49bcd95-924e-3f1f-8b5f-998b66bba723 | -11.4201 | -45.1181 | 2025-07-08 04:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 2eba9e78-d31e-31fb-bdc7-2841744b29f5 | -10.6299 | -49.4504 | 2025-07-08 04:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| aa2ac2e4-67a7-391f-bd6d-fc091158a403 | -10.6489 | -49.4483 | 2025-07-08 04:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| dd0bb80a-f58d-3254-8f19-79ec2f6a8856 | -10.6486 | -49.47 | 2025-07-08 04:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 885c6e29-4f27-3058-9ea8-05d6bb22dcd9 | -11.4393 | -45.1154 | 2025-07-08 04:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| e261f7dc-bbb4-3ba2-92a3-4d5ace6ddcd7 | -10.6299 | -49.4504 | 2025-07-08 05:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 4460a0ea-268f-3140-a4d0-0e4472f356ce | -11.4393 | -45.1154 | 2025-07-08 05:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 662ab38d-4eeb-3058-b811-9a9b7699456a | -11.4205 | -45.095 | 2025-07-08 05:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| f8eaf503-1629-3281-a36c-7a2cc4a359db | -5.3986 | -43.2467 | 2025-07-08 05:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 91aaa6e3-41fc-36aa-8d35-d3cd73167778 | -11.4397 | -45.0923 | 2025-07-08 05:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 771ef5d9-cb2a-3a93-b276-4608de969dfc | -10.6486 | -49.47 | 2025-07-08 05:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| db7feb55-f1b9-3ca9-aed4-7d1ae4824af6 | -11.4201 | -45.1181 | 2025-07-08 05:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 68f3584e-55d9-3365-92f6-07bdae25d13f | -5.25269 | -44.46362 | 2025-07-08 05:01:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8faf8f6f-01d0-3c18-9fc1-5f0365c3f910 | -5.41221 | -46.07529 | 2025-07-08 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b1ce7734-5ba3-336f-a7ab-780ddb1a50ae | -5.40263 | -43.24365 | 2025-07-08 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2931b79a-43ff-3572-94db-e5b69194c7fc | -4.36937 | -48.22719 | 2025-07-08 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 333f646a-63d0-327d-8235-7809ffd0de81 | -6.00665 | -44.5287 | 2025-07-08 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 990ca5c8-5ea3-3412-ba1c-d8a704c50b27 | -6.01213 | -44.53439 | 2025-07-08 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fadf5a82-b699-3fd4-b187-60223e2c4468 | -4.69097 | -47.00563 | 2025-07-08 05:01:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25f5d95c-859a-37c8-81cc-eff25459c172 | -5.39526 | -43.24835 | 2025-07-08 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f039b66b-89cc-39ef-895c-3445b792b4c6 | -5.41228 | -46.0758 | 2025-07-08 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 32d0f3b3-3c22-3395-a2b4-ade5a3f4308c | -3.62013 | -51.91476 | 2025-07-08 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9acc1a45-ac22-3b88-83f5-a9f63b563301 | -5.41327 | -46.06872 | 2025-07-08 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1e6900bf-e510-3322-9184-34c6c6e4db53 | -5.40182 | -43.24956 | 2025-07-08 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 14aefbae-b405-3b45-b650-dd99d4121913 | -5.41271 | -46.07187 | 2025-07-08 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e75fb77e-b264-3d6c-91d2-19785c608e80 | -4.42489 | -48.1441 | 2025-07-08 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 181e2f4f-b21c-3502-a80c-156d4d32347f | -5.41276 | -46.07238 | 2025-07-08 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c9a08987-8fc5-3855-8728-6bea18940bb0 | -5.23709 | -46.04129 | 2025-07-08 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff861254-2872-3bbe-98f2-8d6b73140576 | -5.41326 | -46.06817 | 2025-07-08 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c9bd065-7b9c-389d-8180-11669b14bbf1 | -5.2376 | -46.03772 | 2025-07-08 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97a8570a-0719-3b3f-a82c-3a9931435b02 | -5.39672 | -43.24921 | 2025-07-08 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ba52cab8-0e9d-3bd8-b0b4-9d347bdf3de5 | -6.82401 | -43.58881 | 2025-07-08 05:04:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c7f6402-7589-3510-98c5-291cc5cc15c5 | -10.6508 | -49.45969 | 2025-07-08 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| fa4dbefd-f837-3a15-b216-0c889dae09da | -7.25432 | -43.08628 | 2025-07-08 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| e10cca28-6c9e-3017-92ea-65a87deb58d8 | -6.77633 | -55.48766 | 2025-07-08 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b246f1cc-aeec-3653-b66b-ba3843234919 | -9.3551 | -58.846 | 2025-07-08 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed037310-1765-35a1-ab2c-01b377e6b5da | -10.39394 | -52.17702 | 2025-07-08 05:04:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3966625e-39fe-3d4d-bdf1-8b3ea33de511 | -6.34526 | -46.36367 | 2025-07-08 05:04:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4de83f3c-2322-3f75-9d59-232ff401e812 | -7.31062 | -55.30715 | 2025-07-08 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fd42cdeb-8eda-3fdb-aa3a-394318eaf844 | -12.96694 | -47.82664 | 2025-07-08 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52866736-daff-3e18-96ba-b8468ba2ba6b | -12.97169 | -47.82416 | 2025-07-08 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 903ecfbd-0ea0-3490-b76e-f2390f00daca | -6.89027 | -45.24068 | 2025-07-08 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8dd8b64e-43ed-3c22-8cbb-30332cd10db5 | -13.03509 | -46.2873 | 2025-07-08 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dbf5cbd-a575-3c21-8c56-68226c2a3162 | -12.9924 | -44.88467 | 2025-07-08 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd11aff2-4c1d-3b0c-b269-de1e2e41fbaa | -9.35384 | -58.85368 | 2025-07-08 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 977d916a-9c03-3300-9fe9-e81ccd750e5c | -10.57391 | -49.11882 | 2025-07-08 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c1fac1a-4b7a-3f5c-9dec-a34b765afbb7 | -10.7909 | -49.24905 | 2025-07-08 05:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60112f42-ca10-37be-abc2-d7f4d9a52280 | -11.41779 | -45.11025 | 2025-07-08 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| ad78850f-63d9-3ef1-9929-724177fea9ce | -6.67553 | -43.76385 | 2025-07-08 05:04:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README17.md)
