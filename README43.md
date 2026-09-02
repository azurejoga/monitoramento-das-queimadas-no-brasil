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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e29d780-1f7a-390a-9055-44b9037302d2 | -7.53505 | -60.7157 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a1b0b3c-8524-35f1-b686-1b116daeed3c | -8.71399 | -52.35945 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49134f08-081e-3e48-b02f-7ebe4c02cdae | -7.06388 | -52.72667 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b284a98d-e28c-3cbd-9677-43083dd168c1 | -6.94646 | -56.46354 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c69b3281-be7a-34ef-bed8-08f9ab3928cc | -8.47778 | -54.71383 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| ab7328f4-beb7-3df6-bb2e-50d03acb2e23 | -11.34981 | -45.42466 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fadbb2cb-a668-3da5-b78b-504e9e04db37 | -5.32856 | -60.14599 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35921257-1ef0-3242-9a75-063cf35faeab | -11.48437 | -45.08453 | 2026-09-02 04:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cff6b874-14af-3352-ba60-c123abca38c2 | -6.26133 | -55.42426 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1abe2f66-0ceb-3d45-a985-decb8d32cbf6 | -12.87675 | -45.82828 | 2026-09-02 04:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3f2610c9-6929-32a2-98e8-5888d618b5af | -10.16324 | -50.37644 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38abab49-df42-3859-8bb0-723d42c54adb | -6.87414 | -59.4015 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 178019ec-e171-386b-869a-09732aff9ce4 | -8.47067 | -54.73412 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc8e9c3e-36de-3820-ad0d-aa32f7a2fd3d | -8.46414 | -54.72874 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe1d0fd8-938e-3eca-a9e2-6576d56fbd8f | -10.49351 | -64.32605 | 2026-09-02 04:57:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28a15da8-59c4-3dfd-ac1e-ac3491631483 | -6.18414 | -57.73246 | 2026-09-02 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7480626a-f24b-3641-87a3-1aed046aea3d | -10.90095 | -45.33927 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1780cce3-93c0-3a08-8879-81df3887272f | -9.00193 | -50.77804 | 2026-09-02 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 259c763f-20cd-3b20-8b96-03f021a5467b | -9.39457 | -51.67912 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6436d42-89ad-37d2-bac8-eab2c41c82cf | -8.29323 | -54.92354 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f64cd3a-9500-3224-a060-202f273a5b24 | -10.40767 | -50.00766 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d79566b-0f53-3d41-8bfd-4ac589102bbd | -12.13953 | -47.1335 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dc57dfff-9c37-3018-81bc-76cbeb60e05d | -8.74501 | -62.56662 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb814d03-dbf2-3560-8e9a-385b4cc5341a | -10.74364 | -54.02982 | 2026-09-02 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06475cc1-032d-34bd-af12-84c95d801cc3 | -12.1421 | -47.11504 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 993d5f7d-deee-342e-8ef5-627278bde431 | -7.28803 | -49.81491 | 2026-09-02 04:57:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec0a36ea-4cf6-3ff1-9914-f6c7c57fea91 | -12.09838 | -47.0976 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 393dcec1-6c38-3660-8d2d-c8a63baea291 | -8.45188 | -54.73531 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa8fb93a-1123-3ec5-87a4-72522e85a338 | -11.29213 | -45.16792 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 84bda0f5-9a47-328a-bdf9-5d4740f1adb2 | -10.87225 | -50.46721 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ea2627d-00ed-3827-9642-6ac60c98355f | -11.27915 | -46.56679 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81a68f6a-2472-3a8d-8fd8-abc6c0261c07 | -6.07264 | -53.66986 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78b456d1-53b6-37e4-92ee-9ddb5830e92a | -12.08731 | -47.09948 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53e447f4-b505-31da-a604-7b935457d905 | -12.12048 | -47.05876 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73c6e410-645b-327e-b14e-732b5968717b | -10.43701 | -46.73132 | 2026-09-02 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7961aa3f-3719-3243-affb-429bb42a510f | -5.48472 | -57.15007 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60722dcc-3618-3289-bbc1-d38e62451835 | -8.45971 | -54.71078 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 6104c850-e651-30d4-96e9-fdfd3fd73bdf | -10.31152 | -50.04385 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d52eccdd-f4f3-39f4-8e4f-8dc793379e91 | -10.90743 | -45.32581 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| ddb18efe-472c-3d67-a190-f6c198ba7893 | -11.34087 | -50.6241 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbe8a61c-5b52-36fd-b8fd-0193cf247464 | -6.68057 | -58.75614 | 2026-09-02 04:57:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7c58c8e3-259f-3fa0-a3ca-f36b4954f65f | -9.72707 | -47.76619 | 2026-09-02 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f93e6fd7-adeb-3216-a9f5-6b973d156e7e | -10.3196 | -49.94424 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 171cee80-15b1-3378-b8d2-69aeb9c54021 | -12.12409 | -47.06313 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63ca65be-6adb-3ecf-a99f-8fdb0c6db7de | -12.37825 | -48.14758 | 2026-09-02 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4aa3146e-6961-31fe-bb50-552e1cf9de5f | -6.0902 | -53.80244 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca8d961a-8354-34fe-aac7-f1b9b915622e | -5.97932 | -55.70448 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2cd325a-803d-3bf0-aafb-d5b9a9b17065 | -8.43158 | -54.72333 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce22a187-abff-3046-a81f-bc36daae85c3 | -8.47919 | -54.70539 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 6f20b6ea-6265-36ac-b373-4c885ccb2292 | -11.23828 | -45.38766 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb3a98a7-c6ba-3622-a259-f7e4c50460a2 | -10.77759 | -44.74564 | 2026-09-02 04:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ab2a41bf-2941-3acf-a456-aec09bef6518 | -10.49825 | -59.60896 | 2026-09-02 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2d832a19-a4f8-3f05-be4a-b2b7155ef72f | -12.1272 | -47.10157 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08dfa5e3-8194-3d16-a1bc-2595e5300b6b | -10.78232 | -44.74629 | 2026-09-02 04:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd015ea8-9e62-326f-881d-9dc6772d63e0 | -7.20801 | -60.677 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed76cdf2-5cde-32fe-8052-76addcb2da1f | -12.09427 | -47.097 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0313209-9a15-32d0-a46d-be4502a988aa | -11.12613 | -51.5883 | 2026-09-02 04:57:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f67563b-627c-32bb-9fd1-2deb21daf09a | -8.44093 | -54.71197 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16db7bba-616b-3ed7-92ec-14039fb1c7c3 | -10.79765 | -44.74408 | 2026-09-02 04:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 373cd370-1afa-3dcc-9848-54415394bc27 | -12.07491 | -47.1277 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1100e711-78e2-3e31-84c5-364a16f97c28 | -9.21371 | -48.58145 | 2026-09-02 04:57:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c692e23-a8b3-314d-b023-bfc0adc3d5e4 | -10.96629 | -50.48944 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 242a0d86-d717-3edd-b588-d362a51208ac | -10.78566 | -44.75708 | 2026-09-02 04:57:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 40.2 |
| ec8e75cf-cf88-3dd0-afe1-e48c60f80e22 | -7.3388 | -60.58073 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abc937af-7769-36cd-8380-7efadf73e7df | -8.27028 | -54.95248 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48c4515b-82e4-3e1e-bb9b-f6b5574689f4 | -12.1385 | -47.14089 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a2955773-2836-396c-92a0-8c748753d898 | -10.90486 | -45.34452 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 9d5b415c-760e-3303-b543-7003801006a9 | -9.8722 | -64.97408 | 2026-09-02 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 590a285c-c6c6-353d-a5c6-708a4cce7234 | -7.19903 | -60.665 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5711154-feba-3bb6-8db5-583de283eb2a | -12.12873 | -47.09047 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59e73fe9-f4f7-3064-87df-271f75f1339f | -10.90288 | -45.32521 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6c05483-8b73-38fa-9f72-ddd1cff85511 | -11.66211 | -50.2008 | 2026-09-02 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d1f9b17-61ef-3702-b27d-4282905a3aef | -8.4576 | -54.72338 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 789b864e-7cc4-3d06-a26a-6aea1206cc21 | -8.56441 | -63.18707 | 2026-09-02 04:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9ea32f40-1652-3123-895c-c8f9ec8c199d | -11.68655 | -46.73433 | 2026-09-02 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c22ff6fe-90de-3807-a4c6-c47fb9255097 | -8.11292 | -54.95409 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| febb1f2a-e667-3ebc-be12-f7e1c3130adf | -8.283 | -54.91734 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94eeda85-1137-3775-81ee-7664fdbcac9c | -6.081 | -53.66309 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8424492-7d8a-3fc0-bf81-65143542387a | -8.89857 | -50.56852 | 2026-09-02 04:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 645ccdff-adec-3466-8433-713d989d53b0 | -10.06568 | -59.40179 | 2026-09-02 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 168903da-086a-3aa1-9a39-8955b6fd7f85 | -12.1467 | -47.14212 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9667fc95-8f1f-3fe5-bfc7-40c6418d6ba6 | -10.79025 | -44.76402 | 2026-09-02 04:57:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e8bddf5-92e8-3e53-9929-e2fe452fe165 | -7.55625 | -54.99864 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c9bb02e5-1690-301f-a34a-907e395cdfbb | -15.37904 | -47.68778 | 2026-09-02 04:59:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 98541d94-a608-3491-ab3d-3df4e0d234cb | -17.67325 | -40.13807 | 2026-09-02 04:59:00 | NPP-375D | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 0dbd81f9-0927-3cc5-b799-bfbb192c664a | -16.81502 | -43.91138 | 2026-09-02 04:59:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 411a28eb-4070-3b17-bc50-b56b6142a2ff | -14.97096 | -48.11995 | 2026-09-02 04:59:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ef6575c8-0843-306b-9b79-1c3008d15cad | -14.96191 | -48.1164 | 2026-09-02 04:59:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32440f22-7df1-33bd-8e83-7ff99ca18096 | -15.3479 | -47.04395 | 2026-09-02 04:59:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8ae35940-24fe-3c46-b250-415c662ae5e0 | -15.37442 | -47.69077 | 2026-09-02 04:59:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7ade5e01-5e7d-3273-ad3d-b05d094447a7 | -15.3703 | -47.69009 | 2026-09-02 04:59:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6628c47-0a92-30b9-8b1e-fa970013c5ef | -13.55805 | -59.74478 | 2026-09-02 04:59:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33b9b681-8484-3785-80cb-d01af241da17 | -16.13869 | -46.63698 | 2026-09-02 04:59:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 263dcb30-e0e4-3374-8e0f-1761a139d13f | -17.68018 | -40.13859 | 2026-09-02 04:59:00 | NPP-375D | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 42b523a8-f5d0-3195-a161-a52947b172b9 | -16.1561 | -46.64379 | 2026-09-02 04:59:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2a5d26ca-0269-37f3-8da7-9424dd1a9143 | -15.3657 | -47.04235 | 2026-09-02 04:59:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e2e8852-57e7-30c9-aa3c-86b86d977265 | -14.97496 | -48.12057 | 2026-09-02 04:59:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 87c96ad5-2f2d-38b2-8a72-0397c108b86e | -15.37954 | -47.68402 | 2026-09-02 04:59:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f71cede-30a9-38e3-8ed2-0f6087ce4f86 | -16.74413 | -47.03045 | 2026-09-02 04:59:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 309fcb4f-32c7-3ab0-86a7-187a15c4a409 | -15.50414 | -55.14311 | 2026-09-02 04:59:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README44.md)
