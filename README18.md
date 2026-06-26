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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4ed216d-b1d0-3e29-b4f4-3523d81449e3 | -14.19232 | -47.67845 | 2026-06-26 11:49:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d819b7eb-e747-3ac2-b9ab-d471f191c83d | -14.20964 | -45.62209 | 2026-06-26 11:49:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c9778f61-27df-3be5-9535-26170fb71d46 | -7.75203 | -44.6156 | 2026-06-26 11:49:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 541cfc5a-181a-32a7-9900-b846cee3cd7b | -14.84739 | -48.11441 | 2026-06-26 11:49:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| ebf1564b-b8c5-34a8-bd38-1c3369367e7b | -14.20111 | -47.67974 | 2026-06-26 11:49:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 38.3 |
| bf0ce9f6-c6be-3ce8-b697-dac001beb82e | -13.26064 | -54.42985 | 2026-06-26 11:49:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 26.1 |
| bdb045d2-defd-316f-bf2a-8b126daa25d3 | -8.94094 | -45.67804 | 2026-06-26 11:49:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 42.3 |
| a8299f78-894d-3634-a0b5-3fdf1c631881 | -8.45566 | -46.99601 | 2026-06-26 11:49:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9f838b25-0049-3dea-9e6b-291aa702c825 | -14.69949 | -46.15598 | 2026-06-26 11:49:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 92af4095-1022-32c0-8d90-9706d794acb1 | -13.93441 | -47.34024 | 2026-06-26 11:49:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| db827fc6-5637-3a52-b4ad-8fbf86e1c410 | -14.84608 | -48.1235 | 2026-06-26 11:49:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3c9db684-9ba6-3b13-9034-1442a01d9e44 | -9.0687 | -44.7535 | 2026-06-26 11:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 46181320-1f00-39b4-be24-a6234aa92bcc | -17.60591 | -44.61221 | 2026-06-26 11:51:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 020e9649-0913-38d7-9fb4-df8a086ff39f | -17.54666 | -46.54998 | 2026-06-26 11:51:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 595abb8f-eedc-37d7-b5b5-00b0f84a5b17 | -16.53318 | -47.55815 | 2026-06-26 11:51:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 412732d5-6a36-3093-a079-55608dffbfaf | -31.23381 | -53.10515 | 2026-06-26 11:55:00 | TERRA_M-M | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 20.6 |
| 43d876d6-4aba-3b6a-81c7-ffa71a6255b9 | -9.0687 | -44.7535 | 2026-06-26 12:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 125.8 |
| da7d008d-ee64-3f6b-94fa-ee0eb0ac2756 | -9.0687 | -44.7535 | 2026-06-26 12:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 5c0f35f3-30f1-3d57-a2d9-a72da6cc7b0b | -6.9791 | -42.9034 | 2026-06-26 12:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.8 |
| 860033c4-fa78-3710-b573-639a35014e61 | -12.5135 | -48.2802 | 2026-06-26 12:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 20cf94d0-5367-3e36-a6d4-0363823f53a4 | -9.0687 | -44.7535 | 2026-06-26 12:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 35393712-4fc8-38bb-ae99-f0a8c18852b0 | -9.0876 | -44.7513 | 2026-06-26 12:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 109.5 |
| f6627926-dbe3-3b28-be66-9e462cfbc136 | -12.5135 | -48.2802 | 2026-06-26 12:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 43b4f44a-f4ae-358b-a959-2744d544f199 | -12.5135 | -48.2802 | 2026-06-26 12:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| b37cd023-42b8-3d8c-a4f3-b71f04ebc125 | -6.9791 | -42.9034 | 2026-06-26 12:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| f6a81545-464d-3804-acb5-714a1fd6029a | -9.0876 | -44.7513 | 2026-06-26 12:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 93.8 |
| fb2121ca-0c56-37fb-9817-5e221aede2b2 | -14.6973 | -46.1364 | 2026-06-26 12:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 880f59bc-1828-3f97-9c0d-a6b0c83f0779 | -9.0687 | -44.7535 | 2026-06-26 12:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 148.7 |
| e7128c92-cbd6-35cd-ae41-5183fc6b0147 | -14.6973 | -46.1364 | 2026-06-26 12:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 89.7 |
| f23e02da-2bac-3cf6-a05e-6e0fa74dd50f | -9.0687 | -44.7535 | 2026-06-26 12:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 5b085c06-fa1c-3088-bf86-390b333539a2 | -13.258 | -54.4315 | 2026-06-26 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| b41ea8b2-4486-3439-b06d-8ee689beabc1 | -13.258 | -54.4315 | 2026-06-26 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| a8e3f6bb-b820-3155-baeb-66602895506b | -14.6973 | -46.1364 | 2026-06-26 12:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |
| b5dd7087-97ef-3cd6-afea-cc5c1e2943d7 | -6.9791 | -42.9034 | 2026-06-26 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| ecc320d1-34ab-3885-a748-70fb8d2b8edb | -9.0687 | -44.7535 | 2026-06-26 12:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 114.7 |
| f13f4bcd-e7b0-3148-98c6-3c4392a12d89 | -12.5135 | -48.2802 | 2026-06-26 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 06c39e35-737e-3c5e-913d-63bbfb271e6a | -14.6973 | -46.1364 | 2026-06-26 13:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 84.9 |
| e991a917-874d-352b-b27a-f219127dd05a | -9.0687 | -44.7535 | 2026-06-26 13:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 687b99a3-4476-39fb-8d33-746c0fd5f908 | -13.258 | -54.4315 | 2026-06-26 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 674d6de7-06e5-3108-afd4-fa57defcc106 | -13.2583 | -54.4109 | 2026-06-26 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 122.2 |
| cc6d32e8-095e-39bb-bc9f-e3dfdea1cfae | -6.9791 | -42.9034 | 2026-06-26 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| de4f5ae3-3514-3e5f-bec5-53a031801757 | -9.0687 | -44.7535 | 2026-06-26 13:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 4ddcdc29-5b0c-3f7b-b8c5-440b09feea7d | -12.5138 | -48.2581 | 2026-06-26 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 8d996b7b-024f-35ef-9ab7-f4aa669ce06a | -12.5135 | -48.2802 | 2026-06-26 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ddb929dd-2a62-35b3-8de4-0947b869d505 | -6.9791 | -42.9034 | 2026-06-26 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.3 |
| c737aefe-5a59-3bdf-a84d-0f92f1cdf2ba | -6.9793 | -42.8798 | 2026-06-26 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |
| 85e0ff0a-37e5-3e4e-af19-5a2f4d874d16 | -13.2583 | -54.4109 | 2026-06-26 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 137.7 |
| eed7ba45-dd08-3ae9-96ed-2b6476f9298e | -8.9427 | -45.68 | 2026-06-26 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 3aaa3518-58c1-3cce-87c7-d373bbf8def7 | -12.5138 | -48.2581 | 2026-06-26 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| e63fbc67-209c-3b7e-b888-ee749ca94226 | -14.6973 | -46.1364 | 2026-06-26 13:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 93.1 |
| fa97acc3-4353-378f-925d-2f107d4fdac1 | -12.5135 | -48.2802 | 2026-06-26 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| fb58bfca-5330-3dcf-8fed-ac72af45fe35 | -6.9793 | -42.8798 | 2026-06-26 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| cd561536-2946-3438-ac92-73587d5d3848 | -6.9791 | -42.9034 | 2026-06-26 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 102.7 |
| ace41dec-8a99-35bb-989e-ece3d6b1e5bb | -13.258 | -54.4315 | 2026-06-26 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 164.9 |
| d5fc31a8-bf08-3854-a544-c4efdb30cfc7 | -14.6973 | -46.1364 | 2026-06-26 13:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 108.4 |
| a13ef1a0-a1e5-370a-8f26-246e1cdcf439 | -12.5138 | -48.2581 | 2026-06-26 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 093357b7-9141-3c26-a7c7-d27b55a76362 | -9.0687 | -44.7535 | 2026-06-26 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| e9eb343a-858c-3622-b4eb-01c990a650ea | -6.9793 | -42.8798 | 2026-06-26 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| 712a0e3b-2329-3166-b102-f7fdd7fe7a1e | -12.5135 | -48.2802 | 2026-06-26 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 4ac79125-2878-339a-8fac-2916db6656bb | -6.9791 | -42.9034 | 2026-06-26 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.5 |
| b38a3c0c-47cd-3003-ac3b-69de79d35b24 | -9.0687 | -44.7535 | 2026-06-26 13:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 9004c2ba-a20a-387d-9ac2-200baecd4064 | -13.258 | -54.4315 | 2026-06-26 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 124.0 |
| 8774e004-73e9-3e10-8166-2348089f6aa4 | -14.6973 | -46.1364 | 2026-06-26 13:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 95.9 |
| b7618f3d-5509-317b-8cb4-0f48ed18ba4d | -11.7798 | -46.4367 | 2026-06-26 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 36a41ff9-8591-33e5-9dff-88f59b16b161 | -13.2583 | -54.4109 | 2026-06-26 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 7a471f03-bfc3-3a85-8a64-c9aabba3e4e8 | -6.9791 | -42.9034 | 2026-06-26 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 119.8 |
| 57b188de-dec7-30b5-a8f0-c668cca0ca99 | -12.5135 | -48.2802 | 2026-06-26 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 4083ed27-dbf4-32c8-979a-70c088f88ed6 | -11.7794 | -46.4594 | 2026-06-26 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 7d834f3a-a695-344b-b77b-9ddbe544453a | -6.9793 | -42.8798 | 2026-06-26 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 9eb72713-870b-3e9c-a4d1-31bf1d8cb594 | -12.5138 | -48.2581 | 2026-06-26 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 16481133-d9b1-3c02-ac9b-a124e7aee927 | -6.9793 | -42.8798 | 2026-06-26 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 100a34c4-4c12-394c-9d79-2e5d67ad76bd | -12.5135 | -48.2802 | 2026-06-26 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| b04621ac-cb24-3af1-b4e2-5809491855f9 | -6.9791 | -42.9034 | 2026-06-26 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 123.0 |
| f9497d78-c7d0-3f88-82b8-bd084f755dab | -12.1732 | -45.8348 | 2026-06-26 13:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 6269a4a1-7545-310f-8b4e-33be2266fcff | -8.2344 | -48.1927 | 2026-06-26 13:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 2c7ef471-f102-31e9-a130-e3c8f0f78cc5 | -9.0687 | -44.7535 | 2026-06-26 13:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 141.7 |
| fae8e8f8-f885-34c5-a431-0b6db8ae610e | -14.6973 | -46.1364 | 2026-06-26 13:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 98.9 |
| bab81e62-79a6-3af3-8f8d-beca17f9c55a | -12.5138 | -48.2581 | 2026-06-26 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 2c9922bf-f783-368c-a4d1-7d1f6426a96c | -9.0687 | -44.7535 | 2026-06-26 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 172.1 |
| b292c2de-12f9-301a-aa20-f171e59ad623 | -7.7201 | -43.9525 | 2026-06-26 14:00:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| d698999a-35f2-3f34-ad40-0591f69354d8 | -6.9791 | -42.9034 | 2026-06-26 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 124.6 |
| cc94b21b-f961-3152-a6a4-9772d9cda5a7 | -6.9793 | -42.8798 | 2026-06-26 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.7 |
| b0a80f71-bcba-3100-98b9-fbdb149b9714 | -12.1732 | -45.8348 | 2026-06-26 14:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 370b1d89-1fc9-3767-9dff-8cecedcefcd1 | -14.6973 | -46.1364 | 2026-06-26 14:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 49c8c7d0-0b6b-391c-aa70-9d006ed1f978 | -12.5135 | -48.2802 | 2026-06-26 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 9044855d-253e-364e-8099-1c9097468f42 | -12.5138 | -48.2581 | 2026-06-26 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 09c26036-bed5-3aca-bd47-7d972da01ae4 | -13.2583 | -54.4109 | 2026-06-26 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 129.3 |
| c322e8c9-da7c-34b5-9973-46874d845e01 | -9.5147 | -48.0906 | 2026-06-26 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| b91c2e78-9837-338b-8e1f-a37282b2d471 | -12.5138 | -48.2581 | 2026-06-26 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| dbeb0925-e4bc-3414-9569-b698e4c9c398 | -9.0876 | -44.7513 | 2026-06-26 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 40ce0ae0-9528-3761-8ab9-19b107804112 | -9.0687 | -44.7535 | 2026-06-26 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 70457b43-1349-3786-b747-5fbd1fc4cd54 | -12.5135 | -48.2802 | 2026-06-26 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| b32617f3-ca7a-38e1-a187-56e24cc63489 | -7.7201 | -43.9525 | 2026-06-26 14:10:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 125.4 |
| d166e1c6-955d-3560-a9a0-9817e824d1d4 | -6.9793 | -42.8798 | 2026-06-26 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 102.8 |
| 110e6de3-6b1d-3482-8bfe-6d9c463747a4 | -14.6973 | -46.1364 | 2026-06-26 14:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 906d4ea5-5637-3fd3-968a-d326efa0a807 | -13.2583 | -54.4109 | 2026-06-26 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 199.1 |
| 5163e697-0d25-3267-9185-d1532deb509d | -8.5878 | -46.9054 | 2026-06-26 14:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 263ba7d1-7ebf-346a-b603-c9f3ec09826b | -13.2772 | -54.4295 | 2026-06-26 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 879fe553-9d59-3b4b-a58a-9e44734f190a | -12.5135 | -48.2802 | 2026-06-26 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| fe6c53da-2852-3098-b6e0-daf75fab992a | -6.9793 | -42.8798 | 2026-06-26 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.5 |


[Clique aqui para ver as próximas entradas](README19.md)
