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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3de2f09d-74ed-3d66-882e-90d4cb9b855b | -10.97217 | -44.4506 | 2025-05-09 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 2aba983c-f33c-3845-a43f-7368d280f405 | -14.64755 | -45.13362 | 2025-05-09 00:52:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 88379779-79ff-3e0c-a46d-2ced4eb7726f | -11.40956 | -52.95019 | 2025-05-09 00:52:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| ebb604d7-6a96-35d7-b389-746cad26b32d | -13.80828 | -52.2436 | 2025-05-09 00:52:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9f0a9411-a52b-359f-a0c6-2f49b49aefee | -17.52622 | -52.12649 | 2025-05-09 00:52:00 | TERRA_M-M | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 160df1e0-9f5c-3f30-8673-e745cdc2b66d | -18.26538 | -53.00958 | 2025-05-09 00:52:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 985de3fb-101e-3e61-94e3-82e623a090a5 | -13.38103 | -54.2542 | 2025-05-09 00:52:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| e0cfb868-edd6-3131-886b-6b56c7cb82ff | -11.56437 | -47.62037 | 2025-05-09 00:52:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 41f1e8ed-87ce-3bdc-992a-21456e90bc31 | -13.24587 | -48.41006 | 2025-05-09 00:52:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9603b496-c93a-3cd4-87a4-34f17c2f9e18 | -11.39045 | -52.95273 | 2025-05-09 00:52:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| fcc4dbb2-ebae-38a2-be8d-a272394270d1 | -13.03842 | -53.72365 | 2025-05-09 00:52:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| b3da5028-c8b6-3e5d-8379-f0d81e4e0f7a | -11.3841 | -52.93848 | 2025-05-09 00:52:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 428e2057-5d32-3263-ad53-4228ee539ca0 | -14.64983 | -45.1479 | 2025-05-09 00:52:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1986a62f-8d4f-311b-8fb0-24ce6217ab10 | -10.67102 | -44.39409 | 2025-05-09 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 23e1c65f-7c75-3adb-805b-4850c2786b5d | -10.96911 | -44.43211 | 2025-05-09 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 204e57c4-f11e-3f56-9839-284d63e780e9 | -12.17577 | -54.23358 | 2025-05-09 00:52:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 2cee24b0-21df-3ffb-9c6a-9293bc58dceb | -14.63665 | -45.13551 | 2025-05-09 00:52:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 07a25cf8-99fd-37a8-bd28-b26f60aa8810 | -11.38909 | -52.94217 | 2025-05-09 00:52:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 3eeeac62-b6d7-3cd9-9aed-7a2cc831a300 | -14.20671 | -45.47013 | 2025-05-09 00:52:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 8b1a61f9-780e-37d4-a89c-dbae9a2a647e | -12.32966 | -50.33118 | 2025-05-09 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 338d13b7-d2c1-3fff-b25d-548e131b5bd6 | -14.21743 | -45.46833 | 2025-05-09 00:52:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 93fc624d-6d49-3d88-ae79-eeaa542e18e0 | -11.56674 | -47.61368 | 2025-05-09 00:52:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 61beb510-2b68-33b7-9099-6c27a5b614c4 | -11.4 | -52.95144 | 2025-05-09 00:52:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 1835f9b8-ac16-35bd-a5f5-02f8b5fbde70 | -10.97926 | -44.43619 | 2025-05-09 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d86e7741-d1ee-3baf-852e-715687ff4281 | -13.38277 | -54.26801 | 2025-05-09 00:52:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 3877b4da-5d4a-3865-9265-a9d8efc264c0 | -13.04735 | -53.72942 | 2025-05-09 00:52:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 37.9 |
| da727d9c-76ee-30ec-bba2-ab1218112a93 | -12.36034 | -52.48789 | 2025-05-09 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b4512cfd-7886-38d9-b076-479f66352d85 | -14.63436 | -45.1212 | 2025-05-09 00:52:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 63f18c7c-8e00-394f-8dc9-8293612af93d | -6.68808 | -42.12637 | 2025-05-09 00:54:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 41.8 |
| b84dffbc-238e-3011-af5c-2f06b8b6db62 | -8.0803 | -43.11115 | 2025-05-09 00:54:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| d879c379-5b3f-34da-8c24-6a3f23d83c18 | -7.62176 | -46.48067 | 2025-05-09 00:54:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| efd80e86-bcb8-3611-b504-192b79054f99 | -6.70135 | -42.15154 | 2025-05-09 00:54:00 | TERRA_M-M | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| 782a6e53-108b-3408-9f94-47b893f58c19 | -8.08472 | -43.13763 | 2025-05-09 00:54:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| 6e158692-427b-34d3-ba7f-c11135bd0596 | -8.07873 | -43.11823 | 2025-05-09 00:54:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 139.9 |
| 37bd6389-d31d-3189-a666-20c1af4473c5 | -6.69331 | -42.16003 | 2025-05-09 00:54:00 | TERRA_M-M | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 43.3 |
| 1bfea823-e3ab-30e0-9a26-a43f84ff7fd8 | -8.08293 | -43.14462 | 2025-05-09 00:54:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.9 |
| 7df79938-63a8-37ef-9cef-6fa1f206fa7d | -7.07187 | -44.39219 | 2025-05-09 00:54:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ea20bdbd-d8ad-3b92-b455-465eb39da771 | -5.16184 | -45.1097 | 2025-05-09 00:54:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| bf97d64d-14ac-3fd5-998d-174a76e2367a | -6.69591 | -42.11787 | 2025-05-09 00:54:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 35.2 |
| 768f3157-8366-3509-996c-6c178847aead | -8.0889 | -43.1196 | 2025-05-09 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| e7a7aa5f-bfb3-3f52-acf3-12f04da324e4 | -8.07 | -43.1216 | 2025-05-09 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| 352c3f1a-5694-3dfb-af75-4b411a03ab10 | -8.0889 | -43.1196 | 2025-05-09 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| a76580a3-d3e0-3e69-8b23-15463d112646 | -8.07 | -43.1216 | 2025-05-09 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 6fc79107-f5dc-3aa3-96c1-a1e22c4e1097 | -8.07 | -43.1216 | 2025-05-09 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 0e11fa4e-efb3-3cc0-ac22-aec2de7f9583 | -8.0889 | -43.1196 | 2025-05-09 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| ac8c0787-8b50-3b77-b79c-19d7bfba605c | -8.0889 | -43.1196 | 2025-05-09 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.5 |
| 496299c1-b285-3fbb-8eb6-cdc792ac523d | -8.07 | -43.1216 | 2025-05-09 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.3 |
| 23da1971-541a-3f6e-9bba-7d8ecb1a7fde | -19.166 | -47.8122 | 2025-05-09 01:40:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 45.3 |
| e5a90fbb-fcc0-3f5f-88aa-0692fdb6bd78 | -8.0889 | -43.1196 | 2025-05-09 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| 9fe47f76-5fd5-325e-b7fd-c468310c1550 | -8.07 | -43.1216 | 2025-05-09 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| d2fa9821-d888-3775-997f-8c5889b3a178 | -8.0889 | -43.1196 | 2025-05-09 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.0 |
| edf55342-e436-34ba-9eeb-f78421da1cb5 | -8.07 | -43.1216 | 2025-05-09 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| 5a67efdc-4a58-363f-a073-8c70e615b47a | -8.07 | -43.1216 | 2025-05-09 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| 163a7c20-29dc-3439-9fd3-289c078b1177 | -8.0889 | -43.1196 | 2025-05-09 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| c0d04728-02cf-3058-97e8-ff313c82af4f | -8.07 | -43.1216 | 2025-05-09 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 6302dbd6-7b3e-3bb3-ad25-2edefcdf0ac8 | -8.07 | -43.1216 | 2025-05-09 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| c3cc31d7-b216-3a04-ae13-858ec7d6c248 | -8.0889 | -43.1196 | 2025-05-09 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.7 |
| 2ae881ee-00b1-3f83-a237-4fb20318f864 | -8.0889 | -43.1196 | 2025-05-09 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.2 |
| 57e2bf20-81a0-3834-ae5f-b1c1a388f813 | -8.07 | -43.1216 | 2025-05-09 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| ebb206b1-ca27-309e-9e85-cde3d0023cd4 | -8.07 | -43.1216 | 2025-05-09 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| d6d50b18-fa43-3e17-a69d-99fdbdad06fd | -8.0889 | -43.1196 | 2025-05-09 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.8 |
| 6fbce725-0107-3954-8976-bbc9341dd164 | -7.2303 | -35.59523 | 2025-05-09 02:58:00 | NOAA-21 | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3e13d74f-5c22-3df6-9871-8b8f0cc06e27 | -8.0889 | -43.1196 | 2025-05-09 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 8e14229e-9c73-3cce-b851-a09f94bda659 | -8.07 | -43.1216 | 2025-05-09 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.0 |
| bbdf7286-0f22-3d5d-ade6-acaf481a3894 | -8.07 | -43.1216 | 2025-05-09 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 5ece7330-1cc4-32ba-ba24-8c26ea0d5487 | -8.07 | -43.1216 | 2025-05-09 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| f2278bac-84ca-3e79-a92c-01b682518ce1 | -8.0889 | -43.1196 | 2025-05-09 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| d3c3e017-28c2-3300-bffb-81019115d507 | -6.69891 | -42.13285 | 2025-05-09 03:23:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| a212651b-0a5c-3984-b2e5-eefc87ea1094 | -6.97019 | -42.78669 | 2025-05-09 03:23:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 33571da6-547f-3111-82d9-4835fa387fa0 | -7.07089 | -44.39202 | 2025-05-09 03:23:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6f74f95f-a6e3-3c3b-8515-c6cfcb221cca | -6.698 | -42.13779 | 2025-05-09 03:23:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| ce8ca7a7-7b21-3d31-aaaa-36187a32e16e | -8.01038 | -41.60491 | 2025-05-09 03:23:00 | NPP-375D | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 686341f4-dfc2-3e34-b037-6e8cf5f33488 | -6.97121 | -42.78218 | 2025-05-09 03:23:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fd5fe524-e875-30b6-9202-15845cc08665 | -6.97117 | -42.78147 | 2025-05-09 03:23:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d479799a-29b3-3847-a343-574132b27712 | -6.97026 | -42.7874 | 2025-05-09 03:23:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7488ac4c-9540-3814-8523-9b79d8cfcf08 | -8.05905 | -36.15065 | 2025-05-09 03:23:00 | NPP-375D | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 67129490-0a9c-3dab-9b24-ccebd07eaa68 | -7.21576 | -43.12059 | 2025-05-09 03:23:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e73c226c-44bf-30c9-abce-024875ef12bb | -6.96371 | -42.78555 | 2025-05-09 03:23:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6ca323f4-b851-35b1-bb4b-29606f640807 | -8.01118 | -41.60058 | 2025-05-09 03:23:00 | NPP-375D | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 76547913-b3b0-3b42-9f51-89418abd4b7d | -6.70422 | -42.1391 | 2025-05-09 03:23:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 070cfaae-5c12-3919-9e00-70e10d5f7b0a | -6.96378 | -42.78625 | 2025-05-09 03:23:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9ba5e7e0-b5f9-37f1-943d-52d300478d05 | -10.5543 | -42.42509 | 2025-05-09 03:25:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 22b80109-8386-3d13-aa99-5ae53c5d8d1b | -14.64135 | -45.12918 | 2025-05-09 03:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| afa6204a-fc46-3322-adc3-d186fadd3ced | -10.96765 | -44.43757 | 2025-05-09 03:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1fe97ebd-2822-3309-b6d9-ec78b9555b1d | -14.6449 | -45.13731 | 2025-05-09 03:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75b813ee-01c4-36d8-abe2-446c10f5a380 | -8.06873 | -43.12438 | 2025-05-09 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a2fab544-5f10-3252-88fc-cbc0880d7ae2 | -14.63606 | -45.12199 | 2025-05-09 03:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60cd5bb1-0fd9-31a4-a512-2b0a47e1a978 | -8.08166 | -43.12702 | 2025-05-09 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| ff492be4-fa26-32bc-bf56-04a9452a015e | -14.19977 | -45.46477 | 2025-05-09 03:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2e67d61-eafc-3cf6-b9b0-a65dbd88c5ae | -14.19845 | -45.47089 | 2025-05-09 03:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbb41b54-8954-3d24-a5e2-fbde76b1a9fc | -14.21849 | -45.47542 | 2025-05-09 03:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0857cb0b-b0b9-32e4-8c44-a69cec880f66 | -14.22185 | -45.46891 | 2025-05-09 03:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a81042d-9c36-3ef7-9f3b-c6d6cc3fe35a | -14.64366 | -45.14297 | 2025-05-09 03:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 41a360d9-2be4-3985-8e59-884737af13f5 | -14.20183 | -45.46439 | 2025-05-09 03:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 563f34ae-9f76-3169-928a-cd1dfb8fbe26 | -10.9755 | -44.43314 | 2025-05-09 03:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e8286b8-4333-31e7-be1e-4ccc60111399 | -8.07404 | -43.12601 | 2025-05-09 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.7 |
| e90dd4dd-ce2f-3075-a0c1-4e55d1f888df | -14.20047 | -45.4705 | 2025-05-09 03:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3bfd195a-b657-351c-89f8-af9387955331 | -12.31657 | -44.51136 | 2025-05-09 03:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00cf32f2-82c4-33cf-8b68-7af26fcc07e3 | -14.20645 | -45.46626 | 2025-05-09 03:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0be55882-d676-3b35-a028-88a33a1106aa | -10.9743 | -44.43903 | 2025-05-09 03:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README3.md)
