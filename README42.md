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
| e72d910d-4373-35b9-9bf9-d5409388318a | -9.16815 | -40.59688 | 2025-08-26 04:21:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b0ef38e9-0676-34e9-8233-7cead0347dd5 | -7.74073 | -50.29566 | 2025-08-26 04:21:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b939eab-e7a4-3fd0-995c-538944c83852 | -7.33115 | -43.78271 | 2025-08-26 04:21:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50eeb656-c30a-3c6c-8ba3-ef926e98c2be | -14.39619 | -51.93766 | 2025-08-26 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6638cbdf-c8bc-3875-98d4-cc0a98d1ed1d | -15.03337 | -48.68678 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fcc48bee-4a03-3076-b0bc-fa4417569843 | -11.53464 | -52.1311 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 577adc9b-157d-329d-a50d-45baa819f54e | -16.74189 | -47.5975 | 2025-08-26 04:23:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80cac367-20c0-3f1b-8655-c9ef1a8a2db6 | -17.2105 | -47.22379 | 2025-08-26 04:23:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b03e73e-e685-3e77-91a6-716f628454fd | -12.75853 | -48.14548 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5c834ab-29d3-3849-a788-c4dedb5fb8c8 | -12.76505 | -48.10667 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36089349-55f7-313f-ad2b-54fab4d860f4 | -11.56915 | -52.11354 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| b534fca4-8581-3caa-9ed1-6d3f927c1c27 | -14.722 | -45.37442 | 2025-08-26 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dddecc34-eb28-3192-9929-89e456cf013a | -15.05345 | -48.69438 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b4dfab0-45a4-3377-b6a6-1f1e85739bfa | -11.30377 | -55.11935 | 2025-08-26 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ef3f0957-97f7-3b2e-898f-b70e5dbd03b9 | -13.45101 | -46.99166 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a203debb-3925-38b2-bb8c-bcdddbaf7995 | -13.58727 | -48.19412 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 693eb7e9-0993-3af2-a577-fea0677dd509 | -15.0833 | -48.54739 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84d16941-4670-335e-a8db-6c3e04ada628 | -11.52496 | -52.13205 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 5362b34f-90df-3c89-9979-7df7ef0bc346 | -17.86754 | -42.24419 | 2025-08-26 04:23:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3c2190dd-4fbd-3a4d-a7eb-02063577a6f7 | -15.6176 | -52.70099 | 2025-08-26 04:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a16e5fc6-0e60-36da-8bc8-422137dd8ffa | -9.17998 | -59.45136 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 85d232b7-608a-341f-a9a5-6b5bfcff090a | -13.26349 | -43.5433 | 2025-08-26 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aacee80d-4362-3546-b59e-5540c3cec9c8 | -11.56351 | -52.09471 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2b80968-a8b7-369f-a496-f5664a309ec0 | -11.51977 | -52.13552 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 37b02d3d-586e-3a44-907f-70af218754ea | -11.63576 | -46.40645 | 2025-08-26 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 18a3efd3-71ae-3a55-8a43-e9646cdac4fe | -12.74467 | -48.15573 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24f28733-2808-3f18-8d69-186f2f33b2a5 | -13.63494 | -48.15429 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97753663-0b41-378e-87ce-4d2930d28b00 | -15.10749 | -48.63551 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4964bef4-d44e-3657-9afe-484c7a574988 | -14.25754 | -48.02971 | 2025-08-26 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1859212-3df9-3dd8-8628-c4c8e53fb1e9 | -9.16852 | -59.54331 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 822cdbfe-1235-3bde-a426-8658c4645c78 | -12.75982 | -48.1378 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 104e4e80-cfcb-3be3-a76f-9df3a817a7e8 | -11.56634 | -52.10406 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d6894bf-0fc0-3460-ae33-c4fc3f13fe60 | -11.5449 | -52.12226 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6d9b96b1-fb39-38c4-bcef-2dbb938ff43a | -12.75882 | -48.13453 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3301e7c-93c3-39c9-b95c-0a833bb08ede | -15.03618 | -48.69131 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa703df4-90c7-3a67-b11c-0ffcff8f585b | -12.72865 | -48.14508 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 38a1d81b-6056-3706-94b0-14299269f8c0 | -13.52335 | -46.897 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0dc61e6-99b0-3bca-aa7d-e5937508315d | -12.40919 | -46.50084 | 2025-08-26 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5efcdebe-69f0-35fa-a754-26ce49f10768 | -14.36472 | -51.91252 | 2025-08-26 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9795a105-583d-3ad7-b3dd-96761c70a2fb | -11.30965 | -55.10875 | 2025-08-26 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 168cf5b5-b03a-3835-b5e8-c88e7d41846c | -14.24821 | -48.04387 | 2025-08-26 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 23c9a095-81c7-38a5-b9ae-c7964ee5640c | -11.56711 | -52.09978 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f85c7c0c-ef11-3667-a3d2-44509543fb29 | -12.74748 | -48.16026 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 348fcc96-2331-3395-98fb-5c37a8f4d7ac | -11.5477 | -52.13175 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8dbdf956-cc92-3677-888b-ca3b3908dcc4 | -15.04225 | -48.50523 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6d74f8b1-4c1f-33b1-9aee-e28c9e126ada | -10.64229 | -51.59628 | 2025-08-26 04:23:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d5c84cf-d265-3a51-aad4-891533b1af3f | -12.73304 | -48.16155 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ff84b17e-32f6-3382-97da-eb78f625f043 | -13.58664 | -48.19794 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a220ae8d-b23e-35bd-a1e7-84bcfb519302 | -12.74812 | -48.15638 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6eb89736-0b51-3445-8e52-23d4b7a62ebf | -13.433 | -47.01826 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36d1d102-6097-3e12-b63f-9e312ce47830 | -15.02378 | -48.51007 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80abf106-80a3-3601-b4da-3c930c2a7fab | -11.30427 | -55.10777 | 2025-08-26 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f1ecc16c-f1e9-3910-8a3b-e9986af1af42 | -13.41417 | -46.90091 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3fdbb4f2-ea20-3268-97b4-e8c4022fb861 | -10.24496 | -59.66602 | 2025-08-26 04:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2503668-9271-3405-8f78-bb53bd38e235 | -13.4404 | -46.9936 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e8c7c23-80c9-33bb-9aec-9cc5427b61c3 | -14.26156 | -48.02654 | 2025-08-26 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc17a687-cb40-3df8-a72c-c43f86b3e990 | -12.69581 | -47.87795 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5bc662e9-9d18-3513-bfaf-202ec5faafbd | -11.63227 | -44.86522 | 2025-08-26 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d222cb7-7115-32d5-b3a5-8d00a01b0f31 | -13.65774 | -46.88242 | 2025-08-26 04:23:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24e2a676-776c-3c59-8e6e-e265ab7989e4 | -11.55007 | -52.11879 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46b5885c-1e13-35b9-808a-fe215d743b65 | -14.31129 | -60.36754 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05a506c0-9aa5-3923-84a7-3f06a64bedd1 | -12.41814 | -46.48772 | 2025-08-26 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b03b2490-0ae5-3d4c-821b-9dbed1a0b1d5 | -11.51995 | -52.13727 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| b1f5f76c-71c3-330c-8b6c-32db4dc57ed5 | -11.55523 | -52.11532 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f2b85ba-35de-3b61-a9af-501c94087b76 | -13.44477 | -47.00909 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82d420af-3a4a-33fb-ae8d-0d198a34eef9 | -15.14373 | -48.67358 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc668ead-562a-3e44-a4c5-32eb69845834 | -11.51556 | -52.13641 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| f642ba77-2f0c-36d8-aeed-580500aef103 | -12.75789 | -48.14931 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7432891-16fd-3d15-a3cc-88dccdfe87d0 | -15.49306 | -47.88756 | 2025-08-26 04:23:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60e4815c-45e4-3dac-9289-739867ef0425 | -13.49058 | -46.87341 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ec3716a-3af4-3078-b53f-d7a9d1d45d0e | -10.38888 | -57.69481 | 2025-08-26 04:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6b6e3432-6792-39e3-a08d-15f5351fac77 | -13.63215 | -48.14985 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4be43dd8-a35d-36dc-9ff0-e020a84bdac5 | -9.16705 | -59.55077 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e8764803-569f-3e65-bc11-9f3a356baa88 | -11.51117 | -52.13556 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 72b72bb6-be66-3add-ae1c-7fde1c25708b | -17.86897 | -42.24551 | 2025-08-26 04:23:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7b31ee9f-c931-3ece-b611-bcd851893efc | -11.30577 | -55.10908 | 2025-08-26 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9859514a-5ba2-3c2d-98c7-d18f696793b7 | -11.30749 | -56.26173 | 2025-08-26 04:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 330efe89-a60b-3717-9f5c-e72e5b2358bd | -10.5413 | -57.96895 | 2025-08-26 04:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b04ae2d-5dcd-3f36-9915-aee7516520e4 | -13.8265 | -46.6986 | 2025-08-26 04:23:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c8bae23-7957-3258-a52a-580b2bbe629b | -17.21107 | -47.22017 | 2025-08-26 04:23:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14ec6284-22d8-32a6-b991-3787893f43cc | -13.48267 | -47.00843 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fe626797-0548-396b-9621-f0fe832ca154 | -16.03511 | -48.08207 | 2025-08-26 04:23:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9c7e74e-d217-3c64-b211-d82a461a6607 | -15.31935 | -53.84024 | 2025-08-26 04:23:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5c95107-b95f-3f76-b1b2-066b7ca24765 | -14.97042 | -52.88068 | 2025-08-26 04:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a81bb996-a35a-3f78-9974-ece48c6f4e41 | -14.2969 | -60.36655 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28a44935-4ebb-356f-b886-c70713e36bda | -12.56189 | -44.42228 | 2025-08-26 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ed7e4c0-4eb5-35c9-8415-b66942862403 | -12.9397 | -46.34057 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8c7c4535-1b58-3beb-a05f-2983f72622ff | -15.12172 | -48.67782 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b925dc1f-4101-3431-914c-47e6964706ce | -11.61009 | -46.40241 | 2025-08-26 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88c432b7-2296-33fb-838e-eef0a97b0950 | -12.37338 | -46.55338 | 2025-08-26 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3492e8e1-1834-39f6-b72f-e4e11ecafc6b | -15.04507 | -48.50952 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30a2eed6-3d0f-3d8d-a875-ad3b5b508586 | -12.70643 | -47.89459 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1439ef7e-a67d-3dbd-8417-8ccc6e3273b9 | -12.93586 | -46.32173 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71952e99-9ef0-3176-bf34-4af744a82ed9 | -13.48781 | -46.86925 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5de72a4f-4993-33ed-9de9-bc65107e8809 | -11.54321 | -50.45654 | 2025-08-26 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7344191e-1b32-3d7b-997d-57735a0e6d14 | -12.56133 | -44.42597 | 2025-08-26 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a5d5047-90ac-3373-ae18-77de21b45a12 | -12.41787 | -46.8101 | 2025-08-26 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 39995d70-bd02-3811-86d9-ec9227ef6b05 | -11.56039 | -52.11187 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cd51506-e4c6-31de-9425-faf0e7d178cb | -13.42799 | -46.92156 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f2c8bbd-3c4a-3696-a96f-f290ee58be95 | -11.64176 | -44.8704 | 2025-08-26 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README43.md)
