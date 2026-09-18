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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1501a51-e0b0-3309-b8d6-579c407a3ee1 | -13.25085 | -46.90681 | 2026-09-18 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a9b6f88c-df6b-3caf-a859-c7bdeb8c3911 | -12.43663 | -50.67257 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e59b16a-320a-3c13-8b9a-675e3d877218 | -10.10673 | -45.63372 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51bd371c-714d-3a37-bb61-63b378c37155 | -9.7124 | -47.0942 | 2026-09-18 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d73cc84c-fc09-3928-aacb-9459086ac5a8 | -11.51037 | -46.89707 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 12b2cc74-5299-3823-8d59-88c4b2cfdc92 | -14.39532 | -47.26452 | 2026-09-18 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f5d8ffa-d4e2-30ca-8c16-357cde306bbe | -9.61913 | -45.33875 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e80a288-f997-37bc-adeb-24da1fe89b8f | -9.94573 | -45.33716 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e3d29b0-752b-3b17-b713-093fea980845 | -11.6363 | -51.58311 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05cc67be-8935-3b7a-8d7a-31a4a37b2e2b | -11.29349 | -43.3713 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be4798a5-f504-328f-b7fd-fb3733e2d97f | -9.95764 | -45.45688 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ceede05-df2c-30a4-ab60-061624c027f9 | -13.76322 | -48.03849 | 2026-09-18 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54fda307-d6f8-3034-b68c-29fef55ce6fd | -9.57777 | -49.10966 | 2026-09-18 04:21:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79df5823-0641-31a3-a104-3d983dcb7a4b | -9.90967 | -48.38321 | 2026-09-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fe0b6b82-5f27-313f-95f7-408858b1908e | -12.38923 | -50.69447 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 798f5d23-06c2-3b24-8e8b-f4ff03f5c4c1 | -12.38406 | -48.47018 | 2026-09-18 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8537b78a-98eb-3c00-a905-c2821a25b6af | -10.49883 | -46.28035 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ee0e079-7431-31ec-810a-765afc071212 | -13.74505 | -48.80653 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 53a26a13-5d92-3cb3-99c9-824b2da350e4 | -8.54342 | -44.55346 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ffe29f1-ec62-3b99-a678-dec76263dbd9 | -11.31446 | -43.42308 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3d47534d-1ed7-34a3-b334-4b8843d9b51c | -9.59602 | -45.85544 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c2e773f7-17c5-3fa1-8ea8-32e9f77e6d0b | -9.09417 | -45.71405 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc3cad37-b598-3a2c-a9ac-8a5510ee08b5 | -12.74899 | -46.85347 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3528b5d9-b609-3b0a-bc92-b99bc3cb013e | -10.2956 | -45.3175 | 2026-09-18 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6118b766-b4a7-3c06-b625-f054ddf0f59f | -12.61767 | -50.88778 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47569038-ecca-3b23-bcc2-4fbd1d292ecc | -13.51847 | -48.94225 | 2026-09-18 04:21:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ee6c5294-e4ec-3be4-9ef9-e8ea89dae965 | -8.16334 | -54.82063 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0774958f-d160-3746-9a77-0050db329de6 | -9.71767 | -54.81379 | 2026-09-18 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b5607a02-4bdf-30ab-973e-7e8af6815f2c | -11.66827 | -54.44969 | 2026-09-18 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| e8232d43-00ad-3234-81c0-a9609e8cd612 | -8.15315 | -54.81503 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9af55840-a10f-39ca-a72e-dbd62d678236 | -9.71578 | -54.8241 | 2026-09-18 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| be2a7686-4624-3e73-8e2e-16bddf157a8d | -8.49352 | -57.6282 | 2026-09-18 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09c0d67e-8cfc-37b8-bfe2-2fa93501e3e1 | -8.49142 | -46.88239 | 2026-09-18 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7198cf6b-9753-3d88-9340-6a8fcd1348bc | -8.48804 | -46.88184 | 2026-09-18 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7d90e5a8-0511-31d7-9499-306ecb4ee9fd | -11.31175 | -46.77682 | 2026-09-18 04:21:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df418457-7a36-3479-bba1-8ab6a2707ec1 | -9.19311 | -46.76529 | 2026-09-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7153dd8d-2da8-38b9-ab4b-cec91a5a98ae | -10.12455 | -45.5659 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 83fb6f8a-3042-373e-9363-1c716266d475 | -9.95106 | -45.28084 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef8f0cc2-a68a-369f-a751-6970fd1df603 | -9.76059 | -46.08595 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ab9aac08-e87e-3553-a00b-f00454d6db65 | -13.62286 | -46.94323 | 2026-09-18 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f22ff7a9-4a63-3ff6-a522-a1bf9ee42637 | -9.71117 | -54.81945 | 2026-09-18 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0fcd6839-03a9-36b0-814d-d991ad40367a | -12.44262 | -54.99924 | 2026-09-18 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9fd889c-0625-3599-a00e-47c1509d7801 | -14.94263 | -49.91573 | 2026-09-18 04:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc48e904-1a90-3e71-bf82-ae66f43927fb | -10.11152 | -45.64944 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2b614b38-05e9-35ce-b8cc-828b23f1b1db | -8.48746 | -46.88549 | 2026-09-18 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1d199247-132f-39ca-a6dd-ea2c55ff905d | -11.88164 | -47.61301 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8921927-82fe-3e7e-8a52-c7d4e3d5ef17 | -9.78044 | -45.04208 | 2026-09-18 04:21:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e5c0ca0-508b-3fa4-855a-b9a1ea748b0d | -13.0021 | -46.93138 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a56f05db-4881-3104-831c-b6f98a1d69e2 | -10.20419 | -43.20347 | 2026-09-18 04:21:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1e781725-a32c-3182-ba6c-d6db04ea4b90 | -12.13168 | -45.15854 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 031c6b19-f98b-3f0b-977d-2ac5d5819126 | -8.58048 | -44.55579 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95a2081a-d94b-3861-9922-17123c4ea851 | -13.74363 | -48.79386 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f41fed3-0712-328a-b7ab-723d09b9f85a | -9.70989 | -54.82642 | 2026-09-18 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7787b63d-a0ad-3d94-81b0-ea74afc24afc | -13.36191 | -46.30614 | 2026-09-18 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbcea91e-fd96-357d-bb77-44bb665352bc | -9.72351 | -54.8117 | 2026-09-18 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b7054c9e-e9d7-374d-8af9-eb2cd59dd730 | -10.83684 | -44.95897 | 2026-09-18 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c8f557e-f36a-3477-adf0-1e51ca6dc5b4 | -8.88246 | -45.89444 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e9a672bd-7887-384d-aa91-6b225092be5a | -10.66958 | -50.27354 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7bdbb927-3cf6-3055-86ab-67ab43034ec8 | -10.02344 | -51.10551 | 2026-09-18 04:21:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cb463c7-9436-3c82-96cc-43c5857686ef | -9.91319 | -48.38377 | 2026-09-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3a156fa3-2f3d-3662-a127-2272cbe7e420 | -9.83979 | -48.34397 | 2026-09-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 30fc0e9b-800b-3d48-8bda-95ef0bdf65e5 | -13.00098 | -46.93846 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e7bd6745-5a2d-3054-b0a3-631c0bd26ff9 | -12.44833 | -54.99706 | 2026-09-18 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ca83c88-0951-37c7-bac0-77a42424444c | -9.93245 | -46.52713 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5d8072e6-a183-38b3-996d-dc4ee289f067 | -8.46202 | -44.50861 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86fb5348-f137-33a6-8701-bcaff97a42a7 | -14.18501 | -45.19234 | 2026-09-18 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04f1e16c-1c01-389b-98c2-a819c2d67522 | -12.0594 | -47.50729 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 988cd5c5-ee66-38c8-b8c6-a55065aae14f | -12.44323 | -54.9961 | 2026-09-18 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 882118f8-50fb-32fb-8b2f-d44021324240 | -10.80322 | -46.65822 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6e54bc3c-8e59-3d64-ae70-d8d86c890d2e | -15.33731 | -46.03782 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b8d9076-2c2e-330b-b885-e3f1833669ef | -9.91807 | -46.51035 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5176b178-a5b1-3f6a-b540-2a711f263b91 | -8.16399 | -54.81705 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01d3eb83-df21-39ed-bb5a-589646ffbcaa | -10.59249 | -48.6909 | 2026-09-18 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8284cf15-eab1-3721-94c3-632f7bfe8e44 | -11.31676 | -46.76668 | 2026-09-18 04:21:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4ac4d850-f1c8-3b5a-bf61-6e99293eb706 | -11.48511 | -45.73649 | 2026-09-18 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f494736-0e59-33da-b230-c5cd1d057bfb | -9.97798 | -46.08833 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89595ef2-f754-3ce6-b116-60b76195207f | -13.70081 | -43.62304 | 2026-09-18 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27886435-0a3a-382a-a0bf-0410f0c87a76 | -12.1676 | -46.97955 | 2026-09-18 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 196e5d25-8960-3248-97c9-778654d9ad7c | -12.41571 | -50.67896 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f1c19a7c-e2f8-359c-ad31-162c75e0672d | -8.94507 | -44.3955 | 2026-09-18 04:21:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f38133fe-6191-3ad7-b5b1-8bc519298321 | -11.60008 | -47.37591 | 2026-09-18 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1587b18-5832-3646-a22f-8d50fe4e3fce | -9.19369 | -46.7617 | 2026-09-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47b48623-ab90-39e0-8ecb-7adb75205391 | -8.14364 | -44.85176 | 2026-09-18 04:21:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a29ca13-7a87-3800-9d66-2210d7f02889 | -11.31344 | -46.76614 | 2026-09-18 04:21:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7d00a64-a3c7-36fb-9098-173c287109bc | -10.61431 | -46.56189 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fc543834-2d32-3be7-8354-a6b32f0fa370 | -8.9395 | -51.46548 | 2026-09-18 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94b2bb30-9e1f-3d6c-8897-9d66a46138a9 | -12.26232 | -47.13385 | 2026-09-18 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ca20be9-13c5-3799-b1c9-7cc2dc1db93f | -14.96952 | -46.24347 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 516bf32d-96b4-388e-ac97-4bce42b20f82 | -10.51419 | -46.74175 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b4f5dc2-a9ea-382d-a603-7430309fb687 | -8.54063 | -44.54941 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| efee7052-4952-3ea9-bf31-0e668712be45 | -11.35599 | -44.08105 | 2026-09-18 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27b6da2f-14b0-3634-99b5-f82cae147114 | -9.19264 | -46.7468 | 2026-09-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 299ac260-0fe7-3bd5-8d70-0fa7ea09fb37 | -9.93621 | -46.58952 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4cf8cf4-d646-3ce3-92ee-580dd31794c4 | -12.39031 | -48.47524 | 2026-09-18 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 736e1762-fc2a-3cc5-a5eb-e8e147339364 | -13.74319 | -48.80285 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 696dd275-4a75-3e4f-978d-bb73712a5b4b | -10.40478 | -48.68222 | 2026-09-18 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5473d41d-b6d7-3d86-a11a-9a45682d6539 | -8.76551 | -44.23712 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 790ae131-9c43-32b9-8154-b8e826c33720 | -8.90519 | -45.00814 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3778f620-3b8a-3eb4-9c92-755d35756646 | -8.25922 | -44.83061 | 2026-09-18 04:21:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6c7749a-9dfe-3f5f-8cc2-b2bf06945b93 | -9.76824 | -46.59542 | 2026-09-18 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README42.md)
