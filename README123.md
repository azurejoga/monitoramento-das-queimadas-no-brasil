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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ebdda8b-73ca-3078-a8c2-fb8e232a3dbe | -13.37589 | -47.29514 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ffb25ef6-48d2-3faa-adf5-0b7b04a58376 | -14.92363 | -47.22398 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 58b01190-94f6-32bd-a295-63d45c52ec81 | -11.92453 | -47.8858 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0494dafe-1422-386b-bf84-25e4ee100eab | -12.1461 | -46.6744 | 2025-10-02 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee9064e6-4656-364f-9fa8-eb364b1326c4 | -9.92623 | -43.72966 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 14e28b49-2aa2-3f26-9965-c0a836a9ec75 | -10.81813 | -47.96741 | 2025-10-02 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8133e322-5ae4-3749-8994-0cd26fbd8496 | -11.81734 | -45.02955 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef5ad8ad-3c64-3879-b046-99d291126053 | -10.85603 | -45.41216 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe58edee-dac4-3484-a96f-6f501e18dd17 | -10.82737 | -46.62342 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b78188f-be87-3dcd-88a4-d6fde399a689 | -16.04363 | -50.85965 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 57c5acf0-b118-3880-aa30-f439b26e1415 | -13.00351 | -45.23006 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| adb5ddb1-fb8b-3caa-8ebc-8949646b2d3b | -13.30753 | -47.84357 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b74675e7-05d0-37cb-9a82-82f66361f84b | -11.16686 | -47.27078 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 794722c7-de0a-3c1d-9bc4-51ec0c72b792 | -12.74982 | -46.90923 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 21f31eeb-d225-3e92-84e7-60d7572d952c | -14.65411 | -48.26277 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10b8fbbd-dccb-389d-bfc3-e3b8db990405 | -15.5514 | -48.18085 | 2025-10-02 04:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d1c2bff-42f8-32dd-a238-93416e957408 | -15.93511 | -46.24273 | 2025-10-02 04:51:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2bd11c78-1ddb-30f3-a509-8796f4b11618 | -12.70113 | -48.58079 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 0e9ec9a4-138d-38e1-8de6-8b04cd7107d2 | -9.95321 | -48.78487 | 2025-10-02 04:51:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb6bd686-3ea7-3a8c-8725-27621f9bed23 | -12.69338 | -48.55437 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eaa99e2c-a094-3eb9-9c41-f63018b37f68 | -11.21505 | -48.21164 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13356eeb-23b2-3898-8232-4b8dbf5f42e3 | -13.46078 | -47.25659 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 943e3331-5947-35cb-993e-05221312dcbd | -15.34951 | -46.29067 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6de8bdb0-87be-32ed-849a-d56406d0e47d | -11.08885 | -47.85258 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27f072fc-2d85-385f-969a-83d38f733fee | -13.16181 | -47.83247 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15b760d9-4426-3867-a8b5-27f544162b17 | -13.31517 | -47.8196 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 59d5c84c-a9aa-3ad8-b969-5647a5f8e0a8 | -9.16391 | -50.83967 | 2025-10-02 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05d0e228-4b30-3619-8634-6b801ec29a19 | -14.60971 | -48.23334 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 819053e7-293b-3674-bf61-2dff3b5311d8 | -10.82344 | -46.61803 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc6f6121-b90f-346b-8a21-8ff3c61ebdb6 | -13.32175 | -47.2152 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9ff3f323-e74a-33fe-af7a-2785af0b4a45 | -15.93596 | -43.3476 | 2025-10-02 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 623be828-963b-3707-b893-ccbf87f327c3 | -11.61995 | -52.24861 | 2025-10-02 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfc4964e-176f-3e7f-8b65-ba80553610d1 | -11.67853 | -45.32074 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff3828b4-f120-39a4-a629-cec421a46597 | -11.57661 | -47.02453 | 2025-10-02 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e2b377c4-6134-39c9-a009-d829d4a18acc | -15.27388 | -56.79727 | 2025-10-02 04:51:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f60db12b-709a-304a-b5b7-ba439d2dd778 | -11.99649 | -46.57595 | 2025-10-02 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2cb179e-fae9-3a01-b6e1-8990dbdd5d1d | -11.61888 | -45.03322 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c88c6aee-e70f-3fbb-961d-bac8be23124c | -11.82213 | -45.03312 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 4070225a-e5ae-35b4-9e88-6950a239e9bf | -12.81003 | -47.01781 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ef6c0f1b-4f0e-3200-9bb1-19d2cfa6a3a6 | -12.70569 | -48.57796 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 5447ca04-4830-307b-b8a5-80fc830f6fae | -12.15073 | -46.67503 | 2025-10-02 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46f65593-7ffe-34c6-9b1a-d35a3274358e | -11.81893 | -47.68063 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca9ba582-bcb1-3e0b-a7ef-ab9ffffd940e | -13.69457 | -48.61835 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41e3df31-e04d-3f98-a56b-718b25624434 | -15.13845 | -46.44638 | 2025-10-02 04:51:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7b4be4f6-eaef-3d58-add9-11ec1fc65355 | -15.34447 | -46.29057 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| be2edabf-ca86-3e86-b6ba-e7c1d2a6a06c | -13.01504 | -45.22192 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8219a533-31b6-396c-a7bd-8f9083fbf096 | -9.4477 | -50.90385 | 2025-10-02 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fcf5484b-95a6-3283-b5e7-30b7db5e403c | -14.4249 | -46.10948 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f17d25c2-70ef-36c8-8680-bc251110eb43 | -14.21098 | -46.12081 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 54af239d-d582-3335-919a-fc056a75d801 | -12.85355 | -46.93777 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19ec4ebc-dfea-3d87-a594-e413c81f444d | -10.16709 | -45.45654 | 2025-10-02 04:51:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b74ffca7-7b19-3183-aa94-34f4889261f2 | -13.78445 | -48.00201 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b306256-67f4-36c9-8599-87d9c9a98937 | -13.63735 | -47.65455 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d601de3c-d028-300a-a0c2-d644e3361b72 | -12.11963 | -43.43422 | 2025-10-02 04:51:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ae0d51b-7ee8-38bf-b72d-e90e6205e143 | -11.45009 | -44.96851 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 429a6f3f-c0ee-3eba-9948-efeb9cfbcbcb | -13.0809 | -47.09016 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00afb797-d171-3c49-8b83-36c3f33eae95 | -14.41216 | -46.09818 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 15264e64-b2d1-3a79-94d8-46264c4023c8 | -12.88638 | -46.93689 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 84b981e9-a3f2-371b-a086-f3c3683f799b | -9.94143 | -43.70251 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4895c13-c8d5-34b9-a8de-a46b9bac0cc9 | -12.50627 | -50.24998 | 2025-10-02 04:51:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 166728b5-7f96-36d3-90e9-d63e8a72eba8 | -14.36682 | -45.96441 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da6ecf5b-f14b-32c0-a256-e21adc1848e9 | -11.05587 | -47.80984 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf99df5a-2d44-36d9-af55-f568628587fa | -12.76073 | -50.5571 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 32eff280-c6e9-3987-8016-dfd28d811886 | -9.44971 | -50.90064 | 2025-10-02 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1f778a81-9ada-3020-b747-be038114d63e | -15.24594 | -48.08551 | 2025-10-02 04:51:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 421d6bc4-9238-3655-8223-942f3b61e524 | -12.94439 | -48.43389 | 2025-10-02 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 30f2d67a-7133-359f-a085-4430849894d6 | -12.05721 | -48.77562 | 2025-10-02 04:51:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 611231b8-8014-3fd4-a232-c8b288ce0ec8 | -9.92812 | -43.71561 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| af968bf0-3fe7-370d-9311-dd095399784d | -11.85381 | -44.99036 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2bb81dcd-d07f-3065-b12e-cc829d96b701 | -10.24402 | -50.30745 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b374aba9-66e3-35aa-abdc-341d7c24a576 | -10.70673 | -48.57956 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e816c3a8-c742-3ffc-b887-35f01a9f7e00 | -13.3047 | -47.19665 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0825d06-331c-3564-8812-cbab8bb02561 | -11.21453 | -48.21535 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b833a12-5f19-3683-a504-8fd73f57eab6 | -11.82517 | -48.07706 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09fb85e9-6f62-3925-9816-295edcef661a | -13.46843 | -47.23312 | 2025-10-02 04:51:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3db6939c-b51e-3bc1-8f3c-765a6d689207 | -10.19186 | -50.27505 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e0be6ae2-179b-3839-b48d-0564c970181c | -9.49336 | -63.13177 | 2025-10-02 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26d70104-afa0-3c35-96cb-5618b9005b56 | -12.9211 | -54.7332 | 2025-10-02 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 982c9f14-6124-3e3c-91e8-de3e6e119c43 | -13.51241 | -48.205 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e45c4d35-b3c1-3c55-b012-1b1329bac1d3 | -10.81888 | -46.61735 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 79dba7ba-77a0-3002-90e7-5db1534df089 | -14.87453 | -48.28852 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77ee64d6-2da1-33c2-968a-846e113a329e | -15.25568 | -49.27232 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d77ebdf-a3bc-3629-ad6b-ebe2831abc08 | -14.82168 | -51.40304 | 2025-10-02 04:51:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9caacaf3-ebd8-3b92-ae76-ebb642ca619b | -9.9433 | -43.73159 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 822ee205-5823-396a-b4c0-7899324dde82 | -11.60316 | -47.22781 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 13292316-81db-34a0-9279-38658f7c0c5a | -10.22195 | -48.2205 | 2025-10-02 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d7daa18-8a00-3d2b-a504-e870af7d3cf8 | -13.57437 | -47.59021 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b6b9547-aa31-3687-af22-16a8bf100e7d | -15.14785 | -48.0158 | 2025-10-02 04:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf5cba16-3300-3fef-a046-beeb2fafb28d | -11.83738 | -44.95409 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48852c8c-937e-3691-be18-5c961aa5ff67 | -12.02298 | -49.71317 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 558ab57c-4eee-3197-97de-9f2ae45e71cf | -12.26529 | -47.80896 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7272faae-1e7e-39d9-bf20-fc45a0c228cb | -15.25734 | -49.29079 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2eb59cfa-9ee1-3988-987f-53b6bb39e6aa | -15.10721 | -48.37043 | 2025-10-02 04:51:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f698204-c8c2-3d9b-a756-ed209c1acb29 | -14.02769 | -47.98856 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a91d64e8-61db-3098-99d3-1a0afafedf73 | -13.94733 | -48.13243 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c535c6a0-6455-3bde-bdc8-dfdf6ca8fc14 | -11.86383 | -44.99425 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7937bcd-e558-34fd-9f47-409dfac9077f | -13.3127 | -46.99518 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d556af27-721e-3aab-8221-c55b5b95cc1e | -11.42609 | -43.49578 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84c4eb1d-c93d-3baa-b59d-d91a4e3ae65c | -12.81824 | -47.03107 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b2a07988-7bcc-3f66-a485-1d1fbc1451d2 | -11.86359 | -48.0149 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README124.md)
