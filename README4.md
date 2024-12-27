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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf2e949a-b6dd-31dd-b790-4ec4d6d85dc8 | -4.70296 | -38.16398 | 2024-12-27 03:17:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6e1aea2f-378d-3728-9a8c-bb894c75bef6 | -4.51927 | -42.07885 | 2024-12-27 03:17:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 1224b89f-c51b-38d0-930d-08153fd6ad7c | -10.01233 | -38.40572 | 2024-12-27 03:17:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9db89647-6c95-3fed-8393-c9b3000c3136 | -3.0621 | -40.08253 | 2024-12-27 03:17:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e4bd662d-7e89-32fc-9e5b-de30f60d8e8b | -5.36357 | -39.3485 | 2024-12-27 03:17:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 99d104a9-a043-35f0-afa3-f2b8888a228e | -10.01181 | -38.40862 | 2024-12-27 03:17:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| da3362e9-1518-3a9d-b880-f17b8d92a19b | -3.06743 | -40.08538 | 2024-12-27 03:17:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6fbad35f-1467-30ae-b01c-8d8e7037bf68 | -4.52471 | -42.06261 | 2024-12-27 03:17:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 881bab23-2416-394d-b35b-d8bbf8cec152 | -10.52702 | -36.95815 | 2024-12-27 03:17:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| b0f2c2c5-963d-3e70-951a-24ba6a552ae1 | -3.0357 | -40.11761 | 2024-12-27 03:17:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ddd3e969-8b83-3f87-ab80-8c0cde75a10a | -5.39324 | -42.95752 | 2024-12-27 03:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e1144f3f-c8a1-381c-8a1e-54f42ee32c27 | -11.44383 | -39.5099 | 2024-12-27 03:17:00 | NPP-375D | SÃO DOMINGOS | BAHIA | Brasil | 2928950 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 132ba4bb-859e-3f9b-b525-d7ffb388309f | -4.52172 | -42.06546 | 2024-12-27 03:17:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a678b6ee-5f91-32df-abea-2a4ec8c05249 | -5.3946 | -42.9503 | 2024-12-27 03:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 03c439d5-1a15-3fe5-ac94-3d5b8cda6405 | -10.01128 | -38.41156 | 2024-12-27 03:17:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e70c5967-a533-3e48-9ea0-be10160feaf7 | -10.47 | -37.02029 | 2024-12-27 03:17:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c07c2fb9-8cde-36fc-8fae-ddd321bbac34 | -9.6075 | -35.90504 | 2024-12-27 03:17:00 | NPP-375D | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 76d173c4-dd6b-3098-a8bd-f560921f4f48 | -11.23509 | -41.88866 | 2024-12-27 03:17:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e84ee5f0-c32b-3fab-a93f-6e7f1e8bb4e7 | -10.013 | -38.41043 | 2024-12-27 03:17:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f6b67a26-d394-3f84-b7ce-d831af9a0d62 | -12.18736 | -41.35676 | 2024-12-27 03:17:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 95282c82-43a1-3ba1-adba-bf8a879d689a | -5.35768 | -39.34744 | 2024-12-27 03:17:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 41f2a886-d30f-32c7-b197-84b76c1e65c0 | -7.903 | -35.2239 | 2024-12-27 03:19:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 34052ffa-27dc-3d40-96b2-8162eae13ced | -7.4529 | -35.27582 | 2024-12-27 03:19:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3fc38614-0404-34f1-9220-e29c636b8510 | -8.05863 | -35.15012 | 2024-12-27 03:19:00 | NPP-375D | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 83e1382d-5687-33c3-9721-e7e80e37ac13 | -9.26232 | -35.58771 | 2024-12-27 03:19:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3645ea71-151a-3385-ad36-abca5bd26f45 | -7.82974 | -35.17457 | 2024-12-27 03:19:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| ea5229af-7f12-3358-bcbb-8541e01c5e05 | -7.89872 | -35.22315 | 2024-12-27 03:19:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dc21ee0d-d171-3317-94da-7c6bbf4bf32f | -9.33318 | -35.98253 | 2024-12-27 03:19:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 0d3a8bbd-034f-3e97-89c1-752342d76fad | -9.26302 | -35.58373 | 2024-12-27 03:19:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a4a5b3f8-93c9-3e9c-9613-56db070fdd2f | -8.06287 | -35.1509 | 2024-12-27 03:19:00 | NPP-375D | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 9efe78c7-bf0e-332f-bbbe-7f001e8c0cd3 | -8.06914 | -35.13981 | 2024-12-27 03:19:00 | NPP-375D | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| b726ac62-ffe5-3123-ad2d-39dccf4d0a9e | -7.834 | -35.17535 | 2024-12-27 03:19:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 941d81e5-ae6a-325f-8005-04aca6762d5a | -7.89802 | -35.2272 | 2024-12-27 03:19:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 11f0e691-1f06-3da5-a2df-5c59a58afde0 | -7.42749 | -35.05117 | 2024-12-27 03:19:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6c0d6396-550d-3422-a179-111ef4593532 | -7.1335 | -41.03621 | 2024-12-27 03:19:00 | NPP-375D | CAMPO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202133 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 302df2aa-1fed-3ee6-b1ad-4a664edbb0b4 | -9.32954 | -35.97734 | 2024-12-27 03:19:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e65f0c00-4eca-3e3c-87de-17fcaff5b106 | -9.25871 | -35.58309 | 2024-12-27 03:19:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 585caa45-5bcb-3688-b839-348e9e448ec4 | -15.71806 | -39.35854 | 2024-12-27 03:19:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e16995ff-71c1-358b-ba79-dd660f4965a6 | -7.90582 | -35.20765 | 2024-12-27 03:19:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4f4e162d-5ce7-3402-a216-ba97cc152214 | -9.09143 | -37.10931 | 2024-12-27 03:19:00 | NPP-375D | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 17856ceb-cae3-38ea-adc5-6c8cbe584919 | -8.06354 | -35.14697 | 2024-12-27 03:19:00 | NPP-375D | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| c45834c4-f2c3-3ad4-ba16-769000f82793 | -9.33393 | -35.97818 | 2024-12-27 03:19:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 6e1407e4-0db3-34f7-8823-e8182f4856f5 | -1.64893 | -45.87902 | 2024-12-27 03:38:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43e71ab3-8697-3147-85ff-064cdd578697 | -1.64159 | -45.86961 | 2024-12-27 03:38:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31b612da-7a60-3484-b5da-fc1cff817066 | -1.64345 | -45.87281 | 2024-12-27 03:38:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 834ecd6d-2eb3-3260-84f6-9a331f23e463 | -1.64793 | -45.87071 | 2024-12-27 03:38:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f200dca-f487-30d1-bfb0-175a020ae084 | -1.6471 | -45.87585 | 2024-12-27 03:38:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84f35a89-2fde-3118-8c9a-58736deb05b1 | -4.42824 | -46.56617 | 2024-12-27 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| b676704f-fbb4-33d6-b275-2d5159c3110d | -3.416 | -44.90583 | 2024-12-27 03:40:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| acc3cfe9-6fa4-3b08-8c09-2012ce13445e | -4.56414 | -44.12634 | 2024-12-27 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b9cded5-5b82-3cb3-8609-29d0e69095b8 | -4.9118 | -38.73844 | 2024-12-27 03:40:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 394a8d40-0526-36c6-afca-e2b04575e73d | -5.39257 | -42.95281 | 2024-12-27 03:40:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 48f84f3b-b1b4-3b82-ad75-e3e5a166a5e5 | -3.36787 | -44.20258 | 2024-12-27 03:40:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb55f14b-37d6-3c82-9fe7-3ec2933b0182 | -5.21013 | -44.91057 | 2024-12-27 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27568d0d-b5f8-3cce-ba2a-88c76d54bc62 | -2.99747 | -48.06395 | 2024-12-27 03:40:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3f6a9914-e68b-3a0a-bb23-7ca6446fe21f | -4.52323 | -42.0591 | 2024-12-27 03:40:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ce83d586-e8a6-33a2-9607-b204bc02b641 | -5.64151 | -43.72036 | 2024-12-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4fc91ed0-bb0e-3cd6-bb6d-b929020e1401 | -3.40506 | -44.89966 | 2024-12-27 03:40:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fd6e225-72d7-3230-b9df-55e85045a3dd | -5.64259 | -43.71405 | 2024-12-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a09297a2-1254-3715-b568-7da07451645e | -4.52712 | -42.06494 | 2024-12-27 03:40:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a5b8c31f-c2ac-3b88-bf82-4c282fa33eae | -3.02481 | -40.02455 | 2024-12-27 03:40:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 73fbff40-ca42-3ce1-b872-5256f0a27895 | -4.02701 | -46.17481 | 2024-12-27 03:40:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5152cfa-b3b7-3c8f-a3b3-4b3446de0a8d | -3.55822 | -40.85405 | 2024-12-27 03:40:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9fb246c5-6922-3a33-9957-fe26fc011f7e | -3.06918 | -47.77778 | 2024-12-27 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2fe63ea0-1e4a-3d54-992b-5a1db2bcac57 | -5.37224 | -44.84864 | 2024-12-27 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f738be04-980f-3617-9f58-4a34f91232e3 | -4.5224 | -42.06415 | 2024-12-27 03:40:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c88235d9-8d4c-3616-aa6a-c1b24ae82de0 | -4.42565 | -46.56964 | 2024-12-27 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d887b0f7-cf57-3bc1-b3d0-e79b761f5e7b | -3.6991 | -43.41972 | 2024-12-27 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3be761d9-32a9-3cb1-aca0-f8b0c855ffe8 | -5.39161 | -42.95837 | 2024-12-27 03:40:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c14b7964-f60a-31e7-b872-cf50c93b1589 | -4.56354 | -44.12979 | 2024-12-27 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d8ac43e-5aa5-36a7-a041-3844dfa3c389 | -4.42913 | -46.56123 | 2024-12-27 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 58bce2a2-7e33-3a5f-a832-c36e7cb5e868 | -4.2426 | -41.92395 | 2024-12-27 03:40:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f8f086a3-1a7d-3e89-a3e0-59ea7b95c5e0 | -3.07216 | -41.90006 | 2024-12-27 03:40:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 69c66b2e-bbb8-3e06-9b44-f4133d28f51b | -5.39753 | -42.95361 | 2024-12-27 03:40:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bd9e712b-0bd6-35fc-af92-52dbfd71076e | -5.36892 | -44.84919 | 2024-12-27 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5fd0755f-f641-3c43-8653-bd35ddfff609 | -5.64886 | -43.70863 | 2024-12-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 56b2e1aa-6541-3308-a291-de7571419c09 | -3.06369 | -47.77515 | 2024-12-27 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ae76fe22-b7d9-3a64-950f-84ec2064a056 | -5.64366 | -43.70779 | 2024-12-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 18221059-3efe-37c8-a148-94bb80f8bc7a | -5.13242 | -43.23777 | 2024-12-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8956ff54-4cb0-31bb-9315-e4d7739f1706 | -8.05941 | -35.1215 | 2024-12-27 03:40:00 | NOAA-20 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7c57a5ec-0866-362b-a8f7-d1758c3959b6 | -4.432 | -46.5708 | 2024-12-27 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b2b50c92-8f3e-3183-af7f-aed4eac24e6b | -3.37344 | -44.20348 | 2024-12-27 03:40:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da384ddd-208e-3c59-a899-6186943d78a5 | -5.64725 | -43.71805 | 2024-12-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6ad5117e-cdf5-3a86-a09f-9c2af94eb161 | -5.64313 | -43.71091 | 2024-12-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 454bda82-a864-339f-a14d-b3ddd0dd9a25 | -4.55147 | -44.13495 | 2024-12-27 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43688af4-23b1-3760-8945-af12d40b606c | -5.94678 | -44.45027 | 2024-12-27 03:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6342b5b4-8cbe-3909-9dd3-b6c464313b27 | -5.22005 | -41.27563 | 2024-12-27 03:40:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2bdfda34-9ca7-3efe-b038-9126ca392046 | -4.52156 | -42.06919 | 2024-12-27 03:40:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c45beb84-1d1a-345f-9924-ac32c521815e | -5.35494 | -39.34269 | 2024-12-27 03:40:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 9d522df2-4251-3581-bb4d-d30a446b0110 | -5.2304 | -44.72695 | 2024-12-27 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a2045b3-b49b-3ac9-8c67-1cca44b36702 | -3.6955 | -43.40917 | 2024-12-27 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dfaf352c-1b55-3da1-9744-ceadaf3c773b | -4.42102 | -46.56991 | 2024-12-27 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8e33c71a-1f85-39d9-b1f1-f667f8d563a8 | -5.22112 | -41.27374 | 2024-12-27 03:40:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b319351d-9e55-389a-b6e7-58ca4c3bfadb | -3.40988 | -44.90311 | 2024-12-27 03:40:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8dba61bf-e6d4-3be3-80ff-951150d75ec7 | -4.03234 | -46.18121 | 2024-12-27 03:40:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c9f8914-3377-3ca8-9f74-fcc7c759c7b7 | -3.03498 | -40.12199 | 2024-12-27 03:40:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e2cc877e-f0ea-3fa3-ae18-0d1c61541b9f | -3.69964 | -43.41654 | 2024-12-27 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e81b1567-6403-3d75-a1b2-6a459b012781 | -9.2597 | -35.58669 | 2024-12-27 03:40:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ae313436-8614-30cf-8a3a-61e4b29fae19 | -2.99495 | -48.05481 | 2024-12-27 03:40:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d45cd76-3002-354d-b19d-ddae8a569fc3 | -5.46101 | -36.65802 | 2024-12-27 03:40:00 | NOAA-20 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README5.md)
