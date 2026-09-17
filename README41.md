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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1600980-c8dc-3999-bc66-372d95170867 | -9.56153 | -46.59506 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2adb32bc-f3f6-3c17-8085-b316c8486a59 | -10.83486 | -54.09613 | 2026-09-17 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10562e81-dec7-3156-b3da-09be15de8258 | -5.86518 | -52.05552 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7cad212-2c4c-38cb-b4ff-f7c877842795 | -7.04494 | -42.05663 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| f217ab05-274b-3617-9b26-af4d8856269d | -7.07249 | -41.8287 | 2026-09-17 04:40:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 228e6d64-f2a5-3ccb-ae00-abe66d938621 | -8.42641 | -47.7558 | 2026-09-17 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58deaf8e-18a6-3b6a-bcce-66655e9b4f1c | -9.875 | -48.35447 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1dc292cb-0b8d-386c-a043-f2c5dda17369 | -6.0159 | -46.64262 | 2026-09-17 04:40:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1217080-d257-32c8-a354-98f20194de80 | -6.70368 | -44.14153 | 2026-09-17 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee4862ff-f83d-3df3-8be6-f62ca9ca023e | -11.48122 | -45.77065 | 2026-09-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da4d47dc-ae34-3256-80c1-3259fe0c3cce | -8.53138 | -44.51593 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c78bffa-296c-39de-b98f-e93eef875796 | -5.1475 | -55.94151 | 2026-09-17 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c2af8de-62e4-381d-b182-ae96fd49bf03 | -12.14722 | -48.25918 | 2026-09-17 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1cf62de-edc1-3dff-8cc6-d926e4c324ea | -6.79887 | -58.78885 | 2026-09-17 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e46b3c1a-eea5-3e6b-931a-211e0eedb1db | -8.55991 | -44.55556 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 57a4caa3-d843-3a08-8b9f-8d834aa88bb5 | -10.78752 | -46.19369 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d96e5ebf-46d7-370c-82ed-5dfb4f60f81b | -5.14674 | -55.94597 | 2026-09-17 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8aaa678-9b42-3fad-bcb2-9d5c1935979e | -4.53935 | -54.93224 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9da633fd-61cf-3e47-871d-1b44c96e2a2f | -11.21364 | -42.82573 | 2026-09-17 04:40:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| a112255c-41c1-3ada-af25-5d2194bb64cc | -10.81667 | -50.836 | 2026-09-17 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a6cf6d5-2569-33a3-918c-eca357d330c5 | -7.04247 | -42.06893 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| b004e2c2-4fc1-3b7b-8eea-d0ef304c9a30 | -7.10395 | -43.11191 | 2026-09-17 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c3589325-9737-3826-9085-c426354fa279 | -10.10421 | -45.62447 | 2026-09-17 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4b931fef-aeda-39b0-8335-d0a2beae24ee | -5.75575 | -51.92351 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ca67b3b-9380-30c4-9fc1-0b134ef62e9d | -4.54845 | -54.92957 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71a8c2ae-aacc-32b2-bf5e-fe4743d0f69a | -9.75769 | -46.1156 | 2026-09-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f3dc5db-3760-3a6a-ab72-79cadb0d4245 | -8.2699 | -42.17034 | 2026-09-17 04:40:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 99d916d6-ed3e-3ddf-8d63-85f4682dd0df | -7.8153 | -44.85273 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd0b0e8d-9f1c-36f2-9052-2332d9aa6220 | -8.56622 | -44.5408 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8f36765-8522-3d57-b383-9cb6e9fddf45 | -7.14217 | -42.16426 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 5a4cf8a9-f057-3357-aa76-fc25d57b60b3 | -5.22538 | -49.30968 | 2026-09-17 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48b92237-1c43-3aca-b237-0c252cb70453 | -11.20461 | -42.81895 | 2026-09-17 04:40:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 920bd158-a2b6-3fc7-a245-1739d7a76846 | -6.36162 | -43.36325 | 2026-09-17 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c95e581b-e6b8-33f1-8913-c2499f54ed77 | -7.12924 | -42.15184 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| bdbcf4a8-a01d-3c44-8fb7-2921e0d4c93b | -6.93182 | -41.70788 | 2026-09-17 04:40:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 760c6e73-49e7-37d9-9672-9ca0cd4bf6fc | -8.09528 | -61.81963 | 2026-09-17 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1a9db011-296b-3373-b19e-9a14c2da3a34 | -3.64362 | -58.56387 | 2026-09-17 04:40:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a246f193-b8e3-32d3-802b-c63465ffc64f | -5.42674 | -43.44151 | 2026-09-17 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 348a1073-e7ca-3af1-a2f7-8f2e539c6433 | -9.11553 | -45.73094 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 67008198-6c16-35d3-a707-518af5a95a6a | -9.87735 | -48.38564 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 19e60bb3-0f25-3457-8b21-d55869dfd2a5 | -7.0242 | -44.62919 | 2026-09-17 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cfe18e0-d8e4-3862-ab39-3811bcb455ea | -6.45333 | -46.52457 | 2026-09-17 04:40:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 593bf70b-3ca3-3c42-ae16-9477c30f7eee | -5.64006 | -44.80817 | 2026-09-17 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 025deba9-b204-3b57-97e7-6b66dd7c118a | -6.49366 | -43.86019 | 2026-09-17 04:40:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32bd26ee-83d2-378a-830b-2d7fe520a762 | -9.40824 | -62.70916 | 2026-09-17 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 848caed7-948b-3008-8b5e-df832abfbdc6 | -7.44406 | -44.57436 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c89f5a0-7cf0-365e-a829-428216294e1f | -6.65438 | -43.64381 | 2026-09-17 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b01f1654-8b29-35e6-9ea6-0eae8923ff9f | -9.76873 | -46.09312 | 2026-09-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aab0b2db-ea63-3618-9d1f-dc653207b24b | -10.18504 | -57.85323 | 2026-09-17 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c092b447-9f58-37d6-9643-769c4695efb5 | -5.76943 | -45.10322 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 2f509835-0f74-3179-9cb6-6541c1c5b53f | -6.1681 | -44.62236 | 2026-09-17 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f256a91-b782-364a-be9b-722c37c7d1ea | -4.50671 | -54.97199 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d95c9772-f03f-3120-bfe5-19bb15950127 | -7.5888 | -46.33701 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 67fe3468-bf23-3a12-9395-7251f375702c | -8.54078 | -44.54029 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 20fbc0b8-00c2-306a-b50a-f0c5e557662e | -7.11186 | -43.10521 | 2026-09-17 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d1e2b2ca-0f91-3bdf-a365-dbe397b38c1d | -9.88649 | -48.39481 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 860fd8b7-46e1-33f6-911a-7b9e186b1ef6 | -7.84609 | -44.81563 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6ce2d734-07ed-30cb-b1d9-d2c2fd8996da | -9.42926 | -49.54403 | 2026-09-17 04:40:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a3bd977-36ad-3820-bdaa-c40419d05f58 | -6.10467 | -57.63971 | 2026-09-17 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e105e97f-8aef-3761-877c-6060e66643db | -8.61079 | -44.49661 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d776dcfa-de56-37d5-999d-a523c5171ae2 | -8.52984 | -44.52708 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c8f62ec4-0aa1-3ac0-9805-c1a497d6f885 | -12.30417 | -47.42673 | 2026-09-17 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2bcd8587-9c25-32d4-bc38-e81b31235c6b | -12.19673 | -43.48118 | 2026-09-17 04:40:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a4a6c7e5-d6eb-3d84-8001-292918eff39a | -7.10975 | -43.10354 | 2026-09-17 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 45a2e2f3-4af0-353c-b928-76e97b958ae1 | -9.87157 | -48.35395 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e37f464f-d94e-39a1-b7f2-c1663ba126f3 | -4.52985 | -55.66285 | 2026-09-17 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cd2ab95-0791-34a3-8122-b50043fcc557 | -9.95176 | -45.30124 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45e97c79-3ab5-304a-bd05-bb4e5ab1d7ab | -9.82599 | -49.14765 | 2026-09-17 04:40:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14018f52-8d23-3d99-a0d7-07194e7a17f3 | -11.23182 | -43.43011 | 2026-09-17 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ab593e14-2f13-3595-9412-4cc6fd997d8b | -10.12191 | -45.57541 | 2026-09-17 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e96361de-62ea-3e27-bf87-9b69602e39d4 | -10.83948 | -46.17366 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc2b0b81-b029-3bd1-9b5c-f0d990321db4 | -8.47461 | -46.89616 | 2026-09-17 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 086427fb-89f3-3a7a-a315-f776fb887bb7 | -7.09945 | -43.11129 | 2026-09-17 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3d66382c-22ea-3447-89a6-a924f869a134 | -8.78267 | -45.87378 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8c761d2f-8274-3514-9cb7-b67555cfebc0 | -5.883 | -44.95738 | 2026-09-17 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13e85d60-7ca7-3428-a552-83d553146611 | -10.01595 | -45.50114 | 2026-09-17 04:40:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73ad0dcf-d0e2-38e8-9a13-846ad6467d74 | -9.59092 | -46.65393 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28f60b9c-bc30-33de-8997-9b89cd8a20f7 | -6.95996 | -42.57138 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| e26e43eb-328c-3f29-9ae6-fb8d0d7b09d7 | -7.58697 | -44.93415 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23da56e3-ccbb-3e01-850a-2e84d8ecbc6a | -9.88192 | -48.37851 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ebfe3f1e-683b-3066-aa08-b4a3daf763b7 | -7.08298 | -41.84271 | 2026-09-17 04:40:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 1b5c451e-dee0-37d5-b927-9e0bbb5fe9de | -6.94753 | -41.70365 | 2026-09-17 04:40:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| eb55e493-7900-3d4c-981b-a0dd4b00a354 | -8.13896 | -44.85851 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1f5b8daf-14c1-3eda-b3c4-d23753b6c4eb | -5.45734 | -44.96062 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9cffba2-e85c-3155-b940-41b14f14e7fb | -8.61736 | -44.45043 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34f95070-b85c-37b5-b395-9a637019e7a2 | -9.59591 | -46.64568 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e06e5cf-6d7f-37ac-a010-8a78e1ecee91 | -9.69764 | -58.18243 | 2026-09-17 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2bc3ea02-2356-33f8-a6d0-5b1e679b39e5 | -8.52976 | -44.51689 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 67dee8cf-2827-3631-8df1-1d225931ebf3 | -10.83381 | -46.15774 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63c15177-c2e6-3662-9c18-0990ac005180 | -6.44036 | -58.14462 | 2026-09-17 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98d0a8f1-d19a-38c2-87b4-6d4eb0835c3e | -11.53252 | -46.87185 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e5e757b4-ed0f-3d89-93d7-9843e3149e68 | -8.87893 | -46.92138 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5933431e-f6b7-3c6e-89ef-cfd1be00e6d5 | -4.88066 | -50.91312 | 2026-09-17 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2d67c368-c736-3837-a53a-a644aa8980aa | -8.61854 | -44.50213 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e8da60f0-baa6-34c5-a58b-71234c7c778e | -9.61974 | -45.35918 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f32ea616-c232-39a2-a667-04b7f6306e03 | -8.38703 | -42.20946 | 2026-09-17 04:40:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 908247c7-20b3-3c6e-b344-304ddd91a713 | -4.37656 | -55.02502 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ebf1326-025d-3ad0-8a2b-614138767a92 | -9.11149 | -45.72374 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 928dc4eb-81a0-3f0a-9cde-afbfe663b1a7 | -5.77644 | -45.10925 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| c2cc96b6-e5d8-3b3e-ab92-71da3671690b | -12.51675 | -45.94719 | 2026-09-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README42.md)
