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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bca71389-7650-3002-b295-a6e27d66fa94 | -18.33423 | -54.27051 | 2025-03-28 05:18:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03b3d61c-73cd-3592-9d9e-b70881b10f2f | -20.59671 | -56.10165 | 2025-03-28 05:18:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a2b233f-9bd3-34a5-820c-9cac73db1659 | -18.53759 | -56.18499 | 2025-03-28 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 733626f6-e7d2-3254-bee6-7cdf6d5e1a16 | -20.13787 | -50.72078 | 2025-03-28 05:18:00 | NOAA-20 | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 1c0394ed-a6ce-3b42-9883-0a8d674ce7a1 | -22.07165 | -56.47011 | 2025-03-28 05:18:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba697714-2788-377d-bd20-a3a020287611 | -12.45612 | -41.4527 | 2025-03-28 05:23:00 | AQUA_M-M | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 4ef16bbf-b08a-3d0d-a8bf-2d4cf775ec62 | -12.46408 | -41.46381 | 2025-03-28 05:23:00 | AQUA_M-M | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 7a4cf937-a94d-3e5d-a222-79fcfd5074b2 | -12.4547 | -41.46267 | 2025-03-28 05:23:00 | AQUA_M-M | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 30.7 |
| 4a8cd37b-1081-357f-92db-e4be770d173c | -22.5697 | -47.12805 | 2025-03-28 05:25:00 | AQUA_M-M | ARTUR NOGUEIRA | SÃO PAULO | Brasil | 3503802 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9426f842-6b9c-3512-b900-da4c439c79bf | 3.96734 | -61.50831 | 2025-03-28 06:03:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2922b371-e912-301a-a16c-e4bcb6eb4577 | 2.20033 | -61.81754 | 2025-03-28 06:03:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2beed6e-8014-325e-9e86-213aba512f89 | 4.07738 | -61.5499 | 2025-03-28 06:03:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c192a298-2f9f-384a-9dde-47640977c456 | 3.96823 | -61.51363 | 2025-03-28 06:03:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9da86f5-4f0f-3570-8c54-ba16d269e872 | 3.96267 | -61.56987 | 2025-03-28 06:03:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2844b32b-ef85-38a0-9b9d-86852b173082 | 2.30751 | -61.61576 | 2025-03-28 06:03:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c07567a-ae44-308d-b02e-51af1d1efd2c | 3.98281 | -61.51128 | 2025-03-28 06:03:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be883d15-41e0-3026-af20-09af2c180972 | 3.98856 | -61.51589 | 2025-03-28 06:03:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 500bbe95-63bc-3287-90b5-f5e08a020011 | 2.18477 | -61.81456 | 2025-03-28 06:03:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f815817-ab53-3233-b8e9-bf6f93731561 | 3.96755 | -61.56929 | 2025-03-28 06:03:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5407f9d5-0456-33e2-b4cb-7e0e68f3aa77 | 3.98768 | -61.51053 | 2025-03-28 06:03:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0308666e-2993-3910-97c2-2ae8ad0190a5 | 2.30657 | -61.61018 | 2025-03-28 06:03:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d68fdafa-cb88-360b-96f0-ac9db85e81c5 | 4.66801 | -60.89643 | 2025-03-28 06:03:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 065227b4-a892-36a0-92b7-12caa5fb0662 | 3.21319 | -61.58706 | 2025-03-28 06:03:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b509031-eaa4-3fed-ab36-82b07e3367c1 | 2.30568 | -61.61077 | 2025-03-28 06:03:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c3784f52-ee63-3f08-b92a-3d4dd7585cf8 | 3.96356 | -61.57516 | 2025-03-28 06:03:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c4020212-925e-3f8a-b3c5-11364d325658 | 2.19543 | -61.81829 | 2025-03-28 06:03:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65f88798-daf0-3ce5-b4af-727215e69c77 | 2.17988 | -61.81541 | 2025-03-28 06:03:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ff2c8a1-9ca1-3c9e-b239-8dba09741dac | 3.97309 | -61.51283 | 2025-03-28 06:03:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4855d1ae-d017-35de-9dfd-bb645775b037 | 3.9722 | -61.50753 | 2025-03-28 06:03:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad0911a5-e0c7-367b-aec1-e1ce5acd8738 | 3.96248 | -61.50911 | 2025-03-28 06:03:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74c50a9c-3551-3697-9308-97ac894a2128 | 3.94845 | -61.54446 | 2025-03-28 06:03:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be584282-fb30-3510-ab04-0b197e66577f | 3.98945 | -61.52126 | 2025-03-28 06:03:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c4b164f-c67c-3dc6-b7ab-7d1a25e13d94 | 3.9693 | -61.57981 | 2025-03-28 06:03:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| adca47ee-4fa2-3144-9dcf-65e393279e0c | 4.07253 | -61.55064 | 2025-03-28 06:03:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 291c49fd-23d0-3431-93c5-8182b5a95326 | 3.9647 | -61.50419 | 2025-03-28 06:54:00 | AQUA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| eb21099b-1f59-3c24-8f94-d587abb08b6d | 3.96508 | -61.57384 | 2025-03-28 06:54:00 | AQUA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f738a6ed-0b24-36c7-ae48-b937654b7862 | -10.22389 | -36.97208 | 2025-03-28 11:49:00 | TERRA_M-M | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 43071428-033c-3a20-bb13-707b414e0c6a | -9.55657 | -36.22784 | 2025-03-28 11:49:00 | TERRA_M-M | MARIBONDO | ALAGOAS | Brasil | 2704807 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 78cf5156-960b-37af-b31a-84e160f37015 | -9.41256 | -36.46452 | 2025-03-28 11:49:00 | TERRA_M-M | PAULO JACINTO | ALAGOAS | Brasil | 2706604 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 1d3e5d5b-52eb-314d-b18d-be9b19a7862c | -11.91942 | -38.38487 | 2025-03-28 11:49:00 | TERRA_M-M | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 2bdeaaff-5486-39ec-bbc1-bf1c533cdcf2 | -10.12163 | -37.8709 | 2025-03-28 11:49:00 | TERRA_M-M | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 14d9936c-2063-31d9-a0fc-8b595c65eff5 | -9.63637 | -37.46656 | 2025-03-28 11:49:00 | TERRA_M-M | SÃO JOSÉ DA TAPERA | ALAGOAS | Brasil | 2708402 | 27 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 5606a4f0-1255-3e96-806f-feb71b752f6a | -11.20822 | -38.44765 | 2025-03-28 11:49:00 | TERRA_M-M | NOVA SOURE | BAHIA | Brasil | 2922904 | 29 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 0119dc15-ad37-3d85-8ae4-d43bd4af87bf | -10.97838 | -40.38271 | 2025-03-28 11:49:00 | TERRA_M-M | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 42bd7a7e-2635-3a89-97d7-7d95d79c0696 | -11.3839 | -39.25477 | 2025-03-28 11:49:00 | TERRA_M-M | CONCEIÇÃO DO COITÉ | BAHIA | Brasil | 2908408 | 29 | 33 | nan | nan | nan | Caatinga | 16.3 |
| b5b4347c-bc70-32e6-9dd5-7417f66df255 | -4.96965 | -37.80239 | 2025-03-28 11:49:00 | TERRA_M-M | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |


