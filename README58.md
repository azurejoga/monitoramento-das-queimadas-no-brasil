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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3de9eb4d-c432-304d-89e4-20f7daf5e6a1 | -3.53013 | -44.94851 | 2025-11-15 11:57:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5d123b50-32e3-3407-afc4-9eb2012432db | -6.89303 | -42.05598 | 2025-11-15 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 3aac6702-cb87-38e6-aad6-12d9d1a83023 | -4.70308 | -40.12466 | 2025-11-15 11:57:00 | TERRA_M-M | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 724cbec0-c1ca-3e6b-8107-aa35249b15db | -4.19461 | -45.45022 | 2025-11-15 11:57:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f5c75142-9a36-32a9-ae25-c46388f44050 | -6.2644 | -41.41079 | 2025-11-15 11:57:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| b8a646c1-6d6d-3458-bea0-108dd0dd284a | -3.07206 | -45.19727 | 2025-11-15 11:57:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 46b0075b-1e82-381c-8a33-06bb75d4e844 | -4.74609 | -39.37975 | 2025-11-15 11:57:00 | TERRA_M-M | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 14.5 |
| b1cc288c-2e15-3af9-aa14-12247792fcb8 | -7.10964 | -42.73464 | 2025-11-15 11:57:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 3536839c-87db-394a-bc30-e35519adc20b | -3.67164 | -42.58031 | 2025-11-15 11:57:00 | TERRA_M-M | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Caatinga | 42.0 |
| 42434cd3-df19-3db7-94b8-4c782c6f8adb | -6.33914 | -38.51983 | 2025-11-15 11:57:00 | TERRA_M-M | VENHA-VER | RIO GRANDE DO NORTE | Brasil | 2414753 | 24 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 9215de5f-7bcd-356b-9953-314e0590c40e | -4.25775 | -44.20204 | 2025-11-15 11:57:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| c6093a6f-3342-33c7-89d3-2c9a2ff45231 | -6.08301 | -41.64919 | 2025-11-15 11:57:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 8938f933-bb61-307a-99f7-b2b991c3a99e | -4.90675 | -44.05611 | 2025-11-15 11:57:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 79f0ac97-484f-3df5-b2fc-130527b7f6e9 | -3.75328 | -42.44898 | 2025-11-15 11:57:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7e914043-d471-3e7e-a48e-a4b503c70d66 | -6.64367 | -43.92152 | 2025-11-15 11:57:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 44501115-27c6-31e1-9c55-78e3fdd6d90e | -3.53437 | -44.65866 | 2025-11-15 11:57:00 | TERRA_M-M | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 517e3bc9-dc6a-3808-992b-b2ab777ee6ca | -3.30858 | -39.48557 | 2025-11-15 11:57:00 | TERRA_M-M | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 7ad86cee-ed15-3f76-8734-05695a8c4aae | -7.10837 | -42.7435 | 2025-11-15 11:57:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 8ecce73b-c1b8-3ac1-b67f-c8c003879712 | -4.17242 | -39.16309 | 2025-11-15 11:57:00 | TERRA_M-M | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 2191721e-83cf-36e7-a5f6-6a1307b21d28 | -3.42923 | -42.46523 | 2025-11-15 11:57:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 20.6 |
| d3570ca6-3500-310d-8f33-1c4c3d1c4014 | -3.95446 | -40.78804 | 2025-11-15 11:57:00 | TERRA_M-M | GRAÇA | CEARÁ | Brasil | 2304657 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 3b281702-bf6d-3c10-a50e-d4eb7a5a7b1a | -6.73874 | -42.9521 | 2025-11-15 11:57:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| ca29e071-eb51-31a6-82d8-4d3292aad88e | -4.56634 | -38.6641 | 2025-11-15 11:57:00 | TERRA_M-M | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 56eaad87-f083-3021-bf72-a8ab196dc4f7 | -3.46816 | -42.31908 | 2025-11-15 11:57:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| c3691ceb-4556-3e71-bac2-2045b1e604e2 | -3.36707 | -41.61055 | 2025-11-15 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 532dd448-4957-378b-bc53-6406f77795b9 | -5.18932 | -44.27241 | 2025-11-15 11:57:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5672a8be-541c-3943-bdeb-e90e45bbd2dc | -7.38632 | -39.51734 | 2025-11-15 11:57:00 | TERRA_M-M | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 48.6 |
| bc3114ed-1483-3dce-a5c8-ead091177e34 | -7.38802 | -39.50496 | 2025-11-15 11:57:00 | TERRA_M-M | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| d3971b87-d8cd-36ea-9b4b-b4341edf4cd9 | -6.44871 | -38.393 | 2025-11-15 11:57:00 | TERRA_M-M | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 19.4 |
| c6e6134a-fecd-3aea-a26a-1ac924d6da6d | -3.67572 | -40.60397 | 2025-11-15 11:57:00 | TERRA_M-M | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| d1b11a49-3d2b-3f45-8fa8-2761bbb3bd4e | -3.49881 | -45.02898 | 2025-11-15 11:57:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 48c2111c-eae9-3e52-ad8d-b5f93ce0d714 | -3.45937 | -42.31785 | 2025-11-15 11:57:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 46.1 |
| c002d216-de50-3461-92de-3c991c61194b | -4.52244 | -40.34356 | 2025-11-15 11:57:00 | TERRA_M-M | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| b79c7f3b-35e0-3fa8-b364-f319e200774b | -3.35959 | -42.18202 | 2025-11-15 11:57:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 28.9 |
| ae06d4b2-8cfb-3ead-91fc-2e7c6c36c2c0 | -4.30083 | -40.2943 | 2025-11-15 11:57:00 | TERRA_M-M | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| f9c88471-2102-308b-b7eb-87f926e79154 | -4.43968 | -43.65247 | 2025-11-15 11:57:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| bceeda7a-4d37-3453-95b9-47dc15838812 | -3.47959 | -45.64415 | 2025-11-15 11:57:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 79a78581-c84b-3e74-8eb4-49cfa1b5ee54 | -4.35736 | -45.53028 | 2025-11-15 11:57:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 10d66424-688e-338b-913d-fc300b0273a9 | -4.74505 | -39.38548 | 2025-11-15 11:57:00 | TERRA_M-M | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 7eb9bb31-6793-3e58-94a2-939b3053cd44 | -5.69999 | -38.91549 | 2025-11-15 11:57:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 603b94a7-27de-3458-99f1-af76cc9a533c | -5.22833 | -38.49235 | 2025-11-15 11:57:00 | TERRA_M-M | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 15.4 |
| beefc75f-af39-3119-9da1-9431c2859fc4 | -3.66114 | -44.8162 | 2025-11-15 11:57:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 30.8 |
| b21ffaea-2d19-305e-8edc-4febf16f598d | -3.48072 | -42.16912 | 2025-11-15 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 7575913b-a323-3cb1-a881-8e4a9e573e43 | -3.32319 | -42.31077 | 2025-11-15 11:57:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| bff80357-1bb0-3d16-b8b9-26ec88b8cae8 | -3.5134 | -41.62504 | 2025-11-15 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 32.8 |
| 44e72569-6828-3f05-b20b-5e85c0acef1a | -3.14378 | -42.8358 | 2025-11-15 11:57:00 | TERRA_M-M | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1ffa0419-ce80-3bdd-944f-5b8a5ffacfc0 | -5.72378 | -42.36731 | 2025-11-15 11:57:00 | TERRA_M-M | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 946f2c08-9d80-3056-be35-c2a5be491b60 | -3.67128 | -42.37759 | 2025-11-15 11:57:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 39.6 |
| f877c321-33cb-3231-918e-17b8edd0a0bf | -3.40145 | -41.43317 | 2025-11-15 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 95.1 |
| 8ded4511-5ff8-399f-9896-99d5d0570c5d | -6.81446 | -38.50039 | 2025-11-15 11:57:00 | TERRA_M-M | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 28.8 |
| 7c8661f3-1223-35e5-8ce4-ea2c1965aea8 | -3.48573 | -42.00882 | 2025-11-15 11:57:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 46b16ba8-8213-3979-aefa-044c28acaf43 | -7.32969 | -40.37677 | 2025-11-15 11:57:00 | TERRA_M-M | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 644b6a63-d1f6-3809-9cf1-ca49b0f9dec6 | -4.75922 | -43.3604 | 2025-11-15 11:57:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 05abe552-a7e1-3f0b-ab18-62ebace2227b | -4.32179 | -38.47344 | 2025-11-15 11:57:00 | TERRA_M-M | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| bb785198-be41-33a8-951a-593f91ea18e3 | -3.36545 | -40.18632 | 2025-11-15 11:57:00 | TERRA_M-M | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 1b0223d0-2bb5-3c93-8839-a9ad90afc5cb | -2.15542 | -46.00185 | 2025-11-15 11:57:00 | TERRA_M-M | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e2498d17-d8e9-3dd8-8d67-321c7f12c549 | -7.33117 | -40.36597 | 2025-11-15 11:57:00 | TERRA_M-M | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| a6fc46a6-01d8-3e84-a8b1-b4141e50d1dc | -3.45307 | -42.54879 | 2025-11-15 11:57:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b9c54b65-2f64-3756-a788-4b474cbdc6a7 | -4.25913 | -44.19263 | 2025-11-15 11:57:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 2e1870de-579c-3878-ac89-2bf541ba939e | -6.77881 | -44.76564 | 2025-11-15 11:57:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| b92c04ac-74a2-3597-aa87-a65d78de8b82 | -4.90807 | -44.04693 | 2025-11-15 11:57:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d1f70b16-dde7-3eb9-8316-4c22888f8f62 | -5.64482 | -43.62004 | 2025-11-15 11:57:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 158fd363-6734-343d-8eac-ce09b80560c6 | -6.12978 | -44.09314 | 2025-11-15 11:57:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 0df6c280-c119-3fa0-9362-df356284431d | -3.66375 | -42.36763 | 2025-11-15 11:57:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 3205180c-5c84-3a9d-90d0-32ddeb8ccee7 | -6.15608 | -48.05179 | 2025-11-15 11:57:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 33598d51-1ab9-3d68-9c59-cb6bc00425c0 | -4.05382 | -40.40127 | 2025-11-15 11:57:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| fa0fc26c-5b45-3fdf-9985-e66b76f28bca | -5.4515 | -39.52946 | 2025-11-15 11:57:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| a003c406-164d-3aa9-af00-b257b2ead838 | -4.74669 | -39.37393 | 2025-11-15 11:57:00 | TERRA_M-M | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| e3126f18-bd9e-3d46-b5be-46b0bdc3afd9 | -5.197 | -44.283 | 2025-11-15 11:57:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 564f6563-3161-3e3d-9406-fab101aea6fc | -2.87762 | -42.32446 | 2025-11-15 11:57:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e24dfe4e-5d3d-3188-a3dc-35a553b0c726 | -3.48699 | -42.00003 | 2025-11-15 11:57:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 6893ce71-a8fd-3596-907e-24b60b687f41 | -6.98328 | -44.18811 | 2025-11-15 11:57:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c61cfacf-aafb-3209-93f0-25716b5989cc | -4.46821 | -42.88124 | 2025-11-15 11:57:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3f354251-b49b-3e4a-8d50-534edf6a9476 | -3.23814 | -41.92916 | 2025-11-15 11:57:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 33.5 |
| abed0a5b-29a4-3e11-8d11-cac89ab9a194 | -3.79253 | -45.31699 | 2025-11-15 11:57:00 | TERRA_M-M | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 92fedde3-d4b1-3d2d-9f92-ae2d537344f1 | -11.12294 | -47.05881 | 2025-11-15 11:59:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f87a8963-83a2-3d82-b9a5-7bd0cb9b6a01 | -8.46122 | -39.80568 | 2025-11-15 11:59:00 | TERRA_M-M | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 20.5 |
| b3bbf6cd-6c77-3439-882e-fdd3edf822ed | -11.74658 | -45.33146 | 2025-11-15 11:59:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| d036be08-b0bb-3862-90b2-1be08ac320d7 | -13.21333 | -43.40123 | 2025-11-15 11:59:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b0d87555-3ef3-3bbb-a33d-4bd15eaa6dca | -11.20197 | -41.61405 | 2025-11-15 11:59:00 | TERRA_M-M | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 7b07920e-f13e-37a5-8e69-86fc7ec18ffd | -8.18003 | -45.03342 | 2025-11-15 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 711.0 |
| c0ac096a-aa7b-33d1-8516-14a149f244b5 | -17.70692 | -44.15377 | 2025-11-15 11:59:00 | TERRA_M-M | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1e0a048b-43c7-3e9f-af66-e24886ca6f3c | -13.01428 | -43.04576 | 2025-11-15 11:59:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 140.0 |
| f8ad64dd-21e9-3ba5-ab48-9917c1a8bcaa | -7.62161 | -46.53642 | 2025-11-15 11:59:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7e4b916a-640f-3a83-853a-9530ce151f97 | -7.43893 | -45.29572 | 2025-11-15 11:59:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| d2c2f498-887a-3d30-bb4e-564fe699622f | -12.01461 | -43.27305 | 2025-11-15 11:59:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| ef33ffc4-037f-3dfc-a28a-abd7959fdab1 | -12.49327 | -47.28791 | 2025-11-15 11:59:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 200c07cc-1883-3711-aaf2-dab96fa91c6e | -8.19686 | -45.0418 | 2025-11-15 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 21dc7f50-8c62-360c-a55e-2549ad9ae3f0 | -14.23665 | -43.53542 | 2025-11-15 11:59:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 82199813-33db-3c55-bbce-4149efec0983 | -12.49155 | -47.29899 | 2025-11-15 11:59:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b66f80e0-eb25-3256-9cec-e84709dd69ea | -9.21522 | -45.33776 | 2025-11-15 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 268c44f1-1e8f-3341-84d1-1baf1515afa5 | -7.49474 | -42.55934 | 2025-11-15 11:59:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 34.0 |
| 4ec8487a-6a4d-3799-81ae-8dd165373c6f | -17.70824 | -44.14415 | 2025-11-15 11:59:00 | TERRA_M-M | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0a4c90fc-62f6-37c3-8903-8eca7b380daf | -12.4587 | -43.1977 | 2025-11-15 11:59:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d79623a3-244b-3f83-9cc0-f1f07e57003b | -14.26641 | -42.84772 | 2025-11-15 11:59:00 | TERRA_M-M | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 79894f53-ca4c-3530-a3e6-7ab4ffd80808 | -8.06226 | -43.10833 | 2025-11-15 11:59:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.8 |
| fd9c8a0d-3140-3599-90d9-e7bcfa71aba6 | -9.4884 | -47.27686 | 2025-11-15 11:59:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| caa21ea8-f91d-39f4-8588-30a69f0c400a | -12.67629 | -46.76291 | 2025-11-15 11:59:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| fb6904b7-b77f-3f2a-b6f6-7b0e170b28c0 | -13.02331 | -43.04702 | 2025-11-15 11:59:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 228.6 |
| e77e142f-2600-3265-87ea-d80e59e80aa6 | -8.38008 | -45.05208 | 2025-11-15 11:59:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |


[Clique aqui para ver as próximas entradas](README59.md)
