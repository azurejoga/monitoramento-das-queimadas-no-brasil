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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ee4670f-47a8-3003-a8f4-095270479ad2 | -3.69335 | -43.43361 | 2025-08-01 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7bc2ef3a-566a-3593-aeaa-f77a9d9c196d | -3.39274 | -47.49341 | 2025-08-01 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fa5d87b-fec4-3320-9d60-4b258f30d085 | -3.82194 | -41.56189 | 2025-08-01 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e6a11acd-8a77-37e2-a507-5b496860f09d | -3.5103 | -43.23776 | 2025-08-01 04:12:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a81ad3c0-65d4-3ef1-8a73-4e96aab9c0ac | -3.2512 | -43.26424 | 2025-08-01 04:12:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c5dae7c-d0b0-3f36-937e-68f7ce60e1c3 | -6.41319 | -41.1278 | 2025-08-01 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 045ee7ee-daac-3327-9692-6c139bb6c07e | -3.9114 | -49.0865 | 2025-08-01 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7197b29c-9c76-3be1-9d1a-9e25149322b5 | -5.38278 | -41.54349 | 2025-08-01 04:12:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 94128ed4-1489-3435-bf47-2e385b283c94 | -2.73711 | -42.53978 | 2025-08-01 04:12:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 945f4e48-2674-37ac-8034-0f430e33bb3d | -3.82348 | -41.56958 | 2025-08-01 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 62c58dac-fcf0-398a-aad8-a3293966ca1a | -4.31562 | -48.099 | 2025-08-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a73940c8-b15d-3165-ad32-6dc70b78d9ff | -6.41663 | -41.1283 | 2025-08-01 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a28f3582-7714-3dad-9909-8386ae07ab48 | -3.50312 | -43.24018 | 2025-08-01 04:12:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 67a9b874-b171-3b6d-bc64-d5647c046028 | -3.82249 | -41.55838 | 2025-08-01 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6f402d20-5728-34e5-8c23-b719ead08031 | -3.50643 | -43.2407 | 2025-08-01 04:12:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcda02c1-cfc3-336d-b75d-07fb178f5174 | -4.30617 | -48.105 | 2025-08-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 86a47105-759d-3fda-afa1-e4071609812e | -2.90277 | -48.24857 | 2025-08-01 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aff99c73-30a4-324a-b1be-7f71283f1f88 | -3.49925 | -43.24313 | 2025-08-01 04:12:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77f3b391-0307-3b99-9c34-99406a92d911 | -3.69002 | -43.43309 | 2025-08-01 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9cd7b8bc-3304-394a-835b-719e9f8f7d98 | -3.7011 | -43.42768 | 2025-08-01 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2521264d-5445-3b89-af11-096c81fd3159 | -3.69694 | -42.20486 | 2025-08-01 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 053d63e7-ab2c-3388-b98b-873b1f92cb76 | -3.98421 | -47.88526 | 2025-08-01 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22cd4e03-9e34-3f75-92fe-6055981b02f2 | -3.91091 | -49.08514 | 2025-08-01 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c209ea35-7018-35fe-828b-7f653c00f7f5 | -4.225 | -47.2177 | 2025-08-01 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 834db0f5-0903-38b3-bcf2-65da44b37707 | -3.10838 | -47.01239 | 2025-08-01 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7eca4775-fdea-3a16-8bfe-51b667923505 | -5.40782 | -44.42894 | 2025-08-01 04:12:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7f86046-2d64-3dba-8769-bdab147a483b | -3.82305 | -41.55485 | 2025-08-01 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 99b4f22f-924a-31f6-a843-bcd27143fe99 | -4.30268 | -48.10062 | 2025-08-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f4d6d41-0ede-330b-83ad-2ae45630702c | -3.69364 | -42.20434 | 2025-08-01 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 67983ad3-9553-3168-8866-2158c24a1727 | -3.59893 | -44.7995 | 2025-08-01 04:12:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa9e8bea-a299-359f-a0ff-ebfcf46375a8 | -3.82458 | -41.56255 | 2025-08-01 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ce69b241-0f6f-30b4-a14c-2b2c41e8eede | -3.82294 | -41.57309 | 2025-08-01 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 26869b8e-0e0a-3a69-b06e-831f24fcb69b | -3.91165 | -49.08076 | 2025-08-01 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10cec9be-3d12-3aa0-8638-f2e5de892228 | -3.50698 | -43.23724 | 2025-08-01 04:12:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1117fafd-208e-3cc8-bb11-bc7c674a04de | -4.3109 | -48.102 | 2025-08-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| dce4b4d3-cfbb-38de-81c0-f347a5eecc4b | -4.31028 | -48.10569 | 2025-08-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| e8eb77dc-6bbe-3da9-9770-8b2918f09dd8 | -5.87841 | -43.73339 | 2025-08-01 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b8f8396-7a3f-3c8e-b8ec-216bb4581e2c | -3.91211 | -49.0821 | 2025-08-01 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c9c2b5a6-4d57-3f16-bb42-4ab1991b37e6 | -4.31501 | -48.10269 | 2025-08-01 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6f2f3180-5b96-3bc9-a663-b633bcac5594 | -5.48108 | -42.15633 | 2025-08-01 04:12:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a241c971-36b0-3a13-9b83-709b6a57cc4e | -6.94976 | -37.3921 | 2025-08-01 04:12:00 | NOAA-20 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 30c86c0b-0dfb-3f3e-bce8-c6a71005756b | -6.42007 | -41.12882 | 2025-08-01 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7dab774c-75f6-3b24-8a50-04b896faae0b | -2.90349 | -48.29758 | 2025-08-01 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5f0518e0-27f0-37e1-bfdd-27083fd93b9f | -11.51209 | -44.30867 | 2025-08-01 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d9d181ff-ab3b-3ef7-bfb8-3f37f2ec7be8 | -9.56641 | -44.45259 | 2025-08-01 04:14:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dab3c4c6-2638-3caf-9705-09fc2628c13e | -10.1116 | -58.22826 | 2025-08-01 04:14:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 67a7cb85-d201-322c-bdaa-490322928139 | -11.16563 | -45.75406 | 2025-08-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42858a82-73f7-33ac-a869-9f556b1fb4d2 | -8.41275 | -47.50283 | 2025-08-01 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0a1dbd30-3340-3e6b-a30b-4ead2f8f66e7 | -9.39776 | -45.49586 | 2025-08-01 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 24da1aad-7474-3bc2-b667-04c1c54f40c9 | -10.08239 | -46.74754 | 2025-08-01 04:14:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3184077a-96e0-38df-84e4-4d198541ffd5 | -6.5445 | -56.2064 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a1076074-c4a6-3a18-be2d-87e4d8459324 | -10.08306 | -46.74357 | 2025-08-01 04:14:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 456c875f-4fc6-329a-9912-2a25c6cbaad2 | -8.15472 | -45.01714 | 2025-08-01 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 810bb1a0-78ac-3e29-878c-956b1bb26175 | -12.05203 | -45.44112 | 2025-08-01 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ecb15e4-52d4-3310-a5b6-b838c5780a2d | -6.51229 | -56.21626 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4b86f727-205c-3d1b-8268-633da5416bb2 | -10.43861 | -47.26176 | 2025-08-01 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 009d9e2f-8621-326d-9717-76df460904ad | -7.72564 | -45.09623 | 2025-08-01 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 47b6e7a6-9071-3cd9-9f90-b5190f45dcdd | -8.03717 | -43.12083 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 42.4 |
| 0c78b288-16a7-3bef-a2af-7cdd3b34173e | -6.54916 | -56.20509 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef95b45e-4993-3590-bfb0-417a74a1ccc4 | -9.5736 | -44.45016 | 2025-08-01 04:14:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd039dd6-45ee-39c9-b77d-b7747e55221f | -12.81098 | -45.4353 | 2025-08-01 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09b1b668-b1dc-3f18-a0fc-931f88b34103 | -11.51319 | -44.30165 | 2025-08-01 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96c42642-bc70-3252-87af-b04c8e9bdd00 | -8.3371 | -50.57447 | 2025-08-01 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 411467ff-2bdb-3fe1-a3b4-a5f8ae9d70a9 | -9.80008 | -47.04523 | 2025-08-01 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71a277ac-89bf-374f-8a8b-807f09ec6a98 | -8.03663 | -43.12431 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| b99998a4-9263-3a7b-ae39-54efc75fb13d | -7.58531 | -44.81136 | 2025-08-01 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d57a608-146b-36e0-ad76-7d85cf53db36 | -11.80867 | -48.79098 | 2025-08-01 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0d65939-801b-3ad8-b696-2e3c77b90b6d | -12.09493 | -44.98278 | 2025-08-01 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a415928-afab-3bd6-919b-61c172fdcbd6 | -12.26479 | -45.06892 | 2025-08-01 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ccbcf73-44e3-3922-ae3b-be100868217d | -6.5011 | -56.20149 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6b6926a-140c-3426-9236-49783b129ab7 | -8.95761 | -49.54628 | 2025-08-01 04:14:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 026e0b3c-c3d1-3b56-9f64-e1eb2c946f3a | -13.49823 | -45.64417 | 2025-08-01 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ad4b3e5-a081-31ad-b2d1-e12461fe63d5 | -9.40174 | -45.49279 | 2025-08-01 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 85a5b6c1-2dd5-32a5-bf5a-5627dd834da5 | -12.26204 | -45.06486 | 2025-08-01 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29612abc-37b8-3318-9640-70ff00a6d5bd | -11.75872 | -44.98196 | 2025-08-01 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c114d8ee-81f6-34a9-82b5-790d5d599318 | -10.44719 | -47.25465 | 2025-08-01 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64a73a5e-562a-34ba-97ee-5519312f8518 | -8.03826 | -43.11387 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 711c4818-504c-3b2b-a2ea-9a5dc14f3ed4 | -9.59295 | -44.4353 | 2025-08-01 04:14:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6c2c0c8-f2f3-3d0b-86f4-d5c3781d46cc | -7.7302 | -45.0895 | 2025-08-01 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a073c250-af7c-33c4-b413-46d9cd8595cd | -11.52918 | -44.24311 | 2025-08-01 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05f1ba84-c6fb-30f9-9e1e-10f3693afddb | -6.52797 | -56.20676 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a0fe4f4-4cdf-33e7-a3d1-04bf6ee2af1a | -11.75928 | -44.97842 | 2025-08-01 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ea75759-b14f-32dc-9f4c-6b3fc4667056 | -12.4326 | -44.71698 | 2025-08-01 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c642a3b2-aaf6-3a8d-a9ef-cb4329415628 | -10.40313 | -49.52935 | 2025-08-01 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d3a4139-d2b1-303a-b654-7429e38f051c | -8.04542 | -43.11143 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| de383d59-ef70-3fa1-9c49-134c423b9c4e | -9.74296 | -48.66661 | 2025-08-01 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a6860f2-8651-331a-8810-00288debe013 | -6.50558 | -56.21487 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1155b4d8-854f-3696-abbd-08f009fbd8dd | -8.3297 | -38.09121 | 2025-08-01 04:14:00 | NOAA-20 | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 72ec48e1-392f-3dfa-926f-eed7135253f4 | -7.04941 | -44.40461 | 2025-08-01 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35f0f439-f2cb-3b38-9145-4abad91b673a | -9.79796 | -47.04629 | 2025-08-01 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07892e3d-8fcb-3e8d-bba2-4aafa0f3e5cd | -6.57168 | -41.53434 | 2025-08-01 04:14:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 146e6059-8b1c-3553-ab39-095b0524905c | -7.04551 | -44.40757 | 2025-08-01 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45126a76-dbe4-39ac-b835-63ea807d9f39 | -8.3836 | -36.70326 | 2025-08-01 04:14:00 | NOAA-20 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e6257933-8ee6-3d8d-850a-e3aaefd6529e | -12.63875 | -48.09546 | 2025-08-01 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aed61732-6060-3444-938f-fa1d87d0c2b4 | -6.57112 | -41.538 | 2025-08-01 04:14:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 15f90734-82fa-3a29-8346-3d641a296503 | -11.51153 | -44.31218 | 2025-08-01 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d860be88-144e-310d-8d9c-f396698e9c3f | -7.72167 | -45.09932 | 2025-08-01 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b054a839-a257-3d9a-bf32-4b8d7e8a9eed | -12.04928 | -45.437 | 2025-08-01 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70bca8d7-838c-315b-a99f-b5b94f5b283e | -12.80766 | -45.43475 | 2025-08-01 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8736313b-5de3-30ae-94c4-5cd0a6844b55 | -12.27142 | -45.06995 | 2025-08-01 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README14.md)
