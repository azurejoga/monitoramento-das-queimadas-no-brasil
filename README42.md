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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78eb95ff-cbec-3f02-a42f-a1879f057da2 | -13.73615 | -48.79416 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58a92f83-647f-3522-bf1a-21aaf25282b4 | -10.36475 | -48.89087 | 2026-09-19 04:04:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8945ca41-22f5-34d8-aca0-58c858cf3852 | -14.67509 | -46.68203 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 70d303fe-55e6-322b-b074-89d9bda21f0b | -13.00765 | -46.95113 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 540a565b-075a-3291-b7fe-0c8704678fd3 | -14.10259 | -44.8227 | 2026-09-19 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f142dec2-7799-3d25-8c59-e38c7f81f343 | -12.69056 | -45.95261 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1be5bca2-ff83-3469-9332-e7aaa6188dc5 | -11.13655 | -49.04504 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e0b4db12-e461-37f8-8b14-958a501e2f6d | -14.94864 | -49.93115 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b0d7b03d-78f1-3581-a41f-50826ef84aa1 | -15.02752 | -48.56942 | 2026-09-19 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 402640d3-e64c-3b1d-afbb-897c8631313b | -12.27429 | -49.16854 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 7b3afc6c-f217-33f1-9025-3167d8fee465 | -14.92476 | -49.92665 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 90b28ed3-dd2f-3370-a143-247f043fa08c | -12.86462 | -46.34711 | 2026-09-19 04:04:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ddaaf4ee-2a79-34da-83e5-0bfd37d95be5 | -10.70614 | -50.25721 | 2026-09-19 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 780afddd-4422-3dc1-aca1-ef33f8763f88 | -12.13887 | -46.9826 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 09f7ab0b-3f6f-3734-a727-1eac075fdd46 | -11.91432 | -50.11651 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9772aa97-8bc5-3eb2-ae08-02750bc46450 | -13.6199 | -46.96999 | 2026-09-19 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5593303-7960-3356-a733-d7b7b887e4a9 | -11.40906 | -47.63711 | 2026-09-19 04:04:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8ad34f1-27d6-3e6c-a15d-10b18fbbfb79 | -12.33701 | -50.71825 | 2026-09-19 04:04:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 29127370-11ee-3205-91dc-6769de0877c3 | -10.86491 | -54.11044 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2b06c90b-d503-3abb-9af1-735e9ff59cff | -19.56587 | -47.67108 | 2026-09-19 04:06:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 213f3394-1587-3658-b835-9be7a1663fce | -22.03885 | -49.55664 | 2026-09-19 04:06:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a05eafe6-742e-3b52-a564-2ea46ec91343 | -20.98211 | -48.98882 | 2026-09-19 04:06:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 599df5e9-1780-3f61-9536-5b39625b8e67 | -18.87306 | -49.5092 | 2026-09-19 04:06:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 212abad1-0b30-3a5a-b225-b0cb794dcabf | -18.02369 | -51.07009 | 2026-09-19 04:06:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 88e6ae0d-aa26-32c9-b3fe-916730a1f991 | -19.56677 | -47.66608 | 2026-09-19 04:06:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9c7a622a-0515-33e2-b012-1267d710e92f | -21.25157 | -54.19678 | 2026-09-19 04:06:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2a3041e-83ef-3cb3-8192-1b704f3bbdb8 | -18.8722 | -49.51362 | 2026-09-19 04:06:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c012efc1-dbe6-337a-8f69-2320c9277386 | -23.62037 | -51.78709 | 2026-09-19 04:06:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e2142425-8add-3e4b-bafe-41b7b0762ed2 | -21.02529 | -47.26164 | 2026-09-19 04:06:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0393c9a4-49a7-3d72-aec2-68be1b353560 | -18.87738 | -49.51009 | 2026-09-19 04:06:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0fe20d2e-c819-3c7e-943c-8c6a710448fc | -18.01768 | -51.07481 | 2026-09-19 04:06:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| bb3be407-55be-3916-9c9f-290f06d6abd8 | -20.40917 | -44.49014 | 2026-09-19 04:06:00 | NOAA-21 | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 598c9c17-fdf5-3307-9bcf-c2a93bbd49ae | -21.25042 | -54.19628 | 2026-09-19 04:06:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3100a055-f15b-380a-9d45-24c6148cc88c | -20.905 | -49.06344 | 2026-09-19 04:06:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.5 |
| 483f01da-6007-3ac4-bab9-159f481dd076 | -20.85355 | -49.06909 | 2026-09-19 04:06:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 97acfc16-028e-3b33-b4fa-1197d1a2fd5f | -18.92399 | -44.72766 | 2026-09-19 04:06:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b1c1b54-bbb2-32f7-bb99-728b313016e7 | -19.46188 | -45.65326 | 2026-09-19 04:06:00 | NOAA-21 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef0ce093-902d-3255-9021-94d919a6c5cf | -18.01652 | -51.08057 | 2026-09-19 04:06:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 5637d75e-8aad-3389-8569-2980eb6568cf | -20.85427 | -49.06526 | 2026-09-19 04:06:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 58cfc537-b251-3bf2-bf32-9ed5a7005f7e | -19.19469 | -46.84296 | 2026-09-19 04:06:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a09089da-a44b-34d5-a5ed-5d5b96bb943f | -20.9774 | -48.99166 | 2026-09-19 04:06:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.7 |
| 11c6f2a4-771f-384e-9aa2-7c0c57d2e93b | -20.45393 | -47.59169 | 2026-09-19 04:06:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 6efba667-4efa-3b1c-aa7f-21af0d8af48d | -18.40689 | -49.16153 | 2026-09-19 04:06:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| fb740864-3f3d-33b3-8f16-33b0e972ce69 | -20.98282 | -48.9851 | 2026-09-19 04:06:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 427a5264-093d-3564-a2ad-b9af9fb2242b | -19.56205 | -47.6703 | 2026-09-19 04:06:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1d930465-0c89-3807-9aab-e7159195fc4f | -18.73761 | -48.08837 | 2026-09-19 04:06:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c39a7e90-f55b-35fb-b067-b56ba0fa1341 | -22.03554 | -49.55169 | 2026-09-19 04:06:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1bd3d362-9fe9-3909-94bb-e1b7d9b8e39d | -19.56385 | -47.66036 | 2026-09-19 04:06:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0176be92-876b-3d16-a264-338333b1e238 | -18.82624 | -47.9337 | 2026-09-19 04:06:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2f556751-f319-3f03-affe-21843438f850 | -20.98142 | -48.99253 | 2026-09-19 04:06:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| c181b2bc-5376-3e1f-aea7-941c86df0dc4 | -20.97809 | -48.98796 | 2026-09-19 04:06:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.7 |
| 3aa88bd0-5f8f-341e-b9f5-f260c7689294 | -18.55589 | -47.23762 | 2026-09-19 04:06:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eed1b1de-23f2-35eb-b50c-edde2b018706 | -22.0307 | -49.55474 | 2026-09-19 04:06:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1a698fd3-13b6-3eb4-ae00-d9216a4a2824 | -18.02254 | -51.07579 | 2026-09-19 04:06:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| d25f7bf5-317b-301c-ade0-21f7bc43cc43 | -18.41113 | -49.16246 | 2026-09-19 04:06:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| dea8be0c-9244-304b-8596-dfb13bc75a64 | -19.56295 | -47.66533 | 2026-09-19 04:06:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3a7931c5-4dbe-3d64-a5d8-811a9650c6bc | -19.57059 | -47.66682 | 2026-09-19 04:06:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e3958872-99b7-3cb5-89d4-67d957037e31 | -22.49362 | -47.09763 | 2026-09-19 04:06:00 | NOAA-21 | ENGENHEIRO COELHO | SÃO PAULO | Brasil | 3515152 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d683bf09-6d1e-375b-9251-f99de40b176b | -18.02138 | -51.08156 | 2026-09-19 04:06:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 22.5 |
| e46f0324-9d7c-38bc-9548-753f649918f3 | -20.90574 | -49.0596 | 2026-09-19 04:06:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.5 |
| f5df711c-600d-3ab0-8feb-0983346037c9 | -19.44776 | -47.5682 | 2026-09-19 04:06:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8898e35f-6271-30fe-aabf-410b2814dcc0 | -19.05774 | -46.35435 | 2026-09-19 04:06:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5668e03b-0f51-336a-ba65-0ff6b810955e | -18.87652 | -49.51452 | 2026-09-19 04:06:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 28ef5364-3011-3f36-9281-c1c18136ce89 | -20.85022 | -49.06438 | 2026-09-19 04:06:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 513edb38-6a7d-3dc7-871b-0851001d6e90 | -23.62112 | -51.78384 | 2026-09-19 04:06:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a2518251-4c83-3f4d-bdaa-c3f12234464c | -18.83016 | -47.9345 | 2026-09-19 04:06:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| cdb55163-af07-3ad3-b24b-0887ca32dc75 | -18.01884 | -51.06908 | 2026-09-19 04:06:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| f1559253-38bf-3ea4-92a9-0b28ed885025 | -22.02819 | -49.54569 | 2026-09-19 04:06:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| ad072669-8dc8-3c0d-80a5-2384a3e907bd | -18.83567 | -47.68098 | 2026-09-19 04:06:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 007cb75c-4c48-31b5-a47f-cb406c566a79 | -21.24604 | -54.19554 | 2026-09-19 04:06:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d922825-4abb-3893-8bc5-a763768ab3a8 | -18.88511 | -46.84957 | 2026-09-19 04:06:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa287053-d24a-33a8-8026-17ca47935251 | -21.46 | -48.68273 | 2026-09-19 04:06:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c9fb856-2a0c-3c8c-aef2-d0fac152a968 | -18.92494 | -44.72738 | 2026-09-19 04:06:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 865edb52-3dd5-3f1b-8616-2e3f9a2b3e4c | -20.84949 | -49.06822 | 2026-09-19 04:06:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 3eb2da97-6a4e-31a8-bca5-85e5e968dc6e | -20.97879 | -48.98426 | 2026-09-19 04:06:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| bf518b4b-52cb-36e9-a13a-62faef67e139 | -18.41034 | -49.16663 | 2026-09-19 04:06:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 74a12fc6-1d80-3d3b-9e7a-86d56bb60788 | -10.6928 | -60.7322 | 2026-09-19 04:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| b9c92aa3-b2ce-3b4f-ae3d-1a5324c480fa | -10.7115 | -60.7312 | 2026-09-19 04:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 65d57a4c-c276-38e9-8091-833ba8730640 | -7.5661 | -61.3239 | 2026-09-19 04:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 1273c7de-0317-346b-ba63-0a307c115b36 | -10.7115 | -60.7312 | 2026-09-19 04:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 96c43168-287e-35e1-869b-15eed1393ef9 | -10.7117 | -60.7118 | 2026-09-19 04:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 04b0c3e9-3204-3baa-9b40-873aa4f23872 | 1.22793 | -51.00468 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8e365694-355d-3955-8d07-cbc44ec1f516 | 1.22725 | -51.00031 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 051d6768-c758-3884-a32b-3517fed933d0 | 1.22346 | -51.00538 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 303fa9ed-17cf-3475-b7e3-be683b9fe2b4 | 1.25992 | -50.75078 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80b7cf2d-c8ef-3ce6-bd36-f46bcabf04ec | 1.25574 | -50.97799 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 50c63d34-8719-37af-bf19-8b27d65e095c | -0.26516 | -48.41245 | 2026-09-19 04:36:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a5cee9af-d1b3-320b-bbbb-05ed3ffe3938 | 1.21453 | -51.00675 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5ed7d783-dbbb-31d1-ad3f-1e969f39a50c | 1.25196 | -50.7545 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb847e3d-8542-343b-b49e-97f74f9f243d | -0.75467 | -48.71037 | 2026-09-19 04:36:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2129dac-e0eb-3cf6-a638-c86be7d02e0f | 1.21967 | -51.01042 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 72823695-3582-3968-8845-ecd28e98eb40 | 1.25128 | -50.97868 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cd473c8f-8ccb-33d5-8ae0-2b810f59cffd | 1.22278 | -51.001 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1e4615e9-c4b0-3e99-ac00-227bef95cda8 | 1.21521 | -51.01112 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 5759145d-3f76-3abf-a064-076f9f61ed18 | 1.26366 | -50.74585 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e201ab1e-8dc8-3585-9c4b-72c216894738 | 1.14074 | -50.99059 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a93258fb-7c52-3aa6-ad3a-96f339bc1422 | 1.25553 | -50.75148 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58ecd7cd-6f5e-324c-882c-ef55cd473e64 | -0.26584 | -48.40811 | 2026-09-19 04:36:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64bf35c4-07d9-3699-92f7-f55167cc1f98 | 1.13628 | -50.99127 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d3d734fc-6caf-3e7f-ac4c-45599470c58e | 1.25505 | -50.97363 | 2026-09-19 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README43.md)
