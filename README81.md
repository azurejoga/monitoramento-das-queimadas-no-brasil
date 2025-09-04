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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d847d92-92c9-3476-bc6d-b2cc06a10b12 | -10.98772 | -50.92272 | 2025-09-04 05:16:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5501f676-3076-317f-98a4-f4839f0e27f2 | -9.25923 | -56.89271 | 2025-09-04 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 031d3d9a-d248-3c62-b90f-b45d4dcb5009 | -7.69189 | -48.73176 | 2025-09-04 05:16:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79313414-8cd3-35c3-85dd-794ff5627bcd | -9.26218 | -56.89727 | 2025-09-04 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a42cccaa-3985-3abf-a1bf-40ac2d5b2c22 | -4.99968 | -56.25336 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| c4995293-6b9f-3591-abe7-7a846985f23a | -6.46312 | -55.891 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0a5facb-7d7c-35ae-bc7e-ddd239dd7d22 | -5.70352 | -45.15788 | 2025-09-04 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f79fa335-051a-31cc-9fb3-51cfa60b7477 | -6.67789 | -58.76053 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05de3810-3559-36ab-856a-52132fc8bd96 | -10.15068 | -55.15678 | 2025-09-04 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d03c978-9330-3ec3-b0bc-b0fb8db85d5e | -9.32494 | -55.22397 | 2025-09-04 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7585dc92-0df1-3b33-b5ac-94aae74ef45d | -9.61821 | -47.03021 | 2025-09-04 05:16:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| db03b026-6f52-3d0d-af91-1e0d5374e443 | -9.61671 | -47.04211 | 2025-09-04 05:16:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ba0850da-c34b-30e6-bc92-7a191ddb6596 | -7.25314 | -56.27718 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c73ea386-0f57-3a93-8f28-ab8b138637dd | -7.96743 | -55.29051 | 2025-09-04 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56bb5de6-f61c-3f4e-93af-312ea3a0576d | -9.61005 | -47.04118 | 2025-09-04 05:16:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 12f74fe0-0e9b-3621-b594-d099f022d848 | -9.96082 | -51.64795 | 2025-09-04 05:16:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 507fe0f1-52bd-3900-aea0-5ab69165105e | -5.69554 | -45.16336 | 2025-09-04 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc670ed9-9165-3619-9771-41d423ba2c04 | -9.26277 | -56.89325 | 2025-09-04 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d12ffc0-8ed3-3704-aa0b-1fba02720ecf | -10.42241 | -50.38195 | 2025-09-04 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a4980132-a798-32b1-a82b-0bac96647073 | -3.43011 | -59.57751 | 2025-09-04 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdc11b1a-4b10-3bde-8778-7e5287a70eed | -6.68303 | -48.41232 | 2025-09-04 05:16:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 83b79d25-7446-3c0c-898a-4cfd44997ceb | -6.69488 | -48.41356 | 2025-09-04 05:16:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 50729fa3-8f3a-33b0-a10d-828f08047e1e | -10.49319 | -46.77156 | 2025-09-04 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e138828b-3028-37ae-8a49-5acd37b2804b | -9.43142 | -48.09738 | 2025-09-04 05:16:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df0f4f3d-37a9-3ffa-85cf-1c044e6fffdf | -6.73907 | -58.7382 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 3db92090-1c1f-399f-8d63-81f48036ea64 | -10.09393 | -54.75939 | 2025-09-04 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0294aa6-d350-3803-8ba1-8c4066a76f2c | -6.75119 | -58.72588 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 515d9ef0-55de-370a-9b27-c9c5528a14d4 | -9.97361 | -51.63347 | 2025-09-04 05:16:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| edf6c469-54e5-364c-8597-008d7bcf8138 | -10.1142 | -54.79116 | 2025-09-04 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 642771e0-da9e-37ef-a240-0d3350f85fad | -6.77699 | -63.12997 | 2025-09-04 05:16:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 93235700-a00b-3a14-9cda-962b149dafc2 | -9.51412 | -57.78393 | 2025-09-04 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1a3462d-8ca5-3ff9-88cd-c21b22099de4 | -5.93559 | -51.96949 | 2025-09-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb5073dd-f1b1-3c44-8637-a1f6b285887f | -8.05733 | -52.37499 | 2025-09-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 83db52fe-a858-3c6e-9628-ab61ee8b15ac | -3.43068 | -59.57396 | 2025-09-04 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9058a36-fb7b-3be0-8788-9328b2c35cc7 | -10.09748 | -54.76349 | 2025-09-04 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9d93f77-fcc5-33f2-b3e5-8c64b8d8f023 | -5.38915 | -55.90938 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86cb39ec-d031-3ff3-b35a-f591a74ca91e | -4.12902 | -54.89735 | 2025-09-04 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02d2044c-25bc-3352-8ddb-9ee9a5c376a2 | -10.42879 | -50.37555 | 2025-09-04 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c380edb0-844e-3e73-b274-331c1085c4fb | -6.75064 | -58.72935 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 836f78a5-ea48-3c3d-b8d2-da4a3d3ff3e8 | -10.50514 | -50.43758 | 2025-09-04 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8cd0089-800c-3af3-87e6-6699e0d32b95 | -5.13527 | -56.98008 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 474f413a-1d99-35a5-bb84-93908f3618e8 | -7.96672 | -55.29518 | 2025-09-04 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f90e7402-6e6f-3325-962b-a308606504cb | -7.68641 | -50.27677 | 2025-09-04 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42da2e3d-dfcc-3e4f-971f-03d83992784f | -6.69809 | -48.42026 | 2025-09-04 05:16:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f784d8b1-56c4-3e90-a2b2-3a0df7aafb1c | -6.86932 | -45.58265 | 2025-09-04 05:16:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5c436027-0605-32e3-8c92-1539b673f064 | -10.98283 | -50.9187 | 2025-09-04 05:16:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| d8f13fbc-bade-3432-a290-96c80b78f33d | -6.75728 | -63.13136 | 2025-09-04 05:16:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ae282831-9240-3894-a2c0-d2f57c568389 | -9.96862 | -51.63285 | 2025-09-04 05:16:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f69d57b-1cd9-3fcb-a6ce-aa7b548ce92e | -6.83415 | -59.36361 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 5b147909-1be2-3fab-b853-e748afd4ccc7 | -5.60233 | -45.02298 | 2025-09-04 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 70f86969-fe4e-3d53-9d59-e4f21e3cf1ac | -6.74347 | -58.73177 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 2c8174fc-a407-3643-802d-efa7e7649c39 | -10.50559 | -50.43404 | 2025-09-04 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6919a05-3eb2-328e-9269-84a0d476633c | -8.53425 | -51.33011 | 2025-09-04 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2ce2dbac-b0f8-3036-b3f1-6563dfe3fd63 | -10.49123 | -53.65136 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 324d3de0-6e87-39f3-8092-7a42b5afb423 | -5.68456 | -45.6045 | 2025-09-04 05:16:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0c307646-c7db-3492-9ef0-99afb172d48d | -7.71147 | -50.32384 | 2025-09-04 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad7726d3-2c55-3f7d-aacc-2185b8b12865 | -9.49531 | -57.81541 | 2025-09-04 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10e248f2-153a-3571-ac91-9c735589b061 | -6.67059 | -60.03164 | 2025-09-04 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 361a2a81-14f9-37ee-a464-da92077658c9 | -5.88642 | -51.95332 | 2025-09-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| a0a78c23-8405-33c6-8601-f6d975169837 | -5.10919 | -56.96856 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ba90e2c-593b-3e0f-bcaf-332e801a2a3a | -6.46542 | -55.88501 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73573fc8-0543-3199-a9e0-d6ebf23e49de | -6.8403 | -46.39159 | 2025-09-04 05:16:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c4dddb2-816c-32e8-ba24-d17cee4684ed | -6.8438 | -59.15231 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23868497-3a00-33b5-a892-6c92f070e9a5 | -10.48705 | -46.77116 | 2025-09-04 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5b5abd16-37b3-3024-a2fb-15d18f4f4e29 | -7.02155 | -59.66 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebc67199-8326-3d65-814c-3ebf25f73a5d | -10.15241 | -46.27375 | 2025-09-04 05:16:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e7d3333-d701-3ca0-b30d-e67c0c177361 | -10.98222 | -46.84664 | 2025-09-04 05:16:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 69aea07e-caae-3b21-99ae-660c9fb11bf1 | -8.36522 | -52.55034 | 2025-09-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70c16ead-1d21-3324-a332-700f68396ade | -4.21148 | -55.24146 | 2025-09-04 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7ac7bb6-5daf-36d6-b1b3-49dd6c8db237 | -7.68553 | -48.73464 | 2025-09-04 05:16:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9e0047f-5566-304b-a160-ee5e253ac6aa | -5.00002 | -56.26083 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 45dda256-1912-3579-b0dc-6a085a1432ca | -7.69581 | -48.73883 | 2025-09-04 05:16:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe6b7cd8-23e4-3676-97cd-9a35aa99d14c | -8.42297 | -62.29153 | 2025-09-04 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6734f9e-00d1-38cb-8d10-289d7129fc10 | -7.71805 | -50.31485 | 2025-09-04 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 38ebbdbf-988a-3d79-a5ff-c812fc413a67 | -7.26973 | -57.55703 | 2025-09-04 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c63f285c-9891-3163-ae19-0de442d1b446 | -9.33095 | -55.2099 | 2025-09-04 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3979168-87c7-3596-bde7-e7088f18740e | -9.49114 | -47.62004 | 2025-09-04 05:16:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d121ab4-fd73-3db0-9a52-de2bae22eee8 | -7.69878 | -50.25734 | 2025-09-04 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 58c8b99b-6aa3-31f1-933e-352ec017b896 | -6.69322 | -48.41173 | 2025-09-04 05:16:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a45efb74-ffb1-30f9-9f2d-3158d6603c2b | -5.60948 | -45.02389 | 2025-09-04 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cb6118be-a1b2-36e4-a285-6fe82dc58a1c | -7.69823 | -50.26149 | 2025-09-04 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b23b96a7-6998-3f6a-8a1f-e9a8d626ea35 | -7.39152 | -59.66254 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a78c21c-cb7b-31e5-8556-a4d338470285 | -10.89788 | -50.83183 | 2025-09-04 05:16:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61a232fa-4af4-324d-bccc-268a795f2fa0 | -10.46786 | -53.62631 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e20bce5-1cb9-36b6-8a8d-54b7173e90b4 | -9.6034 | -47.04022 | 2025-09-04 05:16:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| df8eafde-c05a-3817-9030-1a4089ddd576 | -10.14603 | -55.16127 | 2025-09-04 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 223bfc3c-c442-31bb-a824-6ec02c58b2de | -8.36126 | -52.54526 | 2025-09-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7d036adb-ed77-317c-9531-b9e9ce628b8a | -9.60266 | -47.04611 | 2025-09-04 05:16:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1f81b0ac-0274-393e-b870-082d89fc360c | -8.52684 | -51.31479 | 2025-09-04 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 29716013-201c-36ee-bfa1-f63bac97b580 | -7.77852 | -50.96567 | 2025-09-04 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa28a127-1413-3323-b081-1ba3e18b76f1 | -6.87003 | -45.5774 | 2025-09-04 05:16:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3527c7ab-90f3-3e38-81e7-77910fa1b9e7 | -7.33849 | -59.65409 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 779ebd44-9691-3d25-ae48-17513d115ca0 | -6.88394 | -59.09128 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00ebb6b1-e91b-3c25-acc7-e705727fa919 | -6.87989 | -45.55761 | 2025-09-04 05:16:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32025b80-fab2-3f1d-9362-d5fdd06b40ad | -5.70259 | -45.16464 | 2025-09-04 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a3d1928c-563a-3718-87f5-86128a001675 | -9.48538 | -47.61382 | 2025-09-04 05:16:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 48d5cf0b-7c6f-3448-8ef6-9c3c92208711 | -8.52607 | -51.32062 | 2025-09-04 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 47bbf4b2-96e4-3991-a981-23a6b186bbe2 | -6.68626 | -48.41887 | 2025-09-04 05:16:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5d527af3-bf2b-38e7-bda6-36b91324e0dd | -8.08732 | -47.58804 | 2025-09-04 05:16:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 553cad46-0690-3042-9023-6af6a77c5034 | -7.72868 | -61.5263 | 2025-09-04 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README82.md)
