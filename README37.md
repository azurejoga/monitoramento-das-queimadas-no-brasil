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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a34bb133-24da-3760-8e7c-95a5f894c065 | -13.3004 | -45.2442 | 2026-09-07 06:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 2fc36141-b4ea-3054-8f57-8e84d5afe352 | -3.1461 | -60.6696 | 2026-09-07 06:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| fd140399-37c2-3ce2-baa9-94754d90d62e | -13.3009 | -45.2209 | 2026-09-07 06:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 254.4 |
| d7338b01-09d9-3ade-b6ef-13eb662c748b | -2.6381 | -46.76986 | 2026-09-07 06:20:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 6f54dc4b-81e6-338b-ac31-6f4835ae1d17 | -4.383 | -44.39091 | 2026-09-07 06:20:00 | AQUA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 39e22411-98b2-314c-9cb3-dd0a891a5910 | -2.63777 | -46.76266 | 2026-09-07 06:20:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| dc553da4-114f-3cc0-bf3e-eb59689b91a2 | -2.62236 | -46.77968 | 2026-09-07 06:20:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 84da60e6-c28a-3ada-81f7-41286835fddc | -2.62528 | -46.76069 | 2026-09-07 06:20:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| bb142069-4f1f-3f29-ae30-91dc1c5a670d | -2.86819 | -50.43916 | 2026-09-07 06:20:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| f2013db4-e957-3186-8c94-909ac7c7b51b | -2.87829 | -50.43602 | 2026-09-07 06:20:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 09603515-77ba-3a24-9e45-93f64c3787f0 | -2.62561 | -46.76788 | 2026-09-07 06:20:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 2b8a4088-717b-3410-b0ef-573a791c2872 | -2.63489 | -46.78162 | 2026-09-07 06:20:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 9fa0f628-993e-3706-a99d-c0993bbb2e78 | -10.73756 | -45.07353 | 2026-09-07 06:22:00 | AQUA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 622f7f26-4022-3b18-af72-f3535b67cb9c | -9.52322 | -41.9865 | 2026-09-07 06:22:00 | AQUA_M-M | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 6ff1060f-abfb-3ea9-9274-e020a31ac6ac | -13.30534 | -45.21813 | 2026-09-07 06:25:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 7a0bacef-983c-31b6-b86e-f0725c716fef | -13.84798 | -43.64129 | 2026-09-07 06:25:00 | AQUA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 21f42376-8fe0-3743-b2d0-affbe4b4105b | -14.84781 | -45.63021 | 2026-09-07 06:25:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4dc4c936-75b7-3e37-aecc-ec866bcebe8e | -14.83679 | -45.6389 | 2026-09-07 06:25:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e9ff77cc-965e-314a-899d-2ba739cc6a45 | -14.90078 | -44.67289 | 2026-09-07 06:25:00 | AQUA_M-M | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f26fcc97-a24e-38b6-96fa-3aa4c3f5e11f | -14.83847 | -45.62867 | 2026-09-07 06:25:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f8507f3d-7a54-38ff-aec1-1472b4937ad4 | -13.29275 | -45.23711 | 2026-09-07 06:25:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f7ffb95b-0656-35a7-9240-24ea506b0a86 | -13.29438 | -45.22688 | 2026-09-07 06:25:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2045a330-3e55-31b8-80cc-7a2ddf40e49c | -14.90974 | -44.67439 | 2026-09-07 06:25:00 | AQUA_M-M | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 4afa80ef-1275-347c-8ab7-2fbd1e120b75 | -13.30209 | -45.23858 | 2026-09-07 06:25:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 245.4 |
| 9416ca60-73da-3cbd-9bfa-dc30ec4e1a84 | -13.31141 | -45.24015 | 2026-09-07 06:25:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 69f41e90-23b9-3583-8976-1ea088c07d43 | -13.8466 | -43.65033 | 2026-09-07 06:25:00 | AQUA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0b0340b5-e252-3619-b533-d13b743ac5d4 | -13.30371 | -45.22835 | 2026-09-07 06:25:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 602.7 |
| 97d1cdf1-8fdc-3db9-ad9a-99813935314d | -15.93486 | -41.98002 | 2026-09-07 06:25:00 | AQUA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 987b05a3-0d20-3343-9836-1bee500b0bd9 | -14.84614 | -45.64043 | 2026-09-07 06:25:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3f7bf1f6-c6ac-38cc-8292-2f67fa73888d | -14.91124 | -44.66493 | 2026-09-07 06:25:00 | AQUA_M-M | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 6b41dadd-e3f9-3966-8544-bb4e87252a0f | -13.31304 | -45.22988 | 2026-09-07 06:25:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| a9e99eee-6339-355b-8a93-a565cdf4b125 | -15.93627 | -41.97034 | 2026-09-07 06:25:00 | AQUA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| df8f0b63-ccbc-3a37-b62f-e051e69436d4 | -13.2474 | -61.773 | 2026-09-07 06:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 6cfffd7d-4cca-3478-8dd9-7427ae8990c5 | -13.2092 | -61.795 | 2026-09-07 06:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 65.8 |
| af31ca43-2c71-3d94-8cbd-b062bcb0cfa1 | -13.2284 | -61.7743 | 2026-09-07 06:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 40816c17-5bd2-3aa9-8c9e-b7a84e23989b | -13.3009 | -45.2209 | 2026-09-07 06:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 308.4 |
| eeec9865-0d86-3561-8740-583b3c9b4c47 | -13.2094 | -61.7755 | 2026-09-07 06:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 2196fad1-a812-394a-a399-7dad5425e137 | -13.2282 | -61.7937 | 2026-09-07 06:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 34a1a5e7-b80d-3626-8478-2d7a88a7aaf3 | -13.3198 | -45.2409 | 2026-09-07 06:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 175.9 |
| 8741399b-b0e3-3923-b338-264813a63f7f | -13.3203 | -45.2177 | 2026-09-07 06:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 171.4 |
| 36c0441d-0fa3-3f99-9260-cc953d50f571 | -13.3004 | -45.2442 | 2026-09-07 06:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 310.4 |
| 52b6a7e3-e561-3363-8e50-cbd568ac43ac | -13.3009 | -45.2209 | 2026-09-07 06:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 279.5 |
| 0fce2526-0d78-3652-b1e1-d21c2ce8ad7f | -13.3198 | -45.2409 | 2026-09-07 06:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 557a7387-4144-3c62-b0ef-c8fb75d7152f | -13.3203 | -45.2177 | 2026-09-07 06:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 7a9935c2-6412-3d11-9993-52d840b6dd0b | -13.3004 | -45.2442 | 2026-09-07 06:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 268.1 |
| ae8229e6-0f4f-34c5-aba9-8ee4f1e29c41 | -13.3009 | -45.2209 | 2026-09-07 06:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 246.8 |
| e47ad8f5-57a9-3af7-8561-629f0bfa9e50 | -13.3198 | -45.2409 | 2026-09-07 06:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| f6f7cd62-bffd-3351-8593-41faaac07797 | -13.3203 | -45.2177 | 2026-09-07 06:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 2ea97812-c841-319c-b07e-c0c265041168 | -13.3004 | -45.2442 | 2026-09-07 06:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 223.1 |
| e9b8c4d3-807f-3c88-8209-d9e04027ef53 | -9.7332 | -43.3932 | 2026-09-07 07:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 104.0 |
| f710e1e9-cd4e-3325-9eaa-8fae5f3a062b | -13.3004 | -45.2442 | 2026-09-07 07:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 175.3 |
| fcda55bc-c5b0-3cdf-98d4-fd49d57fec8a | -13.3009 | -45.2209 | 2026-09-07 07:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 209.6 |
| e6f64474-aa67-3ee8-abf7-7bfac3943654 | -13.3203 | -45.2177 | 2026-09-07 07:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 1726c895-1c8d-3207-a3c2-7abb4cdd18d3 | -3.1461 | -60.6696 | 2026-09-07 07:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 5c238830-23f1-3f87-8494-f72230d7a02c | -9.7328 | -43.4168 | 2026-09-07 07:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| a19e7c94-9663-31d3-bc9d-b8a5683168a7 | -13.3198 | -45.2409 | 2026-09-07 07:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 5f2efc15-d6fc-3040-ac45-8856b1e963a0 | -13.3198 | -45.2409 | 2026-09-07 07:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| af9f8fa6-ac68-3598-a6ba-abf223edf46f | -13.3009 | -45.2209 | 2026-09-07 07:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 8a096a89-ad9b-3378-90c4-379b06f571e6 | -9.7332 | -43.3932 | 2026-09-07 07:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 159.8 |
| 50ddee3f-b871-3478-9a72-f227c0979c06 | -13.3004 | -45.2442 | 2026-09-07 07:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 183.5 |
| 30b94835-da9c-3896-acb3-e35aa27bf0d3 | -9.7328 | -43.4168 | 2026-09-07 07:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| b84ae0d8-08a5-3b08-830f-e26b07acb10d | -13.3203 | -45.2177 | 2026-09-07 07:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 7d1d2619-d79a-3ab1-8894-0d719370955f | -9.7141 | -43.3956 | 2026-09-07 07:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 59.6 |
| 6afaa9a7-930b-36ac-953a-035828441351 | -13.3 | -45.24 | 2026-09-07 07:15:00 | MSG-03 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 374a97a6-3ad6-3137-a84b-ae9b0f503c04 | -13.3009 | -45.2209 | 2026-09-07 07:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 153.6 |
| cda2b473-993c-31a2-af3d-604a7a4b6cac | -9.7332 | -43.3932 | 2026-09-07 07:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 189.5 |
| 65740c18-e8c7-3bee-9c7c-e884442b1660 | -9.7328 | -43.4168 | 2026-09-07 07:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| cfbf96dc-3796-3c30-996f-0b87fe305ee4 | -13.3004 | -45.2442 | 2026-09-07 07:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 15c154b6-cebc-39b9-963c-783254ac0bb3 | -13.3203 | -45.2177 | 2026-09-07 07:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 73ab75db-98ec-3c42-b52a-4073855bffec | -13.3198 | -45.2409 | 2026-09-07 07:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| ecd49f3a-ffa9-3f04-a147-d091c23fb887 | -9.7141 | -43.3956 | 2026-09-07 07:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 58.4 |
| 5840f8a2-7d0e-3f36-990f-ff513d2eeb5c | -9.7332 | -43.3932 | 2026-09-07 07:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 94.2 |
| c5bd5d77-8d74-3d20-aa6b-9e7cd0ef31e5 | -13.3009 | -45.2209 | 2026-09-07 07:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 26eb5bd6-6178-38af-95a4-77068d6c4074 | -13.3004 | -45.2442 | 2026-09-07 07:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 6dc0593d-6071-34e3-b8fb-07c1fe093f7f | -13.3198 | -45.2409 | 2026-09-07 07:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 3348b84b-4e91-3e4e-8bcb-605739ab8677 | -9.7141 | -43.3956 | 2026-09-07 07:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 71.3 |
| a5ecc8eb-4c02-3b0a-a2e0-a8aed21a3b5e | -9.7328 | -43.4168 | 2026-09-07 07:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 64b8fc2c-b19e-3914-a304-e5146eefc6c9 | -13.3203 | -45.2177 | 2026-09-07 07:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 2905f429-4f5f-39d5-a228-3447437afa26 | -9.7328 | -43.4168 | 2026-09-07 07:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| f5191fb0-2a57-3527-a0dd-7718c5d55688 | -13.3009 | -45.2209 | 2026-09-07 07:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 169.4 |
| 0d5daa28-d773-3c46-88f6-d4a39070564f | -13.3198 | -45.2409 | 2026-09-07 07:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 5784e734-9d6f-3132-a8a1-c61580c37889 | -13.3004 | -45.2442 | 2026-09-07 07:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 6657a99b-3773-36a9-87b1-415e0f821ffd | -9.7332 | -43.3932 | 2026-09-07 07:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 95.6 |
| 82d7b875-109d-399c-b142-400e246ea3e7 | -13.3203 | -45.2177 | 2026-09-07 07:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 66103c67-d4c6-363f-b235-1003c31573d6 | -9.7332 | -43.3932 | 2026-09-07 07:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 70.1 |
| d0e435d1-256c-31d0-9bb1-55a2f0b87225 | -11.5001 | -49.6109 | 2026-09-07 07:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 7997df5f-34b0-3c6e-a3fa-afa44a208a34 | -13.3198 | -45.2409 | 2026-09-07 07:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 756ab98c-0c00-3d48-bab1-e5c336274ea0 | -9.7328 | -43.4168 | 2026-09-07 07:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| c557ec2b-a112-3298-8b93-c70a2cdba30e | -13.3203 | -45.2177 | 2026-09-07 07:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 548cc3a1-c163-3059-8681-b46a0f757514 | -13.3009 | -45.2209 | 2026-09-07 07:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| f860d121-df0f-34d7-b67f-8d1a6037366b | -13.3004 | -45.2442 | 2026-09-07 07:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 31cace4c-9a03-307e-a2be-7624404d85b3 | -3.1461 | -60.6696 | 2026-09-07 07:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| f7b7acd1-8b9d-3de2-8c14-0745cd412a71 | -5.98422 | -57.69836 | 2026-09-07 07:58:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 959bfbfa-fcb1-30b0-ad28-68547ffa12b4 | -5.29751 | -60.1293 | 2026-09-07 07:58:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 1195bc29-dc6c-348f-80a1-71e94788653b | -5.98381 | -57.6937 | 2026-09-07 07:58:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 6edc8fb3-711d-3177-9f89-0a51e60a6c77 | -3.14817 | -60.65881 | 2026-09-07 07:58:00 | AQUA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| a4ee38ea-6de3-3f62-95af-a06e0adb38db | -3.4091 | -59.23724 | 2026-09-07 07:58:00 | AQUA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d31fab7c-8aae-326f-90fb-32d23b497d37 | -3.13707 | -60.6572 | 2026-09-07 07:58:00 | AQUA_M-M | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 70b52645-4e1a-3aeb-9ebc-93468930b888 | -13.3203 | -45.2177 | 2026-09-07 08:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 61aab6c8-bdd8-3f50-9fbe-b21cb51e3ee4 | -3.1461 | -60.6696 | 2026-09-07 08:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |


[Clique aqui para ver as próximas entradas](README38.md)
