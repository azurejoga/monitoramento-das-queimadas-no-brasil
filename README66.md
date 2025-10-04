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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06d9b874-0b92-3d65-b837-3188e5d6f69d | -15.79021 | -43.68137 | 2025-10-04 04:14:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f58119e0-693a-391b-89e2-940fac9cd6bf | -13.10882 | -47.90546 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 556326f5-f2ac-3bad-bfec-dc954e962271 | -13.32326 | -47.79428 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bda2da10-39dc-3b6d-b4bd-0020026fc1f7 | -14.66425 | -48.29001 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b2258dd8-e89f-3213-9538-ca2b8a0432fe | -12.80821 | -46.85591 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c2d264bc-93fa-3309-915d-5d9e03773f79 | -9.92992 | -50.8959 | 2025-10-04 04:14:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a8ea55fb-c761-3a92-84ab-8bf0072d7e22 | -14.8726 | -48.36614 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9e46f2ad-fc76-34de-94e6-00f7e99831be | -12.04524 | -45.20068 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0141454-a427-3815-9f60-fc94647c72ad | -8.17783 | -44.14315 | 2025-10-04 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9212e883-6646-3014-a24e-f23d694072f3 | -14.22121 | -46.07962 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9ffbaecf-b3af-31d0-a2d5-b6bbda7104eb | -12.81518 | -46.85702 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 977f7f81-a4d2-37ce-8ca3-c450ecceeb7b | -13.31843 | -47.18436 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 609ffde1-e573-369c-8ed4-7e24fe657c3e | -13.48639 | -47.26281 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42f65a12-ff94-34c3-9025-3529c382897b | -7.29424 | -55.31935 | 2025-10-04 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d359b30a-dc72-3030-9e79-ffba25aac1ca | -13.27612 | -47.21893 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e92235e9-366e-385a-9171-a743af55d3e1 | -8.44866 | -45.6767 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 101522a2-6324-35a4-b178-58ed63796276 | -13.29668 | -47.5929 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 89e0e8ca-1656-3310-a056-a2a18e3dc3bb | -8.17839 | -44.13964 | 2025-10-04 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6dc928e6-674a-361a-b654-4b5296247287 | -11.47388 | -45.01516 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c34f22df-8c3d-3688-8b96-4a56923f44a0 | -11.09718 | -49.85493 | 2025-10-04 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b26c6c3-c668-3b91-99cd-2dadf1212dea | -10.59489 | -54.35638 | 2025-10-04 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 18eaf087-5e72-3278-996b-676c70126de1 | -13.10595 | -47.87856 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9a4aec2-0ac4-301d-8dca-f85ae1a0cc30 | -8.55489 | -48.65264 | 2025-10-04 04:14:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee855ee4-24a1-35a7-ba47-88b91d445b09 | -11.0486 | -47.79519 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc43ada6-71b2-3a87-9c63-084c4edbfc40 | -14.65053 | -48.23983 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 04d85485-0912-37a7-8a14-9f7d9c79d3f0 | -12.0782 | -45.16589 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08881d55-e958-352a-82f3-90597ba25b45 | -13.88773 | -46.51146 | 2025-10-04 04:14:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f299ba2e-fe14-3274-a032-14c58f83d810 | -15.32394 | -46.38017 | 2025-10-04 04:14:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| daa482b3-1289-3c78-8a64-713f10159a5a | -14.24143 | -46.09416 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 413cdde6-cb75-33e0-8106-0587b193fddc | -8.62759 | -43.986 | 2025-10-04 04:14:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 407d4d2d-b6b8-32e4-a6d3-37123db6c214 | -13.14363 | -47.943 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f73f272-eaa8-3d3a-9fee-f58ab43e1d47 | -11.04416 | -47.79879 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d74d873-7e4e-332c-8889-7ccd2e7d502e | -13.12546 | -47.83007 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9933f516-02ed-3a0d-a856-7d3417cf7c04 | -14.97645 | -46.84693 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| caf69bb2-ab7c-35cb-a72f-3258fba7890f | -13.29879 | -47.82208 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 106cefeb-e516-3008-aa91-2b3afb9b4a76 | -11.28061 | -47.80022 | 2025-10-04 04:14:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dbfffb38-1235-34a2-8495-f49231063f69 | -11.56144 | -47.67259 | 2025-10-04 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 961abb31-61e1-31a0-99b6-e7d2603ad57f | -14.92762 | -46.86626 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 113a22b3-9572-321c-9534-0730cc87bca8 | -11.7018 | -44.43701 | 2025-10-04 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ccaf12a-310a-36fb-bb90-efe584023c9f | -13.24065 | -48.49257 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d10e7a96-76e7-38f7-a29b-0a2ee41ed29a | -9.94952 | -50.24091 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b94f7ba0-8a4a-368a-b291-b50dc138ab9b | -7.55919 | -47.18725 | 2025-10-04 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62ce091e-0202-3f30-9e18-b5a35b4e9546 | -8.50512 | -44.66427 | 2025-10-04 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 014525b4-0807-301b-96e0-bd36c8bb9397 | -12.028 | -45.20148 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73cc3a8d-f62e-3a7d-9480-39eaa5913d56 | -9.90728 | -43.73454 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 711156b8-9a74-33c4-9521-79b8982a4e0b | -11.16903 | -47.75009 | 2025-10-04 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| f2abc211-e963-38c9-b94e-fef842335305 | -10.96913 | -49.57141 | 2025-10-04 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44a8b175-e1f9-3d7d-bf69-3f1672b15d8c | -13.23764 | -48.48768 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29f7f646-cbce-34be-a08d-14756c0d27c7 | -9.11668 | -44.39205 | 2025-10-04 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37586da1-b424-3842-9eab-8a8c6ffc36a2 | -11.4973 | -46.75082 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ce54983-7ecb-3734-b1d8-4dc0cba5d04d | -12.93517 | -46.37154 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fb7bcaf-b087-356b-9b9f-bbb02d97851a | -14.44294 | -46.11741 | 2025-10-04 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f8ce96b-a49b-383c-95e5-7a216911aac3 | -13.7454 | -51.30279 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20727642-b596-3f34-b082-75c0f2867e0e | -13.23321 | -46.43657 | 2025-10-04 04:14:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19befceb-40db-3528-a6b0-ce2a78eacc72 | -13.9732 | -48.18364 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 54a8584b-7562-3c62-9d37-5a01eb60c642 | -13.74466 | -47.94111 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68b27649-cca0-3ff7-b85d-3ee601b38ff7 | -11.46969 | -45.14235 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 131687f9-12d1-33c3-9198-2a24f9eefb2b | -12.90169 | -54.75719 | 2025-10-04 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5163477-040c-392e-9e84-91eabfe2d277 | -13.74245 | -47.95394 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4897da80-2cec-3032-96a1-1c5e8436dfd9 | -14.66787 | -48.29072 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d22016eb-b363-3a9a-80fb-bd1acbc81de7 | -12.70557 | -48.55306 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| efbcd5a1-9b43-3f22-a8c6-2dc8abdae6e3 | -14.45345 | -46.33839 | 2025-10-04 04:14:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5aac452c-0054-3b5a-9fa0-307c6525fbda | -9.94547 | -43.75074 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7dc2416a-faf1-3b70-a50e-0451b244094b | -14.65415 | -48.24048 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 82f501e6-eaed-3e09-970f-66a5ca69e741 | -13.76246 | -48.05513 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4110308-6cb0-3923-94e5-d9281fa966b0 | -12.71007 | -48.57228 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ac4ded0-4862-3651-b67c-00a4456b1004 | -15.25738 | -44.1254 | 2025-10-04 04:14:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1ed6f529-c6dd-330f-8e15-d64fcde72ad8 | -7.73984 | -46.30392 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8b3c15ca-5e65-306b-8530-08e18a7c52d4 | -7.72674 | -49.8554 | 2025-10-04 04:14:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9091b55b-5066-33a1-8abe-a5419eb04a11 | -13.98915 | -48.20045 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8dfa4322-01c6-3231-9fef-19313d3efc0c | -7.8837 | -47.35786 | 2025-10-04 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49c6cdad-a61c-33d7-8c08-a84c3a5b01ee | -10.32552 | -50.34171 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 65c2d81c-c456-352a-8930-2a249924a18a | -13.9659 | -48.18239 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| afa48773-e0d6-39b5-9608-b5d93f176a34 | -11.88849 | -44.99263 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51749c14-2200-3039-865f-d9a0cab83d62 | -8.61902 | -54.96922 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6aa0e444-a9c1-3dab-80ff-aefd2ab1c7a7 | -14.5994 | -46.72939 | 2025-10-04 04:14:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21dea024-2bca-3c00-8434-a7e79dfb9025 | -14.23189 | -46.07753 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e64b99d2-a057-3d83-a3db-3f31369c1dd5 | -15.18909 | -46.39083 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d341711-7d62-3a64-b6ce-6c000f51e278 | -8.22968 | -46.81109 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a06c083-662b-3766-80f0-688ae19e12be | -12.59106 | -49.88519 | 2025-10-04 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59c66c76-62b9-35d8-812c-0934f883164c | -8.61854 | -55.00447 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d487b19-ecac-3a24-9521-18ae0a44d5ae | -11.55521 | -46.99275 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7653e852-c97d-3f91-9210-f50a3247e3cb | -13.26625 | -47.21307 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| babb5735-136f-3c34-a6ff-dc7f2c498fc8 | -13.23082 | -47.82807 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50aa1e6e-b82c-332a-b8b9-75d531a332f9 | -12.03858 | -45.19957 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 34d0da51-b14e-3499-aebb-31ecfad716a1 | -11.50705 | -45.01693 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c42b20e-4afe-3ec9-bb50-e55f6ca83403 | -14.48114 | -46.70122 | 2025-10-04 04:14:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3842898-0f4a-32f1-b5cb-2c2a251e35ff | -13.70396 | -47.35067 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75d572f4-512e-3f97-ab67-53e0963c44b4 | -13.27131 | -46.4822 | 2025-10-04 04:14:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76267437-0cd5-3147-9e62-7ae0e33566ea | -8.96172 | -50.6982 | 2025-10-04 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 354b7290-5cac-3eb1-b2f9-383cfce172d6 | -11.68553 | -47.49248 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6dd6f781-6db1-36aa-a848-6c8a5bda8010 | -14.24297 | -46.1058 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0384a5ea-90a7-3bcb-bb29-9595f46e3266 | -13.11167 | -47.93251 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15941b8c-9031-32f6-818d-f5eec1fca68a | -14.67504 | -48.27098 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0b84fd3-3dce-38d2-b02a-42955f025757 | -9.91129 | -50.50375 | 2025-10-04 04:14:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d6121e6d-2a3d-32fc-ad3f-48606ee752c1 | -10.41934 | -50.67131 | 2025-10-04 04:14:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d52321a8-3359-3b38-b5a4-a27153e35c0d | -7.77084 | -46.27164 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dfa65ed6-52c3-356d-936b-6d608c3f00d4 | -14.88574 | -46.96963 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0dec66c4-d0a2-3c30-a544-4ece78489688 | -9.31705 | -54.528 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 237f215f-f017-3313-bcfc-f433172090c9 | -15.32256 | -46.30437 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README67.md)
