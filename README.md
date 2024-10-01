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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e93c25d9-38d7-3404-b1f7-f09758a3190c | -22.8979 | -43.691898 | 2024-10-01 00:02:35 | METOP-C | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8f34f757-55b6-3d96-8a50-9ecf3d1cd7ea | -22.7185 | -46.6413 | 2024-10-01 00:02:45 | METOP-C | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eafa72fe-b24b-3bd1-aab7-f45918f1c72a | -22.7089 | -46.642799 | 2024-10-01 00:02:45 | METOP-C | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b712d887-122c-3c63-9115-011c66e801ac | -19.9447 | -44.266201 | 2024-10-01 00:03:25 | METOP-C | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 004e27b3-0551-3520-bd89-1908f92c5ce3 | -19.996901 | -44.5168 | 2024-10-01 00:03:25 | METOP-C | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c3a682ad-9c12-3bab-b066-5d2791e0cc1b | -20.006599 | -44.515099 | 2024-10-01 00:03:25 | METOP-C | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 463bc01e-7a71-3dcf-8060-8c2d5d27a0b4 | -19.2428 | -43.340698 | 2024-10-01 00:03:34 | METOP-C | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cab4792e-c4e3-3f92-931c-2028f47f881a | -19.683599 | -47.194199 | 2024-10-01 00:03:38 | METOP-C | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 95054983-5d01-31dc-900c-5f2b7c95ab9e | -19.688601 | -47.2262 | 2024-10-01 00:03:38 | METOP-C | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 861d36fd-e1be-3e37-804c-43f1803acff1 | -19.673901 | -47.195702 | 2024-10-01 00:03:38 | METOP-C | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1bb09842-9af4-3c28-93cf-77ccdb52bfd1 | -19.6789 | -47.227798 | 2024-10-01 00:03:38 | METOP-C | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b44beb32-b184-30ab-b8b3-63bab8b0e489 | -18.849899 | -42.556099 | 2024-10-01 00:03:39 | METOP-C | VIRGINÓPOLIS | MINAS GERAIS | Brasil | 3171808 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dc89be99-f22e-366c-92c7-4a01e34aa3ca | -18.8402 | -42.557999 | 2024-10-01 00:03:39 | METOP-C | VIRGINÓPOLIS | MINAS GERAIS | Brasil | 3171808 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ba765600-8670-3bd8-91ea-9b8ed0c6ed4e | -18.5306 | -43.351601 | 2024-10-01 00:03:46 | METOP-C | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 240bb1fe-3cf9-317d-a286-407a6d80f35e | -16.959101 | -42.2299 | 2024-10-01 00:04:09 | METOP-C | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d6790ec1-f484-31d7-b30b-5db8305be25c | -14.718 | -48.716702 | 2024-10-01 00:05:06 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0416ff77-e00d-37e6-bcd7-f46242133153 | -14.7084 | -48.718399 | 2024-10-01 00:05:06 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b450bc87-49ed-3528-8d2f-b117c452d761 | -13.4386 | -43.766499 | 2024-10-01 00:05:12 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b9a2ca3e-19d9-3fcc-9580-c1bed72efd3b | -10.2717 | -36.486 | 2024-10-01 00:05:38 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b1606e51-9706-33d1-b258-0935f66c4fb5 | -10.2733 | -36.493 | 2024-10-01 00:05:38 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d6436b7f-8241-3c57-8a8a-f4d5fd5974bc | -10.2619 | -36.4883 | 2024-10-01 00:05:38 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bbdf4c12-0a3c-3ec9-933f-fa2f7db0e575 | -10.2635 | -36.4953 | 2024-10-01 00:05:38 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6cfb69c4-f2cd-310f-ae34-1665e106eca6 | -10.2216 | -36.357601 | 2024-10-01 00:05:38 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ff6c2514-f15a-3485-b6a2-911ed1b34622 | -10.1541 | -36.557301 | 2024-10-01 00:05:40 | METOP-C | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 1238394a-ea1c-3a93-ad89-5c179d7a1c64 | -10.1556 | -36.564301 | 2024-10-01 00:05:40 | METOP-C | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 31224621-086b-3027-88ff-f6bd6e760479 | -10.0438 | -36.391399 | 2024-10-01 00:05:41 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 7b122210-b202-39ff-aac8-6a33fef584e0 | -10.0454 | -36.398399 | 2024-10-01 00:05:41 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| ac4095ec-47f1-38b3-aa2f-74690b27eef1 | -10.047 | -36.405399 | 2024-10-01 00:05:41 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 749d0236-8ee1-3aea-b3b1-565b9af04143 | -11.2455 | -43.362801 | 2024-10-01 00:05:46 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 40cec39e-3d23-317f-b074-cba27bf7e326 | -11.2482 | -43.3759 | 2024-10-01 00:05:46 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 24056f89-a220-36b6-973b-b3837ec13da5 | -11.2584 | -45.631599 | 2024-10-01 00:05:54 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a6814607-15b2-33a3-a621-ed9071fbb10b | -11.2487 | -45.633598 | 2024-10-01 00:05:54 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8853a9e8-7de7-3e15-b17d-2ca6f8fc27b1 | -11.2525 | -45.652401 | 2024-10-01 00:05:54 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a1584cfb-6600-3002-893d-516ddd687be3 | -11.1113 | -45.602699 | 2024-10-01 00:05:56 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ec5276ee-cf64-3468-8eb4-19baa92e4d8e | -11.115 | -45.6213 | 2024-10-01 00:05:56 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 919d0578-19d9-314c-8a33-fbdd136deb03 | -11.1052 | -45.623199 | 2024-10-01 00:05:56 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| beb948f3-5404-3117-b5ac-a4e230d40e8d | -11.0992 | -45.643799 | 2024-10-01 00:05:56 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 46212671-78f5-34ce-be86-e1e31ae47938 | -11.1029 | -45.662498 | 2024-10-01 00:05:56 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1c8dedb4-3ca3-31fe-9805-3ea188e28535 | -11.0932 | -45.664398 | 2024-10-01 00:05:56 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 682d166a-5f5a-3dad-8ff4-75df792f610e | -10.8565 | -44.7892 | 2024-10-01 00:05:57 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4c52e293-c3af-33f2-a3c2-f2eaef661e9f | -8.5179 | -35.109798 | 2024-10-01 00:06:01 | METOP-C | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 67dfeaba-cd0e-302a-8163-e34d3705511d | -9.2436 | -40.814999 | 2024-10-01 00:06:10 | METOP-C | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a37d3128-b6e3-3335-8902-8d4d207a1f44 | -9.2455 | -40.823601 | 2024-10-01 00:06:10 | METOP-C | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| df693e00-b683-3fb3-92e7-2495c0189ecd | -9.0142 | -40.563499 | 2024-10-01 00:06:13 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 62fdb5eb-5163-3435-96f4-0e329e086e21 | -7.5123 | -34.871899 | 2024-10-01 00:06:16 | METOP-C | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a73e2269-f8d4-3c5e-b195-e6c2b76abce8 | -7.5142 | -34.879902 | 2024-10-01 00:06:16 | METOP-C | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1acf5270-2489-36dd-8c0c-e80740200e2c | -7.5161 | -34.887901 | 2024-10-01 00:06:16 | METOP-C | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b8ab533b-c8f6-3c8f-8355-06291d5aa361 | -7.5044 | -34.882198 | 2024-10-01 00:06:16 | METOP-C | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e876a76c-88dd-376b-aa5c-6f0cee441ae5 | -7.5063 | -34.890202 | 2024-10-01 00:06:16 | METOP-C | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6a0912e3-ecb7-3529-90fe-7ec7c8a766fb | -7.1073 | -35.2999 | 2024-10-01 00:06:24 | METOP-C | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 4d8bd558-7647-3ab3-8c60-69658e84b9ae | -7.1091 | -35.307701 | 2024-10-01 00:06:24 | METOP-C | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 2debc425-e480-33bb-a5b4-16621698675a | -6.7409 | -35.102402 | 2024-10-01 00:06:30 | METOP-C | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e616d34c-0089-3a37-8652-9c9aa87828b4 | -6.7428 | -35.110401 | 2024-10-01 00:06:30 | METOP-C | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ebfa11fd-91f7-3c1b-b1db-7253d49d45cd | -6.6495 | -35.064499 | 2024-10-01 00:06:31 | METOP-C | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c5163ac3-a0ca-391c-94ef-6b64ddbb29f1 | -6.6514 | -35.072498 | 2024-10-01 00:06:31 | METOP-C | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f071104d-b865-3866-b86b-7e24fa5e4d37 | -8.0353 | -41.0592 | 2024-10-01 00:06:31 | METOP-C | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e1cc1c67-a91b-365d-83cd-fc740c0f7dc1 | -6.6533 | -35.080502 | 2024-10-01 00:06:31 | METOP-C | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 88450be5-9ca1-3d69-a745-ddadc06c1c07 | -6.6416 | -35.074799 | 2024-10-01 00:06:31 | METOP-C | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d5d7eb58-a13f-3cf8-ad18-da0659bb85b9 | -8.5206 | -44.690399 | 2024-10-01 00:06:35 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1e39d622-af28-3616-bd77-14158cd100b5 | -8.5237 | -44.705101 | 2024-10-01 00:06:35 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0526bc78-004c-307d-be48-f6c41f13b46c | -9.1947 | -48.618198 | 2024-10-01 00:06:38 | METOP-C | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4421e4e8-bc68-3a21-9444-ef8fc55cd414 | -9.185 | -48.620098 | 2024-10-01 00:06:38 | METOP-C | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2fee53cb-e74e-37e9-beb6-526fcf312f7a | -7.2305 | -39.382702 | 2024-10-01 00:06:38 | METOP-C | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ccb187a0-ae2f-3625-aabd-2dfa096c5584 | -7.0712 | -39.1325 | 2024-10-01 00:06:39 | METOP-C | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e86a4eb9-08b6-360b-afb3-6557d820a186 | -7.0728 | -39.139599 | 2024-10-01 00:06:39 | METOP-C | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ab077d81-e837-32ef-ad13-0648aec36f22 | -7.0744 | -39.146702 | 2024-10-01 00:06:39 | METOP-C | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6686b440-b2f7-32da-b1b2-790afbc0dfe8 | -8.7365 | -47.097599 | 2024-10-01 00:06:40 | METOP-C | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 51d6cad4-3fec-3e48-b52c-c14649881400 | -8.7409 | -47.119301 | 2024-10-01 00:06:40 | METOP-C | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d40aae5f-0da4-34a9-a7d3-44897e4dc256 | -8.7268 | -47.099602 | 2024-10-01 00:06:40 | METOP-C | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d187ac3b-3e48-339f-915b-c57e7f359806 | -8.7312 | -47.1213 | 2024-10-01 00:06:40 | METOP-C | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 57e945fa-76f3-344d-a367-0dc5f9a8eef9 | -7.8502 | -43.077599 | 2024-10-01 00:06:41 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 01cb64a3-8d10-38d6-932f-362167f6376b | -7.838 | -43.0686 | 2024-10-01 00:06:41 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 95b27e45-bc01-3cb3-b95a-e07ba4b2186d | -7.8404 | -43.0797 | 2024-10-01 00:06:41 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 720b6ce0-51e6-3fbe-9f6b-bfa8eeff2cb7 | -7.8428 | -43.0909 | 2024-10-01 00:06:41 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fa87aac6-be2c-392a-a887-fde9a7cebd8c | -7.6848 | -42.9743 | 2024-10-01 00:06:43 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9121514f-c83e-3e5e-b042-5e02e3465130 | -7.6871 | -42.985199 | 2024-10-01 00:06:43 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0d12bbf6-89ce-37bd-bf34-78587e85a524 | -7.6895 | -42.996201 | 2024-10-01 00:06:43 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1342c59b-3f0e-36d4-938d-87e511a91395 | -5.9129 | -35.3111 | 2024-10-01 00:06:44 | METOP-C | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9478881c-a86e-3620-8bf2-39615c4be543 | -5.9148 | -35.319 | 2024-10-01 00:06:44 | METOP-C | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7d367f84-81c9-3530-ab2a-eefb862ee465 | -7.2797 | -42.2425 | 2024-10-01 00:06:47 | METOP-C | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| aee80841-8665-3bc6-b91c-3b4d971f2a36 | -7.2699 | -42.244598 | 2024-10-01 00:06:47 | METOP-C | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 87730970-9531-34be-8021-7c81efe85339 | -7.2721 | -42.254299 | 2024-10-01 00:06:47 | METOP-C | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ee0055da-c0e2-3c2d-ba26-e94f79669b33 | -7.2966 | -43.779202 | 2024-10-01 00:06:52 | METOP-C | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5fe91a67-56fe-39b3-af83-32ab3c6b9abe | -7.2868 | -43.7813 | 2024-10-01 00:06:52 | METOP-C | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 450eb8b9-f8eb-3d70-b00a-f1069a09c28d | -5.2504 | -36.184601 | 2024-10-01 00:06:58 | METOP-C | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 4af8a0f3-20b8-3580-ac93-3ab4fffe1316 | -6.1753 | -42.952599 | 2024-10-01 00:07:08 | METOP-C | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cd3d69b0-b469-34d7-b00c-d21ec03bade2 | -5.5948 | -41.353001 | 2024-10-01 00:07:11 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 159dff38-8e55-30b1-8c85-d18d5fca1e32 | -5.5966 | -41.361301 | 2024-10-01 00:07:11 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 24bd4ba7-2408-3307-9079-3bc2c6686da6 | -6.2365 | -44.119598 | 2024-10-01 00:07:11 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1ee2dbc0-36fd-398f-991f-34ca2cb0dc53 | -6.2392 | -44.131901 | 2024-10-01 00:07:11 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c38ed28-2eb7-331b-8c77-dc1d9f6bd741 | -6.2419 | -44.144299 | 2024-10-01 00:07:11 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d92b96a-a432-3448-a27c-8a93d17057e9 | -6.2267 | -44.1217 | 2024-10-01 00:07:11 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc221dc9-e9b2-3b70-bb49-a574f5074628 | -6.2294 | -44.133999 | 2024-10-01 00:07:11 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d588bfc-3150-3f58-8ed6-aeb07a79b91b | -6.9557 | -47.5723 | 2024-10-01 00:07:11 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4efae915-db6d-3600-a813-79a98f938257 | -6.9603 | -47.594299 | 2024-10-01 00:07:11 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f127b09d-8ecd-3a4d-bd59-1c9188709627 | -6.0781 | -44.2836 | 2024-10-01 00:07:14 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57f60f55-0a8e-325e-a253-a20bd963f6e0 | -6.0809 | -44.2962 | 2024-10-01 00:07:14 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1876b2e4-ddd9-3864-a44c-05134d39e2b7 | -5.8787 | -43.6991 | 2024-10-01 00:07:15 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1432cc2-c092-3d79-879b-8112a2ad60e1 | -5.8812 | -43.710499 | 2024-10-01 00:07:15 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc419e9a-ae74-3c50-9f80-3630be3992e7 | -5.9725 | -45.346699 | 2024-10-01 00:07:19 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
