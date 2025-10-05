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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed8da371-752c-3904-9ba9-c21a7f3b28d7 | -12.97877 | -51.04203 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 666c8907-3607-3fa4-857a-bffa051f4f46 | -10.56667 | -48.71803 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 29ecbdd6-12e0-3a2e-82ce-c7531e78945e | -7.72514 | -42.38657 | 2025-10-05 04:46:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d224d878-bfb0-39bc-bb1e-6339e14989f0 | -7.02301 | -42.78392 | 2025-10-05 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 29b2c469-394e-3c24-8b7a-b7f9a8f99e99 | -13.3596 | -47.69439 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 593f76fd-e926-38be-9aa6-cd1bf846f889 | -10.4039 | -51.58899 | 2025-10-05 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07079788-323e-39f9-82e5-037eba2095a8 | -11.07058 | -47.77486 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4494fb8a-e67f-377d-971f-b30722719b51 | -7.036 | -42.76461 | 2025-10-05 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5c78fa98-dba6-33a3-8f77-cf9f687fb66b | -10.8287 | -47.98439 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 42286523-5a72-32b8-a833-ba29bd6b1280 | -9.80087 | -48.27563 | 2025-10-05 04:46:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5388028d-3049-373b-9075-d20535049a89 | -12.26487 | -55.11818 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6ad1d09-5646-3625-8269-5ff5317286c0 | -12.87156 | -47.2772 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 351608bc-8497-3147-9203-dd78aba0298e | -10.45966 | -57.50198 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f1071ad-c5b3-379f-a312-6883a4086907 | -13.30538 | -48.12395 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36cef56b-9aef-3d8e-b2c2-998b8799c056 | -6.71457 | -42.8344 | 2025-10-05 04:46:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7551a0ba-1626-39d4-8fed-288366fafe56 | -13.36946 | -48.06208 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 933496f6-8082-3b98-a21f-0c94f4bf8656 | -9.32515 | -54.52864 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cce06ad6-40ef-3766-81de-ef930a79fe00 | -7.27096 | -44.79161 | 2025-10-05 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce41bf6c-ad18-3092-abec-d006f22053ef | -12.89558 | -47.31418 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3fefe44d-0260-381e-b5e3-b9c778ac523e | -13.07974 | -47.89956 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6e48281-eac0-3a3a-a4da-fe6bca541ad5 | -8.59766 | -46.29939 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a2fb7454-da4a-3d80-81e0-d479165a2547 | -7.05551 | -42.77345 | 2025-10-05 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f277f8b6-9c17-3ee4-b1f2-4373b9aac901 | -8.5525 | -47.66391 | 2025-10-05 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a159185-2831-39fd-9673-68b5cb4a012d | -7.24482 | -44.88322 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da1d4bf2-9677-3c8a-a9bc-c5fd64d5d866 | -8.60121 | -46.2743 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b490e08f-2b71-3bd6-9f95-501dfd7e13bf | -9.32559 | -45.79103 | 2025-10-05 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e3c68f36-4b8c-3a6c-8dfe-09ef2971f52d | -9.9995 | -48.29732 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38b66ee1-adb5-3fa2-81cf-4e8113858dc6 | -11.77977 | -47.93554 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 28189d05-1d8e-3eb0-8b0b-47c0020c1fe4 | -10.10364 | -48.3278 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7cdfe777-c488-346f-b660-70f1327fcd29 | -6.71622 | -42.82246 | 2025-10-05 04:46:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b92ed7df-c2d9-3347-8b88-502052cf7103 | -10.35883 | -48.16259 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f2664c9a-909c-3b26-a735-ae3430931763 | -7.11185 | -45.09694 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e06f786-8382-36c7-9b20-e99495cccb60 | -11.52985 | -47.23977 | 2025-10-05 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6e1f7947-8d12-3a80-a853-4fc5c17354d9 | -12.30284 | -55.12866 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0796253c-fa46-3db8-81fd-b00424252135 | -13.3586 | -47.57982 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6cd8b984-096f-37a0-8344-015b37fe5239 | -13.15903 | -42.35538 | 2025-10-05 04:46:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e41eafc5-afcd-304b-884d-c7d85990bf93 | -11.93486 | -46.43716 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c8fbcd0-93ee-34ef-bde5-bfa1bde41360 | -13.10512 | -47.85991 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b53e21b3-06ac-3ed6-9d6d-69bf66ee0f48 | -11.82016 | -44.89476 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ce89f57-696a-38f1-baac-d93e8192c8e4 | -13.27681 | -47.59812 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9d1625b-5773-3137-8e88-8153ec906965 | -12.2344 | -43.77357 | 2025-10-05 04:46:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 419ab1de-eb9f-3057-b189-b1ab7ebfb883 | -8.62019 | -55.00177 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f34fef4a-d976-3bbb-9299-ea1d1e5684b4 | -11.11023 | -49.86581 | 2025-10-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f0db0da-0bc8-3c13-a16b-915c651a4cc0 | -13.26555 | -47.62112 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e25139e6-b524-3aba-835e-b26cb144954f | -11.10446 | -49.85703 | 2025-10-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ecee27d-1925-354e-a952-cbda39bf0808 | -13.33202 | -47.18612 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02176d83-667d-3c97-b3f7-a7b5d9b4e021 | -12.41317 | -51.09746 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cc87d21-850b-3077-9752-6a22f9e39401 | -8.86064 | -46.79131 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 451cdff9-d832-3105-a74b-b7b39bb9d5aa | -8.8737 | -46.72826 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| dc1f0b29-a9a9-359c-a70e-f7b0ab41a244 | -12.57897 | -54.77398 | 2025-10-05 04:46:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5076026d-29e1-31e8-8308-8071c85734ff | -12.59526 | -54.75618 | 2025-10-05 04:46:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ab88708-9024-353c-acbd-65a0284189fd | -9.99617 | -48.29906 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8516cd72-64d7-3666-81f4-67cd891f7c6a | -13.12592 | -43.84769 | 2025-10-05 04:46:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d643b7b6-9ff2-3b57-a76b-61eed0dcc477 | -11.13439 | -47.93094 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 34adb2d9-0298-3ca8-ae97-85a703b2bd50 | -5.62209 | -51.9359 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7da50ea-e23d-3265-8c56-ed55f8c08def | -8.6156 | -54.96124 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 508ae716-0ed0-3e04-9e2b-5205b38f7c7d | -13.1545 | -47.96647 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| acf39baa-bec8-30da-bf1d-1ceb8957dd73 | -11.23067 | -47.74137 | 2025-10-05 04:46:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eba34858-bd31-3193-89bb-d299a8706a38 | -13.95412 | -43.07008 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c3a94b84-0cee-3f4c-bf10-ebaf6e0ccf4d | -9.06156 | -47.012 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0cac7024-e2bf-3169-b9fa-c70c96ed9315 | -10.94518 | -47.08776 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7431fc02-b9a6-3d35-9ec5-11be643fa8fe | -12.92602 | -47.30354 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7df3fee9-f240-3aac-a969-5e34bb931890 | -8.2361 | -46.81305 | 2025-10-05 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d976f0c-a2d2-397f-8be6-3e308b17a270 | -11.271 | -56.44141 | 2025-10-05 04:46:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 424d491f-94b0-3eed-a90b-76d88400bc76 | -13.49084 | -47.27427 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8cd58caf-763c-3f8a-81b1-389c3a13ff5b | -13.1712 | -50.87505 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ea6a248-2338-33a8-9dc3-7a9fb17539ca | -12.12902 | -49.43032 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af6e16e0-7caf-302a-a2bb-716386f2131d | -11.0035 | -46.51822 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 03e8b9ef-1d15-37b9-b539-2493fcb867b7 | -13.09845 | -47.85202 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9107664f-3753-322d-b8d1-25eb83865840 | -8.58032 | -46.33388 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 68260f34-e946-3c14-abf1-e3ca03db8335 | -13.25504 | -47.20492 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db807133-110d-3d35-8f6e-d959b9c98f4d | -13.30628 | -48.08833 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bc28cf18-7f1a-318a-8241-108445a6e0ea | -7.31958 | -45.9862 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4a39e54-411b-35cb-a042-54f97ca9ebdd | -7.1177 | -44.17029 | 2025-10-05 04:46:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a024b4a0-e5a2-39b3-9382-b08b062eb67a | -8.90014 | -46.68589 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c6840048-283a-39ed-9054-757241eb7cb8 | -11.50195 | -54.45724 | 2025-10-05 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 746933fd-5460-3493-9896-b8ca5b025836 | -9.29141 | -46.00579 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9f1f7574-65b9-3d90-9d1b-ee466977d662 | -6.72589 | -46.06098 | 2025-10-05 04:46:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f533b30-3ad6-3262-9481-3bdf0264d230 | -11.24446 | -47.78271 | 2025-10-05 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 00edcfd4-5463-3a54-a06b-db4ffb94298a | -12.22721 | -47.83481 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5343ac94-6706-3f02-9be8-6c8b83947108 | -10.62458 | -43.31077 | 2025-10-05 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 48176bb3-3dbb-3be9-8349-f1eb88a2b9cf | -13.25169 | -47.2296 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8654bea0-e050-3dc3-925a-d221aac5cdb4 | -8.60172 | -46.27074 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8b0532ed-fc32-39ef-a51d-e3c63fc0bf21 | -9.80028 | -48.27968 | 2025-10-05 04:46:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e346957-319b-3c2e-9ca0-be6eb2fcca8c | -13.00027 | -44.00008 | 2025-10-05 04:46:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46a869de-bbe5-313b-880b-16a4ad219408 | -9.81492 | -47.87548 | 2025-10-05 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9400e4c0-5ef9-3fec-a231-4cafe423e489 | -12.98034 | -51.00832 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4f124ca-d45a-347a-a417-5707e753d008 | -10.64521 | -49.16434 | 2025-10-05 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bfbb87b5-d7c2-3c4d-8ec5-91154028c047 | -8.23363 | -46.80252 | 2025-10-05 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f86e4c2b-1bac-3b2f-beaf-6411661090d7 | -9.84974 | -60.05585 | 2025-10-05 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 351cd20b-02f4-37ed-a2b5-761fe6fb6f71 | -8.62454 | -54.99804 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2384ffd-3b17-3476-9c25-2f7a2000b68b | -9.04515 | -47.01468 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9eec9d64-b8f7-3b8c-8854-7c0fba37bf3e | -7.02769 | -42.78757 | 2025-10-05 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| be97caea-8904-3bd2-b6af-3824d007531f | -11.11463 | -47.17418 | 2025-10-05 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b30cd1d1-799f-3161-b23c-bc2a52a24022 | -7.29298 | -39.26567 | 2025-10-05 04:46:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4246cb5e-d1a0-32f9-9c7a-4a438c321fdc | -8.95507 | -48.75104 | 2025-10-05 04:46:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a013af0-18a5-3a3d-ae46-582ffa2cbe59 | -7.51342 | -41.27641 | 2025-10-05 04:46:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| d97dbeed-8dfa-30a0-a3cf-1e2d7b10bd69 | -9.26449 | -51.80539 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5278af76-8ce6-3019-8796-54ba654f6a17 | -12.43029 | -54.50051 | 2025-10-05 04:46:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a80ae60-ac87-3497-bf46-cbc1b92edebf | -8.50414 | -54.59492 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README89.md)
