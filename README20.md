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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d410a94-b5fa-3a76-94aa-159c0f04f4b5 | -3.584 | -40.3264 | 2024-10-29 01:55:26 | GOES-16 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 65.1 |
| 54263296-cf69-33c0-a2d9-0552c6956b89 | -4.2761 | -46.1178 | 2024-10-29 01:55:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 71549f79-5f54-3b63-a9cd-2439d3197a04 | -4.2762 | -46.0956 | 2024-10-29 01:55:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 72715d21-94c8-313d-8eee-9253b5b6d22b | -4.366 | -43.778 | 2024-10-29 01:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 77fa810e-296f-376a-a56f-6e00eac330d8 | -4.3475 | -43.7559 | 2024-10-29 01:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 862e8772-8d68-36bf-abb1-518970b83ba0 | -4.3473 | -43.779 | 2024-10-29 01:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 262.5 |
| 1e0e4b08-3193-39bb-9959-140b2bdb73cd | -4.3286 | -43.7801 | 2024-10-29 01:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 9ac35213-10cc-3ff7-90bc-06b03c3a1dd0 | -4.9326 | -45.4321 | 2024-10-29 01:55:34 | GOES-16 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 865f584d-5774-32b7-acc6-9f3a28979d20 | -6.6143 | -47.3853 | 2024-10-29 01:55:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| d81599f2-caf6-3172-86c7-ccd7132a7b61 | -11.138 | -55.5313 | 2024-10-29 01:56:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 012d50de-3193-3c1c-a647-5a659dbc926d | -12.3522 | -49.94 | 2024-10-29 01:56:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 2bed29be-c526-323b-9967-4beb58bb25f3 | -12.3526 | -49.9184 | 2024-10-29 01:56:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 0b6b02f7-0245-3379-83d2-266e225c4015 | -13.6887 | -46.1247 | 2024-10-29 01:56:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 1d8003f6-cfff-322a-aba9-5cca720b2652 | -13.6222 | -45.5838 | 2024-10-29 01:56:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 0eb3057d-381b-3488-acf1-b51033c7dc1a | -13.6028 | -45.587 | 2024-10-29 01:56:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| d5271cb2-8fb6-307f-945c-f6eeed75ba9d | -24.0103 | -54.110199 | 2024-10-29 02:03:25 | METOP-C | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 69f81376-d366-3a4a-9780-7da31a7ab702 | -1.3847 | -54.0571 | 2024-10-29 02:05:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 6ebd7efb-61bb-3fd1-86a4-ebad97946bef | -1.3847 | -54.037 | 2024-10-29 02:05:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 077162cb-725e-3889-958c-eaed61f664c6 | -2.5066 | -47.4425 | 2024-10-29 02:05:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 1cf66946-ca09-3961-9496-327db7e216ef | -2.5251 | -47.442 | 2024-10-29 02:05:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 1156954a-298b-3542-b311-62fe65e520a4 | -3.0913 | -54.287 | 2024-10-29 02:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 6c2244d3-828a-39bc-9026-16f33b71ba30 | -3.0914 | -54.2669 | 2024-10-29 02:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 9ef32da1-298b-3a1a-adfa-71e48b584c6d | -3.1097 | -54.2865 | 2024-10-29 02:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 9d236b3f-565b-3e83-a1c8-5272a36d7e5c | -3.1098 | -54.2665 | 2024-10-29 02:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| ffcc1389-6788-35c1-ad9c-e5b10b9b360c | -3.1281 | -54.286 | 2024-10-29 02:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 3e2b495f-1f35-384a-b290-deefc2f0e0a8 | -3.1281 | -54.266 | 2024-10-29 02:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| bc8b70e5-762c-38d2-b66d-0bf50e880edc | -3.1794 | -50.3922 | 2024-10-29 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 830dae11-841d-382e-999f-5cf0767cfe7b | -3.2503 | -46.8709 | 2024-10-29 02:05:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| fb67dc1e-8643-3dcf-93fe-6a2b90fe056b | -3.3044 | -47.198 | 2024-10-29 02:05:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| ea522315-9030-3afd-a709-4fc39ce35e1c | -3.9289 | -48.3458 | 2024-10-29 02:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 63bd44da-f0e9-3025-9c73-92ffee4a4f7f | -4.2576 | -46.0965 | 2024-10-29 02:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 85.1 |
| b38897f5-d05c-3eeb-b131-f7e14fb48b37 | -4.2761 | -46.1178 | 2024-10-29 02:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| aa5c3ab1-6f4e-3cf4-8103-63e859452841 | -4.2762 | -46.0956 | 2024-10-29 02:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 141.9 |
| e59f2595-25cc-3f03-aae5-a4895d805e9b | -4.3286 | -43.7801 | 2024-10-29 02:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 6859a54d-7de4-3c58-95f3-d03660baa5fc | -4.3471 | -43.8021 | 2024-10-29 02:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| ecdd89bd-4809-33af-bfd0-b1b0e000481d | -4.3473 | -43.779 | 2024-10-29 02:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 245.2 |
| 6f45de6b-a575-3642-99ed-8325c97f464c | -4.3475 | -43.7559 | 2024-10-29 02:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| a6830db8-3a14-3274-91e6-cab971dd6167 | -4.366 | -43.778 | 2024-10-29 02:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 54953859-a39d-3e10-b6c4-9db830dd5889 | -4.9326 | -45.4321 | 2024-10-29 02:05:34 | GOES-16 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 1bd9ca67-7a36-3fa0-9148-2e9ab568a9b3 | -6.5956 | -47.3867 | 2024-10-29 02:05:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| ac866a82-710d-3955-aecd-84e49361baf1 | -6.6143 | -47.3853 | 2024-10-29 02:05:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 6db6559d-de6d-3e48-b758-414936067154 | -11.138 | -55.5313 | 2024-10-29 02:06:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 286b6168-7110-3853-aaaa-a64d48f73806 | -12.3334 | -49.9208 | 2024-10-29 02:06:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 572aa83f-dad5-381a-94e2-dbd395d5eeb9 | -12.3522 | -49.94 | 2024-10-29 02:06:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| f1f679b2-475e-3cf5-b87f-679f46cef891 | -12.3526 | -49.9184 | 2024-10-29 02:06:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 7cc2cfcb-61f6-3fa2-9efd-ee11909f8479 | -14.1391 | -44.0662 | 2024-10-29 02:06:25 | GOES-16 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 9d9ff5db-191d-3f5f-aa2f-442bb322c55e | -11.1421 | -55.505299 | 2024-10-29 02:06:58 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac135d56-5dac-3544-90e2-0a0ab0d70c2c | -11.1505 | -55.535801 | 2024-10-29 02:06:58 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab208a4c-5099-36b2-8a26-224b51749a81 | -12.4494 | -63.681599 | 2024-10-29 02:07:11 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ba79eac4-7e27-3ba1-8527-47dd8c87e0ed | -9.6405 | -67.2089 | 2024-10-29 02:08:10 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 72730c3e-8d44-3492-92d0-5c68ad31239d | -9.6161 | -67.192497 | 2024-10-29 02:08:10 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a8b3828f-8138-38fb-bcc4-f651b4414a04 | -1.3847 | -54.0571 | 2024-10-29 02:15:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| f2ae1628-fc6f-394a-a3e8-fe9913d13ee4 | -1.3847 | -54.037 | 2024-10-29 02:15:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 3ea9d92b-8e7d-3bf1-84fd-488b62d401a2 | -2.5066 | -47.4425 | 2024-10-29 02:15:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 3f105a15-8cda-34e1-9a0e-2b9fac2fc299 | -3.0913 | -54.287 | 2024-10-29 02:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| a4d98409-bd8d-315c-a2fe-f0820cd9cc04 | -3.1097 | -54.2865 | 2024-10-29 02:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 150.9 |
| 4b9e1714-217c-3d5c-a91f-2d4c5c09e91b | -3.1098 | -54.2665 | 2024-10-29 02:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 0e085742-c5c7-3d64-8799-37a5265c11cd | -3.1281 | -54.286 | 2024-10-29 02:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| e829f58c-2929-3ee6-a21d-e4b3771ac3ce | -3.1281 | -54.266 | 2024-10-29 02:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 612610c3-3072-3bd5-9938-6c439cfaf73a | -3.1794 | -50.3922 | 2024-10-29 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 27b995d4-dad1-3788-996e-cbde393bce34 | -3.2503 | -46.8709 | 2024-10-29 02:15:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 5897b7d5-c550-3a93-a9c2-67b8a42145e0 | -3.2688 | -46.8703 | 2024-10-29 02:15:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 43117ace-87e7-3c3d-85ea-e39279bb21f3 | -3.3044 | -47.198 | 2024-10-29 02:15:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 8bc773b5-f275-3fa9-9361-f49169fb3e7a | -3.9289 | -48.3458 | 2024-10-29 02:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| a6b5eb57-efe0-39a0-9d00-6f76c99c8166 | -4.3475 | -43.7559 | 2024-10-29 02:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 52f3bd1a-efa9-3503-ab00-fb02236fb354 | -4.2575 | -46.1188 | 2024-10-29 02:15:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 0deb560d-c618-30ce-9827-ce82f3ceb0a5 | -4.2576 | -46.0965 | 2024-10-29 02:15:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 220.1 |
| 5e0c4eab-53bb-3d6b-9990-bc71b70ae8b0 | -4.2761 | -46.1178 | 2024-10-29 02:15:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 191.1 |
| 476e1486-36f4-3840-9a71-f7f613367001 | -4.2762 | -46.0956 | 2024-10-29 02:15:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 385.5 |
| e43b9886-9202-3141-b257-ca0e103b9924 | -4.3473 | -43.779 | 2024-10-29 02:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 51c5166a-04d7-3880-bb1d-6c07b509ec2f | -4.9326 | -45.4321 | 2024-10-29 02:15:34 | GOES-16 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 23ced044-fc8a-340f-ac55-0e71ee975f4c | -6.6143 | -47.3853 | 2024-10-29 02:15:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 2530a868-312b-30ef-8ea0-13968130016e | -11.138 | -55.5313 | 2024-10-29 02:16:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 5c0692fc-011d-3e2e-9135-d91175674a96 | -12.3526 | -49.9184 | 2024-10-29 02:16:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 717b571a-1ae5-3bc3-a4a2-4b0b7c8b5638 | -12.3334 | -49.9208 | 2024-10-29 02:16:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 99f2cc5f-1256-38ee-b232-c63cb3d0b5a5 | -12.3522 | -49.94 | 2024-10-29 02:16:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 232236dd-6429-3e0f-96a7-c42c0b36a188 | -2.3353 | -48.9137 | 2024-10-29 02:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 33f42be5-318e-3df6-a859-83bd78d8f24e | -2.8146 | -49.2206 | 2024-10-29 02:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| a97a7b8a-63b5-3913-a3a2-a0816e336b5b | -2.8555 | -53.3459 | 2024-10-29 02:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 41676faf-bd46-3cd8-9360-164d09889e80 | -3.0913 | -54.287 | 2024-10-29 02:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 04373949-c7e7-3391-a32a-28017926370c | -3.1097 | -54.2865 | 2024-10-29 02:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 172.8 |
| 3f0d729c-3f46-34e0-a50c-40b7ec39fb0a | -3.1098 | -54.2665 | 2024-10-29 02:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 466c7074-982e-379b-8e63-51d89f867241 | -3.1281 | -54.286 | 2024-10-29 02:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| e12dca76-b6e5-3ed9-b47f-78fdb00f75bd | -3.1794 | -50.3922 | 2024-10-29 02:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| bffe3837-8aad-3655-ab32-dbfc709cc2ac | -3.2503 | -46.8709 | 2024-10-29 02:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 127.1 |
| e9bdce4a-f4e0-3913-8fac-b7672eb698f9 | -3.2688 | -46.8703 | 2024-10-29 02:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 60ded04e-497f-3b80-b13e-4fd629e1789a | -3.3044 | -47.198 | 2024-10-29 02:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 30f00208-9359-3a0b-b283-6e78cf9205a0 | -3.1281 | -54.266 | 2024-10-29 02:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 750b0c1a-3c47-39a2-be7e-45eb9984219f | -3.9289 | -48.3458 | 2024-10-29 02:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 7d2e14a8-497d-3eed-95d6-9144db9d79b4 | -4.2575 | -46.1188 | 2024-10-29 02:25:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 275.1 |
| 5687fcee-54a9-3728-98ad-58331df2acae | -4.2576 | -46.0965 | 2024-10-29 02:25:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 343.0 |
| d534cae9-3444-3c75-b10b-6f9261d57c0e | -4.2761 | -46.1178 | 2024-10-29 02:25:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 305.2 |
| 1c46270b-d66b-3164-8374-4b6b537021de | -4.2762 | -46.0956 | 2024-10-29 02:25:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 449.7 |
| d79ecb10-7a1c-3f2b-a8e4-0f71e96d9a59 | -4.2763 | -46.0733 | 2024-10-29 02:25:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 52.8 |
| db030454-2578-35cb-b892-8b74068dbd0b | -4.2948 | -46.0946 | 2024-10-29 02:25:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 76.6 |
| e612b22c-e72d-375c-97ef-e5ccad50d19a | -6.5956 | -47.3867 | 2024-10-29 02:25:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 95451185-599a-3e11-8473-a9de53531ad1 | -6.6143 | -47.3853 | 2024-10-29 02:25:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 603108c4-35bf-3f41-a750-63bfd50d89f1 | -11.138 | -55.5313 | 2024-10-29 02:26:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 3ab082d2-077d-3694-8b87-2c4c5f771a71 | -12.3331 | -49.9424 | 2024-10-29 02:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 392ff677-79c9-32f9-90ed-126aa503b4b2 | -12.3334 | -49.9208 | 2024-10-29 02:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |


[Clique aqui para ver as próximas entradas](README21.md)
