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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7472b206-911f-3515-92ef-860fb1ecff43 | -10.65096 | -54.1455 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e2217c78-8944-3db7-bb2f-68bfca2e4d35 | -13.58256 | -47.88924 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 068f751a-8916-30ff-9740-e5908dac5f73 | -15.54782 | -48.78822 | 2026-09-14 04:34:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c4d7695-4bf9-303d-b78e-6b46dc83dc5f | -17.93488 | -44.25582 | 2026-09-14 04:34:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0bcfb787-d928-338a-9751-77a7f796bd64 | -13.32409 | -51.72171 | 2026-09-14 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f48f772-de77-3bea-a378-e6c2b82cf2ea | -10.64861 | -50.57669 | 2026-09-14 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1eac362-3a79-3ec0-af72-434d9030e8ba | -10.4355 | -48.66062 | 2026-09-14 04:34:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 606ae1e2-d47c-3238-880f-a2e363ce0822 | -10.68635 | -54.16826 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 77e82981-f264-35b2-8ea0-3a84572900b5 | -15.07021 | -48.55363 | 2026-09-14 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 327b4238-28d3-375a-b63d-25db0a61a9ef | -13.57136 | -51.46152 | 2026-09-14 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebb4e3a0-f311-3fa2-b471-9b18148ab8f8 | -10.65204 | -54.13964 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a7d822ce-0437-3176-8adb-30c3f924bcee | -10.69586 | -54.17334 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3075a97-268c-3831-a937-5d694b3bf752 | -10.96421 | -49.7033 | 2026-09-14 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 695440bd-0dcc-3128-bd6f-fcc3fdb3677e | -10.67217 | -54.1438 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ca88075c-4394-3a9b-90fc-76938de22e9c | -15.78318 | -42.15827 | 2026-09-14 04:34:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8d53459-1353-3393-936c-6de030446e43 | -11.42771 | -45.14019 | 2026-09-14 04:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4698ea41-84d3-3f53-8ee2-078157535957 | -10.67326 | -54.13787 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e4a7189-3555-353a-bc5e-982baaf849de | -10.36067 | -46.65253 | 2026-09-14 04:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0f6354b-8309-3f8a-bf95-41cfb207a500 | -11.2304 | -46.42892 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 687de0bf-3d14-3136-9ec5-d7cfc4c3492a | -14.18703 | -47.40041 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f4a1eeea-7dcd-3306-ac57-619f939b79ea | -14.17231 | -47.42749 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aff52490-d1c6-37c2-8418-8e626c035d64 | -14.62031 | -42.52861 | 2026-09-14 04:34:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1d66fea2-d4bc-3736-bcf7-1c96fff67b8f | -11.17768 | -42.79739 | 2026-09-14 04:34:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 58794037-dab4-3846-b6c3-a56e3bf1e62f | -10.68299 | -54.17041 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0be53f79-9f92-3f3d-82be-aa31f0707772 | -11.17831 | -42.79323 | 2026-09-14 04:34:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 76f105ff-1471-35f0-96cd-0bcacba8af9f | -11.19361 | -42.79839 | 2026-09-14 04:34:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| de268f81-6e7d-3aa5-97f2-ddf5347b687a | -14.81418 | -48.1574 | 2026-09-14 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 147a0e1d-9b13-380c-beb7-8abdfb4c9db5 | -13.30567 | -51.31613 | 2026-09-14 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60f652ce-4c2a-3c4e-8472-0f6f3f8c3563 | -13.31655 | -51.71652 | 2026-09-14 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74e376d2-7efa-32a1-b45e-617630fe3d14 | -10.67061 | -54.16844 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 791eeeb3-ae84-39ae-8935-c6cb87012890 | -10.54829 | -51.30427 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53cc8368-f9d2-320c-9725-585a24d790e4 | -10.70646 | -47.52751 | 2026-09-14 04:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66184b55-8984-3027-a97f-82095ea3da62 | -10.55276 | -51.32769 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50b6cbe4-1c0f-30ca-b05b-c535f78e94c0 | -14.18395 | -47.44058 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 340d16e7-1c36-3c1b-a52a-bb2d712d5936 | -14.91604 | -44.67118 | 2026-09-14 04:34:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d452300f-053e-3c2f-bb1c-593a256bc215 | -10.68129 | -54.16735 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0a7cc93f-4f58-31d7-af92-01bb66bc0ba2 | -13.5924 | -47.87181 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 953789db-5cf0-34ec-82e4-2ea808d099e4 | -10.67397 | -54.16256 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| a4909342-47e8-3de7-92ee-3ee7b1b8d194 | -14.91202 | -44.6745 | 2026-09-14 04:34:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae467f86-7fa3-396a-96c7-8d202701e2ea | -13.7837 | -48.80986 | 2026-09-14 04:34:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59b50a60-efff-358d-93a7-1457ca8bed3a | -10.68117 | -54.15171 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| e84110c7-840d-30a8-b7c4-9d3cc0fef7b5 | -11.42158 | -45.13556 | 2026-09-14 04:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 121328d9-0c87-3c88-8531-5f1279d6b36c | -10.46385 | -51.24507 | 2026-09-14 04:34:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e066abb-5f76-392a-a27a-a69d6f7d9673 | -10.65941 | -54.15638 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f2e4703d-a599-3e8f-8c99-902419257f0c | -10.67626 | -54.13887 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a54c2c58-fb54-331f-ae46-662e284f636c | -10.66784 | -54.16748 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 1a7f63be-85e7-36b9-a198-26da6acfae46 | -11.78462 | -46.39277 | 2026-09-14 04:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6b003834-af98-365e-adff-48422b31df36 | -10.8076 | -58.57699 | 2026-09-14 04:34:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 386490ae-e695-36d7-b600-9aa24210a573 | -17.36979 | -42.62351 | 2026-09-14 04:34:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 71975603-b279-3485-9ddd-3c7708660384 | -10.6796 | -54.14874 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dca57faf-2cee-38a7-87b9-9557e0cd5663 | -10.23761 | -50.90388 | 2026-09-14 04:34:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e7a2cb0-78a8-3e53-9806-aefdf4e62336 | -16.45408 | -48.72524 | 2026-09-14 04:34:00 | NPP-375D | GAMELEIRA DE GOIÁS | GOIÁS | Brasil | 5208152 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41315935-de2c-3889-9f72-749195984f2e | -14.19038 | -47.40098 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3546744a-e92f-36b6-8eb4-9c0e961a1aa3 | -10.77183 | -48.97251 | 2026-09-14 04:34:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb83e25e-7d5f-3bb3-a3c6-7545d9385b21 | -10.67505 | -54.15662 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 4ece846a-5df5-36e8-823b-455669174394 | -13.62204 | -47.90388 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ea06422-f294-34f4-b9f2-10ca5b1ae0b5 | -10.94711 | -48.36295 | 2026-09-14 04:34:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 69bc473a-7e36-3fec-8f92-b8c1261790c0 | -10.68805 | -54.15933 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cdf43510-8b1a-35b0-ab0d-f6e9de4d6c0d | -9.71854 | -50.85137 | 2026-09-14 04:34:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0aabf8da-ad7a-371e-9df2-00fbcb0c0abf | -13.59155 | -47.89824 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 363219e6-e5ad-3d54-a2fb-9f6a5aeaba08 | -10.56805 | -51.33894 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ce5aa1e1-1f49-3705-a95a-47b0ccdd7416 | -11.22154 | -46.42017 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f45dad2e-3dc9-3e0d-b325-ac294b03b232 | -10.66049 | -54.1505 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| bc1618d2-9133-3300-9160-b8e8e13e90b9 | -10.17667 | -48.06696 | 2026-09-14 04:34:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 35440c77-7de4-3b83-b339-f31ac9fc28ea | -15.08691 | -48.32755 | 2026-09-14 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2d8f5b2-03e2-3d90-8e25-0f68dbd3ce24 | -11.34239 | -46.7799 | 2026-09-14 04:34:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e780a533-5646-3fd7-bcbb-d3dd87b362ef | -14.84378 | -48.14701 | 2026-09-14 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cb37038d-92c0-365a-bf11-9042e0e0ccc9 | -10.06707 | -48.76587 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cc6ad88-9866-37cc-b6a4-2bcc30eabfb2 | -10.06423 | -48.78278 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 438e9f3f-c788-38b1-8c3d-22c1b33008f6 | -13.43874 | -48.4787 | 2026-09-14 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c25c3328-e86f-3f3a-b331-db26639bcfde | -14.19357 | -47.42372 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 588131c3-d11f-3115-b121-f6c2a1289394 | -14.8731 | -49.95075 | 2026-09-14 04:34:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc88f56a-c2cd-3f11-8c99-be7ec690391a | -10.06345 | -48.76522 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d131028a-76ac-3906-ab12-32be28c83bb7 | -10.9807 | -51.42897 | 2026-09-14 04:34:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a1c0052b-c844-38cb-9556-f52bb1c06d83 | -15.54718 | -48.79201 | 2026-09-14 04:34:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4eb93089-67f3-3437-b6f5-e51b6cd57cf8 | -10.06786 | -48.7834 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7aa264d-93e7-35bf-b3bf-50a6028960eb | -11.25899 | -54.13334 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8a0c9eb-66eb-3361-9413-29ee98013a43 | -9.71789 | -50.85509 | 2026-09-14 04:34:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55715d26-4714-3392-a451-872e3f620ac7 | -13.62644 | -47.9004 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ebe57370-f080-37fc-bb96-0c2a7caba9ea | -10.4391 | -48.66117 | 2026-09-14 04:34:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f77d447f-45a3-3d3b-a973-b135393ab170 | -14.61649 | -42.5282 | 2026-09-14 04:34:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bbe6bfcd-b33e-3392-a5c0-a52256e5abd0 | -11.78015 | -46.39931 | 2026-09-14 04:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7ab21530-e128-3a91-9ed7-81736430a12e | -10.2417 | -50.90464 | 2026-09-14 04:34:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d335e3d-3e2d-31d2-80b8-4f0ad6c9a936 | -10.67569 | -54.14183 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba57227d-0b9a-3e04-a6ae-501074bc5b85 | -12.8148 | -38.41519 | 2026-09-14 04:34:00 | NPP-375D | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8468737a-18fd-39b8-881c-245e118070bd | -14.17758 | -47.39507 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d140718c-b10e-347f-b59f-5f5c835d028f | -11.17982 | -42.79199 | 2026-09-14 04:34:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 83cf99a2-252f-3f22-b059-3fcd5f54bec9 | -10.68278 | -54.14291 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01367e29-73d9-3140-ae2f-224526c58fb4 | -9.71507 | -50.8469 | 2026-09-14 04:34:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 378c1b0a-f09f-3f2b-99aa-472ae739fd54 | -10.10021 | -48.85849 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0068af3d-4567-3d5c-b83e-ba9389da7ca3 | -9.69316 | -54.3438 | 2026-09-14 04:34:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0803969f-d0ca-3968-8d9c-c3b164c26ad4 | -14.17798 | -47.41379 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af81f28d-c30a-3172-8684-9837b9279d8f | -10.68245 | -54.17341 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f8c205b4-3a15-30e3-a901-f386d4b9d6f0 | -9.79432 | -55.30969 | 2026-09-14 04:34:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5423ed9d-64ea-38cc-abbb-e74279b0b08c | -10.2706 | -48.34919 | 2026-09-14 04:34:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3713f73-111e-3ed9-9a46-390920e19f6c | -10.44271 | -48.66169 | 2026-09-14 04:34:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dacb635a-46a5-3894-be9d-cc846deda60c | -13.58753 | -47.90151 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4e33cd56-a895-384d-a141-b19f68ba4356 | -10.67109 | -54.14971 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 7349712d-660e-3cda-a9eb-c864b2a97b3b | -10.66157 | -54.14467 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 8c204037-4884-3436-a07d-ce1c9b153c5b | -10.6772 | -54.14486 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |


[Clique aqui para ver as próximas entradas](README32.md)
