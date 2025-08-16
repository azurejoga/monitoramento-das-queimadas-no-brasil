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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c35b68d4-bd8d-3310-997b-cf8c4e6f62c1 | -9.28588 | -68.26249 | 2025-08-16 05:25:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62c92acb-45a5-3fd0-9d4c-5dd7c4dee6d8 | -4.90548 | -62.33847 | 2025-08-16 05:25:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2cbaa954-b092-3831-8deb-70291a39ce0d | -17.21588 | -49.58971 | 2025-08-16 05:25:00 | NOAA-21 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 054aab02-80d9-3978-a4c7-bba9a73c829d | -15.18655 | -53.84967 | 2025-08-16 05:25:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7a51587-4ca8-3393-bd24-e531ed78faee | -11.36498 | -55.43573 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a0097f1-d534-33cc-9379-cd6617a4ad0c | -7.53687 | -50.53168 | 2025-08-16 05:25:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a07cc5b-59c6-337e-bb80-a21106171e32 | -11.35968 | -55.40842 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 041171ed-ac1d-3c17-ab08-7255d4629386 | -10.39439 | -64.50224 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fed97011-ceb4-3013-8e26-bcba65f17000 | -6.6665 | -58.81667 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b121040b-cb3e-35d7-80ff-c4a45c44d9cd | -14.94166 | -54.69823 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 8b37286d-3359-33a6-acd7-99646715468f | -6.07786 | -59.96581 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b469d4c6-1c35-3c0a-be6a-ff494c81f31c | -6.85411 | -57.6565 | 2025-08-16 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebee2e37-4ef8-328d-b876-18538056062f | -14.52958 | -48.59155 | 2025-08-16 05:25:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e2ddea51-4ad2-3cb5-8126-a151b34fef2a | -14.96643 | -54.72562 | 2025-08-16 05:25:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48aff2ed-cd65-3855-ba65-7d1dde4edebb | -6.70821 | -58.81863 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3414a98a-cf56-382a-b584-db1b05ca4e89 | -9.28535 | -68.25952 | 2025-08-16 05:25:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ca206b6-6709-329d-9db0-b9d8e39dcb3d | -6.70371 | -58.84846 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 143519ca-4879-332c-a24e-f49b549ecc60 | -11.94959 | -62.83864 | 2025-08-16 05:25:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e615f74-28c5-3bc9-aabf-0960901742f5 | -14.87813 | -60.08405 | 2025-08-16 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ae431fe3-46c6-3fca-8f88-c6b8957c525e | -5.93669 | -53.64749 | 2025-08-16 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b663c1bd-c13c-3312-9997-29d50d95b752 | -13.12947 | -57.16673 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51629ca3-0cb1-370e-bf2d-e1716cbb028d | -5.93603 | -53.65197 | 2025-08-16 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8c9542d4-e818-3fee-ba4c-840ea439c52d | -13.11187 | -57.13612 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 283cb683-c2df-320e-81e0-ce265ba50a08 | -14.98702 | -56.02272 | 2025-08-16 05:25:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef3cb59a-1c27-3fa0-97a7-3b59e08e2066 | -13.12666 | -57.12624 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17a05eff-5f62-3f69-8382-63e62071cb9a | -13.11763 | -57.1323 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ce26bde1-183f-375c-b4e6-a6a391c990c1 | -12.99915 | -56.87019 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a47c2449-a598-3701-8927-b359b470ce04 | -6.07454 | -59.96531 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00635797-912f-31c3-b850-144f5a63b384 | -13.11715 | -57.13588 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e0654a6d-4750-3622-b38f-0928385645c4 | -10.67713 | -69.48857 | 2025-08-16 05:25:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c16f44db-8f2d-3e22-8696-c49762165b06 | -11.35617 | -55.4345 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 530c10d7-222c-3023-be73-8d297bc26590 | -14.53732 | -48.5857 | 2025-08-16 05:25:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 774ae8f3-b01a-31ac-91f1-6524f7c07017 | -14.98544 | -56.02524 | 2025-08-16 05:25:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76794674-300b-3cab-a0c6-2978b28a1fa8 | -16.23615 | -51.12594 | 2025-08-16 05:25:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab876d0a-3061-3c1c-956e-322ccf178fb6 | -15.60201 | -56.13968 | 2025-08-16 05:25:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddebb111-6e13-3275-a547-5308b2d3c268 | -14.94039 | -54.70836 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| fee775f7-d298-354a-b237-d33ad0e2baf6 | -15.18693 | -53.84644 | 2025-08-16 05:25:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d293616-833f-3696-bbb5-cb43e5acd0ba | -5.57002 | -52.04583 | 2025-08-16 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbc5dca5-5f24-3803-a962-746cc35e4490 | -6.15263 | -57.93644 | 2025-08-16 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2612589d-186c-3696-97fc-0d92c271a95b | -6.14204 | -57.9348 | 2025-08-16 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1dacc2b6-d860-323a-b8bc-f7d56473f866 | -13.41698 | -57.03345 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbef3ae8-f7a0-380a-bf4b-d708ff90a04b | -15.98011 | -59.521 | 2025-08-16 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ec6be7a-5433-32c1-9c09-36974aa48324 | -12.30102 | -50.00978 | 2025-08-16 05:25:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 52a30966-038a-3686-b855-7c12e7568af1 | -13.44852 | -56.67477 | 2025-08-16 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a70d83df-f5f3-37a0-811c-42cc1228a5f0 | -14.94273 | -54.75878 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| bb066096-75f3-31be-bc7e-26b902b873eb | -6.0784 | -59.96233 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d72df389-ea64-3a7f-8d49-99b815d297e8 | -14.93395 | -54.70763 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 57a6d25d-fcc6-3f52-a83a-601d04effd5e | -14.86706 | -60.0863 | 2025-08-16 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 462fb41d-3457-3920-9870-e840d3e633c8 | -14.93942 | -54.7032 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b7ad4f8a-91b9-3c03-bdc0-a4ba865e0507 | -15.66148 | -56.20829 | 2025-08-16 05:25:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2c33217-a4bc-30c9-ba55-3457cde92f79 | -13.44904 | -56.67089 | 2025-08-16 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7700506d-6c6d-3c40-afc1-b573e7697e8a | -14.96101 | -54.72958 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6b41a0e2-ce0a-3a3c-a760-2d38b75b3516 | -8.79287 | -71.02628 | 2025-08-16 05:25:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5b604e7-2fb0-3469-a746-58ea515ab0a0 | -11.71004 | -61.74807 | 2025-08-16 05:25:00 | NOAA-21 | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ae1b8c2-cc54-393c-aae2-4ce94c4a219a | -5.93109 | -53.65252 | 2025-08-16 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb983e2e-d325-395c-8177-a56261cca818 | -13.47598 | -61.00146 | 2025-08-16 05:25:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa4613fe-6a34-39a2-80b2-bc0f78913b30 | -14.94061 | -54.69311 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 370459d6-75c4-36f8-8918-22784361f590 | -11.31568 | -55.20622 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3ac76de-c69c-38f5-838a-1d44d8559720 | -14.53186 | -48.59887 | 2025-08-16 05:25:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 379dbf0f-03d5-33f3-b77a-69efc89a7e2c | -13.00324 | -56.87077 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0040ecf-a55d-3f1c-b68d-58dab1858365 | -6.07616 | -59.95487 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b8a2afd-d07c-3eac-b882-65d9f0ce7347 | -6.56684 | -60.05689 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fef80317-ecfa-32ca-b67f-84c2a7041eaf | -13.4428 | -56.68581 | 2025-08-16 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a72b8788-9b2b-389a-8a3a-5d2734efb322 | -6.81936 | -58.59685 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e66a0eed-c995-38a7-b0e6-91c50146e83f | -6.08002 | -59.95189 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efa9cd7f-c730-36a0-b125-813acfa66935 | -14.97331 | -54.70946 | 2025-08-16 05:25:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b6130f4-4b12-3d61-b88c-d503248a55a0 | -13.12047 | -57.17267 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10bc118c-9730-3048-95bc-dadea642193c | -14.94821 | -54.75411 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3374294f-a2b9-3059-bba3-8f172c306238 | -13.13254 | -57.17444 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b424d00-cd4e-35c0-bdf9-010fc7b17ed4 | -13.12521 | -57.13708 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71d2d5a7-9520-3698-8be0-15dbd60083c9 | -13.11265 | -57.13882 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ea2e396-5017-32b9-ab2b-bb9f29f674ac | -5.62611 | -51.29512 | 2025-08-16 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ca70547-1869-322c-841b-06e92ab70447 | -13.11313 | -57.13524 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 965be2bd-204c-3f07-9658-c04c99b06aaa | -10.67809 | -69.48322 | 2025-08-16 05:25:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1dbdc327-3105-3a52-b267-0433c987aae6 | -11.3106 | -55.21006 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06884eb8-f94a-3bb2-aec8-df96f7e23fe5 | -11.35177 | -55.43386 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b0f3aa75-b3ee-30d3-80df-15919a97c4e7 | -13.12449 | -57.17326 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2641164-670b-37ec-b9e4-beba7c6fae36 | -13.12497 | -57.16969 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5da6d3c1-b11b-3966-b77a-d02f1dccd31a | -11.73738 | -64.89847 | 2025-08-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6848e414-acac-348c-b23e-174cb3d02866 | -14.94596 | -54.73149 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| acc204f2-4dbb-3962-9cf3-6235be3c741b | -6.66993 | -58.81719 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59172b12-7866-38f8-be4d-f10dd3085ac9 | -13.1335 | -57.16731 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc141433-730e-301c-93bd-b9bd97f77f77 | -13.12618 | -57.12985 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 555bfdfa-758c-3925-ba62-24f84f70c069 | -11.35675 | -55.43021 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c41e93b8-2fa9-3d52-9d43-5a106ea6182f | -13.1181 | -57.12871 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b95e2c73-1324-3b35-bf08-6d9fb5835e5d | -13.13398 | -57.16375 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92e698fa-4f5f-384c-93e0-562c7b091efb | -11.35909 | -55.41283 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3adb3fe0-1568-39ec-80d1-b62c89224d54 | -13.00684 | -56.87499 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d986f0d8-f20d-36b5-9c68-fa87f687a204 | -14.95848 | -56.2406 | 2025-08-16 05:25:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33edd095-9db8-34d4-a712-4f2dd48ce1e2 | -6.07948 | -59.95537 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0110155-71d3-3bbe-8015-652b7f78f8ac | -14.94229 | -54.69323 | 2025-08-16 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 38640d47-962a-31d7-ac5c-a18e656379d8 | -5.44972 | -60.13442 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8684e580-edd4-39d9-8f53-684a42c56ba9 | -6.71562 | -58.81595 | 2025-08-16 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d0865b4-05c1-3f34-a2b8-883412c17049 | -13.11243 | -57.17148 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51721fb7-72e4-3f69-a526-4f711be38c60 | -13.12213 | -57.12932 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6e9706f-4cdf-3b9a-8e75-951d8b316bea | -13.11597 | -57.17564 | 2025-08-16 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 213cd363-9214-3f40-8740-c8c970eaa853 | -16.24194 | -51.1312 | 2025-08-16 05:25:00 | NOAA-21 | DIORAMA | GOIÁS | Brasil | 5207105 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 05bfba44-3459-3a06-b670-7701dc91b4c8 | -6.57016 | -60.0574 | 2025-08-16 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81fb89b2-5404-30dc-a6db-1dc8652adcdd | -14.97264 | -54.71505 | 2025-08-16 05:25:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d0a8dd4-ae66-3d6c-8c8c-d29251f9334a | -11.36232 | -55.42217 | 2025-08-16 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README61.md)
