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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41fc1ee4-cf6d-3d0d-a551-8570e8a950b4 | -14.90537 | -48.31366 | 2025-10-02 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aa5e186c-cafd-3583-a876-ba325529207d | -19.63199 | -44.90192 | 2025-10-02 04:04:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 55bf3b45-67eb-34ca-a33f-d1bfa16822ee | -15.23359 | -48.72466 | 2025-10-02 04:04:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22a896e7-600f-31a3-bbb3-8c377defa275 | -12.94318 | -46.9412 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77065d95-b306-31b3-b3aa-41cd6f449a44 | -15.93522 | -43.30173 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bdc6679-bcb6-3880-8d22-2c765e4cd729 | -20.19161 | -46.02173 | 2025-10-02 04:04:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d485a632-d504-3c4f-9ff2-7f264e35441d | -13.28858 | -47.25608 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18304494-eb81-35f3-9dfc-0ccd3eb93f45 | -14.41222 | -46.09844 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b5d1888-8715-3de5-a69c-515830a47e1c | -20.22542 | -43.89835 | 2025-10-02 04:04:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6a57c141-6682-35c7-bfa8-80319050a97f | -13.78257 | -48.04699 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7c0f37ec-6a2f-3ab4-826a-e442473111f4 | -14.72832 | -48.16266 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 014899b2-0c80-3713-a8ae-a9725cfe1cde | -15.91381 | -46.22281 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 343f516a-aecd-366d-8623-c4ceb839704e | -16.36038 | -47.03486 | 2025-10-02 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 13085f2b-eb3c-3ebc-968d-51b2899b1c2b | -20.62295 | -46.22081 | 2025-10-02 04:04:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4649b0b9-9868-352e-b192-1025c6cca941 | -14.21838 | -44.93709 | 2025-10-02 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c37c3fe-a3ff-359d-b9b7-b3cd6b75121b | -20.0793 | -44.19233 | 2025-10-02 04:04:00 | NOAA-21 | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 432749a2-85d6-3e4a-a53e-fd8ecbebc6ba | -13.95845 | -48.13024 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a50b01df-a073-3874-a580-ad9f5cd16588 | -14.48434 | -48.43148 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4e28f849-bc1b-34a4-b46f-f486c95da2ac | -14.47082 | -48.40688 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 1b115b18-cc5a-3a8b-93f2-a2f64d44b065 | -13.32422 | -47.22472 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06ac4a6e-78f7-313e-a5a2-81550caa5839 | -18.50471 | -44.03151 | 2025-10-02 04:04:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6727fdd6-ff1e-3814-9401-2859d534b1f7 | -13.18175 | -47.79096 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d89295fb-eacf-39ce-a443-fcee0acadc2a | -13.78831 | -47.99985 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45beaa50-11d8-334b-b1e2-cc5aaf037dcb | -13.31344 | -47.00287 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7100c36c-636a-3219-8599-48ff1a1c2e2c | -20.80941 | -46.32143 | 2025-10-02 04:04:00 | NOAA-21 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 051d3da6-4aeb-3ed6-9f4c-2e996d8efbef | -13.36946 | -46.33488 | 2025-10-02 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bda55372-8daf-32ed-b88d-177a2701fc31 | -13.32493 | -47.22074 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de37616d-ca88-3507-956d-b7fdfff8b940 | -19.90301 | -44.49878 | 2025-10-02 04:04:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 11fd248c-f54b-342c-8341-e4324268056f | -13.30426 | -47.83902 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f3a326b8-303b-3722-9cf5-c24d41134cc5 | -13.16357 | -47.81699 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 01565788-0997-39d6-a816-db921c816f0c | -13.34774 | -47.3331 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 346c1579-5065-399b-877b-6aa254ce838f | -13.56115 | -47.28566 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 33177ab6-373f-34c4-a51c-163f2c9c0687 | -13.65742 | -47.30918 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 45de73c7-8386-3154-ba27-ca805dd08ab5 | -14.87858 | -48.28927 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4cf865bc-d92d-3d90-b49a-b55805d36f28 | -17.07515 | -43.47865 | 2025-10-02 04:04:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5816ada-b1cf-3632-a51b-fc9bf604ec57 | -14.67453 | -48.11726 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f9e2871-ef04-31cc-b4d4-77c10e5f1e94 | -13.16504 | -47.80904 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 82ad440e-27d9-3790-a88a-5bd2a8f5209d | -16.92342 | -49.78632 | 2025-10-02 04:04:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b9bae1c-7954-39c8-9dd1-cb8222128fb4 | -13.17318 | -47.83743 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d837baad-9202-3f4e-8c2b-91adcd69a46e | -18.25153 | -43.14847 | 2025-10-02 04:04:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 786e8f3c-9ff2-30a8-8ae5-1fb7fda8a25d | -16.01945 | -50.86448 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 144213c4-128c-3e90-ba22-4f58b499ddba | -13.31252 | -47.19488 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8fe89a3-d126-3f0f-b8ec-3e1b45ff45e3 | -14.47113 | -48.40411 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 413a72e4-bd0e-3ff6-abb1-22e73b2b307b | -14.47243 | -48.39838 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b3eeea24-5558-3128-bf39-8fba3c3b8f50 | -13.94966 | -48.12923 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cabae1e8-2dd3-31f3-870f-f7f3297840ae | -15.31859 | -46.39427 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45155873-b04e-3b02-8c09-9fe7cf835cbc | -14.4832 | -48.41343 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a2195d18-7867-31ba-a403-70813d884dbe | -16.00718 | -50.89993 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75eea115-01d9-3f1f-8072-c744a5701818 | -14.02241 | -47.98578 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cbe8c99c-7584-3ff9-908e-d730ce1cc27a | -15.17453 | -43.62654 | 2025-10-02 04:04:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 9.9 |
| bbcc4bf5-9c5a-3d94-b8b6-2428994c9d97 | -16.03518 | -50.91662 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2b650b6-393f-397c-93ba-9ab7dd301402 | -13.54165 | -47.2515 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 344c99f5-c2e5-3d9d-8ffa-57357ed3fbb8 | -14.36678 | -45.95778 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 909fe28d-aec0-3769-a7a5-c8be53f0f9c6 | -19.59925 | -44.86804 | 2025-10-02 04:04:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7986b01f-a457-3492-8a66-f41c79242218 | -15.3277 | -46.27658 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6760622e-3c19-30ea-906e-b906d7dfb82c | -18.39215 | -45.4633 | 2025-10-02 04:04:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 239fb77c-93ba-3094-96a3-9465134afff1 | -14.33961 | -47.12793 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f384cc5-9ae9-3b4f-b4c6-0b8dd0aa63a8 | -13.40249 | -44.3906 | 2025-10-02 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cf72f0a2-550e-30ba-8cab-9bb90763a361 | -14.59858 | -48.32695 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bd2a3c6-d848-306e-be1c-89584643038a | -13.17489 | -47.8523 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84e7d35b-8349-38cc-a401-1f52e988e3e9 | -12.59081 | -49.89885 | 2025-10-02 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e151758-e416-3c4c-ba7c-3953ac5a6dab | -15.1768 | -40.43261 | 2025-10-02 04:04:00 | NOAA-21 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d289ecee-f89b-3ebf-96c4-8c02a2c47990 | -14.58551 | -48.32466 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b1a90547-09c0-3e81-9fb0-530e60f7620c | -13.30159 | -47.20813 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f54f1593-841d-30d7-855e-cc9907e36f7b | -14.98808 | -46.90926 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 94d91957-9176-3de2-afe3-df1cfea59fa1 | -13.91163 | -48.09197 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a531b113-39ed-357f-b830-203eadeaffc3 | -15.54787 | -42.66094 | 2025-10-02 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 72113e9b-41e0-3b2b-9d98-9b2820034881 | -14.37602 | -45.97076 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 882b35ec-8962-3c13-b89c-14ea84bce0f5 | -14.67999 | -49.61147 | 2025-10-02 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| adeed60f-b843-377d-8b52-49e109f21ec0 | -15.18911 | -46.39756 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6dd49607-befa-3f99-a65c-4975a61c30b6 | -19.00138 | -43.01002 | 2025-10-02 04:04:00 | NOAA-21 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c20f9844-d3f9-394a-ac43-e8665e9d91b5 | -14.5799 | -48.30612 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3bda280b-0455-3132-85f0-6367af5a25d4 | -14.59955 | -48.32692 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 16f7a6d9-b53e-363f-9b56-58ee6789547a | -15.22663 | -48.73732 | 2025-10-02 04:04:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 75e5f09e-94ac-3dd4-b11d-7cc684fdb83e | -16.04288 | -50.85117 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 606e4c98-f435-3a58-843e-a03b50b22670 | -13.94525 | -48.1288 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 205d9a35-c549-3c55-b587-199a9f5d5338 | -13.08259 | -47.07219 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cee5740b-f56d-361a-ae2c-60989853d10d | -17.73556 | -46.15809 | 2025-10-02 04:04:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c12a10f-1e5a-3f60-aff2-b9a50d4b163b | -14.32137 | -45.88291 | 2025-10-02 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 10bc368b-e2fb-36be-80c2-72135b42f302 | -19.84589 | -46.70487 | 2025-10-02 04:04:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67d49dd6-357d-33cc-8318-6b4772c6249f | -14.40797 | -46.07794 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92ca2790-6fc3-30a7-be83-f8f9e1be3e8b | -13.32117 | -47.81955 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ad6b9ca4-2892-3a32-90ec-3fb69c84d588 | -13.18244 | -47.78724 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31e360b8-0254-3ce2-b88c-67b7f82c7b91 | -21.11862 | -43.76219 | 2025-10-02 04:04:00 | NOAA-21 | ALFREDO VASCONCELOS | MINAS GERAIS | Brasil | 3101631 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 29492585-31e7-3c03-bcc3-4697459ba0b0 | -19.86889 | -42.59282 | 2025-10-02 04:04:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 80587e8f-0876-3fdc-a49f-534a2c9ba1ca | -13.21912 | -48.45034 | 2025-10-02 04:04:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 95953d89-c1f0-3442-a765-577a743c3089 | -15.78441 | -43.68487 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8f2cda94-7b71-3294-9a17-43c4dc6237e3 | -14.21102 | -44.92355 | 2025-10-02 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8e66865c-ae79-3413-88bb-075510a470ff | -12.68435 | -48.55185 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 62a85a6b-14e4-3b3c-8927-32788fadd44b | -13.17528 | -47.82604 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 200f3a42-be94-3f09-862b-352a675d7daf | -12.50486 | -50.25099 | 2025-10-02 04:04:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ed773ab5-f236-3592-83bd-a7190997cb1a | -13.66164 | -47.30946 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 133df983-05eb-3f68-b746-96f72712215d | -14.5943 | -46.71717 | 2025-10-02 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fb55d0e1-e71a-3c7e-9b81-ff22958717a3 | -15.35168 | -47.0709 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f6f7a72-0860-3900-af02-666ccbc5e5d7 | -13.96369 | -48.12611 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ae718513-ab2b-3888-859a-4c57ac45f841 | -12.5858 | -49.89793 | 2025-10-02 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d998ba82-319f-3e48-8e86-b9c1e691928e | -18.84443 | -43.14261 | 2025-10-02 04:04:00 | NOAA-21 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| f9a164c8-f071-32af-b332-be718b0e6b0e | -14.31306 | -45.88617 | 2025-10-02 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3de371e-142d-3c9b-abd7-54da6c59b140 | -19.06198 | -41.91161 | 2025-10-02 04:04:00 | NOAA-21 | CAPITÃO ANDRADE | MINAS GERAIS | Brasil | 3112653 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dd12e59b-adc5-3487-a62e-374faf3ca532 | -16.06288 | -51.00799 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README50.md)
