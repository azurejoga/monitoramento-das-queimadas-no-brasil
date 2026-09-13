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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0126fb2c-97ed-3e0e-a664-85ead3525178 | -12.5102 | -45.2554 | 2026-09-13 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 217b9ee2-e20c-3b6b-b0cf-d3d315d9a0b5 | -8.9272 | -45.4321 | 2026-09-13 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 892a3311-7d51-3af7-ab8b-9c4de7c51a85 | -14.0823 | -41.4134 | 2026-09-13 13:00:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 111.3 |
| af52e480-5e40-3f11-9989-be8807920998 | -7.0166 | -44.6184 | 2026-09-13 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 331c9f67-b7b9-3554-85ef-f80c56831cd7 | -6.2831 | -59.9394 | 2026-09-13 13:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 8ae335ae-b416-3222-b692-e1aeedf18f2c | -2.6784 | -57.5504 | 2026-09-13 13:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| bf2623d2-43ee-395e-ab96-d6bf7072f3a4 | -10.6829 | -54.1475 | 2026-09-13 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 289.0 |
| 491ab206-7969-3bd8-9a1f-5287c7cbbe5d | -14.0818 | -41.4383 | 2026-09-13 13:10:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 222.2 |
| a6f26864-b4d6-353c-b21c-e2f933e56bf4 | -10.7018 | -54.1458 | 2026-09-13 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 187.9 |
| 05b7efc8-95ad-3717-8e27-1437c886dffc | -10.7535 | -46.2347 | 2026-09-13 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.8 |
| e579fb63-fc7a-307a-861f-1a3ef2635805 | -8.4292 | -46.0271 | 2026-09-13 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| d3946d2c-a3b6-3d12-aeff-2c82eca9aec0 | -8.6001 | -44.4609 | 2026-09-13 13:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 298c76fd-b84e-337f-9b5d-f4a961343c79 | -2.6785 | -57.531 | 2026-09-13 13:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 132.2 |
| d1365ae8-bd3e-3cb7-9b62-e5f91ece6635 | -11.3532 | -46.8324 | 2026-09-13 13:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| fe51909f-bfa3-3225-b197-2227145724b5 | -6.8755 | -47.4313 | 2026-09-13 13:10:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 2e42e539-124a-3b13-93c8-0fb7e4d3bac0 | -11.8189 | -46.386 | 2026-09-13 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 6f33e489-2443-38d2-b386-aecdeecd5df2 | -2.6785 | -57.5115 | 2026-09-13 13:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 5ba88e55-1efd-3340-94cc-e6a1e5432b73 | -9.3948 | -50.1334 | 2026-09-13 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 44328cd7-f211-35ca-956d-aeb1590af791 | -13.5967 | -47.8803 | 2026-09-13 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 52d50ba8-fa4b-3e38-a5fa-efd211bec3b2 | -12.5102 | -45.2554 | 2026-09-13 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| ab724e79-2dfb-3001-83b5-3b13c4e0fdb7 | -2.6784 | -57.5504 | 2026-09-13 13:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| d3a4c6af-e03d-3844-bab5-60fa857122bc | -11.3025 | -44.184 | 2026-09-13 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| e693979c-d99e-3c39-9f88-34d7e97dd03e | -6.6021 | -58.849 | 2026-09-13 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| b2cc90bc-8b14-370f-8737-9c66dcebd8a3 | -6.8567 | -47.4328 | 2026-09-13 13:10:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 6c62f259-a309-3498-9e51-0fedb8c878ef | -10.7015 | -54.1663 | 2026-09-13 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 214.7 |
| f92d9752-6c7e-3c2d-ba3e-209fb0cb013a | -7.0352 | -44.6396 | 2026-09-13 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 34f5f3aa-c8f9-3b57-bf1a-707e93693513 | -13.616 | -47.8774 | 2026-09-13 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 1baa86f6-bdf9-3b8a-924c-f1cae01b024d | -10.6827 | -54.1679 | 2026-09-13 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 367.8 |
| a3bbff65-7267-3437-9ac0-ecf2e84fac59 | -14.0823 | -41.4134 | 2026-09-13 13:10:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 178.4 |
| 69939633-6678-3b77-9684-adac4c25a79e | -9.5129 | -45.4568 | 2026-09-13 13:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 2d6c1ce9-6974-36db-8635-124aa26e312e | -13.4507 | -48.48 | 2026-09-13 13:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 41709981-b1e5-3310-adbe-3bbb450eb1d9 | -13.3055 | -51.3235 | 2026-09-13 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 23164fde-f603-361e-95b2-cfd601f60285 | -10.7532 | -46.2573 | 2026-09-13 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 186.4 |
| 931e44b2-57ee-365c-be5d-f20b4dba16eb | -2.6602 | -57.5313 | 2026-09-13 13:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 2c43d6dd-f82a-3f8c-85a1-b293ccd30c50 | -8.6005 | -44.4378 | 2026-09-13 13:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 882e4297-b877-3d77-9e5c-9dcb12c51e95 | -3.3293 | -42.2893 | 2026-09-13 13:10:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| b35cbd45-4c6f-38b8-b26e-c74142de905e | -10.78 | -46.28 | 2026-09-13 13:15:00 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3cc709e6-f31c-312a-a534-c9ebfc4b94de | -10.75 | -46.27 | 2026-09-13 13:15:00 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 11c02c2f-3b40-32cb-8b77-15dbe00ff489 | -13.4507 | -48.48 | 2026-09-13 13:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 64.0 |
| ebbb7730-17ba-3b24-ba2e-319903c76368 | -14.0823 | -41.4134 | 2026-09-13 13:20:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 158.8 |
| 40902ee6-d96f-39ac-a993-fac5af7eca5f | -6.6758 | -58.8654 | 2026-09-13 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 14327b26-5844-381f-87ce-b1966cea3eef | -6.8755 | -47.4313 | 2026-09-13 13:20:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 3a68edd4-382d-3e5d-bec1-f7ac5b3df875 | -7.0352 | -44.6396 | 2026-09-13 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 42f038ac-6b1c-3fbc-83d0-6852cb52b0f3 | -11.3025 | -44.184 | 2026-09-13 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| b2b2d7f4-525c-379b-8dc4-2d7480c4463c | -2.6784 | -57.5504 | 2026-09-13 13:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 111.4 |
| c1d0b053-4ae5-315c-959f-55a73df4799b | -11.2833 | -44.1868 | 2026-09-13 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 360cccb1-f1ed-3654-b4e1-fc64476db9ef | -5.1255 | -55.955 | 2026-09-13 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| b56d1207-9e12-3ce1-b496-0664a441d0a6 | -8.6001 | -44.4609 | 2026-09-13 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 9057e870-d3fb-3d42-8ec6-4580e16f268d | -7.3687 | -46.7735 | 2026-09-13 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 6b509b91-85ee-36bb-87af-977a59b00188 | -10.6829 | -54.1475 | 2026-09-13 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 292.9 |
| 40cc16f2-026c-3640-bc93-de3eb9eb8ab8 | -10.7015 | -54.1663 | 2026-09-13 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 155.1 |
| 7714b490-8528-3fb7-97c3-d50908df0dbd | -11.5793 | -47.0043 | 2026-09-13 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 3c05b36f-a73b-3e4b-bcab-fb143c50e31c | -11.794 | -47.8673 | 2026-09-13 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 688630fe-bf79-308c-817b-1f3a76f2ca3e | -6.6757 | -58.8847 | 2026-09-13 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| f5d68889-3d96-3de2-8b69-072833594007 | -6.6021 | -58.849 | 2026-09-13 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 7191c6bc-9242-31d5-9de6-a1ae43cc774a | -10.7018 | -54.1458 | 2026-09-13 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 142.4 |
| 76b19d42-203c-3e97-875f-1750b3b2d5e7 | -14.0818 | -41.4383 | 2026-09-13 13:20:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 222.9 |
| cf9c9946-a449-3d75-986f-7bf50762c18c | -7.5394 | -44.9133 | 2026-09-13 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 7e976d6b-a546-37e5-a946-cf9ed8fdfb41 | -11.5796 | -46.9819 | 2026-09-13 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 4a4992a3-f800-314b-9416-a4fa36d76b5a | -6.8567 | -47.4328 | 2026-09-13 13:20:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 63d4780a-7383-3bf6-a668-0a887b1c160e | -11.3021 | -44.2074 | 2026-09-13 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 38b1ecc5-ce71-373e-a0ae-9a188e728562 | -5.8505 | -52.1084 | 2026-09-13 13:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 71e9e282-7747-3aca-b299-7824e435f58f | -8.4292 | -46.0271 | 2026-09-13 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 9cb2ec0f-1077-39a3-977c-6d7ded088b4e | -2.6785 | -57.5115 | 2026-09-13 13:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| dceab9c5-4067-3c5b-8246-c1917edee525 | -13.3055 | -51.3235 | 2026-09-13 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 21e1290f-375d-39a4-bc40-51d24dd34c3f | -10.7532 | -46.2573 | 2026-09-13 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| b8b130a7-e9f3-300a-8224-25616fbe8e11 | -8.6005 | -44.4378 | 2026-09-13 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 4132d8b3-f561-330f-90b2-1b78ef32ffea | -11.838 | -46.3834 | 2026-09-13 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| bd96ae41-b652-3600-bc66-78e6c6ce345d | -8.832 | -46.9476 | 2026-09-13 13:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| c37445b6-2fbc-30a3-915a-beb79a516fc8 | -7.0166 | -44.6184 | 2026-09-13 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| c79a3ecb-74c4-31b3-b4d8-5e4427278b48 | -6.6767 | -58.7105 | 2026-09-13 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 6a2aa499-e26a-3399-96cb-0458c02ce003 | -11.8189 | -46.386 | 2026-09-13 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 01004cd7-d001-3171-804e-f882f7042d02 | -3.3293 | -42.2893 | 2026-09-13 13:20:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 023ef5e9-b2fa-3bab-98d8-dd76e96ee113 | -9.5129 | -45.4568 | 2026-09-13 13:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 565857e7-a601-3e34-a7a9-328b7fed8368 | -2.6785 | -57.531 | 2026-09-13 13:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 154.4 |
| 6685044e-953b-366c-8068-45e25e4961b5 | -10.7018 | -54.1458 | 2026-09-13 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 172.9 |
| c82b914d-973b-3adb-8b42-1276042c083e | -3.3809 | -50.7623 | 2026-09-13 13:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 292015a9-6172-36c4-acd6-85e8e6c1c7b6 | -11.3536 | -46.8099 | 2026-09-13 13:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 991a532a-3dac-35db-81a7-0a6c5c13f010 | -6.2832 | -59.9202 | 2026-09-13 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| f2ba524d-67d8-3a40-9e99-c5a13586cea8 | -11.3021 | -44.2074 | 2026-09-13 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 129.1 |
| ee5971a3-8de4-363f-92b4-06bb7b2709d9 | -13.4503 | -48.5022 | 2026-09-13 13:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| ebe446e4-a856-3494-81e1-c85cb7349c09 | -5.1254 | -55.9748 | 2026-09-13 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 4802fb8b-9eec-32da-b20d-f8af283a35be | -11.0433 | -47.1633 | 2026-09-13 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 104b62c8-f440-34be-8b0d-5714d93ca9a6 | -6.8755 | -47.4313 | 2026-09-13 13:30:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 8eebbc9b-7995-3cd1-b258-3b8c35329876 | -5.1439 | -55.9543 | 2026-09-13 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 79f1bdcc-e594-31d2-92b8-9e7d5ec29b28 | -11.2833 | -44.1868 | 2026-09-13 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 37ba6f2a-2735-3d70-874a-795b5c1edeaa | -7.2072 | -46.0963 | 2026-09-13 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| c58f7828-cd6e-3da8-939e-17d7ce75af00 | -10.6417 | -46.0906 | 2026-09-13 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| c0342164-70fe-3e2d-91ab-6d0d44cafa4c | -8.4292 | -46.0271 | 2026-09-13 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| e67d1a7b-c431-3f1d-bf04-aef28d1959ec | -8.8132 | -46.9495 | 2026-09-13 13:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 74baf3c3-b98a-3afd-8049-f9a3c5c25e45 | -9.5129 | -45.4568 | 2026-09-13 13:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 618d3dae-ff9d-3cc0-8234-19a40ccbc2ce | -10.6829 | -54.1475 | 2026-09-13 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 321.8 |
| 87f96d66-dfcd-3851-bddb-b13e5be2ed3d | -3.3293 | -42.2893 | 2026-09-13 13:30:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| b062424c-9c34-3dd0-9e4c-8ffb7a826507 | -11.372 | -46.8524 | 2026-09-13 13:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 225.3 |
| f0a75eb9-451b-344d-9583-511f7144df9b | -11.0623 | -47.1609 | 2026-09-13 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 178.5 |
| a7373c52-cb15-3950-8005-709ff83130f4 | -6.6757 | -58.8847 | 2026-09-13 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 6f5aea53-cb36-3b69-bf07-ffabb3be8220 | -11.3723 | -46.8299 | 2026-09-13 13:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 179.2 |
| c562ab72-bb45-3ccd-ba0d-9476db9ae39f | -2.6785 | -57.531 | 2026-09-13 13:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 199d2e3f-4f27-3cb4-88cf-15f7ff965714 | -9.8992 | -47.5874 | 2026-09-13 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 018a588e-85e5-3281-8039-fe7d5b29b890 | -8.6005 | -44.4378 | 2026-09-13 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 130.1 |


[Clique aqui para ver as próximas entradas](README62.md)
