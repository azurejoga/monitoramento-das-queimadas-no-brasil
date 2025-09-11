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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9704b63-4c5f-3b85-8c05-72e196c2aa6c | -20.2299 | -41.01315 | 2025-09-11 03:57:00 | NOAA-21 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| df5b2dbf-9853-3325-a52e-68d418d13d34 | -17.68415 | -44.19626 | 2025-09-11 03:57:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da27da43-e516-3938-aeed-f7716df66198 | -15.69985 | -43.85168 | 2025-09-11 03:57:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ad18fe0b-3340-3496-a209-84b1bb57aee2 | -20.70107 | -46.07291 | 2025-09-11 03:57:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 49427cca-b64e-303c-b382-3edf1b743c4c | -14.14016 | -45.41239 | 2025-09-11 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c9d15f4-5a7f-3f9e-8e7c-41484036617b | -19.96199 | -44.15444 | 2025-09-11 03:57:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c9d4e495-3f0d-3529-9bc1-fe91d060ab36 | -20.06768 | -44.65821 | 2025-09-11 03:57:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d1131f2-cb55-3435-aace-f6bdf14926fc | -18.01521 | -47.14036 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a25f33f9-bcf2-3675-bea9-494d3b46a0cc | -14.5003 | -42.47099 | 2025-09-11 03:57:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0a37ba3f-bc23-3a66-9eb5-930d52ec1cda | -16.58695 | -50.08213 | 2025-09-11 03:57:00 | NOAA-21 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb3b305e-2222-3082-9703-a5267bdedd40 | -17.8327 | -46.73043 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa245def-fbd2-30fe-94d0-483f8c92896d | -12.90944 | -47.99641 | 2025-09-11 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 609cf345-4160-3591-92ac-add9d3346627 | -12.9562 | -46.72849 | 2025-09-11 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3266873d-f6ff-323f-892b-ed8bc2c31d27 | -17.94276 | -44.48451 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 428a36c3-ef16-3220-8114-1dd817c14d2b | -13.85861 | -43.82341 | 2025-09-11 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33bf788e-d6cd-3e70-a650-72a6342549af | -14.66613 | -44.04672 | 2025-09-11 03:57:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c9e5e135-634c-3ceb-8e53-2daa998c65e3 | -15.20204 | -44.03572 | 2025-09-11 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e718e3a9-2269-3f62-99bb-bafffb478ea4 | -17.50084 | -43.75744 | 2025-09-11 03:57:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00700351-7b36-3a71-8798-28d684625bb9 | -20.01058 | -47.63271 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf52e967-b601-3981-a06a-5730df8d7f56 | -19.23296 | -47.99998 | 2025-09-11 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b150fc6b-e8fb-32e9-a947-ca7e5333541b | -15.13543 | -52.44093 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d5943c19-63df-30fe-b20e-9bd283904757 | -16.62911 | -51.82214 | 2025-09-11 03:57:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0c103c44-533b-32fc-b2c4-79e2b2442df7 | -20.15773 | -43.66831 | 2025-09-11 03:57:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9b587ca8-e495-3f23-895e-4b7a980d4a72 | -17.74825 | -44.49719 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ea9db5d-be93-3cf8-b195-ad5ccf391234 | -18.29395 | -47.6756 | 2025-09-11 03:57:00 | NOAA-21 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b992f2c1-c773-35b5-92d3-c4ea9845b3a8 | -14.78821 | -48.2399 | 2025-09-11 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4eacc3c1-ac07-3949-8b7b-cd67d92a5968 | -19.98571 | -47.62706 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e49183af-06cf-368a-afff-6257887953c9 | -20.54148 | -47.62621 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e613422-db91-3437-a21e-6c0147ffa2bd | -17.46963 | -45.10276 | 2025-09-11 03:57:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0b871de7-be32-3031-a12c-750ec27a74f6 | -19.25448 | -48.0122 | 2025-09-11 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 671d2473-256c-3a5c-918e-3e62e14e1176 | -13.8557 | -43.81832 | 2025-09-11 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5385be0e-45cf-379f-a338-c1210ddfa0cc | -16.29745 | -50.05924 | 2025-09-11 03:57:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e8ef9940-ff9a-38f4-aa7d-7554f2cc5139 | -15.13646 | -52.43607 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 60c4b5d4-85e3-3593-a26c-857fe902b4a0 | -20.36198 | -42.19494 | 2025-09-11 03:57:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| e464c92e-8e67-3103-b70f-04349f5e3bf6 | -15.14944 | -52.4052 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0775107d-f444-325c-896a-93ac587d11ba | -15.25093 | -44.03548 | 2025-09-11 03:57:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9dd458bb-8ed8-3a70-a1d9-963f7d8fecea | -19.24159 | -48.00176 | 2025-09-11 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 728f6c22-b6cd-3007-b0e9-05ba689b1038 | -19.68391 | -44.35006 | 2025-09-11 03:57:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 644a5049-d936-3405-a90c-57087a59dc6d | -17.24359 | -46.75887 | 2025-09-11 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 254644eb-5f9c-3a65-bff5-897fbfb835a8 | -19.74996 | -45.1897 | 2025-09-11 03:57:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77620d8e-dfc1-352b-97bb-dff2c23a01ca | -15.20127 | -44.04014 | 2025-09-11 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6eb62de9-03e6-3038-8150-60e0c94a2ff6 | -17.55536 | -44.54484 | 2025-09-11 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 333bdb17-5842-3d44-ae00-d541c5130d7f | -16.2846 | -45.67955 | 2025-09-11 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c61ec131-c96f-3f96-8ff8-9ae71f0c0543 | -17.55458 | -44.54936 | 2025-09-11 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 80d7d2f3-cf8c-34c1-a1f4-bfa25384de7d | -20.33747 | -46.61017 | 2025-09-11 03:57:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fff038bc-d45b-3b04-9a4b-a0bb47be8607 | -19.18878 | -48.79847 | 2025-09-11 03:57:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6da48fe-51eb-3b1d-b16a-2fefecc547fd | -20.70832 | -46.05468 | 2025-09-11 03:57:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5de0dab9-244b-3e72-98f1-180e5fc06092 | -20.00079 | -47.63859 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 48ce47ec-65f4-38ef-8cb9-ffb0f324864e | -16.55785 | -49.74023 | 2025-09-11 03:57:00 | NOAA-21 | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4393ba28-49b0-326c-a015-c4f534c5faf4 | -19.96345 | -46.88174 | 2025-09-11 03:57:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f8d9aa4-5f3f-38ee-8369-e0568c00d346 | -14.13132 | -45.39221 | 2025-09-11 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e4d8aa6-6ef3-36b5-a6ed-dd70dc799c90 | -18.01015 | -47.99609 | 2025-09-11 03:57:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aef05080-9eb6-3574-826d-269203709b52 | -17.4994 | -43.74457 | 2025-09-11 03:57:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 097ccb76-e249-3b07-84f2-29490c3997ef | -19.16213 | -43.0578 | 2025-09-11 03:57:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 176e2079-5000-3f0b-9907-d365de7b1010 | -15.25168 | -44.03108 | 2025-09-11 03:57:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 45a17669-3118-304a-bdcb-3055bb261e7f | -17.325 | -46.67824 | 2025-09-11 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4e0ad6a1-cebc-3a50-b42b-a6601e3d6f26 | -18.28102 | -39.69411 | 2025-09-11 03:57:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6e544ea4-c9ca-32f3-b6a5-d25b81acb223 | -18.50405 | -47.30492 | 2025-09-11 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c104e022-75fc-3419-b803-38e4555c7993 | -20.52123 | -47.63036 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5e16f20-b6a8-3dfb-bc9f-caf5b9cacfd8 | -15.12499 | -47.03045 | 2025-09-11 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 055a7808-db7c-3450-a477-6ec4f4d0a1e2 | -20.54228 | -47.62212 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 896eb0fe-749f-3432-8b66-cd47523af1fd | -20.40186 | -46.28062 | 2025-09-11 03:57:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33f9fc46-47a9-318e-af2e-d83ad5f18586 | -14.57928 | -48.76007 | 2025-09-11 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 58c65ba1-f30e-3ab6-bcea-8c4419aa1c02 | -21.11695 | -42.96381 | 2025-09-11 03:57:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6b1e5499-ecab-38a1-b1e8-5a035e72ca72 | -18.60633 | -43.974 | 2025-09-11 03:57:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7bd407ed-976f-387b-914b-1df3e5365794 | -15.61366 | -52.76793 | 2025-09-11 03:57:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67398cfb-2802-3758-9e9c-4c09235d353e | -14.13869 | -45.3973 | 2025-09-11 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 454722bc-17b0-3e97-8011-783837a9d5b4 | -13.85549 | -47.36337 | 2025-09-11 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83b95357-30da-3f4c-85de-13f0eb7095a9 | -14.14268 | -45.39807 | 2025-09-11 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8687245-1f00-3428-a6bc-a72ed5ef826c | -15.62614 | -47.53764 | 2025-09-11 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53d387b9-67ed-3b7d-ab5d-a6b92425e5df | -18.05615 | -50.72351 | 2025-09-11 03:57:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d40b6a0-4721-3b7f-84cc-d9a57aa5d952 | -17.84947 | -46.74901 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cfdcda63-95c8-3aa8-b3c3-bcc06c8dec0c | -19.36215 | -41.30546 | 2025-09-11 03:57:00 | NOAA-21 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c8d5b4a2-839a-3f06-9443-f8eb095e78d2 | -17.84288 | -46.74428 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 67009741-61cb-3262-a373-4e25dba2f4f8 | -14.30229 | -45.04068 | 2025-09-11 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 02d2762d-b5b7-306b-a52e-e9cb629f90cd | -20.08077 | -44.74739 | 2025-09-11 03:57:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 796b791e-4b84-3f0b-8095-5ba3c25b03d5 | -18.7602 | -44.32704 | 2025-09-11 03:57:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07997974-9d52-3be5-bf3d-dbc2da55d321 | -14.85122 | -46.79221 | 2025-09-11 03:57:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b9c6db4-6253-3883-8ce8-2676c5377b31 | -13.97483 | -46.64685 | 2025-09-11 03:57:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56cd6614-d948-3251-8f6a-58c085f57967 | -12.95537 | -46.73295 | 2025-09-11 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ddbf31f-992c-3e2b-9ec9-3cf3332ccc7e | -15.79536 | -52.2485 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7baad05e-c68b-3f34-9254-87ebb3108ebb | -19.10602 | -43.22095 | 2025-09-11 03:57:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 44ffb33e-cdfa-38e6-982d-506f29bc347b | -16.62908 | -51.82269 | 2025-09-11 03:57:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 860ee254-9df7-3a97-958b-1dac1165bb86 | -16.58627 | -50.08547 | 2025-09-11 03:57:00 | NOAA-21 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc4c92e1-fb29-3b98-a47b-2f46c9b81b68 | -14.30318 | -45.03561 | 2025-09-11 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 51207232-6664-3761-adb5-a9ba0e358be7 | -14.39916 | -47.31734 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 856d7fb5-509c-33a3-86e8-8db79c88e322 | -15.15464 | -52.41094 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a741f457-3836-3342-a8b4-bdd2c683570a | -16.33123 | -43.75088 | 2025-09-11 03:57:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c4ddaf3-bcb6-3426-98e7-1cba2c2f59b0 | -17.84273 | -46.73978 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 795e2c01-3d9f-3b7d-94f7-305cb562e18a | -18.34616 | -44.36685 | 2025-09-11 03:57:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0680e2c-a216-3538-a947-e63a58af8e5c | -19.46113 | -40.88372 | 2025-09-11 03:57:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 68c52ef9-c194-3045-892c-09613c62e816 | -13.64952 | -45.69918 | 2025-09-11 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 101521ca-19ee-3bb6-853c-f09232b54883 | -17.33248 | -46.68378 | 2025-09-11 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a928db30-17e0-3ac3-8d19-cc10c7a6bb68 | -18.54535 | -46.69155 | 2025-09-11 03:57:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 12c46e65-afa7-3733-b03f-b0c36477a933 | -20.00565 | -44.23436 | 2025-09-11 03:57:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| defc9753-ef26-32a6-bba0-db3e74992f5a | -19.35885 | -41.3049 | 2025-09-11 03:57:00 | NOAA-21 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8f86f984-9176-3505-bf26-8aae66cbe078 | -13.84906 | -47.34722 | 2025-09-11 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d99f8f5d-f207-309e-944b-7c9cebf973e4 | -17.49589 | -43.74401 | 2025-09-11 03:57:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b60630eb-45e6-3bbd-bd78-1abd268d7f5a | -15.81893 | -52.22653 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93054fff-509e-37c9-b05c-53f9b1b5fe1e | -16.08293 | -47.35025 | 2025-09-11 03:57:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README31.md)
