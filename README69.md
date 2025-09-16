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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66a24494-a40a-3e7a-8cf5-cc92a9a3b57e | -12.68805 | -48.00225 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb0819b2-4d4c-3150-9ff1-57b5588bd224 | -10.72814 | -44.75776 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9d5072d5-162a-3647-8e81-52c2fa5f9268 | -12.05632 | -46.53579 | 2025-09-16 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0cbea978-32a9-3223-920b-e549a02b1507 | -12.73678 | -47.20596 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fbdbe4c2-b078-36d8-b8c8-2b505809272e | -10.71899 | -46.48066 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 76747492-7946-3871-8235-6a7874aae1d3 | -12.673 | -48.0168 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4934d944-ce81-3ed9-95a8-e11f92eeff34 | -11.13371 | -45.33232 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69761660-1de9-3082-8349-efd4544fc5c9 | -8.93615 | -45.79801 | 2025-09-16 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ca9b1e4-63ac-32df-ad74-e176d3c5c609 | -12.78712 | -47.25497 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d803310b-b188-3e22-84f6-9d3ed8f60981 | -15.62234 | -47.36626 | 2025-09-16 04:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6dcd1308-3cad-3b7b-88bc-0769c8323c62 | -12.76523 | -47.96623 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6ba6a971-25ab-352f-84c2-80c01998a752 | -12.82312 | -47.22644 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 873f5b99-7e26-34ad-bbb9-3a286a020c65 | -14.80486 | -51.6655 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 4b7c5e23-5657-3b4e-925d-b30928c3949b | -12.77496 | -47.95892 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c7308fdf-bc07-3075-aa47-c76e73539b7f | -11.42423 | -46.93421 | 2025-09-16 04:51:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5a8e5138-8658-3480-a11f-07fbccba205d | -10.17726 | -46.14329 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f48516d-bb5a-39f1-9b36-e346ff894afd | -11.12792 | -45.33746 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0cdd2300-a11b-3d8d-a9a3-d94dd994066b | -10.56705 | -51.94588 | 2025-09-16 04:51:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f05f2a2f-e8f4-33ae-96e8-8218672f23d3 | -11.02033 | -45.06166 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd8ca16f-595d-37fc-8570-f5530878920e | -13.19166 | -47.30383 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05350d88-68a9-3ccf-8b88-b1a758d66ed0 | -12.66817 | -48.02028 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d665e02-e32b-31b5-a729-f03f6b56327e | -9.79568 | -61.50878 | 2025-09-16 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b1e9e68-1cfb-3906-a9a4-4ee9ee02c7c7 | -11.12568 | -45.35461 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a718b6f9-4ec3-374b-aef3-7de6d87e6770 | -11.97219 | -46.77907 | 2025-09-16 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1987f2d3-3ace-32d8-bab0-84aa9b481780 | -9.09767 | -44.8529 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 05230228-83d5-3faf-9869-423fb3775b4b | -13.03413 | -47.99046 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7373d385-05f8-3888-801d-12024911ba33 | -12.6662 | -47.93604 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce9800c8-ad83-302a-b11c-1d7220dbf0c0 | -12.67675 | -48.02143 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc39f88b-79fb-3906-ae6c-a0a1283cabcb | -12.96295 | -47.96378 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c75d91ab-ac0c-3f79-8b6a-b66e32b466f6 | -9.09457 | -44.83813 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9603f2d9-6e61-3169-888d-e52891e32c52 | -12.62637 | -45.76403 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5fc5a753-1c4d-3e0e-ac5f-89da8f15d925 | -10.43009 | -50.65416 | 2025-09-16 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 286d2965-49f8-3f33-a170-fc4d598f7e09 | -15.09284 | -52.48188 | 2025-09-16 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d91c6517-2df7-3e4e-8439-42934e9b4767 | -12.06239 | -46.56189 | 2025-09-16 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c37b077-0745-3f87-a5ad-d13afa9e7688 | -8.6724 | -46.38417 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e8691b5-df77-3339-8b91-d6d541732574 | -12.80191 | -47.24744 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d701c9a6-af25-3efc-a84f-657a7bac861b | -12.85311 | -47.14046 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ad141510-bf01-3191-a8e4-476094aef6c4 | -14.81257 | -51.66246 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f6cc8d78-2255-38a6-8516-2780ebd88081 | -11.24078 | -49.95323 | 2025-09-16 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4de33516-33db-3306-af86-f424862b0dce | -10.71353 | -44.73967 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| fc74df1f-f295-3c1c-9faa-4cd4da1af492 | -12.6229 | -45.75288 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 62545fa5-d5c0-3567-8f25-307ab4107d45 | -11.11564 | -45.3532 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb784510-9472-39a1-b546-a7d32ff8f780 | -8.43352 | -47.2163 | 2025-09-16 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08f3b783-949f-38e6-8d99-cb941f0b12eb | -9.48686 | -55.96604 | 2025-09-16 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0f502ff-4327-3759-b52a-3246b47391bc | -13.06019 | -50.0817 | 2025-09-16 04:51:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 302608dc-6934-34e8-94e7-20b986e50848 | -11.45733 | -46.92825 | 2025-09-16 04:51:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 233460cc-98ca-340d-a2f4-bef79ea7b63b | -10.71845 | -46.48469 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f8192930-0a10-3254-b82d-26afc29edb2f | -13.78446 | -54.95411 | 2025-09-16 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 68aabe11-01ac-35bc-bb33-21be7f60eb09 | -13.77709 | -54.95999 | 2025-09-16 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b248026-5c30-30c2-b928-1fc3eda249b9 | -12.66182 | -47.72594 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfd9b160-bf32-3a0a-a1d1-4a3e17316d22 | -8.76021 | -48.80143 | 2025-09-16 04:51:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32b8eee2-c650-3e65-b3bc-45421e048936 | -14.81224 | -48.12788 | 2025-09-16 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56bae63c-75fb-3252-a735-4b80b84202e7 | -8.03333 | -49.83005 | 2025-09-16 04:51:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90baa8c1-71aa-3bb3-b19b-d461bd4035aa | -9.14711 | -46.94479 | 2025-09-16 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 60228884-de15-304f-92b9-1ceed14ebe0f | -15.08879 | -52.48537 | 2025-09-16 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 75cafe74-b7ba-38f6-8955-1edabf1eb34c | -8.03694 | -49.83059 | 2025-09-16 04:51:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6d9b2187-0841-3ce7-b9ff-68dd969560a4 | -14.35596 | -52.91961 | 2025-09-16 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04200b6e-6512-3568-a0b9-0347a2d696b9 | -10.72222 | -44.76268 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 38b5abae-5726-3ef5-a079-cb92f769544e | -9.10154 | -44.85426 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 007780eb-5c4a-3c09-a4e2-ee3da8ff969d | -12.17795 | -44.09875 | 2025-09-16 04:51:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f69c4108-2bbf-3edd-8065-7d79cc221245 | -11.70776 | -46.8756 | 2025-09-16 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| edd8548f-90ed-3e49-bd7e-9290a72fba3e | -10.21259 | -54.30439 | 2025-09-16 04:51:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0400edc-731e-3111-8125-e5b0178a0495 | -9.47417 | -54.43961 | 2025-09-16 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19c58bc9-7c37-3f47-b277-2757c8e9b0a5 | -11.1322 | -45.34384 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5c79b98c-72d8-388e-9d21-dd864553f81f | -12.10631 | -44.8301 | 2025-09-16 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9c254e8-1fbf-3059-84d7-1f3238b6ce64 | -11.29963 | -50.85514 | 2025-09-16 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad76d8ce-eef9-3f2e-8a4f-64df9efa27b6 | -8.93161 | -45.51318 | 2025-09-16 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 884dd298-e111-3030-a969-ed1b5e4fef7c | -8.99065 | -45.76077 | 2025-09-16 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f96c00e-49bb-3785-b27f-22cab66b617d | -7.7122 | -55.45013 | 2025-09-16 04:51:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93b5eafa-ae77-32b7-9a9a-fdb12f997ca1 | -10.73804 | -44.76308 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ae77d78-a54e-32cc-a65e-aec3a296f2ef | -9.08883 | -44.8051 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bf9e0a9-5418-399c-8e94-665240a82e30 | -12.6673 | -47.92767 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 56566ebc-5d56-380d-99fe-f651417ae6bf | -11.07657 | -49.75272 | 2025-09-16 04:51:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 660b4448-4311-37c7-ab8e-7daad43a87d1 | -8.75949 | -48.80624 | 2025-09-16 04:51:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b9a821e-5ad8-3e65-b376-b0558eeed336 | -11.64519 | -46.59989 | 2025-09-16 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f94a11b6-093d-33e6-baf6-9f376843a215 | -14.65835 | -52.06934 | 2025-09-16 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e9727e9-438d-3905-911f-cc490625c7bb | -8.92603 | -54.44682 | 2025-09-16 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1266083c-c035-3a9e-94a5-07224588c5a2 | -12.6256 | -45.76985 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a982274-38cb-3e0c-b0f9-26c296659038 | -11.44204 | -47.30311 | 2025-09-16 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32d49c7c-c5f1-344f-bb8f-4ae0b372efce | -10.56649 | -51.94955 | 2025-09-16 04:51:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad327b2f-17fe-319b-bc47-65a29bb6a047 | -10.72186 | -46.49451 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 6bf5dcec-05c6-335d-9251-ef5b4829422a | -12.62483 | -45.77573 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 060a0020-bf55-3940-bd54-8ca08e39d5b2 | -11.05157 | -48.27917 | 2025-09-16 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0020de5-7178-336f-b373-21abe6e5e1bc | -8.44038 | -55.62835 | 2025-09-16 04:51:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03c0ff3f-680b-3825-9ce0-2b5eb7f9a74c | -14.47525 | -46.36218 | 2025-09-16 04:51:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f7d0b9a-7493-3b6e-98cf-22d9d5e4ef91 | -9.09377 | -44.84395 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 294d64d0-385f-30b2-87f8-3afb1f5c11c2 | -13.21187 | -47.29026 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 41d4b3d9-729d-31e7-a739-df7343a495b8 | -8.09574 | -50.15788 | 2025-09-16 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2543e90c-2e68-31c8-bd5d-95cb0fda40cb | -8.87999 | -46.19882 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adc38767-4cfe-377e-b748-55ae4b39f8a6 | -14.64474 | -42.71503 | 2025-09-16 04:51:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d7db476c-48e8-3ac1-8f0b-b24b2f569e3b | -8.64666 | -62.66962 | 2025-09-16 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f22df280-3523-3a33-98c3-f541c15866e8 | -12.74194 | -47.20195 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f288801d-225a-34a7-b4af-da9cceba736d | -8.90529 | -46.15247 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 626def16-678e-3b9a-8260-a4b07ef16da8 | -8.61991 | -45.71957 | 2025-09-16 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef045e6f-9059-3642-8b05-c8dbaa6e25fe | -14.84211 | -51.62755 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f6928576-ebdf-3fc4-99cb-4390c5f04883 | -15.09403 | -52.47388 | 2025-09-16 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5df27cf-9a28-393a-b009-24ad013fb124 | -14.65924 | -52.07291 | 2025-09-16 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 248972f8-8b0e-32d3-a06c-b1ddb41b822b | -12.10183 | -44.8229 | 2025-09-16 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd7cb94c-a472-36ec-ad3d-71d7afdf6924 | -12.66243 | -47.93129 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 647f56f5-b216-3bc6-a03d-dc79065bef6e | -12.77439 | -47.96321 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README70.md)
