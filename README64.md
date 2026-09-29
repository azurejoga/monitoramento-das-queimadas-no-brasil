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
| d8aef13a-6926-3c97-8d00-e326ebe9f360 | -11.9363 | -50.9146 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e974bcf-8f42-39ed-b821-b1018a3b5445 | -9.67225 | -45.55661 | 2026-09-29 05:12:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 355c1fcc-a73e-3767-8957-a853ffd7edd3 | -12.74107 | -47.27945 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f97ff1ce-159b-352d-842a-9620c09d735c | -12.63188 | -47.25723 | 2026-09-29 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15b591d1-9697-31e8-8229-b609599d6aaa | -11.17032 | -44.79741 | 2026-09-29 05:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| c1b9b953-4d39-3019-84f2-2bef96ea5181 | -13.16753 | -48.56128 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 013d6c8c-7510-32ab-80bf-83685568a94e | -11.4759 | -49.73571 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7754987b-d0d0-3501-b95a-353d420e80f8 | -12.55661 | -47.16402 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0232c42a-3657-3a96-8456-476473d8a030 | -14.08483 | -46.31622 | 2026-09-29 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53aef0e7-b18e-35cb-8e27-6c44f3e93aad | -9.69492 | -58.11547 | 2026-09-29 05:12:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c354d0de-1850-3b2c-b965-bd8448fb1f69 | -11.42183 | -43.47302 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ddbe1a89-82ae-33ad-a6eb-568242dcdecd | -11.4141 | -43.4581 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b8c24fa9-9de6-30d3-890e-a2d419b8a58b | -7.5072 | -55.02769 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3773f4db-b8f1-372f-9ce1-515bf5fe6d87 | -12.04461 | -50.94105 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 98a677ed-f23d-3810-9eb1-a7c68ee65dc4 | -9.95953 | -50.16255 | 2026-09-29 05:12:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37eba71d-6975-3833-9028-2da3b834dadc | -13.19893 | -48.56527 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b44b1bc-abbf-3586-8b6d-1fbb0b775782 | -11.33301 | -54.11682 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d630d9d4-9b5e-357c-9b45-6768f76daa4a | -7.56139 | -55.0326 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2a5987ed-bca5-34b5-96f4-4a5ca19ac5d5 | -13.20938 | -48.56675 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4301a591-26c1-33e5-9a22-4057a250a920 | -11.41014 | -43.45098 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7a60c134-5e17-310a-b529-cb80c1cec67f | -11.39052 | -47.45887 | 2026-09-29 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e209a573-7449-39b2-9153-38061469e13a | -12.7364 | -47.27069 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 12c0b6ce-bd79-3b1b-9cf0-b0e508d82b34 | -11.38743 | -43.46213 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c116fc8e-8003-3b38-b116-0e8a0f747cab | -12.94656 | -46.64505 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d53c693e-2ed4-322b-b0df-81b9bb8fc549 | -12.80095 | -54.00717 | 2026-09-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57d75f13-0d82-37d4-a7c8-89fd7ee54e99 | -11.86271 | -47.08281 | 2026-09-29 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96da1c9f-aca6-3bdf-a6be-71df5c816c6f | -12.61158 | -47.28225 | 2026-09-29 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da1071e2-4b18-319a-a4b2-2bf1c882b0b3 | -8.29126 | -54.71501 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 17b39faf-98c3-3347-bbaf-4997da513924 | -12.02096 | -50.95087 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cb20a0e-9b02-30a7-b331-ee5877afac5e | -9.07249 | -49.87724 | 2026-09-29 05:12:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47b93af0-83d3-3c74-a712-32532a42480c | -12.59982 | -47.28459 | 2026-09-29 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c863bed-f1a6-3e52-a953-c7486d867cb8 | -14.07822 | -46.31989 | 2026-09-29 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba71416e-d9e9-3280-8a26-43805fb0a9b4 | -12.00874 | -50.97533 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99d083b9-a79c-3631-abb0-c5e60abf5fb3 | -12.70205 | -46.9763 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f19eff66-966a-3bc2-af63-bc67607020e0 | -13.5578 | -48.94478 | 2026-09-29 05:12:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2012f8e4-8cec-36a2-b542-9e3f635ca999 | -11.00796 | -54.14319 | 2026-09-29 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aaafdf5e-f50e-3d0c-982b-e6184700d937 | -11.98653 | -50.94167 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dfbec026-a984-3496-825d-6c56b3556248 | -12.71773 | -46.99234 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 03cf42ab-b01c-37e0-8b3f-32c3445b3e99 | -13.5302 | -46.9047 | 2026-09-29 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59387478-97aa-3d3c-9cb8-4931f36e505e | -14.1121 | -46.29454 | 2026-09-29 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 02488691-b93e-3bc6-a31a-d65d3a294b74 | -11.41563 | -43.44426 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eb3b6c05-044a-338d-875f-bcf9d2b8240f | -12.73079 | -47.26953 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fd50e493-8f00-3b92-8a6a-cd8d132754fd | -11.18595 | -44.8323 | 2026-09-29 05:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 26fd55ba-1226-382f-bea7-f18cefe452a0 | -14.12533 | -46.28899 | 2026-09-29 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cc2feb4c-7d80-342a-bdb1-b289b206c6c1 | -12.78013 | -54.02191 | 2026-09-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e695f32b-022f-3e52-98a7-e91354502755 | -11.5036 | -47.40751 | 2026-09-29 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2be84da-0ead-3a1f-82d4-59f01e30327f | -12.74028 | -47.31165 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5dddc46b-5006-3cc4-a615-6cf849084323 | -12.68852 | -47.38142 | 2026-09-29 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9660c04-767b-3e14-835d-27f4d4c952bd | -12.69717 | -46.96796 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 193bb409-a052-35c8-a842-9a13993347c5 | -7.50385 | -55.02717 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e51d3ad-3729-3ffc-a1ab-0b9f7bfd6a9d | -12.05434 | -50.21894 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3a8b082-dc5a-374e-afcc-b818c56b9f52 | -12.38942 | -50.22736 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 500b7a1f-4371-3457-883b-c1a5837b6cf4 | -9.7865 | -48.22523 | 2026-09-29 05:12:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72083d07-1dd9-30f9-b98c-5b50409e7a6a | -11.36492 | -54.04959 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f3a6a49-ea40-32d9-a13f-fb169d051e59 | -10.81882 | -48.74621 | 2026-09-29 05:12:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fae2ab1f-cf20-3e46-8d47-3ca3baf88b00 | -11.18996 | -45.14357 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 339f2f41-3a2d-3580-8bfd-94cfb4496bf0 | -7.4881 | -54.97355 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d2e2051-e5ad-3172-8ec8-38953d27311d | -13.43213 | -48.61998 | 2026-09-29 05:12:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 593c0c6d-68f6-3d1e-8a95-9581d0e086ab | -7.49146 | -54.97405 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 498ddd5a-6bc1-37b2-8cde-e0304349bd55 | -10.59475 | -46.21249 | 2026-09-29 05:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6517ae8b-1195-35d2-8b00-6bebee4e72ca | -12.94252 | -46.64656 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8ea65bd9-6265-371b-b235-814465d9dc19 | -9.92534 | -60.72119 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6e2a7560-8f87-3eb8-aa9e-0a875fea7ebf | -9.6876 | -58.11798 | 2026-09-29 05:12:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 62143c3b-32af-30a2-9f7c-3378338a4447 | -12.94841 | -46.64749 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d3e4c023-6318-3240-ae58-64b4d522e897 | -12.93607 | -46.65031 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59fc933e-86be-37bb-a427-cbcdd19703c2 | -9.78687 | -48.22246 | 2026-09-29 05:12:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbbc3ee4-7a3c-3d01-a3ce-285b5db2c552 | -12.79172 | -54.0192 | 2026-09-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e48b7b05-7b53-34e9-8cce-372dfa65ef48 | -11.34758 | -54.0427 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8062724-7183-3b8a-ae28-e7ac5890bb16 | -12.91083 | -52.04066 | 2026-09-29 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3004cb23-46ce-3005-bcd3-a2d64eb88b61 | -12.59053 | -51.9586 | 2026-09-29 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3f8fa2a-f03c-3c38-b93d-e694b3cc455b | -11.44152 | -43.4681 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7bd0ddb9-9d1d-32bf-af35-bebe43e98246 | -7.56194 | -55.02904 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4706991e-7b29-3e64-8846-598427d0aaf6 | -11.39525 | -43.45625 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5e81e92-fbf6-3090-9e98-aca44ba152f5 | -9.16662 | -61.40202 | 2026-09-29 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 292b6df5-4680-36ab-bfce-5d0f7ae91325 | -7.51335 | -55.0323 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a44caccc-720d-3b54-b4e1-e2c62f0f80db | -11.39726 | -47.44975 | 2026-09-29 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 217e0b0c-8d60-35a5-844a-592ffc0eafb2 | -14.11969 | -46.28355 | 2026-09-29 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6a94e7ca-7b49-3323-87f5-507e05042a42 | -14.12549 | -46.28613 | 2026-09-29 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 888b5413-302a-3929-8854-1b715d2f1dfc | -14.12583 | -46.28424 | 2026-09-29 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fb60abf1-d321-31c5-9092-5c2046b15cff | -14.52174 | -48.29562 | 2026-09-29 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46ce88a6-b196-3235-b403-7340443ae002 | -13.48081 | -48.61737 | 2026-09-29 05:12:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 616bd54d-fec1-34ce-ac6c-6390b8a91849 | -11.41721 | -43.45163 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d813221e-27e2-3788-b5c2-f431f553e8f9 | -12.00557 | -44.92685 | 2026-09-29 05:12:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 269d0407-c96a-38c5-9c8d-bcfe83a5f4e3 | -10.38634 | -61.24442 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| be0e2a66-08a8-38f6-aa0c-5d50e4a71008 | -11.42508 | -43.44546 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c8aa83d9-c284-3dca-aa16-dd46a61632e1 | -12.7381 | -47.281 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed187c00-1feb-3bf3-a193-095f224bfc99 | -11.36072 | -54.05319 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2da456f9-1e18-3122-9a96-015ed606bcff | -11.42116 | -43.45881 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8b13753d-ca2f-31b0-9c4f-a6d0ce786c40 | -12.75686 | -54.05371 | 2026-09-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e55e25c-7632-3d26-948a-15e56aa0bab2 | -12.01015 | -50.93185 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 49a29e2c-5a22-3aa5-950a-cb22d4fdb211 | -12.7973 | -54.00663 | 2026-09-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68acd4a9-630a-38be-8519-4fb8846a1121 | -12.73539 | -47.27889 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4ded2317-4efa-325a-92cd-42b9e814dac9 | -11.99148 | -50.93799 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9494793e-c257-35d9-8974-003f071ac4dd | -9.96448 | -50.1265 | 2026-09-29 05:12:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9afed05-4ea4-34a8-a4dd-1d61a87a01f5 | -12.71861 | -46.98489 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 80b3a276-5711-3f9d-8b32-926bbaf09087 | -11.97511 | -50.92693 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 257f870d-724a-3567-8d65-658c922f02fb | -11.86837 | -47.08359 | 2026-09-29 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f29431c9-0d9f-3b29-b849-e06a86df5d2c | -12.12662 | -61.95987 | 2026-09-29 05:12:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7dbca887-d008-3417-a463-1b830cf1ec7c | -11.39767 | -45.41738 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f50cd34d-c796-3f2e-a7bb-99208557fe8b | -13.2202 | -48.56532 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README65.md)
